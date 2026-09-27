label jane_library_dialogue_bissette_find_dictionary:
    show jane:
        flip
        xoffset 100
    show xtra 42
    show player 10f at right
    with dissolve
    player_name "Sepertinya saya tidak dapat menemukan {b}kamus bahasa Prancis{/b}."

    show player 5f
    jane "Hmm, coba kulihat..."

    show jane f_normal_down
    pause
    jane "Seharusnya ada di rak, di sebelah ruang belakang."

    show jane f_normal
    show player 14f
    player_name "Baiklah, saya akan memeriksanya. Terima kasih."

    return

label jane_library_dialogue_bissette_get_dictionary:
    show jane f_normal:
        flip
        xoffset 100
    show xtra 42
    show player 504f at right
    with dissolve
    player_name "Ya, saya menemukan bagian dari {b}kamus bahasa Prancis{/b}."

    show player 503f
    show jane f_sad
    jane "Apa?"

    show player 5f
    show jane f_complain_down a_book1
    with dissolve
    jane "Oh tidak!"

    jane "Saya harus memesan yang baru tetapi akan memakan waktu lama untuk sampai."

    show jane f_sad
    jane "Apakah Anda masih ingin memeriksanya?"

    show player 10f
    player_name "Ya, aku cukup putus asa. Saya hanya berharap saya tidak membutuhkan halaman-halaman yang hilang itu..."

    show player 5f
    jane "Oke, sekali lagi maaf!"

    show jane f_normal
    jane "Anda bisa menyimpannya saja. Tidak akan banyak gunanya di sini..."

    show jane a_idle with dissolve
    show player 504f with dissolve
    player_name "Terima kasih!"

    show player 503f
    show jane f_laugh
    jane "Tidak masalah, semoga harimu menyenangkan!"

    hide player
    hide jane
    with dissolve

    scene library
    show player 34 with dissolve
    player_name "(Saya kira saya harus membawa ini ke {b}Nona Bissette{/b} dan melihat apa yang dia pikirkan... )"

    return

label jane_library_dialogue_bissette_return_overdue_books:
    show jane f_normal:
        flip
    show xtra 42
    show player 14f at right
    with dissolve
    player_name "Saya menemukan semua buku yang sudah lewat waktunya!"

    show player 239_240f with dissolve
    pause
    show player 507f at Position (xoffset=-9) with dissolve
    jane "Benar-benar? Mari kita lihat..."

    show player 13f
    show jane a_book3 with dissolve
    jane "Anda berhasil! Terima kasih banyak!"

    jane "Aku juga punya sesuatu untukmu."

    show player 10f
    player_name "Anda melakukannya?"

    show jane a_book2 with dissolve
    jane "Yup, buku yang Anda pesan sudah masuk."

    pause
    show player 521f
    show jane a_idle
    with dissolve
    player_name "Terima kasih!"

    player_name "{b}My cheese and me{/b}..." (show_native="{b}Mon fromage et moi{/b}...")
    show player 5f with dissolve
    jane "Akankah itu berhasil?"

    show player 10f
    player_name "Err, aku harus menyelesaikannya."

    show player 14f
    player_name "Terima kasih lagi!"

    show player 13f
    show jane f_laugh
    jane "Kembalilah dan temui kami!"

    return

label jane_library_dialogue_pre:
    show jane:
        flip
        xoffset 100
    show xtra 42
    show player 1f at right
    with dissolve
    jane "Hai! Apa yang bisa saya bantu?"

    show player 2f
    player_name "Hai, saya sedang mencari {b}buku{/b}."

    show player 1f
    jane "Tentu saja! Tahukah kamu nama bukunya?"

    return

