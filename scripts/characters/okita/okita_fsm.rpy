init -1 python:
    M_okita = Machine("Okita", default_loc = [[L_school_scienceclassroom, L_school_scienceclassroom, L_school_okitaoffice, L_NULL],
                                              [L_NULL, L_NULL, L_NULL, L_NULL]
                                              ],
                      vars = {"sex speed":0.175,
                              "office locked": True,
                              "glasses assembly fail": False,
                              "belt assembly fail": False,
                              "talked with veronica": False,
                              "talked to annie": False,
                              "in augmented reality": True,
                              "repeatable unlocked": False,
                              "first time repeatable": True,
                              "Q3 completed":False,
                            },
                    )

init -3 python:

    T_okita_intro = Trigger()
    T_okita_get_keycode = Trigger()
    T_okita_keycode_acquired = Trigger()
    T_okita_entered_office = Trigger()
    T_okita_got_items = Trigger()
    T_okita_foam_misshap = Trigger()
    T_okita_get_bifocal_lenses = Trigger()
    T_okita_take_picture_judith = Trigger()
    T_okita_picture_taken = Trigger()
    T_okita_xray_perved_classroom = Trigger()
    T_okita_xray_perving_aftermath = Trigger()
    T_okita_requested_faptic_engine = Trigger()
    T_okita_faptic_get_controller = Trigger()
    T_okita_got_master_blaster_info = Trigger()
    T_okita_belt_assembled = Trigger()
    T_okita_belt_assembled_aftermath = Trigger()
    T_okita_finished_tinkering_belt = Trigger()
    T_okita_get_ingredients = Trigger()
    T_okita_got_all_ingredients = Trigger()
    T_okita_extracted_cum = Trigger()
    T_okita_brewed_serum = Trigger()
    T_okita_dosed_smith = Trigger()
    T_okita_smith_effects_seen = Trigger()
    T_okita_serum_took_effect = Trigger()
    T_okita_had_sex = Trigger()

