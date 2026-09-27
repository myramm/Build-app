label liu_lounge_dialogue:

    if M_anon.is_state(S_ano24_init):
        call ano24_init_liu_lounge
        $ M_anon.trigger(T_ano24_init)

    elif M_anon.is_state(S_ano28_clue):
        call ano28_clue_liu_lounge
        $ game.timer.tick()
        $ player.go_to(L_apt)
        $ M_anon.trigger(T_ano28_clue)

    elif M_liu.pregnancy and not M_liu.pregnancy.announced_pregnancy:
        if M_liu.pregnancy.first_baby:
            call liu_lounge_liu_pregnancy_first
        else:
            call liu_lounge_liu_pregnancy
        if _return:
            $ M_liu.pregnancy.set('announced_pregnancy')
        else:
            $ M_liu.pregnancy.abort_baby()
            $ M_liu.move(L_NULL, 5 - game.timer._tod)
        $ game.timer.tick()
        $ player.go_to(L_apt_hall2)

    $ game.main()
    return


label liu_lounge_card:
    call liu_lounge_card_dialogue

    $ player.get_item('card06')
    call popup ('give', 'card06')

    $ game.main()
    return


label liu_lounge_bag:
    if not M_liu.once('ano24_bag'):
        call ano24_seek_bag
    else:
        call ano24_seek_bag.repeat

    if _return:
        $ M_anon.trigger(T_ano24_seek)

    $ game.main()
    return


label liu_lounge_case:
    if not M_liu.once('ano24_case'):
        call ano24_seek_case
    else:
        call ano24_seek_case.repeat

    if _return:
        $ M_anon.trigger(T_ano24_seek)

    $ game.main()
    return


label liu_lounge_folder:
    if not M_liu.once('ano24_folder'):
        call ano24_seek_folder
    else:
        call ano24_seek_folder.repeat

    if _return:
        $ M_anon.trigger(T_ano24_seek)

    $ game.main()
    return


label liu_lounge_wallet:
    call ano24_seek_wallet
    $ M_kim.set('wallet', _return)

    if _return:
        call popup ('earn', 50)
        $ player.get_money(50)

    $ game.main()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
