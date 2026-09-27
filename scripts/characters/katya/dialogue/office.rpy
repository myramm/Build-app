label katya_button_office:
    $ renpy.dynamic(had_sex=M_katya.finished_state(S_kat01_init))

    if had_sex:
        show anon a_wave with {'master': dissolve}
        anon "Hei, {b}Katya{/b}!"

        katya f_happy "Halo, {b}[firstname]{/b}."

        show anon a_sides
        with {'master': dissolve}
        katya "Anda datang untuk melihat {b}Nadya{/b}?"


    elif not M_katya.once('chat'):
        jump katya_button_office.first
    else:

        show anon f_worried with dissolve
        pause
        anon "Halo lagi."

        katya f_confused @ -m_talk "Hmm?"

        katya f_normal "Oh halo."

        show anon f_shy

    menu katya_button_office.choice:
        "Jadi apa yang kamu lakukan di sana?" if not had_sex:
            jump katya_button_office.what

        "Anda ingat saya?" if not had_sex:
            jump katya_button_office.anon

        "Bagaimana kabarmu?" if not had_sex:
            jump katya_button_office.okay

        "Bagaimana pekerjaanmu?" if had_sex:
            jump katya_button_office.work

        "Bahasa Inggris Anda menjadi cukup bagus." if had_sex:
            jump katya_button_office.language

        "Seks." if had_sex:
            jump katya_button_office.sex
        "Sampai jumpa lagi.":

            pass

    anon "Saya mungkin harus menyerahkan Anda pada pekerjaan Anda."

    katya f_normal "Ya, banyak yang harus dilakukan."

    katya "Vodka membawa banyak uang!"

    show katya f_normal_down
    hide anon
    with dissolve
    return


label katya_button_office.anon:
    anon "Jadi, apakah kamu ingat aku?"

    show katya f_normal
    pause
    anon "Hari itu, ketika semua orang jahat terbunuh..."

    anon "... Aku bersama orang-orang yang-"

    katya f_happy "Ya, kamu selamatkan aku!"

    katya "Ini selalu saya ingat."

    show anon f_happy
    katya "Kamu orang baik!"

    katya "Pria pemberani!"

    show anon a_rub f_shy_left with {'master': dissolve}
    anon "Ahhh, astaga."

    katya "aku akan menciummu..."

    show anon f_surprised
    show katya a_up f_shy with {'master': dissolve}
    katya "... Tapi aku tidak ingin membuat {b}Nadya{/b} marah padaku."

    show anon a_sides f_shy
    show katya a_writing
    with {'master': dissolve}
    anon "Oh, tidak... sungguh, tidak apa-apa!"

    anon "Aku senang kalian aman sekarang."

    katya f_happy "Ya, Amerika adalah tempat yang bagus."

    katya "Saya sangat menyukainya."

    anon "Itu bagus untuk didengar."

    show katya f_happy_down
    anon "Saya senang semuanya berhasil."

    jump katya_button_office.choice


label katya_button_office.cool:
    anon "Dingin."

    pause
    show katya f_normal_down
    jump katya_button_office.choice


label katya_button_office.first:
    show anon f_worried with dissolve
    anon "Hei, um..."

    katya @ -m_talk "Hmm?"

    show anon a_wave f_shy with {'master': dissolve}
    anon "... Hai, itu."

    katya f_confused "Oh, uhh..."

    katya "... Halo?"

    show anon a_sides with {'master': dissolve}
    anon "Kamu {b}Katya{/b}, kan?"

    katya f_normal @ -m_talk "MM."

    katya "Ya?"

    anon f_worried "Dingin."

    show katya f_confused
    pause
    show anon f_worried_surprised
    pause
    show anon f_surprised_left_low
    pause
    show anon a_shy_neck f_shy_high with {'master': dissolve}
    anon "Keren, keren, keren."

    pause
    katya "Ehh, aku membantumu?"

    anon f_confused @ -m_talk "Hmm?"

    show anon a_sides f_worried with {'master': fastdissolve}
    anon "Oh, tidak... Tidak."

    anon f_shy "Aku hanya, sedang memahami keadaannya."

    show katya f_concerned
    pause
    anon f_worried "Anda tahu, memeriksa semuanya?"

    katya @ -m_talk "..."
    anon f_shy "Mencoba bersikap ramah."

    katya @ f_confused "Apakah {b}Nadya{/b} mengatakan bolehkah kamu berada di sini?"

    anon f_confused "{b}Nadya{/b}?"

    anon f_brag "Oh ya..."

    anon "... Benar sekali."

    anon f_brag_closed "Dia cukup memberiku kebebasan untuk mengendalikan tempat itu."

    show katya f_confused
    anon f_flirt_left "Kami berhubungan baik satu sama lain."

    anon f_flirt "Seperti, sungguh, {i}benar-benar{/i} istilah yang baik... jika Anda mengerti maksud saya?"

    show anon f_flirt_grin
    show katya f_confused
    pause
    anon f_shy "Kami uhh..."

    pause
    anon f_worried "... Kamu tahu?"

    anon "Sudahlah."

    pause
    katya f_normal_down "Oke."

    jump katya_button_office.choice


