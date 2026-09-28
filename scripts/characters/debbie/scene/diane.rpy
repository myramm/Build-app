label scene_debbie_diane_bedroom:

    return


label scene_debbie_diane_bedroom.animate:
    show debbie_diane_anim as animation
    return


label scene_debbie_diane_bedroom.loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 3:
        if anim_toggle:
            if not animated:
                show debbie_diane_anim as animation with dissolve
                $ animated = True
            pause 5
            call scene_debbie_diane_bedroom.dialogue
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8,9,10,11,12]
            $ poses_done = []
            while poses_done != pose_list:
                show expression 'debbie_diane_anim {}'.format(pose_list[pose_counter]) as animation
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call scene_debbie_diane_bedroom.dialogue
        $ animcounter += 1
    call screen scene_debbie_diane_bedroom_controls
    if not _return:
        jump scene_debbie_diane_bedroom.loop
    return _return


label scene_debbie_diane_bedroom.dialogue:
    $ renpy.dynamic(rng=renpy.random.random(),
                    slow=M_debbie.get('sex speed') <= 1. / 12)

    if animcounter == 0 and rng <= .66:
        if slow:
            debbie "How do you always find the perfect spot?!{w=2}{nw}"
            diane "Oh, c'mon... we're best friends.{w=2}{nw}"
            diane "If anyone should know your spots, it's me.{w=2}{nw}"
            debbie "Hehe, I guess that makes sense.{w=2}{nw}"
        else:
            diane "Oh, fuck!{w=1}{nw}"
            debbie "Ahh!{w=1}{nw}"
            pause 1
            diane "Oh, {b}[deb_name]{/b}!{w=1}{nw}"
            pause 1
            diane "This feels so amazing!!{w=1}{nw}"
        pause 1

    elif animcounter == 1 and rng <= .33:
        if slow:
            diane "Oh my god, you're sopping wet...{w=1.5}{nw}"
            debbie "{b}Diane{/b}!!{w=1}{nw}"
            debbie "Don't say things like that, you know it embarrasses me!{w=2}{nw}"
            diane "Heh!{w=1}{nw}"
            diane "Yeah, but it excites you too.{w=1.5}{nw}"
            debbie "Ngh!{w=1}{nw}"
            pause .5
            diane "See!{w=1}{nw}"
        else:
            diane "I'm so happy we're close again, like we used to be!!{w=2}{nw}"
            debbie "Me too!{w=1}{nw}"
            diane "I missed you so much, {b}[deb_name]{/b}!{w=2}{nw}"
            debbie "Ahh!!{w=1}{nw}"
            debbie "Don't stop!!{w=1}{nw}"
        pause 1

    elif animcounter == 1 and rng <= .66:
        if slow:
            diane "I love teasing your wet little pussy, {b}[deb_name]{/b}...{w=2}{nw}"
        else:
            diane "Are you gonna cum for me?{w=1.5}{nw}"
            debbie "Yes!!!{w=1}{nw}"

    elif animcounter == 2 and rng <= .66:
        if slow:
            diane "Mmm.{w=1}{nw}"
            diane "You like that?{w=1}{nw}"
            debbie "Y-yes.{w=1}{nw}"
            diane "You like it when our pussies rub together?{w=2}{nw}"
            debbie "I do.{w=1}{nw}"
            pause 1
            diane "Tell me you love it!{w=1.5}{nw}"
            debbie "I love it!{w=1}{nw}"
            diane "C'mon, babe... you can do better than that...{w=2}{nw}"
            debbie "Ahh, I love it when our pussies rub together, {b}Diane{/b}!{w=2}{nw}"
            diane "Fuck, me too!{w=1}{nw}"
        else:
            debbie "Ngh, god!{w=1}{nw}"
            debbie "I'm getting close, {b}Diane{/b}!{w=1.5}{nw}"
            diane "Me too!{w=1}{nw}"
            pause
            debbie "Fuuuuck!!{w=1}{nw}"
        pause 1

    return


label scene_debbie_diane_bedroom.cum:
    debbie "Ahh, {b}Diane{/b}!!"
    debbie "I'm gonna cum!!"
    diane "Cum with me!!"
    pause
    diane "I love you, {b}[deb_name]{/b}!"
    diane "You're my best friend in the whole world!"
    debbie "I love you toooo!!"
    show debbie_body_b_sex_lesb_cum as animation
    diane "NGGHHH!!!" with flash
    debbie "NGGHHH!!!"
    pause
    show debbie_body_b_sex_lesb_fall as animation with dissolve
    diane "Haah... Haah..."
    pause
    diane "Well, that was-"
    pause
    debbie "Strenuous?"
    diane "Heh, yeah."
    debbie "Hehehe!"
    return


label scene_debbie_diane_bedroom.repeat:
    python:
        renpy.dynamic(anim_toggle=True, animated=True)
        M_debbie.set('sex speed', 1 / 8.)

    scene location_home_debbiesidebed_lesb
    call scene_debbie_diane_bedroom.animate
    with fade
    call scene_debbie_diane_bedroom.loop
    call scene_debbie_diane_bedroom.cum
    return


label scene_debbie_diane_bedroom.replay:
    jump scene_debbie_diane_bedroom.repeat


screen scene_debbie_diane_bedroom_controls():
    style_prefix 'sex'

    vbox:

        frame:
            has hbox
            textbutton _('Keep Going') action Return(False)
            textbutton _('Climax') action Return(True)

        frame:
            has hbox
            textbutton _('« Slower'):
                action (Function(M_debbie.set, 'sex speed',
                                 1 / (1 / M_debbie.get('sex speed') - 2)),
                        Return(False))
                sensitive M_debbie.get('sex speed') < 1 / 8.
            textbutton _('Faster »'):
                action (Function(M_debbie.set, 'sex speed',
                                 1 / (1 / M_debbie.get('sex speed') + 2)),
                        Return(False))
                sensitive M_debbie.get('sex speed') > 1 / 16.
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
