label ivy_button_greet:
    show anon with dissolve
    ivy "Hai!"

    ivy "Bisakah saya membantu Anda dengan sesuatu?"

    anon f_worried a_behind_head "Ini pertama kalinya aku ke sini. aku... um..."

    ivy @ f_laugh "Tidak apa-apa! Saya mengerti! Semua orang sedikit malu saat pertama kali datang ke sini..."

    ivy "Kami memiliki banyak pilihan {b}mainan{/b} dan {b}pakaian seksi{/b} yang dapat Anda lihat di pajangan dinding kami."

    show anon f_surprised a_idle with dissolve
    ivy "Kami juga dapat menawarkan... {b}sesi pijat seluruh tubuh{/b} di salah satu... Kamar pribadi kami."

    ivy "Tukang pijat kami menggunakan berbagai teknik relaksasi tubuh alami... Yang pasti akan memuaskan kebutuhan Anda..."

    anon f_normal @ f_confused "Oh... Aku tidak tahu kamu menawarkan pijatan di sini."

    ivy @ f_laugh "Itu salah satu... Layanan yang kurang diiklankan...."

    ivy "Apakah Anda ingin melihat {b}pamflet pilihan pijat kami{/b}?"

    return


label ivy_button_greet_repeat:
    show anon with dissolve
    ivy "Hai!"

    ivy "Bisakah saya membantu Anda dengan sesuatu?"

    return


label button_ivy_massage:
    anon f_shy "Bisakah saya melihat... Pamflet pijat Anda?"

    show ivy a_flyer with dissolve
    ivy "Tentu! Sesuaikan dirimu!"

    anon "Terima kasih..."

    return


label button_ivy_just_shopping:
    anon f_worried "Saya baik-baik saja, terima kasih."

    anon "Aku di sini hanya untuk berbelanja..."

    show anon f_normal
    ivy @ f_laugh "Baiklah kalau begitu! Beri tahu saya jika Anda memerlukan hal lain."

    return


label button_ivy_massage_first:
    show ivy a_flyer
    anon f_normal @ f_shy "Kurasa aku bisa melihatnya..."

    ivy "Tentu! Sesuaikan dirimu!"

    hide ivy
    hide anon
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
