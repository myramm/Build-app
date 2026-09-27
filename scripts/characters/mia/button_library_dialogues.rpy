label mia_library_dialogue_bissette_find_poem_reference_book:
    show player 14 at left
    show old_mia 7 at right
    with dissolve
    player_name "Hei, {b}Mia{/b}! Lagi sibuk apa?"

    show player 13
    show old_mia 10
    mia "Oh, halo, {b}[firstname]{/b}! Saya baru saja akan belajar untuk ujian kimia yang akan datang."

    show old_mia 7
    show player 12
    player_name "Kupikir ibumu tidak mengizinkanmu melakukan apa pun sepulang sekolah?"

    show player 13
    show old_mia 12
    mia "Biasanya dia tidak melakukannya, tapi..."

    show old_mia 10
    mia "Saya mengatakan kepadanya {b}Nona Okita{/b} akan menulis rekomendasi akademis untuk saya jika saya berhasil dalam ujian berikutnya."

    show old_mia 7
    player_name "Akankah dia benar-benar melakukan itu?"

    show old_mia 10
    mia "Mungkin tidak, tapi tidak ada salahnya untuk mencobanya, bukan?"

    mia "Dan aku juga bisa jalan-jalan dengan {b}Judith{/b} di luar rumahku!"

    show old_mia 7
    show player 14
    player_name "Ya, saya kira tidak."

    show player 13
    show old_mia 10
    mia "Apa yang kamu lakukan di sini?"

    show old_mia 7
    show player 14
    player_name "{b}Nona Bissette{/b} memberi saya tugas. Saya pikir mungkin saya bisa mendapatkan inspirasi di sini."

    show player 13
    show old_mia 10
    mia "Oh ya? Apa tugasnya?"

    show old_mia 7
    show player 10
    player_name "Yah, itu agak memalukan..."

    show player 5
    show old_mia 9
    mia "Hehe, benarkah?! Nah, kamu harus memberitahuku sekarang!"

    show old_mia 7
    show player 10
    player_name "{i}*Sigh*{/i} Aku seharusnya menulis puisi romantis dalam bahasa Prancis."

    show player 5
    show old_mia 10
    mia "Itu tidak memalukan!"

    show old_mia 7
    show player 12
    player_name "Tidak?"

    show player 5
    show old_mia 10
    mia "TIDAK! Kita semua harus melakukan itu!"

    show old_mia 12
    mia "Baiklah semuanya kecuali {b}Roxxy{/b}... Dia tidak pernah mengerjakan pekerjaan rumahnya."

    show old_mia 7
    show player 14
    player_name "Saya tidak tahu. Tentang apa puisimu?"

    show player 13
    show old_mia 12
    mia "Oh, aku..."

    show old_mia 56 with dissolve
    mia "...Kau tahu, ini dan itu, hehe..."

    show old_mia 55
    show player 14
    player_name "Ya! Lihat, itu memalukan!"

    show player 13
    show old_mia 10 with dissolve
    mia "Ya, menurutku itu sedikit."

    show old_mia 7
    show player 10
    player_name "Aku bahkan tidak tahu bagaimana memulai menulis hal ini!"

    player_name "Saya mungkin harus mencari-cari buku tentang {b}Romansa Prancis{/b}..."

    show player 13
    show old_mia 10
    mia "Anda tahu, {b}Judith{/b} dan saya menemukan yang sangat informatif."

    show old_mia 7
    show player 10
    player_name "Ah, benarkah?"

    show player 13
    show old_mia 10
    mia "Ya, itu cukup grafis..."

    show old_mia 7
    show player 12
    player_name "Apakah Anda ingat apa namanya?"

    show player 13
    show old_mia 12
    mia "Hmm, tidak, tidak juga."

    show old_mia 10
    mia "{b}Judith{/b} terakhir kali melakukannya. Dia menggunakannya {b}di ruang belakang{/b} di sana, menurutku."

    show old_mia 7
    show player 10
    player_name "Hah, menurutmu dia mungkin meninggalkannya di sana?"

    show player 13
    show old_mia 10
    mia "Mungkin."

    show old_mia 7
    show player 14
    player_name "Kurasa aku akan pergi melihatnya. Terima kasih atas bantuannya, {b}Mia{/b}!"

    show player 13
    show old_mia 10
    mia "Tidak masalah! Selamat mencoba, {b}[firstname]{/b}!"

    show old_mia 7
    show player 14
    player_name "Kamu juga!"

    return

label mia_library_dialogue_bissette_mia_book_feedback:
    show old_mia 10 at right
    show player 13 at left
    with dissolve
    mia "Apakah beruntung menemukannya?"

    show old_mia 7
    show player 10
    player_name "Ya, aku menemukannya..."

    show player 14
    player_name "Anda tidak bercanda, ini sangat gamblang!"

    show player 13
    show old_mia 56 with dissolve
    mia "... Ya."

    show old_mia 55
    show player 10
    player_name "Aku penasaran apa yang {b}Judith{/b} lakukan sendirian di sana."

    show player 5
    show old_mia 56
    mia "Heh, y-ya, entahlah..."

    mia "... Aku harus kembali belajar."

    show old_mia 55
    show player 14
    player_name "Oh benar! Maaf!"

    player_name "Sekali lagi terima kasih, {b}Mia{/b}."

    show player 13
    show old_mia 56
    mia "Tidak masalah, {b}[firstname]{/b}."

    hide old_mia with dissolve
    show player 14
    player_name "Baiklah, sebaiknya saya {b}membawa ini pulang ke komputer saya dan mulai menulis puisi itu untuk Nona Bissette{/b}."

    return

label mia_library_dialogue_do_not_disturb:
    show player 10 with dissolve
    player_name "Tidak, aku harus membiarkan dia belajar dengan tenang..."

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
