label hospital_lobby_dialogue:
    $ player.go_to(L_hospital_lobby)

    if not M_consuela.between_states(S_con02_job3, S_con02_ptsd):
        call hospital_lobby_dialogue.babies

    if M_consuela.is_state(S_con02_job3):
        call con02_job3_hospital_lobby

    elif M_consuela.is_state(S_con02_ptsd):
        $ game.timer.tick()
        call con02_ptsd_hospital_lobby
        $ M_consuela.trigger(T_con02_ptsd)

    $ game.main()
    return

label hospital_lobby_dialogue.babies:
    $ renpy.dynamic('m', 'n', 'r', 'w')
    $ w = ward.items()
    label hospital_lobby_dialogue.continue:
    while w:
        $ r, n = w.pop()
        if not n:
            jump hospital_lobby_dialogue.continue
        $ m = machines[n]
        if m.pregnancy.stage == 5 and not m.pregnancy.seen_in_labor:
            call expression 'hospital_recovery_{}_first'.format(m)
            $ m.pregnancy.set('seen_in_labor')
            $ player.go_to(locations[r])
    if player.location is not L_hospital_lobby:
        $ game.main()
    return

label hospital_desk_caught:
    call hospital_desk_caught_dialogue
    $ player.go_to(L_hospital_lobby)
    jump roz_dialogue_options
    return


label hospital_lobby_photo:
    call hospital_lobby_photo_dialogue

    call screen roz_locker
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
