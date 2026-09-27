init python in popup:
    '''
    Machinery to proxy popups in a way such that if an erroneous popup
    is triggered it unobtrusively yields debug information rather than
    crashing the game. This is important while in active development.
    '''

    def _proxy(name, *args, **kwargs):
        try:
            return globals()[name](*args, **kwargs)
        except:
            return missing()


screen popup_proxy(name, *args, **kwargs):
    modal renpy.get_mode() == 'screen' tag popup
    sensitive renpy.get_mode() == 'screen'

    zorder 100

    add kwargs.pop('background', None)

    default spec = popup._proxy(name, *args, **kwargs)
    use expression spec[0] pass (*spec[1:])


label popup(name, *args, **kwargs):
    with None
    show screen popup_proxy(name, *args, **kwargs)
    with dissolve
    pause
    hide screen popup
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
