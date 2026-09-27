image maria_sex_storage = AnimatedImage('maria_backroom_sex',
                                        (1,2,3,4,5,6,7,8,9,10),
                                        M_maria)


label scene_maria_sex_storage(tony):
    scene location_pizza_storage_sex_front
    show maria b_sex_front_closed f_shy
    with fade
    if tony:
        anon "I can't believe we're doing this..."

        tony "It's alright, champ."

        tony "There ain't nothin' to be nervous about."

        pause
        tony "Just go slow at first, eh?"

        tony "She ain't never had nothin' like that dick of yours up there..."

        tony "Ain't that right, darlin'?"

        maria "Mmhmm."

        tony "Why don't you open your legs for him?"

        show maria f_shy_lipbite b_sex_front_open with dissolve
        maria @ -m_talk "..."
        show maria f_shy_away
        tony "Look at that pussy, champ!"

        tony "I bet it's drippin' with anticipation right now..."

        anon "{i}*Meneguk*{/i}"

        tony "You ready to get fucked, darlin'?"

    else:
        anon "I can't believe we're doing this."

        maria "Ya, saya tahu..."

        pause
        maria "Just go slow at first, eh?"

        maria "I ain't never had nothin' like that dick of yours up there..."

        maria "It's fuckin' ridiculously large!"

        anon "Y-yeah, so I've been told."

        show maria f_shy_lipbite b_sex_front_open with dissolve
        maria @ -m_talk "..."
        show maria f_shy_away
        anon "Apakah kamu siap?"

    maria "Yeah, go ahead, {b}[firstname]{/b}."

    show maria b_sex_front_insert with dissolve
    maria "Put it in."

    show anon_maria_sex_front pre with dissolve
    if tony:
        anon "Oke."

    else:
        anon "{i}*Gulp*{/i} Oke."

    show anon_maria_sex_front insert with dissolve
    pause
    show anon_maria_sex_front inside
    maria "!!!" with hpunch
    if tony:
        tony "That's it, champ."

        tony "All the way in."

    maria "Jesus, Mary, and Joseph!"

    maria "That's a big dick!"

    maria "Haah!"

    pause
    anon "Kamu baik-baik saja?"

    maria "Y-ya, hanya-"

    maria "Go slow, okay?"

    anon "Oke."


    scene location_pizza_storage_sex_side
    call scene_maria_sex_storage.animate (fade)
    if tony:
        tony "Ya Tuhan!"

        tony "It looks like you're spearin' an oyster with a meat harpoon..."

        maria "{b}Tony{/b}, that's not something I wanna hear right-"

        maria "NOOOOWWW!!!"

    else:
        maria "Fuuuuuuuuuuck!"

    pause
    maria "Oh, gawd!"

    pause
    maria "Oh my gawd!!"

    maria "This feels incredible!!"

    pause
    if tony:
        maria "Oh, persetan denganku!!"

    maria "aku akan keluar!!"

    pause
    hide animation
    show maria b_sex_side_cum
    with dissolve
    maria "AHHH, JESUS!!!"

    pause
    if tony:
        tony "Nice job, champ!"

        tony "You made her cum real good!"

        tony "Now keep goin'."

        call scene_maria_sex_storage.animate
    else:
        maria "Jangan berhenti!"

        maria "Please, keep go-"

        call scene_maria_sex_storage.animate
        maria "-IIINGGG!!!"

    maria "sial!!"

    pause
    maria "Ini sangat dalam!"

    if tony:
        maria "Oh gawd!"

        maria "{b}Tony{/b}, this is amazing!"

        tony "hehe!"

    else:
        maria "{b}[firstname]{/b}, you're dick is amazing!"

    maria "I'm gonna cum again!"

    anon "I'm getting close too."

    pause
    if tony:
        tony "That's it, champ!"

        tony "Make sure you cum deep inside her!"

        maria "Yes, {b}[firstname]{/b}!!"

    else:
        maria "Do it, {b}[firstname]{/b}!"

        maria "Put a baby inside me!"

    maria "Silakan!"

    if tony:
        anon "O-oke."

    else:
        anon "Y-ya, Bu."

    call scene_maria_sex_storage.loop
    call scene_maria_sex_storage.cum ('inside')

    show maria b_sex_side_after f_closed
    with dissolve
    anon "Haah... Haah..."

    maria "Oh, gawd..."

    maria "... I ain't never felt anything so good in all my life!"


    $ renpy.dynamic(poly=False)

    if tony:
        tony "Oh ya?"

        maria f_skeptical_down "Phew... Sorry, {b}Tony{/b}... I didn't mean-"

        maria f_surprised_down @ -m_talk "!!!"
        maria "{b}Tony{/b}, what the fuck are ya doin'?!"


        scene expression background(336, 400, 2.) as stage
        show tony b_naked_shirt f_smirk o_dick2:
            flip
        show tony_arms_naked_shirt_a_dick_side as tony_arms:
            flip
        with fade
        tony @ -m_talk "Hmm?"

        show tony a_dick_what
        show tony_arms_naked_shirt_a_dick_what as tony_arms
        tony "Apa?!"

        pause

        scene location_pizza_storage_sex_side
        show maria b_sex_side_after_back f_skeptical_down
        show anon b_maria_sex_side_back f_surprised_left_low
        with fade
        maria "Are you jerkin' off?!"

        tony "C'mon, darlin'... We're makin' magic here!"

        show anon f_worried_back_low
        maria f_unimpressed_down "{b}Tony{/b}..."

        tony "I just wanna feel involved."

        maria "... You're gonna freak the kid out!"

        tony "Aww, it ain't botherin' him none... Is it, champ?!"

        show maria f_worried

        menu:
            "You're making me uncomfortable.":
                anon "... Actually, {b}Tony{/b}..."

                anon "... It's a bit much."

                tony "Oh?"

                maria f_skeptical_down "See, I told ya!"

                maria "Put that thing away!"

                tony "Alright, alright... I'm sorry!"

                jump scene_maria_sex_storage.pullout
            "Saya tidak keberatan.":

                pass

        anon f_normal_back_low "Tidak apa-apa."

        show maria f_confused
        tony "See, I told ya!"

        show maria b_sex_side_after_up
        show anon maria_sex_side f_shy
        with {'master': dissolve}
        maria "Wow, it really don't bother ya, {b}[firstname]{/b}?"

        anon "Sama sekali tidak."


        scene expression background(336, 400, 2.) as stage
        show tony b_naked_shirt f_smirk o_dick2:
            flip
        show tony_arms_naked_shirt_a_dick_side as tony_arms:
            flip
        with fade
        tony "Heh, nothin' phases this kid... I fuckin' love it!"

        tony "I betcha he'd even be open to a little sandwich action... Eh, champ?"

        anon "Sandwich action?"

        tony "Yeah, you know... You're a piece of a white bread, I'm a piece of white bread, and {b}Maria{/b}'s the salami..."

        tony "... Bada bing, bada boom!"


        scene location_pizza_storage_sex_side
        show maria b_sex_side_after_back f_normal
        show anon b_maria_sex_side_back f_confused_back_low
        with fade
        anon "Oh, ehh... I'm not really hungry right now, {b}Tony{/b}..."

        anon f_happy_back_low "... But I could go for another one of those sports drinks, if you've got one?!"

        show maria f_laugh m_talk
        tony "{i}*Snort*{/i} Ya, I bet you could!"

        show maria f_normal -m_talk
        tony "That was quite a show ya just put on."

        maria "Kid, he's asking if he can join us next time..."

        show maria b_sex_side_after_up
        show anon maria_sex_side f_confused
        with {'master': dissolve}
        anon "What, like... for the sex stuff?"

        maria "Ya."

        tony "It's called a devil's threeway, champ."

        show maria b_sex_side_after_back
        show anon b_maria_sex_side_back f_normal_back_low
        with {'master': dissolve}
        anon "Err, umm... S-sure, I guess!"

        maria f_confused "You'd be open to that?"

        show maria b_sex_side_after_up
        show anon maria_sex_side f_normal
        with {'master': dissolve}
        anon "I mean, this is all about you guys starting your family, so..."

        anon "... If that's what you both want, I'm willing to give it try."

        show maria f_happy
        pause
        hide anon
        show maria b_sex_side_after_hug f_closed
        with {'master': dissolve}
        maria "Oh, you have no idea how special you're makin' this for us, {b}[firstname]{/b}!"

        anon "Heh, really... it's no problem."

        maria f_happy_down "Can you believe this kid, {b}Tony{/b}?!"

        tony "I told ya he was a keeper, didn't I?"

        tony "Eh?!"


        $ renpy.dynamic(poly=True)
    else:

        show maria b_sex_side_after_up f_normal
        show anon maria_sex_side
        with {'master': dissolve}
        anon "Ya?"

        maria "Phew... Just don't tell {b}Tony{/b} I said that..."

        anon "Heh, I won't."


    label scene_maria_sex_storage.pullout:
    scene location_pizza_storage_sex_front
    show maria b_sex_front_insert f_happy_closed
    show anon_maria_sex_front inside
    with fade
    pause
    show anon_maria_sex_front insert
    show maria_sex_front_mc_pullout
    with {'master': dissolve}
    maria "Phew, Jesus Christ..."

    show anon_maria_sex_front pre
    show maria_sex_front_mc_after
    hide maria_sex_front_mc_pullout
    with {'master': dissolve}
    maria "I feel like I just got split in two!"

    show maria b_sex_front_open
    hide anon_maria_sex_front
    hide maria_sex_front_mc_after
    show maria_sex_front_open_after
    with {'master': dissolve}

    if tony:
        tony "Yeah, you kinda look like it as well..."

    maria f_happy_closed "Hahahaah!"

    if tony:
        tony "Hehe!"

    else:
        anon "hehe."

    anon "Do you think I got you pregnant?"

    if tony:
        maria "Saya harap begitu."

        tony "Oh, I'm sure ya did..."

        tony "... And if he didn't, we'll just try again, right?"

        tony "You wouldn't mind doin' this again... Would ya, champ?"

    else:
        maria "I certainly hope so..."

        maria "... But if not, we'll just keep tryin'."

        maria "You wouldn't mind doin' this again, would ya?"

    anon "No, I wouldn't mind at all."

    if tony:
        tony "I can tell {b}Maria{/b} wouldn't mind neither..."

        tony "... Right, darlin'?"

        maria @ -m_talk "Hmm?"

        tony "I said, you wouldn't mind doin' this again, would ya?"

        maria f_normal "What, right now?!"

        tony "Heh, not right now!"

        tony "I mean, tomorrow or something... Till we're sure you're pregnant."

        maria f_happy_closed "Mmm, not at all..."

    else:
        maria "Heh, me neither."

    maria "If you'll excuse me, I think I'm just gonna lay here a while and bask in my postcoital bliss..."

    if tony:
        tony "Hah, no problem, darlin'."

        tony "C'mon, champ."

        tony "Let's leave her to compose herself, eh?"

        anon "Y-ya, oke."

        tony "Make sure you keep those legs elevated so his little guys can get to the egg."

        maria "I know how it works, honey..."

    else:
        maria "Why don't you head out and let {b}Tony{/b} know we're finished."

        anon "Ya, Bu."

    maria f_normal "Oh, and {b}[firstname]{/b}?"

    anon "Ya?"

    maria "You did real good."

    maria "Terima kasih."

    anon "You're welcome, {b}Maria{/b}."

    show maria f_happy_closed
    pause

    call call_pregnancy_minigame (None, M_maria)
    return poly


