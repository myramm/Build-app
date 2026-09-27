label button_mrsj_greetings:
    show player 14 at left
    show mrsj 14 at right
    with dissolve
    player_name "Hai, {b}Ny. Johnson{/b}!"

    show player 1
    show mrsj 17
    mrsj "Hai, {b}[firstname]{/b}!"

    mrsj "Bagaimana kabarmu?"

    show player 14
    show mrsj 14
    player_name "Saya baik-baik saja, terima kasih!"

    show player 1
    show mrsj 17
    mrsj "Apakah ada yang bisa saya lakukan untuk Anda?"

    show mrsj 14
    return


label button_mrsj_sex_ed_intro:
    scene erik_upstairs_night_c
    show mrsj 42 at right
    show player 11 zorder 2 at left
    show old_erik 1f zorder 1 at Position(xpos=300)
    with dissolve
    mrsj "Hei, teman-teman..."

    show mrsj 41
    show player 21
    player_name "H-hai, {b}Ny. Johnson{/b}!"

    show player 13
    show old_erik 4f
    erik "Anda... Cantik sekali, {b}Ny. Johnson{/b}."

    show old_erik 1f
    show mrsj 40b with fastdissolve
    mrsj "Nah, apakah kamu hanya akan terus menatapku atau kamu ingin menanyakan sesuatu padaku?"

    show mrsj 39
    return

label button_mrsj_private_yoga_intro:
    scene erik_upstairs_night_c2
    show mrsj 54 at Position(xpos=734,ypos=650)
    show player 433 zorder 2 at left
    with dissolve
    mrsj "Halo, {b}[firstname]{/b}..."

    show mrsj 53
    player_name "!!!"
    show mrsj 54
    mrsj "Apakah ada yang salah?"

    show player 435
    show mrsj 53
    player_name "Anda... Anda telanjang, {b}Ny. Johnson{/b}."

    show player 434
    show mrsj 54
    mrsj "Saya ingin merasa... Nyaman di kamar saya..."

    mrsj "Bukankah kamu hendak menanyakan sesuatu padaku?"

    show mrsj 53
    return

label button_mrsj_erik_learn_fetch_prompt:
    show mrsj 14 at right
    show player 10 at left
    player_name "Bagaimana kami dapat membantu Anda bersiap untuk pendidikan seks kami lagi?"

    show player 5
    show mrsj 17
    mrsj "Saya memerlukan buku instruksional yang bagus, seperti {b}Kama Sutra{/b}."

    mrsj "Dan beberapa {b}pil KB{/b}!"

    show mrsj 49
    mrsj "Anda tidak akan pernah bisa terlalu berhati-hati..."

    show mrsj 50
    show player 14
    player_name "Baiklah."

    player_name "Aku akan mencoba dan menemukannya..."

    show player 5
    show mrsj 17
    mrsj "Ingatlah untuk membawanya bersamamu ke kamarku pada {b}malam hari{/b}."

    hide player
    hide mrsj
    with dissolve
    return

