init -1 python:
    M_mia = Machine("mia", default_loc=[[L_school_scienceclassroom, L_miahouse_entrance, L_miahouse_miaroom, L_miahouse_miaroom],
                        [L_church, L_miahouse_entrance, L_miahouse_miaroom, L_miahouse_miaroom]],
                    vars = {
                        'progress count': 0,
                        'progress mark': 2,
                        'progress max': 16,
                        'front door locked': True,
                        'telescope teddy seen': False,
                        'study': False,
                        'buy donuts': False,
                        'story delay': False,
                        'helens locked room locked': True,
                        'harold left': False,
                        'helen button': False,
                        'helen button change': False,
                        'helen dialogue change': False,
                        'questioned yumi': False,
                        'questioned earl': False,
                        'church night locked': True,
                        'helen angelica training': False,
                        'helen angelica training 2': False,
                        'stolen goods recovered': False,
                        'mia route': False,
                        'sex speed': .175,
                        'sex 1st choice': "",
                        'cum 1st choice': "",
                        'anal sex': False,
                        'vaginal sex': False,
                        'butt speed': 0,
                        'reminded study': False,
                        },
    )

init -3 python:

    T_mia_on_zero = Trigger()
    T_mia_kiss = Trigger()
    T_mia_kicked_out = Trigger()
    T_mia_plan = Trigger()
    T_mia_results = Trigger()
    T_mia_delay = Trigger()
    T_mia_tattoo_start = Trigger()
    T_mia_easel_found = Trigger()
    T_mia_visit = Trigger()
    T_mia_wrong_tattoo = Trigger()
    T_mia_right_tattoo = Trigger()
    T_mia_visit_tattoo_parlor = Trigger()
    T_mia_tattoo_done = Trigger()
    T_mia_night_invite = Trigger()
    T_mia_strip_tease = Trigger()
    T_mia_afterthought = Trigger()
    T_mia_grounded = Trigger()
    T_mia_delay_progress = Trigger()
    T_mia_message = Trigger()
    T_mia_key_found = Trigger()
    T_mia_rescue = Trigger()
    T_mia_concerned = Trigger()
    T_mias_request = Trigger()
    T_mia_helen_deny = Trigger()
    T_mia_church_mention = Trigger()
    T_mia_priest_outfit = Trigger()
    T_mia_thanks = Trigger()
    T_mia_clues_summary = Trigger()
    T_mia_give_news = Trigger()
    T_mia_gives_glasses = Trigger()
    T_mia_dinner_plan = Trigger()
    T_mia_route = Trigger()
    T_mia_family_reunion = Trigger()
    T_mia_sex = Trigger()
    T_mia_stay_alone = Trigger()
    T_yumi_backup_request = Trigger()

