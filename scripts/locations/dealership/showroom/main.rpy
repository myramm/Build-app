label dealership_showroom_dialogue:

    if L_dealership_showroom.first_visit:
        call dealership_showroom_intro
        $ L_dealership_showroom.visited()

    elif M_anon.is_state(S_ano07_deal):
        call ano07_deal_dealership_showroom
        $ M_anon.trigger(T_ano07_deal)

    elif M_josie.is_state(S_jos01_init):
        call jos01_init_dealership_showroom
        $ M_anon.trigger(T_jos01_init)

    elif M_josie.is_state(S_jos02_init):
        call jos02_init_dealership_showroom
        if _return:
            $ M_josie.set('sex', 'lounge' if game.timer.is_day() else 'office')
        $ M_anon.trigger(T_jos02_init)

    elif M_yoyo.is_state(S_yoy01_meet):
        call yoy01_meet_dealership_showroom
        $ M_yoyo.trigger(_return)

    $ game.main()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
