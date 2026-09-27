screen okita_sex_options():
    tag quick_menu

    imagebutton:
        focus_mask True
        pos (250,700)
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("okita_sex_options"), Jump("okita_h_scene_loop")

    imagebutton:
        focus_mask True
        pos (350,665)
        idle "buttons/ar_switch_01.png"
        hover HoverImage("buttons/ar_switch_01.png")
        action Hide("okita_sex_options"), Function(M_okita.toggle, "in augmented reality"), SetVariable("animated", False), Jump("okita_h_scene_loop")

    imagebutton:
        focus_mask True
        pos (450,700)
        idle "buttons/diane_stage01_02.png"
        hover HoverImage("buttons/diane_stage01_02.png")
        action Hide("okita_sex_options"), If(M_okita.is_set("repeatable unlocked"), Jump("okitas_office_hscene_cum"), Jump("okitas_office_hscene_aftermath"))

    if anim_toggle:
        if M_okita.get("sex speed") < .15:
            imagebutton:
                focus_mask True
                pos (250,735)
                idle "buttons/speed_02.png"
                hover HoverImage("buttons/speed_02.png")
                action Hide("okita_sex_options"), Function(M_okita.set, "sex speed", M_okita.get("sex speed") + 0.05), Jump("okita_h_scene_loop")

        if M_okita.get("sex speed") > .051:
            imagebutton:
                focus_mask True
                pos (450,735)
                idle "buttons/speed_01.png"
                hover HoverImage("buttons/speed_01.png")
                action Hide("okita_sex_options"), Function(M_okita.set, "sex speed", M_okita.get("sex speed") - 0.05), Jump("okita_h_scene_loop")

screen okita_handjob_options():
    tag quick_menu

    imagebutton:
        pos (250,700)
        focus_mask True
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("okita_handjob_options"), Jump("okita_handjob_loop")

    imagebutton:
        pos (450,700)
        focus_mask True
        idle "buttons/judith_stage02_02.png"
        hover HoverImage("buttons/judith_stage02_02.png")
        action Hide("okita_handjob_options"), Jump("okita_handjob_cum")

    if M_okita.get('sex speed') < .4:
        imagebutton:
            focus_mask True
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Hide("okita_handjob_options"), Function(M_okita.set, "sex speed", M_okita.get("sex speed") + 0.1), Jump("okita_handjob_loop")
            xpos 250
            ypos 735

    if M_okita.get('sex speed') > .21:
        imagebutton:
            focus_mask True
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Hide("okita_handjob_options"), Function(M_okita.set, "sex speed", M_okita.get("sex speed") - 0.1), Jump("okita_handjob_loop")
            xpos 450
            ypos 735
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
