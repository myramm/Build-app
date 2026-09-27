label micoe_dialogue_blowjob:
    scene expression "backgrounds/location_hospital_room_day_blur.jpg"
    show player 10 at left
    show micoe:
        flip
    with dissolve
    player_name "Ingat ketika Anda membantu saya... Umm, ekstrak sampel saya untuk pengujian."

    show player 5
    show micoe f_sexy
    micoe "Maksudmu, saat aku menghisap penismu di kamar mandi?"

    show player 11
    player_name "!!!"
    show player 29 with dissolve
    player_name "Y-ya."

    show player 3
    micoe @ f_laugh "Hehehe, menurutku kita sudah tidak perlu malu lagi, {b}[firstname]{/b}."

    micoe "Anda di sini untuk memberi saya rasa lagi?"

    show player 17 with dissolve
    player_name "Eh ya."

    hide player
    show micoe b_pulling
    with dissolve
    micoe "Ayo manis."

    $ player.go_to(L_hospital_room_bathroom)
    scene expression player.location.background_blur
    show player 13f at right
    show micoe f_sexy
    with dissolve
    micoe "Apa yang kamu tunggu?"

    micoe "Keluarkan ayam itu!"

    show player 14f
    player_name "O-oke."

    show player 261b with dissolve
    pause
    show player 263b at Position (xoffset=-150)
    show micoe b_knees
    with dissolve
    pause
    show micoe b_knees_talk
    micoe "Mmm, aku akan menghisap ayam cantik ini kapan saja kamu mau, {b}[firstname]{/b}!"

    $ M_micoe.set('sex speed', .12)
    $ anim_toggle = True
    $ animated = True
    scene expression player.location.background_closeup
    show expression AnimatedImage("micoe_bj", [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], M_micoe) as micoe_bj at Position(xalign = 0.0, yoffset = 0)
    with dissolve
    micoe "{i}*Menyeruput*{/i}"

    player_name "Ya Tuhan..."

    player_name "Rasanya luar biasa, {b}Micoe{/b}."

    micoe "Mmhmm!"

    return

label micoe_dialogue_goodbye:
    show player 14 at left
    show micoe:
        flip
    player_name "Hanya menyapa."

    show player 13
    show micoe f_sad
    micoe "Ah, itu mengecewakan..."

    show micoe f_sexy
    micoe "Saya pikir mungkin Anda di sini untuk bersenang-senang."

    show player 14
    player_name "Maaf."

    show player 13
    pause
    show player 14
    player_name "Sampai jumpa, oke?"

    show player 13
    show micoe f_normal
    micoe "Baiklah, manis."

    hide player
    hide micoe
    with dissolve
    return

label micoe_dialogue_intro:
    scene expression player.location.background_blur with None
    show player 13 at left
    show micoe:
        flip
    micoe "Hai, manis."

    micoe "Kamu tersesat?"

    return

