label pier_dialogue:
    $ player.go_to(L_pier)
    $ playSound(audio.a_pier, 1.0)

    if M_iwanka.is_state(S_iwa01_pier):
        call iwa01_pier_pier
        $ L_boat_bridge.unlock()
        $ game.timer.tick()
        $ player.go_to(L_map)
        $ M_iwanka.trigger(T_iwa01_pier)

    elif L_pier.first_visit:
        call pier_intro
        $ L_pier.visited()

    $ game.main()
    return


label pier_board:
    if pier_board_first:
        call pier_board_dialogue
        $ pier_board_first = False
    else:
        call pier_board_dialogue.repeat

    $ game.main()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
