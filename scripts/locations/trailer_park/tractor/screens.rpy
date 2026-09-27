screen tractor():
    add L_trailer_tractor.background

    if not game.timer.is_dark():
        imagebutton:
            focus_mask True
            pos (499,478)
            idle "objects/object_shooting_01.png"
            hover HoverImage("objects/object_shooting_01.png")
            action MoveTo(L_trailer_shootingrange)

    if player.location.is_here(M_clyde):
        imagebutton:
            focus_mask True
            pos (180,307)
            idle "objects/character_clyde_01.png"
            hover HoverImage("objects/character_clyde_01.png")
            action TalkTo(M_clyde)

    imagebutton:
        focus_mask True
        align 0.5,0.97
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action MoveTo(L_trailerpark)

    use mods_screens_hook("tractor")

screen shooting_range():
    use tractor
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
