image josie_sex_slow_anon = AnimatedImage('josephine_office_sex_mc_slow', (7,8,9,10,1,2,3,4,5,6), M_josie)
image josie_sex_slow_josie = AnimatedImage('josephine_office_sex_josephine_slow', (7,8,9,10,1,2,3,4,5,6), M_josie)

image josie_sex_fast_anon = AnimatedImage('josephine_office_sex_mc_fast', (6,7,8,1,2,3,4,5), M_josie)
image josie_sex_fast_josie = AnimatedImage('josephine_office_sex_josephine_fast', (6,7,8,1,2,3,4,5), M_josie)


label scene_josie_sex:
    call scene_josie_sex.stage ('office')
    with fade
    anon "Wow, kamu benar-benar basah!"

    josephine "Heh, apa yang bisa kubilang... Bocah kulit putih kutu buku membuatku bergairah..."

    anon "Benar-benar?"

    josephine "Ugh, diam saja dan masukkan ke dalam diriku!"

    call scene_josie_sex.insert ('fast')
    with fastdissolve
    josephine f_shy @ f_moan "Oh wah!!"

    anon "Kamu baik-baik saja?"

    josephine "Y-ya, hanya-"

    josephine "Ngh, kamu benar-benar besar!"

    anon "Apakah Anda ingin saya melakukannya perlahan atau apa?"

    josephine f_normal "Tidak, persetan!"

    josephine "Saya bisa menerimanya."

    pause
    josephine "Persetan denganku, {b}[firstname]{/b}!"

    anon "Baiklah."

    call scene_josie_sex.animate ('fast')
    josephine "!!!"
    josephine "FUUUUUUCK!"

    pause
    anon "Kamu baik-baik saja?"

    josephine "Ya!!"

    pause
    josephine "Ini luar biasa!"

    pause
    josephine "Oh, {b}[firstname]{/b}!"

    pause
    josephine "Persetan denganku!!"

    josephine "PERCAYA AKU LEBIH KERAS!!"

    anon "Ssst!"

    josephine "Jangan diamkan aku!"

    pause
    josephine "AAH!!"

    josephine "ITU SANGAT DALAM!"

    anon "Seseorang akan mendengarmu!"

    josephine "SAYA TIDAK PEDULI!"

    pause
    josephine "AKU CUMMING!!"

    josephine "aku cum-"

    sato "Apa yang sedang terjadi di-"

    return


label scene_josie_sex.stage(venue):
    if venue == 'lounge':
        scene location_dealership_lounge_sex
        show josephine_sex_table2 as table
        show josephine b_sex_pre_top
        show josephine_body_b_sex_overlay_leg_fix as leg
    else:
        scene location_dealership_office_sex
        show josephine_sex_table1 as table
        show josephine b_sex_pre_top_no_phone
    show mc_josephine_sex pre behind table
    return


label scene_josie_sex.insert(speed):
    hide animation1
    hide animation2
    show mc_josephine_sex insert behind table
    if speed == 'slow':
        show josephine b_sex_insert_top f_moan
    else:
        show josephine b_sex_insert_top_no_phone f_moan
    return


label scene_josie_sex.animate(speed):
    python:
        anim_toggle = True
        animated = True
        M_josie.set('sex speed', .12)
    hide josephine
    hide leg
    hide mc_josephine_sex
    show expression 'josie_sex_{}_anon'.format(speed) as animation1 behind table
    show expression 'josie_sex_{}_josie'.format(speed) as animation2
    with dissolve
    return


label scene_josie_sex.loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 3:
        if anim_toggle:
            if not animated:
                show josie_sex_fast_anon as animation1 behind table
                show josie_sex_fast_josie as animation2
                with dissolve
                $ animated = True
            pause 5
            call scene_josie_sex.dialogue
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [6,7,8,1,2,3,4,5]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "josephine_office_sex_mc_fast {}".format(pose_list[pose_counter]) as animation1 behind table
                show expression "josephine_office_sex_josephine_fast {}".format(pose_list[pose_counter]) as animation2
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call scene_josie_sex.dialogue
        $ animcounter += 1
    call screen scene_josie_sex_controls()
    if not _return:
        jump scene_josie_sex.loop
    return _return


label scene_josie_sex.dialogue:
    if animcounter == 0 and randomizer() > 50:
        josephine "AHH!!{p=1}{nw}"

    if animcounter == 1 and randomizer() > 50:
        josephine "PERCAYA AKU!!{p=1}{nw}"

        anon "Sst, ayahmu akan mendengarkanmu!{p=2}{nw}"

        josephine "SAYA TIDAK PEDULI!{p=1}{nw}"

    if animcounter == 2 and randomizer() > 50:
        josephine "Ya Tuhan!{p=1}{nw}"

    elif animcounter == 2 and randomizer() > 75:
        josephine "Jangan!{p=1}{nw}"

        josephine "Berhenti!{p=1}{nw}"

    return


