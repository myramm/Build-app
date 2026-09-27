label button_eve_talent_show_help:
    anon f_worried "Apakah Anda memainkan instrumen apa pun?"

    eve "Tidak, saya tidak memainkan alat musik apa pun. Saya selalu ingin belajar tetapi saya tidak punya waktu, Anda tahu?"

    anon "Oke, bagaimana kalau bernyanyi?"

    eve f_nervous_down "Oh, um..."

    eve @ f_nervous "Ya, aku suka menyanyi, kurasa... Tapi aku tidak tahu apakah aku pandai."

    anon f_normal "Saya yakin Anda memang demikian! Anda harus mendaftar untuk pertunjukan bakat bersama saya!"

    anon "Kami sangat membutuhkan lebih banyak sukarelawan."

    eve f_nervous "... Ya, entahlah."

    eve @ f_confused "Anda ingin saya bernyanyi di depan seluruh sekolah? Kedengarannya cukup memalukan..."

    eve "... Dan aku sudah lama tidak bernyanyi. Tidak sejak mesin karaokeku rusak."

    eve "Aku sudah kehabisan latihan."

    anon @ f_thinking a_thinking "Hmm..."

    anon "Anda tahu, saya pikir teman saya {b}Erik{/b} memiliki {b}mesin karaoke{/b} di ruang bawah tanahnya."

    eve "Oh ya?"

    anon @ f_laugh "Benar sekali!"

    anon "Anda harus datang kapan-kapan dan berlatih!"

    eve f_happy @ f_laugh "Heh, kamu ingin aku bernyanyi untukmu dan temanmu?"

    anon "Nah, kita semua bisa bernyanyi bersama! Ayo, kita akan melakukannya malam ini, pasti menyenangkan!"

    eve f_nervous_down @ -m_talk "..."
    eve f_happy @ f_eyeroll a_wtf "Baiklah, kurasa aku bisa mampir sebentar."

    anon "Luar biasa! {b}Sampai jumpa di rumah Erik malam ini{/b}."

    return

label button_eve_ross_find_art_pad:
    anon "Saya perlu meminta bantuan Anda."

    eve f_confused "Oh?"

    anon "Anda tahu, saya sedang membantu {b}Nona Ross{/b} dengan sesuatu, dan kami membutuhkan buku seni Anda."

    eve f_normal "Yah, itu tidak masalah."

    eve "Kamu hanya perlu {b}membantuku menemukan ranselku{/b} terlebih dahulu."

    anon f_worried "Anda kehilangan ransel Anda?"

    eve f_nervous_down "Ya..."

    eve f_normal "Buku seniku seharusnya ada di dalamnya."

    anon "Di manakah tempat terakhir yang Anda ingat memilikinya?"

    eve @ f_sad_thinking "Hmm..."

    eve "Yah, menurutku {b}Aku mengalaminya ketika aku pergi jalan-jalan dengan teman-teman di taman tadi malam{/b}."

    anon f_normal "Baiklah, aku ikut!"

    return

label button_eve_ross_find_eve_backpack_have_backpack:
    hide anon
    show player 610 at left
    with dissolve
    anon "Lihat apa yang saya temukan!"

    show player 609
    eve f_happy @ f_laugh "Bagus sekali!"

    hide player
    show anon
    with dissolve
    eve "Terima kasih, {b}[firstname]{/b}!"

    anon "Jangan khawatir. Tapi aku tidak bisa menemukan buku senimu."

    eve f_confused "Itu tidak ada di tasku?"

    anon "Tidak."

    eve f_normal "Aneh."

    eve @ f_confused "Saya ingin tahu apakah {b}Chad{/b} merebutnya lagi?"

    anon f_worried "{b}Anak{/b}?"

    eve "Ya, dia menyukai karya seniku."

    anon "Menarik..."

    anon f_normal "Aku akan bertanya padanya."

    eve "Dingin. Sampai jumpa, {b}[firstname]{/b}."

    anon "Sampai jumpa, {b}Malam{/b}."

    return

