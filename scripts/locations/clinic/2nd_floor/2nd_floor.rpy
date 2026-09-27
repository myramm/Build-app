label hospital_second_floor_dialogue:
    $ player.go_to(L_hospital_floor2)


label hospital_2nd_floor_dialogue:
    scene expression game.timer.image("hospital_second{}_b")

    if M_erik.is_state(S_erik_learn_fetch, S_erik_learn_get_pills) and M_roz.is_state(S_roz_start):
        call hospital_second_floor_erik_learn_started

    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
