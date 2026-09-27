label button_dexter_talent_show:
    show old_dexter 1
    show player 10
    player_name "Hai {b}Dexter{/b}, kamu main alat musik apa saja?"

    show player 5
    show old_dexter 2
    dexter "Hah?"

    show player 12
    player_name "DALAM-S-T-R-U-M-E-N-T-S. Anda tahu, suka musik... Apakah Anda memainkannya?"

    show player 5
    show old_dexter 8
    dexter "Apa aku terlihat seperti penggila band di matamu?!"

    show old_dexter 2
    show player 12
    player_name "Eh, bukan? Saya hanya berpikir mungkin Anda memiliki bakat terpendam dalam memukul drum atau semacamnya?"

    show player 5
    show old_dexter 6 with dissolve
    dexter "Aku ingin memukul wajah bodohmu dengan tinjuku..."

    dexter "Menurutmu itu akan menghasilkan musik?"

    show old_dexter 5
    show player 29 with dissolve
    player_name "Hehe, aku baru saja pergi..."

    show player 3
    show old_dexter 4 with dissolve
    dexter "Ya, kamu lebih baik!"

    return

label button_dexter_challenge:
    show player 12
    player_name "Saya di sini untuk menantang Anda, {b}Dexter{/b}."

    show player 5
    show old_dexter 3
    dexter "Haha!"

    dexter "Untuk apa?!"

    show old_dexter 1
    show player 10
    player_name "Untuk eh..."

    show player 5
    show old_dexter 3
    dexter "Kau tahu aku akan mengalahkanmu dalam hal apa pun."

    show old_dexter 4 with dissolve
    dexter "Sekarang pergilah sebelum aku memutuskan untuk menghajarmu habis-habisan."

    return

label button_dexter_library_book:
    show player 10
    player_name "Hei, umm, {b}Dexter{/b}..."

    show player 5
    show old_dexter 3
    dexter "Apa yang kamu inginkan, twerp?"

    show old_dexter 1
    show player 10
    player_name "Apakah Anda ingat di mana Anda meninggalkan buku perpustakaan yang Anda periksa..."

    show player 5
    show old_dexter 8
    dexter "Buku perpustakaan?"

    show old_dexter 4 with dissolve
    dexter "Bukankah aku sudah bilang padamu untuk keluar dari sini, {b}[firstname]{/b}?"

    dexter "Atau apakah Anda ingin sandwich buku jari!"

    show old_dexter 2 with dissolve
    show player 12
    player_name "Baiklah, baiklah, aku berangkat!"

    hide old_dexter with dissolve
    show player 10f at center with dissolve
    player_name "Saya ingin tahu apakah pustakawan melakukan kesalahan?"

    show player 5f
    player_name "..."
    show player 12f
    player_name "Dia bisa saja berbohong. {b}Saya harus memeriksa lokernya{/b}!"

    player_name "Mudah-mudahan ada di sana, jika tidak, saya tidak tahu apa yang harus saya lakukan..."

    return

label button_dexter_nothing:
    show player 10
    player_name "Aku... Uhh... Tidak bermaksud mengganggumu."

    player_name "Aku harus pergi ke kelas."

    show player 5
    show old_dexter 3
    dexter "Larilah, pecundang."

    return

label dexter_button_pushups:
    show player 16 at left
    show old_dexter 12 at right
    with dissolve
    dexter "Oh, kamu ingin pertandingan ulang ya?"

    dexter "Tidak masalah, kutu buku!"

    dexter "Saya akan menunjukkan cara melakukannya!"

    show old_dexter 11
    scene gym
    show player 16 at left
    show old_dexter 11 at right
    with dissolve
    bridget "Baiklah, teman-teman. Anda tahu latihannya!"

    bridget "Orang terakhir yang bertahan menang!"

    show old_dexter 12
    dexter "Hahaha, tonton dan pelajari... NERD!"

    hide player
    hide old_dexter
    with dissolve
    bridget "PERGI!"

    return

label dexter_button_pushups_rematch:
    show player 5 at left
    show old_dexter 15 at right
    with dissolve
    dexter "Bagaimana kalau pertandingan ulang, kutu buku?!"

    show old_dexter 14
    show player 12
    player_name "Apa?! Ayo kawan... Kamu kalah."

    player_name "Lanjutkan saja."

    show player 5
    show old_dexter 12 with dissolve
    dexter "Psh, kamu takut kalah?"

    show old_dexter 11
    show player 12
    player_name "Tidak."

    show player 90
    show old_dexter 28 with dissolve
    dexter "{b}[firstname]{/b}itu seekor ayam, semuanya!"

    show old_dexter 11 with dissolve
    show player 12
    player_name "... Cih, baiklah."

    player_name "Ayo lakukan!"

    hide player
    hide old_dexter
    with dissolve
    return

label button_dexter_intro_beginning:
    show anon f_worried
    show dexter
    with dissolve
    dexter "Apa yang kamu lihat, pecundang?!"

    anon "Tidak ada apa-apa."

    dexter "Ya itu benar!"

    dexter "Teruslah berjalan, jalang!"

    dexter @ f_laugh "Ha ha ha ha!"

    hide dexter with dissolve
    anon f_angry "Ugh, dia benar-benar brengsek..."

    hide anon with dissolve
    return

