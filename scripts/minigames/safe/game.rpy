init python hide:
    '''
    '''

    from math import log

    from store.util import struct


    class SafeMinigame(renpy.python.NoRollback):
        def __init__(self, combo):
            self.angle = 0
            self.combo = tuple(combo)
            self.input = []
            self.len = len(self.combo)
            self.schedule = Scheduler()
            self.sensitive = True
            self.wait = .0001
        
        def end(self):
            combo = tuple(self.input)
            rv = struct(fail=combo != self.combo, input=combo)
            
            if not rv.fail:
                self.angle += 360 * self.len % 2 - 180
                self.wait = 3.
            
            self.schedule(1., Return(rv))
        
        def next(self):
            if len(self.input) == self.len:
                return self.end()
            
            self.sensitive = True
        
        def rotate(self, num):
            length = len(self.input)
            moment = length % 2 * 2 - 1
            origin = self.input[-1] if self.input else 0
            passes = self.len - length
            
            if cmp(origin, num) == moment:
                passes -= 1
            
            travel = 360 * moment * passes - 36 * (num - origin)
            
            self.angle += travel
            self.input.append(num)
            self.wait = log(abs(travel))
            self.sensitive = False
            self.schedule(self.wait, Function(self.next))
        
        @property
        def rotation(self):
            return safe_dial(self.angle, self.wait)


    store.SafeMinigame = SafeMinigame
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
