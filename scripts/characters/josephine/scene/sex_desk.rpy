label scene_josie_sex_desk:

    return


label scene_josie_sex_desk.stage:
    scene location_dealership_office_desk_sex
    show josephine_sex_top_insert as anim
    show josephine sex_top
    return


label scene_josie_sex_desk.insert:
    hide josephine
    show josephine_sex_top_slide as anim
    return


label scene_josie_sex_desk.animate:
    show josie_sex_desk as anim
    return


label scene_josie_sex_desk.loop:
    call screen scene_josie_sex_desk_controls

    if _return:
        return _return

    python hide:
        blocks = 7
        limit = 3

        renpy.dynamic(pool=random.sample(range(2 - limit, blocks + 1), limit))

    pause

    while pool:
        call scene_josie_sex_desk.dialogue (pool.pop(), rng=random.random())
        pause

    jump scene_josie_sex_desk.loop


label scene_josie_sex_desk.dialogue(opt, rng=-1):

    if opt == 1:
        josephine "Geez, this is a fucking workout!"

        if rng < .5:
            anon "Really?"

        anon "I'm quite comfortable."
        josephine "Hah hah... very funny."

    elif opt == 2:
        josephine "Okay, now I'm starting to sweat..."

        if rng < .5:
            josephine "... Maybe you should get on top for a while?"

        anon "A little sweat isn't going to kill you."
        josephine "Grrraah."

    elif opt == 3:
        anon "Phew, yeah!"
        anon "Bounce that ass, {b}Josephine{/b}!"

    elif opt == 4:
        josephine "You know..."
        josephine "... this is..."
        josephine "... really..."
        josephine "... Ngh, {i}hard{/i}!"
        anon "Heh... Yeah, it is."

        if rng < .5:
            josephine "I'm not talking about your dick, {b}[firstname]{/b}!"

    elif opt == 5:
        anon "Yeah, that's it."
        anon "Work that big cock!"
        josephine "Ngh, fuck!"

    elif opt == 6:
        josephine "I hope you're appreciating this!"
        anon "Oh, I am."

        if rng < .5:
            anon "Keep going!"

    elif opt == 7:
        josephine "Gah!"
        josephine "It keeps bottoming out."
        anon "I can feel it."

        if rng < .5:
            josephine "I don't think I can take much more!"

    return


label scene_josie_sex_desk.switch:
    $ M_josie.set('sex speed', 1 / 8.)

    anon "You wanna get on top again?"
    josephine "Not really."
    call scene_josie_sex.insert ('fast')
    show josephine -f_moan
    with {'master': dissolve}
    anon "C'mon, please?"
    pause
    josephine "Ugh, fine..."

    call scene_josie_sex_desk.stage
    with fade
    anon "You have such a cute little butt on you!"
    josephine "Umm, okay?"
    call scene_josie_sex_desk.insert
    with {'master': dissolve}
    josephine "{i}*Ittthhh*{/i}"
    anon "Fuck me!"
    call scene_josie_sex_desk.animate
    with dissolve
    jump scene_josie_sex_desk.resume


label scene_josie_sex_desk.inside:
    josephine "Come on, {b}[firstname]{/b}!"
    josephine "I wanna feel it inside me!!"
    pause
    josephine "Ah, fuck!!"
    show josephine_sex_top_cum as anim
    anon "HNNGGG!!!" with flash
    show xray_under as xray:
        anchor (.5, .5)
        pos (250 + 262, 250 + 147)
        rotate -66
        rotate_pad False
        xzoom -1
        zoom .72
    with {'master': fastdissolve}
    pause
    hide xray
    anon "Haah... Haah..."
    josephine "Haah... Haah..."
    pause
    anon "I think you can get off me now."
    josephine "Heh, shut up!"
    show josephine_sex_top_pullout as anim
    show josephine sex_top
    show josephine_sex_top_after_dick1 as penis
    show josephine_sex_top_pullout_creampie1 as cum
    with {'master': dissolve}
    josephine "Jesus, it's like trying to climb off a fence post."
    anon "Haha!"
    show josephine_sex_top_after_dick2 as penis
    show josephine_sex_top_pullout_creampie2 as cum
    show josephine_sex_top_pussy_closed as pussy behind penis
    with {'master': dissolve}
    josephine "Holy crap."
    anon "Oh, that's a nice view."
    pause

    call call_pregnancy_minigame (None, M_josie)
    return 'inside'


