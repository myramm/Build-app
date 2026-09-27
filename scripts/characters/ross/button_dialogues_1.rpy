label ross_button_dress_code:
    show anon f_worried:
        flip
    show ross a_sides:
        flip
    with dissolve
    anon "Hai {b}Nona Ross{/b}, saya berharap Anda dapat berbicara dengan {b}Ny. Smith{/b} tentang kebijakan aturan berpakaian yang baru..."

    ross f_confused "Dia menerapkan kebijakan aturan berpakaian yang baru?!"

    ross "T-tapi ini sekolah negeri!!"

    anon f_skeptical "Aku tahu, kan?!"

    anon f_worried @ f_skeptical "Ini konyol!"

    ross f_angry a_hip_angry "Saya harap dia tidak berencana memasukkan kalian para siswa ke dalam seragam jelek yang besar, karena saya tidak akan tahan!"

    ross "Anak-anak seusia Anda perlu mengekspresikan diri, jika tidak, hal itu dapat menghambat perkembangan Anda menjadi dewasa!"

    anon "Yah, sebenarnya tidak ada apa-apa tentang pakaian..."

    ross "Aku bersumpah, aku akan segera menuju ke sana dan-"

    pause
    ross f_confused a_hip "Tunggu sebentar, tidak ada batasan pakaian?"

    anon "Tidak, Bu..."

    anon "... Tapi itu melarang pewarna rambut dan saya pikir-"

    ross f_normal a_sides @ f_laugh "Yah, itu tidak terlalu buruk..."

    ross "Kenapa kamu begitu kesal, {b}[firstname]{/b}?"

    ross @ f_eyeroll "Kamu bahkan tidak mewarnai rambutmu..."

    anon @ a_rub f_tired "Y-ya, tapi-"

    ross "Fiuh, kamu benar-benar membuatku kesal sejenak!"

    anon "Saya khawatir tentang {b}Hawa{/b}."

    anon "Dia sangat menyukai rambut birunya dan-"

    ross "Oh, {b}Eve{/b} akan baik-baik saja, sayang."

    ross "Faktanya, Anda memberi tahu dia menurut saya dia terlihat jauh lebih baik dalam balutan warna pirang alami."

    anon f_skeptical "Y-ya, oke, tapi-"

    ross "Saya tidak tahu mengapa dia mengubahnya sejak awal..."

    anon "Bagaimana dengan kita, anak-anak, yang perlu mengekspresikan diri?"

    ross "Maaf, {b}[firstname]{/b}... Saya tidak mempertaruhkan pekerjaan saya dengan pewarna rambut."

    anon f_surprised "T-tapi-"

    ross "Masih banyak cara lain yang bisa dia lakukan untuk mengekspresikan dirinya."

    ross "Rok pendek yang bagus atau atasan berpotongan rendah, mungkin?"

    anon f_worried "{i}*Sigh*{/i} Menurutku {b}Eve{/b} tidak menyukai hal semacam itu..."

    ross "Tentu saja, sayang."

    ross "Dia hanya membutuhkan seseorang untuk membantu membangun kepercayaan dirinya."

    anon f_skeptical "Saya rasa..."

    hide anon with dissolve
    return

label button_ross_grab_clay:
    scene expression player.location.background_closeup
    show player 1f at right
    show old_ross 2 at left
    with dissolve
    ross "{b}Ambil sebongkah tanah liat{/b}, {b}[firstname]{/b}, agar kita dapat memulai."

    show player 2f
    show old_ross 1
    player_name "Ya, Bu."


    return

