label jiang_button_dialogue:
    call jiang_button_stage

    if M_anon.is_state(S_ano07_mech):
        call ano07_mech_jiang
        $ M_anon.trigger(T_ano07_mech)
        $ L_apt.unlock()

    elif M_anon.is_state(S_ano07_find):
        call ano07_find_jiang

    elif M_anon.is_state(S_ano07_give):
        call ano07_give_jiang
        $ player.remove_item('toolbag')
        $ M_anon.trigger(T_ano07_give)

    elif M_josie.is_state(S_jos01_find) and L_dealership_garage.is_here(M_rump) and not M_josie.jos01_kim:
        call jos01_find_jiang

    elif M_yoyo.where in L_dealership.get_all_children_inclusive() and not M_jiang.once('yoyo'):
        call jiang_event_yoyo

    elif L_dealership_garage.is_here(M_jiang):
        call jiang_button_garage
    else:

        jiang "Oh tidak! Apakah para pengembang juga lupa menghubungkan dialog ini?!"


    $ game.main()
    return

label jiang_button_stage:
    if L_dealership_garage.is_here(M_jiang):
        scene expression background(284, 472, 4.6) as stage
        show jiang:
            flip
            xoffset 500
    else:
        scene expression player.location.background_blur as stage
        show jiang
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
