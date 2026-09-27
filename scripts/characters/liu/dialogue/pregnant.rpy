label liu_button_pregnant:
    $ renpy.dynamic(bank=L_bank_lobby.is_here(M_liu))

    show anon with dissolve

    if bank:
        liu "Selamat datang di {b}Saga Finansial{/b}."

        liu f_normal "Bagaimana saya bisa membantu-"

        show liu a_mouth_cover f_surprised
        with {'master': dissolve}
        liu "{b}[firstname]{/b}!!"

        anon "Hei, Liu."

        show liu a_idle f_nervous with {'master': dissolve}
        liu "Apakah Anda datang untuk memeriksa kami?"

    else:

        anon "Hai, {b}Liu{/b}."

        liu "Hai, {b}[firstname]{/b}."


    menu liu_button_pregnant.choice:
        "Bagaimana perasaanmu?":
            jump liu_button_pregnant.feeling

        "Apakah Tina ada?" if bank and M_tina.is_state(S_tin02_init):
            if L_bank_cubicle.is_here(M_tina):
                jump tin02_init_liu
            jump liu_button_pregnant.tina

        "Apakah Anda memberi tahu {b}Tina{/b}?" if bank:
            jump liu_button_pregnant.lonely

        "Ada yang bisa kuberikan padamu?" if not bank:
            jump liu_button_pregnant.anything
        "Beritahu saya jika Anda memerlukan sesuatu.":

            pass

    show liu f_happy

    if bank:
        anon "Hubungi saya jika Anda butuh sesuatu."

        anon "Aku akan tiba di sini sebentar lagi, aku janji."

        liu "Kamu pria yang baik, {b}[firstname]{/b}."

        liu "Terima kasih."

        anon f_shy "Sama-sama, {b}Liu{/b}."

    else:

        anon "Beritahu saya jika Anda memerlukan sesuatu."

        liu "Oke, {b}[firstname]{/b}."

        liu "Terima kasih telah memeriksa saya."

        anon f_shy "Tentu saja, {b}Liu{/b}."

        anon "Saya akan selalu ada jika Anda membutuhkan sesuatu."


    hide anon with dissolve
    return


label liu_button_pregnant.anything:
    show liu f_happy
    anon "Adakah yang bisa saya berikan untuk Anda?"

    liu f_curious @ -m_talk "Hmm?"

    anon f_thinking "Makanan yang menenangkan mungkin?"

    show anon f_normal
    liu f_nervous_down "Tidak, tawaranmu sangat manis, tetapi aku tetap menjalankan diet ketat demi anak kita."

    anon f_confused "Oh?"

    liu f_happy "Karena saat itu musim panas, saya membeli goji berry, kenari, dan salmon hasil tangkapan liar dari pasar Cina di kota besar."

    anon f_normal "Kedengarannya bagus."

    liu "Saya ingat ibu saya biasa menumis bayam dan telur dengan mentega dan kecap setiap pagi ketika dia sedang mengandung adik laki-laki saya."

    anon "Saya kira Anda sudah mengendalikan makanannya..."

    anon f_thinking "... Mungkin aku bisa menggosok punggungmu atau semacamnya?"

    show anon f_normal
    liu f_nervous_lipbite_back @ -m_talk "MM."

    liu f_sexy "Saya mungkin akan membahasnya nanti, {b}[firstname]{/b}."

    anon f_shy "Heh, saya siap membantu Anda, Nyonya."

    liu f_laugh "hehe!"

    pause
    show liu f_happy
    jump liu_button_pregnant.choice


label liu_button_pregnant.feeling:
    show liu f_happy
    anon f_confused "Bagaimana perasaanmu?"

    liu f_curious @ -m_talk "Hmm?"

    liu f_normal "Oh, aku baik-baik saja."

    show anon f_shy
    liu f_nervous_back "Memiliki anak adalah profesi utama seorang wanita di tempat asalku, jadi..."

    liu f_nervous "... Ibu saya mengajari saya banyak hal sebagai seorang anak."

    anon f_normal "Benar-benar?"

    liu f_normal @ -m_talk "Mhmm."

    liu "Pengobatan rumahannya untuk mencegah mual di pagi hari sangat efektif."

    anon "Wah, itu luar biasa!"

    show anon a_thinking f_thinking with dissolve
    pause
    show anon a_point f_normal with {'master': dissolve}
    anon "Anda tahu, saya yakin ada pasar yang besar untuk pengobatan rumahan seperti itu!"

    liu f_curious "Oh?"

    show anon a_sides f_normal_high with {'master': dissolve}
    anon f_normal_high "Khususnya di Summerville..."

    anon f_normal "... Kehamilan adalah hal besar di sini."

    liu f_surprised "Saya tidak tahu."

    jump liu_button_pregnant.choice


label liu_button_pregnant.lonely:
    show liu f_happy
    anon f_normal "Apakah Anda sudah memberi tahu {b}Tina{/b} tentang bayinya?"

    liu "Oh ya!"

    liu "Dia sangat bersemangat untukku."

    anon "Saya berani bertaruh."

    pause
    liu f_surprised "Tahukah Anda bahwa perempuan mendapat cuti hamil selama enam minggu di negara ini?"

    anon f_confused "Ya, saya pernah mendengar tentang itu."

    show anon f_normal
    liu f_curious "Saat {b}Tina{/b} memberitahuku hal itu, aku tidak percaya!"

    show liu f_worried
    pause
    liu "Bolehkah aku menghabiskan begitu banyak waktu?"

    anon f_happy "Heh, tentu saja {b}Liu{/b}."

    show liu f_curious
    anon f_normal "Mereka memberi Anda banyak waktu karena suatu alasan..."

    anon "... Ini penting untuk kesehatan fisik dan mental Anda."

    liu f_normal "Ya, menurutku itu masuk akal."

    show liu f_ashamed_down
    pause
    liu f_worried_down "Aku masih merasa tidak enak meninggalkan {b}Tina{/b} sendirian di sini."

    show liu f_normal_down
    pause
    liu f_happy "Mungkin kamu bisa mampir dan menemaninya saat aku pergi?"

    anon f_confused "Menemaninya?"

    liu "Ya, hanya untuk memastikan dia tidak terlalu kesepian bersamaku di rumah."

    show anon a_behind_head f_worried with {'master': dissolve}
    anon "Ehh..."

    liu f_nervous "Silakan?"

    show anon a_sides with {'master': dissolve}
    anon "... Jika itu yang kamu inginkan."

    show anon f_normal
    liu f_happy_excited_closed "Hore!!"

    liu f_happy "Terima kasih, {b}[firstname]{/b}!"

    anon "Hehe, tidak masalah."

    jump liu_button_pregnant.choice


label liu_button_pregnant.tina:
    anon f_normal "Apakah Tina ada?"

    if game.timer.is_weekend():
        liu f_worried "Tidak, dia hanya bekerja pada {b}hari kerja{/b}."

    else:
        liu f_worried "Tidak, Dia tidak akan masuk sampai nanti {b}sore ini{/b}."

    show anon f_worried
    liu f_curious "Bisakah saya membantu?"

    anon f_normal "Tidak, tidak, tidak apa-apa, ini bisa menunggu."

    show liu f_nervous
    jump liu_button_pregnant.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
