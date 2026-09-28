label bec01_init_tina_threshold:
    show tina b_casual
    anon "I was hoping to see {b}Becca{/b}."
    tina f_suspicious "Oh, really?"
    anon f_confused "Is that okay?"
    tina f_normal "Yes, of course... I'm just surprised is all!"
    show anon f_normal
    tina "My daughter doesn't get many visitors..."
    tina "... Well, apart from {b}Missy{/b} and that blonde girl from the trailer park."
    anon f_confused "You mean {b}Roxxy{/b}?"
    tina f_annoyed "Yeah, that's the one."
    pause
    tina "I sure wish she'd stop hanging around with that girl."
    anon f_surprised "Ehh, really?"
    show anon a_behind_head f_shy of_blush
    with {'master': dissolve}
    anon "Because she's kinda, sorta... my girlfriend."
    tina f_surprised @ -m_talk "Hmm?!"
    tina "You're kidding?"
    show anon a_sides -of_blush
    with {'master': dissolve}
    anon "No, it's the truth."
    tina f_sad "Oh, umm..."
    tina "... Sorry about that, I didn't mean any offense."
    tina "I'm sure she's a wonderful girl, I just don't like my daughter going over to that side of town."
    show anon f_worried
    tina f_annoyed "It's full of uncouth bikers and drug dealers..."
    show anon a_surprised_up_both behind tina
    with {'master': dissolve}
    anon "Yeah, no... I get it."
    tina "... And rednecks."
    show anon a_sides f_worried
    with {'master': dissolve}
    anon "{b}Roxxy{/b} isn't like that though, really."
    show tina f_suspicious
    anon f_shy "She's actually very sweet, once you get to know her."
    tina f_normal "Oh, I'm sure."
    pause
    tina "And hey, maybe now that you're working for {b}Tony{/b}, you two could get an apartment together in a better neighborhood or something?"
    anon a_shy_neck f_shy_left "Oh, ehh... I don't think we're ready for that yet."
    tina @ f_sexy "Heh, I'm sorry... just wishful thinking on my part..."
    show anon f_shy
    tina "... It's really none of my business."
    show anon a_sides
    show tina a_point_back f_normal
    with {'master': dissolve}
    tina "Come on in, babyface."
    show location_apt_hall3_301_closeup_door2 as door
    show tina a_sides:
        xzoom -1
        xoffset 515
    with {'master': dissolve}
    tina "{b}Rebecca{/b}'s in her bedroom doing homework."
    hide tina
    with {'master': dissolve}
    anon "Thanks, {b}Tina{/b}."
    hide anon
    with {'master': dissolve}
    tina "I'll be in my room if you need me."
    show location_apt_hall3_301_closeup_door1 as door
    with {'master': dissolve}
    anon "Cool."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
