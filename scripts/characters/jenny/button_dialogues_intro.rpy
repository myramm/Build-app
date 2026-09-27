label jenny_button_intro_bedroom_evening_j8:
    scene expression player.location.background_closeup with None
    show anon f_worried
    show jenny f_upset a_crossed
    with dissolve
    jenny "Apa yang kamu lakukan?!"

    anon "Hmm?"

    anon "T-tidak ada... aku hanya-"

    jenny "Keluarlah dari kamarku, dasar mesum!"

    anon f_skeptical "Kenapa suasana hatimu selalu buruk?"

    show jenny f_angry
    jenny "GET OUT OF MY ROOM, {b}[firstname!u]{/b}!!!" with hpunch
    show anon f_surprised a_rub with dissolve
    anon "Oke, oke... aku berangkat."

    hide anon with dissolve
    return

label jenny_button_intro_bedroom_evening_j16:
    scene expression player.location.background_closeup with None
    show anon f_worried
    show jenny f_upset
    with dissolve
    jenny "Ya Tuhan, apa yang kamu inginkan sekarang?!"

    anon "T-tidak ada... aku hanya-"

    jenny "Anda sebaiknya punya alasan bagus untuk mengganggu saya!"

    show anon f_surprised_teeth a_behind_head with dissolve
    anon @ -m_talk "..."
    show anon a_idle
    return

label jenny_button_intro_bedroom_evening_j20:
    scene expression player.location.background_closeup with None
    show anon f_normal a_wave
    show jenny f_upset
    with dissolve
    anon "Hai."

    show anon a_idle
    jenny "Hai."

    show anon f_worried
    pause
    anon "Jadi, uhh..."

    anon "A-ada apa?"

    jenny @ f_eyeroll "Ya Tuhan..."

    jenny "Berhentilah bertingkah aneh dan langsung ke intinya."

    anon f_tired @ -m_talk "..."
    return

label jenny_button_intro_bedroom_evening_j21:
    scene expression player.location.background_closeup with None
    show anon f_normal
    show jenny
    with dissolve
    anon "Hai."

    jenny "Hai."

    pause
    anon "Kamu sibuk?"

    jenny "Tidak juga, saya hanya menunggu {b}Jane{/b} menelepon."

    anon "Oh, ehh... Keren."

    jenny @ f_eyeroll "..."
    jenny "Apa yang kamu inginkan, {b}[firstname]{/b}?"

    return

label jenny_button_intro_backyard_j21:
    scene expression player.location.background_closeup with None
    show anon f_worried
    show jenny f_upset b_swimsuit a_hips
    anon "Hai, {b}[jen_name]{/b}."

    jenny "Hai."

    pause
    anon f_confused "Kamu uhh... Mau aku mengoleskan tabir surya padamu atau apalah?"

    show anon f_worried
    show jenny f_laugh
    jenny "Pfft, kamu mau!"

    show jenny f_grin
    pause
    jenny "Telanjanglah dan aku akan memikirkannya."

    anon "Apa?!"

    jenny "Ayo, keluarkan."

    anon f_skeptical "Mustahil!"

    anon "{b}[deb_name]{/b} ada di sana, di dapur!"

    show jenny f_laugh
    jenny "Hahahaah!"

    show jenny f_grin
    jenny "Akan sangat lucu jika dia keluar dari sini dan kamu telanjang!"

    anon f_worried "Tidak, itu tidak akan..."

    anon "Dia akan panik!"

    jenny "Aku tahu!"

    show jenny f_laugh
    jenny "Hahahaah!"

    show jenny f_grin
    return

label jenny_button_intro_bedroom_j21:
    scene expression player.location.background_closeup with None
    show anon f_worried
    show jenny f_upset
    anon "Hai."

    jenny "Hai."

    pause
    jenny "Anda siap untuk melakukan pertunjukan?"

    jenny "Lepaskan pakaian itu!"

    anon f_confused "Ehh..."

    jenny "Ayo {b}[firstname]{/b}, penggemarku sudah menunggu!"

    return

label jenny_button_intro_diningroom_j21:
    scene expression game.timer.image("dining_room{}")
    show jenny b_breakfast_dressed a_phone f_upset_down zorder 1
    show anon b_dinner_sitting_look_left f_normal zorder 0
    show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
    with dissolve
    anon "Pagi."

    show jenny a_spoon f_normal with dissolve
    jenny "Pagi."

    pause
    anon "Kamu terlihat cantik hari ini."

    jenny @ f_eyeroll "Hehe, ya."

    show anon f_looking_down_eating a_eating with dissolve
    pause
    show anon f_looking_down_food a_resting with dissolve
    jenny "Kamu datang ke kamarku nanti?"

    anon f_surprised_food "Entahlah, mungkin?"

    show anon f_surprised_food
    jenny "Anda sebaiknya."

    jenny "Banyak uang yang bisa dihasilkan."

    anon f_normal "Ya, saya tahu."

    return

label jenny_button_intro_bedroom_j20:
    scene expression player.location.background_closeup with None
    show anon f_worried
    show jenny f_upset
    anon "Hai."

    jenny "Hai."

    show jenny f_gross
    pause
    anon "Jadi, uhh..."

    anon "A-ada apa?"

    show jenny f_eyeroll
    jenny "Ya Tuhan..."

    show jenny f_upset
    jenny "Berhentilah bertingkah aneh dan langsung ke intinya."

    anon f_skeptical @ -m_talk "..."
    return

