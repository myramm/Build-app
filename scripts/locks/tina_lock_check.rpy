label tina_lock_check:
    scene location_apt_hall3_301_closeup as stage
    show location_apt_hall3_301_closeup_door1 as door behind stage

    if M_tina.pregnancy.character_bedridden and motion in route(L_apt_hall3,
                                                                L_tina_lounge):
        show anon with dissolve
        anon @ -m_talk "( {b}Tina{/b} is still in the hospital with the baby. )"

        anon @ -m_talk "( I should visit her there. )"

        hide anon with dissolve

    elif game.timer.is_night() and motion in route(L_apt_hall3,
                                                   L_tina_lounge):
        show anon f_tired with dissolve
        anon @ -m_talk "( They're probably sleeping... I should consider doing that too. )"

        hide anon with dissolve

    elif motion in route(L_apt_hall3, L_tina_lounge):
        if M_tina.where in L_tina_lounge.get_all_children_inclusive():
            if M_anon.is_state(S_ano10_tina):
                return

            if M_tina.is_state(S_tin01_init):
                return

            if M_tina.sex == game.timer._game_day:
                return

        jump tina_lounge_knock

    elif motion in route(L_tina_lounge, L_tina_bed2) and not M_becca.finished_state(S_bec01_init):
        scene expression background(480, 376, 3.5) as stage
        show anon f_worried with dissolve
        anon @ -m_talk "( I'm here for Tina right now, it'd be rude to wander off. )"

        hide anon with dissolve

    elif motion in route(L_tina_lounge, L_tina_bed2) and M_tina.pregnancy.stage in (3, 4):
        scene expression background(480, 376, 3.5) as stage
        show anon a_surprised f_disgusted_wince of_blush with dissolve
        anon @ -m_talk "( The temperature is too damn high! I just want to get out of here! )"

        hide anon with dissolve
    else:

        return

    return True
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
