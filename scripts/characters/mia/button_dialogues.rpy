label mia_dialogue_helen_route:
    if player.location == L_miahouse_miaroom:
        scene mia_bedroom_c
    elif player.location == L_school_scienceclassroom:
        scene school_science_c02
    elif player.location == L_miahouse_entrance:
        scene expression player.location.background_closeup
    show old_mia 8 at right
    if player.location == L_school_scienceclassroom:
        show old_mial 1f at right
    show player 10 at left
    with dissolve
    player_name "Hai, {b}Mia{/b}."

    show player 5
    show old_mia 12
    mia "Oh... Halo, {b}[firstname]{/b}."

    show old_mia 8
    show player 10
    player_name "..."
    show player 11
    pause
    show player 10
    player_name "Jadi, bagaimana kabarmu?"

    show player 5
    show old_mia 12
    mia "Aku masih merasa sedikit sedih karena keluargaku tidak bisa bersama."

    show old_mia 46f
    mia "Aku rindu bangun dan bertemu ayahku setiap pagi."

    mia "Dan {b}Ibu{/b} nampaknya semakin menjauh akhir-akhir ini."

    show old_mia 45f
    show player 10
    player_name "Hah..."

    show player 12
    player_name "Hei, apakah kamu ingin melakukan sesuatu nanti?"

    show player 10
    player_name "Ada kuis lain yang akan datang. Ingin belajar?"

    show player 5
    show old_mia 46f
    mia "Tidak, aku sedang tidak ingin melakukan apa pun saat ini."

    show old_mia 45f
    show player 24
    player_name "..."
    show player 10
    player_name "Baiklah, aku akan menyusulmu nanti!"

    show player 5
    mia "..."
    hide player
    hide old_mia
    hide old_mial
    with dissolve
    return

label mia_dialogue_helen_change_news:
    if player.location == L_miahouse_miaroom:
        scene mia_bedroom_c
    elif player.location == L_school_scienceclassroom:
        scene school_science_c02
    elif player.location == L_miahouse_entrance:
        scene expression player.location.background_closeup
    show player 13 at left
    show old_mia 10 at right
    if player.location == L_school_scienceclassroom:
        show old_mial 1f at right
    with dissolve
    mia "{b}[firstname]{/b}!"

    mia "Apa yang telah terjadi?"

    show old_mia 7
    show player 14
    player_name "Aku berbicara dengan ibumu. Saya pikir saya berhasil menghubunginya!"

    show player 13
    show old_mia 10
    mia "Kamu melakukannya?! Tapi bagaimana..."

    show old_mia 7
    show player 17
    player_name "Aku tahu, ceritanya panjang..."

    show player 14
    player_name "... Tapi semuanya akan baik-baik saja. Saya berjanji!"

    player_name "Kami berbicara, dan dia setuju untuk mencoba mengubah keadaan agar mereka dapat kembali bersama!"

    show player 13
    show old_mia 9
    mia "Itu luar biasa!"

    show old_mia 7
    show player 14
    player_name "Menurutku dia juga akan lebih toleran padamu..."

    player_name "... Aku merasa dia akan mengubah sikapnya."

    show player 13
    show old_mia 10
    mia "Wow... Anda pasti bekerja keras untuk meyakinkannya!"

    show old_mia 7
    show player 17
    player_name "Saya punya beberapa trik. Ha ha!"

    show player 13
    show old_mia 10
    mia "Saya sangat senang! Terima kasih, {b}[firstname]{/b}!"

    show old_mia 7
    pause
    hide player
    show old_mia 49 at left
    if player.location == L_school_scienceclassroom:
        show old_mial 1c
    with dissolve
    player_name "!!!"
    show player 11 at left
    show old_mia 10 at right
    if player.location == L_school_scienceclassroom:
        show old_mial 1f
    with dissolve
    mia "Kalau begitu, sampai jumpa lagi!"

    show old_mia 7
    show player 21
    player_name "Selamat tinggal."

    hide player
    hide old_mial
    hide old_mia
    with dissolve
    return

label mia_dialogue_mia_bedroom_mia_end_intro:
    scene location_mia_bedroom_closeup
    show player 13 at left
    show old_mia 10 at right
    with dissolve
    mia "Saya sangat senang Anda datang."

    show old_mia 7
    show player 14
    player_name "Hai, {b}Mia{/b}."

    show player 13
    show old_mia 10
    mia "Jadi kamu ingin jalan-jalan?"

    mia "Atau apakah Anda di sini untuk mencoba teknik belajar baru saya?"

    show old_mia 7
    return

label mia_dialogue_mia_bedroom_mia_end_study:
    player_name "Mau... Belajar telanjang lagi?"

    show player 13
    show old_mia 10
    mia "Ya!"

    mia "Duduklah di tempat tidur sementara aku berganti pakaian."

    hide player
    hide old_mia
    with dissolve
    return

label mia_dialogue_mia_bedroom_mia_end_leave:
    show old_mia 8
    show player 10
    player_name "Aku ingin sekali... Tapi ini sudah larut..."

    show old_mia 12
    show player 5
    mia "Oh oke..."

    mia "... Apakah kamu akan segera kembali?"

    show player 14
    show old_mia 8
    player_name "Ya. Saya akan melihat apa yang bisa saya lakukan!"

    show old_mia 12
    show player 1
    mia "Selamat malam..."

    hide player
    hide old_mia
    with dissolve
    return

