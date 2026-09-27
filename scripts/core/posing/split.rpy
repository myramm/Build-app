transform splitcoreX(r, anchor=.5, off=0):
    align (anchor, .5)
    rotate r
    rotate_pad False
    subpixel True
    transform_anchor True
    xoffset off
    xpos .5

transform splitshowX(r, off=0, pos=1., s=0, t=.75):
    splitcoreX(0, anchor=pos, off=off)
    xoffset s xpos pos
    easein_cubic t rotate r xoffset off + s * .5 xpos .5

transform splithideX(r, off=0, pos=1., s=0, t=.75):
    splitcoreX(r, anchor=pos, off=off)
    xoffset off + s * .5 xpos .5
    easeout_cubic t rotate 0 xoffset s xpos pos


transform splitcoreY(r, anchor=.5, off=0):
    align (.5, anchor)
    rotate r
    rotate_pad False
    subpixel True
    transform_anchor True
    yoffset off
    ypos .5

transform splitshowY(r, off=0, pos=1., s=0, t=.75):
    splitcoreY(0, anchor=pos, off=off)
    yoffset s ypos pos
    easein_cubic t rotate r yoffset off + s * .5 ypos .5

transform splithideY(r, off=0, pos=1., s=0, t=.75):
    splitcoreY(r, anchor=pos, off=off)
    yoffset off + s * .5 ypos .5
    easeout_cubic t rotate 0 yoffset s ypos pos


init python hide:
    '''
    Custom transform (and transitions) for displaying split screens.
    This is an intentionally naive approach with no foreground
    obfuscation in order to avoid needing to deal with layers.
    '''

    gap = 10

    box = Transform('black', zoom=2)
    opt = {'fit_first': True, 'subpixel': True}

    barX = Transform(Solid('fff', xsize=gap), yzoom=2)
    barY = Transform(Solid('fff', ysize=gap), xzoom=2)


    def splitmask(mask, t, st, at):
        if not isinstance(t.child, AlphaMask):
            t.set_child(AlphaMask(t.child, mask), duplicate=False)


    class Split(_object):
        def __init__(self, angle, anchor='right', delay=.75, offset=0):
            self.delay = delay
            
            if anchor in ('left', 'right'):
                splitcore = splitcoreX
                splithide = splithideX
                splitshow = splitshowX
                bar = barX
            else:
                splitcore = splitcoreY
                splithide = splithideY
                splitshow = splitshowY
                bar = barY
            
            anchor = {'bottom': 1., 'left': 0., 'right': 1., 'top': 0.}[anchor]
            margin = gap * (anchor * 2 - 1)
            
            core = splitcore(angle, off=offset)
            self.core_box = core(anchor=anchor, child=box)
            self.core_bar = core(child=bar)
            
            hide = splithide(angle, off=offset, pos=anchor, t=delay)
            self.hide_box = hide(child=box)
            self.hide_bar = hide(s=margin, child=bar)
            
            show = splitshow(angle, off=offset, pos=anchor, t=delay)
            self.show_box = show(child=box)
            self.show_bar = show(s=margin, child=bar)
            
            new = Transform(self.core_box, rotate=180, transform_anchor=True)
            old = self.core_box
            
            self.new = Transform(function=renpy.partial(splitmask, new))
            self.old = Transform(function=renpy.partial(splitmask, old))
        
        def __call__(self, i):
            return Fixed(AlphaMask(i, self.core_box), self.core_bar, **opt)
        
        def show(self, old_widget=None, new_widget=None):
            bar = self.show_bar()
            old = Fixed(old_widget, bar, **opt)
            new = Fixed(new_widget, bar, **opt)
            return AlphaDissolve(self.show_box(), self.delay)(new, old)
        
        def hide(self, old_widget=None, new_widget=None):
            bar = self.hide_bar()
            old = Fixed(old_widget, bar, **opt)
            new = Fixed(new_widget, bar, **opt)
            return AlphaDissolve(self.hide_box(), self.delay)(old, new)


    store.Split = Split
    store.splitmask = splitmask
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