init python:

    S_okita_start = State(_("I should start focusing on school again"))
    S_okita_intro = State(_("I wonder if there's anything I can do to fix my grade"))
    S_okita_get_keycode = State(_("Smith usually has coffee in the staff room in the afternoon"))
    S_okita_enter_office = State(_("With the code, I should be able to get into Okita's office"))
    S_okita_get_items_from_office = State(_("Okita asked me to get three things from her office..."))
    S_okita_has_items = State(_("I should bring this stuff back to Okita"))
    S_okita_foam_misshap = State(_("I'll let her get cleaned up"))
    S_okita_get_bifocal_lenses = State(_("Hmm... Who at school wears glasses?"))
    S_okita_take_picture_judith = State(_("Judith asked me to meet her at the park this afternoon"))
    S_okita_picture_taken = State(_("Now I can bring Judith's glasses to Okita"))
    S_okita_xray_perving = State(_("Okita asked me to go up to her office. I wonder why?"))
    S_okita_glasses_completed = State(_("That was weird. It's time to head home"))
    S_okita_faptic_engine = State(_("I wonder if there's anything else I can do to raise my grade"))
    S_okita_get_controller_info = State(_("June usually hangs out in the computer lab"))
    S_okita_get_controller = State(_("Erik had a Master Blaster controller once!"))
    S_okita_belt_assembled = State(_("I should meet Okita in her office like she asked"))
    S_okita_tinkering_with_belt = State(_("I'll leave her to work on the belt"))
    S_okita_tinkering_with_belt_delay = State(_("I'll leave her to work on the belt"))
    S_okita_tinkering_with_belt_delay2 = State(_("I'll leave her to work on the belt"))
    S_okita_tinkering_with_belt_delay3 = State(_("I wonder if she's figured out the issue with the belt"))
    S_okita_tired_from_belt = State(_("I'll let her rest after that..."))
    S_okita_get_ingredients = State(_("Where can I find all the stuff she wants?"))
    S_okita_extract_cum = State(_("She asked me to meet her in her office to start"))
    S_okita_start_mixing = State(_("I need to mix the serums together"))
    S_okita_dose_smith = State(_("How can I get Smith to drink her Serum"))
    S_okita_wait_for_smith_serum = State(_("What effect might that Serum have had?"))
    S_okita_wait_for_okita_serum = State(_("What effect might that Serum have had?"))
    S_okita_wait_for_okita_serum_delay = State(_("What effect might that Serum have had?"))
    S_okita_wait_for_okita_serum_delay2 = State(_("What effect might that Serum have had?"))
    S_okita_wait_for_okita_serum_delay3 = State(_("What effect might that Serum have had?"))
    S_okita_is_hypersexual = State(_("I should check to see if her Serum had any major effect"))
    S_okita_end = State()


    S_okita_start.add(T_okita_intro, S_okita_intro)
    S_okita_intro.add(T_okita_get_keycode, S_okita_get_keycode)
    S_okita_get_keycode.add(T_okita_keycode_acquired, S_okita_enter_office)
    S_okita_enter_office.add(T_okita_entered_office, S_okita_get_items_from_office)
    S_okita_get_items_from_office.add(T_okita_got_items, S_okita_has_items)
    S_okita_has_items.add(T_okita_foam_misshap, S_okita_foam_misshap)
    S_okita_foam_misshap.add(T_okita_get_bifocal_lenses, S_okita_get_bifocal_lenses, actions=["exec", "player.increase_grade_science()"])
    S_okita_get_bifocal_lenses.add(T_okita_take_picture_judith, S_okita_take_picture_judith,
                                   actions = ["location", ["judith", {"place": L_park}],
                                              "force", ["judith", {"tod": 1}],
                                             ],
                                   )
    S_okita_take_picture_judith.add(T_okita_picture_taken, S_okita_picture_taken,
                                    actions = ["unforce", "judith"],
                                    )
    S_okita_picture_taken.add(T_okita_xray_perved_classroom, S_okita_xray_perving,
                              actions = ["location", {"place": L_school_okitaoffice},
                                         "force", {"flag": True},
                                        ],
                              )
    S_okita_xray_perving.add(T_okita_xray_perving_aftermath, S_okita_glasses_completed,
                             actions = ["unforce", None],
                             )
    S_okita_glasses_completed.add(T_okita_requested_faptic_engine, S_okita_faptic_engine, actions=["exec", "player.increase_grade_science()"])
    S_okita_faptic_engine.add(T_okita_faptic_get_controller, S_okita_get_controller_info)
    S_okita_get_controller_info.add(T_okita_got_master_blaster_info, S_okita_get_controller)
    S_okita_get_controller.add(T_okita_belt_assembled, S_okita_belt_assembled,
                               actions = ["location", {"place": L_school_okitaoffice},
                                          "force", {"flag": True},
                                         ],
                               )
    S_okita_belt_assembled.add(T_okita_belt_assembled_aftermath, S_okita_tinkering_with_belt,
                               actions = ["unforce", None],
                               )
    S_okita_tinkering_with_belt.add(T_all_sleep, S_okita_tinkering_with_belt_delay)
    S_okita_tinkering_with_belt_delay.add(T_all_sleep, S_okita_tinkering_with_belt_delay2)
    S_okita_tinkering_with_belt_delay2.add(T_all_sleep, S_okita_tinkering_with_belt_delay3)
    S_okita_tinkering_with_belt_delay3.add(T_okita_finished_tinkering_belt, S_okita_tired_from_belt, actions=["exec", "player.increase_grade_science()"])
    S_okita_tired_from_belt.add(T_okita_get_ingredients, S_okita_get_ingredients,
                                actions = ["set", "Q3 completed",
                                           "unlocklocation", L_forest,
                                           "location", ["annie", {"place": L_school_smithoffice,
                                                                  "condition": "not player.has_item('tissue')",
                                                                  }
                                                        ],
                                           "force", ["annie", {"tod": 1}],
                                          ]
                                )
    S_okita_get_ingredients.add(T_okita_got_all_ingredients, S_okita_extract_cum,
                                actions = ["unforce", "annie"]
                                )
    S_okita_extract_cum.add(T_okita_extracted_cum, S_okita_start_mixing)
    S_okita_start_mixing.add(T_okita_brewed_serum, S_okita_dose_smith)
    S_okita_dose_smith.add(T_okita_dosed_smith, S_okita_wait_for_smith_serum)
    S_okita_wait_for_smith_serum.add(T_okita_smith_effects_seen, S_okita_wait_for_okita_serum)
    S_okita_wait_for_okita_serum.add(T_all_sleep, S_okita_wait_for_okita_serum_delay)
    S_okita_wait_for_okita_serum_delay.add(T_all_sleep, S_okita_wait_for_okita_serum_delay2)
    S_okita_wait_for_okita_serum_delay2.add(T_all_sleep, S_okita_wait_for_okita_serum_delay3)
    S_okita_wait_for_okita_serum_delay3.add(T_okita_serum_took_effect, S_okita_is_hypersexual)
    S_okita_is_hypersexual.add(T_okita_had_sex, S_okita_end,
                               actions=["exec", "player.increase_grade_science()",
                                        "exec", A_science_experiments.unlock,
                                        'clear', ('player', 'is_virgin')])

    M_okita.add(S_okita_start, S_okita_intro, S_okita_get_keycode,
                S_okita_enter_office, S_okita_get_items_from_office,
                S_okita_has_items, S_okita_foam_misshap,
                S_okita_get_bifocal_lenses, S_okita_take_picture_judith,
                S_okita_picture_taken, S_okita_xray_perving, S_okita_glasses_completed,
                S_okita_faptic_engine, S_okita_get_controller_info, S_okita_get_controller,
                S_okita_belt_assembled, S_okita_tinkering_with_belt,
                S_okita_tinkering_with_belt_delay, S_okita_tinkering_with_belt_delay2,
                S_okita_tinkering_with_belt_delay3, S_okita_tired_from_belt,
                S_okita_get_ingredients, S_okita_extract_cum, S_okita_start_mixing,
                S_okita_dose_smith, S_okita_wait_for_smith_serum,
                S_okita_wait_for_okita_serum, S_okita_wait_for_okita_serum_delay,
                S_okita_wait_for_okita_serum_delay2, S_okita_wait_for_okita_serum_delay3,
                S_okita_is_hypersexual, S_okita_end)

    M_okita.set_priority(1)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
