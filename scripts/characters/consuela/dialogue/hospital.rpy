label consuela_button_hospital:
    if not M_consuela.finished_state(S_con03_door):
        jump consuela_button_hospital.debt

    show anon with dissolve
    if M_consuela.finished_state(S_con03_done):
        consuela "Buenas noches, ayah."

    else:
        consuela "Buenas noches, {b}Tuan [firstname]{/b}."

    anon @ a_wave "Halo, {b}Consuela{/b}."


    menu consuela_button_hospital.choice:
        "Bekerja keras?":
            jump consuela_button_hospital.working

        "Kerja sendiri?" if M_consuela.pregnancy.stage > 4:
            jump consuela_button_hospital.alone
        "Saya harus pergi.":

            pass

    anon "Sampai jumpa di tempatku nanti, ya?"

    consuela "Ya, tempatmu."

    consuela "aku melakukannya untukmu."

    consuela "Anda berkata, saya bersedia."

    anon @ a_wave "Sampai jumpa, {b}Consuela{/b}."

    consuela "Adiós, {b}Tuan [firstname]{/b}."

    hide anon with dissolve
    return

label consuela_button_hospital.working:
    anon "Bekerja keras?"

    consuela "Oh ya {b}Pak [firstname]{/b}."

    consuela "Saya bekerja keras."

    consuela "Bersih bagus."

    anon "Yah, saya yakin semua orang di sini menghargainya."

    anon "Dan itu pasti lebih baik daripada bekerja untuk {b}Walikota Rump{/b}, bukan?"

    consuela "Ya ampun!"

    consuela f_annoyed "{b}Walikota Rump{/b}, orang jahat."

    consuela "Aku tidak melakukan apa pun untuknya!"

    consuela "Dia bertanya tapi aku tidak melakukannya."

    show consuela f_normal
    jump consuela_button_hospital.choice

label consuela_button_hospital.alone:
    if M_consuela.pregnancy.baby_gender == 'twins':
        anon "Tidak ada anak kecil hari ini?"

    else:
        anon "Tidak ada anak kecil hari ini?"

    consuela f_sad @ -m_talk "Hmm?"

    if M_consuela.pregnancy.baby_gender == 'twins':
        anon "Dimana bayinya?"

    else:
        anon "Dimana bayinya?"

    consuela f_normal "Oh, {b}Camila{/b} tonton."

    anon f_worried "Putri Anda sedang mengasuh anak?"

    consuela "Ya, mengasuh anak."

    consuela "The old lady at reception told me I can't bring children to work." (show_native="La anciana de recepción me dijo que no puedo traer niños al trabajo.")
    anon f_skeptical "Apakah dia pengasuh yang baik?"

    consuela "Oh ya."

    consuela "{b}Camila{/b} kakak yang baik."

    show anon f_normal
    consuela @ f_laugh "Banyak cinta."

    anon "Saya pasti ingin melihatnya!"

    jump consuela_button_hospital.choice

label consuela_button_hospital.debt:
    show anon with dissolve
    anon "Hai {b}Consuela{/b}."

    anon "Apa kabarmu?"

    consuela "Oh, baiklah, {b}Pak [firstname]{/b}."

    consuela "Anda menemukan pekerjaan."

    consuela "Orang baik."

    consuela "aku melakukannya untukmu sekarang?"

    anon @ -m_talk "Hmm?"

    consuela "aku melakukannya untukmu?"

    anon "Tidak, tidak, kamu tidak perlu melakukan apa pun untukku..."

    consuela "Ya, aku melakukannya untukmu!"

    consuela "Anda berkata, saya bersedia."

    anon "Hehe, jangan khawatir tentang itu."

    anon "Aku baik-baik saja."

    consuela @ f_eyeroll "Ck."

    consuela "There must be something I can do for you?" (show_native="Debe haber algo que pueda hacer por ti?")

    menu:
        "Saya harus pergi.":
            pass

    anon "Saya akan membiarkan Anda kembali melakukannya."

    consuela "Tunggu, {b}Pak [firstname]{/b}..."

    consuela "Aku melakukannya untukmu, oke?"

    consuela "Kamu orang baik."

    anon "Hehe, baiklah... Baiklah."

    anon "Jika aku memikirkan sesuatu, aku akan memberitahumu, oke?"

    consuela "Ya."

    consuela "Anda berkata, saya bersedia."

    anon @ a_wave "Sampai jumpa, {b}Consuela{/b}."

    consuela "Adiós, {b}Tuan [firstname]{/b}."

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
