screen helen_bedroom_sex_options():
    tag quick_menu

    imagebutton:
        focus_mask True
        pos (250,700)
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("helens_bedroom"), Jump("helen_bedroom_sex_loop")

    imagebutton:
        focus_mask True
        pos (450,700)
        idle "buttons/diane_stage01_02.png"
        hover HoverImage("buttons/diane_stage01_02.png")
        action Hide("helens_bedroom"), Jump("helen_bedroom_sex_cum")

    if M_helen.get("sex speed") < .175:
        imagebutton:
            focus_mask True
            pos (250,735)
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Hide("helens_bedroom"), Function(M_helen.set, "sex speed", M_helen.get("sex speed") + 0.05), Jump("helen_bedroom_sex_loop")

    if M_helen.get("sex speed") > .076:
        imagebutton:
            focus_mask True
            pos (450,735)
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Hide("helens_bedroom"), Function(M_helen.set, "sex speed", M_helen.get("sex speed") - 0.05), Jump("helen_bedroom_sex_loop")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
