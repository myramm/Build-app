label scene_diane_sex_milk:

    return


label scene_diane_sex_milk.animate:
    show diane_sex_milk_anim as body
    return


label scene_diane_sex_milk.loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 3:
        if anim_toggle:
            if not animated:
                call scene_diane_sex_milk.animate
                $ animated = True
            pause 5
            call scene_diane_sex_milk.dialogue
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = range(1, 10)
            $ poses_done = []
            while poses_done != pose_list:
                show expression "diane_sex_milk_anim {}".format(
                    pose_list[pose_counter]) as body
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call scene_diane_sex_milk.dialogue
        $ animcounter += 1
    call screen scene_diane_sex_milk_controls()
    if not _return:
        jump scene_diane_sex_milk.loop
    return _return


label scene_diane_sex_milk.dialogue:
    $ renpy.dynamic(rng=renpy.random.random())

    if animcounter == 0 and rng <= .33:
        diane "Oh, aku melewatkan ini!"

        anon "Ya, aku juga."

    elif animcounter == 0 and rng <= .66:
        anon "Sobat, jerami ini agak gatal di pantatku..."

        diane "Hmm?"

        anon "... T-tidak apa-apa, sudahlah."

    elif animcounter == 0 and rng <= .77:
        diane "Ahh!!"

    elif animcounter == 0 and rng <= .88:
        diane "YA TUHAN!!!"

    elif animcounter == 0 and rng <= .99:
        anon "Ya Tuhan!"


    elif animcounter == 1 and rng <= .33:
        anon "Saya sangat senang kami melakukannya lagi."

        diane "Mhmm!!"

    elif animcounter == 1 and rng <= .66:
        diane "Ngh, aku suka sekali penis ini..."

        diane "... Berdebar..."

        diane "... Ke dalam vaginaku!"


    elif animcounter == 2 and rng <= .33:
        diane "Berikan padaku, {b}[firstname]{/b}!"

        diane "Ini sangat bagus!"

    elif animcounter == 2 and rng <= .66:
        diane "Kembangkan aku, {b}[firstname]{/b}!"

        diane "Banjir rahimku!!"

        anon "Ahhh!"

    elif animcounter == 2 and rng <= .99:
        diane "Kamu suka aku menunggangimu?"

        anon "Ya!"

        if rng <= .77:
            pause
            diane "Mengendaraimu di gudang kotor ini?"

            anon "YA!!!"

            diane "AAH!!!"


    return


