label odette_1st_sex_bike:
    odette "Nah, haruskah kita melanjutkan dari bagian terakhir yang kita tinggalkan atau-"

    pause
    odette f_smirk @ f_surprised "{i}*Terkesiap*{/i} Oh, sempurna sekali!"

    anon f_confused @ -m_talk "..."
    odette "Aku akan mengajakmu jalan-jalan!"

    anon @ -m_talk "Hmm?"

    odette "Ikutlah denganku, kawan!"

    hide odette with dissolve
    anon f_worried "K-kamu ingin berhubungan seks di sepeda motor {b}Grace{/b}?"

    odette "Hehehe!"

    odette "Ayo, ini akan menyenangkan!"


    scene expression "backgrounds/location_tattoo_garage_sex.jpg" with None
    show odette b_bike_base
    show odette_sex_bike_base_mc
    show odette_sex_arms_bike_base_mc a_pre
    with dissolve
    pause
    odette "Jangan malu, kemarilah."

    anon "O-oke."

    show odette_sex_arms_bike_base_mc a_insert with dissolve
    odette "Sialan, itu bahkan lebih besar dari yang kukira!"

    jump odette_sex_intro

label odette_repeat_sex_bike:
    if _in_replay:
        $ player.go_to(L_tattooparlor_garage)
        scene expression player.location.background_closeup
    anon "Bersiaplah!"

    odette "Mm, saya berharap Anda akan mengatakan itu!"

    label odette_repeat_sex_bike.segue:
    show anon f_flirt_low
    show odette b_panties_remove
    with dissolve
    pause
    show odette b_drop1 with dissolve
    pause
    show odette b_drop2 with dissolve
    show odette b_topless
    with dissolve
    odette "Ikuti aku, kawan!"

    show anon a_behind_head f_shy
    hide odette
    with {'master': dissolve}
    anon "O-oke."

    scene location_tattoo_garage_sex
    show odette b_bike_base
    show odette_sex_bike_base_mc
    show odette_sex_arms_bike_base_mc a_pre
    with fade
    pause
    odette "Cepat {b}[firstname]{/b}, saya sangat membutuhkannya!"

    anon "Itu akan datang."

    show odette_sex_arms_bike_base_mc a_insert with dissolve
    odette "Itu saja, berikan padaku."

    jump odette_sex_intro

label odette_sex_intro:
    hide odette b_bike_base
    hide odette_sex_bike_base_mc
    hide odette_sex_arms_bike_base_mc
    $ anim_toggle = True
    $ animated = True
    $ M_odette.set('sex speed', .09)
    show expression AnimatedImage("odette_sex_bike", [1,2,3,4,5,6,7,8,9,10], M_odette) as odette_sex_bike at Position(xalign = 0.0, yoffset = 0)
    odette "!!!"
    if M_odette.get("bike_1st_time"):
        odette "Oke, wah!"

        odette "Aku punya banyak penis tapi ini berada pada level yang berbeda!"

    else:
        odette "Mmm, sial ya!"

    pause
    odette "Ini sangat dalam!"

    odette "Ahhh!"

    pause
    odette "Ayo {b}[firstname]{/b}, persetan denganku lebih keras!"

    anon "Oke."

    $ M_odette.set('sex speed', .07)
    pause
    if M_odette.get("bike_1st_time"):
        odette "Saya tidak percaya {b}Evie{/b} melakukan hal ini secara rutin."

        odette "Dia adalah salah satu gadis yang beruntung!"

    else:
        odette "Mmm, aku sangat menyukai penis ini!"

        odette "Ahh!!"

    jump odette_sex_bike_loop