label button_mrsj_erik_got_gf:
    show player 14
    player_name "Sepertinya aku bisa memperkenalkan {b}Erik{/b} kepada seorang gadis di sekolah!"

    show player 1
    show mrsj 17
    mrsj "Benar-benar?!"

    show player 14
    show mrsj 14
    player_name "Ya!"

    player_name "Mereka punya banyak kesamaan, mereka akan cocok satu sama lain!"

    show mrsj 17
    show player 17
    player_name "Saya pikir ini pasti akan berhasil!"

    show player 1
    show mrsj 18
    mrsj "Itu luar biasa!!"

    show mrsj 17
    mrsj "Aku tidak percaya kamu begitu baik pada {b}Erik{/b}."

    show mrsj 49
    mrsj "Saya pikir sudah waktunya bagi saya untuk memberi Anda sedikit hadiah..."

    show player 21
    show mrsj 50
    player_name "A... Hadiah?"

    show player 11
    show mrsj 49
    mrsj "Bagaimana kalau saya memberi Anda beberapa... pelajaran yoga {i}pribadi{/i}..."

    mrsj "Jenis yang tidak bisa Anda lihat di gym."

    show mrsj 50
    show player 21
    player_name "Itu akan luar biasa, {b}Ny. Johnson{/b}!"

    show player 13
    show mrsj 49
    if game.timer.is_dark():
        mrsj "Kalau begitu mari kita mulai, oke?"


        scene erik_upstairs_night_c2
        show mrsj 54 at Position(xpos=734,ypos=650)
        show player 433 zorder 2 at left
        with fade
    else:
        mrsj "Datang saja mengunjungiku pada malam hari di kamarku... Pastikan kamu cukup istirahat!"

        show player 11
        mrsj "Ini bisa jadi... Cukup melelahkan."

        show player 21
        show mrsj 50
        player_name "Y-ya, {b}Ny. Johnson{/b}."

        show player 13
        show mrsj 49
        mrsj "Sampai jumpa lagi, aku akan menunggu!"

        hide player
        hide mrsj
        with dissolve
    return

label button_mrsj_erik_introduce_june:
    show player 14
    player_name "Ada gadis di sekolah yang menurutku disukai {b}Erik{/b}."

    show player 1
    show mrsj 17
    mrsj "Benar-benar?"

    show mrsj 18
    mrsj "Itu luar biasa!"

    show mrsj 17
    mrsj "Apakah kamu kenal dia? Seperti apa dia?!"

    show mrsj 14
    show player 14
    player_name "Tidak, aku belum berbicara dengannya."

    player_name "Dia dari kelas yang berbeda, menurutku."

    show mrsj 17
    show player 1
    mrsj "Oh, begitu."

    show player 11
    mrsj "Apakah {b}Erik{/b} berbicara dengannya?"

    show mrsj 14
    show player 10
    player_name "Menurutku tidak... Dia bilang dia terlalu pemalu."

    player_name "Saya mengatakan kepadanya bahwa saya akan mencari tahu lebih banyak tentang dia dan memberi tahu dia seperti apa dia."

    show mrsj 18
    show player 13
    mrsj "Kamu baik sekali!!"

    show mrsj 17
    mrsj "Dia sangat beruntung memilikimu sebagai teman..."

    show mrsj 14
    show player 14
    player_name "Oh, aku yakin dia akan melakukan hal yang sama padaku!"

    show mrsj 49
    show player 1
    mrsj "Begini saja, beri tahu saya bagaimana kelanjutannya..."

    show player 11
    mrsj "Jika kamu bisa menemukan {b}Erik{/b} pacar, ada hadiah spesial menantimu..."

    show mrsj 50
    player_name "..."
    show player 21
    player_name "Tentu, {b}Ny. Johnson{/b}!"

    show player 1
    show mrsj 14
    return

label button_mrsj_breastfeeding:
    show mrsj 38 at right
    show player 12 at left
    player_name "Jadi, sudah berapa lama... Menyusui {b}Erik{/b}?"

    show player 5
    show mrsj 52
    mrsj "Oh..."

    mrsj "Dengar, ini bukan apa yang mungkin kamu pikirkan."

    mrsj "Saya selalu mengasuhnya seperti ini."

    show mrsj 38
    show player 11
    mrsj "..."
    show mrsj 52
    mrsj "Kau tahu dia tidak mendapat banyak perhatian dari gadis-gadis di sekolah."

    mrsj "Aku merasa kasihan padanya!"

    mrsj "Saya hanya ingin {b}Erik{/b} merasakan dan melihat apa itu wanita!"

    show mrsj 20
    mrsj "Tapi mungkin aku... aku sudah berlebihan melakukannya?"

    show mrsj 19c
    show player 5
    player_name "..."
    show player 12
    player_name "Senang sekali Anda begitu peduli dan memberinya perhatian!"

    show mrsj 14
    show player 10
    player_name "Menurutku dia sangat beruntung..."

    show player 11
    show mrsj 18
    mrsj "Oh, haha!"

    show mrsj 17
    mrsj "Baiklah, terima kasih..."

    mrsj "Saya pikir pria muda yang baik seperti Anda membutuhkan semua perhatian yang Anda bisa..."

    show mrsj 14
    show player 13
    player_name "..."
    show mrsj 49
    mrsj "Maksud saya, terima kasih atas pengertiannya, {b}[firstname]{/b}."

    show mrsj 52
    mrsj "Hanya... Ingatlah untuk menjaga ini di antara kita, oke?"

    show mrsj 14
    show player 14
    player_name "Ya, {b}Ny. Johnson{/b}."

    hide player
    hide mrsj
    with dissolve
    return