label mia_dialogue_mia_bedroom_mia_tattoo_help:
    scene location_mia_bedroom_closeup
    show player 13 at left
    show old_mia 10 at right
    with dissolve
    mia "Hei!"

    mia "Saya sangat senang Anda bisa melakukannya!"

    show old_mia 7
    show player 17
    player_name "Tidak apa-apa. Sepertinya ada sesuatu yang penting untuk dibicarakan."

    show player 14
    player_name "Anda ingin menanyakan sesuatu kepada saya?"

    show player 13
    show old_mia 10
    mia "Yah, itu tidak {i}itu{/i} penting..."

    mia "... Saya berharap bisa mendapatkan pendapat Anda tentang sesuatu, dan mungkin Anda bisa membantu saya."

    show old_mia 7
    show player 10
    player_name "Uhh... kurasa begitu. Tentang apa ini?"

    show player 11
    show old_mia 10
    mia "Tahukah Anda tentang tato?"

    show old_mia 7
    show player 10
    player_name "Tato?!"

    show player 12
    player_name "Mengapa? Apakah Anda berpikir untuk mendapatkannya?"

    show player 11
    show old_mia 12
    mia "Aku tahu itu buruk..."

    mia "... Tapi, aku bosan disuruh apa yang harus kulakukan!"

    mia "Saya hanya ingin melakukan sesuatu... Spontan dan bersenang-senang!"

    mia "Untuk merasa bebas..."

    show old_mia 8
    show player 10
    player_name "Apakah ibumu akan baik-baik saja dengan ini?"

    show player 5
    show old_mia 12
    mia "Saya tidak peduli lagi."

    show old_mia 8
    show player 11
    player_name "..."
    show player 14
    player_name "Tato itu cukup keren. Aku hanya tidak ingin kamu mendapat masalah."

    show player 13
    show old_mia 12
    mia "Apakah kamu akan membantuku?"

    show old_mia 8
    show player 14
    player_name "Tentu, tapi bagaimana caranya?"

    show player 13
    show old_mia 10
    mia "Saya tahu Anda suka menggambar sesuatu di kelas sepanjang waktu, dan saya telah melihat karya seni Anda..."

    mia "... Saya berharap Anda akan menggambar sesuatu untuk tato saya!"

    show old_mia 7
    show player 22
    player_name "!!!" with hpunch
    show player 29
    player_name "Apa kamu yakin?"

    show player 13 with dissolve
    show old_mia 10
    mia "Ya! Kamu sangat ahli dalam hal itu."

    show old_mia 7
    show player 21
    player_name "Terima kasih, tapi saya bahkan tidak tahu apa yang Anda inginkan!"

    show player 13
    show old_mia 10
    mia "Hmm... Aku ingin sesuatu yang lucu!"

    show old_mia 9
    mia "Dengan warna-warna cantik!"

    show old_mia 7
    show player 24
    player_name "Bagaimana jika itu buruk dan Anda akhirnya membencinya?"

    show player 13
    show old_mia 10
    mia "Saya yakin semuanya akan baik-baik saja!"

    show old_mia 7
    show player 14
    player_name "Jika kamu berkata begitu..."

    show player 13
    show old_mia 10
    mia "Datang menemui saya ketika Anda memiliki sesuatu."

    show old_mia 7
    show player 14
    player_name "Baiklah."

    show player 13
    show old_mia 10
    mia "Saya harus tidur. Sampai jumpa di sekolah!"

    show old_mia 7
    show player 36 with dissolve
    player_name "Selamat malam!"

    hide player
    hide old_mia
    with dissolve
    return

label mia_dialogue_mia_bedroom_mia_church_plan:
    scene location_mia_bedroom_closeup
    show player 13 at left
    show old_mia 12 at right
    with dissolve
    player_name "Hai, {b}Mia{/b}."

    player_name "Kupikir aku akan menyelinap dan menemuimu."

    show player 5
    show old_mia 10
    mia "Ah, terima kasih. Saya menghargainya."

    mia "Ada apa?"

    show old_mia 7
    return

label mia_dialogue_mia_bedroom_intro:
    scene location_mia_bedroom_closeup
    show old_mia 10 at right
    show player 13 at left with dissolve
    mia "Saya sangat senang Anda datang!"

    show old_mia 7
    show player 21
    player_name "Hai, {b}Mia{/b}!"

    show player 29
    player_name "Terasa aneh, menyelinap ke rumah seseorang di malam hari..."

    show old_mia 9
    show player 13
    mia "Tidak apa-apa! Kita tidak akan mendapat masalah..."

    show old_mia 10
    show player 11
    mia "... Kita hanya perlu {b}diam saja{/b}!"

    show old_mia 7
    show player 17
    player_name "Jika Anda berkata demikian. Ha ha."

    show old_mia 12
    show player 1
    return

label mia_dialogue_science_classroom_mia_strip_aftermath:
    scene school_science_c02
    show player 5 at left
    show old_mia 12 at right
    show old_mial 1f at right
    with dissolve
    mia "Hai, {b}[firstname]{/b}..."

    show old_mia 8
    show player 10
    player_name "Bagaimana kabarmu?"

    show player 5
    show old_mia 12
    mia "Aku baik-baik saja, tapi kita sebaiknya tidak bicara."

    mia "Aku sudah cukup mendapat masalah... Maaf."

    show old_mia 8
    show player 24
    player_name "..."
    hide old_mia
    hide old_mial
    hide player
    with dissolve
    return

