label odette_1st_sex_bike:
    odette "Now then, should we pick up where we left off last time or-"
    pause
    odette f_smirk @ f_surprised "{i}*Gasp*{/i} Oh, that's perfect!"
    anon f_confused @ -m_talk "..."
    odette "I'm going to take you for a ride!"
    anon @ -m_talk "Hmm?"
    odette "Come with me, big fella!"
    hide odette with dissolve
    anon f_worried "Y-you wanna have sex on {b}Grace{/b}'s motorcycle?"
    odette "Hehehe!"
    odette "C'mon, it'll be fun!"

    scene expression "backgrounds/location_tattoo_garage_sex.jpg" with None
    show odette b_bike_base
    show odette_sex_bike_base_mc
    show odette_sex_arms_bike_base_mc a_pre
    with dissolve
    pause
    odette "Don't be shy, get over here."
    anon "O-okay."
    show odette_sex_arms_bike_base_mc a_insert with dissolve
    odette "Holy shit, that's even bigger than I thought!"
    jump odette_sex_intro

label odette_repeat_sex_bike:
    if _in_replay:
        $ player.go_to(L_tattooparlor_garage)
        scene expression player.location.background_closeup
    anon "Saddle up!"
    odette "Mm, I was hoping you'd say that!"
    label odette_repeat_sex_bike.segue:
    show anon f_flirt_low
    show odette b_panties_remove
    with dissolve
    pause
    show odette b_drop1 with dissolve
    pause
    show odette b_drop2 with dissolve
    show odette b_topless
    with dissolve
    odette "Follow me, big fella!"
    show anon a_behind_head f_shy
    hide odette
    with {'master': dissolve}
    anon "O-okay."
    scene location_tattoo_garage_sex
    show odette b_bike_base
    show odette_sex_bike_base_mc
    show odette_sex_arms_bike_base_mc a_pre
    with fade
    pause
    odette "Hurry {b}[firstname]{/b}, I need it bad!"
    anon "It's coming."
    show odette_sex_arms_bike_base_mc a_insert with dissolve
    odette "That's it, give it to me."
    jump odette_sex_intro

label odette_sex_intro:
    hide odette b_bike_base
    hide odette_sex_bike_base_mc
    hide odette_sex_arms_bike_base_mc
    $ anim_toggle = True
    $ animated = True
    $ M_odette.set('sex speed', .09)
    show expression AnimatedImage("odette_sex_bike", [1,2,3,4,5,6,7,8,9,10], M_odette) as odette_sex_bike at Position(xalign = 0.0, yoffset = 0)
    odette "!!!"
    if M_odette.get("bike_1st_time"):
        odette "Okay, wow!"
        odette "I've had a lot of dick but this is on a whole 'nother level!"
    else:
        odette "Mmm, fuck yes!"
    pause
    odette "It's so fucking deep!"
    odette "Ahh!"
    pause
    odette "C'mon {b}[firstname]{/b}, fuck me harder!"
    anon "Okay."
    $ M_odette.set('sex speed', .07)
    pause
    if M_odette.get("bike_1st_time"):
        odette "I can't believe {b}Evie{/b} is getting this on the regular."
        odette "She is one lucky girl!"
    else:
        odette "Mmm, I love this dick, so fucking much!"
        odette "Ahh!!"
    jump odette_sex_bike_loop

