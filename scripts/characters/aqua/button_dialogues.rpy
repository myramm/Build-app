label aqua_dialogue_night:
    show player 10 with dissolve
    player_name "Sudah larut..."

    player_name "Aku harus mencari jalan keluar dari gua bawah air ini sebelum hari menjadi terlalu gelap."

    hide player with dissolve
    return

label aqua_dialogue_aqua_found:
    show aqua 2 zorder 1 at Position(xpos=.5875, ypos=1.0) with dissolve
    pause
    show player 16 zorder 2 at Position(xpos=.125, ypos=1.0) with dissolve
    show aqua 1
    aqua "( !!! )" with hpunch
    aqua "Anda!!"

    show player 15
    show aqua 2
    player_name "Itu benar, aku!"

    player_name "Kamu bilang aku harus datang mengambilnya dan inilah aku!"

    player_name "Sekarang kembalikan padaku yang mengkilat itu!"

    show player 16
    show aqua 1
    aqua "Hahahaha, kamu manusia yang lucu!"

    aqua "Kamu datang jauh..."

    aqua "... Kamu harus menjadi perenang yang baik, seperti {b}Aqua{/b}."

    show player 24
    show aqua 2
    player_name "{i}*Batuk*{/i} Ya, menurutku..."

    show player 30
    player_name "Lagipula tempat apa ini?"

    show player 16
    show aqua 1
    aqua "Ini sarang {b}Aqua{/b}!"

    show player 12
    show aqua 2
    player_name "Anda tinggal di sini?"

    show player 11
    show aqua 1
    aqua "Ya."

    show player 10
    show aqua 2
    player_name "Sendirian?"

    show player 11
    show aqua 4
    aqua "Ya."

    show player 10
    show aqua 3
    player_name "Apakah ada lebih banyak dari Anda?"

    show player 11
    show aqua 4
    aqua "Lebih... tentang aku?"

    show player 10
    show aqua 3
    player_name "Tahukah kamu, sarang lain dengan... umm, Aquas?"

    show player 11
    show aqua 4
    aqua "Oooh, tidak."

    show aqua 5
    aqua "Yang lain sudah lama pergi..."

    aqua "... Mereka meninggalkan {b}Aqua{/b}."

    show player 10
    show aqua 3
    player_name "Ah, kedengarannya sepi."

    show player 5
    show aqua 1
    aqua "Mmm, ya... Kadang-kadang..."

    aqua "... Tapi amis, tetaplah menemani {b}Aqua{/b}!"

    show aqua 2b
    aqua "Fishiesss kamu sssteals dengan ssshiny kamu!"

    show player 15
    show aqua 1b
    player_name "Sudah kubilang itu bukan aku!"

    player_name "Itu milik {b}KAPTEN Terry{/b}."

    show player 16
    show aqua 4
    aqua "{b}Caplan Terry{/b}?"

    show aqua 5
    pause
    show aqua 4
    aqua "Hmm, mungkin Anda mengatakan yang sebenarnya..."

    show player 12
    show aqua 3
    player_name "Saya mengatakan yang sebenarnya, {b}Aqua{/b}."

    show player 16
    show aqua 2b
    aqua "Lalu, apa yang {b}Aqua{/b} lakukan?"

    aqua "{b}Caplan Terry{/b} ssstealsss mencurigakan!"

    show aqua 4
    aqua "Jika semua ikan hilang, dengan siapa {b}Aqua{/b} berbicara?"

    show player 11
    show aqua 5
    aqua "{b}Aqua{/b} menjadi gila dan tidak pernah menemukan pasangan!"

    show player 10
    show aqua 3
    player_name "Pasangan?"

    show player 11
    show aqua 4
    aqua "Yesss, {b}Aqua{/b} nunggu sobat bantu buat babyss."

    show player 10
    show aqua 5
    player_name "Benar-benar?"

    player_name "Sudah berapa lama kamu menunggu?"

    show aqua 4
    show player 11
    aqua "Lama sekali... tapi tak seorang pun datang..."

    aqua "... Tidak ada yang menemukan {b}Aqua{/b}."

    show player 10
    show aqua 5
    player_name "Yah, aku menemukanmu."

    show player 13
    show aqua 1
    aqua "Ya, kamu menemukan {b}Aqua{/b}!"

    show aqua 2
    aqua "Dan jika Anda berbicara benar, mungkin kita berteman."

    show aqua 9
    aqua "Berjanjilah untuk tidak ssstealsss fishiesss dan {b}Aqua{/b} membuat Anda kembali berkilau."

    show player 14
    show aqua 8
    player_name "Ya!"

    player_name "Maksudku, terima kasih, {b}Aqua{/b}."

    show player 13
    show aqua 9
    aqua "Anda berjanji?"

    show player 14
    show aqua 8
    player_name "Saya berjanji, saya tidak akan mencuri \"ikan\"."

    show player 13
    show aqua 9
    aqua "Okeay."

    show aqua 10
    pause
    show aqua 2
    show player 471
    player_name "Fiuh, terima kasih {b}Aqua{/b}!"

    show player 470
    show aqua 1
    aqua "Ingat saja, jangan ssstealsss {b}Aqua{/b} ikan..."

    hide player
    hide aqua
    with dissolve
    call popup ('give', 'special_lure')
    return

