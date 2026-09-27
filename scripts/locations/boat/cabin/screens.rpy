screen boat_cabin():
    add L_boat_cabin.background

    if L_boat_cabin.is_here(M_iwanka):
        imagebutton:
            focus_mask True
            pos 486, 346
            idle M_iwanka.get_button_path('yacht_bed', use_day_timer=True)
            hover HoverImage(M_iwanka.get_button_path('yacht_bed', use_day_timer=True))
            action TalkTo(M_iwanka)

    imagebutton:
        focus_mask True
        pos 952, 406
        idle game.timer.image('objects/object_nuke_01{}.png')
        hover HoverImage(game.timer.image('objects/object_nuke_01{}.png'))
        action HideAll(), Jump('yacht_cabin_nuke')

    imagebutton:
        focus_mask True
        pos 175, 273
        idle game.timer.image('objects/object_door_141{}.png')
        hover HoverImage(game.timer.image('objects/object_door_141{}.png'))
        action MoveTo(L_boat_bridge)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
