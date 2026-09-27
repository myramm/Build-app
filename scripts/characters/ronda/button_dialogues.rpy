label ronda_dialogue_intro:
    scene gym
    show ronda b_jersey
    show anon a_wave
    with dissolve
    anon "Hai, {b}Ronda{/b}. Apa kabarmu?"

    show anon a_idle with dissolve
    ronda "Saya baik-baik saja. Pertanyaannya, apakah Anda sudah berlatih?"

    anon f_worried_low @ -m_talk "..."
    anon "Tidak-"

    show anon f_worried
    ronda f_upset @ f_upset_angry "Lalu berhenti menggerakkan bibir itu dan mulailah menggerakkan... Kaki itu!"

    anon f_skeptical @ -m_talk "???"
    ronda f_normal "Sudahlah. Itu hanya sesuatu yang selalu ayahku katakan..."

    show anon f_worried
    ronda "Pokoknya, sebaiknya kamu bergegas karena ujiannya akan segera tiba!"

    return

label ronda_dialogue_talent_show_help:
    anon f_worried "Saya kira Anda tidak tertarik menjadi sukarelawan untuk pertunjukan bakat musik {b}Miss Dewitt{/b}?"

    show ronda b_jersey f_normal
    ronda "Bakat musik? Tidak, saya tidak akan tertarik."

    anon "Apa kamu yakin? Anda tidak memainkan alat musik atau bernyanyi sama sekali?"

    ronda "Umm, tidak bisakah kamu melihat ada hal lain yang lebih penting untuk aku fokuskan. Seperti lari dan berenang..."

    ronda "Hal-hal yang harus Anda fokuskan juga!"

    ronda "Anda tidak akan pernah masuk tim jika Anda terus mengabaikan pelatihan Anda!"

    anon @ f_skeptical "Tahukah Anda, hidup ini lebih dari sekadar olahraga, {b}Ronda{/b}..."

    ronda "Pfft, ya benar."

    return

label ronda_dialogue_model_help:
    show ronda b_jersey f_normal
    anon f_normal "Saya sedang mengerjakan proyek untuk {b}Miss Ross{/b} dan itu memerlukan model langsung."

    anon @ a_point "Apakah Anda tertarik?"

    ronda "Sibuk."

    anon f_worried "Sibuk?"

    anon "Melakukan apa?"

    show ronda
    ronda f_upset_angry "Sungguh, {b}[firstname]{/b}?!"

    ronda "Saya harus berlari sejauh 6 mil dan mandi es sebelum latihan sepak bola."

    show ronda f_upset
    anon f_surprised @ f_worried_low "Uhh..."

    ronda @ f_upset_angry "Setelah itu, saya hanya punya waktu 40 menit untuk menyelesaikan beberapa putaran sebelum kolam ditutup."

    anon "Itu jelek-"

    show anon f_surprised_teeth
    ronda @ f_upset_angry "Kemudian kembali ke rumah ke bantal pemanas dan crunch."

    anon f_worried "OKE! Oke! Saya mengerti..."

    hide ronda with dissolve
    anon f_surprised "Gadis itu gila!"

    return

label ronda_dialogue_leave:
    show anon
    anon "Baiklah."

    anon @ a_wave "Sampai jumpa lagi."

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
