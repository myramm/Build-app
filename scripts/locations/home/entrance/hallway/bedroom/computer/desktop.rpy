label pc_hook_remote_fail:
    anon "( Weird. It doesn't seem to do anything. )"

    anon "( I wonder if it's trying to connect to another {b}computer{/b}? )"

    return

label pc_hook_saga:
    $ A_inception.unlock()
    return

label pc_hook_saga_ex:
    if not M_player.once('pc_saga_ex'):
        anon "( Man... This game {b}always{/b} has bugs. )"

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
