screen tina_lounge():
    add L_tina_lounge.background

    imagebutton:
        focus_mask True
        pos 27, 284
        idle game.timer.image('objects/object_door_197{}.png')
        hover HoverImage(game.timer.image('objects/object_door_197{}.png'))
        action MoveTo(L_apt_hall3)

    imagebutton:
        focus_mask True
        pos 484, 274
        idle game.timer.image('objects/object_door_198{}.png')
        hover HoverImage(game.timer.image('objects/object_door_198{}.png'))
        action MoveTo(L_tina_bed2)

    if L_tina_lounge.is_here(M_tina) and M_tina.pregnancy.stage:
        imagebutton:
            focus_mask True
            pos 800, 320
            idle M_tina.get_button_path('lounge', use_baby=True)
            hover HoverImage(M_tina.get_button_path('lounge', use_baby=True))
            action TalkTo(M_tina)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
