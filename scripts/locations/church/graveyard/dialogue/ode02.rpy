label ode02_init_church_graveyard:
    scene expression background(768, 456, 3) as stage
    show shower_steam as fog at Transform(alpha=.3)
    show anon f_surprised_teeth behind fog at flip with dissolve
    anon "(Hmm?)"

    anon a_cold f_hurt "( Why did it get so cold all of a sudden? )"

    show anon f_worried_left
    pause
    anon f_worried_low @ -m_talk "( And what's with all the fog? )"

    anon @ -m_talk "( It wasn't like this a minute ago... )"

    anon f_worried_left "{b}Odette{/b}?!"

    anon "Are you out there?!"

    pause
    anon f_worried @ -m_talk "( I guess not... )"

    pause
    anon "Right, well... This is super creepy and you're not here so..."

    anon "... I'm just gonna leave, okay?"

    "{i}*Tap* *Tap* *Tap*{/i}"

    anon f_surprised_teeth a_up @ -m_talk "( !!! )"
    anon a_surprised_up @ -m_talk "( What the hell was that?! )"

    "{i}*Tap* *Tap* *Tap*{/i}"

    show anon a_surprised_shoulders f_surprised with fastdissolve:
        unflip
        xoffset 500
    anon "C'mon, {b}Odette{/b}... Stop playing around!"

    anon a_surprised "This isn't funny, you know?!"

    "{i}*Tap* *Tap* *Tap*{/i}"

    show anon a_surprised_up_both with fastdissolve:
        flip
        xoffset 0
    anon @ -m_talk "( Aww, man... )"

    anon a_sides f_skeptical @ -m_talk "( Huh? )"

    anon @ -m_talk "( What is that glowing? )"

    show anon a_cold f_worried with {'master': dissolve}:
        xoffset -450
    anon "{b}Odette{/b}?"

    hide anon with dissolve
    return


label ode02_find_crypt:
    scene
    show screen church_graveyard_crypt(_layer='master')
    "..."
    anon "( Could {b}Odette{/b} be down there? )"

    "{i}*Tap* *Tap* *Tap*{/i}" with hpunch
    anon "( !!! )"
    anon "( Jesus christ, that made me jump! )"

    anon "( It's like someone is banging on this door from the other side!! )"

    anon "Y-yeah, very funny {b}Odette{/b}..."

    anon "... If you're trying to scare me, it's not going to work!"

    "..."
    anon "Why don't you just come out of there and we'll talk?"

    "..."
    anon "Tidak?"

    "..."
    anon "Alright then, I'm coming in!"


    call screen empty()

    if _return:
        jump ode02_find_crypt.nope

    anon "Ah hah!!"

    pause
    anon "Hmm..."

    anon "( There's nobody here. )"

    anon "... {b}Odette{/b}?"

    pause
    anon "This isn't funny, you know?!"

    "Hehehehe!"

    anon "( !!! )"
    anon "Aduh, bung..."


    call screen empty()

    if _return:
        jump ode02_find_crypt.nope

    jump ode02_find_crypt.next


label ode02_find_crypt.next:
    anon "( This is such a bad idea... )"

    anon "( ... I'm going to get eaten by zombies for sure! )"


    scene location_crypt_entrance_cutscene
    show text _ ("After a few minutes of indecision, I finally gathered my courage and willed my legs into motion.") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("The passageway was dark and the air was stale.") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("You could just barely detect the faint smell of decay, masked heavily by incense and smoke.") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("Who in the heck could be down there?!") as caption with dissolve
    pause

    scene black with dissolve
    return 'enter'


label ode02_find_crypt.nope:
    anon "Tidak."

    anon "Not doing it."


    scene expression background(392, 520, 8) as stage
    show anon f_worried_low:
        xoffset 100
    with fade
    anon "I've seen this movie and it does not end well for the guy who goes down into the creepy crypt!"

    "Hehehehe!"

    show anon f_surprised_low a_sides with fastdissolve
    anon @ -m_talk "( !!! )"
    anon "NOPE!"

    show anon f_surprised with {'master': dissolve}:
        flip
        xoffset -500
    anon "Nope, nope, nope."

    show anon f_worried_low a_whisper_back with {'master': dissolve}:
        unflip
        xoffset 0
    anon "Good luck, {b}Odette{/b}!"

    show anon f_surprised_low a_point_back with {'master': dissolve}
    anon "{b}[firstname]{/b} out."

    show anon a_surprised f_worried with dissolve:
        flip
        xoffset -600
    hide anon with fastdissolve
    return


label ode02_fear_crypt:
    scene
    show screen church_graveyard_crypt(_layer='master')
    anon "( I {i}REALLY{/i} don't wanna go down there... )"


    call screen empty()

    if _return:
        jump ode02_find_crypt.nope

    "Hehehehe!"

    anon "( !!! )"
    anon "Aduh, bung..."


    call screen empty()

    if _return:
        jump ode02_find_crypt.nope

    jump ode02_find_crypt.next


label ode02_warn_crypt:
    scene expression background(392, 520, 8) as stage
    show anon f_worried_low with dissolve:
        xoffset 100
    anon @ -m_talk "( Nah. )"

    anon @ -m_talk "( I'm steering clear of that crypt until I figure this {b}Odette{/b} vampire thing out... )"

    anon @ -m_talk "( Let's go and {b}speak with Eve and her sister{/b} to see what they know. )"

    hide anon with dissolve
    return


label ode02_wake_church_graveyard:
    scene black
    pause
    anon "Tidak."

    pause

    scene location_graveyard_wakeup_cutscene01 with sliteyeopen
    pause
    anon "Ugh, man..."

    anon "... Apa yang telah terjadi?"


    scene black with sliteyeshut
    pause 0.25

    scene location_graveyard_wakeup_cutscene03 with wideeyeopen
    pause

    scene location_graveyard_wakeup_cutscene04 with dissolve
    pause

    scene location_graveyard_ground_day
    show anon b_laying_ground f_tired
    with dissolve
    pause
    anon "Dimana saya?"

    pause
    anon "The graveyard?"

    anon f_worried "What the hell happened last night?!"

    pause
    anon f_thinking "I remember coming here to see {b}Odette{/b}..."

    anon "... But then she wasn't here, and there was this glowing door..."

    anon "... And a creepy banging sound... And then..."

    anon f_worried "... And then..."

    anon f_surprised "!!!"
    show anon a_rub with fastdissolve
    pause
    anon f_skeptical "I could have sworn she-"

    pause
    anon f_surprised "{b}Odette{/b}... She's a vampire?!"

    anon f_worried "My neck is sore but I don't feel any bite marks..."

    anon "Did that really happen?!"

    show anon f_surprised_left
    pause .3
    anon f_surprised "Ini adalah-"

    anon "I've gotta-"

    anon f_worried a_idle "What do I do?!"

    pause
    anon "Maybe {b}I should speak with Eve and her sister{/b} about this?"

    anon "If this is legit, they should know about it..."


    scene black with fade
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
