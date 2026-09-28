label pizzeria_interior_maria_pregnancy:
    call tony_button_stage
    hide tony
    show tony:
        flip
        xoffset 100
    show maria:
        flip
        xoffset -100
    show anon with dissolve:
        flip
    anon "Hey, I came as fast as I cou-"
    show tony b_dressed_hug_mc f_laugh:
        xoffset 300
    hide anon
    anon "!!!" with hpunch
    tony f_normal_down "You did it again, champ!"
    anon "What the-"
    tony f_laugh "You fuckin' did it!!"
    tony "I'm so proud of ya!!!"
    show anon f_surprised:
        flip
        xoffset 100
    show tony b_dressed f_normal:
        xoffset 50
    with dissolve
    anon "You're pregnant, again?"
    maria @ -m_talk "Mhmm."
    show anon b_empty
    show maria b_dressed_hug_mc:
        xoffset 100
    with dissolve
    anon "That's wonderful!"
    tony "We really hit the jackpot when we found you, eh?"
    show anon f_normal b_dressed
    show maria b_dressed:
        xoffset -200
    with dissolve
    anon "I'm so happy for you guys."
    tony "Happy for all three of us, right?"
    show tony a_mc_hip_single:
        xoffset 137
    show tony_arms_dressed_a_mc_shoulder_single:
        flip
        xoffset 137
    with dissolve
    tony "I mean, you're gonna be the godfather, ain't ya?"
    anon "Of course."
    anon "I'd be honored you guys..."
    hide tony_arms_dressed_a_mc_shoulder_single
    show tony a_scrub f_normal_down:
        xoffset 150
    hide anon
    with dissolve
    tony "Ahh, c'mere!!"
    anon "Hehe!"
    tony "I love this kid!"
    show tony a_idle f_normal:
        xoffset 50
    show anon f_hurt a_rub behind tony:
        flip
        xoffset 100
    with dissolve
    tony "You ever need anything... Anything at all..."
    show anon f_shy
    tony "I'm ya guy, capisce?"
    anon f_normal a_idle "Thanks, {b}Tony{/b}."
    maria "We're gonna have to start lookin' for a bigger place soon."
    show tony with {'master': dissolve}:
        unflip
        xoffset -300
    tony "Ain't that the truth!"
    tony f_smirk "Our little shithole apartment wasn't built for a big family like us!"
    maria "We'll have to make sure we have an extra room for {b}[firstname]{/b} too."
    tony "Heh, of course, darlin'."
    anon @ f_surprised "!!!"
    anon "You don't have to-"
    show tony with {'master': dissolve}:
        flip
        xoffset 50
    maria "Shh!"
    maria "Yes, we do have to and that's the end of it!"
    anon @ -m_talk "..."
    show tony a_mc_hip_single:
        xoffset 137
    show tony_arms_dressed_a_mc_shoulder_single:
        flip
        xoffset 137
    with dissolve
    tony "C'mon, champ!"
    tony "We gotta go celebrate!"
    anon "Yeah, okay."
    tony f_normal_right "Why don't you run back and grab us some champagne and cannolis, eh?"
    maria "Yeah, alright."
    maria "I love you boys!"
    hide maria with dissolve
    tony "We love you too, darlin'!"
    hide tony
    hide tony_arms_dressed_a_mc_shoulder_single
    hide anon
    with dissolve
    return


