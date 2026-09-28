label button_mrsj_greetings:
    show player 14 at left
    show mrsj 14 at right
    with dissolve
    player_name "Hi, {b}Mrs. Johnson{/b}!"
    show player 1
    show mrsj 17
    mrsj "Hey, {b}[firstname]{/b}!"
    mrsj "How are you?"
    show player 14
    show mrsj 14
    player_name "I'm good, thanks!"
    show player 1
    show mrsj 17
    mrsj "Is there anything I can do for ya?"
    show mrsj 14
    return


label button_mrsj_sex_ed_intro:
    scene erik_upstairs_night_c
    show mrsj 42 at right
    show player 11 zorder 2 at left
    show old_erik 1f zorder 1 at Position(xpos=300)
    with dissolve
    mrsj "Hey, boys..."
    show mrsj 41
    show player 21
    player_name "H-hi, {b}Mrs. Johnson{/b}!"
    show player 13
    show old_erik 4f
    erik "You're... Very pretty, {b}Mrs. Johnson{/b}."
    show old_erik 1f
    show mrsj 40b with fastdissolve
    mrsj "Well, are you just gonna keep staring at me or do you want to ask me something?"
    show mrsj 39
    return

label button_mrsj_private_yoga_intro:
    scene erik_upstairs_night_c2
    show mrsj 54 at Position(xpos=734,ypos=650)
    show player 433 zorder 2 at left
    with dissolve
    mrsj "Hello, {b}[firstname]{/b}..."
    show mrsj 53
    player_name "!!!"
    show mrsj 54
    mrsj "Is there something wrong?"
    show player 435
    show mrsj 53
    player_name "You... You're naked, {b}Mrs. Johnson{/b}."
    show player 434
    show mrsj 54
    mrsj "I like to feel... Comfortable in my room..."
    mrsj "Weren't you about to ask me something?"
    show mrsj 53
    return

label button_mrsj_erik_learn_fetch_prompt:
    show mrsj 14 at right
    show player 10 at left
    player_name "How can we help you get ready for our sex education again?"
    show player 5
    show mrsj 17
    mrsj "I'll need a good instructional book, like {b}Kama Sutra{/b}."
    mrsj "And some {b}birth control pills{/b}!"
    show mrsj 49
    mrsj "You can never be too careful..."
    show mrsj 50
    show player 14
    player_name "Alright."
    player_name "I'll try and find them..."
    show player 5
    show mrsj 17
    mrsj "Remember to bring them with you to my room in the {b}evening{/b}."
    hide player
    hide mrsj
    with dissolve
    return

label button_mrsj_erik_got_gf:
    show player 14
    player_name "I think I was able to introduce {b}Erik{/b} to a girl at school!"
    show player 1
    show mrsj 17
    mrsj "Really?!"
    show player 14
    show mrsj 14
    player_name "Yeah!"
    player_name "They have so much in common, they would be perfect for each other!"
    show mrsj 17
    show player 17
    player_name "I think it's going to work out for sure!"
    show player 1
    show mrsj 18
    mrsj "That's wonderful!!"
    show mrsj 17
    mrsj "I can't believe you've been so good to {b}Erik{/b}."
    show mrsj 49
    mrsj "I think it's time for me to give you a little reward..."
    show player 21
    show mrsj 50
    player_name "A... A reward?"
    show player 11
    show mrsj 49
    mrsj "How about I give you some... {i}private{/i} yoga lessons..."
    mrsj "The kind you don't get to see in the gym."
    show mrsj 50
    show player 21
    player_name "That would be awesome, {b}Mrs. Johnson{/b}!"
    show player 13
    show mrsj 49
    if game.timer.is_dark():
        mrsj "Then let's get started, shall we?"

        scene erik_upstairs_night_c2
        show mrsj 54 at Position(xpos=734,ypos=650)
        show player 433 zorder 2 at left
        with fade
    else:
        mrsj "Just come visit me at night in my room... Make sure you're well-rested!"
        show player 11
        mrsj "It can be... Quite exhausting."
        show player 21
        show mrsj 50
        player_name "Y-yes, {b}Mrs. Johnson{/b}."
        show player 13
        show mrsj 49
        mrsj "See you later, I'll be waiting!"
        hide player
        hide mrsj
        with dissolve
    return

