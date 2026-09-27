screen odette_sex_bike_options():
    tag quick_menu

    imagebutton:
        focus_mask True
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("odette_sex_bike_options"), Jump("odette_sex_bike_loop")
        xpos 150
        ypos 700

    imagebutton:
        focus_mask True
        idle "buttons/diane_stage01_02.png"
        hover HoverImage("buttons/diane_stage01_02.png")
        action Hide("odette_sex_bike_options"), Jump("odette_sex_bike_cum_inside")
        xpos 350
        ypos 700

    imagebutton:
        focus_mask True
        idle "buttons/diane_stage01_03.png"
        hover HoverImage("buttons/diane_stage01_03.png")
        action Hide("odette_sex_bike_options"), Jump("odette_sex_bike_cum_outside")
        xpos 550
        ypos 700

    if M_odette.get('sex speed') < .09:
        imagebutton:
            focus_mask True
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Hide("odette_sex_bike_options"), Function(M_odette.set, "sex speed", M_odette.get("sex speed") + 0.02), Jump("odette_sex_bike_loop")
            xpos 250
            ypos 735

    if M_odette.get('sex speed') > .051:
        imagebutton:
            focus_mask True
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Hide("odette_sex_bike_options"), Function(M_odette.set, "sex speed", M_odette.get("sex speed") - 0.02), Jump("odette_sex_bike_loop")
            xpos 450
            ypos 735

screen odette_sex_massage_options():
    tag quick_menu

    imagebutton:
        focus_mask True
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("odette_sex_massage_options"), Jump("odette_sex_massage_loop")
        xpos 50
        ypos 700

    imagebutton:
        focus_mask True
        idle "buttons/diane_stage01_02.png"
        hover HoverImage("buttons/diane_stage01_02.png")
        action Hide("odette_sex_massage_options"), Jump("odette_sex_massage_cum_inside")
        xpos 250
        ypos 700

    imagebutton:
        focus_mask True
        idle "buttons/diane_stage01_03.png"
        hover HoverImage("buttons/diane_stage01_03.png")
        action Hide("odette_sex_massage_options"), Jump("odette_sex_massage_cum_outside")
        xpos 450
        ypos 700

    imagebutton:
        focus_mask True
        idle "buttons/diane_stage01_04.png"
        hover HoverImage("buttons/diane_stage01_04.png")
        action Hide("odette_sex_massage_options"), Jump("grace_massage_sex_switcheroo")
        xpos 650
        ypos 700

    if M_odette.get('sex speed') < .09:
        imagebutton:
            focus_mask True
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Hide("odette_sex_massage_options"), Function(M_odette.set, "sex speed", M_odette.get("sex speed") + 0.03), Jump("odette_sex_massage_loop")
            xpos 250
            ypos 735

    if M_odette.get('sex speed') > .031:
        imagebutton:
            focus_mask True
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Hide("odette_sex_massage_options"), Function(M_odette.set, "sex speed", M_odette.get("sex speed") - 0.03), Jump("odette_sex_massage_loop")
            xpos 450
            ypos 735
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
