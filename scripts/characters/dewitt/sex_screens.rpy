screen dewitt_bj_options():
    if M_dewitt.get("sex speed") < .175:
        imagebutton:
            focus_mask True
            pos (250,615)
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Function(M_dewitt.set, "sex speed", M_dewitt.get("sex speed") + 0.05)

    if M_dewitt.get("sex speed") > .076:
        imagebutton:
            focus_mask True
            pos (450,615)
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Function(M_dewitt.set, "sex speed", M_dewitt.get("sex speed") - 0.05)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
