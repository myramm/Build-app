label principals_office_delivery_invoice:
    scene office_clear
    show ronda chair at Position (xoffset=-320,yoffset=-55)
    show principal 22_23f at Position(xpos = 600, ypos = 764)
    player_name "!!!" with hpunch
    player_name "Apa yang-"

    show principal 25f
    smith "Apa maksudnya ini?!"

    show principal 24f
    annie "I'm so sorry, ma'am!"

    scene expression game.timer.image("office{}")
    show old_annie 3f at Position (xpos=375)
    show player 168b at left
    show titty 1f at right
    show principal 26 at Position (xpos=614)
    with dissolve
    annie "I didn't realize-"

    show old_annie 9f
    show principal 27
    smith "You know better than to interrupt me when I'm disciplining miscreants!"

    show principal 26
    ronda "I didn't do anything wrong!"

    show principal 2
    smith "SILENCE!"

    show principal 1
    annie "..."
    show principal 28 at Position (xoffset=-54) with dissolve
    smith "What is that {b}[firstname]{/b}'s carrying?"

    show principal 26 with dissolve
    show old_annie 1f
    show player 168c
    player_name "{i}*Gulp*{/i} It's uhh, milk... Ma'am."

    player_name "For the cafeteria."

    show player 168b
    show old_annie 9f
    show principal 27
    smith "Oh right, the delivery that I ordered."

    smith "What's it doing in my office?!"

    show principal 26
    show player 168c
    player_name "{b}Annie{/b} said-"

    show player 168b
    show principal 27
    smith "I don't care what {b}Annie{/b} said!"

    show old_annie 6f
    smith "Take that downstairs to the cafeteria, immediately!"

    show principal 26
    show player 168c
    player_name "{i}*Sigh*{/i} Down the stairs?"

    show player 168b
    show principal 27
    smith "... Problem?"

    show principal 26
    show player 168c
    player_name "I... Sorry, it's just really heavy and I've already carried it all the way up here..."

    show player 168b
    show principal 27
    smith "Ugh..."

    show principal 28 at Position (xoffset=-54) with dissolve
    smith "Just {b}untie Ronda{/b}, and she'll help you carry it down."

    show principal 26 with dissolve
    ronda "What?! Why do I have to-"

    show principal 27
    smith "It's good enough punishment for her and I'm sick of listening to her mouth!"

    show principal 26
    show player 168c
    player_name "O-oke."

    hide titty
    hide principal
    hide player
    hide old_annie
    with dissolve
    return

label principals_office_no_entry:
    scene expression game.timer.image("office{}")
    show principal 5 at right with dissolve
    show player 1 at left with dissolve
    smith "Apa yang kamu lakukan disini?!"

    show player 11 at left
    show principal 3 at right
    player_name "Oh... Umm..."

    show player 21 at left
    player_name "I was... Looking for the washroom!"

    show player 22 at left
    show principal 4 at right
    smith "Don't play dumb with me, {b}[firstname]{/b}!"

    smith "Didn't I just tell you earlier to get to class?!"

    show player 10 at left
    show principal 1 at right
    player_name "Ya..."

    show player 22 at left
    show principal 2 at right
    smith "Now, get out of my OFFICE!!!"

    hide player 22 at left with dissolve
    hide principal 2 at right with dissolve
    return

label principals_office_no_entry_night:
    scene expression L_school_floor3.background_blur
    show player 10 with dissolve
    player_name "I can't go in there right now..."

    hide player with dissolve
    return

