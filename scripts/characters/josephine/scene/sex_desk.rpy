label scene_josie_sex_desk:

    return


label scene_josie_sex_desk.stage:
    scene location_dealership_office_desk_sex
    show josephine_sex_top_insert as anim
    show josephine sex_top
    return


label scene_josie_sex_desk.insert:
    hide josephine
    show josephine_sex_top_slide as anim
    return


label scene_josie_sex_desk.animate:
    show josie_sex_desk as anim
    return


label scene_josie_sex_desk.loop:
    call screen scene_josie_sex_desk_controls

    if _return:
        return _return

    python hide:
        blocks = 7
        limit = 3

        renpy.dynamic(pool=random.sample(range(2 - limit, blocks + 1), limit))

    pause

    while pool:
        call scene_josie_sex_desk.dialogue (pool.pop(), rng=random.random())
        pause

    jump scene_josie_sex_desk.loop


label scene_josie_sex_desk.dialogue(opt, rng=-1):

    if opt == 1:
        josephine "Ya ampun, ini latihan sialan!"


        if rng < .5:
            anon "Benar-benar?"


        anon "Saya cukup nyaman."

        josephine "Hah hah... lucu sekali."


    elif opt == 2:
        josephine "Oke, sekarang aku mulai berkeringat..."


        if rng < .5:
            josephine "... Mungkin Anda harus menjadi yang teratas sebentar?"


        anon "Sedikit keringat tidak akan membunuhmu."

        josephine "Grrraah."


    elif opt == 3:
        anon "Fiuh, ya!"

        anon "Pantulkan pantat itu, {b}Josephine{/b}!"


    elif opt == 4:
        josephine "Anda tahu..."

        josephine "... ini..."

        josephine "... sungguh..."

        josephine "...Ngh, {i}keras{/i}!"

        anon "Heh... Ya, benar."


        if rng < .5:
            josephine "Aku tidak sedang membicarakan penismu, {b}[firstname]{/b}!"


    elif opt == 5:
        anon "Ya, itu saja."

        anon "Kerjakan ayam besar itu!"

        josephine "Ngh, sial!"


    elif opt == 6:
        josephine "Saya harap Anda menghargai ini!"

        anon "Oh, benar."


        if rng < .5:
            anon "Terus berlanjut!"


    elif opt == 7:
        josephine "Gan!"

        josephine "Itu terus mencapai titik terendah."

        anon "Saya bisa merasakannya."


        if rng < .5:
            josephine "Saya rasa saya tidak dapat mengambil lebih banyak lagi!"


    return


label scene_josie_sex_desk.switch:
    $ M_josie.set('sex speed', 1 / 8.)

    anon "Anda ingin menjadi yang teratas lagi?"

    josephine "Tidak juga."

    call scene_josie_sex.insert ('fast')
    show josephine -f_moan
    with {'master': dissolve}
    anon "Ayolah?"

    pause
    josephine "Uh, baiklah..."


    call scene_josie_sex_desk.stage
    with fade
    anon "Kamu punya pantat kecil yang lucu!"

    josephine "Hmm, oke?"

    call scene_josie_sex_desk.insert
    with {'master': dissolve}
    josephine "{i}*Ittthhh*{/i}"

    anon "Persetan denganku!"

    call scene_josie_sex_desk.animate
    with dissolve
    jump scene_josie_sex_desk.resume


label scene_josie_sex_desk.inside:
    josephine "Ayo, {b}[firstname]{/b}!"

    josephine "Aku ingin merasakannya di dalam diriku!!"

    pause
    josephine "Ah, sial!!"

    show josephine_sex_top_cum as anim
    anon "HNNGGG!!!" with flash
    show xray_under as xray:
        anchor (.5, .5)
        pos (250 + 262, 250 + 147)
        rotate -66
        rotate_pad False
        xzoom -1
        zoom .72
    with {'master': fastdissolve}
    pause
    hide xray
    anon "Haah... Haah..."

    josephine "Haah... Haah..."

    pause
    anon "Saya pikir Anda bisa melepaskan saya sekarang."

    josephine "Hehe, diamlah!"

    show josephine_sex_top_pullout as anim
    show josephine sex_top
    show josephine_sex_top_after_dick1 as penis
    show josephine_sex_top_pullout_creampie1 as cum
    with {'master': dissolve}
    josephine "Astaga, ini seperti mencoba memanjat tiang pagar."

    anon "Haha!"

    show josephine_sex_top_after_dick2 as penis
    show josephine_sex_top_pullout_creampie2 as cum
    show josephine_sex_top_pussy_closed as pussy behind penis
    with {'master': dissolve}
    josephine "Sialan."

    anon "Oh, itu pemandangan yang bagus."

    pause

    call call_pregnancy_minigame (None, M_josie)
    return 'inside'


