# ==========================================
# NBA MODEL BRAIN V3.2 - STARTER MODEL FILE
# ==========================================

from config import BRAIN_CONFIG


def get_team_strength(team_name: str) -> int:
    """
    Look up the dummy strength rating for a team from BRAIN_CONFIG.
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


def run_matchup(team_a: str, team_b: str, spread: float, total: float) -> None:
    """
    Basic version:
    - Prints matchup info
    - Looks up team strength for each team
    - Prints which team is stronger on paper and by how much
    - Shows core teams & active filters
    - Still NO real edge math yet (just wiring)
    """

    print("=== NBA MODEL BRAIN V3.2 ===")
    print(f"Matchup: {team_a} vs {team_b}")
    print(f"Spread: {spread}")
    print(f"Total:  {total}")

    # Get dummy strength ratings
    strength_a = get_team_strength(team_a)
    strength_b = get_team_strength(team_b)

    print(f"\n{team_a} strength: {strength_a}")
    print(f"{team_b} strength: {strength_b}")

    # Compare strengths
    if strength_a > strength_b:
        stronger_team = team_a
        diff = strength_a - strength_b
    elif strength_b > strength_a:
        stronger_team = team_b
        diff = strength_b - strength_a
    else:
        stronger_team = "Equal (push)"
        diff = 0

    print(f"\nOn raw strength numbers, stronger team: {stronger_team}", end="")
    if diff != 0:
        print(f" (diff: {diff} points)")
    else:
        print("")

    print("\nCore teams:", BRAIN_CONFIG["universe_rules"]["core_teams"])
    print("Filters active:", BRAIN_CONFIG["filters"])
    print("\nNOTE: This is still a dummy model. No real edge math yet.")
