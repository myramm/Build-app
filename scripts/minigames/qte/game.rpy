init python hide in qte:
    from random import choice

    from renpy.store import qte as export


    opts = {'focus_down': (.5, .75),
            'focus_left': (.1, .45),
            'focus_right': (.9, .45),
            'focus_up': (.5, .15)}
    keys = opts.keys()


    def seq(length):
        return tuple(choice(keys) for _ in xrange(0, length))


    export.keys = keys
    export.opts = opts
    export.seq = seq
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
