screen minigame_milk(subject='diane'):
    default full = 8.
    default squeeze = None
    default l = 0
    default r = 0

    add 'location_barn_minigame'

    for s, p, z in (('l', l, 1.), ('r', r, -1.)):
        fixed:
            at Transform(xzoom=z)
            anchor (max(z, 0.), 0.)
            pos (.5 + z * .001, 0.)

            if squeeze == s:
                add 'milking_boob_[subject]_milk' at milk_boob
            else:
                add 'milking_boob_[subject]_idle' at milk_boob

            add 'milking_milk_01':
                at milk_level(p / full)

            add 'milking_pump':
                at milk_pump

            add 'milking_bar':
                at milk_pump
                yoffset -200 - 295

        imagebutton:
            action SetScreenVariable(s, p + 1), SetScreenVariable('squeeze', s)
            anchor (.5, .5)
            hover 'milking_button_{}_over'.format(s)
            idle 'milking_button_{}_idle'.format(s)
            insensitive 'milking_button_{}_dead'.format(s)
            keysym ('K_LEFT' if z > 0 else 'K_RIGHT')
            pos (max(0, -z) + .125 * z, .5)
            sensitive p < full and not squeeze

            if not renpy.variant('touch'):
                xpos -1.

    if renpy.variant('touch'):
        label _('Tap the buttons to milk her!'):
            style_prefix 'help'
    else:
        label _('Tap the left and right arrow keys to milk her!'):
            style_prefix 'help'

    if l == full and r == full:
        timer 1. action Return(True)
    elif abs(l - r) > full * .4:
        timer .5 action Return(False)

    if squeeze:
        timer .3 action SetScreenVariable('squeeze', None), With(fastdissolve)


image milking_button_l_idle = 'milking_button_l'
image milking_button_l_over = im.MatrixColor(
    'minigames/milking/milking_button_l.png', over)
image milking_button_l_dead = im.MatrixColor(
    'minigames/milking/milking_button_l.png', dead)
image milking_button_r_idle = 'milking_button_r'
image milking_button_r_over = im.MatrixColor(
    'minigames/milking/milking_button_r.png', over)
image milking_button_r_dead = im.MatrixColor(
    'minigames/milking/milking_button_r.png', dead)


transform milk_boob:
    align (1., 0.)

transform milk_level(x):
    anchor (.5, 1.)
    pos (1., 1.)
    offset (-155, -200)
    crop_relative True
    parallel:
        linear .5 crop (0., 0., 1., x)
    parallel:
        'milking_milk_02' with fastdissolve
        .2
        'milking_milk_01' with fastdissolve
        .2
        'milking_milk_03' with fastdissolve
        .2
        'milking_milk_01' with fastdissolve

transform milk_pump:
    anchor (.5, 1.)
    pos (1., 1.)
    xoffset -155
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
