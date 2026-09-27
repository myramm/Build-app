screen medic_room():
    add L_pool_medicroom.background

    if M_anon.is_state(S_ano07_find):
        imagebutton:
            focus_mask True
            pos 524, 542
            idle game.timer.image("objects/object_toolbag.png")
            hover HoverImage(game.timer.image("objects/object_toolbag.png"))
            action HideAll(), Jump('medic_room_toolbag')

    imagebutton:
        focus_mask True
        align .5, .95
        idle 'boxes/auto_option_generic_01.png'
        hover HoverImage('boxes/auto_option_generic_01.png')
        action MoveTo(L_pool)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
