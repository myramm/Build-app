label scene_odette_couch_anal:
    $ M_odette.set('sex speed', 1 / 8.)
    $ renpy.dynamic(rv={'anal'})

    call scene_odette_couch_anal.stage
    with fade
    anon "So have you done this a lot?"
    odette "What do you think?"
    anon "I'm thinking yes."
    call scene_odette_couch_anal.insert
    odette "OHH, FUCK!!" with hpunch
    show odette -f_surprised m_talk
    anon "Too fast?"
    show odette -m_talk
    odette "Yep."
    anon "Sorry!"
    odette "Haah... Haah..."
    odette "{i}*Iiith*{/i} It's alright..."
    odette "... Just-"
    call scene_odette_couch_anal.animate
    with dissolve
    call scene_odette_couch_anal.dialogue (1)
    pause
    call scene_odette_couch_anal.dialogue (2)
    pause
    call scene_odette_couch_anal.dialogue (3)
    pause
    call scene_odette_couch_anal.dialogue (4)
    pause
    call scene_odette_couch_anal.dialogue (5)
    pause
    call scene_odette_couch_anal.dialogue (6)
    pause
    call scene_odette_couch_anal.dialogue (7)
    pause

    label scene_odette_couch_anal.resume:
    call scene_odette_couch_anal.loop

    if _return == 'switch':
        jump scene_odette_couch_back.switch

    anon "I'm gonna blow!"
    odette "Don't stop!!"
    anon "I can't hold it!"
    odette "Don't-"
    odette "NGGHHH!!!"

    show odette_sex_couch_anal_cum as anim
    anon "HNNGGG!!!" with flash
    pause

    show odette_sex_couch_anal_insert as anim
    show odette sex_couch_anal
    with {'master': dissolve}
    anon "Haah... Haah..."
    show odette_sex_couch_anal_pre as anim
    show odette_sex_couch_anal_after
    with {'master': dissolve}
    odette "Fuuuuuck."
    anon "You alright?"
    odette "Heh, that was fucking intense!"
    anon "Good intense or bad intense?"
    odette "Both."
    anon "Really?"
    odette "Hehe!"
    return rv


label scene_odette_couch_anal.stage:
    scene location_tattoo_garage_anal_sex
    show odette_sex_couch_anal_pre as anim
    show odette sex_couch_anal
    return


label scene_odette_couch_anal.insert:
    show odette_sex_couch_anal_insert as anim
    show odette f_surprised
    return


label scene_odette_couch_anal.animate:
    hide odette
    show odette_sex_couch_anal as anim
    return


label scene_odette_couch_anal.loop:
    call screen scene_odette_couch_anal_controls

    if _return:
        return _return

    python hide:
        blocks = 7
        limit = 3

        renpy.dynamic(pool=random.sample(range(2 - limit, blocks + 1), limit))

    pause

    while pool:
        call scene_odette_couch_anal.dialogue (pool.pop(), rng=random.random())
        pause

    jump scene_odette_couch_anal.loop


label scene_odette_couch_anal.dialogue(opt, rng=-1):

    if opt == 1:
        odette "Holy shit!"

    elif opt == 2:
        odette "Ohmygod, ohmygod, OHMYGOD!!"
        anon "You alright?"
        odette "You're really, REALLY big!"

        if rng < .5:
            anon "Should I stop?"
            odette "N-no!"

    elif opt == 3:
        anon "I can feel your asshole spasming..."
        odette "Fuuuuuck!"
        anon "... And your legs shaking as well!"

    elif opt == 4:
        if rng < .5:
            odette "I'm gonna cum!"
            anon "Already?!"
            odette "Yes!!!"

        odette "GRAAAAAH!!!" with flash
        anon "Whoa!"
        odette "Fuck, fuck, FUUUUCK!!"

    elif opt == 5:
        odette "So fucking deep!"
        anon "I can go deeper."
        odette "N-no, don't-"
        odette "NGH!!"

    elif opt == 6:
        odette "Ahh!!"
        odette "Fuck my ass!"
        odette "Fuck!!"
        anon "This is awesome!"

    elif opt == 7:
        anon "Your ass is so tight, {b}Odette{/b}!"
        anon "I'm not going to last much longer at this rate."
        odette "Ahh!!"

    return


label scene_odette_couch_anal.switch:
    $ M_odette.set('sex speed', 1 / 8.)
    $ rv.add('anal')

    if 'v->a' not in rv:
        $ rv.add('v->a')
        call scene_odette_couch_back.stage
        with dissolve
        odette @ -m_talk "Hmm?"
        odette "Why'd you stop?"
        anon "I'm not stopping... I'm switching holes."
        call scene_odette_couch_anal.stage
        with fade
        odette "Switching holes?!"
        odette "Does that mean what I think-"
        call scene_odette_couch_anal.insert
        with {'master': dissolve}
        odette "OHHHH KAY..."
        odette -f_surprised "... Fuuuuuuuck!"
        anon "You alright?"
        odette "Uhh, yup!"
        odette "Just a {i}really{/i} big fucking cock in my ass..."
        odette "{i}*Ahem*{/i} ... Not a problem."
        anon "You sure?"
        odette @ -m_talk "Mhmm!"
        pause
        anon "So I can go ahead and-"
        odette "YUP!"
        call scene_odette_couch_anal.animate
        with dissolve
        anon "Cool."
        odette "Fuck, fuck, fuck, fuck, fuck..."
    else:

        call scene_odette_couch_back.stage
        with dissolve
        odette "Again?!"
        odette "Seriously?!"
        call scene_odette_couch_anal.stage
        with fade
        anon "I can't decide which hole I like more..."
        odette "Heh, you're lucky I'm a dirty slut..."
        odette "... Pretty sure no other girl would let you get away with-"
        call scene_odette_couch_anal.insert
        odette "Fuuuuuuuuck me!!" with hpunch
        call scene_odette_couch_anal.animate
        with {'master': dissolve}
        anon "That's the plan!"
        odette "Ohmygod, ohmygod, OHMYGOD!!!"

    pause
    jump scene_odette_couch_anal.resume












screen scene_odette_couch_anal_controls():
    style_prefix 'sex'

    vbox:

        frame:
            has hbox
            textbutton _('Keep Going') action Return(False)
            textbutton _('Cum') action Return('inside')
            textbutton _('Switch') action Return('switch')

        frame:
            has hbox
            textbutton _('« Slower'):
                action (Function(M_odette.set, 'sex speed',
                                 1 / (1 / M_odette.get('sex speed') - 2)),
                        Return(False))
                sensitive M_odette.get('sex speed') < 1 / 8.
            textbutton _('Faster »'):
                action (Function(M_odette.set, 'sex speed',
                                 1 / (1 / M_odette.get('sex speed') + 2)),
                        Return(False))
                sensitive M_odette.get('sex speed') > 1 / 16.
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
