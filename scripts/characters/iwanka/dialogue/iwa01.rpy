label iwa01_init_iwanka:
    show anon f_normal with dissolve
    iwanka "{b}[firstname]{/b}?"

    anon "Hai."

    iwanka "Ya ampun, bagaimana kamu bisa melewati penjaga?"

    anon @ f_laugh "Rencanamu berhasil!"

    iwanka f_concerned "Rencana?"

    anon "Ya, kamu ingat?"

    anon f_shy "Suatu malam... Anda menyarankan agar saya memberi tahu mereka bahwa saya asisten baru Anda."

    iwanka "Ya?"

    anon f_worried "Anda tidak ingat?"

    iwanka f_normal @ f_laugh "Heh, aku tidak ingat apa pun dari malam itu kalau boleh jujur..."

    anon "Tidak ada sama sekali?"

    iwanka f_thinking "Hmm, aku ingat aku tiba... Dan wanita aneh itu menyorongkan es loli ke tanganku..."

    pause
    iwanka f_annoyed "... Lalu dia menyebut gaunku jelek."

    show anon f_hurt
    pause .5
    anon f_worried "Ya."

    show iwanka f_thinking
    pause
    iwanka f_suspicious a_hip @ f_laugh a_finger "Oh, aku ingat temanmu membuat Obeng yang sangat enak!"

    iwanka "Siapa namanya lagi?"

    anon f_unimpressed "{b}Erik{/b}."

    iwanka f_disgusted "Tidak, bukan itu."

    show anon f_worried
    pause
    iwanka f_smirk "Ngomong-ngomong, minumannya enak dan ada tariannya..."

    iwanka "... menurutku."

    anon f_worried_low "Ya, ada tarian."

    iwanka "Aku ingat teman kecilmu sedang membicarakan banyak hal yang aku tidak mengerti..."

    show iwanka f_thinking
    show anon f_worried
    pause
    iwanka "... Dan sesuatu tentang..."

    pause
    iwanka f_suspicious "... Seekor gurita?"

    anon f_surprised a_sides @ a_surprised_up "Uhh?"

    iwanka @ a_crossed "Saya tidak ingat."

    iwanka f_smirk "Semuanya suram."

    anon f_shy a_idle @ a_point "Ya, kamu memang banyak minum."

    iwanka f_suspicious "Apakah temanmu punya gurita peliharaan atau semacamnya?"

    anon f_worried "T-tidak."

    iwanka f_concerned "Hmm, mungkin itu hanya mimpi..."

    iwanka "... Ini seperti, tersangkut di kepalaku, karena suatu alasan."

    anon "Hah."

    show anon f_surprised_teeth
    pause
    anon f_worried "Hmm, aneh."

    iwanka f_normal @ f_laugh "Benar?!"

    pause
    iwanka "Jadi apa yang kamu lakukan di sini?"

    anon f_normal "Baiklah, umm... Kau tahu, kita bersenang-senang malam itu..."

    anon f_shy "... Dan kamu ingin lebih sering jalan-jalan, jadi..."

    iwanka "Apakah kamu tidak khawatir akan ketahuan?"

    iwanka @ f_laugh "Para penjaga benar-benar membuat orang gila, Anda tahu?"

    anon f_worried "Ehh, aku pikir kamu bercanda tentang itu..."

    iwanka f_suspicious "Mengapa saya bercanda tentang hal itu?"

    anon "Aku tidak tahu."

    iwanka f_normal @ f_eyeroll "Itu terjadi sepanjang waktu!"

    anon f_surprised "Kamu serius?"

    iwanka "Oh, tentu saja."

    show anon f_hurt a_cover_boner with dissolve
    iwanka f_smirk "Mereka bilang itu seperti, pencegah yang paling efektif atau semacamnya..."

    show anon f_worried
    iwanka "... Saya pikir mereka hanya bosan."

    anon "Itu sungguh kacau!"

    iwanka f_normal @ f_laugh "Hehe, ya."

    iwanka "Tapi itu pasti berhasil, karena belum pernah ada orang yang ketahuan mencoba menerobos masuk dua kali."

    anon a_badge "{i}*Gulp*{/i} Saya mungkin aman dengan {b}lencana staf{/b} ini, bukan?"

    iwanka f_surprised "Wah, dari mana kamu mendapatkannya?!"

    anon "{b}Melonia{/b} memberikannya kepadaku."

    iwanka f_suspicious "Ibuku memberimu {b}lencana staf{/b}?"

    anon f_normal a_idle "Dia pikir aku anak biliar yang baru."

    iwanka "Sungguh?"

    anon "Ya."

    iwanka "Apakah kalian berdua sialan?"


    if M_melonia.finished_state(S_mel05_init):
        anon f_surprised @ f_shy "Ehh."

        pause
        anon f_worried "Entahlah, mungkin..."

        show iwanka a_crossed f_smirk with dissolve
        pause
        anon @ a_fingers_small "...Hanya sedikit."

        iwanka @ f_laugh "Ya ampun, itu lucu!"

        iwanka a_hip "Bagaimana tadi?"

        anon f_confused "Hah?"

        iwanka "Saya yakin itu seperti melakukan push-up melalui lubang got yang terbuka!"

        anon f_shy "Tunggu, jadi... Kamu tidak marah?"

        iwanka @ f_eyeroll "Tolong, {b}[firstname]{/b}."

        iwanka "Jika aku marah setiap kali orang tuaku mengabaikan bantuannya, aku tidak akan pernah bisa mencapai apa pun."

        anon f_surprised @ -m_talk "..."
        iwanka "Jadi Anda tidak hanya menipunya agar memberi Anda akses gratis ke mansion..."

        show anon f_shy
        iwanka "... Tapi dia juga memberimu akses gratis ke vaginanya?"

        anon "Sebenarnya, dia membayarku."

        iwanka f_normal @ f_laugh "Pfft, hahaha!"

        show anon f_normal
        iwanka "Itu sangat menyedihkan!"

        anon @ -m_talk "..."
        iwanka "Anda benar-benar membuat hari saya menyenangkan!"

    else:

        anon f_surprised "T-tidak!"

        show anon f_shy m_talk
        show anon of_blush with {'master': dissolve}
        anon -m_talk "Tentu saja tidak!"

        iwanka a_crossed f_annoyed "{b}[firstname]{/b}, katakan sejujurnya!"

        anon f_worried a_up -of_blush "{b}Iwanka{/b}, sumpah!"

        anon "Aku tidak melakukan apa pun dengan ibumu."

        show anon a_idle with dissolve
        pause
        iwanka f_suspicious "Sungguh?"

        anon "Aku sangat serius."

        iwanka f_concerned "Wow, dia tergelincir di usia tuanya."

        anon f_confused "Tunggu, jadi... Kamu berasumsi aku akan melakukannya?"

        iwanka @ f_eyeroll "Hmm, ya."

        iwanka f_smirk "Katakan padaku ini..."

        iwanka "... Apakah dia sudah memilihkan nama untukmu?"

        show anon f_worried_low
        pause
        anon "... {b}Hektor{/b}."

        iwanka @ f_laugh "Pfft, haha!"

        iwanka a_idle "Anda pasti berada di garis bidiknya."

        anon f_worried "Saya?"

        iwanka "Ingatlah untuk mengantonginya."

        iwanka "Vagina ibu saya lebih banyak melihat penis daripada urinoir toko perkakas."

        anon f_shock "!!!"
        iwanka "Saya cukup yakin ludahnya akan diterima di salah satu klinik donasi sperma tersebut."

        anon f_worried "Aku tidak begitu yakin bagaimana harus menanggapinya..."

        iwanka f_normal @ f_laugh "hehe!"


    anon "Jadi, apakah ada anak laki-laki lain yang menyelinap ke tanah milik ayahmu untuk menemuimu sebelumnya?"

    iwanka @ f_surprised "Oh, tidak!"

    iwanka "Mereka semua terlalu takut pada ayahku."

    anon f_normal @ f_laugh "Apakah itu berarti Anda terkesan?"

    iwanka f_smirk "Mmm, mungkin..."

    anon "Cukup terkesan untuk mengajak saya tur?"

    iwanka f_suspicious "Bagaimana dengan mansionnya?"

    anon "Ya."

    iwanka "Itu hal yang aneh untuk diminta."

    anon "Apakah itu?"

    anon "Aku belum pernah masuk ke dalam rumah sebesar ini sebelumnya."

    iwanka f_bored "Ugh, tidak bisakah kita melakukan hal lain, {b}[firstname]{/b}?"

    iwanka f_smirk @ f_laugh "Anda tahu, sesuatu yang menyenangkan!"

    anon @ f_confused "Umm, tentu... kurasa."

    anon "Apa yang ada dalam pikiranmu?"

    iwanka "Entahlah."

    iwanka @ f_laugh "Ayo menyelinap keluar dan mengadakan pesta lagi!"

    anon f_skeptical "Anda ingin mengadakan pesta lagi di rumah {b}Erik{/b}?"

    iwanka @ f_concerned "Uhh, tidak juga..."

    show anon f_worried
    iwanka f_bored "Dengar, jangan tersinggung, {b}[firstname]{/b}... Tapi rumah temanmu agak kumuh..."

    anon "Oh."

    iwanka f_normal "Jadi, saya berpikir sebaiknya saya memilih tempatnya kali ini."

    anon "Y-ya, oke."

    anon f_normal "Cukup sebutkan tempatnya dan aku akan menemuimu di sana."

    iwanka f_concerned "Yah, ada sedikit tangkapan..."

    anon @ f_confused "Hmm?"

    iwanka @ f_eyeroll "Jadi, ayahku merasa kesal karena aku menyelinap keluar malam itu..."

    iwanka f_annoyed "... Dan dia membuatku menjadi tahanan rumah."

    anon f_worried "Kamu serius?"

    iwanka @ -m_talk "Mhmm."

    anon f_confused "Bukankah kamu bilang kamu berumur dua puluh tujuh tahun?"

    iwanka f_suspicious "Mau kemana dengan ini, {b}[firstname]{/b}?"

    anon "Tidakkah menurutmu itu terlalu kuno untuk dihukum oleh ayahmu?"

    iwanka f_annoyed @ f_eyeroll "Hmm, ya."

    iwanka "Apakah kamu ingin menjelaskan itu padanya?!"

    anon f_sad_down "{i}*Huh*{/i} Tidak, sebenarnya tidak."

    iwanka "Ya, menurutku tidak!"

    iwanka f_concerned "Para penjaga tidak akan membiarkanku keluar begitu saja kali ini..."

    show anon f_worried
    iwanka f_smirk "... Kamu harus menyelinapkanku keluar."

    anon f_surprised a_point_self "Aku?!"

    anon a_up "Saya tidak bisa melakukan itu!"

    show anon a_idle with dissolve
    iwanka f_suspicious "Kenapa tidak?"

    iwanka "Anda menyelinap ke sini, bukan?"

    anon f_shy "Y-ya, tapi-"

    iwanka f_smirk "Jadi lakukan saja lagi, tapi sebaliknya!"

    anon f_hurt a_cover_boner @ f_worried_low -m_talk "..."
    pause
    iwanka f_concerned "{b}[firstname]{/b}?"

    anon f_worried "Ya, maaf... Aku hanya memikirkan betapa aku tidak ingin dikecewakan..."

    iwanka f_smirk @ f_eyeroll "Oh, ayolah... Pasti sepadan!"

    iwanka "Lakukan ini dan aku akan memberikan apa pun yang kamu inginkan!"

    anon f_shy a_idle "Apa pun?"

    iwanka @ -m_talk "Mhmm."

    anon f_normal "Tur ke seluruh rumah?"

    iwanka f_annoyed "Itu yang kamu-"

    show iwanka f_bored
    pause
    iwanka a_crossed f_eyeroll "Ya tentu saja."

    iwanka "Apa pun."

    show iwanka f_normal
    anon @ f_laugh a_cheering "Baiklah, aku akan memikirkan sesuatu."

    iwanka @ f_laugh "Bagus sekali!"

    iwanka "Datang saja dan temukan saya ketika Anda punya rencana."


    scene expression background(640, 240, 9., l=L_rump_lobby) as stage with fade
    show anon f_worried_low with dissolve:
        flip
        xoffset -100
    anon @ -m_talk "(Ini tidak pernah sederhana, bukan?)"

    anon f_thinking @ a_thinking -m_talk "( Bagaimana aku bisa menyelinap {b}Iwanka{/b} melewati para penjaga? )"

    pause
    anon @ -m_talk "( Yang kita butuhkan adalah {b}penyamaran{/b} yang baik. )"

    anon f_normal @ -m_talk "( Mungkin ada sesuatu {b}di sini, di perkebunan{/b} yang akan berhasil... )"

    anon @ -m_talk "( {b}Saya harus melihat-lihat{/b}. )"

    hide anon with dissolve
    return