label button_mrsj_erik_introduce_june:
    show player 14
    player_name "There's this girl at school that I think {b}Erik{/b} likes."
    show player 1
    show mrsj 17
    mrsj "Really?"
    show mrsj 18
    mrsj "That's wonderful!"
    show mrsj 17
    mrsj "Do you know her? What is she like?!"
    show mrsj 14
    show player 14
    player_name "No, I haven't spoken to her yet."
    player_name "She's from a different class, I think."
    show mrsj 17
    show player 1
    mrsj "Oh, I see."
    show player 11
    mrsj "Is {b}Erik{/b} speaking to her?"
    show mrsj 14
    show player 10
    player_name "I don't think so... He says he's too shy."
    player_name "I told him I would find out more about her and let him know what she's like."
    show mrsj 18
    show player 13
    mrsj "That's so nice of you!!"
    show mrsj 17
    mrsj "He's very lucky to have you as a friend..."
    show mrsj 14
    show player 14
    player_name "Oh, I'm sure he would do the same for me!"
    show mrsj 49
    show player 1
    mrsj "Tell you what, let me know how all of this goes..."
    show player 11
    mrsj "If you can find {b}Erik{/b} a girlfriend, there's a special reward waiting for you..."
    show mrsj 50
    player_name "..."
    show player 21
    player_name "Sure, {b}Mrs. Johnson{/b}!"
    show player 1
    show mrsj 14
    return

label button_mrsj_breastfeeding:
    show mrsj 38 at right
    show player 12 at left
    player_name "So, how long have you been... Breastfeeding {b}Erik{/b}?"
    show player 5
    show mrsj 52
    mrsj "Oh..."
    mrsj "Listen, it's not what you might think."
    mrsj "I just always nurtured him like this."
    show mrsj 38
    show player 11
    mrsj "..."
    show mrsj 52
    mrsj "You know he doesn't get much attention from the girls at school."
    mrsj "I felt so bad for him!"
    mrsj "I just wanted {b}Erik{/b} to experience and see what women are all about!"
    show mrsj 20
    mrsj "But maybe I... I over did it?"
    show mrsj 19c
    show player 5
    player_name "..."
    show player 12
    player_name "It's great that you care so much and give him attention!"
    show mrsj 14
    show player 10
    player_name "I think he's very lucky..."
    show player 11
    show mrsj 18
    mrsj "Oh, haha!"
    show mrsj 17
    mrsj "Well, thank you..."
    mrsj "I think nice young men like yourselves need all the attention you can..."
    show mrsj 14
    show player 13
    player_name "..."
    show mrsj 49
    mrsj "I mean, thanks for understanding, {b}[firstname]{/b}."
    show mrsj 52
    mrsj "Just... Remember to keep this between us, okay?"
    show mrsj 14
    show player 14
    player_name "Yes, {b}Mrs. Johnson{/b}."
    hide player
    hide mrsj
    with dissolve
    return

label button_mrsj_yoga_help_repeat:
    show player 10
    player_name "What did you need me to help with?"
    show player 5
    show mrsj 19
    mrsj "I need someone to go and {b}teach my yoga class for me tonight{/b}."
    show mrsj 49
    mrsj "Do you think you could help your... Favorite neighbor??"
    show mrsj 50
    show player 14
    player_name "Of course!"
    show player 13
    show mrsj 17
    mrsj "Remember to {b}study those yoga moves from that list{/b} I gave!"
    return

label button_mrsj_youre_so_fit:
    show mrsj 14 at right
    show player 29 at left
    player_name "I have to say, {b}Mrs. Johnson{/b}, you are really fit!"
    player_name "Do you exercise a lot?"
    show mrsj 18 at right
    show player 13 at left
    mrsj "Aw... You're so nice!"
    show mrsj 17 at right
    mrsj "Well, I try to use the gym as often as I can..."
    mrsj "... I also go jogging! And I do yoga in my room at night as well..."
    show mrsj 19 at right
    show player 21 at left
    player_name "Well, it's working!"
    show player 13 at left
    mrsj "You think?"
    show mrsj 15 at right
    show player 11 at left
    mrsj "My butt is still a bit big..."
    show mrsj 16 at right
    show player 23 at left
    mrsj "... And my boobs are not like they used to be..."
    player_name "..."
    show player 28 at left
    show mrsj 19 at right
    player_name "{i}*Gulp*{/i}"
    show player 1 at left
    show mrsj 18 at right
    mrsj "Is there anything else you wanted to talk about?"
    return

