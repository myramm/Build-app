label iwanka_button_yacht:
    show anon b_onbed_back with dissolve:
        flip
        offset (100, 110)
    iwanka "Hey, you made it!"
    show iwanka f_excited
    anon "Yup."
    iwanka "Pull up a chair."
    iwanka "Fix yourself a drink."
    pause
    iwanka f_smirk "Unless you're ready to move onto a more vigorous activity?"

    menu iwanka_button_yacht.choice:
        "You look really sexy...":
            jump iwanka_button_yacht.sexy
        "This yacht is awesome!":

            jump iwanka_button_yacht.yacht
        "Blowjob.":

            jump iwanka_button_yacht.blowjob
        "Sex.":

            jump iwanka_button_yacht.suggest
        "I can't stay.":

            pass

    anon f_normal "I can't stay."
    iwanka f_pouting "Wait, you're leaving already?!"
    anon "Yeah, sorry..."
    iwanka "But I was totally gonna jump your bones!"
    anon "Maybe next time."
    iwanka f_sad "Aww..."
    hide anon with dissolve
    return


label iwanka_button_yacht.blowjob:
    anon f_normal "Mind giving me a blowjob?"
    iwanka f_smirk "A blowjob?"
    iwanka "Alright, I suppose that's fair after all you've done for me."
    hide iwanka with dissolve
    show anon f_flirt_grin with {'master': dissolve}:
        unflip
        xoffset 650
    iwanka "Come on then!"
    hide anon with {'master': fastdissolve}
    anon "Right behind you!"

    scene expression background(512, 344, 3, l=L_boat_cabin) as stage
    show iwanka b_magic f_smirk
    with fade
    show anon f_flirt with dissolve
    if M_iwanka.outfit.get == 'swimsuit':
        show iwanka a_undress b_swimsuit with dissolve
        pause
        show anon f_flirt_low
        show iwanka b_swimsuit_undress2
        with dissolve
        pause
        show iwanka b_naked a_undress_swimsuit3 with dissolve
        pause
        show anon f_flirt
        show iwanka b_naked a_idle
        with dissolve
    else:
        show iwanka b_naked
    iwanka "Heh, why are you staring at me like that?"
    anon @ -m_talk "Hmm?"
    anon f_shy "N-nothing, I just-"
    pause
    anon f_flirt "You're really sexy."
    iwanka @ f_eyeroll "Umm, duh."
    iwanka a_hip "Are we doing this or what?"
    anon "Yes, please."
    iwanka "Then have a seat."
    anon "Y-yeah, okay."

    call scene_iwanka_blowjob.yacht
    $ unlock_scene('iwanka', '01_unlocked', variant='yacht')

    scene expression background(512, 344, 3, l=L_boat_cabin) as stage
    show iwanka b_naked o_cum f_smirk
    show anon f_flirt
    with fade
    anon "Thank you, for doing that."
    iwanka "No problem."
    iwanka @ f_laugh "It was fun!"
    pause
    iwanka "Now, if you'll excuse me..."
    iwanka "... I'm gonna go clean myself up."
    anon "Y-yeah, sure."
    anon @ a_wave "See ya later."
    iwanka "See ya, {b}[firstname]{/b}."
    hide anon with dissolve
    return 'afterglow'


