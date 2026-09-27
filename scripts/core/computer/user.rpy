init python in computer.user:
    from sys import modules

    from renpy.store import Action, Call, DictEquality, Jump

    from store import M_player, computer


    class User:
        def __init__(self, ref, name, passwd, hint):
            setattr(modules[self.__module__], ref, self)
            self.ref = ref
            self.name = name
            self.passwd = renpy.filter_text_tags(__(passwd), allow=())
            self.hint = hint
            self.apps = computer.apps.Apps(ref)
            self.mail = computer.mail.Inbox(ref)
            
            self.auth = Auth(ref)
        
        def __reduce__(self):
            return str(self.ref)
        
        def __str__(self):
            return self.ref


    @renpy.pure
    class Auth(Action, DictEquality):
        def __init__(self, ref):
            self.ref = ref
        
        def __call__(self):
            M_player.set('pc_know_{}_passwd'.format(self.ref), True)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