label button_mrsj_leave:
    python:
        mrsj_nude = game.timer.is_dark() and \
                    M_erik.finished_state(S_erik_learn_prep)
        mrsj_nude_bed = game.timer.is_dark() and \
                        M_mrsj.finished_state(S_mrsj_cupid_report)

    if mrsj_nude:
        show mrsj 39
        show player 14 at left
        player_name "I have to go, but I'll be back though!"
    else:
        if mrsj_nude_bed:
            show mrsj 53
        else:
            show mrsj 14 at right
        show player 14 at left
        player_name "I should go find {b}Erik{/b}!"
    if mrsj_nude or mrsj_nude_bed:
        if mrsj_nude:
            show mrsj 40
        elif mrsj_nude_bed:
            show mrsj 54
        show player 1 at left
        mrsj "Really?"
        mrsj "Well, be sure to come back soon!"
    else:
        show mrsj 18 at right
        show player 1 at left
        mrsj "Alright, then!"
    if mrsj_nude:
        show mrsj 39
    elif mrsj_nude_bed:
        show mrsj 53
    else:
        show mrsj 14 at right
    show player 17 at left
    player_name "Bye, {b}Mrs. Johnson{/b}!"

    $ del mrsj_nude, mrsj_nude_bed
    return

label mrsj_erik_poker_invite_early:
    player_name "I was wondering if you'd like to join {b}Erik{/b} and me for poker?"
    show player 1
    show mrsj 17
    mrsj "I can't right now, I have to teach a class soon..."
    mrsj "But stop by my room this {b}evening{/b} and I'd be happy to."
    show player 18
    show mrsj 14
    player_name "Awesome! Thanks, {b}Mrs. Johnson{/b}!"
    hide player
    hide mrsj
    with dissolve
    return

label mrsj_erik_poker_invite_fail:
    player_name "I was wondering if you could teach us to play poker?"
    show mrsj 17
    show player 1
    mrsj "The card game?"
    show mrsj 14
    show player 14
    player_name "Yeah, {b}Erik{/b} and I are just looking for a third player."
    show mrsj 17
    show player 14
    mrsj "Oh, I'd love to."
    show player 19
    mrsj "But I really just don't have the time today, sorry..."
    show mrsj 14
    show player 14
    player_name "That's alright, maybe some other time."
    hide player
    hide mrsj
    with dissolve
    return