label button_mrsj_yoga_help_repeat:
    show player 10
    player_name "Apa yang perlu saya bantu?"

    show player 5
    show mrsj 19
    mrsj "Saya membutuhkan seseorang untuk pergi dan {b}mengajar kelas yoga untuk saya malam ini{/b}."

    show mrsj 49
    mrsj "Apakah kamu pikir kamu bisa membantu... Tetangga kesayanganmu??"

    show mrsj 50
    show player 14
    player_name "Tentu saja!"

    show player 13
    show mrsj 17
    mrsj "Ingatlah untuk {b}mempelajari gerakan yoga dari daftar itu{/b} yang saya berikan!"

    return

label button_mrsj_youre_so_fit:
    show mrsj 14 at right
    show player 29 at left
    player_name "Saya harus mengatakan, {b}Ny. Johnson{/b}, kamu benar-benar bugar!"

    player_name "Apakah Anda banyak berolahraga?"

    show mrsj 18 at right
    show player 13 at left
    mrsj "Ah... Kamu baik sekali!"

    show mrsj 17 at right
    mrsj "Baiklah, saya mencoba menggunakan gym sesering mungkin..."

    mrsj "... Saya juga pergi jogging! Dan saya juga melakukan yoga di kamar saya pada malam hari..."

    show mrsj 19 at right
    show player 21 at left
    player_name "Ya, itu berhasil!"

    show player 13 at left
    mrsj "Menurutmu?"

    show mrsj 15 at right
    show player 11 at left
    mrsj "Bokongku masih agak besar..."

    show mrsj 16 at right
    show player 23 at left
    mrsj "... Dan payudaraku tidak seperti dulu lagi..."

    player_name "..."
    show player 28 at left
    show mrsj 19 at right
    player_name "{i}*Meneguk*{/i}"

    show player 1 at left
    show mrsj 18 at right
    mrsj "Apakah ada hal lain yang ingin Anda bicarakan?"

    return

label button_mrsj_leave:
    python:
        mrsj_nude = game.timer.is_dark() and \
                    M_erik.finished_state(S_erik_learn_prep)
        mrsj_nude_bed = game.timer.is_dark() and \
                        M_mrsj.finished_state(S_mrsj_cupid_report)

    if mrsj_nude:
        show mrsj 39
        show player 14 at left
        player_name "Aku harus pergi, tapi aku akan kembali!"

    else:
        if mrsj_nude_bed:
            show mrsj 53
        else:
            show mrsj 14 at right
        show player 14 at left
        player_name "Saya harus mencari {b}Erik{/b}!"

    if mrsj_nude or mrsj_nude_bed:
        if mrsj_nude:
            show mrsj 40
        elif mrsj_nude_bed:
            show mrsj 54
        show player 1 at left
        mrsj "Benar-benar?"

        mrsj "Ya, pastikan untuk segera kembali!"

    else:
        show mrsj 18 at right
        show player 1 at left
        mrsj "Baiklah kalau begitu!"

    if mrsj_nude:
        show mrsj 39
    elif mrsj_nude_bed:
        show mrsj 53
    else:
        show mrsj 14 at right
    show player 17 at left
    player_name "Sampai jumpa, {b}Ny. Johnson{/b}!"


    $ del mrsj_nude, mrsj_nude_bed
    return