label iwa01_find_iwanka:
    show anon with dissolve
    iwanka "Apakah kamu sudah menemukan cara untuk menyelinapkanku keluar?"

    anon f_worried "Tidak, saya masih mengerjakannya."

    iwanka f_disgusted "Eh, serius?"

    anon @ a_up "Cobalah dan bersantai, oke?"

    anon f_normal "Aku akan menemukan sesuatu, aku janji."

    iwanka f_concerned a_crossed "Aku sangat bosan, kamu tidak tahu!"


    scene expression background(640, 240, 9., l=L_rump_lobby) as stage with fade
    show anon f_thinking a_thinking with dissolve:
        flip
        xoffset -100
    anon @ -m_talk "(Hmm.)"

    anon @ -m_talk "( Bagaimana aku bisa menyelinap {b}Iwanka{/b} melewati para penjaga? )"

    pause
    anon @ -m_talk "( Yang kita butuhkan adalah {b}penyamaran{/b} yang baik. )"

    anon f_normal @ -m_talk "( Mungkin ada sesuatu {b}di sini, di perkebunan{/b} yang akan berhasil... )"

    anon @ -m_talk "( {b}Saya harus melihat-lihat{/b}. )"

    hide anon with dissolve
    return


label iwa01_give_iwanka:
    show anon with dissolve
    iwanka "Apakah kamu sudah menemukan cara untuk menyelinapkanku keluar?"

    anon "Ya, menurutku aku sudah menemukan cara agar kamu bisa berjalan melewati para penjaga."

    iwanka f_excited "Hehe, benarkah?"

    iwanka "Bagaimana saya akan melakukan itu?"

    show anon a_backpack f_looking_down with dissolve
    pause
    anon f_laugh a_maid_outfit "Dengan memakai ini!"

    show anon f_normal a_idle
    show iwanka a_maid_uniform f_suspicious_down
    with dissolve
    pause
    iwanka f_suspicious "Anda ingin saya berdandan sebagai pelayan?"

    anon "Ya."

    show iwanka f_suspicious_down
    pause
    anon "Apa?"

    iwanka "Entahlah, hanya saja... Agak..."

    pause
    iwanka f_disgusted "... Eww."

    anon f_unimpressed "Apakah kamu ingin keluar dari rumah ini atau tidak?"

    iwanka f_concerned "Ya."

    pause
    iwanka "Tapi saya hanya mengatakan, alangkah baiknya jika Anda dapat menemukan sesuatu yang kurang-"

    anon "{b}Iwanka{/b}, diam dan pakai seragam!"

    iwanka @ f_surprised "!!!"
    iwanka "Baiklah, baiklah... Astaga!"

    iwanka "Anda tidak harus menjadi pemarah."

    show iwanka a_maid_uniform_smell f_disgusted with dissolve
    show anon f_worried
    pause
    iwanka a_maid_uniform "Eh, bau apa itu?"

    anon "Entahlah."

    anon @ f_confused "Janji Lemon?"

    iwanka "Itu menjijikkan!"


    label iwa01_give_iwanka.retry:
    anon f_worried "Apakah kita akan pergi atau tidak?"


    if game.timer.is_evening():
        jump iwa01_give_iwanka.evening

    iwanka f_normal @ f_eyeroll "Ya, saat ini tidak tepat... Tentu saja."

    anon f_surprised "Jelas sekali?"

    iwanka f_content_closed a_idle @ a_finger "Pesta yang baik terjadi setelah matahari terbenam, ya."

    anon f_sad_down "..."
    show anon f_worried
    iwanka f_normal "Kembalilah malam ini dan kita berangkat, oke?"

    anon "{i}*Huh*{/i} Ya, oke."

    anon a_sides @ a_wave "Sampai jumpa malam ini."

    hide anon with dissolve
    return False


