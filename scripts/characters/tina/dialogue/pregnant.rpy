label tina_button_pregnant:
    $ renpy.dynamic(local=flip if L_bank_lobby.is_here(M_tina) else reset)

    if M_tina.outfit.is_naked:
        show tina f_sad
        show anon f_worried with dissolve
        anon "Wow, panas sekali di-"

        anon f_surprised "!!!"
        anon f_flirt_low "Di sini..."

        tina "Halo, {b}[firstname]{/b}."

        tina "Maaf tentang panasnya."

        anon f_flirt "K-kamu telanjang!"

        tina @ f_laugh "Hehe, ya, aku tahu."

        tina "AC kami rusak dan {b}Tony{/b} mengalami kesulitan untuk memperbaikinya."

    else:
        show anon at local with dissolve
        anon "Hai, {b}Tina{/b}."

        tina "Halo, {b}[firstname]{/b}."


    menu tina_button_pregnant.choice:

        "Tidak bisakah Anda membayar untuk memperbaikinya?" if M_tina.outfit.is_naked:
            jump tina_button_pregnant.aircon
        "Bagaimana perasaanmu?":

            if M_tina.pregnancy.stage == 1:
                jump tina_button_pregnant.excited
            elif M_tina.pregnancy.stage == 2:
                jump tina_button_pregnant.sick
            else:
                jump tina_button_pregnant.bloated
        "Ada yang bisa kuberikan padamu?":

            if M_tina.pregnancy.stage == 1:
                jump tina_button_pregnant.obgyn
            elif M_tina.pregnancy.stage == 2:
                jump tina_button_pregnant.nutritionist
            else:
                jump tina_button_pregnant.masseuse
        "Sampai jumpa lagi.":

            pass

    anon f_normal a_wave "Sampai jumpa lagi."

    show tina f_normal
    anon "Jangan ragu untuk menelepon saya, siang atau malam..."

    anon "... Oke?"

    tina "Hal itu seharusnya tidak perlu, namun saya menghargai sentimennya, {b}[firstname]{/b}."

    anon f_worried @ -m_talk "..."
    tina "Hati-hati di jalan."

    hide anon with dissolve
    return


label tina_button_pregnant.aircon:
    anon f_worried "Tidak bisakah Anda membayar untuk memperbaikinya?"

    tina f_sad "Saya bisa, tentu saja."

    tina "Namun {b}Tony{/b} bersikeras untuk memperbaikinya sendiri."

    anon "Ini tidak baik untuk bayinya..."

    tina "Oh, tidak apa-apa."

    tina "OB/GYN saya mengatakan suhunya pasti jauh lebih panas dari ini sebelum kami perlu khawatir."

    anon "Tetap saja..."

    becca "Hei, Bu?"

    becca "Aku tidak bisa membuat penggemar bodoh ini bekerja-"

    show becca b_panties_sweat f_surprised behind tina with dissolve:
        xoffset -300
    show anon f_surprised
    becca "!!!"

    if M_roxxy.finished_state(S_roxxy_get_oil):
        show becca b_panties_sweat_cover with fastdissolve
        becca "{b}[firstname]{/b}?!"

        anon f_normal "Hai, {b}Becca{/b}."

        becca "Apa-"

        show becca f_upset with dissolve:
            flip
            xoffset 300
        becca "Kenapa kamu tidak memperingatkanku dia akan datang!"

        show anon f_flirt_low
        tina "Karena saya tidak tahu..."

        becca f_concerned "Aku tidak ingin dia melihatku seperti ini!"

        tina "Seperti apa, sayang?"

        anon "Ya, kamu baik-baik saja, {b}Becca{/b}."

        show becca with dissolve:
            unflip
            xoffset -300
        show anon f_flirt
        becca "Tidak, bukan aku!"

        becca "Aku berkeringat, kotor, dan..."

        show becca with dissolve:
            flip
            xoffset 300
        becca "... A-dan jangan lihat aku, aku mengerikan!"

        hide becca with dissolve
        show anon f_skeptical
        pause
        tina f_normal "Oh, jangan pedulikan dia."

        show anon f_normal
        tina "Dia hanya malu."

    else:
        show becca f_upset with dissolve:
            flip
            xoffset 300
        becca "Apa yang dia lakukan disini lagi?!"

        show anon f_flirt_low
        tina "Dia di sini untuk memeriksa bayinya, tentu saja..."

        becca @ f_eyeroll "Ugh!"

        becca "Sungguh kacau sekali kalian berdua punya bayi bersama!"

        tina "{b}Becca{/b}, jangan kasar!"

        becca "Apa pun."

        becca "Ayo bantu aku dengan kipas bodoh ini setelah si kutu buku pergi..."

        hide becca with dissolve
        show anon f_normal
        pause
        tina "Oh, jangan pedulikan dia."

        tina "Dia hanya kesal karena panasnya."


    anon @ -m_talk "..."
    jump tina_button_pregnant.choice


