label scene_daisy_sex_loft:

    return


label scene_daisy_sex_loft.stage:
    scene location_barn_top_sex_daisy
    show daisy_sex_sleep_base as animation
    show daisy sex_sleep
    show daisy_sex_sleep_insert as overlay
    return


label scene_daisy_sex_loft.insert:
    show daisy_sex_sleep_anim01 as animation
    hide daisy
    hide overlay
    with dissolve
    return


label scene_daisy_sex_loft.animate:
    python:
        anim_toggle = True
        animated = True
        M_daisy.set('sex speed', 1 / 8.)
    hide daisy
    show daisy_sex_hayloft as animation
    with dissolve
    return


label scene_daisy_sex_loft.loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 3:
        if anim_toggle:
            if not animated:
                show daisy_sex_hayloft as animation with dissolve
                $ animated = True
            pause 5
            call scene_daisy_sex_loft.dialogue
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8,9]
            $ poses_done = []
            while poses_done != pose_list:
                show expression 'daisy_sex_hayloft {}'.format(pose_list[pose_counter]) as animation
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call scene_daisy_sex_loft.dialogue
        $ animcounter += 1
    call screen scene_daisy_sex_loft_controls
    if not _return:
        jump scene_daisy_sex_loft.loop
    return _return


label scene_daisy_sex_loft.dialogue:
    if animcounter == 0 and randomizer() > 75:
        daisy "Ahh!{p=.75}{nw}"

        daisy "That's it Mr. Weasel!{p=1.25}{nw}"

        daisy "That's it!!{p=1}{nw}"

    if animcounter == 1 and randomizer() > 75:
        anon "{b}Daisy{/b} you're shaking.{p=1.5}{nw}"

        daisy "I know, I'm sorry...{p=1}{nw}"

        daisy "... It's all the tingles, I can't help it!{p=2}{nw}"

    if animcounter == 2 and randomizer() > 75:
        daisy "Haah! Your weasel is so deep, {b}[firstname]{/b}!{p=1.5}{nw}"

    return


label scene_daisy_sex_loft.cum(where):
    daisy "I think I'm about to have one of those orgasm thingies again!"

    anon "Ya, aku juga!"

    pause
    daisy "Oh, {b}[firstname]{/b}!!"

    daisy "AAH!!"

    pause

    if where == 'inside':
        show daisy_sex_sleep_cum as animation
    else:
        show daisy_sex_sleep_base as animation
        show daisy sex_sleep m_talk
        show daisy_sex_sleep_cumshot as cum

    anon "HNNGGG!!!" with flash

    if where == 'inside':
        show xray_front_top as xray with fastdissolve:
            anchor (.5, .5)
            pos (250 + 227, 250 + 152)
            rotate 68
            rotate_pad False
            xzoom -1
            zoom .94

    daisy -m_talk "NGGHHH!!!"

    hide xray

    if where == 'inside':
        show daisy_sex_sleep_base as animation
        show daisy sex_sleep
        show daisy_sex_sleep_insert as overlay
        show daisy_sex_sleep_pullout as cum

    with {'master': dissolve}
    daisy "Oh, wowzers!"

    anon "Haah... Haah..."

    daisy f_calm_up "That was a lot of milk!"

    anon "Ya."

    daisy f_calm_down "hehe!"


    if where == 'inside':
        call call_pregnancy_minigame (None, M_daisy)
    return


label scene_daisy_sex_loft.repeat:
    call scene_daisy_sex_loft.stage
    with fade
    daisy "Come on in Mr. Weasel!"

    anon "Hehe."

    call scene_daisy_sex_loft.insert
    daisy "!!!"
    pause
    call scene_daisy_sex_loft.animate
    daisy "Oh, that's really nice."

    anon "Ya?"

    daisy "Mhmm!"

    pause
    daisy "You're such a good man, {b}[firstname]{/b}..."

    daisy "... Making me feel better after my bad dream."

    anon "Heh, it's no problem, {b}Daisy{/b}..."

    anon "... Believe me, I'm happy to do it."

    pause
    daisy "Mmm, your weasel goes so deep in my hidey hole, {b}[firstname]{/b}!"

    anon "Apakah rasanya enak?"

    daisy "Really, {i}really{/i} good!"

    pause
    daisy "Ahhh!"

    daisy "That's it Mr. Weasel!"

    daisy "That's it!!"

    pause
    anon "{b}Daisy{/b} you're shaking."

    daisy "I know, I'm sorry..."

    daisy "... It's all the tingles, I can't help it!"

    pause
    anon "Oh, you're so wet!"

    daisy "You mean my floogina?"

    anon "{i}Va{/i}-gina, {b}Daisy{/b}."

    daisy "Right, {i}va{/i}-gina."

    pause
    call scene_daisy_sex_loft.loop
    call scene_daisy_sex_loft.cum (_return)
    return


label scene_daisy_sex_loft.replay:
    jump scene_daisy_sex_loft.repeat


screen scene_daisy_sex_loft_controls():
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
                action (Function(M_daisy.set, 'sex speed',
                                 1 / (1 / M_daisy.get('sex speed') - 2)),
                        Return(False))
                sensitive M_daisy.get('sex speed') < 1 / 8.
            textbutton _('Faster »'):
                action (Function(M_daisy.set, 'sex speed',
                                 1 / (1 / M_daisy.get('sex speed') + 2)),
                        Return(False))
                sensitive M_daisy.get('sex speed') > 1 / 16.
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
