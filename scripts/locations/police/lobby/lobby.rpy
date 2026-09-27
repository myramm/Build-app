label police_lobby_dialogue:
    $ player.go_to(L_police_lobby)
    if L_police_lobby.first_visit:
        call expression game.dialog_select("police_lobby_first_visit")
        $ L_police_lobby.visited()

    if M_mia.is_state(S_mia_clues):
        if L_home.is_here(M_yumi):
            call police_lobby_mia_clues_skip
            $ M_mia.set('questioned yumi', 'skip')
        elif not M_mia.get("questioned yumi"):
            call police_lobby_mia_clues_yumi
        elif not M_mia.get("questioned earl"):
            call police_lobby_mia_clues_earl

    if M_roxxy.is_state(S_roxxy_ask_earl_release):
        call expression game.dialog_select("police_lobby_roxxy_ask_earl_release")

    $ game.main()
    return


label police_lobby_pika:
    call police_lobby_pika_dialogue

    $ game.main()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
