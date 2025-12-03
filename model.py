# ==========================================
# NBA MODEL BRAIN V3.2 - MODEL LOGIC V1.3
# ==========================================

from config import BRAIN_CONFIG


# ------------------------------
# Helpers for config lookups
# ------------------------------

def get_team_strength(team_name: str) -> int:
    """
    Look up the strength rating for a team from BRAIN_CONFIG.
    If the team is not found, default to 50.
    """
    teams = BRAIN_CONFIG.get("teams", {})
    team_info = teams.get(team_name, {})
    return team_info.get("strength", 50)


def get_team_profile(team_name: str) -> dict:
    """
    Return the full team profile dict from BRAIN_CONFIG["teams"].
    If not found, return an empty dict.
    """
    teams = BRAIN_CONFIG.get("teams", {})
    return teams.get(team_name, {})


def get_roster_key(team_name: str) -> str:
    """
    Resolve a model team name (e.g. 'Thunder', 'Heat') to the roster.py key
    using universe_rules.team_key_map.

    If no mapping exists, return the team_name itself.
    This does NOT touch actual rosters.py – it just figures out which key
    should be used when we DO look into rosters.
    """
    universe = BRAIN_CONFIG.get("universe_rules", {})
    team_key_map = universe.get("team_key_map", {})
    return team_key_map.get(team_name, team_name)


# ------------------------------
# Pace / scoring model
# ------------------------------

def _pace_score(team_profile: dict) -> int:
    """
    Convert the team's pace identity into a simple numeric pace score.
    fast  -> +1
    medium / missing -> 0
    slow  -> -1
    """
    identity = team_profile.get("identity", {})
    pace_str = identity.get("pace", "medium").lower()
    if pace_str == "fast":
        return 1
    if pace_str == "slow":
        return -1
    return 0  # default "medium" / unknown


def project_spread(team_a: str, team_b: str) -> dict:
    """
    Projected spread model using strength ratings.

    strength_diff = strength_a - strength_b
      > 0  => team_a stronger
      < 0  => team_b stronger

    To avoid cartoon numbers:
    - Clamp strength_diff to [-30, 30]
    - Map ~10 strength points to ~2 spread points
    """
    strength_a = get_team_strength(team_a)
    strength_b = get_team_strength(team_b)
    strength_diff = strength_a - strength_b

    # Clamp huge mismatches
    max_diff = 30
    clamped_diff = max(min(strength_diff, max_diff), -max_diff)

    # 10 strength → 2 spread points  (factor = 0.2)
    # NOTE: negative spread means team_a is FAVORED from team_a perspective.
    raw_spread = -clamped_diff * 0.2
    model_spread_team_a = round(raw_spread * 2) / 2.0  # round to 0.5

    return {
        "team_a_strength": strength_a,
        "team_b_strength": strength_b,
        "strength_diff": strength_diff,
        "clamped_diff": clamped_diff,
        "model_spread_team_a": model_spread_team_a,
    }


def project_total(team_a: str, team_b: str) -> dict:
    """
    First-pass projected total using pace adjustments.

    Base total = 225
    FAST team = +4
    SLOW team = -4
    """
    base_total = 225.0

    profile_a = get_team_profile(team_a)
    profile_b = get_team_profile(team_b)

    pace_score_a = _pace_score(profile_a)
    pace_score_b = _pace_score(profile_b)
    combined_pace_score = pace_score_a + pace_score_b

    pace_adjustment = combined_pace_score * 4.0
    raw_total = base_total + pace_adjustment
    model_total = round(raw_total, 1)

    return {
        "base_total": base_total,
        "pace_score_a": pace_score_a,
        "pace_score_b": pace_score_b,
        "combined_pace_score": combined_pace_score,
        "pace_adjustment": pace_adjustment,
        "model_total": model_total,
    }


# ------------------------------
# Guardrails / edges
# ------------------------------

def _min_edge_points() -> float:
    """
    Minimum edge required by guardrails.
    """
    betting_cfg = BRAIN_CONFIG.get("betting", {})
    guardrails = BRAIN_CONFIG.get("guardrails", {})

    require_min_edge = betting_cfg.get("require_min_edge", True)
    no_low_edge_bets = guardrails.get("no_low_edge_bets", True)

    if not (require_min_edge and no_low_edge_bets):
        return 0.0

    return 2.0  # default threshold


# ------------------------------
# Public API
# ------------------------------

