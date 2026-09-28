label button_crystal_preamble:
    show player 5 at left
    show old_crystal 3 at right
    with dissolve
    crystal "It's my little girl's boyfriend again."
    show old_crystal 1 with dissolve
    show player 10
    player_name "I told you we're not-"
    show player 5
    show old_crystal 2
    crystal "Whatever you say, young man."
    show old_crystal 4 with dissolve
    crystal "{i}*Gulp*{/i}"
    show old_crystal 2 with dissolve
    crystal "So, what do you want?"
    return

label button_crystal_roxxys_dad:
    show player 10
    player_name "Where's {b}Roxxy{/b}'s... Father?"
    show player 11
    show old_crystal 2
    crystal "Hah! She don't have no father!"
    crystal "I raised her myself."
    show old_crystal 1
    show player 10
    player_name "I see."
    show player 11
    show old_crystal 2
    crystal "To tell you the truth, I don't remember which one it was..."
    show old_crystal 4 with dissolve
    crystal "{i}*Gulp*{/i}"
    show old_crystal 2 with dissolve
    crystal "... So her daddy could be anyone, for all I know."
    show old_crystal 1
    show player 22
    player_name "!!!"
    show old_crystal 2
    crystal "Anything else you'd like to talk about?"
    show player 5
    show old_crystal 1
    return

label button_crystal_roxxy:
    show player 10
    player_name "Do you know where I could find {b}Roxxy{/b}?"
    show player 5
    show old_crystal 3 with dissolve
    crystal "Hah! You think I babysit my daughter?"
    show old_crystal 1 with dissolve
    show player 10
    player_name "Hmm..."
    show player 5
    show old_crystal 2
    crystal "She's always out doing stuff..."
    crystal "... But, usually she's at {b}school{/b} or at {b}the beach{/b}."
    show old_crystal 1
    show player 14
    player_name "Oh. I see. Thanks!"
    show player 13
    show old_crystal 2
    crystal "Anything else?"
    show old_crystal 1
    return

label button_crystal_nothing:
    show player 10
    player_name "Oh, nothing."
    player_name "I was just passing by..."
    show player 11
    show old_crystal 2
    crystal "Well, I got a visitor coming soon, so why don't you move along."
    show old_crystal 1
    show player 10
    player_name "I'm sorry. I'll get going then."
    player_name "Bye!"
    hide player
    hide old_crystal
    with dissolve
    return

label button_crystal_roxxy_go_to_picnic:
    scene expression "backgrounds/location_trailer_night_closeup.jpg"
    show player 5 at left
    show player_wet at left
    show old_crystal 3 at right
    with dissolve
    crystal "Mmm, you know I can help you out of them wet clothes if you want?"
    show old_crystal 1 with dissolve
    show player 10
    player_name "Uhh... I..."
    show player 5
    player_name "..."
    show old_crystal 2
    crystal "Don't be shy now."
    crystal "Handsome man, like yourself. You deserve some special attention, don't ya?"
    show old_crystal 1
    show player 3 with dissolve
    player_name "..."
    roxxy "{b}Mom{/b}, leave {b}[firstname]{/b} alone!"
    show old_crystal 2
    crystal "Hehehe, I'm just teasin' the boy a bit."
    show old_crystal 1
    roxxy "Well, stop!"
    show old_crystal 4 with dissolve
    roxxy "{b}[firstname]{/b}, get in here!"
    show old_crystal 1
    player_name "..."
    hide old_crystal
    hide player
    hide player_wet
    with dissolve
    return

label button_crystal_rox8_11_evening:
    scene expression "backgrounds/location_trailer_closeup01_evening.jpg"
    show player 5 at left
    show old_crystal 6 at right
    with dissolve
    crystal "You lost, handsome?"
    show old_crystal 5
    show player 10
    player_name "Huh?"
    show player 5
    show old_crystal 6
    crystal "Oh, yer {b}Roxxy{/b}'s new man."
    show old_crystal 5
    show player 12
    player_name "N-no, I'm-"
    show player 5
    show old_crystal 6
    crystal "She's inside."
    show old_crystal 5
    return

