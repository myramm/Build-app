screen church():
    default mass = game.timer.is_weekend() and game.timer.is_morning()

    add player.location.background

    imagebutton:
        focus_mask True
        pos (281,367)
        idle game.timer.image("objects/object_door_47{}.png")
        hover HoverImage(game.timer.image("objects/object_door_47{}.png"))
        action MoveTo(L_church_confessional_left)

    imagebutton:
        focus_mask True
        pos (440,368)
        idle game.timer.image("objects/object_door_48{}.png")
        hover HoverImage(game.timer.image("objects/object_door_48{}.png"))
        action MoveTo(L_church_confessional_right)

    imagebutton:
        focus_mask True
        pos (287,169)
        idle game.timer.image("objects/object_door_71{}.png")
        hover HoverImage(game.timer.image("objects/object_door_71{}.png"))
        action MoveTo(L_church_stairs)

    if player.location.is_here(M_keeves):
        imagebutton:
            focus_mask True
            if mass:
                pos 606, 367
                idle "characters/keeves/buttons/character_keeves_church_mass.png"
                hover HoverImage("characters/keeves/buttons/character_keeves_church_mass.png")
            else:
                pos 646, 378
                idle "characters/keeves/buttons/character_keeves_church.png"
                hover HoverImage("characters/keeves/buttons/character_keeves_church.png")
            action TalkTo(M_keeves)

    if player.location.is_here(M_angelica):
        if mass:
            add Transform('objects/character_angelica_02.png', zoom=.435):
                at flip
                crop 15, 0, 80, 175
                pos 722, 377
        else:
            imagebutton:
                focus_mask True
                pos (810,380)
                idle "objects/character_angelica_01.png"
                hover HoverImage("objects/character_angelica_01.png")
                action TalkTo(M_angelica)

    imagebutton:
        focus_mask True
        align 0.5,0.95
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action MoveTo(L_church_front)

    use mods_screens_hook("church")

screen church_front():
    add L_church_front.background

    imagebutton:
        focus_mask True
        pos 914, 195
        idle game.timer.image("objects/object_door_207{}.png")
        hover HoverImage(game.timer.image("objects/object_door_207{}.png"))
        action MoveTo(L_church_graveyard)

    imagebutton:
        focus_mask True
        pos (388,335)
        idle game.timer.image("objects/object_door_115{}.png")
        hover HoverImage(game.timer.image("objects/object_door_115{}.png"))
        action MoveTo(L_church)

    use mods_screens_hook("church_front")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
