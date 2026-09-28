label police_lobby_first_visit:
    scene expression player.location.background_blur
    show player 11 with dissolve
    player_name "( The police station... Man, I'm sure glad I never had to come here before. )"
    hide player with dissolve
    return

label police_lobby_mia_clues_yumi:
    scene expression player.location.background_blur
    show player 35 with dissolve
    if M_mia.get('questioned earl'):
        player_name "( Hmm... No luck with his boss... )"
        player_name "( I should {b}question his partner{/b} next. )"
    else:
        player_name "( Hmm... Where to start... )"
        player_name "( I should {b}question his partner{/b} first. )"
    player_name "( They may know where he could be... )"
    hide player with dissolve
    return

label police_lobby_mia_clues_earl:
    scene expression player.location.background_blur
    show player 35 with dissolve
    player_name "( Maybe I should {b}ask his boss{/b} next. )"
    player_name "( They might know something... )"
    hide player with dissolve
    return

label police_lobby_mia_clues_skip:
    scene expression player.location.background_blur
    show player 35 with dissolve
    if M_mia.get('questioned earl'):
        player_name "( Hmm... {b}Yumi{/b}'s busy staking out {b}[deb_name]{/b}'s so she won't have heard anything... )"
        player_name "( I should {b}go back to Harold's office{/b} and think this through. )"
    else:
        player_name "( Hmm... Where to start... )"
        player_name "( I should {b}question Earl{/b}, if anyone knows where {b}Harold{/b} could be... )"
    hide player with dissolve
    return

label police_lobby_roxxy_ask_earl_release:
    scene expression player.location.background_blur
    show player 5 at left
    show old_roxxy 33 at right
    with dissolve
    roxxy "... Okay, so what now?"
    show old_roxxy 32
    show player 10
    player_name "We should {b}find an officer to talk to{/b}."
    hide player
    hide old_roxxy
    with dissolve
    return

label police_board:
    scene police_board
    with dissolve
    player_name "( This looks like the info board... )"
    pause
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
