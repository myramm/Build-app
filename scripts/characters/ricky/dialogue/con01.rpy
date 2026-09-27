label con01_init_ricky:
    anon f_worried "Apakah mereka selalu memperlakukan {b}Consuela{/b} dengan sangat buruk?"

    pause
    ricky f_confused "Anda tampak terkejut?"

    anon "Saya."

    anon "Maksudku, Walikota selalu terlihat seperti orang yang murah hati di TV..."

    ricky f_sad "Kamu harus banyak belajar tentang dunia, temanku."

    ricky "Itu hanya kepribadian publiknya."

    ricky "Kebanyakan politisi bertindak sangat berbeda di balik pintu tertutup."

    anon "Ya, menurutku..."

    pause
    anon "Dapatkah Anda memikirkan cara apa pun yang dapat saya lakukan untuk membantunya?"

    ricky f_smirk "Heh, bisakah kamu memberinya kartu hijau?"

    anon "Tidak."

    ricky "Kalau begitu menurutku tidak."

    pause
    anon f_thinking a_thinking "Saya bisa mencoba berbicara dengan walikota."

    ricky f_surprised "Ide buruk!"

    ricky f_sad "Kemungkinan besar Anda akan memperburuk keadaannya..."

    show anon f_worried
    pause
    ricky f_thinking "Hmm, kamu bisa mencoba {b}berbicara dengan istri Walikota{/b}, menurutku..."

    anon f_surprised "{b}Melonia{/b}?"

    anon f_skeptical "Menurutmu dia mungkin bisa membantu?"

    ricky f_normal "Bukan karena kebaikan, dia tidak akan..."

    ricky "... Tetapi jika Anda dapat meyakinkan dia bahwa membantu {b}Consuela{/b} adalah kepentingan terbaiknya, ada kemungkinan dia akan melakukannya."

    ricky "Apalagi jika itu membuat suaminya kesal."

    ricky "Dia memiliki sedikit cinta padanya."

    anon f_thinking "Hmm."

    pause
    anon f_normal "Yah, sepertinya aku tidak punya ide yang lebih baik."

    anon "{b}Saya akan pergi dan berbicara dengan istri Walikota{/b}."


    if game.timer.is_day():
        ricky "{b}Tunggu sampai malam{/b}, setelah dia berendam di bak mandi, dia merasa rileks."


    anon a_idle @ a_wave "Terima kasih, {b}Ricky{/b}."

    ricky f_smirk "Semoga berhasil, kawan."

    hide anon with dissolve
    return


label con01_init_ricky.repeat:
    ricky f_confused "Apakah Anda {b}berbicara dengan istri Walikota{/b}?"

    anon "Belum."

    ricky f_sad "Berhati-hatilah, ya?"

    ricky "Dia lebih pintar dari yang dia biarkan."

    anon "Saya akan berhati-hati."


    if game.timer.is_day():
        hide anon with {'master': dissolve}
        ricky "Dan ingatlah untuk {b}menunggu malam{/b}, amigo!"

    else:
        hide anon with dissolve
    return


label con01_plan_ricky:
    show ricky f_smirk
    anon f_normal "Kabar baik!"

    anon "Saya rasa saya menemukan cara untuk melihat {b}Consuela{/b} bebas dari tempat ini."

    ricky "Benar-benar?"

    ricky "Bagaimana Anda mengaturnya?"

    anon @ f_brag_closed "Istri Walikota bilang aku hanya perlu mencari pembantu pengganti."

    ricky @ -m_talk "..."
    ricky @ f_laugh "Hahahahahahaah!"

    anon f_worried @ f_skeptical "Mengapa kamu tertawa?"

    ricky "Siapa yang rela bekerja demi upah yang {b}Rumps{/b} membayar dan menerima {b}Mister Rump{/b} ketika dia menjadi tampan?"

    anon "Baiklah, saya berharap Anda mengenal seseorang?"

    ricky @ f_laugh "Pfft, hahahahaah!"

    anon f_sad_down @ -m_talk "..."
    ricky "Bahkan imigran gelap pun punya standar."

    ricky "Saya juga tidak yakin saya akan nyaman menyarankannya kepada mereka."

    anon "{i}*Huh*{/i} Sial."

    ricky "Percayalah, tak seorang pun akan tahan dengan tempat ini jika tidak terpaksa."

    anon "Pasti ada seseorang!"

    ricky "Ya benar."

    ricky "Yang Anda butuhkan adalah {b}pelacur{/b} atau semacamnya..."

    anon f_surprised "Pelacur?!"

    ricky "Pelacur yang benar-benar putus asa."

    anon f_worried "Kami tidak memiliki hal seperti itu di Summerville!"

    ricky "Hah!"

    ricky "Kenaifanmu sungguh menggemaskan, kawan."

    anon @ -m_talk "..."
    ricky "Ada lagi yang bisa saya bantu?"

    anon "Tidak."

    ricky "Tidak ada pelacur di Summerville..."

    hide ricky with {'master': dissolve}
    ricky "Hahahahahahaah!"

    anon f_thinking a_thinking @ -m_talk "( Apakah kita benar-benar memiliki pekerja seks di kota kecil kita? )"

    pause
    anon f_grin a_idle @ -m_talk "( {b}Saya kira tidak ada salahnya untuk memeriksanya{/b}. )"

    hide anon with dissolve

    $ M_consuela.trigger(T_con01_plan)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
