label bissette_dialogue_dress_code:
    hide player
    hide bissette
    show teacher 1 at right
    show anon f_worried
    anon "Sebenarnya, saya berharap Anda bisa berbicara dengan {b}Nyonya. Smith{/b} tentang kebijakan aturan berpakaian yang baru..."

    show teacher 5
    bissette "Apa?"

    show teacher 2
    bissette "Kode berpakaiannya?"

    show teacher 1
    anon "Ya."

    show teacher 2
    bissette "Saya belum pernah mendengar hal ini sebelumnya?"

    show teacher 1
    anon f_unimpressed_bored "Baiklah, {b}Ny. Smith{/b} baru saja menerapkannya dan itu sangat konyol..."

    anon f_worried @ f_unimpressed_bored "Itu melarang kita mewarnai rambut kita dan saya hanya berpikir-"

    show teacher 2
    bissette "Anda berpikir untuk mengecat rambut?"

    show teacher 1
    anon @ f_surprised "Hmm?"

    anon @ f_normal "Oh, tidak... Bukan aku."

    anon "Aku khawatir tentang {b}Eve{/b}, kamu tahu?"

    show teacher 2
    bissette "Ah, ya... Rambut birunya."

    show teacher 1
    anon "Ya, dia sangat menyukainya dan aku hanya berpikir-"

    show teacher 5
    bissette "Maaf, {b}[firstname]{/b}..."

    bissette "Saya ingin membantu tetapi saya sudah mempunyai terlalu banyak masalah dengan kepala sekolah..."

    show teacher 4
    anon "Tidak apa-apa, {b}Nona Bissette{/b}."

    anon "Saya mengerti."

    show teacher 2
    bissette "Mungkin salah satu guru lain bisa membantu Anda?"

    show teacher 1
    anon "Ya, aku akan bertanya pada salah satu dari mereka."

    hide anon with dissolve
    return

label bissette_dialogue_meet_in_office:
    hide anon
    show player 10 at left
    show teacher 1 at right
    with dissolve
    player_name "{b}Nona Bissette{/b}, apa yang perlu saya lakukan?"

    show player 5
    show teacher 12
    bissette "Oh, {b}[firstname]{/b}. Tidak di sini. {b}Temui aku di kantor sepulang sekolah{/b} ya?"

    show teacher 13
    show player 14
    player_name "Oke, aku akan menemuimu di sana."

    return

label bissette_dialogue_check_dictionary:
    hide anon
    show teacher 1 at right
    show player 10 at left
    with dissolve
    player_name "Hai, {b}Nona Bissette{/b}. Saya menemukan {b}kamus{/b} di perpustakaan tetapi ada beberapa halaman yang hilang."

    show player 239_240 with dissolve
    pause
    show player 503 with dissolve
    pause
    show player 5
    show teacher 22b
    with dissolve
    bissette "Ya ampun!"

    bissette "Menurut saya, ini akan membuat segalanya menjadi sangat sulit."

    bissette "Bagian Prancis ke Inggris masih utuh tetapi Anda kehilangan banyak kata..."

    bissette "Saya khawatir beberapa di antaranya mungkin penting bagi mata pelajaran yang akan kita pelajari."

    show teacher 21b
    show player 10
    player_name "Ah, aku takut akan hal itu..."

    show player 5
    show teacher 21
    bissette "Hmm, mungkin semuanya belum hilang. Saya yakin {b}teman sekelas Anda akan bersedia membiarkan Anda menyalin halaman yang hilang dari kamus mereka{/b}."

    bissette "Anda dapat {b}menggunakan mesin fotocopy di lab komputer{/b}."

    show teacher 22
    show player 14
    player_name "Itu ide yang bagus!"

    show player 13
    show teacher 2 with dissolve
    bissette "Ini adalah hal yang baik, {b}[firstname]{/b}."

    bissette "Pastikan untuk mendapatkan kata-kata bahasa Inggris yang diawali dengan huruf \"B\" untuk pelajaran berikutnya."

    show teacher 1
    show player 14
    player_name "Baiklah, {b}saatnya mencari kamus lain{/b}..."

    show player 13
    show teacher 12
    bissette "Sudah bekerja keras. Saya tahu Anda sangat menginginkan hadiah spesial, ya?"

    show teacher 13
    show player 10
    player_name "Adakah pemikiran tentang {b}kamus{/b} siapa yang harus saya pinjam?"

    show player 13
    show teacher 11
    bissette "Hmm..."

    show teacher 2
    bissette "Mungkin {b}Judith{/b}?"

    bissette "Dia menunjukkan banyak bakat untuk bahasa Prancis..."

    show teacher 1
    show player 14
    player_name "Oke, {b}Saya akan mulai dengan Judith{/b}."

    return

