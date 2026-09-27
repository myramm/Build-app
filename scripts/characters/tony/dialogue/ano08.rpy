label ano08_late_tony:
    show tony f_suspicious
    show anon with dissolve
    tony "Kamu {b}mengeluarkan tepung itu dari belakang{/b} untuk {b}Maria{/b}?"

    anon "Belum."

    tony "Yah, itu harus dilakukan besok sekarang."

    tony "Jangan mengecewakannya, jagoan."

    anon @ f_grin a_salute "Ya, tuan."

    hide anon with dissolve
    return


label ano08_sack_tony:
    show tony f_suspicious
    show anon with dissolve:
        flip
    tony "Kamu {b}mengeluarkan tepung itu dari belakang{/b} untuk {b}Maria{/b}?"

    anon "Belum."

    tony @ a_frustrated "Baiklah, kamu harus melakukannya, jagoan!"

    tony "Dia di sana menunggu."

    anon @ f_grin a_salute "Ya, tuan."

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
