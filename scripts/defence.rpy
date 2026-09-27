init python early hide:
    from renpy.python import StoreDict
    from renpy.store import _dict

    def __setitem__(self, name, value):
        if name == 'set_true':
            value = lambda x: None
        return _dict.__setitem__(self, name, value)

    StoreDict.__setitem__ = __setitem__
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