label scene_diane_sex_milk.repeat(outfit='naked'):
    python:
        renpy.dynamic(anim_toggle=True, animated=True, animcounter=0,
                      pose_counter=0, pose_list=None, poses_done=None)
        M_diane.set('sex speed', 1 / 8.)

    scene location_barn_hay_stack_milk
    show diane_sex_milk_base as body
    show diane_sex_milk_rub01 as dick
    show diane a_empty b_empty f_sex_milk_happy_down
    with fade
    anon "Wah, kamu basah banget, {b}Diane{/b}!"

    show diane f_sex_milk_sexy_back
    with {'master': fastdissolve}
    diane "Itu sesi memerah susu..."

    hide diane
    hide dick
    $ renpy.dynamic(face='diane_face_f_sex_milk_sexy_back')
    show diane_sex_milk_rub as body
    with {'master': dissolve}
    anon "!!!"
    $ renpy.dynamic(face='diane_face_f_sex_milk_moan')
    diane @ -m_talk "... Ngh!"

    show diane_sex_milk_insert as body
    with {'master': dissolve}
    anon "Haah!"

    call scene_diane_sex_milk.animate
    with {'master': dissolve}
    pause

    call scene_diane_sex_milk.loop

    anon "{b}Diane{/b}, aku akan-"

    anon "aku akan-"

    diane "Aku juga!!"

    pause
    diane "NGGHHH!!!"

    hide animation
    show diane_sex_milk_cum as body
    show diane_sex_milk_squirt_cum as milk
    anon "HNNGGG!!!" with flash
    show xray_diane_sex_milk as xray
    with {'master': fastdissolve}
    pause
    hide xray
    show diane_sex_milk_base as body
    show diane a_empty b_empty f_sex_milk_exhausted_down m_talk
    show diane_sex_milk_squirt_base as milk
    with {'master': dissolve}
    anon "Haah... Haah..."

    show diane f_sex_milk_happy_down -m_talk
    with {'master': fastdissolve}
    diane "Heh, sepertinya masih ada sedikit yang tersisa di sana..."

    show diane f_sex_milk_embarrassed_back
    with {'master': fastdissolve}
    anon "aku akan mengambilnya."

    show diane f_sex_milk_concerned_back
    with {'master': fastdissolve}
    diane @ -m_talk "... Hmm?"

    show diane_sex_milk_pump_base as body
    show diane f_sex_milk_exhausted_down
    show diane_sex_milk_squirt02 as milk
    show diane_sex_milk_squirt06 as pump
    with {'master': dissolve}
    diane "Oh, aku tidak tahu apakah kita harus-"

    hide milk
    hide pump
    show diane_sex_milk_pump as body
    show diane f_sex_milk_moan
    with {'master': dissolve}
    diane "Tidak!!"

    with {'master': fastdissolve}
    anon "Ini dia..."

    show diane f_sex_milk_ecstasy
    with {'master': fastdissolve}
    diane @ -m_talk "Ffuuuuu-"

    show diane f_sex_milk_moan
    with {'master': fastdissolve}
    anon "... Biarkan saja semuanya keluar."

    pause
    diane "Remas ambingku lebih keras lagi, {b}[firstname]{/b}!"

    anon "Seperti ini?"

    diane "Ya!!"

    pause
    show diane_sex_milk_pump_base as body
    show diane f_sex_milk_moan
    show diane_sex_milk_squirt02 as milk
    show diane_sex_milk_squirt05 as pump
    with {'master': dissolve}
    diane "Haah... Haah..."

    show diane f_sex_milk_exhausted_down
    with {'master': fastdissolve}
    anon "Apakah itu segalanya?"

    show diane f_sex_milk_embarrassed_back
    with {'master': fastdissolve}
    diane "Menurutku begitu..."

    hide pump
    show diane_sex_milk_base as body
    show diane f_sex_milk_happy_down
    show diane_sex_milk_squirt_base as milk
    with {'master': dissolve}
    pause
    hide diane
    show diane_sex_milk_pullout as body
    show diane_sex_milk_squirt_pullout as milk
    with {'master': dissolve}
    diane "... Fiuh!"

    call call_pregnancy_minigame (None, M_diane)
    return


label scene_diane_sex_milk.replay:
    $ renpy.dynamic(variants=persistent.cookie_jar['Diane']['variants']['08_unlocked'])

    if len(variants) > 1:
        scene expression im.Blur('backgrounds/location_barn_day.jpg', 1.7) with fade
        menu:
            "pakaian sapi" if 'cow' in variants:
                call scene_diane_sex_milk.repeat ('cow')

            "Telanjang" if 'naked' in variants:
                call scene_diane_sex_milk.repeat ('naked')
    else:

        call scene_diane_sex_milk.repeat (next(iter(variants)))

    return


screen scene_diane_sex_milk_controls():
    style_prefix 'sex'

    vbox:

        frame:
            has hbox
            textbutton _('Keep Going') action Return(False)
            textbutton _('Cum Inside') action Return('inside')

        frame:
            has hbox
            textbutton _('« Slower'):
                action (Function(M_diane.set, 'sex speed',
                                 1 / (1 / M_diane.get('sex speed') - 2)),
                        Return(False))
                sensitive M_diane.get('sex speed') < 1 / 8.
            textbutton _('Faster »'):
                action (Function(M_diane.set, 'sex speed',
                                 1 / (1 / M_diane.get('sex speed') + 2)),
                        Return(False))
                sensitive M_diane.get('sex speed') > 1 / 16.
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