label button_crystal_rox8_11_day:
    scene trailer_interior_c
    show player 5 at left
    show old_crystal 2 at right
    with dissolve
    crystal "You lost, handsome?"
    show old_crystal 1
    show player 10
    player_name "Huh?"
    show player 5
    show old_crystal 2
    crystal "Oh, yer {b}Roxxy{/b}'s new man."
    show old_crystal 1
    show player 10
    player_name "N-no, I'm-"
    show player 5
    show old_crystal 2
    crystal "She ain't here."
    show old_crystal 4 with dissolve
    return

label button_crystal_final_evening:
    scene expression "backgrounds/location_trailer_closeup01_evening.jpg"
    show player 13 at left
    show old_crystal 6 at right
    with dissolve
    crystal "Mmm, now there's a nice capable man!"
    show old_crystal 5
    show player 14
    player_name "Heh, hi {b}Crystal{/b}..."
    show player 13
    show old_crystal 6
    crystal "Why don't you grab a beer and come sit with me, Romeo?"
    crystal "You can show off that silver tongue some more..."
    show old_crystal 5
    show player 14
    player_name "Oh, I dunno... {b}Roxxy{/b} wouldn't-"
    show player 5
    show old_crystal 6
    crystal "Yer here to call on {b}Roxxy{/b} then?"
    show old_crystal 5
    return

label button_crystal_final_day:
    scene trailer_interior_c
    show player 13 at left
    show old_crystal 2 at right
    with dissolve
    crystal "Mmm, now there's a nice capable man!"
    show old_crystal 1
    show player 14
    player_name "Heh, hi {b}Crystal{/b}..."
    show player 13
    show old_crystal 2
    crystal "Why don't you grab a beer and come sit with me, Romeo?"
    crystal "You can show off that silver tongue some more..."
    show old_crystal 1
    show player 14
    player_name "Oh, I dunno... {b}Roxxy{/b} wouldn't-"
    show player 5
    show old_crystal 2
    crystal "{b}Roxxy{/b} ain't here."
    show old_crystal 1
    return

label button_crystal_sorry_to_bother:
    show player 10
    player_name "Sorry to bother you."
    show player 5
    show old_crystal 6
    crystal "Psh, talkin' don't bother me none..."
    crystal "... In fact, why don't you run on down to the store and buy me a fresh twelve pack?"
    crystal "You do that and we can talk 'til yer ears fall off."
    show old_crystal 5
    show player 17
    player_name "Heh, nah that's okay."
    player_name "I should get inside and see {b}Roxxy{/b}."
    show player 13
    show old_crystal 6
    crystal "Suit yerself."
    hide player
    hide old_crystal
    with dissolve
    return

label button_crystal_roxxy_rox8_rox11:
    show old_crystal 1 with dissolve
    show player 10
    player_name "Do you know where she is?"
    show player 5
    show old_crystal 2
    crystal "Psh, ain't got a clue..."
    crystal "... I can't never keep track of that gal."
    show old_crystal 1
    show player 10
    player_name "Really?"
    show player 5
    show old_crystal 2
    crystal "Ungrateful brat don't tell me nothin'."
    crystal "She needs a whoopin'! What she needs..."
    show old_crystal 1
    player_name "..."
    return

label button_crystal_roxxy_final:
    show old_crystal 4 with dissolve
    show player 12
    player_name "Where's she at?"
    show player 5
    show old_crystal 2 with dissolve
    crystal "Heck if I know."
    crystal "If she ain't at school, then I reckon she's probably at the beach."
    crystal "I swear, that girl is half mermaid!"
    show old_crystal 1
    show player 17
    player_name "Heh, yeah maybe..."
    show player 13
    return