label button_ross_find_partner:
    scene expression player.location.background_closeup
    show player 2f at right
    show old_ross 1 at left
    with dissolve
    player_name "Hai, {b}Nona Ross{/b}. Anda siap untuk memulai?"

    show player 1f
    show old_ross 2
    ross "Halo, {b}[firstname]{/b}! Hanya tentang..."

    show old_ross 11 with dissolve
    ross "Sebenarnya aku ingin mendiskusikan sesuatu denganmu terlebih dahulu."

    show player 2f
    show old_ross 10
    player_name "Oh?"

    show old_ross 11
    show player 1f
    ross "Saya pikir kami harus mencarikan Anda pasangan untuk sesi ini, bagaimana menurut Anda?"

    show old_ross 10
    show player 10f
    player_name "Seorang mitra?"

    show old_ross 11
    show player 11f
    ross "Ya, seseorang untuk bekerja bersama Anda dan melontarkan ide-ide!"

    show old_ross 10
    show player 2f
    player_name "Tentu oke."

    player_name "Apakah Anda memikirkan seseorang?"

    show player 1f
    show old_ross 10b with dissolve
    ross "Hmm..."

    show old_ross 11 with dissolve
    ross "Nah, pemikiran awal saya adalah {b}Eve{/b}. Dia artis berbakat sama sepertimu..."

    ross "... Tapi aku ragu dia punya waktu untuk mempelajari semua pelajaran musiknya."

    show old_ross 10b with dissolve
    pause
    show old_ross 11 with dissolve
    ross "Apakah menurut Anda {b}Mia{/b} akan tertarik?"

    ross "Dia sungguh manis sekali, bukan?"

    show old_ross 10
    show player 2f
    player_name "Salah, ya. Saya kira."

    show player 1f
    show old_ross 11
    ross "Besar! Nah, kenapa kamu tidak bicara dengannya?"

    ross "Katakan padanya aku bilang untuk memasukkan pantat imutnya ke sini!"

    show player 11f
    show old_ross 10
    player_name "..."

    return

label button_ross_ask_mia_partner:
    scene expression player.location.background_closeup
    show player 1f at right
    show old_ross 2 at left
    with dissolve
    ross "{b}[firstname]{/b}, Anda kembali!"

    ross "Dimana {b}Mia{/b}?"

    show player 10f
    show old_ross 1
    player_name "Oh, uhh... Aku belum meyakinkannya."

    show player 11f
    show old_ross 2
    ross "Baiklah, lanjutkan, {b}[firstname]{/b}!"

    ross "Kita membutuhkan antusiasmenya jika kita ingin memenangkan hal ini!"

    return

label button_ross_mia_is_partner:
    scene expression player.location.background_closeup
    show player 1f zorder 1 at right
    show old_ross 2 at left
    show old_mia 7 zorder 0 at Position(xpos=0.65, ypos=1.0)
    with dissolve
    ross "Hei, pai manis!"

    show old_ross 1
    show old_mia 56 at Position(xpos=0.635, ypos=1.0) with dissolve
    mia "... Oh, um. H-halo."

    show old_ross 2
    show old_mia 55
    ross "Saya sangat senang, {b}[firstname]{/b} meyakinkan Anda untuk bergabung dengan kami!"

    show old_ross 1
    show old_mia 56
    mia "Hehe, iya... Dia bilang kalian sangat membutuhkan bantuanku?"

    show old_ross 2
    show old_mia 55
    ross "Kami pasti melakukannya!"

    show old_ross 1
    show player 2f
    show old_mia 8b at Position(xpos=0.65, ypos=1.0) with dissolve
    player_name "Jadi apakah kita siap untuk memulainya sekarang?"

    show player 1f
    show old_ross 11 with dissolve
    ross "Ya! Mengapa Anda berdua tidak mengeluarkan buku seni Anda dan duduk berseberangan."

    show player 2f
    show old_ross 10
    player_name "Oke."

    show old_mia 8
    show player 596f with dissolve
    mia "..."
    show old_mia 12
    mia "Hmm, pertanyaan..."

    show old_mia 8
    show old_ross 11
    ross "Ya sayang?"

    show old_mia 12
    show old_ross 10
    mia "Bagaimana jika saya tidak memiliki buku seni?"

    show old_mia 8
    show old_ross 25
    ross "Oh benar."

    show old_ross 25b
    ross "Biasanya aku akan memberimu salah satu dari itu..."

    show old_ross 25
    ross "... Tapi saya khawatir persediaan kami sudah habis."

    show old_ross 24
    show player 598f
    player_name "Itu menyebalkan!"

    show player 596f
    show old_mia 12b
    mia "Oh baiklah, itu bukan masalah besar. Lagipula aku tidak pandai menggambar..."

    show old_mia 10
    mia "Saya hanya akan menonton."

    show old_mia 7
    show old_ross 11
    ross "Omong kosong!"

    ross "Kami akan membelikanmu satu!"

    show old_ross 27 with dissolve
    ross "{b}[firstname]{/b}, kenapa kamu tidak bertanya pada {b}Eve{/b} apakah kita bisa meminjam salah satu miliknya."

    show old_ross 26
    show player 598f
    player_name "... Y-ya, oke!"

    show old_ross 27
    show player 596f
    ross "Lihat, {b}[firstname]{/b} untuk menyelamatkan!"

    show player 1f
    show old_ross 11
    with dissolve
    ross "Kami hanya akan tinggal di sini dan mengobrol dengan seorang gadis."

    show old_ross 13
    ross "Benar, pai manis?"

    show old_ross 12
    show old_mia 56 at Position(xpos=0.635, ypos=1.0) with dissolve
    mia "Hehe, oke..."

    show old_mia 55
    show player 2f
    player_name "Segera kembali."

    return

