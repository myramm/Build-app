label ano07_hint_josie:
    if M_anon.is_state(S_ano07_mech):
        jump ano07_hint_josie.help

    if M_anon.is_state(S_ano07_find):
        jump ano07_hint_josie.find

    if M_anon.is_state(S_ano07_give):
        jump ano07_hint_josie.give

    if M_anon.is_state(S_ano07_perk):
        jump ano07_hint_josie.perk

    return


label ano07_hint_josie.help:
    anon f_normal "Tentang foto-foto pribadi itu."

    josephine f_normal "Sudahkah Anda berbicara dengan {b}Jiang{/b} tentang masalah kecil saya?"

    anon f_worried "Saya masih mengerjakannya..."

    pause
    anon f_normal "Anda bilang dia kepala mekanik di dealer ini?"

    josephine @ a_point_back "Ya, dia seharusnya {b}di garasi{/b} di belakangku."

    anon "Baiklah, aku akan berbicara dengannya."

    hide anon with dissolve
    return


label ano07_hint_josie.find:
    anon f_normal "Tentang foto-foto pribadi itu."

    josephine f_normal "Sudahkah Anda berbicara dengan {b}Jiang{/b} tentang masalah kecil saya?"

    anon f_worried "Ya, saya pikir dia akan membantu."

    anon @ f_unimpressed -m_talk "(Tetapi hanya sekali saya menemukan tas perkakas keberuntungannya!)"

    pause
    anon f_normal "Saya yakin foto-foto itu akan terhapus dalam waktu singkat."

    josephine f_concerned "Ya..."

    anon "Saya akan kembali segera setelah saya mendapat kabar."

    hide anon with dissolve
    return


label ano07_hint_josie.give:
    anon f_normal "Tentang foto-foto pribadi itu."

    josephine f_surprised "Anda mendapatkannya?!"

    anon f_worried "Belum, tapi saya sedang dalam perjalanan untuk melapor masuk dengan {b}Jiang{/b} sekarang."

    show josephine f_angry_up
    anon @ f_shy -m_talk "(Tas perkakas keberuntungan ada di belakangnya!)"

    pause
    josephine f_concerned "Ya? Apa yang kamu tunggu?"

    anon "T-tidak ada. Segera kembali!"

    hide anon with dissolve
    return


label ano07_hint_josie.perk:
    anon f_shy_low "Tentang foto-foto pribadi itu."

    josephine @ -m_talk "..."
    show anon f_worried_low
    pause
    anon f_unimpressed @ a_wave "{b}Yosephine{/b}! Foto-fotonya?"

    josephine f_angry_down "Bung, streaming."

    josephine "Ssst."

    show josephine f_normal_down
    anon "Ugh."

    anon @ -m_talk "(Saya kira saya akan memberitahunya kabar baik nanti...)"

    hide anon with dissolve
    return