label scene_josie_sex_desk.outside:
    anon "Oh, ini dia!"

    pause
    anon "Ini dia-"

    show josephine_sex_top_fall as anim
    show josephine_sex_top_rope1 as rope1
    anon "HNNGGG!!!" with flash
    show josephine_sex_top_after as anim
    show josephine b_sex_top f_angry_closed
    show josephine_sex_top_after_arm_down as arm
    show josephine_sex_top_cumshot3 as rope1
    show josephine_sex_top_dick3 as penis
    with {'master': fastdissolve}
    josephine "Waaagh!" with vpunch
    show josephine f_annoyed_behind
    pause
    josephine "{b}[firstname]{/b}, apa-apaan ini?"

    hide penis
    show josephine_sex_top_rope2 as rope2
    show josephine f_surprised_down_more
    anon "NGGHHH!!!"

    show josephine_sex_top_cumshot6 as rope2
    show josephine_sex_top_dick3 as penis
    show josephine f_angry_closed
    with {'master': fastdissolve}
    josephine "!!!" with hpunch
    pause
    show josephine_sex_top_after_dick2 as penis
    with {'master': dissolve}
    anon "Haah... Haah..."

    show josephine f_annoyed_down_blink
    with {'master': dissolve}
    pause
    josephine @ f_annoyed_back_blink "Apakah kamu bercanda?!"

    anon "Itu."

    anon "Dulu."

    anon "LUAR BIASA!"

    josephine @ f_annoyed_back_blink "Pfft, bagimu mungkin..."

    pause
    return 'outside'


label scene_josie_sex_desk.repeat:
    $ M_josie.set('sex speed', 1 / 8.)
    $ renpy.dynamic(rv=set())

    call scene_josie_sex_desk.stage
    with fade
    josephine "Ya ampun, benda ini tidak mudah untuk diduduki..."

    josephine "Di sini kita-"

    call scene_josie_sex_desk.insert
    with {'master': dissolve}
    josephine "{i}*Ittthhh*{/i}"

    anon "Oh ya... bagus sekali!"

    call scene_josie_sex_desk.animate
    with dissolve
    pause
    anon "Umm, haruskah kamu benar-benar menggunakan ponselmu saat kita melakukan ini?"

    josephine "Hmm?"

    anon "Aku hanya khawatir kamu akan jatuh dari meja atau semacamnya..."

    josephine "Oh, Tenang, potongan mangkuk..."

    josephine "... Ini meja yang besar..."

    josephine "... Aku tidak akan terjatuh!"

    anon "Oh oke."

    pause
    anon "Apa yang kamu lakukan pada benda itu?"

    josephine "Mengirim SMS dengan rekan lama saya di toko pakaian."

    anon "Kamu mengirim pesan?!"

    josephine "Mhmm."

    pause
    anon "Cukup yakin Anda tidak boleh mengirim pesan teks saat mengoperasikan alat berat."

    josephine "Hehe, oh tolong!"

    josephine "Penismu tidak dihitung sebagai alat berat, {b}[firstname]{/b}."

    anon "Tidak?"

    pause
    call scene_josie_sex_desk.dialogue (1)
    pause
    call scene_josie_sex_desk.dialogue (2)
    pause
    call scene_josie_sex_desk.dialogue (3)
    pause
    call scene_josie_sex_desk.dialogue (4)
    pause
    call scene_josie_sex_desk.dialogue (5)
    pause
    call scene_josie_sex_desk.dialogue (6)
    pause
    call scene_josie_sex_desk.dialogue (7)
    pause

    label scene_josie_sex_desk.resume:
    call scene_josie_sex_desk.loop
    if _return == 'switch':
        jump scene_josie_sex.switch

    anon "Ya ampun..."

    anon "... Aku semakin dekat!"

    josephine "Lakukan!"

    pause
    josephine "Cepatlah, aku tidak bisa meneruskan ini!"


    if _return == 'inside':
        jump scene_josie_sex_desk.inside

    jump scene_josie_sex_desk.outside


label scene_josie_sex_desk.replay:
    jump scene_josie_sex_desk.repeat


screen scene_josie_sex_desk_controls():
    style_prefix 'sex'

    vbox:

        frame:
            has hbox
            textbutton _('Keep Going') action Return(False)
            textbutton _('Cum Inside') action Return('inside')
            textbutton _('Cum Outside') action Return('outside')
            textbutton _('Switch') action Return('switch')

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
