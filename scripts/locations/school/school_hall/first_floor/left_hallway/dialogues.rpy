label left_hall_eve_roxxy_bullying:
    scene expression player.location.background_blur
    show anon f_skeptical with dissolve
    anon "(Hmm?)"

    anon "( There's a lot of laughter coming out of the {b}locker rooms{/b}... )"

    anon "( I wonder what's going on? )"

    hide anon with dissolve
    return

label left_hallway_judith_changing:
    scene lefthall_c
    show judith f_sad_down
    show anon with {'master': dissolve}
    anon "Hey, {b}Judith{/b}..."

    anon f_worried @ -m_talk "..."
    anon "Is everything all right?"

    judith f_sad "Oh, hey, {b}[firstname]{/b}..."

    judith "I'm just not feeling too well; I might just go home."

    anon "You're not coming to the Athletics class?"

    judith f_sad_down "Ya..."

    judith "... I just..."

    judith f_sad "... I can't go in the boys' locker room."

    anon f_surprised "... The boys' locker room?"

    anon "Why would you need to go in the boys' locker room?"

    judith f_surprised "You mean nobody told you?"

    anon f_worried "... Tidak?"

    judith f_normal "A pipe burst in the girls' locker room and it's closed for repairs..."

    judith f_sad @ f_sad_down "We're sharing the boys' locker room now."

    anon f_surprised "Sungguh?!"

    judith "I don't really feel comfortable about it, like the other girls."

    show judith f_sad_down
    anon f_normal a_idle @ f_thinking a_thinking "Ya..."

    anon "The class is starting soon, so there's probably not that many people left in there anyway?"

    judith f_normal "Yeah, I guess you're right..."

    anon "I can go in with you, to make sure you're okay..."

    anon f_normal a_idle @ f_brag_closed a_wave "... And I won't look!"

    judith "Okay... I'll follow you, then."

    hide anon
    hide judith
    with {'master': dissolve}
    return

label left_hallway_latinos_bashing:
    scene lefthall_c
    show old_judith 10 at left
    show martinez:
        xoffset -150
    show lopez
    with dissolve
    lopez "Just look at those nasty-ass saggy tits!"

    show old_judith 7 at left
    judith "..."
    show old_judith 8 at left
    martinez "She's probably too poor to afford a bra..."

    show old_judith 7 at left
    judith "It's not like that!!"

    show old_judith 10 at left
    lopez "You think you're gonna get the boys' attention showing your tits around like that?"

    show old_judith 7 at left
    judith "My breasts are sensitive!! It hurts when I wear a bra..."

    judith "I'm just more comfortable like this!!"

    show old_judith 10 at left
    lopez @ f_laugh "Haha!"

    show old_judith 9 at left
    show martinez f_angry
    martinez "Yo, you better not hang around here no more..."

    show martinez a_sign with dissolve
    martinez "PUTA! Did you just hear? This is our turf, so get out!"

    show martinez a_idle with dissolve
    show player 12 at Position( xpos = 290, ypos = 768)
    hide old_judith 9
    show old_judith 9 at left
    with dissolve
    player_name "Apa yang terjadi disini?!"

    show player 114
    judith "{i}*Sobbing*{/i}"

    show player 90 at Position( xpos = 290, ypos = 768)
    show old_judith 9 at left
    show lopez f_angry
    martinez "You defending this ugly bitch now?"

    lopez "Keep walking white boy!"

    show player 113
    player_name "Are you okay {b}Judith{/b}?"

    hide old_judith
    show player 90 at left
    with dissolve
    martinez "What's the matter, white boy, you not gonna run after your bitch?"

    show player 12 at left
    player_name "You didn't have to do this..."

    show martinez a_sign with dissolve
    martinez "We'll do whatever the fuck we want!"

    show martinez a_idle with dissolve
    show lopez f_laugh
    lopez "Haha! See ya!"

    hide player
    hide lopez
    hide martinez
    with dissolve
    return

label left_hallway_judith_missing:
    scene expression game.timer.image("lefthall{}")
    show player 11 with dissolve
    player_name "..."
    show player 10
    player_name "... Where's {b}Judith{/b}?"

    player_name "( She usually hangs out in this hallway. )"

    show player 34
    player_name "Hmm..."

    show player 35
    player_name "( I can {b}hear{/b} something... )"

    show player 10
    player_name "( Is that someone... Sobbing? )"

    show player 12
    player_name "( It's like a crying voice coming from the girls' locker room... )"

    hide player 12 with dissolve
    return

