label iwanka_button_bed:
    show anon b_onbed_back f_shy with dissolve:
        offset (-100, 20)
    iwanka "{i}*Yawn*{/i} Good morning, {b}[firstname]{/b}."
    anon "Good morning."
    iwanka f_smirk "You're here early..."
    anon f_flirt "Yeah, I guess."
    iwanka f_annoyed "My mother isn't overworking you, is she?"

    menu iwanka_button_bed.choice:
        "No, it's fine.":
            jump iwanka_button_bed.mother
        "You're naked.":

            jump iwanka_button_bed.naked
        "About your father...":

            jump iwanka_button_bed.father
        "Blowjob.":

            jump iwanka_button_bed.blowjob
        "Sex.":

            jump iwanka_button_bed.sex
        "I can't stay.":

            pass

    anon f_normal "I can't stay."
    iwanka f_pouting "Wait, you're leaving already?!"
    anon "Yeah, sorry..."
    iwanka "But I was totally gonna jump your bone!"
    anon "Maybe next time."
    iwanka f_sad "Aww..."
    hide anon with dissolve
    return


label iwanka_button_bed.blowjob:
    anon f_normal "Mind giving me a blowjob?"
    iwanka f_smirk "A blowjob?"
    iwanka "Alright, I suppose that's fair after all you've done for me."
    show anon f_flirt
    show iwanka b_naked:
        reset
        offset (0, 0)
    with slowdissolve
    pause
    iwanka "Heh, why are you staring at me like that?"
    anon @ -m_talk "Hmm?"
    anon f_shy "N-nothing, I just-"
    pause
    anon f_flirt "You're really sexy."
    iwanka @ f_eyeroll "Umm, duh."
    iwanka a_hip "Are we doing this or what?"
    anon "Yes, please."
    iwanka "Then move nearer to the edge of the bed."
    anon "Y-yeah, okay."

    call scene_iwanka_blowjob.bedroom
    $ unlock_scene('iwanka', '01_unlocked', variant='bedroom')

    scene expression background(288, 368, 3.5) as stage
    show iwanka b_magic o_cum f_smirk
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


label iwanka_button_bed.father:
    anon f_worried "About your father."
    iwanka f_excited @ f_laugh "Oh em gee, it's been so awesome having him gone!"
    iwanka "I can basically do whatever I want now!"
    show iwanka f_smirk
    pause
    show anon f_shy
    iwanka "Speaking of which..."
    iwanka "... I was thinking you and I should take a trip somewhere!"
    anon "Oh?"
    iwanka "Have you ever been to France?"
    anon f_surprised "France?!"
    iwanka "Yeah, it's supposed to be like SUPER romantic there!"
    anon "I can't go to France!"
    iwanka "Why not?"
    iwanka "I'll pay for everything and we can totally go shopping and get you a whole new wardrobe."
    anon f_worried @ -m_talk "..."
    iwanka "If you're gonna be my boyfriend, you have to look the part."
    jump iwanka_button_bed.choice


label iwanka_button_bed.mother:
    anon f_normal "No, it's fine."
    iwanka f_smirk "Heh, your job is mostly just fucking her nowadays, huh?"
    anon f_worried "Ehh, yeah... You could say that."
    iwanka f_disgusted "Gross."
    pause
    iwanka "Well, at least it keeps her out of my hair."
    iwanka f_smirk "Just try not to break her hip, huh?"
    jump iwanka_button_bed.choice


label iwanka_button_bed.naked:
    anon f_shy "You're naked."
    iwanka f_smirk "Yeah, well..."
    iwanka "I figure my mother is doing it so why not me too?"
    iwanka "I'm not gonna let her have all the fun."
    anon @ a_take "Hey, I'm not complaining."
    jump iwanka_button_bed.choice

label iwanka_button_bed.sex:
    anon f_flirt "Want to do it?"
    iwanka f_excited @ f_laugh "Oh, definitely!"
    show iwanka f_lipbite
    show anon b_dressed_changing3 f_flirt:
        align (0., 1.)
        offset (-80, 0)
        zoom 1.05
    with dissolve
    pause
    show iwanka f_smirk_down
    show anon b_dressed_changing2
    with dissolve
    pause
    show anon b_naked_undress_bottom with dissolve
    pause
    show iwanka f_lipbite
    show anon b_naked od_naked_dick1
    with dissolve
    pause
    iwanka f_excited "Just make sure you really fuck me hard this time!"
    iwanka "And maybe choke me a little."
    anon f_surprised "Huh?!"
    iwanka "C'mon!"

    call scene_iwanka_sex.bedroom
    $ unlock_scene('iwanka', '02_unlocked', variant='bedroom')

    scene location_rump_iwanka_bed_closeup
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
    iwanka "I bet my mother doesn't fuck like that..."
    anon @ f_laugh "No, she does not."
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

    scene expression background(288, 368, 3.5, o=1) as stage
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
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
