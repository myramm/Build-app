label scene_maria_sex_bedroom:

    return


label scene_maria_sex_bedroom.animate:
    python:
        anim_toggle = True
        animated = True
        M_maria.set('sex speed', .1)
    hide maria
    show maria_body_b_sex_home_anim as animation
    with dissolve
    return


label scene_maria_sex_bedroom.loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 3:
        if anim_toggle:
            if not animated:
                show maria_body_b_sex_home_anim as animation with dissolve
                $ animated = True
            pause 5
            call scene_maria_sex_bedroom.dialogue
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8]
            $ poses_done = []
            while poses_done != pose_list:
                show expression 'maria_body_b_sex_home_anim {}'.format(pose_list[pose_counter]) as animation
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call scene_maria_sex_bedroom.dialogue
        $ animcounter += 1
    call screen scene_maria_sex_bedroom_controls
    if not _return:
        jump scene_maria_sex_bedroom.loop
    return _return


label scene_maria_sex_bedroom.dialogue:
    if animcounter == 0 and randomizer() > 75:
        maria "Fuuuuuuuuuuck!{p=1}{nw}"
    if animcounter == 1 and randomizer() > 75:
        maria "Oh, gawd!{p=1}{nw}"
    elif animcounter == 1 and randomizer() > 75:
        maria "I love this dick, so much!{p=2}{nw}"
    if animcounter == 2 and randomizer() > 75:
        maria "OH, [firstname!u]!!!!{p=1}{nw}"
    elif animcounter == 2 and randomizer() > 75:
        maria "It's so deep!{p=1}{nw}"
        maria "Fuck me harder!{p=1}{nw}"
    return


label scene_maria_sex_bedroom.cum(where):
    if where == 'inside':
        anon "Boy, boy, boy... Very tall boy!"
        maria "Huh?"
        maria "Did you just-"
        maria "AHHH!!!"

    maria "OH MY GAWD!"
    maria "GIVE ME A BABY, {b}[firstname!u]!{/b}!!!"
    pause
    hide animation

    if where == 'inside':
        show maria b_sex_home_cum
    else:
        show maria b_sex_home_pre_after a_cumshot

    anon "HNNGGG!!!" with flash

    if where == 'inside':
        show xray_maria_home with fastdissolve:
            align (0, 0)
    else:
        show maria b_sex_home_pre_after a_idle op_after oc_cumshot with dissolve

    maria "NGGHHH!!!"

    if where == 'inside':
        pause
        hide xray_maria_home with dissolve

    anon "Haah... Haah..."

    if where == 'inside':
        maria "Oh, gawd..."
        maria "... This is the best sex ever!"
        anon "Yeah?"
        maria "Phew... I don't know if I ever wanna quit doin' it..."
        anon "Really?"
        show maria b_sex_home_insert_pullout with dissolve
        maria "Haah!"
        show maria b_sex_home_pre_after op_after_cum od_after with dissolve
        pause
        show maria a_empty with dissolve
        anon "Wouldn't {b}Tony{/b} be upset if we kept doing this?"
        maria "Are you kiddin'?"
        maria "He'll be ecstatic if he finds out you'll give him more than one kid!"
        pause
        anon "Well, I can definitely do that!"
        maria f_normal_closed "Heh, I know you can, handsome..."
    else:
        maria "What happened?"
        maria "You pulled out?"
        anon "Y-yeah, sorry..."
        anon "The moment came and I just-"
        pause
        anon "Sorry, I just couldn't do it."
        show maria a_empty with dissolve
        maria "Oh, it's alright, {b}[firstname]{/b}..."
        maria "... I don't mind."
        anon "You don't?"
        maria "I mean, I would prefer you finish inside me; but if you'd rather pull out, that's okay too."
        anon "Really?"
        maria f_normal_closed "Just don't tell {b}Tony{/b}, yeah?"

    maria "Now if you'll excuse me, I think I'm just gonna lay here a while and bask in my postcoital bliss..."
    anon "Sure, thing."
    anon "I'll see you later, {b}Maria{/b}."
    maria "See ya, {b}[firstname]{/b}."

    if where == 'inside':
        call call_pregnancy_minigame (None, M_maria)
    return


label scene_maria_sex_bedroom.repeat:
    scene location_maria_bedroom_sex
    show maria b_sex_home_pre_after
    with fade
    maria "Don't be shy, {b}[firstname]{/b}..."
    maria "I'm all yours."
    show maria a_pussy_open with dissolve
    anon "{i}*Gulp*{/i}"
    show maria b_sex_home_insert_pullout with dissolve
    pause
    show maria b_sex_home_cum
    maria "!!!" with hpunch
    maria "Haah!"
    pause
    call scene_maria_sex_bedroom.animate
    maria "Fuuuuuuuuuuck!"
    pause
    maria "Oh, gawd!"
    pause
    maria "I love this dick, so much!"
    maria "It feels incredible!!"
    pause
    maria "It's so deep!"
    maria "Oh, gawd, fuck me, {b}[firstname]{/b}!!"
    maria "Fuck me harder!"
    pause
    maria "Ahh!!"
    maria "I'm gonna cum!!!"
    anon "I'm getting close too."
    pause
    maria "Do it, {b}[firstname]{/b}!"
    maria "Put a baby inside me!"
    maria "Please!"
    anon "Y-yes, ma'am."
    pause
    call scene_maria_sex_bedroom.loop
    call scene_maria_sex_bedroom.cum (_return)
    return


label scene_maria_sex_bedroom.replay:
    jump scene_maria_sex_bedroom.repeat


screen scene_maria_sex_bedroom_controls():
    style_prefix 'sex'

    vbox:

        frame:
            has hbox
            textbutton _('Keep Going') action Return(False)
            textbutton _('Cum Inside') action Return('inside')
            if M_anon.finished_state(S_ano11_done):
                textbutton _('Cum Outside') action Return('outside')

        frame:
            has hbox
            textbutton _('« Slower'):
                action (Function(M_maria.set,
                                 'sex speed',
                                 M_maria.get('sex speed') + 0.02),
                        Return(False))
                sensitive M_maria.get('sex speed') < .1
            textbutton _('Faster »'):
                action (Function(M_maria.set,
                                 'sex speed',
                                 M_maria.get('sex speed') - 0.02),
                        Return(False))
                sensitive M_maria.get('sex speed') > .061
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
