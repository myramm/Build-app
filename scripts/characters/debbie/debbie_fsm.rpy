init -1 python:
    M_debbie = Machine("debbie", default_loc = [[L_home_kitchen, L_home_basement, L_home_mombedroom, L_home_mombedroom]],
                    vars = {"sex speed": .4,
                            "mom concerned": 100,
                            "dad question": False,
                            "money question": False,
                            "bad guys question": False,
                            "bedroom locked": True,
                            "shower random": False,
                            "chores": False,
                            "lotion fun": False,
                            "fetch lotion": False,
                            "retrieved lotion": False,
                            "bed locked": True,
                            "panties available": False,
                            "panties taken": False,
                            "no panties": False,
                            "jerk available": False,
                            "caught spying": False,
                            "practice kissing": False,
                            "jerk count": 0,
                            "sleep together": False,
                            "revealing": False,
                            "shower fingered": False,
                            "sex flip": True,
                            "robe on": False,
                            "sex available": False,
                            "change angle": False,
                            "location random": "",
                            "time random": 2,
                            "room sneak": False,
                            "movie night": False,
                            "car jerk": False,
                            "car sex": False,
                            "basement sex": False,
                            "shower sex available": False,
                            "account_money": -30000,
                            "account_debt_interest": [0, 0.02, 0.15],
                            "can_access_account": False,
                           },
    )

init -3 python:

    T_debbie_breakfast = Trigger()
    T_debbie_check = Trigger()
    T_debbie_debt_help = Trigger()
    T_debbie_help_mow = Trigger()
    T_debbie_filled_mower = Trigger()
    T_debbie_mowed_lawn = Trigger()
    T_debbie_sis_bitch = Trigger()
    T_debbie_clean_clothes = Trigger()
    T_deb03_init = Trigger()
    T_debbie_mrsj_condolences = Trigger()
    T_debbie_broken_pipe = Trigger()
    T_debbie_sis_order = Trigger()
    T_debbie_closed_valve = Trigger()
    T_debbie_get_wrench = Trigger()
    T_debbie_fixed_broken_pipe = Trigger()
    T_debbie_sis_nice_boobs = Trigger()
    T_debbie_shower_admire = Trigger()
    T_debbie_vacuumed = Trigger()
    T_debbie_washed_dishes = Trigger()
    T_debbie_cleaned_laundry = Trigger()
    T_debbie_lotion_applied = Trigger()
    T_debbie_steal_panties = Trigger()
    T_debbie_caught_masturbating = Trigger()
    T_debbie_movie_invite = Trigger()
    T_debbie_watch_movie = Trigger()
    T_debbie_movie_night_finish = Trigger()
    T_debbie_hang_out_accept = Trigger()
    T_debbie_hang_out_refuse = Trigger()
    T_debbie_mall_arrival = Trigger()
    T_debbie_cupid_arrival = Trigger()
    T_debbie_pick_necklace = Trigger()
    T_debbie_give_necklace = Trigger()
    T_debbie_dressing_room_check = Trigger()
    T_debbie_dream = Trigger()
    T_debbie_caught_spying = Trigger()
    T_debbie_kiss = Trigger()
    T_debbie_shower_ = Trigger()
    T_debbie_car_help = Trigger()
    T_debbie_check_engine = Trigger()
    T_debbie_deliver_car_news = Trigger()
    T_debbie_lapsed_insurance = Trigger()
    T_debbie_extend_insurance = Trigger()
    T_debbie_car_fun = Trigger()
    T_debbie_midnight_fun = Trigger()
    T_debbie_bad_guys_beatup = Trigger()
    T_debbie_sleepover_accept = Trigger()
    T_debbie_sleepover_morning = Trigger()
    T_debbie_diane_chat = Trigger()
    T_debbie_dinner_help = Trigger()
    T_debbie_dinner_outfit_check = Trigger()
    T_debbie_dinner_fish_caught = Trigger()
    T_debbie_diane_dinner_chat = Trigger()
    T_debbie_midnight_wakeup = Trigger()
    T_debbie_midnight_swim = Trigger()
    T_debbie_gave_towel = Trigger()
    T_debbie_reromp = Trigger()
    T_debbie_read_note = Trigger()
    T_debbie_got_laundry = Trigger()
    T_debbie_basement_fun = Trigger()

