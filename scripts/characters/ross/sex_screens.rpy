screen ross_sex_options():
    tag quick_menu

    imagebutton:
        focus_mask True
        pos (250,700)
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("ross_sex_options"), Jump("ross_hscene_loop")

    imagebutton:
        focus_mask True
        pos (450,700)
        idle "buttons/diane_stage01_02.png"
        hover HoverImage("buttons/diane_stage01_02.png")
        action Hide("ross_sex_options"), Jump("ross_office_ross_sex_cum")

    if anim_toggle:
        if M_ross.get("sex speed") < .15:
            imagebutton:
                focus_mask True
                pos (250,735)
                idle "buttons/speed_02.png"
                hover HoverImage("buttons/speed_02.png")
                action Hide("ross_sex_options"), Function(M_ross.set, "sex speed", M_ross.get("sex speed") + 0.05), Jump("ross_hscene_loop")

        if M_ross.get("sex speed") > .06:
            imagebutton:
                focus_mask True
                pos (450,735)
                idle "buttons/speed_01.png"
                hover HoverImage("buttons/speed_01.png")
                action Hide("ross_sex_options"), Function(M_ross.set, "sex speed", M_ross.get("sex speed") - 0.05), Jump("ross_hscene_loop")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