def evaluate_matchup(team_a: str, team_b: str, spread: float, total: float) -> dict:
    """
    Returns a pure data dict containing all model outputs.
    No printing, no formatting.

    team_a / team_b should be the CONFIG names:
        e.g. "Thunder", "Hornets", "Nuggets", "Magic", "Heat", "Clippers", "Knicks"

    This function also resolves the roster keys (for rosters.py) using
    universe_rules.team_key_map and returns them as:
        - team_a_roster_key
        - team_b_roster_key
    """

    # --- Spread ---
    spread_result = project_spread(team_a, team_b)
    model_spread_team_a = spread_result["model_spread_team_a"]
    spread_edge = model_spread_team_a - spread

    # --- Total ---
    total_result = project_total(team_a, team_b)
    model_total = total_result["model_total"]
    total_edge = model_total - total

    # --- Guardrails / config ---
    universe_rules = BRAIN_CONFIG.get("universe_rules", {})
    core_teams = universe_rules.get("core_teams", [])
    filters = BRAIN_CONFIG.get("filters", {})
    guardrails = BRAIN_CONFIG.get("guardrails", {})
    min_edge = _min_edge_points()

    # --- Recommendations (very simple for now) ---
    spread_reco = "NO BET"
    total_reco = "NO BET"

    if abs(spread_edge) >= min_edge:
        spread_reco = "MODEL LEAN"
    if abs(total_edge) >= min_edge:
        total_reco = "MODEL LEAN"

    # --- Roster keys for future role/roster-aware logic ---
    team_a_roster_key = get_roster_key(team_a)
    team_b_roster_key = get_roster_key(team_b)

    return {
        # matchup
        "team_a": team_a,
        "team_b": team_b,
        "team_a_roster_key": team_a_roster_key,
        "team_b_roster_key": team_b_roster_key,
        "market_spread": spread,
        "market_total": total,

        # spread model
        "team_a_strength": spread_result["team_a_strength"],
        "team_b_strength": spread_result["team_b_strength"],
        "strength_diff": spread_result["strength_diff"],
        "clamped_diff": spread_result["clamped_diff"],
        "model_spread_team_a": model_spread_team_a,
        "spread_edge": spread_edge,

        # total model
        "base_total": total_result["base_total"],
        "pace_score_a": total_result["pace_score_a"],
        "pace_score_b": total_result["pace_score_b"],
        "combined_pace_score": total_result["combined_pace_score"],
        "pace_adjustment": total_result["pace_adjustment"],
        "model_total": model_total,
        "total_edge": total_edge,

        # guardrails
        "core_teams": core_teams,
        "filters": filters,
        "guardrails": guardrails,
        "min_edge": min_edge,

        # outputs
        "spread_reco": spread_reco,
        "total_reco": total_reco,
    }


def run_matchup(team_a: str, team_b: str, spread: float, total: float) -> None:
    """
    Pretty-printed wrapper around evaluate_matchup().

    NOTE:
    - team_a / team_b should be the CONFIG names ("Thunder", "Hornets", etc.)
    - Roster keys are also shown so you know exactly which keys rosters.py uses
      if/when we pull in player/role logic later.
    """

    result = evaluate_matchup(team_a, team_b, spread, total)

    print("=== NBA MODEL BRAIN V3.2 ===")
    print(f"Matchup: {result['team_a']} vs {result['team_b']}")
    print(f"Roster keys: {result['team_a_roster_key']} vs {result['team_b_roster_key']}")
    print(f"Market spread (team_a perspective): {result['market_spread']}")
    print(f"Market total: {result['market_total']}")

    print("\n--- Strength & Spread Model ---")
    print(f"{result['team_a']} strength: {result['team_a_strength']}")
    print(f"{result['team_b']} strength: {result['team_b_strength']}")
    print(f"Strength diff (team_a - team_b): {result['strength_diff']}")
    print(f"Clamped diff used for spread: {result['clamped_diff']}")
    print(f"Model projected spread for {result['team_a']}: {result['model_spread_team_a']}")
    print(f"Spread edge (model - market): {result['spread_edge']:+.1f} points")

    print("\n--- Total Model ---")
    print(f"Base total: {result['base_total']}")
    print(f"{result['team_a']} pace score: {result['pace_score_a']}")
    print(f"{result['team_b']} pace score: {result['pace_score_b']}")
    print(f"Combined pace score: {result['combined_pace_score']}")
    print(f"Pace adjustment: {result['pace_adjustment']:+.1f}")
    print(f"Model projected total: {result['model_total']}")
    print(f"Total edge (model - market): {result['total_edge']:+.1f} points")

    print("\n--- Guardrails & Filters ---")
    print("Core teams:", result["core_teams"])
    print("Filters active:", result["filters"])
    print("Guardrails:", result["guardrails"])
    print(f"\nMinimum edge required by config: {result['min_edge']} points")

    print(f"\nSpread recommendation: {result['spread_reco']}")
    print(f"Total recommendation:  {result['total_reco']}")

    print("\nNOTE:")
    print("- This is V1.3 logic (V1.2 + team_key_map awareness).")
    print("- No injury data or BBall Index matchup stats yet.")
    print("- All roster/role data comes only from user inputs.")
    print("- Guardrails are active and can be tuned later.")
