label scene_nadya_blowjob:
    call scene_nadya_blowjob.stage
    nadya "Wow." (show_native="Ukh ty.")
    show nadya a_wiggle
    pause
    nadya "This is beautiful cock."
    anon "You're very beautiful too."
    show nadya -a_wiggle
    nadya "Da, this is true."
    call scene_nadya_blowjob.insert
    anon "!!!"
    anon "Oh, hello!"
    call scene_nadya_blowjob.animate
    pause
    anon "Mmm, that feels nice."
    pause
    nadya "{i}*Sluuuurp*{/i}"
    anon "Haah!"
    pause
    anon "You really know what you're doing down there!"
    nadya "Mhmm."
    pause
    anon "I'm getting close!"
    hide animation
    show nadya b_sex_bj_pre
    with {'master': dissolve}
    nadya "No."
    show nadya b_sex_bj_after f_disgusted_high with {'master': dissolve}
    anon "Hmm?"
    anon "Why'd you stop?"
    nadya "You are not cumming yet."
    nadya f_sexy_high "I would have you fuck pussy, first."
    anon "Oh, right... yeah."
    anon "I can do that."
    return


label scene_nadya_blowjob.stage:
    scene location_warehouse_office_bj
    show nadya b_sex_bj_pre
    with fade
    return


label scene_nadya_blowjob.insert:
    show nadya b_sex_bj_anim01 with dissolve
    return


label scene_nadya_blowjob.animate:
    python:
        anim_toggle = True
        animated = True
        M_nadya.set('sex speed', .10)
    hide nadya
    show nadya_blowjob_anim as animation
    with dissolve
    return


label scene_nadya_blowjob.loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 3:
        if anim_toggle:
            if not animated:
                show nadya_blowjob_anim as animation with dissolve
                $ animated = True
            pause 5
            call scene_nadya_blowjob.dialogue
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7]
            $ poses_done = []
            while poses_done != pose_list:
                show expression 'nadya_blowjob_anim {}'.format(pose_list[pose_counter]) as animation
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call scene_nadya_blowjob.dialogue
        $ animcounter += 1
    call screen scene_nadya_blowjob_controls
    if not _return:
        jump scene_nadya_blowjob.loop
    return _return


label scene_nadya_blowjob.dialogue:
    if animcounter == 0 and randomizer() > 75:
        anon "Mmm, that feels nice.{w=1}{nw}"
    elif animcounter == 1 and randomizer() > 75:
        nadya "{i}*Sluuuurp*{/i}{w=1}{nw}"
        anon "Haah!{w=1}{nw}"
    elif animcounter == 1 and randomizer() > 75:
        anon "Oh, {b}Nadya{/b}!{w=1}{nw}"
        nadya "Mhmm.{w=1}{nw}"
    elif animcounter == 2 and randomizer() > 75:
        anon "Yeah, just like that.{w=1}{nw}"
        nadya "{i}*Sluuuurp*{/i}{w=1}{nw}"
        anon "Oh, god!{w=1}{nw}"
    return


label scene_nadya_blowjob.repeat:
    call scene_nadya_blowjob.stage
    nadya "Wow." (show_native="Ukh ty.")
    show nadya a_wiggle
    pause
    nadya "Hello, beautiful cock."
    nadya "Is good to be seeing you again."
    anon "Heh."
    nadya -a_wiggle "Let's see how you taste today."
    call scene_nadya_blowjob.insert
    anon "!!!"
    anon "Oh, hello!"
    call scene_nadya_blowjob.animate
    pause
    anon "Mmm, that feels nice."
    pause
    nadya "{i}*Sluuuurp*{/i}"
    anon "Haah!"
    pause
    anon "Oh, {b}Nadya{/b}!"
    nadya "Mhmm."
    pause
    anon "Yeah, just like that."
    nadya "{i}*Sluuuurp*{/i}"
    anon "Oh, god!"
    pause
    call scene_nadya_blowjob.loop
    anon "I'm getting close!"
    pause
    anon "I can't-"
    pause
    hide animation
    show nadya b_sex_bj_cum
    anon "HNNGGG!!!" with flash
    pause
    anon "Haah... Haah..."
    show nadya a_wipe b_sex_bj_after f_surprised_cum_low with {'master': fastdissolve}
    nadya @ -m_talk "!!!"
    pause
    show nadya b_sex_bj_spit with {'master': dissolve}
    nadya "{i}*Ptooey*{/i}"
    pause
    show nadya a_idle b_sex_bj_after f_disgusted_closed with {'master': dissolve}
    nadya "Bleugh!"
    nadya f_disgusted_high "I am not liking taste..."
    anon "Oh?"
    nadya "Cock is good but cum not so..."
    nadya "... Very yuck!"
    anon "Heh, sorry."
    nadya f_sexy_high "Is okay."
    nadya "I still enjoy sucking your beautiful cock."
    pause
    return


label scene_nadya_blowjob.replay:
    jump scene_nadya_blowjob.repeat


screen scene_nadya_blowjob_controls():
    style_prefix 'sex'

    vbox:

        frame:
            has hbox
            textbutton _('Keep Going') action Return(False)
            textbutton _('Cum') action Return('cum')

        frame:
            has hbox
            textbutton _('« Slower'):
                action (Function(M_nadya.set,
                                 'sex speed',
                                 M_nadya.get('sex speed') + 0.03),
                        Return(False))
                sensitive M_nadya.get('sex speed') < .10
            textbutton _('Faster »'):
                action (Function(M_nadya.set,
                                 'sex speed',
                                 M_nadya.get('sex speed') - 0.03),
                        Return(False))
                sensitive M_nadya.get('sex speed') > .041
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
