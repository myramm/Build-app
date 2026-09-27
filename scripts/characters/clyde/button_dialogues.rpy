label button_clyde_pink_beaver:
    scene expression player.location.background_blur with None
    show player 14f at right
    show clyde 1 at left
    if M_clyde.get("cletus"):
        show clyde_hat at left
    player_name "Hei, tentang berang-berang yang kamu inginkan."

    show player 13f
    show clyde 2
    clyde "Ya?"

    show clyde 1
    show player 239_240f
    pause
    show player 709f
    player_name "Apakah ini dia?"

    show player 708f
    show clyde 30
    clyde "!!!"
    show clyde 4 with dissolve
    clyde "Baiklah, olesi pantatku dan panggilkan aku biskuit, kamu benar-benar mengerti!"

    show clyde 3
    show player 709f
    player_name "Saya pikir ini mungkin saja."

    show clyde 34
    show player 13f
    with dissolve
    pause
    show clyde 35
    clyde "Bagaimana kamu bisa memenangkan hal ini?!"

    show clyde 33 with dissolve
    clyde "Pekan raya ini bahkan belum akan diadakan selama 2 bulan lagi!"

    show clyde 32
    show player 12f
    player_name "Saya membelinya di pusat perbelanjaan, {b}Clyde{/b}."

    show player 5f
    show clyde 2 with dissolve
    clyde "Mal?"

    clyde "Ah, tembak."

    clyde "Aku belum pernah ke sana."

    clyde "Ke mana anjing itu lari sekarang?"

    clyde "Ayo, gadis!"

    show clyde 1
    pause
    show player 10f
    player_name "Tunggu. Kamu belum pernah ke mal?"

    show player 5f
    show clyde 9 with dissolve
    clyde "Tidak, tuan."

    show clyde 3
    show player 10f
    player_name "Di mana Anda membeli bahan makanan?"

    show player 5f
    show clyde 4
    clyde "Pfft, kalian penduduk kota dan toko belanjaan kalian..."

    clyde "Aku tidak akan membayar siapa pun untuk barang-barang yang gratis di sini, di hutan!"

    show clyde 3
    show player 10f
    player_name "... Hah?"

    show player 5f
    show clyde 9 with dissolve
    clyde "Aku berburu makanan fer mah, sobat."

    show clyde 4 with dissolve
    clyde "Ngomong-ngomong, aku punya semangkuk besar tupai yang direbus di gubuk mah."

    clyde "Kamu harus datang untuk makan malam!"

    show clyde 3
    show player 12f
    player_name "Eh, tidak, terima kasih."

    show player 5f
    pig "{i}*Memperas*{/i}"

    show clyde 4
    clyde "Itu dia!"

    if M_clyde.get("cletus"):
        show clyde_hat down
    show clyde 36
    with dissolve
    clyde "Kemana saja kamu gadis?!"

    if M_clyde.get("cletus"):
        show clyde_hat
    show clyde 38
    with dissolve
    pig "{i}*Oink*{/i}"

    show clyde 37
    clyde "Lihat apa yang {b}[firstname]{/b} bawakan untukmu!"

    show clyde 38
    pig "{i}*PEREMPUAN*{/i}"

    show clyde 37
    clyde "Hehehe, lihat betapa bahagianya dia!"

    if M_clyde.get("cletus"):
        show clyde_hat down
    show clyde 36
    with dissolve
    clyde "Pergilah dan bersenang-senanglah sekarang!"

    if M_clyde.get("cletus"):
        show clyde_hat
    show clyde 3
    with dissolve
    pig "{i}*Mendengus*{/i}"

    pause
    show clyde 4
    clyde "Sekarang dia adalah seekor anjing yang bahagia."

    clyde "Baiklah sobat..."

    show clyde 9 with dissolve
    clyde "Aku harus membalas budimu entah bagaimana caranya."

    show clyde 3 with dissolve
    show player 12f
    player_name "Jangan khawatir tentang hal itu."

    player_name "Anggap saja itu sebuah hadiah."

    show player 5f
    show clyde 4
    clyde "Sekarang tunggu sebentar."

    show clyde 1 with dissolve
    pause
    show clyde 9 with dissolve
    clyde "Oh!"

    clyde "Saya mendapatkan barangnya!"

    hide clyde
    hide clyde_hat
    with dissolve
    show player 10f
    player_name "Kemana kamu pergi?!"

    show player 5f
    clyde "Tunggu di sana!"

    pause
    clyde "Jangan gerakkan satu otot pun!"

    show player 25f
    player_name "Ya ampun."

    player_name "B-benarkah, tidak apa-apa..."

    player_name "aku tidak perlu-"

    show player 11f
    show clyde 40 at left
    if M_clyde.get("cletus"):
        show clyde_hat at left
    with dissolve
    clyde "Coba lihat!"

    show clyde 39
    if player.has_item("mysterious_statue_1"):
        show player 23f
        player_name "!!!"
        show player 30f
        if M_clyde.get("cletus"):
            player_name "{b}Cletus{/b}, kukira kamu bilang kamu tidak tahu apa-apa tentang patung kakekmu!"

        else:
            player_name "{b}Clyde{/b}, kukira kamu bilang kamu tidak tahu apa-apa tentang patung kakekmu!"

        show player 90f
        show clyde 40
        clyde "Oh benar."

        clyde "Aku memang mengatakan itu, bukan?"

        show clyde 39
        pause
        show clyde 11 with dissolve
        clyde "Yah, aku berbohong."

        show clyde 12
        show player 12f
        player_name "Mengapa?!"

        show player 90f
    else:

        player_name "!!!"
        show player 30f
        player_name "Apa itu?"

        show player 5f
        show clyde 40
        clyde "Ya, dulunya itu milik kakekku."

        show clyde 39
        show player 10f
        player_name "Kakekmu?!"

        show player 5f
        show clyde 9 with dissolve
        clyde "Itu benar!"

        clyde "Ole {b}Jebadiah Delmont{/b} sendiri!"

        show clyde 3
        pause
        player_name "..."
        show clyde 2 with dissolve
        clyde "Anda belum pernah mendengar tentang {b}Jebadiah Delmont{/b}?"

        show clyde 1
        show player 10f
        player_name "Tidak?"

        show player 5f
        show clyde 2
        clyde "{i}*Huh*{/i} Astaga."

        show clyde 4 with dissolve
        clyde "Dia dulu sangat terkenal di sekitar daerah ini karena sapi-sapinya dan susunya yang lezat!"

        clyde "Dia memenangkan segala macam kontes."

        show clyde 3
        show player 10f
        player_name "Dia adalah seorang peternak sapi perah?"

        show player 5f
        show clyde 4
        clyde "Yah, dia tidak hanya melakukan peternakan sapi perah."

        clyde "Dia memiliki segala jenis binatang."

        show clyde 9 with dissolve
        clyde "Anda seharusnya melihat telur ayam yang dia bawa ke pameran."

        clyde "Mereka sebesar bola sepak!"

        show clyde 3 with dissolve
        show player 10f
        player_name "Sungguh?"

        show player 5f
        show clyde 4
        clyde "Heh, ya sobat!"

        show clyde 3
        pause
        show player 17f
        player_name "Kedengarannya luar biasa!"

        show player 14f
        player_name "Ceritakan lebih banyak kepada saya."

        show player 13f
        show clyde 11 with dissolve
        clyde "Oh tidak. aku uhh..."

        clyde "{i}*Ahem*{/i} Aku benar-benar tidak ingin membahas semua itu..."

        show clyde 12
        show player 10f
        player_name "Hah, kenapa tidak?"

        show player 5f
    show clyde 11
    clyde "Begini kawan, kakekku bukanlah kebanggaan {b}keluarga Delmont{/b}..."

    clyde "Kami tidak suka membicarakannya!"

    show clyde 12
    show player 10f
    player_name "Kenapa?"

    show player 5f
    show clyde 2 with dissolve
    clyde "{i}*Sigh*{/i} Anggap saja ole {b}Jebadiah{/b} sedikit, tersentuh di kepala, oke?"

    show clyde 1
    show player 10f
    player_name "Tersentuh di kepala?"

    show player 5f
    show clyde 2
    clyde "Kamu tahu."

    clyde "Dia punya beberapa sekrup yang lepas."

    show clyde 1
    show player 10f
    player_name "Uhh..."

    show player 5f
    show clyde 9 with dissolve
    clyde "Rodanya berputar tetapi hamster itu mati."

    show clyde 3 with dissolve
    show player 10f
    player_name "saya tidak..."

    show player 5f
    show clyde 4
    clyde "Dia kekurangan beberapa kartu untuk mencapai setumpuk penuh."

    show clyde 3
    show player 12f
    player_name "Apa yang kamu bicarakan?!"

    show player 5f
    show clyde 26 with dissolve
    clyde "Cih, dia lebih gila dari porta-potty di festival kacang, oke?!"

    show clyde 25
    show player 12f
    player_name "Maksudmu dia gila?"

    show player 5f
    show clyde 26
    clyde "Itu yang aku coba sampaikan padamu..."

    show clyde 25
    show player 10f
    player_name "Oh."

    show player 5f
    show clyde 2
    clyde "Ya."

    clyde "Mama bilang dia selalu sedikit eksentrik."

    clyde "Orang-orang yang berteriak biasa memanggilnya penyihir dusun."

    show clyde 1
    show player 10f
    player_name "Dia adalah seorang penyihir?"

    show player 5f
    show clyde 2
    clyde "Ya, tapi dia bukan orang yang baik."

    clyde "Aku ingat, dia pernah mencoba mengubahku menjadi katak, karena aku sudah pergi dan kepalaku tersangkut di tangga."

    show clyde 1
    show player 10f
    player_name "Kepalamu tersangkut di tangga?!"

    show player 5f
    show clyde 2
    clyde "Kakakku bilang ada leprechaun yang tinggal di bawah tangga dan aku ingin bertemu dengannya."

    show clyde 1
    show player 17f
    player_name "Pfft, hahaha!"

    show player 13f
    show clyde 2
    clyde "Bagaimanapun, mantranya tidak berhasil."

    show clyde 11 with dissolve
    clyde "Jadi Mama harus mengolesiku dengan lemak bacon dan mengeluarkanku."

    show clyde 12
    show player 17f
    player_name "Haha!"

    show player 13f
    show clyde 4
    clyde "Lalu suatu saat, aku gagal di kelas dua..."

    clyde "... Dan kakek, katanya, \"Jangan khawatir sedikit pun {b}Clyde{/b}. Kakek akan segera memperbaikinya untukmu.\""

    show clyde 3
    pause
    show player 14f
    player_name "Oke, jadi apa yang terjadi?"

    show player 13f
    show clyde 2 with dissolve
    clyde "Yah, aku tidak tahu pasti. Mereka menemukannya di gedung sekolah, di tengah malam, telanjang bulat dan berlumuran darah ayam."

    show clyde 1
    show player 23f
    player_name "Darah ayam?!"

    show player 11f
    show clyde 2
    clyde "Ya, dia bilang dia sedang melakukan semacam ritual untuk membantuku bersekolah."

    clyde "Tampaknya dia adalah orang yang berteriak-teriak, berteriak-teriak, dan terus-terusan."

    show clyde 1
    show player 10f
    player_name "Ya, dia memang terdengar sedikit gila, {b}Clyde{/b}."

    show player 12f
    show clyde 2
    clyde "Ya, menurutku memang begitu."

    clyde "Tapi dia adalah orang yang manis."

    clyde "Sayang sekali semua roh jahat marah padanya."

    show clyde 1
    show player 10f
    player_name "Roh jahat?"

    show player 11f
    show clyde 2
    clyde "Ya, dia memberitahuku semuanya tepat setelah dia memecahkan patung ini dan menyembunyikan potongannya."

    clyde "Katanya mereka akan datang untuknya dan dia ingin dia aman."

    show clyde 1
    show player 10f
    player_name "Dia?"

    show player 5f
    show clyde 40 with dissolve
    clyde "Wanita di dalam patung, tentu saja!"

    clyde "Dia benar-benar sedih karena menyembunyikannya."

    clyde "Bagaimanapun, dia adalah jimat keberuntungannya."

    show clyde 39
    show player 12f
    player_name "Aneh."

    show player 5f
    show clyde 9 with dissolve
    clyde "Lalu kami memergokinya sedang berzina dengan ternaknya dan Mama mengirimnya ke rumah sakit jiwa."

    show clyde 3 with dissolve
    show player 22f
    player_name "!!!" with hpunch
    show player 23f
    player_name "Maksudmu dia-"

    player_name "A-dengan binatang?!"

    show player 37f
    show clyde 11
    with dissolve
    clyde "{i}*Sigh*{/i} Yup, menangis seperti bayi juga."

    clyde "Roh-roh itu pasti telah berbuat banyak padanya, kawan yang malang."

    show clyde 12
    show player 10f with dissolve
    player_name "Jadi uhh..."

    player_name "... Apakah kakekmu masih tinggal di rumah sakit jiwa?"

    show player 5f
    show clyde 2 with dissolve
    clyde "Ah, tidak."

    clyde "Sekitar dua minggu setelah Mama mengirimnya ke sana, kamarnya terbakar dan dia terbakar di dalamnya."

    show clyde 1
    show player 24f
    player_name "Yesus..."

    show clyde 2
    clyde "Mereka tidak yakin bagaimana api mulai terjadi tetapi saya rasa mereka akhirnya berhasil menangkapnya."

    show clyde 1
    player_name "aku bahkan tidak..."

    player_name "..."
    show clyde 30
    clyde "Ya, itu sungguh menyedihkan..."

    show clyde 29
    pause
    show player 11f
    show clyde 2
    clyde "Bagaimanapun!"

    show player 5f
    show clyde 40 with dissolve
    clyde "Kurasa dia tidak keberatan aku memberimu potongan patung ini."

    clyde "Sampai jumpa saat Anda membantu saya dan semuanya."

    clyde "Siapa tahu bisa membawa keberuntungan juga."

    show clyde 39
    show player 10f
    player_name "B-benar."

    player_name "Terima kasih, saya rasa..."

    show player 715f
    show clyde 9
    with dissolve
    clyde "Jangan sebutkan itu, sobat!"

    show player 5f with dissolve
    clyde "Sekarang, permisi."

    clyde "Saya ingin melihat anjing saya memberikan apa yang diberikan kepada berang-berang itu!"

    hide clyde
    hide clyde_hat
    with dissolve
    clyde "Hehehe."

    show player 239_240f with dissolve
    pause
    show player 715f with dissolve
    player_name "( Anda tahu, ini sebenarnya menjelaskan banyak hal tentang {b}Clyde{/b} dan mengapa dia seperti itu... )"

    pause
    player_name "(Saya kira saya harus memperhatikan bagian lain dari patung ini.)"

    hide player with dissolve
    return