init python:

    S_debbie_start = State()
    S_debbie_relaxing = State()
    S_debbie_overheard = State()
    S_debbie_debt_call = State()
    S_debbie_lawn_delay = State()
    S_debbie_lawn_help = State()
    S_debbie_fill_mower = State()
    S_debbie_mow_lawn = State()
    S_debbie_clothes_dirty = State()
    S_debbie_wash_clothes = State()
    S_debbie_mrsj_visit_delay = State()
    S_debbie_mrsj_visit = State()
    S_debbie_pipe_delay = State()
    S_debbie_pipe_help = State()
    S_debbie_sis_check = State()
    S_debbie_close_valve = State()
    S_debbie_pipe_check = State()
    S_debbie_fix_pipe = State()
    S_debbie_sis_boobs_afterthoughts = State()
    S_debbie_shower_delay = State()
    S_debbie_shower_peek = State()
    S_debbie_shower_peek_after = State()
    S_debbie_chores_delay = State()
    S_debbie_vacuum_help = State()
    S_debbie_dishes_help = State()
    S_debbie_laundry_help = State()
    S_debbie_lotion_adventure = State()
    S_debbie_search_panties = State()
    S_debbie_panties_masturbation = State()
    S_debbie_movie_night = State()
    S_debbie_romance_movie = State()
    S_debbie_movie_afterthoughts = State()
    S_debbie_hang_out = State()
    S_debbie_hang_out_return = State()
    S_debbie_mall_outing = State()
    S_debbie_cupid_store = State()
    S_debbie_choose_gift = State()
    S_debbie_show_necklace = State()
    S_debbie_dressing_room = State()
    S_debbie_smith_dream = State()
    S_debbie_spy = State()
    S_debbie_solo_dream = State()
    S_debbie_kissing_practice = State()
    S_debbie_shower_walk_in = State()
    S_debbie_car_broken = State()
    S_debbie_check_car = State()
    S_debbie_car_condition = State()
    S_debbie_fix_car = State()
    S_debbie_car_callback = State()
    S_debbie_car_delay = State()
    S_debbie_car_fixed = State()
    S_debbie_panties_masturbation_again = State()
    S_debbie_night_visit = State()
    S_debbie_bad_guys_revisit = State()
    S_debbie_story_delay = State()
    S_debbie_sleepover_offer = State()
    S_debbie_sleepover = State()
    S_debbie_sleepover_wakeup = State()
    S_debbie_diane_visit = State()
    S_debbie_movie_night_two = State()
    S_debbie_romance_movie_two = State()
    S_debbie_movie_afterthoughts_two = State()
    S_debbie_night_visit_two = State()
    S_debbie_midnight_noises = State()
    S_debbie_midnight_search = State()
    S_debbie_fetch_towel = State()
    S_debbie_midnight_swim_after = State()
    S_debbie_night_visit_three = State()
    S_debbie_do_her_again = State(_("That was so hot! I should invite her to spend the night again!"))
    S_debbie_note = State()
    S_debbie_fetch_laundry = State()
    S_debbie_give_laundry = State()
    S_debbie_end = State()


    S_debbie_start.add(T_debbie_breakfast, S_debbie_relaxing, actions = ["unlocklocation", L_map, "unlocklocation", L_erikhouse])
    S_debbie_relaxing.add(T_all_school_entrance, S_debbie_overheard)
    S_debbie_overheard.add(T_debbie_check, S_debbie_debt_call,
                        actions = ["location", {"place": L_home_kitchen},
                                   "force", {"flag": True},
                                   ],
                        )
    S_debbie_debt_call.add(T_debbie_debt_help, S_debbie_lawn_delay,
                        actions = ["set", "money question",
                                   "unforce", None,
                                   ],
                        )
    S_debbie_lawn_delay.add(T_all_sleep, S_debbie_lawn_help)
    S_debbie_lawn_help.add(T_debbie_help_mow, S_debbie_fill_mower)
    S_debbie_fill_mower.add(T_debbie_filled_mower, S_debbie_mow_lawn)
    S_debbie_mow_lawn.add(T_debbie_mowed_lawn, S_debbie_clothes_dirty)
    S_debbie_clothes_dirty.add(T_debbie_sis_bitch, S_debbie_wash_clothes,
                            actions = ["location", {"place": L_home_basement},
                                       "force", {"flag": True},
                                       ],
                            )
    S_debbie_wash_clothes.add(T_debbie_clean_clothes, S_debbie_mrsj_visit_delay,
                           actions = ["unforce", None,],
                           )
    S_debbie_mrsj_visit_delay.add(T_all_sleep, S_debbie_mrsj_visit_delay,
                                  actions=('condition', ('M_anon.finished_state(S_ano02_thug)',
                                                         ('trigger', T_deb03_init), ())))
    S_debbie_mrsj_visit_delay.add(T_deb03_init, S_debbie_mrsj_visit,
                               actions = ["location", {"place": L_home},
                                          "force", {"flag": True},
                                          ],
                               )
    S_debbie_mrsj_visit.add(T_debbie_mrsj_condolences, S_debbie_pipe_delay,
                         actions = ["unforce", None,],
                         )
    S_debbie_pipe_delay.add(T_all_sleep, S_debbie_pipe_help)
    S_debbie_pipe_help.add(T_debbie_broken_pipe, S_debbie_sis_check,
                        actions = ["location", ["jenny", {"place": L_NULL}],
                                   "force", ["jenny", {"flag": True}],
                                   ],
                        )
    S_debbie_sis_check.add(T_debbie_sis_order, S_debbie_close_valve)
    S_debbie_close_valve.add(T_debbie_closed_valve, S_debbie_pipe_check)
    S_debbie_pipe_check.add(T_debbie_get_wrench, S_debbie_fix_pipe,
                         actions = ["force", ["jenny", {"tod": [0,1]}]],
                         )
    S_debbie_fix_pipe.add(T_debbie_fixed_broken_pipe, S_debbie_sis_boobs_afterthoughts,
                       actions = ["unforce", "jenny"],
                       )
    S_debbie_sis_boobs_afterthoughts.add(T_debbie_sis_nice_boobs, S_debbie_shower_delay)
    S_debbie_shower_delay.add(T_all_sleep, S_debbie_shower_peek)
    S_debbie_shower_peek.add(T_debbie_shower_admire, S_debbie_shower_peek_after)
    S_debbie_shower_peek_after.add(T_all_sleep, S_debbie_chores_delay)
    S_debbie_chores_delay.add(T_all_sleep, S_debbie_vacuum_help,
                           actions = ["set", "chores",
                                      "location", {"place": L_home_entrance},
                                      "force", {"tod":[0,1]},
                                      ],
                           )
    S_debbie_vacuum_help.add(T_all_sleep, S_debbie_vacuum_help,
                          actions = ["set", "chores"],
                          )
    S_debbie_vacuum_help.add(T_debbie_vacuumed, S_debbie_dishes_help,
                          actions = ["unforce", None,],
                          )
    S_debbie_dishes_help.add(T_all_sleep, S_debbie_dishes_help,
                          actions = ["set", "chores"],
                          )
    S_debbie_dishes_help.add(T_debbie_washed_dishes, S_debbie_laundry_help,
                           actions = ["location", {"place": L_home_basement},
                                      "force", {"tod":[0,1]},
                                      ],
                           )
    S_debbie_laundry_help.add(T_all_sleep, S_debbie_laundry_help,
                           actions = ["set", "chores"],
                           )
    S_debbie_laundry_help.add(T_debbie_cleaned_laundry, S_debbie_lotion_adventure,
                           actions = ["clear", "bedroom locked",
                                      "set", "fetch lotion",
                                      ],
                           )
    S_debbie_lotion_adventure.add(T_debbie_lotion_applied, S_debbie_search_panties,
                           actions = ["clear", "fetch lotion",
                                      "clear", "retrieved lotion",
                                      "set", "panties available",
                                      "unforce", None,
                                      ],
                           )
    S_debbie_search_panties.add(T_debbie_steal_panties, S_debbie_panties_masturbation,
                             actions = ["clear", "bed locked"],
                             )
    S_debbie_panties_masturbation.add(T_debbie_caught_masturbating, S_debbie_movie_night,
                                   actions = ["clear", "panties available",
                                              "location", {"place": L_home_entrance},
                                              "force", {"tod": 2},
                                              ],
                                   )
    S_debbie_movie_night.add(T_debbie_movie_invite, S_debbie_romance_movie,
                          actions = ["clear", "panties available",
                                     "location", {"place": L_home_livingroom},
                                     "force", {"flag": True},
                                     ],
                          )
    S_debbie_romance_movie.add(T_debbie_watch_movie, S_debbie_movie_afterthoughts,
                            actions = ["unforce", None,],
                            )
    S_debbie_movie_afterthoughts.add(T_debbie_movie_night_finish, S_debbie_hang_out)
    S_debbie_hang_out.add(T_debbie_hang_out_accept, S_debbie_mall_outing)
    S_debbie_hang_out.add(T_debbie_hang_out_refuse, S_debbie_hang_out_return)
    S_debbie_hang_out_return.add(T_debbie_hang_out_accept, S_debbie_mall_outing)
    S_debbie_mall_outing.add(T_debbie_mall_arrival, S_debbie_cupid_store)
    S_debbie_cupid_store.add(T_debbie_cupid_arrival, S_debbie_choose_gift,
                          actions = ["location", {"place": L_cupid},
                                     "force", {"flag": True},
                                     ],
                          )
    S_debbie_choose_gift.add(T_debbie_pick_necklace, S_debbie_show_necklace)
    S_debbie_show_necklace.add(T_debbie_give_necklace, S_debbie_dressing_room,
                            actions = ["location", {"place": L_cupid_dressroom},],
                            )
    S_debbie_dressing_room.add(T_debbie_dressing_room_check, S_debbie_smith_dream,
                            actions = ["set", "jerk available",
                                       "unforce", None,
                                       ],
                            )
    S_debbie_smith_dream.add(T_debbie_dream, S_debbie_spy,
                          actions = ["location", {"place": L_home_mombedroom},
                                     "force", {"flag": True},
                                     ],
                          )
    S_debbie_spy.add(T_debbie_caught_spying, S_debbie_solo_dream,
                  actions = ["set", "caught spying",
                             "unforce", None,
                             ],
                  )
    S_debbie_solo_dream.add(T_debbie_dream, S_debbie_kissing_practice)
    S_debbie_kissing_practice.add(T_debbie_kiss, S_debbie_shower_walk_in,
                               actions = ["set", "practice kissing"],
                               )
    S_debbie_shower_walk_in.add(T_debbie_shower_admire, S_debbie_car_broken)
    S_debbie_car_broken.add(T_debbie_car_help, S_debbie_check_car)
    S_debbie_check_car.add(T_debbie_check_engine, S_debbie_car_condition)
    S_debbie_car_condition.add(T_debbie_deliver_car_news, S_debbie_fix_car)
    S_debbie_fix_car.add(T_debbie_lapsed_insurance, S_debbie_car_callback)
    S_debbie_car_callback.add(T_debbie_extend_insurance, S_debbie_car_delay)
    S_debbie_fix_car.add(T_debbie_extend_insurance, S_debbie_car_delay)
    S_debbie_car_delay.add(T_all_tick, S_debbie_car_fixed)
    S_debbie_car_fixed.add(T_debbie_car_fun, S_debbie_panties_masturbation_again,
                        actions = ["set", "panties available"],
                        )
    S_debbie_panties_masturbation_again.add(T_debbie_caught_masturbating, S_debbie_night_visit,
                                         actions = ["clear", "panties available"],
                                         )
    S_debbie_night_visit.add(T_debbie_midnight_fun, S_debbie_bad_guys_revisit)
    S_debbie_bad_guys_revisit.add(T_debbie_bad_guys_beatup, S_debbie_story_delay,
                               actions = ["set", "shower random",
                                          "set", "shower sex available",
                                          ],
                               )
    S_debbie_story_delay.add(T_all_sleep, S_debbie_sleepover_offer)
    S_debbie_sleepover_offer.add(T_debbie_sleepover_accept, S_debbie_sleepover,
                              actions = ["set", "sleep together"],
                              )
    S_debbie_sleepover.add(T_all_sleep, S_debbie_sleepover_wakeup,
                              actions=['clear', ('player', 'is_virgin')])
    S_debbie_sleepover_wakeup.add(T_debbie_sleepover_morning, S_debbie_diane_visit)
    S_debbie_diane_visit.add(T_debbie_diane_chat, S_debbie_movie_night_two)
    S_debbie_movie_night_two.add(T_debbie_movie_invite, S_debbie_romance_movie_two)
    S_debbie_romance_movie_two.add(T_debbie_watch_movie, S_debbie_movie_afterthoughts_two)
    S_debbie_movie_afterthoughts_two.add(T_debbie_movie_night_finish, S_debbie_night_visit_two)
    S_debbie_night_visit_two.add(T_debbie_midnight_fun, S_debbie_midnight_noises)
    S_debbie_midnight_noises.add(T_debbie_midnight_wakeup, S_debbie_midnight_search)
    S_debbie_midnight_search.add(T_debbie_midnight_swim, S_debbie_fetch_towel,
                              actions = ["location", {"place": L_home_backyard},
                                         "force", {"tod": [2,3]},
                                         ],
                              )
    S_debbie_fetch_towel.add(T_debbie_gave_towel, S_debbie_night_visit_three,
                          actions = ["unforce", None,],
                          )
    S_debbie_midnight_swim_after.add(T_all_sleep, S_debbie_night_visit_three)
    S_debbie_night_visit_three.add(T_debbie_midnight_fun, S_debbie_do_her_again,
                                actions = ["set", "sex available",
                                           "location", {"place": L_home_mombedroom,
                                                        "condition": "M_debbie.get('sex available') and M_debbie.get('location random') == 'bedroom' and M_debbie.get('time random') == game.timer._tod",
                                                        },
                                           "force", {"tod": [0,1]},
                                           ],
                                )
    S_debbie_do_her_again.add(T_debbie_reromp, S_debbie_note)
    S_debbie_note.add(T_debbie_read_note, S_debbie_fetch_laundry,
                   actions = ["location", {"place": L_home_basement},
                              "force", {"flag": True},
                              ],
                   )
    S_debbie_fetch_laundry.add(T_debbie_got_laundry, S_debbie_give_laundry)
    S_debbie_give_laundry.add(T_debbie_basement_fun, S_debbie_end,
                           actions = ["set", "basement sex",
                                      "location", {"place": L_home_mombedroom,
                                                   "condition": "M_debbie.get('sex available') and M_debbie.get('location random') == 'bedroom' and M_debbie.get('time random') == game.timer._tod",
                                                   },
                                      "force", {"tod": [0,1]},
                                      "exec", A_end_of_chores.unlock,
                                      ],
                           )

    M_debbie.add(
        S_debbie_start, S_debbie_relaxing, S_debbie_overheard,
        S_debbie_debt_call, S_debbie_lawn_delay, S_debbie_lawn_help,
        S_debbie_fill_mower, S_debbie_mow_lawn, S_debbie_clothes_dirty,
        S_debbie_wash_clothes, S_debbie_mrsj_visit,
        S_debbie_mrsj_visit_delay, S_debbie_pipe_delay,
        S_debbie_pipe_help, S_debbie_sis_check, S_debbie_close_valve,
        S_debbie_pipe_check, S_debbie_fix_pipe,
        S_debbie_sis_boobs_afterthoughts, S_debbie_shower_delay,
        S_debbie_shower_peek, S_debbie_shower_peek_after,
        S_debbie_chores_delay, S_debbie_vacuum_help, S_debbie_dishes_help,
        S_debbie_laundry_help, S_debbie_lotion_adventure,
        S_debbie_search_panties, S_debbie_panties_masturbation,
        S_debbie_movie_night, S_debbie_romance_movie,
        S_debbie_movie_afterthoughts, S_debbie_hang_out,
        S_debbie_hang_out_return, S_debbie_mall_outing,
        S_debbie_cupid_store, S_debbie_choose_gift,
        S_debbie_show_necklace, S_debbie_dressing_room,
        S_debbie_smith_dream, S_debbie_spy, S_debbie_solo_dream,
        S_debbie_kissing_practice, S_debbie_shower_walk_in,
        S_debbie_car_broken, S_debbie_check_car, S_debbie_car_condition,
        S_debbie_fix_car, S_debbie_car_callback,
        S_debbie_car_delay, S_debbie_car_fixed,
        S_debbie_panties_masturbation_again, S_debbie_night_visit,
        S_debbie_bad_guys_revisit, S_debbie_story_delay,
        S_debbie_sleepover_offer, S_debbie_sleepover,
        S_debbie_sleepover_wakeup, S_debbie_diane_visit,
        S_debbie_movie_night_two, S_debbie_romance_movie_two,
        S_debbie_movie_afterthoughts_two, S_debbie_night_visit_two,
        S_debbie_midnight_noises, S_debbie_midnight_search,
        S_debbie_fetch_towel, S_debbie_midnight_swim_after,
        S_debbie_night_visit_three, S_debbie_do_her_again,
        S_debbie_note, S_debbie_fetch_laundry, S_debbie_give_laundry,
        S_debbie_end)

    M_debbie.add_action(T_all_sleep, ["clear", "room sneak",
                                   "clear", "movie night",
                                   "assign", ["location random", "random.choice(('bedroom', 'kitchen', 'basement'))"],
                                   "assign", ["time random", "random.choice((0, 1))"]
                                   ])
    M_debbie.set_priority(1)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