label aqua_sex:
    $ game.timer.tick()
    if M_aqua.is_state(S_aqua_mate):
        call expression game.dialog_select("aqua_sex_pre_first")

    call expression game.dialog_select("aqua_sex_pre")
    if M_aqua.is_state(S_aqua_mate):
        label aqua_sex_replay:
            call expression game.dialog_select("aqua_sex_after_first")

    call expression game.dialog_select("aqua_sex_after")
    jump expression game.dialog_select("aqua_sex_loop")

label aqua_sex_pre_first:
    scene location_lair_mount
    show aqua 2 zorder 1 at Position(xpos=.5875, ypos=1.0)
    show player 2 zorder 2 at Position(xpos=.125, ypos=1.0)
    player_name "{b}Aqua{/b}, aku punya kabar baik!"

    show player 1
    show aqua 1
    aqua "{i}*Terkesiap*{/i} Anda belajar bernapas di bawah air, seperti {b}Aqua{/b}?!"

    show player 12
    show aqua 2
    player_name "Apa-"

    player_name "Tidak."

    show player 1
    show aqua 7
    aqua "Oh, oke."

    aqua "Apa kabarnya?"

    show player 2
    show aqua 6
    player_name "Saya meyakinkan {b}Kapten Terry{/b} untuk berhenti memancing!"

    show player 1
    show aqua 7
    aqua "Maksudmu mencurigakan sekali, aman?!"

    aqua "{b}Kapten Terry{/b} pergi?!"

    show player 17
    show aqua 6
    player_name "Hei, kamu mengatakannya dengan benar saat itu!"

    show player 1
    show aqua 7
    aqua "Hah?"

    show player 2
    show aqua 6
    player_name "Anda mengatakan \"{b}Kapten Terry{/b}\" dengan benar saat itu."

    show player 1
    show aqua 7
    aqua "Ya, {b}Caplan Terry{/b}!"

    show player 90
    show aqua 6
    player_name "..."
    show aqua 6b
    aqua "..."

    show player 37
    player_name "Hanya saja, sudahlah."

    show player 2
    player_name "Ikan Anda akan aman mulai sekarang."

    show player 1
    show aqua 7
    aqua "Oh, ini kabar baik!"

    show aqua 14
    aqua "Kamu manusia yang baik!"

    aqua "Manusia yang kuat!"

    show player 29
    show aqua 13
    player_name "Sama-sama, {b}Aqua{/b}..."

    show player 1
    show aqua 11
    aqua "..."
    show aqua 12
    aqua "Jadi, manusia siap kawin dengan {b}Aqua{/b}?"

    show player 21
    show aqua 13
    player_name "B-sekarang?"

    show player 297
    show aqua 14
    aqua "Iya, {b}Aqua{/b} capek menunggu."

    aqua "Teman bawa dia dengan kuat ke dalam air!"

    show player 10
    show aqua 13
    player_name "Di dalam air?"

    show player 11
    show aqua 14
    aqua "Ya, ayo."

    return

