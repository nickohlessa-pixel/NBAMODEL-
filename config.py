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
            "Thunder", "Clippers", "Hawks", "Knicks"
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

    "identity": "Young, volatile, offense-first, poor defense, extreme variance. Elite inside scoring, terrible perimeter shooting and perimeter defense.",

    "offense": {
        "pnr_roll_ppp": "elite",
        "post_up_ppp": "elite",
        "putbacks": "elite",
        "floaters": "strong",
        "isolation": "above_average",
        "shot_profile": "rim-heavy, low-3pt, high-variance",
        "variance": "high"
    },

    "defense": {
        "off_screen_defense": "worst_in_nba",
        "spot_up_defense": "bottom_3_percent",
        "pnr_ball_handler_defense": "bottom_5_percent",
        "pnr_roll_man_defense": "bottom_5_percent",
        "isolation_defense": "poor",
        "transition_defense": "bad",
        "deep_3_defense": "bad"
    },

    "tags": [
        "young_team",
        "high_variance",
        "poor_defense",
        "strong_rim_scoring",
        "weak_shooting",
        "volatile_as_favorite",
        "dangerous_as_dog"
    ],

    "betting_rules": {
        "auto_fade_vs_shooters": True,
        "auto_upgrade_vs_rim_inept_teams": True,
        "totals_lean_over_vs_fast_teams": True,
        "totals_lean_under_vs_slow_ugly_teams": True
    }
},






        
        "Magic":    {"strength": 70},
        "Nuggets":  {"strength": 90},
        "Thunder":  {"strength": 80},
        "Clippers": {"strength": 75},
        "Hawks":    {"strength": 65},
        "Knicks":   {"strength": 72}
    },

    # --- Guardrails ---
    "guardrails": {
        "no_low_edge_bets": True,
        "must_pass_all_filters": True
    }
}

# END OF CONFIG
