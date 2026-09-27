label scene_tina_sex_lounge:
    $ M_tina.set('sex speed', 1. / 8)
    $ renpy.dynamic(variant='first')

    call scene_tina_sex_lounge.stage
    with fade
    pause
    show tina b_sex_insert_pullout
    with {'master': dissolve}
    pause
    show tina b_sex_talk f_moan
    with {'master': dissolve}
    anon "!!!"
    tina f_normal @ f_moan "Haah!"

    tina "Astaga!"

    pause
    tina "Nah, itu penis yang besar!"

    anon "Ya Tuhan..."

    anon "Saya tidak percaya ini terjadi!"

    call scene_tina_sex_lounge.animate
    with {'master': dissolve}
    pause
    tina @ -m_talk "Hmm!"

    anon "aku akan keluar!"

    hide anim
    show anon b_tina_sex
    show tina b_sex_talk
    with {'master': dissolve}
    tina "Tidak!"

    anon "Apa-"

    anon "Kenapa kamu berhenti?!"

    tina "Anda tidak diperbolehkan untuk cum sampai saya mengatakannya!"

    anon "Hah?!"

    anon "I-itu bukan-"

    tina "Ini instruksi saya selanjutnya!"

    anon @ -m_talk "..."
    tina "Dan kamu akan mengikuti instruksiku, bukan, babyface?"

    anon "Maksudku, aku akan mencoba..."

    call scene_tina_sex_lounge.animate
    with {'master': dissolve}
    tina "Aku tidak bisa mendengarmu!"

    anon "Haah!"

    pause
    call scene_tina_sex_lounge.dialogue (1)
    pause
    call scene_tina_sex_lounge.dialogue (2)
    pause
    call scene_tina_sex_lounge.dialogue (3)
    pause
    call scene_tina_sex_lounge.dialogue (4)
    call scene_tina_sex_lounge.loop
    tina "aku hampir..."

    pause
    tina "... Hampir sampai!"

    tina "Sialan!"

    pause
    tina "Haah!"

    pause
    tina "HAAAH!!"

    anon "{b}Tina{/b}, aku tidak bisa-"

    pause
    tina "Lihat aku!"

    anon "Eh ya?"

    tina "Kita akan cum bersama-sama!"

    tina "Katakan!"

    anon "Kita akan cum bersama-sama."

    pause
    tina "DI SINI!"

    tina "DIA!!"

    tina "DATANG!!!"

    call scene_tina_sex_lounge.cum (_return)
    return


label scene_tina_sex_lounge.stage:
    scene location_tina_lounge_sex
    show anon b_tina_sex
    show tina b_sex_laydown_getup
    return


label scene_tina_sex_lounge.insert:
    show tina b_sex_insert_pullout
    return


label scene_tina_sex_lounge.animate:
    hide anon
    hide tina
    show tina_lounge_cowgirl as anim
    return


label scene_tina_sex_lounge.loop:
    call screen scene_tina_sex_lounge_controls

    if _return:
        return _return

    python hide:
        blocks = 4 if variant == 'first' else 7
        limit = 3

        renpy.dynamic(pool=random.sample(range(2 - limit, blocks + 1), limit))

    pause

    while pool:
        call scene_tina_sex_lounge.dialogue (pool.pop(), rng=random.random())
        pause

    jump scene_tina_sex_lounge.loop


label scene_tina_sex_lounge.dialogue(opt, rng=-1):
    if opt == 1:
        tina "Katakanlah Anda akan mengikuti instruksi saya!"

        anon "Y-ya!"


        if rng < .2:
            anon "Aku akan mengikutimu-"

            anon "Ya Tuhan!"


        tina "Anak baik."


    elif opt == 2:
        tina "Ahhh!"

        anon "Ini adalah-"


    elif opt == 3:
        tina "Ini sangat tebal!"

        anon "Kamu bertindak terlalu cepat!"

        tina "Fokus, wajah sayang!"


    elif opt == 4:
        tina "Bernapas saja."


    elif opt == 5:
        tina "Berikan padaku, anak besar!"


    elif opt == 6:
        anon "Kamu sangat seksi!"

        tina "Oh ya?"


    elif opt == 7:
        anon "Aku suka payudara besarmu!"

        tina "Apa lagi yang kamu suka?"


        if rng < 0 or 0 <= rng < .3:
            anon "Rambut merah menyala itu!"

            tina "Terus berlanjut!"


        if rng < 0 or .3 <= rng < .6:
            anon "Mata biru yang indah itu."

            tina "Ahhh!"


        if rng < 0 or .6 <= rng < 1:
            anon "Keledai yang tebal dan lezat ini."

            tina "Oh, {b}[firstname]{/b}..."


    return