label mia_dialogue_science_classroom_mia_consult:
    scene school_science_c02
    show player 1 at left
    show old_mia 9 at right
    show old_mial 1f at right
    with dissolve
    mia "{b}[firstname]{/b}!"

    show old_mia 7
    show player 14
    player_name "Hei, {b}Mia{/b}!"

    show old_mia 10
    show player 13
    mia "Aku ingin mengucapkan terima kasih karena telah datang mengunjungiku malam itu..."

    show player 11
    mia "... Aku sangat menikmatinya, tapi..."

    show old_mia 7
    player_name "..."
    show old_mia 8
    show player 10
    player_name "Apakah ada yang salah?"

    show old_mia 12
    show player 11
    mia "Ya, ibuku semakin curiga."

    show old_mia 8
    show player 10
    player_name "Tentang saya?"

    show old_mia 12
    show player 5
    mia "Ya, menurutku dia tahu kamu datang."

    show old_mia 8
    show player 10
    player_name "Apakah ini benar-benar masalah besar?"

    show old_mia 12
    show player 5
    mia "Dia pasti TIDAK setuju dengan itu."

    show player 11
    mia "Maksudku, mungkin jika entah bagaimana... Kau mempunyai sisi baik dari ayahku? Aku yakin dia bisa berbicara dengannya."

    show old_mia 8
    show player 10
    player_name "Ayahmu? Tapi bagaimana caranya?"

    show old_mia 7
    player_name "Dia tampaknya juga cukup ketat!"

    show old_mia 9
    show player 11
    mia "Tidak mungkin, dia sangat lembut..."

    show old_mia 10
    show player 1
    mia "Dia dulunya sangat keren, tahu?"

    show old_mia 7
    show player 14
    player_name "Oke, jadi bagaimana aku bisa mendapatkan sisi baiknya?"

    show old_mia 10
    show player 1
    mia "Hmm... aku tidak yakin..."

    mia "Mungkin mencoba {b}berikan dia sesuatu yang dia suka, seperti sekotak donat{/b}!"

    show old_mia 7
    show player 14
    player_name "Donat?"

    show old_mia 9
    show player 1
    mia "Ha ha. Aku tahu... Sangat tipikal. Tapi, dia sangat menyukainya!"

    show old_mia 8
    show player 14
    player_name "Apakah dia punya jenis donat favorit?"

    show old_mia 12
    show player 1
    mia "Ah, aku tidak begitu yakin..."

    show old_mia 7
    show player 14
    player_name "Baiklah! Mungkin saya bisa {b}mencari tahu dan memberinya sesuatu{/b}."

    show old_mia 10
    show player 1
    mia "Terima kasih! Kamu manis sekali... Aku yakin dia akan menyukainya!"

    return

label mia_dialogue_science_classroom_mia_parent_unblock:
    scene school_science_c02
    show player 1 at left
    show old_mia 9 at right
    show old_mial 1f at right
    with dissolve
    mia "{b}[firstname]{/b}!"

    show old_mia 10
    show player 11
    mia "Anda tidak akan percaya ini!"

    show player 14
    show old_mia 7
    player_name "Hah? Apa yang telah terjadi?"

    show player 1
    show old_mia 10
    mia "Tadi malam, aku mendengar ayahku membicarakanmu dengan ibuku!"

    show player 14
    show old_mia 7
    player_name "Tentang saya? Sungguh?"

    show player 1
    show old_mia 9
    mia "Ya!"

    show old_mia 10
    mia "Dia mengatakan betapa pentingnya berteman di usiaku..."

    mia "... Betapa menurutnya dia harus mengizinkan aku bertemu denganmu, karena kamu adalah orang yang baik dan sebagainya..."

    show player 14
    show old_mia 7
    player_name "Wah..."

    player_name "Jadi, ibumu baik-baik saja denganku sekarang?!"

    show player 11
    show old_mia 10
    mia "Yah, dia tidak terlalu senang dengan gagasan itu, itu sudah pasti!"

    show player 1
    show old_mia 9
    mia "Tapi, menurutku itu mungkin berhasil sedikit."

    show player 17
    show old_mia 7
    player_name "Saya rasa itu adalah sesuatu."

    show player 13
    show old_mia 10
    mia "Terima kasih telah berbicara dengan ayahku..."

    show player 14
    show old_mia 7
    player_name "Itu bukan masalah besar, dan ayahmu sebenarnya tampak seperti pria yang keren!"

    show player 1
    show old_mia 10
    mia "Ya... Dia dulu lebih banyak bicara dalam hidup kami."

    show player 14
    show old_mia 8
    player_name "Bagaimanapun, aku harus kembali ke kelas-"

    show player 11
    show old_mia 12
    mia "Tunggu!! saya..."

    mia "Saya ingin mendapatkan pendapat Anda tentang sesuatu."

    show player 14
    show old_mia 8
    player_name "Sesuatu?"

    show player 11
    show old_mia 12
    mia "Saya merasa tidak nyaman membicarakannya di sini..."

    show player 13
    mia "Tapi mungkin... Kamu bisa mengunjungiku malam ini?"

    show player 14
    show old_mia 7
    player_name "Saya ingin sekali!"

    show player 1
    show old_mia 9
    mia "Manis!"

    show old_mia 10
    mia "Kalau begitu, aku akan menunggumu di rumah."

    hide old_mia
    hide old_mial
    hide player
    with dissolve
    return