label button_clyde_mysterious_statue_1:
    scene expression player.location.background_blur with None
    show player 239_240f at right
    show clyde 1 at left
    if M_clyde.get("cletus"):
        show clyde_hat at left
    pause
    show player 688cf
    player_name "Anda tahu sesuatu tentang {b}Clyde{/b} ini?"

    show player 688bf
    show clyde 30
    clyde "{i}*Terkesiap*{/i} Di mana kamu menemukannya?!"

    show clyde 29
    show player 688cf
    player_name "Itu terkubur di bawah rumah teman saya."

    show player 688bf
    pause
    show player 688cf
    player_name "Nama {b}Delmont{/b} terukir di bagian bawah."

    show player 688bf
    show clyde 2
    clyde "Ya."

    show clyde 4 with dissolve
    clyde "Itu bagian dari jimat keberuntungan kakekku."

    show clyde 3
    show player 688cf
    player_name "Kakek?"

    player_name "Maksudmu kakekmu?"

    show player 13f with dissolve
    show clyde 4
    clyde "Eh ya, {b}Jebadiah Delmont{/b}."

    clyde "Dia sangat terkenal di wilayah ini bertahun-tahun yang lalu karena susu yang dihasilkan sapi-sapinya."

    show clyde 3
    show player 10f
    player_name "Susu sapi?"

    show player 5f
    clyde "Mmhmm."

    show clyde 4
    clyde "Enak sekali!"

    clyde "Memenangkan banyak kontes dengannya."

    show clyde 3
    show player 14f
    player_name "Itu cukup keren."

    show player 13f
    show clyde 4
    clyde "Dia juga punya beberapa telur ayam yang luar biasa."

    clyde "Mereka sebesar bola sepak!"

    show clyde 3
    pause
    show player 12f
    player_name "Benar..."

    show player 5f
    pause
    show player 10f
    player_name "Jadi uhh..."

    player_name "Tahukah Anda di mana sisa patung ini berada?"

    show player 5f
    show clyde 11 with dissolve
    clyde "Tidak!"

    show clyde 12
    pause
    show player 10f
    player_name "Oh, karena aku hanya berpikir-"

    show player 5f
    show clyde 9 with dissolve
    clyde "Maaf kawan, tidak bisa membantumu!"

    clyde "Aku tidak tahu jongkok!"

    show clyde 3 with dissolve
    show player 10f
    player_name "Baiklah..."

    show player 24f
    player_name "Terima kasih, kurasa."

    show player 5f
    show clyde 1 with dissolve
    return

