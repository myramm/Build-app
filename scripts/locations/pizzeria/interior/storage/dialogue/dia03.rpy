label dia03_stow_pizzeria_storage:

    python hide:
        if M_maria.outfit.get == 'casual':
            renpy.dynamic(M_maria=util.struct(outfit='dressed',
                                              pregnancy=M_maria.pregnancy))

    scene expression background(336, 400, 2.) as stage with None
    show anon a_milk_cartons_small
    show maria b_magic:
        flip
        xoffset 300
    with dissolve
    maria "You can put 'em in the refrigeration unit over here."
    anon "Alright."

    if M_anon.finished_state(S_ano11_bone):
        maria f_sexy "Then maybe we can have a little fun, eh?"
        maria "I know the bed ain't set up but I just can't get enou-"
    else:
        maria "It's nothing fancy but it-"

    show maria b_magic_fall with dissolve:
        unflip
        xoffset 180
    show anon f_surprised_teeth
    maria "!!!"

    if 1 <= M_maria.pregnancy.stage <= 4:
        if M_maria.pregnancy.stage >= 3:
            scene location_pizza_cutscene03
        elif M_maria.pregnancy.stage >= 2:
            scene location_pizza_cutscene05
        else:
            scene location_pizza_cutscene07
        show text _ ("{b}Maria{/b} tripped over a bag of flour and started to fall.\nDesperatly grabbing at the shelf as she went down...") as caption
        with fade
        pause

        if M_maria.pregnancy.stage >= 3:
            scene location_pizza_cutscene04
        elif M_maria.pregnancy.stage >= 2:
            scene location_pizza_cutscene06
        else:
            scene location_pizza_cutscene08
        show text _ ("My heart leapt in my chest and I dropped the milk in an instant,\nmoving as quickly as I could to try and save her.") as caption
        with fade
        pause
        hide caption with dissolve
        show text _ ("I barely managed to catch her wrist and twist her,\nwrapping my other arm under and preventing her from hitting the ground.") as caption with dissolve
        pause

        scene expression background(336, 400, 2.) as stage
        show maria b_magic_mc_hold f_sad_down:
            xoffset 50
        with fade
        maria "Oh my god..."
        anon "A-are you alright?"
        maria "Phew, that was a close one."
        tony "{b}MARIA{/b}?!"
        show tony f_suspicious behind anon:
            flip
            xoffset -68
        with dissolve
        tony "I heard screamin'!"
        tony "She alright?!"
        show anon b_dressed f_worried behind maria:
            flip
            xoffset -100
        show maria b_magic f_sad:
            xoffset 150
        with dissolve
        tony f_sad @ f_question "What happened?"
        maria f_angry "You left that damn flour sittin' out again and I tripped over it!"
        tony "I did?"
        pause
        maria "I nearly killed myself!"
        tony "I'm so sorry, darlin'!"
        pause
        tony "Is the baby okay?"
        maria "Yeah, thanks to {b}[firstname]{/b}."
        maria "Who knows what woulda happened if he hadn't been here..."
        show tony a_mc_hip_single f_eyeroll:
            xoffset -68
        show tony_arms_dressed_a_mc_shoulder_single:
            flip
            xoffset -68
        with dissolve
        tony f_normal @ f_eyeroll "Phew."
        tony "Man, I owe you one, champ."
        show anon f_normal
        show tony f_surprised
        maria "You owe him a lot more than one, {b}Tony{/b}!"
        maria "And you can start by puttin' that flour away like you're supposed to!"
        tony f_sad "Of course."
        tony "Right away, darlin'!"
        show tony b_dressed_pickup:
            xoffset -400
        hide tony_arms_dressed_a_mc_shoulder_single
        with dissolve
        pause
        show tony b_dressed a_flour f_surprised with dissolve:
            xoffset 0
        tony "Hnnggg!!"
        show anon f_normal_left
        show tony f_sad_down:
            unflip
            xoffset -550
        with dissolve
        maria f_sexy "And you..."
        hide tony
        show anon b_empty f_grin:
            unflip
            xoffset 400
        show maria b_magic_kiss_mc_cheek behind anon:
            xoffset 400
        with dissolve
        anon "!!!"
        pause
        show anon f_flirt b_dressed behind maria:
            xoffset 350
        show maria b_magic:
            xoffset 150
        with dissolve
        maria "You need anything; anything at all, you come and see me, yeah?"
        anon "O-okay."
        show tony f_sad_down behind anon:
            flip
            xoffset -118
        show anon f_normal:
            flip
            xoffset -150
        with dissolve
        maria f_angry "Now pay for the milk and put it away yourself!"
        maria "It'll be your penance for nearly killin' me."
        tony "You got it, darlin'."
        show maria behind tony with dissolve:
            xoffset -360
    else:
        hide maria with dissolve
        show anon f_surprised_low
        maria "AAAGGGHHH!!!"

        scene location_pizza_cutscene01
        show text _ ("{b}Maria{/b} tripped over a bag of flour and started to fall.\nDesperatly grabbing at the shelf as she went down...") as caption
        with fade
        pause

        scene location_pizza_cutscene02
        show text _ ("Unfortunately all she managed to do was knock a couple cans of crushed tomatoes over\nbefore tumbling head over heels into a heap on the floor.") as caption
        with fade
        pause
        hide caption with dissolve
        show text _ ("I was frozen like a deer in headlights as she lay there with her lower half exposed...") as caption with dissolve
        pause

        scene expression background(336, 400, 2.) as stage
        show anon f_worried_low
        show maria b_knees
        with fade
        maria "Tch, ow..."
        anon "A-are you alright?"
        show maria b_knees_closed
        tony "{b}MARIA{/b}?!"
        show anon f_worried_left:
            xoffset 80
        show tony f_suspicious:
            flip
            xoffset -200
        with dissolve
        tony "I heard screamin'!"
        tony "She alright?!"
        tony @ f_surprised "!!!"
        tony "Jesus, {b}Maria{/b} you're on display for the whole world to see!"
        show anon f_flirt_low
        show maria b_knees_talk with dissolve
        maria "Ahh, shuddup {b}Tony{/b}!"
        if M_anon.finished_state(S_ano11_bone):
            maria "It ain't like he hasn't seen it already!"
        else:
            maria "It ain't like I did it on purpose!"
        show anon f_worried
        show maria b_dressed a_gross o_sauce f_surprised_down:
            unflip
            xoffset 0
        with {'master': dissolve}
        maria "You're the one who keeps leaving the flour sitting out for me to trip over!{fast}"
        maria "I dunno why you can't just put things back where they belong?!"
        anon b_flour "I'll get it."
        show maria f_shy a_idle with dissolve
        tony f_suspicious "I forgot alright?!"
        show anon b_dressed a_flour f_hurt with {'master': dissolve}:
            xoffset 30
        anon "Hnnggg!!!"
        maria "See, you're makin' the kid do everything around here!"
        anon f_shy "It's alright, I don't mind."
        pause
        anon "You sure you aren't hurt?"
        maria "Yeah, I'm fine."
        tony f_normal "C'mere."
        show anon:
            xoffset 450
        show tony b_dressed_hug:
            xoffset 50
        hide maria
        with dissolve
        pause
        show anon f_normal_left with {'master': dissolve}:
            xoffset 650
        tony "I'm sorry, darlin'."
        show anon b_flour f_worried_low
        show tony b_dressed
        show maria o_sauce:
            xoffset -200
        with dissolve
        tony "I'll make sure it don't happen again."
        show anon a_sides b_dressed f_normal with {'master': dissolve}
        maria f_sexy "You better."
        show anon f_shy a_idle:
            flip
            xoffset 100
        show tony b_dressed_kiss
        hide maria
        with dissolve
        pause
        show anon f_normal
        show tony b_dressed
        show maria o_sauce:
            xoffset -200
        with dissolve
        maria "Now pay the kid and put the milk away yourself!"
        show anon f_normal
        maria "It'll be your penance for nearly killin' me."
        tony "Hah, you got it, darlin'."
    hide maria with dissolve
    show anon behind tony
    show tony f_normal a_money
    with dissolve
    tony "This should take care of the milk..."
    show tony a_idle behind anon
    show anon a_money
    with dissolve
    anon "Alright."
    show anon a_idle
    if M_maria.pregnancy:
        show tony a_mc_hip_single:
            xoffset -118
        show tony_arms_dressed_a_mc_shoulder_single:
            flip
            xoffset -118
    else:
        show tony a_mc_hip_single:
            xoffset 132
        show tony_arms_dressed_a_mc_shoulder_single:
            flip
            xoffset 132
    with dissolve
    if M_maria.pregnancy:
        tony "... And thank you, for savin' her, champ."
    else:
        tony "... And thank you, for puttin' that flour away, champ."
    anon "Yeah, no problem."
    tony "You're a good kid."
    pause
    show tony a_idle
    hide tony_arms_dressed_a_mc_shoulder_single
    with dissolve
    tony "Now run along back to your friend and give her my regards, will ya?"
    anon "Sure thing."
    anon "See ya, {b}Tony{/b}."
    hide anon with dissolve
    pause
    show tony f_suspicious with dissolve:
        unflip
        xoffset -300
    tony @ a_whisper "And don't forget, your real job is here!"
    tony "We got deliveries waitin' on ya!"
    pause
    show tony b_dressed_slumped f_sad_down with dissolve
    tony "{i}*Sigh*{/i} Alright, milk."
    tony "Let's get you in the fridge, eh?"

    scene black with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
