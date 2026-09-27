style hover is window

init python early hide:
    '''

    '''

    from pygame import MOUSEMOTION
    from renpy.display.focus import get_focused, get_grab
    from renpy.display.layout import Window


    class Hover(Window):
        def __init__(self, child=None, owner=None, **properties):
            super(Hover, self).__init__(child, **properties)
            self.owner = owner
            self.hovered = False
        
        def set_style_prefix(self, prefix, root):
            if root:
                super(Hover, self).set_style_prefix(prefix, root)
        
        def event(self, ev, x, y, st):
            rv = super(Hover, self).event(ev, x, y, st)
            
            if not get_grab() and ev.type == MOUSEMOTION:
                xmax, ymax = self.window_size
                hovered = (0 <= x < xmax) and (0 <= y < ymax)
                
                if self.owner:
                    hovered &= get_focused() is self.owner
                
                if hovered and not self.hovered:
                    self.set_style_prefix(self.role + 'hover_', True)
                    self.hovered = True
                
                elif not hovered and self.hovered:
                    self.set_style_prefix(self.role + 'idle_', True)
                    self.hovered = False
            
            return rv


    store.Hover = Hover


    sl = renpy.register_sl_displayable('hover', Hover, 'hover', 1)
    sl.add_property('owner')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
