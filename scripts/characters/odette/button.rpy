label odette_button_dialogue:
    call odette_button_stage

    if M_odette.is_state(S_ode02_tomb):
        call ode02_tomb_odette
        $ M_odette.trigger(T_ode02_tomb)

    elif L_church_crypt.is_here(M_odette):
        call odette_button_crypt
    else:

        jump odette_button_dialogue_legacy

    if _return == 'sleep':
        call popup ('groggy')
        $ game.sleep()
        $ player.go_to(L_church_graveyard)
        jump church_graveyard_dialogue

    $ game.main()
    return


label odette_button_stage:
    if L_church_crypt.is_here(M_odette):
        scene location_crypt_side
        show odette

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
