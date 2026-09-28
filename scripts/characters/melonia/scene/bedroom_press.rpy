label scene_melonia_bedroom_press:

    return


label scene_melonia_bedroom_press.pre:
    show melonia bedroom_press d_insert f_smirk
    return


label scene_melonia_bedroom_press.insert:
    hide melonia
    show melonia_bedroom_press 4 as anim
    return


label scene_melonia_bedroom_press.animate:
    show melonia_bedroom_press as anim
    return


label scene_melonia_bedroom_press.loop:
    call screen scene_melonia_bedroom_press_controls

    if _return:
        return _return

    python hide:
        blocks = 7
        limit = 3

        renpy.dynamic(pool=random.sample(range(2 - limit, blocks + 1), limit))

    pause

    while pool:
        call scene_melonia_bedroom_press.dialogue (pool.pop(), rng=random.random())
        pause

    jump scene_melonia_bedroom_press.loop


label scene_melonia_bedroom_press.dialogue(opt, rng=-1):

    if opt == 1:
        melonia "Oh, god!!!"
        anon "You like that?"
        melonia "FUUUUCK MEEE!!!"

    elif opt == 2:
        melonia "AHHHH!!"
        melonia "{b}[firstname]{/b}!"

        if rng < .7:
            anon "Louder!"
            melonia "{b}[firstname!u]{/b}!!!"

    elif opt == 3:
        if rng < .2:
            melonia "Oh, that's it!"

        melonia "Pound my pussy with your dirty working class cock!"

    elif opt == 4:
        melonia "Ravage me, you filthy immigrant!"

        if rng < .4:
            anon "Wow..."
            anon "... Please stop talking."

    elif opt == 5:
        melonia "Graaah!!!"
        melonia "You're not going to cum inside me, are you {b}Hector{/b}?!"

    elif opt == 6:
        melonia "Soil my womb with your foreign seed!!"

        if rng < .4:
            anon "Oh, that's just gross."
            melonia "I know!"

        melonia "Oh, it's so wrong..."
        melonia "... Fill me to the brim!"

    elif opt == 7:
        melonia "Ruin me!"

    return


label scene_melonia_bedroom_press.switch:
    $ M_melonia.set('sex speed', 1. / 8)

    hide anim
    show melonia b_sex_insert_pullout f_smirk
    with {'master': dissolve}
    anon "Here, flip over."
    call scene_melonia_sex.stage
    with {'master': dissolve}
    melonia f_surprised @ -m_talk "Hmm?"
    anon "On your back."
    melonia f_satisfied "Oh, I think I need a second..."
    anon "What?"
    melonia "Your cock is so... fucking... big!"
    anon "Yeah, I'm aware."
    melonia @ -m_talk "Ngh."
    anon "This is what you wanted, remember?"
    melonia "My poor little pussy, it's-"
    anon "Yeah, yeah... Just shut up and flip over."
    show melonia b_sex_transition
    with {'master': dissolve}
    melonia "{b}Hector{/b}, I'm loving this domineering behavior!"
    call scene_melonia_bedroom_press.pre
    with {'master': dissolve}
    anon "I told you to stop calling me that!"
    melonia f_coy "Oh?"
    pause
    melonia "Silly me..."
    pause
    melonia "... I must have forgotten."
    anon "Well, maybe this will help you remember?"
    call scene_melonia_bedroom_press.insert
    with {'master': dissolve}
    melonia "{i}*Gasp*{/i} Yessss!"
    call scene_melonia_bedroom_press.animate
    with {'master': dissolve}
    call scene_melonia_bedroom_press.dialogue (1)
    anon "Say my name!"
    melonia "{b}Hector{/b}!!!"

    $ M_melonia.set('sex speed', 1. / 14)

    anon "No!" with vpunch
    call scene_melonia_bedroom_press.dialogue (2)
    pause
    call scene_melonia_bedroom_press.dialogue (3)
    anon "What?!"
    call scene_melonia_bedroom_press.dialogue (4)
    pause
    call scene_melonia_bedroom_press.dialogue (5)

    if M_anon.finished_state(S_ano20_done):
        anon "How many times do I have to tell you to stop calling me {b}Hector{/b}?!"
        melonia "Tell me you're gonna cum inside me!"
        anon "Why?"
    else:

        anon "Umm, didn't you tell me specifically {i}not{/i} to do that?"
        melonia "Just play along, I'm almost there!"

    call scene_melonia_bedroom_press.dialogue (6)
    pause
    call scene_melonia_bedroom_press.dialogue (7)
    call scene_melonia_bedroom_press.loop

    if _return == 'switch':
        jump scene_melonia_sex.flip

    if _return == 'switch:blow':
        jump scene_melonia_bedroom_blowjob.switch

    melonia "Oh, give me that huge, illegal cock!"
    anon "This is so fucked up..."
    melonia "I'm gonna cum!!"
    anon "... Ngh, me too!"
    melonia "I'm gonna-"
    melonia "NGGHHH!!!"

    if _return == 'inside':
        show melonia_body_b_sex_missionary_cum as anim
    else:
        hide anim
        show melonia bedroom_press d_cumshot

    anon "HNNGGG!!!" with flash

    if _return == 'inside':
        show xray_front_top as xray:
            anchor (.5, .5)
            pos (250 + 115, 250 + 176)
            rotate 84
            rotate_pad False
            xzoom -1
            zoom .88
    else:
        show melonia bedroom_press d_cumshot2
        with {'master': dissolve}

    melonia "Fuuuuuuuuuuuuuuck!!"
    pause
    hide xray

    if _return == 'inside':
        hide anim
        show melonia bedroom_press d_after

    with {'master': dissolve}
    anon "Haah... Haah..."
    return 'creampie' if _return == 'inside' else 'cumshot'


screen scene_melonia_bedroom_press_controls():
    style_prefix 'sex'

    vbox:

        frame:
            has hbox
            textbutton _('Keep Going') action Return(False)
            if M_anon.finished_state(S_ano20_done):
                textbutton _('Cum Inside') action Return('inside')
            textbutton _('Cum Outside') action Return('outside')
            textbutton _('Shut Up') action Return('switch:blow')
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
