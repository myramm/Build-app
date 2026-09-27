label jenny_dining_room_sex_intro:
    show anon f_worried
    show jenny f_grin
    jenny "Ssst!!"

    show anon f_surprised_teeth_down with None
    show debbie b_breakfast_mug f_normal
    with dissolve
    debbie "Apakah kamu mengatakan sesuatu, sayang?"

    jenny "Maukah kamu membuatkanku sarapan?"

    show anon f_shy_down
    debbie "Kamu ingin aku memasak untukmu?"

    jenny "Ya."

    debbie "Tentu saja aku akan melakukannya, sayang!"

    debbie "Saya selalu khawatir tentang Anda tidak mendapatkan cukup makanan-"

    show debbie f_sad
    show jenny f_eyeroll
    jenny "Ya, aku tahu {b}[deb_name]{/b}... Kamu selalu memberitahuku!"

    show jenny f_upset
    debbie "B-benar... Umm..."

    show anon f_looking_down_eating a_eating with dissolve
    debbie f_normal "Aku akan menyiapkan telur dan bacon untukmu sekarang!"

    show anon f_looking_down_food a_resting with dissolve
    show jenny f_grin
    jenny "Terima kasih."

    debbie "Ini hanya beberapa menit saja, sayang."

    show anon f_surprised_high_food with None
    show expression "characters/xtra/overlay_o_dinner_mug.png"
    hide debbie
    with dissolve
    show jenny f_laugh a_laugh with dissolve
    jenny "hehe..."

    show jenny b_breakfast_gettingup f_grin_down with dissolve
    pause
    show jenny b_breakfast_remove with dissolve
    if M_jenny.get("first_sex_dining"):
        $ M_jenny.set("first_sex_dining", False)
        show anon f_worried_high
        anon "Oke, jadi sekarang apa-"

        show jenny b_breakfast_leaning f_grin with dissolve
        show anon f_surprised_teeth_left
        anon "!!!"
        if M_jenny.get("dominance") <= 0:
            anon f_worried "K-kita tidak bisa-"

            show jenny f_upset
            jenny "{i}*Sigh*{/i} Ya, tidak jika Anda akan menjadi sedikit menyebalkan tentang hal itu..."

            show jenny b_breakfast_remove with dissolve
            pause
            show jenny b_breakfast_gettingup with dissolve
            jenny "... Dan di sini saya pikir Anda akhirnya mulai menumbuhkan tulang punggung."

            anon "Bagus!"

            show jenny b_breakfast_remove with dissolve
            anon "Ayo cepat, oke?"

            show jenny b_breakfast_leaning f_grin with dissolve
            jenny "Ya, ya... Keluarkan penismu!"

        else:
            anon f_worried "Apakah kamu sudah gila?!"

            show jenny b_breakfast_standing_panties_down a_hips f_sexy_down with dissolve
            jenny "Ayolah, {b}[firstname]{/b}... Anda pasti menginginkannya."

            anon "{i}*Huh*{/i} Baik."

            jenny "Sebaiknya kau cepat, kita hanya punya waktu beberapa menit..."

            anon "Diam saja dan kembali ke sana!"

            show jenny b_breakfast_leaning f_laugh with dissolve
            jenny "Hehehe!"

            show jenny f_grin
    else:
        anon f_worried "Kenapa kita tidak naik saja ke atas?!"

        show jenny f_grin b_breakfast_leaning with dissolve
        jenny "Diam saja dan persetan denganku, {b}[firstname]{/b}!"

        anon f_tired "{i}*Huh*{/i}"

        scene black with fade
        pause