label scene_maria_sex_storage.animate(transition=dissolve):
    python:
        anim_toggle = True
        animated = True
        M_maria.set('sex speed', .12)
    hide anon
    hide maria
    show maria_sex_storage as animation
    with transition
    return


label scene_maria_sex_storage.loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    $ renpy.dynamic(diags=random.sample(range(15), 3))
    while animcounter < 3:
        if anim_toggle:
            if not animated:
                show maria_sex_storage as animation
                $ animated = True
            pause 5
            call scene_maria_sex_storage.dialogue (diags.pop())
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8,9,10]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "maria_backroom_sex {}".format(pose_list[pose_counter]) as animation
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call scene_maria_sex_storage.dialogue (diags.pop())
        $ animcounter += 1
    call screen scene_maria_sex_storage_controls(tony)
    if not _return:
        jump scene_maria_sex_storage.loop
    return _return


label scene_maria_sex_storage.dialogue(i, var=None):
    if i == 0:
        maria "Ahh!{p=1}{nw}"


    elif i == 1:
        maria "It's so fucking big!{p=2}{nw}"


    elif i == 2:
        maria "Oh, gawd!{p=1}{nw}"


    elif i == 3:
        maria "Jangan berhenti!{p=1}{nw}"


    elif i == 4 and var == 'mono' and tony:
        tony "Oh, that looks real nice.{p=2}{nw}"

    elif i == 4 and var == 'mono':
        maria "I can't believe it, you feel even bigger with me on top!{p=5}{nw}"

        anon "I do?{p=1.5}{nw}"

    elif i == 4 and var == 'poly':
        tony "Phew, you're so damn tight back here, darlin'!{p=4}{nw}"

        maria "Ngh!{p=1.5}{nw}"


    elif i == 5 and var == 'mono' and tony:
        tony "Does it feel as good as it looks, champ?{p=3}{nw}"

        anon "Mhmm!{p=1}{nw}"

        tony "Hehe!{p=1}{nw}"

    elif i == 5 and var == 'mono':
        maria "You dick is incredible, {b}[firstname]{/b}!{p=3}{nw}"

        anon "Haah!!{p=1}{nw}"

    elif i == 5 and var == 'poly':
        tony "You like that?{p=2}{nw}"

        maria "Yes!!{p=1}{nw}"

        tony "You like it when I work your tight little asshole?{p=4}{nw}"

        maria "YES!!!{p=1.5}{nw}"

        pause .5
        maria "OH, GAWD!!!{p=1.5}{nw}"


    elif i == 6 and var == 'mono' and tony:
        maria "Oh, gawd!{p=1.5}{nw}"

        tony "That's it, darlin'...{p=2}{nw}"

        tony "...Give it to him!{p=2}{nw}"

        maria "It's so deep, {b}Tony{/b}!{p=2}{nw}"

        tony "Yeah, I can see.{p=2}{nw}"

    elif i == 6 and var == 'poly':
        tony "C'mon, champ...{p=1.5}{nw}"

        tony "... Fuck her nice and deep now!{p=3}{nw}"

        anon "I'm trying!{p=2}{nw}"


    elif i == 7:
        anon "This is awesome!{p=2}{nw}"

        if tony:
            tony "Yeah, she knows what she's doin', don't she?{p=3.5}{nw}"

        pause .5
        if tony:
            tony "That feel good, darlin'?{p=2}{nw}"

        maria "So good!{p=1.5}{nw}"

        if tony:
            tony "Hehe!{p=1}{nw}"


    elif i == 8:
        maria "Mmm, give me a baby {b}[firstname]{/b}!{p=3}{nw}"

        anon "Oh, wow!{p=1.5}{nw}"

        maria "Please!!{p=1.5}{nw}"


    elif i == 9 and var == 'poly':
        maria "Does it feel good?{p=2}{nw}"

        anon "Yes!{p=1.5}{nw}"

        maria "Really good?{p=2}{nw}"

        anon "Mhmm!{p=1}{nw}"


    elif i == 10:
        maria "Oh, gawd!{p=1.5}{nw}"

        maria "Oh, my gawd!!{p=1.5}{nw}"

        pause .5
        maria "It's so damn good!!{p=2}{nw}"

        maria "AHH!!!{p=1}{nw}"


    elif i == 11 and tony:
        tony "Is he doin' good, darlin'?{p=2}{nw}"

        maria "Ngh, so good!{p=2}{nw}"

        maria "It feels so good!!{p=2}{nw}"


    elif i == 12:
        maria "JESUS, MARY, AND JOSEPH!!!{p=3}{nw}"

        if tony:
            tony "Hehe!{p=1.5}{nw}"

        else:
            anon "Haah!{p=1.5}{nw}"


    elif i == 13 and var == 'poly':
        tony "Man, this brings back a lot of memories...{p=4}{nw}"

        tony "... Ya know, Luigi and me used to call this move, \"The Kidney Shifter.\"{p=5}{nw}"

        tony "{b}Tina{/b} hated it when he coined that-{p=3}{nw}"

        maria "{b}Tony{/b} focus!!{p=2}{nw}"

        tony "Oh, sorry, darlin'!{p=2.5}{nw}"

        tony "Bad time to be gettin' nostalgic, eh?{p=3.5}{nw}"

    return


