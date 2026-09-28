label nad01_meet_warehouse_depot:
    scene expression background(400, 480, 1.5, b=.85) as stage:
        align (1., .5)
        zoom 2
    show anon a_surprised with {'master': dissolve}
    anon "Whoa, they aren't messing around..."
    anon "... That's a ton of vodka!"
    show anon a_sides with {'master': dissolve}
    jab "Ah, you come!"
    show anon f_confused with {'master': dissolve}:
        xoffset -500
        xzoom -1
    anon @ -m_talk "Hmm?"
    show layer master:
        ease 1. xpos 500
    show anon f_surprised
    show thug f_happy:
        xoffset -500
        xzoom -1
    jab "{b}Miss Chernyshevsky{/b} will be pleased."
    anon "Yeah, I'm here."
    anon f_skeptical a_crossed "This had better be on the up and up."
    jab a_defensive "Hey, relax... we are legitimate business now."
    anon f_normal a_sides "Where's she at?"
    jab f_confused a_sides @ -m_talk "Hmm?"
    anon "Your boss."
    jab f_normal "Oh, yes... of course."
    jab "She is taking {b}Katya{/b} to office for business talkings."
    anon f_confused "{b}Katya{/b}?"
    show anon f_thinking a_thinking with dissolve
    pause
    show anon f_normal a_sides with {'master': dissolve}
    anon "That name sounds familiar."
    jab "Yes, she used to be sex slave."
    jab f_smirk a_boobs "Tits like firm melons." (show_native="Sis'ki like firm melons.")
    show anon f_confused
    jab f_laugh "Very nice."
    anon f_grumpy a_facepalm "Please, don't do that."
    jab a_sides f_happy "Hey, c'mon... is no problem."
    show anon f_unimpressed
    jab f_normal "She is business consultant now."
    anon f_confused a_sides "Huh."
    pause
    anon "Well, good for her I guess..."
    anon "... Do I just go up?"
    jab "Da."
    jab "She will be happy to see you."
    anon "Alright."
    hide anon
    show thug a_wave f_happy
    with {'master': dissolve}
    jab "Farewell, friend." (show_native="Do svidaniya, comrade {b}[firstname]{/b}.")
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
