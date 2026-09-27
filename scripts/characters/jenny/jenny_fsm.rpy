init -1 python:
    M_jenny = Machine("jenny", default_loc = [[L_home_diningroom, L_home_sisbedroom, L_home_sisbedroom, L_home_sisbedroom],
                                              [L_home_backyard, L_home_sisbedroom, L_home_sisbedroom, L_home_sisbedroom]],
                      vars = {"door locked": True,
                              "comp locked": True,
                              "seen MCs penis": False,
                              "sex speed": .175,
                              "first_shower": True,
                              'rng': 0,
                              "diary_progress": 2,
                              "diary_bookmark": 0,
                              "dominance": 0,
                              "j10_caught_her_leaving":False,
                              "pc_hacked": False,
                              "watched_video_ec": False,
                              "watched_video_uv": False,
                              "watched_video_bm": False,
                              "cam show mask": True,
                              'sit': True,
                              'sneak_in_chance': 0,
                              'forced_sneak_in_chance': 0,
                              'first_shower_time': True,
                              'jenny_got_first_baby': False,
                              'seen_in_shower': False,
                              'seen_in_shower_pregnant': False,
                              "didnt_see_first_baby_dialogue": True,
                              "couch_sex_first": True,
                              "had_couch_sex": False,
                              'teasin_before_sex': False,
                              'hack_pc_notice':False,
                              'went_to_her_room': False,
                              'first_time_deep_bj': True,
                              'jenny_bj_deep': True,
                              'first_sex_dining': True,
                              'force_couch_sex': False,
                              'first_sex_pool': True,
                              'pool_clothes': True,
                              'jenny_bed_cum_inside': True,
                              'jenny_girlfriend_first_time': True,
                              'girlfriend_time': False,
                              'bed_sex_first_time': True,
                              'jenny_bed_cum_inside':False,
                              'checked_diary_j22': False,
                              'girlfriend_in_progress': False,
                              'figure_out_pass_dialogue': False,
                              'had_sex_bedroom': False,
                              "videos": ('ec', 'uv'),
                              "jenXX_lite_ivy": False,
                              "photo_reaction": False,
                              "preg_afterglow": False,
                              "fertile": False
                              },
                      pregnancy_chance=0.4,
                      default_pregnancy_schedule={
                          "_baby_twins": LocationSchedule([[L_home_sisbedroom] * 4]),
                          "_baby_girl":  LocationSchedule([[L_home_sisbedroom] * 4]),
                          "_baby_boy":   LocationSchedule([[L_home_sisbedroom] * 4])}
    )

