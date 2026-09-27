label liu_button_recovery:
    show anon with dissolve:
        xoffset 200
    anon "Hei, bagaimana perasaanmu?"

    liu f_nervous "Agak gila karena terjebak di tempat tidur ini tapi selain itu bagus."

    show anon f_confused

    if M_liu.pregnancy.baby_gender == 'boy':
        anon "Adakah perbaikan setelah dia menempel?"

    else:
        anon "Adakah perbaikan setelah dia menempel?"


    show anon f_normal_low
    show liu f_happy_baby

    if M_liu.pregnancy.baby_gender == 'boy':
        liu "Ya, dia juga orang yang rakus."

        liu "Bukankah kamu{#boy}, anak kecil?"

    else:
        liu "Ya, dia juga gadis yang rakus."

        liu "Bukankah kamu{#girl}, anak kecil?"


    anon f_laugh "hehe."

    pause
    show liu f_happy
    anon f_normal "Nah, kalian berdua akan sampai di rumah sebelum kalian menyadarinya."

    anon "Anda harus menikmati istirahat di tempat tidur dan pasukan perawat selagi bisa."

    liu "Ya, Anda mungkin benar tentang itu."

    anon "Hubungi saya jika Anda butuh sesuatu, ya?"

    liu f_happy "Saya akan."

    liu "Terima kasih, {b}[firstname]{/b}."

    show anon a_wave f_happy with dissolve
    pause
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
