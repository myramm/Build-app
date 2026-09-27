screen minigame_pizza2(order=None, quota=None):
    style_prefix 'pizza2'
    sensitive 'game' in locals() and game.phase in ('fail', 'pass', 'play')

    default game = Pizza2Minigame(order=order, quota=quota)

    add game.schedule

    add 'pizza2_scene'

    label _('Add the correct toppings on all pizzas before the time runs out!'):
        style_prefix 'help'

    showif game.phase in ('enter', 'swap'):
        add 'pizza2_base':
            align (.5, .42)
            at pizza2_enter

    showif game.phase in ('play', 'fail'):
        frame:
            align (.5, .42)
            at pizza2_leave

            has fixed
            fit_first True

            add 'pizza2_base'

            for i in game.toppings:
                add 'minigames/pizza2/topping/pizza2_{}.png'.format(i):
                    at pizza2_fade

    showif game.phase == 'play' and game.expect:
        fixed:
            at pizza2_fade

            add 'minigames/pizza2/item/pizza2_[game.expect].png':
                anchor (.5, .5)
                at pizza2_pulse(1)
                pos (.5, .1725)

            add 'pizza2_arrow':
                align (.5, .27)
                at pizza2_point

    frame:
        style_suffix 'timer'
        has bar
        style_suffix 'timer_bar'
        range 1
        if game.phase in ('intro', 'play'):
            value AnimatedValue(1, old_value=0, delay=game.ttl)
        else:
            value 1

    if game.phase == 'intro':
        default t = game.ttl
        timer 1 repeat True action SetScreenVariable('t', t - 1)
        for i in xrange(game.ttl):
            showif i == t:
                text str(i):
                    at pizza2_countdown(.5)

    if game.phase == 'enter':
        text 'GO':
            at pizza2_countdown(1.)

    grid 7 2:
        for i in game.opts:
            imagebutton:
                action Function(game.add, i)
                idle pizza2_item('minigames/pizza2/item/pizza2_{}.png'.format(i))
                hover pizza2_item(im.MatrixColor('minigames/pizza2/item/pizza2_{}.png'.format(i), over))
                insensitive pizza2_item(im.MatrixColor('minigames/pizza2/item/pizza2_{}.png'.format(i), dead))
                sensitive game.phase == 'play'

    if game.phase in ('fail', 'pass'):
        timer .5 action Return(game.code)


image pizza2_item_frame = Frame('minigames/pizza2/pizza2_item.png', 5)


style pizza2_grid:
    xspacing 38.4
    yspacing 25.6
    align (.5, .935)

style pizza2_image_button:
    align (.5, .5)
    background 'pizza2_item_frame'
    padding (5, 5, 5, 2)

style pizza2_text:
    outlines ((10, 'f70', 0, 0),)
    align (.5, .3)
    size 120
    bold True

style pizza2_timer_bar:
    right_bar '#f339'
    xysize (650, 10)

style pizza2_timer:
    align (.5, .585)


transform pizza2_countdown(t):
    on start:
        subpixel True
        zoom .6
        ease .1 zoom 1.
        t
        ease .4 alpha 0.
    on show:
        subpixel True
        zoom .6
        ease .1 zoom 1.
        t
        ease .4 alpha 0.
transform pizza2_enter:
    subpixel True
    on show:
        xoffset 1024 * 1.25
        .5
        ease 1 xoffset 0
transform pizza2_fade:
    on start:
        alpha 0.
        easein .2 alpha 1.
    on show:
        alpha 0.
        easein .2 alpha 1.
    on hide:
        alpha 1.
        easein .2 alpha 0.
transform pizza2_item:
    subpixel True
    zoom .75
transform pizza2_leave:
    subpixel True
    on hide:
        .5
        ease 1 xoffset -1024 * 1.25
        xoffset 0
transform pizza2_point:
    subpixel True
    ease 1 yoffset -5
    ease 1 yoffset 5
    repeat
transform pizza2_pulse(t):
    subpixel True
    ease t zoom .90
    ease t zoom 1.05
    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
