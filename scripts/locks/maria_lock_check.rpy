label maria_lock_check:
    if player.location == L_apt_hall3:
        scene location_apt_hall3_301_closeup as stage
        show location_apt_hall3_302_closeup_door1 as door behind stage
    else:
        scene expression player.location.background_blur

    if M_maria.pregnancy.character_bedridden and motion in route(L_apt_hall3,
                                                                 L_maria_lounge):
        show anon with dissolve
        anon @ -m_talk "( {b}Maria{/b} and {b}Tony{/b} are still in the hospital with the baby. )"
        anon @ -m_talk "( I should visit them there. )"
        hide anon with dissolve

    elif game.timer.is_night() and motion in route(L_apt_hall3,
                                                   L_maria_lounge):
        show anon f_tired with dissolve
        anon @ -m_talk "( They're probably sleeping... I should consider doing that too. )"
        hide anon with dissolve

    elif M_anon.is_state(S_ano20_done, S_ano21_cops, S_ano21_home) and motion in route(L_apt_hall3,
                                                                                       L_maria_lounge):
        show anon f_worried with dissolve
        anon @ -m_talk "( I can't face {b}Tony{/b} right now. I know he disapproved of getting the cops involved... )"
        if M_anon.is_state(S_ano21_home):
            anon f_sad_down @ -m_talk "( ... And he was totally right. I don't know if I'm more mad at myself or the cops... )"
        else:
            anon @ -m_talk "( ... But what was the alternative? I should wait and see how this plays out before visting him again. )"
        hide anon with dissolve

    elif M_anon.is_state(S_ano25_sick) and motion in route(L_apt_hall3, L_maria_lounge):
        return

    elif M_anon.between_states(S_ano25_sick, S_ano26_done) and motion in route(L_apt_hall3, L_maria_lounge):
        show anon f_worried with dissolve
        anon @ -m_talk "( {b}Maria{/b} is probably sleeping. I should let her rest in peace. )"
        hide anon with dissolve

    elif motion in route(L_apt_hall3, L_maria_lounge):
        jump maria_lounge_knock

    elif M_maria.sex and motion not in route(L_maria_lounge, L_maria_bedroom):
        show anon with dissolve
        anon @ -m_talk "( I can't leave now. )"
        anon f_grin @ -m_talk "( {b}Maria{/b} is waiting for me. )"
        hide anon with dissolve

    elif M_maria.sex:
        return

    elif game.timer.is_night():
        show anon f_tired with dissolve
        anon @ -m_talk "( It's pretty late, I should be getting home. )"
        hide anon with dissolve
        $ player.go_to(L_apt_hall3)
    else:

        return

    return True
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