label aqua_sex_pre:
    scene location_lair_cutscene
    show text _ ("{b}Aqua{/b}'s touch was soft and gentle as she took my hand and started towards the luminescent pool.") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("I struggled to keep pace, fumbling with my clothes.") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("But she didn't seem to notice, her excitement palpable as she lead her new mate into the water.") as caption with dissolve
    pause
    return

label aqua_sex_after_first:
    scene location_lair_water
    show aswim 1 at left
    show pswim 1 at right
    with fade
    pause
    show aswim 2
    aqua "Ooh, sobat memiliki tubuh yang bagus."

    show aswim 1
    show pswim 2
    player_name "Terima kasih, {b}Aqua{/b}..."

    show aswim 3
    show pswim 1
    pause
    show aswim 2
    aqua "Belutmu sedang tidur."

    show aswim 1
    show pswim 2
    player_name "Hah?"

    show aswim 3
    pause
    show pswim 3
    pause
    show pswim 2
    player_name "Oh ya."

    show aswim 2
    show pswim 1
    aqua "Apakah sobat menyukai tubuh {b}Aqua{/b}?"

    show aswim 1
    show pswim 2
    player_name "Ya... {i}*Gulp*{/i} Umm, \"mate\" sangat menyukai tubuh {b}Aqua{/b}."

    show aswim 2
    show pswim 1
    aqua "Bagus, tubuh {b}Aqua{/b} milikmu sekarang."

    aqua "Belut Anda dapat bermain di dalam {b}Aqua{/b} kapan pun ia mau."

    show aswim 3
    pause
    show aswim 2
    aqua "Di dalam hangat {b}Aqua{/b}..."

    show aswim 3
    pause
    show aswim 2
    aqua "... Dan sssoft..."

    show aswim 3
    pause
    show aswim 2
    aqua "... Dan basah."

    show pswim 3
    pause
    show aswim 3
    show pswim 4
    pause
    show aswim 4
    show pswim 5
    pause
    show pswim 9
    pause
    show aswim 2
    show pswim 6
    aqua "Ooh, belut sukass ini ya?"

    show aswim 3
    show pswim 7
    player_name "Y-ya."

    show aswim 4
    aqua "Mmm, {b}Aqua{/b} menginginkannya."

    show aswim 3
    show pswim 8
    player_name "..."
    show aswim 4
    aqua "{b}Aqua{/b} menginginkannya sekarang!"

    hide pswim
    show aswim 5
    with dissolve
    pause
    show aswim 6 at right with dissolve
    player_name "{i}*Meneguk*{/i}"

    aqua "Aaah, yessss... Ayo belut, kamu main di dalam {b}Aqua{/b} sekarang."

    aqua "Berikan {b}Aqua{/b} ssstrong babyss..."

    player_name "Wah!"

    aqua "Hmm!"

    return

label aqua_sex_after:
    scene location_lair_watersex
    show aquas 1 at Position(xalign = 1.0, yalign = 1.0)
    with fade
    aqua "{b}Aqua{/b} membutuhkannya di dalam dirinya!"

    aqua "Cepatlah kawanku!"

    player_name "..."
    show aquas 2 with dissolve
    aqua "Desis."

    aqua "Belutmu sangat besar!"

    aqua "Bawa aku kuat-kuat!"

    $ M_aqua.set("sex speed", .175)
    show expression AnimatedImage("aquas", [3,4,5,6,7], M_aqua) as aquas with dissolve
    aqua "Ooohh!"

    pause
    aqua "Sangat kuat!"

    pause
    aqua "Dan dalam!"

    $ M_aqua.set("sex speed", .125)
    aqua "Aaahh!"

    pause
    aqua "Hmm, temanku."

    aqua "Lebih cepat!"

    $ M_aqua.set("sex speed", .075)
    pause
    return

