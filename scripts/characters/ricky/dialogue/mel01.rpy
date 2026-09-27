label mel01_hint_ricky:
    show ricky f_laugh
    show anon f_sad with dissolve:
        flip
    ricky "Fiuh, itu sulit untuk ditonton, amigo..."

    anon "Anda melihatnya, ya?"

    ricky f_normal "Dia benar-benar menyukaimu."

    anon "Ya."

    ricky a_finger "Jangan khawatir, kawan."

    ricky "Saya akan membantu Anda!"

    show ricky a_idle with dissolve
    anon f_shy "Saya akan sangat menghargainya."

    anon "Saya tidak tahu apa-apa tentang pemeliharaan bak mandi air panas."

    ricky "Ini sangat sederhana."

    ricky "Ayo, {b}ambil leaf skimmer{/b} di sana dan saya akan menunjukkannya kepada Anda."

    hide ricky
    show anon f_confused:
        unflip
        xoffset 500
    with {'master': dissolve}
    anon "{b}Peluncur daun{/b}?"

    anon f_worried "Y-ya, oke."

    hide anon with dissolve
    return


label mel01_find_ricky:
    show anon f_worried with dissolve
    ricky "Ada masalah, kawan?"

    anon "Umm, apa sebenarnya {b}leaf skimmer{/b} itu?"

    ricky @ f_laugh "Hehe, kamu serius?"

    ricky "Itu adalah jaring kecil pada sebatang tongkat."

    ricky @ a_finger_down "Di tanah, di sana."

    show anon f_worried_low
    pause .5
    anon f_normal_low "Oh, begitu."

    anon "Aku akan mengambilnya."

    ricky f_laugh "Go on, friend!" (show_native="Andale, amigo!")
    ricky "{b}Ny. Rump{/b} akan segera kembali."

    hide anon with dissolve
    return


