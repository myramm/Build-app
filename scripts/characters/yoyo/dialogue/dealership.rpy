label yoyo_button_dealership:
    show anon f_worried with dissolve
    yoyo "Selamat datang di Saga Dearership, bagaimana bisa {b}Kim{/b} herp-"

    yoyo "Oh, apakah kamu?"

    show yoyo a_idle
    with {'master': dissolve}
    yoyo "Apa yang kamu inginkan, pria bodoh?"


    menu yoyo_button_dealership.choice:
        "Bisakah kita tidak melakukan ini?":
            jump yoyo_button_dealership.vendetta

        "Apa urusanmu dan {i}lainnya{/i} {b}Kim{/b}?" if M_yoyo.is_state(S_yoy01_init):
            jump yoyo_button_dealership.villain
        "Tidak ada apa-apa.":

            pass

    anon f_brag "Tidak ada apa-apa."

    yoyo "Lalu pergi."

    yoyo "Hari perhitungan cepat Anda semakin dekat."

    yoyo "Kamu akan menyesali hari ketika kamu mengacaukan keluarga {b}Kim{/b}."

    anon "Eh ya."

    show anon a_wave f_unimpressed with {'master': dissolve}
    anon "Semoga beruntung dengan itu."

    hide anon with dissolve
    yoyo f_angry @ -m_talk "..."
    pause
    yoyo "Dasar pria bodoh..."

    yoyo "... Aku akan segera menjemputmu."

    return


label yoyo_button_dealership.vendetta:
    anon f_confused "Bisakah kita tidak melakukannya?"

    yoyo f_quizzical @ -m_talk "...?"
    anon f_worried "Kau tahu, seluruh musuh bebuyutan ini... penjahat jahat yang ingin membalas dendam atas keluarga mereka yang juga jahat..."

    show yoyo f_normal
    anon "... Karena aku harus memberitahumu, aku sangat lelah setelah berurusan dengan kakakmu..."

    pause
    anon f_confused "... Tidak?"

    show yoyo a_crossed with dissolve
    pause
    anon f_tired "{i}*Huh*{/i} Baik."

    jump yoyo_button_dealership.choice


label yoyo_button_dealership.villain:
    anon f_confused "Sebenarnya apa urusanmu dan kakakmu?"

    yoyo f_quizzical "Sayang?!"

    anon "Ya, Anda tahu... keseluruhan cerita penjahat jahat di buku komik..."

    anon f_confused "... Apakah kalian punya kisah tragis atau sesuatu yang menjelaskan semua ini?"

    yoyo f_confused "Menurutmu {b}Kim{/b} baik?"

    show anon a_frustrated f_shy
    with {'master': dissolve}
    anon "Nah, jika sepatunya pas..."

    show yoyo a_gimme f_annoyed
    with {'master': dissolve}
    yoyo "Apakah ini benar-benar takdir seseorang?!"

    show anon a_sides f_confused
    with {'master': dissolve}
    anon "... Eh?"

    show yoyo a_reach
    with {'master': dissolve}
    yoyo "Keluarga {b}Kim{/b} ditakdirkan untuk membaca!"

    show anon f_surprised
    yoyo "Ini adalah beban berat yang harus ditanggung oleh {b}Kim{/b} demi kemanusiaan!"

    show yoyo a_sides
    with {'master': dissolve}
    anon f_worried "Oke, jadi kamu benar-benar gila."

    yoyo "{b}Kim{/b} tidak gila, {b}Kim{/b} tuhan!"

    show anon f_surprised
    show yoyo a_fists
    with {'master': dissolve}
    yoyo f_angry @ f_angry_teeth_up "KESAYANGAN TUHAN!!"

    anon f_skeptical "Ya, lihat... itu pembicaraan gila."

    show yoyo a_hips f_quizzical
    with {'master': dissolve}
    yoyo "Oh, sekarang {b}Kim{/b} evir {i}dan{/i} gila?!"

    anon f_worried "Maksudku, kamu harus mempertimbangkan kemungkinan itu, ya."

    show anon a_surprised_up_both f_surprised_teeth
    show yoyo a_frustrated f_angry
    yoyo "NO!!!" with hpunch
    show anon a_surprised_up f_worried_surprised
    with {'master': dissolve}
    yoyo "{b}Kim{/b} pembaca tertinggi!!"

    show anon a_sides f_unimpressed
    with {'master': dissolve}
    yoyo "{b}Kim{/b} harus mundur dari tempat tinggi dengan tangan besi!!"

    anon "Benar."

    show anon a_point_back
    with {'master': dissolve}
    anon "Umm, aku akan pergi saja."

    yoyo "Kata-kata bergetar di kaki {b}Kim{/b}!"

    hide anon
    with {'master': dissolve}
    yoyo "Hei, mau kemana?!"

    yoyo "Kembali ke sini dan berlutut sebelum {b}Kim{/b}!!"

    show yoyo a_hips
    with {'master': dissolve}
    yoyo "Dasar anak nakal!!"

    yoyo "Kembalilah dan mohon maaf!!"

    return T_yoy01_init
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
