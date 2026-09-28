image maria_blowjob = AnimatedImage('maria_sex_bj_anim', (1,2,3,4,5,6,7,8,9,10), M_maria)


label scene_maria_blowjob:
    return


label scene_maria_blowjob.animate:
    python:
        anim_toggle = True
        animated = True
        M_maria.set('sex speed', .12)
    hide maria
    show maria_blowjob as animation
    return


label scene_maria_blowjob.loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 3:
        if anim_toggle:
            if not animated:
                show maria_blowjob as animation with dissolve
                $ animated = True
            pause 5
            call scene_maria_blowjob.dialogue
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8,9,10]
            $ poses_done = []
            while poses_done != pose_list:
                show expression 'maria_sex_bj_anim {}'.format(pose_list[pose_counter]) as animation
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call scene_maria_blowjob.dialogue
        $ animcounter += 1
    call screen scene_maria_blowjob_controls
    if not _return:
        jump scene_maria_blowjob.loop
    return _return


label scene_maria_blowjob.dialogue:
    if animcounter == 0 and randomizer() > 75:
        anon "Oh, that feels good...{p=2}{nw}"
    if animcounter == 1 and randomizer() > 75:
        anon "I like the way you use your hand.{p=2}{nw}"
    elif animcounter == 1 and randomizer() > 75:
        anon "Oh, yeah.{p=1}{nw}"
    if animcounter == 2 and randomizer() > 75:
        maria "Mmhmm.{p=1}{nw}"
    elif animcounter == 2 and randomizer() > 75:
        anon "Haah, your tongue feels amazing!{p=2}{nw}"
        maria "{i}*Sluuuuuuurp*{/i}{p=1}{nw}"
    return


label scene_maria_blowjob.cum:
    anon "Here it comes!"
    maria "Mmm!"
    pause
    hide animation
    show maria b_sex_bj_base f_cumshot
    show maria_sex_bj_cum
    anon "HNNGGG!!!" with flash
    pause
    hide maria_sex_bj_cum
    show maria_sex_bj_dick3
    show maria f_swallow1
    pause 1
    show maria f_swallow2
    anon "!!!"
    maria f_swallow_after "Mmm, delicious!"
    show maria f_swallow2
    pause .01
    return


label scene_maria_blowjob.repeat:
    scene location_pizza_kitchen_bj
    call scene_maria_blowjob.animate
    with fade
    anon "!!!"
    call scene_maria_blowjob.loop
    call scene_maria_blowjob.cum
    return


label scene_maria_blowjob.replay:
    jump scene_maria_blowjob.repeat


screen scene_maria_blowjob_controls():
    style_prefix 'sex'

    vbox:

        frame:
            has hbox
            textbutton _('Keep Going') action Return(False)
            textbutton _('Cum') action Return('cum')

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