label mrsj_erik_poker_invite_pass:
    player_name "I was wondering if you'd like to join {b}Erik{/b} and me for poker?"
    show player 1
    show mrsj 17
    mrsj "Right now?"
    show player 14
    show mrsj 14
    player_name "Yeah..."
    player_name "I mean, you don't have to!"
    player_name "{b}Erik{/b} and I are just looking for a third player..."
    show player 1
    show mrsj 17
    mrsj "He's waiting downstairs?"
    show player 14
    show mrsj 14
    player_name "Yeah, we'd like to play now, if you're free?"
    show player 1
    mrsj "Hmm..."
    show mrsj 17
    mrsj "Sounds like fun, I might even be able to teach you boys a thing or two."
    show mrsj 18
    show player 13
    mrsj "Let's go!"
    show player 18
    show mrsj 14
    player_name "Awesome! Thanks, {b}Mrs. Johnson{/b}!"
    hide mrsj
    hide player
    with dissolve

    scene erik_basement_c
    show old_erik 1f at Position(xpos=300,ypos=768)
    with fade
    show mrsj 19 at right
    show player 1 at left
    with dissolve
    mrsj "You boys aren't planning on playing like this, are you?"
    show player 11
    show mrsj 14
    player_name "..."
    show player 10
    player_name "What do you mean?"
    show player 11
    show mrsj 18
    mrsj "You can't play poker without a nice drink!"
    show mrsj 14
    show player 1
    show old_erik 4f
    erik "A drink?"
    show old_erik 1f
    show mrsj 18
    mrsj "Let's see what's left in the {b}alcohol cabinet{/b}, shall we?"
    hide mrsj
    hide old_erik
    hide player
    with dissolve

    scene erik_basement_cabinet with fade
    show old_erik 5f at Position(xpos=300,ypos=768)
    show player 1 at left
    show mrsj 14 at right
    with dissolve
    erik "Whiskey..."
    erik "Whiskey... Whiskey..."
    erik "Whiskey... Whiskey... Whiskey..."
    erik "There's nothing but whiskey in here..."
    show old_erik 1f
    show mrsj 17
    mrsj "My husband only drank whiskey."
    show mrsj 14
    show player 14
    player_name "That's fine!"
    player_name "We'll take whatever's in there, haha!"
    show old_erik 15
    show player 1
    with dissolve
    erik "Should we try it before we take it to the table?"
    show old_erik 16
    show mrsj 22
    with dissolve
    mrsj "Let's see how this tastes..."
    show old_erik 20
    show mrsj 21
    show player 185
    with dissolve
    erik "Here we go..."
    show player 186
    show old_erik 17
    player_name "Cheers!"
    show player 189
    show old_erik 19
    show mrsj 25
    with fastdissolve
    pause
    show mrsj 26
    show old_erik 17
    show player 190
    with fastdissolve
    pause
    show player 191
    player_name "Ugh!!"
    show player 188
    show mrsj 24
    show old_erik 17
    with dissolve
    mrsj "Woaa..."
    show old_erik 20
    show mrsj 14
    with dissolve
    erik "Hmm... Not bad!"
    show old_erik 17
    player_name "..."
    show player 187
    player_name "You liked that?!"
    show player 188
    show old_erik 20
    erik "Yeah, it's kind of sweet."
    show player 185
    show old_erik 17
    show mrsj 18
    mrsj "Alright, boys! Let's take this back and start the game!"
    hide mrsj
    hide old_erik
    hide player
    with dissolve

    scene expression "minigames/poker/location_erik_basement_poker.jpg"
    show mrsjpoker 2 zorder 1 at Position(xpos=857,ypos=626)
    show mrsjpokerc1 7 zorder 2 at Position(xpos=815,ypos=584)
    show mrsjpokerc2 8 zorder 2 at Position(xpos=910,ypos=387)
    show old_erikpoker 1 zorder 1 at Position(xpos=153,ypos=626)
    show old_erikpokerc 9 zorder 2 at Position(xpos=144,ypos=592)
    with fade
    mrsj "So..."
    mrsj "Are we playing Omaha, or Texas hold'em?"
    show mrsjpoker 1
    player_name "..."
    player_name "We only know strip poker..."
    show mrsjpoker 2
    mrsj "Haha! Are you kidding me?"
    show mrsjpoker 10 at Position(xpos=856,ypos=627)
    player_name "It's the only kind people play at school..."
    show old_erikpoker 2
    erik "You don't have to... {b}Mrs. Johnson{/b}."
    show old_erikpoker 11
    show mrsjpoker 9 at Position(xpos=856,ypos=627)
    mrsj "I'll play!"
    show mrsjpoker 4 at Position(xpos=857,ypos=626)
    mrsj "I'm not a prude. I can have fun, too!"
    show mrsjpoker 2
    mrsj "I used to play strip poker back in the day..."
    show mrsjpoker 5
    mrsj "... And I was the {b}best{/b} at it!"
    show old_erikpoker 12
    show mrsjpoker 1
    erik "So, what do we do now?"
    show old_erikpoker 1
    return

