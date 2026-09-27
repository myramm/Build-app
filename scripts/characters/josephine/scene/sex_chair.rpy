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
        josephine "Astaga!!"


    elif opt == 2:
        anon "Ini dia."

        josephine "Ahhh!"


        if rng < 0:
            anon "Sempurna."


    elif opt == 3:
        anon "Saya tidak percaya Anda menyukai hal ini."


        if rng < 0:
            josephine "Apa maksudmu?"

            anon "Game porno animasi."


        josephine "Menurutku itu lucu."

        anon "Oh, apakah ini saat kamu memberitahuku bahwa kamu hanya memainkannya untuk ceritanya?"


        if rng < 0:
            josephine "Hmm, ya."

            pause

        josephine "Atau tahukah Anda, saat saya benar-benar bosan dan ingin cum."


        if rng < .5:
            anon "Aku mengetahuinya!"


    elif opt == 4:
        anon "Musik ini mengerikan."

        josephine "Entahlah, aku agak menyukainya."

        anon "Kamu benar-benar troll."

        josephine "Benar sekali."


    elif opt == 5:
        if rng < 0:
            josephine "Cih, hati-hati di belakang sana!"


        anon "Apakah aku menariknya terlalu keras?"

        josephine "Tidak, menarik rambutnya bagus."


        if rng < 0:
            josephine "Cukup yakin kau sedang meninju ginjalku."

            anon "Oh maaf."


    return


label scene_josie_sex_chair.cum(where):
    anon "Apakah kamu semakin dekat?"

    josephine "Mhmm!"

    anon "Bagus karena aku tinggal sekitar dua detik lagi untuk muncul!"

    pause
    anon "Di sini..."

    anon "... itu..."

    anon "... DATANG!!"


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
        josephine @ -m_talk "MM."


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
    anon "Itu pasti cara terbaik untuk menonton aliran seni!"

    josephine "Kamu bodoh."

    anon "Ya, tapi kamu menyukainya."

    josephine f_happy "{i}*Huh*{/i} Ya, memang begitu."


    if where == 'inside':
        call call_pregnancy_minigame (None, M_josie)
    return where


label scene_josie_sex_chair.repeat:
    $ M_josie.set('sex speed', 1 / 8.)

    call scene_josie_sex_chair.stage
    with fade
    josephine "Bisakah kamu melihat?"

    anon "Tidak, kepalamu menghalangi."

    josephine "Tunggu."

    call scene_josie_sex_chair.insert
    with {'master': dissolve}
    anon "Jangan khawatir, saya mengerti."

    josephine f_curious_back @ -m_talk "Hmm?"

    call scene_josie_sex_chair.animate
    with dissolve
    call scene_josie_sex_chair.dialogue (1)
    pause
    call scene_josie_sex_chair.dialogue (2)
    pause
    call scene_josie_sex_chair.dialogue (3)
    pause
    anon "Sekarang siapakah dua orang lainnya yang sedang berbicara?"

    josephine "Oh, salah satunya adalah pembuat kode untuk tim..."

    josephine "... Dan yang lainnya adalah penulisnya."

    josephine "{b}Darkcookie{/b} meminta mereka menjawab pertanyaan penggemar sesekali."

    anon "Itu cukup rapi."

    josephine "Ya, kecuali itu biasanya jebakan dan dia menghabiskan seluruh waktunya untuk menindas mereka."

    anon "Benar-benar?"

    josephine "Hehe, ya."

    pause
    call scene_josie_sex_chair.dialogue (4)
    pause
    josephine "Ayo, {b}[firstname]{/b}..."

    josephine "... Persetan dengan vagina trollku!"

    anon "Eugh, tolong jangan pernah katakan itu lagi."

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
