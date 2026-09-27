label eriks_room_dialogue:

    if not player.location.is_here(M_erik):
        if M_erik.is_state(S_erik_vr_ready) and game.timer.is_weekend():
            call expression game.dialog_select("eriksroom_erik_vr_ready")
        $ game.main()

    if player.location.is_here(M_june):
        call eriksroom_mrsj_cupid_caught
        $ player.go_to(L_erikhouse_entrance)
        $ M_erik.set('in_flagrante', True)

    elif M_erik.is_state(S_erik_bully_promise):
        call expression game.dialog_select("eriksroom_erik_bully_coax")
        $ M_erik.trigger(T_erik_bully_coax)

    elif M_erik.is_state(S_erik_feed_curious) and game.timer.is_dark():
        call expression game.dialog_select("eriksroom_erik_feed_missing")
        $ M_erik.trigger(T_erik_feed_missing)

    elif M_erik.is_state(S_erik_learn_ready) and L_erikhouse_mrsjroom.is_here(M_mrsj):
        call expression game.dialog_select("eriksroom_erik_learn_intro")
        $ M_erik.trigger(T_erik_learn_request)
        $ player.go_to(L_erikhouse_entrance)

    elif M_mrsj.is_state(S_mrsj_fork_ready):
        call expression game.dialog_select("eriksroom_mrsj_fork_intro")
        $ M_erik.trigger(T_mrsj_fork_crush)

    elif (M_june.finished_state(S_june_date_ready) and
          L_erikhouse_mrsjroom.is_here(M_mrsj) and
          M_erik.get('confessed') < 0):
        call eriksroom_june_date_confession
        $ M_erik.set('confessed', game.timer._game_day)
        $ player.go_to(L_erikhouse)

    if not M_erik.is_state(S_erik_cards_lost) and not player.location.is_here(M_june):
        $ playSound("<loop 3>audio/ambience_erikroom.ogg")

    $ game.main()

label sock_pile_book_search:
    scene expression game.timer.image("eriks_room{}_c")
    show player 517 with dissolve
    player_name "Hmm, what's with these socks?"

    player_name "They're stiff as a board!"

    show player 516
    player_name "..."
    show player 517
    player_name "Gross..."

    player_name "I'm not even going to bother digging for the book in there..."

    hide player with dissolve
    $ game.main()

label dresser_book_search:
    scene expression game.timer.image("backgrounds/location_erik_house_bedroom_dresser_day{}.jpg")
    player_name "!!!"
    player_name "Are those stained?"

    pause
    player_name "His dresser is such a mess like his room!"

    $ game.main()

label under_bed_book_search:
    scene expression game.timer.image("under_eriks_bed{}")
    show book_03 at Position (xpos=431,ypos=425,xanchor=0,yanchor=0)
    player_name "Just a bunch of dust bunnies..."

    player_name "... Wait a minute! There's a book under here!"

    call screen under_eriks_bed

    player_name "Sweet, this is it!"

    hide book_03
    show book_04_c with dissolve
    player_name "{i}Oedipuss{/i}?"

    player_name "{i}Doin' it the Ancient Way{/i}..."

    player_name "Why in the world would {b}Erik{/b} want this?"

    hide book_04_c with dissolve

    scene expression game.timer.image("eriks_room{}_c")
    if M_bissette.get_state() == S_bissette_jane_return_books:
        show player 12 with dissolve
        player_name "Well, two more books to go."


    elif M_bissette.get_state() in [S_bissette_got_dexters_book, S_bissette_got_eriks_book, S_bissette_got_martinez_book]:
        show player 14 with dissolve
        player_name "Just one book left."

    else:

        show player 14 with dissolve
        player_name "Great! That's the last book!"

        player_name "Now, I just need to {b}return them to the library{/b}!"

    hide player with dissolve
    $ M_bissette.trigger(T_bissette_ask_erik)
    $ player.get_item("oedipuss")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
