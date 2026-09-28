label church_lock_check:
    scene expression player.location.background_blur

    if motion in route(L_diane_garden, L_church_graveyard):
        call diane_house_lock_check
        if _return:
            return True

    if game.timer.is_night() and destination not in (L_church_front,
                                                     L_church_graveyard,
                                                     L_church_crypt):
        show anon f_tired with dissolve
        anon @ -m_talk "( It's pretty late, I should go home to bed. )"
        hide anon with dissolve
        $ player.go_to(L_church_front)

    elif game.timer.is_night() and game.timer.is_fullmoon() and destination == L_church_graveyard and L_church_crypt.is_here(M_odette) and (
            game.sleep_lock or M_anon.is_state(S_ano21_home) or
            M_mia.is_state(S_mia_strip_aftermath, S_mia_midnight_call,
                           S_mia_midnight_help, S_mia_locked_room)):
        show anon f_worried with dissolve
        anon @ -m_talk "( I can't be playing {b}Odette{/b}'s silly games right now. )"
        if M_anon.is_state(S_ano21_home):
            anon @ -m_talk "( The mayor might be done, but the Russians are still out there. )"
            anon @ -m_talk "( I should head to {b}[deb_name]{/b}'s tonight. )"
        elif M_mia.is_state(S_mia_strip_aftermath, S_mia_midnight_call):
            anon f_tired @ -m_talk "( I feel so tired all of a sudden. )"
            anon @ -m_talk "( I just want to go {b}home and sleep{/b}.. )"
        elif M_mia.is_state(S_mia_midnight_help, S_mia_locked_room):
            anon @ -m_talk "( {b}Mia{/b} needs my help! I should get over to {b}her house{/b}! )"
        else:
            anon @ -m_talk "( I still have some things to do today... )"
        hide anon with dissolve

    elif game.timer.is_evening() and M_mia.is_set('church night locked') and motion in route(L_church_front,
                                                                                             L_church):
        show anon with dissolve
        anon @ -m_talk "( It's locked. )"
        hide anon with dissolve

    elif M_consuela.is_state(S_con02_job1) and motion not in route(L_church_front,
                                                                   L_church):
        show anon with dissolve
        anon @ -m_talk "( No time for that now, {b}Consuela{/b}'s with me. )"
        anon @ -m_talk "( We should go inside. )"
        hide anon with dissolve

    elif M_odette.is_state(S_ode02_find) and motion not in route(L_church_graveyard,
                                                                 L_church_crypt):
        show anon f_worried with dissolve
        anon @ -m_talk "( No, I can't chicken out now... )"
        anon f_worried_left @ f_worried -m_talk "( ... This is probably just {b}Odette{/b} trying to scare me. )"
        pause
        anon f_worried @ -m_talk "( {b}I should investigate that glowing beneath the tree{/b}. )"
        hide anon with dissolve

    elif M_odette.is_state(S_ode02_tomb) and motion in route(L_church_crypt,
                                                             L_church_graveyard):
        show anon with dissolve
        anon @ -m_talk "( Well I'm here now, and it's only {b}Odette{/b}. )"
        anon f_worried @ -m_talk "( I think..? )"
        hide anon with dissolve

    elif M_mia.is_state(S_mia_priest_act) and destination == L_church_front:
        show player 18 at center:
            xoffset -1
        show players robe
        with dissolve
        anon @ -m_talk "( This is my window! Time to take confession! )"
        hide player
        hide players robe
        with dissolve

    elif M_mia.is_state(S_mia_priest_act) and destination == L_church_confessional_left:
        show player 10 at center:
            xoffset -1
        show players robe
        with dissolve
        anon @ -m_talk "( I can't go in that side. )"
        anon @ -m_talk "( I have to use the door on the {b}right side{/b} of the confessional... )"
        hide player
        hide players robe
        with dissolve

    elif M_mia.is_state(S_mia_return_priest_outfit) and destination in (L_church_confessional_left, L_church_confessional_right):
        show player 10 at center:
            xoffset -1
        show players robe
        with dissolve
        anon @ -m_talk "( I need to return this robe before someone sees me. )"
        hide player
        hide players robe
        with dissolve


    elif M_mia.is_state(S_mia_return_priest_outfit) and destination == L_church_front:
        show player 10 at center:
            xoffset -1
        show players robe
        with dissolve
        anon @ -m_talk "( I should return this robe to where I found it. )"
        anon f_shock @ -m_talk "( It's no dog, but why take that risk... {i}*Gulp*{/i}! )"
        hide player
        hide players robe
        with dissolve
    else:

        return

    return True
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