label button_clyde_mysterious_statue_2:
    scene expression player.location.background_blur with None
    show player 239_240f at right
    show clyde 1 at left
    if M_clyde.get("cletus"):
        show clyde_hat at left
    pause
    show player 715bf with dissolve
    player_name "Adakah yang tahu di mana saya bisa menemukan lebih banyak patung ini?"

    show player 715cf
    show clyde 2
    clyde "Emm, tidak juga."

    clyde "Kakekku, potongan terakhir itu mungkin akan {b}menemukanmu{/b}."

    show clyde 1
    show player 10f with dissolve
    player_name "Apa maksudmu?"

    show player 5f
    show clyde 2
    clyde "Ya, sepertinya aku akan segera {b}menemukan tempat nyaman yang bagus untuk bersantai{/b}..."

    clyde "... {b}di suatu tempat dekat pantai, mungkin{/b}."

    show clyde 1
    pause
    show clyde 2
    clyde "Saya yakin {b}kepala itu akan muncul dengan sendirinya{/b}."

    show clyde 1
    show player 10f with dissolve
    player_name "Eh, benar..."

    player_name "Terima kasih. Saya rasa..."

    show player 5f
    show clyde 9 with dissolve
    clyde "Tidak masalah, sobat."

    show clyde 1 with dissolve
    return


