label ano05_cell_sato:
    return


label ano05_cell_sato.fail:
    show anon a_point f_surprised with {'master': fastdissolve}
    anon "Lihat! Monyet berkepala tiga!"

    show sato:
        flip
        xoffset 520
    show anon b_dressed_bending_phone
    with dissolve
    sato "Seekor burung berkepala tiga"

    $ display.toast(dex_fail)
    show sato f_confused with hpunch:
        unflip
        xoffset 0
    sato f_angry @ f_confused "Hei, jangan sentuh itu!"

    show anon f_surprised_low a_surprised_up_both b_dressed with dissolve
    show sato f_normal
    anon a_behind_head f_sad_down "Oh, ehh... Maaf."

    sato "Itu telepon putriku."

    sato f_confused "Dia tidak mengirimmu ke sini untuk mengambilnya, kan?"

    anon f_worried "T-tidak, Pak."

    anon "Aku hanya penasaran kenapa pria sepertimu punya telepon feminin di mejanya."

    sato f_normal "Dia sepertinya tidak bisa melepaskan diri darinya selama jam kerja, jadi saya harus menyitanya."

    anon "Mengerti."

    sato "Saya akan mengembalikannya setelah dia melakukan penjualan pertamanya."

    hide anon with dissolve
    return


label ano05_cell_sato.pass:
    anon @ a_point "Itu pedang yang sangat rapi yang kamu miliki di atas sana!"

    show sato with dissolve:
        flip
        xoffset 520
    sato @ -m_talk "Hmm?"

    show anon b_dressed_bending_phone with dissolve
    pause .5
    show anon f_grin a_phone_josephine_give b_dressed
    hide phone
    with dissolve
    $ display.toast(dex_pass)
    anon @ -m_talk "(Aku akan mengambilnya.)"

    show anon f_shy_down a_idle with dissolve
    pause
    show anon f_grin
    sato "Oh ya!"

    show sato f_smiling:
        unflip
        xoffset -30
    show anon f_normal
    with dissolve
    sato "Percayakah Anda saya memenangkan karnaval itu?"

    anon f_surprised "Benar-benar?"

    sato "Ya memang."

    sato "Menghabiskan hampir empat puluh dolar pada undian kuarter, namun {b}Josephine{/b} bersikeras agar saya memenangkannya untuknya."

    anon "Apakah itu nyata?"

    sato "Ya, itu hanya replika."

    anon f_unimpressed "Oh."

    sato "Tapi ada tanda tangan Hattori Hanzō di sana!"

    anon f_confused "Hattori Hanzo?"

    anon "Siapa itu?"

    sato "Tidak tahu, sungguh..."

    sato "... Tapi aku curiga dia adalah seseorang yang menandatangani pedang."

    pause
    anon f_normal "Benar."

    anon @ a_wave "Baiklah, lanjutkan saja."

    hide anon with dissolve

    $ player.go_to(L_dealership_showroom)
    scene expression player.location.background_blur with fade
    show anon f_grin with dissolve
    anon @ -m_talk "(Baiklah, itu tidak terlalu sulit.)"

    anon @ -m_talk "(Saya harus mengembalikan ponsel ini ke {b}Josephine{/b} sekarang. )"

    hide anon with dissolve
    return 'josie_phone'
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
