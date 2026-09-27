init -1 python:
    M_dewitt = Machine("Dewitt", default_loc = [[L_school_musicclassroom, L_school_musicclassroom, L_school_dewittoffice, L_NULL],
                                                [L_NULL, L_NULL, L_NULL, L_NULL]
                                                ],
                       vars = {"sex speed": .175,
                               "talent ask erik": False,
                               "talent ask eve": False,
                               "talent ask dexter": False,
                               "talent ask judith": False,
                               "talent ask kevin": False,
                               "talent ask mia": False,
                               "talent ask ronda": False,
                               "talent ask roxxy": False,
                               "talent helping eve": False,
                               "talent helping kevin": False,
                               "failcount": 0,
                              },
    )

init -3 python:

    T_dewitt_mc_welcome_back = Trigger()
    T_dewitt_mc_overhear = Trigger()
    T_dewitt_mc_talent_show_help = Trigger()
    T_dewitt_judith_flute = Trigger()
    T_dewitt_get_flute = Trigger()
    T_dewitt_fix_flute = Trigger()
    T_dewitt_flute_practice = Trigger()
    T_dewitt_talent_hunt = Trigger()
    T_dewitt_annies_refusal = Trigger()
    T_dewitt_eves_agreement = Trigger()
    T_dewitt_karaoke_jam = Trigger()
    T_dewitt_find_last_talent = Trigger()
    T_dewitt_kevins_agreement = Trigger()
    T_dewitt_eriks_agreement_shed = Trigger()
    T_dewitt_eriks_agreement_no_shed = Trigger()
    T_dewitt_no_paint = Trigger()
    T_dewitt_diane_find_paint = Trigger()
    T_dewitt_shed_find_paint = Trigger()
    T_dewitt_shed_paint = Trigger()
    T_dewitt_made_replacement_guitar = Trigger()
    T_dewitt_get_fender_guitar = Trigger()
    T_dewitt_give_fender_guitar = Trigger()
    T_dewitt_talent_show_excitement = Trigger()
    T_dewitt_auditorium_problem = Trigger()
    T_dewitt_bandit_clue = Trigger()
    T_dewitt_clue_dead_end = Trigger()
    T_dewitt_crying = Trigger()
    T_dewitt_gang_deal = Trigger()
    T_dewitt_erik_deal = Trigger()
    T_dewitt_erik_met = Trigger()
    T_dewitt_fixed_auditorium = Trigger()
    T_dewitt_fetch_dewitt = Trigger()
    T_dewitt_talent_show_uncancelled = Trigger()
    T_dewitt_twerk_n_derk = Trigger()
    T_dewitt_smith_payback_plan = Trigger()
    T_dewitt_sticky_tape_get = Trigger()
    T_dewitt_school_sneak_in = Trigger()
    T_dewitt_trap_set = Trigger()
    T_dewitt_double_check_trap = Trigger()
    T_dewitt_trap_check_ok = Trigger()
    T_dewitt_talent_show_intro = Trigger()
    T_dewitt_talent_show_success = Trigger()
    T_dewitt_sex_it_up = Trigger()

