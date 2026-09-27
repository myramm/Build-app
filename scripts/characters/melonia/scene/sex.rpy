label scene_melonia_sex:
    $ M_melonia.set('sex speed', 1. / 8)
    $ renpy.dynamic(variant='first')

    call scene_melonia_sex.stage
    with fade
    melonia @ -m_talk "MM."

    melonia "Masukkan ke dalam, {b}Hector{/b}!"

    melonia "Saya tidak sabar menunggu sedetik pun!"

    anon "Oke."

    call scene_melonia_sex.insert
    with {'master': dissolve}
    melonia "Ya Tuhan!"

    melonia "YA TUHAN!!"

    melonia f_surprised "Itu terlalu besar!"

    melonia "Ini adalah-"

    call scene_melonia_sex.animate
    with {'master': dissolve}
    melonia "Ahhh!!"

    pause
    anon "Apakah kamu baik-baik saja!"

    melonia "aku tidak bisa-"

    call scene_melonia_sex.dialogue (1)
    pause
    melonia "OHMYGODOHMYGODOHMYGOD!!!"

    anon "Inilah yang Anda inginkan..."

    melonia "{b}HEKTOR{/b}!!"

    melonia "OH, {b}HEKTOR{/b}!!!"

    hide anim
    show melonia b_sex_insert_pullout f_surprised
    with {'master': dissolve}
    melonia "Apa?!"

    melonia "Mengapa kamu-"

    show melonia b_sex_anim_hard
    anon "MY." with vpunch
    show melonia b_sex_anim_hard
    anon "NAME." with vpunch
    show melonia b_sex_anim_hard
    anon "IS." with vpunch
    show melonia b_sex_anim_hard
    anon "[firstname!u]!" with vpunch
    show melonia b_sex_insert_pullout f_moan
    with {'master': dissolve}
    call scene_melonia_sex.dialogue (2)
    show melonia f_surprised with {'master': dissolve}
    anon "Katakan!"

    melonia "{b}[firstname]{/b}?"

    call scene_melonia_sex.animate
    melonia "AHH, [nama depan!u]!"

    pause
    call scene_melonia_sex.loop
    call scene_melonia_sex.cum (_return)
    return


label scene_melonia_sex.stage:
    scene location_rump_bedroom_bed_sex
    show melonia b_sex_pre_after f_smirk
    return


label scene_melonia_sex.insert:
    show melonia b_sex_insert_pullout f_moan
    return


label scene_melonia_sex.animate:
    hide melonia
    hide melonia_body_b_sex_anim_hard
    show melonia_body_b_sex_anim as anim
    return


label scene_melonia_sex.loop:
    call screen scene_melonia_sex_controls

    if _return:
        return _return

    python hide:
        blocks = 9
        limit = 3

        renpy.dynamic(pool=random.sample(range(2 - limit, blocks + 1), limit))

    pause

    while pool:
        call scene_melonia_sex.dialogue (pool.pop(), rng=random.random())
        pause

    jump scene_melonia_sex.loop


label scene_melonia_sex.dialogue(opt, rng=-1):

    if opt == 1:
        if rng < .2:
            anon "Apakah kamu baik-baik saja!"

            melonia "aku tidak bisa-"


        melonia "Ini keterlaluan!"

        anon "Haruskah saya berhenti?"


        if variant == 'first':
            melonia "Oh, persetan denganku!!"

        else:
            melonia "Tidak, jangan berhenti!!"


        if rng < .5:
            anon "Oke."


    elif opt == 2:
        melonia "{i}* Merengek*{/i}"


    elif opt == 3:
        melonia "Ahhh!!"


    elif opt == 4:
        melonia "OHMYGODOHMYGODOHMYGOD!!!"

        anon "Inilah yang Anda inginkan..."

        melonia "[nama depan!u]!!!"

        melonia "OH, [nama depan!u]!!!!"


    elif opt == 5:
        anon "Saya senang Anda menggunakan nama asli saya sekarang."

        melonia "{i}* Merengek*{/i}"


    elif opt == 6:
        anon "Katakan!"

        melonia "{b}[firstname]{/b}!"

        anon "Lebih keras!"

        melonia "AHH, [nama depan!u]!"


    elif opt == 7:
        melonia "[nama depan!u]!"


    elif opt == 8:
        melonia "Oh, persetan denganku!!"


    elif opt == 9:
        melonia "OH, [nama depan!u]!!!!"


    return


label scene_melonia_sex.flip:
    $ M_melonia.set('sex speed', 1. / 8)

    hide anim
    call scene_melonia_bedroom_press.pre
    show melonia f_confused
    with {'master': dissolve}
    anon "Baiklah, balikkan kembali."

    melonia "Hei..."

    melonia f_annoyed "... Aku hampir sampai!"

    anon "Ya, tidak peduli."

    anon "Baliklah, aku tidak ingin melihatmu lagi."

    melonia f_eyeroll "Oh, berhentilah bersikap seperti bayi..."

    melonia "... Itu hanya pembicaraan kotor kecil."

    show melonia f_smirk
    anon "Balik!"

    anon "Lebih!"

    show melonia b_sex_transition
    with {'master': dissolve}
    melonia "{b}Hector{/b}, kamu sangat agresif hari ini!"

    call scene_melonia_sex.stage
    with {'master': dissolve}
    anon "Demi keparat..."

    anon "... Itu bukan namaku!"

    show melonia b_sex_insert_pullout f_moan
    with {'master': dissolve}
    melonia "{i}*Terkesiap*{/i} Oh ho ho ..."

    show melonia b_sex_anim01
    melonia "FUUUUUUCK!!!" with vpunch
    call scene_melonia_sex.animate
    with {'master': dissolve}
    jump scene_melonia_sex.resume


