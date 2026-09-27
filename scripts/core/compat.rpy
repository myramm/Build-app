init python early hide:
    try:
        from renpy.compat import PY2
    except ImportError:
        from renpy.six import PY2


    if renpy.version_tuple <= (7, 3, 5, 606):
        orig_dynamic = renpy.dynamic
        
        
        def dynamic(*args, **kwargs):
            if args:
                return orig_dynamic(*args)
            
            args = args + tuple(kwargs)
            orig_dynamic(*args)
            
            for k, v in kwargs.items():
                setattr(renpy.store, k, v)
        
        
        renpy.dynamic = dynamic


    if PY2:
        import math
        math.inf = float('inf')
        
        try:
            import copyreg
        except ImportError:
            import copy_reg as copyreg
        import weakref
        copyreg.pickle(weakref.ReferenceType, lambda r: (print, ()))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