label jane_library_dialogue_production_ask_librarian:
    scene librarydesk
    show jane:
        flip
        xoffset 100
    show xtra 42
    show player 10f at right
    with dissolve
    player_name "Anda pasti tidak punya buku tentang peningkatan produksi susu pada sapi, bukan?"

    show player 5f
    show jane f_sad
    jane "Hmm, itu pertanyaan yang aneh."

    show jane f_normal
    show player 29f with dissolve
    player_name "Eh, ya. Saya rasa memang demikian."

    player_name "Ini untuk uhh... temanku."

    show player 3f at Position (xoffset=-8)
    show jane f_laugh
    jane "Hehe, tentu saja."

    show jane f_eyeroll a_hand_out with dissolve
    jane "Um, aku tidak tahu."

    jane "Saya yakin kita punya banyak hal tentang sapi, tetapi sejauh menyangkut pemerahan..."

    show jane f_normal
    jane "... {b}Coba rak sebelah sana{/b}."

    show jane a_idle
    show player 14f
    with dissolve
    player_name "Terima kasih!"

    hide player with dissolve
    pause
    show jane f_sad
    jane "Aneh sekali."

    hide jane
    with dissolve
    return

label jane_library_dialogue_french_poetry:
    show player 10f
    player_name "Apakah Anda punya puisi Perancis?"

    show player 5f
    show jane f_normal_down
    jane "Hmm..."

    show jane f_normal
    jane "Sebenarnya..."

    jane "Beberapa gadis di sini membaca sesuatu seperti itu {b}kemarin sore{/b}."

    show player 10f
    player_name "Benar-benar?"

    show player 12f
    player_name "Apakah mereka memeriksanya?"

    show player 5f
    jane "Tidak."

    show player 10f
    player_name "Tahukah kamu dimana itu?"

    show player 5f
    show jane f_normal_down
    jane @ -m_talk "..."
    show jane f_sad
    jane "Tidak..."

    jane "Tapi, mungkin mereka akan kesini lagi {b}siang{/b} ini."

    jane "Anda bisa bertanya kepada salah satu dari mereka di mana mereka menaruhnya."

    show jane f_normal
    show player 12f
    player_name "Terima kasih."

    return

label jane_library_dialogue_french_food_find_books:
    show player 10f
    player_name "Saya ingin tahu apakah Anda punya buku berbahasa Prancis tentang makanan?"

    show player 13f
    show jane f_laugh
    jane "Itu topik yang menarik..."

    show jane f_normal
    show player 14f
    player_name "Ya, saya membutuhkannya untuk tugas sekolah."

    show player 13f
    jane "Baiklah, izinkan saya melihat dan melihat apa yang kita miliki."

    show jane f_normal_down
    jane @ -m_talk "..."
    show player 11f
    player_name "..."
    show player 5f
    jane "Hmm, sepertinya kami tidak memiliki hal seperti itu."

    show jane f_normal
    show player 12f
    player_name "Tidak ada apa-apa?"

    show player 5f
    show jane f_normal_down
    jane "Tidak... Oh, tunggu sebentar!"

    jane "Dikatakan bahwa cabang saudara kita memiliki buku Perancis tentang keju."

    show jane f_normal
    jane "Apakah itu akan berhasil?"

    show player 14f
    player_name "Tentu, saya suka keju! Di mana saya harus mengambilnya?"

    show player 13f
    jane "Saya dapat meminta mereka untuk mengirimkannya ke sini. Seharusnya hanya memakan waktu beberapa hari..."

    jane "Sementara itu, saya ingin tahu apakah Anda dapat membantu saya melakukan sesuatu?"

    show player 10f
    player_name "... Tentu saja, menurutku. Apa yang kamu perlukan?"

    show player 5f
    jane "{b}Beberapa teman sekelasmu memiliki buku yang sudah lewat batas waktunya{/b} Saya ingin mengembalikannya."

    jane "Saya telah mengirim surat ke rumah mereka tetapi sepertinya tidak berhasil."

    jane "Aku benci kehilangan buku-buku itu."

    show player 10f
    player_name "Ya, saya bisa mencoba {b}berbicara dengan mereka{/b}. Siapa nama mereka?"

    show player 5f
    show jane f_normal_down
    jane "Hmm, yang pertama adalah {b}Nona Martinez{/b}."

    jane "Yang kedua adalah {b}Tuan. Erik J{/b}-"

    show jane f_normal
    show player 14f
    player_name "{b}Erik{/b} punya buku?!"

    player_name "Itu seharusnya mudah."

    show player 13f
    show jane f_normal_down
    jane "... Dan akhirnya..."

    jane "Hah. Hanya tertulis {b}Dexter{/b}."

    jane "Ada yang berbunyi?"

    show jane f_normal
    show player 12f
    player_name "Ya ampun, bukan {b}Dexter{/b}... Anda yakin?"

    show player 11f
    jane "Itu yang tertulis di log..."

    show player 12f
    player_name "Sial! Baiklah, saya akan lihat apa yang bisa saya lakukan."

    show player 5f
    show jane f_laugh
    jane "Terima kasih, saya sangat menghargai ini!"

    hide jane with dissolve
    show player 12 at center with dissolve
    player_name "Eh, kenapa harus {b}Dexter{/b}?"

    return

