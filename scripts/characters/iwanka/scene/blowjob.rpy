label scene_iwanka_blowjob(venue='basement', outfit='dress'):
    call scene_iwanka_blowjob.stage
    anon "Haah!"
    call scene_iwanka_blowjob.animate
    iwanka "{i}*Sluuuurp*{/i}"
    pause
    erik "Dude, this is so crazy!"
    erik "I'm having a party at my house right now, and my best friend in the whole wide world, {b}[firstname]{/b}..."
    erik "... Is getting his dick sucked by the mayor's daughter!"
    pause
    erik "See, that's {b}[firstname]{/b}'s dick!"
    pause
    erik "And that's {b}Iwanka{/b}."
    erik "Say hi to my guildies, {b}Iwanka{/b}."
    iwanka "Mmrllo!"
    iwanka "{i}*Glllcck*{/i}"
    pause
    anon "{b}Erik{/b}, can you put that thing away?"
    anon "This is awkward enough already without you-"
    anon "!!!"
    anon "Oh my god, right there!"
    pause
    erik "No way, dude!"
    erik "Every good cameraman knows you don't stop filming until the money shot!"
    anon "Grr!"
    pause
    iwanka "Mmm."
    erik "Your eyes are really beautiful, {b}Iwanka{/b}!"
    erik "I didn't notice until right now."
    iwanka "Thrrnnu!"
    pause
    call scene_iwanka_blowjob.loop
    anon "I'm getting close!"
    erik "You hear that, {b}Iwanka{/b}?"
    erik "Money-shot time!"
    iwanka "Mhmm."
    pause
    anon "Here it comes!"
    hide animation
    show iwanka b_bj f_cum a_cum
    anon "HNNGGG!!!" with flash
    pause
    show iwanka f_normal o_cum a_after with dissolve
    erik "Wow, you look just like Hamako after her first session with the octopus..."
    iwanka @ f_laugh "Hehe!"
    erik "... Only, this sperm is white and not blue."
    iwanka "And she got all her holes filled..."
    iwanka "... So far I only got the one."
    return


label scene_iwanka_blowjob.stage:
    if venue == 'basement':
        scene location_erik_basement_back_bj
        show iwanka b_bj a_pre
        show rec zorder 1
    else:
        if venue == 'yacht':
            scene location_boat_interior_evening_bed_bj
        else:
            scene location_rump_iwanka_day_bj
        show iwanka b_bj_naked a_pre
    with fade
    return


label scene_iwanka_blowjob.animate:
    python:
        anim_toggle = True
        animated = True
        M_iwanka.set('sex speed', .10)
    hide iwanka
    show expression 'iwanka_blowjob_{}'.format(outfit) as animation
    with dissolve
    return


label scene_iwanka_blowjob.loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 3:
        if anim_toggle:
            if not animated:
                show expression 'iwanka_blowjob_{}'.format(outfit) as animation with dissolve
                $ animated = True
            pause 5
            call scene_iwanka_blowjob.dialogue
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
            $ poses_done = []
            while poses_done != pose_list:
                show expression 'iwanka_sex_bj_anim_{} {}'.format(outfit, pose_list[pose_counter]) as animation
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call scene_iwanka_blowjob.dialogue
        $ animcounter += 1
    call screen scene_iwanka_blowjob_controls
    if not _return:
        jump scene_iwanka_blowjob.loop
    return _return


label scene_iwanka_blowjob.dialogue:
    if animcounter == 0 and randomizer() > 75:
        anon "Oh, that feels good...{p=2}{nw}"
    if animcounter == 1 and randomizer() > 75:
        anon "I like the way you use your hand.{p=2}{nw}"
    elif animcounter == 1 and randomizer() > 75 and venue == 'basement':
        erik "This is AWESOME!{p=1}{nw}"
    if animcounter == 2 and randomizer() > 75:
        iwanka "Mmhmm.{p=1}{nw}"
    elif animcounter == 2 and randomizer() > 75:
        anon "Haah, your mouth feels amazing!{p=2}{nw}"
        iwanka "{i}*Glllcck*{/i}{p=1}{nw}"
    return


label scene_iwanka_blowjob.repeat(venue, outfit='naked'):
    call scene_iwanka_blowjob.stage
    iwanka "You know, you're lucky I've had a lot of practice doing this in college."
    iwanka "Never with one this big, mind you."
    anon "Oh?"
    iwanka "It's very impressive."
    call scene_iwanka_blowjob.animate
    pause
    iwanka "Mmm."
    anon "Oh, that feels great."
    pause
    anon "Haah!"
    iwanka "{i}*Sluuuurp*{/i}"
    pause
    anon "You know, {b}Erik{/b} was right about your eyes..."
    anon "... They're really beautiful."
    iwanka "Thrrnnu!"
    pause
    iwanka "{i}*Glllcck*{/i}"
    anon "Wow, I don't know how you're taking it so deep!"
    call scene_iwanka_blowjob.loop
    anon "I'm getting close!"
    iwanka "Mmm."
    pause
    anon "Do you want it on your face again?"
    iwanka "Mhmm!!"
    hide animation
    show iwanka b_bj_naked f_cum a_cum
    anon "HNNGGG!!!" with flash
    pause
    show iwanka f_normal o_cum a_after with dissolve
    anon "Haah... Haah..."
    iwanka "Well, how do I look?"
    anon "Messy."
    iwanka "Hehe!"
    iwanka "If only my father could see me now."
    iwanka "He'd be so pissed."
    anon "Yeah, he'd probably kill me."
    iwanka "Oh, he'd definitely kill you."
    return


label scene_iwanka_blowjob.basement:
    call scene_iwanka_blowjob
    return

label scene_iwanka_blowjob.yacht:
    call scene_iwanka_blowjob.repeat ('yacht')
    return

label scene_iwanka_blowjob.bedroom:
    call scene_iwanka_blowjob.repeat ('bedroom')
    return


label scene_iwanka_blowjob.replay:
    $ renpy.dynamic(variants=persistent.cookie_jar['iwanka']['variants']['01_unlocked'])

    if len(variants) > 1:
        scene expression background(l=L_boat_bridge) with fade
        menu:
            "Basement (Video)" if 'basement' in variants:
                jump scene_iwanka_blowjob.basement

            "Yacht" if 'yacht' in variants:
                jump scene_iwanka_blowjob.yacht

            "Bedroom" if 'bedroom' in variants:
                jump scene_iwanka_blowjob.bedroom
    else:

        jump expression 'scene_iwanka_blowjob.{}'.format(next(iter(variants)))

    return


screen scene_iwanka_blowjob_controls():
    style_prefix 'sex'

    vbox:

        frame:
            has hbox
            textbutton _('Keep Going') action Return(False)
            textbutton _('Cum') action Return('cum')

        frame:
            has hbox
            textbutton _('« Slower'):
                action (Function(M_iwanka.set,
                                 'sex speed',
                                 M_iwanka.get('sex speed') + 0.03),
                        Return(False))
                sensitive M_iwanka.get('sex speed') < .10
            textbutton _('Faster »'):
                action (Function(M_iwanka.set,
                                 'sex speed',
                                 M_iwanka.get('sex speed') - 0.03),
                        Return(False))
                sensitive M_iwanka.get('sex speed') > .041
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
