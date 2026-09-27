screen minigame_safe(code):
    style_prefix 'safe'
    sensitive renpy.get_mode() == 'screen'

    default game = SafeMinigame(code)

    add game.schedule

    add 'safe_background'

    add 'safe_door_shut':
        pos 79, 62

    if renpy.get_mode() == 'screen':
        label _('Enter the combination by selecting the correct digits!'):
            style_prefix 'help'

    frame:
        background '#fff2'
        add '#fff5'

    fixed:
        style_suffix 'dial'
        at game.rotation

        add 'safe_dial'

        for tick in xrange(0, 10):
            fixed:
                style_suffix 'digit'
                at safe_rotate(tick * 36)
                textbutton str(tick * 1):
                    sensitive game.sensitive
                    action Function(game.rotate, tick)
                    keysym str(tick), 'K_KP_' + str(tick)

    if renpy.get_mode() == 'screen' and len(game.input) < game.len:
        imagebutton:
            focus_mask True
            align .5, .95
            idle 'boxes/auto_option_generic_01.png'
            hover HoverImage('boxes/auto_option_generic_01.png')
            action Return(util.struct(fail='abort'))


style safe_button:
    align (.5, 0.)
    padding (20, 35)

style safe_button_text:
    color '000c'
    hover_color '000'
    hover_outlines ((1, '0004', 0, 0),)
    size 18

style safe_dial:
    anchor (.5, .5)
    fit_first True
    pos (507, 362)

style safe_digit:
    align (.5, .5)
    xysize (20, 290)

style safe_frame:
    anchor (.5, .5)
    fit_first True
    padding (1, 0)
    pos (507, 205)
    xysize (4, 12)


transform safe_dial(a, d):
    subpixel True
    ease d rotate a
    repeat

transform safe_rotate(a):
    subpixel True
    rotate a
    transform_anchor False
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
