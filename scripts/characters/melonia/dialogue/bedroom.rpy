label melonia_button_bedroom:
    return

label melonia_button_bedroom.intro0:
    show melonia f_confused
    show anon f_worried with dissolve
    melonia "{b}Hektor{/b}?!"

    melonia "Apa yang kamu lakukan di kamarku?"

    pause
    melonia f_surprised "{i}*Terkesiap*{/i} Apakah kamu masuk ke sini untuk pergi bersamaku?!"

    anon f_surprised "!!!"
    melonia f_smirk "Apakah kamu akan menjebakku?"

    melonia "Merobek semua pakaianku?!"

    show anon f_surprised_teeth
    melonia "Hancurkan aku?!!"

    anon "T-tidak, Bu!"

    melonia f_surprised a_dramatic "Ya ampun, aku benar-benar tidak berdaya!"

    melonia "Apapun yang akan aku-"

    anon "Aku bersumpah, aku hanya ingin bicara!"

    show melonia f_confused
    pause
    melonia a_idle "K-kamu hanya ingin bicara?"

    anon f_worried "Ya!"

    show melonia f_pouting
    pause
    melonia f_annoyed "Uh, baiklah."

    melonia "Lakukan dengan cepat!"

    return


label melonia_button_bedroom.intro1:
    show melonia f_smirk
    show anon f_worried with dissolve
    melonia "Ya ampun, {b}Hector{/b}..."

    melonia @ a_dramatic "Apakah kamu di sini untuk menghancurkanku lagi?"

    show anon f_unimpressed
    pause
    anon "Kupikir kita sudah selesai dengan semua omong kosong \"Hector\" itu?"

    melonia @ f_laugh "Heh, persetan denganku seperti terakhir kali dan aku akan memanggilmu sesukamu."

    return


label melonia_button_bedroom.intro2:
    show melonia b_naked f_smirk
    show anon f_worried_low with dissolve
    melonia "Halo, {b}[firstname]{/b}."

    show melonia b_naked_sexy with dissolve
    melonia "Lihat sesuatu yang kamu suka?"

    return


label melonia_button_bedroom.outro0:
    anon "Saya mungkin harus mulai bekerja."

    melonia f_normal @ a_point "Jangan lupa kenakan seragammu."

    anon "Ya, Bu."

    hide anon with dissolve
    return


label melonia_button_bedroom.outro1:
    jump melonia_button_common.outro1


label melonia_button_bedroom.outro2:
    anon f_normal "Saya harus pergi."

    melonia f_pouting "Sudah apa?"

    anon "Ya, aku khawatir begitu."

    show melonia b_naked a_idle f_annoyed with dissolve
    melonia "Tapi kamu bahkan belum meniduriku!"

    anon f_surprised_teeth @ f_worried a_wave "Maaf, mungkin nanti."

    hide anon with dissolve
    melonia "{b}[firstname]{/b}!!"

    melonia "Jangan pergi!"

    pause
    hide melonia with dissolve
    melonia "Kembali ke sini dan persetan denganku sekarang juga!"

    return 'escape'


label melonia_button_bedroom.dirty:
    if _return == 'cumshot':
        show melonia o_cumshot

    with fade
    melonia "Mmm, itu luar biasa!"

    show anon a_sides b_dressed f_unimpressed_low
    with {'master': dissolve}
    melonia "Terima kasih, {b}[firstname]{/b}."

    anon "Eh ya."

    melonia "Uangmu ada di meja samping tempat tidur."

    anon "Ya, bagus."

    hide anon
    with {'master': dissolve}
    melonia "Ambilkan aku handuk, ya?"

    anon "Ambil sendiri."

    show melonia b_onbed_naked_belly_turn f_surprised
    with {'master': dissolve}
    melonia "Permisi?!"

    anon "Anda mendengar saya!"

    melonia f_smirk_lipbite @ -m_talk "Hmm!"

    pause
    show melonia b_onbed_naked_back f_normal
    with {'master': dissolve}
    melonia "Persetan."

    return 'afterglow'


label melonia_button_bedroom.guards:
    anon f_worried "Bisakah kamu membantu para penjaga?"

    melonia f_normal "Apakah Anda ingin saya mengirim penjaga pergi malam ini?"

    anon f_worried "Tidak, saya masih belum memiliki kode untuk melewati pintu itu."

    melonia "Yah, aku tidak bisa membantumu di sana."

    melonia "Itu kode suamiku, aku tidak mengetahuinya."

    anon "Apakah ada orang lain yang mengetahuinya?"

    melonia "Putri kami kadang-kadang membantunya dalam pekerjaannya..."

    melonia "... Dia mungkin telah memberitahukan kodenya padanya."

    anon "{b}Iwanka{/b}?"

    melonia @ -m_talk "Mhmm."

    anon f_normal "Menarik."

    anon f_thinking @ -m_talk "( {b}Iwanka{/b} mungkin akan memberiku kode jika aku membantunya. )"

    anon @ -m_talk "(Saya harus berbicara dengannya.)"

    jump melonia_button_common.choice