init python:

    S_dewitt_start = State()
    S_dewitt_intro = State(_("My music grades are slipping. I should talk to Miss Dewitt to fix that."))
    S_dewitt_smith_berating = State(_("My music grades are slipping. I should talk to Miss Dewitt to fix that."))
    S_dewitt_talent_show_help = State()
    S_dewitt_find_flute = State(_("Miss Dewitt asked me to find a flute."))
    S_dewitt_judith_locker_search = State(_("Judith may have a flute in her locker."))
    S_dewitt_make_new_flute = State(_("I have to make a flute! For that I'll need some wood..."))
    S_dewitt_return_flute = State(_("I have to return that flute to Miss Dewitt."))
    S_dewitt_talent_show_progress = State(_("I need to find people that'd be interested in participating in the talent show."))
    S_dewitt_talent_show_ask_annie = State(_("I need to find people that'd be interested in participating in the talent show."))
    S_dewitt_talent_show_ask = State(_("I need to find people that'd be interested in participating in the talent show."))
    S_dewitt_talent_show_ask_eve = State(_("I need to find people that'd be interested in participating in the talent show."))
    S_dewitt_eve_karaoke = State()
    S_dewitt_talent_show_ask_kevin = State(_("I need to find people that'd be interested in participating in the talent show."))
    S_dewitt_erik_borrow_guitar = State(_("Erik might have a guitar for me."))
    S_dewitt_garage_find_paint = State(_("I need to find some paint for the guitar."))
    S_dewitt_ask_deb_paint = State(_("I need to find some paint for the guitar. Maybe [deb_name] has some."))
    S_dewitt_ask_diane_paint = State(_("I need to find some paint for the guitar. Maybe Diane has some."))
    S_dewitt_shed_get_paint = State(_("Diane told me there is some paint in the Shed."))
    S_dewitt_make_replacement_guitar = State(_("I have to make a replacement guitar."))
    S_dewitt_replace_guitar = State()
    S_dewitt_kevin_give_guitar = State(_("I should give that guitar to Kevin, so that he can train for the talent show."))
    S_dewitt_talent_get = State()
    S_dewitt_music_sheets_delay = State()
    S_dewitt_music_sheets = State()
    S_dewitt_graffiti_mess = State(_("Someone vandalized the Auditorium! I need to find the culprit."))
    S_dewitt_paint_trail = State(_("I should follow this paint trail."))
    S_dewitt_check_up = State()
    S_dewitt_eve_meet_up = State(_("I should get some help to clean this mess. Maybe some people around town need some good karma..."))
    S_dewitt_erik_get_beer = State()
    S_dewitt_clean_graffiti = State()
    S_dewitt_find_dewitt = State()
    S_dewitt_show_auditorium = State()
    S_dewitt_office_reward = State()
    S_dewitt_talent_show_practice = State()
    S_dewitt_talent_show_practice_delay = State()
    S_dewitt_science_adhesive = State()
    S_dewitt_school_sneak_mission_help = State()
    S_dewitt_school_sneak_mission_ready = State(_("Erik agreed to help me sneak into the school in the evening."))
    S_dewitt_school_sneak_mission = State()
    S_dewitt_smith_office_trap = State()
    S_dewitt_pre_talent_show_chat = State()
    S_dewitt_trap_check_up = State()
    S_dewitt_attend_talent_show = State()
    S_dewitt_talent_show = State()
    S_dewitt_office_night_visit_delay = State()
    S_dewitt_office_night_visit = State()
    S_dewitt_end = State()


    S_dewitt_start.add(T_bridget_workout, S_dewitt_intro)
    S_dewitt_intro.add(T_dewitt_mc_welcome_back, S_dewitt_smith_berating)
    S_dewitt_smith_berating.add(T_dewitt_mc_overhear, S_dewitt_talent_show_help)
    S_dewitt_talent_show_help.add(T_dewitt_mc_talent_show_help, S_dewitt_find_flute)
    S_dewitt_find_flute.add(T_dewitt_judith_flute, S_dewitt_judith_locker_search)
    S_dewitt_judith_locker_search.add(T_dewitt_get_flute, S_dewitt_make_new_flute)
    S_dewitt_make_new_flute.add(T_dewitt_fix_flute, S_dewitt_return_flute)
    S_dewitt_return_flute.add(T_dewitt_flute_practice, S_dewitt_talent_show_progress,
                              actions = ["exec", "player.increase_grade_music()"]
                              )
    S_dewitt_talent_show_progress.add(T_dewitt_talent_hunt, S_dewitt_talent_show_ask_annie)
    S_dewitt_talent_show_ask_annie.add(T_dewitt_annies_refusal, S_dewitt_talent_show_ask,
                                       actions = ["set", "talent ask erik",
                                                  "set", "talent ask eve",
                                                  "set", "talent ask dexter",
                                                  "set", "talent ask judith",
                                                  "set", "talent ask kevin",
                                                  "set", "talent ask mia",
                                                  "set", "talent ask ronda",
                                                  "set", "talent ask roxxy",
                                                 ]
                                       )
    S_dewitt_talent_show_ask.add(T_dewitt_eves_agreement, S_dewitt_eve_karaoke,
                                 actions = ["clear", "talent ask eve",
                                            "set", "talent helping eve",
                                           ]
                                 )
    S_dewitt_talent_show_ask.add(T_dewitt_kevins_agreement, S_dewitt_erik_borrow_guitar,
                                 actions = ["clear", "talent ask kevin",
                                            "set", "talent helping kevin",
                                           ]
                                 )
    S_dewitt_talent_show_ask_eve.add(T_dewitt_eves_agreement, S_dewitt_eve_karaoke)
    S_dewitt_eve_karaoke.add(T_dewitt_find_last_talent, S_dewitt_talent_show_ask_kevin,
                             actions = ["clear", "talent helping eve"]
                             )
    S_dewitt_eve_karaoke.add(T_dewitt_karaoke_jam, S_dewitt_talent_get,
                             actions = ["clear", "talent helping eve"]
                             )
    S_dewitt_talent_show_ask_kevin.add(T_dewitt_kevins_agreement, S_dewitt_erik_borrow_guitar)
    S_dewitt_erik_borrow_guitar.add(T_dewitt_eriks_agreement_shed, S_dewitt_shed_get_paint)
    S_dewitt_erik_borrow_guitar.add(T_dewitt_eriks_agreement_no_shed, S_dewitt_garage_find_paint)
    S_dewitt_garage_find_paint.add(T_dewitt_no_paint, S_dewitt_ask_deb_paint)
    S_dewitt_ask_deb_paint.add(T_dewitt_diane_find_paint, S_dewitt_ask_diane_paint)
    S_dewitt_ask_diane_paint.add(T_dewitt_shed_paint, S_dewitt_shed_get_paint)
    S_dewitt_shed_get_paint.add(T_dewitt_shed_find_paint, S_dewitt_make_replacement_guitar)
    S_dewitt_make_replacement_guitar.add(T_dewitt_made_replacement_guitar, S_dewitt_replace_guitar)
    S_dewitt_replace_guitar.add(T_dewitt_get_fender_guitar, S_dewitt_kevin_give_guitar)
    S_dewitt_kevin_give_guitar.add(T_dewitt_find_last_talent, S_dewitt_talent_show_ask_eve,
                                   actions = ["clear", "talent helping kevin"]
                                   )
    S_dewitt_kevin_give_guitar.add(T_dewitt_give_fender_guitar, S_dewitt_talent_get,
                                   actions = ["clear", "talent helping kevin"]
                                   )
    S_dewitt_talent_get.add(T_dewitt_talent_show_excitement, S_dewitt_music_sheets_delay,
                            actions = ["clear", "talent ask erik",
                                       "clear", "talent ask eve",
                                       "clear", "talent ask dexter",
                                       "clear", "talent ask judith",
                                       "clear", "talent ask kevin",
                                       "clear", "talent ask mia",
                                       "clear", "talent ask ronda",
                                       "clear", "talent ask roxxy",
                                       "exec", "player.increase_grade_music()",
                                      ]
                            )
    S_dewitt_music_sheets_delay.add(T_all_sleep, S_dewitt_music_sheets)
    S_dewitt_music_sheets.add(T_dewitt_auditorium_problem, S_dewitt_graffiti_mess,
                              actions = ["location", {"place": L_school_assemblyhall},
                                         "force", {"flag": True},
                                         ],
                              )
    S_dewitt_graffiti_mess.add(T_dewitt_bandit_clue, S_dewitt_paint_trail,
                               actions = ["unforce", None,
                                          "location", ["annie", {"place": L_school_smithoffice}],
                                          "force", ["annie", {"flag": True}],
                                          "location", ["smith", {"place": L_school_smithoffice}],
                                          "force", ["smith", {"flag": True}],
                                          ],
                               )
    S_dewitt_paint_trail.add(T_dewitt_clue_dead_end, S_dewitt_check_up,
                             actions = ["unforce", "annie",
                                        "unforce", "smith",
                                        ],
                             )
    S_dewitt_check_up.add(T_dewitt_crying, S_dewitt_eve_meet_up)
    S_dewitt_eve_meet_up.add(T_dewitt_gang_deal, S_dewitt_erik_get_beer)
    S_dewitt_erik_get_beer.add(T_dewitt_erik_deal, S_dewitt_clean_graffiti)
    S_dewitt_clean_graffiti.add(T_dewitt_fixed_auditorium, S_dewitt_find_dewitt,
                                actions = ["location", {"place": L_school_musicclassroom},
                                           "force", {"flag": True},
                                           ],
                                )
    S_dewitt_find_dewitt.add(T_dewitt_fetch_dewitt, S_dewitt_show_auditorium,
                             actions = ["location", {"place": L_school_assemblyhall}],
                             )
    S_dewitt_show_auditorium.add(T_dewitt_talent_show_uncancelled, S_dewitt_office_reward,
                                 actions = ["location", {"place": L_school_dewittoffice}],
                                 )
    S_dewitt_office_reward.add(T_dewitt_twerk_n_derk, S_dewitt_talent_show_practice_delay,
                               actions = ["exec", "player.increase_grade_music()",
                                          "unforce", None,
                                          ],
                               )
    S_dewitt_talent_show_practice_delay.add(T_all_sleep, S_dewitt_talent_show_practice)
    S_dewitt_talent_show_practice.add(T_dewitt_smith_payback_plan, S_dewitt_science_adhesive)
    S_dewitt_science_adhesive.add(T_dewitt_sticky_tape_get, S_dewitt_school_sneak_mission_help)
    S_dewitt_school_sneak_mission_help.add(T_dewitt_erik_deal, S_dewitt_school_sneak_mission_ready)
    S_dewitt_school_sneak_mission_ready.add(T_dewitt_erik_met, S_dewitt_school_sneak_mission)
    S_dewitt_school_sneak_mission.add(T_dewitt_school_sneak_in, S_dewitt_smith_office_trap)
    S_dewitt_smith_office_trap.add(T_dewitt_trap_set, S_dewitt_pre_talent_show_chat)
    S_dewitt_pre_talent_show_chat.add(T_dewitt_double_check_trap, S_dewitt_trap_check_up,
                                      actions = ["location", ["annie", {"place": L_school_smithoffice}],
                                                 "force", ["annie", {"flag": True}],
                                                 "location", ["smith", {"place": L_school_smithoffice}],
                                                 "force", ["smith", {"flag": True}],
                                                 ],
                                      )
    S_dewitt_trap_check_up.add(T_dewitt_trap_check_ok, S_dewitt_attend_talent_show)
    S_dewitt_attend_talent_show.add(T_dewitt_talent_show_intro, S_dewitt_talent_show)
    S_dewitt_talent_show.add(T_dewitt_talent_show_success, S_dewitt_office_night_visit_delay)
    S_dewitt_office_night_visit_delay.add(T_all_sleep, S_dewitt_office_night_visit,
                                          actions = ["unforce", "annie",
                                                     "unforce", "smith",
                                                     ],
                                          )
    S_dewitt_office_night_visit.add(T_dewitt_sex_it_up, S_dewitt_end,
                                    actions = ["exec", "player.increase_grade_music()",
                                               "exec", A_music_taste.unlock,
                                               'clear', ('player', 'is_virgin')]
                                    )

    M_dewitt.add(S_dewitt_start, S_dewitt_intro, S_dewitt_smith_berating,
                 S_dewitt_talent_show_help, S_dewitt_find_flute,
                 S_dewitt_judith_locker_search, S_dewitt_make_new_flute,
                 S_dewitt_return_flute, S_dewitt_talent_show_progress,
                 S_dewitt_talent_show_ask_annie, S_dewitt_talent_show_ask,
                 S_dewitt_talent_show_ask_eve, S_dewitt_eve_karaoke,
                 S_dewitt_talent_show_ask_kevin, S_dewitt_erik_borrow_guitar,
                 S_dewitt_garage_find_paint, S_dewitt_ask_deb_paint,
                 S_dewitt_ask_diane_paint, S_dewitt_shed_get_paint, S_dewitt_make_replacement_guitar,
                 S_dewitt_replace_guitar, S_dewitt_kevin_give_guitar,
                 S_dewitt_talent_get, S_dewitt_music_sheets_delay,
                 S_dewitt_music_sheets, S_dewitt_graffiti_mess,
                 S_dewitt_paint_trail, S_dewitt_check_up,
                 S_dewitt_eve_meet_up, S_dewitt_erik_get_beer,
                 S_dewitt_clean_graffiti, S_dewitt_find_dewitt,
                 S_dewitt_show_auditorium, S_dewitt_office_reward,
                 S_dewitt_talent_show_practice, S_dewitt_talent_show_practice_delay,
                 S_dewitt_science_adhesive, S_dewitt_school_sneak_mission_help,
                 S_dewitt_school_sneak_mission_ready,
                 S_dewitt_school_sneak_mission, S_dewitt_smith_office_trap,
                 S_dewitt_pre_talent_show_chat, S_dewitt_trap_check_up,
                 S_dewitt_attend_talent_show, S_dewitt_talent_show,
                 S_dewitt_office_night_visit_delay, S_dewitt_office_night_visit,
                 S_dewitt_end)
    M_dewitt.set_priority(1)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
