label scene_becca_sex_bedroom:

    return


label scene_becca_sex_bedroom.stage:
    scene location_tina_becca_bedroom_sex as underlay at Transform(xoffset=-300)
    show becca_body_b_sex_bed_pre as animation at Transform(xoffset=-300)
    show roxxy bed b_rub f_horny at Split(-15, 'right', offset=-253).new:
        xoffset 253
    show expression phoneleft.core_bar as split
    return


label scene_becca_sex_bedroom.animate:
    show becca_sex_bedroom_anim as animation behind stage
    return


label scene_becca_sex_bedroom.pre:
    show becca_body_b_sex_bed_pre as animation
    return


label scene_becca_sex_bedroom.insert:
    show becca_body_b_sex_bed_cum as animation
    return


label scene_becca_sex_bedroom.loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 3:
        if anim_toggle:
            if not animated:
                call scene_becca_sex_bedroom.animate
                $ animated = True
            pause 5
            call scene_becca_sex_bedroom.dialogue
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8,9]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "becca_sex_bedroom_anim {}".format(pose_list[pose_counter]) as animation
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call scene_becca_sex_bedroom.dialogue
        $ animcounter += 1
    call screen scene_becca_sex_bedroom_controls
    if not _return:
        jump scene_becca_sex_bedroom.loop
    return _return


label scene_becca_sex_bedroom.dialogue:
    $ renpy.dynamic(rng=renpy.random.random())

    if animcounter == 0 and rng <= .33:
        becca "Ahh!!{w=1}{nw}"
        becca "It's too much, I can't-{w=1}{nw}"
        roxxy @ f_horny -m_talk "Mmm!{w=1}{nw}"

    elif animcounter == 0 and rng <= .66:
        roxxy f_horny "Ahh!{w=1}{nw}"
        becca "{i}*Whimpers*{/i}{w=1}{nw}"
        roxxy "Mmm, this is getting me so wet!{w=1.5}{nw}"
        show roxxy f_horny_lipbite

    elif animcounter == 1 and rng <= .33:
        roxxy f_horny "You enjoying that dick, {b}Becca{/b}?{w=1.5}{nw}"
        becca "Yes!{w=1}{nw}"
        roxxy "What's that?{w=1}{nw}"
        roxxy f_smug "I can't hear you!{w=1}{nw}"
        becca "YES!!{w=1}{nw}"
        roxxy f_horny_lipbite @ f_laugh "Hehe!{w=1}{nw}"

    elif animcounter == 1 and rng <= .66:
        roxxy @ f_smug "Bounce on it, {b}Becca{/b}!{w=1}{nw}"
        becca "I'm trying!{w=1}{nw}"
        becca "It's too...{w=1}{nw}"
        becca "... fucking...{w=1}{nw}"
        becca "... Ahh, shit!{w=1}{nw}"
        roxxy @ f_laugh "Hehe!!{w=1}{nw}"

    elif animcounter == 2 and rng <= .44:
        becca "Oh!!{w=1}{nw}"
        becca "Oh, {b}[firstname]{/b}!!{w=1}{nw}"
        roxxy @ f_horny "Mmm, look at those titties bounce...{w=1.5}{nw}"

    elif animcounter == 2 and rng <= .66:
        becca "It's so good!{w=1}{nw}"
        roxxy f_horny "I know.{w=1}{nw}"
        pause 1
        roxxy f_smug "You should really be thanking me for this, you know?{w=2}{nw}"
        becca "Thank you, {b}Roxxy{/b}!{w=1}{nw}"
        becca "Ahh!!{w=1}{nw}"
        show roxxy f_horny_lipbite
        becca "Thank you, thank you, thank you!!{w=1.5}{nw}"

    return


