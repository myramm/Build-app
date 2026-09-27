init -1 python:
    M_roxxy = Machine("roxxy", default_loc = [[L_school_frenchclassroom, L_school_frenchclassroom, L_trailer_bedroom, L_trailer_bedroom],
                                              [L_trailer_interior, L_trailer_interior, L_beach_water, L_NULL]
                                              ],
                      vars = {"sex speed": .3,
                              "roxxy relationship": 0, 
                              "left hallway lock": False,
                              "dexter argument got information": False,
                              "get erik clothes" : False,
                              "heard clyde in trailer" : False,
                              "lost shooting": False,
                              "alcohol talked to eve": False,
                              "talked to roxxy booze": False,
                              "talked to roxxy id": False,
                              "take roxxy mall": False,
                              "talked to terry": False,
                              "trailer foreclosed": False,
                              "talked to harold": False,
                              "caught by smith": False,
                              "give_space": -1,
                              "massage": False,
                              "done basketball": False,
                              "basketball unlocked": False,
                              "shower event intro done" : False,
                              "roxxy trailer sex": 0,
                              "roxxy trailer sex first": True,
                              "roxxy beach sex": 0,
                              "roxxy locker sex": 0,
                              "roxxy locker sex first": True,
                              "meet for locker sex": False,
                              "roxxy crystal sex": 0,
                              },
    )

init -3 python:
    T_roxxy_teachers_berating = Trigger()
    T_roxxy_locker_room = Trigger()
    T_roxxy_argument = Trigger()
    T_roxxy_start_gymercise = Trigger()
    T_roxxy_in_shower = Trigger()
    T_roxxy_get_homework = Trigger()
    T_roxxy_lolipop_once = Trigger()
    T_roxxy_lolipop_lolipop = Trigger()
    T_roxxy_confrontation = Trigger()
    T_roxxy_do_assignment = Trigger()
    T_roxxy_study_at_roxxy = Trigger()
    T_roxxy_study_at_mcs = Trigger()
    T_roxxy_find_cheerleader_outfit= Trigger()
    T_roxxy_get_cheerleader = Trigger()
    T_roxxy_confront_clyde = Trigger()
    T_roxxy_beaten_clyde = Trigger()
    T_roxxy_wait_in_her_room = Trigger()
    T_roxxy_returned_to_school = Trigger()
    T_roxxy_has_uniform = Trigger()
    T_roxxy_go_to_basketball = Trigger()
    T_roxxy_get_beer = Trigger()
    T_roxxy_ask_terry = Trigger()
    T_roxxy_take_picture = Trigger()
    T_roxxy_give_id = Trigger()
    T_roxxy_home_foreclosed = Trigger()
    T_roxxy_checked_trailer = Trigger()
    T_roxxy_confronted_clyde = Trigger()
    T_roxxy_go_to_police = Trigger()
    T_roxxy_talk_to_crystal = Trigger()
    T_roxxy_sell_meth = Trigger()
    T_roxxy_meth_asked_roxxy = Trigger()
    T_roxxy_meet_clyde = Trigger()
    T_roxxy_meet_buyer = Trigger()
    T_roxxy_drug_deal_over = Trigger()
    T_roxxy_chat_with_becca_missy = Trigger()
    T_roxxy_get_goldenschwagger = Trigger()
    T_roxxy_spun_bottle = Trigger()
    T_roxxy_failing_exams = Trigger()
    T_roxxy_find_evidence = Trigger()
    T_roxxy_find_exams = Trigger()
    T_roxxy_escaped_smith = Trigger()
    T_roxxy_gave_exams = Trigger()
    T_roxxy_help_dewitt = Trigger()

    T_roxxy_invitation_bikini = Trigger()
    T_roxxy_check_on_roxxy = Trigger()
    T_roxxy_go_see_contest = Trigger()
    T_roxxy_go_to_cabin = Trigger()
    T_roxxy_bikini_failure = Trigger()
    T_roxxy_get_oil = Trigger()
    T_roxxy_contest_over = Trigger()
    T_roxxy_dexter_challenge_pushups = Trigger()
    T_roxxy_beaten_dexter_pushups = Trigger()
    T_roxxy_accepted_picnic = Trigger()
    T_roxxy_picnic_done = Trigger()
    T_roxxy_kissed = Trigger()
    T_roxxy_basket_challenged = Trigger()
    T_roxxy_humiliated_dexter = Trigger()
    T_roxxy_ninja_dexter = Trigger()
    T_roxxy_trailer_sex = Trigger()
    T_roxxy_beach_sex = Trigger()
    T_roxxy_locker_sex = Trigger()
    T_roxxy_crystal_sex = Trigger()

