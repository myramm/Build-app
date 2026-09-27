label jab_button_cargo:
    $ renpy.dynamic(queries=set())

    show thug a_bottle_drink f_drink -m_talk with dissolve
    pause
    show anon with dissolve:
        xoffset 150
        xzoom -1
    pause
    show anon:
        xoffset -300
        xzoom -1
    show thug a_bottle_throw f_surprised
    with dissolve
    pause
    show anon a_surprised f_hurt:
        xoffset -575
    show thug a_wave b_dressed
    with {'master': dissolve}
    jab "Hello, friend." (show_native="Privet, comrade {b}[firstname]{/b}.")
    show anon a_sides f_tired with dissolve
    pause
    show anon with {'master': dissolve}:
        xoffset -75
        xzoom 1
    anon "Hai, {b}Jab{/b}."

    jab a_sides "Bisakah saya mengajukan pertanyaan?"


    menu jab_button_cargo.choice:
        "Eh, tentu saja.":
            jump jab_button_cargo.question
        "Nama macam apa itu {b}Jab{/b}?":

            jump jab_button_cargo.name
        "Tidak sekarang.":

            pass

    if len(queries) > 8:
        show anon a_crossed f_annoyed with {'master': dissolve}
        anon "Tunggu!"

        anon f_confused "Bagaimana mungkin Anda bisa mendapatkan lebih banyak?!"

    elif queries:
        show anon a_up f_worried with {'master': dissolve}
        anon "Tolong jangan lagi!"

    else:
        anon "Tolong jangan sekarang."


    show thug a_defensive f_normal with {'master': dissolve}
    jab "Oke, tapi mungkin saya bisa memberi Anda dokumen yang sedang saya kerjakan ini dengan saran untuk membuat game lebih baik?"

    show anon a_sides
    show thug a_sides
    with {'master': dissolve}
    anon f_confused "Ehh..."

    jab "Hanya dua puluh lima halaman tetapi masih banyak lagi yang akan datang, jadi jangan khawatir."

    anon f_surprised "Dua puluh lima halaman?!"

    anon f_confused "Apa-"

    show thug a_scratch_head f_concerned with {'master': dissolve}
    jab "Ehh, maaf... Dua puluh delapan."

    jab "Saya lupa saya menambahkan ide saya untuk membuat momen seksi dengan semua wanita di rumah pantai."

    show anon a_pocket
    show thug a_sides
    with {'master': dissolve}
    anon "Kami sudah merencanakannya."

    jab f_happy "Oh bagus. Maka ide saya sangat membantu."

    anon f_skeptical @ -m_talk "..."
    show anon a_point f_confused
    with {'master': dissolve}
    anon "..."
    show anon a_sides f_sad_down
    with {'master': dissolve}
    anon @ -m_talk "..."
    show thug:
        xoffset 500
        xzoom -1
    with {'master': dissolve}
    jab "Biarkan aku menemukan dokumenku..."

    show anon a_surprised_up_both f_surprised_teeth
    hide thug
    with {'master': dissolve}
    jab "... Aku tahu mereka ada di sini di suatu tempat."

    show anon a_protect f_worried with {'master': dissolve}
    jab "Anda ingin saya memberi Anda diagram untuk perluasan peta di masa mendatang?"

    show anon:
        easeout 3 xoffset -800
    jab "Awalnya saya membuat lima tetapi sekarang telah berkembang menjadi dua belas."


    scene expression background(104, 512, 5, l=L_warehouse_depot) with fade
    show anon b_dressed_catch_breath with fastdissolve:
        xoffset -100
    anon @ -m_talk "(Haah... Haah...)"

    anon @ -m_talk "(Ya ampun, haah... Itu menakutkan!)"

    show anon a_surprised b_dressed f_worried with {'master': dissolve}
    anon "(Aku harus terus berjalan, dia mungkin masih menemukanku di sini...)"

    hide anon with fastdissolve
    return 'escape'


