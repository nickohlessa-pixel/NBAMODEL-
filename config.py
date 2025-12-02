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
    "identity": "young, volatile, offense-first, bad defense, perimeter issues",
    "offense_strengths": [
        "elite PnR roll man scoring (#1 in NBA)",
        "elite post scoring",
        "elite putback scoring",
        "elite floater creation",
        "above-average isolation scoring",
        "strong halfcourt shot creation"
    ],
    "defense_weaknesses": [
        "terrible off-screen defense (0th percentile)",
        "bottom 3% spot-up defense",
        "bottom 5% PnR defense (ball handler & roll man)",
        "bad isolation defense",
        "bad transition defense",
        "bad deep 3 defense"
    ],
    "betting_tags": [
        "high-variance team",
        "good underdog",
        "dangerous favorite",
        "totals lean over vs fast teams",
        "fade vs shooting/motion teams",
        "upgrade when LaMelo + Miller are healthy"
    ]
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