label button_clyde_your_dog:
    scene expression player.location.background_blur with None
    show player 10f at right
    show clyde 1 at left
    if M_clyde.get("cletus"):
        show clyde_hat at left
    player_name "Jadi, tentang anjingmu..."

    show player 5f
    show clyde 4 with dissolve
    clyde "Ah ya, dia gadis yang baik, bukan?"

    show clyde 3
    show player 10f
    player_name "Oke, tentu saja."

    show player 12f
    player_name "Kamu sadar dia bukan anjing, kan?"

    show player 5f
    show clyde 4
    clyde "Anjing terbaik yang pernah saya miliki!"

    show clyde 3
    show player 24f
    player_name "{i}*Huh*{/i}"

    show player 5f
    show clyde 4
    clyde "Itu sebabnya aku berlatih keras, untuk memenangkan salah satu {b}boneka berang-berang{/b} di pekan raya."

    show clyde 3
    show player 12f
    player_name "Ya, Anda menyebutkan itu."

    show player 10f
    player_name "Mengapa kamu tidak membelikannya saja?"

    show player 5f
    show clyde 9 with dissolve
    clyde "Psh, sekarang kamu bicara gila..."

    clyde "Bagaimana menurut Anda {b}Berang-berang merah muda{/b} hanya tumbuh di pohon atau apa saja?"

    show clyde 3 with dissolve
    show player 10f
    player_name "Apakah warna itu penting?"

    show player 5f
    show clyde 4
    clyde "Heck ya itu penting!"

    clyde "{b}Berang-berang merah muda{/b} adalah berang-berang terbaik."

    show clyde 9 with dissolve
    clyde "Semua orang tahu itu!"

    show clyde 3 with dissolve
    show player 402f
    player_name "... Benar."

    show player 10f
    player_name "Oke, semoga sukses dengan semuanya, saya kira..."

    show player 5f
    show clyde 4
    clyde "\"Keberuntungan\" adalah nama tengahku, saudara."

    show clyde 3
    pause
    show clyde 2 with dissolve
    clyde "Sebenarnya itu Kornelius."

    show clyde 1
    show player 12f
    player_name "Hah?"

    show player 5f
    show clyde 2
    if M_clyde.get("cletus"):
        clyde "{b}Cletus Cornelius Delmont{/b}."

    else:
        clyde "{b}Clyde Cornelius Delmont{/b}."

    show clyde 1
    show player 10f
    player_name "Nama tengahmu Cornelius?"

    show player 5f
    show clyde 9 with dissolve
    clyde "Ya sobat."

    clyde "Seperti pencari rusa di pertunjukan rusa kutub."

    show clyde 4
    clyde "Kamu lihat yang pertama?!"

    show clyde 3
    show player 10f
    player_name "Saya kira tidak demikian..."

    show player 5f
    show clyde 4
    clyde "Maaan, bagus sekali!"

    show clyde 3
    show player 10f
    player_name "Kamu pria yang aneh, {b}Clyde{/b}."

    show player 5f
    show clyde 4
    clyde "Eh ya!"

    show clyde 1 with dissolve
    return

label button_clyde_roxxy_get_evidence_intro:
    scene expression player.location.background_blur
    show clyde 1 at left
    show player 12f at right
    with dissolve
    player_name "Kita perlu membicarakan situasi ini dengan {b}Crystal{/b}."

    show player 5f
    show clyde 22
    clyde "Saya lebih suka tidak..."

    show clyde 21
    show player 10f
    player_name "{b}Clyde{/b}, mereka akan mengirimnya ke penjara dan mengambil trailernya!"

    show player 5f
    show clyde 26
    clyde "Lihat di sini! Kamu pikir aku tidak tahu itu!"

    clyde "Aku merasa tidak enak tapi tidak ada yang bisa kulakukan untuk menghentikannya!"

    show clyde 25
    show player 12f
    player_name "Anda bisa menyerahkan diri..."

    show player 5f
    show clyde 22
    clyde "Ya benar..."

    clyde "Lalu kami berdua akan berakhir di balik jeruji besi!"

    show clyde 21
    show player 10f
    player_name "Tidak jika Anda memberi tahu mereka bahwa {b}Crystal{/b} tidak tahu Anda menyembunyikan narkoba di sana."

    show player 5f
    clyde "..."
    show clyde 2
    clyde "... Dan mengapa saya melakukan itu?"

    show clyde 1
    show player 12f
    player_name "... Karena itu adalah hal yang benar untuk dilakukan!"

    show player 90f
    show clyde 2
    clyde "Pfft."

    clyde "Saya tidak bisa pergi ke penjara!"

    clyde "Pria tampan sepertiku, hewan-hewan itu akan memakanku hidup-hidup di dere."

    show clyde 1
    return

