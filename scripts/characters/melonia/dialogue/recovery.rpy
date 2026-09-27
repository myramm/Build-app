label melonia_button_recovery:
    show anon f_worried with dissolve
    melonia "Anda kembali!"

    show anon with dissolve:
        xoffset 200
    anon "Ya, aku hanya ingin memeriksa dan memastikan kalian berdua baik-baik saja."

    melonia a_baby_give "Di Sini!"

    anon "Tunggu sebentar, aku-"

    show anon a_melonia_baby
    show melonia a_crossed
    with dissolve
    anon "{b}Melonia{/b}, aku tidak bisa tinggal."

    melonia "Terlambat!"

    show melonia b_gown_bed_back with dissolve
    pause
    anon f_sad_down "Aduh, bung..."

    pause
    show anon f_frown_down
    anon "Ayahmu langsung melakukan hal itu, bukan, Nak?"

    anon f_shy_down "Ya, benar."

    if M_melonia.pregnancy.baby_gender == "boy":
        anon @ f_laugh "Heh, kamu{#male} manis sekali!"

    else:
        anon @ f_laugh "Heh, kamu{#female} manis sekali!"


    scene black with slowdissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
