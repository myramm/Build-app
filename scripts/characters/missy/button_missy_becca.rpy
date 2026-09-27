label missy_button_dialogue:
    jump missy_becca_button_dialogue

label missy_becca_button_dialogue:
    scene expression player.location.background_blur
    if M_roxxy.is_state(S_roxxy_chat_with_becca_missy):
        call expression game.dialog_select("button_missy_becca_chat_with_becca_missy")
        $ M_roxxy.trigger(T_roxxy_get_goldenschwagger)
    elif M_roxxy.is_state(S_roxxy_spin_bottle):
        if player.has_item("goldschwagger"):
            show player 5f with dissolve
            player_name "(Saya seharusnya tidak mengganggu mereka lagi.)"

            player_name "( Saya akan menemui mereka {b}Sabtu sore di pantai{/b}. )"

            hide player with dissolve
        else:
            show player 5f with dissolve
            player_name "(Saya seharusnya tidak mengganggu mereka lagi.)"

            player_name "(Saya perlu {b}berbicara dengan Kapten Terry tentang hal GoldSchwagger ini{/b}. )"

            hide player with dissolve
        $ game.main()
    else:
        if M_roxxy.between_states(S_roxxy_ask_exam_copy_delay, S_roxxy_invite_to_bikini_contest):
            call expression game.dialog_select("button_missy_becca_intro_rox11")
        elif not M_roxxy.finished_state(S_roxxy_ask_exam_copy_delay):
            call expression game.dialog_select("button_missy_becca_intro_0_1")
            $ game.main()
        else:
            call expression game.dialog_select("button_missy_becca_intro")
        menu:
            "Kalian terlihat cantik." if M_roxxy.between_states(S_roxxy_ask_exam_copy_delay, S_roxxy_invite_to_bikini_contest):
                call expression game.dialog_select("button_missy_becca_look_nice")
            "Aku hanya ingin menyapa." if M_roxxy.between_states(S_roxxy_ask_exam_copy_delay, S_roxxy_invite_to_bikini_contest):
                call expression game.dialog_select("button_missy_becca_leave_rox11")
            "Kalian berdua terlihat cantik hari ini." if M_roxxy.finished_state(S_roxxy_invite_to_bikini_contest):
                call expression game.dialog_select("button_missy_becca_look_beautiful")
            "Sampai jumpa." if M_roxxy.finished_state(S_roxxy_invite_to_bikini_contest):
                call expression game.dialog_select("button_missy_becca_leave")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
