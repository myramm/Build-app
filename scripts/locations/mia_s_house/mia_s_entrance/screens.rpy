screen mias_house_entrance():
    add player.location.background

    if player.location.is_here(M_mia):
        imagebutton:
            focus_mask True
            pos (280,330)
            idle "objects/character_mia_01c.png"
            hover HoverImage("objects/character_mia_01c.png")
            action TalkTo(M_mia)

    imagebutton:
        focus_mask True
        pos (531,267)
        idle game.timer.image("objects/object_stairs_05{}.png")
        hover HoverImage(game.timer.image("objects/object_stairs_05{}.png"))
        action MoveTo(L_miahouse_upstairs)

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_08.png"
        hover HoverImage("boxes/auto_option_08.png")
        action MoveTo(L_miahouse)

    use mods_screens_hook("mias_house_entrance")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
