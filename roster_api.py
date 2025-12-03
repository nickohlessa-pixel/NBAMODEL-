# ==========================================
# NBA MODEL BRAIN V3.2 - ROSTER API
# Option_A_AutoSave (in-memory helpers)
# ==========================================
#
# PURPOSE:
#   - Provide simple, safe functions for updating rosters.
#   - All data must come from the USER (notes, roles, etc.).
#   - No internal/training data about players is ever used.
#
# RULES:
#   - If a player/team is unknown, the model should ASK THE USER.
#   - User is TRUTH for all team assignments, roles, and notes.
#
# This is an in-memory layer. Persistence (saving back to disk)
# will be added later in a controlled way.
# ==========================================

from rosters import ROSTERS


def ensure_team(team_name: str) -> None:
    """
    Make sure the team exists in ROSTERS.
    If it doesn't, create a blank shell for it.
    This still respects user-as-truth: we never guess players,
    just create an empty bucket for the team name string.
    """
    if team_name not in ROSTERS:
        ROSTERS[team_name] = {
            "players": {},
            "notes": "Created automatically. User must populate actual roster."
        }


def add_player(team_name: str, player_name: str, role: str = "unknown", notes: str = "") -> None:
    """
    Add or update a player on a given team.

    team_name: string like "Hornets"
    player_name: string like "LaMelo Ball"
    role: "starter", "bench", "inactive", etc. (free text, user-defined)
    notes: any text notes about usage, injuries, etc. (user-defined)

    This function NEVER infers anything from internal data.
    It just trusts what the user says.
    """
    ensure_team(team_name)

    team = ROSTERS[team_name]
    players = team.setdefault("players", {})

    players[player_name] = {
        "role": role,
        "notes": notes
    }


def update_player_role(team_name: str, player_name: str, role: str) -> None:
    """
    Update only the role for an existing player.
    If the player/team doesn't exist, the function does nothing.
    (The calling code should handle asking the user what to do.)
    """
    team = ROSTERS.get(team_name)
    if not team:
        return

    players = team.get("players", {})
    if player_name not in players:
        return

    players[player_name]["role"] = role


def update_player_notes(team_name: str, player_name: str, notes: str) -> None:
    """
    Update only the notes for an existing player.
    If the player/team doesn't exist, the function does nothing.
    """
    team = ROSTERS.get(team_name)
    if not team:
        return

    players = team.get("players", {})
    if player_name not in players:
        return

    players[player_name]["notes"] = notes


def get_team_roster(team_name: str) -> dict:
    """
    Return the roster dict for a given team.
    If team doesn't exist yet, returns an empty shell.
    """
    ensure_team(team_name)
    return ROSTERS[team_name]


def list_team_players(team_name: str):
    """
    Convenience helper: return a list of player names for a team.
    If team doesn't exist, returns an empty list.
    """
    team = ROSTERS.get(team_name)
    if not team:
        return []

    return list(team.get("players", {}).keys())


# END OF ROSTER API