label scene_becca_sex_bedroom.cum:
    becca "Ngh, f-fuck!!"
    pause
    anon "I'm getting close!"
    becca "Me too!"
    roxxy @ f_horny "Heh, me three!"
    pause
    anon "I'm gonna-"
    roxxy f_annoyed "Don't stop!"
    anon "I can't-"
    show roxxy f_horny_lipbite
    with {'master': dissolve}
    becca "OH GOD!!!"
    pause
    anon "Here it comes!!"
    roxxy f_horny_lipbite_close @ -m_talk "NGGHHH!!!"
    show roxxy b_rub_cum f_cum
    show becca_body_b_sex_bed_cum as animation
    anon "HNNGGG!!!" with flash
    show xray_becca_sex_bedroom at Transform(xoffset=-300) with fastdissolve
    pause
    hide xray_becca_sex_bedroom
    show becca_sex_bedroom_anim 3 as animation
    show roxxy b_rub_under01 f_horny_lipbite_close
    with {'master': dissolve}
    becca "{i}*Whimpers*{/i}"
    pause
    show roxxy b_wet_hand f_horny_down
    show roxxy_bed_overlay_o_stain as stain:
        xoffset 253
    with {'master': dissolve}
    anon "Haah... Haah..."
    show roxxy f_suspicious
    with {'master': dissolve}
    anon "Wow."
    show roxxy b_stomach c_stomach f_horny
    with {'master': dissolve}
    roxxy "Hehe, did you cum?"
    anon "Y-yeah."
    show becca_body_b_sex_bed_after01 as animation
    with {'master': dissolve}
    anon "Hmm?"
    show becca_body_b_sex_bed_after02 as animation
    show becca_body_b_sex_bed_after_drip at Transform(xoffset=-300)
    show roxxy f_surprised_happy m_talk
    with {'master': dissolve}
    pause
    roxxy f_horny_lipbite -m_talk @ f_happy "Oh, wow... you came a lot!"
    becca "Ugh..."
    roxxy f_smug "Heh, she's dripping all over the place..."
    return


label scene_becca_sex_bedroom.repeat:
    python:
        renpy.dynamic(anim_toggle=True, animated=True)
        M_becca.set('sex speed', 1 / 8.)

    call scene_becca_sex_bedroom.stage
    with fade
    roxxy "C'mon, {b}Becca{/b}... What's taking so long?"
    call scene_becca_sex_bedroom.pre
    becca "Umm, your boyfriend's dick is fucking huge, remember?!"
    becca "I can't just jam it in."
    roxxy f_eyeroll "You're such a prissy little slut..."
    show becca_body_b_sex_bed_pre02 as animation
    with {'master': dissolve}
    becca "Shut up, {b}Roxxy{/b}!"
    show roxxy f_smug
    pause
    call scene_becca_sex_bedroom.insert
    show roxxy f_happy m_talk
    with {'master': dissolve}
    becca "Oh, shit!!!"
    roxxy -m_talk @ f_smug "Hehe, there we go!"
    show roxxy f_horny_lipbite
    call scene_becca_sex_bedroom.animate
    with dissolve
    pause
    becca "Haaaaah!!"
    roxxy f_horny "Mmm, this is fucking hot..."
    show roxxy b_rub_insert f_horny_down
    with dissolve
    pause
    show roxxy b_rub_under f_horny
    with dissolve
    pause
    roxxy "How's she feel, {b}[firstname]{/b}?"
    anon "Really, really tight."
    show roxxy f_horny_lipbite
    becca "{i}*Whimpers*{/i}"
    pause
    roxxy f_horny "C'mon, {b}[firstname]{/b}, fuck her harder!"
    roxxy f_smug "I wanna hear her squeal!"
    becca "N-no, we can't be too loud... my mom will hear and-"
    show roxxy f_happy m_talk
    $ M_becca.set('sex speed', 1 / 18.)
    becca "Oh my god!!" with vpunch
    roxxy f_horny_lipbite -m_talk @ f_smug "Hehe!"
    call scene_becca_sex_bedroom.loop
    call scene_becca_sex_bedroom.cum
    return


label scene_becca_sex_bedroom.replay:
    jump scene_becca_sex_bedroom.repeat


screen scene_becca_sex_bedroom_controls():
    style_prefix 'sex'

    vbox:

        frame:
            has hbox
            textbutton _('Keep Going') action Return(False)
            textbutton _('Cum') action Return('inside')

        frame:
            has hbox
            textbutton _('« Slower'):
                action (Function(M_becca.set, 'sex speed',
                                 1 / (1 / M_becca.get('sex speed') - 2)),
                        Return(False))
                sensitive M_becca.get('sex speed') < 1 / 8.
            textbutton _('Faster »'):
                action (Function(M_becca.set, 'sex speed',
                                 1 / (1 / M_becca.get('sex speed') + 2)),
                        Return(False))
                sensitive M_becca.get('sex speed') > 1 / 16.
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
