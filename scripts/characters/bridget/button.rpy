label bridget_button_dialogue:
    if player.location == L_school_bridgetoffice:
        if M_eve.is_state(S_eve_dress_code_ask_teachers) and not M_eve.get("failed_bridget_test"):
            call expression game.dialog_select("bridget_dialogue_eve_dress_code_intro_first")
            if player.has_required_dex(5):
                $ display.toast(dex_pass)
                call expression game.dialog_select("bridget_dialogue_eve_dress_code_success_first")
                $ M_eve.trigger(T_eve_found_helping_teacher)
            else:
                $ display.toast(dex_fail)
                call expression game.dialog_select("bridget_dialogue_eve_dress_code_failure_first")
                $ M_eve.set("failed_bridget_test", True)
            $ game.timer.tick()
            $ player.go_to(L_map)
            $ game.main()
        else:
            call expression game.dialog_select("coach_bridget_dialogue_office_intro")

    elif player.location == L_school_track:
        call expression game.dialog_select("coach_bridget_dialogue_courtyard_intro")
        if M_eve.is_state(S_eve_dress_code_ask_teachers):
            call expression game.dialog_select("bridget_button_dress_code_track")
            $ game.main()

    menu:
        "Kode berpakaian." if M_eve.get("failed_bridget_test") and M_eve.is_state(S_eve_dress_code_ask_teachers):
            call expression game.dialog_select("bridget_dialogue_eve_dress_code_intro_repeat")
            if player.has_required_dex(5):
                $ display.toast(dex_pass)
                call expression game.dialog_select("bridget_dialogue_eve_dress_code_success_repeat")
                $ M_eve.trigger(T_eve_found_helping_teacher)
            else:
                $ display.toast(dex_fail)
                call expression game.dialog_select("bridget_dialogue_eve_dress_code_failure_repeat")
                $ M_eve.set("failed_bridget_test", True)
            $ game.timer.tick()
            $ player.go_to(L_map)
            $ game.main()
        "Di mana saya berlatih?":

            call expression game.dialog_select("coach_bridget_dialogue_training_advice")
        "Tidak ada apa-apa.":

            call expression game.dialog_select("coach_bridget_dialogue_leave")
    hide bridget
    hide player
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
