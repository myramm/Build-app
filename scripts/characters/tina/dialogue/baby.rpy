label tina_button_baby:
    show anon with dissolve
    tina "Itu benar, kamu adalah keajaiban!"

    tina "Ya, kamu tadi..."

    tina "Ibu memasang implan agar dia tidak hamil, tetapi kamu sangat ingin dilahirkan sehingga itu tidak menjadi masalah!"

    tina "Itu sebabnya Ibu tidak mengeluarkan biaya apa pun, memastikan kamu bisa mendapatkan kehidupan terbaik."


    menu tina_button_baby.choice:
        "Bagaimana kabarnya?":

            jump tina_button_baby.status
        "Aku akan meninggalkanmu.":

            pass

    anon f_normal "Aku akan meninggalkanmu."

    if M_tina.pregnancy.baby_gender == 'boy':
        tina f_normal "Ya, aku harus mengajaknya tidur siang..."

    elif M_tina.pregnancy.baby_gender == 'girl':
        tina f_normal "Ya, aku harus mengajaknya tidur siang..."

    else:
        tina f_normal "Ya, lagipula aku harus mengajak mereka tidur siang..."

    anon "Sampai jumpa lagi, oke?"

    tina f_normal_down @ -m_talk "Mhmm."

    hide anon with dissolve
    return


label tina_button_baby.status:
    anon f_normal "Bagaimana kabarnya?"

    tina f_normal_down @ f_normal "Besar!"

    if M_tina.pregnancy.baby_gender == 'boy':
        tina "Bukankah dia luar biasa, {b}[firstname]{/b}?"

    elif M_tina.pregnancy.baby_gender == 'girl':
        tina "Bukankah dia luar biasa, {b}[firstname]{/b}?"

    else:
        tina "Luar biasa kan, {b}[firstname]{/b}?"

    pause
    tina f_normal "Bagaimana kita bisa seberuntung itu?"

    if M_tina.pregnancy.baby_gender == 'boy':
        anon "Dia berasal dari keluarga yang baik, dari pihak ibunya."

    elif M_tina.pregnancy.baby_gender == 'girl':
        anon "Dia berasal dari keluarga yang baik, dari pihak ibunya."

    else:
        anon "Mereka berasal dari keturunan yang baik, dari pihak ibu mereka."

    tina @ f_laugh "Heh, kamu lebih menyanjung..."

    if M_tina.pregnancy.baby_gender == 'boy':
        tina "... Sisi ayahnya juga tidak terlalu buruk, tahu?"

    elif M_tina.pregnancy.baby_gender == 'girl':
        tina "... Sisi ayahnya juga tidak terlalu buruk, tahu?"

    else:
        tina "... Sisi ayah mereka juga tidak terlalu buruk, tahu?"

    pause
    tina "Kamu telah membuatku menjadi wanita yang sangat bahagia, {b}[firstname]{/b}."

    tina "Saya harap Anda mengetahuinya?"

    anon "Terima kasih, {b}Tina{/b}."

    jump tina_button_baby.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
