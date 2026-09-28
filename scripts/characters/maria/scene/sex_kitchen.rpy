image maria_sex_kitchen_normal = AnimatedImage("maria_kitchen_sex", (3,4,5,6,7,1,2), M_maria)
image maria_sex_kitchen_pregnant = AnimatedImage("maria_kitchen_sex_preggo", (3,4,5,6,7,1,2), M_maria)


label scene_maria_sex_kitchen:

    return


label scene_maria_sex_kitchen.animate(pregnant=False):
    python:
        anim_toggle = True
        animated = True
        M_maria.set('sex speed', .12)
    if pregnant:
        show maria_sex_kitchen_pregnant as animation
    else:
        show maria_sex_kitchen_normal as animation
    hide maria
    with dissolve
    return


label scene_maria_sex_kitchen.loop(pregnant=False):
    while True:
        show screen sex_anim_buttons
        pause
        hide screen sex_anim_buttons
        $ animcounter = 0
        while animcounter < 3:
            if anim_toggle:
                if not animated:
                    if pregnant:
                        show maria_sex_kitchen_pregnant as animation
                    else:
                        show maria_sex_kitchen_normal as animation
                    $ animated = True
                pause 5
                call scene_maria_sex_kitchen.dialogue
                pause 3
            else:

                $ pose_counter = 0
                $ pose_list = [3,4,5,6,7,1,2]
                $ poses_done = []
                while poses_done != pose_list:
                    if pregnant:
                        show expression "maria_kitchen_sex_preggo {}".format(pose_list[pose_counter]) as animation
                    else:
                        show expression "maria_kitchen_sex {}".format(pose_list[pose_counter]) as animation
                    pause
                    $ poses_done.append(pose_list[pose_counter])
                    $ pose_counter += 1
                call scene_maria_sex_kitchen.dialogue
            $ animcounter += 1
        call screen scene_maria_sex_kitchen_controls
        if _return:
            return _return
    return


label scene_maria_sex_kitchen.dialogue:
    if animcounter == 0 and randomizer() > 50:
        maria "Oh, gawd!!{p=1}{nw}"
        maria "OH MY GAWD!!!{p=1}{nw}"
    if animcounter == 1 and randomizer() > 50:
        anon "I'm getting close!{p=1}{nw}"
    if animcounter == 2 and randomizer() > 50:
        anon "I'm gonna cum!{p=1}{nw}"
        maria "Ngh, me too!{p=1}{nw}"
    elif randomizer() > 50:
        maria "Don't stop!{p=1}{nw}"
    return


label scene_maria_sex_kitchen.cum(where, pregnant=False):
    if where == 'inside':
        jump scene_maria_sex_kitchen.inside
    jump scene_maria_sex_kitchen.outside


label scene_maria_sex_kitchen.inside:
    if randomizer() > 50:
        anon "Should I cum inside you?"
        maria "YES!!!"
    else:
        anon "Here it comes!"
    pause
    hide animation
    if pregnant:
        show maria b_sex_kitchen_cum_pregnant_belly
    else:
        show maria b_sex_kitchen_cum
    anon "HNNGGG!!!" with flash
    show xray_maria_kitchen with fastdissolve:
        align (0, 0)
    maria "NGGHHH!!!"
    hide xray_maria_kitchen
    if pregnant:
        show maria b_sex_kitchen_talk_pregnant_belly f_shy_lipbite
    else:
        show maria b_sex_kitchen_talk_uncovered f_shy_lipbite
    show anon_maria_sex_kitchen insert
    show maria_sex_kitchen_mc_insert_cum_overlay
    with dissolve
    anon "Haah... Haah..."
    pause
    if randomizer() > 50:
        maria f_normal "Mmm, I love it when you finish inside me, {b}[firstname]{/b}..."
    else:
        maria f_normal "Oh, gawd... That was just what I needed!"
    anon "Heh, happy to oblige."

    call call_pregnancy_minigame (None, M_maria)
    return


