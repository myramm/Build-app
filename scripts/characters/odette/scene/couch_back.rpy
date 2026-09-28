label scene_odette_couch_back:

    return


label scene_odette_couch_back.stage:
    scene location_tattoo_garage_sex_couch
    show odette_sex_couch_back_base as anim
    show odette_sex_couch_back_base_anon as legs
    show odette sex_couch_back
    show odette_sex_couch_back_pre as overlay
    return


label scene_odette_couch_back.insert:
    hide legs
    show odette_sex_couch_back_insert as overlay
    return


label scene_odette_couch_back.animate:
    hide odette
    hide overlay
    show odette_sex_couch_back as anim
    return


label scene_odette_couch_back.loop:
    call screen scene_odette_sex_couch_controls

    if _return:
        return _return

    python hide:
        blocks = 5
        limit = 3

        renpy.dynamic(pool=random.sample(range(2 - limit, blocks + 1), limit))

    pause

    while pool:
        call scene_odette_couch_back.dialogue (pool.pop(), rng=random.random())
        pause

    jump scene_odette_couch_back.loop


label scene_odette_couch_back.dialogue(opt, rng=-1):

    if opt == 1:
        odette "Oooh, yeah..."
        odette "... That's it, big fella."

    elif opt == 2:
        odette "Nice and deep..."
        odette "... Just like that!"

    elif opt == 3:
        if rng < .5:
            odette "Fuck!"

        anon "Phew, you weren't kidding..."
        odette "Hmm?"
        anon "... Just look at those things go!"
        odette "Oh, hehe!"

    elif opt == 4:
        odette "Oof!" with hpunch

        if rng < 0:
            odette "What was that?!"
            anon "Sorry."
            anon "I'm just trying to see how high I can make them bounce."

        odette "{b}[firstname]{/b}, stop fooling around and focus!"
        anon "I can't help it, they're mesmerizing."

        if rng < .5:
            odette "C'mon, I was nearly there!"

    elif opt == 5:
        odette "Ahh!"
        odette "So fucking deep!"

        if rng < .5:
            anon "You like that?"
            odette "Yes!"

    elif opt == 5:
        odette "Fuck, {b}Eve{/b} is so lucky..."
        odette "... I can't believe her first boyfriend and she's got a dick this good!"

        if rng < .5:
            anon "Dick you're technically stealing from her."
            odette "Not stealing..."
            odette "... Borrowing!"
            anon "Mhmm."

    elif opt == 6:
        odette "Faster, big fella!"

    return


label scene_odette_couch_back.cum(where):
    odette "I'm getting close!"
    anon "Me too!"
    odette "Harder, {b}[firstname]{/b}!!"
    anon "I'm trying but-"
    anon "I can't-"
    odette "NGGHHH!!!"

    if where == 'inside':
        show odette_sex_couch_back_cum as anim
    else:
        show odette_sex_couch_back_base as anim
        show odette_sex_couch_back_base_anon as legs
        show odette sex_couch_back f_surprised m_talk
        show odette_sex_couch_back_cumshot as cum

    anon "HNNGGG!!!" with flash

    if where == 'inside':
        show xray_left_back as xray with fastdissolve:
            anchor (.5, .5)
            pos (250 + 323, 250 + 96)
            rotate -15
            rotate_pad False
            zoom 1.02

    pause
    hide xray

    if where == 'inside':
        show odette_sex_couch_back_base as anim
        show odette_sex_couch_back_base_anon as legs
        show odette sex_couch_back
        show odette_sex_couch_back_pre as overlay
        show odette_sex_couch_back_pullout as cum
    else:
        show odette -f_surprised

    with {'master': dissolve}
    anon "Haah... Haah..."
    odette -m_talk "Phew, holy fuck that was good!"
    anon "Yeah?"
    odette "Heh, we should be doing this a lot more often!"
    anon "I dunno about that..."

    if where == 'inside':
        call call_pregnancy_minigame (None, M_odette)
    return


