label micoe_dialogue_blowjob:
    scene expression "backgrounds/location_hospital_room_day_blur.jpg"
    show player 10 at left
    show micoe:
        flip
    with dissolve
    player_name "Remember when you helped me... Umm, extract my sample for testing."
    show player 5
    show micoe f_sexy
    micoe "You mean, when I sucked your cock in the bathroom?"
    show player 11
    player_name "!!!"
    show player 29 with dissolve
    player_name "Y-yeah."
    show player 3
    micoe @ f_laugh "Hehehe, I think we're past being shy, {b}[firstname]{/b}."
    micoe "You here to let me have another taste?"
    show player 17 with dissolve
    player_name "Uh huh."
    hide player
    show micoe b_pulling
    with dissolve
    micoe "C'mon cutie."
    $ player.go_to(L_hospital_room_bathroom)
    scene expression player.location.background_blur
    show player 13f at right
    show micoe f_sexy
    with dissolve
    micoe "What are you waiting for?"
    micoe "Get that cock out!"
    show player 14f
    player_name "O-okay."
    show player 261b with dissolve
    pause
    show player 263b at Position (xoffset=-150)
    show micoe b_knees
    with dissolve
    pause
    show micoe b_knees_talk
    micoe "Mmm, I'll suck this beautiful cock anytime you want, {b}[firstname]{/b}!"
    $ M_micoe.set('sex speed', .12)
    $ anim_toggle = True
    $ animated = True
    scene expression player.location.background_closeup
    show expression AnimatedImage("micoe_bj", [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], M_micoe) as micoe_bj at Position(xalign = 0.0, yoffset = 0)
    with dissolve
    micoe "{i}*Slurp*{/i}"
    player_name "Oh, god..."
    player_name "That feels amazing, {b}Micoe{/b}."
    micoe "Mmhmm!"
    return

label micoe_dialogue_goodbye:
    show player 14 at left
    show micoe:
        flip
    player_name "Just saying hello."
    show player 13
    show micoe f_sad
    micoe "Oh, well, that's disappointing..."
    show micoe f_sexy
    micoe "I thought maybe you were here to have a little fun."
    show player 14
    player_name "Sorry."
    show player 13
    pause
    show player 14
    player_name "I'll see you around, okay?"
    show player 13
    show micoe f_normal
    micoe "Alright, cutie."
    hide player
    hide micoe
    with dissolve
    return

label micoe_dialogue_intro:
    scene expression player.location.background_blur with None
    show player 13 at left
    show micoe:
        flip
    micoe "Hey there, cutie."
    micoe "You lost?"
    return

