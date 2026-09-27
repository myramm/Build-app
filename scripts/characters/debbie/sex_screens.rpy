screen basement_mom_sex_options():
    tag quick_menu

    imagebutton:
        focus_mask True
        pos (250,700)
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("basement_mom_sex_options"), Jump("basement_mom_sex_loop")

    imagebutton:
        focus_mask True
        pos (450,700)
        idle "buttons/diane_stage01_02.png"
        hover HoverImage("buttons/diane_stage01_02.png")
        action Hide("basement_mom_sex_options"), Jump("basement_mom_sex_cum")

    if M_debbie.get("sex speed") < .176:
        imagebutton:
            focus_mask True
            pos (250,735)
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Hide("basement_mom_sex_options"), Function(M_debbie.set, "sex speed", M_debbie.get("sex speed") + 0.05), Jump("basement_mom_sex_loop")

    if M_debbie.get("sex speed") > .075:
        imagebutton:
            focus_mask True
            pos (450,735)
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Hide("basement_mom_sex_options"), Function(M_debbie.set, "sex speed", M_debbie.get("sex speed") - 0.05), Jump("basement_mom_sex_loop")

screen debbie_movie_night_couch_blowjob_options():
    tag quick_menu

    imagebutton:
        pos (250,700)
        focus_mask True
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("debbie_movie_night_couch_blowjob_options"), Jump("debbie_movie_night_couch_blowjob_loop")

    imagebutton:
        pos (450,700)
        focus_mask True
        idle "buttons/judith_stage02_02.png"
        hover HoverImage("buttons/judith_stage02_02.png")
        action Hide("debbie_movie_night_couch_blowjob_options"), Jump("debbie_movie_night_couch_blowjob_cum")

    if M_debbie.get('sex speed') < .175:
        imagebutton:
            focus_mask True
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Hide("debbie_movie_night_couch_blowjob_options"), Function(M_debbie.set, "sex speed", M_debbie.get("sex speed") + 0.05), Jump("debbie_movie_night_couch_blowjob_loop")
            xpos 250
            ypos 735

    if M_debbie.get('sex speed') > .076:
        imagebutton:
            focus_mask True
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Hide("debbie_movie_night_couch_blowjob_options"), Function(M_debbie.set, "sex speed", M_debbie.get("sex speed") - 0.05), Jump("debbie_movie_night_couch_blowjob_loop")
            xpos 450
            ypos 735

screen debbie_movie_night_couch_sex_options():
    tag quick_menu

    imagebutton:
        pos (250,700)
        focus_mask True
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("debbie_movie_night_couch_sex_options"), Jump("debbie_movie_night_couch_sex_loop")

    imagebutton:
        pos (450,700)
        focus_mask True
        idle "buttons/judith_stage02_02.png"
        hover HoverImage("buttons/judith_stage02_02.png")
        action Hide("debbie_movie_night_couch_sex_options"), Jump("debbie_movie_night_couch_sex_cum")

    if M_debbie.get('sex speed') < .175:
        imagebutton:
            focus_mask True
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Hide("debbie_movie_night_couch_sex_options"), Function(M_debbie.set, "sex speed", M_debbie.get("sex speed") + 0.05), Jump("debbie_movie_night_couch_sex_loop")
            xpos 250
            ypos 735

    if M_debbie.get('sex speed') > .076:
        imagebutton:
            focus_mask True
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Hide("debbie_movie_night_couch_sex_options"), Function(M_debbie.set, "sex speed", M_debbie.get("sex speed") - 0.05), Jump("debbie_movie_night_couch_sex_loop")
            xpos 450
            ypos 735

