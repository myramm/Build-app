label beach_house_lock_check:
    scene expression player.location.background_blur

    if not M_anon.finished_state(S_ano02_thug) and motion in route(L_beachhouse_front,
                                                                   L_beachhouse_entrance):
        show anon f_surprised_teeth with dissolve
        anon @ -m_talk "( This isn't my house! )"

        anon f_thinking @ -m_talk "( But maybe {b}in future the owner will want to sell...{/b} )"

        anon f_grin @ -m_talk "( Living right on the beach would be great! )"

        hide anon with dissolve

    elif not player.has_item('beach_house_key') and motion in route(L_beachhouse_front,
                                                                    L_beachhouse_entrance):
        show player 3 at left
        player_name "Man, I don't have the key..."

        show player 4 at left
        player_name "Hmm... There's a sale sign on the lawn..."

        show player 1 at left with dissolve
        player_name "I guess I could save up some of that money {b}Diane{/b} gives me..."

        with dissolve
    else:

        return

    return True
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