init python:

    S_roxxy_start = State(_("I should go to the school..."))
    S_roxxy_teachers_event_delay = State(_("Roxxy is such a bitch, I should check on her tomorrow"))
    S_roxxy_teachers_event = State(_("Roxxy is such a bitch, I should check on her."))
    S_roxxy_lockerroom_event_delay = State(_("Wow, she's in so much trouble, I wonder if I can help"))
    S_roxxy_lockerroom_event = State(_("I should check out the School..."))
    S_roxxy_dexter_argument_delay = State(_("I overheard Roxxy talking about issues with Dexter... Things are coming up to me!"))
    S_roxxy_dexter_argument = State(_("Roxxy has issues with Dexter, I should check out the school..."))
    S_roxxy_intense_gymercise = State(_("Coach Bridget wants me to prove I can do push-ups..."), delay=1)
    S_roxxy_shower_event = State(_("After that workout, I need a good shower."))
    S_roxxy_lolipop = State(_("Roxxy wants to copy my homework."))
    S_roxxy_lolipop_delay = State(_("I should wait a little while..."))
    S_roxxy_lolipop_just_once = State(_("I agreed to give her my homework, just this once."))
    S_roxxy_lolipop_for_lolipop = State(_("I agreed to give her my homework for a reward."))
    S_roxxy_dexter_confront_delay = State(_("I have a lollipop, I don't think I'll get anything more right now."))
    S_roxxy_dexter_confront = State(_("I should go to school."))
    S_roxxy_assignment_delay = State(_("Dexter is pissed at me for hanging out with Roxxy. When will she dump his dumb ass?"))
    S_roxxy_assignment = State(_("Roxxy may need help studying for her assignment."))
    S_roxxy_studying_at_roxxys = State(_("We're heading over to her place to study."))
    S_roxxy_studying_at_mcs = State(_("My place is more quiet in the end. What is Crystal up to?"))
    S_roxxy_missing_outfit_delay = State(_("I should give her some space."))
    S_roxxy_missing_outfit_delay2 = State(_("I should give her some space."))
    S_roxxy_missing_outfit = State(_("I should talk to Roxxy."))
    S_roxxy_get_cheerleader_outfit = State(_("Roxxy needs her cheerleading outfit to practice."))
    S_roxxy_beat_clyde = State(_("Clyde has it, maybe I can convince him to give it back."))
    S_roxxy_get_uniform_on_doggo = State(_("He put it on his dog/pig thing!"))
    S_roxxy_wait_in_her_room = State(_("Roxxy is going to get changed. I should go to her room"))
    S_roxxy_return_to_school = State(_("The second period is starting soon. I should get back to school!"))
    S_roxxy_dexter_alcohol_fight_delay = State(_("I shouldn't be too pushy with her."))
    S_roxxy_dexter_alcohol_fight = State(_("Let's head to the basketball court, Eve mentioned a fight!"))
    S_roxxy_need_booze = State(_("Roxxy got into a fight over alcohol. I might help her get some."))
    S_roxxy_get_fake_id = State(_("Roxxy needs a fake ID to buy some alcohol"))
    S_roxxy_fake_id_ask_terry = State(_("I heard that Terry, at the pier, makes fake IDs"))
    S_roxxy_fake_id_get_picture = State(_("Terry needs a picture and $400. I should tell Roxxy."))
    S_roxxy_trailer_park_trouble_delay = State(_("I should give her some time..."))
    S_roxxy_trailer_park_trouble_delay2 = State(_("I should give her some time..."))
    S_roxxy_trailer_park_trouble = State(_("I should go talk to her."))
    S_roxxy_check_trailer = State(_("I have to accompany Roxxy to her home, in the Trailer Park"))
    S_roxxy_confront_clyde = State(_("Clyde has to have something to do with the trailer being foreclosed."))
    S_roxxy_cookies_and_milk = State(_("Roxxy needs some place to go, I'll bring her to my home for some comfort"))
    S_roxxy_ask_earl_release = State(_("I should check the Police station out."))
    S_roxxy_talk_to_crystal = State(_("According to Earl, Crystal won't say anything. Maybe I can help?"))
    S_roxxy_get_evidence = State(_("Crystal didn't do anything, it was all Clyde's fault. I have to garner evidence."))
    S_roxxy_selling_meth_ask_roxxy = State(_("I should tell Roxxy what happened..."))
    S_roxxy_selling_meth = State(_("Clyde has a plan to get bail money : selling meth."))
    S_roxxy_meeting_clyde = State(_("Let's meet Clyde for the drug deal."))
    S_roxxy_meeting_buyer = State(_("Let's meet that mysterious buyer."))
    S_roxxy_shut_down_lab = State(_("Crystal is out, but Clyde is nowhere to be seen..."))
    S_roxxy_hows_it_going_delay = State(_("I should give Roxxy some time after the events"))
    S_roxxy_hows_it_going_delay2 = State(_("I should give Roxxy some time after the events"))
    S_roxxy_hows_it_going_delay3 = State(_("I should give Roxxy some time after the events"))
    S_roxxy_hows_it_going = State(_("I should ask her how's she holding up..."))
    S_roxxy_chat_with_becca_missy = State(_("I need to get Becca and Missy to warm up to me."))
    S_roxxy_spin_bottle = State(_("The girls have invited me to the beach on weekends, but I can't go empty-handed"))
    S_roxxy_ask_exam_copy_delay = State(_("That was wild... And hot."))
    S_roxxy_ask_exam_copy = State(_("Roxxy still needs to pass her exams."))
    S_roxxy_sneak_into_smith = State(_("Mrs. Smith apparently keeps a copy of the exams at her house."))
    S_roxxy_give_exams_delay = State(_("I have the exams!"))
    S_roxxy_give_exams = State(_("I gave Roxxy the exams. Hope for the best!"))
    S_roxxy_dexter_flirt_delay = State(_("I sure hoped Roxxy passed her test."))
    S_roxxy_dexter_flirt = State(_("I should go to School."))
    S_roxxy_go_in_auditorium = State(_("I heard some stuff going on in the auditorium."))
    S_roxxy_invite_to_bikini_contest = State(_("Dexter is such a pig! At least, I get to see Roxxy in a bikini at the beach this saturday afternoon."))
    S_roxxy_go_see_contest = State(_("I should check out the contest, Captain Terry is on the stage"))
    S_roxxy_check_on_roxxy = State(_("I should check up on the girls at the showers"))
    S_roxxy_in_cabin = State(_("Roxxy's top snapped! I should check on her."))
    S_roxxy_get_new_bikini = State(_("Roxxy needs a new bikini! Sara threw her's on the podium."))
    S_roxxy_get_oil = State(_("Roxxy needs to be oiled up for the contest. There's some oil in the lifeguard's tower."))
    S_roxxy_do_pushups_delay = State(_("That contest was wild, I'm glad Roxxy won!"))
    S_roxxy_do_pushups_intro = State(_("Coach Bridget needs me at the School."))
    S_roxxy_do_pushups = State(_("I gotta show Dexter he took on the wrong guy."))
    S_roxxy_trailer_park_romance_delay = State(_("Take that, Dexter!"))
    S_roxxy_trailer_park_romance = State(_("Roxxy is definitely warming up to me, I should go talk to her."))
    S_roxxy_go_to_picnic = State(_("She invited me to dinner this afternoon!"))
    S_roxxy_picnic_done = State(_("Dexter saw me kissing Roxxy. It's not good..."))
    S_roxxy_dexter_basketball = State(_("Dexter will definitely want to beat me up... But I can't not go to school!"))
    S_roxxy_dexter_basketball_delay = State(_("Dexter saw me kissing Roxxy. It's not good..."))
    S_roxxy_basketball_challenge = State(_("If I beat Dexter at his own game he'll definitely leave me alone, right?"))
    S_roxxy_fight_dexter_delay = State(_("It's not gonna end well. He deserved it though."))
    S_roxxy_fight_dexter = State(_("Now that I humiliated him at basketball, Dexter is gonna want to kill me for sure!"))
    S_roxxy_end = State()


    S_roxxy_start.add(T_roxxy_teachers_berating, S_roxxy_teachers_event_delay)
    S_roxxy_teachers_event_delay.add(T_all_sleep, S_roxxy_teachers_event,
                                     actions = ["location", {"tod": [0,1], "place": L_school_floor3},
                                                "force", {"tod": [0,1]},
                                                ]
                                     )
    S_roxxy_teachers_event.add(T_roxxy_locker_room, S_roxxy_lockerroom_event_delay,
                               actions = ["unforce", None]
                               )
    S_roxxy_lockerroom_event_delay.add(T_all_sleep, S_roxxy_lockerroom_event,
                                       actions = ["exec", L_school_girlsroom.unlock,
                                                  "location", {"tod": [0,1], "place": L_school_girlsroom},
                                                  "force", {"tod": [0,1]},
                                                  ]
                                       )
    S_roxxy_lockerroom_event.add(T_roxxy_argument, S_roxxy_dexter_argument_delay,
                                 actions = ["clear", "left hallway lock",
                                            "unforce", None,
                                            ]
                                 )
    S_roxxy_dexter_argument_delay.add(T_all_sleep, S_roxxy_dexter_argument)
    S_roxxy_dexter_argument.add(T_roxxy_start_gymercise, S_roxxy_intense_gymercise)
    S_roxxy_intense_gymercise.add(T_roxxy_in_shower, S_roxxy_shower_event,
                                  actions = ["location", {"tod": [0,1], "place": L_school_shower},
                                             "force", {"tod": [0,1]},
                                             ]
                                  )
    S_roxxy_shower_event.add(T_roxxy_get_homework, S_roxxy_lolipop_delay,
                             actions = ["unforce", None]
                             )
    S_roxxy_lolipop_delay.add(T_all_sleep, S_roxxy_lolipop)
    S_roxxy_lolipop.add(T_roxxy_lolipop_lolipop, S_roxxy_lolipop_for_lolipop)
    S_roxxy_lolipop.add(T_roxxy_lolipop_once, S_roxxy_lolipop_just_once)
    S_roxxy_lolipop_for_lolipop.add(T_roxxy_confrontation, S_roxxy_dexter_confront_delay)
    S_roxxy_lolipop_just_once.add(T_roxxy_confrontation, S_roxxy_dexter_confront_delay)
    S_roxxy_dexter_confront_delay.add(T_all_sleep, S_roxxy_dexter_confront)
    S_roxxy_dexter_confront.add(T_roxxy_do_assignment, S_roxxy_assignment_delay, actions=["assign", ("roxxy relationship", 1)])
    S_roxxy_assignment_delay.add(T_all_sleep, S_roxxy_assignment)
    S_roxxy_assignment.add(T_roxxy_study_at_roxxy, S_roxxy_studying_at_roxxys, actions=["unlocklocation", L_trailerpark,
                                                                                        "location", ["clyde", {"tod":None, "place":L_trailer_interior}],
                                                                                        "force", ["clyde", {"flag":[True]*4}]])
    S_roxxy_studying_at_roxxys.add(T_roxxy_study_at_mcs, S_roxxy_studying_at_mcs,
                                   actions=('location', ('crystal', {'place': L_trailer_interior}),
                                            'force', ('crystal', {'tod': 2})))
    S_roxxy_studying_at_mcs.add(T_roxxy_get_cheerleader, S_roxxy_missing_outfit_delay,
                                actions=('unforce', 'clyde',
                                         'unforce', 'crystal'))
    S_roxxy_missing_outfit_delay.add(T_all_sleep, S_roxxy_missing_outfit_delay2)
    S_roxxy_missing_outfit_delay2.add(T_all_sleep, S_roxxy_missing_outfit)
    S_roxxy_missing_outfit.add(T_roxxy_find_cheerleader_outfit, S_roxxy_get_cheerleader_outfit)
    S_roxxy_get_cheerleader_outfit.add(T_roxxy_confront_clyde, S_roxxy_beat_clyde)
    S_roxxy_beat_clyde.add(T_roxxy_beaten_clyde, S_roxxy_get_uniform_on_doggo)
    S_roxxy_get_uniform_on_doggo.add(T_roxxy_wait_in_her_room, S_roxxy_wait_in_her_room)
    S_roxxy_wait_in_her_room.add(T_roxxy_has_uniform, S_roxxy_return_to_school)
    S_roxxy_return_to_school.add(T_roxxy_returned_to_school, S_roxxy_dexter_alcohol_fight_delay, actions=["assign", ("roxxy relationship", 2)])
    S_roxxy_dexter_alcohol_fight_delay.add(T_all_sleep, S_roxxy_dexter_alcohol_fight, actions=["location", {"tod":0, "place":L_basketball_court},
                                                                                               "force", {"tod": 0},
                                                                                               "location", ["dexter", {"tod":0, "place":L_basketball_court}],
                                                                                               "force", ["dexter", {"tod":0}]])
    S_roxxy_dexter_alcohol_fight.add(T_roxxy_go_to_basketball, S_roxxy_need_booze, actions=["unforce", None, "unforce", "dexter"])
    S_roxxy_need_booze.add(T_roxxy_get_beer, S_roxxy_get_fake_id, actions=['unlocklocation', L_pier, "clear", "talked to roxxy booze"])
    S_roxxy_get_fake_id.add(T_roxxy_ask_terry, S_roxxy_fake_id_ask_terry)
    S_roxxy_fake_id_ask_terry.add(T_roxxy_take_picture, S_roxxy_fake_id_get_picture)
    S_roxxy_fake_id_get_picture.add(T_roxxy_give_id, S_roxxy_trailer_park_trouble_delay)

    S_roxxy_trailer_park_trouble_delay.add(T_all_sleep, S_roxxy_trailer_park_trouble_delay2)
    S_roxxy_trailer_park_trouble_delay2.add(T_all_sleep, S_roxxy_trailer_park_trouble, actions=["set", "trailer foreclosed",
                                                                                                "location", ["crystal", {"place":L_police_basement}],
                                                                                                "force", ["crystal", {"tod":[0,1,2,3]}],
                                                                                                "location", {"tod":2},
                                                                                                "location", {"tod":3},
                                                                                                "force", {"tod":[2,3]}])
    S_roxxy_trailer_park_trouble.add(T_roxxy_home_foreclosed, S_roxxy_check_trailer)
    S_roxxy_check_trailer.add(T_roxxy_checked_trailer, S_roxxy_confront_clyde)
    S_roxxy_confront_clyde.add(T_roxxy_confronted_clyde, S_roxxy_cookies_and_milk)
    S_roxxy_cookies_and_milk.add(T_roxxy_go_to_police, S_roxxy_ask_earl_release,
                                actions=["unlocklocation", L_police_front,
                                         "location", ["earl", {"place": L_police_office}],
                                         "force", ["earl", {"tod":[0, 1, 2]}]])
    S_roxxy_ask_earl_release.add(T_roxxy_talk_to_crystal, S_roxxy_talk_to_crystal,
                                actions=["unforce", "earl"])
    S_roxxy_talk_to_crystal.add(T_roxxy_find_evidence, S_roxxy_get_evidence, actions=["unlocklocation", L_trailer_shack_interior])
    S_roxxy_get_evidence.add(T_roxxy_sell_meth, S_roxxy_selling_meth_ask_roxxy)
    S_roxxy_selling_meth_ask_roxxy.add(T_roxxy_meth_asked_roxxy, S_roxxy_selling_meth)
    S_roxxy_selling_meth.add(T_roxxy_meet_clyde, S_roxxy_meeting_clyde)
    S_roxxy_meeting_clyde.add(T_roxxy_meet_buyer, S_roxxy_meeting_buyer,
                                actions=["location", ["park_douches", {"place":L_NULL}],
                                         "force", ["park_douches", {"tod":[2, 3]}]])
    S_roxxy_meeting_buyer.add(T_roxxy_drug_deal_over, S_roxxy_shut_down_lab,
                              actions=('unforce', 'park_douches'))
    S_roxxy_shut_down_lab.add(T_roxxy_failing_exams, S_roxxy_hows_it_going_delay, actions=["clear", "trailer foreclosed",
                                                                                      "unforce", None,
                                                                                      "unforce", "crystal",
                                                                                      "location", ["clyde", {"place":L_NULL}],
                                                                                      "force", ["clyde", {"flag":[True]*4}]])

    S_roxxy_hows_it_going_delay.add(T_all_sleep, S_roxxy_hows_it_going_delay2)
    S_roxxy_hows_it_going_delay2.add(T_all_sleep, S_roxxy_hows_it_going_delay3)
    S_roxxy_hows_it_going_delay3.add(T_all_sleep, S_roxxy_hows_it_going)
    S_roxxy_hows_it_going.add(T_roxxy_chat_with_becca_missy, S_roxxy_chat_with_becca_missy)
    S_roxxy_chat_with_becca_missy.add(T_roxxy_get_goldenschwagger, S_roxxy_spin_bottle)
    S_roxxy_spin_bottle.add(T_roxxy_spun_bottle, S_roxxy_ask_exam_copy_delay)

    S_roxxy_ask_exam_copy_delay.add(T_all_sleep, S_roxxy_ask_exam_copy)
    S_roxxy_ask_exam_copy.add(T_roxxy_find_exams, S_roxxy_sneak_into_smith, actions=["unlocklocation", L_smith_front])
    S_roxxy_sneak_into_smith.add(T_roxxy_escaped_smith, S_roxxy_give_exams_delay)
    S_roxxy_give_exams_delay.add(T_all_sleep, S_roxxy_give_exams)
    S_roxxy_give_exams.add(T_roxxy_gave_exams, S_roxxy_dexter_flirt_delay)
    S_roxxy_dexter_flirt_delay.add(T_all_sleep, S_roxxy_dexter_flirt)
    S_roxxy_dexter_flirt.add(T_roxxy_help_dewitt, S_roxxy_go_in_auditorium)
    S_roxxy_go_in_auditorium.add(T_roxxy_invitation_bikini, S_roxxy_invite_to_bikini_contest, actions=["location", {"place":L_beach_water, "dow":6},
                                                                                                       "location", {"place":L_beach_water, "dow":5},
                                                                                                       "force", {"tod":[0,1]}])

    S_roxxy_invite_to_bikini_contest.add(T_roxxy_go_see_contest, S_roxxy_go_see_contest)
    S_roxxy_go_see_contest.add(T_roxxy_check_on_roxxy, S_roxxy_check_on_roxxy)
    S_roxxy_check_on_roxxy.add(T_roxxy_go_to_cabin, S_roxxy_in_cabin)
    S_roxxy_in_cabin.add(T_roxxy_bikini_failure, S_roxxy_get_new_bikini)
    S_roxxy_get_new_bikini.add(T_roxxy_get_oil, S_roxxy_get_oil)
    S_roxxy_get_oil.add(T_roxxy_contest_over, S_roxxy_do_pushups_delay, actions = ["unforce", None])
    S_roxxy_do_pushups_delay.add(T_all_sleep, S_roxxy_do_pushups_intro)
    S_roxxy_do_pushups_intro.add(T_roxxy_dexter_challenge_pushups, S_roxxy_do_pushups)
    S_roxxy_do_pushups.add(T_roxxy_beaten_dexter_pushups, S_roxxy_trailer_park_romance_delay)
    S_roxxy_trailer_park_romance_delay.add(T_all_sleep, S_roxxy_trailer_park_romance)
    S_roxxy_trailer_park_romance.add(T_roxxy_accepted_picnic, S_roxxy_go_to_picnic)
    S_roxxy_go_to_picnic.add(T_roxxy_picnic_done, S_roxxy_picnic_done)
    S_roxxy_picnic_done.add(T_roxxy_kissed, S_roxxy_dexter_basketball_delay, actions=["unforce", "clyde", "assign", ("roxxy relationship", 3)])
    S_roxxy_dexter_basketball_delay.add(T_all_sleep, S_roxxy_dexter_basketball)
    S_roxxy_dexter_basketball.add(T_roxxy_basket_challenged, S_roxxy_basketball_challenge)
    S_roxxy_basketball_challenge.add(T_roxxy_humiliated_dexter, S_roxxy_fight_dexter_delay)
    S_roxxy_fight_dexter_delay.add(T_all_sleep, S_roxxy_fight_dexter)
    S_roxxy_fight_dexter.add(T_roxxy_ninja_dexter, S_roxxy_end, actions=["assign", ("roxxy relationship", 4), "priority", 0])


    S_roxxy_end.add(T_roxxy_trailer_sex, S_roxxy_end,
                    actions = ["inc", "roxxy trailer sex",
                               "exec", A_the_man.unlock,
                               'clear', ('player', 'is_virgin'),
                               ]
                    )
    S_roxxy_end.add(T_roxxy_beach_sex, S_roxxy_end,
                    actions = ["inc", "roxxy beach sex",
                               'clear', ('player', 'is_virgin')]
                    )
    S_roxxy_end.add(T_roxxy_locker_sex, S_roxxy_end,
                    actions = ["inc", "roxxy locker sex",
                               "clear", "meet for locker sex",
                               'clear', ('player', 'is_virgin'),
                               ]
                    )
    S_roxxy_end.add(T_roxxy_crystal_sex, S_roxxy_end,
                    actions = ["inc", "roxxy crystal sex",
                               'clear', ('player', 'is_virgin')]
                    )

    M_roxxy.set_priority(1)
    M_roxxy.add(S_roxxy_start, S_roxxy_teachers_event_delay, S_roxxy_teachers_event, S_roxxy_lockerroom_event_delay,
                S_roxxy_lockerroom_event, S_roxxy_dexter_argument_delay, S_roxxy_dexter_argument, S_roxxy_shower_event,
                S_roxxy_lolipop, S_roxxy_dexter_confront, S_roxxy_intense_gymercise, S_roxxy_lolipop_delay,
                S_roxxy_lolipop_for_lolipop, S_roxxy_lolipop_just_once, S_roxxy_dexter_confront_delay,
                S_roxxy_assignment_delay, S_roxxy_assignment, S_roxxy_studying_at_roxxys, S_roxxy_studying_at_mcs,
                S_roxxy_missing_outfit, S_roxxy_missing_outfit_delay, S_roxxy_missing_outfit_delay2,
                S_roxxy_get_cheerleader_outfit, S_roxxy_beat_clyde, S_roxxy_get_uniform_on_doggo, S_roxxy_wait_in_her_room,
                S_roxxy_get_fake_id, S_roxxy_fake_id_ask_terry, S_roxxy_return_to_school,
                S_roxxy_dexter_alcohol_fight, S_roxxy_dexter_alcohol_fight_delay, S_roxxy_need_booze,
                S_roxxy_fake_id_get_picture, S_roxxy_trailer_park_trouble, S_roxxy_get_evidence,
                S_roxxy_trailer_park_trouble_delay, S_roxxy_trailer_park_trouble_delay2,
                S_roxxy_check_trailer, S_roxxy_confront_clyde, S_roxxy_cookies_and_milk, S_roxxy_ask_earl_release,
                S_roxxy_talk_to_crystal, S_roxxy_selling_meth, S_roxxy_selling_meth_ask_roxxy, S_roxxy_meeting_buyer,
                S_roxxy_meeting_clyde, S_roxxy_shut_down_lab, S_roxxy_hows_it_going_delay, S_roxxy_hows_it_going_delay2,
                S_roxxy_hows_it_going_delay3, S_roxxy_hows_it_going, S_roxxy_chat_with_becca_missy, S_roxxy_spin_bottle,
                S_roxxy_ask_exam_copy_delay, S_roxxy_give_exams_delay, S_roxxy_dexter_flirt_delay, S_roxxy_go_in_auditorium,
                S_roxxy_ask_exam_copy, S_roxxy_sneak_into_smith, S_roxxy_give_exams, S_roxxy_dexter_flirt,
                S_roxxy_invite_to_bikini_contest, S_roxxy_get_new_bikini, S_roxxy_do_pushups, S_roxxy_picnic_done,
                S_roxxy_do_pushups_delay, S_roxxy_do_pushups_intro, S_roxxy_trailer_park_romance_delay, S_roxxy_go_to_picnic,
                S_roxxy_go_see_contest, S_roxxy_check_on_roxxy, S_roxxy_in_cabin, S_roxxy_get_oil,
                S_roxxy_basketball_challenge, S_roxxy_dexter_basketball_delay, S_roxxy_fight_dexter_delay,
                S_roxxy_trailer_park_romance, S_roxxy_fight_dexter, S_roxxy_dexter_basketball, S_roxxy_end)

    M_roxxy.add_action(T_all_sleep, ["clear", "massage",
                                     "clear", "meet for locker sex",
                                     ]
    )
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
