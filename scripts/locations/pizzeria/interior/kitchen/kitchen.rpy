label pizzeria_kitchen_dialogue:
    if M_anon.is_state(S_ano06_cook):
        call ano06_cook_pizzeria_kitchen
        $ M_anon.trigger(T_ano06_cook)
        $ game.timer.tick()
        $ player.go_to(L_map)

    elif M_anon.is_state(S_ano11_bone):
        call ano11_bone_pizzeria_kitchen

    elif M_diane.is_state(S_dia03_stow):
        $ player.go_to(L_pizzeria_storage)
        jump pizzeria_storage_dialogue

    elif not M_maria.once('met'):
        call pizzeria_kitchen_intro

    $ game.main()
    return


label pizzeria_kitchen_eotm:
    call pizzeria_kitchen_eotm_dialogue

    $ game.main()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