label button_ross_find_art_pad:
    scene expression player.location.background_closeup
    show old_ross 13 at left
    show old_mia 55 at Position(xpos=0.435, ypos=1.0)
    show player 1f at right
    with dissolve
    ross "... Tahukah kamu, {b}Mia{/b}. Aku pernah berteman dengan seorang gadis yang mirip denganmu!"

    show old_ross 12
    show old_mia 56
    mia "Benar-benar?"

    show old_ross 13
    show old_mia 55
    ross "Sangat! Namanya Starchild, dan kami biasa mengikuti band favorit kami di seluruh negeri."

    show old_ross 12
    show old_mia 12b at Position(xpos=0.45, ypos=1.0) with dissolve
    mia "Ya, kedengarannya cukup bagus!"

    show old_ross 13
    show old_mia 8b
    ross "Oh, benar!"

    ross "Gadis itu selalu mendapatkan obat terbaik!"

    show old_ross 11
    ross "... Dan sungguh pencium yang luar biasa! Dia bisa melakukan hal-hal dengan lidahnya yang akan-"

    show player 10f
    show old_ross 10
    show old_mia 55 at Position(xpos=0.435, ypos=1.0) with dissolve
    player_name "{i}*Ahem*{/i} Apakah saya mengganggu sesuatu?"

    show player 11f
    show old_mia 12f with dissolve
    mia "{b}[firstname]{/b}, Anda kembali!"

    show old_mia 12bf
    mia "Untunglah!"

    show old_mia 8bf
    show old_ross 11
    ross "Apakah kamu berhasil {b}mendapatkan art pad Eve{/b}?"

    show player 10f
    show old_ross 10
    player_name "Tidak, maaf. Saya masih mengerjakannya."

    show player 11f
    show old_ross 11
    ross "Cih, kalau begitu, ayolah! Kami sedang ngobrol cewek di sini..."

    show old_ross 10
    show player 10f
    player_name "... B-baiklah. Saya akan kembali."

    hide player with dissolve
    show old_mia 12f at Position(xpos=0.55, ypos=1.0) with dissolve

    mia "TIDAK! Tunggu! Tahan!"

    show old_mia 8f
    pause
    show old_ross 13 at Position(xpos=0.15, ypos=1.0) with dissolve
    ross "Sekarang dimana aku?"

    show old_ross 12
    show old_mia 8b with dissolve
    mia "..."
    show old_ross 13
    ross "Oh benar! Dia bisa melakukan hal-hal dengan lidahnya yang bisa membuat pelacur tersipu malu!"

    show old_ross 12
    show old_mia 56 at Position(xpos=0.535, ypos=1.0) with dissolve
    mia "... Ya ampun."

    return

