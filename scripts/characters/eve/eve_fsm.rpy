init -1 python:
    M_eve = Machine("eve", default_loc = [[L_school_frenchclassroom, L_school_righthallway, L_park, L_tattooparlor_bedroom],
                                          [L_tattooparlor_bedroom, L_park, L_park, L_tattooparlor_bedroom]
                                          ],
                    vars = {"first park visit": True,
                            "first rap battle": True,
                            "failed_bridget_test": False,
                            "talked_tuuku_douches": False,
                            "sex speed": 0.4,
                            "biggus_dickus": '_alt',
                            "party_in_progress": False,
                            "party_in_progress_apartment_first": True,
                            "odette_depressed": False,
                            "make_up_go_to_mall_first": True,
                            "HJ_1st_time": True,
                            "69_1st_time": True,
                            "sex_front_1st_time": True,
                            "sex_back_1st_time": True,
                            "had_sex_with_odette": False,
                            "sex_front_anal": False,
                            "shower": False,
                            },
                    pregnancy_chance=0.2,
                    can_birth_twins=False,
                    default_pregnancy_schedule={
                        "":                LocationSchedule([[L_tattooparlor_bedroom] * 4]),
                        "_pregnant_bump":  LocationSchedule([[L_tattooparlor_bedroom] * 4]),
                        "_pregnant_belly": LocationSchedule([[L_tattooparlor_bedroom, L_tattooparlor_bedroom, (L_tattooparlor_bedroom, L_tattooparlor_bathroom), L_tattooparlor_bedroom]]),
                        "_baby_twins":     LocationSchedule([[L_tattooparlor_bedroom] * 4]),
                        "_baby_girl":      LocationSchedule([[L_tattooparlor_bedroom] * 4]),
                        "_baby_boy":       LocationSchedule([[L_tattooparlor_bedroom] * 4]),
                       },
                    )
    M_eve.set_priority(1)

init -3 python:

    T_eve_park_hangout = Trigger()
    T_eve_bullied_by_douches = Trigger()
    T_eve_caf_lunch = Trigger()
    T_eve_ross_argument = Trigger()
    T_eve_auditorium_bummed = Trigger()
    T_eve_visited_tattoo_shop = Trigger()
    T_eve_visited_garage = Trigger()
    T_eve_visited_roof = Trigger()
    T_eve_visited_apartment = Trigger()
    T_eve_visited_bedroom = Trigger()
    T_eve_big_sis_problem = Trigger()
    T_eve_big_sis_checked_garage = Trigger()
    T_eve_big_sis_talked_to_odette = Trigger()
    T_eve_big_sis_checked_apartment = Trigger()
    T_eve_roxxy_bullied = Trigger()
    T_eve_dress_code_change = Trigger()
    T_eve_talked_to_smith_dress_code = Trigger()
    T_eve_found_helping_teacher = Trigger()
    T_eve_announced_bridget_help = Trigger()
    T_eve_distract_grace = Trigger()
    T_eve_distracted_grace = Trigger()
    T_eve_bathroom_mishap = Trigger()
    T_eve_bathroom_event_left = Trigger()
    T_eve_apologized = Trigger()
    T_eve_pranked_roxxy = Trigger()
    T_eve_douches_prank_plan = Trigger()
    T_eve_pranked_douches = Trigger()
    T_eve_police_trouble_resolved = Trigger()
    T_eve_upset_pot = Trigger()
    T_eve_pot_cheerup = Trigger()
    T_eve_pot_entered_apartment = Trigger()
    T_eve_pot_cheered_up = Trigger()
    T_eve_voyeurism_meetup = Trigger()
    T_eve_voyeurism_follow_roof = Trigger()
    T_eve_voyeurism_follow_tent = Trigger()
    T_eve_trap_revealed = Trigger()
    T_eve_got_detention = Trigger()
    T_eve_bike_breakdown_started = Trigger()
    T_eve_bike_breakdown_check_bike = Trigger()
    T_eve_bike_breakdown_repair_pass = Trigger()
    T_eve_bike_breakdown_repair_fail = Trigger()
    T_eve_bike_breakdown_repaired_bike = Trigger()
    T_eve_talked_to_grace = Trigger()
    T_eve_talked_to_eve = Trigger()
    T_eve_woke_odette = Trigger()
    T_eve_woke_grace = Trigger()
    T_eve_mall_fliers_hung = Trigger()
    T_eve_library_fliers_hung = Trigger()
    T_eve_park_fliers_hung = Trigger()
    T_eve_tattoo_shop_crowded = Trigger()
    T_eve_took_care_clients = Trigger()
    T_eve_party_started = Trigger()
    T_eve_party_spoke_to_grace = Trigger()
    T_eve_party_spoke_to_jenny = Trigger()
    T_eve_party_spoke_to_odette = Trigger()
    T_eve_party_end = Trigger()
    T_eve_make_up_mall = Trigger()
    T_eve_bought_candles_chocolate = Trigger()
    T_eve_got_wine = Trigger()
    T_eve_picked_up_lasagna = Trigger()
    T_eve_dressed_table = Trigger()
    T_eve_talked_about_grace_odette = Trigger()
    T_eve_had_sixtynine = Trigger()
    T_eve_had_sexy_time = Trigger()