label aqua_sex_loop:
    show screen sex_anim_buttons 
    pause
    hide screen sex_anim_buttons 
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("aquas", [3,4,5,6,7], M_aqua) as aquas
                $ animated = True
            pause 5
            call expression game.dialog_select("aqua_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [3,4,5,6,7]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "aquas {}".format(pose_list[pose_counter]) as aquas
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("aqua_hscene_dialog")
        $ animcounter += 1
    call screen aqua_sex_options

label aqua_hscene_dialog:
    if animcounter == 1:
        aqua "Ahhhh!!!{p=1}{nw}"


    elif animcounter == 3:
        aqua "Bawa aku!!!{p=1}{nw}"

        player_name "Uhhh...{p=1}{nw}"

    return

label aqua_sex_cum:
    call expression game.dialog_select("aqua_sex_cum_pre")
    if not store._in_replay == None or M_aqua.is_state(S_aqua_mate):
        call expression game.dialog_select("aqua_sex_cum_first")
    scene black with dissolve

    $ renpy.end_replay()
    $ persistent.cookie_jar["Aqua"]["unlocked"] = True
    $ persistent.cookie_jar["Aqua"]["gallery"]["01_unlocked"] = True
    $ M_aqua.trigger(T_aqua_mated)
    $ player.go_to(L_map)
    $ game.main()

label aqua_sex_cum_pre:
    player_name "Ini sulit dipercaya!"

    player_name "{b}Aqua{/b}, aku akan..."

    aqua "Yesss... YA TEMAN SAYA!"

    aqua "Berikan {b}Aqua{/b} salammu!"

    aqua "HISSSSS!!!"

    show aquas 8 with flash
    player_name "UHHH!!"

    aqua "AAAAHHH!!!!"

    pause
    show aquas 9
    player_name "Wah!"

    player_name "Itu luar biasa!"

    aqua "Ya..."

    aqua "... {b}Aqua{/b} bisa merasakan benih yang kuat berenang di dalam dirinya!"

    pause
    return

label aqua_sex_cum_first:
    scene location_lair_mount
    show aqua 11 zorder 1 at Position(xpos=.5875, ypos=1.0)
    show player 2 zorder 2 at Position(xpos=.125, ypos=1.0)
    with fade
    player_name "Jadi kamu menikmatinya?"

    show player 1
    show aqua 12
    aqua "Ya, {b}Aqua{/b} sangat menikmati..."

    aqua "... Terasa seperti ssseafoam seluruhnya."

    show player 2
    show aqua 11
    player_name "Anda luar biasa, saya belum pernah merasakan hal seperti itu sebelumnya."

    show player 1
    show aqua 14
    aqua "Iya, ini {b}Aqua{/b} pertama kalinya juga..."

    show aqua 12
    aqua "... Tapi Mate harus meminum {b}Aqua{/b} berkali-kali!"

    show aqua 14
    aqua "Diperlukan lebih banyak ssseeed, ya?"

    show player 2
    show aqua 13
    player_name "Tentu saja, saya akan segera kembali lagi!"

    show player 1
    show aqua 14
    aqua "Janji kawan?"

    show player 2
    show aqua 13
    player_name "Oh, aku berjanji!"

    show player 1
    show aqua 12
    aqua "Bagus."

    aqua "{b}Aqua{/b} ingin lebih banyak lagi!"

    show aqua 14
    aqua "Kembalilah secepatnya, manusia."

    show aqua 11
    aqua "{b}Aqua{/b} tunggu disini sampai ssseafoam ssberhenti menari..."

    return

label aqua_dialogue_pre:
    show aqua 2 zorder 1 at Position(xpos=.5875, ypos=1.0) with dissolve
    show player 36 zorder 2 at Position(xpos=.125, ypos=1.0) with dissolve
    player_name "Hai, {b}Aqua{/b}!"

    show player 1
    show aqua 1
    aqua "Iya?"

    show player 2
    show aqua 2
    player_name "Saya ingin berbicara dengan Anda."

    show player 1
    show aqua 4
    aqua "Apa yang diinginkan anak manusia?"

    return

label aqua_dialogue_the_others:
    show aqua 3 zorder 1 at Position(xpos=.5875, ypos=1.0)
    show player 10 zorder 2 at Position(xpos=.125, ypos=1.0)
    player_name "{b}Aqua{/b}, apa yang terjadi dengan kaummu yang lain?"

    show player 11
    show aqua 4
    aqua "Hmm, {b}Aqua{/b} tidak yakin..."

    aqua "... Mungkin mereka tidak suka {b}Aqua{/b}..."

    aqua "... atau mungkin mereka lupa?"

    show aqua 5
    show player 10
    player_name "Aduh, maafkan aku {b}Aqua{/b}."

    show player 11
    show aqua 1
    aqua "Anda bertanya lebih banyak pertanyaan?"

    show aqua 2
    return

label aqua_dialogue_how_are_you:
    show aqua 3 zorder 1 at Position(xpos=.5875, ypos=1.0)
    show player 2 zorder 2 at Position(xpos=.125, ypos=1.0)
    player_name "{b}Aqua{/b}, apa kabar?"

    show player 1
    show aqua 4
    aqua "Hmm?"

    show player 2
    show aqua 3
    player_name "Bagaimana perasaanmu?"

    show player 1
    show aqua 5
    aqua "Hmm, {b}Aqua{/b} sepi, dengan sedikit ikan..."

    show aqua 4
    aqua "... Tapi sukass ketika anak manusia datang berkunjung."

    show player 2
    show aqua 3
    player_name "Aku juga suka ngobrol denganmu, {b}Aqua{/b}."

    show player 1
    show aqua 1
    aqua "Ya, seperti berbicara."

    aqua "Anda bertanya lebih banyak pertanyaan?"

    show aqua 2
    return

label aqua_dialogue_mating_pre:
    show aqua 3 zorder 1 at Position(xpos=.5875, ypos=1.0)
    show player 10 zorder 2 at Position(xpos=.125, ypos=1.0)
    player_name "{b}Aqua{/b}, jodoh seperti apa yang kamu cari?"

    show player 11
    show aqua 4
    aqua "Pria."

    aqua "Ssorang kuat, itu memberi {b}Aqua{/b} ssstrong babyss."

    show aqua 1
    aqua "Anda tahu pria seperti ini?"

    show player 34
    show aqua 3
    player_name "Hmm."

    return

label aqua_dialogue_mating_stat_fail:
    show aqua 3 zorder 1 at Position(xpos=.5875, ypos=1.0)
    show player 29 zorder 2 at Position(xpos=.125, ypos=1.0)
    player_name "Bagaimana dengan saya?"

    show player 3
    show aqua 4
    aqua "Kamu pria yang kuat?"

    show player 29
    show aqua 3
    player_name "Ya?"

    show player 3
    show aqua 5
    aqua "..."
    aqua "Hmm..."

    pause
    show aqua 4
    aqua "... {b}Aqua{/b} berpikir... Tidak."

    aqua "Ini adalah ide yang buruk."

    show player 24
    show aqua 3
    player_name "Ah, kawan."

    return

label aqua_dialogue_mating_stat_pass:
    show aqua 3 zorder 1 at Position(xpos=.5875, ypos=1.0)
    show player 2 zorder 2 at Position(xpos=.125, ypos=1.0)
    player_name "Mungkin saya bisa membantu?"

    show player 1
    show aqua 7
    aqua "Anda?"

    show player 2
    show aqua 6
    player_name "Maksudku, aku berenang jauh ke sini untuk mencarimu."

    show player 1
    show aqua 7
    aqua "Anda melakukannya."

    show player 2
    show aqua 6
    player_name "... Dan aku melawan cumi-cumi yang sangat kejam di sepanjang jalan."

    show player 1
    show aqua 7 with hpunch
    aqua "Kamu melawan Inky?!"

    show player 2
    show aqua 6
    player_name "bertinta?"

    player_name "Ya, saya melawan Inky."

    show aqua 7
    aqua "Oooh, Inky kuat sekali!"

    show aqua 12
    pause
    show aqua 11
    aqua "Mungkin Anda memberi {b}Aqua{/b} ssstrong babyss."

    show player 14
    show aqua 13
    player_name "Benar-benar?!"

    show player 1
    show aqua 14
    aqua "Iya, tapi belum ada sobat!"

    aqua "Pertama Anda membuktikan kekuatan."

    show player 10
    show aqua 13
    player_name "Buktikan kekuatanku?"

    player_name "Bagaimana saya bisa melakukan itu?"

    show player 1
    show aqua 7
    aqua "Kamu bilang {b}Caplan Terry{/b} ssstealsss mencurigakan, ya?"

    show player 12
    show aqua 6
    player_name "{b}KAPTEN Terry{/b}."

    player_name "Ya, dialah orang yang sedang memancing di dermaga."

    show player 11
    show aqua 7
    aqua "Hmm, kamu membuat {b}Caplan Terry{/b} pergi!"

    show aqua 11
    aqua "Anda melakukan ini dan kemudian Anda kawin dengan {b}Aqua{/b}."

    show player 10
    show aqua 13
    player_name "Yah, kurasa aku bisa mencobanya."

    show player 11
    show aqua 14
    aqua "Bagus, pergilah."

    aqua "Selamatkan ikan!"

    return

label aqua_dialogue_mating_hint:
    show aqua 3 zorder 1 at Position(xpos=.5875, ypos=1.0)
    show player 12 zorder 2 at Position(xpos=.125, ypos=1.0)
    player_name "Apa yang perlu saya lakukan lagi, {b}Aqua{/b}?"

    player_name "Untuk membuktikan kekuatanku?"

    show player 11
    show aqua 7
    aqua "Singkirkan {b}Caplan Terry{/b}!"

    aqua "Selamatkan ikan!"

    show player 10
    show aqua 6
    player_name "Oh iya... {b}KAPTEN Terry{/b}."

    show player 11
    show aqua 7
    aqua "Itulah yang {b}Aqua{/b} katakan... {b}Caplan Terry{/b}!"

    show player 12
    show aqua 6
    player_name "KAPTEN-"

    player_name "{i}*Huh*{/i} Sudahlah."

    player_name "Kurasa, aku akan mencoba dan berbicara dengannya."

    show player 5
    show aqua 7
    aqua "Ya, suruh dia tinggalkan fishiesss sendirian!"

    return

label aqua_dialogue_mate:
    show aqua 2 zorder 1 at Position(xpos=.5875, ypos=1.0)
    show player 21 zorder 2 at Position(xpos=.125, ypos=1.0)
    player_name "Saya pikir mungkin Anda ingin... masuk ke dalam air lagi?"

    show player 26
    show aqua 3
    aqua "..."
    show aqua 1
    aqua "Oh, kamu ingin membuat babyss?"

    show player 21
    show aqua 12
    player_name "Aku, er... ya?"

    show player 26
    show aqua 11
    aqua "Hahaha, kamu manusia yang lucu."

    aqua "Kalian {b}Aqua{/b} sobat sekarang..."

    show aqua 14
    aqua "... {b}Aqua{/b} selalu siap untuk mendapatkan lebih banyak ssseed!"

    aqua "Jika sobat menginginkan {b}Aqua{/b}, dia harus membawanya..."

    aqua "... Sangat kuat di dalam air adalah yang terbaik tetapi sobat harus memilih!"

    return

label aqua_dialogue_nothing:
    show aqua 3 zorder 1 at Position(xpos=.5875, ypos=1.0)
    show player 36 zorder 2 at Position(xpos=.125, ypos=1.0)
    player_name "Tidak ada, aku hanya menyapa!"

    show player 1
    show aqua 4
    aqua "Bocah manusia isss... lucu..."

    show aqua 1
    aqua "... Aku suka anak manusia..."

    show player 21
    show aqua 2
    player_name "Aku salah... menyukaimu juga, {b}Aqua{/b}."

    show player 13
    aqua "..."
    show player 29
    player_name "Bagaimanapun, aku harus segera pergi."

    show player 3
    show aqua 1
    aqua "Ssst, segera?"

    aqua "Anda kembali besok?"

    show player 17
    show aqua 2
    player_name "Anda yakin!"

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
