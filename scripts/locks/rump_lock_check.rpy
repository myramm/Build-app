label rump_lock_check:
    scene expression player.location.background_blur

    if game.timer.is_night() and destination is not L_rump_front:
        show anon f_tired with dissolve
        anon @ -m_talk "( It's pretty late, I should be getting home. )"

        hide anon with dissolve
        $ player.go_to(L_rump_front)

    elif destination is L_rump_lobby and L_rump_lobby.locked and game.timer.is_dark():
        call misc_lock_rump_lobby_late

    elif destination is L_rump_lobby and L_rump_lobby.locked:
        scene expression background(688, 464, 4.65)
        call bodyguard_button_estate

        if _return:
            $ M_anon.trigger(T_ano18_init)
            $ L_rump_lobby.unlock()
            $ game.timer.tick(1)
            return

        $ player.go_to(L_map)
        if M_anon.is_state(S_ano15_init):
            $ M_anon.trigger(T_ano15_fail)

    elif M_anon.is_state(S_ano18_yell) and destination not in (L_rump_lobby, L_rump_kitchen):
        show anon f_surprised with dissolve
        anon @ -m_talk "( It sounds like shouting coming from that {b}door on the lower right{/b}... )"

        anon f_worried @ -m_talk "( ... I wonder what's going on? )"

        hide anon with dissolve

    elif M_anon.is_state(S_ano18_yard) and destination is not L_rump_back:
        show anon f_worried with dissolve
        anon @ -m_talk "( That poor woman, I can't leave without seeing if she's okay... )"

        hide anon with dissolve

    elif M_anon.is_state(S_ano18_trap) and player.location is L_rump_master:
        call ano18_trap_lock
        $ M_anon.trigger(T_ano18_trap)

    elif M_anon.is_state(S_ano18_rage, S_ano18_trap) and motion in route(L_rump_lobby, L_rump_front):
        show anon with dissolve
        anon @ -m_talk "( I might not get this chance again... )"

        anon f_grin @ -m_talk "( I can't leave without taking a quick peek at his bedroom... )"

        hide anon with dissolve

    elif M_anon.is_state(S_ano18_hide):
        show anon f_shock with dissolve
        anon @ -m_talk "( I can't get out that way, they're coming! )"

        anon @ -m_talk "( There has to be some place to hide in here. )"

        hide anon with dissolve

    elif M_iwanka.is_state(S_iwa01_exit) and motion not in route(L_rump_second,
                                                                 L_rump_lobby,
                                                                 L_rump_front):
        scene expression background(800, 472, 2.5) as stage
        show iwanka b_maid f_suspicious o_glasses
        show anon f_worried:
            flip
            xoffset -500
        iwanka "Kemana kamu pergi?"

        show anon with dissolve:
            unflip
            xoffset 0
        anon @ -m_talk "Hmm?"

        iwanka "We're supposed to walk straight out the front door, remember?"

        anon f_shy "Benar, maaf."

        hide anon with dissolve

    elif M_melonia.is_state(S_mel01_init) and M_melonia.scare and destination == L_rump_master:
        show anon f_worried_forward with dissolve
        anon @ -m_talk "( Are you nuts? )"

        anon @ -m_talk "( I'm not going in there while she's angry with me! )"

        pause
        anon f_sad_down @ -m_talk "( I should really {b}clean her hot tub{/b}... )"

        hide anon with dissolve

    elif M_melonia.between_states(S_mel01_hint, S_mel01_help):
        show anon f_worried with dissolve
        anon @ -m_talk "( If I leave now {b}Melonia{/b} might take away my {b}staff badge{/b}. )"

        anon @ -m_talk "( I better just crack on with cleaning the hot tub. )"

        hide anon with dissolve

    elif M_anon.is_state(S_ano20_oval) and motion not in route(L_rump_lobby,
                                                               L_rump_office):
        show anon with dissolve
        anon @ -m_talk "( I should hurry into {b}Mayor Rump{/b}'s office and look for evidence. )"

        anon @ -m_talk "( There's no telling when or if someone will come back through here. )"

        hide anon with dissolve

    elif M_anon.is_state(S_ano20_find, S_ano20_open) and player.location == L_rump_office:
        scene expression background(0,0,1.15) as stage
        show anon with dissolve:
            flip
        anon @ -m_talk "( I can't leave empty-handed. )"

        anon @ -m_talk "( There has to be {b}evidence{/b} in here somewhere! )"

        hide anon with dissolve

    elif M_anon.is_state(S_ano20_cops) and motion not in route(L_rump_office,
                                                               L_rump_lobby,
                                                               L_rump_front):
        show anon f_worried with dissolve
        anon @ -m_talk "( I can't do that. )"

        anon @ -m_talk "( I need to get this evidence over to {b}Harold{/b} at the {b}police station{/b}! )"

        hide anon with dissolve

    elif L_rump_office.locked and destination is L_rump_office:
        call rump_office_lock
    else:

        return

    return True


label misc_lock_rump_lobby_late:
    scene expression background(688, 464, 4.65)
    show bodyguard
    show anon with dissolve
    show anon f_shock
    bodyguard @ a_stop "Hold it!" with hpunch
    anon f_surprised "Tapi aku-"

    bodyguard "Sorry sir, {b}Mrs. Rump{/b} was very clear."

    bodyguard "No visitors. She has a migraine. Now please be on your way."

    anon f_worried @ -m_talk "..."
    hide anon with dissolve

    scene expression L_rump_front.background_blur with fade
    show anon f_worried with dissolve
    anon @ -m_talk "( I guess I should try again tomorrow... )"

    hide anon with dissolve
    return


label rump_office_lock:
    scene expression background(432, 432, 4.5)
    show bodyguard at flip
    show anon at flip with dissolve
    show anon f_shock
    bodyguard @ a_stop "Hey, that area is off-limits to staff!" with hpunch
    anon f_worried "O-oh?"

    anon "Sorry, I didn't-"

    bodyguard a_crossed "I suggest you turn around and head back the way you came."

    anon "Tentu, tidak masalah."

    hide anon with dissolve
    return


label ano18_trap_lock:
    scene expression background(200, 384, 5.) as stage
    show anon f_shock with dissolve:
        flip
    melonia "{b}Iwanka{/b}!!"

    melonia "I need to see you in my room!"

    anon @ -m_talk "( Oh, crap! )"

    iwanka "Ugh, I'm on the phone!"

    anon @ -m_talk "( What do I do?! )"

    melonia "Now, {b}Iwanka{/b}!!!"

    anon f_surprised_teeth @ -m_talk "( I've gotta hide somewhere! )"

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
