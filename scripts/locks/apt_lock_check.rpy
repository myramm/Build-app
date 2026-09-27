label apt_lock_check:
    if M_maria.is_state(S_mar01_help):
        jump apt_lock_check.skip

    if not L_liu_lounge.locked and destination in L_liu_lounge.get_all_children_inclusive():
        jump liu_lock_check

    if not L_maria_lounge.locked and destination in L_maria_lounge.get_all_children_inclusive():
        jump maria_lock_check

    if not L_tina_lounge.locked and destination in L_tina_lounge.get_all_children_inclusive():
        jump tina_lock_check

    label apt_lock_check.skip:

    scene expression player.location.background_blur

    if M_anon.is_state(S_ano10_tina) and destination == L_apt:
        show anon a_pizza f_worried with dissolve
        anon @ -m_talk "( I can't leave yet! )"

        anon @ -m_talk "( {b}Tony{/b} said to take this pizza to {b}room 301{/b}. )"

        anon f_grin @ -m_talk "( That will probably be on the {b}third floor{/b}. )"

        hide anon with dissolve

    elif M_anon.is_state(S_ano24_seek) and destination == L_apt_hall2:
        show anon with dissolve
        anon @ -m_talk "( No, I can't leave yet. )"

        anon @ -m_talk "( I should continue searching for evidence that {b}Kim{/b} was mixed up in {b}Rump{/b}'s affairs. )"

        hide anon with dissolve

    elif M_anon.is_state(S_ano24_find) and destination == L_apt_hall2:
        show anon with dissolve
        anon @ -m_talk "( I should follow {b}Liu{/b} into the bedroom and continue our search. )"

        hide anon with dissolve

    elif M_anon.is_state(S_ano25_find) and destination == L_apt_hall3:
        show anon with dissolve
        anon @ -m_talk "( {b}I can't leave without the duffelbag.{/b} )"

        anon @ -m_talk "( {b}Tony said it should be in their closet, in the bedroom.{/b} )"

        hide anon with dissolve

    elif M_maria.is_state(S_mar01_help) and destination == L_maria_lounge:
        return

    elif M_maria.is_state(S_mar01_help) and destination not in (
        L_apt_hall1, L_apt_hall2, L_apt_hall3, L_apt_lift, L_apt_lobby, L_maria_lounge):
        show anon a_grocery_bags with dissolve
        anon @ -m_talk "( I should take these groceries to {b}Maria and Tony's apartment{/b}. )"

        anon @ -m_talk "( It's on the {b}third floor, room 302{/b}. )"

        hide anon with dissolve

    elif M_maria.sex and motion in route(L_maria_lounge, L_apt_hall3):
        show anon with dissolve
        anon @ -m_talk "( I can't leave now. )"

        anon f_grin @ -m_talk "( {b}Maria{/b} is waiting for me. )"

        hide anon with dissolve

    elif destination not in (L_apt, L_apt_hall1, L_apt_hall2, L_apt_hall3,
                             L_apt_lift, L_apt_lobby):
        if game.timer.is_night():
            show anon f_tired with dissolve
            anon @ -m_talk "( It's pretty late to be bothering people... )"

            anon @ -m_talk "( I should be getting home too. )"

            hide anon with dissolve
        else:
            show anon f_worried with dissolve
            anon @ -m_talk "( I don't want to just show up uninvited... )"

            anon f_surprised @ -m_talk "( That'd be suuuper awkward. )"

            hide anon with dissolve
    else:

        return

    return True
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
