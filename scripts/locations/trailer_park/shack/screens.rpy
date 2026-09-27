screen trailer_shack():
    add L_trailer_shack.background

    if player.location.is_here(M_clyde):
        imagebutton:
            focus_mask True
            pos (368,461)
            idle game.timer.image("objects/character_clyde_03{}.png")
            hover HoverImage(game.timer.image("objects/character_clyde_03{}.png"))
            action TalkTo(M_clyde)

    imagebutton:
        focus_mask True
        pos (425,406)
        idle game.timer.image("objects/object_door_129{}.png")
        hover HoverImage(game.timer.image("objects/object_door_129{}.png"))
        action MoveTo(L_trailer_shack_interior)

    if not game.timer.is_dark():
        if M_roxxy.is_state(S_roxxy_get_uniform_on_doggo) and not player.has_item("roxxy_uniform"):
            imagebutton:
                focus_mask True
                pos (148,498)
                idle "objects/object_door_131.png"
                hover HoverImage("objects/object_door_131.png")
                action HideAll(), Jump('rox00_trailerpark_shack_doghouse')
        else:
            add 'object_door_131b' pos (148, 498)

    imagebutton:
        focus_mask True
        align 0.5,0.97
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action MoveTo(L_trailerpark)

    use mods_screens_hook("shack")

screen trailer_shack_interior():
    add L_trailer_shack_interior.background

    if player.location.is_here(M_clyde):
        imagebutton:
            focus_mask True
            pos (384,336)
            idle "objects/character_clyde_04.png"
            hover HoverImage("objects/character_clyde_04.png")
            action Hide("shack_interior"), Jump("clyde_button_dialogue")

    imagebutton:
        focus_mask True
        pos (84,0)
        idle game.timer.image("objects/object_door_130{}.png")
        hover HoverImage(game.timer.image("objects/object_door_130{}.png"))
        action MoveTo(L_trailer_shack)

    use mods_screens_hook("shack_interior")

screen shack_doghouse():
    use trailer_shack
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
