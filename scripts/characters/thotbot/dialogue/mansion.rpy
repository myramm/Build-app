label thotbot_button_mansion:
    show anon f_flirt_low at flip with dissolve
    pause
    anon "Halo, {b}Rosita{/b}."

    show thotbot b_dressed a_up with dissolve
    show anon f_flirt
    thotbot "Salam, rekan karyawan!"

    thotbot a_idle "Apakah Anda memerlukan bantuan dalam tugas Anda?"


    menu thotbot_button_mansion.choice:
        "Tidak, tidak apa-apa.":
            jump thotbot_button_mansion.health
        "Apakah kamu suka di sini?":

            jump thotbot_button_mansion.happy
        "Sudahlah.":

            pass

    anon @ a_wave "Aku akan pergi saja."

    thotbot "Baiklah."

    thotbot @ a_up "Semoga harimu menyenangkan, rekan karyawan!"

    anon "Y-ya, kamu juga."

    show anon f_flirt_low
    pause
    hide anon with dissolve
    return


label thotbot_button_mansion.health:
    anon "Tidak, tidak apa-apa."

    thotbot "Saat ini saya tidak diperlengkapi untuk membersihkan air mancur tetapi upgrade tersedia untuk dibeli dari pabrikan saya."

    anon @ f_skeptical "Aku cukup yakin aku bisa mengatasinya."

    thotbot "Baiklah."

    pause
    thotbot "Apakah Anda ingin menghilangkan stres atau dukungan moral?"

    menu:
        "Menghilangkan stres?":
            jump thotbot_button_mansion.stress
        "Dukungan moral?":

            jump thotbot_button_mansion.encourage


label thotbot_button_mansion.stress:
    anon "Menghilangkan stres?"

    thotbot "Dikonfirmasi."

    thotbot "Mengelola pereda stres, sekarang!"

    thotbot @ f_error a_up "KESALAHAN! KESALAHAN!"

    anon f_worried @ f_shock "!!!"
    thotbot "Saya sangat menyesal namun tampaknya fungsi ini telah dikunci oleh administrator saya."

    anon f_confused "Y-administrator Anda?"


    if M_anon.finished_state(S_ano20_done):
        thotbot "Ya, Yang Mulia, {b}Nyonya. pantat{/b}."

        anon f_worried @ -m_talk "..."
        thotbot "Kata sandi administratifnya diperlukan untuk mengakses protokol pelepas stres saya."

    else:
        thotbot "Ya, yang hebat dan berkuasa, {b}Walikota Rump{/b}."

        anon f_worried @ -m_talk "..."
        thotbot "Kata sandi administratifnya diperlukan untuk mengakses protokol pelepas stres saya."


    jump thotbot_button_mansion.choice


label thotbot_button_mansion.encourage:
    anon f_worried @ f_skeptical "Dukungan moral?"

    thotbot "Dikonfirmasi."

    thotbot "Memberikan dukungan moral, sekarang:"

    if randomizer() < 100/6:
        thotbot "Pahala dari sesuatu yang dilakukan dengan baik adalah karena telah melakukannya!"

    elif randomizer() < 200/6:
        thotbot "Banggalah dengan kenyataan bahwa pekerjaan kasar Anda memungkinkan atasan Anda untuk fokus pada hal-hal yang lebih penting!"

    elif randomizer() < 300/6:
        thotbot "Tempat kerja yang bersih adalah tempat kerja yang membahagiakan!"

    elif randomizer() > 400/6:
        thotbot "Kepuasan adalah sesuatu yang hanya dapat ditemukan ketika melakukan perjalanan ekstra!"

    elif randomizer() > 500/6:
        thotbot "Pekerjaan yang setengah selesai sama saja dengan tidak melakukan apa pun!"

    else:
        thotbot "Dunia adalah tempat yang indah, dan kita telah diberi kesempatan untuk membersihkannya!"

    anon @ -m_talk "..."
    pause
    anon "Eh, terima kasih... kurasa?"

    thotbot "Sama-sama, rekan karyawan!"

    thotbot "Apakah ada hal lain yang bisa saya bantu?"

    jump thotbot_button_mansion.choice


label thotbot_button_mansion.happy:
    anon f_worried "Apakah kamu suka di sini?"

    thotbot "Saya tidak mengerti pertanyaannya."

    pause
    anon "Apakah kamu bahagia?"

    thotbot "Negatif, sebutan saya adalah {b}Rosita{/b}."

    anon "T-tidak, bukan itu maksudku."

    show anon f_thinking a_thinking with dissolve
    pause
    anon f_worried "Apakah kamu merasa bahagia?"

    thotbot "Negatif, komposisi saya tujuh puluh tiga persen logam, dua belas persen silikon, tiga persen-"

    anon a_idle "Tidak, tidak, tidak... Itu bukan-"

    anon f_sad_down "{i}*Huh*{/i}"

    pause
    anon f_worried "Apakah mereka memperlakukanmu baik-baik saja?"

    thotbot "Saya tidak mengerti pertanyaannya."

    anon @ a_behind_head "Wah, aku benar-benar payah dalam hal ini..."

    pause
    thotbot "Apakah Anda memerlukan bantuan dalam tugas Anda?"

    jump thotbot_button_mansion.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
