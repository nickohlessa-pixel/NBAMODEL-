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
            "strength": 40,  # rough overall baseline, we'll tune later

            # 2025-26 core roster snapshot (no Mark Williams)
            "roster_2025_26": [
                "LaMelo Ball",
                "Tre Mann",
                "Collin Sexton",
                "KJ Simpson",
                "Kon Knueppel",
                "Sion James",
                "Josh Green",
                "Pat Connaughton",
                "Liam McNeeley",
                "Miles Bridges",
                "Drew Peterson",
                "Ryan Kalkbrenner",
                "Moussa Diabaté",
                "Mason Plumlee",
                "Grant Williams"
            ],

            # Quick tags about who they are right now
            "style_tags": [
                "offense_middle_of_pack",   # ORtg ~115, around 19–20th :contentReference[oaicite:0]{index=0}
                "defense_bottom_10",        # DRtg ~120, about 24th :contentReference[oaicite:1]{index=1}
                "rebounds_top_half",        # good rebounding rates, esp. defensive :contentReference[oaicite:2]{index=2}
                "pace_medium"               # not super fast like old Melo teams, more middle-ish :contentReference[oaicite:3]{index=3}
            ],

            # Snapshot team stats for 2025-26 to drive future logic
            "team_stats_2025_26": {
                "off_rating": 115.1,          # offensive rating :contentReference[oaicite:4]{index=4}
                "def_rating": 119.8,          # defensive rating :contentReference[oaicite:5]{index=5}
                "net_rating": -4.7,           # net rating (bad but not worst) :contentReference[oaicite:6]{index=6}
                "pts_per_game": 115.2,        # team PPG :contentReference[oaicite:7]{index=7}
                "opp_pts_per_game": 120.0     # opponent PPG :contentReference[oaicite:8]{index=8}
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
