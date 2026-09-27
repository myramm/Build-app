default computer.data.jenny.mail = {'read': {'419', 'beg', 'ptv', 'toy'}}


init python in computer.mail:
    from datetime import datetime

    from renpy import store
    from renpy.store import Action, Call, DictEquality


    class Inbox:
        def __init__(self, user):
            self.user = user
            self.mail = {}
        
        def __iter__(self):
            return iter(sorted(self.mail.values(), key=lambda m: m.arr, reverse=True))
        
        def add(self, ref, sndr, sub, arr, **kwargs):
            self.mail[ref] = Message(self.user, ref, sndr, sub, arr, **kwargs)


    class Message:
        def __init__(self, user, ref, sndr, sub, arr, att=False, hook=None):
            self.user = user
            self.ref = ref
            self.sndr = sndr
            self.sub = sub
            self.arr = datetime.utcfromtimestamp(arr)
            self.att = att
            
            self.read = Read(ref)
            
            if hook:
                label = 'pc_hook_' + hook
                if renpy.has_label(label):
                    hook = Call(label)
            
            self.hook = hook
            
            self.sender = __(sndr).split('<')[0].strip()
            self.short = __(sub)
            if len(self.short) > 35:
                self.short = self.short[:35].rpartition(' ')[0] + '...'
        
        @property
        def date(self): 
            timer = store.game.timer
            
            epoch = store.pc.var.mail.setdefault('epoch', timer.game_day())
            today = 1527854400 + (timer.game_day() - epoch) * 24 * 60 * 60
            age = datetime.utcfromtimestamp(today) - self.arr
            
            if age.days < 1:
                return __('{time.hour}:{time:%M}').format(time=self.arr)
            elif age.days < 2:
                return __('Yesterday')
            else:
                return __('{date.day} {date:%b}').format(date=self.arr)
        
        @property 
        def state(self):
            read = self.ref in store.pc.var.mail.setdefault('read', set())
            return 'read' if read else 'unread'


    @renpy.pure
    class Read(Action, DictEquality):
        def __init__(self, ref):
            self.ref = ref
        
        def __call__(self):
            store.pc.var.mail.setdefault('read', set()).add(self.ref)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
