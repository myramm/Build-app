label scene_daisy_sex_yard:
    call scene_daisy_sex_yard.stage
    with fade
    anon "You know, I think I like pink flowers the best."
    daisy "Oh?"
    daisy "How come?"
    anon "Well, because they're pretty..."
    call scene_daisy_sex_yard.insert
    anon "... Mmm, and wet..."
    call scene_daisy_sex_yard.animate
    daisy "Ahh!"
    daisy "W-wet?!"
    anon "... and warm."
    daisy "{b}[firstname]{/b}!!"
    daisy "Flowers don't get warm!"
    anon "Are you sure?"
    daisy "I'm pretty-"
    daisy "Ngh!!"
    daisy "P-pretty sure."
    pause
    daisy "Oh, wowzers!!"
    daisy "This feels even better out here in the sunlight!"
    anon "Really?"
    daisy "Mhmm!"
    pause
    daisy "Careful you don't knock me over, {b}[firstname]{/b}!"
    anon "Don't worry, {b}Daisy{/b}... I've got you."
    daisy "Ahh!"
    pause
    daisy "{i}*Gasp*{/i} I think my floogina's gonna do that orgasm thing again!"
    anon "That's good."
    daisy "Yes!"
    daisy "Very, {i}very{/i} good!!"
    pause
    daisy "Oh, wowzers!!"
    daisy "NGH!!!" with flash
    anon "That's it, good girl."
    daisy "{b}[firstname]{/b}!!!"
    pause
    call scene_daisy_sex_yard.loop
    call scene_daisy_sex_yard.cum
    return


label scene_daisy_sex_yard.stage:
    scene location_diane_garden_sex_daisy
    show daisy_sex_stand_insert as animation
    show daisy sex_stand
    return


label scene_daisy_sex_yard.insert:
    show daisy_sex_stand_anim01 as animation
    hide daisy
    with dissolve
    return


label scene_daisy_sex_yard.animate:
    python:
        anim_toggle = True
        animated = True
        M_daisy.set('sex speed', 1 / 8.)
    hide daisy
    show daisy_sex_garden as animation
    with dissolve
    return


label scene_daisy_sex_yard.loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 3:
        if anim_toggle:
            if not animated:
                show daisy_sex_garden as animation with dissolve
                $ animated = True
            pause 5
            call scene_daisy_sex_yard.dialogue
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8]
            $ poses_done = []
            while poses_done != pose_list:
                show expression 'daisy_sex_garden {}'.format(pose_list[pose_counter]) as animation
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call scene_daisy_sex_yard.dialogue
        $ animcounter += 1
    call screen scene_daisy_sex_yard_controls
    if not _return:
        jump scene_daisy_sex_yard.loop
    return _return


label scene_daisy_sex_yard.dialogue:
    if animcounter == 0 and randomizer() > 75:
        daisy "Careful you don't knock me over, {b}[firstname]{/b}!{p=2}{nw}"
        anon "Don't worry, {b}Daisy{/b}... I've got you.{p=1.5}{nw}"
        daisy "Ahh!{p=1}{nw}"
    if animcounter == 1 and randomizer() > 75:
        daisy "I love having sex out here in the sunlight...{p=2}{nw}"
        daisy "... With all the pretty flowers!{p=1.5}{nw}"
        anon "Yeah, me too.{p=1}{nw}"
    if animcounter == 2 and randomizer() > 75:
        daisy "Haah! Your weasel is so big, {b}[firstname]{/b}!{p=1.5}{nw}"
    return


label scene_daisy_sex_yard.cum:
    anon "I'm getting close!"
    daisy "Haah... Haah..."
    pause
    anon "You ready?"
    daisy "Yes!!"
    show daisy_sex_stand_cum as animation
    anon "HNNGGG!!!" with flash
    show xray_front_under as xray with fastdissolve:
        anchor (.5, .5)
        pos (250 + 339, 250 + 167)
        rotate 14
        rotate_pad False
        xzoom -1
        zoom .74
    daisy "!!!"
    hide xray
    show daisy_sex_stand_insert as animation
    show daisy sex_stand
    show daisy_sex_stand_after
    with {'master': dissolve}
    daisy "Oh, wowzers!"
    anon "Phew..."
    anon "... That was a big one."
    daisy "Hehe, your weasel must have really needed it."
    anon "Y-yeah, I guess so."
    pause

    call call_pregnancy_minigame (None, M_daisy)
    return


label scene_daisy_sex_yard.repeat:
    call scene_daisy_sex_yard.stage
    with fade
    anon "Here's my favorite pink flower."
    daisy @ -m_talk "Hmm?"
    daisy "Where?!"
    call scene_daisy_sex_yard.insert
    daisy "Oh, wowzers!!"
    call scene_daisy_sex_yard.animate
    pause
    anon "Does that feel okay?"
    daisy "Yeah, it feels good!"
    pause
    daisy "{b}[firstname]{/b}, I think you might be feeding your weasel too much..."
    anon "Hmm?"
    daisy "... Seems like he gets bigger and bigger every day."
    anon "Heh, You think I should put him on a diet?"
    daisy "Yeah, I think so."
    pause
    daisy "Careful you don't knock me over, {b}[firstname]{/b}!"
    anon "Don't worry, {b}Daisy{/b}... I've got you."
    daisy "Ahh!"
    pause
    daisy "Oh, I love having sex out here in the sunlight..."
    daisy "... With all the pretty flowers!"
    anon "Yeah, me too."
    pause
    daisy "So when are you gonna show me this pink flower that you love so much?"
    anon "You wanna see it?"
    daisy "Of course!"
    pause
    daisy "{b}[firstname]{/b}, you know I love flowers!"
    daisy "And if it's your favorite, it must be {i}really{/i} pretty."
    anon "Oh, it is."
    anon "The most beautiful flower in the world."
    daisy "{i}*Gasp*{/i} Show me, show me!!"
    anon "Hehe, maybe later... if you're good."
    daisy "Aww."
    pause
    daisy "{i}*Gasp*{/i} I think my floogina's gonna do that orgasm thing again!"
    anon "That's good."
    daisy "Yes!"
    daisy "Very, {i}very{/i} good!!"
    pause
    daisy "Oh, wowzers!!"
    daisy "NGH!!!" with flash
    anon "That's it, good girl."
    daisy "{b}[firstname]{/b}!!!"
    pause
    call scene_daisy_sex_yard.loop
    call scene_daisy_sex_yard.cum
    return


label scene_daisy_sex_yard.replay:
    jump scene_daisy_sex_yard.repeat


screen scene_daisy_sex_yard_controls():
    style_prefix 'sex'

    vbox:

        frame:
            has hbox
            textbutton _('Keep Going') action Return(False)
            textbutton _('Cum') action Return()

        frame:
            has hbox
            textbutton _('« Slower'):
                action (Function(M_daisy.set, 'sex speed',
                                 1 / (1 / M_daisy.get('sex speed') - 2)),
                        Return(False))
                sensitive M_daisy.get('sex speed') < 1 / 8.
            textbutton _('Faster »'):
                action (Function(M_daisy.set, 'sex speed',
                                 1 / (1 / M_daisy.get('sex speed') + 2)),
                        Return(False))
                sensitive M_daisy.get('sex speed') > 1 / 16.
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
