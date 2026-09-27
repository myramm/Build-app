init -1 python:
    M_diane = Machine("diane", default_loc = [[L_diane_garden, L_diane_garden, L_diane_bedroom, L_diane_bedroom]],
                      vars = {"sex speed": .4,
                              "previous outfit": "naked",
                              "wearing cow outfit": False,
                              "garden first time": True,
                              "aunt drink made":False,
                              "aunt_drink_made": False,
                              "change angle": False,
                              "acquired milk": False,
                              "random drink": "Martini",
                              "first boobjob": True,
                              "first cucumber": True,
                              "change partner": False,
                              "cum inside": False,
                              "breed first time": True,
                              "3way first time":True,
                              "refused 3way": False,
                              "seen_shed_locked": False,
                              "sex_pre_milking": False,
                              "diaXX_cowsuit_ivy": False,
                              },
                      default_pregnancy_schedule = {"": LocationSchedule([[L_diane_barn_interior, L_diane_barn_interior, L_home_livingroom, L_home_livingroom]]),
                                                    "_pregnant_bump":  LocationSchedule([[L_diane_barn_interior, L_diane_barn_interior, L_home_livingroom, L_home_livingroom]]),
                                                    "_pregnant_belly": LocationSchedule([[L_diane_barn_interior, L_diane_barn_interior, L_home_livingroom, L_home_livingroom]]),
                                                    "_baby_girl": LocationSchedule([[L_diane_barn_interior, L_diane_barn_interior, L_home_livingroom, L_home_livingroom]]),
                                                    "_baby_boy": LocationSchedule([[L_diane_barn_interior, L_diane_barn_interior, L_home_livingroom, L_home_livingroom]]),
                                                    "_baby_twins": LocationSchedule([[L_diane_barn_interior, L_diane_barn_interior, L_home_livingroom, L_home_livingroom]])},
                      pregnancy_chance=0.6,
    )

init -3 python:
    T_dia01_init = Trigger()
    T_dia01_find = Trigger()
    T_dia01_give = Trigger()
    T_dia01_work = Trigger()

    T_dia02_pass = Trigger()
    T_dia02_fail = Trigger()
    T_dia02_done = Trigger()

    T_dia03_init = Trigger()
    T_dia03_milk = Trigger()
    T_dia03_give = Trigger()
    T_dia03_stow = Trigger()
    T_dia03_wrap = Trigger()


    T_diane_help_carry_to_bed = Trigger()
    T_diane_find_cold_towel = Trigger()
    T_diane_found_cold_towel = Trigger()
    T_diane_nip_slip_n_dip = Trigger()


    T_diane_fix_infested_garden = Trigger()
    T_diane_cleaned_garden = Trigger()
    T_diane_clean_garden_reported = Trigger()
    T_diane_arrived_at_mall = Trigger()
    T_diane_entered_consumr = Trigger()
    T_diane_find_correct_bug_spray = Trigger()
    T_diane_use_bug_spray_on_garden = Trigger()
    T_diane_inform_diane = Trigger()


    T_diane_check_on_garden = Trigger()
    T_diane_search_kitchen = Trigger()
    T_diane_cucumber_aftermath = Trigger()
    T_diane_worked_on_garden = Trigger()


    T_diane_chat_at_home = Trigger()
    T_diane_find_pump = Trigger()
    T_diane_found_pump = Trigger()
    T_diane_brought_pump = Trigger()


    T_diane_get_delivery_2_task = Trigger()
    T_diane_found_delivery_2_goods = Trigger()
    T_diane_make_delivery_2 = Trigger()
    T_diane_delivery_2_finished = Trigger()


    T_diane_getting_sleep = Trigger()
    T_diane_debbie_request = Trigger()
    T_diane_house_locked = Trigger()
    T_diane_caught_milking = Trigger()


    T_diane_dump_pump = Trigger()
    T_diane_make_drink = Trigger()
    T_diane_drunk = Trigger()
    T_diane_made_drink = Trigger()
    T_diane_gave_drink = Trigger()
    T_diane_drunken_massage = Trigger()


    T_diane_apologizing = Trigger()


    T_diane_help_her = Trigger()
    T_diane_milking_malfunction_help = Trigger()


    T_diane_debbie_overhear_conversation = Trigger()


    T_diane_get_delivery_3_task = Trigger()
    T_diane_found_delivery_3_goods = Trigger()
    T_diane_make_delivery_3 = Trigger()
    T_diane_delivery_3_got_invoice = Trigger()
    T_diane_delivery_3_finished = Trigger()
    T_diane_delivery_3_report_back = Trigger()


    T_diane_dinner_task_acquired = Trigger()
    T_diane_debbie_check_outfit = Trigger()
    T_diane_debbie_ask_fish = Trigger()
    T_diane_debbie_gave_dinner_outfit_advice = Trigger()
    T_diane_got_dinner_fish = Trigger()
    T_diane_dinner_finished = Trigger()


    T_diane_found_carpenter = Trigger()
    T_diane_asked_annie_help = Trigger()
    T_diane_find_tools = Trigger()
    T_diane_helped_annie = Trigger()
    T_diane_carpenter_agreed = Trigger()
    T_diane_informed = Trigger()
    T_diane_moved_in = Trigger()


    T_diane_barn_built = Trigger()
    T_diane_checked_out_barn = Trigger()
    T_diane_research_milk_production = Trigger()
    T_diane_bought_milk_jug = Trigger()
    T_diane_find_production_book = Trigger()
    T_diane_asked_librarian = Trigger()
    T_diane_got_production_book = Trigger()
    T_diane_gave_production_book = Trigger()


    T_diane_gotta_jack_it = Trigger()
    T_diane_learns_your_secret = Trigger()
    T_diane_breeding_partner = Trigger()
    T_diane_go_to_hospital = Trigger()
    T_diane_bathroom_sampling = Trigger()
    T_diane_cup_o_jizz = Trigger()
    T_diane_get_fertility_pills = Trigger()
    T_diane_package_block = Trigger()


    T_diane_get_outfit_package = Trigger()
    T_diane_got_outfit_package = Trigger()
    T_diane_brought_outfit_package = Trigger()


    T_diane_breeding = Trigger()


    T_diane_debbie_caught = Trigger()
    T_diane_debbie_3way = Trigger()
    T_diane_3way_finished = Trigger()

