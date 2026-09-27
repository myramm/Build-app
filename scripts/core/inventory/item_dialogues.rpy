label generic_item_closeup(item):
    scene location_backpack_closeup
    show expression item.closeup
    pause
    return

label obituary_records(item):
    scene location_backpack_closeup
    show expression item.closeup at Position(xalign = 0.5, yalign = 1.0)
    with None
    player_name "Hmm..."

    player_name "Sepertinya satu-satunya nama di bawah pembuat kapal adalah..."

    player_name "...Ben Dover?"

    player_name "Sekarang saya hanya perlu {b}mengunjungi kuburan dan menemukan batu nisan yang tepat{/b}."

    $ M_aqua.trigger(T_aqua_obituary_records)
    return

label keycode_note_closeup(item):
    scene location_backpack_closeup
    show expression item.closeup at Position(xalign = 0.5, yalign = 1.0)
    with None
    player_name "Ini adalah {b}kode ke kantor Nona Okita{/b}. {b}6219{/b}."

    return


label scroll(item):
    scene location_backpack_closeup
    show expression item.closeup at Position(xalign = 0.5, yalign = 1.0)
    with None
    player_name "Hmm..."

    player_name "Ada gambar aneh di sana."

    player_name "Sepertinya bulan sabit..."

    player_name "Pasti {b}berguna untuk sesuatu{/b}..."

    return

label treasure_map(item):
    scene location_backpack_closeup
    show expression item.closeup at Position(xalign = 0.5, yalign = 1.0)
    with None
    player_name "Ini terlalu keren!"

    player_name "Peta harta karun yang sebenarnya!"

    player_name "Hmm."

    player_name "Ini terlihat seperti gambar pantai..."

    player_name "... Dan itu terlihat seperti pantai lokal kita?"

    player_name "Oh, dan di sini, {b}ada tanda X di pulau kecil{/b}."

    player_name "Saya ingin tahu apa tujuannya?"

    $ M_aqua.trigger(T_aqua_obituary_records)
    return

label weird_coin(item):
    scene location_backpack_closeup
    show expression item.closeup at Position(xalign = 0.5, yalign = 1.0)
    with None
    player_name "Hah?"

    player_name "Itu terlihat seperti koin yang sangat tua."

    player_name "Lihat saja {b}simbol ganjil{/b} ini!"

    player_name "Saya harus menyimpannya. Mungkin itu sesuatu yang berharga?"

    return

label old_book(item):
    scene location_backpack_closeup
    show expression item.closeup at Position(xalign = 0.5, yalign = 1.0)
    with None
    player_name "Buku ini sepertinya akan berguna untuk memecahkan kode sesuatu."

    player_name "..."
    if not player.has_item("weird_coin"):
        player_name "Hehe. Mungkin harta karun bajak laut tersembunyi yang dibuang sembarangan oleh seseorang."

        player_name "Tapi itu hanya angan-angan saja."

    else:
        player_name "Menurutku {b}koin bajak laut itu memiliki empat digit angka{/b}."

        player_name "Saya harus {b}melihatnya lagi{/b}."

    return

label golden_compass(item):
    scene location_backpack_closeup
    show expression item.closeup at Position(xalign = 0.5, yalign = 1.0)
    with None
    player_name "Wah!!"

    player_name "Saya tidak percaya! Saya menemukan harta karun itu!"

    player_name "Ini pasti kompas yang {b}Kapten Terry{/b} bicarakan."

    return

label tigger(item):
    scene location_backpack_closeup
    show expression item.closeup at Position(xalign = 0.5, yalign = 1.0)
    with None
    player_name "Wah, bajingan jahat ini melakukan perlawanan yang cukup keras."

    player_name "... Dan lihat saja gigi itu!"

    player_name "Tidak heran mengapa {b}Kapten Terry{/b} menginginkan dia mati."

    player_name "Saya tidak sabar untuk menunjukkannya padanya!"

    return


