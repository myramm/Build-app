label attic_dialogue:
    $ player.go_to(L_home_attic)

    if L_home_attic.first_visit:
        $ L_home_attic.visited()
        call expression game.dialog_select('attic_first_visit')

    $ game.main()
    return


label home_attic_evidence:
    if M_anon.is_state(S_ano13_hint, S_ano13_clue):
        call ano13_clue_home_attic_evidence
        $ player.get_item('picture2')
        call popup ('give', 'picture2')
        $ player.get_item('picture4')
        call popup ('give', 'picture4')
        $ player.get_item('safe_deposit_key')
        call popup ('give', 'safe_deposit_key')
        if M_anon.is_state(S_ano13_hint):
            $ M_anon.trigger(T_ano13_hint)
        $ M_anon.trigger(T_ano13_clue)
    else:
        call home_attic_evidence_dialogue

    $ game.main()
    return


label home_attic_globe:
    call home_attic_globe_dialogue

    $ game.main()
    return


label home_attic_painting:
    call home_attic_painting_dialogue

    $ A_rooster.unlock()
    $ game.main()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
