# ==========================================
# NBA MODEL BRAIN V3.5 - MODEL CORE (V1.5)
# Spread, Totals, Edges, Confidence + Injuries
# ==========================================
#
# PURPOSE:
#   - Project spreads and totals between two teams.
#   - Estimate edges vs market lines.
#   - Assign confidence tiers (S / A / B / C / NO BET).
#   - Integrate basic injury/availability risk using roster_api.
#
# RULES:
#   - USER IS TRUTH for rosters, roles, status.
#   - NEVER use internal/training rosters.
#   - If a team or player is unknown: CALLER SHOULD ASK USER.
# ==========================================

from typing import Dict, Any

try:
    from config import TEAM_CONFIG, MODEL_SETTINGS, TEAM_NAME_MAP
except ImportError:
    TEAM_CONFIG = {}
    MODEL_SETTINGS = {}
    TEAM_NAME_MAP = {}

from roster_api import (
    get_team_roster,
    get_team_injury_summary,
)


# -----------------------------
# Defaults / guardrails
# -----------------------------
DEFAULT_MODEL_SETTINGS = {
    "min_edge_to_bet": 1.5,
    "confidence_thresholds": {
        "S": 4.0,
        "A": 3.0,
        "B": 2.0,
        "C": 1.0,
    },
    "injury_penalty_per_starter_out": 0.15,   # 15% per missing starter
    "injury_penalty_per_other_out": 0.05,     # 5% per missing non-starter
    "max_injury_penalty": 0.50,               # cap overall penalty at 50%
    "no_bet_if_starters_out": 3,              # 3+ starters out -> NO BET
}


def get_setting(key: str, default_key: str = None):
    if not MODEL_SETTINGS:
        return DEFAULT_MODEL_SETTINGS.get(key)
    if key in MODEL_SETTINGS:
        return MODEL_SETTINGS[key]
    if default_key and default_key in DEFAULT_MODEL_SETTINGS:
        return DEFAULT_MODEL_SETTINGS[default_key]
    return DEFAULT_MODEL_SETTINGS.get(key)


def get_conf_thresholds() -> Dict[str, float]:
    custom = MODEL_SETTINGS.get("confidence_thresholds") if MODEL_SETTINGS else None
    if isinstance(custom, dict):
        return {
            "S": float(custom.get("S", DEFAULT_MODEL_SETTINGS["confidence_thresholds"]["S"])),
            "A": float(custom.get("A", DEFAULT_MODEL_SETTINGS["confidence_thresholds"]["A"])),
            "B": float(custom.get("B", DEFAULT_MODEL_SETTINGS["confidence_thresholds"]["B"])),
            "C": float(custom.get("C", DEFAULT_MODEL_SETTINGS["confidence_thresholds"]["C"])),
        }
    return DEFAULT_MODEL_SETTINGS["confidence_thresholds"]


# -----------------------------
# Team / config helpers
# -----------------------------
def normalize_team_name(team: str) -> str:
    """Map any alt key (e.g. 'CHA', 'Charlotte Hornets') to our config key."""
    if TEAM_NAME_MAP and team in TEAM_NAME_MAP:
        return TEAM_NAME_MAP[team]
    return team


def get_team_config(team: str) -> Dict[str, Any]:
    team_key = normalize_team_name(team)
    cfg = TEAM_CONFIG.get(team_key)
    if not cfg:
        raise ValueError(f"[MODEL] Unknown team config for '{team}' (normalized: '{team_key}').")
    return cfg


# -----------------------------
# Projections
# -----------------------------
def project_spread(home_team: str, away_team: str) -> float:
    """
    Project home - away spread (negative means home favored).
    Simple version: strength differential + home advantage.
    """
    home_cfg = get_team_config(home_team)
    away_cfg = get_team_config(away_team)

    home_strength = float(home_cfg.get("strength", 0.0))
    away_strength = float(away_cfg.get("strength", 0.0))
    home_edge = float(home_cfg.get("home_edge", 0.0))

    # Positive means home better. Convert to a spread in points.
    diff = home_strength - away_strength
    projected_spread = -(diff + home_edge)
    return projected_spread


def project_total(home_tea
