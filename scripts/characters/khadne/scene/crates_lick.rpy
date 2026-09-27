label scene_khadne_crates_lick:
    $ M_khadne.set('sex speed', 1. / 8)
    $ renpy.dynamic(variant='first')

    call scene_khadne_crates_lick.stage
    with fade
    khadne "A-apa yang harus aku lakukan?"

    anon "Coba santai saja, oke?"

    khadne @ -m_talk "..."
    call scene_khadne_crates_lick.animate
    with dissolve
    pause
    call scene_khadne_crates_lick.dialogue (1)
    pause
    call scene_khadne_crates_lick.dialogue (2)
    pause
    call scene_khadne_crates_lick.dialogue (3)
    pause
    call scene_khadne_crates_lick.dialogue (4)
    pause
    call scene_khadne_crates_lick.dialogue (5)
    pause
    label scene_khadne_crates_lick.resume:
    call scene_khadne_crates_lick.loop
    khadne "Ahh!!"

    khadne "menurutku..."


    if variant == 'first':
        khadne "... S-ada sesuatu yang..."

    else:
        khadne "... Ini terjadi lagi..."


    anon "{i}*Sluuuurp*{/i}"

    khadne "... Fuuuu-"

    anon "{i}*Mlemlemlemlemlem*{/i}"

    hide anim
    show khadne crates_lick b_cum
    khadne "NGGHHH!!!" with flash
    pause
    khadne "Haah... Haah..."

    return


label scene_khadne_crates_lick.stage:
    scene location_warehouse_hostage_vodka_crate_front_any
    show khadne crates_lick
    show anon khadne_crates_lick
    return


label scene_khadne_crates_lick.animate:
    hide anon
    hide khadne
    show khadne_crates_lick_body_b_anim as anim
    return


label scene_khadne_crates_lick.loop:
    call screen scene_khadne_crates_lick_controls

    if _return:
        return _return

    python hide:
        blocks = 5 if variant == 'first' else 10
        limit = 3

        renpy.dynamic(pool=random.sample(range(2 - limit, blocks + 1), limit))

    pause

    while pool:
        call scene_khadne_crates_lick.dialogue (pool.pop(), rng=random.random())
        pause

    jump scene_khadne_crates_lick.loop


label scene_khadne_crates_lick.dialogue(opt, rng=-1):

    if opt == 1:
        khadne "Ahhh!"


        if rng < .3:
            khadne "Itu menyenangkan."

            anon "Mhmm."


    elif opt == 2:
        anon "{i}*Sluuuurp*{/i}"

        khadne "Haah... Ya ampun..."


    elif opt == 3:
        anon "Haruskah saya melanjutkan?"

        khadne "Ya!"


        if rng < .35:
            khadne "Silakan!"


        if rng < .5:
            anon "{i}*Mlem*{/i}"

            khadne "Tidak!!"


    elif opt == 4:
        if rng < 0:
            khadne "Oh, that feels wonderful!" (show_native="O, eto prekrasno!")

        anon "{i}*Mlemlemlemlemlem*{/i}"

        khadne "Haah!!"


    elif opt == 5:
        if rng < .5:
            anon "Mmm, kamu rasanya enak."


        khadne "Jangan berhenti!"

        khadne "Jangan-"

        khadne "Ahh!!"


    elif opt == 6:
        khadne "Ya ampun!"


    elif opt == 7:
        anon "{i}*Mlemlemlemlemlem*{/i}"

        khadne "I love it when you lick my pussy!" (show_native="Ya lyublyu, kogda ty lizhesh' moyu kisku!")
        anon "Hah?"

        khadne "Saya menyukainya!"


    elif opt == 8:
        anon "{i}*Sluuuurp*{/i}"

        khadne "Ahh!!"


    elif opt == 9:
        anon "Kamu rasanya enak sekali!"

        khadne "Yes, taste me!" (show_native="Da, poprobuy menya!")
        anon "MM."


    elif opt == 10:
        khadne "Your tongue feels wonderful!" (show_native="Vash yazyk chuvstvuyet sebya prekrasno!")

        if rng < .1:
            anon "Apakah kamu dekat?"

            khadne "Ya!!"


    return


label scene_khadne_crates_lick.repeat:
    $ M_khadne.set('sex speed', 1. / 10)
    $ renpy.dynamic(variant='repeat')

    call scene_khadne_crates_lick.stage
    show khadne f_happy
    with fade
    anon "Santai saja, oke?"

    khadne "Ya."

    call scene_khadne_crates_lick.animate
    with dissolve
    call scene_khadne_crates_lick.dialogue (6)
    pause
    call scene_khadne_crates_lick.dialogue (7)
    pause
    call scene_khadne_crates_lick.dialogue (8)
    pause
    call scene_khadne_crates_lick.dialogue (9)
    pause
    call scene_khadne_crates_lick.dialogue (10)
    pause
    jump scene_khadne_crates_lick.resume


label scene_khadne_crates_lick.first:
    jump scene_khadne_crates_lick


label scene_khadne_crates_lick.replay:
    $ renpy.dynamic(variants=persistent.cookie_jar['khadne']['variants']['01_unlocked'])
    $ M_anon._cleared_states[S_ano27_done] = True

    if len(variants) > 1:
        scene expression background(l=L_warehouse_storage) with fade
        menu:
            "Pertama" if 'first' in variants:
                jump scene_khadne_crates_lick.first

            "Ulangi" if 'repeat' in variants:
                jump scene_khadne_crates_lick.repeat

    jump expression 'scene_khadne_crates_lick.{}'.format(next(iter(variants)))


screen scene_khadne_crates_lick_controls():
    style_prefix 'sex'

    vbox:

        frame:
            has hbox
            textbutton _('Keep Going') action Return(False)
            textbutton _('Finish') action Return()

        frame:
            has hbox
            textbutton _('« Slower'):
                action (Function(M_khadne.set, 'sex speed',
                                 1 / (1 / M_khadne.get('sex speed') - 2)),
                        Return(False))
                sensitive M_khadne.get('sex speed') < 1 / 8.
            textbutton _('Faster »'):
                action (Function(M_khadne.set, 'sex speed',
                                 1 / (1 / M_khadne.get('sex speed') + 2)),
                        Return(False))
                sensitive M_khadne.get('sex speed') > 1 / 16.
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
