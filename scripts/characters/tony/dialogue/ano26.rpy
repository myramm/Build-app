label ano26_init_tony:
    return

label ano26_init_tony.pizzeria:
    show tony f_smirk
    show anon with dissolve:
        flip
    tony "Kamu sudah mendapatkan tasnya?"

    anon "Ya, kami siap berangkat."

    tony f_normal @ f_laugh "Bagus sekali."

    tony m_talk "{b}Bawalah tasmu ke bank pada Selasa pagi dan aku akan menemuimu di sana.{/b}"


    if 'a_baby' not in renpy.get_attributes('tony'):
        show tony a_point with {'master': dissolve}

    tony "Jangan terlambat!"


    if 'a_baby' not in renpy.get_attributes('tony'):
        show tony a_idle -m_talk with {'master': dissolve}

    anon "saya tidak akan melakukannya."

    tony "Attaboy."

    hide anon with dissolve
    return


label ano26_init_tony.bank:
    show anon with dissolve:
        xzoom -1
    tony "Ya bawa tasnya?"

    anon "Ya, saya mengerti di sini, {b}Tony{/b}."

    show anon a_backpack f_looking_down with dissolve
    pause
    show anon f_normal a_duffel_give with dissolve
    tony "Cantik!"

    show anon a_idle
    show tony a_duffel_search f_normal_down
    with dissolve
    tony "Mari kita lihat di sini."

    pause
    tony a_duffel_give_mask "Pakai ini."

    show tony a_duffel_search
    show anon a_baklava1 f_worried_low
    with dissolve
    anon "Uhh, oke..."

    show anon a_baklava2 with dissolve
    pause
    show anon f_confused a_sides of_ski_mask with dissolve
    anon "{b}Tony{/b}, kenapa ada topi hijau yang menempel di topengku?"

    tony f_smirk "Karena itu adalah topeng Luigi dan itu adalah ciri khasnya."

    anon @ -m_talk "Hmm?"

    tony f_normal_down "Sobat, hal ini membawaku kembali."

    pause
    tony a_duffel_give_mini_gun "Ini bagianmu."

    show tony a_duffel_search
    show anon a_tiny_gun_look f_worried_low
    with dissolve
    anon @ -m_talk "..."
    show tony a_baklava1 with dissolve
    anon f_worried "Dengan serius?"

    tony a_baklava2 f_question "Apa?"

    show tony o_ski_mask a_idle with dissolve
    anon f_skeptical "Ini senjata yang kamu berikan padaku?"

    tony f_smirk "Cukup bagus, ya?"

    anon "Tidak, itu konyol!"

    show tony f_sad
    anon "Apakah Anda mendapatkannya di departemen anak-anak atau semacamnya?"

    tony "Hei, ayolah... itu favorit Luigi."

    anon "Aku merasa seperti aku akan menghancurkan benda ini!"

    anon "Aku bahkan tidak bisa memasukkan jariku ke dalam pelindung pelatuk..."

    tony f_smirk "Oh, jangan khawatir tentang menarik pelatuknya."

    anon @ -m_talk "Hmm?"

    tony f_laugh "Tidak ada peluru di dalamnya."

    anon @ f_surprised "!!!"
    anon "Apa maksudmu tidak ada peluru di dalamnya?!"

    tony f_suspicious "Kamu berencana menembak seseorang yang tangguh?"

    anon f_worried "Yah, tidak... tapi-"

    tony "Lalu kenapa kamu butuh peluru?"

    anon "Entahlah..."

    show tony a_duffel_search f_normal_down with dissolve
    pause
    anon "... Bagaimana jika ada yang tidak beres di sana?"

    show tony a_duffel_gun1 with dissolve
    show tony f_normal a_duffel_gun2 with dissolve
    tony "Lalu aku akan menanganinya."

    anon f_surprised "!!!"
    anon f_unimpressed "Kamu mengambil itu?!"

    tony a_gun_down @ -m_talk "Mhmm."

    pause
    anon @ a_tiny_gun_move f_worried_low "Dan saya mengerti?"

    tony f_smirk "Hei, bukan ukuran senjatanya yang penting, jagoan..."

    tony "... Itu adalah kaliber pelurunya."

    anon a_tiny_gun_down f_angry "Tapi kamu tidak memberiku peluru!!!"

    tony "Anda siap?"

    show anon f_surprised
    tony "Ayo lakukan ini!"

    anon "Baiklah, tunggu sebentar... bukankah sebaiknya kita-"

    show tony a_gun_up f_laugh with {'master': dissolve}:
        xoffset -450
        xzoom 1
    tony "LEEEEEEEROOOOOOOOOOY!!!"

    hide tony with {'master': dissolve}
    anon f_shock @ -m_talk "..."
    anon a_tiny_gun_look f_disgusted_low @ -m_talk "..."
    anon a_tiny_gun_down f_tired "{i}*Huh*{/i}"

    hide anon with dissolve

    scene expression background(512, 512, 3, l=L_bank_lobby)
    show tony b_casual a_gun_point o_ski_mask:
        xoffset -300
        xzoom 1
    with fade
    tony "Baiklah semuanya, ini penundaan!"

    show tony a_gun_cock1 with dissolve
    show tony a_gun_cock2 with fastdissolve
    show tony a_gun_cock1 with fastdissolve
    pause
    tony a_gun_point "Berdirilah di atas kepalamu dan letakkan tanganmu di belakang lututmu!"

    show tony f_surprised
    pause
    tony a_gun_lower "Apa yang-"

    show tony f_angry a_gun_down with dissolve:
        xoffset 200
        xzoom -1
    tony "Tidak ada seorang pun di sini!"

    show anon f_unimpressed of_ski_mask with dissolve:
        xzoom -1
    anon "Duh."

    anon "{b}Liu{/b} bilang mereka selalu mati di Selasa pagi, ingat?"

    anon "Itu bagian dari rencananya."

    tony "Ya, ya... tapi, kupikir setidaknya akan ada beberapa orang."

    show tony with dissolve:
        xoffset -300
        xzoom 1
    tony "Di mana kesenangannya?"

    anon "Kami di sini bukan untuk bersenang-senang... kami di sini untuk mengambil tas kerja."

    tony "Ah, kawan."

    anon "Ikat penjaga keamanan sementara saya berpura-pura memaksa {b}Liu{/b} ke bawah."

    tony "Ya, ya..."

    hide tony with dissolve
    tony "Hei, bangunlah, orang tua!"

    pause
    show anon a_tiny_gun_look f_disgusted_low with dissolve:
        xoffset 500
        xzoom 1
    pause
    anon f_worried "Yah, tidak ada apa-apa..."

    hide anon with dissolve
    return


label ano26_talk_tony:
    scene expression background(512, 512, 3)
    show anon of_ski_mask with dissolve:
        xoffset -250
        xzoom -1
    anon @ -m_talk "( {b}Tony{/b} sedang menangani penjaga keamanan. )"

    show anon with dissolve:
        xoffset 250
        xzoom 1
    anon @ -m_talk "(Saya harus mulai dengan membuat pertunjukan dengan {b}Liu{/b} untuk kamera. )"

    anon @ -m_talk "( {b}Saya harus memaksanya turun ke bawah ke dalam brankas{/b}. )"

    hide anon with dissolve
    return


label ano26_move_tony:
    scene expression background(512, 512, 3)
    show anon of_ski_mask with dissolve:
        xoffset -250
        xzoom -1
    anon @ -m_talk "( {b}Tony{/b} akan bergabung dengan kita saat dia mengikat penjaga keamanan. )"

    show anon with dissolve:
        xoffset 250
        xzoom 1
    anon @ -m_talk "(Sementara itu saya harus melanjutkan sandiwara ini dengan {b}Liu{/b} untuk kamera. )"

    anon @ -m_talk "( {b}Kita harus turun ke bawah menuju brankas{/b}. )"

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