label bissette_dialogue_intro:
    show anon
    show bissette
    with dissolve
    bissette "Hai, {b}[firstname]{/b}!"

    anon @ f_laugh "Hai, {b}Nona Bissette{/b}!"

    bissette @ a_finger "Apakah kamu sudah bisa melanjutkan studimu?"

    bissette "Saya sangat berharap Anda melakukannya!"

    bissette "Sekarang, apakah ada sesuatu yang ingin Anda bicarakan?"

    return

label bissette_dialogue_food_assignment_intro:
    hide anon
    hide bissette
    show teacher 1 at right
    show player 10 at left
    player_name "Apa tugasku selanjutnya?"

    show player 5
    show teacher 2
    bissette "Saya ingin Anda {b}menulis beberapa paragraf tentang makanan favorit Anda, dalam bahasa Prancis{/b}."

    bissette "Kalau begitu kita akan membahasnya bersama, ya?"

    show teacher 1
    show player 14
    player_name "Oh ya!"

    return

label bissette_dialogue_food_assignment_prepare_assignment:
    anon "Saya harus mengunjungi pustakawan itu lagi. Mungkin dia bisa mencarikan buku tentang {b}makanan Prancis{/b} untuk saya."

    anon "Lalu aku bisa mengetik sesuatu di komputerku."

    anon "Terima kasih, {b}Nona Bissette{/b}!"

    return

label bissette_dialogue_food_assignment_do_assignment:
    anon "Saya harus mengetik sesuatu di komputer saya."

    anon "Terima kasih, {b}Nona Bissette{/b}!"

    return

label bissette_dialogue_poem_assignment_intro:
    hide anon
    hide bissette
    show teacher 1 at right
    show player 10 at left
    player_name "Ingatkan saya, tugas apa lagi?"

    show player 5
    show teacher 2
    bissette "Lekuel? Kamu sebagai déjà oublié?"

    bissette "Anda akan {b}menulis puisi romantis dalam bahasa Prancis{/b}!"

    show teacher 1
    show player 14
    player_name "Oh benar!"

    player_name "Terima kasih, {b}Nona Bissette{/b}."

    show player 13
    show teacher 2
    bissette "{b}Kembalikan kepada saya setelah selesai{/b}."

    bissette "Jangan biarkan aku menunggu, mon bel homme."

    return

label bissette_dialogue_poem_assignment_do_assignment:
    hide anon
    show player 14 at left
    player_name "Saya harus mengetik sesuatu di komputer saya."

    return

label bissette_dialogue_poem_assignment_print_assignment:
    hide anon
    hide bissette
    show teacher 1 at right
    show player 14 at left
    player_name "Saya menyelesaikan puisinya, {b}Nona Bissette{/b}."

    show player 13
    show teacher 2
    bissette "Bagus, coba saya lihat!"

    show teacher 1
    show player 10
    player_name "Oh ya, aku harus mencetaknya dulu.."

    show player 5
    show teacher 2
    bissette "Nah, printernya ada di {b}lab komputer{/b} ya?"

    show teacher 1
    show player 14
    player_name "Yup, segera kembali!"

    return

label bissette_dialogue_private_tutoring:
    hide anon
    hide bissette
    show teacher 1 at right
    show player 10 at left
    player_name "Apa menurutmu kita bisa bertemu di kantormu malam ini?"

    show player 26
    player_name "Anda tahu, untuk beberapa... Bimbingan belajar?"

    show player 13
    show teacher 12
    bissette "Oh, les. Ya!"

    bissette "Sampai jumpa malam ini untuk pertemuan tatap muka, ya?"

    show teacher 13
    show player 33
    player_name "Ya!"

    show player 13
    show teacher 12
    bissette "Très bien, mon bel homme!"

    return

