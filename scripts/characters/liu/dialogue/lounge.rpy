label liu_button_lounge:
    show anon b_dressed_floor behind table with dissolve:
        xoffset -230
    liu "Saya sedang minum teh hijau dengan madu."

    liu "Ini sangat sehat."

    show liu a_hold
    show liu_overlay_o_tea_table_pot as table
    with dissolve
    pause
    liu f_happy "Apakah Anda mau?"


    menu liu_button_lounge.choice:
        "uang ayah." if M_anon.is_state(S_ano28_cash):
            jump liu_button_lounge.backpack
        "Ya tentu saja.":

            jump liu_button_lounge.tea
        "Aku mencintaimu dengan kimono itu!":

            jump liu_button_lounge.kimono
        "Seks.":

            jump liu_button_lounge.sex
        "Sampai jumpa nanti.":

            pass

    anon "Sampai jumpa nanti."

    liu f_worried "Berangkat begitu cepat?"

    anon f_shy "Ya, ada yang harus kulakukan."

    liu f_worried_down "Ah, oke..."

    hide anon
    hide liu
    with dissolve

    scene expression background(400, 400, 2) as stage
    show anon b_empty f_shy_low
    show liu b_robe_hug behind anon:
        xoffset 0
    with fade
    pause
    liu "Anda akan kembali lagi, ya?"

    show anon a_beer_cheer b_dressed f_normal behind liu
    show liu b_robe_hair:
        xoffset -300
    with {'master': dissolve}
    anon "Tentu saja."

    liu f_happy "Sampai jumpa, {b}[firstname]{/b}."

    anon "Nanti, {b}Liu{/b}."

    hide anon with dissolve
    return


label liu_button_lounge.backpack:
    anon f_worried_left "Celana!"

    show liu f_confused
    anon f_worried "Saya meninggalkan ransel saya di dekat pintu, dua detik!"

    hide anon with dissolve

    scene expression background(216, 384, 4.5) as stage
    show anon a_backpack1 f_looking_down
    with fade
    show liu b_robe_hair f_worried behind anon with dissolve
    liu "Apa itu?!"

    show anon f_normal
    jump ano28_cash_liu_money


label liu_button_lounge.kimono:
    anon f_flirt "Aku mencintaimu dengan kimono itu!"

    liu f_curious "Ya?"

    anon @ -m_talk "Mhmm."

    liu f_sexy "Mungkin saya harus membuat modelnya lagi untuk Anda?"


    menu:
        "Ya, tolong!":
            jump liu_button_lounge.model
        "Mungkin nanti?":

            pass

    anon f_worried "Saya tidak ingin teh enak Anda menjadi dingin."

    liu f_worried_down "Oh ya... Itu pemikiran yang bagus!"

    show anon a_tea_drink f_drink
    show liu a_drink f_drink
    with dissolve
    pause
    show anon a_down f_normal
    show liu a_down f_happy
    with {'master': dissolve}
    anon "Hmm, enak."

    jump liu_button_lounge.choice


label liu_button_lounge.model:
    anon "Tentu saja!"

    liu f_laugh "Heh, apa pun untukmu, {b}[firstname]{/b}!"

    show anon f_shy_high
    hide liu
    with dissolve

    scene expression game.timer.image('location_liu_lounge_close{}')
    show liu b_robe_front1 f_normal
    with fade
    liu "Seperti ini?"

    anon "Kamu cantik sekali!"

    liu f_normal_down "{b}[firstname]{/b}!!"

    liu "Kamu membuatku tersipu!"

    anon "Ayolah, sayang... tunjukkan padaku sedikit..."

    liu b_robe_front2 f_normal "Hehe, seperti ini?"

    anon "Ya."

    anon "Sama seperti itu."

    pause
    anon "Ya ampun, kamu seksi sekali!"

    liu "hehe!"


    scene expression game.timer.image('location_liu_lounge_tea{}')
    show anon b_dressed_floor f_shy_high:
        xoffset -230
    show liu_overlay_o_tea_table_pot as table
    with fade
    show anon f_flirt
    show liu b_robe_tea f_happy behind table
    with dissolve
    liu "Terima kasih, {b}[firstname]{/b}."

    liu "Kamu selalu membuatku begitu baik tentang diriku sendiri."

    anon f_normal "Anda juga harus melakukannya."

    anon f_happy "Kamu cantik!"

    liu "hehe!"

    jump liu_button_lounge.choice


label liu_button_lounge.sex:
    jump liu_button_bedroom.sex


label liu_button_lounge.tea:
    anon "Oooh, ya, tolong!"

    show anon f_normal_low
    show liu a_give
    with {'master': dissolve}
    liu "Ini dia."

    show anon a_tea_hold f_normal
    show liu a_down
    with dissolve
    anon "Terima kasih."

    show anon a_tea_drink f_thinking_down with dissolve
    pause
    show anon a_down f_surprised with {'master': dissolve}
    anon "Wah, enak sekali!"

    liu f_happy "Hehe, terima kasih."

    show anon f_normal
    liu "Ibu saya biasa membuatkannya untuk saya ketika saya masih kecil, itu adalah favoritnya."

    anon "Itu bagus!"

    pause
    anon f_confused "Katakanlah, apakah kamu pernah berpikir untuk menghubungi orang tuamu?"

    show liu f_nervous
    anon "Anda tahu, sekarang {b}Kim{/b} sudah tidak ada lagi..."

    liu "Um, tidak juga..."

    show anon f_worried
    liu f_worried_down "... Menurutku mereka tidak punya telepon atau semacamnya, menghubungi mereka tidak akan mudah."

    anon f_shy "Anda dapat mencoba menulisnya."

    show liu f_worried
    anon "Aku yakin ibumu akan senang mendengar bahwa kamu baik-baik saja sekarang."

    liu f_nervous "Heh, kamu manis sekali, {b}[firstname]{/b}."

    liu f_happy "Mungkin saya harus mencoba dan menulis surat kepada mereka..."

    anon "Ya, menurutku begitu."

    anon f_normal "Akan lebih baik bagi Anda untuk terhubung kembali, meskipun hanya melalui surat."

    jump liu_button_lounge.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