label melonia_button_bedroom.sex:
    melonia "Ya?"

    anon f_flirt @ -m_talk "Hmm?"

    melonia f_annoyed b_naked a_idle "Apakah kamu akan membuka pakaian?"

    anon "Oh benar."

    show melonia f_smirk_low
    show anon b_dressed_changing3 with dissolve
    pause
    show anon b_dressed_changing2 with dissolve
    pause
    show anon b_naked_undress_bottom with dissolve
    pause
    show anon b_naked f_flirt_low a_sides od_naked_dick1 with dissolve
    melonia f_smirk "Bagus sekali!"

    hide anon
    show melonia b_naked_kiss
    with dissolve
    melonia "Aku ingin ayam besar itu ada di dalam diriku sekarang juga!"


    if venue == 'bedroom':
        scene location_rump_bedroom_bed_closeup as stage

    show anon b_onbed_naked_falling od_empty behind melonia:
        flip
        xoffset -200
    show melonia b_naked_push

    if venue == 'bedroom':
        with fastfade
    else:
        with fastdissolve

    anon "A-wah!"

    show anon b_onbed_naked f_surprised -od_empty with {'master': dissolve}:
        flip
        offset (-240, -20)
    melonia @ f_laugh "hehe!"

    show melonia b_naked_back_climb with dissolve:
        flip
        xoffset -200
    melonia "Mmm, berikan padaku {b}[firstname]{/b}!"


    call scene_melonia_sex.repeat
    $ unlock_scene('melonia', '01_unlocked', variant='repeat')

    scene location_rump_bedroom_bed_closeup as stage
    show melonia b_onbed_naked_back
    show anon b_dressed_changing:
        xoffset -50

    if _return == 'blowjob':
        jump melonia_button_bedroom.shock

    if _return in ('creampie', 'cumshot'):
        jump melonia_button_bedroom.dirty

    with fade
    pause
    show anon a_sides b_dressed f_shy_low
    with {'master': dissolve}
    anon "Apakah Anda membutuhkan yang lain, Bu?"

    melonia @ -m_talk "Hmm?"

    melonia "Oh, tidak... Terima kasih, tapi... Aku hanya ingin berbaring di sini sebentar."

    anon "Baiklah."

    melonia "Kamu luar biasa seperti biasanya, {b}[firstname]{/b}."

    melonia "Ada uang di meja samping tempat tidur untukmu."

    anon @ f_laugh a_cheering "Luar biasa, terima kasih!"

    hide anon with dissolve
    melonia @ -m_talk "Mhmm."

    return 'afterglow'


label melonia_button_bedroom.shock:
    if _return == 'blowjob':
        show melonia o_cumface

    with fade
    pause
    show anon a_sides b_dressed f_happy_low
    with {'master': dissolve}
    anon "Nah, itu menyenangkan!"

    melonia "{i}*Mengerang*{/i}"

    anon f_worried_low "Uhh, kamu baik-baik saja?"

    melonia "Hmm..."

    melonia @ -m_talk "{i}*Meneguk*{/i}"

    anon "{b}Melonia{/b}?"

    melonia @ -m_talk "Mhmm?"

    anon "Kamu baik-baik saja?"

    melonia "Menurutku itu sangat menyenangkan."

    anon f_flirt_low "Heh, kamu dan aku sama-sama."

    anon "Uang di meja samping tempat tidur?"

    melonia @ -m_talk "Mhmm."

    show anon a_wave
    with {'master': dissolve}
    anon "Sampai jumpa lagi."

    hide anon
    with {'master': dissolve}
    melonia @ -m_talk "..."
    return 'afterglow'


label melonia_button_bedroom.suggest:
    anon f_flirt "Ingin berhubungan seks?"

    melonia f_smirk "Mmm, kamu membaca pikiranku."


    if not M_melonia.outfit.is_naked:
        show anon f_flirt_low
        show melonia a_undress1 f_smirk_down
        with dissolve
        pause
        show melonia b_dressed_undress2 with dissolve
        pause
        show melonia b_dressed_undress3 with dissolve
        pause
        show melonia b_undies a_undress4 with dissolve
        pause
        show melonia b_dressed_undress5 with dissolve
        pause
        show melonia b_dressed_undress6 with dissolve
        show melonia b_dressed_undress7 with dissolve
        pause
        show melonia b_naked a_pull_panties f_smirk with dissolve
        pause
        show melonia b_swimsuit_bottom_remove2 with dissolve
        pause
        show melonia b_naked_sexy f_smirk with dissolve

    pause
    jump melonia_button_bedroom.sex
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