label ano07_perk_josie:
    show josephine:
        xoffset 100
    show anon with dissolve:
        xoffset 100
    anon "Aku menghapus foto-foto itu dari ponsel {b}Kim{/b} untukmu."

    show josephine b_dressed f_surprised with fastdissolve:
        xoffset 0
    josephine "Mustahil!"

    josephine "Benar-benar?"

    anon "Ya."

    anon "Semuanya sudah diurus."

    josephine f_shy "Sialan."

    josephine "Saya tidak percaya Anda benar-benar berhasil melakukannya!"

    pause
    josephine "Kurasa, aku berhutang banyak padamu..."

    pause
    josephine f_sexy "Heh, apa yang harus aku lakukan untuk membalas budimu?"

    anon "Yah, aku masih butuh bantuan untuk menemukan mobil itu untuk-"

    josephine "Ikutlah denganku!"

    show xtra3 as counter behind josephine
    show anon b_pulling5 f_worried_left behind josephine:
        xoffset -152
    show josephine b_empty:
        xoffset -768
    with {'master': dissolve}
    anon "Apa yang-"

    hide anon
    hide josephine
    with dissolve

    $ player.go_to(L_dealership_lounge)
    scene expression background(472, 360, 1.8) with fade
    show josephine a_hips f_sexy
    show anon f_worried
    with dissolve
    anon "Apa yang terjadi?"

    josephine "Aku memberimu hadiahmu, ya!"

    anon "Eh, oke?"


    if M_josie.peeked:
        josephine "Tunggu sebentar."

        josephine f_concerned "Anda tidak melihat fotonya, bukan?"


        menu:
            "Ya, sedikit.":

                anon "Ya, sedikit."

                josephine f_angry "Eh, serius?"

                anon f_shy @ a_behind_head "Saya tidak bisa menahannya."

                anon "Saya penasaran."

                josephine a_crossed "Baiklah, AKU akan menghadiahimu dengan pertunjukan pribadi, tetapi karena kamu sudah menghadiahi dirimu sendiri..."

                anon f_worried "Saya benar-benar minta maaf."

            "Apa?! Tentu saja tidak!":

                anon f_shy "Apa?! Tentu saja tidak!"

                show anon f_grin
                josephine @ -m_talk "..."
                josephine f_angry a_crossed "Kamu pembohong!"

                anon f_worried "Hah?"

                josephine "Kamu benar-benar berbohong padaku sekarang!"

                anon "T-tidak, aku tidak..."


        josephine @ f_eyeroll "Terserahlah, kawan."

        josephine "Sayang sekali karena aku merasa cukup murah hati untuk membiarkanmu pergi langsung..."

        anon f_sad_down "Aduh, bung!"

        josephine "Mungkin lain kali kamu akan-"

    else:

        josephine "Sekarang ingatlah bahwa saya melakukan ini hanya karena Anda membantu saya hari ini dan saya benar-benar sekarat karena bosan dengan pekerjaan ini..."

        anon f_confused "Melakukan apa sebenarnya?"

        josephine a_flash2 @ a_flash1 "Apa pendapatmu tentang ini, potongan mangkuk?"

        anon f_shock "!!!"
        anon f_flirt_low "I-itu bagus sekali."

        josephine "Benar?"

        pause
        josephine "Anda ingin menyentuhnya?"

        anon f_shy "{i}*Gulp*{/i} Apakah Anda yakin?"

        josephine "Tentu saja aku yakin, aku menawarkannya bukan?"

        anon f_flirt_low "Ya baiklah."

        show anon b_empty:
            xoffset 357
            yoffset 22
        show josephine b_dressed_fondle a_idle
        with dissolve
        pause
        anon "Wow, mereka sangat bersemangat!"

        josephine f_concerned "Apa yang kamu lakukan?"

        show josephine a_squeeze1 with dissolve
        anon f_worried "Hah?"

        josephine "Itu bukan tombol radio, tahu?!"

        anon f_worried_low "Oh, uhh... Maaf."

        show josephine a_idle f_normal with dissolve
        show anon f_flirt_low
        pause
        anon "Aku suka putingmu, sangat kecil dan imut!"

        josephine "Yah, saya tidak yakin saya menghargai komentar kecil itu tetapi saya akan mengakui hal yang lucu itu..."

        pause
        josephine "Anda ingin mencicipi-"


    show anon b_dressed a_up f_surprised behind josephine:
        flip
        xoffset -150
        yoffset 0
    if not M_josie.peeked:
        show josephine b_dressed a_flash2 f_surprised
    with dissolve
    sato "{b}Yosephine{/b}!!!"

    show anon a_sides f_surprised_teeth
    if not M_josie.peeked:
        show josephine a_cover
    with dissolve
    josephine f_concerned "Ayah?!"

    show sato f_angry a_hips with dissolve:
        flip
    sato "Apa yang kamu lakukan di sini!"

    josephine a_hips "Aduh Buyung."

    josephine "Kamu telah memergokiku lagi, lagi..."

    josephine "Apakah kebobrokanku tidak ada habisnya?!"

    josephine "Anda pasti harus memecat saya kali ini-"

    sato "Ini bukan waktu istirahat yang dijadwalkan, nona muda!"

    show anon f_confused
    show josephine f_surprised m_talk
    pause
    josephine "I-itulah yang membuatmu marah?!"

    if M_josie.peeked:
        josephine "Saya baru saja akan membiarkan pelanggan ini merasakan saya dan Anda marah karena saya tidak ada di meja depan!"

    else:
        josephine "Saya membiarkan pelanggan ini merasakan saya dan Anda marah karena saya tidak ada di meja depan!"

    show josephine -m_talk
    sato "Saya tidak punya waktu untuk bercanda saat ini, {b}Josephine{/b}!"

    show anon f_worried
    josephine "Tapi aku-"

    sato "Anda memiliki tanggung jawab terhadap perusahaan ini dan saya berharap Anda menanggapinya dengan serius!"

    show josephine a_crossed f_pouting with dissolve
    sato "Sekarang kembalilah ke bawah dan pastikan kebutuhan pelanggan kami terpenuhi saat ini juga!"

    josephine @ -m_talk "..."
    sato "Maksudku!"

    josephine f_angry "Bagus!"

    hide josephine with dissolve
    pause
    sato f_confused "Saya sangat menyesal mengenai hal itu, Pak."

    sato "Jika Anda tidak keberatan kembali ke ruang pamer, saya jamin, putri saya akan dengan senang hati membantu Anda..."

    anon f_skeptical "Hmm, terima kasih?"

    sato f_smiling "Dengan senang hati, Pak."

    hide sato with dissolve
    pause
    anon f_worried "Aneh."

    hide anon with dissolve
    return


