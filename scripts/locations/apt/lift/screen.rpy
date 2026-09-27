screen apt_lift():
    add L_apt_lift.background

    vbox:
        anchor .5, .5
        spacing 20
        pos 505, 330

        imagebutton:
            focus_mask True
            idle "buttons/elevator_03.png"
            hover HoverImage("buttons/elevator_03.png")
            action MoveTo(L_apt_hall3)

        imagebutton:
            focus_mask True
            idle "buttons/elevator_02.png"
            hover HoverImage("buttons/elevator_02.png")
            action MoveTo(L_apt_hall2)

        imagebutton:
            focus_mask True
            idle "buttons/elevator_01.png"
            hover HoverImage("buttons/elevator_01.png")
            action MoveTo(L_apt_lobby)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
