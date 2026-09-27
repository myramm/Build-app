label nadya_button_pregnant:
    if L_warehouse_depot.is_here(M_nadya):
        jump nadya_button_pregnant_depot
    jump nadya_button_pregnant_office


label nadya_button_pregnant_depot:
    pause .1
    show nadya f_surprised
    show svetlana f_surprised
    "{i}*Pekerja mengobrol*{/i}"

    show svetlana a_crossed
    show nadya a_angry f_angry:
        xoffset 675
        xzoom -1
    with {'master': dissolve}
    nadya "Hei, berhentilah berkeliaran!"

    show svetlana:
        xoffset 450
    with {'master': dissolve}
    nadya "Kembali bekerja, kalian semua!"

    show anon f_worried behind nadya with dissolve:
        xoffset -100
    nadya "Apa, menurutmu karena aku hamil aku tidak akan mencontohmu?!"

    show anon f_worried_surprised
    nadya "Aku memasukkanmu ke dalam karung kentang dan mengirimmu kembali ke Rusia!"

    show anon f_worried
    anon "Ehh, {b}Nadya{/b}?"

    show anon a_surprised_up_both f_worried_surprised
    show nadya a_hips f_frowning:
        xoffset 100
        xzoom 1
    show svetlana a_sides f_curious:
        xoffset -100
        xzoom 1
    with {'master': dissolve}
    nadya "Apa?!"

    show svetlana f_happy
    nadya f_normal "Oh."

    show anon a_sides f_worried
    with {'master': dissolve}
    nadya "Sorry, {b}[firstname]{/b}." (show_native="Izvinite, {b}[firstname]{/b}.")
    nadya "Hormon-hormon menjadi gila dalam diriku..."

    show anon a_surprised f_shy_cringe
    show nadya f_angry:
        xoffset 675
        xzoom -1
    show svetlana f_concerned_back
    with {'master': dissolve}
    nadya "... Dan tenaga kerja idiotku sedang menguji keberanian terakhirku!"

    show anon a_sides f_worried with {'master': dissolve}
    anon f_worried "Y-ya, aku bisa melihatnya."

    show nadya f_frowning:
        xoffset 100
        xzoom 1
    show svetlana f_normal
    with dissolve
    pause

    menu nadya_button_pregnant_depot.choice:
        "Bagaimana kabar bayinya?" if 1 == M_nadya.pregnancy.stage:
            jump nadya_button_pregnant_depot.sick

        "Bagaimana kabar bayinya?" if 2 == M_nadya.pregnancy.stage:
            jump nadya_button_pregnant_depot.predict

        "Bagaimana kabar bayinya?" if 3 <= M_nadya.pregnancy.stage:
            jump nadya_button_pregnant_depot.soon
        "Bukankah kamu seharusnya menjauh?":

            jump nadya_button_pregnant_depot.work
        "Aku serahkan padamu.":

            pass

    anon f_shy "Berhati-hatilah, oke?"

    nadya f_normal "Bah, kamu terlalu khawatir."

    nadya "Saya baik-baik saja."

    show svetlana a_hips f_concerned:
        xoffset 450
        xzoom -1
    with {'master': dissolve}
    svetlana "Ah, apa yang mereka lakukan?"

    show anon f_confused
    show nadya f_confused:
        xoffset 675
        xzoom -1
    with {'master': dissolve}
    nadya @ -m_talk "Hmm?"

    show anon f_surprised_teeth
    show nadya a_angry f_angry
    with {'master': dissolve}
    nadya "Hei, itu untuk pelanggan VIP!"

    show anon f_surprised
    nadya "Taruh di tumpukan pengiriman semalaman, dasar bodoh!"

    show anon a_facepalm f_eyeroll with {'master': dissolve}
    svetlana "Anda seharusnya membayar ekstra untuk pekerja yang melek huruf..."

    hide anon with dissolve
    return


