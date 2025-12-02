%%writefile config.py
# ==========================================
# NBA MODEL BRAIN V3.2 - CONFIG SKELETON
# ==========================================

BRAIN_CONFIG = {

     # --- Universe Rules ---
    "universe_rules": {
        "user_is_truth": True,
        "roster_engine": "Option_A_AutoSave",
        "core_teams": [
            "Hornets", "Magic", "Nuggets",
            "Thunder", "Clippers", "Heat", "Knicks"
        ]
    },


    # --- Betting Rules ---
    "betting": {
        "unit_system": "1U_default",
        "allow_props": False,
        "high_conviction_only": True,
        "require_min_edge": True
    },

    # --- Filters (7-filter system) ---
    "filters": {
        "info_certainty": True,
        "trend_confirmation": True,
        "matchup_logic": True,
        "line_value_required": True,
        "no_emotion": True,
        "variance_filter": True,
        "anti_ass_blast": True
    },

    # --- Team Profiles (dummy strength ratings) ---
    "teams": {
     
                "Hornets": {
            "strength": 40,
            "identity": {
                "offense": "elite paint and PnR scoring, bad 3PT shooting, high variance",
                "defense": "poor POA, bad vs shooters and movement, weak PnR defense",
                "pace": "fast",
                "variance": "high",
                "shot_profile": {
                    "rim": "high",
                    "midrange": "medium",
                    "threes": "low"
                }
            }
        },

        
        "Magic": {"strength": 70},
        "Nuggets": {"strength": 90},
        "Thunder": {"strength": 80},
        "Clippers": {"strength": 75},
        "Heat": {"strength": 50},
        "Knicks": {"strength": 72}
    },

    # --- Guardrails ---
    "guardrails": {
        "no_low_edge_bets": True,
        "must_pass_all_filters": True
    }
}

# END OF CONFIG
