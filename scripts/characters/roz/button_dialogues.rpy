label roz_dialogue_basement_priya:
    scene hospital_desk
    show old_roz 1 at left
    if Game.is_christmas():
        show xtra 35 zorder 2 at Position(xalign = 0.1, yalign = 0.251)
    show roz_desk at left
    show player 10f at right
    player_name "Saya ingin bertanya tentang ruang bawah tanah."

    show player 5f
    show old_roz 2
    roz "Itu dibatasi."

    show old_roz 1
    show player 12f
    player_name "Y-ya, aku tahu..."

    player_name "... Tapi saya berharap, mungkin, Anda bisa memberi tahu saya siapa yang punya akses?"

    show player 5f
    show old_roz 2
    roz "Tidak, itu dibatasi."

    show old_roz 1
    show player 12f
    player_name "... Tapi aku hanya perlu-"

    show player 5f
    show old_roz 2
    roz "Terbatas."

    show old_roz 1
    show player 35f
    player_name "Bisakah Anda menyukai halaman pertama dari dokter yang bekerja di sana?"

    player_name "Saya perlu berbicara dengan {b}Dokter Singh{/b}."

    show player 90f
    show old_roz 2
    roz "saya bisa."

    show old_roz 1
    pause
    player_name "..."
    show player 10f
    player_name "Maukah kamu?"

    show player 5f
    show old_roz 2
    roz "Tidak."

    show old_roz 1
    show player 15f
    player_name "Dengar, aku benar-benar perlu bicara dengannya."

    player_name "Ini sangat penting!"

    show player 16f
    show old_roz 2
    roz "Oh, aku tidak menyadari itu penting..."

    show old_roz 1
    pause
    show player 10f
    player_name "Jadi kamu akan melakukannya?"

    show player 5f
    show old_roz 2
    roz "... Tidak."

    show old_roz 1
    show player 15f
    player_name "Lalu kenapa kamu?!"

    show player 16f
    show old_roz 2
    roz "Itu dibatasi."

    show old_roz 1
    show player 37f with dissolve
    player_name "{i}*Huh*{/i}"

    show player 38f with dissolve
    player_name "Adakah yang bisa saya lakukan untuk mengubah pikiran Anda?"

    show player 90f with dissolve
    show old_roz 2
    roz "Batasi-"

    show old_roz 1
    pause
    show old_roz 2
    roz "Oh."

    roz "Hmm, aku meragukannya."

    show old_roz 1
    pause
    show player 25f
    player_name "Saya akan melakukan apa saja!"

    show player 24f
    show old_roz 2
    roz "Apa pun?"

    show old_roz 1
    show player 25f
    player_name "Secara harfiah. Apa pun."

    show player 24f
    roz "Hmm."

    show old_roz 2
    roz "Kamu pandai menggunakan kamera?"

    show old_roz 1
    show player 12f
    player_name "Kamera?"

    player_name "Ya, menurutku."

    show player 5f
    show old_roz 2
    roz "Saya mendapatkan yang baru ini dari toko dan barangnya tidak berfungsi."

    show old_roz 1
    show player 14f
    player_name "Saya mungkin bisa mengetahuinya!"

    show player 13f
    roz "Hmm."

    show old_roz 2
    roz "Ikuti aku kalau begitu."

    hide old_roz
    hide xtra 35
    with dissolve
    pause
    show player 4f
    player_name "( Wow, dia akan membawaku ke {b}ruang bawah tanah{/b} hanya untuk memperbaiki kameranya? )"

    player_name "(Bagaimana kalau begitu, aku akhirnya bisa istirahat.)"

    hide player with dissolve
    return

label roz_dialogue_basement:
    scene hospital_desk
    show old_roz 1 at left
    if Game.is_christmas():
        show xtra 35 zorder 2 at Position(xalign = 0.1, yalign = 0.251)
    show roz_desk at left
    show player 10f at right
    player_name "Saya ingin bertanya tentang ruang bawah tanah."

    show player 5f
    show old_roz 2
    roz "Itu dibatasi."

    show old_roz 1
    show player 12f
    player_name "Y-ya, aku tahu..."

    player_name "... Tapi saya berharap, mungkin, Anda bisa memberi tahu saya siapa yang punya akses?"

    show player 5f
    show old_roz 2
    roz "Tidak, itu dibatasi."

    show old_roz 1
    show player 12f
    player_name "... Tapi aku hanya perlu-"

    show player 5f
    show old_roz 2
    roz "Terbatas."

    return