label mrsj_erik_poker_invite_early:
    player_name "Saya ingin tahu apakah Anda ingin bergabung dengan {b}Erik{/b} dan saya untuk bermain poker?"

    show player 1
    show mrsj 17
    mrsj "Saya tidak bisa sekarang, saya harus segera mengajar kelas..."

    mrsj "Tapi mampirlah ke kamarku {b}malam ini{/b} dan aku akan dengan senang hati melakukannya."

    show player 18
    show mrsj 14
    player_name "Luar biasa! Terima kasih, {b}Ny. Johnson{/b}!"

    hide player
    hide mrsj
    with dissolve
    return

label mrsj_erik_poker_invite_fail:
    player_name "Saya ingin tahu apakah Anda bisa mengajari kami bermain poker?"

    show mrsj 17
    show player 1
    mrsj "Permainan kartu?"

    show mrsj 14
    show player 14
    player_name "Ya, {b}Erik{/b} dan saya hanya mencari pemain ketiga."

    show mrsj 17
    show player 14
    mrsj "Oh, aku ingin sekali."

    show player 19
    mrsj "Tapi aku benar-benar tidak punya waktu hari ini, maaf..."

    show mrsj 14
    show player 14
    player_name "Tidak apa-apa, mungkin lain kali."

    hide player
    hide mrsj
    with dissolve
    return