label pizzeria_interior_maria_baby:
    $ player.last_baby_gender = M_maria.pregnancy.baby_gender
    call tony_button_stage
    show tony f_angry a_baby_phone:
        unflip
        xoffset -500
    show anon with dissolve:
        flip
    tony "Yeah, double pepperoni, hold the olives..."
    tony "... I got it."
    pause
    tony "Because I heard ya the first fuckin' time, asshole!"
    show anon f_worried
    "{i}*Crying*{/i}"
    tony f_sad_down "Oh, Jesus..."
    pause
    tony f_angry "Pfft, you can shove your tip right up your ass for all I care!"
    pause
    tony "Yeah, it'll be there in twenty minutes."
    pause
    tony "What did I just say?"
    tony a_baby "Fuckin' douchebag."
    anon "Hello?"
    tony @ f_eyeroll "Yeah, just come in and take a seat."
    tony "I'll be with ya in-"
    show tony f_normal with dissolve:
        flip
        xoffset 0
    tony "Champ!"
    tony "You sure got some fortuitous timin'!"
    if M_maria.pregnancy.baby_gender == 'boy':
        tony "Hold your godson for a second, would ya?"
    elif M_maria.pregnancy.baby_gender == 'girl':
        tony "Hold your goddaughter for a second, would ya?"
    else:
        tony "Hold your godchildren for a second, would ya?"
    show tony a_idle
    show anon a_baby
    with dissolve
    anon "What's goin' on?"
    tony @ -m_talk "Hmm?"
    anon "Where's {b}Maria{/b}?"
    tony @ f_eyeroll "Oh, she's back there, cookin' up a storm."
    if M_maria.pregnancy.baby_gender == 'twins':
        tony "We decided I would watch the little ones in the morning so she could get ahead in the orders..."
    else:
        tony "We decided I would watch the little one in the morning so she could get ahead in the orders..."
    tony "... That way in the afternoon, she can focus on more important things."
    if M_maria.pregnancy.baby_gender == 'twins':
        tony "Like puttin' these little stinkers down for a nap."
    else:
        tony "Like puttin' that little stinker down for a nap."
    tony @ f_laugh "Haha!"
    if M_maria.pregnancy.baby_gender == 'twins':
        anon f_shy_down "Your kids look great, {b}Tony{/b}."
    else:
        anon f_shy_down "Your kid looks great, {b}Tony{/b}."
    if M_maria.pregnancy.baby_gender == 'boy':
        tony "Yeah, he's somethin' else, ain't he?"
    elif M_maria.pregnancy.baby_gender == 'girl':
        tony "Yeah, she's somethin' else, ain't she?"
    else:
        tony "Yeah, they're somethin' else, ain't they?"
    if M_maria.pregnancy.baby_gender == 'twins':
        maria "Why are the babys cryin', {b}Tony{/b}?"
    else:
        maria "Why is the baby cryin', {b}Tony{/b}?"
    show maria f_annoyed with dissolve:
        flip
        xoffset -200
    if M_maria.pregnancy.baby_gender == 'twins':
        tony "Ahh, the babies are fine!"
    else:
        tony "Ahh, the baby's fine!"
    tony "Just a little scuffle on the telephone, that's all."
    maria f_surprised "Oh, hey, {b}[firstname]{/b}!"
    maria "I didn't know you were comin' in today?!"
    anon f_normal "I wasn't certain either."
    show maria a_take_baby with dissolve
    if M_maria.pregnancy.baby_gender == 'boy':
        maria "Here, I'll take him."
    elif M_maria.pregnancy.baby_gender == 'girl':
        maria "Here, I'll take her."
    else:
        maria "Here, I'll take them."
    show maria a_baby f_normal_down
    show anon a_idle
    with dissolve
    anon @ -m_talk "..."
    maria "I sure am glad to see ya!"
    anon "Yeah, likewise."
    pause
    anon "You doing alright?"
    maria @ f_normal "Oh, I'm better than alright!"
    maria "You gave us the greatest gift anyone could ever give!"
    tony "Ain't that the truth."
    pause
    maria f_normal "So, back to work already?"
    anon "Yeah, if you need me?"
    tony @ a_frustrated "Pfft, of course we need ya, champ!"
    tony "This is a family-run business..."
    tony "... It don't work without the godfather."
    anon "Heh, thanks, {b}Tony{/b}."
    tony "You bet."
    tony @ a_point_back "C'mon, I got some deliveries waitin' for ya."
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