label odette_sex_bike_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("odette_sex_bike", [1,2,3,4,5,6,7,8,9,10], M_odette) as odette_sex_bike at Position(xalign = 0.0, yoffset = 0)
                $ animated = True
            pause 5
            call expression game.dialog_select("odette_sex_bike_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8,9,10]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "odette_sex_bike {}".format(pose_list[pose_counter]) as odette_sex_bike at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("odette_sex_bike_hscene_dialog")
        $ animcounter += 1
    call screen odette_sex_bike_options

label odette_sex_bike_hscene_dialog:
    if animcounter == 0 and randomizer() < 50:
        odette "Wah, hehehe!{p=1}{nw}"

    if animcounter == 1 and randomizer() > 50:
        anon "Ya Tuhan!{p=1}{nw}"

    if animcounter == 2 and randomizer() < 50:
        odette "Sial!{p=1}{nw}"

    if animcounter == 3 and randomizer() > 50:
        anon "Saya semakin dekat...{p=2}{nw}"

    return

label odette_sex_bike_cum_inside:
    odette "Mmm, aku akan mengotori penis besar itu!"

    anon "Aku juga semakin dekat!"

    pause
    odette "Jangan berhenti, {b}[firstname]{/b}!"

    anon "aku akan-"

    pause
    odette "Isi vaginaku sampai penuh!"

    anon "Ini dia!"

    pause
    hide odette_sex_bike
    show odette b_bike_cum
    anon "HNNGGG!!!" with flash
    show odette b_bike_cum2
    show xray_odette_bike:
        align (0,0)
    odette "NGGHHH!!!"

    hide xray_odette_bike
    pause
    show odette b_bike_base
    show odette_sex_bike_base_mc
    show odette_sex_arms_bike_base_mc a_after
    show odette_creampie
    with dissolve
    pause
    call call_pregnancy_minigame ("odette_sex_bike_end", M_odette)

label odette_sex_bike_cum_outside:
    odette "Mmm, aku akan mengotori penis besar itu!"

    anon "Aku juga semakin dekat!"

    pause
    odette "Jangan berhenti, {b}[firstname]{/b}!"

    anon "aku akan-"

    pause
    odette "Isi vaginaku sampai penuh!"

    anon "Ini dia!"

    anon "aku tidak bisa-"

    hide odette_sex_bike
    show odette b_bike_base
    show odette_sex_bike_base_mc
    show odette_sex_arms_bike_base_mc a_cumshot
    anon "HNNGGG!!!" with flash
    odette "NGGHHH!!!"

    pause
    show odette_sex_arms_bike_base_mc a_cumshot3
    with dissolve
    jump odette_sex_bike_end

label odette_sex_bike_end:
    anon "Haah... Haah..."

    odette "Sial, itu beban yang sangat besar {b}[firstname]{/b}!"

    anon "Y-ya, maaf..."

    odette "Hehehe!"

    scene expression background(l=L_tattooparlor_garage) as stage
    show anon
    show odette f_smirk b_topless
    with fade
    if M_odette.get("gotta_have_that_dick"):
        odette "Mmm, aku sangat membutuhkannya."

        pause
        odette "Anda merasa lebih baik sekarang?"

        anon "Ya, menurutku."

        odette @ f_laugh "Hehehe!"

        anon f_worried "Jadi ini benar-benar terjadi?"

        odette "Ya."

        odette "Sembilan bulan dari sekarang, kita akan memiliki mesin kotoran kecil!"

        anon @ -m_talk "..."
        odette "Aku harus kembali ke toko."

        anon "aku akan menjadi seorang ayah..."

        odette "Ya."

        odette @ f_laugh "Selamat!"

        hide odette with dissolve
        odette "Hehehe!"

        $ M_odette.set("gotta_have_that_dick", False)
        jump odette_pregnancy_have_baby_end
    elif M_odette.get("bike_1st_time"):
        odette @ f_confused "Apakah kamu membuat perjanjian dengan Setan atau semacamnya?"

        anon "Apa?!"

        anon "T-tidak?"

        odette "Kontol itu luar biasa, {b}[firstname]{/b}!"

        anon @ f_laugh "Hehe, terima kasih!"

        odette "Saya harus mendapatkan {b}Grace{/b} untuk mencobanya."

        anon @ a_wave f_brag_closed "Ya benar."

        anon "Bagaimana cara meyakinkan {b}Grace{/b} untuk berhubungan seks dengan pacar saudara perempuannya?"

        odette @ f_laugh "Oh, aku punya caraku sendiri..."

        odette "Serahkan padaku."

        anon @ -m_talk "..."
        odette "Sementara itu, fokus saja untuk membuat {b}Evie{/b} kecil bahagia, oke?"

        anon @ a_point "Saya bisa melakukan itu."

        pause
        odette "Oh, dan {b}[firstname]{/b}?!"

        anon @ -m_talk "Hmm?"

        odette "Anda memberi tahu saya kapan Anda ingin melakukan perjalanan lagi, ya?"

        odette "Kontol itu terlalu bagus untuk dilewatkan!"

        anon @ a_behind_head "O-oke."

        odette @ f_laugh "Hehehe!"

        $ M_odette.set("bike_1st_time", False)
    else:
        odette "Mm, aku sangat membutuhkannya..."

        anon "Ya?"

        odette "Jangan salah paham, {b}Grace{/b} bisa melakukan hal-hal menakjubkan dengan mulutnya, tapi tidak ada yang bisa menggantikan mulutnya, tahu?"

        anon "Ehh, ya... Oke."

        odette "Terkadang seorang gadis hanya butuh hubungan yang baik dan keras..."

        anon "Yah, aku dengan senang hati menurutinya."

        odette @ f_laugh "Hehehe!"

        anon "Sampai ketemu lagi nanti?"

        odette "Tentu saja."

        odette "Anda tahu di mana menemukan saya."

        anon @ a_wave "Sampai jumpa, {b}Odette{/b}."

        odette "Nanti, kawan."

        hide anon with dissolve
        odette "Berikan {b}Evie{/b} ciuman untukku!"

    $ renpy.end_replay()
    $ persistent.cookie_jar["Odette"]["unlocked"] = True
    $ persistent.cookie_jar["Odette"]["gallery"]["01_unlocked"] = True
    $ game.timer.tick()
    $ player.go_to(L_tattooparlor)
    $ game.main()

label odette_pregnancy_have_baby_end:
    anon @ -m_talk "( {b}Odette{/b} akan melahirkan anakku... )"

    anon f_sad_down @ -m_talk "( ... Dan aku tidak bisa memberitahu siapa pun bahwa akulah ayahnya. )"

    pause
    anon @ -m_talk "(Ya ampun, kenapa semuanya harus begitu rumit?)"

    hide anon with dissolve
    $ game.timer.tick()
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