label bissette_dialogue_tutoring:
    hide anon
    hide bissette
    show teacher 1 at right
    show player 10 at left
    player_name "Saya ingin tahu apakah Anda masih menawarkan les privat?"

    show player 5
    show teacher 3
    bissette "Oh ya!"

    show teacher 1
    show player 14
    player_name "Luar biasa! Kapan Anda akan tersedia-"

    show player 11
    show teacher 2
    bissette "Mengesankan! Anda adalah siswa pertama yang bertanya tentang bimbingan belajar!"

    show teacher 1
    show player 12
    player_name "Benar-benar? Itu aneh..."

    show player 5
    show teacher 5
    bissette "Saya mulai berpikir tidak ada seorang pun yang tertarik dengan hadiah khusus tersebut."

    show teacher 1
    show player 12
    player_name "Oh iya, aku lupa hadiah spesialnya..."

    show player 5
    show teacher 5
    bissette "Apa? Anda juga tidak menginginkan imbalannya?!"

    show teacher 4
    show player 29 with dissolve
    player_name "Err... Bukan, maksudku... A-hadiah spesial terdengar luar biasa, {b}Nona Bissette{/b}."

    show player 3
    show teacher 3
    bissette "Ah luar biasa!"

    show teacher 2
    bissette "Lalu kita akan bertemu sepulang sekolah untuk pelajaran tatap muka, ya?"

    show teacher 1
    show player 10 with dissolve
    player_name "Umm... Ya, menurutku itu akan-"

    show player 11
    show teacher 2
    bissette "Sangat bagus!"

    bissette "Pastikan untuk {b}membawa kamus bahasa Prancis Anda{/b}."

    show teacher 1
    show player 24
    player_name "Ah, sial. Tentang itu... {b}Nona Bissette{/b}, sepertinya saya tidak dapat menemukan {b}kamus bahasa Prancis{/b} saya."

    show player 25
    player_name "Itu tidak ada di ranselku, di rumahku, atau di lokerku..."

    show player 5
    show teacher 5
    bissette "Oh tidak, ini tidak bagus!"

    bissette "Mungkin Anda harus {b}mampir ke perpustakaan{/b} dan melihat apakah mereka memilikinya?"

    show teacher 2
    bissette "Aku ingin meminjamkan milikku padamu, tapi sayangnya aku baru saja menumpahkan anggur ke atasnya."

    show teacher 1
    show player 14
    player_name "Oh ya, aku lupa tentang perpustakaan!"

    show player 13
    show teacher 2
    bissette "Ya ampun, aku sendiri sering pergi ke sana."

    show teacher 12
    bissette "Saya suka merasakan buku bagus di tangan saya."

    bissette "Dipeluk oleh api hangat dengan anggur kental..."

    bissette "Ini adalah surga."

    show teacher 13
    show player 11
    player_name "..."
    show teacher 2
    bissette "Oh, bodohnya aku, terus mengoceh. {b}beri tahu saya jika Anda sudah memiliki kamusnya{/b} ya?"

    show teacher 1
    show player 14
    player_name "Tentu saja, {b}Nona Bissette{/b}."

    return

label bissette_dialogue_get_dictionary:
    hide anon
    hide bissette
    show teacher 1 at right
    show player 12 at left
    player_name "Ingatkan saya apa yang perlu saya dapatkan sebelum kita bisa belajar bersama?"

    show player 5
    show teacher 2
    bissette "Anda memerlukan {b}kamus Bahasa Prancis ke Bahasa Inggris{/b}."

    bissette "{b}Cek perpustakaan{/b} ya?"

    show teacher 1
    show player 14
    player_name "Oh benar!"

    player_name "Terima kasih!"

    return

label bissette_dialogue_replace_missing_pages:
    hide anon
    hide bissette
    show teacher 1 at right
    show player 12 at left
    player_name "Apa yang harus saya lakukan lagi?"

    show player 5
    show teacher 2
    bissette "{b}Salin halaman yang hilang dari kamus teman sekelas{/b}."

    show teacher 1
    show player 14
    player_name "Oh benar!"

    show player 13
    show teacher 2
    bissette "Periksa dengan {b}Judith{/b}. Dia sangat pandai berbahasa Prancis."

    show teacher 1
    show player 14
    player_name "Dan kemudian {b}lab komputer memiliki mesin fotokopi{/b}..."

    player_name "Mengerti, sekali lagi terima kasih!"

    return

label bissette_dialogue_chat:
    hide teacher
    hide player
    show bissette
    show anon f_shy a_behind_head
    anon "{b}Nona Bissette{/b}, saya hanya ingin mengatakan bahwa saya sangat menghargai bantuan dalam menyelesaikan tugas sekolah saya!"

    show anon f_normal
    bissette f_sexy @ f_laugh a_hair "Dengan senang hati! Yang saya inginkan hanyalah memastikan bahwa Anda termotivasi untuk tampil..."

    bissette "... Dan saya suka memberi penghargaan kepada siswa pekerja keras!"

    anon "Saya akan melakukan yang terbaik. aku sangat ingin mendapat nilai bagus..."

    bissette f_normal "Itu yang ingin saya dengar!"

    bissette "Saya bisa {b}meninjau pekerjaan rumah Anda bersama Anda{/b} saat Anda menyerahkannya, jika Anda mau!"

    anon @ f_laugh "Kedengarannya bagus, {b}Nona Bissette{/b}! Terima kasih!"

    return

label bissette_dialogue_leave:
    hide player
    hide teacher
    show anon f_normal
    show bissette
    anon "Tidak, aku hanya ingin menyapa."

    bissette f_normal "Baiklah, duduklah. Kelas akan segera dimulai!"

    bissette @ f_laugh "Saya punya pelajaran menarik yang direncanakan untuk hari ini!"

    anon "Kedengarannya bagus, {b}Nona Bissette{/b}."

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