label mrsj_erik_poker_invite_repeat:
    python:
        mrsj_nude = game.timer.is_dark() and \
                    M_erik.finished_state(S_erik_learn_prep)
        mrsj_nude_bed = game.timer.is_dark() and \
                        M_mrsj.finished_state(S_mrsj_cupid_report)

    show player 14 at left
    if mrsj_nude:
        show mrsj 39
    elif mrsj_nude_bed:
        show mrsj 53
    else:
        show mrsj 14 at right
    player_name "Would you like to play some poker with us again?"
    show player 1
    if mrsj_nude:
        show mrsj 40
    elif mrsj_nude_bed:
        show mrsj 54
    else:
        show mrsj 17
    mrsj "Still looking for friends to play with?"
    show player 14
    if mrsj_nude:
        show mrsj 39
    elif mrsj_nude_bed:
        show mrsj 53
    else:
        show mrsj 14
    player_name "Well, it's just that-"
    show player 1
    if mrsj_nude:
        show mrsj 40
    elif mrsj_nude_bed:
        show mrsj 54
    else:
        show mrsj 18
    mrsj "It's fine!!"
    show player 1
    if mrsj_nude:
        show mrsj 40
    elif mrsj_nude_bed:
        show mrsj 54
    else:
        show mrsj 17
    mrsj "I'll play with you boys..."
    show player 14
    if mrsj_nude:
        show mrsj 39
    elif mrsj_nude_bed:
        show mrsj 53
    else:
        show mrsj 14
    player_name "Really?"
    show player 1
    if mrsj_nude:
        show mrsj 40b
    elif mrsj_nude_bed:
        show mrsj 54
    else:
        show mrsj 20
    mrsj "Well... Last time was a bit much..."
    show player 13
    if mrsj_nude:
        show mrsj 40
    elif mrsj_nude_bed:
        show mrsj 54
    else:
        show mrsj 18
    mrsj "But, why not?"
    show player 14
    if mrsj_nude:
        show mrsj 39
    elif mrsj_nude_bed:
        show mrsj 53
    else:
        show mrsj 14
    player_name "Okay."
    show player 13
    if mrsj_nude:
        show mrsj 40
    elif mrsj_nude_bed:
        show mrsj 54
    else:
        show mrsj 17
    mrsj "When are we playing?"
    show player 14
    if mrsj_nude:
        show mrsj 39
    elif mrsj_nude_bed:
        show mrsj 53
    else:
        show mrsj 14
    if mrsj_nude:
        player_name "Right now!"
    else:
        player_name "{b}Erik{/b}'s already downstairs waiting."
    show player 1
    if mrsj_nude:
        show mrsj 40b
    elif mrsj_nude_bed:
        show mrsj 54
    else:
        show mrsj 18
    mrsj "Haha, alright."
    if mrsj_nude or mrsj_nude_bed:
        mrsj "Just let me get dressed."
        if mrsj_nude_bed:
            mrsj "So you can undress me again!"
        else:
            mrsj "Otherwise, it'll be a very short game!"
    hide mrsj
    hide old_erik
    hide player
    with dissolve

    $ del mrsj_nude, mrsj_nude_bed

    scene erik_basement_cabinet
    show old_erik 4f at Position(xpos=300)
    with fade
    erik "I'll fetch the whiskey!"
    show player 1 at left
    show mrsj 14 at right
    with dissolve
    show old_erik 1f
    show mrsj 19
    show player 11
    mrsj "Oh, are you two sure about that?"
    show mrsj 19c
    show player 10
    player_name "About what?"
    show mrsj 19
    show player 11
    mrsj "The alcohol, you remember what happened last time, right?"
    show mrsj 19c
    show old_erik 5f
    erik "But, we all had fun, didn't we?"
    show old_erik 1f
    pause
    show mrsj 14 with fastdissolve
    pause
    show mrsj 17
    show player 1
    mrsj "I suppose you're right..."
    show mrsj 18
    mrsj "Oh, what the heck, let's do it!"
    hide mrsj
    hide old_erik
    hide player
    with dissolve

    scene expression "minigames/poker/location_erik_basement_poker.jpg"
    show mrsjpoker 2 zorder 1 at Position(xpos=857,ypos=626)
    show mrsjpokerc1 7 zorder 2 at Position(xpos=815,ypos=584)
    show mrsjpokerc2 8 zorder 2 at Position(xpos=910,ypos=387)
    show old_erikpoker 1 zorder 1 at Position(xpos=153,ypos=626)
    show old_erikpokerc 9 zorder 2 at Position(xpos=144,ypos=592)
    with fade
    mrsj "So..."
    mrsj "Are we playing strip poker again?"
    show mrsjpoker 1
    player_name "..."
    show mrsjpoker 2
    mrsj "Haha! I can read you two like a pair of books!"
    show mrsjpoker 10 at Position(xpos=856,ypos=627)
    show old_erikpoker 2
    erik "You don't have-"
    show old_erikpoker 11
    show mrsjpoker 9 at Position(xpos=856,ypos=627)
    mrsj "I'll play!"
    show mrsjpoker 4 at Position(xpos=857,ypos=626)
    mrsj "I'm not a prude. I'd have thought you'd know that by now!"
    show mrsjpoker 2
    show old_erikpoker 1
    return

label mrsj_erik_fork:
    show player 14 at left
    show mrsj 14 at right
    player_name "I wanted to talk about {b}Erik{/b}..."
    show player 1
    show mrsj 19
    mrsj "Oh, is he okay?"
    show player 14
    show mrsj 19c
    player_name "Yeah, he's fine."
    player_name "I was talking to him about what happened the other night..."
    show player 11
    show mrsj 19
    mrsj "Is he upset?"
    show player 14
    show mrsj 19c
    player_name "No, not at all."
    show player 10
    player_name "He's just not sure about what he wants..."
    show player 11
    show mrsj 19
    mrsj "How so?"
    show player 10
    show mrsj 19c
    player_name "I think he's given up on meeting girls."
    player_name "I could try and help him get a girlfriend, but I think he likes you more..."
    show player 13
    show mrsj 19
    mrsj "Oh, my..."
    show mrsj 20
    mrsj "Have I really sheltered him too much?"
    show mrsj 19
    mrsj "What do you think I should do?"
    show mrsj 19c
    return