label micoe_dialogue_increase_chance_of_conception:
    show micoe:
        flip
    show player 10 at left
    with dissolve
    player_name "Is there anything more I could be doing to help my fri-"
    player_name "{i}*Ahem*{/i} I mean, help my girlfriend conceive a baby?"
    show player 5
    show micoe f_normal
    micoe "Hmm, is she stressing out about it?"
    show player 10
    player_name "Ehh, not really..."
    player_name "I just want to make sure I'm doing everything I can to help her."
    show player 5
    micoe @ f_laugh "Aww, you're so sweet!"
    show player 13
    micoe "Well, are you two having lots of sex?"
    show player 29 with dissolve
    player_name "Y-yeah."
    show player 13 with dissolve
    micoe "... And what position are you using?"
    show player 10
    player_name "... Position?"
    show player 5
    show micoe f_sexy
    micoe "Yeah, what position are you having sex in?"
    show player 10
    player_name "Err, I dunno."
    show player 14
    player_name "I guess I'm usually behind her..."
    show player 13
    micoe "Doggy style?"
    show player 5
    player_name "..."
    show micoe f_laugh
    micoe "Hehe, you're so cute!"
    show micoe f_normal
    micoe "Doggy style should work fine for conception."
    show player 13
    micoe "A lot of doctors recommend it, because it allows for the deepest penetration."
    show micoe f_wink
    pause
    show micoe f_sexy
    micoe "Though, with what you're packing, deep penetration isn't going to be issue."
    show player 29 with dissolve
    player_name "Heh, y-yeah..."
    show player 13 with dissolve
    show micoe f_normal
    micoe "You might try the missionary position."
    show player 10
    player_name "What's that?"
    show player 13
    micoe "It's when the woman lies on her back and you're on top."
    micoe "In that position, gravity will help carry your semen to the cervix."
    show player 17
    player_name "Ohh, I get it! Normal style."
    show player 18
    show micoe f_sad
    pause
    show player 14
    player_name "That makes sense."
    show player 13
    pause
    show player 14
    player_name "Anything else?"
    show player 13
    show micoe f_normal
    micoe @ -m_talk "Hmm."
    micoe "Not really."
    micoe "Unfortunately, the biggest hurdle in your situation is your girlfriend's age."
    show player 10
    player_name "Yeah."
    show player 5
    pause
    show player 10
    player_name "Are you sure there's nothing else I can do to help?"
    show player 5
    micoe "Well..."
    show micoe f_look_back
    pause
    show micoe f_normal
    micoe "There is one thing... But I'm really not supposed to talk about it."
    show player 12
    player_name "Huh?"
    player_name "How come?"
    show player 5
    pause
    show player 14
    player_name "If there's a chance it will help, I really have to know!"
    player_name "{b}Diane{/b} really has her heart set on getting pregnant."
    show player 13
    pause
    show player 18
    player_name "Please?"
    micoe @ f_laugh "Ngh, you're just so sweet!"
    show player 13
    micoe "Alright, I'll tell you... But you didn't hear this from me!"
    micoe "Understand?"
    show player 14
    player_name "Y-yeah, I understand!"
    show player 13
    micoe "There's a new drug that's been showing a lot of promise when it comes to increasing conception rates."
    micoe "They're calling it {b}Pregnax{/b}."
    show player 14
    player_name "That sounds perfect!"
    show player 12
    player_name "What's the catch?"
    show player 5
    micoe "Well, the catch is that they're still in the testing phase with it."
    pause
    show player 14
    player_name "That's alright, I don't mind helping you test it."
    show player 13
    micoe @ f_laugh "Hehe, you'll have to talk with {b}Dr. Singh{/b} about that."
    show player 10
    player_name "{b}Dr. Singh{/b}?"
    show player 5
    micoe "Yeah, {b}Singh{/b}'s this new fancy pants doctor they shipped in from somewhere overseas."
    micoe "Works down in the {b}basement{/b}."
    micoe "Been developing {b}Pregnax{/b} for years now."
    show player 14
    player_name "Okay, so I'll just go and talk with him!"
    show player 13
    show micoe f_sad
    micoe "Heh, I wish it were that easy."
    micoe "Unfortunately, the {b}basement{/b} is a restricted area."
    micoe "Even I don't have access to it."
    show micoe f_normal
    show player 12
    player_name "So how do I get access?"
    show player 5
    micoe "I can't really help you there, cutie."
    micoe "Not many people in the hospital have the credentials to get down to the basement."
    show player 24
    player_name "Crap."
    pause
    show player 10
    player_name "Alright, thanks for the info {b}Micoe{/b}."
    show player 5
    show micoe f_laugh
    micoe "No problem, cutie!"
    show micoe f_sexy
    micoe "Feel free to come and see me if you have any more questions..."
    show player 13
    show micoe f_wink
    pause
    show micoe f_sexy
    micoe "... Or you feel like having a bit of naughty fun!"
    show player 29 with dissolve
    player_name "Y-yeah, okay."
    show player 3
    micoe "Mmm, so adorable..."
    hide player
    hide micoe
    with dissolve
    return

label micoe_dialogue_pregnax:
    scene expression "backgrounds/location_hospital_room_day_blur.jpg"
    show player 10 at left
    show micoe:
        flip
    with dissolve
    player_name "Where can I find that fertility drug again?"
    show player 5
    show micoe f_sad a_shh with dissolve:
        xoffset -175
    micoe "Shh!"
    micoe "Not so loud!"
    show micoe f_normal a_idle with dissolve
    show player 10
    player_name "Oh, sorry."
    show player 5
    micoe "They keep it down in the {b}basement{/b}."
    show player 14
    player_name "{b}Basement{/b}, got it!"
    show player 13
    micoe "Hold on, you can't just waltz down there."
    micoe "You'll have to {b}find someone with access{/b} to take you."
    show player 10
    player_name "Hmm, who could I ask?"
    show player 5
    micoe "Sorry cutie, I can't help you with that."
    micoe "Just remember, you didn't hear any of this from me!"
    show player 14
    player_name "Don't worry, I won't tell."
    show player 18
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
