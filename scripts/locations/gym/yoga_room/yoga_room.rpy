label yoga_room_dialogue:
    $ player.go_to(L_yoga_room)

    if M_mrsj.is_state(S_mrsj_yoga_class) and player.location.is_here(M_anna):
        call expression game.dialog_select("yoga_room_mrsj_yoga_class")
        $ M_anna.trigger(T_anna_intro)
        jump yoga_room_class

    elif M_mrsj.is_state(S_mrsj_yoga_retry) and player.location.is_here(M_anna):
        call expression game.dialog_select("yoga_room_mrsj_yoga_retry")
        label yoga_room_class:
        call yoga_minigame
        if _return:
            if M_mrsj.is_state(S_mrsj_yoga_class, S_mrsj_yoga_retry):
                $ persistent.cookie_jar["Anna"]["unlocked"] = True
                $ persistent.cookie_jar["Anna"]["gallery"]["01_unlocked"] = True
                call popup ('minigame', 'yoga')
                $ A_yoga_apprentice.unlock()
            $ M_mrsj.trigger(T_mrsj_yoga_pass)
        else:
            $ M_mrsj.trigger(T_mrsj_yoga_fail)
        $ game.timer.tick()

    elif not player.location.is_here(M_mrsj) and not player.location.is_here(M_anna):
        call expression game.dialog_select("yoga_room_strangers_only")

    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
