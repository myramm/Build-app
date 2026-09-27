label bissette_book_search_2_books_left:
    show player 12 with dissolve
    player_name "Well, two more books to go."

    hide player with dissolve
    return

label bissette_book_search_1_book_left:
    show player 14 with dissolve
    player_name "Just one book left."

    hide player with dissolve
    return

label bissette_book_search_no_books_left:
    show player 14 with dissolve
    player_name "Great! That's the last book!"

    player_name "Now, I just need to {b}return them to the library{/b}!"

    hide player with dissolve
    return

label annie_locker_first_visit:
    player_name "Yup. I expected as much."

    player_name "{b}Annie{/b} is such a suck up to {b}Mrs. Smith{/b}."

    return

label dexter_locker_first_visit:
    player_name "I'd better not let {b}Dexter{/b} see me in here."

    player_name "Typical jock stuff."

    player_name "What a weird basketball air pump."

    return

label dexter_locker_book_search:
    player_name "He was lying! I knew it!"

    return

label dexter_locker_book_found:
    scene dexter_locker
    show book_05_c with dissolve
    player_name "{b}Quick mafs{/b}?"

    player_name "This is a book for little kids..."

    player_name "Hah, I guess it matches his mafs-"

    player_name "Math level!"

    player_name "I need to get out of here!"

    player_name "Something about being next to {b}Dexter{/b} or his stuff is making me dumber!"

    hide book_05_c with dissolve
    show expression game.timer.image("location_school_right_hall_day{}_blur")
    return

label erik_locker_first_visit:
    player_name "{b}Erik{/b} has a lot of {i}Dungeon 'N Orcettes{/i} stuff."

    player_name "There's his lunch bag too."

    player_name "His landlady always packs him some of her homemade fudge."

    player_name "Lucky guy. His landlady sure must like him."

    return

label eve_locker_first_visit:
    player_name "Yikes! I'd better not let anyone else see her locker."

    player_name "Those headphones sure do look comfy though."

    return

label eve_locker_drawing_pick_up:
    $ player.get_item("eve_drawing")
    call expression game.dialog_select("eve_locker_drawing_picked_up")
    $ player.location.call_screen(False)

label eve_locker_drawing_picked_up:
    scene eve_locker
    show closeup_drawing_01
    with dissolve
    player_name "Huh, this IS really good!"

    player_name "... {b}Chad{/b} was right. It's pretty sexy!"

    player_name "I wonder if she actually thinks about wearing something like that?"

    hide closeup_drawing_01
    with dissolve
    call popup ('give', 'eve_drawing')
    return

label judith_locker_first_visit:
    player_name "Mmm... {i}Mountain Jizz{/i}?"

    player_name "That stuff can sure make a mess."

    player_name "Must be all the sugar that makes it so sticky."

    pause
    player_name "She must like cows."

    player_name "I do too-"

    player_name "Hey! How did she get that picture of me?"

    return

label take_judith_glasses:
    scene judith_locker
    player_name "That must be her spare set."

    player_name "Now, I just need to {b}get these back to Miss Okita{/b}."

    $ player.get_item("judith_glasses")
    call popup ('give', 'judith_glasses')
    $ game.main()

label take_broken_flute:
    scene judith_locker
    player_name "( That should be the {b}flute{/b} that {b}Judith{/b} borrowed from Miss Dewitt. )"

    scene lefthall_c with fade
    $ player.get_item("broken_flute")
    call expression game.dialog_select("take_broken_flute_dialogue")
    $ M_dewitt.trigger(T_dewitt_get_flute)
    $ game.main()

label take_broken_flute_dialogue:
    show player 563f at left with dissolve
    player_name "Wow, this thing really got flattened..."

    player_name "It's all bent up!"

    show player 564f with dissolve
    pause
    show player 565f with dissolve
    player_name "Hmm, it smells funny too."

    show player 564f with dissolve
    show old_erik 5 at right with dissolve
    erik "Uhh, what are you doing there, dude?"

    show old_erik 52
    show player 22f at Position (xoffset=139) with hpunch
    player_name "!!!"
    show player 29 with dissolve
    player_name "N-nothing! You really scared me!"

    show player 14 with dissolve
    player_name "Apa yang sedang kamu lakukan?"

    show player 13
    show old_erik 5
    erik "Just heading to my next class..."

    show old_erik 53
    erik "Was that a flute?"

    show player 563
    show old_erik 3c
    with dissolve
    player_name "Y-yeah. Well, it used to be anyways."

    show player 562
    show old_erik 53
    erik "It has definitely seen better days..."

    show old_erik 3c
    show player 563
    player_name "I was gonna play it for {b}Miss Dewitt{/b}'s talent show."

    show player 13 with dissolve
    show old_erik 5
    erik "Hmm, well, maybe you could build your own?"

    show old_erik 52
    show player 10
    player_name "Menurutmu?"

    show player 5
    show old_erik 54
    erik "Tentu saja!"

    show old_erik 4
    erik "I had to build a flute in a video game once."

    erik "All you need is a good piece of wood and a drill to make all the holes."

    show old_erik 1
    show player 12
    player_name "You built one in a video game?"

    show player 5
    show old_erik 4
    erik "Totally! I used it to charm all the orc girls in the village!"

    erik "Then we had a giant orgy in the Chief's hut!"

    show old_erik 1
    show player 10
    player_name "Oh, that's... Nice."

    show player 5
    show old_erik 4
    erik "Heh, dude, it was anything but nice. I can assure you!"

    show player 13
    show old_erik 54
    erik "Green chicks are crazy in the sack!"

    show old_erik 1
    show player 14
    player_name "I should probably get busy if I'm going to build a flute from scratch."

    show player 13
    show old_erik 4
    erik "Oh, right. I hear you."

    show old_erik 1
    show player 14
    player_name "Thanks, {b}Erik{/b}."

    show player 13
    show old_erik 4
    erik "My pleasure, dude!"

    hide player
    hide old_erik
    with dissolve
    return

label kevin_locker_first_visit:
    player_name "Hah?"

    player_name "That looks like my missing jock strap!"

    pause
    player_name "I didn't know we bought the same one."

    return

label mia_locker_first_visit:
    player_name "{b}Mia{/b}'s locker smells nice."

    return

label mia_locker_first_visit_early_route:
    player_name "She has such great life."

    return

label mia_locker_first_visit_helping_parents:
    player_name "I should help her parents get back together."

    return

label mia_locker_first_visit_helen_route:
    player_name "I wonder if I should have helped her parents get back together..."

    return

label ronda_locker_first_visit:
    player_name "Is there any sport she isn't good at?"

    player_name "I bet she doesn't even have to pay for college."

    player_name "She probably has a full-ride scholarship."

    return

label roxxy_locker_first_visit:
    player_name "Wow."

    player_name "{b}Roxxy{/b}'s locker is nice."

    player_name "Looks like she's popped the seal on a new jar of {b}Cherry Pops{/b}."

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