label micoe_dialogue_increase_chance_of_conception:
    show micoe:
        flip
    show player 10 at left
    with dissolve
    player_name "Apakah ada hal lain yang bisa saya lakukan untuk membantu teman saya?"

    player_name "{i}*Ahem*{/i} Maksudku, membantu pacarku mengandung bayi?"

    show player 5
    show micoe f_normal
    micoe "Hmm, apakah dia stres karenanya?"

    show player 10
    player_name "Ehh, tidak juga..."

    player_name "Saya hanya ingin memastikan saya melakukan semua yang saya bisa untuk membantunya."

    show player 5
    micoe @ f_laugh "Aduh, kamu manis sekali!"

    show player 13
    micoe "Nah, apakah kalian berdua sering berhubungan seks?"

    show player 29 with dissolve
    player_name "Y-ya."

    show player 13 with dissolve
    micoe "... Dan posisi apa yang kamu gunakan?"

    show player 10
    player_name "... Posisi?"

    show player 5
    show micoe f_sexy
    micoe "Ya, di posisi apa kamu berhubungan seks?"

    show player 10
    player_name "Eh, entahlah."

    show player 14
    player_name "Kurasa aku biasanya berada di belakangnya..."

    show player 13
    micoe "Gaya anjing?"

    show player 5
    player_name "..."
    show micoe f_laugh
    micoe "Hehe, kamu lucu sekali!"

    show micoe f_normal
    micoe "Gaya doggy seharusnya berfungsi dengan baik untuk pembuahan."

    show player 13
    micoe "Banyak dokter yang merekomendasikannya, karena memungkinkan penetrasi yang paling dalam."

    show micoe f_wink
    pause
    show micoe f_sexy
    micoe "Namun, dengan apa yang Anda bawa, penetrasi yang dalam tidak akan menjadi masalah."

    show player 29 with dissolve
    player_name "Hehe, y-ya..."

    show player 13 with dissolve
    show micoe f_normal
    micoe "Anda bisa mencoba posisi misionaris."

    show player 10
    player_name "Apa itu?"

    show player 13
    micoe "Saat itulah wanita berbaring telentang dan Anda berada di atas."

    micoe "Dalam posisi tersebut, gravitasi akan membantu membawa air mani Anda ke leher rahim."

    show player 17
    player_name "Ohh, aku mengerti! Gaya biasa."

    show player 18
    show micoe f_sad
    pause
    show player 14
    player_name "Itu masuk akal."

    show player 13
    pause
    show player 14
    player_name "Ada lagi?"

    show player 13
    show micoe f_normal
    micoe @ -m_talk "Hmm."

    micoe "Tidak juga."

    micoe "Sayangnya, rintangan terbesar dalam situasi Anda adalah usia pacar Anda."

    show player 10
    player_name "Ya."

    show player 5
    pause
    show player 10
    player_name "Apakah Anda yakin tidak ada lagi yang bisa saya lakukan untuk membantu?"

    show player 5
    micoe "Ya..."

    show micoe f_look_back
    pause
    show micoe f_normal
    micoe "Ada satu hal... Tapi aku tidak seharusnya membicarakannya."

    show player 12
    player_name "Hah?"

    player_name "Kenapa?"

    show player 5
    pause
    show player 14
    player_name "Jika ada kemungkinan itu akan membantu, saya benar-benar harus mengetahuinya!"

    player_name "{b}Diane{/b} benar-benar ingin hamil."

    show player 13
    pause
    show player 18
    player_name "Silakan?"

    micoe @ f_laugh "Ngh, kamu manis sekali!"

    show player 13
    micoe "Baiklah, aku akan memberitahumu... Tapi kamu tidak mendengar ini dariku!"

    micoe "Memahami?"

    show player 14
    player_name "Y-ya, aku mengerti!"

    show player 13
    micoe "Ada obat baru yang menunjukkan banyak harapan dalam meningkatkan angka pembuahan."

    micoe "Mereka menyebutnya {b}Pregnax{/b}."

    show player 14
    player_name "Kedengarannya sempurna!"

    show player 12
    player_name "Apa menariknya?"

    show player 5
    micoe "Nah, masalahnya adalah mereka masih dalam tahap pengujian."

    pause
    show player 14
    player_name "Tidak apa-apa, saya tidak keberatan membantu Anda mengujinya."

    show player 13
    micoe @ f_laugh "Hehe, Anda harus bicara dengan {b}Dr. Singh{/b} tentang itu."

    show player 10
    player_name "{b}Dr. Singh{/b}?"

    show player 5
    micoe "Ya, {b}Singh{/b} adalah dokter bercelana mewah baru yang mereka kirimkan dari suatu tempat di luar negeri."

    micoe "Bekerja di {b}basement{/b}."

    micoe "Telah mengembangkan {b}Pregnax{/b} selama bertahun-tahun sekarang."

    show player 14
    player_name "Oke, jadi aku akan pergi dan berbicara dengannya!"

    show player 13
    show micoe f_sad
    micoe "Heh, kuharap semudah itu."

    micoe "Sayangnya, {b}basement{/b} adalah area terlarang."

    micoe "Bahkan saya tidak memiliki akses ke sana."

    show micoe f_normal
    show player 12
    player_name "Jadi bagaimana cara mendapatkan akses?"

    show player 5
    micoe "Aku tidak bisa membantumu di sana, manis."

    micoe "Tidak banyak orang di rumah sakit yang memiliki izin untuk turun ke ruang bawah tanah."

    show player 24
    player_name "Omong kosong."

    pause
    show player 10
    player_name "Baiklah, terima kasih infonya {b}Micoe{/b}."

    show player 5
    show micoe f_laugh
    micoe "Tidak masalah, manis!"

    show micoe f_sexy
    micoe "Jangan ragu untuk datang dan menemui saya jika Anda memiliki pertanyaan lagi..."

    show player 13
    show micoe f_wink
    pause
    show micoe f_sexy
    micoe "... Atau Anda ingin bersenang-senang nakal!"

    show player 29 with dissolve
    player_name "Y-ya, oke."

    show player 3
    micoe "Hmm, menggemaskan sekali..."

    hide player
    hide micoe
    with dissolve
    return

label micoe_dialogue_pregnax:
    scene expression "backgrounds/location_hospital_room_day_blur.jpg"
    show player 10 at left
    show micoe:
        flip
    with dissolve
    player_name "Di mana saya bisa menemukan obat kesuburan itu lagi?"

    show player 5
    show micoe f_sad a_shh with dissolve:
        xoffset -175
    micoe "Ssst!"

    micoe "Tidak terlalu keras!"

    show micoe f_normal a_idle with dissolve
    show player 10
    player_name "Oh maaf."

    show player 5
    micoe "Mereka menyimpannya di {b}basement{/b}."

    show player 14
    player_name "{b}Ruang bawah tanah{/b}, mengerti!"

    show player 13
    micoe "Tunggu, kamu tidak bisa melenggang begitu saja di sana."

    micoe "Anda harus {b}menemukan seseorang yang memiliki akses{/b} untuk mengantar Anda."

    show player 10
    player_name "Hmm, siapa yang bisa kutanyakan?"

    show player 5
    micoe "Maaf sayang, aku tidak bisa membantumu dengan itu."

    micoe "Ingat saja, Anda tidak mendengar semua ini dari saya!"

    show player 14
    player_name "Jangan khawatir, saya tidak akan memberi tahu."

    show player 18
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