label button_ross_found_art_pad:
    scene expression player.location.background_closeup
    show old_ross 46 at left
    show old_mia 55 at Position(xpos=0.435, ypos=1.0)
    show player 11f zorder 1 at right
    with dissolve
    ross "... Hmm, menurutku yang favoritku adalah {b}Praia do Abricó{/b}."

    show old_ross 11 with dissolve
    ross "Itu kembali ke rumah di Rio de Janeiro."

    show old_ross 10
    show old_mia 56
    mia "Oh, entahlah..."

    mia "... Saya rasa saya tidak cukup berani untuk pergi ke pantai telanjang."

    show old_ross 13
    show old_mia 55
    ross "Oh, tentu saja, kue manis!"

    ross "Tidak seorang pun boleh malu dengan tubuhnya. Bagaimanapun juga, bentuk manusia adalah sebuah karya seni..."

    show old_ross 13
    ross "... Terutama milikmu."

    ross "Kamu benar-benar cantik, {b}Mia{/b}!"

    show old_ross 12
    show old_mia 56
    mia "Wah, aku... Uhh..."

    show player 10f

    player_name "{i}*Ehem*{/i}"

    show player 11f
    show old_mia 12bf with dissolve
    mia "Oh, {b}[firstname]{/b}, syukurlah kamu kembali!"

    show old_mia 8b zorder 0 at Position(xpos=0.65, ypos=1.0) with dissolve
    show player 2f
    player_name "Kalian bersenang-senang?"

    show player 1f
    show old_ross 11
    ross "Kami bersenang-senang!"

    ross "Saya berasumsi Anda {b}mendapatkan art pad{/b}?"

    show old_ross 10
    show player 598f with dissolve
    player_name "Yup, saya mendapatkannya di sini."

    show player 596f
    show old_ross 11 with dissolve
    ross "Kerja bagus, {b}[firstname]{/b}!"

    ross "Kita harus memulainya sekarang."

    ross "Saya ingin Anda berdua duduk berseberangan."

    show old_ross 58 with dissolve
    ross "... Karena hari ini kalian akan menggambar satu sama lain menggunakan pensil dan kertas."

    show player 598f
    show old_ross 10 with dissolve
    player_name "Jadi kamu ingin aku menggambar {b}Mia{/b}?"

    show player 596f
    show old_ross 11
    ross "Itu benar dan {b}Mia{/b}, saya ingin kamu menggambar {b}[firstname]{/b}."

    show old_ross 10
    show old_mia 12b
    mia "saya akan mencoba..."

    show old_ross 13
    show old_mia 8b
    ross "Kamu terlalu menggemaskan, bukan?"

    show old_ross 12
    show old_mia 55 at Position(xpos=0.635, ypos=1.0) with dissolve
    ross "Jangan khawatir, tidak ada seni yang buruk!"

    show old_mia 56
    mia "... Jika kamu berkata begitu."

    show old_mia 55
    show old_ross 11
    ross "Sekarang mari kita mulai."


    scene location_school_art_cutscene06
    show text _ ("I always did enjoy art but drawing a live model was a totally different experience...") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("... I'm glad {b}Miss Ross{/b} had chosen {b}Mia{/b} as my partner for this.") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("She really was cute!") as caption with dissolve
    pause

    scene expression player.location.background_closeup
    show player 1 zorder 1 at left
    show old_mia 8b at right
    show old_ross 11f zorder 0 at Position(xpos=0.535, ypos=1.0)
    with fade
    ross "Bagus sekali, kalian berdua!"

    ross "Gambarnya sangat indah, {b}[firstname]{/b}!"


    show old_ross 28f at Position(xpos=0.435, ypos=1.0) with dissolve
    ross "Saya merasa sangat senang dengan peluang kami dalam kontes seni ini..."

    ross "Anda harus menunjukkan {b}Mia{/b}."

    show old_ross 12 at Position(xpos=0.35, ypos=1.0)
    show player 560
    with dissolve

    pause
    show old_mia 69
    mia "{i}*Terkesiap*{/i}"

    show old_mia 10
    mia "Wow! Ini sangat bagus!"

    show old_mia 7
    show old_ross 11
    ross "Bukan?"

    show old_ross 13
    ross "Ini hampir seindah aslinya!"

    show old_ross 13c
    ross "Bukankah begitu, {b}[firstname]{/b}?"

    show player 561
    show old_ross 12b
    player_name "Y-ya, hampir..."


    show player 560
    show old_ross 12
    show old_mia 56 with dissolve
    mia "Ah, terima kasih, {b}[firstname]{/b}."

    show old_mia 55
    show old_ross 13
    ross "Baiklah kalau begitu, mari kita lihat bagaimana kinerjamu {b}Mia{/b}?"

    show old_mia 59b with dissolve
    mia "Hmm, tidak. Tidak apa-apa. Saya lebih suka tidak melakukannya."

    show old_ross 11
    show old_mia 59d
    ross "Oh, mewah sekali! Jangan bermain terlalu keras untuk mendapatkannya!"

    ross "Ingat, tidak ada seni yang buruk..."

    show old_ross 10
    show old_mia 59e
    mia "... Oke."

    show old_mia 59c
    show old_ross 24

    ross "..."
    show old_mia 59
    mia "Sudah kubilang, aku tidak terlalu baik..."

    show old_mia 59c
    show old_ross 25
    ross "Ya tidak, itu... Menarik..."

    show old_ross 11
    ross "Pasti ada ruang untuk perbaikan."

    show player 561
    show old_ross 10
    player_name "Saya menyukainya, {b}Mia{/b}!"

    show player 560
    show old_mia 57
    mia "Anda melakukannya?"

    show player 561
    show old_mia 58
    player_name "Ya, itu sangat lucu!"


    show player 560
    show old_ross 11
    ross "Nah, sekarang lihat, {b}Mia{/b}. {b}[firstname]{/b} menyukainya!"

    show old_ross 10
    mia "..."
    show old_ross 11
    ross "Baiklah, menurutku sebaiknya kita hentikan saja hari ini."

    ross "Kami membuat kemajuan yang sangat bagus, kalian berdua!"

    show old_ross 58 at Position(xpos=0.41, ypos=1.0) with dissolve
    ross "Pastikan Anda berdua banyak istirahat dan jangan lupa melakukan meditasi yang saya ajarkan!"

    show old_ross 10 at Position(xpos=0.35, ypos=1.0) with dissolve
    show player 2
    with dissolve
    player_name "Baiklah, saya akan coba, {b}Nona Ross{/b}."

    player_name "Sampai jumpa, {b}Mia{/b}!"

    show player 1
    show old_mia 56 with dissolve
    mia "Sampai jumpa, {b}[firstname]{/b}."

    return