label katya_button_office.language:
    anon f_normal "Bahasa Inggris Anda benar-benar meningkat."

    katya "Terima kasih, {b}[firstname]{/b}."

    katya "Aku punya lebih banyak waktu untuk belajar sekarang karena kamu memberikan {b}Nadya{/b} saat-saat seksi yang menyenangkan."

    show anon a_idle f_shy of_blush
    with {'master': dissolve}
    anon "O-oh?"

    katya @ -m_talk "Mhmm."

    katya "Senang juga mengistirahatkan rahangku."

    katya f_concerned_down "Dia memiliki nafsu makan yang tidak pernah terpuaskan."

    anon f_sad_down "Ya, katakan padaku sesuatu yang aku tidak tahu..."

    show katya f_confused
    pause
    show katya f_thinking_up
    pause
    katya f_happy "Oke!"

    show anon f_confused -of_blush
    with {'master': dissolve}
    katya "Tahukah Anda bahwa negara saya menciptakan Tetris?"

    show anon a_surprised_up_both f_worried_surprised
    with {'master': dissolve}
    anon "Itu hanya kiasan, {b}Katya{/b}... Kamu sebenarnya tidak seharusnya-"

    show anon f_confused
    pause
    anon f_skeptical "Tunggu, serius?!"

    show anon a_sides
    with {'master': dissolve}
    anon "Tetris ditemukan di Rusia?"

    katya "Apakah benar."

    anon f_happy_surprised "Saya tidak mengetahuinya!"

    katya f_proud "Heh, kamu terus belajar hal baru dari {b}Katya{/b}!"

    anon f_normal @ f_happy "Ya, menurutku begitu."

    jump katya_button_office.choice


label katya_button_office.okay:
    anon "Jadi kalian akur oke?"

    katya f_happy "Lebih baik daripada oke!"

    katya "{b}Nayda{/b} menjadikanku asisten pribadi."

    anon f_happy "Ah, benarkah?"

    katya "Untuk pertama kalinya dalam hidupku aku punya uang milikku..."

    katya "... {b}Nadya{/b} mengajakku membeli pakaian bagus dan membelikanku apartemen."

    anon "Itu luar biasa."

    katya "Dan makanan di negara ini..."

    katya "... Saya makan seperti ratu!"

    anon "Ya, itulah Amerika untukmu."

    katya "Seperti ehh, anjing keju cabai!"

    anon @ f_happy_closed "Ah, ya..."

    anon "... Itu bagus!"

    katya "Oh, dengan bawang bombay dan sedikit acar di atasnya..."

    katya "... Delicious!" (show_native="... Pal'chiki oblizhesh!")
    katya "Dan kentang goreng Perancis tanpa dasar..."

    katya f_surprised "... Tidak ada orang yang bisa makan sebanyak itu!"

    show katya a_wide
    with {'master': dissolve}
    katya "Mereka pasti akan meledak!"

    anon "Heh, ya... anjing cabai dan kentang goreng bisa mempunyai dampak yang {i}meledak-ledak{/i}, itu sudah pasti."

    show katya a_writing f_happy
    with {'master': dissolve}
    katya "Apa itu bantal?"

    anon f_shy "Anda tahu, karena mereka membuat Anda..."

    anon "... Ehh..."

    anon f_shy_left "... {size=-2}Kentut{/size}."

    katya f_confused @ -m_talk "Hmm?"

    show anon a_behind_head f_shy_down
    with {'master': dissolve}
    anon "Heh, uhh... sudahlah."

    anon f_shy "Itu tidak penting."

    katya "Tapi aku tidak bisa mendengarmu."

    show anon a_sides f_normal
    with {'master': dissolve}
    anon "Oh bagus."

    pause
    anon "Percayalah, itu yang terbaik."

    katya f_happy @ f_laugh "hehe!"

    katya "Kamu terkadang pria yang aneh!"

    show katya f_happy_down
    jump katya_button_office.choice