label scene_maria_sex_kitchen.outside:
    maria "NGGHHH!!!"
    hide animation
    if pregnant:
        show maria b_sex_kitchen_base_pregnant_belly
    else:
        show maria b_sex_kitchen_base
    show anon_maria_sex_kitchen cumshot
    show maria_sex_kitchen_mc_cumshot_dick
    anon "HNNGGG!!!" with flash
    hide maria_sex_kitchen_mc_cumshot_dick
    show anon_maria_sex_kitchen pre
    show maria_sex_kitchen_mc_pre_cum_overlay
    show maria_overlay_sex_kitchen_o_cumshot:
        xoffset 12
    with dissolve
    pause
    if pregnant:
        show maria b_sex_kitchen_talk_pregnant_belly f_shy_lipbite
    else:
        show maria b_sex_kitchen_talk_uncovered f_shy_lipbite
    show maria_overlay_sex_kitchen_o_cumshot:
        xoffset 0
        yoffset 4
    anon "Haah... Haah..."
    if randomizer() > 50:
        maria f_normal "Mmm, that was incredible, {b}[firstname]{/b}!"
    else:
        maria f_normal "Oh, gawd... That was just what I needed!"
    if pregnant:
        anon "Sorry I came all over you..."
    else:
        anon "Sorry about your dress..."
    maria "No, that's okay."
    maria "I don't mind."
    return


label scene_maria_sex_kitchen.normal:
    scene location_pizza_kitchen_sex
    show maria b_sex_kitchen_talk
    with fade
    maria "Just make it quick, okay?"
    maria "I don't want some customer walkin' in and seein' us."
    anon "Awesome."
    show anon_maria_sex_kitchen pre with dissolve
    maria f_shy "I can't believe I'm doin' this."
    show maria b_sex_kitchen_mc_remove_panties1 f_shy_lipbite
    hide anon_maria_sex_kitchen
    with dissolve
    pause
    show maria b_sex_kitchen_mc_remove_panties2 with dissolve
    anon "I love this job!"
    show maria b_sex_kitchen_mc_remove_panties3 f_normal with dissolve
    maria "Hehe!"
    show maria b_sex_kitchen_talk_uncovered
    show anon_maria_sex_kitchen pre
    with dissolve
    maria "You're such a naughty boy..."
    show maria b_sex_kitchen_base
    show anon_maria_sex_kitchen insert
    with dissolve
    maria "!!!"
    show maria b_sex_kitchen_cum
    hide anon_maria_sex_kitchen
    with dissolve
    maria "Ahh!!"
    call scene_maria_sex_kitchen.animate
    pause
    maria "Oh, {b}[firstname]{/b}!"
    maria "You're so big!"
    pause
    maria "Oh, gawd!"
    maria "Yes!!"
    pause
    maria "Fuck me, {b}[firstname]{/b}!"
    maria "Ahh!!"
    pause
    call scene_maria_sex_kitchen.loop
    call scene_maria_sex_kitchen.cum (_return)
    return _return


label scene_maria_sex_kitchen.pregnant:
    scene location_pizza_kitchen_sex
    show maria b_sex_kitchen_talk_pregnant_belly
    with fade
    maria "Get over here quick, handsome..."
    anon "Yes, ma'am!"
    show anon_maria_sex_kitchen pre with dissolve
    pause
    show maria b_sex_kitchen_base_pregnant_belly
    show anon_maria_sex_kitchen insert
    with dissolve
    maria "Hurry, {b}[firstname]{/b}!"
    show maria b_sex_kitchen_cum_pregnant_belly
    hide anon_maria_sex_kitchen
    with dissolve
    maria "!!!"
    maria "Ahh!!"
    call scene_maria_sex_kitchen.animate (pregnant=True)
    pause
    maria "Oh, {b}[firstname]{/b}!"
    maria "I needed this so bad!"
    pause
    maria "Oh, gawd!"
    maria "Yes!!"
    pause
    maria "Fuck me, {b}[firstname]{/b}!"
    maria "Ahh!!"
    pause
    call scene_maria_sex_kitchen.loop (pregnant=True)
    call scene_maria_sex_kitchen.cum (_return, pregnant=True)
    return _return


label scene_maria_sex_kitchen.replay:
    $ renpy.dynamic(variants=persistent.cookie_jar['maria']['variants']['03_unlocked'])

    if len(variants) > 1:
        scene expression background(l=L_pizzeria_kitchen) with fade
        menu:
            "Normal" if 'normal' in variants:
                jump scene_maria_sex_kitchen.normal

            "Pregnant" if 'pregnant' in variants:
                jump scene_maria_sex_kitchen.pregnant
    else:

        jump expression 'scene_maria_sex_kitchen.{}'.format(next(iter(variants)))

    return


screen scene_maria_sex_kitchen_controls():
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
                action (Function(M_maria.set,
                                 'sex speed',
                                 M_maria.get('sex speed') + 0.03),
                        Return(False))
                sensitive M_maria.get('sex speed') < .12
            textbutton _('Faster »'):
                action (Function(M_maria.set,
                                 'sex speed',
                                 M_maria.get('sex speed') - 0.03),
                        Return(False))
                sensitive M_maria.get('sex speed') > .061
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