screen mom_sex_options():
    tag quick_menu

    imagebutton:
        if mom_sex_position == "missionary":
            pos (50,700)

        elif mom_sex_position in ["cowgirl", "suck tits"]:
            pos (-30,700)
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("mom_sex_options"), Jump("mom_sex_loop")

    imagebutton:
        if mom_sex_position == "missionary":
            pos (250,700)

        elif mom_sex_position in ["cowgirl", "suck tits"]:
            pos (170,700)
        idle "buttons/diane_stage01_02.png"
        hover HoverImage("buttons/diane_stage01_02.png")
        action Hide("mom_sex_options"), Jump("mom_sex_cum_inside")

    imagebutton:
        if mom_sex_position == "missionary":
            pos (450,700)

        elif mom_sex_position in ["cowgirl", "suck tits"]:
            pos (370,700)
        idle "buttons/diane_stage01_03.png"
        hover HoverImage("buttons/diane_stage01_03.png")
        action Hide("mom_sex_options"), Jump("mom_sex_cum_outside")

    if mom_sex_position in ["cowgirl", "suck tits"]:
        imagebutton:
            pos (570,700)
            if mom_sex_position == "cowgirl":
                idle "buttons/judith_stage01_03.png"
                hover HoverImage("buttons/judith_stage01_03.png")

            elif mom_sex_position == "suck tits":
                idle "buttons/debbie_stage01_07.png"
                hover HoverImage("buttons/debbie_stage01_07.png")
            action Hide("mom_sex_options"), If(mom_sex_position == "cowgirl", SetVariable("mom_sex_position", "suck tits"), SetVariable("mom_sex_position", "cowgirl")), SetVariable("animated", False), Jump("mom_sex_loop_pre")

    imagebutton:
        if mom_sex_position == "missionary":
            pos (650,700)
            idle "buttons/debbie_stage01_07.png"
            hover HoverImage("buttons/debbie_stage01_07.png")

        elif mom_sex_position in ["cowgirl", "suck tits"]:
            pos (770,700)
            idle "buttons/debbie_stage01_08.png"
            hover HoverImage("buttons/debbie_stage01_08.png")
        action Hide("mom_sex_options"), If(mom_sex_position == "missionary", SetVariable("mom_sex_position", "cowgirl"), SetVariable("mom_sex_position", "missionary")), SetVariable("animated", False), Jump("mom_sex_loop_pre")

    if mom_sex_position == "cowgirl":
        imagebutton:
            pos (370,665)
            idle "buttons/diane_stage01_04.png"
            hover HoverImage("buttons/diane_stage01_04.png")
            action Hide("mom_sex_options"), Function(M_debbie.toggle, "change angle"), SetVariable("animated", False), Jump("mom_sex_loop_pre")

    if mom_sex_position in ["missionary", "cowgirl"]:
        if M_debbie.get("sex speed") < .4:
            imagebutton:
                focus_mask True
                pos (250,735)
                idle "buttons/speed_02.png"
                hover HoverImage("buttons/speed_02.png")
                action Hide("mom_sex_options"), Function(M_debbie.set, "sex speed", M_debbie.get("sex speed") + 0.1), Jump("mom_sex_loop")

        if M_debbie.get("sex speed") > .21:
            imagebutton:
                focus_mask True
                pos (450,735)
                idle "buttons/speed_01.png"
                hover HoverImage("buttons/speed_01.png")
                action Hide("mom_sex_options"), Function(M_debbie.set, "sex speed", M_debbie.get("sex speed") - 0.1), Jump("mom_sex_loop")

screen mom_finger_options():
    tag quick_menu

    imagebutton:
        focus_mask True
        pos (250,700)
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("mom_finger_options"), Jump("mom_finger_loop")

    imagebutton:
        focus_mask True
        pos (450,700)
        idle "buttons/cam_stage01_02.png"
        hover HoverImage("buttons/cam_stage01_02.png")
        action Hide("mom_finger_options"), Jump("mom_finger_cum")

    if M_debbie.get("sex speed") < .225:
        imagebutton:
            focus_mask True
            pos (250,735)
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Hide("mom_finger_options"), Function(M_debbie.set, "sex speed", M_debbie.get("sex speed") + 0.05), Jump("mom_finger_loop")

    if M_debbie.get("sex speed") > 0.126:
        imagebutton:
            focus_mask True
            pos (450,735)
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Hide("mom_finger_options"), Function(M_debbie.set, "sex speed", M_debbie.get("sex speed") - 0.05), Jump("mom_finger_loop")

screen mom_kitchen_fuck_options():
    tag quick_menu

    imagebutton:
        focus_mask True
        pos (250,700)
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("mom_kitchen_fuck_options"), Jump("mom_kitchen_fuck_loop")

    imagebutton:
        focus_mask True
        pos (450,700)
        idle "buttons/diane_stage01_02.png"
        hover HoverImage("buttons/diane_stage01_02.png")
        action Hide("mom_kitchen_fuck_options"), Jump("mom_kitchen_fuck_cum")

    if M_debbie.get('sex speed') < .175:
        imagebutton:
            focus_mask True
            pos (250,735)
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Hide("mom_kitchen_fuck_options"), Function(M_debbie.set, "sex speed", M_debbie.get("sex speed") + 0.05), Jump("mom_kitchen_fuck_loop")

    if M_debbie.get('sex speed') > .076:
        imagebutton:
            focus_mask True
            pos (450,735)
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Hide("mom_kitchen_fuck_options"), Function(M_debbie.set, "sex speed", M_debbie.get("sex speed") - 0.05), Jump("mom_kitchen_fuck_loop")

screen bedroom_debbie_sleepover_options():
    tag quick_menu

    imagebutton:
        focus_mask True
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("bedroom_debbie_sleepover_options"), Jump("bedroom_debbie_sleepover_loop")
        xpos 250
        ypos 700

    imagebutton:
        focus_mask True
        idle "buttons/diane_stage01_02.png"
        hover HoverImage("buttons/diane_stage01_02.png")
        action Hide("bedroom_debbie_sleepover_options"), Jump("bedroom_debbie_sleepover_cum")
        xpos 450
        ypos 700

    imagebutton:
        pos (370,665)
        idle "buttons/diane_stage01_04.png"
        hover HoverImage("buttons/diane_stage01_04.png")
        action Hide("bedroom_debbie_sleepover_options"), Function(M_debbie.toggle, "change angle"), SetVariable("animated", False), Jump("bedroom_debbie_sleepover_loop")

    if M_debbie.get('sex speed') < .12:
        imagebutton:
            focus_mask True
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Hide("bedroom_debbie_sleepover_options"), Function(M_debbie.set, "sex speed", M_debbie.get("sex speed") + 0.03), Jump("bedroom_debbie_sleepover_loop")
            xpos 250
            ypos 735

    if M_debbie.get('sex speed') > .061:
        imagebutton:
            focus_mask True
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Hide("bedroom_debbie_sleepover_options"), Function(M_debbie.set, "sex speed", M_debbie.get("sex speed") - 0.03), Jump("bedroom_debbie_sleepover_loop")
            xpos 450
            ypos 735