label mel01_help_ricky:
    show anon a_net with dissolve:
        xoffset -150
    anon "Baiklah, saya punya {b}leaf skimmer{/b}."

    ricky "Bagus sekali, kawan."

    ricky "Sekarang, Anda hanya perlu menghilangkan semua hal buruk ini."

    show anon f_disgusted_low
    anon "Eh, apa-apaan ini..."

    ricky "Ya, Walikota pasti sangat bersenang-senang tadi malam..."

    anon "{b}Walikota Rump{/b} melakukan ini?"

    ricky "Dia suka bersantai di malam hari."

    anon "Menjijikkan sekali!"

    ricky @ f_laugh "Hehe, ini bukan apa-apa..."

    ricky f_smirk "... Kamu akan melihatnya setelah dia ditemani!"

    anon f_sad_down "Ah, kawan."

    ricky "Lihat sisi baiknya, ya?"

    ricky "Setidaknya bayarannya sangat buruk."

    anon @ -m_talk "..."
    ricky f_laugh "Hahahaah!"

    ricky "Hei, tidak ada yang bilang pekerjaan itu mudah, kawan."

    anon f_disgusted_low "Ya, tapi ini menjijikkan."

    ricky "Setelah Anda selesai melakukan skimming, saya akan mengajari Anda cara memeriksa level dan menyaring air."

    anon f_tired "{i}*Huh*{/i} Oke."

    ricky f_normal "Anda akan baik-baik saja."

    ricky "Jangan pikirkan itu."

    hide ricky with dissolve
    pause
    show anon b_dressed_back_cleaning a_net2 with dissolve:
        yoffset 155
    anon "Jangan pikirkan itu..."

    anon "... Temukan tempat bahagiamu."


    call minigame_hottub (1, 5)

    scene expression background(768, 368, 4.) as stage
    show location_rump_backyard_jacuzzi_overlay as hottubback:
        yoffset 140
    show location_rump_backyard_jacuzzi_overlay as hottub:
        yoffset 155
    show anon a_net_wipe f_tired:
        xoffset -150
    show ricky:
        xoffset 150
    with fade
    ricky "Hei, kelihatannya cukup bagus!"

    show anon a_net with dissolve
    pause
    ricky f_smirk "Ehh, kamu melewatkan satu tempat."

    anon @ -m_talk "Hmm?"

    ricky @ a_finger_tub "Di sana saja."

    show anon b_dressed_back_cleaning a_idle with dissolve:
        yoffset 155
    pause
    show anon b_dressed f_shock a_net_condom:
        yoffset 0
    anon "!!!" with hpunch
    show anon a_net_condom_fling with dissolve
    anon "UEGH!!!"

    show anon a_net f_surprised_teeth
    show ricky f_thinking:
        flip
        xoffset 600
    with dissolve
    pause
    ricky f_smirk @ -m_talk "Hmm."

    show ricky f_laugh with dissolve:
        xoffset 150
        unflip
    ricky "Jarak yang bagus!"

    show ricky f_smirk
    anon f_unimpressed a_net_sides "Ya terima kasih."

    anon f_disgusted "Kau tahu, aku telah melakukan beberapa hal yang cukup kacau dalam hidupku..."

    anon "... Tapi memancing kondom bekas dari bak mandi air panas milik walikota adalah sebuah level yang benar-benar baru."

    ricky f_sad "Bisa jadi lebih buruk lagi, kawan."

    anon "Saya tidak mengerti caranya."

    ricky f_smirk "Anda bisa berada di sini ketika dia menggunakannya."

    anon "Eh..."

    ricky @ f_laugh "Hahahaah!"

    anon "... Aku tidak membutuhkan gambaran itu di kepalaku, {b}Ricky{/b}!"

    ricky f_normal "Ayo, saya tunjukkan langkah selanjutnya."

    anon f_worried "Oke."

    show ricky b_pull_pants with dissolve:
        yoffset 50
    pause
    show ricky b_dressed a_chlorine with dissolve:
        yoffset 0
    ricky "Oke, di sinilah keajaiban terjadi..."

    anon @ f_confused "Apa itu?"

    ricky "Klorin, teman."

    show ricky a_chlorine_pour1 with dissolve
    pause
    anon f_disgusted_wince "Wah, kuat sekali!"

    ricky "Ya."

    show anon f_worried_low
    ricky "Ini lima kali lebih kuat dari biasanya."

    ricky "{b}Ny. Rump{/b} memesannya khusus dari Meksiko."

    anon f_worried "Ini membakar mataku..."

    ricky "Heh, iya... Hati-hati jangan terlalu banyak menghirupnya."

    ricky "Ini akan mengubah bagian dalam Anda menjadi menempel."

    anon f_surprised "!!!"
    anon "Apakah kamu serius?!"

    ricky @ f_laugh "Tentu saja tidak!"

    ricky "Kamu sangat mudah tertipu, amigo!"

    anon f_unimpressed @ -m_talk "..."
    pause
    anon "Sheesh, berapa banyak yang akan kamu tuangkan ke sana?"

    ricky "Tentu saja semuanya."

    ricky "Tidak ada hal yang berlebihan, percayalah."

    ricky a_chlorine_pour2 "Anda akan berterima kasih kepada saya nanti."

    anon "Hmm?"

    ricky a_hips @ a_chlorine_throw "Baiklah, ini waktunya untuk langkah terakhir."

    anon "Oke."

    show ricky b_dressed_back_jacuzzi with dissolve:
        yoffset 155
    ricky "Kita tinggal nyalakan jetnya dan beri waktu sekitar sepuluh menit untuk menyaring airnya."

    anon "Itu saja?"

    show ricky b_dressed with dissolve:
        yoffset 0
    ricky @ f_laugh "Itu dia!"

    ricky "Sepotong kue, ya?"

    anon "Ya, menurutku."

    melonia "{i}*Ehem*{/i}"

    show anon f_shock with dissolve:
        flip
        xoffset -250
    anon "!!!"
    show anon f_worried
    show melonia b_swimsuit f_normal with dissolve:
        flip
        xoffset -100
    melonia "Bagaimana kabarmu di sini, {b}Ricky{/b}?"

    ricky @ f_laugh "Ya, bagus sekali, Senora."

    ricky "Anak baru belajar dengan cepat."

    melonia @ f_annoyed -m_talk "Mhmm."

    melonia "Saya percaya dia bisa belajar tepat waktu mulai sekarang?"

    anon "Y-ya, Bu."

    melonia "Pastikan dia mendapat seragam yang pantas."

    ricky "Dengan senang hati, Bu."

    melonia "Dan saya ingin Anda tahu, {b}Hector{/b}, bahwa uang Anda untuk hari ini akan disalurkan ke {b}Ricky{/b}..."

    anon f_surprised @ -m_talk "Hmm?"

    melonia "... Karena dia harus meluangkan waktu untuk mengajari Anda cara melakukan pekerjaan Anda."

    ricky f_confused a_up "T-tidak, tidak apa-apa..."

    ricky "... Dia melakukan sebagian besar pekerjaan."

    show ricky a_idle with dissolve
    melonia f_annoyed "Omong kosong!"

    melonia "Saya tidak akan memberi penghargaan kepada salah satu karyawan saya atas keterlambatan dan ketidakmampuannya!"

    anon f_worried_left "Tidak apa-apa, {b}Ricky{/b}."

    anon "Saya tidak peduli."

    ricky "Ehh."

    show anon f_worried
    melonia "Kembalilah dan temui aku setelah kamu selesai dengannya."

    melonia a_shoulder "Aku ingin kamu bekerja di pundakku lagi."

    ricky f_normal "Ya, señora."

    show melonia a_idle with dissolve
    show anon f_worried_left
    ricky a_finger "Ayo, teman-teman."

    ricky @ f_laugh "Sudah waktunya bagi Anda untuk naik tempat tidur gantung!"

    hide ricky with dissolve
    show melonia f_smirk
    anon f_worried "B-tempat tidur gantung?"

    hide anon with dissolve
    show melonia f_smirk_down
    pause

    scene expression background(304, 448, 3.) as stage
    show anon f_worried:
        flip
    show ricky a_finger:
        flip
    with fade
    ricky "Sekarang, kami harus menemukan tempat tidur gantung yang sempurna untuk Anda!"

    anon "{b}Ricky{/b}, menurutku tidak-"

    ricky "Percayalah padaku, temanku!"

    ricky "Anda akan terlihat luar biasa!"

    show ricky f_laugh a_pocket with dissolve
    anon f_worried_low "Ehh, apa yang kamu-"

    ricky a_hammock_bunch f_smirk "Manjakan matamu, amigo!"

    anon f_surprised_low a_up "!!!"
    anon f_worried a_sides "Apakah Anda hanya membawanya kemana-mana sepanjang hari?"

    ricky f_confused "Ya?"

    pause
    ricky f_smirk "Saya ingin membiarkan pilihan saya tetap terbuka."

    ricky @ f_smirk_wink "Prajurit Aztec kecilku suka memakai aksesori!"

    anon @ a_facepalm f_sad_down -m_talk "..."
    ricky "Jadi yang mana?!"

    anon f_worried_low "Sobat, aku tidak tahu..."

    ricky "Secara pribadi, menurut saya yang berwarna merah muda akan terlihat sangat bagus."

    ricky @ f_laugh "Dan rendanya akan terasa nyaman di paket Anda."

    anon f_worried "Tidak ada warna merah muda."

    ricky f_confused "Kalau begitu yang ungu?"

    show anon f_tired
    ricky f_smirk @ f_smirk_wink "{b}Ny. Bokong{/b} tidak akan mampu menahan bola-bola berbulu halus itu ya?"

    anon f_unimpressed @ -m_talk "..."
    ricky @ f_laugh "Mereka akan menghipnotisnya saat Anda bekerja."

    anon f_worried_low "Ehh, menurutku itu... Agak terlalu..."

    ricky "Luar biasa?"

    anon "... Flamboyan..."

    show ricky f_sad
    anon f_worried "... Untukku."

    ricky "Mari kita sepakat untuk tidak setuju mengenai hal itu."

    anon f_worried_low "Mungkin yang hijau?"

    ricky f_confused "Anda ingin yang hijau?"

    ricky "Tapi itu sangat polos dan membosankan?"

    ricky "aku belum pernah memakainya sekali pun..."

    anon f_surprised @ f_laugh "SEMPURNA!"

    show ricky f_sad
    anon "Eh, maksudku..."

    anon f_worried "{i}*Ahem*{/i} Saya rasa saya akan ehh... Cobalah yang itu."

    ricky @ -m_talk "..."
    ricky a_hammock_bunch_shrug "Sesuaikan dirimu."

    show ricky a_idle
    show anon a_hammock
    with dissolve
    anon f_worried_low "Terima kasih."

    anon "Saya rasa..."

    ricky f_smirk "Sekarang, mari kita lihat apakah cocok."

    anon f_surprised "Apa sekarang?"

    ricky "Tidak ada waktu seperti sekarang."

    anon f_disgusted "Ehh... T-tidak, tidak apa-apa."

    show anon a_backpack f_looking_down with dissolve
    pause
    anon f_worried a_idle "Saya pikir saya akan menyimpannya untuk lain kali."

    ricky f_sad "Aww, kamu cukup menggoda, amigo."

    anon @ -m_talk "..."
    melonia "{b}Ricky{/b}!!"

    show anon f_surprised
    melonia "Tidak bijaksana membuatku menunggu!!"

    ricky a_whisper f_normal "Ya, señora!"

    ricky a_idle "Lain kali saja."

    ricky "Hati-hati, kawan."

    anon f_normal "Y-ya, sampai jumpa, {b}Ricky{/b}."

    hide ricky
    show anon a_wave:
        unflip
        xoffset 500
    with {'master': dissolve}
    ricky "Ini aku datang, señora!"

    show anon a_backpack2 f_looking_down with dissolve:
        flip
        xoffset 0
    pause
    anon a_hammock f_worried_low @ -m_talk "..."
    anon f_sad_down "{i}*Huh*{/i} Apa yang telah aku lakukan?"

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
