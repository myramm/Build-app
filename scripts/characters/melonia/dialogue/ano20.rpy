label ano20_init_melonia_guards:
    anon f_worried "Can you help with the guards?"
    melonia f_normal "Is it time?"
    anon "Yes, please."
    melonia f_smirk "I can't wait to see his stupid face once he realizes he's been robbed!"
    show anon f_normal
    melonia "Just make sure to stay out of sight until I've sent the guards away."
    anon "Of course."
    melonia @ f_laugh "Heh, this is going to be fun!"
    hide melonia
    show anon:
        flip
        xoffset -500
    with dissolve
    pause
    anon f_worried "Wow, you're really enjoying this..."
    hide anon with dissolve

    scene expression background(480, 432, 4.5, l=L_rump_lobby) as stage
    show bodyguard:
        xoffset -600
    with fade
    bodyguard "{i}*Sigh*{/i} Night shift is the worst..."
    melonia "Hey, meathead!"
    show melonia f_smirk
    show bodyguard f_suspicious:
        flip
        xoffset 0
    with dissolve
    bodyguard @ -m_talk "Hmm?"
    bodyguard f_surprised "{b}Mrs. Rump{/b}?"
    bodyguard "What are you doing here?"
    melonia @ f_eyeroll "I live here, dumbass..."
    bodyguard "R-right, of course... I meant-"
    melonia "{i}*Ahem*{/i} Yeah, I know what you mean."
    melonia "Listen, your services are no longer needed here tonight."
    bodyguard "I'm sorry?"
    melonia "My husband and I are having important guests over and we don't need a bunch of goons in cheap suits leering and making them feel uncomfortable."
    bodyguard f_normal "Oh, I dunno, ma'am..."
    bodyguard "I have very strict orders to-"
    melonia f_annoyed "Excuse me?"
    melonia "I give the orders around here or have you forgotten?!"
    bodyguard f_surprised a_defensive "{i}*Gulp*{/i} N-no, of course not!"
    melonia "You have until the count of ten to get out of my sight or I swear, I'll have you scrubbing toilets in Guantanamo Bay before the end of the week!"
    bodyguard a_wave "That's not necessary, I-"
    melonia f_yell "ONE!"
    bodyguard a_defensive "Ma'am, please, if you would just let me-"
    melonia "TWO!"
    bodyguard "The mayor will-"
    melonia "FIVE!!"
    bodyguard "What happened to three and four?!"
    melonia "SEVEN!!!"
    bodyguard "Eep!"
    hide bodyguard with fastdissolve
    melonia f_smirk "Hmph, moron..."
    pause
    show melonia f_smirk_up with dissolve:
        flip
        xoffset 200
    melonia "You can come out now."
    show anon f_worried:
        flip
    show melonia f_smirk
    with dissolve
    anon "Wow, that was umm..."
    melonia "Impressive?"
    anon "I was gonna say scary but sure, let's go with impressive."
    melonia @ f_laugh "Hah!"
    melonia "Well, it worked, didn't it?"
    melonia "You should have the office all to yourself for a few hours at least..."
    anon f_normal "I shouldn't need that long."
    melonia "Oh."
    melonia "Well, feel free to break some stuff, if you'd like."
    anon "Ehh, yeah... Maybe."
    melonia "I'll be upstairs in bed if you get bored."
    melonia "I sleep naked by the way..."
    show melonia f_smirk_lipbite
    anon f_surprised @ -m_talk "!!!"
    melonia f_smirk "Just some food for thought."
    hide melonia
    show anon:
        unflip
        xoffset 500
    with dissolve
    melonia "Have fun!"
    show anon f_surprised_high
    pause
    show anon f_grin with {'master': dissolve}:
        flip
        xoffset 0
    anon f_grin @ -m_talk "( Hmm, naked {b}Melonia{/b}... )"
    anon f_flirt @ -m_talk "( You know, a few hours is a long time... Maybe I could just- )"
    pause
    anon f_hurt @ -m_talk "( NO! NO! NO! )"
    anon @ -m_talk "( C'mon, {b}[firstname]{/b}, focus! )"
    anon f_angry @ -m_talk "( I'm here for evidence and to get justice for {b}Dad{/b}. )"
    anon @ -m_talk "( Let's {b}get in there and find it{/b}! )"
    hide anon with dissolve

    $ player.go_to(L_rump_lobby)
    $ L_rump_office.unlock()
    $ M_anon.trigger(T_ano20_init)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
