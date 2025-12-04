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
        raise ValueError(f"Unknown tea
