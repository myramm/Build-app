label scene_jenny_sex_pregnant:
    call scene_jenny_sex_pregnant.stage
    with fade
    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"
    jenny "Thee, ahh tord eww is ood bring in oons of morney!"
    anon "Yeah, that's not the part I had a problem with..."
    jump scene_jenny_sex_pregnant.resume


label scene_jenny_sex_pregnant.stage:
    scene location_home_jennybedroom_sex_preg as stage
    show jenny_sex_preg_pre as animation
    show jenny_sex_preg_insert as dick
    return


label scene_jenny_sex_pregnant.animate:
    hide dick
    show jenny_sex_preg_anim as animation
    return


label scene_jenny_sex_pregnant.loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 3:
        if anim_toggle:
            if not animated:
                call scene_jenny_sex_pregnant.animate
                $ animated = True
            pause 5
            call scene_jenny_sex_pregnant.dialogue
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8,9]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "jenny_sex_preg_anim {}".format(pose_list[pose_counter]) as animation
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call scene_jenny_sex_pregnant.dialogue
        $ animcounter += 1
    call screen scene_jenny_sex_pregnant_controls
    if not _return:
        jump scene_jenny_sex_pregnant.loop
    return _return


label scene_jenny_sex_pregnant.dialogue:
    $ renpy.dynamic(rng=renpy.random.random())

    if animcounter == 0 and rng <= .33:
        jenny "Oh, at 'eels oh 'ucking good!{w=1.5}{nw}"

    elif animcounter == 0 and rng <= .66:
        jenny "NGGHHH!!!{w=1}{nw}"

    elif animcounter == 0:
        jenny "Oh my god, oh my god, OH MY GOD!!!{w=1.5}{nw}"

    elif animcounter == 1 and rng <= .33:
        jenny "Mmm, ood damn!{w=1}{nw}"
        pause 1
        jenny "It's so 'ucking 'eep!{w=1}{nw}"

    elif animcounter == 1 and rng <= .66:
        jenny "Eww 'iking iss boys?{w=1}{nw}"
        "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}{w=1}{nw}"

    elif animcounter == 2 and rng <= .33:
        jenny "Uhh, 'iss baby isn' 'ettin up!{w=1.5}{nw}"
        anon "Still?!{w=1}{nw}"
        jenny "Yeah, an you 'eel it kicking yet?{w=1.5}{nw}"

    elif animcounter == 2 and rng <= .44:
        jenny "Don't stop!{w=1}{nw}"
        jenny "I'm 'onna cum again!!{w=1}{nw}"
        anon "Wow, again?!{w=1}{nw}"
        jenny "OH MUH GOD! YES!!!{w=1}{nw}"
        "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}{w=1}{nw}"
        pause 1
        jenny "NGGHHH!!!{w=2}{nw}" with flash
        "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}{w=1}{nw}"

    return


label scene_jenny_sex_pregnant.cum:
    anon "Here it comes!"
    jenny "Yes!!"
    anon "Where do you want it?"
    jenny "YES!!!"
    anon "{b}[jen_name]{/b}?!"
    jenny "My belly!!"
    jenny "My-"
    jenny "NGGHHH!!!"
    show jenny_sex_preg_cum as animation
    show jenny_sex_preg_cumshot as dick
    anon "HNNGGG!!!" with flash
    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"
    hide dick
    show jenny_sex_preg_after as animation
    anon "Hurggk!!" with vpunch
    pause
    anon "Haah... haah..."
    pause
    anon "{b}[jen_name]{/b}?"
    pause
    anon "You okay?"
    jenny "{i}*Mumbles incoherently*{/i}"
    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"
    anon "Umm, what?"
    pause
    anon "{b}[jen_name]{/b}?!"
    jenny "Ugh... shushit..."
    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"
    return


label scene_jenny_sex_pregnant.repeat:
    call scene_jenny_sex_pregnant.stage
    with fade
    jenny "Try nnt ew cum ew 'ast!"
    anon "Yeah, speak for yourself..."

    label scene_jenny_sex_pregnant.resume:
    python:
        renpy.dynamic(anim_toggle=True, animated=True)
        M_jenny.set('sex speed', 1 / 8.)

    jenny "Ahh, fuck!!!"
    jenny "Oh!"
    pause
    call scene_jenny_sex_pregnant.animate
    with dissolve
    jenny "Oh, at 'eels oh 'ucking good!"
    pause
    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"
    jenny "Mmm, 'od damn!"
    pause
    jenny "It's so 'ucking 'eep!"
    jenny "I'm gonna cum already!"
    pause
    jenny "NGGHHH!!!" with flash
    pause
    jenny "Oh my god, oh my god, OH MY GOD!!!"
    pause
    jenny "Eww 'iking is boys?"
    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"
    pause
    jenny "Uhh baby is going crazy in 'ere!"
    anon "Really?"
    jenny "Yeah, an you 'eel it kicking?"
    pause
    jenny "Don't stop!"
    jenny "I'm 'onna cum again!!"
    anon "Wow, again?!"
    jenny "YES!!!"
    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"
    pause
    jenny "NGGHHH!!!" with flash
    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"
    pause
    jenny "Are eww 'etting close yet?"
    anon "Kinda."
    pause
    jenny "Well, 'urry up!!"
    jenny "I 'unno if I can-"
    $ M_jenny.set('sex speed', 1 / 14.)
    with vpunch
    jenny "OH, FUCK!!!"
    call scene_jenny_sex_pregnant.loop
    call scene_jenny_sex_pregnant.cum
    return


label scene_jenny_sex_pregnant.replay:
    jump scene_jenny_sex_pregnant.repeat


screen scene_jenny_sex_pregnant_controls():
    style_prefix 'sex'

    vbox:

        frame:
            has hbox
            textbutton _('Keep Going') action Return(False)
            textbutton _('Cum') action Return('outside')

        frame:
            has hbox
            textbutton _('« Slower'):
                action (Function(M_jenny.set, 'sex speed',
                                 1 / (1 / M_jenny.get('sex speed') - 2)),
                        Return(False))
                sensitive M_jenny.get('sex speed') < 1 / 8.
            textbutton _('Faster »'):
                action (Function(M_jenny.set, 'sex speed',
                                 1 / (1 / M_jenny.get('sex speed') + 2)),
                        Return(False))
                sensitive M_jenny.get('sex speed') > 1 / 16.
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