label roz_dialogue_intro:
    scene hospital_desk
    show old_roz 1 at left
    if Game.is_christmas():
        show xtra 35 zorder 2 at Position(xalign = 0.1, yalign = 0.251)
    show roz_desk at left
    show player 14f at right
    with dissolve
    player_name "Hai!"

    show player 13f
    show old_roz 2
    roz "Ya?"

    roz "Apa yang bisa saya lakukan untuk Anda?"

    show old_roz 1
    return

label roz_dialogue_1st_floor:
    show player 12f
    player_name "Apa yang bisa saya temukan di lantai 1?"

    show player 5f
    roz "..."
    show old_roz 2
    roz "Itu lobi."

    show old_roz 1
    show player 10f
    player_name "Oh... Apakah ada hal lain?"

    show player 5f
    show old_roz 3 with dissolve
    roz "Apakah Anda melihat hal lain?"

    show old_roz 1 with dissolve
    show player 24f
    player_name "Saya kira tidak..."

    show player 25f
    show old_roz 2
    roz "Ada lagi yang bisa saya lakukan?"

    show old_roz 1
    show player 13f
    return

label roz_dialogue_2nd_floor:
    show player 12f
    player_name "Apa yang bisa saya temukan di lantai 2?"

    show player 5f
    show old_roz 2
    roz "Kami memiliki kamar sakit, dan ruang penyimpanan di lantai 2."

    show old_roz 1
    show player 12f
    player_name "Oh. Jadi begitu."

    show player 5f
    show old_roz 2
    roz "Ada lagi yang bisa saya lakukan?"

    show old_roz 1
    show player 13f
    return

label roz_dialogue_3rd_floor:
    show player 12f
    player_name "Apa yang bisa saya temukan di lantai 3?"

    show player 5f
    show old_roz 2
    roz "Itu lantai bersalin kami, di situlah Anda akan menemukan ruang pemulihan kami."

    show old_roz 1
    show player 12f
    player_name "Oke terima kasih."

    show player 5f
    show old_roz 2
    roz "Ada lagi yang bisa saya lakukan?"

    show old_roz 1
    show player 13f
    return

label roz_dialogue_schedule:
    show player 12f
    player_name "Apakah selalu ada seseorang di resepsi?"

    show player 5f
    show old_roz 2
    roz "Ya."

    roz "Saya selalu di sini."

    show old_roz 1
    show player 12f
    player_name "Anda tidak pernah meninggalkan meja Anda?"

    show player 5f
    show old_roz 2
    roz "Mengapa kamu bertanya?"

    show old_roz 1
    show player 10f
    player_name "Err... Hanya ingin tahu?"

    show player 5f
    show old_roz 2
    roz "Saya hanya meninggalkan meja saya jika terjadi keadaan darurat."

    show player 11f
    roz "Jika saya tidak menerima {b}panggilan telepon{/b}, saya tidak akan pergi."

    show old_roz 1 with dissolve
    show player 14f
    player_name "Oh. Jadi begitu."

    show player 13f
    show old_roz 2
    roz "Ada lagi yang bisa saya lakukan?"

    show old_roz 1
    return

