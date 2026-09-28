label scene_josie_sex_chair:

    return


label scene_josie_sex_chair.stage:
    scene location_dealership_lounge_chair_sex
    show josephine_sex_chair_base as anim
    show josephine_sex_chair_arm_after as arm
    show josephine_sex_chair_dick_base as penis
    show josephine sex_chair
    return


label scene_josie_sex_chair.insert:
    show josephine_sex_chair_arm_insert as arm
    hide penis
    return


label scene_josie_sex_chair.animate:
    hide arm
    hide josephine
    show josie_sex_chair as anim behind stage
    return


label scene_josie_sex_chair.loop:
    call screen scene_josie_sex_chair_controls

    if _return:
        return _return

    python hide:
        blocks = 5
        limit = 3

        renpy.dynamic(pool=random.sample(range(2 - limit, blocks + 1), limit))

    pause

    while pool:
        call scene_josie_sex_chair.dialogue (pool.pop(), rng=random.random())
        pause

    jump scene_josie_sex_chair.loop


label scene_josie_sex_chair.dialogue(opt, rng=-1):

    if opt == 1:
        josephine "Oh, shit!!"

    elif opt == 2:
        anon "There we go."
        josephine "Ahh!"

        if rng < 0:
            anon "Perfect."

    elif opt == 3:
        anon "I can't believe you're into this stuff."

        if rng < 0:
            josephine "What do you mean?"
            anon "Animated porn games."

        josephine "I think it's funny."
        anon "Oh, is this where you tell me you only play it for the story?"

        if rng < 0:
            josephine "Umm, yeah."
            pause

        josephine "Or you know, when I'm really bored and I wanna cum."

        if rng < .5:
            anon "I knew it!"

    elif opt == 4:
        anon "This music is horrible."
        josephine "I dunno, I kinda like it."
        anon "You are such a troll."
        josephine "Damn right."

    elif opt == 5:
        if rng < 0:
            josephine "Tch, careful back there!"

        anon "Am I pulling too hard?"
        josephine "No, the hair pulling is great."

        if rng < 0:
            josephine "Just pretty sure you're dick punching me in the kidney."
            anon "Oh, sorry."

    return


label scene_josie_sex_chair.cum(where):
    anon "Are you getting close?"
    josephine "Mhmm!"
    anon "Good because I'm about two seconds away from popping off!"
    pause
    anon "Here..."
    anon "... it..."
    anon "... COMES!!"

    if where == 'inside':
        show josephine_sex_chair_cum as anim
    else:
        show josephine_sex_chair_base as anim
        show josephine_sex_chair_arm_after as arm
        show josephine_sex_chair_dick_base as penis
        show josephine_sex_chair_cumshot as cum
        show josephine_sex_chair_hair_after as hair
        show josephine sex_chair f_lipbite

    anon "HNNGGG!!!" with flash

    if where == 'inside':
        show xray_front_top as xray:
            anchor (.5, .5)
            pos (250 + 173, 250 + 138)
            rotate 90
            rotate_pad False
            xzoom -1
            zoom .92
        with {'master': fastdissolve}
        josephine "NGGHHH!!!"
    else:
        josephine @ -m_talk "Mmm."

    pause
    hide xray

    if where == 'inside':
        show josephine_sex_chair_base as anim
        show josephine_sex_chair_arm_after as arm
        show josephine_sex_chair_dick_base as penis
        show josephine_sex_chair_dick_after as cum
        show josephine_sex_chair_hair_after as hair
        show josephine sex_chair

    with {'master': dissolve}
    anon "Haah... Haah..."
    show josephine -f_lipbite
    anon "Now that's gotta be the best way to watch an art stream!"
    josephine "You're a dork."
    anon "Yeah, but you love it."
    josephine f_happy "{i}*Sigh*{/i} I kinda do, yeah."

    if where == 'inside':
        call call_pregnancy_minigame (None, M_josie)
    return where


label scene_josie_sex_chair.repeat:
    $ M_josie.set('sex speed', 1 / 8.)

    call scene_josie_sex_chair.stage
    with fade
    josephine "Can you see?"
    anon "No, your head is in the way."
    josephine "Hold on."
    call scene_josie_sex_chair.insert
    with {'master': dissolve}
    anon "Don't worry, I've got it."
    josephine f_curious_back @ -m_talk "Hmm?"
    call scene_josie_sex_chair.animate
    with dissolve
    call scene_josie_sex_chair.dialogue (1)
    pause
    call scene_josie_sex_chair.dialogue (2)
    pause
    call scene_josie_sex_chair.dialogue (3)
    pause
    anon "Now who are the other two guys that are talking?"
    josephine "Oh, one of them is the coder for the team..."
    josephine "... And the other is the writer."
    josephine "{b}Darkcookie{/b} has them come on to answer fan questions every once in a while."
    anon "That's pretty neat."
    josephine "Yeah, except it's usually a trap and he spends the entire time bullying the shit out of them."
    anon "Really?"
    josephine "Heh, yeah."
    pause
    call scene_josie_sex_chair.dialogue (4)
    pause
    josephine "C'mon, {b}[firstname]{/b}..."
    josephine "... Fuck my troll pussy!"
    anon "Eugh, please don't ever say that again."
    josephine "Haha!"
    pause
    call scene_josie_sex_chair.dialogue (5)
    pause

    call scene_josie_sex_chair.loop
    call scene_josie_sex_chair.cum (_return)
    return _return


label scene_josie_sex_chair.replay:
    jump scene_josie_sex_chair.repeat


screen scene_josie_sex_chair_controls():
    style_prefix 'sex'

    vbox:

        frame:
            has hbox
            textbutton _('Keep Going') action Return(False)
            textbutton _('Cum Inside') action Return('inside')
            textbutton _('Cum Outside') action Return('outside')

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
