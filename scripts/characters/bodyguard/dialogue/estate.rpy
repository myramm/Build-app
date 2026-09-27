label bodyguard_button_estate:
    show bodyguard f_suspicious
    show anon with dissolve
    bodyguard "{i}*Ahem*{/i} Menurutmu kamu mau pergi ke mana?"

    anon f_worried @ -m_talk "Hmm?"

    bodyguard f_normal "Anda tidak seharusnya berada di sini."

    anon "O-oh, um..."

    anon @ f_confused "Bukankah ini rumah {b}Walikota Rump{/b}?"

    bodyguard "Ya itu benar."

    bodyguard "Dan itu terlarang bagi warga sipil!"


    menu bodyguard_button_estate.choice:

        "Saya di sini untuk menemui {b}Iwanka{/b}." if M_anon.finished_state(S_ano17_done):
            jump bodyguard_button_estate.assistant
        "Aku seharusnya berada di sini.":

            jump bodyguard_button_estate.manager
        "Maaf, saya tidak tahu.":

            pass

    anon "Maaf, saya tidak tahu."

    bodyguard "Lanjutkan sekarang, Pak."

    bodyguard "Kalau tidak, aku harus mengeluarkanmu dengan paksa."

    anon @ f_shock "Tidak perlu untuk itu!"

    anon @ a_wave "aku pergi."

    hide anon with dissolve
    return


label bodyguard_button_estate.assistant:
    anon f_brag @ f_brag_closed a_point "Saya asisten baru {b}Iwanka{/b}."

    show bodyguard a_crossed with fastdissolve
    bodyguard "Anda?!"

    pause
    bodyguard "Saya belum pernah mendengar apa pun tentang {b}Walikota Rump{/b} mempekerjakan asisten baru untuk putrinya..."

    anon f_worried "O-oh?"


    if player.stats.chr() < 5:
        jump bodyguard_button_estate.temporary

    anon f_normal "Itu mungkin karena walikota tidak mempekerjakan saya."

    bodyguard f_suspicious @ -m_talk "Hmm?"

    anon "Sebenarnya {b}Ny. Pantat{/b} yang mempekerjakan saya."

    bodyguard f_normal a_defensive "Oh!"

    bodyguard a_relief "Sekarang lihat, itu masuk akal!"

    bodyguard a_idle "Saya pikir {b}Ricky{/b} tidak akan cukup baginya..."

    anon f_confused "{b}Ricky{/b}?"

    bodyguard "Oh, jangan khawatir... Anda akan mengetahuinya."

    show anon f_surprised
    pause
    bodyguard "Anda bisa masuk ke dalam."

    anon f_worried "Saya bisa?"

    anon f_brag_closed "Maksudku, ya, tentu saja aku bisa."

    anon "Terima kasih."

    show anon f_snarky
    bodyguard "Pastikan saja {b}Ny. Rump{/b} memberimu {b}lencana staf{/b}, oke?"

    bodyguard "Kalau tidak, kita harus terus melakukan tarian ini."

    anon f_normal @ a_wave "Oke terima kasih."

    hide anon with {'master': dissolve}
    bodyguard "Semoga harimu menyenangkan, Pak."


    $ display.toast(chr_pass)
    scene expression L_rump_lobby.background_blur with fade
    show anon with dissolve
    anon @ f_laugh -m_talk "(Baiklah, rencana {b}Iwanka{/b} berhasil! )"

    anon f_worried @ -m_talk "(Sekarang saya hanya perlu mendapatkan {b}lencana staf{/b}. )"

    if game.timer.is_morning():
        anon f_bored @ -m_talk "(Para penjaga itu tak henti-hentinya melakukan hal itu!)"

        anon @ -m_talk "(Aku sudah menyia-nyiakan seluruh pagiku dengan para idiot itu.)"

    else:
        anon @ a_thinking f_thinking -m_talk "(Sepertinya itu akan sangat berguna.)"

        anon @ -m_talk "(Mungkin saya harus berbicara dengan {b}Iwanka{/b} tentang hal itu? )"

        pause
        anon @ -m_talk "(Aku hanya perlu menemukannya dulu...)"

    hide anon with dissolve
    return True

label bodyguard_button_estate.temporary:
    anon f_brag @ f_brag_closed "Itu mungkin karena saya hanya karyawan sementara..."

    anon "...Kau tahu, sampai mereka menemukan wanita yang lebih berkualitas."

    bodyguard f_suspicious "Sewa sementara?"

    anon f_worried "{i}*Gulp*{/i} Y-ya?"

    pause
    bodyguard f_normal "Suatu saat sementara saya mengkonfirmasi hal itu."

    bodyguard a_ear "Ya, kami memiliki karakter mencurigakan di depan yang mengaku sebagai asisten sementara {b}Nona Iwanka{/b}..."

    pause
    bodyguard @ -m_talk "Mmhmm."

    pause
    bodyguard "Jadi begitu."

    bodyguard a_ear "Haruskah saya menahannya, Pak?"

    anon f_shock "!!!"
    bodyguard "Itu afirmatif."

    show anon f_worried a_surprised_up_both with fastdissolve:
        xoffset -50
    anon "K-kamu tahu, setelah dipikir-pikir... Aku akan kembali lagi nanti."

    show anon f_surprised_teeth a_sides:
        xoffset -100
    show bodyguard a_stop
    with fastdissolve
    bodyguard "Tetap di tempat Anda sekarang, Tuan!"

    hide anon with fastdissolve
    anon "Astaga!!"


    scene black with dissolve
    pause 2

    $ display.toast(chr_fail)
    scene expression L_rump_front.background_blur with dissolve
    show anon b_dressed_catch_breath with dissolve
    anon "Haah... Haah..."

    anon @ -m_talk "(Hampir saja!)"

    anon @ -m_talk "(Saya benar-benar harus lebih berhati-hati dalam melakukan hal ini.)"

    hide anon with dissolve
    return


label bodyguard_button_estate.manager:
    anon @ a_behind_head "Aku seharusnya berada di sini."

    show bodyguard f_suspicious
    anon @ a_point "Aku uhh, di sini untuk... Hal?"

    bodyguard "Masalahnya?"

    anon @ a_behind_head "Ya, kamu tahu... Masalahnya... Di tempat..."

    show bodyguard a_crossed f_normal with dissolve
    pause
    anon "Mereka ingin aku mengurusnya."

    bodyguard @ -m_talk "..."
    anon @ -m_talk "..."
    bodyguard a_ear "Saya akan membutuhkan bantuan di gerbang depan, ada orang mencurigakan yang ingin masuk."

    anon f_shock "!!!"
    bodyguard "Bawa tasernya."

    show anon f_worried a_surprised_up_both with fastdissolve:
        xoffset -50
    anon "K-kau tahu, setelah dipikir-pikir lagi... Aku mungkin salah rumah."

    show bodyguard a_stop
    with fastdissolve
    bodyguard "Tetap di tempat Anda sekarang, Tuan!"

    hide anon with {'master': fastdissolve}
    anon "Jangan menggodaku, kawan!"


    scene black with dissolve
    pause 2

    scene expression L_rump_front.background_blur with dissolve
    show anon b_dressed_catch_breath with dissolve
    anon "Haah... Haah..."

    anon @ -m_talk "(Hampir saja!)"

    anon @ -m_talk "(Saya benar-benar harus lebih berhati-hati dalam melakukan hal ini.)"

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