label button_ross_collage:
    scene expression player.location.background_closeup
    show player 2f zorder 1 at right
    show old_mia 2f zorder 0 at Position(xpos=0.55, ypos=1.0)
    with dissolve
    player_name "Anda siap untuk sesi berikutnya dengan {b}Nona Ross{/b}?"

    show player 1f
    show old_mia 6f
    mia "Ya, menurutku..."

    show player 10f
    show old_mia 2f
    player_name "Tampaknya kamu tidak begitu bersemangat mengenai hal itu."

    player_name "Saya pikir kamu menyukai seni?"

    show player 11f
    show old_mia 6f
    mia "Saya memang menyukai seni."

    mia "... Dan saya sangat suka melihat Anda dan {b}Nona Ross{/b} bekerja."

    show old_mia 6bf
    mia "Hanya saja..."

    show old_mia 6f
    mia "{b}Nona Ross{/b} membuatku merasa sedikit minder."

    show player 10f
    show old_mia 2f
    player_name "Dia melakukannya?"

    show player 11f
    show old_mia 6f
    mia "Dia sangat terbuka padaku, bukan begitu?"

    show player 2f
    show old_mia 2f
    player_name "Ya, tapi dia seperti itu pada semua orang."

    show player 1f
    show old_mia 6f
    mia "Apakah dia?"

    mia "Entahlah, dia menjalani kehidupan yang penuh petualangan, dan dia sangat penuh pengalaman..."

    show old_mia 6bf
    mia "Dia membuatku merasa sangat membosankan."

    show player 2f
    show old_mia 2f
    player_name "Menurutku kamu tidak membosankan, {b}Mia{/b}."

    show player 1f
    show old_mia 4f
    mia "Kamu tidak?"

    show old_mia 1f
    show player 2f
    player_name "Sama sekali tidak."

    player_name "Saya pikir Anda hanya perlu bersantai dan tetap berpikiran terbuka."

    player_name "Saya yakin {b}Nona Ross{/b} bisa mengajari kita banyak hal keren!"

    show old_mia 5f
    show player 1f
    mia "..."
    show old_mia 3f
    mia "Ya, mungkin kamu benar, {b}[firstname]{/b}!"

    show old_mia 4f
    mia "saya bisa-"

    show old_mia 1f
    show player 11f
    show old_ross 11 at left with dissolve

    ross "Itu murid favoritku!"

    show old_mia 8b at Position(xpos=0.65, ypos=1.0) with dissolve
    ross "Apa yang kalian berdua bicarakan?"

    show old_mia 55 at Position(xpos=0.635, ypos=1.0) with dissolve
    show player 10f
    player_name "Burung lovebird?"

    show old_mia 56
    show player 11f
    mia "Kami hanya ingin tahu tentang apa sesi hari ini?"

    show old_mia 55
    show old_ross 13
    ross "Langsung ke bisnis, ya?"

    ross "Dasar petasan kecil, aku menyukainya!"

    show old_ross 12
    mia "..."
    show old_ross 58 with dissolve
    ross "Hari ini kalian masing-masing akan membuat kolase!"

    show old_ross 10 with dissolve
    show old_mia 12b at Position(xpos=0.65, ypos=1.0) with dissolve
    mia "Kolase? Aku bahkan tidak tahu apa maksudnya..."

    show old_mia 8b
    show old_ross 27 with dissolve
    ross "Oh, mereka sangat menyenangkan! Anda akan menyukainya {b}Mia{/b}!"

    ross "Kami akan memotong gambar dari majalah dan merekatkannya untuk membuat karya seni."

    show old_ross 26
    show player 2f
    show old_mia 7
    player_name "Kedengarannya menyenangkan bagiku."

    show player 1f
    show old_mia 10
    mia "Ya, itu benar."

    show old_mia 7
    show old_ross 11 with dissolve
    ross "Baiklah, baiklah, saya punya semua yang kita perlukan di sini. Kami hanya kekurangan {b}semen karet{/b} dan {b}setumpuk besar majalah{/b}."

    ross "Mengapa kalian berdua tidak mencarikan kami beberapa?"

    show old_ross 10
    show player 2f
    player_name "Kita bisa melakukan itu, kan {b}Mia{/b}?"

    show player 1f
    show old_mia 10b
    mia "Sangat. Sebenarnya, menurutku ayahku punya semen karet di rumah."

    show old_mia 10
    mia "Aku akan mengambilnya!"

    hide old_mia with dissolve

    show old_ross 11
    ross "... Dan dia pergi!"

    ross "Saya kira itu berarti Anda bertanggung jawab untuk menemukan {b}majalah{/b}, {b}[firstname]{/b}."

    ross "Jika Anda dapat menemukan {b}tiga tumpukan majalah BESAR{/b}, saya rasa itu sudah cukup."

    show player 2f
    show old_ross 10
    player_name "Adakah yang tahu di mana saya bisa menemukannya?"

    show player 1f
    show old_ross 10b with dissolve
    ross "Hmm..."

    show old_ross 11
    ross "... Saya akan mulai dari {b}Perpustakaan{/b}. Mereka harus memiliki banyak pilihan untuk dipilih!"

    show player 2f
    show old_ross 10
    player_name "Baiklah, aku akan memeriksanya."

    return

