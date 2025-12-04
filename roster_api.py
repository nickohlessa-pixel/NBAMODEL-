# ==========================================
# NBA MODEL BRAIN V3.2 - ROSTER API (V1.5)
# Injury + Status A-Path
# Option_A_AutoSave (in-memory helpers)
# ==========================================
#
# PURPOSE:
#   - Provide simple, safe functions for updating rosters.
#   - Track player roles AND injury/availability status.
#   - All data must come from the USER (notes, roles, status).
#   - No internal/training data about players is ever used.
#
# RULES:
#   - If a player/team is unknown, the model should ASK THE USER.
#   - User is TRUTH for all team assignments, roles, status, and notes.
#
# This is an in-memory layer. Persistence (saving back to disk)
# will be added later in a controlled way.
# ==========================================

from rosters import ROSTERS


# -----------------------------
# Core team utilities
# -----------------------------
def ensure_team(team_name: str) -> None:
    """
    Make sure the team exists in ROSTERS.
    If it doesn't, create a blank shell for it.
    We never guess players, we only create an empty bucket
    for the team name string.
    """
    if team_name not in ROSTERS:
        ROSTERS[team_name] = {
            "players": {},
            "notes": "Created automatically. User must populate actual roster."
        }


# -----------------------------
# Player creation / updates
# -----------------------------
def add_player(
    team_name: str,
    player_name: str,
    role: str = "unknown",
    notes: str = "",
    status: str = "active"
) -> None:
    """
    Add or update a player on a given team.

    team_name: string like "Hornets"
    player_name: string like "LaMelo Ball"
    role: user-defined string like "starter", "bench", "inactive", etc.
    notes: any text notes about usage, injuries, etc. (user-defined)
    status: "active", "out", "injured_out", "questionable", etc.

    This function NEVER infers anything from internal data.
    It just trusts what the user says.
    """
    ensure_team(team_name)

    team = ROSTERS[team_name]
    players = team.setdefault("players", {})

    player_entry = players.get(player_name, {})
    player_entry["role"] = role
    player_entry["notes"] = notes
    player_entry["status"] = status

    players[player_name] = player_entry


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


# -----------------------------
# Status / injury helpers
# -----------------------------
def set_player_status(team_name: str, player_name: str, status: str) -> None:
    """
    Set the availability/injury status for a player.

    Recommended statuses (but free-form):
      - "active"
      - "out"
      - "injured_out"
      - "questionable"
      - "probable"
      - "rest"

    If the player doesn't exist yet, this function does nothing.
    Callers should ask the user to confirm rosters if missing.
    """
    team = ROSTERS.get(team_name)
    if not team:
        return

    players = team.get("players", {})
    if player_name not in players:
        return

    players[player_name]["status"] = status


def mark_player_active(team_name: str, player_name: str) -> None:
    """Convenience wrapper for setting a player to active."""
    set_player_status(team_name, player_name, "active")


def mark_player_out(team_name: str, player_name: str) -> None:
    """Convenience wrapper for setting a player to out."""
    set_player_status(team_name, player_name, "out")


def mark_player_injured_out(team_name: str, player_name: str) -> None:
    """Convenience wrapper for setting a player to injured_out."""
    set_player_status(team_name, player_name, "injured_out")


def get_player_status(team_name: str, player_name: str) -> str:
    """
    Return the status string for a player.
    If anything is missing, returns "unknown".
    """
    team = ROSTERS.get(team_name)
    if not team:
        return "unknown"

    players = team.get("players", {})
    if player_name not in players:
        return "unknown"

    return players[player_name].get("status", "unknown")


# -----------------------------
# Read-only roster views
# -----------------------------
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


def get_active_players(team_name: str):
    """
    Return a list of player names whose status is NOT clearly out.

    For now we treat:
      - "active" -> included
      - missing/unknown status -> included (model can decide how to penalize)
      - any status containing "out" -> excluded

    This keeps the API simple and defers deeper logic to model.py.
    """
    team = ROSTERS.get(team_name)
    if not team:
        return []

    players = team.get("players", {})
    active = []
    for name, info in players.items():
        status = str(info.get("status", "active")).lower()
        if "out" in status:
            continue
        active.append(name)
    return active


def get_inactive_players(team_name: str):
    """
    Return a list of player names whose status clearly indicates they are out.

    Any status string containing "out" is treated as inactive here.
    """
    team = ROSTERS.get(team_name)


def get_team_injury_summary(team_name: str) -> dict:
    """
    Lightweight snapshot for the model:

    Returns:
      {
        "team": <team_name>,
        "active": [list of active-ish players],
        "inactive": [list of players marked out/injured_out/...],
      }
    """
    return {
        "team": team_name,
        "active": get_active_players(team_name),
        "inactive": get_inactive_players(team_name),
    }

