label ano06_init_pizzeria_interior:
    call tony_button_stage
    show anon with dissolve:
        flip
    tony @ a_frustrated "Oh, hey there, champ!"
    tony "Boy, am I glad to see you."
    anon "What's going on, {b}Tony{/b}?"
    tony "I got an appointment up at the clinic in an hour and I need you to help {b}Maria{/b} around the store."
    anon "Clinic?"
    anon "Is something the matter?"
    tony @ f_suspicious "Huh?"
    tony @ a_wave "Oh, nah."
    tony "It's nothin' to be concerned about."
    show tony f_sad
    pause
    tony "Just a little test I need the doc to run."
    anon @ f_shy "Phew, okay."
    show tony with dissolve:
        unflip
        xoffset -400
    tony "It might take me a while, though..."
    tony f_suspicious @ a_whisper "Hey, {b}Maria{/b}!"
    maria "What?"
    tony "C'mere, will ya?"
    maria "Ugh, now what?"
    pause
    show maria f_annoyed behind counter with dissolve:
        flip
        xoffset -200
    tony f_sad "I just got off the phone with the doc."
    show maria f_sad
    tony "He's ready to run those tests."
    maria "Right now?"
    tony "I need to be down there in an hour or so."
    maria "So what, are we shuttin' down?"
    tony "Of course not."
    maria f_annoyed "Well, I can't cook the pizzas and run the counter at the same time."
    tony f_normal "{b}[firstname]{/b} can help ya."
    show tony with dissolve:
        flip
        xoffset 0
    tony @ a_point "Right, champ?"

    menu:
        "Wait, what?!":

            anon f_worried "Wait, what?!"
            maria f_sad "I'm not sure about this, {b}Tony{/b}..."
            tony "It'll be fine!"
            tony @ a_frustrated "C'mon, champ!"
            tony "You can do this, no problem."
            anon f_normal "You think?"
            tony "I know."
            tony @ a_fists "You just gotta man up, like I been tellin' ya."
            anon "Y-yeah, okay."
            show tony a_mc_hip_single:
                xoffset 32
            show tony_arms_dressed_a_mc_shoulder_single:
                flip
                xoffset 32
            with dissolve
            tony "Attaboy!"
            tony "I knew I could count on ya."
        "Sure!":

            anon "Y-yeah, I'll help."
            maria f_sad "You really think he's ready for this?"
            show tony f_suspicious with dissolve:
                unflip
                xoffset -400
            tony "Of course he's ready!"
            tony "He's my protégé, ain't he?"
            maria f_normal @ f_laugh "Heh, your protégé, huh?"
            show tony f_normal a_mc_hip_single:
                flip
                xoffset 32
            show tony_arms_dressed_a_mc_shoulder_single:
                flip
                xoffset 32
            with dissolve
            tony "That's right."
            tony "Pretty soon, you won't even be able to tell us apart."
            maria "Oh, you mean he's gonna gain fifty pounds and go bald?"
            show anon f_surprised
            tony f_surprised @ -m_talk "!!!"
            maria @ f_laugh "Hahahaah!"
            show tony f_suspicious a_idle:
                unflip
                xoffset -400
            hide tony_arms_dressed_a_mc_shoulder_single
            with dissolve
            tony "Jesus, {b}Maria{/b}..."
            tony "Why you gotta hit a guy below the belt like that?"
            maria "Aww, I'm justing bustin' ya balls, honey."
            maria "You know I love that belly..."
            show tony f_normal
            maria "... And you got all the hair you need, right there on your upper lip."
            show tony f_smirk_wink with dissolve:
                flip
                xoffset 32
            tony "She does love a good mustache ride."
            show tony -f_smirk_wink
            show maria f_surprised
            anon f_confused "Mustache ride?"
            maria "{b}Tony{/b}, don't go tellin' the kid stuff like that!"
            tony @ f_laugh "Hahahaah!"
            anon "What's a mustache ride?"
            maria a_crossed f_annoyed "Never you mind."
            show tony a_mc_hip_single:
                flip
                xoffset 32
            show tony_arms_dressed_a_mc_shoulder_single:
                flip
                xoffset 32
            with dissolve
            tony "I'll explain it to ya another time, eh?"

    show anon f_normal
    show tony a_idle:
        xoffset 32
    hide tony_arms_dressed_a_mc_shoulder_single
    with dissolve
    tony "For now, I need ya to head back to the kitchen with {b}Maria{/b}, capisce?"
    anon "Yes, sir."
    show tony with dissolve:
        unflip
        xoffset -400
    tony "Just teach him the basics, and then roll out a dozen or so pies before movin' to the counter."
    tony "I'll be back in the blink of an eye, alright?"
    maria f_normal "Yeah, yeah..."
    maria "Just gimme a kiss and get out of here, ya big galoot!"
    show tony b_dressed_kiss
    hide maria
    with dissolve
    pause
    show tony b_dressed
    show maria behind counter:
        flip
        xoffset -200
    with dissolve
    maria "Bring me back some good news!"
    tony @ f_smirk_wink "You got it, darlin'."
    maria "C'mon, kid."
    hide maria with {'master': dissolve}
    maria "Follow me."
    hide anon with dissolve
    return