label roz_dialogue_ancestory:
    show player 14f
    show old_roz 1
    player_name "{b}Roz{/b}! Aku perlu menanyakan sesuatu padamu."

    show player 11f
    show old_roz 2
    roz "Hmm, ya?"

    show old_roz 1
    show player 10f
    player_name "Saya mencoba mencari kuburan seseorang yang meninggal di kota ini, dahulu kala."

    show player 29f
    player_name "Saya pikir dia adalah semacam pembuat kapal."

    player_name "Apakah Anda punya ide tentang cara terbaik untuk menemukannya?"

    show player 3f
    show old_roz 2
    roz "Saya mungkin punya satu atau dua ide."

    show old_roz 1
    roz "..."
    show player 11f
    player_name "..."
    show player 12f
    player_name "Bisakah kamu memberitahuku?"

    show player 11f
    show old_roz 2
    roz "Saya mungkin bisa."

    show old_roz 1
    roz "..."
    show player 16f
    player_name "..."
    show player 30f
    player_name "{i}*Huh*{/i} Maukah Anda memberi tahu saya?"

    show player 16f
    show old_roz 2
    roz "Siapa nama orang ini?"

    show player 29f
    show old_roz 1
    player_name "Nah, itu masalahnya... Saya tidak tahu namanya."

    show player 11f
    show old_roz 2
    roz "Hmm..."

    roz "...Yah, itu membuat segalanya menjadi sulit, bukan?"

    show player 25f
    show old_roz 1
    player_name "... Ya."


    show player 24f
    show old_roz 2
    roz "Saya kira mungkin saja Anda bisa {b}menemukannya di catatan obituari lama{/b}."

    show player 11f
    roz "Sepertinya saya ingat ada beberapa orang yang profesinya tercantum di sana."

    show player 10f
    show old_roz 1
    player_name "Benar-benar?!"

    player_name "Kedengarannya menjanjikan!"

    show player 11f
    show old_roz 2
    roz "Masalahnya, ini akan merepotkan... aku menggali hal lama itu."

    show player 29f
    show old_roz 1
    player_name "Oh?"

    show player 3f
    show old_roz 2
    roz "Mungkin Anda bisa melakukan sesuatu agar hal ini bermanfaat bagi saya?"

    show player 29f
    show old_roz 1
    player_name "O-tentu saja!"

    show player 2f
    player_name "Izinkan saya melihat {b}catatan{/b} itu dan saya akan melakukan apa pun yang Anda inginkan!"

    show player 1f
    show old_roz 2
    roz "Hmm, apa saja?"

    show player 2f
    show old_roz 1
    player_name "Apa pun!"

    show player 1f
    roz "..."
    show old_roz 2
    roz "Baiklah, aku beritahu padamu apa..."

    roz "... {b}Bawa kunci sandi ini ke penyimpanan lantai 2{/b}."

    roz "Anda akan menemukan {b}sebuah kotak jelek di rak{/b}, sangat menarik perhatian, Anda tidak boleh melewatkannya."

    show player 2f
    show old_roz 1
    player_name "Kotak jelek, mengerti."

    show player 1f
    show old_roz 2
    roz "Pergilah {b}ambilkan saya kotak itu dan bawa kembali ke sini{/b}, sementara saya menggali catatan-catatan itu."

    show player 2f
    show old_roz 1
    player_name "Kedengarannya cukup mudah!"

    player_name "Saya akan kembali dalam sekejap!"

    hide player with dissolve

    show old_roz 2
    roz "Heh, tentu saja kamu akan bercanda. Tentu saja Anda akan melakukannya."

    return

label roz_dialogue_go_on_break:
    show player 14f
    show old_roz 1
    player_name "Aku ingin tahu apakah kamu ingin... Ya tahu, istirahatlah?"

    show player 13f
    show old_roz 2
    roz "ah..."

    roz "Masih belum puas dengan ole {b}Roz{/b} ya, Nak?"

    show old_roz 1
    player_name "..."
    show old_roz 2
    roz "Jangan khawatir, pesan sudah diterima."

    roz "Pergilah ke tempat penyimpanan dan saya akan segera menyusul..."

    roz "... Hanya perlu waktu sejenak untuk menyegarkan diri."

    show old_roz 1
    player_name "..."
    show player 14f
    player_name "T-tentu saja, aku akan menunggu di atas sana."

    show player 13f
    hide player with dissolve
    show old_roz 2
    roz "Itu anak yang baik..."

    return

label roz_dialogue_nothing:
    show player 14f
    player_name "Tidak, menurutku itu saja!"

    show player 13f
    show old_roz 2
    roz "Selamat tinggal."

    return

label roz_phone_prompt:
    scene expression player.location.background_blur
    show player 13f with dissolve
    player_name "(Saya tidak bisa meyakinkan dia untuk pergi dari sini.)"

    player_name "(Mungkin saya bisa meminta seseorang meneleponnya melalui interkom?)"

    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
