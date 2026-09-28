label police_lock_check:
    scene expression player.location.background_blur

    if game.timer.is_night() and destination != L_police_front:
        show player 11 with dissolve
        player_name "( It's pretty late, I should be getting home. )"
        hide player with dissolve
        $ player.go_to(L_police_front)

    elif M_anon.is_state(S_ano20_cops) and motion not in route(L_police_front,
                                                               L_police_lobby,
                                                               L_police_office):
        show anon f_worried with dissolve
        anon @ -m_talk "( No distractions. Straight to {b}Harold{/b} to hand this over. )"
        hide anon with dissolve

    elif M_anon.is_state(S_ano20_cops) and destination == L_police_office:
        return

    elif M_anon.is_state(S_ano21_cops) and motion not in route(L_police_front,
                                                               L_police_lobby,
                                                               L_police_office):
        show anon f_worried with dissolve
        anon @ -m_talk "( {b}Harold{/b}'s probably in the office, I have to know if they got him! )"
        hide anon with dissolve

    elif game.timer.is_dark() and destination == L_police_office:
        show anon f_thinking with dissolve
        anon @ -m_talk "( Huh... It's locked. They must have gone home. )"
        hide anon with dissolve

    elif destination == L_police_lobby and player.location == L_police_basement and M_mia.is_state(S_mia_inmate_status):
        show player 11 with dissolve
        player_name "( People are shouting! )"
        player_name "( I should check what's happening in those cells! )"
        hide player with dissolve
    else:

        return

    return True
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
