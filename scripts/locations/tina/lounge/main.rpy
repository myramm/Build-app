label tina_lounge_dialogue:

    if M_anon.is_state(S_ano10_tina):
        call ano10_tina_tina_lounge
        $ M_anon.trigger(T_ano10_tina)
        $ game.timer.tick()
        $ M_tina.set('becca_crush', M_roxxy.finished_state(S_roxxy_get_oil))

    elif M_tina.is_state(S_tin01_init):
        call tin01_init_tina_lounge
        $ M_tina.trigger(T_tin01_init)
        $ player.go_to(L_apt_hall3)

    elif M_tina.pregnancy:
        pass

    elif M_tina.sex == game.timer._game_day:
        $ M_tina.once('sexfriend')
        call tina_lounge_sex
        $ game.timer.tick()
        $ player.go_to(L_apt_hall3)

    $ game.main()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
