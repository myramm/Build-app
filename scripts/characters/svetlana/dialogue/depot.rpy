label svetlana_button_depot:
    show anon a_wave with {'master': dissolve}:
        xoffset 100
        xzoom -1
    anon "Hai, {b}Svet{/b}."

    show anon a_sides
    show svetlana a_sides:
        xoffset 150
        xzoom -1
    with dissolve
    svetlana "Halo."


    menu svetlana_button_depot.choice:
        "Hanya menjaga pintu kantor yang lama ya?":
            jump svetlana_button_depot.guard
        "Kamu pernah istirahat?":

            jump svetlana_button_depot.break
        "Selamat bersenang-senang.":

            pass

    anon f_normal "Nikmati seluruh keadaan Anda yang berdiri diam dan tampak mengancam."

    svetlana "Ya."

    svetlana f_smirk "Nikmati saat-saat seksi Anda bersama {b}Nona Chernyshevsky{/b}."

    anon f_surprised @ -m_talk "!!!"
    svetlana "Saya akan menghitung orgasmenya."

    show anon a_behind_head f_shy of_blush with {'master': dissolve}
    anon "Wah oke..."

    anon "... Tapi tidak ada tekanan, kan?"

    svetlana f_concerned "Tekanan sangat penting untuk orgasme yang baik."

    svetlana f_smirk "Coba gunakan pada klitoris untuk hasil yang luar biasa."

    show anon a_surprised f_shock -of_blush with {'master': dissolve}
    anon @ -m_talk "..."
    show anon a_sides f_shy
    with {'master': dissolve}
    anon "B-benar."

    show anon a_salute
    with {'master': dissolve}
    anon "Akan dilakukan."

    show anon a_sides
    with {'master': dissolve}
    anon "Terima kasih, {b}Svetlana{/b}."

    show svetlana a_wave with {'master': dissolve}
    svetlana "Farewell, {b}[firstname]{/b}" (show_native="Do svidaniya, {b}[firstname]{/b}.")
    hide anon with dissolve
    return


label svetlana_button_depot.break:
    anon f_normal "Kapan istirahatmu selanjutnya?"

    show svetlana a_crossed f_normal with {'master': dissolve}
    svetlana "{b}Nona Chernyshevsky{/b} tidak membayar saya untuk istirahat."

    anon f_confused "Ya, oke... Tapi pastinya kamu harus tidur kapan-kapan?"

    show anon f_surprised
    show svetlana a_sides f_annoyed
    with {'master': dissolve}
    svetlana "Jadwal tidurku seharusnya bukan urusanmu."

    show anon f_worried
    svetlana "Saya pengawal dan {b}Nona Chernyshevsky{/b} memberi saya banyak uang."

    svetlana f_happy "Dia wanita yang baik dan aku tidak akan mengecewakannya."

    anon @ -m_talk "Hmm."

    anon f_normal "Baiklah, itu cukup adil, menurutku..."

    jump svetlana_button_depot.choice


label svetlana_button_depot.guard:
    anon f_confused "Hanya menjaga pintu kantor yang lama ya?"

    svetlana f_normal "Ya."

    show anon f_normal
    svetlana "{b}Nona Chernyshevsky{/b} lebih menyukai privasi saat berada di dalam kantor."

    show svetlana a_hips f_happy
    with {'master': dissolve}
    svetlana "Tapi saya selalu siap jika dia membutuhkan saya."

    anon @ -m_talk "Mhmm."

    pause
    show svetlana a_sides with {'master': dissolve}
    anon f_shy "Yah, kacang keren, kurasa."

    jump svetlana_button_depot.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
