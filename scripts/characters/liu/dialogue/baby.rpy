label liu_button_baby:
    show anon with dissolve
    anon "Hei, bagaimana kabarmu?"

    liu f_happy "Hai, {b}[firstname]{/b}."

    liu f_happy_baby "Bukankah bayi kita luar biasa?"

    show anon f_shy_low

    menu liu_button_baby.choice:
        "Terbaik.":

            jump liu_button_baby.best
        "Bagaimana perasaanmu?":

            jump liu_button_baby.feeling
        "Saya akan membiarkan Anda kembali melakukannya.":

            pass

    show liu f_happy
    anon f_normal "Saya akan membiarkan Anda kembali melakukannya."

    liu f_happy_baby "Ucapkan selamat tinggal pada Ayah."

    anon f_shy_low "Heh, selamat tinggal si kecil."

    show anon a_wave
    with {'master': dissolve}
    anon "Jaga ibumu untukku."

    hide anon with dissolve
    return


label liu_button_baby.best:
    anon @ f_happy "Terbaik!"


    if M_liu.pregnancy.baby_gender == 'boy':
        liu "Dia tidak rewel sama sekali!"

    else:
        liu "Dia tidak rewel sama sekali!"


    show liu f_happy
    anon f_confused "Tidur sepanjang malam oke?"

    show anon f_normal
    liu "Ya, sejauh ini."

    anon "Itu bagus."

    anon "Semoga terus berlanjut."

    liu "Itu akan."

    liu "Saya tahu itu akan terjadi."

    show anon f_shy_low
    show liu f_happy_baby

    if M_liu.pregnancy.baby_gender == 'boy':
        liu "Dia sempurna."

    else:
        liu "Dia sempurna."


    jump liu_button_baby.choice


label liu_button_baby.feeling:
    show liu f_normal
    anon f_confused "Menikmati waktu istirahat Anda?"

    show anon f_normal
    liu f_worried "Ya, kenapa?"

    liu "Apakah semuanya baik-baik saja di bank?!"

    anon f_surprised "Hah?!"

    anon f_worried "Y-ya semuanya baik-baik saja."

    liu "Anda telah memeriksa {b}Tina{/b} dan menemaninya seperti yang saya minta, bukan?"

    anon f_normal "Ya, tentu saja."

    liu f_ashamed_down "Saya serius, {b}[firstname]{/b}."

    liu f_worried "Anda tidak tahu betapa sepinya saat Anda berada di sana sendirian."

    anon "Heh, aku akan menghabiskan waktu bersama {b}Tina{/b}, aku janji."

    liu f_normal "Hmm, oke."

    liu f_happy_baby "Kita akan baik-baik saja di sini, kan, si kecil?"

    show anon f_shy_low
    liu "Ya, kami akan melakukannya."

    jump liu_button_baby.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
