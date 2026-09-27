screen police_lobby():
    add player.location.background

    imagebutton:
        focus_mask True
        pos (151,360)
        idle "images/objects/object_door_49.png"
        hover HoverImage("images/objects/object_door_49.png")
        action MoveTo(L_police_basement)

    imagebutton:
        focus_mask True
        pos 512, 395
        idle "images/objects/object_picture_pika.png"
        hover HoverImage("images/objects/object_picture_pika.png")
        action HideAll(), Jump('police_lobby_pika')

    imagebutton:
        focus_mask True
        pos (586,376)
        idle "images/objects/object_door_50.png"
        hover HoverImage("images/objects/object_door_50.png")
        action MoveTo(L_police_office)

    imagebutton:
        focus_mask True
        pos (12,338)
        idle "images/objects/object_board_03.png"
        hover HoverImage("images/objects/object_board_03.png")
        action Hide("police_lobby"), Jump("police_board")

    imagebutton:
        focus_mask True
        align 0.5,0.95
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action ExitLocation()

    use mods_screens_hook("police_lobby")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
