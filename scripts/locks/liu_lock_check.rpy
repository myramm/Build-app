label liu_lock_check:
    if player.location == L_apt_hall2:
        scene location_apt_hall2_204_closeup as stage
        show location_apt_hall2_204_closeup_door1 as door behind stage
    else:
        scene expression player.location.background_blur

    if M_liu.pregnancy.character_bedridden and motion in route(L_apt_hall2,
                                                               L_liu_lounge):
        show anon with dissolve
        anon @ -m_talk "( {b}Liu{/b} is still in the hospital with the baby. )"
        anon @ -m_talk "( I should visit her there. )"
        hide anon with dissolve

    elif game.timer.is_night() and motion in route(L_apt_hall2,
                                                   L_liu_lounge):
        show anon f_tired with dissolve
        anon @ -m_talk "( Liu's probably sleeping... I should consider doing that too. )"
        hide anon with dissolve

    elif M_anon.is_state(S_ano24_seek) and destination == L_liu_bedroom:
        show anon with dissolve
        anon @ -m_talk "( Well, hold on... )"
        anon @ -m_talk "( ... I should finish searching this room first! )"
        hide anon with dissolve

    elif M_anon.is_state(S_ano24_find) and destination == L_liu_lounge:
        show anon f_thinking a_thinking with dissolve
        anon @ -m_talk "( There has to be something in here that proves {b}Kim{/b} was involved in all this... )"
        anon @ -m_talk "( I should continue looking around. )"
        hide anon with dissolve

    elif M_anon.between_states(S_ano26_take, S_ano28_food) and destination == L_liu_lounge:
        show anon f_shy with dissolve
        anon @ -m_talk "( I should steer clear of {b}Liu{/b}'s place for the time being. )"
        anon @ -m_talk "( Wouldn't want the mob to think she's involved in the bank robbery. )"
        pause
        anon f_normal @ -m_talk "( {b}I'll come back once they've been dealt with{/b}. )"
        hide anon with dissolve

    elif motion in route(L_apt_hall2, L_liu_lounge):
        if M_liu.where in L_liu_lounge.get_all_children_inclusive():
            if M_anon.is_state(S_ano24_init):
                return

            if M_anon.is_state(S_ano28_clue):
                return

            if M_liu.pregnancy and not M_liu.pregnancy.announced_pregnancy:
                return

        jump liu_lounge_knock
    else:

        return

    return True
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