label tina_button_pregnant.bloated:
    anon f_worried "Bagaimana perasaanmu?"

    tina f_sad "Kembung."

    tina "Sakit."

    tina "Belum lagi aku meleleh dalam panas ini!"

    anon "Y-ya, tidak diragukan lagi."

    pause
    tina "Setidaknya kita sudah mendekati akhir."

    tina f_normal "Saya tidak sabar untuk bertemu anak kami!"

    anon f_normal "Ya, itu cukup menarik."

    jump tina_button_pregnant.choice


label tina_button_pregnant.excited:
    anon f_normal "Bagaimana perasaanmu?"

    tina f_normal @ f_laugh "Heh, periksa aku, ya?"

    anon "Ya, jika tidak apa-apa?"

    tina "Tentu saja."

    tina "Kamu manis sekali!"

    tina "Aku belum punya pria yang menyayangiku sejak Luigi meninggal..."

    anon "Baiklah, saya di sini jika Anda butuh sesuatu."

    tina "Terima kasih, {b}[firstname]{/b}."

    jump tina_button_pregnant.choice


label tina_button_pregnant.masseuse:
    anon f_normal "Ada yang bisa kuberikan padamu?"

    anon "Pijat punggung atau pijat kaki mungkin?"

    tina f_normal @ f_laugh "Hehe, tidak, tidak apa-apa."

    tina "{b}Becca{/b} dan saya pergi ke tukang pijat dua kali seminggu."

    anon "Seorang tukang pijat?"

    tina "Ya."

    tina "Seperti saya katakan, penting untuk melakukan semua yang saya bisa untuk membantu memastikan bayi lahir bahagia dan sehat."

    anon f_unimpressed "Dan untungnya, Anda punya banyak uang untuk melakukan hal itu..."

    tina @ -m_talk "Mhmm."

    anon @ -m_talk "(Saya yakin saya berharap bisa memainkan peran yang lebih besar di sini...)"

    jump tina_button_pregnant.choice


label tina_button_pregnant.nutritionist:
    anon f_normal "Ada yang bisa kuberikan padamu?"

    anon "Sesuatu untuk dimakan atau diminum mungkin?"

    tina f_normal "Hehe, tidak, tidak apa-apa."

    tina "Ahli gizi saya memberi saya aturan makanan yang sangat ketat untuk bayi..."

    anon @ f_skeptical "Anda punya ahli gizi?"

    tina "Tentu saja."

    tina "Bagi seorang wanita seusia saya, penting untuk melakukan semua yang saya bisa untuk membantu memastikan bayinya lahir dengan bahagia dan sehat."

    pause
    tina "Untungnya, saya punya banyak uang untuk melakukan hal itu."

    anon "Y-ya, itu luar biasa, {b}Tina{/b}."

    jump tina_button_pregnant.choice


label tina_button_pregnant.obgyn:
    anon f_normal "Ada yang bisa kuberikan padamu?"

    anon "Obat mual mungkin?"

    tina f_normal "Hehe, tidak, tidak apa-apa."

    tina "Saya mempunyai seorang spesialis yang menelepon ke rumah tiga kali seminggu..."

    anon @ f_skeptical "Seorang spesialis?"

    tina "Ya, OB/GYN saya."

    tina "Seperti saya katakan, penting untuk melakukan semua yang saya bisa untuk membantu memastikan bayi lahir bahagia dan sehat."

    pause
    tina "Untungnya, saya punya banyak uang untuk melakukan hal itu."

    anon @ f_laugh "Y-ya, itu luar biasa, {b}Tina{/b}."

    jump tina_button_pregnant.choice


label tina_button_pregnant.sick:
    anon f_normal "Bagaimana perasaanmu?"

    tina f_sad "Ugh, aku lupa betapa aku benci mual di pagi hari..."

    anon f_worried "Sangat buruk, ya?"

    tina "Ini sepuluh kali lebih buruk dibandingkan dengan {b}Becca{/b}!"

    tina "Mungkin karena aku sudah lebih tua sekarang..."

    anon "Ya, itu masuk akal."

    jump tina_button_pregnant.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
