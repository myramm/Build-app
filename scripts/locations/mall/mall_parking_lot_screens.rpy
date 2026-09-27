screen mall_parking_lot():
    add L_mall_parking_lot.background

    imagebutton:
        focus_mask True
        pos 257, 382
        idle game.timer.image("objects/object_door_153{}.png")
        hover HoverImage(game.timer.image("objects/object_door_153{}.png"))
        action MoveTo(L_mall)

    if player.location.is_here(M_consuela):
        imagebutton:
            focus_mask True
            pos 164, 357
            idle 'characters/consuela/buttons/character_consuela_mall.png'
            hover HoverImage('characters/consuela/buttons/character_consuela_mall.png')
            action TalkTo(M_consuela)

    use mods_screens_hook("mall_parking_lot")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
