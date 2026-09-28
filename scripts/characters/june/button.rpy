label june_button_dialogue:
    if M_june.is_state(S_june_cosplay_acquired):
        scene school_computer_b
        call expression game.dialog_select("june_intro_intimate")
        call expression game.dialog_select("june_dialogue_cosplay_has_costume")
        $ player.remove_item("orcette_cosplay")
        $ M_june.trigger(T_june_cosplay_given)
        $ game.main()

    elif M_bissette.is_state(S_bissette_fix_printer):
        if M_bissette.is_set("printer fix fail"):
            call expression game.dialog_select("june_dialogue_bissette_fix_printer_repeat")
        else:

            call expression game.dialog_select("june_dialogue_bissette_fix_printer_first")

        if player.stats.str() < 2:
            $ display.toast(str_fail)
            call expression game.dialog_select("june_dialogue_bissette_fix_printer_fail")
            $ M_bissette.trigger(T_bissette_june_printer_error)
        else:

            $ display.toast(str_pass)
            call expression game.dialog_select("june_dialogue_bissette_fix_printer_pass")
            $ player.get_item('french_scans')
            call popup ('give', 'french_scans')
            $ M_bissette.trigger(T_bissette_june_scan_pages)
        $ game.main()

    elif M_okita.is_state(S_okita_faptic_engine):
        call expression game.dialog_select("june_dialogue_okita_faptic_engine")
        $ M_okita.trigger(T_okita_faptic_get_controller)

    elif M_okita.is_state(S_okita_get_controller_info):
        call expression game.dialog_select("june_dialogue_okita_get_controller_info")

    elif M_okita.is_state(S_okita_get_controller) and player.has_item("controller"):
        call expression game.dialog_select("june_dialogue_okita_has_controller")
        $ player.remove_item("controller")
        $ player.get_item("faptic_engine")
        $ game.main()
    else:

        scene school_computer_b
        if M_june.finished_state(S_june_date_ready):
            call expression game.dialog_select("june_intro_intimate")
        else:
            call expression game.dialog_select("june_intro")
        menu june_button_menu:
            "Lenses." if M_okita.is_state(S_okita_get_bifocal_lenses):
                call expression game.dialog_select("june_dialogue_okita_get_bifocal_lenses")

            "Model." if M_ross.is_state(S_ross_ask_model):
                call expression game.dialog_select("june_dialogue_ross_ask_model")

            "Hang out." if (M_june.finished_state(S_june_date_ready) and
                           not M_june.is_state(S_june_date_shame)):
                if M_june.get('hang_time'):
                    call june_date_later
                else:
                    if M_june.get('excuse') == 'tired':
                        call june_date_tired
                    elif M_june.get('excuse') == 'retry':
                        call june_date_retry
                    else:
                        call expression game.dialog_select("june_date_hang")
                    $ M_june.set('hang_time', True)
                    $ M_june.trigger(T_june_date_ask)

            "Sorry." if M_june.is_state(S_june_date_shame):
                call june_date_sorry
                $ M_june.trigger(T_june_date_sorry)

            "Cosplay." if M_june.is_state(S_june_cosplay_ready):
                call expression game.dialog_select("june_dialogue_cosplay_no_costume")

            "Ask about class." if M_mrsj.is_state(S_mrsj_fork_meet):
                call screen popup_branch
                if not _return:
                    jump june_button_menu
                call expression game.dialog_select("june_dialogue_ask_about_class")
                menu june_route_split:
                    "My friend {b}Erik{/b}!":
                        call expression game.dialog_select("june_dialogue_erik_help")
                        $ M_mrsj.trigger(T_mrsj_fork_setup)
                    "I'll play!":

                        call expression game.dialog_select("june_dialogue_mc_help")
                        $ M_mrsj.trigger(T_mrsj_fork_steal)
            "Nothing.":

                call expression game.dialog_select("june_dialogue_leave")

    hide june
    hide player
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