label iwanka_button_yacht.sex:
    iwanka f_excited @ f_laugh "Oh, definitely!"
    hide iwanka with dissolve
    show anon f_surprised with {'master': dissolve}:
        unflip
        xoffset 650
    iwanka "What are you waiting for? An invitation?"
    hide anon with {'master': fastdissolve}
    anon "!!!"

    scene expression background(240, 344, 3, l=L_boat_cabin) as stage
    show iwanka b_magic f_smirk
    with fade
    show anon f_flirt with dissolve
    show iwanka b_swimsuit a_undress f_smirk_down
    show anon b_dressed_changing3
    with dissolve
    pause
    show iwanka b_swimsuit_undress2
    show anon b_dressed_changing2
    with dissolve
    pause
    show iwanka b_naked a_undress_swimsuit3
    show anon b_naked_undress_bottom
    with dissolve
    pause
    show iwanka b_naked a_hip f_smirk
    show anon b_naked od_naked_dick1
    with dissolve
    iwanka "Just make sure you really fuck me hard this time!"
    iwanka "And maybe choke me a little."
    anon f_surprised "Huh?!"
    show anon b_empty od_empty:
        xoffset 300
        unflip
    show iwanka b_naked_pulling_anon behind anon:
        unflip
        xoffset 300
    with dissolve
    iwanka "C'mon!"
    anon "W-whoa, wait a second!"

    call scene_iwanka_sex.yacht
    $ unlock_scene('iwanka', '02_unlocked', variant='yacht')

    scene location_boat_interior_bed_closeup
    show iwanka b_onbed_cuddle_naked f_content_closed
    show anon b_empty f_flirt_low:
        xzoom -1
        offset (84, -17)
    show anon_overlay_dick_onbed_naked_od_dick1
    with fade
    iwanka "Mmm, well done!"
    anon "Y-yeah, you too."
    pause
    show iwanka f_excited_up
    iwanka "I bet you're glad you came out here now, huh?"
    anon "Yes, very glad!"
    iwanka @ f_laugh "Hehe!"
    iwanka f_content_closed "You know, you can hang out awhile..."
    iwanka "... If you want."
    anon "Oh?"
    iwanka "Yeah, I like laying here with you."
    iwanka "It's umm, I dunno..."
    anon "Nice?"
    iwanka @ f_excited_up "... Yeah."
    iwanka "Nice."
    anon "Alright, but only for a little bit."
    iwanka "Mm, okay."
    pause
    iwanka "Thanks, {b}[firstname]{/b}."

    scene expression background(512, 344, 3, l=L_boat_cabin, o=1) as stage
    show anon
    show iwanka b_naked f_excited
    with slowfade
    iwanka "That was fun!"
    anon "Yeah, it was."
    hide anon
    show iwanka b_naked_kiss:
        xoffset -200
    with dissolve
    pause
    show iwanka b_naked:
        xoffset 0
    show anon f_shy
    with dissolve
    iwanka "Let's do it again soon, okay?"
    anon "Definitely."
    hide anon with dissolve
    return 'afterglow'


label iwanka_button_yacht.sexy:
    anon f_flirt "You look really sexy..."
    iwanka f_smirk "Well, I should hope so!"
    iwanka "After all the money my father spent on my plastic surgeries..."
    anon f_surprised_low "You've had plastic surgeries?!"
    iwanka "Three times."
    pause
    iwanka @ f_thinking "Hmm, four if you count my boobs."
    anon "You seem way too young for all that!"
    iwanka "You're never too young to visually enhance yourself."
    show anon f_worried_low
    pause
    iwanka "At least, that's what my father's plastic surgeon says..."
    jump iwanka_button_yacht.choice


label iwanka_button_yacht.suggest:
    anon f_flirt "Want to do it?"

    if game.timer.is_evening():
        jump iwanka_button_yacht.sex

    iwanka "I'm kinda sunbathing right now... But maybe later, okay?"
    show anon f_sad
    pause
    jump iwanka_button_yacht.choice


label iwanka_button_yacht.yacht:
    anon f_normal "This yacht is awesome!"
    iwanka f_normal "Right?!"
    iwanka f_excited "I love being out here on the ocean."
    iwanka @ f_laugh "Plus it's got wifi and satellite TV."
    anon @ f_surprised "Holy crap, really?"
    iwanka "Yeah, my dad dumped more money into pimping this thing out than the boat itself."
    anon "That's nuts!"
    iwanka "State-of-the-art security system, luxury furniture, heated decks, a fully stocked bar, built-in theater quality custom audio..."
    iwanka "... And there's a stripper pole around here somewhere."
    anon f_surprised "Really?"
    anon f_flirt "I would like that!"
    iwanka @ f_laugh "Hehe, I bet you would."
    jump iwanka_button_yacht.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
