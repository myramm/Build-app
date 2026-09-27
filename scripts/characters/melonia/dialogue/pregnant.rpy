label melonia_button_pregnant:
    show melonia f_annoyed
    show anon with dissolve
    anon "Bagaimana kabarnya?"

    melonia "Cih, aku hamil anak idiotmu.."

    show anon f_worried
    melonia "... Menurut Anda bagaimana kelanjutannya?"


    menu melonia_button_pregnant.choice:
        "Apakah kamu merasa baik-baik saja?":

            if M_melonia.pregnancy.stage == 1:
                jump melonia_button_pregnant.annoyed
            elif M_melonia.pregnancy.stage == 2:
                jump melonia_button_pregnant.vain
            else:
                jump melonia_button_pregnant.nauseous
        "Tetap keluar dari bak mandi air panas?":

            jump melonia_button_pregnant.hottub
        "Saya harus pergi.":

            pass

    anon f_worried "Saya harus pergi."

    anon "Beritahu aku jika kamu butuh sesuatu, oke?"

    melonia f_annoyed "Ya, bagaimana dengan anak biliar yang tahu cara menarik diri?"

    anon f_thinking @ -m_talk "..."
    anon f_normal @ f_laugh "Sangat lucu."

    melonia "Pukul saja dan biarkan aku rileks, ya?!"

    anon f_sad_down "Bagus."

    hide anon with dissolve
    return


label melonia_button_pregnant.annoyed:
    anon f_worried "Apakah kamu merasa baik-baik saja?"

    melonia f_annoyed "Tidak."

    melonia "Aku merasa sangat, sangat kesal padamu saat ini karena membujukku melakukan hal ini!"

    anon "Oke..."

    anon "... Tapi sebaliknya, kamu merasa baik-baik saja?"

    melonia @ f_pouting "{i}*Huh*{/i} Saya merasa hamil."

    melonia "Ada pertanyaan lagi?!"

    jump melonia_button_pregnant.choice


label melonia_button_pregnant.hottub:
    anon f_shy "Tetap keluar dari bak mandi air panas?"

    melonia f_glaring "Apakah kamu ingin aku memukulmu?"

    anon f_brag_closed "Penting bagi Anda untuk tidak berendam air panas saat sedang hamil, {b}Melonia{/b}..."

    anon "... Anda tahu itu."

    show anon f_shy
    melonia "Ya, {b}[firstname]{/b}."

    melonia "Saya menghindari bak mandi air panas; Aku bukan monster!"

    anon a_point "Dan tanpa alkohol?"

    melonia a_fists @ -m_talk "..."
    anon a_idle f_worried @ f_surprised a_surprised_up_both "Oh ya, aku anggap itu sebagai ya..."

    show melonia a_idle with dissolve
    jump melonia_button_pregnant.choice


label melonia_button_pregnant.nauseous:
    anon f_worried "Apakah kamu merasa baik-baik saja?"

    melonia f_annoyed "Tidak, aku merasa tidak enak badan!"

    melonia "Punggungku sakit, aku mual, kakiku bengkak, dan payudaraku bocor ke mana-mana!"

    anon "Itu, um-"

    melonia @ f_pouting "Dan yang terpenting, setiap kali saya bersin, saya buang air kecil sedikit!"

    anon f_surprised @ -m_talk "!!!"
    melonia "Ya."

    melonia "Itu berita gembira kecil yang menarik, bukan?!"

    anon f_worried "Dapatkah saya melakukan sesuatu untuk membuat Anda merasa lebih baik?"

    melonia "Anda bisa saja meninju wajah Anda sendiri, seperti, SANGAT keras."

    anon @ f_hurt -m_talk "..."
    anon "Adakah yang tidak terlalu kejam?"

    melonia "{i}*Huh*{/i} Tidak."

    melonia "Aku hanya ingin anak iblis ini keluar dariku..."

    anon "Anda hampir sampai, tinggal beberapa hari lagi."

    jump melonia_button_pregnant.choice


label melonia_button_pregnant.vain:
    anon f_worried "Apakah kamu merasa baik-baik saja?"

    melonia f_annoyed "Eh, lihat aku..."

    anon "Hah?"

    melonia "Apakah Anda tahu berapa banyak usaha yang diperlukan untuk bangkit kembali setelah saya {b}Iwanka{/b}?"

    anon @ f_thinking "Hmm."

    melonia @ f_yell "Terlalu banyak!"

    melonia "Dan sekarang saya harus mengulanginya lagi, terima kasih!"

    anon "Kamu bersikap konyol."

    anon "Menurutku kamu tampak hebat!"

    melonia @ f_eyeroll "Yah, kamu idiot."

    jump melonia_button_pregnant.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
