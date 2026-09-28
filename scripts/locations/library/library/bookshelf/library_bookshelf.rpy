label kamasutra:
    $ player.get_item("kamasutra")
    call expression game.dialog_select("kamasutra_dialogue")
    $ player.go_to(L_library)
    $ M_erik.trigger(T_erik_learn_kamasutra)
    $ game.main()

label kamasutra_dialogue:
    scene libraryshelf with None
    show book_02_c at truecenter with dissolve
    player_name "Woa..."
    player_name "This book has all sorts of sex... Positions?"
    player_name "It must be what she asked for..."
    hide book_02_c with dissolve
    return

label french_dictionary:
    $ player.get_item("french_dictionary")
    call expression game.dialog_select("french_dictionary_dialogue")
    $ player.go_to(L_library)
    $ game.main()

label french_dictionary_dialogue:
    scene libraryshelf with None
    player_name "Aha! {i}French to English dictionary{/i}!"
    player_name "Great! Now I can-"
    show book_03_c at truecenter with dissolve
    player_name "Wait a second..."
    player_name "Some of the pages are missing!"
    player_name "Now what do I do?"
    pause
    player_name "Hopefully nothing important is gone."
    hide book_03_c with dissolve
    return

label library_old_book:
    $ player.get_item("old_book")
    call expression game.dialog_select("library_old_book_dialogue")
    $ player.go_to(L_library)
    $ game.main()

label library_old_book_dialogue:
    scene libraryshelf with None
    show closeup_book_09 at truecenter with dissolve
    player_name "This book looks like it would be useful decoding something."
    player_name "..."
    if not player.has_item("weird_coin"):
        player_name "Heh. Maybe some {b}hidden pirate treasure{/b} someone tossed aside carelessly."
        player_name "But that's just wishful thinking."
    else:

        player_name "I think {b}that pirate coin had a four-digit number on it{/b}."
        player_name "I should {b}look at it again{/b}."
    call popup ('give', 'old_book')
    hide closeup_book_09 with dissolve
    return

label breeding_guide:
    call expression game.dialog_select("breeding_guide_dialogue")
    $ player.get_item("breeding_guide")
    $ M_diane.trigger(T_diane_got_production_book)
    hide book_01_c with dissolve
    $ player.go_to(L_library)
    $ game.main()

label breeding_guide_dialogue:
    scene libraryshelf
    player_name "( Hmm, {i}Breeder's Guide{/i}? )"
    player_name "( This might have what I'm looking for... )"
    show book_01_c at truecenter with dissolve
    player_name "( Here we go, \"Increasing milk yield.\" )"
    pause
    player_name "!!!" with hpunch
    player_name "( Holy crap! )"
    player_name "( {b}Veronica{/b} was right! )"

    scene expression "backgrounds/location_library_day_blur.jpg"
    show player 369b
    with dissolve
    player_name "( It seems like, if {b}Diane{/b} gets pregnant, it will increase her milk production significantly. )"
    pause
    player_name "{i}*Gulp*{/i}"
    player_name "( I know we've been having a bit of fun together but would {b}Diane{/b} really want to... )"
    player_name "( ... With me?! )"
    player_name "( ... )"
    player_name "( This is going to be a really awkward conversation. )"
    player_name "( ... But I promised I'd help her in any way I could! )"
    player_name "( I have to {b}show her this book{/b}! )"
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