label jab_button_cargo.name:
    show anon a_wave f_normal_closed with {'master': dissolve}
    anon "Izinkan {i}saya{/i} bertanya..."

    show anon a_sides f_skeptical
    with {'master': dissolve}
    anon "... Nama macam apa itu {b}Jab{/b}?"

    jab f_happy "Merupakan kependekan dari {b}Jabzap{/b}."

    show anon f_confused
    jab "Nama panggilan."

    anon f_skeptical "Jadi siapa nama aslimu?"

    show thug a_finger f_smirk with {'master': dissolve}
    jab "Oh, aku mengerti apa yang kamu lakukan..."

    jab "... Jangan menipuku, kawan!"

    anon f_confused "Hah?"

    show thug a_chest with {'master': dissolve}
    jab "Pikiran orang Rusia kuat!"

    jab "Saya tidak akan menjadi korban permainan pikiran licik Anda!"

    anon f_sad_down "Anda tahu apa..."

    anon "... Sudahlah."

    anon "Saya tidak ingin tahu."

    show thug a_sides f_laugh with {'master': dissolve}
    jab "Ah hah!"

    jab f_happy "Saya menang!"

    show thug f_laugh
    anon f_worried "Tidak, aku sungguh tidak ingin tahu."

    jab f_happy "Terlambat!"

    jab "saya menang."

    show thug f_laugh
    show anon a_pocket
    with {'master': dissolve}
    anon "Benar... Terserah."

    anon "Tidak peduli."

    jab f_normal "Saya juga tidak."

    pause
    jab f_happy "Karena saya sudah menang."

    show anon a_crossed f_annoyed
    show thug f_laugh
    with {'master': dissolve}
    anon "Tidak, kamu tidak melakukannya!"

    jab f_happy "Ya, benar."

    pause
    show thug a_cheer1 f_smirk with dissolve
    show thug a_cheer with None
    jab "Lakukan {b}Jab{/b}!!"

    extend "Lakukan {b}Jab{/b}!!"

    extend "Lakukan {b}Jab{/b}!!"

    show thug a_cheer1 with None
    anon f_eyeroll "Astaga, kamu menyebalkan!"

    hide anon with {'master': dissolve}
    jab f_concerned "Oh ayolah, jangan jadi pecundang!"

    return


label jab_button_cargo.question:
    python:
        renpy.dynamic(q=random.randint(1, 9),
                      intro=random.random(), outro=random.random())
        queries.add(q)

    if intro <= .33:
        anon "Eh, tentu saja."

    elif intro <= .66:
        anon "Saya rasa..."

    elif intro <= .99:
        anon "Kenapa tidak?"

    else:
        anon "Adakah yang bisa mencegah hal itu sekarang?"


    call expression 'jab_button_cargo.question{}'.format(q)

    if outro < .40:
        show anon a_thinking f_thinking
    elif outro < .80:
        show anon a_rub f_worried
    else:
        show anon a_crossed f_thinking_down

    with {'master': dissolve}
    anon @ -m_talk "(Saya tidak tahu bagaimana menanggapi ini...)"

    show anon a_sides f_shy -of_blush with {'master': dissolve}
    anon "Biarkan saya menghubungi Anda kembali tentang hal itu."

    show thug a_sides f_normal_down with {'master': dissolve}
    jab "{i}*Huh*{/i} Baiklah..."

    pause
    jab f_normal "Satu pertanyaan lagi?"

    show anon f_tired
    jump jab_button_cargo.choice


label jab_button_cargo.question1:
    show thug a_hips f_normal with {'master': dissolve}
    jab "Tampaknya banyak karakter di kota yang mengubah penampilan."

    show anon f_confused
    jab "Kebanyakan orang tampaknya berpikir ini adalah perbaikan tetapi saya tidak yakin..."

    jab f_confused "... Bukankah lebih baik membiarkan mereka apa adanya?"

    show anon a_behind_head with {'master': dissolve}
    anon "Ehh..."

    jab "Menurut saya, perubahan bukan tanpa alasan yang jelas."

    return


label jab_button_cargo.question2:
    jab f_normal "Saya mendengar cerita tentang wanita yang mengubah rumah menjadi kandang hewan..."

    show anon f_worried_surprised
    show thug a_confused f_confused
    with {'master': dissolve}
    jab "... Mengapa seseorang melakukan ini?!"

    jab "Tidak masuk akal!"

    show anon a_behind_head f_shy
    show thug a_hips
    with {'master': dissolve}
    anon "Ehh..."

    jab "Saya harus mengajukan petisi untuk memperbaiki keputusan ini..."

    jab "... Apakah kegilaan, menurutku."

    return


