label church_graveyard_dialogue:
    $ player.go_to(L_church_graveyard)
    if not game.timer.is_dark():
        if getPlayingSound("<loop 2>audio/ambience_graveyard.ogg"):
            $ playSound("<loop 2>audio/ambience_graveyard.ogg")

    if M_odette.is_state(S_ode02_init) and game.timer.is_night() and game.timer.is_fullmoon() and L_church_crypt.is_here(M_odette):
        call ode02_init_church_graveyard
        $ M_odette.trigger(T_ode02_init)

    elif M_odette.is_state(S_ode02_wake):
        call ode02_wake_church_graveyard
        $ player.go_to(L_map)
        $ M_odette.trigger(T_ode02_wake)

    elif M_player.is_set('just wokeup'):
        call church_graveyard_wake
        call player_just_wokeup.skip

    $ game.main()
    return


label church_graveyard_crypt:
    $ renpy.dynamic(active=game.timer.is_night() and game.timer.is_fullmoon() and L_church_crypt.is_here(M_odette))

    if active and M_odette.is_state(S_ode02_find):
        call ode02_find_crypt
        $ M_odette.trigger(T_ode02_find)

    elif active and M_odette.is_state(S_ode02_fear):
        call ode02_fear_crypt

    elif M_odette.is_state(S_ode02_warn):
        call ode02_warn_crypt

    elif not M_odette.finished_state(S_ode02_warn):
        call church_graveyard_crypt_dialogue

    elif active:
        call church_graveyard_crypt_dialogue.fullmoon
    else:

        call screen church_graveyard_crypt()

    if _return == 'enter':
        $ player.go_to(L_church_crypt)
        $ M_odette.trigger(T_ode02_fear)

    $ game.main()
    return


label church_graveyard_grave:
    if M_anon.is_state(S_ano22_sign):
        if game.timer.is_day():
            call ano22_sign_headstone
            $ player.go_to(L_map)
            $ game.timer.tick(1)
            $ M_anon.trigger(T_ano22_sign)
        else:
            call ano22_sign_headstone.wait

    elif M_anon.finished_state(S_ano22_sign):
        if game.timer.is_day():
            call church_graveyard_grave_dialogue
        else:
            call church_graveyard_grave_dialogue.dark
    else:

        call church_graveyard_grave_dialogue.wait

    $ game.main()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
