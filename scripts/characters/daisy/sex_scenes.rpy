label first_time_dialogue_daisy_sex:
    scene expression "backgrounds/location_barn_sex_back_day.jpg"
    show daisy_sex_breed pre_talk
    show daisy_sex_breed_mc
    with dissolve
    daisy "Saya sangat bersemangat, {b}[firstname]{/b}!"

    player_name "Ya, saya bisa melihatnya."

    daisy "I hope your weasel will fit, it's really larg-"

    hide daisy_sex_breed_mc
    show daisy_sex_breed insert_and_pullout
    with dissolve
    pause
    show daisy_sex_breed creampie_pullout with dissolve
    pause 1
    show daisy_sex_breed creampie
    daisy "!!!" with hpunch
    daisy "Wowzers!"

    player_name "Kamu baik-baik saja?"

    daisy "Uh huh, your weasel is just really big!"

    player_name "Let me know if I hurt you, okay?"

    daisy "Oke."

    $ M_daisy.set('sex speed', 0.09)
    show expression AnimatedImage("daisy_sex_back", [1,2,3,4,5,6,7,8,9,10], M_daisy) as daisy_sex_breed at Position(xalign = 0.0, yoffset = 0)
    $ animated = True
    pause
    player_name "Wow, you're really tight, {b}Daisy{/b}!"

    daisy "Is that good?"

    player_name "Yes, it's very good."

    daisy "Hehe, oke!"

    pause
    daisy "Ahhh!"

    daisy "This feels way better than it did with Master!"

    pause
    daisy "Your weasel is so deep inside me!"

    daisy "I mean... Your penis..."

    daisy "Your penis is really deep, in my floogina!"

    player_name "Hehe, kamu terlalu manis!"

    daisy "Terima kasih!"

    jump daisy_sex_breed_start

label daisy_sex_breed_start:
    if store._in_replay is not None:
        scene expression "backgrounds/location_barn_sex_back_day.jpg"
    $ anim_toggle = True
    if not animated:
        $ M_daisy.set('sex speed', 0.09)
        show expression AnimatedImage("daisy_sex_back", [1,2,3,4,5,6,7,8,9,10], M_daisy) as daisy_sex_breed at Position(xalign = 0.0, yoffset = 0)
        $ animated = True

