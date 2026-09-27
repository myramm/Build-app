init -1 python:
    M_anna = Machine('anna', default_loc=[[L_NULL] * 4],
                     vars={'sex speed': .3,
                           'awesomo lured': False,
                           'yoga_fail_retry' : False})

init -3 python:
    T_anna_intro = Trigger()
    T_anna_find_awesomo = Trigger()
    T_anna_found_dog = Trigger()

init python:
    S_anna_start = State()
    S_anna_dog_hunt = State(_("Anna needs my help in the park!"))
    S_anna_find_dog = State(_("Oh no! Awesomo is missing in the forest!"))
    S_anna_end = State()

init python:

    S_anna_start.add(T_anna_intro, S_anna_dog_hunt,
                     actions=('setdefaultloc', [[L_NULL, L_NULL, L_yoga_room, L_NULL]],
                              'priority', 1,
                              'location', {'place': L_park},
                              'force', {'tod': [0,1]}))


    S_anna_dog_hunt.add(T_anna_find_awesomo, S_anna_find_dog,
                        actions=('unlocklocation', L_forest))
    S_anna_find_dog.add(T_anna_found_dog, S_anna_end,
                        actions=('priority', 0,
                                 'unforce', None))

init python:
    M_anna.add(S_anna_start,
               S_anna_dog_hunt, S_anna_find_dog,
               S_anna_end)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
