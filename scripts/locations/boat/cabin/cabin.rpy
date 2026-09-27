label boat_cabin_dialogue:

    $ game.main()
    return


label yacht_cabin_nuke:
    call yacht_cabin_nuke_dialogue

    if _return:
        $ A_world_war_3.unlock()
        $ player.go_to(L_map)

    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
