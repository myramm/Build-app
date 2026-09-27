label apt_lobby_dialogue:

    if M_maria.is_state(S_mar01_init):
        call mar01_init_apt_lobby
        $ player.get_item('grocery_bags')
        call popup ('give', 'grocery_bags')
        $ M_maria.trigger(T_mar01_init)

    $ game.main()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
