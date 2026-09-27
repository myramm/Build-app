init python hide:
    '''
    Clean the hottub by dragging the net over the items floating on its
    surface.
    '''

    from random import randint, sample


    class HottubMinigame(object):
        @staticmethod
        def pool(min, max):
            use = sample(xrange(1, 16), randint(min, max))
            use += (None,) * (15 - len(use))
            return tuple(sample(use, len(use)))


    store.HottubMinigame = HottubMinigame
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
