screen mia_bedroom_sex_options():
    tag quick_menu

    imagebutton:
        focus_mask True
        pos (150,700)
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("mia_bedroom_sex_options"), Jump("mia_bedroom_sex_loop")

    imagebutton:
        focus_mask True
        pos (350,700)
        idle "buttons/diane_stage01_03.png"
        hover HoverImage("buttons/diane_stage01_03.png")
        action Hide("mia_bedroom_sex_options"), Jump("mia_bedroom_sex_cum_outside")

    imagebutton:
        focus_mask True
        pos (550,700)
        idle "buttons/diane_stage01_02.png"
        hover HoverImage("buttons/diane_stage01_02.png")
        action Hide("mia_bedroom_sex_options"), Jump("mia_bedroom_sex_cum_inside")

    if anim_toggle:
        if M_mia.get("sex speed") < .175:
            imagebutton:
                focus_mask True
                pos (250,735)
                idle "buttons/speed_02.png"
                hover HoverImage("buttons/speed_02.png")
                action Hide("mia_bedroom_sex_options"), Function(M_mia.set, "sex speed", M_mia.get("sex speed") + 0.05), Jump("mia_bedroom_sex_loop")

        if (M_mia.get("sex speed") > .076 and M_mia.is_set("vaginal sex")) or (M_mia.get("sex speed") > .126 and M_mia.get("butt speed") == 1) or (M_mia.get("sex speed") > .076 and M_mia.get("butt speed") > 1):
            imagebutton:
                focus_mask True
                pos (450,735)
                idle "buttons/speed_01.png"
                hover HoverImage("buttons/speed_01.png")
                action Hide("mia_bedroom_sex_options"), If(not M_mia.is_set("vaginal sex"), If(M_mia.get("butt speed") == 1, Function(M_mia.set, "sex speed", .125), Function(M_mia.set, "sex speed", M_mia.get("sex speed") - 0.05)), Function(M_mia.set, "sex speed", M_mia.get("sex speed") - 0.05)), Jump("mia_bedroom_sex_loop")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
