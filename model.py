# ==========================================
# NBA MODEL BRAIN V3.2 - STARTER MODEL FILE
# ==========================================

from config import BRAIN_CONFIG


def run_matchup(team_a, team_b, spread, total):
    """
    Starter function.
    Right now it only prints what you typed.
    Later we add the full V3.2 brain logic here.
    """

    print("=== NBA MODEL BRAIN V3.2 ===")
    print(f"Matchup: {team_a} vs {team_b}")
    print(f"Spread: {spread}")
    print(f"Total:  {total}")
    print("\nCore teams:", BRAIN_CONFIG["universe_rules"]["core_teams"])
    print("Filters active:", BRAIN_CONFIG["filters"])
    print("\nModel not wired yet — this is just the starter skeleton.")


# Optional: quick test
if __name__ == "__main__":
    run_matchup("Hornets", "Knicks", -3.5, 228.5)