label button_eve_ross_find_eve_backpack_no_backpack:
    anon f_normal "Di mana kamu meninggalkan ranselmu lagi?"

    eve @ f_confused "Saya tidak sepenuhnya yakin. Saya ingat membawanya bersama saya {b}di taman{/b} tadi malam."

    anon "Oke, saya akan periksa di sana!"

    return

label button_eve_ross_get_eve_drawing:
    anon f_worried "Di mana tadi kamu bilang kalau art pad itu ada lagi?"

    eve @ f_eyeroll "Oh, {b}Chad mungkin memilikinya{/b}."

    eve "Dia menggali karya seni saya."

    anon f_normal "Oke, terima kasih!"

    return

label button_eve_ask_model:
    anon f_normal "Saya sedang mengerjakan proyek untuk {b}Miss Ross{/b} dan itu memerlukan model langsung."

    anon "Apakah Anda tertarik?"

    eve "Pemodelan? Itu mungkin menyenangkan."

    anon "Benar-benar?! Luar biasa! Saya berharap Anda akan mengatakan itu!"

    eve "Ya, saya tidak keberatan."

    eve @ f_laugh "Untung saja aku memakai pakaian lucu ini hari ini."

    anon f_worried "... Oh, um. Itu akan menjadi model telanjang."

    eve f_surprised a_rossed "Telanjang?!"

    eve "Oh, tidak!"

    show eve f_nervous_down
    anon "Jadi kamu tidak akan melakukannya? Saya pikir Anda menyukai hal-hal yang berseni?"

    eve f_surprised "Ya, tapi bukan berarti aku suka telanjang di depan umum!"

    show eve f_nervous
    anon "Poin bagus. Maaf."

    eve "Tidak apa-apa. Hanya tidak tertarik."

    anon f_normal @ a_wave "Yah, terima kasih..."

    return

label button_eve_ross_get_paint:
    anon f_normal "Saya sedang mencari cat. Adakah yang tahu di mana saya bisa menemukannya?"

    show eve f_confused a_idle
    eve "Entahlah, mungkin coba ke toko?"

    show eve f_normal
    anon "Ya, aku tahu... Ya kan?"

    anon "Tapi cat ini untuk {b}Nona Ross{/b}, dan dia tidak mampu membelinya."

    eve @ f_laugh "Oh, hehe."

    eve "Hmm, cat gratis. Itu sulit..."

    anon "Ceritakan padaku tentang hal itu..."

    eve @ a_point "Kita bisa mencoba bertanya pada adikku."

    if M_eve.finished_state(S_eve_visit_bedroom):
        anon "Menurutmu {b}Grace{/b} akan memberiku beberapa?"

        eve f_happy "Yah, dia mungkin tidak akan memberikannya begitu saja padamu..."

        eve "... Tapi aku yakin kalian berdua bisa menemukan solusinya."

        anon "Itu akan sangat membantu!"

        eve "Kita bisa bertanya padanya sepulang sekolah apakah kamu mau?"

        anon @ f_confused "Aku akan menemuimu di {b}Sugar Tats{/b} kalau begitu?"

        eve "Tentu, itu berhasil."

    else:
        anon "Dia seorang seniman tato, kan?"

        eve f_happy "Dia seniman tato terbaik!"

        eve "Anda harus melihat karyanya, sungguh luar biasa!"

        anon "Menurutmu dia akan mengizinkanku melukis?"

        eve "Kita bisa bertanya padanya."

        anon @ f_skeptical "Bukankah ruang tamunya bernama {b}Sugar Tats{/b}?"

        eve "Yuuuup. Letaknya {b}di sisi utara kota{/b}."

    anon "Baiklah, aku akan menemuimu di sana!"

    return

label button_eve_ross_get_paint_grace:
    anon @ f_worried "Di mana ruang tamu adikmu lagi?"

    eve f_happy "{b}Tat Gula{/b}? Letaknya di sisi kota {b}Utara{/b}."

    anon "Oke, {b}Sampai jumpa di sana{/b}!"

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
