label scene_odette_paizuri:
    return


label scene_odette_paizuri.animation:
    python:
        anim_toggle = True
        animated = True
        M_odette.set('sex speed', 1. / 8)
    show odette_paizuri as animation
    return


label scene_odette_paizuri.loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 3:
        if anim_toggle:
            if not animated:
                show odette_paizuri as animation with dissolve
                $ animated = True
            pause 5
            call scene_odette_paizuri.dialogue
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [7,8,9,10,11,1,2,3,4,5,6]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "odette_paizuri {}".format(pose_list[pose_counter]) as animation
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call scene_odette_paizuri.dialogue
        $ animcounter += 1
    call screen scene_odette_paizuri_controls
    if not _return:
        jump scene_odette_paizuri.loop
    return _return


label scene_odette_paizuri.dialogue:
    $ renpy.dynamic(rng=randomizer())
    if animcounter == 0 and rng > 85:
        anon "Fiuh, ya..."

        anon "... Itu luar biasa!"

    elif animcounter == 1 and rng > 85:
        anon "Apakah itu baik untukmu?"

        odette "Mhmm."

    elif animcounter == 2 and rng > 85:
        anon "Oh, {b}Odette{/b}!"

        anon "Oh, aku suka payudaramu!!"

    return



label scene_odette_paizuri.repeat:
    scene location_tattoo_garage_sex_titjob
    show odette_sex_boobjob_anim07 as animation
    with fade
    anon "Anda siap?"

    odette "Mhmm."

    anon "Ini dia!"

    call scene_odette_paizuri.animation
    with dissolve
    anon "Fiuh, ya..."

    anon "... Itu luar biasa!"

    pause
    anon "Rasanya penisku terjepit di antara dua awan empuk surga murni saat ini..."

    odette "hehe!"

    anon "... Sungguh, aku bisa mendengar malaikat bernyanyi!"

    pause
    anon "Apakah itu baik untukmu?"

    odette "Mhmm."

    pause
    anon "Kamu sedikit menggigil."

    odette "Ya, itu menggelitik..."

    anon "Itu bagus, bukan?"

    odette "... Sangat!"

    pause
    anon "Oh, {b}Odette{/b}!"

    anon "Oh, aku suka payudaramu!!"

    call scene_odette_paizuri.loop
    anon "aku akan keluar!"

    odette "Silakan, sobat besar..."

    anon "aku akan-"

    anon "aku-"

    pause
    show odette_sex_boobjob_cum as animation
    show odette_sex_boobjob_cumshot
    anon "HNNGGG!!!" with flash
    pause
    anon "Haah... Haah..."

    anon "... sial."

    odette "hehe!"

    return


label scene_odette_paizuri.replay:
    jump scene_odette_paizuri.repeat


screen scene_odette_paizuri_controls():
    style_prefix 'sex'

    vbox:

        frame:
            has hbox
            textbutton _('Keep Going') action Return(False)
            textbutton _('Cum') action Return()

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