label jane_library_dialogue_french_food_book_holders:
    show player 10f
    player_name "Siapa nama siswanya lagi?"

    player_name "Anda tahu, yang buku-bukunya sudah lewat waktu."

    show player 5f
    show jane f_normal
    jane "Satu detik..."

    show jane f_normal_down
    jane "Hmm, {b}Nona Martinez{/b}, {b}Tuan. Erik{/b}, dan {b}Dexter{/b}."

    show jane f_normal
    show player 12f
    player_name "Ugh, aku lupa tentang {b}Dexter{/b}..."

    player_name "Baiklah, aku sedang mengerjakannya."

    return

label jane_library_dialogue_magazines_first:
    show player 2f
    player_name "Saya sedang membuat kolase untuk kelas seni dan saya memerlukan beberapa majalah lama."

    player_name "Bisakah Anda menunjukkan di mana menemukannya?"

    show player 1f
    show jane f_normal
    jane "Saya khawatir Anda kurang beruntung. Kami berhenti membawanya beberapa bulan yang lalu."

    show player 10f
    player_name "Anda tidak punya?"

    show player 1f
    jane "Sayangnya tidak. Kami mengirim semua yang kami miliki untuk didaur ulang."

    show player 10f
    player_name "Ya ampun..."

    player_name "Terima kasih."

    show player 11f
    jane "Maaf."

    hide jane
    hide xtra
    hide player
    with dissolve
    show player 10 with dissolve
    player_name "Apa yang akan saya lakukan sekarang?"

    show player 11
    player_name "..."
    show player 10
    player_name "Saya kira {b}Saya akan kembali ke sekolah dan melihat-lihat{/b}."

    player_name "Pasti ada beberapa majalah di suatu tempat."

    return

label jane_library_dialogue_magazines_repeat:
    show player 10f
    player_name "Jadi kamu tidak punya satu majalah pun di sini?"

    show player 11f
    show jane f_normal
    jane "Tidak."

    jane "Kami membatalkan langganan dan membuang apa yang kami miliki."

    show player 10f
    player_name "Oke, terima kasih."

    hide jane
    hide xtra
    hide player
    with dissolve
    show player 10 with dissolve
    player_name "{i}*Huh*{/i}"

    player_name "Sepertinya aku harus {b}kembali ke sekolah dan melihat sekeliling sana{/b}."

    player_name "... Mungkin aku akan beruntung?"

    return

label jane_library_dialogue_return_books_pre:
    show player 14f
    player_name "Saya ingin mengembalikan buku."

    show player 13f
    show jane f_laugh
    jane "Besar!"

    return

label jane_library_dialogue_return_books_first:
    show jane f_normal
    jane "Tidak banyak orang yang melakukannya."

    show player 10f
    player_name "Lalu apa yang terjadi?"

    show player 5f
    show jane f_mad
    jane "Saya memburu mereka dan mematahkan salah satu kaki mereka, agar mereka tidak melakukannya lagi."

    show player 22f
    player_name "!!!"
    show jane f_laugh
    jane "Cuma bercanda!"

    show jane f_normal
    show player 29f with dissolve
    player_name "Oh."

    show player 3f at Position (xoffset=-8)
    return

label jane_library_dialogue_return_books_after:
    show jane f_normal
    jane "Letakkan saja buku yang ingin Anda kembalikan di konter dan saya akan mengurusnya."

    show jane f_laugh
    jane "Dan segera kembali!"

    return

label jane_library_dialogue_leave:
    show player 24f
    show jane f_sad
    player_name "Maaf. Saya akan kembali setelah saya ingat nama bukunya."

    show player 5f
    show jane f_normal
    jane "Sampai jumpa."

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
