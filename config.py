# ==========================================
# NBA MODEL BRAIN V3.2 - CONFIG (Updated Strengths)
# ==========================================

BRAIN_CONFIG = {

    # --- Universe Rules ---
    "universe_rules": {
        "user_is_truth": True,
        "roster_engine": "Option_A_AutoSave",
        "core_teams": [
            "Hornets",
            "Magic",
            "Nuggets",
            "Thunder",
            "Clippers",
            "Heat",
            "Knicks"
        ]
    },

    # --- Betting Rules ---
    "betting": {
        "unit_system": "1U_default",
        "allow_props": False,
        "high_conviction_only": True,
        "require_min_edge": True
    },

    # --- Filters ---
    "filters": {
        "info_certainty": True,
        "trend_confirmation": True,
        "matchup_logic": True,
        "line_value_required": True,
        "no_emotion": True,
        "variance_filter": True,
        "anti_ass_blast": True
    },

    # --- Team Profiles ---
    "teams": {
        "Thunder": {
            "strength": 90,
            "identity": {
                "offense": "drive-and-kick, efficient slashing, good spacing, lots of free throws",
                "defense": "switchable, disruptive on-ball, vulnerable on glass vs size",
                "pace": "fast",
                "variance": "medium",
                "shot_profile": {"rim": "high", "midrange": "low", "threes": "high"}
            }
        },

        "Knicks": {
            "strength": 85,
            "identity": {
                "offense": "heavy on star creation, offensive rebounding, iso scoring",
                "defense": "physical, strong glass control, susceptible to pull-up shooting",
                "pace": "slow",
                "variance": "low",
                "shot_profile": {"rim": "medium", "midrange": "medium", "threes": "medium"}
            }
        },

        "Heat": {
            "strength": 80,
            "identity": {
                "offense": "grindy, movement-based, handoff sets, streaky shooting",
                "defense": "schemey, zone/switch, disciplined but vulnerable to size/talent gaps",
                "pace": "slow",
                "variance": "medium",
                "shot_profile": {"rim": "low", "midrange": "medium", "threes": "medium"}
            }
        },

        "Magic": {
            "strength": 75,
            "identity": {
                "offense": "size-based, downhill pressure, post-heavy, streaky shooting",
                "defense": "elite length, strong rotations, rim protection, weakness vs elite shooters",
                "pace": "medium",
                "variance": "medium",
                "shot_profile": {"rim": "high", "midrange": "low", "threes": "medium"}
            }
        },

        "Nuggets": {
            "strength": 70,
            "identity": {
                "offense": "Jokic-engine, elite halfcourt efficiency, cutting & two-man game",
                "defense": "solid structure, drops in bench minutes, vulnerable without Jokic",
                "pace": "medium",
                "variance": "low",
                "shot_profile": {"rim": "medium", "midrange": "medium", "threes": "medium"}
            }
        },

        "Hornets": {
            "strength": 65,
            "identity": {
                "offense": "paint-heavy, PnR, floaters, terrible 3pt shooting",
                "defense": "poor POA, bad vs movement & shooting, weak PnR defense",
                "pace": "fast",
                "variance": "high",
                "shot_profile": {"rim": "high", "midrange": "medium", "threes": "low"}
            }
        },

        "Clippers": {
            "strength": 60,
            "identity": {
                "offense": "iso/PnR heavy, midrange leaning, veteran shot-making",
                "defense": "aging switch defenders, inconsistent intensity",
                "pace": "slow",
                "variance": "high",
                "shot_profile": {"rim": "low", "midrange": "high", "threes": "medium"}
            }
        }
    },

    # --- Guardrails ---
    "guardrails": {
        "no_low_edge_bets": True,
        "must_pass_all_filters": True
    }
}

# END OF CONFIG
