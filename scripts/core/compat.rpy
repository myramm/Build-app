init python early hide:
    try:
        import renpy.exports
        import types

        class _CallableModule(object):
            def __init__(self, m, f):
                self._m = m
                self._f = f
            def __call__(self, *args, **kwargs):
                return self._f(*args, **kwargs)
            def __getattr__(self, name):
                return getattr(self._m, name)
            def __setattr__(self, name, val):
                if name in ('_m', '_f'):
                    object.__setattr__(self, name, val)
                else:
                    setattr(self._m, name, val)

        excluded = {'version'}
        for k in dir(renpy.exports):
            if not k.startswith('_') and k not in excluded:
                existing = getattr(renpy, k, None)
                if k == 'error' and isinstance(existing, types.ModuleType):
                    setattr(renpy, k, _CallableModule(existing, getattr(renpy.exports, k)))
                elif not isinstance(existing, types.ModuleType):
                    setattr(renpy, k, getattr(renpy.exports, k))

        import renpy.curry
        renpy.curry = getattr(renpy.exports, 'curry', getattr(renpy.curry, 'curry', renpy.curry))
        renpy.random = getattr(renpy.exports, 'random', getattr(renpy, 'random', None))
        renpy.file = getattr(renpy.exports, 'file', getattr(renpy, 'file', None))
        import renpy.display.core
        renpy.Displayable = renpy.display.core.Displayable
    except Exception:
        pass

    try:
        from renpy.compat import PY2
    except ImportError:
        from renpy.six import PY2


    if renpy.version_tuple <= (7, 3, 5, 606):
        orig_dynamic = getattr(renpy, 'dynamic', getattr(renpy.exports, 'dynamic', None))
        if orig_dynamic is not None:
            def dynamic(*args, **kwargs):
                if args:
                    return orig_dynamic(*args)
                args = args + tuple(kwargs)
                orig_dynamic(*args)
                for k, v in kwargs.items():
                    setattr(renpy.store, k, v)
            renpy.dynamic = dynamic
            try:
                renpy.exports.dynamic = dynamic
            except Exception:
                pass


    if PY2:
        import math
        math.inf = float('inf')
        
        try:
            import copyreg
        except ImportError:
            import copy_reg as copyreg
        import weakref
        def _dummy_print(*args):
            pass
        copyreg.pickle(weakref.ReferenceType, lambda r: (_dummy_print, ()))