label mrsj_erik_fork_teach:
    show player 14 at left
    show mrsj 19c at right
    player_name "I think it's best if you give him the attention he needs..."
    show mrsj 19
    show player 1
    mrsj "You really think so?"
    show mrsj 19c
    show player 14
    player_name "Well, I don't think he wants to see any other girls..."
    player_name "... And he really likes you!"
    show mrsj 19
    show player 1
    mrsj "He's always been close to me..."
    show mrsj 19c
    show player 14
    player_name "We had such a great time the other night!"
    player_name "I've never seen {b}Erik{/b} this happy."
    show mrsj 19
    show player 11
    mrsj "Do you think... You boys would like more of that kind of... Attention?"
    show mrsj 19c
    show player 21
    player_name "I... I think so!"
    show mrsj 20
    show player 13
    mrsj "If none of the girls from school will give him the attention he needs..."
    show mrsj 19
    mrsj "... Maybe I should be the one?"
    show mrsj 14
    show player 14
    player_name "I think he would like that."
    show mrsj 49
    show player 11
    mrsj "What if I gave you guys some... Personal sex education?"
    show mrsj 50
    player_name "!!!" with vpunch
    show mrsj 49
    mrsj "It's only for educational purposes of course..."
    show mrsj 50
    show player 29
    player_name "Oh, I emm... I wouldn't mind at all!"
    show mrsj 49
    show player 13
    mrsj "I'd have to think it over first, though."
    show mrsj 50
    show player 14
    player_name "Sure, {b}Mrs. Johnson{/b}!"
    show mrsj 14
    show player 1
    with None
    hide player
    hide mrsj
    with dissolve
    return

label mrsj_erik_fork_match:
    show player 14 at left
    show mrsj 19c
    player_name "I think we should try and find him a girlfriend."
    show player 1
    show mrsj 19
    mrsj "You really think so?"
    show player 14
    show mrsj 19c
    player_name "Well, I think he would be happier..."
    player_name "... And it'd build up his confidence!"
    show player 1
    show mrsj 20
    mrsj "He does need to go out more..."
    show player 10
    show mrsj 19c
    player_name "Don't get me wrong, we had a lot of fun the other night..."
    show player 14
    player_name "... But I think {b}Erik{/b} needs to meet other girls."
    show player 13
    show mrsj 20
    mrsj "You're right..."
    show player 11
    show mrsj 19
    mrsj "But what about... Me?"
    show player 10
    show mrsj 19c
    player_name "What do you mean?"
    show player 11
    show mrsj 19
    mrsj "Well..."
    mrsj "If {b}Erik{/b} finds a girlfriend... What will I do?"
    show mrsj 20
    mrsj "I won't have anyone to give my attention to..."
    show player 21
    show mrsj 19c
    player_name "Oh, I'm sure you will find someone {b}Mrs. Johnson{/b}!"
    show mrsj 14
    player_name "You're very... Attractive, and loving!"
    show player 13
    show mrsj 17
    mrsj "Aww, that's very sweet of you to say."
    show mrsj 50
    mrsj "Hmm..."
    show mrsj 49
    show player 1
    mrsj "I have a different idea!"
    mrsj "What if I took that attention..."
    show player 11
    mrsj "... And gave it to {i}you{/i}?"
    show mrsj 50
    player_name "!!!" with vpunch
    show mrsj 49
    mrsj "What's wrong?"
    mrsj "Only if you wanted to, is what I meant to say..."
    show player 21
    show mrsj 50
    player_name "I-I wouldn't mind at all!"
    player_name "But, only as long as {b}Erik{/b} is okay with it."
    show player 1
    show mrsj 49
    mrsj "Just ask him!"
    mrsj "I'm sure he would be okay with that..."
    show player 13
    mrsj "... Especially if he's too busy playing with another girl! Haha."
    show player 29
    show mrsj 50
    player_name "I suppose so, haha."
    show player 14
    player_name "I'll try and find someone for him..."
    show player 13
    show mrsj 49
    mrsj "Come back and let me know what happens."
    show player 17
    show mrsj 50
    player_name "Sure, {b}Mrs. Johnson{/b}!"
    show mrsj 14
    show player 1
    with None
    hide player
    hide mrsj
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
