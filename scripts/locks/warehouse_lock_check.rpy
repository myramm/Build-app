label warehouse_lock_check:
    scene expression player.location.background_blur

    if M_anon.is_state(S_ano12_oops) and motion in route(L_warehouse,
                                                         L_warehouse_depot):
        show anon f_surprised with dissolve:
            flip
            xoffset 150
        anon @ -m_talk "( I can't just waltz in the front door! )"

        anon f_thinking @ -m_talk "( There should be a place along the perimeter where I can observe without being seen. )"

        hide anon with dissolve

    elif not M_anon.finished_state(S_ano27_plan) and motion in route(L_warehouse,
                                                                     L_warehouse_depot):
        show anon f_worried with dissolve:
            flip
            xoffset 150
        anon @ -m_talk "( Nothing about that seems like a good idea. )"

        anon @ -m_talk "( Better to keep a low profile. )"

        hide anon with dissolve

    elif M_anon.is_state(S_ano27_jabb) and motion not in route(L_warehouse_sewer,
                                                               L_warehouse_cargo):
        show anon f_worried o_sewage with dissolve
        anon @ -m_talk "( I should talk to {b}Jab{/b} first. {b}Nadya{/b} mentioned him having supplies for me. )"

        hide anon with dissolve

    elif M_anon.is_state(S_ano27_yolo) and motion in route(L_warehouse_furnace,
                                                           L_warehouse_depot):
        show anon f_worried with dissolve
        anon @ -m_talk "( I can't just wander out there, there's too many of them. I need an edge... )"

        anon f_thinking @ -m_talk "( There must be something here I can use. )"

        hide anon with dissolve

    elif M_anon.is_state(S_ano27_free) and motion not in route(L_warehouse_depot,
                                                               L_warehouse_lab):
        show anon f_worried with dissolve
        anon @ -m_talk "( No, I've gotta rescue the girls before I deal with {b}Raz{/b}. )"

        anon @ -m_talk "( {b}I wonder what's through those double doors on the right{/b}? )"

        hide anon with dissolve


    elif M_anon.is_state(S_ano27_help) and motion not in route(L_warehouse_lab,
                                                               L_warehouse_storage):
        show anon f_worried with dissolve
        anon @ -m_talk "( No, I can't go back now... )"

        anon @ -m_talk "( {b}[deb_name]{/b} and {b}[jen_name]{/b} need me! )"

        hide anon with dissolve

    elif M_anon.is_state(S_ano27_boss) and motion not in route(L_warehouse_depot,
                                                               L_warehouse_office):
        show anon f_annoyed with dissolve
        anon @ -m_talk "( There's no time to waste! )"

        anon @ -m_talk "( {b}Nadya{/b} and the bastard who killed my father are upstairs. )"

        anon @ -m_talk "( Let's go up end this! )"

        hide anon with dissolve

    elif M_anon.between_states(S_ano27_plan, S_ano27_done):
        return

    elif not M_nadya.finished_state(S_nad01_thug) and motion in route(L_warehouse,
                                                                      L_warehouse_depot):
        show anon f_worried with dissolve
        anon @ -m_talk "( There's no reason for me to go back in there. )"

        anon @ -m_talk "( {b}Harold{/b} and his colleagues have everything well in hand. )"

        hide anon with dissolve

    elif M_nadya.is_state(S_nad01_find) and motion not in route(L_warehouse_depot,
                                                                L_warehouse_office):
        show anon with dissolve
        anon @ -m_talk "( {b}Jab{/b} said I could find {b}Nadya{/b} in the office. )"

        anon @ -m_talk "( No time like the present I guess. )"

        hide anon with dissolve

    elif M_nadya.is_state(S_nad01_lewd):
        show anon f_surprised with dissolve
        anon @ -m_talk "( {b}I should speak with Nadya first.{/b} )"

        hide anon with dissolve

    elif M_khadne.is_state(S_kha01_lewd) and motion not in route(L_warehouse_depot,
                                                                 L_warehouse_lab):
        show anon f_worried with dissolve
        anon @ -m_talk "( {b}I'm meant to be speaking to Khadne in the lab.{/b} )"

        anon f_worried_surprised @ -m_talk "( What Nadya might do if I don't doesn't bare thinking about! )"

        hide anon with dissolve

    elif M_khadne.is_state(S_kha01_talk) and motion not in route(L_warehouse_lab,
                                                                 L_warehouse_depot):
        show anon f_shy with dissolve
        anon @ -m_talk "( Probably best if I leave her to recover for a little while. )"

        show anon a_fists f_grin
        with {'master': dissolve}
        anon @ -m_talk "( That was pretty intense! )"

        hide anon with dissolve

    elif game.timer.is_night() and destination != L_warehouse:
        show anon f_tired with dissolve
        anon @ -m_talk "( It's pretty late, I should go home to bed. )"

        hide anon with dissolve
        $ player.go_to(L_warehouse)
    else:

        return

    return True
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
