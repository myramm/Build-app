label library_eve_clients_library_fliers:
    scene expression player.location.background_blur with None
    show anon:
        flip
        xoffset 100
    show eve a_flyers f_happy_right:
        xoffset -200
    with dissolve
    eve "Alright, I'll put one on each of these tables while you're hanging some, okay?"

    anon "Ya baiklah."

    jane "{i}*Ahem*{/i} Can I help you two?"

    show eve f_normal
    show jane:
        flip
    with dissolve
    eve "Oh, umm... Hi."

    eve "We're trying to advertise for my sister's tattoo parlor."

    eve "Is it okay if we hang a few of these flyers around here?"

    show jane f_normal_down a_flyer2 with dissolve
    jane "{b}Sugar Tats{/b}?"

    jane f_normal "I've heard of that place."

    jane @ f_sexy "Is your sister {b}Grace Rogers{/b}?"

    eve f_happy "Yeah, that's her."

    jane f_normal_down "Hah, I went to school with her back in the day."

    pause
    jane f_normal "Sure, you can hang up a few."

    jane "Tell your sister I said hello, okay?"

    eve "Y-ya, aku akan melakukannya."

    eve "Terima kasih!"

    hide jane with dissolve
    pause
    eve f_happy_right "She was nice."

    anon "Ya."

    eve @ f_confused "Do you know her?"

    anon f_worried @ f_worried_left a_behind_head "Ehh, kinda..."

    anon "She's friends with my roommate."

    eve "Benar-benar?"

    eve "I wonder if your roommate went to school with my sister too?"

    anon f_normal "Heh, probably."

    pause
    eve "Alright, let's get to work!"

    eve "After this, we'll hit the park."

    anon "Mengerti."

    hide anon
    hide eve
    with dissolve
    return

label library_diane_production_ask_librarian:
    scene expression "backgrounds/location_library_day_blur.jpg"
    show player 13 with dissolve
    player_name "( I should ask the librarian about those milking books {b}Veronica{/b} mentioned. )"

    hide player with dissolve
    return

label library_jane_intro:
    call expression game.dialog_select("library_jane_intro_pre")
    menu:
        "Tentu." if player.has_money(20):
            call expression game.dialog_select("library_jane_intro_sure")
            $ player.spend_money(20)
            $ M_player.set("library subscription", True)
            $ M_jane.trigger(T_jane_library_pass)
        "saya akan lulus.":

            call expression game.dialog_select("library_jane_intro_not_yet")
            $ player.go_to(L_map)
            $ game.main()

    hide player
    hide jane
    with dissolve
    return

label library_jane_intro_pre:
    scene library
    show player 1 at left
    show jane
    with dissolve
    jane "Hai!"

    show player 14
    player_name "Oh, hi!"

    player_name "I'm looking for some school {b}textbooks{/b}."

    show player 1
    jane "Do you have a membership subscription?"

    show player 10
    player_name "Umm... I don't think I have one."

    show player 13
    show jane f_laugh
    jane "Oh. That's okay!"

    show jane f_normal
    jane "Would you like to get one?"

    show jane f_laugh
    show player 11
    jane "Membership subscriptions are {b}$20{/b}, and you get access to all of our selections!"

    show jane f_normal
    show player 2
    player_name "Uhh... I guess I have no choice. Haha."

    show jane f_laugh
    show player 13
    jane "Knowledge is priceless, right?"

    show jane f_normal
    jane "Would you like to subscribe right now?"

    return

label library_jane_intro_sure:
    show player 4
    player_name "Hmm..."

    show player 174b at Position(xoffset=38) with fastdissolve
    player_name "All right. Here's twenty dollars."

    show player 1 with fastdissolve
    show jane f_laugh
    jane "Terima kasih!"

    show jane f_normal
    jane "If you're looking for a specific book, just come to the front desk."

    jane "I'll look them up and find 'em for ya!"

    show player 2
    player_name "That sounds great! Thanks!"

    return

label library_jane_intro_not_yet:
    show player 4
    player_name "Hmm..."

    show player 35
    player_name "Actually, I think I'll pass..."

    show jane f_normal
    show player 1
    jane "Oh... Alright then."

    show player 2
    player_name "I might come by another time!"

    show player 1
    jane "Okay, have a good day!"

    return

label library_bissette_find_poem_reference_book:
    scene library
    show player 14f with dissolve
    player_name "Now, to find something on French romance."

    show player 12f
    player_name "This isn't going to be easy-"

    show player 32f at Position(xoffset=-69) with dissolve
    player_name "Is that {b}Mia{/b}?"

    show player 14f with dissolve
    player_name "I wonder what she's doing here?"

    player_name "I should go and say hi!"

    hide player with dissolve
    return

label library_ross_find_magazines:
    scene library
    show player 2
    with dissolve
    player_name "Hmm, I should {b}ask the Librarian{/b} where she keeps the magazines."

    return

label check_out_lock:
    scene library
    show player 5 with dissolve
    player_name "( I need to check out this book first. )"

    player_name "( I should {b}talk to the librarian again{/b}. )"

    hide player with dissolve
    $ game.main()

label poem_assignment_lock:
    if M_bissette.is_state(S_bissette_find_poem_reference_book) and player.location.is_here(M_mia):
        call expression game.dialog_select("poem_assignment_lock_bissette_find_poem_reference_book")
    else:
        call expression game.dialog_select("poem_assignment_lock_bissette_reference_book_search")
    $ game.main()

label poem_assignment_lock_bissette_find_poem_reference_book:
    scene library
    show player 14f with dissolve
    player_name "I should go say hello to {b}Mia{/b}."

    hide player with dissolve
    return

label poem_assignment_lock_bissette_reference_book_search:
    scene library
    show player 14 with dissolve
    player_name "I should {b}check the back room for that book Mia was talking about{/b}."

    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