label button_clyde_roxxy_get_evidence_about_roxxy_pass:
    scene expression player.location.background_blur
    show player 90f at right
    show clyde 1 at left
    clyde "..."
    show player 10f
    player_name "Lihat, kawan. Dia jatuh cinta padamu karena dia keluargamu."

    player_name "... Tapi ini jauh lebih buruk dari yang dia kira!"

    player_name "Dia akan pergi untuk waktu yang lama dan {b}Roxxy{/b} akan kehilangan ibu dan rumahnya."

    show player 12f
    player_name "{b}Roxxy{/b} tidak melakukan apa pun sehingga pantas mendapatkannya!"

    show player 5f
    show clyde 21
    clyde "..."
    show clyde 22
    clyde "... Aduh, sial! Anda benar."

    clyde "{b}Roxanne{/b} seharusnya tidak perlu menderita karena aku..."

    clyde "... Tapi aku tidak akan kembali ke penjara! ... Tidak tuan!"

    show clyde 21
    player_name "..."
    show player 14f
    player_name "Bagaimana jika Anda mengirimkan pengakuan Anda melalui surat?"

    player_name "Beritahu mereka tentang gubuk Anda dan biarkan mereka datang mencari buktinya."

    player_name "Jika Anda melakukannya dengan benar, Anda bisa pergi jauh sebelum mereka mulai mencari Anda."

    show player 13f
    clyde "..."
    show clyde 22
    clyde "Saya kira saya bisa kembali berteriak..."

    clyde "Mereka tidak akan pernah menemukanku di sana."

    clyde "... Tapi aku pasti akan merindukan {b}Bibi Crystal{/b}..."

    show clyde 21
    show player 10f
    player_name "Anda akan menyelamatkannya dari penjara, kawan."

    show player 5f
    show clyde 22
    clyde "Hmm, menurutku kamu punya rencana bagus."

    show player 13f
    clyde "Jadi saya melakukan ini dan dia bebas dari hukuman?"

    show clyde 21
    show player 12f
    player_name "... Kami masih harus memberikan uang jaminan untuknya tapi ini awal yang baik."

    show player 5f
    show clyde 22
    clyde "Berapa banyak uang yang Anda butuhkan?"

    show clyde 21
    show player 12f
    player_name "Lima puluh ribu dolar..."

    show player 5f
    show clyde 2
    clyde "... Hah."

    clyde "Yah, aku bisa melakukan itu!"

    show clyde 1
    show player 10f
    player_name "What?!" with hpunch
    player_name "Kamu tidak bisa serius..."

    player_name "Anda punya lima puluh ribu dolar tergeletak di suatu tempat?"

    show player 11f
    show clyde 2
    clyde "Tidak tepat."

    show clyde 4 with dissolve
    clyde "... Tapi aku mendapat kekacauan dari sabu itu."

    clyde "Saya kira, cukup untuk membayar seratus ribu dolar kepada pembeli yang tepat."

    show clyde 3
    show player 10f
    player_name "Itu gila!"

    player_name "Bisakah Anda benar-benar menjualnya?"

    show player 5f
    show clyde 4
    clyde "Pfft! Ayo sobat..."

    clyde "Tidak tahukah kamu dengan siapa kamu bicara?"

    clyde "Saya bisa menjual es loli saus tomat kepada seorang gadis yang mengenakan sarung tangan putih!"

    show clyde 3
    show player 11f
    player_name "..."
    show player 12f
    player_name "... es loli kecap?"

    show player 5f
    show clyde 9 with dissolve
    clyde "Ya, sobat!"

    show clyde 3 with dissolve
    show player 14f
    player_name "... Kapan kamu bisa melakukannya?"

    show player 13f
    show clyde 4
    clyde "Hmm, aku harus menelpon mah pembeli."

    clyde "... Tapi sebentar lagi, kurasa."

    show clyde 3
    show player 14f
    player_name "Aku akan memberitahu {b}Roxxy{/b} kabar baiknya!"

    hide player
    hide clyde
    with dissolve
    return

label button_clyde_roxxy_get_evidence_about_roxxy_fail:
    scene expression player.location.background_blur
    show clyde 1 at left
    show player 12f at right
    player_name "Anda seorang pengecut!"

    show player 90f
    show clyde 26
    clyde "Hei sekarang, jangan panggil aku bukan pengecut!"

    clyde "Anda tidak tahu bagaimana rasanya di penjara oleh orang seperti saya!"

    clyde "Aku belum pernah ke sana sekali pun dan aku akan terkutuk jika aku kembali!"

    show clyde 25
    show player 15f
    player_name "Terserah... PENGECUT!"

    show player 16f
    show clyde 26
    clyde "Persetan denganmu!"

    clyde "Aku tidak perlu mengambil ini!"

    hide clyde
    hide player
    with dissolve
    return

label button_clyde_roxxy_get_evidence_nevermind:
    show player 12f
    player_name "Ah, lupakan saja!"

    show player 90f
    show clyde 22
    clyde "Ya, itulah yang saya rencanakan!"

    clyde "Menurutku, ada banyak sekali yang lupa di dasar kaleng bir ini!"

    hide clyde
    hide player
    with dissolve
    return

label button_clyde_roxxy_selling_meth_ask_roxxy:
    scene expression player.location.background_blur
    show clyde 1 at left
    show player 10f at right
    with dissolve
    player_name "Kapan Anda bisa menjual sabu itu?"

    show player 5f
    show clyde 2
    clyde "Pegang kudamu, sobat!"

    clyde "Hal-hal ini membutuhkan waktu."

    show clyde 1
    player_name "..."
    show clyde 2
    clyde "Lanjutkan saja dan beri tahu sepupu manisku bahwa {b}Clyde{/b} akan mengurus semuanya!"

    show clyde 1
    show player 14f
    player_name "... Benar."

    hide player
    hide clyde
    with dissolve
    return

