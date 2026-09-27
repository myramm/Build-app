label con01_idea_ivy:
    anon f_worried "Apakah Anda tertarik melakukan sedikit pekerjaan pembantu untuk {b}walikota{/b}?"

    ivy f_confused "Pekerjaan pembantu?"

    ivy "Apakah itu sebuah eufemisme untuk sesuatu?"

    anon f_normal @ f_shy a_behind_head "T-tidak."

    anon "Dia membutuhkan seseorang untuk membersihkan rumahnya."

    ivy f_normal "Heh, apa aku terlihat seperti pelayan bagimu?"

    anon f_worried "Anda tidak."

    ivy "Baiklah, ini dia."

    anon @ f_sad_down "{i}*Huh*{/i} Sial."

    ivy "Mungkin mencoba layanan tata graha atau semacamnya?"

    anon "Tidak, itu tidak akan berhasil."

    ivy "Kenapa tidak?"

    anon "{b}Walikota{/b} punya beberapa, eh, \"berkebutuhan khusus.\""

    ivy "Maksudmu-"

    pause
    ivy f_shy @ f_eww "eh."

    anon "Ya."

    ivy f_normal "Anda tahu apa?"

    show ivy b_naked_pickup with dissolve
    ivy "Saya mungkin punya jawaban untuk masalah Anda."

    anon f_surprised "Benar-benar?"

    ivy "Yup, beri aku satu-"

    show anon f_normal
    ivy "Ah hah!"

    show ivy b_dressed a_thotbot with dissolve
    ivy "Ini dia."

    pause

    scene expression player.location.background_closeup
    show closeup_thotbot
    with fade
    pause
    anon "{b}Bot itu{/b}?"

    anon "Solusi pembersihan untuk pria kesepian."

    anon "Dengan alat kelamin yang realistis?"


    call ivy_button_stage
    show anon f_skeptical a_thotbot
    with fade
    anon "Apakah ini nyata?"

    ivy "Ya."

    ivy "Dulu aku punya satu di toko ini, tapi seorang wanita berjas lab membelinya."

    anon f_thinking a_thinking "Hmm, ini sebenarnya bisa berhasil."

    anon f_normal "Bisakah kamu memberikanku satu?"

    ivy "Jika Anda punya uang, saya bisa mendapatkannya di sini dalam beberapa hari."

    anon "Berapa harganya?"

    ivy "Dengan pengiriman, katakanlah... Seribu dolar?"

    anon f_shock a_surprised_up_both "Seribu dolar?!"

    return


label con01_deal_ivy:
    anon "Apakah kamu masih bersedia memesan robot pembantu itu untukku?"

    ivy "Boleh, selama kamu punya uang?"


    menu con01_deal_ivy.choice:
        "Baiklah, ini dia." if player.has_money(1000):
            jump con01_deal_ivy.purchase
        "Saya tidak mampu membelinya!":

            pass

    anon f_worried a_idle @ f_sad_down "Saya tidak punya itu!"

    ivy "Baiklah, kembalilah dan temui aku ketika kamu melakukannya."

    anon "Astaga, baiklah."

    anon "Saya akan kembali."

    hide anon with dissolve
    return


label con01_deal_ivy.purchase:
    anon f_normal a_money "Baiklah, ini dia."

    show anon a_idle
    show ivy a_money
    with dissolve
    ivy "Sempurna!"

    ivy a_idle "Saya akan segera memesannya."

    ivy "Kembalilah dan ambil dalam beberapa hari, oke?"

    anon "Baiklah terima kasih!"

    hide anon with dissolve

    $ player.spend_money(1000)
    $ M_consuela.trigger(T_con01_deal)
    return


