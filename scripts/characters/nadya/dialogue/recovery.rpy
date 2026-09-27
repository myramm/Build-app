label nadya_button_recovery:
    show anon f_worried with dissolve
    nadya f_sleep @ -m_talk "..."
    anon f_confused "Apakah dia sedang tidur?"

    show svetlana:
        xoffset -100
        xzoom 1
    with {'master': dissolve}
    svetlana "Ya."

    anon f_normal "Bagus, dia bisa memanfaatkan waktu istirahatnya."

    anon "Aku tahu kalian, gadis-gadis Rusia itu tangguh, tapi tidak apa-apa untuk sesekali menjadi rentan."

    pause
    svetlana f_happy "Anda pasangan yang cocok untuk {b}Nona Chernyshevksy{/b} Saya pikir..."

    anon f_surprised "Oh?"

    svetlana "... Baguslah dia memilihmu."

    show anon f_shy
    show svetlana f_happy_down
    pause
    svetlana "Dan Anda menghasilkan bayi yang cantik bersama-sama."

    anon f_shy_low "Heh, ya... kami benar-benar melakukannya."

    pause
    show anon f_shy

    if M_nadya.pregnancy.baby_gender == 'boy':
        anon "Kamu baik-baik saja mengawasinya?"

    else:
        anon "Anda baik-baik saja mengawasinya?"


    svetlana f_happy "Ya, aku menonton."

    anon "Terima kasih, {b}Svet{/b}."

    svetlana "Tidak masalah."

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
