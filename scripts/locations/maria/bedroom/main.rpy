label maria_bedroom_dialogue:

    if M_maria.is_state(S_mar01_tour):
        call mar01_tour_maria_bedroom

    $ game.main()
    return


label maria_bedroom_duffel:
    if M_anon.is_state(S_ano25_find):
        call ano25_find_duffel
        call popup ('give', 'duffel')
        $ player.get_item('duffel')
        $ M_anon.trigger(T_ano25_find)
    else:
        call maria_bedroom_duffel_dialogue

    $ game.main()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
