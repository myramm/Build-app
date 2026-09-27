screen iwanka_rumps_bedroom():
    add L_rump_second.background

    imagebutton:
        focus_mask True
        pos 55, 142
        idle game.timer.image('objects/object_door_166{}.png')
        hover HoverImage(game.timer.image('objects/object_door_166{}.png'))
        action MoveTo(L_rump_lobby)

    if L_rump_second.is_here(M_iwanka):
        imagebutton:
            focus_mask True
            if M_iwanka.pregnancy.stage > 4:
                pos 271, 286
                idle M_iwanka.get_button_path('bedroom', use=('baby',))
                hover HoverImage(M_iwanka.get_button_path('bedroom', use=('baby',)))
            elif M_iwanka.pregnancy.stage > 1:
                pos 270, 272
                if M_iwanka.outfit.is_naked:
                    idle M_iwanka.get_button_path('bedroom_naked', use=('bump', 'belly'))
                    hover HoverImage(M_iwanka.get_button_path('bedroom_naked', use=('bump', 'belly')))
                else:
                    idle M_iwanka.get_button_path('bedroom', use=('bump', 'belly'))
                    hover HoverImage(M_iwanka.get_button_path('bedroom', use=('bump', 'belly')))
            elif M_iwanka.outfit.is_naked:
                pos 484, 398
                idle M_iwanka.get_button_path('bedroom_naked')
                hover HoverImage(M_iwanka.get_button_path('bedroom_naked'))
            elif game.timer.is_evening() or game.timer.is_weekend() and game.timer.is_afternoon():
                pos 283, 357
                idle M_iwanka.get_button_path('bedroom_bored')
                hover HoverImage(M_iwanka.get_button_path('bedroom_bored'))
            else:
                pos 278, 332
                idle M_iwanka.get_button_path('bedroom')
                hover HoverImage(M_iwanka.get_button_path('bedroom'))
            action TalkTo(M_iwanka)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
