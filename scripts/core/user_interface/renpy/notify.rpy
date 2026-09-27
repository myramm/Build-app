

screen notify(message):

    zorder 100
    style_prefix 'notify'

    frame at notify_appear:
        text '[message!tq]'

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame:
    background 'notify'
    padding (10, 6, 40, 5)
    ypos 135
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
