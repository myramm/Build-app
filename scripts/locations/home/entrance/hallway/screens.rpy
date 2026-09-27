screen hallway():
    add player.location.background


    imagebutton:
        focus_mask True
        pos (175,280)
        idle game.timer.image("objects/object_door_02{}.png")
        hover HoverImage(game.timer.image("objects/object_door_02{}.png"))
        action MoveTo(L_home_bedroom)


    imagebutton:
        focus_mask True
        pos (387,225)
        idle game.timer.image("objects/object_door_03{}.png")
        hover HoverImage(game.timer.image("objects/object_door_03{}.png"))
        action MoveTo(L_home_sisbedroom)


    imagebutton:
        focus_mask True
        if game.in_shower is not None:
            pos (526,108)
            idle "objects/object_door_04_busy.png"
            hover HoverImage("objects/object_door_04_busy.png")
        else:
            pos (580,108)
            idle game.timer.image("objects/object_door_04{}.png")
            hover HoverImage(game.timer.image("objects/object_door_04{}.png"))
        action MoveTo(L_home_shower)


    imagebutton:
        focus_mask True
        pos (830,0)
        idle game.timer.image("objects/object_door_19{}.png")
        hover HoverImage(game.timer.image("objects/object_door_19{}.png"))
        action MoveTo(L_home_entrance)


    imagebutton:
        focus_mask True
        pos (360,40)
        idle game.timer.image("objects/object_door_40{}.png")
        hover HoverImage(game.timer.image("objects/object_door_40{}.png"))
        action MoveTo(L_home_attic)

    use mods_screens_hook("hallway")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
