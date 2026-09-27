init -1 python hide:
    '''
    Themes are a legacy feature these days and using them gets in the
    way of normal styling. To better facilitate moving away from them
    incrementally we the one we care about but in a namespace.
    '''




    store.build.include_old_themes = True


    class StyleManagerProxy(_object):
        __slots__ = ('_wrapped', '_namespace')
        
        def __init__(self, style, namespace):
            self._wrapped = style
            self._namespace = namespace
        
        def __setattr__(self, name, value):
            if name in self.__class__.__slots__:
                return _object.__setattr__(self, name, value)
            return setattr(self._wrapped, self._namespace + '_' + name, value)
        
        def __getattr__(self, name):
            if name in self.__class__.__slots__:
                return _object.__getattr__(self, name)
            try:
                return getattr(self._wrapped, self._namespace + '_' + name)
            except AttributeError:
                return getattr(self._wrapped, name)


    store.style = StyleManagerProxy(style, 'rr')

    theme.roundrect(
        widget = "#8833ce",
        widget_hover = "#cd249b",
        widget_text = "#000000",
        widget_selected = "#b6d754",
        disabled = "#57cdff",
        disabled_text = "#717be5",
        label = "#000000",
        frame = "#04b4ff",
        mm_root = "backgrounds/menu_menu.jpg",
        gm_root = "backgrounds/menu_quit.jpg",
        rounded_window = False,
    )

    store.style = style._wrapped
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