label mia_dialogue_science_classroom_mia_favor:
    scene school_science_c02
    show player 13 at left
    show old_mia 10 at right
    show old_mial 1f at right
    with dissolve
    mia "Selamat pagi, {b}[firstname]{/b}!"

    show old_mia 7
    show player 14
    player_name "Selamat pagi, {b}Mia{/b}."

    show player 13
    show old_mia 10
    mia "Saya berharap Anda dapat membantu saya dengan sesuatu... Sekali lagi?"

    show old_mia 7
    show player 14
    player_name "Tentu saja, {b}Mia{/b}. Saya tidak keberatan!"

    show player 13
    show old_mia 10
    mia "Aku ingin kamu melakukan keajaibanmu dan mengajak ayahku keluar untuk makan malam bersama ibuku dan aku."

    mia "Dia mendengarkanmu..."

    show old_mia 7
    show player 14
    player_name "Makan malam? Sepertinya hubungan orang tuamu baik-baik saja lagi."

    player_name "Saya akan {b}mengunjungi karyanya{/b} dan melihat apa yang dapat saya lakukan!"

    show player 13
    show old_mia 12
    mia "Saya menghargai bantuan Anda, {b}[firstname]{/b}. Aku hanya tidak tahu apa yang akan kulakukan pada diriku sendiri jika mereka tidak kembali bersama."

    show old_mia 46f
    mia "aku merasa ini semua salahku..."

    show old_mia 45f
    show player 10
    player_name "Oh, ayolah, {b}Mia{/b}... Kamu tidak boleh berpikir seperti itu!"

    show player 14
    player_name "Jangan khawatir, aku akan mengantar ayahmu ke kencan makan malam itu."

    show player 13
    show old_mia 46f
    mia "Terima kasih... Kamu manis."

    hide old_mia
    hide old_mial
    hide player
    with dissolve
    return

label mia_dialogue_science_classroom_mia_need_space:
    scene school_science_c02
    show player 10 at left
    show old_mia 8 at right
    show old_mial 1f at right
    with dissolve
    player_name "Hai, {b}Mia{/b}..."

    player_name "Bagaimana kabarmu?"

    show player 5
    show old_mia 12
    mia "Saya baik-baik saja."

    show old_mia 8
    mia "..."
    show player 3 with dissolve
    player_name "..."
    show old_mia 12
    mia "Kurasa aku hanya ingin ruang saat ini."

    show old_mia 8
    show player 10 with dissolve
    player_name "Baiklah..."

    player_name "Saya akan berbicara dengan Anda nanti. Namun, beri tahu saya jika Anda membutuhkan sesuatu."

    show player 5
    show old_mia 12
    mia "Terima kasih, {b}[firstname]{/b}..."

    hide old_mia
    hide old_mial
    hide player
    with dissolve
    return

label mia_dialogue_science_classroom_mia_church_plan:
    scene school_science_c02
    show player 12 at left
    show old_mia 8 at right
    show old_mial 1f at right
    with dissolve
    player_name "Hei, {b}Mia{/b}!"

    player_name "Bagaimana kabarmu?"

    show player 5
    show old_mia 12
    mia "saya baik-baik saja."

    mia "Tapi saya berharap semuanya bisa kembali seperti semula di rumah."

    show old_mia 8
    show player 10
    player_name "Maaf..."

    show player 5
    show old_mia 12
    mia "Apakah ada sesuatu yang ingin Anda bicarakan?"

    show old_mia 8
    return

label mia_dialogue_science_classroom_mia_urgent_help:
    scene school_science_c02
    show player 5 at left
    show old_mia 12 at right
    show old_mial 1f at right
    with dissolve
    mia "Hai, {b}[firstname]{/b}!"

    mia "Tolong {b}mampir ke rumah saya hari ini{/b}, oke?"

    show old_mia 8
    show player 10
    player_name "Baiklah."

    show player 5
    show old_mia 12
    mia "Ada lagi yang Anda butuhkan?"

    show old_mia 8
    return

label mia_dialogue_science_classroom_intro:
    scene school_science_c02
    show player 14 at left
    show old_mia 7 at right
    show old_mial 1f at right
    with dissolve
    player_name "Hei, {b}Mia{/b}!"

    player_name "Bagaimana kabarmu?"

    show player 13
    show old_mia 10
    mia "Saya baik-baik saja."

    show old_mia 12
    mia "Tidak terlalu menantikan kelas saya berikutnya."

    show old_mia 7
    show player 17
    player_name "Ya. Aku mendengarmu."

    show player 13
    show old_mia 10
    mia "Apakah ada sesuatu yang ingin Anda bicarakan?"

    show old_mia 7
    return

label mia_dialogue_mias_house_entrance_mia_favor:
    scene expression player.location.background_closeup with fade
    show player 13 at left
    show old_mia 10 at right
    with dissolve
    mia "Selamat pagi, {b}[firstname]{/b}!"

    show old_mia 7
    show player 14
    player_name "Selamat pagi, {b}Mia{/b}."

    show player 13
    show old_mia 10
    mia "Saya berharap Anda dapat membantu saya dengan sesuatu... Sekali lagi?"

    show old_mia 7
    show player 14
    player_name "Tentu saja, {b}Mia{/b}. Saya tidak keberatan!"

    show player 13
    show old_mia 10
    mia "Aku ingin kamu melakukan keajaibanmu dan mengajak ayahku keluar untuk makan malam bersama ibuku dan aku."

    mia "Dia mendengarkanmu..."

    show old_mia 7
    show player 14
    player_name "Makan malam? Sepertinya hubungan orang tuamu baik-baik saja lagi."

    player_name "Saya akan {b}mengunjungi karyanya{/b} dan melihat apa yang dapat saya lakukan!"

    show player 13
    show old_mia 12
    mia "Saya menghargai bantuan Anda, {b}[firstname]{/b}. Aku hanya tidak tahu apa yang akan kulakukan pada diriku sendiri jika mereka tidak kembali bersama."

    show old_mia 46f
    mia "aku merasa ini semua salahku..."

    show old_mia 45f
    show player 10
    player_name "Oh, ayolah, {b}Mia{/b}... Kamu tidak boleh berpikir seperti itu!"

    show player 14
    player_name "Jangan khawatir, aku akan mengantar ayahmu ke kencan makan malam itu."

    show player 13
    show old_mia 46f
    mia "Terima kasih... Kamu manis."

    hide old_mia
    hide player
    with dissolve
    return

