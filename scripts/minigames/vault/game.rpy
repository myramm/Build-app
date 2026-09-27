init python in vault:
    '''
    Work out how to navigate the wall of randomised safety deposit boxes
    and find box number 11082.
    '''

    from math import sqrt


    def distance(o, vp):
        n = (vp.xadjustment.value, vp.yadjustment.value)
        return sqrt((o[0] - n[0]) ** 2 + (o[1] - n[1]) ** 2)


    def scroll(x):
        if renpy.display.focus.get_grab():
            return 0.
        return x
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
