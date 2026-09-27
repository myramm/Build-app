screen school_frontyard():
    add L_school_front.background

    imagebutton:
        focus_mask True
        pos 432, 309
        idle game.timer.image("objects/object_door_151{}.png")
        hover HoverImage(game.timer.image("objects/object_door_151{}.png"))
        action MoveTo(L_school_hall)

    use mods_screens_hook("school_frontyard")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