label principals_office_annie_trouble:
    scene expression game.timer.image("office{}")
    show principal 6 at right
    show player 11 at left
    with dissolve
    annie "{b}Mrs. Smith{/b}?"

    show principal 7 at right
    smith "Apa itu?"

    show principal 6 at right
    annie "Reporting repeated offenders as you ordered!"

    show principal 9 at right
    smith "{b}[firstname]{/b}?"

    show principal 8 at right
    annie "Yes, ma'am. He was being inappropriate in the locker room!"

    show principal 9 at right
    smith "Don't you have enough problems?"

    smith "What with your failing grades and all..."

    show player 10 at left
    show principal 13
    player_name "Uh, yes ma'am!"

    show player 11 at left
    show principal 9
    smith "... And yet, you feel the need to cause problems in the locker room as well?"

    show principal 7 at right
    smith "What happened, exactly, {b}Annie{/b}?"

    show principal 6 at right
    annie "Well, his... He... He's showing inappropriate body parts to the girls in the locker room, ma'am."

    show principal 9 at right
    smith "Apakah begitu?"

    show player 10 at left
    player_name "Well... I can explain-"

    show player 22 at left
    show principal 10 at right with hpunch
    smith "SILENCE!!!"

    show principal 9 at right
    show player 5 at left
    smith "... I need to see exactly what happened. Show me what you did, now."

    show principal 6 at right
    annie "Ma'am, it won't work..."

    annie "It only seems to happen when... He sees women in the {i}nude{/i}, ma'am."

    show principal 7 at right
    smith "Well, what are you waiting for, {b}Annie{/b}?"

    smith "You're going to have to help him with that."

    show principal 11 at right
    show player 11 at left
    annie "Apa?!"

    show principal 12 at right
    smith "You're the one who witnessed it and reported the infraction..."

    smith "... It's your {i}duty{/i} to carry out the report!"

    player_name "We really don't have to do this-"

    show principal 10 at right
    show player 22 at left
    smith "No one's leaving until I get a full report! Do it, or you both are in DETENTION!!!"

    show principal 13 at right
    annie "..."
    show player 8 at left
    show principal 14 at right
    window hide
    pause
    show player 63 at left
    show principal 15 at right
    window hide
    pause
    show principal 16 at right
    show player 64 at left
    smith "Now, look at those {i}firm breasts{/i} of hers..."

    show principal 17 at right
    smith "Don't you want to... Suck on them? {b}[firstname]{/b}?"

    show player 65 at left
    player_name "..."
    show player 66 at left
    window hide
    pause
    show player 66 at left with hpunch
    window hide
    pause
    show player 67 at left
    smith "There we are..."

    show principal 18 at right
    smith "That's enough, {b}Annie{/b}. You can leave now..."

    show principal 5 at right with dissolve
    smith "So...!"

    smith "This is what I've been hearing about this whole time."

    hide player 67 at left
    show principal 19 at left
    with dissolve
    smith "You've made quite a reputation around school..."

    smith "I can see why..."

    smith "... This has been a..."

    show principal 20 at left
    window hide
    pause
    show principal 21 at left with hpunch
    window hide
    pause
    smith "... Distraction!"

    show player 69 at left
    show principal 1 at right
    with dissolve
    player_name "I'm sorry, ma'am!"

    player_name "It won't happen again, I promise!"

    show principal 5 at right
    show player 68 at left
    smith "Alright, young man: here's the deal..."

    smith "I won't send you to detention, as long as you keep this... \"problem\" of yours... To yourself."

    smith "My priority is order and discipline in this school, and I plan on keeping it that way!"

    show principal 1 at right
    show player 69 at left
    player_name "Yes, {b}Mrs. Smith{/b}!"

    show principal 2 at right
    show player 68 at left
    smith "Now, get out of my OFFICE!!"

    hide player 68 at left with dissolve
    hide principal 2 at right with dissolve
    $ renpy.end_replay()
    return

