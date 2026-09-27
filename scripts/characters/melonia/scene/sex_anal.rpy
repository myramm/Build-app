label scene_melonia_sex_anal:

    return


label scene_melonia_sex_anal.insert:
    hide anim
    show melonia b_sex_anim_anal01
    return


label scene_melonia_sex_anal.animate:
    hide melonia
    show melonia_body_b_sex_anim_anal as anim
    return


label scene_melonia_sex_anal.loop:
    call screen scene_melonia_sex_anal_controls

    if _return:
        return _return

    python hide:
        blocks = 5 if anal == 'first' else 7
        limit = 3

        renpy.dynamic(pool=random.sample(range(2 - limit, blocks + 1), limit))

    pause

    while pool:
        call scene_melonia_sex_anal.dialogue (pool.pop(), rng=random.random())
        pause

    jump scene_melonia_sex_anal.loop


label scene_melonia_sex_anal.dialogue(opt, rng=-1):

    if opt == 1:
        if rng < 0:
            anon "Apakah kamu ingin aku berhenti?"

            melonia "Entahlah, ini aneh..."

            anon "Aneh sekali?"

            melonia "T-tidak, hanya-"


        melonia "{i}*Terkesiap*{/i} Astaga!"


    elif opt == 2:
        anon "Kalau begitu, kamu menyukainya?"


        if rng < 0:
            melonia "Hah?"


        if rng < .35:
            melonia "Entahlah... Mungkin..."

            anon "Ini pertanyaan ya atau tidak, {b}Melonia{/b}."


        melonia "Grr, diam dan persetan denganku!"

        anon "Baiklah."


    elif opt == 3:
        melonia "FUUUUUUCK!!"


    elif opt == 4:
        melonia "Rasanya seperti kamu akan mematahkan tulang punggungku!"

        anon "Saya bisa berhenti jika Anda-"

        melonia "Jangan berani-berani berhenti!"


    elif opt == 5:
        melonia "AAH!!"

        melonia "Ini luar biasa!!"


    elif opt == 6:
        melonia "Sial ya!!"


    elif opt == 7:
        melonia "Tidak, itu dia!"

        melonia "Gunakan aku seperti aku gadis kotor!!"


    return


label scene_melonia_sex_anal.switch:
    $ M_melonia.set('sex speed', 1 / 8.)

    if not M_melonia.once('done_anal'):
        jump scene_melonia_sex_anal.first

    jump scene_melonia_sex_anal.repeat


label scene_melonia_sex_anal.first:
    $ renpy.dynamic(anal='first')

    hide anim
    show melonia b_sex_insert_pullout f_smirk
    with {'master': dissolve}
    melonia "A-apa yang kamu lakukan?"

    anon "Mencoba sesuatu yang baru..."

    pause
    melonia f_surprised "Apakah kamu gila?!"

    melonia "Benda itu tidak akan muat di pantatku!"

    anon "Tentu saja itu akan terjadi."

    melonia "Tidak itu-"

    call scene_melonia_sex_anal.insert
    melonia "!!!" with hpunch
    melonia "Sialan, {b}[firstname]{/b}!"

    anon "Apakah kamu baik-baik saja?"

    melonia "Tidak, aku tidak baik-baik saja!"

    melonia "Penismu terlalu besar untuk-"

    call scene_melonia_sex_anal.animate
    with {'master': dissolve}
    melonia "!!!"
    pause
    call scene_melonia_sex_anal.dialogue (1)
    pause
    call scene_melonia_sex_anal.dialogue (2)
    pause
    call scene_melonia_sex_anal.dialogue (3)
    jump scene_melonia_sex_anal.resume


label scene_melonia_sex_anal.repeat:
    $ renpy.dynamic(anal='repeat')

    melonia "Bisakah kamu, mungkin... Memasukkannya ke dalam pantatku lagi?"

    hide anim
    show melonia b_sex_insert_pullout f_smirk
    with {'master': dissolve}
    anon "Aku tahu kamu menikmatinya."

    melonia "Mmm, diam dan lakukan!"

    call scene_melonia_sex_anal.insert
    melonia "!!!" with hpunch
    call scene_melonia_sex_anal.animate
    with {'master': dissolve}
    call scene_melonia_sex_anal.dialogue (6)
    pause
    call scene_melonia_sex_anal.dialogue (7)
    pause
    label scene_melonia_sex_anal.resume:
    call scene_melonia_sex_anal.dialogue (4)
    pause
    call scene_melonia_sex_anal.dialogue (5)
    call scene_melonia_sex_anal.loop

    if _return == 'switch':
        jump scene_melonia_sex.switch

    call scene_melonia_sex.cum (_return, type='anal')

    return


screen scene_melonia_sex_anal_controls():
    style_prefix 'sex'

    vbox:

        frame:
            has hbox
            textbutton _('Keep Going') action Return(False)
            textbutton _('Cum Inside') action Return('inside')
            textbutton _('Cum Outside') action Return('outside')
            textbutton _('Vaginal') action Return('switch')

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
