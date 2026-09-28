label scene_melonia_sex_anal:

    return


label scene_melonia_sex_anal.insert:
    hide anim
    show melonia b_sex_anim_anal01
    return


label scene_melonia_sex_anal.animate:
    hide melonia
    show melonia_body_b_sex_anim_anal as anim
    return


label scene_melonia_sex_anal.loop:
    call screen scene_melonia_sex_anal_controls

    if _return:
        return _return

    python hide:
        blocks = 5 if anal == 'first' else 7
        limit = 3

        renpy.dynamic(pool=random.sample(range(2 - limit, blocks + 1), limit))

    pause

    while pool:
        call scene_melonia_sex_anal.dialogue (pool.pop(), rng=random.random())
        pause

    jump scene_melonia_sex_anal.loop


label scene_melonia_sex_anal.dialogue(opt, rng=-1):

    if opt == 1:
        if rng < 0:
            anon "Do you want me to stop?"
            melonia "I dunno, this is weird..."
            anon "Bad weird?"
            melonia "N-no, just-"

        melonia "{i}*Gasp*{/i} Oh fuck!"

    elif opt == 2:
        anon "You like it then?"

        if rng < 0:
            melonia "Huh?"

        if rng < .35:
            melonia "I don't know... Maybe..."
            anon "It's a yes-or-no question, {b}Melonia{/b}."

        melonia "Grr, shut up and fuck me!"
        anon "Alright."

    elif opt == 3:
        melonia "FUUUUUUCK!!"

    elif opt == 4:
        melonia "It feels like you're going to break my fucking spine!"
        anon "I can quit if you-"
        melonia "Don't you dare stop!"

    elif opt == 5:
        melonia "AHH!!"
        melonia "This is amazing!!"

    elif opt == 6:
        melonia "Fuck yes!!"

    elif opt == 7:
        melonia "Ngh, that's it!"
        melonia "Use me like the dirty girl I am!!"

    return


label scene_melonia_sex_anal.switch:
    $ M_melonia.set('sex speed', 1 / 8.)

    if not M_melonia.once('done_anal'):
        jump scene_melonia_sex_anal.first

    jump scene_melonia_sex_anal.repeat


label scene_melonia_sex_anal.first:
    $ renpy.dynamic(anal='first')

    hide anim
    show melonia b_sex_insert_pullout f_smirk
    with {'master': dissolve}
    melonia "W-what are you doing?"
    anon "Trying something new..."
    pause
    melonia f_surprised "Are you crazy?!"
    melonia "That thing isn't going to fit in my ass!"
    anon "Sure it will."
    melonia "No it-"
    call scene_melonia_sex_anal.insert
    melonia "!!!" with hpunch
    melonia "God damnit, {b}[firstname]{/b}!"
    anon "Are you alright?"
    melonia "No, I'm not okay!"
    melonia "Your cock is way too big for-"
    call scene_melonia_sex_anal.animate
    with {'master': dissolve}
    melonia "!!!"
    pause
    call scene_melonia_sex_anal.dialogue (1)
    pause
    call scene_melonia_sex_anal.dialogue (2)
    pause
    call scene_melonia_sex_anal.dialogue (3)
    jump scene_melonia_sex_anal.resume


label scene_melonia_sex_anal.repeat:
    $ renpy.dynamic(anal='repeat')

    melonia "Could you, maybe... Put it in my ass again?"
    hide anim
    show melonia b_sex_insert_pullout f_smirk
    with {'master': dissolve}
    anon "I knew you enjoyed that."
    melonia "Mmm, shut up and do it!"
    call scene_melonia_sex_anal.insert
    melonia "!!!" with hpunch
    call scene_melonia_sex_anal.animate
    with {'master': dissolve}
    call scene_melonia_sex_anal.dialogue (6)
    pause
    call scene_melonia_sex_anal.dialogue (7)
    pause
    label scene_melonia_sex_anal.resume:
    call scene_melonia_sex_anal.dialogue (4)
    pause
    call scene_melonia_sex_anal.dialogue (5)
    call scene_melonia_sex_anal.loop

    if _return == 'switch':
        jump scene_melonia_sex.switch

    call scene_melonia_sex.cum (_return, type='anal')

    return


screen scene_melonia_sex_anal_controls():
    style_prefix 'sex'

    vbox:

        frame:
            has hbox
            textbutton _('Keep Going') action Return(False)
            textbutton _('Cum Inside') action Return('inside')
            textbutton _('Cum Outside') action Return('outside')
            textbutton _('Vaginal') action Return('switch')

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