label nadya_button_pregnant_depot.predict:
    show anon f_normal

    if M_nadya.pregnancy.baby_gender == 'girl':
        anon "Bagaimana kabar bayinya{#girl}?"

        show nadya a_idle f_sexy_down with {'master': dissolve}
        nadya "Dia mulai menendang."

        anon f_confused "Dia?"

        nadya f_happy "Da, itu perempuan."

        anon "Anda tahu?"

        show svetlana a_hips f_happy with {'master': dissolve}
        svetlana "{b}Nona Chernyshevsky{/b} mendambakan makanan manis."

        svetlana "Artinya bayinya perempuan."

    else:

        anon "Bagaimana kabar bayinya{#boy}?"

        show nadya a_idle f_sexy_down with {'master': dissolve}
        nadya "Dia mulai menendang."

        anon f_confused "Dia?"

        nadya f_happy "Ya, laki-laki."

        anon f_confused "Anda tahu?"

        show svetlana a_crossed f_normal with {'master': dissolve}
        svetlana "{b}Nona Chernyshevsky{/b} mendambakan makanan yang gurih."

        svetlana "Artinya bayinya laki-laki."


    anon f_skeptical "Apa?"

    anon "Kedengarannya seperti cerita istri tua yang tidak masuk akal bagi saya..."

    show nadya a_hips f_angry
    show svetlana a_sides f_annoyed
    with {'master': dissolve}
    svetlana "Hal ini diketahui."

    show anon f_worried
    nadya "Ya, sudah diketahui."

    show anon a_hands_up f_worried_surprised with {'master': dissolve}
    anon "Oke, oke... sudah diketahui."

    show nadya f_normal
    show svetlana f_normal
    show anon a_sides f_tired
    with {'master': dissolve}
    anon "Astaga."

    jump nadya_button_pregnant_depot.choice


label nadya_button_pregnant_depot.sick:
    anon f_normal "Bagaimana kabar bayinya?"

    nadya f_normal "Belum sayang."

    show svetlana f_concerned_back
    nadya f_annoyed_down "Lebih mirip kacang, dengan kebencian yang tidak masuk akal terhadap sarapan."

    anon f_worried "Anda merasa mual di pagi hari?"

    nadya f_frowning "Ya."

    show svetlana f_concerned
    nadya f_normal "{b}Svetlana{/b} berkata, itu normal saja."

    show svetlana a_hips f_normal with {'master': dissolve}
    svetlana @ -m_talk "Mhmm."

    svetlana "Bayi selalu sakit-sakitan di awal kehamilan."

    svetlana "Ini pada akhirnya akan berhenti."

    anon f_shy "Itu kabar baik."

    show svetlana a_sides with dissolve
    jump nadya_button_pregnant_depot.choice


label nadya_button_pregnant_depot.soon:
    anon f_normal "Bagaimana kabar bayinya?"

    show anon f_worried
    show svetlana f_concerned_back
    show nadya f_annoyed_down

    if M_nadya.pregnancy.baby_gender == 'girl':
        nadya "Dia dengan keras kepala menolak untuk meninggalkan rahim..."

    else:
        nadya "Dia dengan keras kepala menolak untuk meninggalkan rahim..."


    nadya "... Menyebalkan!"

    show nadya f_frowning
    show svetlana f_concerned:
        xoffset 450
        xzoom -1
    with {'master': dissolve}
    svetlana "Sudah kubilang, orgasme membuat bayi lahir lebih cepat."

    show anon f_surprised
    nadya @ f_eyeroll "Dan aku beritahu kamu..."

    show anon a_surprised_up m_talk
    with {'master': dissolve}
    nadya "... {b}Katya{/b} membuatku enam kali orgasme kemarin dan masih belum punya bayi!"

    show anon a_surprised_up_both f_surprised_teeth -m_talk
    with {'master': dissolve}
    nadya "Klitoris saya bengkak seperti binatang balon!"

    svetlana @ f_curious "Yah, itu selalu berhasil untukku..."

    show anon a_sides f_surprised
    with {'master': dissolve}
    nadya f_bored_down @ f_bored "{i}*Huh*{/i} Berhenti bicara."

    svetlana f_timid "Ya, {b}Nona Chernyshevsky{/b}."

    show svetlana:
        xoffset -100
        xzoom 1
    with {'master': dissolve}
    anon "Wah, baiklah kalau begitu."

    pause
    anon f_shy "Apakah ada yang bisa saya lakukan?"

    nadya f_bored "No." (show_native="Nyet.")
    show anon f_worried
    nadya f_worried "Saya hanya akan menyibukkan pikiran dengan pekerjaan."

    jump nadya_button_pregnant_depot.choice


