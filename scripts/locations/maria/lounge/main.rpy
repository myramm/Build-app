label maria_lounge_dialogue:

    if M_anon.is_state(S_ano25_sick):
        call ano25_find_maria_lounge
        $ M_anon.trigger(T_ano25_sick)

    elif M_maria.is_state(S_mar01_help):
        call mar01_help_maria_lounge
        $ player.remove_item('grocery_bags')
        $ M_maria.trigger(T_mar01_help)

    $ game.main()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