label scene_josie_sex_desk.outside:
    anon "Oh, here it comes!"
    pause
    anon "Here it-"
    show josephine_sex_top_fall as anim
    show josephine_sex_top_rope1 as rope1
    anon "HNNGGG!!!" with flash
    show josephine_sex_top_after as anim
    show josephine b_sex_top f_angry_closed
    show josephine_sex_top_after_arm_down as arm
    show josephine_sex_top_cumshot3 as rope1
    show josephine_sex_top_dick3 as penis
    with {'master': fastdissolve}
    josephine "Waaagh!" with vpunch
    show josephine f_annoyed_behind
    pause
    josephine "{b}[firstname]{/b}, what the fu-"
    hide penis
    show josephine_sex_top_rope2 as rope2
    show josephine f_surprised_down_more
    anon "NGGHHH!!!"
    show josephine_sex_top_cumshot6 as rope2
    show josephine_sex_top_dick3 as penis
    show josephine f_angry_closed
    with {'master': fastdissolve}
    josephine "!!!" with hpunch
    pause
    show josephine_sex_top_after_dick2 as penis
    with {'master': dissolve}
    anon "Haah... Haah..."
    show josephine f_annoyed_down_blink
    with {'master': dissolve}
    pause
    josephine @ f_annoyed_back_blink "Are you fucking kidding me?!"
    anon "That."
    anon "Was."
    anon "AWESOME!"
    josephine @ f_annoyed_back_blink "Pfft, for you maybe..."
    pause
    return 'outside'


label scene_josie_sex_desk.repeat:
    $ M_josie.set('sex speed', 1 / 8.)
    $ renpy.dynamic(rv=set())

    call scene_josie_sex_desk.stage
    with fade
    josephine "Geez, this thing is not easy to sit on..."
    josephine "Here we-"
    call scene_josie_sex_desk.insert
    with {'master': dissolve}
    josephine "{i}*Ittthhh*{/i}"
    anon "Oh, yeah... that's nice!"
    call scene_josie_sex_desk.animate
    with dissolve
    pause
    anon "Umm, should you really be on your phone while we're doing this?"
    josephine "Hmm?"
    anon "I'm just worried you're gonna fall off the desk or something..."
    josephine "Oh, Relax, bowl cut..."
    josephine "... It's a big desk..."
    josephine "... I'm not gonna fall of!"
    anon "Oh kay."
    pause
    anon "What are you doing on that thing anyway?"
    josephine "Texting with my old colleague at the clothing store."
    anon "You're texting?!"
    josephine "Mhmm."
    pause
    anon "Pretty sure you're not supposed to text while operating heavy machinery."
    josephine "Heh, oh please!"
    josephine "Your dick does not count as heavy machinery, {b}[firstname]{/b}."
    anon "It doesn't?"
    pause
    call scene_josie_sex_desk.dialogue (1)
    pause
    call scene_josie_sex_desk.dialogue (2)
    pause
    call scene_josie_sex_desk.dialogue (3)
    pause
    call scene_josie_sex_desk.dialogue (4)
    pause
    call scene_josie_sex_desk.dialogue (5)
    pause
    call scene_josie_sex_desk.dialogue (6)
    pause
    call scene_josie_sex_desk.dialogue (7)
    pause

    label scene_josie_sex_desk.resume:
    call scene_josie_sex_desk.loop
    if _return == 'switch':
        jump scene_josie_sex.switch

    anon "Oh, man..."
    anon "... I'm getting close!"
    josephine "Do it!"
    pause
    josephine "Hurry, I can't keep this up!"

    if _return == 'inside':
        jump scene_josie_sex_desk.inside

    jump scene_josie_sex_desk.outside


label scene_josie_sex_desk.replay:
    jump scene_josie_sex_desk.repeat


screen scene_josie_sex_desk_controls():
    style_prefix 'sex'

    vbox:

        frame:
            has hbox
            textbutton _('Keep Going') action Return(False)
            textbutton _('Cum Inside') action Return('inside')
            textbutton _('Cum Outside') action Return('outside')
            textbutton _('Switch') action Return('switch')

        frame:
            has hbox
            textbutton _('« Slower'):
                action (Function(M_josie.set, 'sex speed',
                                 1 / (1 / M_josie.get('sex speed') - 2)),
                        Return(False))
                sensitive M_josie.get('sex speed') < 1 / 8.
            textbutton _('Faster »'):
                action (Function(M_josie.set, 'sex speed',
                                 1 / (1 / M_josie.get('sex speed') + 2)),
                        Return(False))
                sensitive M_josie.get('sex speed') > 1 / 16.
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