init python:

    S_mia_start = State(_("Welcoming MC back from his"))
    S_mia_do_homework = State(_("Waiting for MC to catch up on homework"))
    S_mia_wait_homework = State(_("Waiting for MC to bring the finished homework"))
    S_mia_parent_blocking = State(_("Helen prevents you from visiting Mia"))
    S_mia_consult = State(_("Consult with Mia to be able to do night study sessions again"))
    S_mia_impress_harold = State(_("Impress Harold by finding his favorite donut"))
    S_mia_parent_unblock = State(_("Find out if from Mia if you were unbanned"))
    S_mia_tattoo_help = State(_("Mia wants me to visit her in the evening."))
    S_mia_tattoo_idea = State(_("Help Mia get a tattoo, huh? Well, I do my best thinking in my bedroom..."))
    S_mia_find_easel = State(_("Find an easel to draw a tattoo for Mia"))
    S_mia_draw_tattoo = State(_("Draw a tattoo for Mia"))
    S_mia_show_tattoo = State(_("Show Mia the tattoo you drew"))
    S_mia_get_tattoo = State(_("I promised to meet Mia at the tattoo parlor on Saturday."))
    S_mia_buy_tattoo = State(_("I hope Mia knows what she's doing. We should speak to Grace together."))
    S_mia_return_favor = State(_("Mia wants to return the favor for helping her get her tattoo"))
    S_mia_night_visit = State(_("Mia has invited you for a secret night visit"))
    S_mia_night_visit_afterthought = State(_("I should go over today's events in my room"))
    S_mia_strip_aftermath = State(_("Talk to Mia to find out what happend after she was caught"))
    S_mia_midnight_call = State(_("Mia sent you a message"))
    S_mia_midnight_help = State(_("Go to Mia and see why she needs help"))
    S_mia_locked_room = State(_("Enter the secret locked room"))
    S_mia_need_space = State(_("Best to leave Mia and her parents alone for now"))
    S_mia_concerning_visit = State(_("You've decided to visit Mia since you haven't heard from her"))
    S_mia_helen_fight = State(_("Mia has a fight with Helen"))
    S_mia_helen_talk = State(_("Mia asked you to try talk to Helen"))
    S_mia_helen_refusal = State(_("Helen refused to talk to you"))
    S_mia_church_plan = State(_("Go to church to see if there's a way to convince Helen"))
    S_mia_convince_helen = State(_("Go to the confessional to talk to Helen"))
    S_mia_priest_act = State(_("Act as a priest to try convince Helen"))
    S_mia_return_priest_outfit = State(_("Return the priest outfit to the nun's chambers"))
    S_mia_nun_thoughts = State(_("You go over the predicament the nun has put you in"))
    S_mia_helen_change_news = State(_("You tell Mia the good news that Helen is willing to change"))
    S_mia_waiting_for_harold = State(_("Mia and Helen are waiting for Harold to return"))
    S_mia_urgent_message = State(_("You wake up to an urgent message from Mia"))
    S_mia_urgent_help = State(_("Mia urgently needs help finding Harold"))
    S_mia_clues = State(_("Look for clues as to where Harold dissapeared to"))
    S_mia_search_desk = State(_("Search Harold's desk for clues"))
    S_mia_find_harold = State(_("Look for Harold at Ravens Hill"))
    S_mia_harold_found_news = State(_("Return and give the news that Harold is okay"))
    S_mia_angelicas_patience = State(_("Angelica is awaiting your end of the deal"))
    S_mia_angelicas_impatience = State(_("Angelica decided to pay you a visit to remind you of your deal"))
    S_mia_church_night_visit = State(_("You visit the church at night like Angelica told you to"))
    S_mia_find_sinners = State(_("Angelica wants you to find sinners for her sacrement"))
    S_mia_church_sacrement = State(_("Go with Helen to the church to do the first sacrement"))
    S_mia_glasses_favor = State(_("Mia wants to ask you a favor to return her dads glasses"))
    S_mia_harold_gift = State(_("Go to Harold to give him his pair of glasses"))
    S_mia_inmate_status = State(_("Harold needs a status update on the inmate transfer"))
    S_mia_harold_backup = State(_("Go tell Harold that his back is needed"))
    S_mia_harold_to_the_rescue = State(_("Harold comes to rescue Yumi"))
    S_mia_harold_yumi_out = State(_("Harold and Yumi take the rest of the day off"))
    S_mia_unexpected_visit = State(_("You pay Mia an unexpected visit"))
    S_mia_helen_outfit_request = State(_("Helen has asked you to buy her a sexy lingerie outfit"))
    S_mia_angelicas_delay = State(_("Angelica will contact you in the morning"))
    S_mia_angelicas_home_visit = State(_("Angelica visits your home to tell you part 2 of her sacrement"))
    S_mia_angelicas_order = State(_("Angelica has ordered you to acquire a whip for her"))
    S_mia_angelicas_whip = State(_("Angelica requires a whip"))
    S_mia_helen_condition = State(_("You are worried about Helen's condition after her whipping"))
    S_mia_favor = State(_("Mia has a favor to ask of you"))
    S_mia_convince_harold = State(_("You need to try convince Harold to go to dinner with Mia and Helen"))
    S_mia_stolen_goods = State(_("Harold needs to find the stolen goods of a thief for a promotion"))
    S_mia_return_goods = State(_("You should return the stolen goods to Harold"))
    S_mia_angelicas_final_delay = State(_("Angelica will contact you in the morning"))
    S_mia_angelicas_final_home_visit = State(_("Angelica visits your home to tell you the final part of her sacrement"))
    S_mia_harolds_thoughts = State(_("You want to ask Harold about his relationship with Helen before you do the final sacrament"))
    S_mia_angelicas_final_request = State(_("You've decided to listen to Angelica's final request"))
    S_mia_helens_final_sacrament = State(_("You are now attending the final sacrament for Helen"))

    S_mia_route_split = State(_("With Helen \"saved\" I should see if it's made a difference to Mia's family."))
    S_mia_study_sex = State(_("Mia has a new study trick that she wants to try in the evening."))
    S_mia_end = State(_("The end of Mia's route"))























    S_mia_start.add(T_all_school_entrance, S_mia_do_homework,
                    actions = ["assign", ["homework", 1],
                               "unlocklocation", L_miahouse,
                               "location", {"place": L_miahouse},
                               "force", {"tod": 1},
                               ],
                    )
    S_mia_do_homework.add(T_mc_homework, S_mia_do_homework,
                          actions = ["triggerOnZero", ["homework", T_mia_on_zero],],
                          )
    S_mia_do_homework.add(T_mia_on_zero, S_mia_wait_homework,
                          actions = ["clear", "front door locked",
                                     "inc", "progress count",
                                     "unforce", None,
                                     ],
                          )
    S_mia_wait_homework.add(T_mia_kiss, S_mia_parent_blocking,
                            actions = ["set", "study",
                                       "inc", "progress count",],
                            )
    S_mia_parent_blocking.add(T_mia_kicked_out, S_mia_consult)
    S_mia_consult.add(T_mia_plan, S_mia_impress_harold,
                      actions = ["set", "buy donuts",
                                 "unlocklocation", L_donutshop,
                                 ],
                      )
    S_mia_impress_harold.add(T_harold_donuts, S_mia_parent_unblock)
    S_mia_parent_unblock.add(T_mia_results, S_mia_tattoo_help,
                             actions = ["inc", "progress count"]
                             )
    S_mia_tattoo_help.add(T_mia_delay, S_mia_tattoo_idea,
                             actions = ["set", "story delay"]
                             )
    S_mia_tattoo_idea.add(T_mia_tattoo_start, S_mia_find_easel,
                          actions = ["clear", "story delay"]
                          )
    S_mia_find_easel.add(T_mia_easel_found, S_mia_draw_tattoo)
    S_mia_draw_tattoo.add(T_mia_visit, S_mia_show_tattoo)
    S_mia_show_tattoo.add(T_mia_wrong_tattoo, S_mia_draw_tattoo)
    S_mia_show_tattoo.add(T_mia_right_tattoo, S_mia_get_tattoo,
                          actions = ["inc", "progress count",
                                     "unlocklocation", L_tattooparlor,
                                     "location", {"place": L_tattooparlor_interior,
                                                  "dow": 5,
                                                  },
                                     "force", {"tod": [0,1]},
                                     ],
                          )
    S_mia_get_tattoo.add(T_mia_visit_tattoo_parlor, S_mia_buy_tattoo)
    S_mia_buy_tattoo.add(T_mia_tattoo_done, S_mia_return_favor,
                         actions = ["unforce", None]
                         )
    S_mia_return_favor.add(T_mia_night_invite, S_mia_night_visit)
    S_mia_night_visit.add(T_mia_strip_tease, S_mia_strip_aftermath,
                          actions = ["inc", "progress count","exec", "game.lock_sleep()",]
                          )
    S_mia_strip_aftermath.add(T_mia_grounded, S_mia_midnight_call,
                              actions = ["clear", "story delay",
                                         "exec", "game.unlock_sleep()",
                                         ],
                              )
    S_mia_midnight_call.add(T_mia_message, S_mia_midnight_help,
                            actions = ["location", {"place": L_miahouse_lockedroom},
                                       "force", {"tod": [2,3]},
                                       "location", ["helen", {"place": L_NULL}],
                                       "force", ["helen", {"tod": 3}],
                                       ],
                            )
    S_mia_midnight_help.add(T_mia_key_found, S_mia_locked_room,
                            actions = ["clear", "helens locked room locked"]
                            )
    S_mia_locked_room.add(T_mia_rescue, S_mia_need_space,
                          actions = ["assign", ["Trigger delay", 4],
                                     "inc", "progress count",
                                     "unforce", None,
                                     "unforce", "helen",
                                     ],
                          )
    S_mia_need_space.add(T_all_sleep, S_mia_need_space,
                         actions = ["triggerOnZero", ["Trigger delay", T_mia_concerned]]
                         )
    S_mia_need_space.add(T_mia_concerned, S_mia_concerning_visit)
    S_mia_concerning_visit.add(T_harold_leaves, S_mia_helen_fight,
                               actions = ["set", "harold left",
                                          "location", ["helen", {"place": L_miahouse_helensbedroom}],
                                          "force", ["helen", {"tod": [2,3]}],
                                          "location", ["harold", {"place": [[L_police_office, L_police_office, L_NULL, L_NULL], [L_police_office, L_police_office, L_NULL, L_NULL]]}],
                                          "force", ["harold", {"flag": True}],
                                          ],
                               )
    S_mia_helen_fight.add(T_mias_request, S_mia_helen_talk)
    S_mia_helen_talk.add(T_mia_helen_deny, S_mia_helen_refusal,
                         actions = ["set", "helen button",
                                    "set", "helen button change",
                                    ],
                         )
    S_mia_helen_refusal.add(T_mia_church_mention, S_mia_church_plan,
                            actions = ["inc", "progress count"]
                            )
    S_mia_church_plan.add(T_mia_priest_outfit, S_mia_convince_helen)
    S_mia_convince_helen.add(T_helen_confessional, S_mia_priest_act,
                             actions=('location', ('helen', {'place': L_NULL}),
                                      'force', ('helen', {'flag': True}),
                                      'location', ('keeves', {'place': L_NULL}),
                                      'force', ('keeves', {'flag': True}),
                                      'location', ('angelica', {'place': L_NULL}),
                                      'force', ('angelica', {'flag': True})))
    S_mia_priest_act.add(T_helen_convince_fail, S_mia_church_plan,
                         actions=('unforce', 'keeves',
                                  'unforce', 'angelica',
                                  'location', ('helen', {'place': L_miahouse_helensbedroom}),
                                  'force', ('helen', {'tod': [2,3]})))
    S_mia_priest_act.add(T_helen_convince_change, S_mia_return_priest_outfit,
                         actions = ["set", "helen dialogue change",
                                    "location", ["helen", {"place": L_miahouse_helensbedroom}],
                                    "force", ["helen", {"tod": [2,3]}],
                                    ],
                         )
    S_mia_return_priest_outfit.add(T_mia_priest_outfit, S_mia_nun_thoughts,
                                   actions=('unforce', 'keeves',
                                            'unforce', 'angelica',
                                            "clear", "helen button change"))
    S_mia_nun_thoughts.add(T_mc_nun_thoughts, S_mia_helen_change_news,
                           actions = ["inc", "progress count"]
                           )
    S_mia_helen_change_news.add(T_mia_thanks, S_mia_waiting_for_harold,
                                actions = ["assign", ["Trigger delay", 3]]
                                )
    S_mia_waiting_for_harold.add(T_all_sleep, S_mia_waiting_for_harold,
                                 actions = ["triggerOnZero", ["Trigger delay", T_mia_on_zero]]
                                 )
    S_mia_waiting_for_harold.add(T_mia_on_zero, S_mia_urgent_message,
                                 actions = ["inc", "progress count", "exec", "game.lock_sleep()"]
                                 )
    S_mia_urgent_message.add(T_mia_message, S_mia_urgent_help,
                             actions=('location', {'place': L_miahouse_entrance},
                                      'force', {'flag': True},
                                      'location', ['harold', {'place': L_hill}],
                                      'exec', 'game.unlock_sleep()'))
    S_mia_urgent_help.add(T_harold_missing, S_mia_clues)
    S_mia_clues.add(T_mia_clues_summary, S_mia_search_desk,
                    actions = ["clear", "questioned yumi",
                               "clear", "questioned earl",
                               ],
                    )
    S_mia_search_desk.add(T_harold_photo_clue, S_mia_find_harold)
    S_mia_find_harold.add(T_harold_found, S_mia_harold_found_news)
    S_mia_harold_found_news.add(T_mia_give_news, S_mia_angelicas_patience,
                                actions=('unforce', None,
                                         "assign", ["Trigger delay", 3],
                                         "inc", "progress count",
                                         "location", ("harold", {"place": [[L_police_office,
                                                                            L_police_office,
                                                                            L_NULL,
                                                                            L_NULL]]})))
    S_mia_angelicas_patience.add(T_all_sleep, S_mia_angelicas_patience,
                                 actions = ["triggerOnZero", ["Trigger delay", T_mia_on_zero]]
                                 )
    S_mia_angelicas_patience.add(T_mia_on_zero, S_mia_angelicas_impatience)
    S_mia_angelicas_impatience.add(T_angelica_house_visit, S_mia_church_night_visit,
                                   actions = ["clear", "church night locked"]
                                   )
    S_mia_church_night_visit.add(T_angelica_ritual_deal, S_mia_find_sinners)
    S_mia_find_sinners.add(T_helen_secret_sacrement, S_mia_church_sacrement,
                           actions = ["inc", "progress count"]
                           )
    S_mia_church_sacrement.add(T_helen_angelica_ritual, S_mia_glasses_favor,
                               actions = ["set", "helen angelica training",
                                          "set", "church night locked"]
                               )
    S_mia_glasses_favor.add(T_mia_gives_glasses, S_mia_harold_gift)
    S_mia_harold_gift.add(T_harold_glasses, S_mia_inmate_status,
                          actions = ["set", "harold left",
                                     "location", ["yumi", {"place":L_NULL}],
                                     "force", ["yumi", {"flag": True}],
                                     ],
                          )
    S_mia_inmate_status.add(T_yumi_backup_request, S_mia_harold_backup)
    S_mia_harold_backup.add(T_harold_grows_a_pair, S_mia_harold_to_the_rescue)
    S_mia_harold_to_the_rescue.add(T_harold_backup, S_mia_harold_yumi_out,
                                   actions = ["location", ["harold", {"place": L_NULL}],
                                              "unforce", M_earl,
                                              ],
                                   )
    S_mia_harold_yumi_out.add(T_all_sleep, S_mia_unexpected_visit,
                              actions = ["inc", "progress count",
                                         "location", {"place": L_NULL},
                                         "force", {"tod": [1,2,3]},
                                         "force", ["helen", {"tod": [1,2,3]}],
                                         "location", ["harold", {"place": [[L_police_office, L_police_office, L_NULL, L_NULL], [L_police_office, L_police_office, L_NULL, L_NULL]]}],
                                         "unforce", "yumi",
                                         ],
                              )
    S_mia_unexpected_visit.add(T_helen_caught_masturbating, S_mia_helen_outfit_request)
    S_mia_helen_outfit_request.add(T_helen_sexy_lingerie, S_mia_angelicas_delay,
                                   actions = ["unforce", None,
                                              "force", ["helen", {"tod": [2,3]}],
                                              ],
                                   )
    S_mia_angelicas_delay.add(T_all_sleep, S_mia_angelicas_home_visit)
    S_mia_angelicas_home_visit.add(T_angelica_requires_whip, S_mia_angelicas_order,
                                   actions = ["clear", "church night locked",
                                              "location", ["helen", {"place": L_church_angelica}],
                                              ],
                                   )
    S_mia_angelicas_order.add(T_angelica_sinful_thoughts, S_mia_angelicas_whip,
                              actions = ["set", "helen angelica training 2",],
                              )
    S_mia_angelicas_whip.add(T_helen_torture, S_mia_helen_condition,
                             actions = ["inc", "progress count",
                                        "location", ["helen", {"condition": "M_mia.is_set('helen angelica training 2')"}],
                                        ],
                             )
    S_mia_helen_condition.add(T_helen_thanks, S_mia_favor)
    S_mia_favor.add(T_mia_dinner_plan, S_mia_convince_harold)
    S_mia_convince_harold.add(T_harold_find_goods, S_mia_stolen_goods,
                              actions = ["condition", ["M_mia.is_set('stolen goods recovered')", ["trigger", T_harold_found_goods], []]]
                              )
    S_mia_stolen_goods.add(T_harold_found_goods, S_mia_return_goods,
                           actions = ["set", "stolen goods recovered"]
                           )
    S_mia_return_goods.add(T_harold_promotion, S_mia_angelicas_final_delay,
                           actions = ["inc", "progress count"]
                           )
    S_mia_angelicas_final_delay.add(T_all_sleep, S_mia_angelicas_final_home_visit)
    S_mia_angelicas_final_home_visit.add(T_angelica_strapon_request, S_mia_harolds_thoughts)
    S_mia_harolds_thoughts.add(T_harold_indecisiveness, S_mia_angelicas_final_request)
    S_mia_angelicas_final_request.add(T_angelicas_final_ritual, S_mia_helens_final_sacrament,
                                      actions = ["inc", "progress count"]
                                      )
    S_mia_helens_final_sacrament.add(T_mia_route, S_mia_route_split,
                                     actions = ["set", "mia route",
                                                "clear", "harold left",
                                                "clear", "helen angelica training",
                                                "clear", "helen angelica training 2",
                                                "unforce", "helen",
                                                "unforce", "harold",
                                                ],
                                     )
    S_mia_helens_final_sacrament.add(T_helen_route, S_mia_helens_final_sacrament,
                                     actions=('priority', 0))


    S_mia_route_split.add(T_mia_family_reunion, S_mia_study_sex)
    S_mia_study_sex.add(T_mia_sex, S_mia_end,
                        actions = ["inc", "progress count",
                                   "exec", A_not_a_prude.unlock,
                                   'clear', ('player', 'is_virgin')]
                        )


    M_mia.add(S_mia_start, S_mia_do_homework, S_mia_wait_homework,
              S_mia_parent_blocking, S_mia_consult, S_mia_impress_harold,
              S_mia_parent_unblock, S_mia_tattoo_help, S_mia_tattoo_idea,
              S_mia_find_easel, S_mia_draw_tattoo, S_mia_show_tattoo,
              S_mia_get_tattoo, S_mia_buy_tattoo, S_mia_return_favor,
              S_mia_night_visit, S_mia_night_visit_afterthought, S_mia_strip_aftermath,
              S_mia_midnight_call, S_mia_midnight_help, S_mia_locked_room,
              S_mia_need_space, S_mia_concerning_visit, S_mia_helen_fight,
              S_mia_helen_talk, S_mia_helen_refusal, S_mia_church_plan,
              S_mia_convince_helen, S_mia_priest_act,
              S_mia_return_priest_outfit, S_mia_nun_thoughts,
              S_mia_helen_change_news, S_mia_waiting_for_harold,
              S_mia_urgent_message, S_mia_urgent_help, S_mia_clues,
              S_mia_search_desk, S_mia_find_harold,
              S_mia_harold_found_news, S_mia_angelicas_patience,
              S_mia_angelicas_impatience, S_mia_church_night_visit,
              S_mia_find_sinners, S_mia_church_sacrement,
              S_mia_glasses_favor, S_mia_harold_gift, S_mia_inmate_status,
              S_mia_harold_backup, S_mia_harold_to_the_rescue,
              S_mia_harold_yumi_out, S_mia_unexpected_visit,
              S_mia_helen_outfit_request, S_mia_angelicas_delay,
              S_mia_angelicas_home_visit, S_mia_angelicas_order,
              S_mia_angelicas_whip, S_mia_helen_condition, S_mia_favor,
              S_mia_convince_harold, S_mia_stolen_goods,
              S_mia_return_goods, S_mia_angelicas_final_delay,
              S_mia_angelicas_final_home_visit, S_mia_harolds_thoughts,
              S_mia_angelicas_final_request, S_mia_helens_final_sacrament,
              S_mia_route_split, S_mia_study_sex, S_mia_end
        )
    M_mia.set_priority(1)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