label jenny_dining_room_sex_pre_insert:
    scene expression "backgrounds/location_home_diningroom_sex.jpg"
    show jenny_sex_table b_default f_back
    show player_jenny_diningroom_sex pre
    with fade
    anon "Hanya saja, jangan terlalu keras..."

    show jenny_sex_table f_back_talk
    jenny "Oh, tolong... Aku cukup yakin aku bisa mengendalikan-"

    hide jenny_sex_table
    hide player_jenny_diningroom_sex
    show jenny_diningroom_sex insert
    with dissolve
    pause 1
    show jenny_diningroom_sex 1
    jenny "SELF!!!" with hpunch
    $ animated = True
    $ anim_toggle = True
    $ M_jenny.set('sex speed', .12)
    show expression AnimatedImage("jenny_diningroom_sex", [1,2,3,4,5,6,7,8,9], M_jenny) as jenny_diningroom_sex at Position(xalign = 0.0, yoffset = 0) with dissolve
    jenny "Oh, sial!"

    anon "Ssst!!!"

    jenny "Ngghhh!"

    pause
    jenny "Suci-"

    jenny "!!!"
    anon "Kamu harus diam atau aku akan berhenti!"

    jenny "Jangan berani-berani berhenti!"

    pause
    anon "Kamu meremasku terlalu erat!"

    jenny "Aku tidak bisa menahannya, ini benar-benar membuatku bergairah!"

    pause
    debbie "{b}[jen_name]{/b}?!"

    hide jenny_diningroom_sex
    show jenny_sex_table b_default f_surprised
    show player_jenny_diningroom_sex pre
    with dissolve
    anon "!!!" with hpunch
    jenny "!!!"
    show jenny_sex_table f_angry_talk
    jenny "Y-ya?"

    show jenny_sex_table f_angry
    debbie "Apakah Anda ingin telur Anda diorak-arik atau terlalu mudah?"

    show jenny_sex_table f_angry_talk
    jenny "Oh, umm... Orak-arik oke!"

    hide jenny_sex_table
    hide player_jenny_diningroom_sex
    show expression AnimatedImage("jenny_diningroom_sex", [1,2,3,4,5,6,7,8,9], M_jenny) as jenny_diningroom_sex at Position(xalign = 0.0, yoffset = 0) with hpunch
    debbie "Baiklah, sayang."

    jenny "Buruan, {b}[firstname]{/b}!"

    pause
    anon "Aku semakin dekat."

    jenny "Saya juga!"


