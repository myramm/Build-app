label button_okita_ingredients_mushroom:
    scene location_school_science_closeup
    show anon f_worried
    show okita 2 at right
    okita "{b}Jamur falicum tumbuh di hutan{/b} di sini di Summerville."

    show okita 3
    okita "Mereka mudah dikenali karena bentuknya yang falus."

    show okita 1
    anon @ f_sad_down "... Bruto."

    return

label button_okita_ingredients_toad:
    scene location_school_science_closeup
    show anon f_worried
    show okita 2 at right
    okita "Ini musim kawin {b}Horny Toad{/b}. Jadi carilah {b}kolam atau sungai{/b}."

    okita "Mereka seharusnya mudah dikenali dari bagian belakangnya yang berwarna ungu dan menggumpal."

    show okita 1
    anon "Kedengarannya seperti seekor katak jelek..."

    return

label button_okita_ingredients_flower:
    scene location_school_science_closeup
    show anon f_worried
    show okita 2 at right
    okita "{b}Euphorbia Psikotropika{/b} adalah bunga bercahaya yang hanya tumbuh di tempat gelap."

    okita "Taruhan terbaik Anda adalah {b}gua{/b}."

    show okita 1
    anon @ f_thinking a_thinking "Hmm, {b}gua{/b}..."

    return

label button_okita_ingredients_stock:
    scene location_school_science_closeup
    show anon f_worried
    show okita 2 at right
    okita "Kita memerlukan sesuatu yang ringan sebagai bahan dasar serum. Kaldu sayur akan bekerja paling baik."

    okita "Anda seharusnya bisa membelinya di Consum-R."

    show okita 1
    anon "... Setidaknya salah satu bahannya sederhana."

    return

label button_okita_ingredients_tissue:
    scene location_school_science_closeup
    show anon f_worried
    show okita 2 at right
    okita "Sampel rambut atau air liur adalah pilihan terbaik."

    show okita 1
    anon @ f_skeptical "Ya, oke, tapi bagaimana aku bisa mendapatkannya?"

    show okita 9
    okita "... Saya yakin Anda akan memikirkan sesuatu."

    show okita 4
    anon @ f_sad_down -m_talk "..."
    return

label button_okita_got_all_ingredients:
    scene location_school_science_closeup
    show anon
    show okita 1 at right
    with dissolve
    anon "Baiklah Bu, saya rasa saya sudah mendapatkan segalanya."

    show okita 3
    okita "... Menurutmu?"

    show okita 1
    hide anon
    show player 533 at left
    with dissolve
    anon "Nah, ada satu masalah kecil..."

    show okita 3
    show player 532
    okita "... Apakah itu kaldu ayam?"

    show player 533
    show okita 1
    anon "Ya. Hanya itu yang dimiliki Consum-R..."

    anon "Saya pikir, mungkin kaldu ayam masih bisa digunakan?"

    show player 532
    show okita 2b
    okita "Hah, ya. Itu seharusnya baik-baik saja..."

    hide player
    show anon f_worried
    with dissolve
    show okita 6
    anon @ -m_talk "..."
    show okita 7
    okita "Sepertinya semuanya beres."

    okita "Temui aku di kantorku malam ini, dan kita akan mulai mixing."

    show okita 6
    anon "Malam ini?"

    show okita 3
    okita "Masalah?"

    show okita 4
    anon "TIDAK! ... Tidak. Sampai jumpa nanti."

    return

label button_okita_extract_cum:
    scene location_school_science_closeup
    show anon f_worried
    show okita 4 at right
    anon "Jadi, kami punya semua yang kami perlukan untuk membuat serum Anda?"

    show okita 5
    okita "... Uhh, ya. Bukankah itu yang baru saja kukatakan padamu?!"

    okita "{b}Temui saya di kantor saya malam ini{/b}, agar kita dapat mengerjakannya."

    show okita 4
    anon "... O-oke."

    return

