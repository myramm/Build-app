screen eve_sex_back_options():
    tag quick_menu

    imagebutton:
        focus_mask True
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("eve_sex_back_options"), Jump("eve_sex_back_loop")
        xpos 150
        ypos 700

    imagebutton:
        focus_mask True
        idle "buttons/diane_stage01_02.png"
        hover HoverImage("buttons/diane_stage01_02.png")
        action Hide("eve_sex_back_options"), Jump("eve_sex_back_cum_inside")
        xpos 350
        ypos 700

    imagebutton:
        focus_mask True
        idle "buttons/diane_stage01_03.png"
        hover HoverImage("buttons/diane_stage01_03.png")
        action Hide("eve_sex_back_options"), Jump("eve_sex_back_cum_outside")
        xpos 550
        ypos 700

    if M_eve.get('sex speed') < .08:
        imagebutton:
            focus_mask True
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Hide("eve_sex_back_options"), Function(M_eve.set, "sex speed", M_eve.get("sex speed") + 0.02), Jump("eve_sex_back_loop")
            xpos 250
            ypos 735

    if M_eve.get('sex speed') > .041:
        imagebutton:
            focus_mask True
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Hide("eve_sex_back_options"), Function(M_eve.set, "sex speed", M_eve.get("sex speed") - 0.02), Jump("eve_sex_back_loop")
            xpos 450
            ypos 735

screen eve_sex_front_options():
    tag quick_menu

    imagebutton:
        focus_mask True
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("eve_sex_front_options"), Jump("eve_sex_front_loop")
        ypos 700
        if not M_eve.get("biggus_dickus") and not M_eve.get("sex_front_1st_time"):
            xpos 50
        else:
            xpos 150

    imagebutton:
        focus_mask True
        idle "buttons/diane_stage01_02.png"
        hover HoverImage("buttons/diane_stage01_02.png")
        action Hide("eve_sex_front_options"), Jump("eve_sex_front_cum_inside")
        ypos 700
        if not M_eve.get("biggus_dickus") and not M_eve.get("sex_front_1st_time"):
            xpos 250
        else:
            xpos 350

    imagebutton:
        focus_mask True
        idle "buttons/diane_stage01_03.png"
        hover HoverImage("buttons/diane_stage01_03.png")
        action Hide("eve_sex_front_options"), Jump("eve_sex_front_cum_outside")
        ypos 700
        if not M_eve.get("biggus_dickus") and not M_eve.get("sex_front_1st_time"):
            xpos 450
        else:
            xpos 550

    if not M_eve.get("biggus_dickus") and not M_eve.get("sex_front_1st_time"):
        imagebutton:
            focus_mask True
            idle "buttons/diane_stage01_04.png"
            hover HoverImage("buttons/diane_stage01_04.png")
            action Hide("eve_sex_front_options"), Function(M_eve.toggle, "sex_front_anal"), SetVariable("animated", False), Jump("eve_sex_front_switcheroo")
            xpos 650
            ypos 700

    if M_eve.get('sex speed') < .12:
        imagebutton:
            focus_mask True
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Hide("eve_sex_front_options"), Function(M_eve.set, "sex speed", M_eve.get("sex speed") + 0.03), Jump("eve_sex_front_loop")
            xpos 250
            ypos 735

    if M_eve.get('sex speed') > .061:
        imagebutton:
            focus_mask True
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Hide("eve_sex_front_options"), Function(M_eve.set, "sex speed", M_eve.get("sex speed") - 0.03), Jump("eve_sex_front_loop")
            xpos 450
            ypos 735

screen eve_sex_bj_options():
    tag quick_menu

    imagebutton:
        focus_mask True
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("eve_sex_bj_options"), Jump("eve_sex_bj_loop")
        xpos 250
        ypos 700

    imagebutton:
        focus_mask True
        idle "buttons/diane_stage01_02.png"
        hover HoverImage("buttons/diane_stage01_02.png")
        action Hide("eve_sex_bj_options"), Jump("eve_sex_bj_cum")
        xpos 450
        ypos 700

    if M_eve.get('sex speed') < .12:
        imagebutton:
            focus_mask True
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Hide("eve_sex_bj_options"), Function(M_eve.set, "sex speed", M_eve.get("sex speed") + 0.03), Jump("eve_sex_bj_loop")
            xpos 250
            ypos 735

    if M_eve.get('sex speed') > .061:
        imagebutton:
            focus_mask True
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Hide("eve_sex_bj_options"), Function(M_eve.set, "sex speed", M_eve.get("sex speed") - 0.03), Jump("eve_sex_bj_loop")
            xpos 450
            ypos 735

screen eve_sex_jerk_options():
    tag quick_menu

    imagebutton:
        focus_mask True
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("eve_sex_jerk_options"), Jump("eve_sex_jerk_loop")
        xpos 250
        ypos 700

    imagebutton:
        focus_mask True
        idle "buttons/judith_stage02_02.png"
        hover HoverImage("buttons/judith_stage02_02.png")
        action Hide("eve_sex_jerk_options"), Jump("eve_sex_jerk_cum")
        xpos 450
        ypos 700

    if M_eve.get('sex speed') < .08 and M_eve.biggus_dickus or M_eve.get('sex speed') < .09:
        imagebutton:
            focus_mask True
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            if M_eve.biggus_dickus:
                action Hide("eve_sex_jerk_options"), Function(M_eve.set, "sex speed", M_eve.get("sex speed") + 0.02), Jump("eve_sex_jerk_loop")
            else:
                action Hide("eve_sex_jerk_options"), Function(M_eve.set, "sex speed", M_eve.get("sex speed") + 0.015), Jump("eve_sex_jerk_loop")
            xpos 250
            ypos 735

    if M_eve.get('sex speed') > .041 and M_eve.biggus_dickus or M_eve.get('sex speed') > .061:
        imagebutton:
            focus_mask True
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            if M_eve.biggus_dickus:
                action Hide("eve_sex_jerk_options"), Function(M_eve.set, "sex speed", M_eve.get("sex speed") - 0.02), Jump("eve_sex_jerk_loop")
            else:
                action Hide("eve_sex_jerk_options"), Function(M_eve.set, "sex speed", M_eve.get("sex speed") - 0.015), Jump("eve_sex_jerk_loop")
            xpos 450
            ypos 735

screen eve_sex_mc_jerk_options():
    tag quick_menu

    imagebutton:
        focus_mask True
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("eve_sex_mc_jerk_options"), Jump("eve_sex_mc_jerk_loop")
        xpos 250
        ypos 700

    imagebutton:
        focus_mask True
        idle "buttons/judith_stage02_02.png"
        hover HoverImage("buttons/judith_stage02_02.png")
        action Hide("eve_sex_mc_jerk_options"), Jump("eve_sex_mc_jerk_cum")
        xpos 450
        ypos 700

    if M_eve.get('sex speed') < .4:
        imagebutton:
            focus_mask True
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Hide("eve_sex_mc_jerk_options"), Function(M_eve.set, "sex speed", M_eve.get("sex speed") + 0.1), SetVariable("animated", False), Jump("eve_sex_mc_jerk_loop")
            xpos 250
            ypos 735

    if M_eve.get('sex speed') > .21:
        imagebutton:
            focus_mask True
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Hide("eve_sex_mc_jerk_options"), Function(M_eve.set, "sex speed", M_eve.get("sex speed") - 0.1), SetVariable("animated", False), Jump("eve_sex_mc_jerk_loop")
            xpos 450
            ypos 735
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
