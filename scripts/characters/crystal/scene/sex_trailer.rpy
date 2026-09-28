label scene_crystal_sex_trailer:

    return


label scene_crystal_sex_trailer.insert:
    show crystal_sex_chair_anim 8 as animation
    return

label scene_crystal_sex_trailer.animate:
    show crystal_sex_chair_anim as animation
    return


label scene_crystal_sex_trailer.loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 3:
        if anim_toggle:
            if not animated:
                call scene_crystal_sex_trailer.animate
                $ animated = True
            pause 5
            call scene_crystal_sex_trailer.dialogue
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = range(1, 11)
            $ poses_done = []
            while poses_done != pose_list:
                show expression "crystal_sex_chair_anim {}".format(
                    pose_list[pose_counter]) as animation
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call scene_crystal_sex_trailer.dialogue
        $ animcounter += 1
    call screen scene_crystal_sex_chair_controls()
    if not _return:
        jump scene_crystal_sex_trailer.loop
    return _return


label scene_crystal_sex_trailer.dialogue:
    $ renpy.dynamic(rng=renpy.random.random())

    if animcounter == 0 and rng <= .33:
        crystal "Ya like that, Romeo?{w=2}{nw}"
        anon "Y-yes!{w=1}{nw}"
        if rng <= .06:
            crystal "I said, ya like the way I'm workin' that pussy?!{w=4}{nw}"
            anon "YES!!{w=1}{nw}"
            crystal "Hehe!{w=1}{nw}"

    elif animcounter == 0 and rng <= .66:
        crystal "Pretty good, ain't it?{w=2}{nw}"
        anon "Mhmm!{w=1.5}{nw}"
        crystal "Yessir, that's years of practice... S'what that is!{w=4}{nw}"

    elif animcounter == 1 and rng <= .33:
        crystal "Ya best hold on tight now, cause I'm 'bout to turn up the heat!{w=4.5}{nw}"
        anon "!!!{w=1}{nw}"

    elif animcounter == 1 and rng <= .66:
        crystal "Ngh, this is just what I needed!{w=2}{nw}"
        crystal "Ain't nothin' better for gettin' mah blood pumpin'!{w=3.5}{nw}"

    elif animcounter == 1 and rng <= .99:
        crystal "Sooey, that's a deep dicken!{w=2}{nw}"
        anon "Shh, {b}Roxxy{/b}'s gonna hear you!!{w=2.5}{nw}"
        crystal "Oh, she don't give a hoot what I'm doin' out here...{w=3}{nw}"
        crystal "... You just focus on fillin' me up!{w=2.5}{nw}"

    elif animcounter == 2 and rng <= .33:
        crystal "Grab mah titty, it'll help ya cum faster.{w=3.5}{nw}"

    elif animcounter == 2 and rng <= .66:
        crystal "Careful ya ain't leanin' too far back now...{w=3.5}{nw}"
        crystal "... Don't want ya breakin' mah good sittin' chair!{w=3.5}{nw}"
        anon "This is your good sitting chair?{w=2.5}{nw}"
        crystal "Yer darn tootin'!{w=1.5}{nw}"

    elif animcounter == 2 and rng <= .99:
        crystal "Goddamn, I ain't had dick this good in years!{w=2.5}{nw}"
        crystal "Ya got me leakin' like a chicken coop in a rain storm!{w=4.5}{nw}"
        anon "Huh?!{w=1.5}{nw}"

    return


label scene_crystal_sex_trailer.cum(where):
    anon "Oh man, I can't hold out much longer..."
    crystal "That's alright, I'm close too."
    crystal "You go on and let that poison out!"
    anon "O-okay."
    pause
    anon "Here it..."
    anon "... Comes!!"
    crystal "NGGHHH!!!"
    show crystal_body_b_sex_chair_cum as animation

    if where == 'outside':
        show crystal_sex_chair_cumshot as cum

    anon "HNNGGG!!!" with flash

    if where == 'inside':
        show xray_crystal_sex_chair as xray
        with {'master': fastdissolve}

    pause
    hide xray
    with {'master': dissolve}

    anon "Haah... Haah..."
    show crystal_body_b_sex_chair_unmount as animation

    if where == 'outside':
        show crystal_body_b_sex_chair_unmount_cum as cum

    with {'master': dissolve}
    crystal "Haah..."
    return where


label scene_crystal_sex_trailer.repeat:
    python:
        renpy.dynamic(anim_toggle=True, animated=True, animcounter=0,
                      pose_counter=0, pose_list=None, poses_done=None)
        M_crystal.set('sex speed', 1 / 8.)

    scene location_trailer_sex_chair_evening
    show crystal_body_b_sex_chair_insert as animation
    with fade
    crystal "Mmm, that's it..."
    crystal "... Here comes Momma!"
    call scene_crystal_sex_trailer.insert
    with {'master': dissolve}
    crystal "Oof!"
    crystal "Now that's tighter than a gnats asshole..."
    call scene_crystal_sex_trailer.animate
    with {'master': dissolve}
    pause
    crystal "Goddamn!"
    pause
    crystal "Oh, there it goes..."
    crystal "... Nice and deep."

    call scene_crystal_sex_trailer.loop
    call scene_crystal_sex_trailer.cum (_return)
    return _return


label scene_crystal_sex_trailer.replay:
    jump scene_crystal_sex_trailer.repeat


screen scene_crystal_sex_chair_controls():
    style_prefix 'sex'

    vbox:

        frame:
            has hbox
            textbutton _('Keep Going') action Return(False)
            textbutton _('Cum Inside') action Return('inside')
            textbutton _('Cum Outside') action Return('outside')

        frame:
            has hbox
            textbutton _('« Slower'):
                action (Function(M_crystal.set, 'sex speed',
                                 1 / (1 / M_crystal.get('sex speed') - 2)),
                        Return(False))
                sensitive M_crystal.get('sex speed') < 1 / 8.
            textbutton _('Faster »'):
                action (Function(M_crystal.set, 'sex speed',
                                 1 / (1 / M_crystal.get('sex speed') + 2)),
                        Return(False))
                sensitive M_crystal.get('sex speed') > 1 / 16.
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