screen shower_mom_sex_options():
    tag quick_menu

    imagebutton:
        pos (250,700)
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("shower_mom_sex_options"), Jump("mom_shower_sex_loop")

    imagebutton:
        pos (450,700)
        idle "buttons/diane_stage01_02.png"
        hover HoverImage("buttons/diane_stage01_02.png")
        action Hide("shower_mom_sex_options"), Jump("mom_shower_sex_cum")

    if anim_toggle:
        if M_debbie.get("sex speed") < .4:
            imagebutton:
                pos (250,735)
                idle "buttons/speed_02.png"
                hover HoverImage("buttons/speed_02.png")
                action Hide("shower_mom_sex_options"), Function(M_debbie.set, "sex speed", M_debbie.get('sex speed') + 0.1), Jump("mom_shower_sex_loop")

        if M_debbie.get("sex speed") > .21:
            imagebutton:
                pos (450,735)
                idle "buttons/speed_01.png"
                hover HoverImage("buttons/speed_01.png")
                action Hide("shower_mom_sex_options"), Function(M_debbie.set, "sex speed", M_debbie.get('sex speed') - 0.1), Jump("mom_shower_sex_loop")

screen debbie_shower_blowjob_options():
    tag quick_menu

    imagebutton:
        pos (170,700)
        focus_mask True
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("debbie_shower_blowjob_options"), Jump("debbie_shower_blowjob_loop")

    imagebutton:
        pos (370,700)
        focus_mask True
        idle "buttons/diane_stage01_02.png"
        hover HoverImage("buttons/diane_stage01_02.png")
        action Hide("debbie_shower_blowjob_options"), Jump("debbie_shower_blowjob_cum_in")

    imagebutton:
        pos (570,700)
        focus_mask True
        idle "buttons/diane_stage01_03.png"
        hover HoverImage("buttons/diane_stage01_03.png")
        action Hide("debbie_shower_blowjob_options"), Jump("debbie_shower_blowjob_cum_out")

    if M_debbie.get('sex speed') < .4:
        imagebutton:
            focus_mask True
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Hide("debbie_shower_blowjob_options"), Function(M_debbie.set, "sex speed", M_debbie.get("sex speed") + 0.1), Jump("debbie_shower_blowjob_loop")
            xpos 250
            ypos 735

    if M_debbie.get('sex speed') > .21:
        imagebutton:
            focus_mask True
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Hide("debbie_shower_blowjob_options"), Function(M_debbie.set, "sex speed", M_debbie.get("sex speed") - 0.1), Jump("debbie_shower_blowjob_loop")
            xpos 450
            ypos 735

screen car_mom_jerk_options():
    tag quick_menu

    imagebutton:
        pos (250,700)
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("car_mom_jerk_options"), Jump("mom_car_jerk_loop")

    imagebutton:
        pos (450,700)
        idle "buttons/cam_stage01_02.png"
        hover HoverImage("buttons/cam_stage01_02.png")
        action Hide("car_mom_jerk_options"), Jump("home_front_mom_car_fixed_check_car_finished")

screen car_mom_sex_options():
    tag quick_menu

    imagebutton:
        focus_mask True
        pos (250,700)
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("car_mom_sex_options"), Jump("car_mom_sex_loop")

    imagebutton:
        focus_mask True
        pos (450,700)
        if M_debbie.is_set("car jerk"):
            idle "buttons/cam_stage01_02.png"
            hover HoverImage("buttons/cam_stage01_02.png")
        else:
            idle "buttons/diane_stage01_02.png"
            hover HoverImage("buttons/diane_stage01_02.png")
        action Hide("car_mom_sex_options"), Jump("car_mom_sex_cum")

    if (M_debbie.get("sex speed") < .225 and M_debbie.is_set("car jerk")) or (M_debbie.get("sex speed") < .175 and not M_debbie.is_set("car jerk")):
        imagebutton:
            focus_mask True
            pos (250,735)
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Hide("car_mom_sex_options"), Function(M_debbie.set, "sex speed", M_debbie.get("sex speed") + 0.05), Jump("car_mom_slower_dialogue")

    if (M_debbie.get("sex speed") > .126 and M_debbie.is_set("car jerk")) or (M_debbie.get("sex speed") > .076 and not M_debbie.is_set("car jerk")):
        imagebutton:
            focus_mask True
            pos (450,735)
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Hide("car_mom_sex_options"), Function(M_debbie.set, "sex speed", M_debbie.get("sex speed") - 0.05), Jump("car_mom_faster_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
