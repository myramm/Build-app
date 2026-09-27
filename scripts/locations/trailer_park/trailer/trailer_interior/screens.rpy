screen trailer_interior():
    add player.location.background

    imagebutton:
        focus_mask True
        pos (0,0)
        idle game.timer.image("objects/object_door_86{}.png")
        hover HoverImage(game.timer.image("objects/object_door_86{}.png"))
        action MoveTo(L_trailer)

    imagebutton:
        focus_mask True
        pos (411,312)
        idle game.timer.image("objects/object_door_87{}.png")
        hover HoverImage(game.timer.image("objects/object_door_87{}.png"))
        action MoveTo(L_trailer_bedroom)

    if player.location.is_here(M_crystal):
        imagebutton:
            focus_mask True
            pos (690,288)
            idle M_crystal.get_button_path(1)
            hover HoverImage(M_crystal.get_button_path(1))
            action TalkTo(M_crystal)

    use mods_screens_hook("trailer_interior")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