label scene_josie_sex.cum(venue, where):
    hide animation1
    hide animation2
    show josephine b_sex_cum_top
    show mc_josephine_sex cum behind table

    if where != 'inside':
        show josephine_sex_cum_cumshot

    anon "HNNGGG!!!" with flash
    if where == 'inside':
        show xray_josephine_top with fastdissolve:
            align (0, 0)
    josephine "NGGHHH!!!"

    if venue == 'lounge':
        show josephine_body_b_sex_overlay_leg_fix as leg
    hide xray_josephine_top
    if where != "inside":
        hide josephine_sex_cum_cumshot
        show josephine b_sex_pre_top_no_phone o_sex_after_cumshot_no_phone f_moan
        show mc_josephine_sex pre
    else:
        show mc_josephine_sex pullout
        show josephine b_sex_pullout_top_no_phone f_moan
    with dissolve
    pause
    anon "Haah... Haah..."

    if where == 'inside':
        show josephine b_sex_after_top_no_phone f_normal
        show mc_josephine_sex after
    else:
        show josephine f_normal
    with dissolve
    return where


label scene_josie_sex.morning:
    call scene_josie_sex.stage ('lounge')
    with fade
    anon "Apa yang kamu lakukan hari ini?"

    josephine "Hanya ngobrol dengan beberapa orang."

    anon "Bagaimana dengan?"

    josephine "Oh, hanya hal yang membosankan..."

    josephine "Video game, camilan, momen buruk-"

    call scene_josie_sex.insert ('slow')
    with fastdissolve
    josephine f_normal @ f_moan "MOOOOOVVVIESS!"

    anon "hehe."

    josephine "Brengsek!"

    call scene_josie_sex.animate ('slow')
    pause
    josephine "Sial, itu dalam!!"

    anon "Mmhmm."

    pause
    josephine "Orang-orang ini punya selera film terburuk, sumpah..."

    anon "Oh ya?"

    josephine "Mereka terus mengungkit hal ini, tentang marinir futuristik yang memerangi serangga luar angkasa raksasa..."

    anon "Maksudmu, Startroopers Galaxyship?"

    josephine "Ya, itu dia."

    anon "Saya suka film itu!"

    josephine "Eh, kamu juga?"

    anon "Ya, itu luar biasa!"

    pause
    josephine "Mungkin itu hanya masalah laki-laki..."

    anon "Apa?"

    josephine "Menyukai film jelek."

    anon "Oh."

    josephine "Maksudku, tidak ada yang menentang fiksi ilmiah tapi aku-"

    call scene_josie_sex.animate ('fast')
    $ M_josie.set('sex speed', .09)
    josephine "Haah, sial!!!"

    pause
    anon "Apa yang kamu katakan?"

    josephine "Hmm?"

    josephine "Oh, aku tidak tahu... Terus lakukan itu!"

    anon "Hehe, baiklah."

    call scene_josie_sex.loop
    josephine "SIALAN, AKU AKAN CUM!"

    anon "Saya juga!"

    pause
    call scene_josie_sex.cum ('lounge', _return)
    if _return == "inside":
        josephine "Mmm, aku akan merasakannya besok..."

    else:
        josephine "Mmm, itu air mani yang banyak..."

    anon "Lebih baik daripada ngobrol online, ya?"

    josephine "Hehe, ya..."

    pause
    josephine "Bantu aku berdiri."


    if _return == 'inside':
        call call_pregnancy_minigame (None, M_josie)
    return


label scene_josie_sex.afternoon:
    call scene_josie_sex.stage ('lounge')
    with fade
    anon "Wow, kamu benar-benar basah!"

    josephine "Ya, saya sedang menonton aliran seni dewasa..."

    anon "Jadi Anda menonton film porno saat istirahat makan siang?"

    josephine "Itu bukan porno, bodoh..."

    josephine "Itu adalah-"

    call scene_josie_sex.insert ('slow')
    with fastdissolve
    josephine f_normal @ f_moan "AAAAARRRTTT!!"

    anon "hehe."

    josephine "Sangat lucu."

    call scene_josie_sex.animate ('slow')
    pause
    josephine "Sial, itu dalam!!"

    anon "Mmhmm."

    pause
    anon "Jadi apa yang dia streaming hari ini?"

    josephine "Hanya hal-hal latar belakang yang membosankan."

    anon "Apa, tidak ada payudara?"

    josephine "Aku tidak memperhatikan payudaranya, tahu?!"

    anon "Tentu Anda tidak..."

    pause
    anon "Bisakah kamu meletakkan teleponnya?"

    josephine "Hmm?"

    josephine "Tidak, sudah kubilang aku akan menonton streamingku..."

    call scene_josie_sex.animate ('fast')
    $ M_josie.set('sex speed', .09)
    josephine "Haah, sial!!!"

    anon "Itu lebih baik."

    pause
    josephine "Heh, kamu brengsek!"

    anon "Anda tidak menyukainya?"

    josephine "Ngh, aku tidak mengatakan itu!"

    call scene_josie_sex.loop
    josephine "SIALAN, AKU AKAN CUM!"

    anon "Saya juga!"

    pause
    call scene_josie_sex.cum ('lounge', _return)
    if _return == "inside":
        josephine "Mmm, aku akan merasakannya besok..."

    else:
        josephine "Mmm, itu air mani yang banyak..."

    anon "Lebih baik dari aliran seni, ya?"

    josephine "Hehe, ya..."

    pause
    josephine "Bantu aku berdiri."


    if _return == 'inside':
        call call_pregnancy_minigame (None, M_josie)
    return