label jenny_button_intro_backyard_j20:
    scene expression player.location.background_closeup with None
    show anon f_worried
    show jenny f_upset b_swimsuit a_hips
    anon "Pagi."

    show jenny f_normal
    jenny "Pagi."

    pause
    anon f_normal "Pasti menyenangkan di sini hari ini..."

    show jenny f_eyeroll
    jenny "Ya."

    show jenny f_gross
    pause
    anon @ -m_talk "..."
    show jenny f_upset
    jenny "Sudahlah!"

    jenny "Saya mencoba bersantai di sini."

    anon f_worried @ -m_talk "..."
    return

label jenny_button_intro_diningroom_j20:
    scene expression game.timer.image("dining_room{}")
    show jenny b_breakfast_dressed a_phone f_upset_down zorder 1
    show anon b_dinner_sitting_look_left f_worried zorder 0
    show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
    with dissolve
    anon "Pagi."

    jenny "Pagi."

    pause
    anon "Anda melihat bagian komentar Anda lagi?"

    jenny "Ya, orang-orang ini benar-benar gila!"

    jenny "Anda harus membaca beberapa hal yang mereka minta saya lakukan..."

    anon "Tapi itu uang yang bagus, bukan?"

    jenny "Ya, ya!"

    show jenny f_upset
    jenny "Apakah kamu menginginkan sesuatu?"

    return

label jenny_button_intro_bedroom_j16:
    scene expression player.location.background_closeup with None
    show jenny f_eyeroll
    show anon f_worried
    jenny "Ya Tuhan, apa yang kamu inginkan sekarang?!"

    show jenny f_upset
    anon "T-tidak ada... aku hanya-"

    jenny "Anda sebaiknya punya alasan bagus untuk mengganggu saya!"

    anon @ -m_talk "..."
    return

label jenny_button_intro_backyard_j16:
    scene expression player.location.background_closeup with None
    show jenny f_upset b_swimsuit a_hips
    show anon f_worried
    anon "H-hei."

    jenny @ -m_talk "..."
    pause
    anon "Aku suka pakaian renangmu-"

    show anon f_surprised
    jenny "Apa yang kamu inginkan?!"

    anon f_worried "aku tidak-"

    show anon f_confused
    jenny "Ludahkan atau kesal!"

    jenny "Saya mencoba bersantai di sini."

    anon @ -m_talk "..."
    return

label jenny_button_intro_diningroom_j16:
    scene expression game.timer.image("dining_room{}")
    show jenny b_breakfast_dressed a_phone f_upset_down zorder 1
    show anon b_dinner_sitting_look_left f_worried zorder 0
    show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
    with dissolve
    anon "Pagi."

    jenny "Ya, ya..."

    pause
    anon "Apa yang sedang kamu lakukan?"

    jenny "Ugh, bajingan sialan ini..."

    anon "Hah?!"

    jenny "Tidak ada... Sudahlah!"

    show jenny f_upset
    jenny "Apa yang kamu inginkan, {b}[firstname]{/b}?!"

    return

label jenny_button_intro_bedroom_j8:
    scene expression player.location.background_closeup with None
    show jenny f_upset a_crossed
    show anon f_worried
    jenny "Apa yang kamu lakukan?!"

    anon "Hmm?"

    anon "T-tidak ada... aku hanya-"

    show jenny f_angry
    jenny "Keluarlah dari kamarku, dasar mesum!"

    anon f_skeptical "Kenapa suasana hatimu selalu buruk?"

    show anon f_surprised
    jenny "GET OUT OF MY ROOM, {b}[firstname!u]{/b}!!!" with hpunch
    anon f_worried "Oke, oke... aku berangkat."

    hide anon with dissolve
    return

label jenny_button_intro_backyard_j8:
    scene expression player.location.background_closeup with None
    show jenny f_upset b_swimsuit a_hips
    show anon f_worried
    anon "H-hei."

    jenny @ -m_talk "..."
    pause
    anon "Aku suka pakaian renangmu-"

    show anon f_surprised
    jenny "Pergilah."

    anon @ -m_talk "..."
    anon f_confused "Aku hanya mencoba memberimu persetujuan."

    jenny "Aku bilang, pergilah, pecundang!"

    jenny "Saya mencoba bersantai di sini."

    anon "Cih, baiklah."

    hide anon with dissolve
    return

label jenny_button_intro_diningroom_j8:
    scene expression game.timer.image("dining_room{}")
    show jenny b_breakfast_dressed a_phone f_upset_down zorder 1
    show anon b_dinner_sitting_look_left f_worried zorder 0
    show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
    with dissolve
    anon "Pagi."

    jenny @ -m_talk "..."
    pause
    anon "Aku berkata, selamat pagi-"

    jenny "aku mendengarmu."

    jenny "Diam saja dan tinggalkan aku sendiri, pecundang..."

    anon f_tired "Cih, baiklah."

    show anon f_looking_down_eating a_eating with dissolve
    pause
    show anon f_looking_down_food a_resting with dissolve
    pause
    scene black with fade
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
