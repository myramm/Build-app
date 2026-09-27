label eriks_house_dialogue:
    $ player.go_to(L_erikhouse)
    if not game.timer.is_dark():
        if getPlayingSound("<loop 7 to 114>audio/ambience_suburb.ogg"):
            $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg", 1.0)
    else:
        if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
            $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)

    if game.timer.is_morning():
        if M_erik.is_state(S_erik_start):
            call expression game.dialog_select("erikshouse_erik_intro_known")
            $ M_erik.trigger(T_erik_intro_meet)
        elif M_erik.is_state(S_erik_intro_met):
            call expression game.dialog_select("erikshouse_erik_intro_started")
    $ game.main()

label eriks_mailbox_dialogue:
    $ player.location.call_screen(False)

label eriks_mailbox_item:
    scene expression player.location.background_blur

    if game.mail["erik"] == "m_magazine":
        call expression game.dialog_select("eriks_mailbox_magazine")

    elif game.mail["erik"] == "m_dad_letter":
        player_name "( I didn't know they received letters. I wonder who it's addressed to... )"

        player_name "( It's for {b}Erik{/b}. )"

        menu:
            "Leave it alone.":
                pass
            "Open it.":

                show mailbox_letter at Position(xpos = 565, ypos = 768) with dissolve
                player_name "( A letter from D?! )"

                player_name "I'd better put this back."

                hide mailbox_letter with dissolve
                $ A_long_lost_father.unlock()

    elif game.mail["erik"] == "m_pizza_pamphlet":
        call expression game.dialog_select("mailbox_pizza_pamphlet")

    elif game.mail["erik"] == "m_newspaper":
        call expression game.dialog_select("mailbox_newspaper")

    $ player.location.call_screen(False)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