label jenny_diningroom_sex_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("jenny_diningroom_sex", [1,2,3,4,5,6,7,8,9], M_jenny) as jenny_diningroom_sex at Position(xalign = 0.0, yoffset = 0)
                $ animated = True
            pause 5
            call expression game.dialog_select("jenny_diningroom_sex_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8,9]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "jenny_diningroom_sex {}".format(pose_list[pose_counter]) as jenny_diningroom_sex at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("jenny_diningroom_sex_hscene_dialog")
        $ animcounter += 1
    call screen jenny_diningroom_sex_options

label jenny_diningroom_sex_hscene_dialog:
    if animcounter == 0 and randomizer() < 10:
        jenny "Ahh!!{p=1}{nw}"

    if animcounter == 1 and randomizer() < 10:
        jenny "Enak sekali!{p=1}{nw}"

    if animcounter == 2 and randomizer() < 10:
        jenny "FUUUUUCK!!!{p=1}{nw}"

    if animcounter == 3 and randomizer() < 10:
        anon "Uhh!{p=1}{nw}"

    return

label jenny_diningroom_sex_cum_inside:
    anon "Ini dia!"

    jenny "Jangan berhenti!!"

    show jenny_diningroom_sex cum
    anon "HNNGGG!!!" with flash
    show jenny_diningroom_sex cum2
    show xray_jenny_diningroom_table:
        align (0,0)
    jenny "NGGHHH!!!"

    hide xray_jenny_diningroom_table
    pause
    show jenny_diningroom_sex 1 with dissolve
    anon "Haah... Haah..."

    jenny "Astaga..."

    anon "Ya..."

    jenny "Lepaskan aku."

    hide jenny_diningroom_sex
    show jenny_sex_table b_default f_angry
    show player_jenny_diningroom_sex after
    with dissolve
    pause
    call call_pregnancy_minigame ("jenny_diningroom_sex_cum_inside_post_pregnancy", M_jenny)

label jenny_diningroom_sex_cum_inside_post_pregnancy:
    scene expression game.timer.image("dining_room{}")
    show jenny b_breakfast_standing_panties_down a_cum2 f_upset_down zorder 1
    show anon b_dinner_sitting_look_left f_shy_down zorder 0
    show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
    show expression "characters/xtra/overlay_o_dinner_mug.png" zorder 2
    with fade
    jenny "Sialan, {b}[firstname]{/b}!"

    jenny "Jika aku hamil aku akan membunuhmu!"

    show jenny a_cum1 with dissolve
    show anon f_flirt_left
    anon "Kamu menyuruhku untuk tidak berhenti..."

    show jenny f_gross_down
    jenny "Ya, tapi aku tidak menyuruhmu untuk masuk ke dalam diriku, kan?"

    anon @ -m_talk "..."
    jenny "Dasar bodoh..."

    anon f_worried "Diam!"

    debbie "Oke, siapa yang lapar?!"

    show anon f_surprised
    show jenny f_surprised
    jenny "!!!" with hpunch
    show jenny b_breakfast_remove with dissolve
    pause
    show jenny b_breakfast_dressed a_spoon f_upset_down with dissolve
    show anon f_normal_high with None
    show debbie b_breakfast_potatoes f_normal zorder 1
    with dissolve
    debbie "Dua butir telur orak-arik dan tiga potong bacon, sesuai keinginan Anda."

    show jenny f_normal
    jenny "T-terima kasih, {b}[deb_name]{/b}."

    show anon f_shy_down
    debbie "Sama-sama sayang!"

    hide expression "characters/xtra/overlay_o_dinner_mug.png"
    show debbie b_breakfast_sitting a_mug
    with dissolve
    pause
    debbie "{b}[firstname]{/b}, kamu terlihat lelah..."

    debbie "Apakah kamu baik-baik saja, sayang?"

    show anon f_surprised
    anon @ -m_talk "Hmm?"

    jenny "Dia baik-baik saja."

    anon b_dinner_sitting f_normal "Ya, aku merasa baik-baik saja."

    debbie "Baiklah, pastikan kamu cukup istirahat, oke?"

    anon "O-oke."

    show anon f_shy_down
    show debbie a_mug_drink f_kiss with dissolve
    pause
    show debbie f_sad a_mug with dissolve
    debbie "Mmm, apa baunya aneh di sini?"

    anon f_worried "T-tidak?"

    show debbie f_normal
    jenny "Saya tidak mencium bau apa pun."

    debbie "Hmm, ada yang berbau lucu..."

    show jenny f_laugh a_phone with dissolve
    anon "Y-ya, entahlah {b}[deb_name]{/b}..."

    jenny "Hehehe!"

    hide anon with dissolve
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["15_unlocked"] = True
    $ game.timer.tick()
    $ player.go_to(L_home_diningroom)
    $ game.main()

label jenny_diningroom_sex_cum_outside:
    anon "Ini dia!"

    jenny "Jangan berhenti!!"

    hide jenny_diningroom_sex
    show jenny_sex_table b_default f_angry
    show player_jenny_diningroom_sex after
    with dissolve
    pause
    scene expression game.timer.image("dining_room{}")
    show jenny b_breakfast_standing_panties_down a_hips f_gross_down zorder 1
    show anon b_dinner_standing_cumming f_surprised_teeth_down zorder 0
    show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
    with fade
    jenny "Apa-apaan ini, {b}[firstname]{/b}?!"

    show anon f_brag
    anon @ -m_talk "HNNGGG!!!" with flash
    jenny "Sudah kubilang jangan berhenti!"

    show anon f_surprised_teeth_down
    pause
    show anon b_dinner_sitting_look_left f_tired zorder 0
    show expression "characters/xtra/overlay_o_dinner_mug.png" zorder 2
    with dissolve
    anon "Haah... Haah..."

    anon f_worried "Apa yang kamu ingin aku lakukan, {b}[jen_name]{/b}?!"

    anon "Apa aku harus masuk ke dalam dirimu?!"

    show jenny b_breakfast_remove with dissolve
    pause
    show jenny b_breakfast_dressed a_spoon f_upset with dissolve
    jenny "T-tidak..."

    jenny "{i}*Sigh*{/i} Pasti menyenangkan untuk menyelesaikannya, brengsek!"

    anon "Diam!"

    debbie "Oke, siapa yang lapar?!"

    show anon f_surprised
    show jenny f_surprised
    jenny "!!!" with hpunch
    show anon f_normal_high with None
    show debbie b_breakfast_potatoes f_normal zorder 1
    with dissolve
    debbie "Dua butir telur orak-arik dan tiga potong bacon, sesuai keinginan Anda."

    show jenny f_normal
    jenny "T-terima kasih, {b}[deb_name]{/b}."

    show anon f_shy_down
    debbie "Sama-sama sayang!"

    hide expression "characters/xtra/overlay_o_dinner_mug.png"
    show debbie b_breakfast_sitting a_mug
    with dissolve
    pause
    debbie "{b}[firstname]{/b}, kamu terlihat lelah..."

    debbie "Apakah kamu baik-baik saja, sayang?"

    show anon f_surprised
    anon @ -m_talk "Hmm?"

    jenny "Dia baik-baik saja."

    anon b_dinner_sitting f_normal "Ya, aku merasa baik-baik saja."

    debbie "Baiklah, pastikan kamu cukup istirahat, oke?"

    anon "O-oke."

    show anon f_surprised
    show jenny f_surprised
    show debbie a_mug_drink f_kiss with dissolve
    anon "T-tunggu-"

    pause
    show jenny f_laugh
    show debbie f_gross a_mug with dissolve
    debbie "Eugh, kopi ini rasanya tidak enak!"

    anon f_worried "B-benarkah?"

    debbie "Ya!"

    jenny "{i}*Mendengus*{/i}"

    show jenny f_grin
    debbie "Saya tidak mengerti, rasanya enak beberapa menit yang lalu..."

    anon "A-aneh..."

    anon "Anda mungkin harus membuangnya dan membeli cangkir baru."

    debbie "Ya, menurutku juga begitu."

    debbie "sial!"

    show jenny f_laugh
    jenny "Hehehe!"

    hide anon with dissolve
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["15_unlocked"] = True
    $ game.timer.tick()
    $ player.go_to(L_home_diningroom)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
