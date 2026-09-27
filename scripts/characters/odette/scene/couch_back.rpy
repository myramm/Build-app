label scene_odette_couch_back:

    return


label scene_odette_couch_back.stage:
    scene location_tattoo_garage_sex_couch
    show odette_sex_couch_back_base as anim
    show odette_sex_couch_back_base_anon as legs
    show odette sex_couch_back
    show odette_sex_couch_back_pre as overlay
    return


label scene_odette_couch_back.insert:
    hide legs
    show odette_sex_couch_back_insert as overlay
    return


label scene_odette_couch_back.animate:
    hide odette
    hide overlay
    show odette_sex_couch_back as anim
    return


label scene_odette_couch_back.loop:
    call screen scene_odette_sex_couch_controls

    if _return:
        return _return

    python hide:
        blocks = 5
        limit = 3

        renpy.dynamic(pool=random.sample(range(2 - limit, blocks + 1), limit))

    pause

    while pool:
        call scene_odette_couch_back.dialogue (pool.pop(), rng=random.random())
        pause

    jump scene_odette_couch_back.loop


label scene_odette_couch_back.dialogue(opt, rng=-1):

    if opt == 1:
        odette "Oooh, ya..."

        odette "... Itu dia, kawan."


    elif opt == 2:
        odette "Bagus dan dalam..."

        odette "... Persis seperti itu!"


    elif opt == 3:
        if rng < .5:
            odette "Sial!"


        anon "Fiuh, kamu tidak bercanda..."

        odette "Hmm?"

        anon "... Lihat saja hal-hal itu!"

        odette "Oh, hehe!"


    elif opt == 4:
        odette "Oof!" with hpunch

        if rng < 0:
            odette "Apa itu tadi?!"

            anon "Maaf."

            anon "Saya hanya mencoba melihat seberapa tinggi saya bisa membuat mereka memantul."


        odette "{b}[firstname]{/b}, berhenti main-main dan fokus!"

        anon "Aku tidak bisa menahannya, mereka memesona."


        if rng < .5:
            odette "Ayolah, aku hampir sampai!"


    elif opt == 5:
        odette "Ahhh!"

        odette "Sangat dalam!"


        if rng < .5:
            anon "Anda suka itu?"

            odette "Ya!"


    elif opt == 5:
        odette "Sial, {b}Eve{/b} beruntung sekali..."

        odette "... Aku tidak percaya pacar pertamanya dan dia punya penis sebagus ini!"


        if rng < .5:
            anon "Dick, kamu secara teknis mencuri darinya."

            odette "Bukan mencuri..."

            odette "... Meminjam!"

            anon "Mhmm."


    elif opt == 6:
        odette "Lebih cepat, kawan!"


    return


label scene_odette_couch_back.cum(where):
    odette "Aku semakin dekat!"

    anon "Saya juga!"

    odette "Lebih sulit, {b}[firstname]{/b}!!"

    anon "Aku sedang mencoba tapi-"

    anon "aku tidak bisa-"

    odette "NGGHHH!!!"


    if where == 'inside':
        show odette_sex_couch_back_cum as anim
    else:
        show odette_sex_couch_back_base as anim
        show odette_sex_couch_back_base_anon as legs
        show odette sex_couch_back f_surprised m_talk
        show odette_sex_couch_back_cumshot as cum

    anon "HNNGGG!!!" with flash

    if where == 'inside':
        show xray_left_back as xray with fastdissolve:
            anchor (.5, .5)
            pos (250 + 323, 250 + 96)
            rotate -15
            rotate_pad False
            zoom 1.02

    pause
    hide xray

    if where == 'inside':
        show odette_sex_couch_back_base as anim
        show odette_sex_couch_back_base_anon as legs
        show odette sex_couch_back
        show odette_sex_couch_back_pre as overlay
        show odette_sex_couch_back_pullout as cum
    else:
        show odette -f_surprised

    with {'master': dissolve}
    anon "Haah... Haah..."

    odette -m_talk "Fiuh, astaga, itu bagus!"

    anon "Ya?"

    odette "Heh, kita harus melakukan ini lebih sering!"

    anon "Aku tidak tahu tentang itu..."


    if where == 'inside':
        call call_pregnancy_minigame (None, M_odette)
    return