label nadya_button_pregnant_depot.work:
    show anon f_confused
    show svetlana a_surprised f_surprised
    with {'master': dissolve}
    anon "Bukankah kamu seharusnya menjauh?"

    nadya f_frowning @ -m_talk "Hmm?"

    show svetlana a_sides f_concerned_back
    with {'master': dissolve}
    nadya "Saya hamil, bukan cacat."

    show anon a_behind_head f_shy with {'master': dissolve}
    anon "Y-ya, tapi-"

    show svetlana a_crossed f_concerned with {'master': dissolve}
    svetlana "Bisnis tidak menunggu bayi."

    svetlana f_normal "{b}Rusia{/b} wanita itu kuat."

    show anon a_sides f_worried
    with {'master': dissolve}
    svetlana "Saya melihat mereka melahirkan di ladang gandum dan langsung kembali bekerja."

    show anon f_shock
    svetlana "Tidak masalah."

    nadya f_normal "Lihat, {b}Svetlana{/b} tahu!"

    show anon f_surprised
    show svetlana a_sides
    with {'master': dissolve}
    nadya "Saya akan terus bekerja."

    show anon f_worried_surprised
    nadya "Banyak uang yang bisa dihasilkan."

    anon @ -m_talk "..."
    jump nadya_button_pregnant_depot.choice


label nadya_button_pregnant_office:
    show anon b_sit with dissolve:
        xoffset -250
    nadya "Hello, {b}[firstname]{/b}." (show_native="Privet, {b}[firstname]{/b}.")
    nadya f_confused "Anda datang untuk memeriksa saya?"


    menu nadya_button_pregnant_office.choice:
        "Bagaimana kabar bayinya?" if 1 == M_nadya.pregnancy.stage:
            jump nadya_button_pregnant_office.tired

        "Bagaimana kabar bayinya?" if 2 == M_nadya.pregnancy.stage:
            jump nadya_button_pregnant_office.kick

        "Bagaimana kabar bayinya?" if 3 <= M_nadya.pregnancy.stage:
            jump nadya_button_pregnant_office.soon
        "Ada yang bisa kuberikan padamu?":

            jump nadya_button_pregnant_office.anything
        "Aku akan membiarkanmu beristirahat.":

            pass

    anon "Aku akan membiarkanmu beristirahat."

    nadya f_normal "Ya, istirahat."

    nadya "Kita akan bicara lebih banyak lagi nanti."

    anon "Sampai jumpa, {b}Nadya{/b}."

    hide anon with dissolve
    return


label nadya_button_pregnant_office.anything:
    anon f_normal "Bagaimana kalau digosok kaki?"

    nadya f_sexy_low "Mmm, kedengarannya bagus..."

    pause
    nadya f_sexy "...Mungkin nanti ya?"

    anon "Ya, tentu saja."

    jump nadya_button_pregnant_office.choice


label nadya_button_pregnant_office.kick:
    anon "Bagaimana kabar bayinya?"

    nadya f_worried "Ugh, sayang mulai menendang sekarang."

    anon "Oh ya?"

    nadya "Apakah gangguan saat downtime."

    nadya f_annoyed_down "Diam dan duduk diam!"

    anon f_worried_surprised "Umm, mungkin sebaiknya kamu tidak membentak janin itu?"

    nadya f_frowning "Kamu mau aku malah membentakmu?!"

    show anon a_surprised f_surprised with {'master': dissolve}
    anon "aku uhh-"

    pause
    show anon a_idle f_worried_low with {'master': dissolve}
    anon "T-tidak."

    nadya "Kalau begitu diamlah!"

    nadya f_annoyed_down "Kalian berdua!"

    show anon f_worried
    nadya f_worried "Mama butuh waktu relaksasi."

    jump nadya_button_pregnant_office.choice


label nadya_button_pregnant_office.soon:
    anon "Bagaimana kabar bayinya?"

    nadya f_normal "{b}Svetlana{/b} mengatakan bayi akan segera lahir."

    nadya "Saya sangat ingin menyelesaikan ini."

    anon f_worried "Ya, aku tahu kamu merasa tidak nyaman..."

    anon f_shy "... Tapi kamu harus bertahan beberapa hari lagi, kan?"

    nadya f_worried "{i}*Huh*{/i} Ya."

    pause
    nadya f_pouting "Saya akan membunuh demi rokok sekarang."

    jump nadya_button_pregnant_office.choice


label nadya_button_pregnant_office.tired:
    anon "Bagaimana kabar bayinya?"

    nadya f_worried "Tolong, jangan ada pertanyaan... Saya lelah karena hari yang panjang."

    anon f_worried "Oh, umm... Oke."

    jump nadya_button_pregnant_office.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