label button_okita_dose_smith:
    scene location_school_science_closeup
    show anon
    show okita 5 at right
    with dissolve
    okita "Anda masih belum memberi dosis {b}Ny. Smith{/b}?!"

    show okita 4
    anon f_sad_down @ -m_talk "..."
    show okita 5
    okita "Apa yang kamu tunggu?"

    show okita 4
    anon f_worried "Ini tidak mudah lho!"

    anon "Tidak bisakah kamu memberiku nasihat atau semacamnya?!"

    show okita 3
    okita "Berikut beberapa sarannya: cepatlah dan lakukanlah!"

    show okita 5
    okita "Yang harus kamu lakukan hanyalah {b}menyelipkannya ke dalam makanannya atau apalah{/b}."

    show okita 4
    anon @ f_skeptical "Baiklah baiklah. Saya akan kembali."

    return

label button_okita_wait_for_smith_serum:
    scene location_school_science_closeup
    show anon
    show okita 6 at right
    anon "Baiklah, {b}Nona Okita{/b}. Sudah selesai."

    show okita 7
    okita "Luar biasa!"

    okita "Sekarang kita tunggu saja efeknya..."

    show okita 6
    anon "Berapa lama waktu yang dibutuhkan?"

    show okita 7
    okita "Ini akan bekerja dengan cepat. Mengapa kamu tidak tinggal di sini saja, dan kita akan memeriksanya setelah kelas selesai?"

    show okita 6
    anon "Tentu."

    pause 1
    scene black with dissolve
    scene location_school_lounge_day_blur
    show okita 5f zorder 1 at Position(xpos=0.3, ypos=1.0)
    show anon f_worried zorder 0:
        xoffset -100
    show principal 33 at right
    with dissolve
    okita "{i}*Ehem*{/i}"

    show okita 4f
    show principal 32 with dissolve
    smith "Hmm? Oh, halo {b}Tori{/b}..."

    smith "Bagaimana kabar Nona Tahu Segalanya hari ini?"

    show principal 31
    okita "... Hmm."

    show okita 3f
    okita "Saya baru saja memeriksa status kantor saya?"

    show okita 4f
    show principal 32
    smith "Kantor Anda?"

    show okita 5f
    show principal 31
    okita "Nah, suatu hari Anda tampak bersikeras untuk mengganti kunci."

    show okita 4f
    show principal 32
    smith "Apakah saya?"

    smith "Itu lucu... Saya tidak ingat."

    show okita 3f
    show principal 31
    okita "Ah, benarkah?"

    smith "..."
    show principal 30b at Position(xpos=0.95, ypos=1.0) with dissolve
    smith "Bawk bawk."

    show principal 31 at right with dissolve
    show okita 8f
    okita "..."
    show okita 3f
    okita "... Apakah kamu baik-baik saja?"

    show okita 4f
    show principal 32
    smith "... Hah?"

    smith "Aku baik-baik saja, kenapa?"

    show okita 5f
    show principal 31
    okita "Anda mengatakan sesuatu tentang kunci di kantor saya?"

    show okita 4f
    show principal 32
    smith "Apakah saya?"

    smith "Itu lucu... Aku tidak-"

    show principal 30b at Position(xpos=0.95, ypos=1.0) with dissolve
    smith "BAWK!!! Bawk bawk bawk..."

    show principal 31 at right with dissolve
    show okita 6f
    anon "Uhh..."

    show okita 9f
    okita "Ssst!"

    show principal 33 with dissolve
    okita "Jangan ganggu kami {b}[firstname]{/b}."

    show okita 4f
    show principal 32 with dissolve
    smith "... Kopi ini rasanya lucu."

    show principal 31
    anon @ -m_talk "..."
    show okita 7f
    okita "Sudahkah saya memberi tahu Anda tentang penemuan baru yang sedang saya kerjakan?"

    show okita 6f
    show principal 32
    smith "Penemuan?"

    smith "Tidak, menurutku kamu tidak-"

    show principal 30b at Position(xpos=0.95, ypos=1.0) with dissolve
    smith "Bawk bawk..."

    smith "Bawk bawk BAWK!!"

    show principal 31 at right with dissolve
    show okita 7f
    okita "Aku harus membawanya ke kantormu kapan-kapan. Sungguh menarik!"

    show principal 32
    show okita 6f
    smith "Tentu oke!"

    show okita 7f
    show principal 31
    okita "Ya ampun, lihat jamnya."

    okita "Kita harus benar-benar pergi."

    show okita 7 at Position(xpos=0.05, ypos=1.0) with dissolve
    okita "Ayo, {b}[firstname]{/b}."

    hide okita with dissolve
    anon @ -m_talk "..."
    show principal 32
    hide anon with dissolve
    smith "... Kopi ini rasanya lucu."

    scene black with dissolve
    scene location_school_science_closeup
    show anon f_worried
    show okita 7 at right
    okita "Jadi, menurutku {b}kaldu ayam{/b} menimbulkan sedikit efek samping..."

    show okita 2b
    okita "Pffft, hahaha!!"

    show okita 6
    anon @ f_skeptical "Bagaimana ini lucu?!"

    anon "Kami mengacaukan kepalanya, dan dia di sana berkotek seperti ayam!"

    show okita 2b
    okita "Ya, benar! Ha ha ha!"

    show okita 7
    okita "Oh, maukah kamu bersantai?"

    okita "Itu hanya sementara."

    show okita 9
    okita "... menurutku."

    show okita 6
    anon f_surprised "Menurutmu?!"

    show okita 9
    okita "Maksudku, aku cukup yakin."

    show okita 7
    okita "Lihat yang penting disini serumnya berhasil!"

    okita "Dia benar-benar tidak memihak pada eksperimenku sekarang!"

    okita "... Dan dia bahkan tidak ingat ingin mengunci saya di luar kantor!"

    show okita 6
    anon f_worried "Ya, tapi dia berkotek seperti ayam!"

    show okita 2b
    okita "Pffftt, hahahaaaah!"

    anon @ f_skeptical "Yah, aku senang kamu menganggapnya lucu..."

    show okita 6
    anon "Jadi bagaimana sekarang?"

    show okita 7
    okita "Sekarang, saya perlu waktu untuk mempelajari efek serum lainnya."

    show okita 6
    anon "Oh, aku benar-benar lupa tentang serum lainnya!"

    anon "Apakah kamu merasa ada yang berbeda?"

    show okita 7
    okita "Mmm, mungkin..."

    show okita 2b
    okita "Hehehe!"

    anon "Kamu memang tampak agak berbeda."

    show okita 7
    okita "Bagaimana bisa?"

    show okita 6
    anon f_skeptical "Kamu seperti... Pusing."

    show okita 2b
    okita "Hehehe! Saya hanya senang."

    anon f_worried "Sejujurnya itu membuatku takut."

    show okita 7
    okita "... Dan panas."

    show okita 3
    okita "Apakah kamu seksi? Di sini panas!"

    show okita 6
    anon "Tidak, aku baik-baik saja."

    show okita 7
    okita "Baiklah, baiklah, aku akan pergi ke kantorku dan menyelesaikan beberapa pekerjaan."

    okita "Ayo temui aku beberapa hari lagi."

    show okita 6
    anon "Hmm, oke."

    show okita 2b
    okita "Sampai jumpa, {b}[firstname]{/b}!"

    okita "Hehehehe..."

    hide okita with dissolve
    anon "Aku harap dia akan baik-baik saja..."

    return