label scene_maria_sex_storage.switch:
    anon "You wanna switch?"

    hide animation
    show maria b_sex_3some_base
    with {'master': dissolve}
    maria "Hmm?"

    show maria b_sex_side_after_up f_surprised
    show anon maria_sex_side f_normal
    with {'master': dissolve}
    maria "Oh!"

    maria f_happy "Ya getting a second wind, are ya?"

    anon "Itu benar!"

    maria @ f_laugh "Hehehe!"

    maria "So feisty today!"

    call scene_maria_sex_storage.animate
    anon "Mhmm."

    jump scene_maria_sex_storage.resume


label scene_maria_sex_storage.cum(where):
    if where == 'inside':
        jump scene_maria_sex_storage.inside
    jump scene_maria_sex_storage.outside


label scene_maria_sex_storage.inside:
    anon "Boy, boy, boy... Very tall boy!"

    maria "Hah?"

    maria "Apakah kamu baru saja-"

    maria "Ahhh!!!"

    maria "OH MY GAWD!"

    maria "GIVE ME A BABY, {b}[firstname!u]{/b}!!!"

    pause
    hide animation
    show maria b_sex_side_cum
    anon "HNNGGG!!!" with flash
    show xray_maria_back with fastdissolve:
        align (0,0)
    maria "NGGHHH!!!"

    hide xray_maria_back
    pause
    return 'inside'


