label con01_init_melonia:
    anon f_worried "Bisakah saya berbicara dengan Anda tentang {b}Consuela{/b}?"

    melonia f_confused "Siapa?"

    anon "Anda tahu, pembantunya?"

    melonia @ -m_talk "..."
    anon "Wanita yang membersihkan rumahmu."

    melonia "Oh, maksudmu perempuan jalang gemuk dengan gigi berlubang itu?"

    anon "{i}*Huh*{/i} Kurasa?"

    melonia "Suamiku tidak menghamilinya, bukan?"

    anon f_surprised "APA?!"

    melonia f_annoyed "Karena aku akan membawanya pulang ke rumah sebelum dia bisa berkedip!"

    anon "TIDAK!!"

    anon "Tidak tidak tidak!"

    show anon f_worried
    melonia "Anda yakin?"

    anon "Cukup yakin."

    melonia f_normal @ f_eyeroll a_heart "Oke, fiuh..."

    melonia "Jangan menakutiku seperti itu, {b}Hector{/b}!"

    anon "M-maaf."

    pause
    anon "Bolehkah saya bertanya mengapa Anda mempekerjakannya?"

    melonia f_annoyed "saya tidak melakukannya."

    melonia "Suami saya yang bodoh mempekerjakannya dan bukan karena kemampuannya membersihkan, saya dapat memberitahu Anda itu!"

    anon "Mengapa kamu tidak menggantinya dengan orang lain saja?"

    melonia f_normal @ f_eyeroll "Kayaknya sesederhana itu..."

    melonia "Carikan saya seseorang yang mau melakukan pekerjaan rumah tangga dengan upah di bawah upah minimum dan tahan menghadapi suami saya yang terus-menerus melecehkan mereka."

    anon "Jika ya, maukah Anda mengizinkan saya membawa {b}Consuela{/b} keluar dari sini?"

    melonia f_confused "Anda ingin membawanya?"

    anon "Ya."

    pause
    melonia "Untuk apa?!"

    pause
    melonia f_smirk @ f_eyeroll "Anda tahu, sudahlah."

    melonia "Aku tidak peduli, bawa dia."

    pause
    melonia @ f_confused "Meskipun alasanmu menginginkan perempuan jalang jelek itu berada di luar jangkauanku..."

    melonia "Dia bahkan tidak bisa berbahasa Inggris!"

    anon f_normal "Saya akan {b}membawakan Anda penggantinya{/b}, jangan khawatir."

    melonia @ f_eyeroll "Eh ya."

    hide anon with {'master': dissolve}
    melonia @ f_laugh "Bawakan aku leprechaun juga, selagi kamu melakukannya!"


    $ player.go_to(L_rump_lobby)
    scene expression player.location.background_blur with None
    show anon f_thinking with dissolve
    anon @ -m_talk "( Hmm, jadi aku perlu {b}menemukan seseorang{/b} yang akan membersihkan rumah ini dengan upah di bawah upah minimum dan tidak akan diganggu oleh walikota yang terus-menerus melecehkan mereka... )"

    pause
    anon f_sad_down @ -m_talk "(Saya tidak akan pernah menemukan orang seperti itu!)"

    anon @ -m_talk "(Ini adalah rencana yang buruk.)"

    pause
    anon f_worried @ -m_talk "( Mungkin {b}Saya harus berbicara dengan Ricky{/b} dan melihat apakah dia mengenal seseorang yang mungkin bersedia? )"

    hide anon with dissolve

    $ M_consuela.trigger(T_con01_init)
    return


label con01_plan_melonia:
    melonia "Apakah kamu sudah menemukan pengganti pelayan menjijikkan itu?"


    if venue == 'hottub':
        show anon f_worried_low
    else:
        show anon f_worried

    anon "Tidak, belum."

    melonia f_laugh "Semoga berhasil menemukan seseorang yang mau melakukan pekerjaan rumah tangga dengan upah di bawah upah minimum dan tahan menghadapi suami saya yang terus-menerus melecehkan mereka."


    if venue == 'hottub':
        show melonia f_normal_up
    else:
        show melonia f_normal

    anon "Saya akan {b}mencari penggantinya{/b}."

    anon @ a_point "Ingat saja, kamu berjanji akan mengizinkanku membawa {b}Consuela{/b} keluar dari sini jika aku melakukannya."

    melonia @ f_eyeroll "Eh ya."

    jump melonia_button_common.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