label cumdoom_pills(item):
    scene expression player.location.background_blur
    if player.pregnancy_chance == 0:
        show player 705b with dissolve
        player_name "(Hmm, petunjuknya mengatakan saya perlu {b}minum satu pil, secara oral, sebelum melakukan aktivitas seksual{/b}. )"

        player_name "( {b}Efek akan bertahan selama 24 jam{/b}. )"

        player_name "(Ada juga label peringatan: \"Jangan gunakan obat ini jika pasangan Anda sedang menstruasi atau telah mengalami menopause.\" )"

        player_name "(Saya sudah meminum satu dosis hari ini.)"

        player_name "(Saya pastinya tidak boleh mengambil yang lain.)"

        hide player with dissolve
    else:
        show player 705b with dissolve
        player_name "(Hmm, petunjuknya mengatakan saya perlu {b}minum satu pil, secara oral, sebelum melakukan aktivitas seksual{/b}. )"

        player_name "( {b}Efeknya akan bertahan sampai saya meminum pil Pregnax{/b}. )"

        player_name "(Ada juga label peringatan: \"Jangan gunakan obat ini jika pasangan Anda sedang menstruasi atau telah mengalami menopause.\" )"

        player_name "(Haruskah saya minum pil {b}Cumdoom{/b}? )"

        menu:
            "Ya.":
                show player 706b with dissolve
                player_name "(Yah, tidak ada apa-apa...)"

                show player 707b with dissolve
                pause
                $ player.pregnancy_chance = 0.0
                hide player with dissolve
            "Tidak.":
                show player 705b
                player_name "Nah, menurutku sekarang bukan waktu terbaik untuk mengambil salah satu dari ini."

                hide player with dissolve
    return

label pregnax_pills(item):
    scene expression player.location.background_blur
    if player.pregnancy_chance >= 40:
        show player 705 with dissolve
        player_name "(Hmm, petunjuknya mengatakan saya perlu {b}minum satu pil, secara oral, sebelum melakukan aktivitas seksual{/b}. )"

        player_name "( {b}Efek akan bertahan selama 24 jam{/b}. )"

        player_name "(Ada juga label peringatan: \"Jangan gunakan obat ini jika pasangan Anda sedang menstruasi atau telah mengalami menopause.\" )"

        player_name "(Saya sudah meminum satu dosis hari ini.)"

        player_name "(Saya pastinya tidak boleh mengambil yang lain.)"

        hide player with dissolve
    else:
        show player 705 with dissolve
        player_name "(Hmm, petunjuknya mengatakan saya perlu {b}minum satu pil, secara oral, sebelum melakukan aktivitas seksual{/b}. )"

        player_name "( {b}Efeknya akan bertahan sampai saya meminum pil Cumdoom{/b}. )"

        player_name "(Ada juga label peringatan: \"Jangan gunakan obat ini jika pasangan Anda sedang menstruasi atau telah mengalami menopause.\" )"

        player_name "(Haruskah saya minum pil Pregnax?)"

        menu:
            "Ya.":
                show player 706 with dissolve
                player_name "(Yah, tidak ada apa-apa...)"

                show player 707 with dissolve
                pause
                $ player.pregnancy_chance += 0.5
                hide player with dissolve
            "Tidak.":
                show player 705
                player_name "Nah, menurutku sekarang bukan waktu terbaik untuk mengambil salah satu dari ini."

                hide player with dissolve
    return

label condom:
    scene expression game.timer.image("jennybedroom{}")
    show expression "objects/closeup_condom.png" with dissolve
    player_name "Kondom?!"

    player_name "{b}[jen_name]{/b} pasti menyembunyikannya di kamarnya."

    player_name "Dia mungkin tidak akan menyadarinya jika aku hanya mengambil satu..."

    hide expression "objects/closeup_condom.png" with dissolve
    call popup ('give', 'condom')
    $ game.main()

label mysterious_statue_1(item):
    scene expression player.location.background_blur
    show player 688
    with dissolve
    player_name "(Hmm, sepertinya bagian bawah wanita telanjang.)"

    player_name "(Tapi ada apa dengan ekornya?)"

    show player 689
    player_name "(Ada sesuatu yang tertulis di bawahnya.)"

    show expression item.closeup
    hide player
    player_name "{b}\"Delmont.\"{/b}"

    player_name "Hmm, {b}Delmont{/b}..."

    player_name "Kedengarannya familiar."

    hide expression item.closeup
    return

