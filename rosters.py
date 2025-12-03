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
#   - Player roles (starter / bench / OOR / out / injured_out)
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
        "players": [
            {"name": "Shai Gilgeous-Alexander", "role": "starter", "notes": "PG, 6-6, 195, superstar, MVP, key offensive driver"},
            {"name": "Ajay Mitchell", "role": "bench", "notes": "SG, 6-4, 190, key rotational player"},
            {"name": "Cason Wallace", "role": "bench", "notes": "SG, 6-3, 195, 6th man, key rotational player"},
            {"name": "Jaylin Williams", "role": "bench", "notes": "PF, 6-9, 240, key rotational big man"},
            {"name": "Isaiah Hartenstein", "role": "starter", "notes": "C, 7-0, 250, starting center, defensive hinge, rebounding threat"},
            {"name": "Chet Holmgren", "role": "starter", "notes": "PF, 7-1, 208, scorer, shot blocker, versatility"},
            {"name": "Isaiah Joe", "role": "bench", "notes": "SG, 6-4, 165"},
            {"name": "Chris Youngblood", "role": "bench", "notes": "SG, 6-4, 221, (TW)"},
            {"name": "Luguentz Dort", "role": "starter", "notes": "SF, 6-4, 220, elite defender"},
            {"name": "Alex Caruso", "role": "bench", "notes": "SG, 6-5, 186, key rotational player, elite defender"},
            {"name": "Brooks Barnhizer", "role": "OOR", "notes": "SG, 6-5, 230, (TW)"},
            {"name": "Branden Carlson", "role": "OOR", "notes": "C, 7-0, 220, (TW)"},
            {"name": "Ousmane Dieng", "role": "bench", "notes": "C, 6-9, 185"},
            {"name": "Aaron Wiggins", "role": "bench", "notes": "SG, 6-5, 190, key rotational player"},
            {"name": "Kenrich Williams", "role": "bench", "notes": "PF, 6-7, 210"},
            {"name": "Jalen Williams", "role": "starter", "notes": "SG, 6-5, 211, 2nd best player on the team, offensive and defensive motor"},
            {"name": "Nikola Topić", "role": "out", "notes": "PG, 6-6, 200, OUT"},
            {"name": "Thomas Sorber", "role": "OOR", "notes": "C, 6-9, 250"}
        ],
        "injuries": {},
        "notes": []
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
        "notes": "User-defined Knicks roster for 2025-26 universe."
    },

    # ==========================================
    # MIAMI HEAT (USER CANON)
    # ==========================================
    "Miami Heat": {
        "players": [
            {"name": "Kel'el Ware", "role": "starter", "notes": "C, 7-0, 230, starter, key big man"},
            {"name": "Davion Mitchell", "role": "starter", "notes": "PG, 6-0, 202, starter, ball stopping defensive anchor"},
            {"name": "Pelle Larsson", "role": "bench", "notes": "SG, 6-5, 215, bench, rotational player"},
            {"name": "Dru Smith", "role": "bench", "notes": "SG, 6-2, 203, bench, rotational player"},
            {"name": "Jaime Jaquez Jr.", "role": "bench", "notes": "SF, 6-6, 225, bench, key rotational player, 6th man"},
            {"name": "Simone Fontecchio", "role": "bench", "notes": "SF, 6-7, 209, bench, rotational player, floor spacing shooter"},
            {"name": "Andrew Wiggins", "role": "starter", "notes": "SF, 6-6, 197, starter, veteran leadership"},
            {"name": "Norman Powell", "role": "starter", "notes": "SG, 6-3, 215, starter, offensive engine, scoring threat"},
            {"name": "Nikola Jović", "role": "bench", "notes": "PF, 6-10, 205, bench, key rotational player"},
            {"name": "Bam Adebayo", "role": "starter", "notes": "C, 6-9, 255, starter, primary offensive weapon"},
            {"name": "Keshad Johnson", "role": "bench", "notes": "SF, 6-6, 225, bench"},
            {"name": "Tyler Herro", "role": "starter", "notes": "SG, 6-5, 195, starter, primary offensive weapon"},
            {"name": "Jahmir Young", "role": "OOR", "notes": "(TW)"},
            {"name": "Myron Gardner", "role": "OOR", "notes": "(TW)"},
            {"name": "Kasparas Jakucionis", "role": "OOR", "notes": ""},
            {"name": "Vladislav Goldin", "role": "OOR", "notes": "(TW)"},
            {"name": "Terry Rozier", "role": "out", "notes": "PG, 6-1, 190, out indefinitely"}
        ],
        "injuries": {},
        "notes": []
    },

    # ==========================================
    # MAGIC (USER CANON)
    # ==========================================
    "Magic": {
        "players": [
            {"name": "Franz Wagner", "role": "starter", "notes": "SF, 6-10, 220, offensive engine"},
            {"name": "Desmond Bane", "role": "starter", "notes": "SG, 6-6, 215, 3 point floor spacer"},
            {"name": "Anthony Black", "role": "bench", "notes": "PG, 6-7, 200, 6th man, scorer"},
            {"name": "Tristan Da Silva", "role": "bench", "notes": "SF, 6-8, 217, key rotational player, glue guy"},
            {"name": "Tyus Jones", "role": "bench", "notes": "PG, 6-0, 196, backup point guard"},
            {"name": "Wendell Carter Jr.", "role": "starter", "notes": "C, 6-10, 270, defense, rebounds"},
            {"name": "Goga Bitadze", "role": "bench", "notes": "C, 6-11, 250, backup center"},
            {"name": "Jonathan Isaac", "role": "OOR", "notes": "PF, 6-10, 230, out of rotation"},
            {"name": "Jalen Suggs", "role": "starter", "notes": "PG, 6-5, 205, defensive anchor"},
            {"name": "Jett Howard", "role": "bench", "notes": "SF, 6-8, 215"},
            {"name": "Paolo Banchero", "role": "starter", "notes": "PF, 6-10, 250, elite offensive engine"},
            {"name": "Noah Penda", "role": "bench", "notes": "SF, 6-7, 215, rotational player"},
            {"name": "Jase Richardson", "role": "bench", "notes": "SG, 6-1, 180, rotational player"},
            {"name": "Jamal Cain", "role": "OOR", "notes": "SF, 6-7, 191, (TW), out of rotation"},
            {"name": "Orlando Robinson", "role": "OOR", "notes": "C, 6-10, 235, (TW), out of rotation"},
            {"name": "Moritz Wagner", "role": "out", "notes": "C, 6-11, 245, OUT recovering from ACL surgery"},
            {"name": "Colin Castleton", "role": "OOR", "notes": "C, 6-10, 250, (TW), out of rotation"}
        ],
        "injuries": {},
        "notes": "User-defined Magic roster for 2025-26 universe."
    },

    # ==========================================
    # NUGGETS (USER CANON)
    # ==========================================
    "Nuggets": {
        "players": [
            {"name": "Nikola Jokić", "role": "starter", "notes": "C, 6-11, 284, MVP, offensive engine, passer, scorer, rebounder"},
            {"name": "Tim Hardaway Jr.", "role": "bench", "notes": "SG, 6-5, 205, key rotational player, 3 & D"},
            {"name": "Peyton Watson", "role": "bench", "notes": "SF, 6-8, 200, key rotational player, 6th man"},
            {"name": "Jonas Valančiūnas", "role": "bench", "notes": "C, 6-11, 265, backup center"},
            {"name": "Bruce Brown", "role": "bench", "notes": "SG, 6-4, 202, key rotational player"},
            {"name": "Jamal Murray", "role": "starter", "notes": "PG, 6-4, 215, offensive engine, scorer"},
            {"name": "Cameron Johnson", "role": "starter", "notes": "SF, 6-8, 210, floor spacing stretch big"},
            {"name": "Spencer Jones", "role": "bench", "notes": "SF, 6-7, (TW), rotational player"},
            {"name": "Aaron Gordon", "role": "starter", "notes": "PF, 6-8, 235, scorer, rebounder, defensive anchor"},
            {"name": "Christian Braun", "role": "starter", "notes": "SG, 6-6, 220, floor spacer, defender"},
            {"name": "Zeke Nnaji", "role": "OOR", "notes": "PF, 6-10, 240, bench, out of rotation"},
            {"name": "Julian Strawther", "role": "OOR", "notes": "SG, 6-6, 205, bench, out of rotation"},
            {"name": "Jalen Pickett", "role": "OOR", "notes": "SG, 6-2, 202, bench, out of rotation"},
            {"name": "Hunter Tyson", "role": "OOR", "notes": "PF, 6-8, 215, bench, out of rotation"},
            {"name": "DaRon Holmes", "role": "OOR", "notes": "PF, 6-9, 225, bench, out of rotation"},
            {"name": "Curtis Jones", "role": "OOR", "notes": "SG, 6-3, 195, (TW), bench, out of rotation"},
            {"name": "Tamar Bates", "role": "OOR", "notes": "SG, 6-4, 195, (TW), bench, out of rotation"}
        ],
        "injuries": {},
        "notes": "User-defined Nuggets roster for 2025-26 universe."
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
        "notes": "User-defined Hornets roster for 2025-26 universe."
    },

    # ==========================================
    # CLIPPERS (USER CANON)
    # ==========================================
    "Clippers": {
        "players": [
            {"name": "Ivica Zubac", "role": "starter", "notes": "C, 7-0, 240, defensive anchor, rebounder, secondary scorer"},
            {"name": "John Collins", "role": "starter", "notes": "PF, 6-9, 226, defender, scorer"},
            {"name": "Kris Dunn", "role": "starter", "notes": "PG, 6-3, 205"},
            {"name": "Nicolas Batum", "role": "bench", "notes": "PF, 6-7, key rotational player"},
            {"name": "James Harden", "role": "starter", "notes": "PG, 6-5, 220, MVP, offensive engine, scorer, assists, rebounder"},
            {"name": "Brook Lopez", "role": "bench", "notes": "C, 7-1, 282, rotational player"},
            {"name": "Cam Christie", "role": "bench", "notes": "SG, 6-5, 190, rotational player"},
            {"name": "Kobe Brown", "role": "bench", "notes": "PF, 6-7, 250, rotational player"},
            {"name": "Derrick Jones Jr.", "role": "bench", "notes": "SF, 6-6, 210, key rotational player"},
            {"name": "Kobe Sanders", "role": "OOR", "notes": "SG, 6-8, 207, (TW), out of rotation"},
            {"name": "Kawhi Leonard", "role": "starter", "notes": "SF, 6-6, 225, June 29, 1991, starter, defensive anchor, scorer"},
            {"name": "Yanic Konan Niederhauser", "role": "OOR", "notes": "C, 6-11, 242, out of rotation"},
            {"name": "Bogdan Bogdanović", "role": "bench", "notes": "SG, 6-5, 225, 6th man, scorer, 3pt floor spacer"},
            {"name": "Jahmyl Telfort", "role": "OOR", "notes": "PF, 6-7, 225, (TW), out of rotation"},
            {"name": "Bradley Beal", "role": "out", "notes": "SG, 6-4, 207, injured, out for the season"},
            {"name": "Jordan Miller", "role": "OOR", "notes": "SF, 6-5, 194, (TW), out of rotation"}
        ],
        "injuries": {},
        "notes": "User-defined Clippers roster for 2025-26 universe."
    }
}

# END OF ROSTERS FILE
