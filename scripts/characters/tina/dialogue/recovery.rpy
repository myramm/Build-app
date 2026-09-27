label tina_button_recovery:
    show anon with dissolve
    if M_tina.pregnancy.baby_gender == 'twins':
        anon "Hei, kalian bertiga."

    else:
        anon "Hei, kalian berdua."

    tina @ f_normal "Halo, {b}[firstname]{/b}."

    tina "Anda datang untuk memeriksa kami lagi?"


    menu tina_button_recovery.choice:
        "Ya.":
            pass

    anon "Ya, bagaimana kabar kalian?"

    tina @ f_laugh "Kami baik-baik saja!"

    if M_tina.pregnancy.baby_gender == 'boy':
        tina "Anda harus melihat berapa banyak yang dimakan si kecil kita!"

    elif M_tina.pregnancy.baby_gender == 'girl':
        tina "Anda harus melihat berapa banyak gadis kecil kami makan!"

    else:
        tina "Anda harus melihat berapa banyak yang dimakan anak kecil kita!"

    tina f_normal "Spesialis laktasi itu benar-benar akan membuahkan hasil!"

    anon "Ya, itu bagus."

    pause
    anon "Apakah ada yang bisa saya lakukan?"

    tina f_normal_down @ f_laugh "Hmm, bukan itu yang terpikirkan olehku..."

    anon f_sad_down @ -m_talk "..."
    tina "Kami akan segera pulang dan kamu bisa datang berkunjung, oke?"

    anon "Ya baiklah."

    tina "Terima kasih, {b}[firstname]{/b}."

    if M_tina.pregnancy.baby_gender == 'twins':
        anon "Kurasa, sampai jumpa nanti."

    else:
        anon "Kurasa, sampai jumpa lagi nanti."

    tina @ -m_talk "Mhmm."

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