label button_clyde_roxxy_selling_meth:
    scene expression player.location.background_blur
    show clyde 3 at left
    show player 10f at right
    player_name "Anda sudah menghubungi pembeli Anda?"

    show player 5f
    show clyde 4 with dissolve
    clyde "Ya, sobat!"

    show player 13f
    clyde "Aku sedang berusaha membuat kesepakatan yang mematikan di sini!"

    show clyde 3
    show player 12f
    player_name "{b}Roxxy{/b} bilang kamu belum pernah menjual sabu sebelumnya!"

    show player 90f
    show clyde 26 with dissolve
    clyde "Apa?!"

    clyde "Dia tidak tahu apa-apa!"

    clyde "Saya telah mengikuti banyak penawaran di sini!"

    show clyde 25
    show player 12f
    player_name "Anda sebenarnya pernah berurusan dengan pembeli sebelumnya?"

    show player 5f
    show clyde 1
    clyde "..."
    show clyde 22
    clyde "Ya, saya menonton {b}Bibi Crystal{/b} melakukannya ratusan kali!"

    show clyde 1
    show player 37f with dissolve
    player_name "..."
    player_name "{i}*Huh*{/i} Aku ikut denganmu."

    show player 90f with dissolve
    show clyde 2
    clyde "Hah?"

    clyde "Apa yang Anda ketahui tentang menjual narkoba?"

    show clyde 1
    show player 12f
    player_name "Bukan apa-apa."

    player_name "... Tapi saya mengenal Anda, dan Anda jelas tidak cukup kompeten untuk melakukan ini sendirian."

    show player 90f
    show clyde 22
    clyde "Ya, bukan itu... Tunggu sebentar, apa maksudnya \"campito\"?!"

    show clyde 1
    show player 12f
    player_name "... Tepat."

    show player 90f
    show clyde 2
    clyde "Cih, terserah, sobat."

    clyde "Datang atau tidak datang. Tidak masalah bagi saya!"

    show clyde 26
    clyde "... Tapi jika kamu datang, sebaiknya {b}temui aku di trailer, malam ini{/b}."

    clyde "Anda mengerti?"

    show clyde 1
    show player 12f
    player_name "Ya, saya mengerti."

    player_name "Sampai jumpa {b}malam ini di trailer Roxxy{/b}."

    hide player
    hide clyde
    with dissolve
    return

label button_clyde_roxxy_meeting_buyer:
    scene expression player.location.background_blur
    show clyde 1 at left
    show player 12f at right
    player_name "Apakah kita masih bisa menjual sabu itu?"

    show player 90f
    show clyde 4 with dissolve
    clyde "Tentu 'tidak."

    clyde "Cukup {b}berada di sini malam ini{/b} jika rencana Anda adalah ikut serta."

    show clyde 3
    show player 12f
    player_name "Ya, saya mengerti."

    player_name "Sampai jumpa {b}malam ini{/b}."

    hide player
    hide clyde
    with dissolve
    return

label button_clyde_roxxy_meeting_buyer_dark:
    scene expression player.location.background_blur
    show clyde 1 at left
    show player 12f at right
    player_name "Anda siap berangkat?"

    show player 90f
    show clyde 1
    clyde "..."
    show clyde 2
    clyde "Kamu memakainya?"

    show clyde 1
    show player 5f
    player_name "..."
    show player 10f
    player_name "Apa yang salah dengan apa yang aku kenakan?"

    show player 5f
    show clyde 2
    clyde "Eugh... Entahlah, sobat. Kamu terlihat sangat mencurigakan..."

    clyde "Aku yakin, aku tidak akan membeli narkoba dari orang yang mirip denganmu."

    show clyde 1
    show player 10f
    player_name "Yah, aku tidak membawa pakaian lain..."

    show player 5f
    clyde "..."
    show clyde 2
    clyde "Tunggu sebentar. Aku punya sesuatu untuk kamu pakai!"

    hide clyde with dissolve
    show player 12f
    player_name "... Ini pasti menarik."

    scene black with fade
    pause
    scene park_bench
    show clyde 4 at left
    with dissolve
    clyde "Ayo sekarang sobat..."

    clyde "Kamu akan membuat kami terlambat!"

    show clyde 3
    show player 12f at right
    show player_outfit bb 638ef at Position (xpos=866)
    with dissolve
    player_name "Aku tidak percaya aku membiarkanmu membujukku untuk memakai ini..."

    player_name "Saya merasa konyol!"

    show player 90f
    show clyde 4
    clyde "Psh, jangan konyol."

    clyde "Kamu terlihat seperti aslinya!"

    show clyde 3
    player_name "..."
    show clyde 4
    clyde "Pembeli akan tiba di sini kapan saja."

    hide clyde
    hide player
    hide player_outfit
    with dissolve
    return