label scene_tina_sex_lounge.switch:
    tina "Sini, biar aku ke atas lagi."

    anon "Hmm?"

    tina "Saya ingin finis di atas."

    call scene_tina_lounge_doggy.insert
    with {'master': dissolve}
    anon "Oh, uhh..."

    show tina b_sex_doggy_insert_anon as anon_body
    show tina_body_b_sex_doggy_insert_arm as anon_arm
    call scene_tina_lounge_doggy.pre
    with {'master': dissolve}
    anon "... Ya baiklah."

    hide anim
    hide leg
    show tina b_sex_inbetween f_sexy_left behind anon_body
    with {'master': dissolve}
    pause

    $ M_tina.set('sex speed', 1. / 8)

    hide anon_body
    hide anon_arm
    show tina f_sexy_down
    show anon b_tina_sex
    with {'master': dissolve}
    pause
    show anon behind tina
    jump scene_tina_sex_lounge.merge


label scene_tina_sex_lounge.cum(where):
    hide anim

    if where == 'inside':
        show tina b_sex_cum
    else:
        show tina b_sex_cumshot
        show tina_sex_body_cumshot_dick

    anon "HNNGGG!!!" with flash

    if where == 'inside':
        show xray_tina_top with fastdissolve:
            align (0, 0)

    tina "NGGHHH!!!"

    show anon b_tina_sex behind tina
    show tina b_sex_talk

    if where == 'inside':
        hide xray_tina_top
    else:
        show tina_overlay_sex_o_cumshot behind tina
        hide tina_sex_body_cumshot_dick

    with {'master': dissolve}
    pause
    anon "Haah... Haah..."

    anon "Wah!"

    anon "Itu tadi..."

    tina "Kuat?"

    anon "Y-ya."

    tina "hehe!"


    if where == 'inside':
        call call_pregnancy_minigame (None, M_tina)
    return


label scene_tina_sex_lounge.first:
    jump scene_tina_sex_lounge


label scene_tina_sex_lounge.repeat:
    $ M_tina.set('sex speed', 1. / 8)
    $ renpy.dynamic(variant='repeat')

    call scene_tina_sex_lounge.stage
    with fade
    pause
    label scene_tina_sex_lounge.merge:
    show tina b_sex_insert_pullout
    with {'master': dissolve}
    pause
    show tina b_sex_talk f_moan
    with {'master': dissolve}
    anon "!!!"
    tina f_normal @ f_moan "Haah!"

    pause
    tina "Mmm, aku sangat senang {b}Tony{/b} mengirimkanmu!"

    anon "Y-ya, aku juga!"

    call scene_tina_sex_lounge.animate
    with {'master': dissolve}
    call scene_tina_sex_lounge.dialogue (5)
    pause
    call scene_tina_sex_lounge.dialogue (6)
    pause
    call scene_tina_sex_lounge.dialogue (7)
    pause
    label scene_tina_sex_lounge.resume:
    call scene_tina_sex_lounge.loop

    if _return == 'switch':
        jump scene_tina_lounge_doggy.switch

    tina "aku akan keluar!"

    anon "Saya juga!"

    tina "Bersama-sama kalau begitu!"

    pause
    tina "Hampir!"

    tina "Di sana!!"

    call scene_tina_sex_lounge.cum (_return)
    return


label scene_tina_sex_lounge.replay:
    $ renpy.dynamic(variants=persistent.cookie_jar['tina']['variants']['01_unlocked'])

    if len(variants) > 1:
        scene expression background(l=L_tina_lounge) with fade
        menu:
            "Pertama" if 'first' in variants:
                jump scene_tina_sex_lounge.first

            "Ulangi" if 'repeat' in variants:
                jump scene_tina_sex_lounge.repeat

    jump expression 'scene_tina_sex_lounge.{}'.format(next(iter(variants)))


screen scene_tina_sex_lounge_controls():
    style_prefix 'sex'

    vbox:

        frame:
            has hbox
            textbutton _('Keep Going') action Return(False)
            textbutton _('Cum Inside') action Return('inside')
            textbutton _('Cum Outside') action Return('outside')
            if variant == 'repeat':
                textbutton _('Switch') action Return('switch')

        frame:
            has hbox
            textbutton _('« Slower'):
                action (Function(M_tina.set, 'sex speed',
                                 1 / (1 / M_tina.get('sex speed') - 2)),
                        Return(False))
                sensitive M_tina.get('sex speed') < 1 / 8.
            textbutton _('Faster »'):
                action (Function(M_tina.set, 'sex speed',
                                 1 / (1 / M_tina.get('sex speed') + 2)),
                        Return(False))
                sensitive M_tina.get('sex speed') > 1 / 16.
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
