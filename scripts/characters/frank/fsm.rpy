init -1 python:
    M_frank = Machine('frank')


    def fra01_done():
        player.inventory.savings += 250000


init python:

    S_fra01_init = State()
    S_fra01_wait = State()
    S_fra01_done = State()


init python:
    S_fra01_init.add(T_ano28_cash, S_fra01_wait)
    S_fra01_wait.add(T_all_sleep, S_fra01_done,
                     actions=('exec', fra01_done))


init python:
    M_frank.add(S_fra01_init, S_fra01_wait, S_fra01_done)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
