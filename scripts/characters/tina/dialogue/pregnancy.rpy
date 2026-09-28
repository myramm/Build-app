label tina_pregnancy_notify:
    scene expression player.location.background
    "{i}*Brrrzzzt* *Brrrzzzt*{/i}"

    scene expression background(808, 400, 2.4, l=L_tina_lounge) as underlay:
        xoffset -400
    show tina a_phone:
        xoffset -500

    $ renpy.dynamic(stage=player.location.background_phone)
    show expression stage as stage
    show anon f_confused with dissolve:
        flip
    anon @ -m_talk "Hmm?"
    anon a_phone f_thinking_down "I don't recognize this number..."
    show anon a_phone_talk f_skeptical with dissolve:
        unflip
        xoffset 500
    show expression stage as stage at phoneleft with phoneleft.show
    anon "Hello?"
    tina "Hello, {b}[firstname]{/b}?"
    anon "Who is this?"
    tina "It's {b}Tina{/b}."
    anon f_surprised "!!!"
    anon f_worried "{b}Mrs. Hendicks{/b}?!"
    tina @ -m_talk "Mhmm."
    tina "I asked {b}Tony{/b} for your number... I hope you don't mind?"
    anon f_shy "N-no, not at all!"
    pause
    anon "Did you need-"
    anon "{i}*Ahem*{/i} I mean, is there something I can do for you?"
    tina f_sexy "Well, I wouldn't say no to another tumble in the sack but unfortunately, that's not the reason for my call..."
    anon "Oh?"
    tina f_normal "I'm pregnant, {b}[firstname]{/b}."
    anon f_surprised "Oh!"
    pause
    anon "Umm..."
    tina "Yeah."
    tina "I wanted you to know that I didn't plan on this happening."
    tina @ f_laugh "In fact, it shouldn't have been possible at all!"
    anon f_worried "What do you mean?"
    tina "Well, I've had the contraceptive implant for years now and nothing has ever gotten through before..."
    anon "Really?"
    tina "Either something went wrong or your sperm is magical!"
    anon @ -m_talk "..."
    tina "Regardless, I'm taking it as a sign and keeping the baby."
    anon f_normal "O-okay."
    tina "I think it will be nice to have a little one around once again."
    tina "And it's entirely your decision how involved you want to be, okay?"
    tina "No pressure."
    anon "I definitely want to be involved."
    tina "You do?"
    anon "If that's alright?"
    tina @ f_laugh "Of course, {b}[firstname]{/b}!"
    tina "I think that would be wonderful!"
    tina "Just feel free to come by anytime you'd like, okay?"
    anon "Yeah, okay."
    tina "See you soon."
    anon "B-bye, {b}Tina{/b}."
    show anon f_looking_down a_phone with dissolve
    show expression stage as stage with {'master': phoneleft.hide}
    "{i}*Beep*{/i}"
    anon @ -m_talk "( Well, that was unexpected... )"
    anon a_idle f_grin @ -m_talk "( I can't believe I'm going to have a baby with {b}Mrs. Hendicks{/b}! )"
    anon @ -m_talk "( This is so exciting! )"
    hide anon with dissolve
    return True


label tina_pregnancy_notify.repeat:
    scene expression player.location.background
    "{i}*Brrrzzzt* *Brrrzzzt*{/i}"

    scene expression background(808, 400, 2.4, l=L_tina_lounge) as underlay:
        xoffset -400
    show tina a_phone:
        xoffset -500

    $ renpy.dynamic(stage=player.location.background_phone)
    show expression stage as stage
    show anon f_confused with dissolve:
        flip
    anon @ -m_talk "Hmm?"
    anon a_phone f_worried_low "It's {b}Tina{/b}."
    show anon a_phone_talk f_normal with dissolve:
        unflip
        xoffset 500
    show expression stage as stage at phoneleft with phoneleft.show
    anon "Hello?"
    tina "Hello, {b}[firstname]{/b}?"
    anon "Yeah, it's me."
    anon "It's something wrong?"
    tina @ f_laugh "Well, it's official!"
    anon f_confused @ -m_talk "Hmm?"
    tina f_sexy "You must have magical sperm because I'm pregnant again!"
    anon f_surprised "!!!"
    anon "Again?"
    tina "I might as well get this contraceptive implant removed for all the good it does me."
    anon f_worried "Or we should stop having sex..."
    tina "Oh, now don't start getting crazy on me!"
    anon f_normal @ -m_talk "..."
    anon "I assume you're keeping it?"
    tina "Of course."
    tina "The more the merrier as far as I'm concerned."
    tina "As usual, you don't have to be-"
    anon "I want to be involved!"
    tina "Oh."
    pause
    tina @ f_laugh "Well, that's wonderful {b}[firstname]{/b}, thank you!"
    anon @ -m_talk "Mhmm."
    anon "I'll be over there to see you ASAP."
    tina "Alright."
    tina "See you soon."
    show anon f_looking_down a_phone with dissolve
    show expression stage as stage with {'master': phoneleft.hide}
    "{i}*Beep*{/i}"
    anon @ -m_talk "( Magical sperm, huh? )"
    pause
    anon a_idle f_grin @ -m_talk "( Nah, I'm sure it's just a defective implant... )"
    anon @ -m_talk "( Magic isn't a thing! )"
    hide anon with dissolve
    return True


label tina_pregnant_labor_1:
    scene expression player.location.background_blur
    show anon f_normal with dissolve
    anon "Looks like I got a text."
    hide anon with dissolve
    return


label tina_pregnant_labor_2:
    scene expression player.location.background_blur
    if player.location != L_map:
        show anon f_surprised a_phone with dissolve
    anon "{b}Tina{/b} had the baby?!"
    anon "Holy crap!"
    pause
    anon "I'd better {b}head to the hospital{/b} to check on them."
    if player.location != L_map:
        hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
