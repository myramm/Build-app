screen scene_roz_blowjob_options():
    tag quick_menu

    imagebutton:
        focus_mask True
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("scene_roz_blowjob_options"), Jump("scene_roz_blowjob.loop")
        xpos 250
        ypos 700

    imagebutton:
        focus_mask True
        idle "buttons/judith_stage02_02.png"
        hover HoverImage("buttons/judith_stage02_02.png")
        action Hide("scene_roz_blowjob_options"), Jump("scene_roz_blowjob.finish")
        xpos 450
        ypos 700

    if M_roz.get('sex speed') < .12:
        imagebutton:
            focus_mask True
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Hide("scene_roz_blowjob_options"), Function(M_roz.set, "sex speed", M_roz.get("sex speed") + 0.03), Jump("scene_roz_blowjob.loop")
            xpos 250
            ypos 735

    if M_roz.get('sex speed') > .061:
        imagebutton:
            focus_mask True
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Hide("scene_roz_blowjob_options"), Function(M_roz.set, "sex speed", M_roz.get("sex speed") - 0.03), Jump("scene_roz_blowjob.loop")
            xpos 450
            ypos 735


screen scene_roz_sex_options():
    tag quick_menu

    imagebutton:
        focus_mask True
        pos (250,700)
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("scene_roz_sex_options"), Jump("scene_roz_sex.loop")

    imagebutton:
        focus_mask True
        pos (450,700)
        idle "buttons/diane_stage01_02.png"
        hover HoverImage("buttons/diane_stage01_02.png")
        action Hide("scene_roz_sex_options"), Jump("scene_roz_sex.finish")

    if M_roz.get('sex speed') < .175:
        imagebutton:
            focus_mask True
            pos (250,735)
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Hide("scene_roz_sex_options"), Function(M_roz.set, "sex speed", M_roz.get("sex speed") + 0.05), Jump("scene_roz_sex.loop")

    if M_roz.get('sex speed') > .076:
        imagebutton:
            focus_mask True
            pos (450,735)
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Hide("scene_roz_sex_options"), Function(M_roz.set, "sex speed", M_roz.get("sex speed") - 0.05), Jump("scene_roz_sex.loop")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