label button_dexter_intro:
    show player 5 at left
    show old_dexter 3 at right
    with dissolve
    dexter "Kupikir aku berbau sedikit menyebalkan!"

    show old_dexter 2
    show player 12
    player_name "Persetan denganmu, {b}Dexter{/b}..."

    show player 90
    show old_dexter 6 with dissolve
    dexter "APA YANG KAMU BILANG?!"

    show old_dexter 4 with dissolve
    show player 11
    dexter "Kamu ingin aku menjatuhkanmu, kan?!"

    show old_dexter 2 with dissolve
    player_name "..."
    show old_dexter 3
    dexter "Ya, itulah yang saya pikirkan."

    show old_dexter 6 with dissolve
    dexter "Sebaiknya kau menjauh dari gadisku!"

    show old_dexter 2 with dissolve
    show player 5
    player_name "..."
    show old_dexter 4 with dissolve
    dexter "Kamu mendengarku, jalang?!"

    show old_dexter 2 with dissolve
    return

label button_dexter_intro_final:
    show player 90 at left
    show old_dexter 2 at right
    with dissolve
    dexter "..."
    show player 12
    player_name "Maaf, apakah Anda mengatakan sesuatu, {b}Dexter{/b}?"

    show player 91
    show old_dexter 8
    dexter "Tidak!"

    show old_dexter 2
    show player 12
    player_name "Ya, itulah yang saya pikirkan."

    show player 91

    dexter "..."
    return

label button_dexter_basketball_final:
    show player 12
    player_name "Masih bermain basket?"

    show player 91
    dexter "..."
    show player 12
    player_name "Apakah kalian sudah berhasil memenangkan permainan?"

    show player 91
    show old_dexter 8
    dexter "Saya tidak ingin membicarakannya!"

    show old_dexter 2
    show player 12
    player_name "Aku hanya mencoba untuk-"

    show player 11
    show old_dexter 8
    dexter "Tinggalkan aku sendiri, {b}[firstname]{/b}!"

    hide old_dexter with dissolve
    pause
    show player 10
    player_name "Astaga, baiklah."

    hide player with dissolve
    return

label button_dexter_basketball:
    show player 12
    player_name "Masih bermain basket?"

    show player 90
    show old_dexter 3
    dexter "Tentu saja, saya dilahirkan untuk bermain!"

    show old_dexter 1
    show player 12
    player_name "Apakah Anda sudah memenangkan pertandingan?"

    show player 90
    show old_dexter 3
    dexter "Ya ampun. Seperti seratus juta..."

    show old_dexter 1
    show player 12
    player_name "Ya benar! Kalian mengerikan..."

    show player 90
    show old_dexter 4 with dissolve
    dexter "HEI! Kamu ingin sandwich buku jari, pecundang?!"

    show old_dexter 2 with dissolve
    player_name "..."
    show old_dexter 3
    dexter "Lagipula, apa yang diketahui wanita jalang sepertimu tentang bola basket?!"

    dexter "Itu olahraga pria!"

    show old_dexter 1
    show player 17
    player_name "Oh, kalau begitu, tidak heran kenapa kalian para wanita tidak bisa memenangkan pertandingan."

    show player 13
    show old_dexter 3
    dexter "Hah? aku tidak-"

    dexter "Oh, menurutmu itu lucu?!"

    show old_dexter 8
    dexter "Bagaimana kalau aku mencabut beberapa gigimu?!"

    show player 5
    dexter "Itu akan sangat lucu, bukan?!"

    show old_dexter 2
    return

label button_dexter_whatever:
    show player 12
    player_name "Cih, ya. Terserahlah kawan..."

    hide player with dissolve
    pause
    show old_dexter 8
    dexter "Hei, aku tidak bercanda {b}[firstname]{/b}!"

    dexter "Jauhi {b}Roxxy{/b}!"

    dexter "Dia milikku!"

    hide old_dexter
    hide player
    with dissolve
    return

label button_dexter_behaving:
    show player 12
    player_name "Saya yakin Anda berperilaku baik."

    show player 90
    show old_dexter 8
    dexter "... Ya."

    show old_dexter 2
    show player 12
    player_name "Kamu ingat apa yang terjadi jika aku memergokimu sedang bermain-main dengan teman-temanku lagi, kan?"

    show player 92
    player_name "Apakah Anda memerlukan pengingat?!"

    show player 91
    show old_dexter 8
    dexter "TIDAK!"

    dexter "saya ingat..."

    show old_dexter 2
    show player 92
    player_name "Bagus."

    show player 91
    return

label button_dexter_run_along:
    show player 12
    player_name "Jalankan sekarang, {b}Dexter{/b}."

    show player 91
    dexter "..."
    show old_dexter 8
    dexter "GRRRR!!!"

    hide old_dexter with dissolve
    pause
    show player 17
    player_name "Ha ha ha!"

    player_name "Saya suka {b}Dexter{/b} yang baru!"

    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
