screen june_mcbedroom_normal_sex_options():
    tag quick_menu

    imagebutton:
        focus_mask True
        pos (150,700)
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("june_mcbedroom_normal_sex_options"), Jump("june_bedroom_dialogue_normal_sex_loop")

    imagebutton:
        focus_mask True
        pos (350,700)
        idle "buttons/diane_stage01_03.png"
        hover HoverImage("buttons/diane_stage01_03.png")
        action Hide("june_mcbedroom_normal_sex_options"), Jump("june_bedroom_dialogue_normal_sex_cum_outside")

    imagebutton:
        focus_mask True
        pos (550,700)
        idle "buttons/diane_stage01_02.png"
        hover HoverImage("buttons/diane_stage01_02.png")
        action Hide("june_mcbedroom_normal_sex_options"), Jump("june_bedroom_dialogue_normal_sex_cum_inside")

    if M_june.get('sex speed') < .3:
        imagebutton:
            focus_mask True
            pos (250,735)
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Hide("june_mcbedroom_normal_sex_options"), Function(M_june.set, "sex speed", M_june.get("sex speed") + 0.1), Jump("june_bedroom_dialogue_normal_sex_loop")

    if M_june.get('sex speed') > .11:
        imagebutton:
            focus_mask True
            pos (450,735)
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Hide("june_mcbedroom_normal_sex_options"), Function(M_june.set, "sex speed", M_june.get("sex speed") - 0.1), Jump("june_bedroom_dialogue_normal_sex_loop")

screen june_mcbedroom_cosplay_sex_options():
    tag quick_menu

    imagebutton:
        focus_mask True
        pos (150,700)
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("june_mcbedroom_cosplay_sex_options"), Jump("june_bedroom_dialogue_cosplay_sex_loop")

    imagebutton:
        focus_mask True
        pos (350,700)
        idle "buttons/diane_stage01_03.png"
        hover HoverImage("buttons/diane_stage01_03.png")
        action Hide("june_mcbedroom_cosplay_sex_options"), Jump("june_bedroom_dialogue_cosplay_sex_cum_outside")

    imagebutton:
        focus_mask True
        pos (550,700)
        idle "buttons/diane_stage01_02.png"
        hover HoverImage("buttons/diane_stage01_02.png")
        action Hide("june_mcbedroom_cosplay_sex_options"), Jump("june_bedroom_dialogue_cosplay_sex_cum_inside")

    if M_june.get("sex speed") < .3:
        imagebutton:
            focus_mask True
            pos (250,735)
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Hide("june_mcbedroom_cosplay_sex_options"), Function(M_june.set, "sex speed", M_june.get("sex speed") + 0.1), Jump("june_bedroom_dialogue_cosplay_sex_loop")

    if M_june.get("sex speed") > .11:
        imagebutton:
            focus_mask True
            pos (450,735)
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Hide("june_mcbedroom_cosplay_sex_options"), Function(M_june.set, "sex speed", M_june.get("sex speed") - 0.1), Jump("june_bedroom_dialogue_cosplay_sex_loop")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
