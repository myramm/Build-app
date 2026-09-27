label nad01_find_svetlana:
    show anon with dissolve:
        xoffset -100
        xzoom -1
    anon "Hei, aku kenal kamu!"

    show svetlana f_happy a_surprised with dissolve:
        xoffset 150
        xzoom -1
    svetlana "Ahh, manusia kecil itulah yang menyelamatkan kita dari manusia jahat."

    svetlana a_sides "Senang bertemu denganmu lagi."

    anon "Jadi ke sinilah kamu menghilang?"

    svetlana "Ya."

    svetlana "Saya bekerja keamanan sekarang untuk {b}Nona Chernyshevsky{/b}."

    anon f_brag "Tidak bercanda?"

    svetlana a_hips "Dia wanita yang baik."

    svetlana "Membayar banyak uang dan memperlakukan kami dengan baik."

    anon "Yah, aku senang mendengarnya."

    svetlana "Anda punya janji?"

    anon f_shy a_behind_head "Eh, ya?"

    svetlana "Satu detik."

    show anon a_sides f_normal:
        xoffset 370
        xzoom 1
    show svetlana a_sides:
        xoffset 700
    with {'master': dissolve}
    svetlana f_normal "{b}Nona Chernyshevsky{/b}?"

    show anon f_confused
    nadya "What is it, {b}Svetlana{/b}?" (show_native="Chego ty khochesh', {b}Svetlana{/b}?")
    svetlana "The young man you've been waiting for is here to see you." (show_native="K vam prishel molodoy chelovek, kotorogo vy tak dolgo zhdali.")
    show anon a_phone f_normal_low with {'master': dissolve}:
        xoffset -200
        xzoom -1
    nadya "Shit." (show_native="Blyat.")
    show anon with {'master': dissolve}:
        xoffset -400
    nadya "Wait one second." (show_native="Podozhdite odnu sekundu.")
    show svetlana with {'master': dissolve}:
        xzoom 1
        xoffset 150
    svetlana m_talk "Dia baru saja menyelesaikan pembicaraan bisnis dengan {b}Katya{/b}."

    show anon a_sides f_normal with {'master': dissolve}:
        xoffset 100
        xzoom 1
    svetlana -m_talk "Suatu saat."

    anon "Oke."

    pause
    show katya b_naked_disheveled f_surprised a_clothes behind svetlana with dissolve:
        xoffset -80
    pause
    show svetlana f_happy
    anon f_surprised_low a_surprised_up @ -m_talk "!!!"
    katya f_happy "Halo."

    anon f_flirt a_behind_head "H-hai."

    pause
    show svetlana f_curious
    katya f_concerned "Ehh..."

    katya "... Tolong, permisi."

    hide katya
    show anon a_sides f_flirt_grin:
        xoffset -400
        xzoom -1
    with dissolve
    pause
    svetlana f_smirk a_hips "{b}Nona Chernyshevsky{/b} sampai jumpa sekarang."

    show anon with {'master': dissolve}:
        xoffset 100
        xzoom 1
    anon f_confused @ -m_talk "Hmm?"

    anon f_shy "Oh iya... terima kasih!"

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
