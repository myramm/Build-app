label scene_melonia_bedroom_press:

    return


label scene_melonia_bedroom_press.pre:
    show melonia bedroom_press d_insert f_smirk
    return


label scene_melonia_bedroom_press.insert:
    hide melonia
    show melonia_bedroom_press 4 as anim
    return


label scene_melonia_bedroom_press.animate:
    show melonia_bedroom_press as anim
    return


label scene_melonia_bedroom_press.loop:
    call screen scene_melonia_bedroom_press_controls

    if _return:
        return _return

    python hide:
        blocks = 7
        limit = 3

        renpy.dynamic(pool=random.sample(range(2 - limit, blocks + 1), limit))

    pause

    while pool:
        call scene_melonia_bedroom_press.dialogue (pool.pop(), rng=random.random())
        pause

    jump scene_melonia_bedroom_press.loop


label scene_melonia_bedroom_press.dialogue(opt, rng=-1):

    if opt == 1:
        melonia "Ya Tuhan!!!"

        anon "Anda suka itu?"

        melonia "FUUUUCK AKU!!!"


    elif opt == 2:
        melonia "Ahhh!!"

        melonia "{b}[firstname]{/b}!"


        if rng < .7:
            anon "Lebih keras!"

            melonia "{b}[nama depan!u]{/b}!!!"


    elif opt == 3:
        if rng < .2:
            melonia "Itu dia!"


        melonia "Pukul vaginaku dengan ayam kelas pekerja kotormu!"


    elif opt == 4:
        melonia "Hancurkan aku, dasar imigran kotor!"


        if rng < .4:
            anon "Wah..."

            anon "...Tolong berhenti bicara."


    elif opt == 5:
        melonia "Graaah!!!"

        melonia "Kamu tidak akan masuk ke dalam diriku, kan {b}Hector{/b}?!"


    elif opt == 6:
        melonia "Tanah rahimku dengan benih asingmu!!"


        if rng < .4:
            anon "Oh, itu menjijikkan."

            melonia "Aku tahu!"


        melonia "Ah, itu sangat salah..."

        melonia "... Isi aku sampai penuh!"


    elif opt == 7:
        melonia "Hancurkan aku!"


    return


label scene_melonia_bedroom_press.switch:
    $ M_melonia.set('sex speed', 1. / 8)

    hide anim
    show melonia b_sex_insert_pullout f_smirk
    with {'master': dissolve}
    anon "Ini, balikkan."

    call scene_melonia_sex.stage
    with {'master': dissolve}
    melonia f_surprised @ -m_talk "Hmm?"

    anon "Di punggungmu."

    melonia f_satisfied "Oh, sepertinya aku perlu waktu sebentar..."

    anon "Apa?"

    melonia "Penismu sangat... sial... besar!"

    anon "Ya, aku sadar."

    melonia @ -m_talk "Tidak."

    anon "Ini yang kamu inginkan, ingat?"

    melonia "Vagina kecilku yang malang, itu-"

    anon "Ya, ya... Diam saja dan balik."

    show melonia b_sex_transition
    with {'master': dissolve}
    melonia "{b}Hector{/b}, saya menyukai perilaku mendominasi ini!"

    call scene_melonia_bedroom_press.pre
    with {'master': dissolve}
    anon "Sudah kubilang jangan panggil aku seperti itu!"

    melonia f_coy "Oh?"

    pause
    melonia "Konyolnya aku..."

    pause
    melonia "... Aku pasti lupa."

    anon "Mungkin ini bisa membantu Anda mengingatnya?"

    call scene_melonia_bedroom_press.insert
    with {'master': dissolve}
    melonia "{i}*Terkesiap*{/i} Ya!"

    call scene_melonia_bedroom_press.animate
    with {'master': dissolve}
    call scene_melonia_bedroom_press.dialogue (1)
    anon "Sebutkan namaku!"

    melonia "{b}Hektor{/b}!!!"


    $ M_melonia.set('sex speed', 1. / 14)

    anon "No!" with vpunch
    call scene_melonia_bedroom_press.dialogue (2)
    pause
    call scene_melonia_bedroom_press.dialogue (3)
    anon "Apa?!"

    call scene_melonia_bedroom_press.dialogue (4)
    pause
    call scene_melonia_bedroom_press.dialogue (5)

    if M_anon.finished_state(S_ano20_done):
        anon "Berapa kali aku harus memberitahumu untuk berhenti meneleponku {b}Hector{/b}?!"

        melonia "Katakan padaku kamu akan masuk ke dalam diriku!"

        anon "Mengapa?"

    else:

        anon "Umm, bukankah kamu memberitahuku secara spesifik {i}tidak{/i} untuk melakukan itu?"

        melonia "Main saja, saya hampir sampai!"


    call scene_melonia_bedroom_press.dialogue (6)
    pause
    call scene_melonia_bedroom_press.dialogue (7)
    call scene_melonia_bedroom_press.loop

    if _return == 'switch':
        jump scene_melonia_sex.flip

    if _return == 'switch:blow':
        jump scene_melonia_bedroom_blowjob.switch

    melonia "Oh, berikan aku ayam ilegal yang besar itu!"

    anon "Ini sangat kacau..."

    melonia "aku akan keluar!!"

    anon "... Ngh, aku juga!"

    melonia "aku akan-"

    melonia "NGGHHH!!!"


    if _return == 'inside':
        show melonia_body_b_sex_missionary_cum as anim
    else:
        hide anim
        show melonia bedroom_press d_cumshot

    anon "HNNGGG!!!" with flash

    if _return == 'inside':
        show xray_front_top as xray:
            anchor (.5, .5)
            pos (250 + 115, 250 + 176)
            rotate 84
            rotate_pad False
            xzoom -1
            zoom .88
    else:
        show melonia bedroom_press d_cumshot2
        with {'master': dissolve}

    melonia "Fuuuuuuuuuuuuuuck!!"

    pause
    hide xray

    if _return == 'inside':
        hide anim
        show melonia bedroom_press d_after

    with {'master': dissolve}
    anon "Haah... Haah..."

    return 'creampie' if _return == 'inside' else 'cumshot'


screen scene_melonia_bedroom_press_controls():
    style_prefix 'sex'

    vbox:

        frame:
            has hbox
            textbutton _('Keep Going') action Return(False)
            if M_anon.finished_state(S_ano20_done):
                textbutton _('Cum Inside') action Return('inside')
            textbutton _('Cum Outside') action Return('outside')
            textbutton _('Shut Up') action Return('switch:blow')
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