label odette_sex_bike_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("odette_sex_bike", [1,2,3,4,5,6,7,8,9,10], M_odette) as odette_sex_bike at Position(xalign = 0.0, yoffset = 0)
                $ animated = True
            pause 5
            call expression game.dialog_select("odette_sex_bike_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8,9,10]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "odette_sex_bike {}".format(pose_list[pose_counter]) as odette_sex_bike at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("odette_sex_bike_hscene_dialog")
        $ animcounter += 1
    call screen odette_sex_bike_options

label odette_sex_bike_hscene_dialog:
    if animcounter == 0 and randomizer() < 50:
        odette "Whooo, hehehe!{p=1}{nw}"
    if animcounter == 1 and randomizer() > 50:
        anon "Oh my god!{p=1}{nw}"
    if animcounter == 2 and randomizer() < 50:
        odette "Fuuuuck!{p=1}{nw}"
    if animcounter == 3 and randomizer() > 50:
        anon "I'm getting close...{p=2}{nw}"
    return

label odette_sex_bike_cum_inside:
    odette "Mmm, I'm going to cum all over that big dick!"
    anon "I'm getting close too!"
    pause
    odette "Don't stop, {b}[firstname]{/b}!"
    anon "I'm gonna-"
    pause
    odette "Fill my pussy to the brim!"
    anon "Here it comes!"
    pause
    hide odette_sex_bike
    show odette b_bike_cum
    anon "HNNGGG!!!" with flash
    show odette b_bike_cum2
    show xray_odette_bike:
        align (0,0)
    odette "NGGHHH!!!"
    hide xray_odette_bike
    pause
    show odette b_bike_base
    show odette_sex_bike_base_mc
    show odette_sex_arms_bike_base_mc a_after
    show odette_creampie
    with dissolve
    pause
    call call_pregnancy_minigame ("odette_sex_bike_end", M_odette)

label odette_sex_bike_cum_outside:
    odette "Mmm, I'm going to cum all over that big dick!"
    anon "I'm getting close too!"
    pause
    odette "Don't stop, {b}[firstname]{/b}!"
    anon "I'm gonna-"
    pause
    odette "Fill my pussy to the brim!"
    anon "Here it comes!"
    anon "I can't-"
    hide odette_sex_bike
    show odette b_bike_base
    show odette_sex_bike_base_mc
    show odette_sex_arms_bike_base_mc a_cumshot
    anon "HNNGGG!!!" with flash
    odette "NGGHHH!!!"
    pause
    show odette_sex_arms_bike_base_mc a_cumshot3
    with dissolve
    jump odette_sex_bike_end

label odette_sex_bike_end:
    anon "Haah... Haah..."
    odette "Damn, that's a huge load {b}[firstname]{/b}!"
    anon "Y-yeah, sorry..."
    odette "Hehehe!"
    scene expression background(l=L_tattooparlor_garage) as stage
    show anon
    show odette f_smirk b_topless
    with fade
    if M_odette.get("gotta_have_that_dick"):
        odette "Mmm, I so needed that."
        pause
        odette "You feel better now?"
        anon "Yeah, I guess."
        odette @ f_laugh "Hehehe!"
        anon f_worried "So this is really happening?"
        odette "Yup."
        odette "Nine months from now, we're gonna have a little poop machine!"
        anon @ -m_talk "..."
        odette "I should get back to the shop."
        anon "I'm going to be a father..."
        odette "Yup."
        odette @ f_laugh "Congrats!"
        hide odette with dissolve
        odette "Hehehe!"
        $ M_odette.set("gotta_have_that_dick", False)
        jump odette_pregnancy_have_baby_end
    elif M_odette.get("bike_1st_time"):
        odette @ f_confused "Did you make a pact with Satan or something?"
        anon "What?!"
        anon "N-no?"
        odette "That dick is mind-blowing, {b}[firstname]{/b}!"
        anon @ f_laugh "Heh, thanks!"
        odette "I've gotta get {b}Grace{/b} to try it."
        anon @ a_wave f_brag_closed "Yeah, right."
        anon "How are you going to convince {b}Grace{/b} to have sex with her sister's boyfriend?"
        odette @ f_laugh "Oh, I have my ways..."
        odette "Leave it to me."
        anon @ -m_talk "..."
        odette "In the meantime, you just focus on keeping little {b}Evie{/b} happy, okay?"
        anon @ a_point "I can do that."
        pause
        odette "Oh, and {b}[firstname]{/b}?!"
        anon @ -m_talk "Hmm?"
        odette "You let me know when you wanna take another ride, yeah?"
        odette "That dick is too good to pass up!"
        anon @ a_behind_head "O-okay."
        odette @ f_laugh "Hehehe!"
        $ M_odette.set("bike_1st_time", False)
    else:
        odette "Mm, I so needed that..."
        anon "Yeah?"
        odette "Don't get me wrong, {b}Grace{/b} can do some amazing things with her mouth but there's just no substitute for the real thing, you know?"
        anon "Ehh, yeah... Okay."
        odette "Sometimes a girl just needs a good, hard fucking..."
        anon "Well, I'm happy to oblige."
        odette @ f_laugh "Hehehe!"
        anon "Catch you later?"
        odette "Oh, sure."
        odette "You know where to find me."
        anon @ a_wave "See ya, {b}Odette{/b}."
        odette "Later, big fella."
        hide anon with dissolve
        odette "Give {b}Evie{/b} a kiss for me!"
    $ renpy.end_replay()
    $ persistent.cookie_jar["Odette"]["unlocked"] = True
    $ persistent.cookie_jar["Odette"]["gallery"]["01_unlocked"] = True
    $ game.timer.tick()
    $ player.go_to(L_tattooparlor)
    $ game.main()

label odette_pregnancy_have_baby_end:
    anon @ -m_talk "( {b}Odette{/b} is having my kid... )"
    anon f_sad_down @ -m_talk "( ... And I can't tell anyone that I'm the father. )"
    pause
    anon @ -m_talk "( Oh man, why does everything have to be so complicated? )"
    hide anon with dissolve
    $ game.timer.tick()
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