label mia_dialogue_mias_house_entrance_mia_helen_talk:
    scene expression player.location.background_closeup
    show player 5 at left
    show old_mia 12 at right
    with dissolve
    mia "Bisakah kamu {b}berbicara dengan ibuku{/b}? Dia ada di {b}kamarnya di lantai atas{/b}..."

    show player 10
    show old_mia 8
    player_name "Saya akan mencoba, {b}Mia{/b}."

    hide old_mia
    hide player
    with dissolve
    return

label mia_dialogue_mias_house_entrance_mia_church_plan:
    scene expression player.location.background_closeup
    show player 13 at left
    show old_mia 12 at right
    with dissolve
    mia "Hai, {b}[firstname]{/b}."

    show player 5
    pause
    show player 10
    show old_mia 8
    player_name "Halo, {b}Mia{/b}."

    show player 5
    show old_mia 12
    mia "Ada apa?"

    show old_mia 8
    return

label mia_dialogue_mias_house_entrance_intro:
    scene expression player.location.background_closeup
    show player 13 at left
    show old_mia 10 at right
    with dissolve
    mia "Hai, {b}[firstname]{/b}."

    show player 14
    show old_mia 7
    player_name "Halo, {b}Mia{/b}."

    show player 13
    show old_mia 10
    mia "Ada apa?"

    show old_mia 7
    return

label mia_dialogue_chat:
    show old_mia 7
    show player 2
    player_name "Tentu!"

    show player 10
    player_name "Umm... Kamu tidak perlu menjawab ini, tapi..."

    show old_mia 8
    player_name "Tidakkah kamu merasa aneh kalau orang tuamu tidak mengizinkanmu mempunyai teman?"

    show player 5
    mia "..."
    show old_mia 12
    mia "Hanya saja... Begitulah yang terjadi pada ibuku."

    show old_mia 8
    show player 12
    player_name "Dan kamu tidak keberatan?"

    show player 11
    show old_mia 12
    mia "Dia hanya bersikap protektif!"

    mia "Aku tahu dia sangat mencintaiku, dan menginginkan yang terbaik untukku..."

    show old_mia 8
    show player 12
    player_name "Tapi kamu harus bertemu dengan teman secara diam-diam..."

    show old_mia 12
    show player 5
    mia "Aku tahu... Tapi dia tidak akan mengerti."

    show old_mia 8
    show player 24
    player_name "begitu..."

    show player 21
    player_name "Selama kamu bahagia?"

    show old_mia 9
    show player 13
    mia "Ya!"

    return

label mia_dialogue_talent_show_help:
    show player 10
    player_name "Apakah Anda memainkan alat musik atau bernyanyi?"

    show player 5
    show old_mia 9
    mia "Ya, saya bernyanyi di paduan suara di gereja sepanjang waktu!"

    show old_mia 7
    show player 14
    player_name "Anda melakukannya? Luar biasa!"

    player_name "Anda harus bernyanyi di acara pencarian bakat {b}Miss Dewitt{/b}!"

    player_name "Kami benar-benar membutuhkan lebih banyak orang untuk menjadi sukarelawan."

    show player 13
    show old_mia 12
    mia "Oh, um."

    mia "Aku ingin tapi aku tidak bisa."

    show old_mia 8
    show player 10
    player_name "Hah? Mengapa tidak?"

    show player 5
    show old_mia 12
    mia "Ibuku bahkan tidak mengizinkanku pergi ke pertunjukan bakat, apalagi berpartisipasi."

    show old_mia 8
    show player 12
    player_name "Kenapa?"

    show player 5
    show old_mia 12
    mia "Dia tidak ingin aku mendengarkan musik rock atau rap..."

    mia "Dia takut itu akan mencemari pikiran mudaku atau semacamnya."

    show old_mia 8
    show player 12
    player_name "Itu menyebalkan!"

    show player 5
    show old_mia 12
    mia "Ya. Maaf."

    show player 10
    player_name "Tidak apa-apa, {b}Mia{/b}. Terima kasih!"

    return

label mia_dialogue_parents:
    show player 14
    player_name "Jadi, bagaimana kabar orang tuamu?"

    show player 13
    show old_mia 10
    mia "Sibuk. Ibuku selalu di gereja dan Ayah selalu bekerja."

    show old_mia 12
    mia "Mungkin yang terbaik adalah seperti itu."

    show old_mia 8
    show player 10
    player_name "Bagaimana bisa?"

    show player 11
    show old_mia 12
    mia "Saat orang tuaku berkumpul, yang mereka lakukan hanyalah berdebat."

    show player 5
    mia "Aku sangat membencinya."

    mia "Aku berharap mereka rukun, seperti dulu..."

    show old_mia 8
    show player 10
    player_name "Saya tidak tahu kalau seperti itu. Tampaknya mereka baik-baik saja."

    show player 5
    show old_mia 12
    mia "Ya, ibuku sepertinya yang paling sering mengaduk panci."

    mia "Dia sangat keras kepala dan tidak mau menerima jawaban tidak."

    mia "Jadi {b}Ayah{/b} ikuti saja apa pun yang dia katakan sekarang..."

    show old_mia 8
    show player 10
    player_name "Itu menyebalkan."

    show player 5
    show old_mia 12
    mia "Dia bahkan memaksaku untuk melakukan studi Alkitab akhir-akhir ini..."

    mia "... Dan bilang aku harus bertemu dengan seorang anak laki-laki dari gereja, jika aku sudah siap."

    show old_mia 8
    show player 11
    player_name "..."
    show old_mia 12
    mia "Aku tahu, ini... Aneh."

    show old_mia 9
    mia "Bagaimanapun! Mari kita bicara tentang hal lain."

    show old_mia 7
    show player 13
    return

