label player_just_wokeup(woke_with=None):
    if M_debbie.is_state(S_debbie_sleepover_wakeup):
        call expression game.dialog_select("moms_bedroom_mom_sleepover_makeup")
        $ M_debbie.trigger(T_debbie_sleepover_morning)
        $ player.go_to(L_home_livingroom)
        $ M_player.set('just wokeup', False)
        $ game.main()

    if M_player.is_state(S_player_start):
        call expression game.dialog_select("bedroom_mc_start_just_wokeup")

    elif player.location == L_home_mombedroom:
        if woke_with is M_diane:
            if M_diane.is_set("3way first time"):
                call expression game.dialog_select("diane_debbie_sleepover_wakeup_first")
                $ M_diane.set("3way first time", False)
            else:

                call expression game.dialog_select("diane_debbie_sleepover_wakeup_repeat")

        elif randomizer() <= 50:
            call expression game.dialog_select("mom_sleeping_sex_available_random")
        else:

            call expression game.dialog_select("mom_sleeping_sex_available")

    elif player.location == L_home_sisbedroom:
        call expression game.dialog_select("player_jenny_sleepover_sisbedroom")
        $ player.go_to(L_home_bedroom)
        jump player_just_wokeup

    elif player.location == L_beachhouse_bedroom:
        if game.timer.is_weekend():
            call expression game.dialog_select("beachhouse_weekend_just_wokeup")
        else:

            call expression game.dialog_select("beachhouse_weekday_just_wokeup")

    elif player.location == L_home_bedroom:
        if woke_with is M_jenny:
            call expression game.dialog_select("player_jenny_sleepover_mcbedroom")
            $ M_jenny.set('had_sex_bedroom', False)

        elif M_anon.is_state(S_ano28_init):
            call ano28_init_wakeup
            $ M_anon.trigger(T_ano28_init)
            jump player_just_wokeup.skip

        elif M_nadya.is_state(S_nad01_init):
            call nad01_init_wakeup
            $ M_nadya.trigger(T_nad01_init)
            jump player_just_wokeup.skip

        elif M_jenny.is_state(S_jenny_get_a_toy):
            call expression game.dialog_select("bedroom_jenny_get_a_toy")

        elif M_jenny.is_state(S_jenny_morning_visit):
            call expression game.dialog_select("bedroom_jenny_morning_visit")
            $ M_jenny.trigger(T_jenny_start_camshow_blowjob)

        elif M_jenny.is_state(S_jenny_bedroom_intrusion):
            call expression game.dialog_select("bedroom_jenny_bedroom_intrusion_1")

        elif M_erik.is_state(S_erik_bully_ready):
            with None
            call expression game.dialog_select("bedroom_erik_bullying")
            $ M_erik.trigger(T_erik_bully_visitor)

        elif M_jenny.is_state(S_jen0m_init) and M_jenny.pregnancy.stage in (3, 4):
            call jen0m_init_wakeup
            $ M_anon.trigger(T_jen0m_init)
            jump player_just_wokeup.skip

        elif game.timer.is_weekend():
            call expression game.dialog_select("bedroom_mc_weekend_just_wokeup")
        else:

            call expression game.dialog_select("bedroom_mc_weekday_just_wokeup")



    if player.location == L_home_bedroom:

        if M_anon.is_state(S_ano01_init):
            call ano01_init_wakeup
            $ L_mall_parking_lot.unlock()
            $ L_beach.unlock()
            $ L_treehouse.unlock()
            $ L_hill.unlock()
            $ L_beachhouse_front.unlock()

        elif M_anon.is_state(S_ano01_cops):
            call ano01_cops_wakeup

        elif M_anon.is_state(S_ano02_food):
            call ano02_food_wakeup

        elif M_anon.is_state(S_ano04_init):
            if not game.timer.is_dow(6):
                call ano04_init_wakeup
                $ L_pizzeria_exterior.unlock()
                $ L_bank.unlock()
                $ M_anon.trigger(T_ano04_init)
                jump player_just_wokeup.skip
            else:
                call ano04_init_wakeup.delay

        elif M_anon.is_state(S_ano13_init):
            call ano13_init_wakeup
            $ M_anon.trigger(T_ano13_init)

        elif M_anon.is_state(S_ano21_init):
            call ano21_init_wakeup
            $ M_anon.trigger(T_ano21_init)

        elif M_anon.is_state(S_ano25_init):
            if game.timer.is_date(dow=6):
                call ano25_init_wakeup.wait
            else:
                call ano25_init_wakeup
                $ M_anon.trigger(T_ano25_init)

        elif M_josie.is_state(S_jos01_init) and not M_josie.once('jos01_call'):
            call jos01_init_wakeup

        if M_debbie.is_set("chores"):
            call expression game.dialog_select("bedroom_mom_chores")

        elif M_debbie.is_state(S_debbie_search_panties):
            call expression game.dialog_select("bedroom_mom_search_panties")

        elif M_debbie.is_state(S_debbie_kissing_practice):
            call expression game.dialog_select("bedroom_mom_kissing_practice")

        elif M_debbie.is_state(S_debbie_note):
            call expression game.dialog_select("bedroom_mom_note_just_wokeup")

        if M_diane.is_state(S_diane_get_augmentation):
            call expression game.dialog_select("bedroom_diane_get_augmentation")
            $ M_diane.trigger(T_diane_chat_at_home)

        elif M_diane.is_state(S_diane_debbie_dinner):
            call expression game.dialog_select("bedroom_diane_debbie_dinner")
            $ M_diane.trigger(T_diane_dinner_task_acquired)

        elif M_diane.is_state(S_diane_barn_news):
            call expression game.dialog_select("bedroom_diane_barn_news")

        elif M_diane.is_state(S_diane_breeding_candidate):
            call expression game.dialog_select("bedroom_diane_breeding_candidate")

        if M_roxxy.is_state(S_roxxy_spin_bottle) and game.timer == Date(dow="saturday"):
            call expression game.dialog_select("bedroom_roxxy_spin_bottle")
            if not player.has_item("goldschwagger"):
                call expression game.dialog_select("bedroom_roxxy_spin_bottle_no_goldschwagger")
            hide player with dissolve

        if M_jenny.pregnancy.stage == 4 and not M_jenny.get("seen_in_shower_pregnant"):
            call expression game.dialog_select("bedroom_jenny_pregnant_and_peeing")
            $ M_jenny.set("seen_in_shower_pregnant", True)
            $ game._in_shower = None
            $ player.go_to(L_home_hallway)
            $ game.main()

        if M_jenny.is_state(S_jenny_breakfast_notice):
            call expression game.dialog_select("bedroom_jenny_breakfast_notice")
            $ M_jenny.trigger(T_jenny_breakfast_notice)

        elif M_jenny.is_state(S_jenny_pics_afterthought):
            call expression game.dialog_select("bedroom_jenny_pics_afterthought")
            $ M_jenny.trigger(T_jenny_snoop_in_her_room)

        elif M_jenny.is_state(S_jenny_breakfast_notice_2):
            call expression game.dialog_select("bedroom_jenny_breakfast_notice")
            $ M_jenny.trigger(T_jenny_breakfast_notice_2)

        elif M_jenny.is_state(S_jenny_snooping_laptop_notice):
            call expression game.dialog_select("bedroom_jenny_snoopin_laptop_notice")

        elif M_jenny.is_state(S_jenny_new_video_notice):
            call expression game.dialog_select("bedroom_jenny_new_video_notice")

        elif M_jenny.is_state(S_jenny_buy_bad_monster):
            call expression game.dialog_select("bedroom_jenny_buy_bad_monster")

        elif M_jenny.is_state(S_jenny_spy_on_mia_telescope):
            call expression game.dialog_select("bedroom_jenny_spy_on_mia_telescope")

        elif M_jenny.is_state(S_jenny_pissed_at_handjob, S_jenny_pissed_at_blowjob):
            call expression game.dialog_select("bedroom_jenny_pissed_at_handjob")

        elif M_jenny.is_state(S_jenny_perv_on_tammy):
            call expression game.dialog_select("bedroom_jenny_perv_on_tammy_notice")

        elif M_jenny.is_state(S_jenny_bedroom_intrusion):
            call expression game.dialog_select("bedroom_jenny_bedroom_intrusion_2")
            $ M_jenny.trigger(T_jenny_go_breakfast)

        elif M_jenny.is_state(S_jenny_weird_relationship):
            call expression game.dialog_select("bedroom_jenny_weird_relationship")
            $ M_jenny.trigger(T_jenny_final_breakfast)

        if M_mia.is_state(S_mia_angelicas_impatience):
            call expression game.dialog_select("bedroom_mia_angelicas_impatience")

        elif M_mia.is_state(S_mia_angelicas_home_visit):
            call expression game.dialog_select("bedroom_mia_angelicas_home_visit")

        elif M_mia.is_state(S_mia_angelicas_final_home_visit):
            call expression game.dialog_select("bedroom_mia_angelicas_final_home_visit")

        if M_eve.is_state(S_eve_clients_hangover_wakeup):
            call expression game.dialog_select("bedroom_eve_clients_hangover_wakeup")

    label player_just_wokeup.skip:
    $ M_player.set("just wokeup", False)
    call check_pregnancies
    $ Machine.trigger(T_player_woke_up)

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
