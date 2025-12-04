# ==========================================
# NBA MODEL BRAIN V3.5 - MODEL CORE (V1.5)
# Spread, Totals, Edges, Confidence + Injuries
# ==========================================

from typing import Dict, Any

try:
    from config import TEAM_CONFIG, MODEL_SETTINGS, TEAM_NAME_MAP
except ImportError:
    TEAM_CONFIG = {}
    MODEL_SETTINGS = {}
    TEAM_NAME_MAP = {}

from roster_api import get_team_roster, get_team_injury_summary


# -----------------------------
# Defaults
# -----------------------------
DEFAULT_MODEL_SETTINGS = {
    "min_edge_to_bet": 1.5,
    "confidence_thresholds": {"S": 4.0, "A": 3.0, "B": 2.0, "C": 1.0},
    "injury_penalty_per_starter_out": 0.15,
    "injury_penalty_per_other_out": 0.05,
    "max_injury_penalty": 0.50,
    "no_bet_if_starters_out": 3,
}


def get_setting(key: str, default_key: str = None):
    if MODEL_SETTINGS and key in MODEL_SETTINGS:
        return MODEL_SETTINGS[key]
    if default_key and default_key in DEFAULT_MODEL_SETTINGS:
        return DEFAULT_MODEL_SETTINGS[default_key]
    return DEFAULT_MODEL_SETTINGS.get(key)


def get_conf_thresholds() -> Dict[str, float]:
    if MODEL_SETTINGS and isinstance(MODEL_SETTINGS.get("confidence_thresholds"), dict):
        c = MODEL_SETTINGS["confidence_thresholds"]
        return {
            "S": float(c.get("S", 4.0)),
            "A": float(c.get("A", 3.0)),
            "B": float(c.get("B", 2.0)),
            "C": float(c.get("C", 1.0)),
        }
    return DEFAULT_MODEL_SETTINGS["confidence_thresholds"]


# -----------------------------
# Team helpers
# -----------------------------
def normalize_team_name(team: str) -> str:
    return TEAM_NAME_MAP.get(team, team) if TEAM_NAME_MAP else team


def get_team_config(team: str) -> Dict[str, Any]:
    key = normalize_team_name(team)
    cfg = TEAM_CONFIG.get(key)
    if not cfg:
        raise ValueError(f"Unknown team config: {team} (normalized: {key})")
    return cfg


# -----------------------------
# Projections
# -----------------------------
def project_spread(home_team: str, away_team: str) -> float:
    home = get_team_config(home_team)
    away = get_team_config(away_team)
    diff = float(home.get("strength", 0)) - float(away.get("strength", 0))
    home_edge = float(home.get("home_edge", 0))
    return -(diff + home_edge)


def project_total(home_team: str, away_team: str) -> float:
    home = get_team_config(home_team)
    away = get_team_config(away_team)

    pace_home = float(home.get("pace", 100))
    pace_away = float(away.get("pace", 100))
    base = (pace_home + pace_away) / 2.0

    off_home = float(home.get("offense_strength", home.get("strength", 0)))
    off_away = float(away.get("offense_strength", away.get("strength", 0)))
    def_home = float(home.get("defense_strength", home.get("strength", 0)))
    def_away = float(away.get("defense_strength", away.get("strength", 0)))

    total = base + 0.5 * ((off_home + off_away) / 2.0) - 0.5 * ((def_home + def_away) / 2.0)
    return total


# -----------------------------
# Injury evaluation
# -----------------------------
def evaluate_injury_risk(team_name: str) -> Dict[str, Any]:
    summary = get_team_injury_summary(team_name)
    roster = get_team_roster(team_name).get("players", {})

    inactive = summary.get("inactive", [])
    total_out = len(inactive)

    starters_out = sum(1 for p in inactive if roster.get(p, {}).get("role", "").lower() == "starter")

    # NO BET guardrail
    if starters_out >= int(get_setting("no_bet_if_starters_out")):
        return {
            "team": team_name,
            "starters_out": starters_out,
            "total_out": total_out,
            "penalty_multiplier": 0.0,
            "no_bet": True,
            "summary": summary,
        }

    per_starter = float(get_setting("injury_penalty_per_starter_out"))
    per_other = float(get_setting("injury_penalty_per_other_out"))
    max_penalty = float(get_setting("max_injury_penalty"))

    others_out = max(total_out - starters_out, 0)
    raw_penalty = starters_out * per_starter + others_out * per_other
    penalty = min(raw_penalty, max_penalty)

    return {
        "team": team_name,
        "starters_out": starters_out,
        "total_out": total_out,
        "penalty_multiplier": max(0.0, 1.0 - penalty),
        "no_bet": False,
        "summary": summary,
    }


