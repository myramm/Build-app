label scene_eve_sex_wake:

    return


label scene_eve_sex_wake.stage:
    scene location_tattoo_bedroom_sex_wakeup
    show eve sex_wake trans
    if gender == 'cis':
        show eve cis -trans
    if anal:
        show eve anal
    return


label scene_eve_sex_wake.animate:
    hide eve
    show eve_sex_wake_anim trans
    if gender == 'cis':
        show eve_sex_wake_anim cis -trans
    if anal:
        show eve_sex_wake_anim anal
    return


label scene_eve_sex_wake.loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 3:
        if anim_toggle:
            if not animated:
                call scene_eve_sex_wake.animate
                $ animated = True
            pause 5
            call scene_eve_sex_wake.dialogue
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "eve_sex_wake_anim {} {} {}".format(
                    gender, 'anal' if anal else '', pose_list[pose_counter]) as eve_sex_wake_anim
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call scene_eve_sex_wake.dialogue
        $ animcounter += 1
    call screen scene_eve_sex_wake_controls(gender, anal)
    if not _return:
        jump scene_eve_sex_wake.loop
    return _return


label scene_eve_sex_wake.dialogue:
    $ renpy.dynamic(rng=renpy.random.random())

    if animcounter == 0 and rng <= .33:
        eve "Fuuuuck!{w=1}{nw}"

    elif animcounter == 0 and rng <= .55:
        anon "Is it too deep?{w=1}{nw}"
        eve "No.{w=1}{nw}"
        anon "Are you sure?{w=1}{nw}"
        eve "Y-yes!{w=1}{nw}"
        eve "Ah, fuck!!{w=1}{nw}"

    elif animcounter == 1 and rng <= .33:
        anon "Does that feel good?{w=1.5}{nw}"
        eve "Yes!!{w=1}{nw}"

    elif animcounter == 1 and rng <= .66:
        anon "Is that okay?{w=1}{nw}"
        eve "Mhmm!{w=1}{nw}"
        anon "It feels good?{w=1}{nw}"
        eve "Yes!!{w=1}{nw}"

    elif animcounter == 1 and rng <= .88 and gender == 'cis':
        anon "I can't believe how wet you're getting!{w=2}{nw}"
        eve "{i}*Whimpers*{/i}{w=1}{nw}"

    elif animcounter == 1 and rng <= .88 and gender == 'trans':
        anon "I love watching your girldick bounce when I fuck you...{w=2.5}{nw}"
        eve "{i}*Whimpers*{/i}{w=1}{nw}"
        anon "... It's so adorable!{w=1}{nw}"

    elif animcounter == 2 and rng <= .22 and anal:
        anon "Your ass is amazing, {b}Eve{/b}!{w=2}{nw}"
        eve "Ahh!{w=1}{nw}"
        pause 1
        anon "It's so tight!{w=1}{nw}"
        eve "Oh, {b}[firstname]{/b}!!{w=1}{nw}"

    elif animcounter == 2 and rng <= .33:
        eve "It's so fucking deep!{w=1.5}{nw}"
        eve "Ahh!{w=1}{nw}"
        pause 1
        eve "Oh, {b}[firstname]{/b}!!{w=1}{nw}"

    elif animcounter == 2 and rng <= .55:
        eve "I love you, {b}[firstname]{/b}!{w=1}{nw}"
        pause 1
        eve "I love you so fucking-{w=1.5}{nw}"
        eve "... Ngh, MUCH!!{w=1}{nw}"

    return


label scene_eve_sex_wake.anal:
    call scene_eve_sex_wake.stage
    show eve insert lipbite
    with {'master': dissolve}
    anon "Can I put it in your ass again?"
    show eve embarrassed
    with {'master': fastdissolve}
    eve "I don't care where you put it, just hurry!"
    eve "Please!"
    $ anal = True
    show eve anal lipbite
    with {'master': dissolve}
    anon "Alright."
    show eve slam
    eve "!!!" with hpunch
    eve "AHH!"
    jump scene_eve_sex_wake.resume


label scene_eve_sex_wake.vaginal:
    call scene_eve_sex_wake.stage
    show eve insert lipbite
    with {'master': dissolve}
    anon "Can I swap back?"
    show eve embarrassed
    with {'master': fastdissolve}
    eve "Just do me already!"
    eve "Please!"
    $ anal = False
    show eve -anal lipbite
    with {'master': dissolve}
    anon "Alright."
    show eve slam
    eve "!!!" with hpunch
    eve "Ngghhh!"
    jump scene_eve_sex_wake.resume


