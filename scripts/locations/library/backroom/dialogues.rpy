label backroom_blocked_dialogue:
    scene library
    show player 35 with dissolve
    player_name "Hmm... I'm not sure where the school {b}textbooks{/b} are..."

    player_name "Maybe I should ask the {b}Librarian{/b} at the {b}reception desk{/b} first."

    hide player 35 with dissolve
    $ game.main()

label backroom_dialogue_backroom_count:
    scene expression player.location.background
    show library 1_2 at Position(xpos = 486, ypos = 707) with dissolve
    player_name "( OH SHIT!!! )"

    player_name "..."
    player_name "( People are having sex back here... )"

    pause 4
    player_name "..."
    player_name "( Is that a webcam on the shelf? )"

    player_name "( I think it's filming... Do they even know that it's there? )"

    player_name "( Should I tell the {b}librarian{/b}? )"

    return

label backroom_couple_finish:
    call expression game.dialog_select("backroom_couple_finish_dialogue")
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jane"]["unlocked"] = True
    $ persistent.cookie_jar["Jane"]["gallery"]["01_unlocked"] = True
    $ M_jane.set("couple_backroom_sex", False)
    $ game.main()

label backroom_couple_finish_dialogue:
    scene expression player.location.background
    show library 1_2 at Position(xpos = 486, ypos = 707)
    pause 4
    hide library 1_2
    pause .2
    show library 3 at Position(xpos = 486, ypos = 707) with dissolve
    window hide
    pause
    show library 4
    window hide
    pause
    player_name "( Oh shit! )"

    player_name "( I hear someone coming!! )"

    show library 5 at Position(xpos = 512, ypos = 707) with hpunch
    window hide
    pause
    hide library with dissolve

    scene expression player.location.background
    show jane f_mad
    show player 23 at left
    with dissolve
    jane "Oh for crying out loud!"

    show player 11
    jane "NOT AGAIN!!!" with hpunch
    show jane f_eyeroll a_hand_out with dissolve
    jane "Ugh..."

    show jane f_mad with dissolve
    show player 10
    player_name "Is this common?"

    show player 5
    show jane f_normal_down
    jane @ -m_talk "..."
    show jane f_sad
    jane "Unfortunately..."

    jane "People seem to love doing it back here."

    jane "Just keep this to yourself, pretty please?"

    show jane f_normal
    show player 12
    player_name "Yeah, I won't tell anyone..."

    show player 5
    jane "Terima kasih."

    jane "I'm going back to my desk."

    jane "If you need help finding something or you see anyone else doing it in here, let me know!"

    hide jane with dissolve
    show player 17
    player_name "I should visit the library more often!"

    hide player with dissolve
    return

label poem_assignment_book:
    call poem_assignment_book_dialogue
    $ player.get_item('french_love')
    call popup ('give', 'french_love')
    $ M_bissette.trigger(T_bissette_reference_book_found)

    $ game.main()
    return

label poem_assignment_book_dialogue:
    scene expression player.location.background
    show book_01 at Position (xpos=376,ypos=426,xanchor=0,yanchor=0)
    player_name "This must be the book-"

    scene expression background(800, 250, 4) as stage
    show book_07_c at Transform(align=(.5, .3))
    player_name "!!!" with hpunch
    player_name "Wah!"

    player_name "{b}Mia{/b} was right. This thing is really graphic!"

    player_name "Hmm, I wonder what {b}Judith{/b} was doing with it back here in this dark room by herself?"

    player_name "..."
    player_name "Baiklah, sebaiknya saya {b}membawa ini pulang ke komputer saya dan mulai menulis puisi itu untuk Nona Bissette{/b}."

    pause
    scene expression player.location.background_blur with fade
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
