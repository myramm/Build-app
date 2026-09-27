screen trailer():
    add game.timer.image("backgrounds/location_trailer{}.jpg")

    if player.location.is_here(M_clyde) and not M_crystal.mood:
        imagebutton:
            focus_mask True
            pos (347,373)
            idle game.timer.image("objects/character_clyde_02{}.png")
            hover HoverImage(game.timer.image("objects/character_clyde_02{}.png"))
            action TalkTo(M_clyde)

    if player.location.is_here(M_roxxy):
        imagebutton:
            focus_mask True
            pos (622,412)
            idle "objects/character_roxxy_01.png"
            hover HoverImage("objects/character_roxxy_01.png")
            action TalkTo(M_roxxy)

    if player.location.is_here(M_crystal):
        imagebutton:
            focus_mask True
            if M_crystal.mood == 'bliss':
                pos 548, 471
                idle M_crystal.get_button_path(3)
                hover HoverImage(M_crystal.get_button_path(3))
            else:
                pos 570, 447
                idle M_crystal.get_button_path(2)
                hover HoverImage(M_crystal.get_button_path(2))
            action TalkTo(M_crystal)

    if M_roxxy.get("trailer foreclosed"):
        imagebutton:
            focus_mask True
            pos (771,319)
            idle game.timer.image("objects/object_door_85b{}.png")
            hover HoverImage(game.timer.image("objects/object_door_85b{}.png"))
            action Hide("trailer"), Jump("trailer_foreclosed_dialogue")

    else:
        imagebutton:
            focus_mask True
            pos (787,320)
            idle game.timer.image("objects/object_door_85{}.png")
            hover HoverImage(game.timer.image("objects/object_door_85{}.png"))
            action MoveTo(L_trailer_interior)

    imagebutton:
        focus_mask True
        align 0.5,0.97
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action MoveTo(L_trailerpark)

    use mods_screens_hook("trailer")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
