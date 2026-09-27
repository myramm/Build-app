label scene_khadne_crates_sex:
    $ M_khadne.set('sex speed', 1. / 6)
    $ renpy.dynamic(variant='first')

    call scene_khadne_crates_sex.stage
    with fade
    anon "Anda siap?"

    khadne "{i}*Gulp*{/i} Saya kira begitu."

    anon "Ini dia."

    call scene_khadne_crates_sex.insert
    with dissolve
    khadne @ -m_talk "{i}*Iiiitthh*{/i}"

    anon "Bagaimana rasanya?"

    khadne f_moan "Ngh, sakit!"

    anon "Baiklah, aku tidak akan melangkah lebih jauh..."

    khadne @ -m_talk "{i}* Merengek*{/i}"

    anon "Bernafas."

    khadne f_nervous "{i}*Fiuh*{/i} Haah... Haah... {i}*Fiuh*{/i}"

    anon "Itu dia..."

    anon "... Berikan waktu pada tubuh Anda untuk menyesuaikan diri."

    khadne "{i}*Fiuh*{/i} Haah... Haah... {i}*Fiuh*{/i}"

    khadne "Saya pikir mungkin itu berhasil..."

    anon "Ya?"

    khadne "{i}*Fiuh*{/i} Haah... Haah... {i}*Fiuh*{/i}"

    anon "Aku akan mulai bergerak sedikit, oke?"

    khadne "O-oke."

    call scene_khadne_crates_sex.animate
    with dissolve
    pause
    khadne "{i}* Merengek*{/i}"

    anon "Bernapaslah, {b}Khadne{/b}."

    khadne "{i}*Fiuh*{/i} Haah... Haah... {i}*Fiuh*{/i}"

    anon "Ini dia."

    pause
    anon "Masih sakit?"

    khadne "Ya, tapi tidak terlalu buruk."

    anon "Anda ingin saya berhenti?"

    khadne "T-tidak."

    pause
    khadne "Ahhh!"

    anon "Lebih baik?"

    khadne "Menurutku begitu..."

    khadne "... Ya."

    pause
    khadne "Oh my god..." (show_native="O moy Bog...")
    anon "Merasa baik?"

    khadne "Mhmm!"

    pause
    anon "Bisakah saya mempercepat?"

    khadne "Ya."

    $ M_khadne.set('sex speed', 1. / 10)
    pause
    call scene_khadne_crates_sex.dialogue (1)
    pause
    call scene_khadne_crates_sex.dialogue (2)
    pause
    call scene_khadne_crates_sex.dialogue (3)
    pause
    label scene_khadne_crates_sex.resume:
    call scene_khadne_crates_sex.loop
    anon "aku rasa aku tidak bisa bertahan lebih lama lagi..."

    khadne "Anda ingin membuat cum?"

    anon "... Ya!"

    khadne "Ahh!!"

    pause
    khadne "Lakukan!"

    khadne "Buatkan air mani untukku!"

    anon "Haaah!!"

    pause
    anon "Ya Tuhan..."

    anon "... Ini dia!"

    khadne "Ya!!"

    pause

    hide anim
    if _return == 'inside':
        show khadne crates_sex b_cum
    else:
        show khadne crates_sex b_base f_moan m_talk o_cumshot

    anon "HNNGGG!!!" with flash

    if _return == 'inside':
        show xray_side as xray:
            anchor (.5, .5)
            pos (250 + 386, 250 + 179)
            rotate 4
            rotate_pad False
            xzoom -1
            zoom .75
        with {'master': fastdissolve}
    else:
        show khadne o_cumshot3

    khadne "NGGHHH!!!"

    pause
    hide xray

    if _return == 'inside':
        show khadne b_base f_moan m_talk o_pullout
        with {'master': dissolve}

    anon "Haah... Haah..."

    show khadne f_normal
    anon "Fiuh!"

    return _return


label scene_khadne_crates_sex.stage:
    scene location_warehouse_hostage_vodka_crate_up_any
    show khadne crates_sex
    return


label scene_khadne_crates_sex.insert:
    show khadne b_insert f_moan_teeth
    return


label scene_khadne_crates_sex.animate:
    hide khadne
    show khadne_crates_sex_body_b_anim as anim
    return


label scene_khadne_crates_sex.loop:
    call screen scene_khadne_crates_sex_controls

    if _return:
        return _return

    python hide:
        blocks = 3 if variant == 'first' else 4
        limit = 2

        renpy.dynamic(pool=random.sample(range(2 - limit, blocks + 1), limit))

    pause

    while pool:
        call scene_khadne_crates_sex.dialogue (pool.pop(), rng=random.random())
        pause

    jump scene_khadne_crates_sex.loop


label scene_khadne_crates_sex.dialogue(opt, rng=-1):

    if opt == 1:
        khadne "Oh, wow!" (show_native="Vot eto da!")
        anon "Anda suka itu?"

        khadne "Ya!"


        if rng < .2:
            khadne "Ini sangat berbeda dari sebelumnya!"

            anon "Aku sudah bilang padamu."


    elif opt == 2:
        khadne "Oh, fuck me!" (show_native="Oh, trakhni menya!")

        if rng < .4:
            anon "Hmm?"

            khadne "Persetan denganku, {b}[firstname]{/b}!"


        anon "Ya, Bu!"


    elif opt == 3:
        if rng < .5:
            khadne "So good!" (show_native="Tak khorosho!")

        if rng < .3:
            khadne "Fuck my pussy, {b}[firstname]{/b}!" (show_native="Trakhni moyu kisku, {b}[firstname]{/b}!")

        anon "Sial, kamu seksi."

        khadne "Ahh!!"


    elif opt == 4:
        khadne "Lebih sulit!"


        if rng < .25:
            anon "Wah, hati-hati jangan sampai botolnya terjatuh!"


    return


label scene_khadne_crates_sex.first:
    jump scene_khadne_crates_sex


label scene_khadne_crates_sex.repeat:
    $ M_khadne.set('sex speed', 1. / 8)
    $ renpy.dynamic(variant='repeat')

    call scene_khadne_crates_sex.stage
    with fade
    anon "Ingatlah untuk memberitahuku apakah aku akan berpuasa, oke?"

    khadne "Y-ya, oke."

    call scene_khadne_crates_sex.insert
    with dissolve
    khadne f_nervous @ f_moan_teeth -m_talk "!!!"
    anon "Kamu baik-baik saja?"

    khadne "Very."

    anon "Luar biasa!"

    call scene_khadne_crates_sex.animate
    with dissolve
    pause
    call scene_khadne_crates_sex.dialogue (1)
    pause
    call scene_khadne_crates_sex.dialogue (2)
    pause
    call scene_khadne_crates_sex.dialogue (3)
    pause
    call scene_khadne_crates_sex.dialogue (4)
    pause
    jump scene_khadne_crates_sex.resume


label scene_khadne_crates_sex.replay:
    $ renpy.dynamic(variants=persistent.cookie_jar['khadne']['variants']['02_unlocked'])
    $ M_anon._cleared_states[S_ano27_done] = True

    if len(variants) > 1:
        scene expression background(l=L_warehouse_storage) with fade
        menu:
            "Pertama" if 'first' in variants:
                jump scene_khadne_crates_sex.first

            "Ulangi" if 'repeat' in variants:
                jump scene_khadne_crates_sex.repeat

    jump expression 'scene_khadne_crates_sex.{}'.format(next(iter(variants)))


screen scene_khadne_crates_sex_controls():
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
