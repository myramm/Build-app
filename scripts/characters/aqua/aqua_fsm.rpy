init -1 python:
    M_aqua = Machine("aqua", default_loc=[[L_lair, L_lair, L_lair, L_lair]],
                     vars = {"sex speed": .175,
                             "tomb search": False,
                             "bell search": False,
                             "altar search": False,
                             "altar pass": False,
                             "treasure search": False,
                             "treasure pass": False,
                             "squid pass": False,
                             "maze pass": False,
                             "seasucc available": False,
                            },
    )

init -3 python:

    T_aqua_special_lure = Trigger()
    T_aqua_obituary_records = Trigger()
    T_aqua_tomb_engraving = Trigger()
    T_aqua_bell_engraving = Trigger()
    T_aqua_altar_puzzle_solve = Trigger()
    T_aqua_treasure_found = Trigger()
    T_aqua_treasure_unlocked = Trigger()
    T_aqua_lure_steal = Trigger()
    T_aqua_dive = Trigger()
    T_aqua_chase_fail = Trigger()
    T_aqua_squid_defeated = Trigger()
    T_aqua_maze_conquered = Trigger()
    T_aqua_lair_found = Trigger()
    T_aqua_friended = Trigger()
    T_aqua_mating_offer = Trigger()
    T_aqua_test_pass = Trigger()
    T_aqua_mated = Trigger()
    T_aqua_seasucc = Trigger()
    T_aqua_seasucc_fuck = Trigger()

init 1 python:

    S_aqua_start = State()
    S_aqua_boatsmith_search = State(_("Search for the holder of the golden compass"))
    S_aqua_graveyard_search = State(_("Search the graveyard for clues"))
    S_aqua_bell_search = State(_("Search the church bell for clues"))
    S_aqua_altar_search = State(_("Search the forest altar for clues"))
    S_aqua_treasure_search = State(_("Search the beach for the treasure"))
    S_aqua_treasure_unlock = State(_("Now you need to unlock the treasure chest"))
    S_aqua_trade = State(_("You need to trade Terry for the golden lure"))
    S_aqua_fishing = State(_("You might meet someone whilst fishing with the new lure"))
    S_aqua_chase = State(_("You need to chase after Aqua to get back your lure"))
    S_aqua_squid_gaurd = State(_("You need to fight off the squid guarding the lair"))
    S_aqua_maze = State(_("You need to traverse the maze to get into the lair"))
    S_aqua_lair = State(_("You have discovered the secret lair of Aqua"))
    S_aqua_found = State(_("You found Aqua after she stole your lure"))
    S_aqua_mating_proposal = State(_("You need to try to convince Aqua to take you as her mate"))
    S_aqua_valor_test = State(_("Aqua has given you a test of valor to become her mate"))
    S_aqua_mate = State(_("You can now mate with Aqua"))
    S_aqua_seasucc_intro = State(_("Aqua's pal and friend, SeaSucc"))
    S_aqua_seasucc_mushroom = State(_("SeaSucc wants a mushroom before he becomes your friend"))
    S_aqua_end = State(_("The end of Aqua's story"))


    S_aqua_start.add(T_aqua_special_lure, S_aqua_boatsmith_search)
    S_aqua_boatsmith_search.add(T_aqua_obituary_records, S_aqua_graveyard_search,
                                actions = ["set", "tomb search"]
                                )
    S_aqua_graveyard_search.add(T_aqua_tomb_engraving, S_aqua_bell_search,
                                actions = ["set", "bell search"]
                                )
    S_aqua_bell_search.add(T_aqua_bell_engraving, S_aqua_altar_search,
                           actions = ["set", "altar search"]
                           )
    S_aqua_altar_search.add(T_aqua_altar_puzzle_solve, S_aqua_treasure_search,
                            actions = ["set", "treasure search",
                                       "set", "altar pass"]
                            )
    S_aqua_treasure_search.add(T_aqua_treasure_found, S_aqua_treasure_unlock)
    S_aqua_treasure_unlock.add(T_aqua_treasure_unlocked, S_aqua_trade, 
                               actions = ["set", "treasure pass"]
                               )
    S_aqua_trade.add(T_terry_lure_trade, S_aqua_fishing)
    S_aqua_fishing.add(T_aqua_lure_steal, S_aqua_chase)
    S_aqua_chase.add(T_aqua_dive, S_aqua_squid_gaurd)
    S_aqua_squid_gaurd.add(T_aqua_squid_defeated, S_aqua_maze, 
                           actions = ["set", "squid pass"]
                           )
    S_aqua_squid_gaurd.add(T_aqua_chase_fail, S_aqua_chase)
    S_aqua_maze.add(T_aqua_maze_conquered, S_aqua_lair, 
                    actions = ["set", "maze pass"]
                    )
    S_aqua_maze.add(T_aqua_chase_fail, S_aqua_chase)
    S_aqua_lair.add(T_aqua_lair_found, S_aqua_found, actions = ["unlocklocation", L_lair])
    S_aqua_found.add(T_aqua_friended, S_aqua_mating_proposal)
    S_aqua_mating_proposal.add(T_aqua_mating_offer, S_aqua_valor_test)
    S_aqua_valor_test.add(T_aqua_test_pass, S_aqua_mate)
    S_aqua_mate.add(T_aqua_mated, S_aqua_seasucc_intro,
                    actions = ["set", "seasucc available",
                               'clear', ('player', 'is_virgin')]
                    )
    S_aqua_seasucc_intro.add(T_aqua_seasucc, S_aqua_seasucc_mushroom)
    S_aqua_seasucc_mushroom.add(T_aqua_seasucc_fuck, S_aqua_end, actions=["exec", A_mermaid.unlock])

    M_aqua.add(S_aqua_start, S_aqua_boatsmith_search, S_aqua_graveyard_search,
               S_aqua_bell_search, S_aqua_altar_search, S_aqua_treasure_search,
               S_aqua_treasure_unlock, S_aqua_trade, S_aqua_fishing, S_aqua_chase,
               S_aqua_squid_gaurd, S_aqua_maze, S_aqua_lair, S_aqua_found,
               S_aqua_mating_proposal, S_aqua_valor_test, S_aqua_mate,
               S_aqua_seasucc_intro, S_aqua_seasucc_mushroom, S_aqua_end)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