label principals_office_dewitt_paint_trail:
    if M_dewitt.is_state(S_dewitt_paint_trail):
        scene smith_office_spying
        show old_annie spying 1
        show principal spying 2
        with dissolve
        smith "You should have seen their faces!"

        smith "Complete and utter devastation!"

        smith "Ha ha ha!"

        show principal spying 1
        show old_annie spying 2
        annie "So, did they believe it was {b}Tyrone{/b} and his gang like you planned?"

        show old_annie spying 1
        show principal spying 2
        smith "Nah, {b}Dewitt{/b} knows I had something to do with it, but she can't prove anything."

        show principal spying 1
        show old_annie spying 3
        annie "I'm sorry, ma'am. I tried my best to make it look like a bunch of hooligans did it."

        show old_annie spying 1
        show principal spying 2
        smith "Yes, yes, I'm sure you did."

        smith "I just can't get that image out of my mind!"

        smith "Poor little {b}Dewitt{/b} on the verge of tears."

        smith "Her silly talent show in shambles!"

        show principal spying 3
        smith "Hmm..."

        show principal spying 2
        smith "It's actually getting me kinda worked up."

        smith "Why don't you come over here and help me out."

        show principal spying 1
        show old_annie spying 3
        annie "Tentu saja, Bu."

        show old_annie spying 4
        show principal spying 4
        with dissolve
        pause
        show old_annie spying 5 with dissolve
        pause
        show principal spying 3
        smith "Ahh, that's it."

        smith "Good girl..."

        smith "Hehehehe, I can't wait to see the look on her face when I tell her the board has pulled her funding!"

        scene black with fade

        scene outside_smith_office
        show old_kevin 24 at Position (xpos=800)
        show player 107 at Position (xpos=400)
        with dissolve
        kevin "Bro, {b}Mrs. Smith{/b} WAS behind it!"

        show old_kevin 23
        player_name "..."
        show old_kevin 24
        kevin "What a mega bitch!"

        kevin "We have to say something!"

        show old_kevin 23
        player_name "..."
        show old_kevin 24
        kevin "{b}[firstname]{/b}?"

        kevin "{b}[firstname]{/b}?!"

        show old_kevin 23
        pause 1
        show old_kevin 25 at Position (xoffset=-82) with hpunch
        kevin "Bro!"

        show old_kevin 23
        show player 12 with dissolve
        player_name "Hey! Chill out, man!"

        show player 5
        show old_kevin 24
        kevin "I'm trying to talk to you!"

        show old_kevin 23
        show player 12
        player_name "Well, I'm sorry but did you see what they are doing in there right now?!"

        show player 5
        show old_kevin 24
        kevin "Uh, yeah and it's super gross!"

        kevin "{b}Mrs. Smith{/b} is the devil man, I bet her coochie smells like brimstone and sulfur!"

        show old_kevin 23
        show player 113
        player_name "{b}Annie{/b} doesn't seem to mind..."

        show player 114
        show old_kevin 24
        kevin "C'mon, it's getting late and you're supposed to {b}meet Eve in the park{/b}, remember?!"

        show old_kevin 23
        show player 113
        player_name "Uh huh, just five more minutes..."

        show player 114
        show old_kevin 24
        kevin "Let's go, before we get caught, ya perv!"

        hide old_kevin
        hide player
        with dissolve
    else:

        scene smith_office_spying
        show old_annie spying 5
        show principal spying 3
        with dissolve
        smith "You're getting pretty good at this, my little pet."

        smith "Mmm, right there!"

        smith "Ahhh!"

        scene black with fade
    return

label principals_office_dewitt_smith_office_trap:
    scene expression game.timer.image("office{}")
    show old_erik 51 at right
    show player 12 at left
    with dissolve
    player_name "You watch the door while I apply the adhesive, alright?"

    show player 5
    show old_erik 53
    erik "Ya baiklah."

    erik "Just hurry up, dude. I want to get out of here..."

    show old_erik 52
    show player 12
    player_name "Saya akan."

    hide player
    hide old_erik
    with dissolve

    scene smith_office_cs01
    show text _ ("I made sure the chairs were glued to the floor before moving onto the cushions.\nThere was no way I would let {b}Mrs. Smith{/b} and {b}Annie{/b} ruin the talent show.") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("Not after all the hard work we had put into it!\nI didn't stop until every last drop of the adhesive had been used.") as caption with dissolve
    pause

    scene smith_office_night_b
    show old_erik 52 at right
    show player 14 at left
    with fade
    player_name "Alright, that should do it."

    show player 17
    player_name "I disconnected her phone from the outlet too so there's no way they can call for help!"

    show player 13
    show old_erik 54
    erik "Nice thinking!"

    show old_erik 53
    erik "Now let's get out of here, {b}[firstname]{/b}!"

    show old_erik 52
    show player 14
    player_name "Yeah, I'm right behind you!"

    hide player
    hide old_erik
    with dissolve

    scene expression L_school_front.background_blur with fade
    show player 13 at left
    show old_erik 53 at right
    with dissolve
    erik "Fiuh."

    erik "Let's never do that again, okay?"

    show old_erik 52
    show player 14
    player_name "Hehe, ya."

    player_name "At least we accomplished what we came here to do."

    show player 13
    show old_erik 54
    erik "Mission successful!"

    show old_erik 1
    show player 14
    player_name "Thanks for your help, {b}Erik{/b}."

    show player 13
    show old_erik 4
    erik "Don't mention it, {b}[firstname]{/b}."

    show old_erik 1
    show player 14
    player_name "I'll see you later!"

    show player 13
    show old_erik 7 with dissolve
    erik "Sampai jumpa!"

    hide player
    hide old_erik
    with dissolve
    return

