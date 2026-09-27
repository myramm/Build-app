init python hide:
    '''
    A no-op displayable used for scheduling arbitrary time-based actions
    within a screen offering more flexibilty than the vanilla Timer.
    '''

    from renpy.display.behavior import run
    from renpy.display.layout import Null
    from renpy.exports import timeout


    class Scheduler(Null):
        __version__ = 0
        
        def __init__(self, replaces=None, **properties):
            super(self.__class__, self).__init__(**properties)
            self.active = []
            self.queued = []
        
        def __call__(self, delay, action=None, args=(), kwargs={}):
            if delay <= 0:
                raise Exception('delay must be greater than zero')
            self.queued.append((delay, action, args, kwargs))
        
        def clear(self):
            self.active.clear()
            self.queued.clear()
        
        def event(self, ev, x, y, st):
            if self.queued:
                self.active.extend((e[0] + st,) + e[1:] for e in self.queued)
                self.active.sort(reverse=True)
                self.queued.clear()
            
            if not self.active:
                return
            
            if self.active[-1][0] > st:
                timeout(self.active[-1][0] - st)
                return
            
            _, fn, args, kwargs = self.active.pop()
            
            if self.active:
                timeout(self.active[-1][0] - st)
            
            return run(fn, *args, **kwargs)


    store.Scheduler = Scheduler
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