label mia_dialogue_mia_clues:
    show player 10
    player_name "Di mana Anda bilang saya bisa menemukan petunjuk tentang keberadaan {b}Harold{/b}?"

    show player 5
    show old_mia 12
    mia "{b}Mulailah dengan menanyai rekan kerjanya di kantor polisi{/b}..."

    mia "... Dan {b}mencari petunjuk di sekitar tempat kerjanya{/b}."

    show old_mia 8
    show player 12
    player_name "Saya kira saya bisa bertanya-tanya untuk melihat di mana dia berada..."

    show player 5
    show old_mia 12
    mia "Terima kasih..."

    return

label mia_dialogue_mia_convince_harold:
    show player 10
    player_name "Apa yang kamu ingin aku lakukan lagi pada ayahmu?"

    show player 13
    show old_mia 10
    mia "Aku ingin kamu {b}mengundangnya makan malam bersama ibuku dan aku{/b}."

    mia "Kalian berdua sangat rukun. Mungkin Anda bisa memelintir lengannya jika diperlukan."

    show old_mia 7
    show player 14
    player_name "Tentu! Saya akan {b}menangkapnya di kantor polisi{/b}."

    show player 13
    show old_mia 10
    mia "Terima kasih, {b}[firstname]{/b}."

    return

label mia_dialogue_glasses:
    show player 12
    player_name "Apa yang kamu ingin aku lakukan dengan kacamata ini lagi?"

    show player 5
    show old_mia 10
    mia "Oh, aku berharap kamu bisa {b}menyerahkannya ke tempat kerja ayahku{/b}."

    show old_mia 7
    show player 14
    player_name "Itu benar... Aku ingat sekarang."

    player_name "Kalau begitu, aku akan melakukannya!"

    return

label mia_dialogue_donuts:
    show player 14 at left
    show old_mia 7 at right
    player_name "Ada ide bagaimana cara mengetahui jenis donat yang disukai ayahmu?"

    show player 1
    show old_mia 10
    mia "Oh, ehmm..."

    mia "Mungkin {b}bertanya seputar pekerjaannya{/b}?"

    mia "Mereka SUKA makan donat di sana..."

    show old_mia 7
    show player 17
    player_name "Haha, mungkin Anda benar, itu bisa berhasil."

    show old_mia 10
    show player 1
    mia "Ada lagi yang ingin Anda bicarakan?"

    show old_mia 7
    show player 1
    return

label mia_dialogue_mia_draw_tattoo:
    show old_mia 7 at right
    show player 10 at left
    player_name "Tentang seni tato yang Anda inginkan..."

    show player 5
    show old_mia 10
    mia "Oh! Apakah kamu memilikinya?!"

    show old_mia 7
    show player 10
    player_name "Tidak, belum."

    player_name "Tapi, apa yang kamu inginkan lagi?"

    show player 5
    show old_mia 10
    mia "Hmm... Sesuatu yang lucu dan penuh warna!"

    show old_mia 7
    show player 17
    player_name "Haha, baiklah."

    show player 14
    player_name "Saya akan melihat apa yang bisa saya lakukan."

    show player 13
    show old_mia 9
    mia "Terima kasih banyak, {b}[firstname]{/b}."

    return

label mia_dialogue_mia_show_tattoo_fail:
    show old_mia 7 at right
    show player 2 at left
    player_name "Tentang seni tato yang Anda inginkan..."

    show player 13
    show old_mia 10
    mia "Oh! Apakah kamu memilikinya?!"

    show old_mia 7
    show player 14
    player_name "Ya!"

    show player 239_240 with dissolve
    player_name "Butuh beberapa saat bagi saya untuk membuatnya..."

    show player 386 with dissolve
    player_name "Ini dia!"

    show player 13
    show old_mia 32
    if player.location == L_school_scienceclassroom:
        show old_mial 1b
    with dissolve
    mia "Hmm..."

    show player 10
    player_name "Apakah ada yang salah?"

    show player 11
    show old_mia 33
    mia "Yah, aku mengharapkan sesuatu yang berbeda."

    show old_mia 34
    show player 25
    player_name "Oh..."

    show player 24
    show old_mia 30
    mia "Saya menyukainya!!"

    show old_mia 33
    mia "Tapi mungkin Anda bisa mencoba yang lain?"

    show old_mia 34
    show player 10
    player_name "Seperti apa?"

    show player 5
    show old_mia 30
    mia "Cobalah sesuatu yang lucu, yang warnanya cantik!"

    show old_mia 31
    show player 14
    player_name "Baiklah, saya akan mencoba membuat yang lain..."

    show player 13
    show old_mia 30
    mia "Terima kasih banyak, {b}[firstname]{/b}."

    return

