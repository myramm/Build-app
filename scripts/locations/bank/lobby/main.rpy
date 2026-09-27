label bank_lobby_dialogue:

    if L_bank_lobby.first_visit:
        call bank_lobby_intro
        $ L_bank_lobby.visited()

    $ game.main()
    return


label bank_lobby_atm:
    if player.has_item('atm_card'):
        call screen atm()
    else:
        call bank_lobby_atm_dialogue

    $ game.main()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