label mrsj_erik_poker_invite_pass:
    player_name "Saya ingin tahu apakah Anda ingin bergabung dengan {b}Erik{/b} dan saya untuk bermain poker?"

    show player 1
    show mrsj 17
    mrsj "Sekarang?"

    show player 14
    show mrsj 14
    player_name "Ya..."

    player_name "Maksudku, kamu tidak perlu melakukannya!"

    player_name "{b}Erik{/b} dan saya hanya mencari pemain ketiga..."

    show player 1
    show mrsj 17
    mrsj "Dia menunggu di bawah?"

    show player 14
    show mrsj 14
    player_name "Ya, kami ingin bermain sekarang, jika Anda senggang?"

    show player 1
    mrsj "Hmm..."

    show mrsj 17
    mrsj "Kedengarannya menyenangkan, saya bahkan mungkin bisa mengajari kalian satu atau dua hal."

    show mrsj 18
    show player 13
    mrsj "Ayo pergi!"

    show player 18
    show mrsj 14
    player_name "Luar biasa! Terima kasih, {b}Ny. Johnson{/b}!"

    hide mrsj
    hide player
    with dissolve

    scene erik_basement_c
    show old_erik 1f at Position(xpos=300,ypos=768)
    with fade
    show mrsj 19 at right
    show player 1 at left
    with dissolve
    mrsj "Kalian tidak berencana bermain seperti ini, kan?"

    show player 11
    show mrsj 14
    player_name "..."
    show player 10
    player_name "Apa maksudmu?"

    show player 11
    show mrsj 18
    mrsj "Anda tidak bisa bermain poker tanpa minuman yang enak!"

    show mrsj 14
    show player 1
    show old_erik 4f
    erik "Minuman?"

    show old_erik 1f
    show mrsj 18
    mrsj "Mari kita lihat apa yang tersisa di {b}lemari alkohol{/b}, oke?"

    hide mrsj
    hide old_erik
    hide player
    with dissolve

    scene erik_basement_cabinet with fade
    show old_erik 5f at Position(xpos=300,ypos=768)
    show player 1 at left
    show mrsj 14 at right
    with dissolve
    erik "Wiski..."

    erik "Wiski... Wiski..."

    erik "Wiski... Wiski... Wiski..."

    erik "Tidak ada apa-apa selain wiski di sini..."

    show old_erik 1f
    show mrsj 17
    mrsj "Suamiku hanya minum wiski."

    show mrsj 14
    show player 14
    player_name "Tidak apa-apa!"

    player_name "Kami akan mengambil apa pun yang ada di sana, haha!"

    show old_erik 15
    show player 1
    with dissolve
    erik "Haruskah kita mencobanya sebelum menyajikannya ke meja?"

    show old_erik 16
    show mrsj 22
    with dissolve
    mrsj "Mari kita lihat bagaimana rasanya..."

    show old_erik 20
    show mrsj 21
    show player 185
    with dissolve
    erik "Ini dia..."

    show player 186
    show old_erik 17
    player_name "Bersulang!"

    show player 189
    show old_erik 19
    show mrsj 25
    with fastdissolve
    pause
    show mrsj 26
    show old_erik 17
    show player 190
    with fastdissolve
    pause
    show player 191
    player_name "Ugh!!"

    show player 188
    show mrsj 24
    show old_erik 17
    with dissolve
    mrsj "Wah..."

    show old_erik 20
    show mrsj 14
    with dissolve
    erik "Hmm... Lumayan!"

    show old_erik 17
    player_name "..."
    show player 187
    player_name "Kamu menyukainya?!"

    show player 188
    show old_erik 20
    erik "Ya, itu agak manis."

    show player 185
    show old_erik 17
    show mrsj 18
    mrsj "Baiklah, teman-teman! Ayo ambil ini kembali dan mulai permainannya!"

    hide mrsj
    hide old_erik
    hide player
    with dissolve

    scene expression "minigames/poker/location_erik_basement_poker.jpg"
    show mrsjpoker 2 zorder 1 at Position(xpos=857,ypos=626)
    show mrsjpokerc1 7 zorder 2 at Position(xpos=815,ypos=584)
    show mrsjpokerc2 8 zorder 2 at Position(xpos=910,ypos=387)
    show old_erikpoker 1 zorder 1 at Position(xpos=153,ypos=626)
    show old_erikpokerc 9 zorder 2 at Position(xpos=144,ypos=592)
    with fade
    mrsj "Jadi..."

    mrsj "Apakah kita bermain Omaha, atau Texas Hold'em?"

    show mrsjpoker 1
    player_name "..."
    player_name "Kami hanya tahu strip poker..."

    show mrsjpoker 2
    mrsj "Haha! Apakah kamu bercanda?"

    show mrsjpoker 10 at Position(xpos=856,ypos=627)
    player_name "Itu satu-satunya orang baik yang bermain di sekolah..."

    show old_erikpoker 2
    erik "Anda tidak perlu... {b}Ny. Johnson{/b}."

    show old_erikpoker 11
    show mrsjpoker 9 at Position(xpos=856,ypos=627)
    mrsj "saya akan bermain!"

    show mrsjpoker 4 at Position(xpos=857,ypos=626)
    mrsj "Saya bukan orang yang pemalu. Aku juga bisa bersenang-senang!"

    show mrsjpoker 2
    mrsj "Saya biasa bermain strip poker dulu..."

    show mrsjpoker 5
    mrsj "... Dan saya adalah yang {b}terbaik{/b} dalam hal itu!"

    show old_erikpoker 12
    show mrsjpoker 1
    erik "Jadi, apa yang kita lakukan sekarang?"

    show old_erikpoker 1
    return

