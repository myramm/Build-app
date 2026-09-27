screen bank():
    add L_bank.background

    imagebutton:
        focus_mask True
        pos 495, 372
        idle game.timer.image('objects/object_door_189{}.png')
        hover HoverImage(game.timer.image('objects/object_door_189{}.png'))
        action MoveTo(L_bank_lobby)

    if L_bank.is_here(M_tony):
        imagebutton:
            focus_mask True
            pos 735, 408
            idle M_tony.get_button_path('bank', use_day_timer=True)
            hover HoverImage(M_tony.get_button_path('bank', use_day_timer=True))
            action TalkTo(M_tony)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
