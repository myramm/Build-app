label hospital_storage_room_dialogue:
    if M_consuela.is_state(S_con02_scam):
        call con02_scam_hospital_storage
        $ M_roz.set('fun time', False)
        $ player.go_to(L_hospital_floor2)
        $ M_consuela.trigger(T_con02_scam)
        $ persistent.cookie_jar['Roz']['unlocked'] = True
        $ persistent.cookie_jar['Roz']['gallery']['03_unlocked'] = True

    elif M_roz.is_state(S_roz_obits_collect):
        call roz02_hospital_sex
        $ M_roz.set('fun time', False)
        $ game.timer.tick()
        $ player.go_to(L_hospital_floor2)
        $ player.get_item('obituary_records')
        $ M_roz.trigger(T_roz_obits_acquired)
        $ persistent.cookie_jar['Roz']['unlocked'] = True
        $ persistent.cookie_jar['Roz']['gallery']['01_unlocked'] = True

    elif M_roz.is_set('fun time'):
        call hospital_storage_funtime
        $ M_roz.set('fun time', False)
        $ game.timer.tick()
        if not player.has_item('hospital_access_card'):
            $ player.go_to(L_hospital_floor2)

    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