label scene_eve_sex_wake.cum(where):
    anon "I'm getting close!"
    eve "Me too!"
    pause
    eve "Oh, fuck!"
    eve "Oh, fuck me!!"
    pause
    eve "Haah!"
    pause

    if gender == 'trans':
        $ AnimatedImage2.signal(-1)

    eve "NGGHHH!!!" with flash
    pause

    if gender == 'cis':
        eve "Ohhh!"
    else:

        eve "Oh, no..."
        anon "Wow, did you just-"
        eve "{b}*Whimpers*{/b}"

    anon "You are so sexy, {b}Eve{/b}!"
    anon "I'm gonna-"

    call scene_eve_sex_wake.stage

    if where == 'inside':
        show eve cum
    else:
        show eve cumshot gasp

    anon "HNNGGG!!!" with flash





    pause
    hide xray

    if where == 'inside':
        show eve pullout
    else:
        show eve after outside

    show eve lipbite
    with {'master': dissolve}
    anon "Haah... Haah..."

    if where == 'inside':
        show eve after inside
        with {'master': dissolve}

    if gender == 'trans':
        eve surprised "I can't believe I did that..."
        anon "Hmm?"
        eve "I'm so embarrassed... I-"
        anon "Don't be embarrassed!"
        anon "That was awesome!"
        show eve embarrassed
        with {'master': dissolve}
        eve "Heh, really?"
        anon "Oh my god, yes!"
        pause
    else:

        eve horny "Oh, wow!"
        eve "That was-"
        pause
        eve "Wow."
        show eve laugh
        with {'master': fastdissolve}
        eve "Hehehe!"

        if where == 'inside':
            anon "Hehe!"

            if not anal:
                call call_pregnancy_minigame (None, M_eve)

            return

    show eve horny
    with {'master': fastdissolve}
    pause
    eve "That's not the type of shower I usually take in the mornings..."
    anon "Hehe!"
    show eve laugh
    with {'master': fastdissolve}
    eve "Hehehe!"
    show eve horny
    with {'master': fastdissolve}
    pause
    anon "Let me get you a towel."
    eve "Yeah, thanks."
    return


label scene_eve_sex_wake.repeat(gender, anal=True):
    python:
        renpy.dynamic(anim_toggle=True, animated=True,
                      animcounter=0, animstate=None)
        M_eve.set('sex speed', 1 / 8.)
        anal = gender == 'trans' or (False if anal else None)

    call scene_eve_sex_wake.stage
    with fade
    anon "Wow, now that's a view I would happily wake up to every morning!"
    eve "Ngh, don't tease me..."

    if gender == 'cis':
        eve "... I'm so wet for you."
    else:
        eve "... I'm so hard for you."

    anon "Yeah, I can see that."
    show eve insert
    with {'master': dissolve}
    eve "I want you inside me!"

    if gender == 'cis':
        show eve lipbite
        with {'master': fastdissolve}
        anon "Alright."
        show eve slam
        eve "!!!" with hpunch
    else:

        show eve embarrassed
        with {'master': fastdissolve}
        eve "Just go slow..."
        eve "... I'm getting used to it but you're so damn big."
        show eve lipbite
        with {'master': fastdissolve}
        anon "I will."
        show eve enter
        with {'master': dissolve}
        eve "!!!"

    eve "Fuuuuck!"
    label scene_eve_sex_wake.resume:
    call scene_eve_sex_wake.animate
    with dissolve
    call scene_eve_sex_wake.loop
    if _return == 'switch':
        if anal:
            jump scene_eve_sex_wake.vaginal
        else:
            jump scene_eve_sex_wake.anal
    call scene_eve_sex_wake.cum (_return)
    return


label scene_eve_sex_wake.replay:
    $ renpy.dynamic(variants=persistent.cookie_jar['Eve']['variants']['07_unlocked'])

    if variants >= {'cis', 'trans'}:
        scene expression background(l=L_tattooparlor_bedroom) with fade
        menu:
            "Cis" if 'cis' in variants:
                call scene_eve_sex_wake.repeat ('cis', 'cis anal' in variants)

            "Trans" if 'trans' in variants:
                call scene_eve_sex_wake.repeat ('trans')
    else:

        call scene_eve_sex_wake.repeat (next(iter(variants)), True)

    return


screen scene_eve_sex_wake_controls(gender, anal):
    style_prefix 'sex'

    vbox:

        frame:
            has hbox
            textbutton _('Keep Going') action Return(False)
            textbutton _('Cum Inside') action Return('inside')
            textbutton _('Cum Outside') action Return('outside')
            if gender == 'cis':
                if anal is True:
                    textbutton _('Vaginal') action Return('switch')
                elif anal is False:
                    textbutton _('Anal') action Return('switch')

        frame:
            has hbox
            textbutton _('« Slower'):
                action (Function(M_eve.set, 'sex speed',
                                 1 / (1 / M_eve.get('sex speed') - 2)),
                        Return(False))
                sensitive M_eve.get('sex speed') < 1 / 8.
            textbutton _('Faster »'):
                action (Function(M_eve.set, 'sex speed',
                                 1 / (1 / M_eve.get('sex speed') + 2)),
                        Return(False))
                sensitive M_eve.get('sex speed') > 1 / 16.
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
