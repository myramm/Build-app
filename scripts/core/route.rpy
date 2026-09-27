init python hide:
    '''
    Basic helper for route checking when the game is on rails.
    '''

    from itertools import izip


    def route(*path):
        return izip(path, path[1:])


    store.route = route
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