label daisy_sex_breed_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                if M_daisy.get("change angle"):
                    scene expression "backgrounds/location_barn_sex_front_day.jpg"
                    show expression AnimatedImage("daisy_sex_front", [1,2,3,4,5,6,7,8,9,10], M_daisy) as daisy_sex_breed at Position(xalign = 0.0, yoffset = 0)
                    with dissolve
                else:
                    scene expression "backgrounds/location_barn_sex_back_day.jpg"
                    show expression AnimatedImage("daisy_sex_back", [1,2,3,4,5,6,7,8,9,10], M_daisy) as daisy_sex_breed at Position(xalign = 0.0, yoffset = 0)
                    with dissolve
                $ animated = True
            pause 5
            call expression game.dialog_select("daisy_sex_breed_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8,9,10]
            $ poses_done = []
            while poses_done != pose_list:
                if M_daisy.get("change angle"):
                    scene expression "backgrounds/location_barn_sex_front_day.jpg"
                    show expression "daisy_sex_front {}".format(pose_list[pose_counter]) as daisy_sex_breed at Position(xalign = 0.0, yoffset = 0)
                else:
                    scene expression "backgrounds/location_barn_sex_back_day.jpg"
                    show expression "daisy_sex_back {}".format(pose_list[pose_counter]) as daisy_sex_breed at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("daisy_sex_breed_hscene_dialog")
        $ animcounter += 1
    call screen daisy_sex_breed_options

label daisy_sex_breed_hscene_dialog:
    if animcounter == 0 and randomizer() < 50:
        daisy "Ahh!{p=1}{nw}"

    if animcounter == 0 and randomizer() < 10:
        daisy "I love your weasel!{p=1}{nw}"

        daisy "He's the best weasel ever!{p=2}{nw}"

        pause 1
        player_name "Pretty sure my weasel loves you too!{p=2}{nw}"

        daisy "He loves my hidey-hole, doesn't he?!{p=2}{nw}"

        player_name "Uh huh!{p=1}{nw}"

    if animcounter == 0 and randomizer() < 25:
        daisy "Gimme your milk weasel!{p=1}{nw}"

    if animcounter == 1 and randomizer() < 25:
        daisy "{i}*Gasp*{/i} Wowzers!{p=1}{nw}"

    if animcounter == 1 and randomizer() < 25:
        daisy "Harder, {b}[firstname]{/b}, harder!{p=1}{nw}"

        daisy "Ahhh!!{p=1}{nw}"

    if animcounter == 2 and randomizer() < 25:
        daisy "Aahhh!!{p=1}{nw}"

    if animcounter == 2 and randomizer() < 10:
        daisy "MooAAAHHH!!!{p=1}{nw}"

        daisy "MooooooooAAAHHHH!!!{p=1}{nw}"

        player_name "Are you-?{p=1}{nw}"

        daisy "MOOOOOOOAAAHHH!!!{p=1}{nw}"

        player_name "Whoa!{p=1}{nw}"

    if animcounter == 4 and randomizer() < 25:
        daisy "Oh goodness, I'm really sensitive toda-{p=2}{nw}"

        daisy "MooAAAHHHH!!!{p=1}{nw}"

        player_name "You okay?{p=1}{nw}"

        daisy "Don't stop!!{p=1}{nw}"

    if animcounter == 4:
        if randomizer() < 25:
            daisy "I'm gonna orgasm, {b}[firstname]{/b}!{p=1}{nw}"

            player_name "Haah, me too!{p=1}{nw}"

        elif randomizer() < 10:
            daisy "Oh, oh!{p=1}{nw}"

            daisy "{b}[firstname]{/b} something's happening!{p=1}{nw}"

            player_name "I know, I'm getting close too!{p=1}{nw}"

            pause 1
            daisy "Ahh, don't stop!{p=1}{nw}"

            daisy "Don't stop!!!{p=1}{nw}"

    return

label daisy_sex_breed_cum_out:
    daisy "Oh my, oh my!"

    scene expression "backgrounds/location_barn_sex_back_day.jpg"
    show daisy_sex_breed after
    show daisy_sex_breed_mc cumshot 2
    player_name "HNNGGG!!!" with flash
    daisy "NGGHHH!!!"

    show daisy_sex_breed_mc cumshot 1
    show daisy_sex_flying_cum 1
    with dissolve
    pause 1
    show daisy_sex_flying_cum 2
    with dissolve
    pause
    player_name "Haah... Haah..."

    player_name "Itu luar biasa!"

    daisy "Hehe, you squirted your milk all over me!"

    pause
    hide daisy_sex_flying_cum
    hide daisy_sex_breed_mc
    hide daisy_sex_breed
    with dissolve
    jump daisy_sex_post_pregnancy_minigame

label daisy_sex_breed_cum_in:
    daisy "Oh my, oh my!"

    scene expression "backgrounds/location_barn_sex_back_day.jpg"
    $ M_daisy.set("sex speed",0.4)
    show daisy_sex_breed creampie zorder 0
    show xray_diane_back zorder 1 at Position (align=(0,0))
    player_name "HNNGGG!!!" with flash
    hide xray_diane_back
    show daisy_sex_breed creampie_pullout
    with dissolve
    daisy "NGGHHH!!!"

    show daisy_sex_breed insert_and_pullout
    show daisy_sex_dick_cum 2 zorder 3
    with dissolve
    pause
    show daisy_sex_breed after
    show daisy_sex_cum zorder 1
    show daisy_sex_breed_mc zorder 2
    show daisy_sex_dick_cum 1
    with dissolve
    pause
    show daisy_sex_breed after_spread
    show daisy_sex_cum spread
    with dissolve
    player_name "Haah... Haah..."

    player_name "Itu luar biasa!"

    daisy "Hehe, I can feel your milk inside me..."

    pause
    if store._in_replay is not None:
        jump daisy_sex_post_pregnancy_minigame
    call call_pregnancy_minigame ("daisy_sex_post_pregnancy_minigame", M_daisy)

label daisy_sex_post_pregnancy_minigame:
    hide daisy_sex_cum
    hide daisy_sex_breed
    hide daisy_sex_dick_cum
    hide daisy_sex_breed_mc
    with dissolve
    $ renpy.end_replay()

    scene expression "backgrounds/location_barn_day_blur.jpg"
    show player 365 at left
    show daisy b_naked f_shy:
        xoffset -200
    with dissolve

    if M_daisy.get("daisy_breed_first_time"):
        player_name "Kamu baik-baik saja?"

        show player 366
        daisy "My legs feel funny..."

        show player 365
        player_name "Hehe."

        show player 366
        daisy "Apa itu tadi?"

        show player 365
        player_name "Uhh, an orgasm I think."

        show player 366
        daisy "Orgasm?"

        show player 365
        player_name "Yeah, it felt good, didn't it?"

        show player 366
        show daisy f_laugh a_up with dissolve
        daisy "It felt REALLY good!"

        show daisy f_normal a_idle with dissolve
        pause
        daisy "Is that supposed to happen every time?"

        show player 365
        player_name "Well, hopefully..."

        show player 366
        daisy f_shy "It never happened with Master."

        pause
        show daisy f_laugh
        daisy "Can we do it again?!"

        show daisy f_normal
        show player 365
        player_name "Heh, maybe in a little while... I need to rest first."

        show player 366
        daisy f_sad "Oh baiklah."

        pause
        show daisy f_normal:
            flip
            xoffset 200
        daisy "{b}Diane{/b}!!!"

        show player 367
        player_name "Whoa, what are yo-"

        show player 368
        daisy "{b}Diane{/b}!!!"

        show diane b_naked f_sad:
            xoffset 100
        with dissolve
        diane "{b}Daisy{/b}?!"

        diane "What's the matter with-"

        show diane f_surprised
        pause
        diane f_smirk "You two just had sex, didn't you."

        show player 367
        player_name "Uhh..."

        show player 368
        show diane f_smirk_fardown
        daisy "Yup, and guess what?!"

        diane "Apa?"

        show daisy f_laugh a_up with dissolve
        daisy "I had an orgasm!"

        show daisy f_normal a_idle with dissolve
        diane "{i}*Gasp*{/i} You did?"

        daisy "Eh ya!"

        daisy "My insides felt all tingly and my legs went silly and, and..."

        show diane f_laugh
        diane "Haha!"

        diane "Okay, okay, I get it."

        show diane f_smirk_fardown
        diane "He's pretty good, isn't he?"

        daisy "You mean at sex?"

        diane "Yes, at sex."

        show daisy f_laugh
        daisy "Oh ya!"

        show daisy f_normal
        daisy "I can't wait to do it again."

        show diane f_laugh
        diane "hehe!"

        show diane f_smirk
        show player 367
        player_name "Uhh, I'm gonna get a drink..."

        show player 368 with None
        show daisy:
            unflip
            xoffset -200
        with dissolve
        daisy "aku akan melakukannya!"

        show player 367
        player_name "No, I can-"

        show player 368
        daisy "You just stay and rest!"

        hide daisy with dissolve
        pause
        diane "So you went through with it, huh?"

        show player 365
        player_name "Hehe, ya..."

        show player 366
        diane @ f_laugh "I'm happy for you two!"

        show player 365
        player_name "T-terima kasih."

        show player 366
        pause
        diane "Just don't forget to throw me a bone once in a while too."

        diane "I have a business to run, you know?"

        show player 365
        player_name "Tentu saja."

        show player 366
        diane "hehe."

        hide player
        show diane b_kiss_both_naked:
            xoffset -217
        with dissolve
        pause
        show player 366 at left
        show diane b_naked
        with dissolve
        diane "Don't wear yourself out, stud."

        show diane f_smirk
        show player 365
        player_name "Yeah, I won't."

        $ M_daisy.set("daisy_breed_first_time", False)
    else:
        show daisy f_laugh
        daisy "Itu menyenangkan!"

        show daisy f_normal
        show player 365
        player_name "Heh, yeah it was..."

        show player 366
        daisy "Let's do it again!"

        show player 365
        player_name "Uhh, maybe later... I need to rest first."

        show player 366
        daisy "Oh benar."

        daisy "I always forget about that..."

        show player 365
        player_name "hehe."

        show player 366
        show daisy f_laugh
        daisy "Let me get you a glass of water!"

        hide daisy with dissolve
        show player 367
        player_name "No, you don't hav-"

        show player 368
        pause
        show player 367
        player_name "{i}*Sigh*{/i} Have to do that."

        player_name "She's gone."

        show player 368
        pause
        show player 365
        player_name "Heh, crazy cow girl."

    hide player
    hide diane
    with dissolve
    $ persistent.cookie_jar["Daisy"]["unlocked"] = True
    $ persistent.cookie_jar["Daisy"]["gallery"]["01_unlocked"] = True
    $ game.timer.tick()
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