label principals_office_dewitt_trap_check_up:
    scene office_clear
    show old_annie 19
    with dissolve
    annie "... It's a great plan, ma'am!"

    annie "It'll put a stop to that stupid talent show once and for all."

    show old_annie 20
    smith "Yes, so long as you don't screw it up again..."

    show old_annie 19
    annie "But I didn't..."

    annie "... Ya, Bu."

    show old_annie 20
    smith "Just go make the preparations!"

    show old_annie 19
    annie "Right away, ma'am!"

    show old_annie 20b with dissolve
    annie "..."
    annie "I'm stuck!"

    show old_annie 20c with dissolve
    smith "Apa?"

    show old_annie 20b with dissolve
    annie "I can't get out of my chair!"

    show old_annie 20c with dissolve
    smith "Stop fooling around, {b}Annie{/b}. We don't have time to waste!"

    show old_annie 20b with dissolve
    annie "I'm seriously stuck to the chair!"

    show old_annie 20c with dissolve
    smith "Oh for heaven's sake!"

    show old_annie 21
    smith "( !!! )" with hpunch
    smith "WHAT THE HELL?!"

    smith "I'm stuck too!!!"

    smith "How is this possible?!"

    annie "..."
    smith "{b}Annie{/b} get your butt over here and help me!"

    annie "I can't, I'm stuck too!"

    scene black with fade

    scene outside_smith_office
    show player 107 at Position (xpos=400)
    with dissolve
    pause
    show player 17f at Position (xoffset=100) with dissolve
    player_name "( It worked! )"

    show player 14f at Position (xoffset=100)
    player_name "( There's no way they can interfere with the talent show now! )"

    player_name "( They'll be stuck there arguing until somebody finds them. )"

    player_name "( I'd better {b}get to the auditorium{/b} quickly or I'll miss the introductions. )"

    hide player with dissolve
    return

label principals_office_dewitt_office_night_visit_delay:
    scene expression game.timer.image("office{}")
    show old_annie 22f at left
    show principal 36 at right
    with dissolve
    annie "Can you get this cushion off me?"

    show old_annie 23f
    show principal 37
    smith "Not now, idiot!"

    smith "What I want is a full report on who did this!"

    smith "Whoever ruined my chair... And... And my suit!"

    smith "My beautiful suit!"

    show principal 40 with dissolve
    smith "Just look at what they did!"

    smith "FIND THEM!"

    scene black with fade

    scene outside_smith_office
    show player 107 at Position (xpos=400)
    with dissolve
    pause
    show player 17f at Position (xoffset=100) with dissolve
    player_name "( I'd better get out of here before they see me! )"

    hide player with dissolve
    return

label desk03_locked_dialogue:
    scene expression game.timer.image("office{}")
    if player.location.is_here(M_smith):
        show player 30 at left
        player_name "Hmmm... I wonder what's in there?"

        show player 22 at left with hpunch
        show principal 4 at right with dissolve
        smith "Apa yang sedang kamu lakukan?"

        show principal 1 at right
        show player 29 at left
        player_name "Oh, I'm sorry... I was just looking!"

        show player 3 at left
        show principal 5 at right
        smith "If I EVER catch you going through my things..."

        show principal 2 at right
        smith "... You can be sure, you'll be spending the rest of the year in DETENTION!!!"

    else:
        $ pass
    $ game.main()

label principle_drawer:
    scene expression game.timer.image('location_school_office_drawer{}')
    show expression game.timer.image('objects/object_papers_01.png') at Position(xpos = 378, ypos = 526)
    player_name "..."
    player_name "What's with all those... Leather things... In here?"

    player_name "Weird..."

    call screen principle_drawer

label principle_drawer_diane_delivery_3_fetch_invoice:
    scene expression game.timer.image("office{}")
    show player 167f at right
    show titty 1 at left
    show principal 28f at Position (xpos = 470)
    with dissolve
    smith "Ah, wonderful."

    smith "Are those the new {b}milk cartons{/b}?"

    show player 168f
    show principal 26f at Position (xpos = 415)
    player_name "Umm... Yeah."

    show principal 27f
    show player 163f
    smith "I sampled the last batch..."

    smith "It was quite... Delightful. You're lucky I'm in a good mood."

    smith "Please, tell the milk provider I'm doubling our next order."

    smith "We keep running out. The students absolutely love it!"

    show principal 26f
    show player 164f
    player_name "Will do! Where can I put these cartons?"

    show principal 27f
    show player 163f
    smith "You can give them to {b}Annie{/b}, she'll take care of them."

    show principal 4f at Position (xpos = 470)
    show player 167f
    smith "Now, get out of my office, I have some unfinished business to attend to."

    show principal 26f at Position (xpos = 415)
    show player 168f
    player_name "Yes, {b}Mrs. Smith{/b}!"

    hide principal
    hide titty
    hide player
    with dissolve
    $ M_diane.trigger(T_diane_delivery_3_got_invoice)
    $ game.main()