label scene_josie_sex.switch:
    $ M_josie.set('sex speed', .12)

    josephine "Haah... Haah..."

    anon "Baiklah, aku akan mengambil alih sebentar."

    call scene_josie_sex_desk.stage
    with dissolve
    josephine "Fiuh, terima kasih!"


    call scene_josie_sex.stage ('office')
    with fade

    if 'kink' not in rv:
        $ rv.add('kink')
        anon "Wow, kamu benar-benar basah!"

        josephine "Sudah kubilang ini benar-benar membuatku bergairah..."

        anon "Kamu cukup aneh, ya?"

        josephine "Apa?!"

        josephine "Aku tidak nakal, aku hanya-"

        call scene_josie_sex.insert ('fast')
        with fastdissolve
        josephine f_shy @ f_moan "Ahhh, sial!!"

        anon "Anda tadi bilang?"

        josephine "Baiklah, aku keriting."

        josephine "Tolong, persetan denganku!"

    else:
        anon "Lebih baik?"

        josephine "Hmm, jauh lebih baik."

        call scene_josie_sex.insert ('fast')
        with fastdissolve
        josephine f_shy @ f_moan "Ahhh!"

        anon "Terasa enak?"

        josephine "Ya ya!"


    call scene_josie_sex.animate ('fast')
    $ M_josie.set('sex speed', .09)
    josephine "!!!"
    josephine "FUUUUUUCK!"

    pause
    anon "Anda suka itu?"

    josephine "Ya!!"

    pause
    josephine "Ini luar biasa!"

    pause
    josephine "Oh, {b}[firstname]{/b}!"

    pause
    josephine "Persetan denganku!!"

    josephine "PERCAYA AKU LEBIH KERAS!!"

    anon "Ssst!"

    josephine "Jangan diamkan aku!"

    pause
    josephine "AAH!!"

    josephine "ITU SANGAT DALAM!"

    anon "Seseorang akan mendengarmu!"

    josephine "SAYA TIDAK PEDULI!"


    call scene_josie_sex.loop
    if _return == 'switch':
        jump scene_josie_sex_desk.switch

    josephine "AKU CUMMING!!"

    anon "Saya juga!"

    pause
    call scene_josie_sex.cum ('office', _return)
    if _return == 'inside':
        josephine "Ya Tuhan, itu luar biasa!"

        anon "Ya, benar."

        josephine "Hehe, aku datang dengan susah payah..."

    else:
        josephine "Wow, kamu membuatku basah kuyup!"

        anon "Ya, maaf soal itu."

        josephine "Hehe, tidak, panas!"

    pause
    josephine "Bantu aku berdiri."


    if _return == 'inside':
        call call_pregnancy_minigame (None, M_josie)
    return


label scene_josie_sex.replay:
    $ renpy.dynamic(variants=persistent.cookie_jar['josie']['variants']['02_unlocked'])

    if len(variants) > 1:
        scene expression background(l=L_dealership) with fade
        menu:
            "Pagi" if 'morning' in variants:
                jump scene_josie_sex.morning

            "Sore" if 'afternoon' in variants:
                jump scene_josie_sex.afternoon
    else:

        jump expression 'scene_josie_sex.{}'.format(next(iter(variants)))

    return


screen scene_josie_sex_controls():
    style_prefix 'sex'

    vbox:

        frame:
            has hbox
            textbutton _('Keep Going') action Return(False)
            textbutton _('Cum Inside') action Return('inside')
            textbutton _('Cum Outside') action Return('outside')

            if renpy.showing('location_dealership_office_sex'):
                textbutton _('Switch') action Return('switch')

        frame:
            has hbox
            textbutton _('« Slower'):
                action (Function(M_josie.set,
                                 'sex speed',
                                 M_josie.get('sex speed') + 0.03),
                        Return(False))
                sensitive M_josie.get('sex speed') < .12
            textbutton _('Faster »'):
                action (Function(M_josie.set,
                                 'sex speed',
                                 M_josie.get('sex speed') - 0.03),
                        Return(False))
                sensitive M_josie.get('sex speed') > .061
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