label mrsj_erik_poker_invite_repeat:
    python:
        mrsj_nude = game.timer.is_dark() and \
                    M_erik.finished_state(S_erik_learn_prep)
        mrsj_nude_bed = game.timer.is_dark() and \
                        M_mrsj.finished_state(S_mrsj_cupid_report)

    show player 14 at left
    if mrsj_nude:
        show mrsj 39
    elif mrsj_nude_bed:
        show mrsj 53
    else:
        show mrsj 14 at right
    player_name "Apakah Anda ingin bermain poker bersama kami lagi?"

    show player 1
    if mrsj_nude:
        show mrsj 40
    elif mrsj_nude_bed:
        show mrsj 54
    else:
        show mrsj 17
    mrsj "Masih mencari teman untuk bermain?"

    show player 14
    if mrsj_nude:
        show mrsj 39
    elif mrsj_nude_bed:
        show mrsj 53
    else:
        show mrsj 14
    player_name "Yah, hanya saja-"

    show player 1
    if mrsj_nude:
        show mrsj 40
    elif mrsj_nude_bed:
        show mrsj 54
    else:
        show mrsj 18
    mrsj "Tidak apa-apa!!"

    show player 1
    if mrsj_nude:
        show mrsj 40
    elif mrsj_nude_bed:
        show mrsj 54
    else:
        show mrsj 17
    mrsj "aku akan bermain denganmu kawan..."

    show player 14
    if mrsj_nude:
        show mrsj 39
    elif mrsj_nude_bed:
        show mrsj 53
    else:
        show mrsj 14
    player_name "Benar-benar?"

    show player 1
    if mrsj_nude:
        show mrsj 40b
    elif mrsj_nude_bed:
        show mrsj 54
    else:
        show mrsj 20
    mrsj "Yah... Terakhir kali agak berlebihan..."

    show player 13
    if mrsj_nude:
        show mrsj 40
    elif mrsj_nude_bed:
        show mrsj 54
    else:
        show mrsj 18
    mrsj "Tapi kenapa tidak?"

    show player 14
    if mrsj_nude:
        show mrsj 39
    elif mrsj_nude_bed:
        show mrsj 53
    else:
        show mrsj 14
    player_name "Oke."

    show player 13
    if mrsj_nude:
        show mrsj 40
    elif mrsj_nude_bed:
        show mrsj 54
    else:
        show mrsj 17
    mrsj "Kapan kita bermain?"

    show player 14
    if mrsj_nude:
        show mrsj 39
    elif mrsj_nude_bed:
        show mrsj 53
    else:
        show mrsj 14
    if mrsj_nude:
        player_name "Sekarang!"

    else:
        player_name "{b}Erik{/b} sudah menunggu di bawah."

    show player 1
    if mrsj_nude:
        show mrsj 40b
    elif mrsj_nude_bed:
        show mrsj 54
    else:
        show mrsj 18
    mrsj "Haha, baiklah."

    if mrsj_nude or mrsj_nude_bed:
        mrsj "Biarkan aku berpakaian."

        if mrsj_nude_bed:
            mrsj "Jadi kamu bisa menanggalkan pakaianku lagi!"

        else:
            mrsj "Jika tidak, ini akan menjadi pertandingan yang sangat singkat!"

    hide mrsj
    hide old_erik
    hide player
    with dissolve

    $ del mrsj_nude, mrsj_nude_bed

    scene erik_basement_cabinet
    show old_erik 4f at Position(xpos=300)
    with fade
    erik "Aku akan mengambil wiski!"

    show player 1 at left
    show mrsj 14 at right
    with dissolve
    show old_erik 1f
    show mrsj 19
    show player 11
    mrsj "Oh, apakah kalian berdua yakin tentang itu?"

    show mrsj 19c
    show player 10
    player_name "Tentang apa?"

    show mrsj 19
    show player 11
    mrsj "Alkoholnya, kamu ingat apa yang terjadi terakhir kali, kan?"

    show mrsj 19c
    show old_erik 5f
    erik "Tapi, kita semua bersenang-senang, bukan?"

    show old_erik 1f
    pause
    show mrsj 14 with fastdissolve
    pause
    show mrsj 17
    show player 1
    mrsj "Saya kira Anda benar..."

    show mrsj 18
    mrsj "Oh, apa-apaan ini, ayo kita lakukan!"

    hide mrsj
    hide old_erik
    hide player
    with dissolve

    scene expression "minigames/poker/location_erik_basement_poker.jpg"
    show mrsjpoker 2 zorder 1 at Position(xpos=857,ypos=626)
    show mrsjpokerc1 7 zorder 2 at Position(xpos=815,ypos=584)
    show mrsjpokerc2 8 zorder 2 at Position(xpos=910,ypos=387)
    show old_erikpoker 1 zorder 1 at Position(xpos=153,ypos=626)
    show old_erikpokerc 9 zorder 2 at Position(xpos=144,ypos=592)
    with fade
    mrsj "Jadi..."

    mrsj "Apakah kita akan bermain strip poker lagi?"

    show mrsjpoker 1
    player_name "..."
    show mrsjpoker 2
    mrsj "Ha ha! Aku bisa membacakan kalian berdua seperti sepasang buku!"

    show mrsjpoker 10 at Position(xpos=856,ypos=627)
    show old_erikpoker 2
    erik "Anda tidak punya-"

    show old_erikpoker 11
    show mrsjpoker 9 at Position(xpos=856,ypos=627)
    mrsj "saya akan bermain!"

    show mrsjpoker 4 at Position(xpos=857,ypos=626)
    mrsj "Saya bukan orang yang pemalu. Saya pikir Anda sudah mengetahuinya sekarang!"

    show mrsjpoker 2
    show old_erikpoker 1
    return

