label tony_button_baby:
    show anon with dissolve:
        flip
    if randomizer() > 80:
        tony "Lalu, saya menatap wajah si bajingan itu dan mengatakan kepadanya, \"Pengampunan itu antara kamu dan Tuhan.\""

        tony "\"Saya di sini hanya untuk mengatur pertemuan.\""

        tony @ f_laugh "Hahahah!!"

        tony "Wah, kalau begitu dia buang air di celananya... Biar kuberitahu ya!"

    elif randomizer() > 60:
        tony "Lalu, Luigi memberi tahu pria itu, \"Saya datang ke sini untuk memecahkan tengkorak dan makan sandwich ciabatta\"..."

        tony "... \"Dan aku sudah kehabisan sandwich ciabatta.\""

        tony @ f_laugh "Hahahah!!"

        tony "Bajingan itu menutup mulutnya dengan sangat cepat setelah itu..."

    elif randomizer() > 40:
        tony "Lalu, aku berkata, \"Ya, aku akan mengantarmu ke bank\"..."

        tony "... \"Bank darah sialan itu!\""

        tony "Bang, bang, bang!"

        tony @ f_laugh "Hahahah!!"

        tony "Butuh waktu berjam-jam untuk membersihkan otaknya dari karpet!"

        tony "Itu sebabnya Anda selalu membawanya ke suatu tempat dengan lantai kayu keras..."

    elif randomizer() > 20:
        tony "Lalu, Luigi berkata, \"Kamu masih berbahaya\"..."

        tony "... \"Tapi kamu bisa menjadi wingmanku kapan saja!\""

        tony "Lalu saya berkata, \"Omong kosong!\"..."

        tony "... \"Kamu bisa menjadi milikku!\"."

        tony @ f_laugh "Hahahah!!"

        tony "Anda seharusnya melihat wajahnya!"

    else:
        tony "Lalu, aku berkata, \"Sampaikan salamku pada teman kecilku!\""

        tony "Bang, bang, bang!"

        tony @ f_laugh "Hahahah!!"

        tony "Bajingan bodoh tidak tahu apa yang menimpa mereka!"


    menu tony_button_baby.choice:
        "Apa yang sedang kamu lakukan?":

            jump tony_button_baby.stories
        "{b}Di mana Maria{/b}?":

            jump tony_button_baby.maria
        "Aku akan meninggalkanmu.":

            pass

    anon f_normal a_wave "Aku akan meninggalkanmu."

    tony f_normal "Ada beberapa pengiriman di konter untukmu."

    anon "Terima kasih!"

    hide anon with dissolve
    return


label tony_button_baby.maria:
    anon f_normal "{b}Di mana Maria{/b}?"

    tony f_normal "Dia di belakang, sedang memasak badai."

    anon "Baiklah."

    tony "Berikan dia cintaku, ya?"

    anon "Tentu saja."

    tony @ f_smirk_wink "Dan jangan terlalu berisik!"

    pause
    tony "Aku tidak ingin ada pelanggan yang mendengar kalian berdua..."

    hide anon with dissolve
    return


label tony_button_baby.stories:
    anon f_normal "Apa yang sedang kamu lakukan?"

    tony f_normal @ -m_talk "Hmm?"

    tony "Oh, aku baru saja menceritakan beberapa cerita dari masa lalu..."

    anon "Untuk bayinya?"

    tony @ f_laugh "Ya."

    pause
    tony f_sad "Terlalu banyak?"

    anon f_shy a_behind_head "Ehh."

    anon "Aku hanya khawatir ini sedikit.... Menimbulkan mimpi buruk..."

    show anon a_idle with dissolve
    tony f_normal "Pfft, bukannya aku menceritakan cerita hantu..."

    tony "Ini adalah hal yang benar-benar terjadi!"

    anon "Mungkin menempel pada cerita anak-anak?"

    anon "Aku akan membelikanmu buku atau sesuatu..."

    tony "Hehe, kamu melakukan itu."

    jump tony_button_baby.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
