# ==========================================
# NBA MODEL BRAIN V3.2 - CONFIG (Updated Strengths + Team Key Map)
# ==========================================

BRAIN_CONFIG = {

    # --- Metadata / Version ---
    "meta": {
        "version": "3.2",
        "description": "Core team strengths, identities, and guardrails for NBA Model Brain V3.2"
    },

    # --- Universe Rules ---
    "universe_rules": {
        "user_is_truth": True,
        "roster_engine": "Option_A_AutoSave",

        # Core teams the brain will treat as highest priority for accuracy/depth
        "core_teams": [
            "Hornets",
            "Magic",
            "Nuggets",
            "Thunder",
            "Clippers",
            "Heat",
            "Knicks"
        ],

        # Mapping between shorthand model names and roster.py keys
        # This prevents any confusion between "Thunder" vs "Oklahoma City Thunder", etc.
        "team_key_map": {
            "Thunder": "Oklahoma City Thunder",
            "Heat": "Miami Heat",
            "Magic": "Magic",
            "Nuggets": "Nuggets",
            "Hornets": "Hornets",
            "Clippers": "Clippers",
            "Knicks": "Knicks"
        }
    },

    # --- Betting Rules ---
    "betting": {
        "unit_system": "1U_default",
        "allow_props": False,
        "high_conviction_only": True,
        "require_min_edge": True
    },

    # --- Filters / Guardrails Switches ---
    "filters": {
        "info_certainty": True,       # Must have up-to-date info
        "trend_confirmation": True,   # Trends must be real, not one-game noise
        "matchup_logic": True,        # Basketball logic must align with numbers
        "line_value_required": True,  # No bets without clear value vs line
        "no_emotion": True,           # No vibes-only bets
        "variance_filter": True,      # Avoid ultra-high volatility spots unless edge is huge
        "anti_ass_blast": True        # Explicitly avoid spots likely to create blowouts against us
    },

    # --- Team Profiles (Strengths + Identities) ---
    "teams": {
        "Thunder": {
            "strength": 90,
            "identity": {
                "offense": "drive-and-kick, efficient slashing, good spacing, lots of free throws",
                "defense": "switchable, disruptive on-ball, vulnerable on glass vs size",
                "pace": "fast",
                "variance": "medium",
                "shot_profile": {
                    "rim": "high",
                    "midrange": "low",
                    "threes": "high"
                }
            }
        },

        "Knicks": {
            "strength": 85,
            "identity": {
                "offense": "heavy on star creation, offensive rebounding, iso scoring",
                "defense": "physical, strong glass control, susceptible to pull-up shooting",
                "pace": "slow",
                "variance": "low",
                "shot_profile": {
                    "rim": "medium",
                    "midrange": "medium",
                    "threes": "medium"
                }
            }
        },

        "Heat": {
            "strength": 80,
            "identity": {
                "offense": "grindy, movement-based, handoff sets, streaky shooting",
                "defense": "schemey, zone/switch, disciplined but vulnerable to size/talent gaps",
                "pace": "slow",
                "variance": "medium",
                "shot_profile": {
                    "rim": "low",
                    "midrange": "medium",
                    "threes": "medium"
                }
            }
        },

        "Magic": {
            "strength": 75,
            "identity": {
                "offense": "size-based, downhill pressure, post-heavy, streaky shooting",
                "defense": "elite length, strong rotations, rim protection, weakness vs elite shooters",
                "pace": "medium",
                "variance": "medium",
                "shot_profile": {
                    "rim": "high",
                    "midrange": "low",
                    "threes": "medium"
                }
            }
        },

        "Nuggets": {
            "strength": 70,
            "identity": {
                "offense": "Jokic-engine, elite halfcourt efficiency, cutting & two-man game",
                "defense": "solid structure, drops in bench minutes, vulnerable without Jokic",
                "pace": "medium",
                "variance": "low",
                "shot_profile": {
                    "rim": "medium",
                    "midrange": "medium",
                    "threes": "medium"
                }
            }
        },

        "Hornets": {
            "strength": 65,
            "identity": {
                "offense": "paint-heavy, PnR, floaters, terrible 3pt shooting",
                "defense": "poor POA, bad vs movement & shooting, weak PnR defense",
                "pace": "fast",
                "variance": "high",
                "shot_profile": {
                    "rim": "high",
                    "midrange": "medium",
                    "threes": "low"
                }
            }
        },

        "Clippers": {
            "strength": 60,
            "identity": {
                "offense": "iso/PnR heavy, midrange leaning, veteran shot-making",
                "defense": "aging switch defenders, inconsistent intensity",
                "pace": "slow",
                "variance": "high",
                "shot_profile": {
                    "rim": "low",
                    "midrange": "high",
                    "threes": "medium"
                }
            }
        }
    },

    # --- Guardrails / Safety Logic ---
    "guardrails": {
        "no_low_edge_bets": True,     # Skip if edge vs line is too small
        "must_pass_all_filters": True # All filters must greenlight before a bet is allowed
    }
}

# END OF CONFIG
