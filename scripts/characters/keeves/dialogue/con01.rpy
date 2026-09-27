label con02_init_keeves:
    anon "Baiklah, umm... Saya tidak butuh bantuan {b}Pastor Keeves{/b} tapi saya kenal seseorang yang membutuhkannya."

    keeves f_happy @ f_laugh a_rock "Bagus sekali!"

    keeves "Lanjutkan."

    anon "Oke."

    anon f_worried "Begini, akhir-akhir ini aku sedang melakukan sedikit pekerjaan di {b}rumah Walikota{/b} dan aku sadar bahwa salah satu pelayan di sana dianiaya..."

    keeves f_confused "Bagaimana bisa?"

    anon "Ya, {b}walikota{/b} dan {b}istrinya{/b} pada dasarnya menyuruhnya bekerja sebagai pembantu kontrak."

    keeves f_sad "Benar-benar?"

    anon "Ya."

    anon "Mereka tidak membayar apa pun dan menyerangnya secara verbal setiap ada kesempatan."

    keeves "Kedengarannya buruk."

    anon "Saya cukup yakin {b}Walikota{/b} juga melecehkannya."

    keeves f_surprised @ -m_talk "!!!"
    keeves "{b}Walikota{/b} adalah?"

    anon "Y-ya, tuan."

    keeves f_sad @ f_woa "Wah!"

    pause
    keeves "Itu sangat palsu!"

    anon "Benar?"

    keeves f_normal "Kedengarannya hal-hal aneh sedang terjadi di {b}rumah walikota{/b}."

    keeves "Kita harus segera melakukan intervensi."

    show anon f_normal
    pause
    keeves "Ini seperti gadis klasik Anda dalam situasi kesusahan."

    keeves "Yang menurut pengalaman saya, hampir selalu mengarah pada petualangan yang paling luar biasa."

    anon @ f_skeptical -m_talk "..."
    anon "Benar."

    anon f_normal "Yah, saya sudah berhasil membebaskannya dari pekerjaan itu dan menjauh dari {b}walikota{/b} dan {b}istrinya{/b}."

    keeves "Oh?"

    keeves f_happy "Bagus sekali, kawan kecil!"

    keeves f_confused "Jadi apa masalahnya?"

    anon "Nah, sekarang dia benar-benar membutuhkan pekerjaan baru."

    keeves f_normal "Ah, begitu."

    anon "Yang sulit ditemukan karena, dia agak... Seorang imigran gelap."

    pause
    anon "Siapa yang tidak bisa berbahasa Inggris."

    keeves f_sad "Gelandangan!"

    anon "Ya."

    pause
    anon "Jadi, kupikir mungkin dia bisa membantu di sekitar sini, tahu?"

    keeves f_happy @ a_point "Itu ide yang sangat bagus, kawan!"

    keeves "Tapi pertama-tama, saya punya dua pertanyaan yang sangat penting."

    anon "Oke."

    keeves "Bagaimana perasaan wanita ini mengenai Tuhan dan Juruselamat kita, Yesus Kristus?"

    anon "Oh, dia seorang Katolik yang taat."

    anon "Itu sebabnya aku langsung berpikir untuk meminta bantuanmu."

    keeves @ f_laugh a_rock "berbentuk tabung!"

    keeves "Sekarang, pertanyaan kedua..."

    keeves @ f_confused a_raise "Apakah dia masih bayi?"

    anon f_surprised @ -m_talk "..."
    anon f_confused "Hah?"

    keeves f_normal @ a_point "Bagaimana situasi kerucutnya?"

    anon f_worried "Apakah kamu serius saat ini?"

    keeves "Apakah mereka dibuat untuk kecepatan atau kenyamanan?"

    anon "Maksudku, menurutku dia cantik..."

    keeves a_raise @ f_laugh "Baiklah, dua untuk dua!"

    keeves -a_raise @ f_laugh a_rock "Sangat luar biasa!"

    anon f_normal "Jadi, Anda akan mempekerjakannya?"

    keeves f_happy "Pastinya."

    anon "Oh, itu luar biasa!"

    anon "Terima kasih banyak, {b}Pastor Keeves{/b}!"

    keeves "Jangan khawatir, kawan kecil."

    anon "Aku akan membawanya secepatnya."

    hide anon with dissolve

    scene expression player.location.background_blur with fade
    show anon with dissolve
    anon f_brag_closed @ -m_talk "( Ya, saya tahu saya dapat menemukan {b}Consuela{/b} pekerjaan baru! )"

    anon @ -m_talk "( Saya tidak sabar untuk {b}memberi tahu dia kabar baik{/b}! )"

    hide anon with dissolve

    $ M_consuela.trigger(T_con02_init)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
