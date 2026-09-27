label hospital_2nd_floor_room_dialogue:
    if M_diane.is_state(S_diane_jizz_checkup) and L_hospital_room.is_here(M_diane):
        call expression game.dialog_select("hospital_second_floor_room_jizz_checkup")
        $ M_diane.trigger(T_diane_bathroom_sampling)

    elif M_erik.is_state(S_erik_bully_blackout):
        call expression game.dialog_select("clinic_erik_bully_fight_concussion")
        $ M_erik.trigger(T_erik_bully_recover)
        $ L_hospital.unlock()

    $ game.main()

label hospital_2nd_floor_bathroom_dialogue:
    if M_diane.is_state(S_diane_jizz_checkup_extra_hand) and L_hospital_room.is_here(M_diane):
        jump micoe_bj_scene
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