label mrsj_erik_fork:
    show player 14 at left
    show mrsj 14 at right
    player_name "Saya ingin berbicara tentang {b}Erik{/b}..."

    show player 1
    show mrsj 19
    mrsj "Oh, apakah dia baik-baik saja?"

    show player 14
    show mrsj 19c
    player_name "Ya, dia baik-baik saja."

    player_name "Aku sedang berbicara dengannya tentang apa yang terjadi malam itu..."

    show player 11
    show mrsj 19
    mrsj "Apakah dia kesal?"

    show player 14
    show mrsj 19c
    player_name "Tidak, tidak sama sekali."

    show player 10
    player_name "Dia hanya tidak yakin dengan apa yang dia inginkan..."

    show player 11
    show mrsj 19
    mrsj "Bagaimana bisa?"

    show player 10
    show mrsj 19c
    player_name "Saya pikir dia sudah menyerah untuk bertemu gadis-gadis."

    player_name "Aku bisa mencoba membantunya mendapatkan pacar, tapi menurutku dia lebih menyukaimu..."

    show player 13
    show mrsj 19
    mrsj "Ya ampun..."

    show mrsj 20
    mrsj "Apakah aku terlalu melindunginya?"

    show mrsj 19
    mrsj "Menurut Anda apa yang harus saya lakukan?"

    show mrsj 19c
    return

label mrsj_erik_fork_teach:
    show player 14 at left
    show mrsj 19c at right
    player_name "Saya pikir yang terbaik adalah jika Anda memberinya perhatian yang dia butuhkan..."

    show mrsj 19
    show player 1
    mrsj "Menurutmu begitu?"

    show mrsj 19c
    show player 14
    player_name "Yah, menurutku dia tidak ingin bertemu gadis lain..."

    player_name "... Dan dia sangat menyukaimu!"

    show mrsj 19
    show player 1
    mrsj "Dia selalu dekat denganku..."

    show mrsj 19c
    show player 14
    player_name "Kami bersenang-senang malam itu!"

    player_name "Aku belum pernah melihat {b}Erik{/b} sebahagia ini."

    show mrsj 19
    show player 11
    mrsj "Menurutmu... Kalian ingin lebih... Perhatian?"

    show mrsj 19c
    show player 21
    player_name "Aku... menurutku begitu!"

    show mrsj 20
    show player 13
    mrsj "Jika tidak ada gadis di sekolah yang memberinya perhatian yang dia butuhkan..."

    show mrsj 19
    mrsj "... Mungkin aku yang harus menjadi orangnya?"

    show mrsj 14
    show player 14
    player_name "Saya pikir dia akan menyukainya."

    show mrsj 49
    show player 11
    mrsj "Bagaimana jika saya memberi kalian beberapa... Pendidikan seks pribadi?"

    show mrsj 50
    player_name "!!!" with vpunch
    show mrsj 49
    mrsj "Tentu saja itu hanya untuk tujuan pendidikan..."

    show mrsj 50
    show player 29
    player_name "Oh, aku emm... Aku tidak keberatan sama sekali!"

    show mrsj 49
    show player 13
    mrsj "Tapi aku harus memikirkannya terlebih dahulu."

    show mrsj 50
    show player 14
    player_name "Tentu, {b}Ny. Johnson{/b}!"

    show mrsj 14
    show player 1
    with None
    hide player
    hide mrsj
    with dissolve
    return