init python:


    S_eve_start = State(_("I should get to school..."))

    S_eve_park_hangout = State(_("Eve asked me to hang out at the {b}Park{/b} with her later."))

    S_eve_cafeteria_troubles = State(_("I should check on Eve at the school."), delay=2)

    S_eve_ross_argument_delay = State(_("I should wait for a few days."))
    S_eve_ross_argument = State(_("I should check in on Eve at school."))
    S_eve_auditorium_bummed = State(_("I saw Eve running away to the Auditorium."))

    S_eve_visit_tattoo_shop = State(_("Eve asked me to come by her house, north of SummerVille"))
    S_eve_visit_garage = State(_("Eve told me to follow her to the garage."))
    S_eve_visit_roof = State(_("I should follow her to the roof."))
    S_eve_visit_apartment = State(_("She went into her apartment. I should follow her."))
    S_eve_visit_bedroom = State(_("She went into her bedroom."))

    S_eve_big_sister_problems = State(_("I should check on her at school."), delay=3)
    S_eve_big_sis_check_garage = State(_("Eve was headed to the garage."))
    S_eve_big_sis_talk_odette = State(_("I should check on Odette in Eve's garage."))
    S_eve_big_sis_check_apartment = State(_("Eve is headed for her place upstairs."))

    S_eve_roxxy_bullying_prepare = State(_("Maybe I should wait a few days..."), delay=1)
    S_eve_roxxy_bullying = State(_("I should check on Eve at School."))
    S_eve_roxxy_bullying_upset = State(_("Roxxy was harsh on her. I bet she's in the Assembly Hall."))
    S_eve_school_dress_code = State(_("The dress code for the school has changed. I need to talk to Mrs. Smith..."))

    S_eve_dress_code_ask_teachers = State(_("Mrs. Smith wasn't any help. I need to ask the teachers for help on this."))
    S_eve_bridgets_help = State(_("Coach bridget agreed to help, I should tell Eve the good news."))
    S_eve_ask_distract_grace = State(_("Eve asked me to meet her at the tattoo parlor."))
    S_eve_distract_grace = State(_("Eve asked me to distract her sister."))
    S_eve_bathroom_break = State(_("I need to go to the bathroom, it's right through the bedroom."))
    S_eve_bathroom_embarassed = State(_("Well, that was awkward, I should leave now."))

    S_eve_apologize = State(_("I should find Eve at the School, and apologize to her."), delay=1)
    S_eve_pranking_roxxy = State(_("I heard her in the Left Hallway, I should go apologize."))
    S_eve_pranking_douches = State(_("Eve asked me to meet her at the Park this evening."))

    S_eve_tuuku_with_douches = State(_("Eve asked me to stink up the park douches' backpacks."))

    S_eve_police_trouble = State(_("Eve is in deep trouble with the police. I should talk to her tomorrow."))

    S_eve_school_stinker = State(_("I should look for Eve at school."))
    S_eve_upset_pot = State(_("Chad got an earful! No trace of Eve, though... Maybe at the tattoo place?"))
    S_eve_pot_look_for_eve = State(_("According to Grace, Eve is in her bedroom, I should cheer her up."))
    S_eve_pot_cheerup = State(_("According to Grace, Eve is in her bedroom, I should cheer her up."))

    S_eve_voyeurism_start = State(_("I should meet up with Eve at the school."), delay=2)
    S_eve_voyeurism_meetup = State(_("Eve asked me to come to the tattoo parlor in the evening."))
    S_eve_voyeurism_follow_roof = State(_("I should follow her to the roof."))

    S_eve_voyeurism_follow_tent = State(_("She wants to talk to me in the tent."))

    S_eve_detention = State(_("I should talk to her at school."), delay=1)

    S_eve_bike_breakdown_start = State(_("I should check on Eve at school."), delay=1)
    S_eve_bike_breakdown_check_bike = State(_("I should check out that bike Grace is working on this weekend."))
    S_eve_bike_breakdown_repair = State(_("Grace is having some trouble with the repairs, maybe I could help?"))
    S_eve_bike_breakdown_repair_again = State(_("I should train a bit, and attempt these repairs again..."))
    S_eve_bike_breakdown_start_repair = State(_("I should talk to Eve about that bike."))

    S_eve_talk_to_girls = State(_("I should probably talk to either Grace or Eve."))
    S_eve_talked_to_eve = State(_("I should probably talk to Grace now."))
    S_eve_talked_to_grace = State(_("I should probably talk to Eve now."))

    S_eve_clients_hangover_wakeup = State(delay=1)
    S_eve_clients_check_shop = State(_("I should check on Eve and Grace at the tattoo shop."))
    S_eve_clients_wake_up_grace = State(_("Odette asked me to wake up Grace. Gently."))
    S_eve_clients_mall_fliers = State(_("Eve and I have to go to the mall to advertise for Sugar Tats"))
    S_eve_clients_library_fliers = State(_("Eve and I have to go to the library for advertisement now."))
    S_eve_clients_park_fliers = State(_("Eve and I need to advertise in the park."))
    S_eve_clients_tattooshop_crowd = State(_("We should go back to the tattoo parlor, see if it worked."))
    S_eve_clients_take_care_clients = State(_("Now that's a crowd! Grace probably needs help inside."))

    S_eve_party_start = State(_("I should check on the party at Eve's tattoo parlor on Saturday evening."), delay=1)
    S_eve_party_speak_to_grace = State(_("I should check on Grace."))
    S_eve_party_speak_to_jenny = State(_("Grace asked me to check on Odette on the roof."))
    S_eve_party_speak_to_odette = State(_("Grace asked me to check on Odette on the roof."))
    S_eve_party_speak_to_tuuku = State(_("Odette asked me to find Tuuku outside and let him know his plants are being disturbed."))

    S_eve_make_up_grace_upset = State(_("Grace is upset at Odette after the party. I should check on her."), delay=1)
    S_eve_make_up_go_to_mall = State(_("Odette needs Candles and Chocolates for her surprise dinner."))
    S_eve_make_up_extort_tuuku = State(_("I should go back to the tattoo parlor and chat with Tuuku about that wine."))
    S_eve_make_up_pick_up_lasagna = State(_("I need to pick up some lasagna from Tony's"))
    S_eve_make_up_dress_table = State(_("Time to bring everything back and dress the table."))

    S_eve_lesbians_aftermath = State(_("I should get some news from Eve at the School."))

    S_eve_six6nine9_time = State(_("I should check on Eve, at her place tonight."))
    S_eve_sexy_time = State(_("I should talk to Eve this evening, in her bedroom."))

    S_eve_end = State()


    S_eve_start.add(T_eve_park_hangout, S_eve_park_hangout, actions=["location", {"place":L_park},
                                                                     "force", {"tod": 2}])

    S_eve_park_hangout.add(T_eve_bullied_by_douches, S_eve_cafeteria_troubles, actions=["location", {"place": L_school_cafeteria},
                                                                                        "force", {"tod": [0, 1]},
                                                                                        'setdefaultloc', ('park_douches', [[L_NULL, L_NULL, L_park, L_NULL]])])
    S_eve_cafeteria_troubles.add(T_eve_caf_lunch, S_eve_ross_argument_delay, actions=["unforce", None])

    S_eve_ross_argument_delay.add(T_all_sleep, S_eve_ross_argument,
                            actions=["location", {"place": L_school_righthallway},
                                     "force", {"tod": [0, 1]}])
    S_eve_ross_argument.add(T_eve_ross_argument, S_eve_auditorium_bummed,
                            actions=["location", {"place": L_school_assemblyhall},
                                     "force", {"tod": [0, 1]}])
    S_eve_auditorium_bummed.add(T_eve_auditorium_bummed, S_eve_visit_tattoo_shop,
                            actions=["unforce", None,
                                     "unlocklocation", L_tattooparlor,
                                     "unlocklocation", L_tattooparlor_garage])

    S_eve_visit_tattoo_shop.add(T_eve_visited_tattoo_shop, S_eve_visit_garage)
    S_eve_visit_garage.add(T_eve_visited_garage, S_eve_visit_roof)
    S_eve_visit_roof.add(T_eve_visited_roof, S_eve_visit_apartment)
    S_eve_visit_apartment.add(T_eve_visited_apartment, S_eve_visit_bedroom)
    S_eve_visit_bedroom.add(T_eve_visited_bedroom, S_eve_big_sister_problems,
                            actions=["setcantalk", {"odette": [True, True, True, False]}])

    S_eve_big_sister_problems.add(T_eve_big_sis_problem, S_eve_big_sis_check_garage)
    S_eve_big_sis_check_garage.add(T_eve_big_sis_checked_garage, S_eve_big_sis_talk_odette)
    S_eve_big_sis_talk_odette.add(T_eve_big_sis_talked_to_odette, S_eve_big_sis_check_apartment)
    S_eve_big_sis_check_apartment.add(T_eve_big_sis_checked_apartment, S_eve_roxxy_bullying_prepare)

    S_eve_roxxy_bullying_prepare.add(T_all_sleep, S_eve_roxxy_bullying,
                            actions=["location", {"place": L_NULL},
                                     "force", {"tod": [0, 1]}])

    S_eve_roxxy_bullying.add(T_eve_roxxy_bullied, S_eve_roxxy_bullying_upset,
                            actions=["location", {"place": L_school_assemblyhall},
                                     "force", {"tod": [0, 1]}])
    S_eve_roxxy_bullying_upset.add(T_eve_dress_code_change, S_eve_school_dress_code,
                            actions=["unforce", None])
    S_eve_school_dress_code.add(T_eve_talked_to_smith_dress_code, S_eve_dress_code_ask_teachers)
    S_eve_dress_code_ask_teachers.add(T_eve_found_helping_teacher, S_eve_bridgets_help)
    S_eve_bridgets_help.add(T_eve_announced_bridget_help, S_eve_ask_distract_grace)
    S_eve_ask_distract_grace.add(T_eve_distract_grace, S_eve_distract_grace,
                            actions=["location", ["grace", {"place":L_tattooparlor_apartment}],
                                     "force", ["grace", {"flag": True}]])
    S_eve_distract_grace.add(T_eve_distracted_grace, S_eve_bathroom_break)
    S_eve_bathroom_break.add(T_eve_bathroom_mishap, S_eve_bathroom_embarassed,
                             actions=('set', ['player', 'jerk eve']))
    S_eve_bathroom_embarassed.add(T_eve_bathroom_event_left, S_eve_apologize,
                            actions=["unforce", "grace",
                                     "location", {"place": L_school_lefthallway},
                                     "force", {"tod": [0,1]}])
    S_eve_apologize.add(T_eve_apologized, S_eve_pranking_roxxy)
    S_eve_pranking_roxxy.add(T_eve_pranked_roxxy, S_eve_pranking_douches,
                            actions=["location", {"place": L_park},
                                     "force", {"flag": [False, False, True, False]}])
    S_eve_pranking_douches.add(T_eve_douches_prank_plan, S_eve_tuuku_with_douches,
                            actions=["unforce", None,
                                     "location", {"place": L_NULL},
                                     "force", {"tod": 2}])
    S_eve_tuuku_with_douches.add(T_eve_pranked_douches, S_eve_police_trouble,
                            actions=["unforce", None,
                                     "location", {"place": L_police_front},
                                     "force", {"flag": True},
                                     "unlocklocation", L_police_front])
    S_eve_police_trouble.add(T_eve_police_trouble_resolved, S_eve_school_stinker,
                            actions=["location", {"place": L_NULL},
                                     "location", ["grace", {"place":L_tattooparlor_interior}],
                                     "location", ["odette", {"place":L_tattooparlor_interior}],
                                     "force", ["grace", {"flag":True}],
                                     "force", ["odette", {"flag":True}],
                                     ])

    S_eve_school_stinker.add(T_eve_upset_pot, S_eve_upset_pot)
    S_eve_upset_pot.add(T_eve_pot_cheerup, S_eve_pot_look_for_eve)
    S_eve_pot_look_for_eve.add(T_eve_pot_entered_apartment, S_eve_pot_cheerup)
    S_eve_pot_cheerup.add(T_eve_pot_cheered_up, S_eve_voyeurism_start,
                            actions=["setdefaultloc", [[L_school_frenchclassroom, L_school_righthallway, L_tattooparlor_roof, L_tattooparlor_bedroom], [L_tattooparlor_bedroom, L_tattooparlor_roof, L_tattooparlor_roof, L_tattooparlor_bedroom]],
                                     "unforce", "grace",
                                     "unforce", "odette",
                                     "unforce", None,
                                     "unlocklocation", L_tattooparlor_roof])

    S_eve_voyeurism_start.add(T_eve_voyeurism_meetup, S_eve_voyeurism_meetup)
    S_eve_voyeurism_meetup.add(T_eve_voyeurism_follow_roof, S_eve_voyeurism_follow_roof,
                            actions=['location', {'place': L_tattooparlor_roof},
                                     'force', {'tod': 2}])
    S_eve_voyeurism_follow_roof.add(T_eve_voyeurism_follow_tent, S_eve_voyeurism_follow_tent,
                            actions=['location', {'place': L_tattooparlor_tent},
                                     'force', {'tod': 2}])

    S_eve_voyeurism_follow_tent.add(T_eve_trap_revealed, S_eve_detention,
                            actions=['location', {'place': L_school_righthallway},
                                     'force', {'tod': [0,1]}])

    S_eve_detention.add(T_eve_got_detention, S_eve_bike_breakdown_start,
                            actions=['unforce', None])

    S_eve_bike_breakdown_start.add(T_eve_bike_breakdown_started, S_eve_bike_breakdown_check_bike,
                            actions=['location', ['odette', {'place': L_tattooparlor_interior, "dow": [5, 6], "tod":[0, 1, 2]}],
                                     'force', ['odette', {'tod': [0, 1, 2]}],
                                     'location', {'place': [[None, None, L_NULL, None]]},
                                     'force', {'tod': 2},
                                     'location', ['grace', {'place': L_NULL, "dow": [5, 6]}],
                                     'force', ['grace', {'tod': [0, 1, 2]}]])
    S_eve_bike_breakdown_check_bike.add(T_eve_bike_breakdown_check_bike, S_eve_bike_breakdown_repair)
    S_eve_bike_breakdown_repair.add(T_eve_bike_breakdown_repair_fail, S_eve_bike_breakdown_repair_again,
                            actions=["exec", "game.unlock_ui()"])
    S_eve_bike_breakdown_repair.add(T_eve_bike_breakdown_repair_pass, S_eve_bike_breakdown_start_repair,
                            actions=['unforce', 'odette',
                                     'unforce', 'grace',
                                     'unforce', None,
                                     'exec', 'game.unlock_ui()'])
    S_eve_bike_breakdown_repair_again.add(T_eve_bike_breakdown_repair_pass, S_eve_bike_breakdown_start_repair,
                            actions=['unforce', 'odette',
                                     'unforce', None])
    S_eve_bike_breakdown_start_repair.add(T_eve_bike_breakdown_repaired_bike, S_eve_talk_to_girls,
                            actions=['location', ['grace', {'place': L_tattooparlor_roof}],
                                     'force', ['grace', {'tod': [2, 3]}],
                                     'location', {'place': L_tattooparlor_roof},
                                     'force', {'tod': [2, 3]}])

    S_eve_talk_to_girls.add(T_eve_talked_to_grace, S_eve_talked_to_grace)
    S_eve_talk_to_girls.add(T_eve_talked_to_eve, S_eve_talked_to_eve)
    S_eve_talked_to_grace.add(T_eve_talked_to_eve, S_eve_clients_hangover_wakeup,
                            actions=["unforce", "grace",
                                     "unforce", None])
    S_eve_talked_to_eve.add(T_eve_talked_to_grace, S_eve_clients_hangover_wakeup,
                            actions=["unforce", "grace",
                                     "unforce", None])

    S_eve_clients_hangover_wakeup.add(T_player_woke_up, S_eve_clients_check_shop,
                            actions=["location", ["grace", {"place": L_NULL}],
                                     "location", {"place": L_NULL},
                                     "force", ["grace", {"tod": [0, 1]}],
                                     "force", {"tod": [0, 1]}])
    S_eve_clients_check_shop.add(T_eve_woke_odette, S_eve_clients_wake_up_grace)
    S_eve_clients_wake_up_grace.add(T_eve_woke_grace, S_eve_clients_mall_fliers,
                            actions=["unforce", "grace"])
    S_eve_clients_mall_fliers.add(T_eve_mall_fliers_hung, S_eve_clients_library_fliers)
    S_eve_clients_library_fliers.add(T_eve_library_fliers_hung, S_eve_clients_park_fliers)
    S_eve_clients_park_fliers.add(T_eve_park_fliers_hung, S_eve_clients_tattooshop_crowd,
                                  actions=['location', ['odette', {'place': L_tattooparlor_garage, 'tod': [0, 1]}],
                                           'force', ['odette', {'tod': [0, 1]}]])
    S_eve_clients_tattooshop_crowd.add(T_eve_tattoo_shop_crowded, S_eve_clients_take_care_clients)
    S_eve_clients_take_care_clients.add(T_eve_took_care_clients, S_eve_party_start,
                            actions=["unforce", None,
                                     'unforce', 'odette',
                                     "cleanlocation", None,
                                     "set", "party_in_progress"])

    S_eve_party_start.add(T_eve_party_started, S_eve_party_speak_to_grace,
                            actions=["cleanlocation", "grace",
                                     "cleanlocation", "odette",
                                     "cleanlocation", "tuuku",
                                     "location", {"place": L_NULL, "tod":[2, 3], 'dow': [5]},
                                     "force", {"tod": [2, 3]},
                                     "location", ["grace", {"place": L_tattooparlor_garage, "tod": [2, 3], "dow": [5]}],
                                     "force", ["grace", {"tod": [2, 3]}]])
    S_eve_party_speak_to_grace.add(T_eve_party_spoke_to_grace, S_eve_party_speak_to_jenny,
                            actions=["location", ["jenny", {"place": L_tattooparlor_roof, "tod": [2], "dow": [5]}],
                                     "force", ["jenny", {"tod": [2]}]])
    S_eve_party_speak_to_jenny.add(T_eve_party_spoke_to_jenny, S_eve_party_speak_to_odette,
                            actions=["location", ["odette", {"place": L_tattooparlor_roof, "tod": [2], "dow": [5]}],
                                     "force", ["odette", {"tod": [2]}],
                                     "unforce", "jenny"])
    S_eve_party_speak_to_odette.add(T_eve_party_spoke_to_odette, S_eve_party_speak_to_tuuku,
                            actions=["location", ["tuuku", {"place": L_tattooparlor_alley, "tod": [2], "dow": [5]}],
                                     "force", ["tuuku", {"tod": [2]}]])
    S_eve_party_speak_to_tuuku.add(T_eve_party_end, S_eve_make_up_grace_upset,
                            actions=["unforce", "grace",
                                     "unforce", "odette",
                                     "unforce", "tuuku",
                                     "unforce", None,
                                     "clear", "party_in_progress",
                                     "location", ["odette", {"place": L_tattooparlor_garage}],
                                     "force", ["odette", {"tod":[0, 1, 2]}],
                                     "set", "odette_depressed",
                                     "setdefaultloc", [[L_school_frenchclassroom, L_school_righthallway, L_tattooparlor_bedroom, L_tattooparlor_bedroom], [L_tattooparlor_bedroom, L_tattooparlor_roof, L_tattooparlor_bedroom, L_tattooparlor_bedroom]]])

    S_eve_make_up_grace_upset.add(T_eve_make_up_mall, S_eve_make_up_go_to_mall,
                                  actions=["location", ["odette", {"place": L_NULL}]])
    S_eve_make_up_go_to_mall.add(T_eve_bought_candles_chocolate, S_eve_make_up_extort_tuuku)
    S_eve_make_up_extort_tuuku.add(T_eve_got_wine, S_eve_make_up_pick_up_lasagna)
    S_eve_make_up_pick_up_lasagna.add(T_eve_picked_up_lasagna, S_eve_make_up_dress_table)
    S_eve_make_up_dress_table.add(T_eve_dressed_table, S_eve_lesbians_aftermath,
                                    actions=["unforce", "odette",
                                             "clear", "odette_depressed",
                                             'setdefaultloc', ('grace', [[L_tattooparlor_interior, L_tattooparlor_interior, L_tattooparlor_apartment, L_tattooparlor_bedroom], [L_tattooparlor_interior, L_tattooparlor_apartment, L_tattooparlor_apartment, L_tattooparlor_bedroom]]),
                                             'setdefaultloc', ('odette', [[L_tattooparlor_garage, L_tattooparlor_interior, L_tattooparlor_interior, L_tattooparlor_garage], [L_tattooparlor_garage, L_tattooparlor_interior, L_tattooparlor_apartment, L_tattooparlor_garage]]),
                                             ])

    S_eve_lesbians_aftermath.add(T_eve_talked_about_grace_odette, S_eve_six6nine9_time,
                                actions=["setcantalk", {"odette": [True, True, True, False]}])

    S_eve_six6nine9_time.add(T_eve_had_sixtynine, S_eve_sexy_time)

    S_eve_sexy_time.add(T_eve_had_sexy_time, S_eve_end,
                                    actions=["exec", A_eve_tat_too_point_oh.unlock])


    M_eve.add(S_eve_start,
              S_eve_park_hangout,
              S_eve_cafeteria_troubles,
              S_eve_ross_argument_delay, S_eve_ross_argument, S_eve_auditorium_bummed,
              S_eve_visit_tattoo_shop, S_eve_visit_garage, S_eve_visit_roof, S_eve_visit_apartment, S_eve_visit_bedroom,
              S_eve_big_sister_problems, S_eve_big_sis_check_garage, S_eve_big_sis_talk_odette, S_eve_big_sis_check_apartment,
              S_eve_roxxy_bullying_prepare, S_eve_roxxy_bullying, S_eve_roxxy_bullying_upset, S_eve_school_dress_code,
              S_eve_dress_code_ask_teachers, S_eve_bridgets_help, S_eve_distract_grace, S_eve_ask_distract_grace, S_eve_bathroom_break, S_eve_bathroom_embarassed,
              S_eve_apologize, S_eve_pranking_roxxy, S_eve_pranking_douches,
              S_eve_tuuku_with_douches,
              S_eve_police_trouble,
              S_eve_school_stinker, S_eve_upset_pot, S_eve_pot_look_for_eve, S_eve_pot_cheerup,
              S_eve_voyeurism_start, S_eve_voyeurism_meetup, S_eve_voyeurism_follow_roof,
              S_eve_voyeurism_follow_tent,
              S_eve_detention,
              S_eve_bike_breakdown_start, S_eve_bike_breakdown_check_bike, S_eve_bike_breakdown_repair, S_eve_bike_breakdown_repair_again, S_eve_bike_breakdown_start_repair,
              S_eve_talk_to_girls, S_eve_talked_to_grace, S_eve_talked_to_eve,
              S_eve_clients_hangover_wakeup, S_eve_clients_check_shop, S_eve_clients_wake_up_grace, S_eve_clients_mall_fliers, S_eve_clients_library_fliers, S_eve_clients_park_fliers, S_eve_clients_tattooshop_crowd, S_eve_clients_take_care_clients,
              S_eve_party_start, S_eve_party_speak_to_grace, S_eve_party_speak_to_jenny, S_eve_party_speak_to_odette, S_eve_party_speak_to_tuuku,
              S_eve_make_up_grace_upset, S_eve_make_up_go_to_mall, S_eve_make_up_extort_tuuku,  S_eve_make_up_pick_up_lasagna, S_eve_make_up_dress_table,
              S_eve_lesbians_aftermath,
              S_eve_six6nine9_time, S_eve_sexy_time,
              S_eve_end)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
