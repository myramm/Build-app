screen boat_bridge():
    add L_boat_bridge.background

    if L_boat_bridge.is_here(M_iwanka):
        imagebutton:
            focus_mask True
            if M_iwanka.pregnancy.stage > 1:
                pos 431, 249
                idle M_iwanka.get_button_path('yacht_naked', use=('bump', 'belly'))
                hover HoverImage(M_iwanka.get_button_path('yacht_naked', use=('bump', 'belly')))
            else:
                pos 44, 389
                if M_iwanka.outfit.is_naked:
                    idle M_iwanka.get_button_path('yacht_deck', use_day_timer=True)
                    hover HoverImage(M_iwanka.get_button_path('yacht_deck', use_day_timer=True))
                else:
                    idle M_iwanka.get_button_path('yacht_deck_swimsuit', use_day_timer=True)
                    hover HoverImage(M_iwanka.get_button_path('yacht_deck_swimsuit', use_day_timer=True))
            action TalkTo(M_iwanka)

    imagebutton:
        focus_mask True
        pos (679,278)
        idle game.timer.image("objects/object_door_140{}.png")
        hover HoverImage(game.timer.image("objects/object_door_140{}.png"))
        action MoveTo(L_boat_cabin)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
