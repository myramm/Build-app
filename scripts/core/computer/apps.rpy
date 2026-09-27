init python in computer.apps:
    from renpy import store
    from renpy.exports import random
    from renpy.store import Action, Call, DictEquality


    class Apps:
        def __init__(self, user):
            self.user = user
            self.apps = {}
            self.root = ()
        
        def __iter__(self):
            return (app for app in self.apps.values() if app.screen)
        
        def add(self, ref, name, screen=None, *args, **kwargs):
            self.apps[ref] = App(self.user, ref, name, screen, *args, **kwargs)
        
        def fetch(self, keys):
            return (self.apps[key] for key in keys)


    class App:
        def __init__(self, user, ref, name, screen, *args, **kwargs):
            action = kwargs.get('action', None)
            hook = kwargs.pop('hook', None)
            icon = kwargs.pop('icon', ref)
            
            self.user = user
            self.ref = ref
            self.title = name
            self.screen = screen
            self.icon = icon
            self.args = args
            self.kwargs = kwargs
            
            self.show = Show(self.ref)
            self.hide = Hide(self.ref)
            
            if screen:
                action = (self.show,)
                if hook:
                    label = 'pc_hook_' + hook
                    if renpy.has_label(label):
                        action += (Call(label),)
            
            self.action = action
            
            
            self.name = __(name).replace('_', '_\u200B')
            
            self.tmp = State(ref)
        
        @property 
        def focused(self):
            z = self.z
            return z and z == store.pc.tmp.z.max
        
        @property 
        def pos(self):
            return store.pc.var.pos.setdefault(
                self.ref, (random.randint(120, 200), random.randint(0, 100)))
        
        @property 
        def z(self):
            return store.pc.tmp.z.get(self.ref, 0)


    class State:
        def __init__(self, ref):
            self.ref = ref
        
        def init(self, **kwargs):
            store.pc.tmp.apps.setdefault(self.ref, dict(**kwargs))
        
        def __getattr__(self, name):
            return self.get(name)
        
        def __setstate__(self, state):
            self.__dict__.update(state)
        
        def get(self, name):
            return store.pc.tmp.apps[self.ref][name]
        
        def set(self, name, value):
            return Update(self.ref, name, value)


    @renpy.pure
    class Show(Action, DictEquality):
        def __init__(self, ref):
            self.ref = ref
        
        def __call__(self):
            store.pc.tmp.z[self.ref] = store.pc.tmp.z.max + 1


    @renpy.pure
    class Hide(Action, DictEquality):
        def __init__(self, ref):
            self.ref = ref
        
        def __call__(self):
            store.pc.tmp.apps.pop(self.ref, None)
            store.pc.tmp.z.pop(self.ref, None)


    @renpy.pure
    class Move(Action, DictEquality):
        def __init__(self, ref, pos):
            self.ref = ref
            self.pos = pos
        
        def __call__(self):
            store.pc.var.pos[self.ref] = self.pos


    @renpy.pure
    class Update(Action, DictEquality):
        def __init__(self, ref, name, value):
            self.ref = ref
            self.name = name
            self.value = value
        
        def __call__(self):
            store.pc.tmp.apps[self.ref][self.name] = self.value


    def move(drags, drop):
        rv = []
        for d in drags:
            ref, pos = d.drag_name, (d.x, d.y)
            if store.pc.var.pos.get(ref, None) != pos:
                rv.append(Move(ref, pos))
            if not store.pc.apps.apps[ref].focused:
                rv.append(Show(ref))
        return rv
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
