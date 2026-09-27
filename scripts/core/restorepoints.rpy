
init python hide:
    from random import getrandbits
    from threading import Thread


    def setrestorepoint():
        if not hasattr(store, 'restorepoint'):
            name = '_restorepoint_{:08x}'.format(getrandbits(32))
            store.restorepoint = name
        
        t = Thread(target=renpy.save, args=(restorepoint,),
                   kwargs={'extra_info': restorepoint})
        t.daemon = True
        t.start()


    store.setrestorepoint = setrestorepoint
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