label attic_key:
    scene expression player.location.background_blur
    show expression "objects/closeup_key.png" with dissolve
    player_name "(Saya belum pernah melihat kunci ini sebelumnya.)"

    player_name "(Ini agak kecil...)"

    hide expression "objects/closeup_key.png" with dissolve
    $ player.get_item("attic_key")
    call popup ('give', 'attic_key')
    jump entrance_dialogue

label ring:
    scene expression game.timer.image("attic{}")
    show expression "objects/closeup_ring.png" with dissolve
    player_name "(Itu terlihat seperti cincin yang mahal!)"

    player_name "(Apa yang dilakukannya di atas sana?)"

    hide expression "objects/closeup_ring.png" with dissolve
    call popup ('give', 'ring')
    jump attic_dialogue

label cheerleader_outfit:
    scene expression game.timer.image("attic{}")
    if M_jenny.is_state(S_jenny_get_cheerleader_outfit):
        show anon with dissolve
        anon @ -m_talk "( Hmm, saya tidak melihat debu atau sarang laba-laba... )"

        anon @ -m_talk "(Saya harus membawa ini ke kamar {b}[jen_name] pada sore hari{/b}. )"

        hide anon with dissolve
        $ player.get_item("cheerleader_outfit")
        call popup ('give', 'cheerleader_outfit')
        $ M_jenny.trigger(T_jenny_got_cheerleader_outfit)
    else:
        show anon with dissolve
        anon @ -m_talk "( Ini adalah pakaian pemandu sorak {b}[jen_name] dari kampus. )"

        anon @ -m_talk "(Aku ingin tahu apa yang dilakukannya di sini?)"

        hide anon with dissolve
    jump attic_dialogue

label fishing_rod:
    scene expression game.timer.image("attic{}")
    show expression "objects/closeup_rod.png" with dissolve
    player_name "Itu pancing tua {b}Ayah{/b}!"

    player_name "(Saya ingat ketika kami biasa pergi memancing di dermaga, ketika saya masih kecil.)"

    player_name "{i}*Huh*{/i}"

    player_name "Aku rindu {b}Ayah{/b}..."

    hide expression "objects/closeup_rod.png" with dissolve
    call popup ('give', 'fishing_rod')
    if L_pier.locked:
        $ L_pier.unlock()
    jump attic_dialogue

label backpack_pickup_dialogue:
    scene location_park_day_blur
    show player 608
    with dissolve
    pause
    show player 608b
    player_name "Ini jelas merupakan tas punggung {b}Eve{/b}."

    player_name "Hmm, aku tidak melihatnya {b}art pad{/b} miliknya."

    show player 610 with dissolve
    player_name "Saya harus {b}menanyakannya ketika saya mengembalikan ini{/b}."

    hide player with dissolve
    $ player.get_item("eve_backpack")
    call popup ('give', 'eve_backpack')
    jump park_dialogue

label roxxy_homework_pickup_dialogue:
    scene mc_locker
    player_name "Ini dia!"

    player_name "Sekarang saya hanya perlu {b}membawa ini ke Roxxy{/b}."

    $ player.get_item("roxxy_homework")
    call popup ('give', 'roxxy_homework')
    $ player.go_to(L_school_hall)
    $ game.main()

label poem(item):
    scene location_backpack_closeup
    show expression item.closeup at truecenter
    anon "( \"I slip slowly under the satin sheets.\" )" (show_native="( {i}\"Je me glisse lentement sous les draps de satin.\"{/i} )")
    anon "( \"You are lying on your stomach, your back welcomes my hand.\" )" (show_native="( {i}\"Tu es allong? sur le ventre, ton dos accueil ma main.\"{/i} )")
    anon "( \"Slowly your naked body you expose.\" )" (show_native="( {i}\"Tout doucement ton corps nu tu exposes.\"{/i} )")
    anon "( \"On your breasts my mouth rests.\" )" (show_native="( {i}\"Sur tes seins ma bouche se pose.\"{/i} )")
    pause
    anon "( Saya perlu menyerahkan ini kepada {b}Ms. Bissette{/b} dan berharap tidak ada orang lain yang membaca ini! )"

    return

label french_scans(item):
    scene location_backpack_closeup
    show expression item.closeup at truecenter
    anon "( Kata yang aneh... Aku penasaran apa maksudnya. Sebaiknya aku lihat {b}Ms. Bissette{/b}. )"

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
