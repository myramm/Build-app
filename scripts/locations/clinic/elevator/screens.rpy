screen hospital_elevator():
    add player.location.background

    vbox:
        anchor .5, .5
        spacing 10
        pos 505, 330

        imagebutton:
            focus_mask True
            idle "buttons/elevator_03.png"
            hover HoverImage("buttons/elevator_03.png")
            action MoveTo(L_hospital_floor3)

        imagebutton:
            focus_mask True
            idle "buttons/elevator_02.png"
            hover HoverImage("buttons/elevator_02.png")
            action MoveTo(L_hospital_floor2)

        imagebutton:
            focus_mask True
            idle "buttons/elevator_01.png"
            hover HoverImage("buttons/elevator_01.png")
            action MoveTo(L_hospital_lobby)

        imagebutton:
            focus_mask True
            idle "buttons/elevator_00.png"
            hover HoverImage("buttons/elevator_00.png")
            action MoveTo(L_hospital_basement)

    use mods_screens_hook("hospital_elevator")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
