init python early hide:
    from operator import attrgetter

    from renpy import store


    unpack = attrgetter('ctrl', 'loop', 'spec', 'ttl')


    class AnimatedImage2(renpy.Displayable):
        
        @classmethod
        def signal(cls, code):
            if hasattr(store, 'animstate'):
                store.animstate.ctrl = code
        
        
        def __init__(self, machine=None, speed=12, **kwargs):
            super(AnimatedImage2, self).__init__(**kwargs)
            self.frame = 0
            self.spec = []
            self.ttl = 1. / speed
            self.machine = machine
        
        def _duplicate(self, args):
            if renpy.predicting():
                return Fixed(*self.visit())
            
            state = getattr(store, 'animstate', None)
            
            if not state or not renpy.showing(args.name):
                state = object()
                state.ctrl = None
                state.spec = list(reversed(self.spec))
                state.ttl = self.ttl
                state.loop = state.spec.pop()
                store.animstate = state
            
            rv = AnimatedImage2()
            rv.name = args.name
            rv.machine = self.machine
            rv.state = state
            rv._unique()
            
            return rv
        
        def loop(self, asset, count, shift=1, start=0):
            loop = tuple(renpy.displayable(asset.format(shift + i % count))
                         for i in xrange(start, start + count))
            
            self.spec.append(loop)
            return self
        
        def render(self, width, height, st, at):
            state = self.state
            ctrl, loop, spec, ttl = unpack(state)
            
            if spec:
                if spec[-1] == ctrl:
                    spec.pop()
                    state.ctrl = None
                
                if spec[-1] == self.frame:
                    spec.pop()
                
                if isinstance(spec[-1], tuple):
                    loop = state.loop = spec.pop()
                    self.frame = 0
            
            rv = renpy.render(loop[self.frame], width, height, st, at)
            
            if self.machine in store.machines:
                ttl = store.machines[self.machine].get('sex speed')
            
            renpy.redraw(self, ttl)
            
            self.frame += 1
            self.frame %= len(loop)
            
            return rv
        
        def visit(self):
            return [] 
        
        def wait(self, event):
            self.spec.append(event)
            return self


    store.AnimatedImage2 = AnimatedImage2
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
