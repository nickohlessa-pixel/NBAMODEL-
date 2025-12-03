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
#   - Player roles (starter / bench / out_of_rotation / injured_out / out)
#   - Notes (injuries, usage, matchups, trends)
#
# Future expansion:
#   - Auto-saving updates
#   - Tracking roles over time
#   - Minutes estimates
#   - Injury state
#   - Export/import roster packs
# ==========================================


ROSTERS = {

    # ==========================================
    # OKLAHOMA CITY THUNDER (USER CANON)
    # ==========================================
    "Oklahoma City Thunder": {
        "players": {
            "Shai Gilgeous-Alexander": {
                "role": "starter",
                "notes": "PG, 6-6, 195, superstar, MVP, key offensive driver"
            },
            "Ajay Mitchell": {
                "role": "bench",
                "notes": "SG, 6-4, 190, key rotational player"
            },
            "Cason Wallace": {
                "role": "bench",
                "notes": "SG, 6-3, 195, 6th man, key rotational player"
            },
            "Jaylin Williams": {
                "role": "bench",
                "notes": "PF, 6-9, 240, key rotational big man"
            },
            "Isaiah Hartenstein": {
                "role": "starter",
                "notes": "C, 7-0, 250, starting center, defensive hinge, rebounding threat"
            },
            "Chet Holmgren": {
                "role": "starter",
                "notes": "PF, 7-1, 208, scorer, shot blocker, versatility"
            },
            "Isaiah Joe": {
                "role": "bench",
                "notes": "SG, 6-4, 165"
            },
            "Chris Youngblood": {
                "role": "bench",
                "notes": "SG, 6-4, 221, two-way (TW)"
            },
            "Luguentz Dort": {
                "role": "starter",
                "notes": "SF, 6-4, 220, elite defender"
            },
            "Alex Caruso": {
                "role": "bench",
                "notes": "SG, 6-5, 186, key rotational player, elite defender"
            },
            "Brooks Barnhizer": {
                "role": "out_of_rotation",
                "notes": "SG, 6-5, 230, two-way (TW)"
            },
            "Branden Carlson": {
                "role": "out_of_rotation",
                "notes": "C, 7-0, 220, two-way (TW)"
            },
            "Ousmane Dieng": {
                "role": "bench",
                "notes": "C, 6-9, 185"
            },
            "Aaron Wiggins": {
                "role": "bench",
                "notes": "SG, 6-5, 190, key rotational player"
            },
            "Kenrich Williams": {
                "role": "bench",
                "notes": "PF, 6-7, 210"
            },
            "Jalen Williams": {
                "role": "starter",
                "notes": "SG, 6-5, 211, 2nd best player on the team, offensive and defensive motor"
            },
            "Nikola Topić": {
                "role": "out",
                "notes": "PG, 6-6, 200, OUT"
            },
            "Thomas Sorber": {
                "role": "out_of_rotation",
                "notes": "C, 6-9, 250"
            }
        },
        "injuries": {},
        "notes": ""
    },

    # ==========================================
    # KNICKS (USER CANON)
    # ==========================================
    "Knicks": {
        "players": {
            "Karl-Anthony Towns": {
                "role": "starter",
                "notes": "C, 7-0, 248, key player, superstar, shooter, spacing big"
            },
            "Mikal Bridges": {
                "role": "starter",
                "notes": "SF, 6-6, 209, elite 3&D, key player"
            },
            "Jordan Clarkson": {
                "role": "starter",
                "notes": "SG, 6-5, 194, key rotational player, currently starting"
            },
            "Josh Hart": {
                "role": "starter",
                "notes": "SF, 6-5, 215, key rotational player"
            },
            "Jalen Brunson": {
                "role": "starter",
                "notes": "PG, 6-2, 190, elite superstar, primary creator, heavy on-ball usage"
            },
            "Guerschon Yabusele": {
                "role": "bench",
                "notes": "C/F, 6-7, physical big, bench depth"
            },
            "Miles McBride": {
                "role": "bench",
                "notes": "SG/guard, 6-2, 195, key rotational 3&D player"
            },
            "Tyler Kolek": {
                "role": "bench",
                "notes": "PG, 6-2, 195, born March 27 2001, rookie, George Mason/Marquette"
            },
            "Mitchell Robinson": {
                "role": "bench",
                "notes": "C, 7-0, 240, first big off bench, rim protector"
            },
            "Mohamed Diawara": {
                "role": "bench",
                "notes": "SF, 6-9, 225, rookie, born April 29 2005, France"
            },
            "Landry Shamet": {
                "role": "injured_out",
                "notes": "SG, 6-5, 190, 6th man shooter, currently hurt"
            },
            "OG Anunoby": {
                "role": "injured_out",
                "notes": "PF/F, 6-7, 240, key starter-level player, currently injured"
            },
            "Ariel Hukporti": {
                "role": "out_of_rotation",
                "notes": "C, 7-0, 246, born April 11 2002, depth big"
            },
            "Pacome Dadiet": {
                "role": "out_of_rotation",
                "notes": "SG/wing, 6-9, 210, born July 27 2005, rookie, France"
            },
            "Tosan Evbuomwan": {
                "role": "out_of_rotation",
                "notes": "SF, 6-8, 217, two-way, born February 16 2001, Princeton"
            },
            "Trey Jemison": {
                "role": "out_of_rotation",
                "notes": "C, 6-10, 270, two-way, born November 28 1999, Clemson/UAB"
            },
            "P.J. Tucker": {
                "role": "out_of_rotation",
                "notes": "F, 6-5, 245, born May 5 1985, defensive vet, 14th year"
            },
            "Kevin McCullar Jr.": {
                "role": "out_of_rotation",
                "notes": "SF, 6-6, 210, two-way wing"
            }
        },
        "injuries": {},
        "notes": "User-defined Knicks roster for 2025-26 universe."
    },

    # ==========================================
    # HEAT (USER CANON)
    # ==========================================
    "Heat": {
        "players": {
            "Kel'el Ware": {
                "role": "starter",
                "notes": "C, 7-0, 230, starter, key big man"
            },
            "Davion Mitchell": {
                "role": "starter",
                "notes": "PG, 6-0, 202, starter, ball stopping defensive anchor"
            },
            "Pelle Larsson": {
                "role": "bench",
                "notes": "SG, 6-5, 215, bench, rotational player"
            },
            "Dru Smith": {
                "role": "bench",
                "notes": "SG, 6-2, 203, bench, rotational player"
            },
            "Jaime Jaquez Jr.": {
                "role": "bench",
                "notes": "SF, 6-6, 225, bench, key rotational player, 6th man"
            },
            "Simone Fontecchio": {
                "role": "bench",
                "notes": "SF, 6-7, 209, bench, rotational player, floor spacing shooter"
            },
            "Andrew Wiggins": {
                "role": "starter",
                "notes": "SF, 6-6, 197, starter, veteran leadership"
            },
            "Norman Powell": {
                "role": "starter",
                "notes": "SG, 6-3, 215, starter, offensive engine, scoring threat"
            },
            "Nikola Jović": {
                "role": "bench",
                "notes": "PF, 6-10, 205, bench, key rotational player"
            },
            "Bam Adebayo": {
                "role": "starter",
                "notes": "C, 6-9, 255, starter, primary offensive weapon"
            },
            "Keshad Johnson": {
                "role": "bench",
                "notes": "SF, 6-6, 225, bench"
            },
            "Tyler Herro": {
                "role": "starter",
                "notes": "SG, 6-5, 195, starter, primary offensive weapon"
            },
            "Jahmir Young": {
                "role": "out_of_rotation",
                "notes": "PG, 6-0, 185, two-way (TW), out of rotation"
            },
            "Myron Gardner": {
                "role": "out_of_rotation",
                "notes": "SF, 6-5, 220, two-way (TW), out of rotation"
            },
            "Kasparas Jakucionis": {
                "role": "out_of_rotation",
                "notes": "PG, 6-5, 200, out of rotation"
            },
            "Vladislav Goldin": {
                "role": "out_of_rotation",
                "notes": "C, 7-0, 250, two-way (TW), out of rotation"
            },
            "Terry Rozier": {
                "role": "out",
                "notes": "PG, 6-1, 190, out indefinitely"
            }
        },
        "injuries": {},
        "notes": ""
    },

    # ==========================================
    # HORNETS (USER CANON)
    # ==========================================
    "Hornets": {
        "players": {
            "Miles Bridges": {
                "role": "starter",
                "notes": "PF, 6-7, 225, born March 21 1998, Michigan State"
            },
            "Kon Knueppel": {
                "role": "starter",
                "notes": "SF, 6-6, 215, born August 3 2005, rookie, Duke"
            },
            "Ryan Kalkbrenner": {
                "role": "starter",
                "notes": "C, 7-1, 256, born January 17 2002, rookie, Creighton"
            },
            "LaMelo Ball": {
                "role": "starter",
                "notes": "PG, 6-7, 180, born August 22 2001, 5th year"
            },
            "Brandon Miller": {
                "role": "starter",
                "notes": "SF, 6-7, 200, born November 22 2002, 2nd year, Alabama"
            },
            "Moussa Diabaté": {
                "role": "bench",
                "notes": "C, 6-10, 210, born January 21 2002, 3rd year, Michigan"
            },
            "Sion James": {
                "role": "bench",
                "notes": "SG, 6-5, 220, born December 4 2002, rookie, Tulane/Duke"
            },
            "Collin Sexton": {
                "role": "bench",
                "notes": "SG, 6-3, 190, born January 4 1999, 7th year, Alabama"
            },
            "Tre Mann": {
                "role": "bench",
                "notes": "PG, 6-4, 178, born February 3 2001, 4th year, Florida"
            },
            "Tidjane Salaün": {
                "role": "bench",
                "notes": "PF, 6-10, 207, born August 10 2005, rookie"
            },
            "Liam McNeeley": {
                "role": "out_of_rotation",
                "notes": "SF, 6-7, 210, born October 10 2005, rookie, UConn"
            },
            "Pat Connaughton": {
                "role": "out_of_rotation",
                "notes": "SG, 6-5, 209, born January 6 1993, 10th year, Notre Dame"
            },
            "KJ Simpson": {
                "role": "out_of_rotation",
                "notes": "PG, 6-2, 189, born August 8 2002, two-way, Colorado"
            },
            "Mason Plumlee": {
                "role": "out_of_rotation",
                "notes": "C, 7-0, 254, born March 5 1990, 12th year, Duke"
            },
            "Drew Peterson": {
                "role": "out_of_rotation",
                "notes": "PF, 6-8, 205, born November 9 1999, two-way, Rice/USC"
            },
            "Antonio Reeves": {
                "role": "out_of_rotation",
                "notes": "SG, 6-5, 205, born November 20 2000, two-way, Illinois State/Kentucky"
            },
            "Josh Green": {
                "role": "injured_out",
                "notes": "SG, 6-6, 200, born November 16 2000, 5th year, Arizona, OUT injured"
            },
            "Grant Williams": {
                "role": "injured_out",
                "notes": "PF, 6-7, 236, born November 30 1998, 6th year, Tennessee, OUT injured"
            }
        },
        "injuries": {},
        "notes": "User-defined Hornets roster for 2025-26 universe."
    },

    # ==========================================
    # MAGIC – SHELL (TO BE POPULATED BY USER)
    # ==========================================
    "Magic": {
        "players": {},
        "injuries": {},
        "notes": "User will populate Magic roster."
    },

    # ==========================================
    # NUGGETS – SHELL (TO BE POPULATED BY USER)
    # ==========================================
    "Nuggets": {
        "players": {},
        "injuries": {},
        "notes": "User will populate Nuggets roster."
    },

    # ==========================================
    # CLIPPERS – SHELL (TO BE POPULATED BY USER)
    # ==========================================
    "Clippers": {
        "players": {},
        "injuries": {},
        "notes": "User will populate Clippers roster."
    }
}

# END OF ROSTERS FILE
