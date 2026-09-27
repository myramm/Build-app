label gamsay_button_kitchen:
    show anon f_worried with dissolve:
        xoffset -100
    show gamsay b_dressed f_angry a_pan with dissolve:
        unflip
        xoffset -100
    gamsay "Kenapa kamu ada di dapurku lagi?!"

    anon "Maaf, Koki."

    anon "Aku baru saja lewat, aku bersumpah!"

    gamsay "Kamu pelacur kelas satu, bukan?"

    anon @ f_skeptical "Kamu tidak perlu bersikap kasar, aku hanya-"

    gamsay "Persetan segera, kamu keledai!"

    gamsay "Saya mencoba bekerja di sini!"

    anon @ -m_talk "..."
    hide anon
    show gamsay b_dressed_back:
        flip
        xoffset 450
    with dissolve

    scene expression player.location.background_blur with fade
    show anon f_worried with dissolve
    anon @ -m_talk "(Wah, pria itu psikopat!)"

    hide anon with dissolve
    return


label gam01_gamsay_meet:
    show anon behind gamsay with dissolve:
        xoffset -100
    anon "Permisi, Pak?"

    gamsay @ -m_talk "..."
    anon "Apakah kamu bekerja di sini?"

    gamsay "Tidak, saya hanya suka memakai pakaian ini dan memanggang kue di dapur panas walikota untuk bersenang-senang..."

    anon f_worried "Hah?"

    gamsay "Tinggalkan aku sendiri nak, aku sibuk!"

    pause
    anon "Aku hanya berharap kamu bisa memberitahuku di mana-"

    show gamsay b_dressed a_pan with {'master': fastdissolve}:
        unflip
        xoffset 0
    gamsay "Apakah kamu tuli?"

    anon "T-tidak."

    gamsay "Tidak bisakah kamu melihat aku mencoba fokus di sini?"

    anon "Maafkan aku, aku-"

    show gamsay f_angry_down a_pan_show
    show anon f_surprised_down
    with {'master': fastdissolve}
    gamsay "Lihat ayam ini."

    anon f_worried "Apa?"

    show anon f_surprised_down
    gamsay f_angry "LIHAT ITU!"

    gamsay "Ini benar-benar MENTAH!!!"

    anon f_worried @ -m_talk "..."
    gamsay "Dan tahukah Anda mengapa itu mentah?"

    anon "Tidak?"

    gamsay "Karena kamu menggangguku!"

    anon "Bagaimana aku mengalihkan perhatian-"

    gamsay a_idle @ a_pan_throw "Ini adalah sampah sekarang!"

    anon f_surprised "!!!"
    gamsay "Anda telah menyia-nyiakannya sepenuhnya!"

    anon f_worried "Aku akan pergi saja."

    gamsay "Oh, tidak... Maukah kamu tinggal di sini?!"

    hide anon with dissolve
    gamsay "Akan sangat disayangkan jika Anda tidak ada di sini untuk mengacaukan hidangan saya berikutnya juga!"

    show gamsay b_dressed_back with dissolve:
        flip
        xoffset 450
    pause
    gamsay "Sandwich bodoh sialan, orang itu..."

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
