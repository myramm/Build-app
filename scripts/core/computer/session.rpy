init python in computer:
    from renpy.store import computer


    class Session:
        def __init__(self, system):
            self.stack = []
            self.system = system
            self.push(system)
        
        def pop(self):
            self.stack.pop()
        
        def push(self, user):
            self.stack.append((user, Volatile()))
        
        @property
        def apps(self):
            return self.user.apps
        
        @property
        def mail(self):
            return self.user.mail
        
        @property
        def tmp(self):
            return self.stack[-1][1]
        
        @property
        def user(self):
            return getattr(computer.user, self.stack[-1][0])
        
        @property
        def var(self):
            return getattr(computer.data, self.stack[-1][0])


    class Volatile:
        def __init__(self):
            self.apps = dict()
            self.z = maxdict()


    class maxdict(dict):
        def __setstate__(self, state):
            self.update(state)
        
        @property
        def max(self):
            return max(self.values() or (0,))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
