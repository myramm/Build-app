label ricky_button_garden:
    show ricky f_smirk
    show anon f_worried at flip with dissolve
    ricky "Halo, teman-teman."

    ricky "Mengapa kamu tidak melepas baju itu dan membantuku berkebun?"

    anon "Uhh, aku tidak yakin itu ide yang bagus..."

    ricky "Hmm, bukan?"

    ricky "Buka saja bajunya dan awasi."

    ricky "Saya bisa menggunakan motivasi."


    menu ricky_button_garden.choice:
        "{b}Consuela{/b}." if M_consuela.is_state(S_con01_init):
            if M_ricky.once('con02_dialogue_consuela'):
                jump con01_init_ricky.repeat
            else:
                jump con01_init_ricky

        "Pengganti {b}Consuela{/b}." if M_consuela.is_state(S_con01_plan):
            jump con01_plan_ricky
        "Motivasi?":

            jump ricky_button_garden.motivation
        "Apakah kamu gay?":

            jump ricky_button_garden.gay
        "Saya harus pergi.":

            pass

    show ricky f_smirk
    anon f_normal "Sampai jumpa, {b}Ricky{/b}."

    ricky @ f_sad "Aww, aku benci melihatmu pergi, amigo..."

    pause
    ricky "... Tapi aku senang melihatmu pergi."

    anon f_grumpy @ -m_talk "..."
    hide anon with dissolve
    return


label ricky_button_garden.motivation:
    show ricky f_smirk
    anon @ f_confused "Motivasi?"

    ricky "Itu benar!"

    ricky "Tidak ada yang lebih memotivasi saya selain taquito kecil pedas yang menggonggong perintah kepada saya."

    anon f_grumpy "Eh."

    ricky "Biarkan aku memilikinya, ya?"

    ricky "aku sudah menjadi anak yang nakal..."


    menu:
        "Lulus.":
            anon "Yaaa, tidak."

            ricky f_sad "Aduh."

            pause
            ricky f_smirk "Kamu tidak menyenangkan, kawan."

            show anon f_worried
        "Mungkin nanti.":

            anon f_worried "Mungkin lain kali..."

            ricky "Ah, jika kamu mau, teman-teman..."

            ricky "... Tapi aku menahanmu, kan?"

            anon @ -m_talk "..."
            ricky @ f_laugh "Hehehe!"


    jump ricky_button_garden.choice


label ricky_button_garden.gay:
    show ricky f_smirk
    anon f_skeptical "Apakah kamu gay?"

    ricky "Apa yang memberikannya?"

    ricky @ f_laugh "hehe!"

    anon f_worried "Saya pikir Anda dan {b}Ny. Pantat{/b} itu uhh... Kamu tahu?"

    ricky f_confused "Kamu pikir aku akan membiarkan perempuan tua itu mengambil tindakan bersamaku?!"

    ricky f_smirk @ f_laugh "Ha ha ha ha!!"

    anon f_confused @ -m_talk "..."
    anon "Aku melihatnya di sekitarmu tadi!"

    ricky "Oh, dia menginginkannya, itu pasti!"

    ricky "Dia membayarku sedikit tambahan untuk menghiburnya..."

    ricky "... Dan ya, saya sedikit menggodanya, tetapi hanya untuk meningkatkan penghasilan saya!"

    ricky "Seorang gadis harus dibayar, kau tahu?"

    anon f_worried @ -m_talk "..."
    ricky "Saya tidak akan berhubungan seks dengannya demi semua uang di dunia!"

    anon "Anda tidak mau?"

    ricky "Tidak!"

    ricky "Prajurit Aztec kecilku hanya menyukai laki-laki, ya?"

    anon f_skeptical "Apa kecilmu-"

    ricky f_laugh "Prajurit Aztecku, amigo!"

    anon @ -m_talk "..."
    ricky f_smirk "Lihat dirimu tersipu!"

    ricky "Kamu terlalu menggemaskan!"

    anon f_worried "Y-ya, terima kasih."

    jump ricky_button_garden.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
