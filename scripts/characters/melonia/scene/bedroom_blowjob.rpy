label scene_melonia_bedroom_blowjob:

    return


label scene_melonia_bedroom_blowjob.stage:
    scene location_rump_bedroom_bed_sex_bj
    show melonia_body_b_sex_bj_base as anim
    show melonia_body_b_sex_bj_base_face_talk_pre as face
    show melonia_body_b_sex_bj_base_dick as dick
    return


label scene_melonia_bedroom_blowjob.insert:
    hide face
    hide dick
    show melonia_bedroom_blowjob 1 as anim
    return


label scene_melonia_bedroom_blowjob.animate:
    show melonia_bedroom_blowjob as anim
    return


label scene_melonia_bedroom_blowjob.loop:
    call screen scene_melonia_bedroom_blowjob_controls

    if _return:
        return _return

    python hide:
        blocks = 5
        limit = 2

        renpy.dynamic(pool=random.sample(range(2 - limit, blocks + 1), limit))

    pause

    while pool:
        call scene_melonia_bedroom_blowjob.dialogue (pool.pop(), rng=random.random())
        pause

    jump scene_melonia_bedroom_blowjob.loop


label scene_melonia_bedroom_blowjob.dialogue(opt, rng=-1):

    if opt == 1:
        melonia "{i}*Garbled noises*{/i}"

        if rng < .5:
            anon "What's that?"
            melonia "{i}*Garbled noises intensify*{/i}"

        if rng < .3:
            anon "You want it deeper?"
            melonia "{i}*Challenging groan*{/i}"

        anon "I mean, it's pretty deep already but if you insist..."
        $ M_melonia.set('sex speed', 1 / (
            20. if rng < 0 else (1 / M_melonia.get('sex speed') + 4)))
        melonia "{i}*Gllllckk* *Gllllckk* *Gllllckk*{/i}"

        if rng < .5:
            anon "... That's right, take it!"

    elif opt == 2:
        anon "Yeah, just like that."
        melonia "{i}*Whimpers*{/i}"
        anon "Careful with the teeth."

    elif opt == 3:
        anon "Oh, man..."
        anon "... I'm not gonna lie, this is by far the most enjoyable sex I've ever had with you."

        if rng < .4:
            anon "Maybe I should jam my cock down your throat more often?"
            melonia "{i}*Unintelligible grunt*{/i}"

    elif opt == 4:
        if rng < .6:
            melonia "Mmm."

        melonia "{i}*Breathing intensifies*{/i}"
        anon "You're starting to get off on this, aren't you?"
        melonia "{i}*Enthusiastic moan*{/i}"

        if rng < .4:
            anon "I knew it!"

    elif opt == 5:
        melonia "{i}*Gllllckk* *Gllllckk* *Gllllckk*{/i}"

        if rng < .6:
            melonia "{i}*Gulp*{/i}"

        if rng < .3:
            melonia "{i}*Gllllckk* *Gllllckk* *Gllllckk*{/i}"

    return


label scene_melonia_bedroom_blowjob.switch:
    $ M_melonia.set('sex speed', 1. / 8)

    hide anim
    call scene_melonia_bedroom_press.pre
    show melonia f_annoyed
    with {'master': dissolve}
    melonia "Hey..."
    melonia f_confused "... Why'd you stop?!"
    anon "I can't listen to your mouth anymore!"

    call scene_melonia_bedroom_blowjob.stage
    with fade
    melonia "W-what are you doing?!"
    show melonia_body_b_sex_bj_base_face_pre as face
    anon "Shutting you up for good."
    show melonia_body_b_sex_bj_base_face_talk_pre as face
    melonia "Wha-"
    call scene_melonia_bedroom_blowjob.insert
    melonia "{i}*Gaaaum*{/i}" with hpunch
    call scene_melonia_bedroom_blowjob.animate
    with {'master': dissolve}
    melonia "!!!"
    pause
    anon "There we go..."
    melonia "{i}*Gllllckk*{/i}"
    anon "... That's much better!"
    pause
    call scene_melonia_bedroom_blowjob.dialogue (1)
    pause
    call scene_melonia_bedroom_blowjob.dialogue (2)
    pause
    call scene_melonia_bedroom_blowjob.dialogue (3)
    pause
    call scene_melonia_bedroom_blowjob.dialogue (4)
    pause
    call scene_melonia_bedroom_blowjob.dialogue (5)
    pause
    call scene_melonia_bedroom_blowjob.loop

    show melonia_body_b_sex_bj_cum as anim
    anon "HNNGGG!!!" with flash
    melonia "!!!"
    melonia "{i}*Gulp* *Gulp* *Gulp*{/i}"
    anon "Oh, take it all... You dirty girl!"
    show melonia_body_b_sex_bj_cum_drip1 as cum
    melonia "{i}*Splurrrt*{/i}" with flash
    show melonia_bedroom_blowjob_cum as cum
    melonia "{i}*Cough* *Sputter* *Cough*{/i}" with flash
    show melonia_body_b_sex_bj_base as anim
    show melonia_body_b_sex_bj_base_face_after
    show melonia_body_b_sex_bj_base_dick
    show melonia_body_b_sex_bj_base_dick_wet
    with {'master': dissolve}
    pause
    return 'blowjob'


screen scene_melonia_bedroom_blowjob_controls():
    style_prefix 'sex'

    vbox:

        frame:
            has hbox
            textbutton _('Keep Going') action Return(False)
            textbutton _('Cum') action Return()

        frame:
            has hbox
            textbutton _('« Slower'):
                action (Function(M_melonia.set, 'sex speed',
                                 1 / (1 / M_melonia.get('sex speed') - 2)),
                        Return(False))
                sensitive M_melonia.get('sex speed') < 1 / 8.
            textbutton _('Faster »'):
                action (Function(M_melonia.set, 'sex speed',
                                 1 / (1 / M_melonia.get('sex speed') + 2)),
                        Return(False))
                sensitive M_melonia.get('sex speed') > 1 / 16.
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
