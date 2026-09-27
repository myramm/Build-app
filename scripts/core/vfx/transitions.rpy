init python hide in transition:
    from renpy.store import Fixed, Solid
    from store import transition as export


    def FadeOver(*args, **kwargs):
        if 'widget' not in kwargs:
            kwargs['widget'] = Fixed(kwargs['old_widget'],
                                     Solid(kwargs.pop('color', 'fff7')),
                                     fit_first=True)
        return renpy.display.transition.Fade(*args, **kwargs)


    export.FadeOver = FadeOver


init python:
    Blink = renpy.partial(ImageDissolve, 'vfx/eyemask.jpg', ramplen=16)
    FadeOver = renpy.curry(transition.FadeOver)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