label mrsj_erik_fork_match:
    show player 14 at left
    show mrsj 19c
    player_name "Saya pikir kita harus mencoba mencarikannya pacar."

    show player 1
    show mrsj 19
    mrsj "Menurutmu begitu?"

    show player 14
    show mrsj 19c
    player_name "Yah, menurutku dia akan lebih bahagia..."

    player_name "... Dan itu akan membangun kepercayaan dirinya!"

    show player 1
    show mrsj 20
    mrsj "Dia memang perlu keluar lebih banyak..."

    show player 10
    show mrsj 19c
    player_name "Jangan salah paham, kami bersenang-senang malam itu..."

    show player 14
    player_name "... Tapi menurutku {b}Erik{/b} perlu bertemu gadis lain."

    show player 13
    show mrsj 20
    mrsj "Anda benar..."

    show player 11
    show mrsj 19
    mrsj "Tapi bagaimana dengan... Aku?"

    show player 10
    show mrsj 19c
    player_name "Apa maksudmu?"

    show player 11
    show mrsj 19
    mrsj "Ya..."

    mrsj "Jika {b}Erik{/b} menemukan pacar... Apa yang akan saya lakukan?"

    show mrsj 20
    mrsj "Aku tidak ingin ada orang yang memberikan perhatianku..."

    show player 21
    show mrsj 19c
    player_name "Oh, saya yakin Anda akan menemukan seseorang {b}Ny. Johnson{/b}!"

    show mrsj 14
    player_name "Kamu sangat... Menarik, dan penuh kasih sayang!"

    show player 13
    show mrsj 17
    mrsj "Aww, manis sekali ucapanmu."

    show mrsj 50
    mrsj "Hmm..."

    show mrsj 49
    show player 1
    mrsj "Saya punya ide berbeda!"

    mrsj "Bagaimana jika saya mengambil perhatian itu..."

    show player 11
    mrsj "... Dan memberikannya kepada {i}kamu{/i}?"

    show mrsj 50
    player_name "!!!" with vpunch
    show mrsj 49
    mrsj "Ada apa?"

    mrsj "Hanya jika Anda menginginkannya, itulah yang ingin saya katakan..."

    show player 21
    show mrsj 50
    player_name "A-aku tidak keberatan sama sekali!"

    player_name "Tapi, hanya selama {b}Erik{/b} tidak masalah."

    show player 1
    show mrsj 49
    mrsj "Tanyakan saja padanya!"

    mrsj "aku yakin dia akan baik-baik saja dengan itu..."

    show player 13
    mrsj "... Apalagi kalau dia terlalu sibuk bermain-main dengan gadis lain! Ha ha."

    show player 29
    show mrsj 50
    player_name "Saya kira begitu, haha."

    show player 14
    player_name "Aku akan mencoba mencarikan seseorang untuknya..."

    show player 13
    show mrsj 49
    mrsj "Kembalilah dan beri tahu saya apa yang terjadi."

    show player 17
    show mrsj 50
    player_name "Tentu, {b}Ny. Johnson{/b}!"

    show mrsj 14
    show player 1
    with None
    hide player
    hide mrsj
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
