label ano18_trap_consuela:
    show consuela:
        xoffset -100
    show anon behind consuela with dissolve:
        flip
        xoffset 100
    pause
    show ricky:
        xoffset -100
    show consuela f_sad a_facepalm:
        flip
        xoffset 200
    with dissolve
    consuela "No, no, no... He has to go!" (show_native="¡No, no, no... El tiene que irse!")
    show consuela a_idle with dissolve
    ricky "Kamu harus pergi, tampan!"

    ricky "Anda benar-benar tidak ingin {b}Mister Rump{/b} menangkap Anda kembali ke sini."

    show anon f_worried
    ricky "Percayalah kepadaku."

    anon "Y-ya, baiklah."

    anon "Tapi aku akan kembali!"

    consuela @ a_point "Pergi!"

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
