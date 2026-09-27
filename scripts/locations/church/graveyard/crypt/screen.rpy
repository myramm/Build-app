screen church_crypt():
    add L_church_crypt.background

    imagebutton:
        focus_mask True
        pos 403, 363
        idle game.timer.image('objects/object_throne.png')
        hover HoverImage(game.timer.image('objects/object_throne.png'))
        action TalkTo(M_odette)

    imagebutton:
        focus_mask True
        align .5, .95
        idle 'boxes/auto_option_generic_01.png'
        hover HoverImage('boxes/auto_option_generic_01.png')
        action MoveTo(L_church_graveyard)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