label button_okita_wait_for_okita_serum:
    scene location_school_science_closeup
    show anon f_worried
    show okita 6 at right
    with dissolve
    anon "Anda baik-baik saja, Bu?"

    anon "Sudah tahukah ada efek samping dari serum Anda?"

    show okita 7
    okita "Saya masih menguji."

    okita "... Saya menghargai Anda menghubungi saya."

    show okita 6
    anon "... iya kan?"

    show okita 7
    okita "Tentu saja!"

    show okita 2b
    okita "Itu membuatku merasa hangat dan tidak jelas!"

    show okita 6
    anon @ -m_talk "..."
    anon f_skeptical "Oke, serius! Kamu bertingkah sangat aneh!"

    show okita 7
    okita "Apakah saya?"

    show okita 2b
    okita "Aku tidak tahu apa yang harus kukatakan padamu. Saya merasa luar biasa!"

    show okita 6
    anon f_worried "Oke, baiklah, hati-hati saja, menurutku."

    show okita 7
    okita "Bisa, ganteng!"

    show anon f_surprised
    show okita 2b
    okita "Hehehe!"

    anon f_worried @ f_sad_down a_behind_head "..."
    return

label button_okita_serum_effects:
    scene location_school_science_closeup
    show anon f_worried
    show okita 6 at right
    with dissolve
    anon "Sudah ada hasil dari serumnya?"

    show okita 7
    okita "Sebenarnya, {b}[firstname]{/b}, saya berharap Anda dapat membantu saya menguji penemuan terbaru saya?"

    show okita 6
    anon "Ya ampun, kamu ingin aku membuat yang lain?"

    show okita 3
    okita "Hmm? Tidak, tidak!"

    show okita 7
    okita "Saya membuat yang ini sendiri. Ini revolusioner!"

    show okita 6
    anon "Anda membangunnya?"

    anon "Tapi membangun adalah pekerjaan monyet. Saya pikir kamu tidak melakukan pekerjaan monyet?"

    show okita 7
    okita "Saya membuat pengecualian kali ini karena..."

    okita "Ya, saya membuat penemuan ini untuk Anda, sebagai kejutan."

    show okita 6
    anon "Untukku?"

    show okita 7
    okita "Ya, datanglah ke kantorku malam ini sepulang sekolah dan aku akan menunjukkannya padamu."

    show okita 7
    anon "Ini mulai membuatku khawatir..."

    anon "Lagi sibuk apa?"

    show okita 2b
    okita "Jangan jadi bayi! Anda harus datang dan melihat!"

    show okita 6
    anon "Bagus."

    show okita 7
    okita "Anda berjanji?"

    show okita 6
    anon f_skeptical "Uhh, ya."

    anon "... aku berjanji."

    show okita 2b
    okita "Hore!"

    show okita 7
    okita "Sampai jumpa lagi, {b}[firstname]{/b}!"

    hide okita with dissolve
    anon f_worried @ f_sad_down "..."
    return