label ano07_sale_josie:
    show anon with dissolve
    label ano07_sale_josie.anon:
    anon f_normal @ f_grin a_point "Tolong, satu mobil!"

    josephine b_dressed f_normal "Ini adalah mobil termurah yang kami miliki saat ini."

    josephine "Vulva Mini."

    anon f_surprised "Mini-apa?!"

    josephine "Ini sangat populer di kalangan pelanggan persuasi wanita."

    josephine "Nilai ecerannya sebelas ribu lima ratus."

    anon "Sebelas ribu?!"

    anon "Itu agak berlebihan, bukan?"

    josephine "Harga terendah yang bisa saya lepaskan adalah enam ribu."

    josephine "Tapi dengan perdagangan Anda, kami bisa menghasilkan empat puluh lima ratus."

    anon f_worried "Empat puluh lima ratus, ya?"

    anon "Aku mungkin bisa mengayunkannya..."

    josephine "Jadi, kamu mau atau tidak?"

    show anon f_thinking a_thinking with dissolve

    menu:
        "Ya. ($4.500)":
            jump ano07_sale_josie.deal
        "Mungkin nanti.":

            pass

    anon a_thinking f_worried "Saya harus memikirkannya."

    josephine @ f_eyeroll "Besar."

    hide josephine
    show josephine b_dressed_sleeping behind anon
    show anon f_worried_low
    with {'master': dissolve}
    josephine "Luangkan waktumu, potong mangkuk."

    josephine "Bukannya aku akan pergi kemana-mana..."

    hide anon with dissolve
    return


label ano07_sale_josie.deal:
    if player.has_money(4500):
        anon f_normal a_idle "aku akan mengambilnya!"

        josephine @ f_eyeroll "Luar biasa."

        show anon a_money with dissolve
        pause
        show anon a_idle with dissolve
        josephine "Ayahku akan sangat bangga..."

        anon "Oh, ayolah... Tidak seburuk itu."

        josephine @ f_eyeroll "Ya."

        josephine "Ambil saja mobil kecilmu dan kalahkan, ya, potong mangkuk?"

        josephine "Aku punya pekerjaan yang aku coba untuk tidak lakukan."

        show josephine f_normal_down a_phone with dissolve
        anon "Baiklah."

        anon "Terima kasih sekali lagi!"

        hide anon with dissolve
        return 'compact_key'
    else:
        anon f_worried "Saya akan kembali untuk mengambilnya segera setelah saya punya uang."

        josephine @ f_eyeroll "Besar."

        show josephine f_normal_down a_phone
        show anon f_worried_low
        with {'master': dissolve}
        josephine "Bukannya aku akan pergi kemana-mana..."

        hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