label jab_button_cargo.question3:
    jab f_normal "Anda sadar bahwa rumah yang Anda tinggali tidak masuk akal?"

    show anon f_confused
    show thug a_finger
    with {'master': dissolve}
    jab "Kamar tidak cocok dengan eksterior."

    show thug a_confused f_confused
    with {'master': dissolve}
    jab "... Apakah ini disengaja atau kelalaian?"

    anon f_worried_left "Ehh..."

    show anon f_worried
    show thug a_sides f_normal
    with {'master': dissolve}
    jab "Menurutku, ini membuat artis terlihat bodoh."

    return


label jab_button_cargo.question4:
    show thug a_scratch_head f_confused with {'master': dissolve}
    jab "Kenapa belum semua karakter hamil?"

    show anon a_facepalm f_worried_down
    show thug a_hips
    with {'master': dissolve}
    jab "Aku ingin punya bayi dengan semua orang tapi tidak."

    jab "... Kenapa kamu melakukan ini pada penggemar yang memujanya?"

    show anon a_sides f_worried with {'master': dissolve}
    anon "Ehh..."

    jab f_normal "Setidaknya tambahkan {b}Roxxy{/b}."

    jab f_smirk "Dia adalah waifu terbaik..."

    show thug a_boobs with {'master': dissolve}
    jab "...dengan payudara seperti torpedo!"

    return


label jab_button_cargo.question5:
    jab f_normal "Tahukah Anda bahwa beberapa latar belakang masih memerlukan pengambilan gambar eksterior?"

    show anon f_eyeroll
    jab "Mereka ada untuk banyak orang tetapi tidak semua."

    show anon f_tired
    jab f_confused "... Apakah ini disengaja atau kelalaian?"

    anon "Ehh..."

    show thug a_crossed with {'master': dissolve}
    jab "Pembuat kue ini menurutku pemalas."

    return


label jab_button_cargo.question6:
    jab f_normal "Mengapa {b}Kevin{/b} ada dalam daftar tugas Anda?"

    show anon f_confused
    jab f_confused "Apakah kamu gay, kawan?"

    show anon f_surprised
    jab f_normal "...Maksudku, tidak apa-apa jika kamu... Selama kamu mengerti, aku tidak menyukainya."

    anon f_confused "Ehh..."

    jab f_smirk "Penisku hanya seperti lubang pantat wanita."

    show anon f_worried_surprised
    pause
    return


label jab_button_cargo.question7:
    jab f_normal "Mengapa putri induk semang belum mencintaimu?"

    show anon f_surprised
    show thug a_hips f_angry
    with {'master': dissolve}
    jab "Menyebalkan!"

    jab "... Anda melakukan begitu banyak hal, dan memberinya banyak uang..."

    show anon a_shy_neck f_shy_left of_blush with {'master': dissolve}
    anon @ -m_talk "..."
    show thug a_confused with {'master': dissolve}
    jab "... Kenapa dia tidak bisa mengakui bahwa dia mencintaimu?!"

    jab "Tidak bisa diterima!"

    show anon a_sides f_worried -of_blush
    show thug a_hips
    with {'master': dissolve}
    jab "Saya sangat marah!"

    return


label jab_button_cargo.question8:
    jab f_confused "Ada apa dengan wanita tua di rumah sakit yang mendapatkan begitu banyak momen seksi?"

    show anon f_confused
    jab "Cookie punya fetish wanita tua?"

    show anon f_unimpressed
    jab "... Sementara itu, karakter yang lebih baik hanya memiliki satu!"

    show anon a_behind_head with {'master': dissolve}
    anon "Ehh..."

    jab f_normal "Tidak bisa diterima!"

    show anon a_sides f_flirt_grin
    show thug a_finger
    with {'master': dissolve}
    jab "Saya ingin meminta lebih banyak adegan dengan guru musik!"

    show thug a_sides f_smirk
    with {'master': dissolve}
    jab "Milkshake-nya membuat semua anak laki-laki Rusia datang ke halaman, ya?"

    return


label jab_button_cargo.question9:
    jab f_confused "Kenapa {b}Judith{/b} tidak mendapatkan waktu cinta yang lebih seksi?"

    show anon f_surprised
    jab "Ya, dia cantik dan kutu buku dengan kacamata kebesaran."

    jab f_smirk "... Tapi rapikan itu!"

    show anon a_behind_head f_shy of_blush with {'master': dissolve}
    anon "Ehh..."

    show thug a_boobs with {'master': dissolve}
    jab "Saya ingin menutupinya dengan krim kocok dan saus coklat..."

    show anon f_shy_left
    jab "... Dan kemudian mengikatnya di sekitar penisku!"

    show thug a_sides f_normal
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
