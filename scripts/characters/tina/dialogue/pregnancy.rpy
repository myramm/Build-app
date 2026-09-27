label tina_pregnancy_notify:
    scene expression player.location.background
    "{i}*Brrrzzzt* *Brrrzzzt*{/i}"


    scene expression background(808, 400, 2.4, l=L_tina_lounge) as underlay:
        xoffset -400
    show tina a_phone:
        xoffset -500

    $ renpy.dynamic(stage=player.location.background_phone)
    show expression stage as stage
    show anon f_confused with dissolve:
        flip
    anon @ -m_talk "Hmm?"

    anon a_phone f_thinking_down "Saya tidak mengenali nomor ini..."

    show anon a_phone_talk f_skeptical with dissolve:
        unflip
        xoffset 500
    show expression stage as stage at phoneleft with phoneleft.show
    anon "Halo?"

    tina "Halo, {b}[firstname]{/b}?"

    anon "Siapa ini?"

    tina "Itu {b}Tina{/b}."

    anon f_surprised "!!!"
    anon f_worried "{b}Ny. Hendiks{/b}?!"

    tina @ -m_talk "Mhmm."

    tina "Saya menanyakan nomor telepon Anda kepada {b}Tony{/b}... Saya harap Anda tidak keberatan?"

    anon f_shy "T-tidak, tidak sama sekali!"

    pause
    anon "Apakah Anda perlu-"

    anon "{i}*Ahem*{/i} Maksudku, adakah yang bisa kulakukan untukmu?"

    tina f_sexy "Yah, saya tidak akan mengatakan tidak jika ada yang terjatuh lagi, tapi sayangnya, itu bukan alasan saya menelepon..."

    anon "Oh?"

    tina f_normal "Saya hamil, {b}[firstname]{/b}."

    anon f_surprised "Oh!"

    pause
    anon "Hmm..."

    tina "Ya."

    tina "Saya ingin Anda tahu bahwa saya tidak merencanakan hal ini terjadi."

    tina @ f_laugh "Faktanya, hal itu seharusnya tidak mungkin terjadi sama sekali!"

    anon f_worried "Apa maksudmu?"

    tina "Ya, saya sudah memakai implan kontrasepsi selama bertahun-tahun dan belum pernah ada yang berhasil sebelumnya..."

    anon "Benar-benar?"

    tina "Entah ada yang tidak beres atau sperma Anda ajaib!"

    anon @ -m_talk "..."
    tina "Apapun itu, saya menganggapnya sebagai tanda dan menjaga bayi itu."

    anon f_normal "O-oke."

    tina "Menurutku akan menyenangkan jika ada si kecil lagi."

    tina "Dan sepenuhnya terserah Anda seberapa terlibatnya Anda, oke?"

    tina "Tidak ada tekanan."

    anon "Saya pasti ingin terlibat."

    tina "Anda melakukannya?"

    anon "Jika tidak apa-apa?"

    tina @ f_laugh "Tentu saja, {b}[firstname]{/b}!"

    tina "Saya pikir itu akan luar biasa!"

    tina "Silakan datang kapan pun Anda mau, oke?"

    anon "Ya baiklah."

    tina "Sampai berjumpa lagi."

    anon "Sampai jumpa, {b}Tina{/b}."

    show anon f_looking_down a_phone with dissolve
    show expression stage as stage with {'master': phoneleft.hide}
    "{i}*Bip*{/i}"

    anon @ -m_talk "(Yah, itu tidak terduga...)"

    anon a_idle f_grin @ -m_talk "( Saya tidak percaya saya akan punya bayi dengan {b}Nyonya Hendicks{/b}! )"

    anon @ -m_talk "(Ini sangat menarik!)"

    hide anon with dissolve
    return True


label tina_pregnancy_notify.repeat:
    scene expression player.location.background
    "{i}*Brrrzzzt* *Brrrzzzt*{/i}"


    scene expression background(808, 400, 2.4, l=L_tina_lounge) as underlay:
        xoffset -400
    show tina a_phone:
        xoffset -500

    $ renpy.dynamic(stage=player.location.background_phone)
    show expression stage as stage
    show anon f_confused with dissolve:
        flip
    anon @ -m_talk "Hmm?"

    anon a_phone f_worried_low "Itu {b}Tina{/b}."

    show anon a_phone_talk f_normal with dissolve:
        unflip
        xoffset 500
    show expression stage as stage at phoneleft with phoneleft.show
    anon "Halo?"

    tina "Halo, {b}[firstname]{/b}?"

    anon "Ya, ini aku."

    anon "Ada yang salah?"

    tina @ f_laugh "Yah, itu resmi!"

    anon f_confused @ -m_talk "Hmm?"

    tina f_sexy "Kamu pasti punya sperma ajaib karena aku hamil lagi!"

    anon f_surprised "!!!"
    anon "Lagi?"

    tina "Sebaiknya saya melepas implan kontrasepsi ini demi kebaikan saya."

    anon f_worried "Atau kita harus berhenti berhubungan seks..."

    tina "Oh, sekarang jangan mulai tergila-gila padaku!"

    anon f_normal @ -m_talk "..."
    anon "Saya berasumsi Anda menyimpannya?"

    tina "Tentu saja."

    tina "Semakin banyak semakin meriah sejauh yang saya ketahui."

    tina "Seperti biasa, Anda tidak perlu-"

    anon "Saya ingin terlibat!"

    tina "Oh."

    pause
    tina @ f_laugh "Bagus sekali {b}[firstname]{/b}, terima kasih!"

    anon @ -m_talk "Mhmm."

    anon "Aku akan ke sana untuk menemuimu secepatnya."

    tina "Baiklah."

    tina "Sampai berjumpa lagi."

    show anon f_looking_down a_phone with dissolve
    show expression stage as stage with {'master': phoneleft.hide}
    "{i}*Bip*{/i}"

    anon @ -m_talk "(Sperma ajaib, ya?)"

    pause
    anon a_idle f_grin @ -m_talk "(Tidak, saya yakin itu hanya implan yang rusak...)"

    anon @ -m_talk "(Sihir bukanlah suatu hal!)"

    hide anon with dissolve
    return True


label tina_pregnant_labor_1:
    scene expression player.location.background_blur
    show anon f_normal with dissolve
    anon "Sepertinya aku mendapat pesan teks."

    hide anon with dissolve
    return


label tina_pregnant_labor_2:
    scene expression player.location.background_blur
    if player.location != L_map:
        show anon f_surprised a_phone with dissolve
    anon "{b}Tina{/b} punya bayi?!"

    anon "Sialan!"

    pause
    anon "Sebaiknya saya {b}pergi ke rumah sakit{/b} untuk memeriksanya."

    if player.location != L_map:
        hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
