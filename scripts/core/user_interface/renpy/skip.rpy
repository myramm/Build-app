

screen skip_indicator():

    zorder 100
    style_prefix 'skip'

    frame:

        has hbox
        spacing 5

        text _('Skipping')

        text '▸' at delayed_blink(0.0, 1.0) style 'skip_triangle'
        text '▸' at delayed_blink(0.2, 1.0) style 'skip_triangle'
        text '▸' at delayed_blink(0.4, 1.0) style 'skip_triangle'


transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is notify_frame:
    ypos 100

style skip_triangle is skip_text
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