label iwa01_give_iwanka.evening:
    iwanka f_annoyed "Ya, ya."

    show anon f_surprised
    show iwanka b_dressed_back_unzip1 with dissolve
    pause
    show iwanka b_dressed_back_unzip2 with dissolve
    show anon f_surprised_low
    iwanka "Aku tidak percaya kamu membuatku memakai pakaian jelek ini..."

    show iwanka b_dressed_back_unzip3 with dissolve
    pause
    show iwanka b_dressed_back_unzip4 with dissolve
    show anon f_flirt_low
    anon "T-tunggu, kenapa kamu tidak memakainya saja di bajumu?"

    show iwanka b_dressed_back_unzip5 with dissolve
    iwanka "Umm, aku tidak akan mencium bau ini di seluruh pakaian bagusku!"

    anon f_surprised @ f_unimpressed a_frustrated "Baunya enak, {b}Iwanka{/b}!"

    show iwanka b_naked a_maid_uniform f_disgusted with dissolve
    iwanka "Itu pendapat Anda!"

    show anon f_flirt_low
    iwanka @ f_eyeroll "Selain itu, mengapa kamu mengeluh?"

    anon @ f_flirt "{i}*Gulp*{/i} Poin bagus."

    show iwanka f_suspicious_down
    pause
    iwanka @ -m_talk "..."
    show iwanka b_naked_dressing_maid with dissolve
    pause
    iwanka "Eww.{w} Eww.{w} Eww."

    show iwanka b_maid_scarfless f_disgusted a_out_gross with dissolve
    show anon f_normal
    iwanka "Ini sangat menjijikkan!"

    show iwanka a_hips with dissolve
    anon f_worried @ f_eyeroll "Ya, terserah..."

    anon "Apakah Anda memiliki sesuatu untuk menyembunyikan rambut Anda?"

    iwanka f_surprised_up @ -m_talk "Hmm?"

    anon f_normal "Seperti syal atau apa?"

    iwanka f_normal @ f_laugh "Oh benar!"

    hide iwanka with dissolve
    pause
    anon "Anda mungkin ingin memakai kacamata hitam atau sesuatu juga."

    iwanka "Pada malam hari?"

    iwanka "Umm, itu seperti kecerobohan mode yang besar!"

    anon f_worried "Ya, baiklah... Begitu juga dengan menjadi gila!"

    iwanka "Apa?"

    iwanka "Tahukah Anda apa itu kecerobohan?"

    anon "{b}Iwanka{/b}, tolong temukan sesuatu..."

    iwanka "Uh, baiklah!"

    anon f_looking_down a_phone @ f_eyeroll a_facepalm "Yesus."

    pause
    pause
    show iwanka b_maid f_annoyed o_glasses with dissolve
    iwanka "Di sana."

    show anon f_normal a_idle with dissolve
    iwanka "Senang?"

    anon f_worried "Saya akan senang ketika kacang saya berhasil melewati penjaga dengan selamat."

    anon "Ayo, kita selesaikan ini."

    hide anon with dissolve
    iwanka @ f_eyeroll a_dust "Oh, jangan jadi banci!"

    hide iwanka with dissolve
    return True


label iwa01_wait_iwanka:
    show anon with dissolve

    jump iwa01_give_iwanka.retry
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