label button_crystal_roxxys_mom:
    show old_crystal 1 with dissolve
    show player 10
    player_name "So you're {b}Roxxy's mom{/b}?"
    show player 5
    show old_crystal 2
    crystal "That's right."
    crystal "Can't you see the resemblance?"
    show old_crystal 1
    menu:
        "Yeah, I suppose.":
            show player 12
            player_name "Now that you mention it, you two do look a lot alike."
            show player 5
            show old_crystal 2
            crystal "Yeah, she really lucked out, takin' after me."
            crystal "Her father was ugly as sin!"
            show old_crystal 1
            player_name "..."
            show old_crystal 2b
            crystal "Hahaha!"
            show old_crystal 1
            jump roxmom_dialogue_repeat
        "You look so young though!":
            show player 12
            player_name "I see the resemblance but you look way too young to be {b}Roxxy{/b}'s mom."
            show player 10
            player_name "Are you sure you're not her sister?"
            show player 5
            show old_crystal 2
            crystal "Well now, if you ain't got a silver tongue on you!"
            crystal "I reckon that's how you dun got my daughter's attention, huh?"
            show old_crystal 1
            show player 10
            player_name "Well, I-"
            show player 5
            show old_crystal 2
            crystal "Hate to break it to ya there, Romeo... But it's gonna take more than fancy talk to keep hold of her."
            crystal "I brought her up right, you see?"
            crystal "Showed her that the worth of a man is in his actions and not his words!"
            show old_crystal 1
            player_name "..."
            show old_crystal 2
            crystal "Iffin' you can't take proper care of my girl then you best be movin' on, kiddo."
            show old_crystal 1
            jump roxmom_dialogue_repeat
    return

label button_crystal_roxxy_busy:
    show player 29 with dissolve
    player_name "Is {b}Roxxy{/b} busy?"
    show player 3
    show old_crystal 6
    crystal "Psh, I doubt it..."
    crystal "... She's probably just in there yappin' on that damn phone of hers."
    show old_crystal 5
    show player 12 with dissolve
    player_name "So I can just go in and see her?"
    show player 5
    show old_crystal 11
    crystal "... You expectin' me to stop ya or something?"
    show old_crystal 10
    show player 10
    player_name "I don't-"
    show player 11
    show old_crystal 6
    crystal "Good grief, Romeo."
    crystal "Grow a pair and get in there already!"
    hide old_crystal
    hide player
    with dissolve
    return

label button_crystal_happy_home:
    show player 10
    player_name "Are you happy to be home?"
    show player 5
    show old_crystal 2
    crystal "Darn tootin' I am!"
    crystal "This place might be a shithole but it beats the hell outta that jail cell, I'll tell ya that for free!"
    crystal "I reckon, I got you to thank for gettin' me outta there, huh?"
    show old_crystal 4 with dissolve
    show player 14
    player_name "Oh, no thanks needed. I was just happy to help."
    show player 13
    show old_crystal 2 with dissolve
    crystal "Heh, yeah... Okay."
    crystal "If you say so, Romeo."
    crystal "The offer stands iffin' you change yer mind."
    crystal "I can be REAL thankful... if ya know what I mean?"
    show old_crystal 1
    show player 5
    player_name "{i}*Gulp*{/i}"
    show old_crystal 2
    crystal "Hehehe."
    return

label button_crystal_should_go_evening:
    show player 14
    player_name "I should probably get in there..."
    show player 13
    show old_crystal 6
    crystal "Yeah, I reckon yer right about that."
    crystal "Take good care of my girl now, ya hear?"
    show old_crystal 5
    show player 14
    player_name "Yes, ma'am."
    hide player with dissolve
    pause
    show old_crystal 6
    crystal "Hahaha, \"ma'am\"..."
    crystal "That kills me every time!"
    hide old_crystal with dissolve
    return

label button_crystal_should_go_day:
    show player 14
    player_name "I should probably go and find {b}Roxxy{/b}."
    show player 13
    show old_crystal 2
    crystal "Well, you don't have to go runnin' off now..."
    crystal "... I'm more than happy to keep you company 'til she gets home."
    show old_crystal 1
    show player 14
    player_name "Heh, no that's alright. I'd hate to be a bother."
    show player 13
    show old_crystal 2
    crystal "Psh, ain't no bother."
    crystal "I know a few ways we could pass the time..."
    show old_crystal 1
    show player 3 with dissolve
    player_name "{i}*Gulp*{/i}"
    show player 29
    player_name "I'll uhh... See you later, {b}Crystal{/b}."
    show player 3
    show old_crystal 2
    crystal "Suit yerself."
    hide player
    hide old_crystal
    with dissolve
    return

label button_crystal_she_here:
    show player 14
    player_name "Yeah, is she here?"
    show player 13
    show old_crystal 6
    crystal "Oh, yeah she's in there..."
    show old_crystal 11
    crystal "Probably yappin' on her phone, as usual."
    crystal "If I didn't know better, I'd swear that thing was glued to the side of that girl's head!"
    show old_crystal 5
    show player 17
    player_name "Heh, yeah."
    show player 13
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