init python:
    S_dia00_init = State()
    S_dia00_done = State()


    S_dia01_init = State(_("[deb_name] mentioned that Diane needed some help in her garden."))
    S_dia01_find = State(_("Diane needs a shovel, if I recall correctly there's should be one in the garage."))
    S_dia01_give = State(_("Diane's waiting for me, I should get back there quick before it gets dark!"))
    S_dia01_work = State(_("One functional shovel, one vegetable garden ready to be worked... Time to dig in!"))
    S_dia01_done = State(_("Diane has odd gardening requirements, but hey, it pays!"))


    S_dia02_init = State(_("I wonder how Diane's getting on with her vegetable garden."), delay=5)
    S_dia02_redo = State(_("That wheelbarrow can't hold out forever! I will prevail!"), delay=1)
    S_dia02_done = State(_("Gardening in Summertime hardly feels like work. Greenfingers earning greenbacks!"), delay=3)


    S_dia03_init = State(_("Diane needs me at her house."))
    S_dia03_give = State(_("I need to head to the Pizzeria to delivery this milk."))
    S_dia03_stow = State(_("Maria's in the back waiting for me to carry in the milk."))
    S_dia03_wrap = State(_("Wow, Maria really is quite sexy... But I should return to Diane with her earnings."))
    S_dia03_done = State(_("I can't believe I got to keep the profit!"))


    S_diane_drunken_splur = State(_("I should check up Diane and her garden."), delay=1)
    S_diane_get_cold_towel = State(_("Find a glass of water for Diane in the kitchen."))
    S_diane_bring_cold_towel = State(_("Now to return to Diane."))
    S_diane_drunken_splur_aftermath = State(_("I should let her rest"))


    S_diane_bug_infested_garden = State(_("I should check up on Diane and her garden."))
    S_diane_clean_garden = State(_("I need to try to clean up that infestation!"))
    S_diane_clean_garden_report = State(_("I should tell Diane the job is done."))
    S_diane_go_to_mall = State(_("Diane and I are going to the mall."))
    S_diane_go_to_consumr = State(_("I need to look in Consum-R for bug spray."))
    S_diane_get_bug_spray = State(_("I need to get bug spray for the garden."))
    S_diane_clear_bug_infested_garden = State(_("Use the spray to clear the garden."))
    S_diane_garden_restored = State(_("Tell Diane the garden has been cleared."))


    S_diane_check_up_on_garden = State(_("I should check up on Diane and her garden."), delay=1)
    S_diane_look_in_kitchen = State(_("Diane isn't in her garden, maybe the kitchen?"))
    S_diane_seen_cucumber = State(_("Diane is certainly into some weird sex stuff"))
    S_diane_work_on_garden = State(_("Should probably work on the garden now..."))


    S_diane_get_augmentation = State(_("I'm tired, I should get some sleep..."))
    S_diane_pump_request = State(_("Diane has a small task for me."))
    S_diane_fetch_pump = State(_("The pump should be in the kitchen."))
    S_diane_return_pump = State(_("I should bring the pump back to Diane."))


    S_diane_delivery_2_task = State(_("Diane needs me at her house."), delay=3)
    S_diane_delivery_2_fetch_goods = State(_("Fetch the delivery from the shed."))
    S_diane_delivery_2 = State(_("I need to head to Annie's house for the delivery."))
    S_diane_delivery_2_done = State(_("Diane seems to be struggling to meet her delivery demands."))
    S_diane_delivery_2_resting = State(_("Diane is exhausted and needs to rest some more."))


    S_diane_d9_intro = State(_("Diane wants to talk to me in her garden"), delay=1)
    S_diane_debbie_drop_off_request = State(_("[deb_name] has something to ask of me."))
    S_diane_debbie_drop_off = State(_("[deb_name] asked me to drop something off at Diane's."))
    S_diane_check_shed_light = State(_("The shed lights are still on."))


    S_diane_ready_for_day_off = State(_("I should see what Diane is doing."), delay=1)
    S_diane_dump_pump = State(_("I should dump the content of the pump in the shed into the storage jug."))
    S_diane_daylight_drinking = State(_("I should go see what Diane is doing."))
    S_diane_make_drink = State(_("Head to the kitchen to make another drink for Diane."))
    S_diane_return_drink = State(_("Return to Diane with the drink."))
    S_diane_drunken_garden_work = State(_("Do some gardening while diane drinks the day away."))


    S_diane_drunken_shenanigans_apology = State(_("I should check up on Diane to see if she is okay."), delay=1)


    S_diane_gardening_help = State(_("Time to see if Diane needs anything again."), delay=2)
    S_diane_milking_help = State(_("Diane seemed in pain. Hurry to the shed."))


    S_diane_debbie_evening_visit = State(_("I hear something from the kitchen in the evening."), delay=1)


    S_diane_delivery_3_task = State(_("Diane has another delivery for me to do."), delay=1)
    S_diane_delivery_3_fetch_goods = State(_("Get the delivery goods from the shed."))
    S_diane_delivery_3 = State(_("Deliver the goods to the School Cafeteria."))
    S_diane_delivery_3_fetch_invoice = State(_("Annie requires a delivery invoice from Mrs. Smith."))
    S_diane_delivery_3_drop_off_goods = State(_("Hand the goods over to Annie in the School Cafeteria."))
    S_diane_delivery_3_done = State(_("Report to Diane about the delivery."))


    S_diane_debbie_dinner = State(_("[deb_name] needs my help for dinner with Diane."), delay=1)
    S_diane_meet_debbie_kitchen = State(_("I should go see [deb_name] in the kitchen"))
    S_diane_debbie_dinner_outfit = State(_("[deb_name] wants my advice on her dinner outfit."))
    S_diane_debbie_dinner_fish = State(_("I need to acquire a fish for the dinner with Diane."))
    S_diane_dinner = State(_("Time for dinner with Diane and the gang."))


    S_diane_find_carpenter = State(_("I need to look for a carpenter to help build the barn. Diane may know who to ask."), delay=1)
    S_diane_ask_help_annie = State(_("I need to help Annie's dad to build some tools before he can work on Diane's barn."))
    S_diane_help_annie = State(_("In exchange for carpenting services, I need to help Annie."))
    S_diane_build_toys = State(_("Time to build some toys!"))
    S_diane_inform_carpenter = State(_("Inform the carpenter that my end of the deal is completed."))
    S_diane_couch_crashing = State(_("I hear some noises coming from the living room in the evening."))


    S_diane_barn_news = State(_("Diane has news about the barn."), delay=7)
    S_diane_check_barn_out = State(_("Let's check the progress on Diane's barn!"))
    S_diane_get_milk_jug = State(_("I need a milk jug from Consum-R."))
    S_diane_buy_milk_jug = State(_("I need a milk jug from Consum-R."))
    S_diane_increase_milk_production = State(_("Diane needs my help to find out how to increase milk production."))
    S_diane_production_ask_librarian = State(_("I should ask the librarian if the Library has a book on how to increase production."))
    S_diane_check_bookshelf = State(_("The librarian says the book is on the shelf."))
    S_diane_return_production_book = State(_("Time to return the book to Diane."))


    S_diane_peeking = State(_("NB! [deb_name]'s story needs to be complete for this."), delay=2)
    S_diane_peeking_masturbate = State(_("Time to beat the meat!"))
    S_diane_breeding_candidate = State(_("Diane has an idea that she wants to run by me."))
    S_diane_barn_checkup = State(_("Diane told me to meet her at the Barn"))
    S_diane_jizz_checkup = State(_("I should head to the hospital for a checkup."))
    S_diane_jizz_checkup_extra_hand = State(_("Need to head into the bathroom to get that sample."))
    S_diane_checkup_results = State(_("Head on back to Diane with the results."))


    S_diane_outfit_package = State(_("I should check up on Diane at the Barn"), delay=1)
    S_diane_get_outfit_package = State(_("I need to collect the package for Diane from the Pink store."))
    S_diane_return_outfit_package = State(_("Head on to Diane to hand over the package."))


    S_diane_milk_production_increase = State(_("Diane wants to explain how to increase her milk production."))


    S_diane_risky_frisky_kinky = State(_("Diane wants to explain how to increase her milk production."))
    S_diane_get_dirty_with_debbie = State(_("I can't believe I'm about to ride the tricycle!"))
    S_diane_3way_aftermath = State(_("Smells good! [deb_name] is probably cooking me breakfast in the kitchen."))


    S_diane_end = State()