init -3 python:

    T_jenny_hallway = Trigger()
    T_jenny_spied_shower = Trigger()
    T_jenny_altercation_with_debbie = Trigger()
    T_jenny_breakfast_notice = Trigger()
    T_jenny_had_breakfast = Trigger()
    T_jenny_eavesdropped = Trigger()
    T_jenny_took_pictures = Trigger()
    T_jenny_snoop_in_her_room = Trigger()
    T_jenny_looked_at_diary = Trigger()
    T_jenny_looked_at_nightstand = Trigger()
    T_jenny_caught_snooping = Trigger()
    T_jenny_breakfast_notice_2 = Trigger()
    T_jenny_had_breakfast_2 = Trigger()
    T_jenny_pay_for_favors = Trigger()
    T_jenny_get_a_toy = Trigger()
    T_jenny_got_a_toy = Trigger()
    T_jenny_ivy_jane_leaving = Trigger()
    T_jenny_brought_back_toy = Trigger()
    T_jenny_have_breakfast = Trigger()
    T_jenny_catch_her_in_shower = Trigger()
    T_jenny_wait_a_day = Trigger()
    T_jenny_leave_house = Trigger()
    T_jenny_go_at_pinks = Trigger()
    T_jenny_buy_vibrator = Trigger()
    T_jenny_bought_vibrator = Trigger()
    T_jenny_check_laptop = Trigger()
    T_jenny_return_from_shower = Trigger()
    T_jenny_a_real_penis = Trigger()
    T_jenny_checked_pc_for_new_vids = Trigger()
    T_jenny_get_her_a_new_toy = Trigger()
    T_jenny_bought_bad_monster = Trigger()
    T_jenny_gave_bad_monster = Trigger()
    T_jenny_check_new_vid = Trigger()
    T_jenny_checked_new_vid = Trigger()
    T_jenny_talk_to_cedric = Trigger()
    T_jenny_talked_to_cedric = Trigger()
    T_jenny_cedric_didnt_call = Trigger()
    T_jenny_beaten_up_with_dildo = Trigger()
    T_jenny_spied_on_mia = Trigger()
    T_jenny_get_a_mask = Trigger()
    T_jenny_buy_mask = Trigger()
    T_jenny_bought_mask = Trigger()
    T_jenny_delivered_mask = Trigger()
    T_jenny_gave_handjob = Trigger()
    T_jenny_reconciliation_handjob = Trigger()
    T_jenny_gave_footjob  = Trigger()
    T_jenny_start_camshow_blowjob = Trigger()
    T_jenny_done_camshow_blowjob = Trigger()
    T_jenny_reconciliation_blowjob = Trigger()
    T_jenny_spied_on_tammy = Trigger()
    T_jenny_gave_cunni = Trigger()
    T_jenny_go_breakfast = Trigger()
    T_jenny_get_cheerleader_outfit = Trigger()
    T_jenny_got_cheerleader_outfit = Trigger()
    T_jenny_had_cheerleader_sex = Trigger()
    T_jenny_pool_talk = Trigger()
    T_jenny_stalked = Trigger()
    T_jenny_its_mr_bubbles = Trigger()
    T_jenny_movie_date = Trigger()
    T_jenny_righteous_punch = Trigger()
    T_jenny_didnt_sleep_much = Trigger()
    T_jenny_final_breakfast = Trigger()
    T_jenny_end = Trigger()
    T_jenny_diary_clue = Trigger()
    T_jenny_give_necklace = Trigger()
    T_jen0m_hook = Trigger()
    T_jen0m_init = Trigger()
    T_jen0m_food = Trigger()

