init python hide:
    '''
    A single-child displayable used to track the cursor, snapping back
    to a default position should the cursor leaves the game's bounds.
    '''

    from renpy.display.core import Displayable


    class Cursor(Displayable):
        def __init__(self, child, **properties):
            super(Cursor, self).__init__()
            self.transform = Transform(child, **properties)
            self.child = Fixed(self.transform)
            self.pos = self.transform.get_placement()[:2]
        
        def render(self, width, height, st, at):
            return renpy.render(self.child, width, height, st, at)
        
        def event(self, ev, x, y, st):
            pos = x, y
            if pos < (0, 0):
                pos = self.pos
            if self.transform.pos != pos:
                self.transform.pos = pos
                renpy.redraw(self, 0)


    store.Cursor = Cursor
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