label mia_dialogue_mia_show_tattoo_pass:
    show old_mia 7 at right
    show player 2 at left
    player_name "Tentang seni tato yang Anda inginkan..."

    show player 13
    show old_mia 10
    mia "Oh! Apakah kamu memilikinya?!"

    show old_mia 7
    show player 14
    player_name "Ya!"

    show player 239_240 with dissolve
    player_name "Butuh beberapa saat bagi saya untuk membuatnya..."

    show player 386 with dissolve
    player_name "Ini dia!"

    show player 13
    show old_mia 29
    if player.location == L_school_scienceclassroom:
        show old_mial 1b at right
    with dissolve
    mia "wah!!!"

    show old_mia 30
    mia "Saya sangat MENYUKAINYA!"

    show old_mia 31
    show player 17
    player_name "Benar-benar?"

    show player 18
    show old_mia 30
    mia "Ya!"

    show old_mia 29
    mia "Cantik sekali..."

    show old_mia 31
    show player 14
    player_name "Keren! Saya senang Anda menyukainya."

    show player 13
    show old_mia 30
    mia "Kita harus {b}mengunjungi Sugar Tats{/b} dan melihat apakah mereka bisa membuatkannya untuk saya."

    show old_mia 7
    if player.location == L_school_scienceclassroom:
        show old_mial 1f
    with dissolve
    show player 12
    player_name "Sekarang?!"

    show player 5
    show old_mia 9
    mia "Jangan sekarang, bodoh!"

    show old_mia 10
    mia "Bagaimana kalau hari Sabtu?"

    show old_mia 7
    show player 10
    player_name "Oke, saya bisa {b}menemui Anda di sana pada hari Sabtu{/b}."

    show player 5
    show old_mia 10
    mia "Berjanjilah kamu akan menemuiku di sana {b}siang hari{/b}!"

    show old_mia 7
    show player 14
    player_name "Saya berjanji!"

    show player 13
    show old_mia 10
    mia "Oke, bagus. Aku tidak yakin aku bisa melakukannya sendiri, haha."

    mia "Sampai jumpa."

    hide player
    hide old_mia
    hide old_mial
    with dissolve
    return

label mia_dialogue_mia_get_tattoo:
    show old_mia 7 at right
    show player 12 at left
    player_name "Tentang tato itu..."

    show player 5
    show old_mia 12
    mia "Apakah kamu masih datang?"

    show old_mia 8
    show player 14
    player_name "Tentu saja!"

    show player 10
    player_name "Tapi kapan kamu ingin pergi?"

    show player 11
    show old_mia 12
    mia "Kamu sudah lupa?!"

    show old_mia 8
    show player 21
    player_name "Sepertinya aku sedang memikirkan banyak hal akhir-akhir ini..."

    show player 13
    show old_mia 9
    mia "Tidak apa-apa, haha."

    show old_mia 10
    mia "Aku ingin kamu {b}menemuiku pada hari Sabtu di salon tato, pada siang hari{/b}!"

    show old_mia 7
    show player 14
    player_name "Baiklah, aku akan memastikan untuk berada di sana bersamamu."

    show player 13
    show old_mia 10
    mia "Terima kasih banyak, {b}[firstname]{/b}."

    return

label mia_dialogue_church:
    show player 12
    player_name "Kapan ibumu pergi ke gereja?"

    show player 5
    show old_mia 12
    mia "{b}Pada akhir pekan di pagi hari{/b}."

    show old_mia 8
    show player 34
    player_name "Hmm..."

    show player 14
    player_name "Baiklah terima kasih."

    show player 13
    show old_mia 12
    mia "Apa yang akan kamu lakukan?!"

    show old_mia 8
    show player 12
    player_name "Saya belum sepenuhnya yakin, namun saya akan menghubungi Anda kembali jika saya menemukan caranya."

    show player 13
    show old_mia 12
    mia "Oke..."

    return

label mia_dialogue_art_sessions_intro:
    show player 10
    player_name "Hei, jadi uhh... {b}Nona Ross{/b} memintaku untuk datang berbicara denganmu."

    show player 11
    show old_mia 10
    mia "Benar-benar?"

    show player 10
    show old_mia 7
    player_name "Ya, dia ingin kamu menjadi rekanku untuk beberapa sesi seni pribadi."

    return

label mia_dialogue_art_sessions_stat_pass:
    show player 10
    player_name "Saya sangat ingin Anda datang membantu, {b}Mia{/b}."

    show player 5
    show old_mia 12
    mia "Anda akan melakukannya?"

    show old_mia 8
    show player 29 with dissolve
    player_name "Benar sekali."

    show player 3
    show old_mia 8b
    mia "Hmm..."

    show old_mia 9
    mia "Oke!"

    show player 13 with dissolve
    show old_mia 10
    mia "Aku akan datang untukmu, {b}[firstname]{/b}."

    show old_mia 7
    show player 14
    player_name "Manis! Terima kasih, {b}Mia{/b}!"

    show player 13
    show old_mia 9
    mia "Hehe, tidak masalah."

    show old_mia 7
    show player 14
    player_name "Jadi, sampai jumpa di sana?"

    show player 13
    show old_mia 10
    mia "Anda yakin!"

    return

label mia_dialogue_art_sessions_stat_fail:
    player_name "Dia cukup bersikeras bahwa itu pasti Anda."

    show player 11
    show old_mia 12
    mia "... Tapi aku bahkan tidak pandai seni."

    show player 10
    show old_mia 8
    player_name "Kamu tidak mungkin seburuk itu..."

    show player 11
    show old_mia 12
    mia "Percayalah, aku benar-benar jahat!"

    mia "Anda harus mencari orang lain."

    mia "Lagi pula, ibuku hanya akan mengatakan tidak."

    show player 10
    show old_mia 8
    player_name "Oh, baiklah kalau begitu."

    return

label mia_dialogue_homework_want_parents_back:
    show player 14
    player_name "Kalian ingin belajar bersama tentang apa?"

    show player 13
    show old_mia 12
    mia "Aku sedang tidak sanggup melakukannya saat ini."

    show old_mia 8
    show player 10
    player_name "Baiklah..."

    show player 5
    show old_mia 12
    mia "Maaf."

    mia "Aku hanya ingin orang tuaku kembali bersama."

    show old_mia 8
    show player 10
    player_name "Aku tahu."

    player_name "Beri tahu saya jika Anda membutuhkan bantuan saya."

    show player 5
    show old_mia 12
    mia "Terima kasih, {b}[firstname]{/b}."

    show old_mia 8
    return

