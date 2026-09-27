label tony_button_lounge:
    show anon behind tony with dissolve:
        flip
        xoffset 100
    tony @ a_frustrated "'Hei, jagoan!"

    anon "Hai, {b}Tony{/b}."

    tony "Anda ingin menonton pertandingan dengan saya?"

    anon @ -m_talk "Hmm?"

    tony "Lakukan jongkok dan ambil sepotong, ini baru saja dimulai."

    tony @ a_point "Anda ingin bir?"


    menu tony_button_lounge.choice:
        "Permainan apa?":

            jump tony_button_lounge.game
        "Tidak ada pekerjaan hari ini?":

            jump tony_button_lounge.work
        "Saya tidak bisa tinggal.":

            pass

    anon f_normal "Saya tidak bisa tinggal."

    tony f_suspicious "Tidak?"

    tony f_normal "Ya, itu memalukan."

    anon "Mungkin lain kali."

    tony f_laugh a_pizza "Kurasa itu artinya aku harus makan seluruh pizza ini sendirian, ya?"

    hide anon with dissolve
    return


label tony_button_lounge.game:
    anon f_normal "Permainan apa?"

    tony f_surprised "Kamu bercanda kan?"

    anon f_worried "Eh, bukan?"

    tony f_normal @ f_laugh "Pertandingan bisbol, juara!"

    anon f_normal @ f_skeptical "Tunggu, kamu penggemar baseball?"

    tony @ a_point_back "Tentu saja saya."

    tony "Hot dog, Cracker Jacks, dan pria dewasa menghancurkan barang-barang dengan tongkat kayu..."

    tony @ a_frustrated "... Apa yang tidak disukai?!"

    anon "Heh, menurutku itu terdengar seperti sesuatu yang kamu sukai."

    tony f_smirk "Ya benar sekali."

    tony "Itu adalah hiburan favorit orang Amerika, Anda tahu?"

    show anon f_thinking
    pause
    anon f_skeptical "Bukankah kamu orang Italia?"

    tony a_point f_angry "Ah!"

    show anon f_worried
    tony "Perhatikan omong kosong itu."

    tony f_normal a_idle @ f_laugh a_point_back "Saya orang Italia-Amerika."

    anon f_shy "Benar."

    anon "Maaf."

    tony f_smirk "Ahh, maaf!"

    jump tony_button_lounge.choice


label tony_button_lounge.work:
    anon f_normal "Tidak ada pekerjaan hari ini?"

    tony f_normal "Kamu tidak seharusnya bekerja pada hari Minggu, jagoan..."

    tony @ f_question "... Bukankah tidak ada seorang pun yang pernah mengajarimu hal itu?"

    anon "Tidak."

    pause
    anon "Kenapa?"

    tony @ a_frustrated "Itu ada di dalam Alkitab, kamu orang bodoh."

    anon "Hah?"

    tony @ a_finger_up "Dan pada hari ketujuh, Tuhan beristirahat."

    anon f_worried "Itu ada di dalam Alkitab?"

    tony f_smirk "Anda sebaiknya mempercayainya."

    anon f_normal "Saya tidak tahu."

    tony "Heh, kamu belajar hal baru setiap hari saat jalan-jalan bersama {b}Paman Tony{/b}, ya?"

    anon "Y-ya, menurutku begitu..."

    jump tony_button_lounge.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