# -----------------------------
# Edges + Confidence
# -----------------------------
def compute_edge(projected: float, market: float) -> float:
    return projected - market


def edge_to_confidence(edge: float) -> str:
    thresholds = get_conf_thresholds()
    x = abs(edge)
    if x >= thresholds["S"]: return "S"
    if x >= thresholds["A"]: return "A"
    if x >= thresholds["B"]: return "B"
    if x >= thresholds["C"]: return "C"
    return "NO BET"


# -----------------------------
# Main Model Function
# -----------------------------
def run_matchup(home_team: str, away_team: str, spread_line: float = None, total_line: float = None) -> Dict[str, Any]:
    home_team = normalize_team_name(home_team)
    away_team = normalize_team_name(away_team)

    proj_spread = project_spread(home_team, away_team)
    proj_total = project_total(home_team, away_team)

    home_inj = evaluate_injury_risk(home_team)
    away_inj = evaluate_injury_risk(away_team)

    penalty_mult = min(home_inj["penalty_multiplier"], away_inj["penalty_multiplier"])
    injury_no_bet = home_inj["no_bet"] or away_inj["no_bet"]

    min_edge = float(get_setting("min_edge_to_bet"))

    # -------------------------
    # Spread logic
    # -------------------------
    spread_recommend = "NO BET"
    spread_conf = "NO BET"
    spread_edge = None
    spread_edge_adj = None

    if spread_line is not None:
        spread_edge = compute_edge(proj_spread, spread_line)
        spread_edge_adj = spread_edge * penalty_mult

        if not injury_no_bet and abs(spread_edge_adj) >= min_edge:
            if spread_edge_adj < 0:
                spread_recommend = f"BET HOME ({home_team}) ATS"
            else:
                spread_recommend = f"BET AWAY ({away_team}) ATS"
            spread_conf = edge_to_confidence(spread_edge_adj)

    # -------------------------
    # Total logic
    # -------------------------
    total_recommend = "NO BET"
    total_conf = "NO BET"
    total_edge = None
    total_edge_adj = None

    if total_line is not None:
        total_edge = compute_edge(proj_total, total_line)
        total_edge_adj = total_edge * penalty_mult

        if not injury_no_bet and abs(total_edge_adj) >= min_edge:
            total_recommend = "BET OVER" if total_edge_adj > 0 else "BET UNDER"
            total_conf = edge_to_confidence(total_edge_adj)

    # Injury override
    if injury_no_bet:
        spread_recommend = total_recommend = "NO BET (injury chaos)"
        spread_conf = total_conf = "NO BET"

    # -------------------------
    # Print summary
    # -------------------------
    print("==========================================")
    print(f"MATCHUP: {away_team} @ {home_team}")
    print("==========================================")
    print(f"Projected Spread (home-away): {proj_spread:.2f}")
    print(f"Projected Total: {proj_total:.2f}")
    print("------------------------------------------")

    if spread_line is not None:
        print(f"Market Spread: {spread_line}")
        print(f"Raw Spread Edge: {spread_edge}")
        print(f"Adj Spread Edge: {spread_edge_adj}")
        print(f"Recommendation: {spread_recommend} [{spread_conf}]")
    else:
        print("No spread line provided.")

    print("------------------------------------------")
    if total_line is not None:
        print(f"Market Total: {total_line}")
        print(f"Raw Total Edge: {total_edge}")
        print(f"Adj Total Edge: {total_edge_adj}")
        print(f"Recommendation: {total_recommend} [{total_conf}]")
    else:
        print("No total line provided.")

    print("------------------------------------------")
    print("INJURY SUMMARY:")
    for side, inj in [("Home", home_inj), ("Away", away_inj)]:
        print(f"{side} ({inj['team']}): starters_out={inj['starters_out']} total_out={inj['total_out']}")
        print(f"Inactive: {inj['summary']['inactive']}")
    print(f"Penalty Multiplier: {penalty_mult}")
    if injury_no_bet:
        print("NOTE: Injury chaos triggered NO BET.")
    print("==========================================")

    return {
        "matchup": {"home": home_team, "away": away_team},
        "projections": {"spread": proj_spread, "total": proj_total},
        "market": {"spread": spread_line, "total": total_line},
        "edges": {
            "spread": spread_edge,
            "spread_adj": spread_edge_adj,
            "total": total_edge,
            "total_adj": total_edge_adj,
        },
        "recommendations": {
            "spread": spread_recommend,
            "spread_conf": spread_conf,
            "total": total_recommend,
            "total_conf": total_conf,
        },
        "injuries": {
            "home": home_inj,
            "away": away_inj,
            "penalty_multiplier": penalty_mult,
            "injury_no_bet": injury_no_bet,
        },
    }
