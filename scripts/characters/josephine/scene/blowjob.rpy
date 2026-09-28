image josie_blowjob = AnimatedImage("josephine_office_bj",
                                    (7,8,9,10,11,12,1,2,3,4,5,6),
                                    M_josie)


label scene_josie_blowjob:
    scene location_dealership_indoor_sex_bj
    call scene_josie_blowjob.ready
    call scene_josie_blowjob.animate
    with fade
    pause
    call scene_josie_blowjob.loop
    if _return:
        call scene_josie_blowjob.outside
    anon "Haah... Haah..."
    josephine "Hehe!"
    anon "That was incredible!"
    josephine b_sex_bj_lick o_empty "Mmm, you taste good."
    pause
    return


label scene_josie_blowjob.ready:
    show josephine b_sex_bj_talk
    show josephine_office_bj_mc as overlay
    return


label scene_josie_blowjob.animate:
    python:
        anim_toggle = True
        animated = True
        M_josie.set('sex speed', .12)
    hide josephine
    show josie_blowjob as animation behind overlay
    return


label scene_josie_blowjob.loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 3:
        if anim_toggle:
            if not animated:
                show josie_blowjob as animation with dissolve
                $ animated = True
            pause 5
            call scene_josie_blowjob.dialogue
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [7,8,9,10,11,12,1,2,3,4,5,6]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "josephine_office_bj {}".format(pose_list[pose_counter]) as animation
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call scene_josie_blowjob.dialogue
        $ animcounter += 1
    call screen scene_josie_blowjob_controls
    if not _return:
        jump scene_josie_blowjob.loop
    return _return


label scene_josie_blowjob.dialogue:
    if animcounter == 0 and randomizer() > 75:
        anon "AAHHHPP!!!{p=1}{nw}"
        josephine "Mmm.{p=1}{nw}"
    if animcounter == 1 and randomizer() > 75:
        anon "Holy crap!{p=1}{nw}"
    elif animcounter == 1 and randomizer() > 75:
        anon "Oh, yeah.{p=1}{nw}"
    if animcounter == 2 and randomizer() > 75:
        anon "Those lips are magical...{p=2}{nw}"
        josephine "Mmm.{p=1}{nw}"
    elif animcounter == 2 and randomizer() > 75:
        anon "You're incredible {b}Josie{/b}!{p=2}{nw}"
        josephine "{i}*Sluuuuuuurp*{/i}{p=1}{nw}"
    return


label scene_josie_blowjob.outside:
    anon "I'm gonna cum!"
    pause
    anon "{b}Josie{/b}, I'm gonna-"
    pause
    hide animation
    show josephine b_sex_bj_talk f_cum
    show josephine_office_bj_dick_cum
    show josephine_office_bj_mc
    anon "HNNGGG!!!" with flash
    hide josephine_office_bj_dick_cum
    show josephine f_normal o_cum
    with dissolve
    pause
    return


label scene_josie_blowjob.repeat:
    scene location_dealership_indoor_sex_bj
    call scene_josie_blowjob.ready
    with fade
    josephine "You know, you're lucky I like you..."
    pause
    josephine "... And that it's so freaking boring in this dealership!"
    anon "Amen to that!"
    call scene_josie_blowjob.animate
    with dissolve
    call scene_josie_blowjob.loop
    if _return:
        call scene_josie_blowjob.outside
    josephine "You like cumming on my face, don't you?"
    anon "You bet I do!"
    josephine "Hehe!"
    show josephine b_sex_bj_lick o_empty with dissolve
    pause
    return


label scene_josie_blowjob.replay:
    jump scene_josie_blowjob.repeat


screen scene_josie_blowjob_controls():
    style_prefix 'sex'

    vbox:

        frame:
            has hbox
            textbutton _('Keep Going') action Return(False)
            textbutton _('Cum') action Return('outside')

        frame:
            has hbox
            textbutton _('« Slower'):
                action (Function(M_josie.set,
                                 'sex speed',
                                 M_josie.get('sex speed') + 0.03),
                        Return(False))
                sensitive M_josie.get('sex speed') < .12
            textbutton _('Faster »'):
                action (Function(M_josie.set,
                                 'sex speed',
                                 M_josie.get('sex speed') - 0.03),
                        Return(False))
                sensitive M_josie.get('sex speed') > .061
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
