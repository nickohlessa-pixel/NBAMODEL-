# ==========================================
# NBA MODEL BRAIN V3.2 - STARTER MODEL FILE
# ==========================================

from config import BRAIN_CONFIG

def get_team_strength(team_name: str) -> int:
    """
    Look up the dummy strength rating for a team from BRAIN_CONFIG.
    If the team is not found, default to 50.
    """
    teams = BRAIN_CONFIG["teams"]
    team_info = teams.get(team_name, {})
    return team_info.get("strength", 50)


def run_matchup(team_a, team_b, spread, total):
    """
    Basic version:
    - Prints matchup info
    - Looks up team strength for each team
    - Prints which team is stronger on paper and by how much
    - Gives a DUMMY lean (no real edge logic yet)
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
    elif strength_b > strength_a:
        stronger_team = team_b
    else:
        stronger_team = "Equal (push)"

    strength_diff = abs(strength_a - strength_b)
    print(f"\nOn raw strength numbers, stronger team: {stronger_team} (diff: {strength_diff} points)")

    print("\nCore teams:", BRAIN_CONFIG["universe_rules"]["core_teams"])
    print("Filters active:", BRAIN_CONFIG["filters"])
    print("\nNOTE: This is still a dummy model. No real edge math yet.")


def get_team_profile(team_name: str):
    """Return the full team profile dictionary (not just strength)."""
    teams = BRAIN_CONFIG["teams"]
    return teams.get(team_name, {})


def get_team_profile(team_name: str):
    return BRAIN_CONFIG["teams"].get(team_name, {})



def get_team_profile(team_name: str):
    """
    Returns the full team block from BRAIN_CONFIG.
    This lets the model use the real V3.2 knowledge pack
    instead of the old placeholder 'strength only' system.
    """
    teams = BRAIN_CONFIG.get("teams", {})
    profile = teams.get(team_name)
    
    if profile is None:
        return {"error": f"Team '{team_name}' not found in BRAIN_CONFIG"}
    
    return profile



