label scene_melonia_sex:
    $ M_melonia.set('sex speed', 1. / 8)
    $ renpy.dynamic(variant='first')

    call scene_melonia_sex.stage
    with fade
    melonia @ -m_talk "Mmm."
    melonia "Put it in, {b}Hector{/b}!"
    melonia "I can't wait another second!"
    anon "Okay."
    call scene_melonia_sex.insert
    with {'master': dissolve}
    melonia "Oh god!"
    melonia "OH MY GOD!!"
    melonia f_surprised "It's too big!"
    melonia "This is-"
    call scene_melonia_sex.animate
    with {'master': dissolve}
    melonia "AHHH!!"
    pause
    anon "Are you alright!"
    melonia "I can't-"
    call scene_melonia_sex.dialogue (1)
    pause
    melonia "OHMYGODOHMYGODOHMYGOD!!!"
    anon "This is what you wanted..."
    melonia "{b}HECTOR{/b}!!"
    melonia "OH, {b}HECTOR{/b}!!!"
    hide anim
    show melonia b_sex_insert_pullout f_surprised
    with {'master': dissolve}
    melonia "Whaa?!"
    melonia "Why did you-"
    show melonia b_sex_anim_hard
    anon "MY." with vpunch
    show melonia b_sex_anim_hard
    anon "NAME." with vpunch
    show melonia b_sex_anim_hard
    anon "IS." with vpunch
    show melonia b_sex_anim_hard
    anon "[firstname!u]!" with vpunch
    show melonia b_sex_insert_pullout f_moan
    with {'master': dissolve}
    call scene_melonia_sex.dialogue (2)
    show melonia f_surprised with {'master': dissolve}
    anon "Say it!"
    melonia "{b}[firstname]{/b}?"
    call scene_melonia_sex.animate
    melonia "AHH, [firstname!u]!"
    pause
    call scene_melonia_sex.loop
    call scene_melonia_sex.cum (_return)
    return


label scene_melonia_sex.stage:
    scene location_rump_bedroom_bed_sex
    show melonia b_sex_pre_after f_smirk
    return


label scene_melonia_sex.insert:
    show melonia b_sex_insert_pullout f_moan
    return


label scene_melonia_sex.animate:
    hide melonia
    hide melonia_body_b_sex_anim_hard
    show melonia_body_b_sex_anim as anim
    return


label scene_melonia_sex.loop:
    call screen scene_melonia_sex_controls

    if _return:
        return _return

    python hide:
        blocks = 9
        limit = 3

        renpy.dynamic(pool=random.sample(range(2 - limit, blocks + 1), limit))

    pause

    while pool:
        call scene_melonia_sex.dialogue (pool.pop(), rng=random.random())
        pause

    jump scene_melonia_sex.loop


label scene_melonia_sex.dialogue(opt, rng=-1):

    if opt == 1:
        if rng < .2:
            anon "Are you alright!"
            melonia "I can't-"

        melonia "This is too much!"
        anon "Should I stop?"

        if variant == 'first':
            melonia "Oh, fuck me!!"
        else:
            melonia "No, don't stop!!"

        if rng < .5:
            anon "Okay."

    elif opt == 2:
        melonia "{i}*Whimpers*{/i}"

    elif opt == 3:
        melonia "AHHH!!"

    elif opt == 4:
        melonia "OHMYGODOHMYGODOHMYGOD!!!"
        anon "This is what you wanted..."
        melonia "[firstname!u]!!!"
        melonia "OH, [firstname!u]!!!!"

    elif opt == 5:
        anon "I'm happy you're using my real name now."
        melonia "{i}*Whimpers*{/i}"

    elif opt == 6:
        anon "Say it!"
        melonia "{b}[firstname]{/b}!"
        anon "Louder!"
        melonia "AHH, [firstname!u]!"

    elif opt == 7:
        melonia "[firstname!u]!"

    elif opt == 8:
        melonia "Oh, fuck me!!"

    elif opt == 9:
        melonia "OH, [firstname!u]!!!!"

    return


label scene_melonia_sex.flip:
    $ M_melonia.set('sex speed', 1. / 8)

    hide anim
    call scene_melonia_bedroom_press.pre
    show melonia f_confused
    with {'master': dissolve}
    anon "Alright, flip back over."
    melonia "Hey..."
    melonia f_annoyed "... I was almost there!"
    anon "Yeah, don't care."
    anon "Flip over, I don't wanna look at you anymore."
    melonia f_eyeroll "Oh, stop being such a baby..."
    melonia "... It's just a little dirty talk."
    show melonia f_smirk
    anon "Flip!"
    anon "Over!"
    show melonia b_sex_transition
    with {'master': dissolve}
    melonia "{b}Hector{/b}, you're so aggressive today!"
    call scene_melonia_sex.stage
    with {'master': dissolve}
    anon "For fucks sake..."
    anon "... That's not my name!"
    show melonia b_sex_insert_pullout f_moan
    with {'master': dissolve}
    melonia "{i}*Gasp*{/i} Oh ho ho ..."
    show melonia b_sex_anim01
    melonia "FUUUUUUCK!!!" with vpunch
    call scene_melonia_sex.animate
    with {'master': dissolve}
    jump scene_melonia_sex.resume