label scene_maria_sex_storage.outside:
    maria "OH MY GAWD!"

    maria "GIVE ME A BABY, {b}[firstname!u]{/b}!!!"

    pause
    scene location_pizza_storage_sex_front
    show maria b_sex_front_insert
    show anon_maria_sex_front cumshot
    show maria_sex_front_mc_cumshot_dick
    anon "HNNGGG!!!" with flash
    maria "NGGHHH!!!"

    pause
    hide maria_sex_front_mc_cumshot_dick
    show maria b_sex_front_open
    show anon_maria_sex_front pre
    show maria_sex_front_open_after_cumshot
    with dissolve
    return 'outside'


label scene_maria_sex_storage.repeat(tony):
    if tony:
        scene location_pizza_storage_sex_front
        show maria b_sex_front_closed
        with fade
        tony "God, you are so fuckin' sexy, darlin'!"

        show maria f_shy_lipbite b_sex_front_open with dissolve
        tony "You better get in there, champ..."

        show maria f_normal b_sex_front_insert with dissolve
        tony "... She wants it bad tonight!"

        show anon_maria_sex_front pre with dissolve
        anon "{i}*Meneguk*{/i}"

        show anon_maria_sex_front insert with dissolve
        pause
        show anon_maria_sex_front inside
        maria "!!!" with hpunch
        tony "That's it, champ."

        tony "All the way in."

        maria "Haah!"

        pause
    else:
        scene location_pizza_storage_sex_front
        show maria b_sex_front_closed
        with fade
        maria "Don't be shy, {b}[firstname]{/b}..."

        show maria f_shy_lipbite b_sex_front_open with dissolve
        pause
        show maria f_normal b_sex_front_insert with dissolve
        maria "I'm all yours."

        show anon_maria_sex_front pre with dissolve
        anon "{i}*Meneguk*{/i}"

        show anon_maria_sex_front insert with dissolve
        pause
        show anon_maria_sex_front inside
        maria "!!!" with hpunch
        maria "Haah!"


    scene location_pizza_storage_sex_side
    call scene_maria_sex_storage.animate (fade)
    maria "Fuuuuuuuuuuck!"

    pause
    if tony:
        tony "How's that feel, darlin'?"

    maria "Oh, gawd!"

    maria "Ini sangat bagus!"

    pause
    maria "I love this dick, so much!"

    maria "It feels incredible!!"

    if tony:
        tony "Hehe!"

    pause
    if randomizer() > 50:
        maria "Ini sangat dalam!"

    maria "Oh, gawd, fuck me, {b}[firstname]{/b}!!"

    maria "Persetan aku lebih keras!"

    if tony:
        tony "You heard her, champ!"

    pause
    maria "Ahh!!"

    maria "I'm gonna cum!!!"

    anon "I'm getting close too."

    if tony:
        tony "Make sure you cum deep inside her."

    pause
    maria "Do it, {b}[firstname]{/b}!"

    maria "Put a baby inside me!"

    maria "Silakan!"

    anon "Y-ya, Bu."

    label scene_maria_sex_storage.resume:
    call scene_maria_sex_storage.loop
    if _return == 'switch':
        jump scene_maria_sex_tony.switch
    call scene_maria_sex_storage.cum (_return)

    label scene_maria_sex_storage.outro:
    $ renpy.dynamic(where=_return)

    if where == 'inside':
        scene location_pizza_storage_sex_front
        show maria b_sex_front_insert f_happy_closed
        show anon_maria_sex_front inside
        with fade
        anon "Haah... Haah..."

        maria f_normal "Oh, gawd..."

        if tony:
            tony "That was incredible, champ!"

        else:
            maria "... This is the best sex ever!"

        anon "Ya?"

        if tony:
            tony "You really fucked her brains out..."

            maria "Hehehe!"

        else:
            maria "Phew... I don't know if I ever wanna quit doin' it..."

            anon "Benar-benar?"

        show anon_maria_sex_front insert
        show maria_sex_front_mc_pullout
        pause
        maria "Haah!"

        show anon_maria_sex_front pre
        show maria_sex_front_mc_after
        hide maria_sex_front_mc_pullout
        with dissolve
        pause
        show maria b_sex_front_open
        hide anon_maria_sex_front
        hide maria_sex_front_mc_after
        show maria_sex_front_open_after
        with dissolve

        if tony:
            maria "You know, I think we might have to try for more kids, {b}Tony{/b}..."

            tony "You serious?"

            maria f_happy_closed "Oh, I am very serious!"

            maria "Bagaimana menurutmu?"

        else:
            anon "Wouldn't {b}Tony{/b} be upset if we kept doing this?"

            maria "Are you kiddin'?"

            maria "He'll be ecstatic if he finds out you'll give him more than one kid!"

            pause
            anon "Well, I can definitely do that!"

            maria f_happy_closed "Heh, I know you can, handsome..."

            maria "Now if you'll excuse me, I think I'm just gonna lay here a while and bask in my postcoital bliss..."

            anon "Sure, thing."

            anon "See ya tomorrow, {b}Maria{/b}."

            maria "Sampai jumpa, {b}[firstname]{/b}."


        call call_pregnancy_minigame (None, M_maria)
    else:
        maria "Apa yang telah terjadi?"

        tony "You pulled out?"

        anon "Y-ya, maaf..."

        anon "The moment came and I just-"

        pause
        anon "Sorry, I just couldn't do it."

        hide anon_maria_sex_front with dissolve
        maria "Oh, it's alright, {b}[firstname]{/b}..."

        maria "... I don't mind."

        anon "Kamu tidak?"


        if tony:
            maria f_happy_closed "Mm, right now I just wanna enjoy this feeling..."

        else:
            maria "I mean, I would prefer you finish inside me; but if you'd rather pull out, that's okay too."

            anon "Benar-benar?"

            maria f_happy_closed "Just don't tell {b}Tony{/b}, yeah?"

            maria "Now if you'll excuse me, I think I'm just gonna lay here a while and bask in my postcoital bliss..."

            anon "Tentu saja."

            anon "See ya tomorrow, {b}Maria{/b}."

            maria "Sampai jumpa, {b}[firstname]{/b}."


    return where


