screen grace_sex_massage_options():
    tag quick_menu

    imagebutton:
        focus_mask True
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("grace_sex_massage_options"), Jump("grace_sex_massage_loop")
        if not M_grace.get("massage_sex_1st_time") and not M_grace.get("grace_massage_alone"):
            xpos 50
        else:
            xpos 150
        ypos 700

    imagebutton:
        focus_mask True
        idle "buttons/diane_stage01_02.png"
        hover HoverImage("buttons/diane_stage01_02.png")
        action Hide("grace_sex_massage_options"), Jump("grace_sex_massage_cum_inside")
        if not M_grace.get("massage_sex_1st_time") and not M_grace.get("grace_massage_alone"):
            xpos 250
        else:
            xpos 350
        ypos 700

    imagebutton:
        focus_mask True
        idle "buttons/diane_stage01_03.png"
        hover HoverImage("buttons/diane_stage01_03.png")
        action Hide("grace_sex_massage_options"), Jump("grace_sex_massage_cum_outside")
        if not M_grace.get("massage_sex_1st_time") and not M_grace.get("grace_massage_alone"):
            xpos 450
        else:
            xpos 550
        ypos 700

    if not M_grace.get("massage_sex_1st_time") and not M_grace.get("grace_massage_alone"):
        imagebutton:
            focus_mask True
            idle "buttons/diane_stage01_04.png"
            hover HoverImage("buttons/diane_stage01_04.png")
            action Hide("grace_sex_massage_options"), Jump("odette_massage_sex_switcheroo")
            xpos 650
            ypos 700

    if M_grace.get('sex speed') < .06:
        imagebutton:
            focus_mask True
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Hide("grace_sex_massage_options"), Function(M_grace.set, "sex speed", M_grace.get("sex speed") + 0.015), Jump("grace_sex_massage_loop")
            xpos 250
            ypos 735

    if M_grace.get('sex speed') > .031:
        imagebutton:
            focus_mask True
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Hide("grace_sex_massage_options"), Function(M_grace.set, "sex speed", M_grace.get("sex speed") - 0.015), Jump("grace_sex_massage_loop")
            xpos 450
            ypos 735
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