init python:
    S_dia00_init.add(T_debbie_breakfast, S_dia00_done)
    S_dia00_done.add(T_all_tick, S_dia01_init,
                     actions=('priority', 1))


    S_dia01_init.add(T_dia01_init, S_dia01_find)
    S_dia01_find.add(T_dia01_find, S_dia01_give)
    S_dia01_give.add(T_dia01_give, S_dia01_work)
    S_dia01_work.add(T_dia01_work, S_dia01_done)
    S_dia01_done.add(T_all_sleep, S_dia02_init)


    S_dia02_init.add(T_dia02_pass, S_dia02_done)
    S_dia02_init.add(T_dia02_fail, S_dia02_redo)
    S_dia02_redo.add(T_dia02_pass, S_dia02_done)
    S_dia02_redo.add(T_dia02_fail, S_dia02_redo,
                     actions=('exec', 'setattr(S_dia02_redo, "delay", 1)'))
    S_dia02_done.add(T_all_sleep, S_dia02_done,
                     actions=('condition', ('M_anon.finished_state(S_ano04_tony)',
                                            ('trigger', T_dia02_done))))
    S_dia02_done.add(T_dia02_done, S_dia03_init)


    S_dia03_init.add(T_dia03_init, S_dia03_give,
                     actions=('location', ('tony', {'place': L_pizzeria_interior}),
                              'force', ('tony', {'flag': True}),
                              'location', ('maria', {'place': L_pizzeria_kitchen}),
                              'force', ('maria', {'flag': True})))
    S_dia03_give.add(T_dia03_give, S_dia03_stow)
    S_dia03_stow.add(T_dia03_stow, S_dia03_wrap,
                     actions=('unforce', 'tony',
                              'unforce', 'maria'))
    S_dia03_wrap.add(T_dia03_wrap, S_dia03_done)
    S_dia03_done.add(T_all_sleep, S_diane_drunken_splur)


    S_diane_drunken_splur.add(T_diane_help_carry_to_bed, S_diane_get_cold_towel,
                              actions=("location", {"place": L_diane_bedroom},
                                       "force", {"tod": [0,1]},
                                       "unlocklocation", L_diane_kitchen,
                                       "unlocklocation", L_diane_home))
    S_diane_get_cold_towel.add(T_diane_found_cold_towel, S_diane_bring_cold_towel)
    S_diane_bring_cold_towel.add(T_diane_nip_slip_n_dip, S_diane_drunken_splur_aftermath)
    S_diane_drunken_splur_aftermath.add(T_all_sleep, S_diane_bug_infested_garden,
                                        actions = ["location", {"place": L_diane_shed},
                                                   "force", {"tod": [0,1]},
                                                   ]
                                        )


    S_diane_bug_infested_garden.add(T_diane_fix_infested_garden, S_diane_clean_garden)
    S_diane_clean_garden.add(T_diane_cleaned_garden, S_diane_clean_garden_report)
    S_diane_clean_garden_report.add(T_diane_clean_garden_reported, S_diane_go_to_mall)
    S_diane_go_to_mall.add(T_diane_arrived_at_mall, S_diane_go_to_consumr)
    S_diane_go_to_consumr.add(T_diane_entered_consumr, S_diane_get_bug_spray)
    S_diane_get_bug_spray.add(T_diane_find_correct_bug_spray, S_diane_clear_bug_infested_garden)
    S_diane_clear_bug_infested_garden.add(T_diane_use_bug_spray_on_garden, S_diane_garden_restored)
    S_diane_garden_restored.add(T_diane_inform_diane, S_diane_check_up_on_garden,
                                actions = ["location", {"place": L_diane_kitchen},
                                           "force", {"tod": [0,1]},
                                           ]
                                )


    S_diane_check_up_on_garden.add(T_diane_check_on_garden, S_diane_look_in_kitchen)
    S_diane_look_in_kitchen.add(T_diane_search_kitchen, S_diane_seen_cucumber,
                                actions = ["action", ["player", "set", "jerk diane"]
                                           ]
                                )
    S_diane_seen_cucumber.add(T_diane_cucumber_aftermath, S_diane_work_on_garden)
    S_diane_work_on_garden.add(T_diane_worked_on_garden, S_diane_get_augmentation,
                                actions = ["unforce", None]
                                )


    S_diane_get_augmentation.add(T_diane_chat_at_home, S_diane_pump_request)
    S_diane_pump_request.add(T_diane_find_pump, S_diane_fetch_pump)
    S_diane_fetch_pump.add(T_diane_found_pump, S_diane_delivery_2_task,
                           actions = ["setdefaultloc", [[L_diane_shed, L_diane_shed, L_diane_shed, L_diane_bedroom]]]
                           )


    S_diane_delivery_2_task.add(T_diane_get_delivery_2_task, S_diane_delivery_2_fetch_goods,
                                actions = ["unlocklocation", L_annie_front,
                                           "unlocklocation", L_diane_shed,
                                           "location", {"place": L_diane_bedroom},
                                           "force", {"tod": [0,1]}
                                           ]
                                )
    S_diane_delivery_2_fetch_goods.add(T_diane_found_delivery_2_goods, S_diane_delivery_2)
    S_diane_delivery_2.add(T_diane_make_delivery_2, S_diane_delivery_2_done,
                           actions = ["location", {"place": L_diane_bedroom},
                                      "force", {"tod": [0,1,2,3]},
                                      'setdefaultloc', ('richard', [[L_annie_front] * 2 +
                                                                    [L_annie_livingroom, L_NULL]])
                                      ]
                          )
    S_diane_delivery_2_done.add(T_diane_delivery_2_finished, S_diane_delivery_2_resting)
    S_diane_delivery_2_resting.add(T_all_sleep, S_diane_d9_intro,
                                   actions = ["unforce", None]
                                   )


    S_diane_d9_intro.add(T_diane_getting_sleep, S_diane_debbie_drop_off_request, actions=["setdefaultoutfit", [["shirtless","shirtless","shirtless","shirtless"]]])
    S_diane_debbie_drop_off_request.add(T_diane_debbie_request, S_diane_debbie_drop_off)
    S_diane_debbie_drop_off.add(T_diane_house_locked, S_diane_check_shed_light)
    S_diane_check_shed_light.add(T_diane_caught_milking, S_diane_ready_for_day_off)


    S_diane_ready_for_day_off.add(T_diane_dump_pump, S_diane_dump_pump,
                                  actions = ["location", {"place": L_diane_garden},
                                             "force", {"tod": [0,1]},
                                              ]
                                  )
    S_diane_dump_pump.add(T_diane_make_drink, S_diane_daylight_drinking)
    S_diane_daylight_drinking.add(T_diane_drunk, S_diane_make_drink)
    S_diane_make_drink.add(T_diane_made_drink, S_diane_return_drink)
    S_diane_return_drink.add(T_diane_gave_drink, S_diane_drunken_garden_work)
    S_diane_drunken_garden_work.add(T_diane_drunken_massage, S_diane_drunken_shenanigans_apology,
                             actions = ["unforce", None]
                             )


    S_diane_drunken_shenanigans_apology.add(T_diane_apologizing, S_diane_gardening_help)


    S_diane_gardening_help.add(T_diane_help_her, S_diane_milking_help)
    S_diane_milking_help.add(T_diane_milking_malfunction_help, S_diane_debbie_evening_visit,
                             actions = ["location", {"place": L_home_kitchen,
                                                     "condition": "not M_diane.is_set('first cucumber')",
                                                     },
                                        "force", {"tod": 2},
                                        ]
                             )


    S_diane_debbie_evening_visit.add(T_diane_debbie_overhear_conversation, S_diane_delivery_3_task,
                                     actions = ["unforce", None]
                                     )


    S_diane_delivery_3_task.add(T_diane_get_delivery_3_task, S_diane_delivery_3_fetch_goods)
    S_diane_delivery_3_fetch_goods.add(T_diane_found_delivery_3_goods, S_diane_delivery_3)
    S_diane_delivery_3.add(T_diane_make_delivery_3, S_diane_delivery_3_fetch_invoice)
    S_diane_delivery_3_fetch_invoice.add(T_diane_delivery_3_got_invoice, S_diane_delivery_3_drop_off_goods)
    S_diane_delivery_3_drop_off_goods.add(T_diane_delivery_3_finished, S_diane_delivery_3_done)
    S_diane_delivery_3_done.add(T_diane_delivery_3_report_back, S_diane_debbie_dinner)


    S_diane_debbie_dinner.add(T_diane_dinner_task_acquired, S_diane_meet_debbie_kitchen,
                              actions = ["location", ["debbie", {"place": L_home_kitchen}],
                                         "force", ["debbie", {"tod": [0,1]}],
                                         ]
                              )
    S_diane_meet_debbie_kitchen.add(T_diane_debbie_check_outfit, S_diane_debbie_dinner_outfit,
                                    actions = ["location", ["debbie", {"place": L_home_mombedroom}],
                                               "force", ["debbie", {"tod": [0,1]}],
                                               ]
                                    )
    S_diane_meet_debbie_kitchen.add(T_diane_debbie_ask_fish, S_diane_debbie_dinner_fish,
                                    actions = ["unlocklocation", L_pier,
                                               "unforce", "debbie",
                                               ]
                                    )
    S_diane_debbie_dinner_outfit.add(T_diane_debbie_gave_dinner_outfit_advice, S_diane_debbie_dinner_fish,
                                     actions = ["unlocklocation", L_pier,
                                                "unforce", "debbie",
                                                ]
                                     )
    S_diane_debbie_dinner_fish.add(T_diane_got_dinner_fish, S_diane_dinner)
    S_diane_dinner.add(T_diane_dinner_finished, S_diane_find_carpenter)


    S_diane_find_carpenter.add(T_diane_found_carpenter, S_diane_ask_help_annie,
                               actions = ["location", ["richard", {"place": L_diane_yard}],
                                          "force", ["richard", {"tod": [0,1]}],
                                          ]
                               )
    S_diane_ask_help_annie.add(T_diane_asked_annie_help, S_diane_help_annie)
    S_diane_help_annie.add(T_diane_find_tools, S_diane_build_toys)
    S_diane_build_toys.add(T_diane_helped_annie, S_diane_inform_carpenter)
    S_diane_inform_carpenter.add(T_diane_carpenter_agreed, S_diane_couch_crashing,
                                 actions = ["unforce", "richard"])
    S_diane_couch_crashing.add(T_diane_moved_in, S_diane_barn_news,
                               actions = ["setdefaultloc", [[L_diane_barn_building, L_diane_barn_building, L_home_livingroom, L_home_livingroom]],
                                          "setdefaultoutfit", [["shirtless", "shirtless", "nightgown", "nightgown"]]]
                               )


    S_diane_barn_news.add(T_diane_barn_built, S_diane_check_barn_out,
                          actions = ["unforce", None,
                                     "setdefaultloc", [[L_diane_barn_interior, L_diane_barn_interior, L_home_livingroom, L_home_livingroom]],
                                     "setdefaultoutfit", [["shirtless", "shirtless", "nightgown", "nightgown"]]
                                     ]
                          )
    S_diane_check_barn_out.add(T_diane_checked_out_barn, S_diane_get_milk_jug)
    S_diane_get_milk_jug.add(T_diane_research_milk_production, S_diane_buy_milk_jug)
    S_diane_buy_milk_jug.add(T_diane_bought_milk_jug, S_diane_increase_milk_production)
    S_diane_increase_milk_production.add(T_diane_find_production_book, S_diane_check_bookshelf)
    S_diane_check_bookshelf.add(T_diane_got_production_book, S_diane_return_production_book)
    S_diane_return_production_book.add(T_diane_gave_production_book, S_diane_peeking)


    S_diane_peeking.add(T_diane_gotta_jack_it, S_diane_peeking_masturbate, actions=["exec", "game.lock_sleep()"])
    S_diane_peeking_masturbate.add(T_diane_learns_your_secret, S_diane_breeding_candidate, actions=["exec", "game.unlock_sleep()"])
    S_diane_breeding_candidate.add(T_diane_breeding_partner, S_diane_barn_checkup)
    S_diane_barn_checkup.add(T_diane_go_to_hospital, S_diane_jizz_checkup,
                             actions = ["unlocklocation", L_hospital,
                                        "location", {"place": L_hospital_room},
                                        "force", {"tod": [0,1]},
                                        ]
                             )
    S_diane_jizz_checkup.add(T_diane_bathroom_sampling, S_diane_jizz_checkup_extra_hand,
                             actions = ["location", ["micoe", {"place": L_NULL}],
                                        "force", ["micoe", {"tod": [0,1]}],
                                        ]
                             )
    S_diane_jizz_checkup_extra_hand.add(T_diane_cup_o_jizz, S_diane_checkup_results,
                                        actions = ["unforce", None,
                                                   "unforce", "micoe",
                                                   ]
                                        )
    S_diane_checkup_results.add(T_diane_package_block, S_diane_outfit_package, actions=["priority", ["priya", 1]])


    S_diane_outfit_package.add(T_diane_get_outfit_package, S_diane_get_outfit_package)
    S_diane_get_outfit_package.add(T_diane_got_outfit_package, S_diane_return_outfit_package,
                                   actions=('assign', ('diaXX_cowsuit_ivy', 'game.timer.now')))
    S_diane_return_outfit_package.add(T_diane_brought_outfit_package, S_diane_milk_production_increase)


    S_diane_milk_production_increase.add(T_diane_breeding, S_diane_risky_frisky_kinky,
                            actions=["setdefaultoutfit", [["cow","cow","nightgown","nightgown"]],
                                     'clear', ('player', 'is_virgin')])


    S_diane_risky_frisky_kinky.add(T_diane_debbie_caught, S_diane_get_dirty_with_debbie,
                                   actions=("setdefaultloc", [[L_diane_barn_interior,
                                                               L_diane_barn_interior,
                                                               L_home_mombedroom,
                                                               L_home_livingroom]],
                                            'exec', 'game.lock_sleep()'))
    S_diane_get_dirty_with_debbie.add(T_diane_debbie_3way, S_diane_3way_aftermath,
                                      actions=('exec', 'game.unlock_sleep()',
                                               'location', ('debbie', {'place': L_home_kitchen}),
                                               'force', ('debbie', {'flag': True})))
    S_diane_3way_aftermath.add(T_diane_3way_finished, S_diane_end,
                               actions=('unforce', 'debbie',
                                        'exec', A_milky_business.unlock))


    M_diane.add(
        S_dia00_init, S_dia00_done,
        S_dia01_init, S_dia01_find, S_dia01_give, S_dia01_work, S_dia01_done,
        S_dia02_init, S_dia02_redo, S_dia02_done,
        S_dia03_init, S_dia03_give, S_dia03_stow, S_dia03_wrap, S_dia03_done,
                S_diane_drunken_splur,
                S_diane_get_cold_towel, S_diane_bring_cold_towel, S_diane_bug_infested_garden,
                S_diane_clean_garden, S_diane_clean_garden_report, S_diane_go_to_mall,
                S_diane_go_to_consumr, S_diane_get_bug_spray, S_diane_clear_bug_infested_garden,
                S_diane_garden_restored, S_diane_check_up_on_garden, S_diane_look_in_kitchen,
                S_diane_pump_request, S_diane_fetch_pump, S_diane_return_pump,
                S_diane_delivery_2_task, S_diane_delivery_2_fetch_goods, S_diane_delivery_2,
                S_diane_delivery_2_done, S_diane_delivery_2_resting, S_diane_debbie_drop_off_request,
                S_diane_debbie_drop_off, S_diane_check_shed_light, S_diane_daylight_drinking,
                S_diane_make_drink, S_diane_return_drink, S_diane_drunken_garden_work,
                S_diane_drunken_shenanigans_apology, S_diane_milking_help, S_diane_gardening_help,
                S_diane_debbie_evening_visit, S_diane_delivery_3_task, S_diane_delivery_3_fetch_goods,
                S_diane_delivery_3, S_diane_delivery_3_fetch_invoice, S_diane_delivery_3_drop_off_goods,
                S_diane_delivery_3_done, S_diane_debbie_dinner, S_diane_debbie_dinner_outfit,
                S_diane_debbie_dinner_fish, S_diane_dinner, S_diane_find_carpenter,
                S_diane_help_annie, S_diane_inform_carpenter, S_diane_get_milk_jug, S_diane_buy_milk_jug,
                S_diane_peeking_masturbate,S_diane_couch_crashing, S_diane_barn_news,
                S_diane_increase_milk_production, S_diane_production_ask_librarian, S_diane_check_bookshelf,
                S_diane_return_production_book, S_diane_peeking, S_diane_breeding_candidate,
                S_diane_jizz_checkup, S_diane_jizz_checkup_extra_hand, S_diane_checkup_results, S_diane_barn_checkup,
                S_diane_check_barn_out, S_diane_outfit_package, S_diane_return_outfit_package,
                S_diane_get_outfit_package, S_diane_milk_production_increase, S_diane_risky_frisky_kinky,
                S_diane_end, S_diane_dump_pump, S_diane_meet_debbie_kitchen,
                S_diane_seen_cucumber, S_diane_d9_intro, S_diane_ready_for_day_off, S_diane_drunken_splur_aftermath,
                S_diane_get_augmentation, S_diane_work_on_garden, S_diane_ask_help_annie, S_diane_build_toys,
                S_diane_get_dirty_with_debbie, S_diane_3way_aftermath,
                )
    M_diane.add_action(T_all_sleep, ["clear", "refused 3way",
                                     "assign", ["random drink", "random.choice(['Martini', 'Piña Colada', 'Margarita'])"],
                                     ])
    M_diane.outfit.set_default_outfit_schedule([["dressed", "dressed", "dressed", "dressed"]])
    M_diane.outfit.bind_outfit_to_location(L_home_livingroom, "nightgown")
    M_diane.outfit.bind_outfit_to_location(L_diane_shed, "shirtless")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
