screen mias_house_upstairs():
    add player.location.background

    imagebutton:
        focus_mask True
        pos (444,419)
        idle game.timer.image("objects/object_door_33{}.png")
        hover HoverImage(game.timer.image("objects/object_door_33{}.png"))
        action MoveTo(L_miahouse_miaroom)

    imagebutton:
        focus_mask True
        pos (615,337)
        idle game.timer.image("objects/object_door_92{}.png")
        hover HoverImage(game.timer.image("objects/object_door_92{}.png"))
        action MoveTo(L_miahouse_helensbedroom)

    imagebutton:
        focus_mask True
        pos (257,238)
        idle game.timer.image("objects/object_door_93{}.png")
        hover HoverImage(game.timer.image("objects/object_door_93{}.png"))
        action MoveTo(L_miahouse_lockedroom)

    imagebutton:
        focus_mask True
        pos (758,110)
        idle game.timer.image("objects/object_door_94{}.png")
        hover HoverImage(game.timer.image("objects/object_door_94{}.png"))
        action MoveTo(L_miahouse_haroldsoffice)

    imagebutton:
        focus_mask True
        pos (0,0)
        idle game.timer.image("objects/object_door_95{}.png")
        hover HoverImage(game.timer.image("objects/object_door_95{}.png"))
        action MoveTo(L_miahouse_entrance)

    use mods_screens_hook("mias_house_upstairs")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
