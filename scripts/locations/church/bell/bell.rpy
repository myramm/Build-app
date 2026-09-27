label church_cloister_bell_dialogue:

    $ game.main()
    return


label church_tower_bell:
    scene expression game.timer.image('location_church_bell_closeup{}')

    if M_aqua.is_state(S_aqua_bell_search):
        call church_bell_aqua_bell_search
        $ M_aqua.trigger(T_aqua_bell_engraving)
    else:

        call church_tower_bell_dialogue

    $ game.main()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
