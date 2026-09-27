label library_lock_check:
    scene expression player.location.background_blur

    if game.timer.is_dark() and destination != L_library_front:
        show anon with dissolve
        anon @ -m_talk "( Huh... It's locked. I guess it's closed for the day. )"

        hide anon with dissolve

    elif M_bissette.is_state(S_bissette_get_dictionary) and player.has_item("french_dictionary"):
        show player 5 with dissolve
        player_name "( I need to check out this book first. )"

        player_name "( I should {b}talk to the librarian again{/b}. )"

        hide player with dissolve

    elif M_bissette.is_state(S_bissette_find_poem_reference_book) and player.location.is_here(M_mia):
        show player 14f with dissolve
        player_name "I should go say hello to {b}Mia{/b}."

        hide player with dissolve

    elif M_bissette.is_state(S_bissette_reference_book_search) and player.location.is_here(M_mia) and destination != L_library_backroom:
        show player 14 with dissolve
        player_name "I should {b}check the back room for that book Mia was talking about{/b}."

        hide player with dissolve
    else:

        return

    return True
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