label scene_melonia_sex.switch:
    $ M_melonia.set('sex speed', 1. / 8)

    hide anim
    show melonia b_sex_insert_pullout f_smirk
    with dissolve
    anon "I think your pussy needs some more attention."
    show melonia b_sex_anim01
    melonia "OHMYGODOHMYGODOHMYGOD!!!" with vpunch
    call scene_melonia_sex.animate
    with {'master': dissolve}
    anon "This is what you needed, isn't it?"
    melonia "[firstname!u]!!!"
    anon "Say it!"
    melonia "This is what I needed!"
    anon "Louder!"
    melonia "AHH, I need it so bad!"
    pause
    jump scene_melonia_sex.resume


label scene_melonia_sex.cum(where, type='vaginal'):
    melonia "I'm gonna cum!"
    anon "Me too!"
    pause
    melonia "Don't stop!"
    melonia "Oh my god, {b}[firstname]{/b}!!"
    melonia "DON'T STOP!!!"
    melonia "NGGHHH!!!"
    hide anim

    if where == 'inside':
        show melonia b_sex_cum
    else:
        show melonia b_sex_insert_pullout a_cumshot f_moan

    anon "HNNGGG!!!" with flash

    if where == 'inside' and type == 'vaginal':
        show xray_melonia_top with fastdissolve:
            align (0,0)
        pause
        hide xray_melonia_top with dissolve

    elif where == 'outside':
        show melonia a_empty f_satisfied
        show melonia_arms_sex_insert_pullout_a_cumshot3
        with {'master': dissolve}

    anon "Haah... Haah..."
    pause

    if where == 'inside':
        show melonia b_sex_insert_pullout f_satisfied with dissolve

    anon "Do you feel better now?"

    if where == 'inside':
        show melonia b_sex_pre_after a_after with dissolve

    melonia @ -m_talk "{i}*Whimper*{/i}"
    anon "{b}Melonia{/b}?"
    anon "Are you alright?"
    melonia "I can't..."
    melonia "... Talk."
    anon "Hmm?"
    melonia "Fireworks."
    anon "Right."
    anon "I'll umm-"

    if where == 'inside':
        anon "Okay."

        if type == 'vaginal':
            call call_pregnancy_minigame (None, M_melonia)
    else:

        anon "Get you a towel or something..."

    return


label scene_melonia_sex.first:
    jump scene_melonia_sex


label scene_melonia_sex.repeat:
    $ M_melonia.set('sex speed', 1. / 8)
    $ renpy.dynamic(variant='repeat')

    call scene_melonia_sex.stage
    with fade
    melonia "Put it in!"
    melonia "I can't wait another second!"
    anon "Okay."
    call scene_melonia_sex.insert
    with {'master': dissolve}
    melonia "Oh god!"
    melonia "OH MY GOD!!"
    melonia "It's so big!"
    melonia "I thought it would be easier!"
    pause
    call scene_melonia_sex.animate
    with {'master': dissolve}
    call scene_melonia_sex.dialogue (3)
    pause
    call scene_melonia_sex.dialogue (1)
    pause
    call scene_melonia_sex.dialogue (4)
    pause
    call scene_melonia_sex.dialogue (5)
    pause
    call scene_melonia_sex.dialogue (6)
    pause
    label scene_melonia_sex.resume:
    call scene_melonia_sex.loop

    if _return == 'switch':
        jump scene_melonia_bedroom_press.switch
    elif _return == 'switch:anal':
        jump scene_melonia_sex_anal.switch

    call scene_melonia_sex.cum (_return)
    return


label scene_melonia_sex.replay:
    $ renpy.dynamic(variants=persistent.cookie_jar['melonia']['variants']['01_unlocked'])

    if len(variants) > 1:
        scene expression background(l=L_rump_master) with fade
        menu:
            "First" if 'first' in variants:
                jump scene_melonia_sex.first

            "Repeat" if 'repeat' in variants:
                jump scene_melonia_sex.repeat

    jump expression 'scene_melonia_sex.{}'.format(next(iter(variants)))


screen scene_melonia_sex_controls():
    style_prefix 'sex'

    vbox:

        frame:
            has hbox
            textbutton _('Keep Going') action Return(False)
            if M_anon.finished_state(S_ano20_done):
                textbutton _('Cum Inside') action Return('inside')
            textbutton _('Cum Outside') action Return('outside')

            if variant == 'repeat':
                textbutton _('Anal') action Return('switch:anal')
                textbutton _('Switch') action Return('switch')

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