label principals_office_okita_get_keycode_morning:
    scene expression game.timer.image("office{}")
    show player 22 at left
    show principal 26 at right
    player_name "( Oh crap! She's here! )"

    smith "..."
    show principal 27
    smith "... Can I help you with something?"

    show player 10
    show principal 26
    player_name "Oh! I was just-"

    show player 29
    player_name "... Err, I was... Just wondering..."

    show principal 2
    show player 3
    smith "Spit it out, {b}[firstname]{/b}!"

    show principal 26
    pause
    show player 10
    player_name "Uhh, how are you doing, {b}Mrs. Smith{/b}?"

    show player 11
    smith "..."
    show principal 27
    smith "Sibuk."

    show principal 2
    smith "Sekarang keluar!"

    show player 10
    show principal 26
    player_name "Y-ya, Bu!"



    return

label principals_office_okita_get_keycode_afternoon:
    scene expression game.timer.image("office{}")
    show player 1
    with dissolve
    player_name "( She's not here! This is my chance to {b}find that key code{/b}! )"

    player_name "( I should {b}look around{/b}. )"

    return

label masterkey_taken:
    show expression "backgrounds/location_school_office_desk.jpg"
    $ player.get_item("master_key")
    call popup ('give', 'master_key')
    $ game.main()

label keycode_note_taken:
    scene expression game.timer.image("office{}")
    show player 544
    with dissolve
    pause
    show player 543
    player_name "Aha! This has gotta be it! {b}6219{/b}."

    show expression "backgrounds/location_school_office_desk.jpg"
    $ player.get_item("keycode_note")
    call popup ('give', 'keycode_note')
    player_name "Now, I just have to {b}go unlock Miss Okita's office to grab all those things she wanted{/b}."

    $ M_okita.trigger(T_okita_keycode_acquired)
    $ game.main()
    return

label tissue_taken:
    $ player.go_to(L_school_smithoffice)
    scene location_school_office_day_blur
    show player 528
    with dissolve
    pause
    show player 529
    player_name "Ugh, oh man..."


    player_name "Gross!"

    show player 528
    pause
    show player 529
    player_name "I think this will work..."

    player_name "I'd better get outta here before {b}Annie{/b} comes back."

    hide player with dissolve
    $ player.get_item("tissue")
    call popup ('give', 'tissue')
    $ game.main()

label desk_open:
    python:
        for image in renpy.get_showing_tags():
            renpy.hide(image)
    call screen desk_drawer

label principals_office_okita_get_ingredients_morning:
    scene expression game.timer.image("office{}")
    show player 22 at left
    with dissolve
    player_name "( Oh crap! She's here! )"

    show principal 3b at Position(xpos=0.85, ypos=1.0) with dissolve
    smith "..."
    show principal 27 at right with dissolve
    smith "... Can I help you with something?"

    show player 29 with dissolve
    show principal 26
    player_name "Oh! I was just-"

    player_name "... Err, I was... Just wondering..."

    show player 3
    show principal 27 with dissolve
    smith "Spit it out, {b}[firstname]{/b}!"

    show player 29
    show principal 26
    player_name "Uhh, how are you doing, {b}Mrs. Smith{/b}?"

    show player 3
    smith "..."
    show principal 27
    smith "Sibuk."

    show player 22
    show principal 2
    with dissolve
    smith "Now get out!" with hpunch
    show principal 1
    show player 10
    player_name "Y-ya, Bu!"


    return

label principal_trash:
    if M_okita.is_state(S_okita_get_ingredients) and not player.has_picked_up_item("tissue"):
        call screen principle_garbage
    else:
        scene location_school_office_day_blur
        show player 10
        player_name "I don't want to look through {b}Mrs. Smith{/b}'s garbage."

    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
