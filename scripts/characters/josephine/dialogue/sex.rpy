label josie_button_sex:
    if game.timer.is_day():
        jump josie_button_sex.morning

    jump josie_button_sex.evening
    return


label josie_button_sex.morning:
    scene expression background(496, 384, 2.75) as stage
    show josephine b_naked a_phone f_normal_down:
        flip
        xoffset 150
    show anon with dissolve:
        flip
    josephine @ -m_talk "..."
    anon "Wow, you're just hanging out in here naked, huh?"
    josephine f_sexy "Heh, shut up and get those pants off."
    anon "Alright."
    show anon b_flour f_looking_down with dissolve:
        yoffset 110
    pause
    show anon b_shirt od_dick4 f_normal with dissolve:
        yoffset 0
    josephine f_sexy_down "You know, I'm starting to think this job isn't so bad..."
    anon "Heh, is that right?"
    hide josephine with dissolve
    josephine "Ready when you are, bowl cut."
    anon f_unimpressed "Stop calling me that!!"
    hide anon with {'master': dissolve}
    josephine "Hehe!"

    call scene_josie_sex.morning
    $ unlock_scene('josie', '02_unlocked', variant='morning')

    scene expression background(496, 384, 2.75) as stage
    show anon b_flour f_looking_down:
        flip
        yoffset 110
    show josephine b_naked a_phone f_normal_down:
        flip
        xoffset 150
    with fade
    josephine @ -m_talk "..."
    show anon b_dressed f_unimpressed with dissolve:
        yoffset 0
    anon "And you're back on the phone again..."
    josephine f_concerned "What, we're done, aren't we?"
    anon "Yeah, I suppose."
    show josephine f_normal_down
    pause
    josephine f_sexy "I'm telling them I just had sex in the break room at work..."
    anon f_surprised "Really?"
    josephine "Hehe, yeah."
    josephine "They are totes jealous right now."
    show anon f_normal
    pause
    anon "I'll see you later, {b}Josephine{/b}."
    josephine "See ya, {b}[firstname]{/b}."
    hide anon with dissolve
    return 'afterglow'


label josie_button_sex.evening:
    scene josephine b_chair f_sexy
    anon "!!!"
    josephine "See something you like?"
    anon "Wow, you're sexy!"
    josephine @ f_laugh "Hehe!"
    josephine "Not so worried now, huh?"
    anon "..."
    josephine "C'mon, I want to ride you on my father's desk..."
    anon "O-okay."

    call scene_josie_sex_desk.repeat
    $ unlock_scene('josie', '04_unlocked')

    if _return == 'inside':
        jump josie_button_sex.inside
    if _return == 'outside':
        jump josie_button_sex.outside

    scene expression background(712, 400, 3.) as stage
    show anon b_flour f_looking_down:
        flip
        offset (-50, 110)
    show josephine b_naked f_sexy:
        flip
        xoffset 150
    with fade
    josephine @ -m_talk "..."
    show anon b_dressed f_worried with dissolve:
        yoffset 0
    anon "Where's your phone?"
    josephine @ -m_talk "Hmm?"
    josephine "Oh, I don't know..."
    josephine @ f_eyeroll "... Who cares?"
    pause
    anon @ f_confused "Are you feeling okay?"
    josephine "Mmm, I feel wonderful."
    josephine "We should do this more often..."
    anon f_normal "Heh, I'd be down for that."
    show josephine b_naked_kiss:
        xoffset 200
    hide anon
    with dissolve
    pause
    show josephine b_naked:
        xoffset 150
    show anon b_dressed:
        flip
        xoffset -50
    with dissolve
    josephine "It's a date then."
    anon "Heh."
    hide anon with dissolve
    return 'afterglow'


label josie_button_sex.inside:
    scene expression background(712, 400, 3.) as stage
    show anon b_flour f_looking_down:
        flip
        offset (-50, 110)
    show josephine a_phone b_naked f_angry_down:
        flip
        xoffset 150
    with fade
    josephine "Tsk, those motherfuckers!"
    show anon a_sides b_dressed f_worried:
        yoffset 0
    with {'master': dissolve}
    anon "Uh oh, what now?"
    josephine "I was just informed they upped the employee discount to fifteen percent!"
    anon f_confused "That's pretty good, isn't it?"
    josephine f_annoyed "Really good."
    pause
    josephine "Too bad I don't fucking work there anymore!"
    show anon f_worried
    show josephine f_angry_down
    pause
    show anon a_shy_neck f_worried_back_low
    with {'master': dissolve}
    anon "Well, that's a shame."
    pause
    show anon f_worried
    show josephine f_bored_down
    with {'master': dissolve}
    pause
    show anon a_sides
    with {'master': dissolve}
    anon "Anyways, I'll catch you later..."
    show anon a_wave f_shy
    with {'master': dissolve}
    anon "... Bye!"
    josephine "Yeah, yeah."
    hide anon with dissolve
    josephine f_eyeroll "{i}*Sigh*{/i} Stupid car dealership with my stupid father."
    return 'afterglow'


label josie_button_sex.outside:
    scene expression background(712, 400, 3.) as stage
    show anon b_flour f_looking_down:
        offset (-50, 110)
        xzoom -1
    show josephine a_hips b_naked f_angry_down:
        xoffset -450
    with fade
    josephine "Where the hell did my phone go?"
    show anon a_sides b_dressed f_confused:
        yoffset 0
    with {'master': dissolve}
    anon "What do you mean?"
    show anon f_worried
    show josephine a_sides f_confused:
        xoffset 150
        xzoom -1
    with {'master': dissolve}
    josephine "What do you think I mean?!"
    show josephine a_gimme f_annoyed
    with {'master': dissolve}
    josephine "It's completely vanished!"
    show anon f_confused
    show josephine a_sides
    with {'master': dissolve}
    anon "How did you lose it?"
    josephine f_eyeroll "Oh, I dunno..."
    josephine f_annoyed "... It probably had something to do with you unceremoniously tossing me off your dick like I was a fucking rag doll!"
    show anon a_behind_head f_shy
    with {'master': dissolve}
    anon "Heh, I kinda did do that, didn't I?"
    show josephine a_crossed f_angry
    with {'master': dissolve}
    pause
    show anon a_sides f_worried
    with {'master': dissolve}
    anon "Well, I'm sorry..."
    show josephine f_eyeroll
    anon f_shy "... The kettle was about to boil over and I had to think quickly!"
    show anon f_shy_low
    hide josephine
    with {'master': dissolve}
    josephine "Did it roll under the bookshelf or something?!"
    anon f_confused_low "Maybe?"
    pause
    josephine "No, it's not there either."
    show anon f_surprised:
        xoffset -500
    with {'master': dissolve}
    anon "Geez, is that the time?!"
    show anon:
        xoffset 0
        xzoom 1
    with {'master': dissolve}
    anon f_worried_low "You know, I'd really love to stay and help you look but it's getting awful late..."
    show anon f_worried
    show josephine a_hips b_naked f_angry_down:
        xoffset 500
        xzoom -1
    with {'master': dissolve}
    anon "... And I wouldn't want my landlady to start worrying, so..."
    show anon f_surprised:
        xoffset -100
    show josephine a_frustrated
    with {'master': dissolve}
    josephine @ f_angry_closed "Grr, it's not anywhere!!"
    pause
    show anon a_wave f_shy
    show josephine a_sides
    with {'master': dissolve}
    anon "... Ok, bye!"
    hide anon with dissolve
    show josephine a_hips f_pouting
    with {'master': dissolve}
    josephine "I'm gonna have to fucking call it!"
    return 'afterglow'
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