label mia_dialogue_homework_intro:
    show player 14
    player_name "Kalian ingin belajar bersama tentang apa?"

    show player 13
    show old_mia 10
    mia "Kami akan mempelajari hal-hal yang berkaitan dengan {b}PR kelas bahasa Prancis{/b} terakhir. Apakah Anda sudah menyerahkan tugas itu?"

    show old_mia 7
    return

label mia_dialogue_homework_still_busy:
    show player 24
    player_name "Tidak, aku masih mengerjakannya."

    show player 13
    show old_mia 10
    mia "Nah, setelah selesai, {b}singgah ke rumah saya{/b}."

    hide old_mia
    hide old_mial
    with dissolve
    show player 5 with dissolve
    player_name "(Saya harus mencoba dan {b}menyelesaikan pekerjaan rumah bahasa Prancis saya{/b}, sehingga saya bisa belajar dengan {b}Mia{/b}. )"

    show player 4 with dissolve
    pause
    player_name "(Saya bertanya-tanya mengapa dia memilih saya untuk membantunya belajar.)"

    player_name "(Dia biasanya belajar dengan {b}Judith{/b}, dan dia sangat pandai dalam bahasa Prancis... )"

    player_name "(Saya tidak yakin bagaimana saya bisa membantunya.)"

    show player 13 with dissolve
    player_name "(Setidaknya kita bisa jalan-jalan, dan dia sangat manis...)"

    hide player with dissolve
    return

label mia_dialogue_homework_study:
    show player 14
    player_name "Saya menyerahkannya belum lama ini."

    show player 13
    show old_mia 10
    mia "Kalau ada waktu, {b}menyelinap ke kamarku di malam hari{/b}, supaya kita bisa belajar nanti."

    show old_mia 7
    show player 17
    player_name "Akan berhasil!"

    show player 13
    return

label mia_dialogue_study_repeat:
    show player 14
    player_name "Tentu saja!"

    scene mia_bedroom_closeup
    show old_mia 16 zorder 1 at Position (xpos = 680, ypos = 574)
    show player 141 zorder 0 at Position (xpos = 250, ypos = 578)
    with dissolve
    mia "Terima kasih telah menyelinap ke sini lagi."

    show old_mia 13
    show player 142
    player_name "Tidak terlalu sulit jika orang tua Anda terpaku pada TV."

    show player 143
    show old_mia 16
    mia "Ya, hanya itu yang membuat mereka tidak saling berteriak."

    mia "Mereka sangat suka menonton tayangan ulang."

    mia "Kadang-kadang saya menonton bersama mereka ketika saya selesai mengerjakan pekerjaan rumah."

    show old_mia 22
    mia "Namun sebagian besar waktu saya berdiam di sini... Lebih tenang."

    show old_mia 14
    show player 146
    player_name "Agak disayangkan orang tuamu tidak akur."

    show player 141
    show old_mia 18
    mia "... Ya."

    mia "Mungkin akan kembali seperti dulu."

    show old_mia 14
    pause
    show old_mia 16
    mia "Sebaiknya kau pergi sebelum orang tuaku memperhatikanmu."

    show old_mia 13
    show player 142
    player_name "Aku akan mampir lagi, oke?"

    show player 141
    show old_mia 15
    mia "Besar! Selamat malam {b}[firstname]{/b}!"

    show old_mia 13
    show player 142
    player_name "Selamat malam, {b}Mia{/b}."

    hide player
    hide old_mia
    with dissolve
    return

label mia_dialogue_study_first:
    show old_mia 7
    show player 21
    player_name "Menurutku kita harus belajar?"

    show old_mia 9
    show player 13
    mia "Tentu saja!"

    show old_mia 10
    mia "Kalau begitu, ayo lakukan itu."

    show player 11
    mia "Izinkan saya mengambil semua buku pelajaran dan menyiapkannya {b}di tempat tidur saya{/b}?"

    show old_mia 7
    show player 21
    player_name "Uh... Oke!"

    return

label mia_dialogue_study_want_parents_back:
    show player 12
    player_name "Apakah Anda ingin belajar bersama?"

    show player 5
    show old_mia 12
    mia "Aku sedang tidak sanggup melakukannya saat ini."

    show old_mia 8
    show player 10
    player_name "Baiklah..."

    show player 5
    show old_mia 12
    mia "Maaf."

    mia "Aku hanya ingin orang tuaku kembali bersama."

    show old_mia 8
    show player 10
    player_name "Aku tahu."

    player_name "Beri tahu saya jika Anda membutuhkan bantuan saya."

    show player 5
    show old_mia 12
    mia "Terima kasih, {b}[firstname]{/b}."

    show old_mia 8
    return

label mia_dialogue_mias_bedroom_leave:
    show old_mia 8
    show player 10
    player_name "Aku ingin sekali... Tapi ini sudah larut..."

    show old_mia 12
    show player 5
    mia "Oh oke..."

    mia "... Apakah kamu akan segera kembali?"

    show player 14
    show old_mia 8
    player_name "Ya. Saya akan melihat apa yang bisa saya lakukan!"

    show old_mia 12
    show player 1
    mia "Selamat malam..."

    return

label mia_dialogue_science_classroom_leave:
    show player 10
    player_name "Sebenarnya, sebaiknya aku kembali ke kelas."

    show player 5
    show old_mia 12
    mia "Oh, oke... Bicara lagi nanti!"

    show old_mia 8
    show player 14
    player_name "Sampai jumpa!"

    return

label mia_dialogue_mias_house_entrance_leave:
    show player 10
    player_name "Sebenarnya, aku ingat ada sesuatu yang harus kulakukan."

    show player 5
    show old_mia 12
    mia "Oh, oke... Bicara lagi nanti!"

    show old_mia 8
    show player 14
    player_name "Sampai jumpa!"

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