label ano06_coax_pizzeria_interior:
    call tony_button_stage
    show anon with dissolve:
        flip
    tony @ a_fists "Hey there, champ."
    anon "Hey, {b}Tony{/b}."
    anon "Feeling better today?"
    tony @ a_heart "Ahh, yeah."
    tony "I'm fine."
    tony "Sorry for makin' a scene last time."
    anon "It's no problem."
    pause
    anon "You mind if I ask what happened?"
    tony @ f_laugh a_belly "Heh, I'd be surprised if you didn't!"
    tony @ a_point_back "Long story short, I've been tryin' to get {b}Maria{/b} pregnant for over a year now..."
    tony "... And I found out yesterday that our odds ain't exactly good."
    anon f_worried "Oh?"
    tony f_sad_down "More accurately, they're nonexistant."
    anon "How come?"
    tony f_sad @ a_finger_up "Well, my batter's expired."
    anon f_confused "Huh?"
    tony a_belly "My milk's turned sour."
    anon @ -m_talk "..."
    tony a_idle @ a_point "My gun's shootin' blanks."
    anon "I have no idea what you're talking about..."
    tony f_suspicious @ f_eyeroll a_frustrated "Jesus, champ."
    tony @ a_whisper "My semen doesn't have any sperm!"
    pause
    anon f_worried @ f_brag_closed a_facepalm "O-oh!"
    anon "That sucks, {b}Tony{/b}..."
    anon "I'm so sorry."
    tony f_sad "Yeah, thanks, champ."
    pause
    tony @ a_wave "Of course, there ain't nobody to blame but myself... Waitin' all these years."
    tony f_normal "I shoulda knocked her up the second I married her."
    tony "It just never seemed like the right time, you know?"
    anon "I just kinda figured you guys already had kids..."
    tony @ f_smirk_wink "Well, I might have a couple floatin' around out there somewhere."
    show anon f_normal
    tony "I was kinda open for business back in my younger days, if you know what I mean?"
    pause
    tony "But {b}Maria{/b} and I were always real careful."
    tony "Our life back in Brooklyn just wasn't very kid-friendly..."
    tony "Now that we're out of that life, and here in Summerville..."
    tony f_sad_down "Man, I really wanted to start a family."
    anon "There's other ways to start a family, {b}Tony{/b}."
    tony "Yeah, that's what {b}Maria{/b} keeps sayin'."
    tony "She wants to try adoptin' but I just don't know..."
    tony "It kinda weirds me out, thinkin' about raisin' a stranger's kid."
    anon f_worried @ -m_talk "..."
    tony f_suspicious "Anyways, it ain't nothin' for you to worry about, champ."
    tony @ a_pizza "I need you focused on deliverin' pizzas, eh?"
    tony "Pretty soon, you're gonna want to upgrade that scooter into something flashier..."
    anon f_surprised "I am?"
    tony f_normal "Of course!"
    tony @ f_smirk_wink "You ain't gonna make many panties drop ridin' around on that thing, I can tell you that."
    pause
    tony "So you'd better start savin' up again, capisce?"
    anon f_normal "Alright, {b}Tony{/b}."
    tony @ a_frustrated "Attaboy!"
    tony "Best get started now, eh?"
    anon @ f_brag_closed a_salute "Yes, sir."
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