label button_clyde_cletus_introduce:
    show player 12f at right
    show clyde 3 at left
    show clyde_hat at left
    with dissolve
    player_name "{b}Clyde{/b}?!"

    show player 5f
    show clyde 22 with dissolve
    clyde "!!!"
    show clyde 21
    show player 10f
    player_name "Kapan kamu kembali ke kota?!"

    show player 5f
    show clyde 2
    clyde "Ehh, maaf kawan."

    clyde "Kamu salah orang..."

    show clyde 1
    show player 10f
    player_name "Hah?"

    show player 5f
    show clyde 4 with dissolve
    clyde "Namanya {b}Cletus{/b}!"

    clyde "Senang bertemu denganmu!"

    show clyde 3
    player_name "..."
    show player 12f
    player_name "Apa yang kamu bicarakan, {b}Clyde{/b}?"

    show player 5f
    show clyde 2 with dissolve
    clyde "{i}*Ahem*{/i} Sekali lagi..."

    clyde "Namanya bukan {b}Clyde{/b}... Ini {b}Cletus{/b}."

    show clyde 1
    show player 12f
    player_name "... Tapi kamu terlihat seperti sepupu {b}Roxxy{/b} {b}Clyde{/b}."

    show player 5f
    show clyde 2
    clyde "Hmm, baiklah, maaf. Saya tidak kenal orang {b}Clyde{/b} ini."

    show clyde 9 with dissolve
    clyde "Dia benar-benar terdengar seperti pria jalang yang tampan!"

    show clyde 3 with dissolve
    player_name "..."
    show player 17f
    player_name "Apakah kamu bercanda denganku sekarang?!"

    show player 13f
    show clyde 4
    clyde "Izinkan saya menanyakan ini kepada Anda..."

    clyde "Apakah {b}Clyde{/b} ini memakai topi?"

    show clyde 3
    show player 10f
    player_name "... Tidak."

    show player 5f
    show clyde 4
    clyde "Baiklah, ini dia!"

    clyde "Seperti yang bisa kamu lihat... {b}Cletus{/b} tidak pernah pergi ke mana pun, tanpa topi terpercayanya!"

    show clyde 3
    player_name "..."
    show player 25f
    player_name "Ini aneh."

    show player 12f
    player_name "aku akan pergi."

    show player 5f
    show clyde 4
    clyde "Baiklah. Senang bertemu denganmu, {b}[firstname]{/b}!"

    show clyde 3
    player_name "..."
    show player 92f
    player_name "Aku tidak memberitahumu namaku!"

    show player 91f
    show clyde 22
    clyde "!!!" with hpunch
    clyde "Oh, salah..."

    clyde "...Yah, aku..."

    show clyde 11 with dissolve
    clyde "Umm... Telepati!"

    show clyde 12
    show player 10f
    player_name "Hah?!"

    show player 5f
    show clyde 11
    clyde "Saya, {b}Cletus{/b}... Saya seorang telepatis."

    show clyde 4 with dissolve
    clyde "... Dan aku tidak membaca pikiranmu dengan peluru pikiran mah!"

    show clyde 3
    show player 10f
    player_name "Peluru pikiran?"

    show player 5f
    show clyde 9 with dissolve
    clyde "Itu benar, sobat!"

    show clyde 4 with dissolve
    clyde "Jadi jangan beritahu orang-orang bahwa aku ada di sini."

    clyde "Karena aku akan tahu..."

    clyde "Apalagi kalau orang-orang itu adalah orang yang tidak tahu malu."

    show clyde 3
    player_name "..."
    show player 25f
    player_name "saya..."

    player_name "... Hanya..."

    player_name "... Sampai jumpa."

    hide player with dissolve
    pause
    show clyde 4
    clyde "Sampai jumpa, sobat!"

    hide clyde
    hide clyde_hat
    with dissolve
    return

label button_clyde_intro_0:
    show clyde 2 at left
    show player 5f at right
    with dissolve
    clyde "Bolehkah aku membantumu melakukan sesuatu?"

    show clyde 1
    show player 10f
    player_name "Eh, bukan?"

    show player 5f
    show clyde 22
    clyde "Ya ampun. Apakah Anda salah satu dari mereka dari pintu ke pintu, Yesus mengasihi kalian?"

    show clyde 21
    show player 12f
    player_name "Apa?! TIDAK!"

    show player 5f
    show clyde 26
    clyde "{i}*Terkesiap*{/i} Apakah kamu seorang polisi?!"

    clyde "Anda harus memberi tahu saya sekarang, itu hukumnya!"

    show clyde 25
    show player 12f
    player_name "Tidak, kawan... Kita baru bertemu kemarin malam!"

    show player 5f
    clyde "..."
    show player 10f
    player_name "Saya sedang membantu {b}Roxxy{/b} mengerjakan pekerjaan rumahnya?"

    show player 5f
    show clyde 4 with dissolve
    clyde "Oh, sial ya!"

    clyde "Pacar barumu {b}Roxanne{/b}!"

    show clyde 3
    show player 10f
    player_name "Tidak, kami hanya teman-"

    show player 5f
    show clyde 4
    clyde "Bagaimana kabarnya, saudara?!"

    show clyde 3
    player_name "..."
    return

label button_clyde_intro_1:
    show clyde 4 at left
    show player 5f at right
    with dissolve
    clyde "Ada apa, saudara?"

    show clyde 3
    show player 14f
    player_name "Oh, hai {b}Clyde{/b}..."

    show player 5f
    show clyde 4
    clyde "Apa yang kamu lakukan di sini?"

    show clyde 3
    return

label button_cletus_intro:
    show player 12f at right
    show clyde 3 at left
    show clyde_hat at left
    with dissolve
    player_name "Jadi, {b}Cletus{/b}, kan?"

    show player 5f
    show clyde 9 with dissolve
    clyde "Itu benar, sobat!"

    show clyde 4 with dissolve
    clyde "Apa yang bisa aku lakukan ya, Fer?"

    show clyde 3
    return

label button_clyde_how_are_you:
    show player 37f with dissolve
    player_name "{i}*Huh*{/i} Saya baik-baik saja."

    player_name "Apa kabarmu?"

    show player 5f with dissolve
    show clyde 9 with dissolve
    clyde "Lebih tepatnya, siapa yang tidak aku lakukan!"

    clyde "Hahah, tahu maksudku, saudara?"

    show clyde 3 with dissolve
    show player 24f
    player_name "..."
    show clyde 11 with dissolve
    clyde "Karena aku sering berhubungan seks... Dengan para wanita..."

    clyde "{i}*Ahem*{/i} Wanita manusia."

    show clyde 12
    show player 12f
    player_name "Ya, saya mengerti, {b}Clyde{/b}..."

    show clyde 9 with dissolve
    clyde "Heh, ya, benar!"

    show clyde 3 with dissolve
    return