label scene_odette_couch_back.switch:
    $ M_odette.set('sex speed', 1 / 8.)
    $ rv.add('vaginal')
    $ renpy.dynamic(switch=True)

    if 'a->v' not in rv:
        $ rv.add('a->v')
        call scene_odette_couch_anal.stage
        with dissolve
        odette "{b}[firstname]{/b}?!"
        odette "I was almost there!!!"
        anon "No worries."
        call scene_odette_couch_back.stage
        with fade
        anon "We're not finished yet!"
        odette "Wait a second..."
        odette "... You're not supposed to double dip, it's-"
        call scene_odette_couch_back.insert
        odette f_surprised "Oh, fuck shit balls!!" with hpunch
        call scene_odette_couch_back.animate
        with {'master': dissolve}
        anon "What's that you were saying?"
        odette "Nothing, nothing..."
        odette "... Keep going!"
    else:

        call scene_odette_couch_anal.stage
        with dissolve
        odette "Again?!"
        odette "Seriously?!"
        call scene_odette_couch_back.stage
        with fade
        anon "I can't decide which hole I like more..."
        odette "Heh, you're lucky I'm a dirty slut..."
        odette "... Pretty sure no other girl would let you get away with-"
        call scene_odette_couch_back.insert
        odette f_surprised "Fuuuuuuuuck me!!" with hpunch
        call scene_odette_couch_back.animate
        with {'master': dissolve}
        anon "That's the plan!"
        odette "Ohmygod, ohmygod, OHMYGOD!!!"

    pause
    jump scene_odette_couch_back.resume


label scene_odette_couch_back.repeat(switch):
    $ M_odette.set('sex speed', 1 / 8.)
    $ renpy.dynamic(rv={'vaginal'})

    call scene_odette_couch_back.stage
    with fade
    anon "Now this is a hell of a view!"
    odette "Heh, just stick it in me already..."
    anon "Hey, you can't hate on a guy for appreciating the scenery!"
    odette "Yeah, well... I can hate on you for teasing me wit-"
    call scene_odette_couch_back.insert
    with {'master': dissolve}
    odette f_lipbite @ -m_talk "Ngh!!"
    anon "Better?"
    odette -f_lipbite "Yes!!"
    call scene_odette_couch_back.animate
    with dissolve
    call scene_odette_couch_back.dialogue (1)
    pause
    call scene_odette_couch_back.dialogue (2)
    pause
    call scene_odette_couch_back.dialogue (3)
    pause
    call scene_odette_couch_back.dialogue (4)
    pause
    call scene_odette_couch_back.dialogue (5)
    pause
    call scene_odette_couch_back.dialogue (6)
    pause

    label scene_odette_couch_back.resume:
    call scene_odette_couch_back.loop

    if _return == 'switch':
        jump scene_odette_couch_anal.switch

    call scene_odette_couch_back.cum (_return)
    return rv


label scene_odette_couch_back.anal:
    jump scene_odette_couch_anal


label scene_odette_couch_back.back:
    call scene_odette_couch_back.repeat ('anal' in variants)
    return


label scene_odette_couch_back.replay:
    $ renpy.dynamic(variants=persistent.cookie_jar['Odette']['variants']['06_unlocked'])

    if len(variants) > 1:
        scene expression background(l=L_tattooparlor_garage, t=2) with fade
        menu:
            "Normal" if 'back' in variants:
                jump scene_odette_couch_back.back

            "First Anal" if 'anal' in variants:
                jump scene_odette_couch_back.anal
    else:

        jump expression 'scene_odette_couch_back.{}'.format(next(iter(variants)))

    return



screen scene_odette_sex_couch_controls():
    style_prefix 'sex'

    vbox:

        frame:
            has hbox
            textbutton _('Keep Going') action Return(False)
            textbutton _('Cum Inside') action Return('inside')
            textbutton _('Cum Outside') action Return('outside')

            if switch:
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
