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
        "offense": "elite paint scoring, PnR-heavy, good floaters, terrible 3pt shooting",
        "defense": "poor POA, bad vs shooters and movement, weak PnR defense",
        "pace": "fast",
        "variance": "high",
        "shot_profile": {
            "rim": "high",
            "midrange": "medium",
            "threes": "low",
            "creation": "heliocentric LaMelo-driven"
        }
    },

    "rotation": {
        "LaMelo Ball": "primary creator, high-usage engine, high-variance scorer",
        "Brandon Miller": "secondary creator, improving shotmaker",
        "Mark Williams": "rim finisher, rebounder, roll man (only if user confirms he's active in 25–26)",
        "Supporting Wings": "volatile, inconsistent shooting, defensive issues"
    },

    "strengths": [
        "Elite PnR roll-man scoring",
        "Elite post-up scoring",
        "Elite putback efficiency",
        "Elite floater creation",
        "Top-1 transition scoring efficiency"
    ],

    "weaknesses": [
        "Worst off-screen defense in NBA",
        "Bottom 3% spot-up defense",
        "Bottom-tier PnR ball-handler defense",
        "Bad in isolation defense",
        "Terrible 3pt shooting and spacing"
    ],

    "betting_angles": [
        "High-variance: good dogs, bad favorites",
        "Overs vs soft defenses",
        "Unders vs slow rock-fight teams",
        "Fade them vs shooting teams",
        "Back them vs non-shooting interior teams"
    ]
},





        
        "Magic":    {"strength": 70},
        "Nuggets":  {"strength": 90},
        "Thunder":  {"strength": 80},
        "Clippers": {"strength": 75},
        "Heat":    {"strength": 65},
        "Knicks":   {"strength": 72}
    },

    # --- Guardrails ---
    "guardrails": {
        "no_low_edge_bets": True,
        "must_pass_all_filters": True
    }
}

# END OF CONFIG