label scene_melonia_sex.switch:
    $ M_melonia.set('sex speed', 1. / 8)

    hide anim
    show melonia b_sex_insert_pullout f_smirk
    with dissolve
    anon "Saya pikir vagina Anda perlu perhatian lebih."

    show melonia b_sex_anim01
    melonia "OHMYGODOHMYGODOHMYGOD!!!" with vpunch
    call scene_melonia_sex.animate
    with {'master': dissolve}
    anon "Ini yang Anda butuhkan, bukan?"

    melonia "[nama depan!u]!!!"

    anon "Katakan!"

    melonia "Inilah yang saya butuhkan!"

    anon "Lebih keras!"

    melonia "AHH, aku sangat membutuhkannya!"

    pause
    jump scene_melonia_sex.resume


label scene_melonia_sex.cum(where, type='vaginal'):
    melonia "aku akan keluar!"

    anon "Saya juga!"

    pause
    melonia "Jangan berhenti!"

    melonia "Ya Tuhan, {b}[firstname]{/b}!!"

    melonia "JANGAN BERHENTI!!!"

    melonia "NGGHHH!!!"

    hide anim

    if where == 'inside':
        show melonia b_sex_cum
    else:
        show melonia b_sex_insert_pullout a_cumshot f_moan

    anon "HNNGGG!!!" with flash

    if where == 'inside' and type == 'vaginal':
        show xray_melonia_top with fastdissolve:
            align (0,0)
        pause
        hide xray_melonia_top with dissolve

    elif where == 'outside':
        show melonia a_empty f_satisfied
        show melonia_arms_sex_insert_pullout_a_cumshot3
        with {'master': dissolve}

    anon "Haah... Haah..."

    pause

    if where == 'inside':
        show melonia b_sex_insert_pullout f_satisfied with dissolve

    anon "Apakah kamu merasa lebih baik sekarang?"


    if where == 'inside':
        show melonia b_sex_pre_after a_after with dissolve

    melonia @ -m_talk "{i}* Merengek*{/i}"

    anon "{b}Melonia{/b}?"

    anon "Apakah kamu baik-baik saja?"

    melonia "saya tidak bisa..."

    melonia "... Bicara."

    anon "Hmm?"

    melonia "Kembang api."

    anon "Benar."

    anon "aku akan um-"


    if where == 'inside':
        anon "Oke."


        if type == 'vaginal':
            call call_pregnancy_minigame (None, M_melonia)
    else:

        anon "Ambilkanmu handuk atau apalah..."


    return


label scene_melonia_sex.first:
    jump scene_melonia_sex


label scene_melonia_sex.repeat:
    $ M_melonia.set('sex speed', 1. / 8)
    $ renpy.dynamic(variant='repeat')

    call scene_melonia_sex.stage
    with fade
    melonia "Masukkan!"

    melonia "Saya tidak sabar menunggu sedetik pun!"

    anon "Oke."

    call scene_melonia_sex.insert
    with {'master': dissolve}
    melonia "Ya Tuhan!"

    melonia "YA TUHAN!!"

    melonia "Ini sangat besar!"

    melonia "Saya pikir ini akan lebih mudah!"

    pause
    call scene_melonia_sex.animate
    with {'master': dissolve}
    call scene_melonia_sex.dialogue (3)
    pause
    call scene_melonia_sex.dialogue (1)
    pause
    call scene_melonia_sex.dialogue (4)
    pause
    call scene_melonia_sex.dialogue (5)
    pause
    call scene_melonia_sex.dialogue (6)
    pause
    label scene_melonia_sex.resume:
    call scene_melonia_sex.loop

    if _return == 'switch':
        jump scene_melonia_bedroom_press.switch
    elif _return == 'switch:anal':
        jump scene_melonia_sex_anal.switch

    call scene_melonia_sex.cum (_return)
    return


label scene_melonia_sex.replay:
    $ renpy.dynamic(variants=persistent.cookie_jar['melonia']['variants']['01_unlocked'])

    if len(variants) > 1:
        scene expression background(l=L_rump_master) with fade
        menu:
            "Pertama" if 'first' in variants:
                jump scene_melonia_sex.first

            "Ulangi" if 'repeat' in variants:
                jump scene_melonia_sex.repeat

    jump expression 'scene_melonia_sex.{}'.format(next(iter(variants)))


screen scene_melonia_sex_controls():
    style_prefix 'sex'

    vbox:

        frame:
            has hbox
            textbutton _('Keep Going') action Return(False)
            if M_anon.finished_state(S_ano20_done):
                textbutton _('Cum Inside') action Return('inside')
            textbutton _('Cum Outside') action Return('outside')

            if variant == 'repeat':
                textbutton _('Anal') action Return('switch:anal')
                textbutton _('Switch') action Return('switch')

        frame:
            has hbox
            textbutton _('« Slower'):
                action (Function(M_melonia.set, 'sex speed',
                                 1 / (1 / M_melonia.get('sex speed') - 2)),
                        Return(False))
                sensitive M_melonia.get('sex speed') < 1 / 8.
            textbutton _('Faster »'):
                action (Function(M_melonia.set, 'sex speed',
                                 1 / (1 / M_melonia.get('sex speed') + 2)),
                        Return(False))
                sensitive M_melonia.get('sex speed') > 1 / 16.
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