init python:

    S_jenny_start = State(_("I'm living in the same house as she does..."))
    S_jenny_shower_spy = State(_("[jen_name] is a stuck up bitch. She has a nice body though..."))
    S_jenny_debbie_altercation = State(_("[jen_name] is not just busting my balls. She seems to get on the nerves of [deb_name] as well."), delay=1)
    S_jenny_breakfast_notice = State(_("Something smells good downstairs"), delay=2)
    S_jenny_have_breakfast = State(_("I should have some breakfast downstairs."))
    S_jenny_hallway_eavesdropping = State(_("[jen_name] is up to something... I don't know what though."), delay=2)
    S_jenny_sluttygram_pics = State(_("I hear [jen_name] eating in the {b}dining room{/b} downstairs."), delay=3)
    S_jenny_pics_afterthought = State(_("I can't believe that just happened!"))
    S_jenny_snoop_around = State(_("Mmh. I should look for the photos in her room while she showers."))
    S_jenny_snoop_diary = State(_("Can't hurt to check out her diary while I'm here."))
    S_jenny_snoop_nightstand = State(_("Maybe she keeps the camera in her nightstand."))
    S_jenny_caught_snooping = State(_("{b}[jen_name]{/b} caught me snooping around. It was costly but worth it."))
    S_jenny_breakfast_notice_2 = State(_("Something smells good {b}downstairs{/b}."), delay=3)
    S_jenny_have_breakfast_2 = State(_("Something smells good {b}downstairs{/b}."))
    S_jenny_go_to_her_room = State(_("{b}[jen_name]{/b} told me to go wait in her room for some kind of deal."))
    S_jenny_get_a_toy = State(_("{b}[jen_name]{/b} has a favor to ask me."), delay=2)
    S_jenny_go_to_pink = State(_("{b}[jen_name]{/b} wants a specific toy. She told me {b}Pink{/b}, at the mall, had it."))
    S_jenny_bring_toy_back = State(_("I should bring this {b}Electroclit Light{/b} to {b}[jen_name]{/b}."))
    S_jenny_ivy_jane_leave_pink = State(_("That toy is laying on the counter. It should be enough for {b}[jen_name]{/b}."))
    S_jenny_helping_with_breakfast = State(_("{b}[jen_name]{/b} is downstairs. I bet {b}[deb_name]{/b} is fixing her breakfast again..."), delay=2)
    S_jenny_have_breakfast_3 = State(_("At this point, I should grab a bite to eat in the {b}dining room{/b}"))
    S_jenny_confront_her_hallway = State(_("{b}[jen_name]{/b}'s going to the {b}shower{/b}, maybe I could catch her and confront her."))
    S_jenny_catch_her_leaving = State(_("{b}[jen_name]{/b} is leaving the house right now. Where is she going?"), delay=1)
    S_jenny_go_shopping = State(_("Great, now we're heading to the mall for some errands..."))
    S_jenny_shop_for_toys = State(_("She left me hanging! She said she was going to {b}Pink{/b}. It's upstairs."))
    S_jenny_buy_vibrator = State(_("I have to buy a vibrator. She mentioned the name : {b}UltraVibrator 2000{/b}."))
    S_jenny_snooping_laptop_notice = State()
    S_jenny_snoop_around_for_laptop = State(_("She's in the shower, I should sneak into her room..."))
    S_jenny_check_laptop = State(_("That laptop must have some kind of information on [jen_name]'s whereabouts."))
    S_jenny_figure_out_password = State(_("I have to figure out her password. She mentioned it in her diary... I should go at night though."))
    S_jenny_new_video_notice = State(_("Mmmh, I wonder if [jen_name] has posted a new video yet..."), delay=3)
    S_jenny_check_for_new_video = State(_("Mmmh, I wonder if [jen_name] has posted a new video yet..."))
    S_jenny_checked_for_new_video = State(_("Mmmh, I wonder if [jen_name] has posted a new video yet..."))
    S_jenny_buy_bad_monster = State(_("If I buy her a toy, she'll definitely make a new video! What's her favorite toy again?"))
    S_jenny_deliver_bad_monster = State(_("Thank god {b}Ivy{/b} had a Bad Monster in stock! I should give that to [jen_name]."))
    S_jenny_video_3_production = State(_("I should wait until tomorrow and see if {b}[jen_name]{/b} has used that bad monster."))
    S_jenny_video_3_uploaded = State(_("I should check if {b}[jen_name]{/b} has uploaded a new video with that bad monster."))
    S_jenny_cedric_upset = State(_("I should get some breakfast in the {b}dining room{/b}."), delay=2)
    S_jenny_talk_to_cedric = State(_("{b}[jen_name]{/b} wants me to talk to {b}Cedric{/b} at the {b}gym{/b}."))
    S_jenny_talked_to_cedric = State(_("I should get back home."))
    S_jenny_caught_talking_to_camslut = State(_("I should check on {b}[jen_name]{/b}..."), delay=3)
    S_jenny_spy_on_mia_telescope = State(_("I wonder what Mia is doing right now..."), delay=1)
    S_jenny_get_a_mask_quest = State(_("I should check on {b}[jen_name]{/b} in the afternoon."))
    S_jenny_get_a_mask = State(_("{b}[jen_name]{/b} asked me to buy a mask to make camshows with her."))
    S_jenny_buy_mask = State(_("{b}[jen_name]{/b} asked me to buy a mask to make camshows with her."))
    S_jenny_bought_mask = State(_("I should get this back to {b}[jen_name]{/b}."))
    S_jenny_come_back_camshow= State(_("I have to come back to {b}[jen_name]{/b} tomorrow to start the camshows."))
    S_jenny_start_camshow_handjob = State(_("{b}[jen_name]{/b} told me to come to her room to start the camshow."))
    S_jenny_pissed_at_handjob = State(_("She's pissed at me because of what happened during the camshow. I should try and talk to her."))
    S_jenny_catch_her_jilling = State(_("I should check the living room at night."), delay=2)
    S_jenny_morning_visit = State(_("I should get some sleep now..."))
    S_jenny_start_camshow_blowjob = State(_("{b}[jen_name]{/b} asked me to come to her room in the afternoon."))
    S_jenny_pissed_at_blowjob = State(_("She's pissed at me because of what happened during the camshow. I should try and talk to her."))
    S_jenny_perv_on_tammy = State(_("I wonder what Mrs Johnson's routine is like in the mornings."), delay=1)
    S_jenny_give_cunni = State()
    S_jenny_bedroom_intrusion = State(delay=1)
    S_jenny_have_breakfast_4 = State(_("{b}[jen_name]{/b} is waiting downstairs for breakfast."))
    S_jenny_get_cheerleader_outfit = State(_("{b}[jen_name]{/b} needs me to pick up her old cheerleader outfit in the attic."))
    S_jenny_cheerleader_sex = State(_("I got the cheerleader outfit, I should bring it to her."))
    S_jenny_want_some_breakfast = State(_("I should check on [jen_name] this weekend."), delay=1)
    S_jenny_pool_talk = State(_("[deb_name] asked me to talk to [jen_name]. She's by the pool on the weekends."))
    S_jenny_find_stalker = State(_("I have to find that creep! I followed him back to the mall."))
    S_jenny_ask_movie_date = State(_("Mr. Bubbles has to give out his apology to [jen_name]."))
    S_jenny_movie_date = State(_("Mr. Bubbles has to give out his apology to [jen_name]."))
    S_jenny_night_time_sex = State(_("[jen_name] told me to expect a surprise tonight, I can't wait!"))
    S_jenny_weird_relationship = State(delay=1)
    S_jenny_final_breakfast = State(_("{b}[jen_name]{/b} is having breakfast downstairs, I should go talk to her."))
    S_jenny_end = State()
    S_jenny_hallway_talk = State(_("I should check on {b}[jen_name]{/b}."), delay=3)
    S_jenny_diary_clue = State(_("I really want her to warm up to me, I should check her diary for ideas."))
    S_jenny_necklace_rebutal = State(_("{b}[jen_name]{/b} refused my gift, but she offered an alternative."))

    S_jen0m_init = State(delay=3)
    S_jen0m_food = State(_('I still can\'t believe her sometimes. Breakfast does sound like a good idea though...'))
    S_jen0m_done = State()


    S_jenny_start.add(T_jenny_hallway, S_jenny_shower_spy)
    S_jenny_shower_spy.add(T_jenny_spied_shower, S_jenny_debbie_altercation)
    S_jenny_debbie_altercation.add(T_jenny_altercation_with_debbie, S_jenny_breakfast_notice,
                                   actions=('assign', ('diary_progress', 3)))
    S_jenny_breakfast_notice.add(T_jenny_breakfast_notice, S_jenny_have_breakfast)
    S_jenny_have_breakfast.add(T_jenny_had_breakfast, S_jenny_hallway_eavesdropping)
    S_jenny_hallway_eavesdropping.add(T_jenny_eavesdropped, S_jenny_sluttygram_pics,
                                      actions=('assign', ('diary_progress', 6)))
    S_jenny_sluttygram_pics.add(T_jenny_took_pictures, S_jenny_pics_afterthought,
                                actions=('assign', ('diary_progress', 7)))
    S_jenny_pics_afterthought.add(T_jenny_snoop_in_her_room, S_jenny_snoop_around,
                          actions = ["location", {"place": L_home_shower},
                                     "force", {"tod": 0},
                                     "unlocklocation", L_home_sisbedroom,
                                     "setinshower", "jenny",
                                     ])
    S_jenny_snoop_around.add(T_jenny_looked_at_diary, S_jenny_snoop_nightstand)
    S_jenny_snoop_around.add(T_jenny_looked_at_nightstand, S_jenny_snoop_diary)
    S_jenny_snoop_nightstand.add(T_jenny_looked_at_nightstand, S_jenny_caught_snooping)
    S_jenny_snoop_diary.add(T_jenny_looked_at_diary, S_jenny_caught_snooping)
    S_jenny_caught_snooping.add(T_jenny_caught_snooping, S_jenny_breakfast_notice_2,
                                actions=('unforce', None,
                                         'set', ('player', 'jerk jenny'),
                                         'assign', ('diary_progress', 8)))
    S_jenny_breakfast_notice_2.add(T_jenny_breakfast_notice_2, S_jenny_have_breakfast_2,
                          actions = ["location", {"place": L_home_diningroom},
                                     "force", {"tod": 0},
                                     ])
    S_jenny_have_breakfast_2.add(T_jenny_had_breakfast_2, S_jenny_go_to_her_room,
                          actions=["unforce", None,
                                   "location", {"place":L_home_sisbedroom},
                                   "force", {"tod": [0, 1, 2, 3]}])
    S_jenny_go_to_her_room.add(T_jenny_pay_for_favors, S_jenny_get_a_toy,
                               actions=('unforce', None,
                                        'assign', ("diary_progress", 9)))

    S_jenny_get_a_toy.add(T_jenny_get_a_toy, S_jenny_go_to_pink,
                          actions=('assign', ('diary_progress', 11)))
    S_jenny_go_to_pink.add(T_jenny_ivy_jane_leaving, S_jenny_ivy_jane_leave_pink,
                           actions=('assign', ('jenXX_lite_ivy', 'game.timer.now')))
    S_jenny_ivy_jane_leave_pink.add(T_jenny_got_a_toy, S_jenny_bring_toy_back)
    S_jenny_bring_toy_back.add(T_jenny_brought_back_toy, S_jenny_helping_with_breakfast,
                               actions=('assign', ('diary_progress', 12)))


    S_jenny_helping_with_breakfast.add(T_jenny_have_breakfast, S_jenny_have_breakfast_3,
                                       actions=('assign', ('diary_progress', 13)))
    S_jenny_helping_with_breakfast.add(T_jenny_catch_her_in_shower, S_jenny_confront_her_hallway,
                                       actions=('assign', ('diary_progress', 13)))
    S_jenny_have_breakfast_3.add(T_jenny_wait_a_day, S_jenny_catch_her_leaving)
    S_jenny_confront_her_hallway.add(T_jenny_wait_a_day, S_jenny_catch_her_leaving)
    S_jenny_catch_her_leaving.add(T_jenny_leave_house, S_jenny_go_shopping,
                          actions = ["location", {"place": L_NULL},
                                     "force", {"tod": [0,1]},
                                     ])
    S_jenny_go_shopping.add(T_jenny_go_at_pinks, S_jenny_shop_for_toys)
    S_jenny_shop_for_toys.add(T_jenny_buy_vibrator, S_jenny_buy_vibrator)
    S_jenny_buy_vibrator.add(T_jenny_bought_vibrator, S_jenny_snooping_laptop_notice,
                             actions=('unforce', None))


    S_jenny_snooping_laptop_notice.add(T_player_woke_up, S_jenny_snoop_around_for_laptop)
    S_jenny_snoop_around_for_laptop.add(T_jenny_check_laptop, S_jenny_check_laptop)
    S_jenny_check_laptop.add(T_jenny_return_from_shower, S_jenny_figure_out_password,
                          actions = ["force", {"tod":[2]},
                                     "location", {"place":L_NULL}])
    S_jenny_figure_out_password.add(T_jenny_a_real_penis, S_jenny_new_video_notice,
                          actions = ["unforce", None])

    S_jenny_new_video_notice.add(T_player_woke_up, S_jenny_check_for_new_video,
                                 actions=('assign', ('diary_progress', 14)))
    S_jenny_check_for_new_video.add(T_jenny_checked_pc_for_new_vids, S_jenny_checked_for_new_video)
    S_jenny_checked_for_new_video.add(T_jenny_get_her_a_new_toy, S_jenny_buy_bad_monster,
        actions=('condition', ('player.has_item("badmonster")',
                               (('trigger', T_jenny_bought_bad_monster)), ())))
    S_jenny_buy_bad_monster.add(T_jenny_bought_bad_monster, S_jenny_deliver_bad_monster)
    S_jenny_deliver_bad_monster.add(T_jenny_gave_bad_monster, S_jenny_video_3_production,
                                    actions=('assign', ('diary_progress', 15)))
    S_jenny_video_3_production.add(T_all_sleep, S_jenny_video_3_uploaded,
                                   actions=['assign', ('videos', ('ec', 'uv', 'bm'))])
    S_jenny_video_3_uploaded.add(T_jenny_checked_new_vid, S_jenny_cedric_upset)

    S_jenny_cedric_upset.add(T_jenny_talk_to_cedric, S_jenny_talk_to_cedric)
    S_jenny_talk_to_cedric.add(T_jenny_talked_to_cedric, S_jenny_talked_to_cedric)
    S_jenny_talked_to_cedric.add(T_jenny_cedric_didnt_call, S_jenny_caught_talking_to_camslut,
                                 actions=('assign', ('diary_progress', 16)))

    S_jenny_caught_talking_to_camslut.add(T_jenny_beaten_up_with_dildo, S_jenny_spy_on_mia_telescope,
                                          actions=('assign', ('diary_progress', 17)))

    S_jenny_spy_on_mia_telescope.add(T_jenny_spied_on_mia, S_jenny_get_a_mask_quest,
                                     actions=('assign', ('diary_progress', 18)))
    S_jenny_get_a_mask_quest.add(T_jenny_get_a_mask, S_jenny_get_a_mask,
                          actions = ["location", ["rump", {"place": L_NULL, "dow":[5, 6]}],
                                     "force", ["rump", {"tod": [0, 1]}],
                                     ])
    S_jenny_get_a_mask.add(T_jenny_buy_mask, S_jenny_buy_mask,
                          actions = ["unforce", "rump",
                                     ])
    S_jenny_buy_mask.add(T_jenny_bought_mask, S_jenny_bought_mask)
    S_jenny_bought_mask.add(T_jenny_delivered_mask, S_jenny_come_back_camshow)
    S_jenny_come_back_camshow.add(T_all_sleep, S_jenny_start_camshow_handjob)

    S_jenny_start_camshow_handjob.add(T_jenny_gave_handjob, S_jenny_pissed_at_handjob,
                                      actions=('assign', ('diary_progress', 19)))
    S_jenny_pissed_at_handjob.add(T_jenny_reconciliation_handjob, S_jenny_catch_her_jilling,
                                  actions=('assign', ('diary_progress', 20)))


    S_jenny_catch_her_jilling.add(T_jenny_gave_footjob, S_jenny_morning_visit,
                                  actions=('assign', ('diary_progress', 21)))
    S_jenny_morning_visit.add(T_jenny_start_camshow_blowjob, S_jenny_start_camshow_blowjob)
    S_jenny_start_camshow_blowjob.add(T_jenny_done_camshow_blowjob, S_jenny_pissed_at_blowjob,
                                      actions=('assign', ('diary_progress', 22)))
    S_jenny_pissed_at_blowjob.add(T_jenny_reconciliation_blowjob, S_jenny_perv_on_tammy)

    S_jenny_perv_on_tammy.add(T_jenny_spied_on_tammy, S_jenny_give_cunni)
    S_jenny_give_cunni.add(T_jenny_gave_cunni, S_jenny_bedroom_intrusion,
                           actions=('assign', ('diary_progress', 23)))


    S_jenny_bedroom_intrusion.add(T_jenny_go_breakfast, S_jenny_have_breakfast_4,
                                  actions=('assign', ('diary_progress', 25)))
    S_jenny_have_breakfast_4.add(T_jenny_get_cheerleader_outfit, S_jenny_get_cheerleader_outfit)
    S_jenny_get_cheerleader_outfit.add(T_jenny_got_cheerleader_outfit, S_jenny_cheerleader_sex)
    S_jenny_cheerleader_sex.add(T_jenny_had_cheerleader_sex, S_jenny_want_some_breakfast,
                                actions=('clear', ('player', 'is_virgin'),
                                         'assign', ('diary_progress', 26)))


    S_jenny_want_some_breakfast.add(T_jenny_pool_talk, S_jenny_pool_talk,
                                    actions=('assign', ('diary_progress', 27)))
    S_jenny_pool_talk.add(T_jenny_stalked, S_jenny_find_stalker)
    S_jenny_find_stalker.add(T_jenny_its_mr_bubbles, S_jenny_ask_movie_date)
    S_jenny_ask_movie_date.add(T_jenny_movie_date, S_jenny_movie_date)
    S_jenny_movie_date.add(T_jenny_righteous_punch, S_jenny_night_time_sex,
                           actions=('assign', ('sneak_in_chance', 100),
                                    'assign', ('diary_progress', 28)))
    S_jenny_night_time_sex.add(T_jenny_didnt_sleep_much, S_jenny_weird_relationship,
                               actions=('assign', ('sneak_in_chance', 5)))

    S_jenny_weird_relationship.add(T_jenny_final_breakfast, S_jenny_final_breakfast)
    S_jenny_final_breakfast.add(T_jenny_end, S_jenny_end,
                                actions=('exec', A_prolific_camshow.unlock))

    S_jenny_end.add(T_all_sleep, S_jenny_hallway_talk,
                    actions=('assign', ('diary_progress', 29)))
    S_jenny_hallway_talk.add(T_jenny_diary_clue, S_jenny_diary_clue,
                             actions=('assign', ('diary_progress', 30)))
    S_jenny_diary_clue.add(T_jenny_give_necklace, S_jenny_necklace_rebutal,
                           actions=('assign', ('diary_progress', 31),
                                    'priority', 0,
                                    'set', 'fertile'))
    S_jenny_necklace_rebutal.add(T_jen0m_hook, S_jen0m_init)

    S_jen0m_init.add(T_jen0m_init, S_jen0m_food,
                     actions=('exec', 'game.lock_sleep()',
                              'priority', 1))
    S_jen0m_food.add(T_jen0m_food, S_jen0m_done,
                     actions=('exec', 'game.unlock_sleep()'))

    M_jenny.add(S_jenny_start, S_jenny_shower_spy, S_jenny_debbie_altercation,
                S_jenny_breakfast_notice, S_jenny_have_breakfast,
                S_jenny_hallway_eavesdropping,
                S_jenny_sluttygram_pics,
                S_jenny_pics_afterthought, S_jenny_snoop_around, S_jenny_snoop_diary, S_jenny_snoop_nightstand, S_jenny_caught_snooping,
                S_jenny_breakfast_notice_2, S_jenny_have_breakfast_2, S_jenny_go_to_her_room,
                S_jenny_get_a_toy, S_jenny_go_to_pink, S_jenny_ivy_jane_leave_pink, S_jenny_bring_toy_back,
                S_jenny_helping_with_breakfast, S_jenny_have_breakfast_3, S_jenny_confront_her_hallway,
                S_jenny_catch_her_leaving, S_jenny_go_shopping, S_jenny_shop_for_toys, S_jenny_buy_vibrator,
                S_jenny_snooping_laptop_notice, S_jenny_snoop_around_for_laptop, S_jenny_check_laptop, S_jenny_figure_out_password,
                S_jenny_new_video_notice, S_jenny_check_for_new_video, S_jenny_checked_for_new_video, S_jenny_buy_bad_monster,
                S_jenny_deliver_bad_monster, S_jenny_video_3_production, S_jenny_video_3_uploaded,
                S_jenny_cedric_upset, S_jenny_talk_to_cedric, S_jenny_talked_to_cedric,
                S_jenny_caught_talking_to_camslut,
                S_jenny_spy_on_mia_telescope,
                S_jenny_get_a_mask_quest, S_jenny_get_a_mask, S_jenny_buy_mask, S_jenny_bought_mask, S_jenny_come_back_camshow,
                S_jenny_start_camshow_handjob, S_jenny_pissed_at_handjob,
                S_jenny_catch_her_jilling, S_jenny_morning_visit, S_jenny_start_camshow_blowjob, S_jenny_pissed_at_blowjob,
                S_jenny_perv_on_tammy, S_jenny_give_cunni,
                S_jenny_bedroom_intrusion, S_jenny_have_breakfast_4, S_jenny_get_cheerleader_outfit, S_jenny_cheerleader_sex,
                S_jenny_want_some_breakfast, S_jenny_pool_talk, S_jenny_find_stalker,
                S_jenny_ask_movie_date, S_jenny_movie_date, S_jenny_night_time_sex,
                S_jenny_weird_relationship, S_jenny_final_breakfast,
                S_jenny_end,
                S_jenny_hallway_talk, S_jenny_diary_clue, S_jenny_necklace_rebutal,
                S_jen0m_init, S_jen0m_food, S_jen0m_done)

    M_jenny.add_action(T_all_sleep, ["assign", ("forced_sneak_in_chance", 0),
                                     "assign", ("had_couch_sex", False),
                                     "assign", ('force_couch_sex', False),
                                     "assign", ('preg_afterglow', False),
                                     "assign", ('girlfriend_in_progress', False),
                                     "assign", ('peephole', False)])

    M_jenny.pregnancy.add_action('first', 1, ('assign', (
        'diary_extra_pregnancy', '(M_jenny.diary_progress, game.timer.now)')))
    M_jenny.pregnancy.add_action('first', 6, ('assign', (
        'diary_extra_baby', '(M_jenny.diary_progress, game.timer.now)')))

    M_jenny.pregnancy.add_action('first', 3, ('trigger', T_jen0m_hook))


    M_jenny.set_priority(1)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