label katya_button_office.sex:
    anon "Jadi, kamu pikir kita bisa ehh... kamu tahu?"

    katya f_happy "Sex?" (show_native="Seks?")
    katya "Tentu saja."

    show anon a_surprised_up f_surprised
    with {'master': dissolve}
    anon "Benar-benar?!"

    katya "Heh, aku akan menyambut istirahatnya."

    show anon a_sides f_happy
    show katya a_front b_dressed
    with {'master': dissolve}
    katya "Dan nyonyaku mengatakan aku akan menjadi milikmu kapan pun kamu menginginkannya."

    show anon a_surprised f_surprised
    with {'master': dissolve}
    anon "Dia melakukannya?!"

    show katya f_confused
    show anon f_surprised_teeth
    pause
    show anon a_shy_neck f_worried
    with {'master': dissolve}
    anon f_worried "Maksudku, ya..."

    show anon a_sides
    with {'master': dissolve}
    anon f_shy "... D-dia melakukannya."

    show katya a_undress1 f_happy
    with {'master': dissolve}
    katya "Bagus."

    show anon f_shy_low
    show katya a_undress2 b_dressed_boobs
    with {'master': dissolve}
    pause
    show anon f_flirt_grin
    show katya a_pull1 b_dressed_boobs
    with {'master': dissolve}
    katya "Datang."

    show katya a_pull2 b_dressed_boobs_pulled
    with {'master': dissolve}
    katya "Kami bercinta di meja."

    anon f_flirt "Manis!"


    call scene_katya_sex_desk_side.repeat
    $ unlock_scene('katya', '01_unlocked', variant='repeat')

    call katya_button_stage
    show katya a_pull2 b_dressed_disheveled_boobs_pulled f_happy_down
    show anon b_dressed_changing2
    with fade
    anon "Fiuh, itu berhasil."

    show anon b_dressed_changing
    show katya a_pull1 b_dressed_disheveled_boobs
    with {'master': dissolve}
    katya @ -m_talk "Mhmm."

    show anon b_dressed a_sides
    show katya a_undress1 b_dressed_disheveled f_happy
    with {'master': dissolve}
    katya "Istirahat yang sempurna."

    show katya a_fix_hair1 b_dressed_sit
    with {'master': dissolve}
    katya "Tapi sekarang aku harus kembali melakukannya."

    show katya a_fix_hair2 f_normal_down
    with {'master': dissolve}
    anon f_worried "Ya baiklah."

    show katya a_writing
    with {'master': dissolve}
    pause
    anon f_shy "Jangan bekerja terlalu keras, oke?"

    katya f_confused @ -m_talk "Hmm?"

    katya "Pekerjaan ini tidak sulit."

    anon @ f_worried "Ehh..."

    anon "Sudahlah."

    show katya f_concerned
    pause
    show anon a_wave
    with {'master': dissolve}
    anon "Sampai jumpa, {b}Katya{/b}."

    hide anon
    with {'master': dissolve}
    katya f_normal "Farewell, {b}[firstname]{/b}." (show_native="Do svidaniya, {b}[firstname]{/b}.")
    show katya f_normal_down
    pause
    return 'afterglow'


