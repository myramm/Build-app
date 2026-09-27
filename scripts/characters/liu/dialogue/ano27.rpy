label ano27_lock_liu:
    show anon with dissolve
    liu "Selamat datang di {b}Saga Finansial{/b}."

    liu "Bagaimana saya bisa membantu-"

    liu a_mouth_cover f_surprised "{b}[firstname]{/b}?!"

    anon a_wave "Hai, {b}Liu{/b}."

    show anon a_sides with {'master': dissolve}
    liu a_nervous f_shocked "K-kamu seharusnya tidak berada di sini..."

    liu "... Polisi masih mengintai, menyelidiki perampokan bank."

    anon f_surprised "Oh benar."

    anon f_worried "aku uhh..."


    menu ano27_lock_liu.choice:
        "Hanya ingin memeriksamu.":
            jump ano27_lock_liu.check
        "Saya akan berbicara dengan Anda nanti.":

            pass

    liu f_frightened "Cepat, sebelum mereka kembali!"

    anon "Baiklah."

    anon "Aku akan menemuimu setelah semua ini selesai, aku janji."

    hide anon with dissolve
    return


label ano27_lock_liu.check:
    liu f_frightened "Ya, ya, aku baik-baik saja..."

    liu "... Tapi kamu harus pergi, cepat!"

    liu "Saya tidak bisa membiarkan Anda ditangkap karena akun saya!"

    jump ano27_lock_liu.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