label con01_take_ivy:
    anon "Apakah paket saya sudah sampai?"

    ivy "Tentu saja!"

    show anon f_normal
    ivy "Satu detik."

    hide ivy with dissolve
    pause
    ivy "Anda tahu, ketika mereka berkata, \"alat kelamin yang realistis\" mereka tidak bercanda!"

    ivy "Hal ini luar biasa!"

    show ivy f_laugh
    show thotbot:
        flip
        xoffset -100
    with dissolve
    show anon f_surprised
    ivy "Aku tidak bisa menjamin kemampuan pembersihannya, tapi vagina itu prima!"

    show ivy f_normal
    anon f_confused "Eh, kamu mencobanya?"

    ivy f_sexy "Tentu saja!"

    ivy "Saya melakukan pengujian jaminan kualitas pada semua produk saya di sini di {b}Pink{/b}."

    anon "... Benar."

    ivy @ f_laugh "hehe!"

    show anon f_flirt_grin
    pause
    ivy "Ada lagi yang bisa saya bantu?"

    anon f_flirt_low "T-tidak, aku baik-baik saja."

    anon "Saya hanya berharap {b}walikota{/b} menyukainya."

    ivy "Saya yakin dia akan melakukannya."

    ivy f_normal "Semoga harimu menyenangkan!"

    anon @ f_flirt a_wave "Terima kasih!"

    show anon a_backpack_robot
    hide thotbot
    with dissolve
    pause

    scene expression player.location.background_blur
    show anon f_worried
    with fade
    anon @ -m_talk "( Sobat, kuharap aku tidak bertemu dengan siapa pun yang kukenal saat aku membawa barang ini... )"

    anon @ -m_talk "( Saya harus {b}bergegas menemui istri walikota{/b} dan melihat apakah itu cukup untuk membebaskan {b}Consuela{/b}. )"

    hide anon with dissolve
    return


label con01_take_ivy.check:
    anon "Apakah paket saya sudah sampai?"

    ivy "Sayangnya tidak."

    ivy "Biasanya diperlukan waktu dua atau tiga hari untuk pengiriman di sini."

    anon f_sad_down "{i}*Huh*{/i} Baiklah, terima kasih."

    hide anon with dissolve
    return


label con01_skip_ivy:
    if player.has_item('thotbot'):
        show anon a_backpack f_looking_down with dissolve
        pause
        anon a_backpack_robot f_normal "Saya ingin mengembalikan ini."

        show anon a_sides f_normal
        show thotbot:
            flip
            xoffset -100
        with dissolve
        ivy "Tentu saja!"

        ivy "Anda belum menggunakannya kan? Kami tidak dapat menerima barang bekas, Anda mengerti."

        show anon f_surprised
        show anon of_blush with {'master': dissolve}
        anon "Aku-- T-- Tidak! Itu sudah ada di tasku sepanjang waktu!"

        ivy "Luar biasa, itu pasti membantu."

    else:
        anon "Saya ingin membatalkan {b}Thotbot{/b} yang saya pesan."

        ivy "Tidak masalah!"


    ivy f_surprised_down "Hmm, lebih sedikit pengiriman dan penanganan, Anda berhak mendapatkan pengembalian dana delapan puluh persen."

    show ivy f_normal
    anon -of_blush f_shock "!!!" with hpunch
    anon f_surprised "Hanya delapan puluh persen?!"

    ivy "Itu adalah pesanan khusus. Saya sangat menyesal."

    anon f_sad "Kurasa lebih baik daripada tidak sama sekali."

    if player.has_item('thotbot'):
        hide ivy with dissolve
        pause .6
        show ivy behind thotbot with dissolve:
            xoffset -50
        pause
        hide thotbot
        hide ivy
        with dissolve
        pause .6
        show ivy behind counter with dissolve
    ivy a_money "Ini dia, maaf pembelian Anda tidak berhasil."

    show anon a_money
    show ivy a_idle
    with dissolve
    anon "Terima kasih."

    show anon a_idle with dissolve
    ivy "Akankah ada hal lain?"

    anon "Tidak saat ini."

    ivy f_normal "Semoga hari Anda membaik!"

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
