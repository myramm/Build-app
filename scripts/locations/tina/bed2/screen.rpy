screen tina_bed2():
    add L_tina_bed2.background

    imagebutton:
        focus_mask True
        pos 220, 343
        idle game.timer.image('objects/object_door_216{}.png')
        hover HoverImage(game.timer.image('objects/object_door_216{}.png'))
        action MoveTo(L_tina_lounge)

    if L_tina_bed2.is_here(M_becca):
        imagebutton:
            focus_mask True
            pos 736, 349
            idle M_becca.get_button_path('bedroom_reading')
            hover HoverImage(M_becca.get_button_path('bedroom_reading'))
            action TalkTo(M_becca)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