label scene_maria_sex_storage.replay:
    $ renpy.dynamic(variants=persistent.cookie_jar['maria']['variants']['01_unlocked'])

    $ M_anon._cleared_states[S_ano11_done] = True

    if len(variants) > 1:
        scene expression im.Blur('backgrounds/location_pizza_storage_bed_night.jpg', 1.7) with fade
        menu:
            "With Tony" if True in variants:
                call scene_maria_sex_storage.repeat (True)

            "Without Tony" if False in variants:
                call scene_maria_sex_storage.repeat (False)

            "Threesome" if 'plus' in variants:
                call scene_maria_sex_storage.repeat ('plus')
    else:

        call scene_maria_sex_storage.repeat (next(iter(variants)))

    return


screen scene_maria_sex_storage_controls(tony):
    style_prefix 'sex'

    vbox:

        frame:
            has hbox
            textbutton _('Keep Going') action Return(False)
            textbutton _('Cum Inside') action Return('inside')
            if M_anon.finished_state(S_ano11_done):
                textbutton _('Cum Outside') action Return('outside')
                if tony == 'plus':
                    textbutton _('Threesome') action Return('switch')
                else:
                    textbutton _('Catch breath') action Return('switch')

        frame:
            has hbox
            textbutton _('« Slower'):
                action (Function(M_maria.set,
                                 'sex speed',
                                 M_maria.get('sex speed') + 0.03),
                        Return(False))
                sensitive M_maria.get('sex speed') < .12
            textbutton _('Faster »'):
                action (Function(M_maria.set,
                                 'sex speed',
                                 M_maria.get('sex speed') - 0.03),
                        Return(False))
                sensitive M_maria.get('sex speed') > .061
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
