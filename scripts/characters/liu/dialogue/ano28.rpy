label ano28_cash_liu_money:
    $ renpy.dynamic(bank=L_bank_lobby.is_here(M_liu))

    anon "Aku punya sesuatu untukmu."

    show anon a_backpack f_looking_down:
        xoffset 190
    show liu f_confused_down
    with {'master': dissolve}
    liu @ -m_talk "Hmm?"

    show anon a_stashed_bag
    show liu f_confused
    with {'master': dissolve}
    anon f_normal "Coba lihat."

    show anon a_stashed_bag_show
    show liu f_confused_down
    with dissolve
    show anon a_idle
    show liu a_bag_look
    with dissolve
    pause
    show anon f_grin
    liu f_surprised_down "!!!" with hpunch
    liu f_shocked "Dari mana kamu mendapatkan ini?!"

    anon f_normal "Itu adalah uang yang diambil {b}Ayah{/b} dari massa."

    liu f_surprised "Anda menemukannya?!"

    anon @ -m_talk "Mhmm."

    anon "Petunjuk yang Anda berikan kepada saya mengarah langsung ke sana."

    liu f_happy "Luar biasa, {b}[firstname]{/b}!"

    anon "Saya tahu, benar!"

    anon "Jadi saya ingin Anda mengambil apa yang diperlukan untuk melunasi hutang {b}[deb_name]{/b}."

    liu f_normal "Saya bisa melakukan itu."

    anon f_thinking "Lalu saya ingin Anda membagi sisanya."

    liu "Oke."

    anon f_shy "Masukkan setengahnya ke rekening bank saya..."

    liu @ -m_talk "Mhmm."

    anon f_normal "... dan separuh lainnya milikmu."

    show liu a_mouth_cover f_surprised m_talk with dissolve
    pause
    liu -m_talk "K-kamu tidak mungkin serius!"

    anon "aku serius."

    liu a_cover f_worried "Saya tidak bisa mengambil setengah uang Anda, {b}[firstname]{/b}."

    anon f_brag "Tentu saja bisa."

    show liu f_ashamed_down
    anon "Aku tahu betapa pentingnya kamu bagi {b}Ayah{/b} sebelum dia meninggal..."

    anon f_normal "... Dan Anda membutuhkannya."

    pause
    show liu a_sides f_nervous with {'master': dissolve}
    anon "Ditambah lagi, aku tidak akan pernah bisa mencapai semua ini tanpamu."

    liu "saya-"

    show liu f_nervous_lipbite
    pause
    liu f_happy "Saya tidak tahu harus berkata apa."

    anon "Anda tidak perlu mengatakan apa pun, {b}Liu{/b}."


    if bank:
        show anon f_confused
        show liu f_happy_down_back
        pause
        show anon a_up f_surprised with {'master': fastdissolve}
        anon "Tunggu, apa yang kamu-"

        show anon b_dressed_blocking:
            xoffset 130
        show liu b_dressed_jump
        show liu_desk as counter behind liu
        with dissolve
        pause .1
        show liu b_dressed_bend with vpunch
        pause
        show anon b_dressed f_surprised_teeth
        show liu b_dressed f_surprised_down m_talk
        with dissolve
        pause
        show anon f_surprised
        show liu f_surprised
        with dissolve
        pause
        show liu f_laugh -m_talk
        pause
        show anon b_empty f_surprised_low:
            xoffset 0
        show liu b_dressed_hug:
            xoffset 0
    else:

        show anon b_empty f_shy_low
        show liu b_robe_hug:
            xoffset 190

    with {'master': dissolve}
    liu "Anda adalah pria paling luar biasa yang masih hidup!"

    anon f_shy "Heh, serius... kamu pantas mendapatkannya."

    hide anon

    if bank:
        show liu b_dressed_kiss_2:
            xoffset -100
    else:
        show liu b_robe_kiss:
            xoffset 90

    with dissolve
    liu "MM."

    pause
    show anon a_sides b_dressed f_shy
    show liu a_sides f_happy

    if bank:
        show anon:
            xoffset -140
        show liu b_dressed:
            xoffset -440
    else:

        show anon:
            xoffset 50
        show liu b_robe_hair:
            xoffset -250

    with dissolve
    anon "Jadi kamu akan mengurus semuanya untukku?"

    liu "Y-ya, tentu saja!"

    liu "Saya akan melakukan apa pun yang Anda ingin saya lakukan, {b}[firstname]{/b}."

    anon "Terima kasih, {b}Liu{/b}."

    pause
    anon f_normal "Sekarang, permisi..."

    anon "... Saya harus pergi dan menyampaikan {b}[deb_name]{/b} kabar baik."

    hide anon with dissolve
    pause
    liu a_cover f_sexy "Ya Tuhan, dia pria yang sempurna..."

    return 'ano28'
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