label button_okita_generic_after_q3:
    call expression game.dialog_select("button_okita_generic_after_q3_intro")
    menu:
        "Penemuan baru." if M_okita.is_state(S_okita_is_hypersexual):
            call expression game.dialog_select("button_okita_generic_after_q3_new_invention")
        "Tidak ada apa-apa.":

            call expression game.dialog_select("button_okita_generic_after_q3_leave")
    return

label button_okita_generic_before_q3:
    scene location_school_science_closeup
    show anon
    show okita 4 at right
    with dissolve
    anon "Hai, {b}Nona Okita{/b}."

    show okita 5
    okita "Apa itu, {b}[firstname]{/b}?"

    okita "Saya sangat sibuk..."

    show okita 4
    return

label button_okita_generic_after_q3_intro:
    scene location_school_science_closeup
    show anon
    show okita 6 at right
    with dissolve
    anon "Hai, {b}Nona Okita{/b}."

    show okita 2b
    okita "{b}[firstname]{/b}!"

    show okita 7
    okita "Senang sekali Anda berkunjung!"

    okita "Apa yang bisa saya bantu?"

    show okita 6
    return

label button_okita_generic_after_q3_new_invention:
    show anon f_normal
    anon "Jadi, Anda sedang mengerjakan penemuan baru, ya?"

    show okita 7
    okita "Oh ya!"

    okita "Ini revolusioner! Anda benar-benar harus datang dan melihatnya!"

    show okita 6
    anon "Hehe, oke! Saya akan {b}menemui Anda di kantor Anda malam ini{/b}."

    show okita 2b
    okita "Anda harus berjanji akan datang dan melihat!"

    show okita 6
    anon f_skeptical @ -m_talk "..."
    anon "... Ya. Saya berjanji."

    show okita 2b
    show anon f_worried
    okita "Saya tidak sabar!"

    return

label button_okita_generic_after_q3_leave:
    show anon f_normal
    anon "Tidak ada, aku hanya ingin menyapa!"

    show okita 5
    okita "Kamu baik sekali."

    okita "Meskipun begitu, saya sedang sibuk mengerjakan beberapa desain baru saat ini."

    show okita 7
    okita "Temui saya di {b}kelas{/b} saya jika Anda ingin membantu saya."

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