label scene_odette_couch_back.switch:
    $ M_odette.set('sex speed', 1 / 8.)
    $ rv.add('vaginal')
    $ renpy.dynamic(switch=True)

    if 'a->v' not in rv:
        $ rv.add('a->v')
        call scene_odette_couch_anal.stage
        with dissolve
        odette "{b}[firstname]{/b}?!"

        odette "Aku hampir sampai!!!"

        anon "Jangan khawatir."

        call scene_odette_couch_back.stage
        with fade
        anon "Kita belum selesai!"

        odette "Tunggu sebentar..."

        odette "... Kamu tidak seharusnya melakukan double dip, itu-"

        call scene_odette_couch_back.insert
        odette f_surprised "Oh, fuck shit balls!!" with hpunch
        call scene_odette_couch_back.animate
        with {'master': dissolve}
        anon "Apa yang tadi kamu katakan?"

        odette "Tidak ada, tidak ada..."

        odette "... Lanjutkan!"

    else:

        call scene_odette_couch_anal.stage
        with dissolve
        odette "Lagi?!"

        odette "Dengan serius?!"

        call scene_odette_couch_back.stage
        with fade
        anon "Saya tidak bisa memutuskan lubang mana yang lebih saya sukai..."

        odette "Heh, kamu beruntung aku pelacur kotor..."

        odette "... Cukup yakin tidak ada gadis lain yang akan membiarkanmu pergi bersama-"

        call scene_odette_couch_back.insert
        odette f_surprised "Fuuuuuuuuck me!!" with hpunch
        call scene_odette_couch_back.animate
        with {'master': dissolve}
        anon "Itu rencananya!"

        odette "Ya Tuhan, ya Tuhan, Ya Tuhan!!!"


    pause
    jump scene_odette_couch_back.resume


label scene_odette_couch_back.repeat(switch):
    $ M_odette.set('sex speed', 1 / 8.)
    $ renpy.dynamic(rv={'vaginal'})

    call scene_odette_couch_back.stage
    with fade
    anon "Ini pemandangan yang luar biasa!"

    odette "Heh, tempelkan saja padaku..."

    anon "Hei, kamu tidak bisa membenci pria karena menghargai pemandangan!"

    odette "Ya, baiklah... Aku bisa membencimu karena menggodaku dengan-"

    call scene_odette_couch_back.insert
    with {'master': dissolve}
    odette f_lipbite @ -m_talk "Tidak!!"

    anon "Lebih baik?"

    odette -f_lipbite "Ya!!"

    call scene_odette_couch_back.animate
    with dissolve
    call scene_odette_couch_back.dialogue (1)
    pause
    call scene_odette_couch_back.dialogue (2)
    pause
    call scene_odette_couch_back.dialogue (3)
    pause
    call scene_odette_couch_back.dialogue (4)
    pause
    call scene_odette_couch_back.dialogue (5)
    pause
    call scene_odette_couch_back.dialogue (6)
    pause

    label scene_odette_couch_back.resume:
    call scene_odette_couch_back.loop

    if _return == 'switch':
        jump scene_odette_couch_anal.switch

    call scene_odette_couch_back.cum (_return)
    return rv


label scene_odette_couch_back.anal:
    jump scene_odette_couch_anal


label scene_odette_couch_back.back:
    call scene_odette_couch_back.repeat ('anal' in variants)
    return


label scene_odette_couch_back.replay:
    $ renpy.dynamic(variants=persistent.cookie_jar['Odette']['variants']['06_unlocked'])

    if len(variants) > 1:
        scene expression background(l=L_tattooparlor_garage, t=2) with fade
        menu:
            "Biasa" if 'back' in variants:
                jump scene_odette_couch_back.back

            "Anal Pertama" if 'anal' in variants:
                jump scene_odette_couch_back.anal
    else:

        jump expression 'scene_odette_couch_back.{}'.format(next(iter(variants)))

    return



screen scene_odette_sex_couch_controls():
    style_prefix 'sex'

    vbox:

        frame:
            has hbox
            textbutton _('Keep Going') action Return(False)
            textbutton _('Cum Inside') action Return('inside')
            textbutton _('Cum Outside') action Return('outside')

            if switch:
                textbutton _('Switch') action Return('switch')

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
