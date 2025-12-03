# ==========================================
# NBA MODEL BRAIN V3.2 - ROSTER ENGINE (Option_A_AutoSave)
# ==========================================
#
# This file stores rosters *only from user inputs*.
# NOTHING in this file should EVER come from internal training data.
# User is TRUTH. If a player isn't listed here, the model must ask:
#
#   "What team is X on in our universe?"
#
# This file is the single source of truth for:
#   - Team rosters
#   - Player roles (starter / bench / inactive)
#   - Notes (injuries, usage, matchups, trends)
#
# Future expansion:
#   - Auto-saving updates
#   - Tracking roles over time
#   - Minutes estimates
#   - Injury state
#   - Export/import roster packs
#
# For now, start simple:
#   - Empty rosters for all core teams
#   - Guaranteed safe structure for expansion
# ==========================================


ROSTERS = {
    "Thunder": {
        "players": {},
        "notes": "User will populate Thunder roster."
    },
    "Knicks": {
        "players": {},
        "notes": "User will populate Knicks roster."
    },
    "Heat": {
        "players": {},
        "notes": "User will populate Heat roster."
    },
    "Magic": {
        "players": {},
        "notes": "User will populate Magic roster."
    },
    "Nuggets": {
        "players": {},
        "notes": "User will populate Nuggets roster."
    },
    "Hornets": {
        "players": {},
        "notes": "User will populate Hornets roster."
    },
    "Clippers": {
        "players": {},
        "notes": "User will populate Clippers roster."
    }
}

# END OF ROSTERS FILE