label button_clyde_where_are_you_from:
    show player 10f
    player_name "Saya belum pernah mendengar orang berbicara seperti Anda, {b}Clyde{/b}..."

    show player 12f
    player_name "Ngomong-ngomong, dari mana asalmu?"

    show player 5f
    show clyde 4
    clyde "Itu karena kalian semua orang kota jadi bicara aneh!"

    clyde "Sambil berteriak, kita semua berbicara seperti ini..."

    show clyde 3
    show player 10f
    player_name "... Teriakannya?"

    show player 5f
    show clyde 4
    clyde "Ya."

    show clyde 3
    show player 10f
    player_name "Apa itu?"

    show player 5f
    show clyde 4
    clyde "Uhh, tempat aku dibesarkan. Duh!"

    show clyde 3
    show player 11f
    player_name "..."
    show clyde 4
    clyde "Hanya beberapa kabupaten di utara dari sini."

    clyde "Di atas bukit."

    show clyde 3
    show player 10f
    player_name "Kupikir di utara semuanya hutan?"

    show player 5f
    show clyde 4
    clyde "Ya, sangat banyak..."

    show clyde 3
    show player 12f
    player_name "Orang-orang tinggal di atas sana?"

    show player 5f
    show clyde 4
    clyde "Psh, sebagian besar keluargaku masih tinggal di sana."

    clyde "Kupikir aku akan pindah ke sini bersama {b}Bibi Crystal{/b} untuk membaca mantra."

    clyde "Berikan kehidupan kota yang menyenangkan."

    show clyde 3
    show player 10f
    player_name "Bagaimana hasilnya?"

    show player 5f
    show clyde 2 with dissolve
    clyde "Ehh, ada naik turunnya."

    clyde "Aku rindu minuman keras dari rumah dan semua rumput liar."

    show clyde 1
    player_name "..."
    show clyde 4 with dissolve
    clyde "... Tapi aku sedang masak-masak di sini!"

    show clyde 22 with dissolve
    clyde "!!!"
    show clyde 21
    show player 12f
    player_name "Masak apa?"

    show player 5f
    show clyde 22
    clyde "Ehh..."

    show clyde 21
    clyde "..."
    show clyde 22
    clyde "Ayam!"

    show clyde 4 with dissolve
    clyde "Hehe, ya! Aku sedang memasak banyak ayam goreng!"

    clyde "Kalian warga kota tidak pernah merasa cukup..."

    show clyde 3
    show player 4f with dissolve
    player_name "..."
    clyde "..."
    show player 5f with dissolve
    return

label button_clyde_see_ya:
    show player 36f with dissolve
    player_name "aku harus pergi..."

    show player 5f with dissolve
    show clyde 4
    clyde "Ya baiklah."

    clyde "Teruslah bergoyang, saudara!"

    clyde "Wooo!!"

    show clyde 3
    show player 30f
    player_name "..."
    hide player
    hide clyde
    with dissolve
    return

label button_clyde_whats_going_on:
    show player 12f
    player_name "Apa yang terjadi di sana?"

    show player 5f
    show clyde 2 with dissolve
    clyde "Eh, maaf saudaraku."

    clyde "Gubuk ini dilarang keras!"

    show clyde 9 with dissolve
    clyde "Kecuali kamu punya bagian wanita?!"

    show clyde 3 with dissolve
    show player 30f
    player_name "... Tidak."

    show player 5f
    show clyde 4
    clyde "Heh, baiklah, ingat ini... Kalau gubuknya sedang asik, sebaiknya jangan diketuk!"

    show clyde 9 with dissolve
    clyde "Tahu maksudku?!"

    show clyde 3
    show player 401f
    player_name "... Ya. Aku harap aku tidak melakukannya..."

    show player 403f
    return

label button_clyde_nice_tractor:
    show player 14f
    player_name "Traktor yang bagus."

    show player 13f
    show clyde 4
    clyde "Oh ya!"

    clyde "Itu adalah {b}Big Bertha{/b}!"

    clyde "Bukankah dia cantik?"

    show clyde 3
    player_name "..."
    show clyde 4
    clyde "Saya sendiri yang membangunnya dari sisa."

    clyde "31,2 tenaga kuda, 2500 rpm, tangki 8,5 galon..."

    clyde "... Dan lihat saja hasil akhir berwarna merah delima itu!"

    clyde "Hmm! Dia yang paling seksi di kendaraan roda empat!"

    show clyde 9 with dissolve
    clyde "Tahu maksudku?"

    show clyde 3 with dissolve
    show player 5f
    player_name "..."
    return

label button_clyde_nevermind:
    show player 10f
    player_name "Sebenarnya, sudahlah."

    player_name "... Mungkin lain kali?"

    show player 5f
    show clyde 4
    clyde "Psh, ya, saudara!"

    clyde "Anda tahu di mana menemukan saya."

    hide player
    hide clyde
    hide clyde_hat
    with dissolve
    return

label button_clyde_know_youre_clyde:
    show player 15f
    player_name "Ayo, {b}Clyde{/b}! Aku tahu itu kamu!"

    show player 16f
    show clyde 4
    clyde "Aku tidak tahu apa yang kamu bicarakan..."

    show clyde 3
    show player 15f
    player_name "Ini bodoh, aku tidak akan memberitahu siapa pun kamu kembali..."

    show player 16f
    show clyde 4
    clyde "Apa yang sedang merokok, kawan?"

    show player 428f
    clyde "Namanya {b}Cletus{/b} dan ini pertama kalinya saya berada di sini."

    clyde "Pernah."

    show clyde 3
    show player 403f
    player_name "..."
    show player 402f with dissolve
    player_name "Masih tertulis {b}Clyde{/b} di atas kotak teks Anda!"

    show player 403f
    show clyde 2 with dissolve
    clyde "Hai sekarang!"

    clyde "Jangan merusak tembok keempat!"

    clyde "Itu curang!"

    clyde "Namanya {b}Cletus{/b}!!!"

    show clyde 26
    clyde "Katakan!"

    show clyde 25
    show player 90f
    player_name "..."
    show clyde 2
    clyde "Ayolah, kamu tahu kamu ingin mengatakannya..."

    show clyde 1
    show player 24f
    player_name "{i}*Huh*{/i}"

    show player 25f
    player_name "{b}Cletus{/b}."

    show player 24f
    show clyde 4 with dissolve
    clyde "Ini dia!"

    clyde "Itu tidak terlalu sulit sekarang, bukan?"

    show clyde 3
    player_name "..."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