label left_hallway_martinez_book_search:
    scene lefthall_c
    show martinez a_backpack:
        xoffset -150
    show lopez f_angry
    show player 10 at left
    with dissolve
    player_name "Hey, {b}Martinez{/b}?"

    show player 5
    martinez "... What do you want, culo?"

    lopez "Yeah! What do you want?"

    show player 10
    player_name "Uhh, I heard you had a book that's overdue from the library."

    show player 5
    show martinez f_angry
    martinez "What, are you stalking me or something, white boy?"

    show player 10
    player_name "Huh? No, the librarian sent me!"

    show player 5
    lopez "So, you're just the librarian's little bitch?"

    show martinez f_laugh
    martinez "Haha!"

    show martinez f_normal
    show player 12
    player_name "What? No, she ordered a book for me and asked if I could talk to you guys in return."

    show player 5
    show martinez f_angry
    martinez "Whatever, bitch! We ain't got time for this..."

    show martinez f_normal
    martinez "C'mon, {b}Lopez{/b}. We gotta get ready for gym class."

    lopez "Sure thing, {b}Martinez{/b}. Later, culo!"

    show lopez f_laugh
    lopez "Ha ha ha!"

    hide lopez
    show martinez b_back
    with dissolve
    show player 428
    pause
    show martinez with dissolve:
        xoffset 500
    show player 11
    player_name "!!!"
    hide martinez with dissolve
    show player 12
    player_name "I bet that's it in her backpack!"

    show player 30
    player_name "I should try and {b}grab it while they are showering{/b}. They probably wouldn't even realize it's gone."

    show player 33
    player_name "I just have to be sneaky..."

    hide player with dissolve
    return

label left_hallway_school_sneak_mission:
    scene cult_event 5
    with dissolve
    window hide
    pause
    scene cult_event 6
    with Dissolve(0.3)
    pause
    scene expression game.timer.image("lefthall{}")
    show player 11 at left with dissolve
    show old_erik 51 at right with dissolve
    player_name "..."
    show player 12
    player_name "They went into the utility closet?"

    show player 90
    show old_erik 53
    erik "Why would they go in there?"

    show old_erik 52
    show player 35
    player_name "It doesn't make sense."

    player_name "They couldn't all fit in there!"

    show player 34
    show old_erik 53
    erik "You think maybe there's a secret tunnel or something?"

    show old_erik 52
    show player 10
    player_name "Hmm, I dunno. Maybe?"

    show player 5
    show old_erik 53
    erik "This is really creeping me out."

    erik "Can we leave now?"

    show old_erik 52
    show player 12
    player_name "Hold on. We still have a mission to complete."

    show player 5
    show old_erik 50
    erik "..."
    show player 12
    player_name "C'mon, let's {b}head up to Mrs. Smith's office on the third floor{/b}."

    hide player
    hide old_erik
    with dissolve
    return

label left_hallway_roxxy_lockerroom_event:
    scene expression game.timer.image("lefthall{}")
    show player 34 with dissolve
    player_name "Hmm?"

    player_name "( There are voices coming from the girls' locker room! )"

    player_name "( It's supposed to be off-limits... )"

    show player 4 at Position (xoffset=6) with dissolve
    player_name "( ... I wonder what's going on? )"

    hide player with dissolve
    return

label left_hallway_roxxy_shower_event:
    scene expression game.timer.image("lefthall{}")
    show old_erik 62 at right
    show anon f_worried b_jersey
    with dissolve
    anon "{b}Erik{/b}?"

    show old_erik 61
    anon "Where are all your clothes?"

    show old_erik 63
    erik "Hai, {b}[firstname]{/b}..."

    erik "I was just in the boys' locker room changing, when {b}Roxxy{/b} and her friends came in..."

    show old_erik 62
    erik "... They kicked me out."

    show old_erik 61
    anon "So your clothes are still in there?"

    show old_erik 62
    erik "... Ya."

    show old_erik 61
    anon f_skeptical "C'mon man, I'll go with you."

    anon "We'll grab your clothes and then I need to hit the shower."

    show old_erik 62
    erik "O-oke..."

    hide anon
    hide old_erik
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