label button_ross_find_magazines:
    scene expression player.location.background_closeup
    show player 2f zorder 1 at right
    show old_ross 10 at left
    with dissolve
    player_name "Di mana kamu bilang aku harus mencarinya lagi?"

    show player 1f
    show old_ross 11
    ross "Untuk {b}majalah{/b}?"

    ross "{b}Coba perpustakaannya{/b}."

    ross "Dan lihat apakah kamu dapat menemukan {b}tiga tumpukan majalah BESAR{/b}, oke?"

    if M_ross.get("talked with jane"):
        hide old_ross with dissolve
        show player 10 with dissolve
        player_name "{i}*Huh*{/i}"

        player_name "Perpustakaan tidak memiliki majalah apa pun."

        if M_ross.get("magazines remaining") == 3:
            player_name "Dan saya masih perlu mencari 3 majalah lagi."

        elif M_ross.get("magazines remaining") == 2:
            player_name "Dan saya masih perlu mencari 2 majalah lagi."

        elif M_ross.get("magazines remaining") == 1:
            player_name "Dan saya masih perlu mencari 1 majalah lagi."

        player_name "Saya kira saya harus {b}melihat-lihat di sekolah{/b}."

    else:
        show old_ross 10
        show player 2f
        player_name "{b}Perpustakaan{/b}, mengerti!"

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
