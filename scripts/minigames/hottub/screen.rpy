screen minigame_hottub(min, max):
    style_prefix 'hottub'

    default pool = HottubMinigame.pool(min, max)
    default done = [not bool(i) for i in pool]

    add 'hottub_scene'
    add 'hottub_net'

    label _('Clean the hot tub by dragging the net over the detritus!'):
        style_prefix 'help'

    grid 5 3:
        for i, item in enumerate(pool):
            if item:
                showif not done[i]:
                    imagebutton:
                        at hottub_float((1 + i / 5 + i % 5) / 7.)
                        idle 'hottub_item_{:02}'.format(item)
                        xoffset i / 5 * (2 - i % 5) * -20
                        action NullAction()
                        hovered SetDict(done, i, True)
            else:
                null

    if all(done):
        timer 1. action Return()


image hottub_net = Cursor('minigames/hottub/hottub_net.png',
                          anchor=(.3, .5), pos=(.5, 680))


style hottub_grid:
    align (.5, .5)
    xspacing 5
    yoffset 30
    yspacing 10


transform hottub_float(t):
    subpixel True
    yoffset 0
    parallel:
        t
        block:
            ease 1. yoffset 4
            ease 1. yoffset 0
            repeat
    parallel:
        on hide:
            linear .3 alpha 0.
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