label katya_button_office.what:
    anon "Jadi apa yang kamu tulis?"

    katya "Accounting work." (show_native="Bukhgalterskaya rabota.")
    katya "For vodka business." (show_native="Dlya vodochnogo biznesa.")
    anon f_confused @ -m_talk "Hmm?"

    anon "Saya tidak mengerti."

    katya f_normal "Ehh, kami... menjual, vodka..."

    show anon f_confused_low
    show katya a_paper
    with {'master': dissolve}
    katya @ f_normal_low "... Dan simpan angka untuk dihitung."

    anon f_normal "Oh, jadi kamu mencatat semua uangnya?"

    show katya a_writing f_happy
    with {'master': dissolve}
    katya "Ya, uang."

    katya "Sejak saya masih kecil, saya pandai berhitung."

    katya "Di Rusia saya juga membantu ayah dengan uang."

    anon "Tidak bercanda?"


    menu:
        "Kacang dingin.":
            jump katya_button_office.cool
        "Apa yang dia lakukan?":

            pass

    anon "Apa yang dia lakukan?"

    katya f_confused @ -m_talk "Hmm?"

    anon "Bisnis ayahmu."

    anon "Anda menjual vodka tapi apa yang dia jual?"

    katya f_shy "Oh, umm... mushrooms." (show_native="Oh, umm... griby.")
    anon f_confused "Griby?"

    katya f_happy "Heh, da." (show_native="Heh, yes.")
    katya f_thinking_up "Ehh, apa itu kata?"

    pause
    katya "rawa..."

    show anon a_thinking
    with {'master': dissolve}
    pause
    show anon a_point2 f_happy
    with {'master': dissolve}
    anon "Marshmallow?"

    show katya f_confused
    pause
    show anon a_sides f_sad
    with {'master': dissolve}
    katya "Nyet." (show_native="No.")
    katya f_thinking_up "Bukan rawa... itu ehh..."

    katya "... M-bubur..."

    show anon a_point2 f_happy
    with {'master': dissolve}
    anon "Jamur?!"

    show anon a_fist f_grin
    with {'master': dissolve}
    katya f_happy "Ya, jamur!"

    show anon a_sides f_normal
    with {'master': dissolve}
    anon "Jadi ayahmu menjual jamur?"

    katya f_proud "Yah, dia menjual banyak barang yang dia ambil dari hutan belantara..."

    katya "... Madu, beri, hewan untuk dimakan atau dijual kulitnya..."

    katya "... Terkadang obat-obatan."

    anon "Tidak bercanda?"

    katya "Tapi jamur adalah best seller."

    katya "Orang-orang di Rusia sangat menyukai jamur asin!"

    anon f_confused "Saya tidak tahu."

    katya "Cocok untuk camilan saat dicampur dengan vodka."

    anon f_normal "Nah bagaimana dengan itu?"

    show katya f_happy_down
    anon "Sepertinya benar Anda mempelajari sesuatu yang baru setiap hari."

    jump katya_button_office.choice


label katya_button_office.work:
    anon "Bagaimana kabarnya?"

    katya "Good!" (show_native="Khorosho!")
    katya "{b}Nadya{/b} promosikan saya menjadi kepala penjualan!"

    anon @ f_happy "Kamu tidak bilang?!"

    katya "Tidak, itu benar!"

    katya "Dia berkata, \"{b}Katya{/b} kamu punya hadiah untuk dijual kepada pebisnis Amerika yang gemuk.\""

    show katya a_squeeze f_happy_down
    show anon f_surprised_low
    with {'master': dissolve}
    katya "Tapi kenyataannya, aku hanya tersenyum dan memakai bra yang membenturkan payudaraku seperti saudara kandung yang sedang marah di antrean tiket makan."

    show anon o_boner
    with {'master': dissolve}
    anon @ -m_talk "..."
    katya a_writing f_proud "Kemudian mereka memesan tiga kali lipat."

    pause
    show katya f_proud_teeth_low
    pause
    show anon f_surprised_down
    pause .4
    show anon a_cover_boner f_shy
    show katya f_laugh
    with {'master': dissolve}
    anon "Maaf, saya tidak mendengar apa pun setelah kata payudara."

    katya f_proud "Mungkin aku juga menjualmu vodka, ya?"

    anon "Heh, tidak... Tidak apa-apa."

    anon "Aku baik-baik saja."

    katya f_laugh "hehe!"

    show anon a_idle -o_boner
    show katya f_happy
    with {'master': dissolve}
    jump katya_button_office.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
