label miahouse_lock_check:
    scene expression player.location.background_blur

    if M_mia.is_state(S_mia_midnight_help) and destination == L_miahouse_lockedroom and M_mia.get("helens locked room locked"):
        show anon f_worried with dissolve
        anon @ -m_talk "( The door is locked. )"
        anon @ -m_talk "( I have to {b}find a key{/b}... )"
        hide anon with dissolve

    elif M_mia.is_state(S_mia_midnight_help, S_mia_locked_room):
        return

    elif game.timer.is_night() and destination != L_miahouse:
        show player 10 with dissolve
        player_name "( Everyone is probably asleep... I should come back tomorrow. )"
        hide player with dissolve
        $ player.go_to(L_miahouse)

    elif M_mia.is_state(S_mia_unexpected_visit) and game.timer.is_afternoon() and destination == L_miahouse:
        show player 12 with dissolve
        player_name "( I should find {b}Mia{/b} before I leave... )"
        hide player with dissolve

    elif M_mia.between_states(S_mia_urgent_help, S_mia_harold_found_news) and destination == L_miahouse_entrance:
        return

    elif (game.timer.is_morning() or (game.timer.is_afternoon() and M_mia.get("front door locked"))) and destination == L_miahouse_entrance:
        show player 12 with dissolve
        if game.timer.is_morning() and not game.timer.is_weekend():
            player_name "( There's no one here... )"
            show player 35
            player_name "( {b}Mia{/b} probably left for {b}school{/b} already. )"
        else:
            player_name "( {b}Mia{/b} is outside, I shouldn't go in there. )"

    elif M_mia.is_state(S_mia_need_space) and destination == L_miahouse_entrance:
        show player 12 with dissolve
        player_name "I should leave {b}Mia{/b} and her family alone for now..."
        hide player with dissolve

    elif (game.timer.is_evening() and not (not M_mia.get("front door locked") or M_mia.is_state(S_mia_midnight_help, S_mia_locked_room))) and destination == L_miahouse_entrance:
        show player 2 with dissolve
        player_name "( {b}Mia{/b} is probably asleep... I should come back tomorrow. )"
        hide player 2 with dissolve

    elif M_mia.get("helens locked room locked") and destination == L_miahouse_lockedroom:
        player_name "( The door is locked. )"

    elif game.timer.is_dark() and player.location == L_miahouse and destination == L_miahouse_entrance:
        scene mia_sneak01
        show text _ ("The door is unlocked.\nI hope I don't get in trouble for this...\nAlright, I'm going in.") as caption
        with fade
        pause

        if not M_mia.is_set("harold left"):
            scene mia_sneak02
            show text _ ("Both her parents are watching TV.\nI just have to be quiet and make my way upstairs now...") as caption
            with fade
            pause

        scene black with dissolve
        pause .5
        return
    else:

        return

    return True
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
