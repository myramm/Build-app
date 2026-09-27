label melonia_button_hottub:
    return

label melonia_button_hottub.intro0:
    show anon f_worried_low with dissolve
    anon "Permisi, {b}Ny. Bokong{/b}?"

    melonia "Apa?"

    anon "Boleh saya bertanya sesuatu?"

    melonia @ f_annoyed_up "Ugh, baiklah, tapi cepatlah!"

    melonia "Saya mencoba bersantai di sini, {b}Hector{/b}."

    return


label melonia_button_hottub.intro1:
    show anon f_worried_low with dissolve
    anon "Permisi, {b}Ny. Bokong{/b}?"

    melonia "Apa?"

    anon "Boleh saya bertanya sesuatu?"

    melonia "Itu tergantung..."

    melonia @ f_smirk_peek "... Apakah kamu akan menghiburku hari ini?"

    anon @ f_skeptical "Menghibur Anda?"

    melonia f_smirk_up "Menarilah untukku, {b}Hector{/b}."

    show anon f_unimpressed
    pause
    anon "Kupikir kita sudah selesai dengan semua omong kosong \"Hector\" itu?"

    melonia f_smirk_up "Heh, menarilah untukku dan aku akan memanggilmu sesukamu."

    return


label melonia_button_hottub.intro2:
    show anon f_worried_low
    anon "Selamat siang, Bu."

    melonia "Tolong, {b}[firstname]{/b}..."

    melonia "... Hubungi saya {b}Melonia{/b}."

    anon "Baiklah."

    return


label melonia_button_hottub.outro0:
    jump melonia_button_common.outro0


label melonia_button_hottub.outro1:
    jump melonia_button_common.outro1


label melonia_button_hottub.outro2:
    anon f_worried_low "Saya harus pergi."

    melonia f_pouting_up "Sudah apa?"

    anon "Ya, aku khawatir begitu."

    melonia f_annoyed_up "Tapi kamu bahkan belum meniduriku!"

    anon "Maaf, mungkin nanti."

    hide anon with dissolve
    melonia "{b}[firstname]{/b}!!"

    show melonia b_jacuzzi_topless_edge f_annoyed with dissolve
    melonia "Jangan pergi!"

    pause
    melonia f_yell "Kembali ke sini dan persetan denganku sekarang juga!"

    return


label melonia_button_hottub.dance:
    if level == 1:
        anon f_worried_low "Baiklah, aku akan menari."

        melonia f_smirk_up "Anak baik."

    else:
        anon f_shy_low "Haruskah aku menari untukmu?"

        melonia f_smirk_up "Oh ya!"

        melonia f_laugh a_clap "Saya bisa melakukan beberapa hiburan."

    show melonia f_smirk_lipbite a_idle
    show anon b_dressed_changing3
    with dissolve
    pause
    show anon b_dressed_changing2 with dissolve
    pause
    show anon b_naked_undress_bottom with dissolve
    pause
    melonia f_smirk "Itu sempurna, di sana."

    show anon b_naked a_empty f_worried_low od_naked_dick1
    show anon_arms_naked_a_cover
    with {'master': dissolve}
    anon @ -m_talk "Hmm?"

    anon "Apakah kamu tidak ingin aku mengenakan seragamku untuk ini?"

    melonia "Tidak, aku ingin kamu seperti itu."

    show anon f_worried_left
    pause
    anon f_worried_low "Bagaimana jika seseorang melihatku?"

    melonia f_smirk_up "Hanya {b}Ricky{/b} dan saya di sini."

    melonia "Lagipula, apa yang membuatmu malu?"

    anon @ f_worried_left -m_talk "..."
    anon "Baiklah baiklah."

    anon "Apa pun."

    melonia @ f_laugh "Hehe, menyenangkan!"

    melonia f_smirk "Anda bisa memulai."

    anon "Ehh."

    hide anon_arms_naked_a_cover
    show anon b_naked_spin_frown_down od_empty:
        xoffset 150
    with dissolve
    pause
    show anon b_naked_spin_worried_low_talk with dissolve
    anon "Seperti ini?"

    show anon b_naked_spin_worried_low
    melonia @ -m_talk "Mhmm."

    pause
    show ricky f_smirk_low behind anon with dissolve:
        flip
        xoffset -200
    pause
    melonia "Datang untuk menikmati pertunjukannya, {b}Ricky{/b}?"

    show anon b_naked_spin_frown_down
    ricky "Ya, señora."

    ricky @ f_laugh "Tampilannya cukup mengesankan, amigo!"

    show anon b_naked_spin_frown_down_talk
    anon "Dia?"

    show anon b_naked_spin_frown_down
    pause
    ricky @ f_laugh "Itu seperti helikopter!"

    melonia "Hehe, kamu benar!"

    pause
    melonia "Anda pikir dia mungkin terbang?"

    ricky "Anda pernah melihat polisi memutar tongkat billy?"

    melonia @ f_laugh "{i}*Mendengus*{/i} Tidak."

    ricky a_finger_tub "Ini terlihat seperti ini..."

    pause
    ricky a_idle @ a_finger "Ini memberi saya kilas balik ke El Salvador!"

    melonia "Tenang saja, aku tidak akan membiarkan dia menyakitimu."

    ricky "Ada cara yang lebih buruk untuk dilakukan, señora..."

    melonia @ f_laugh "Haha!"

    show anon b_naked od_naked_dick1 a_idle f_frown_down with dissolve
    anon "Kau tahu, ini cukup canggung tanpa adanya bolak-balik dari kalian berdua..."

    melonia f_smirk_up "Aduh, malangnya {b}Hector{/b}..."

    melonia @ f_laugh "Kamu telah mempermalukannya, {b}Ricky{/b}!"

    ricky @ a_up f_smirk "Maaf, teman-teman."

    show anon b_naked_undress_bottom od_empty with dissolve
    pause
    show anon b_dressed_changing2 with dissolve
    anon "Saya pikir itu cukup untuk hari ini."

    show anon b_dressed_changing with dissolve
    melonia "Huuu!!"

    show anon b_dressed f_unimpressed a_sides with dissolve
    melonia @ f_laugh a_clap "Ulangi, ulangi!"

    ricky f_smirk "Yah, itu bagus selagi masih ada."

    ricky @ a_finger "Kurasa, aku akan kembali ke taman..."

    melonia f_pouting "Aduh, ayo teman-teman!"

    hide ricky with dissolve
    melonia "Segalanya menjadi baik!"

    hide anon with dissolve
    pause
    if M_melonia.outfit.is_naked:
        show melonia b_jacuzzi_topless_edge with dissolve
    else:
        show melonia b_jacuzzi_edge with dissolve
    melonia "Teman-teman?!"

    melonia "Jangan tinggalkan..."

    pause
    if M_melonia.outfit.is_naked:
        show melonia b_jacuzzi_topless f_annoyed with dissolve
    else:
        show melonia b_jacuzzi f_annoyed with dissolve
    melonia "Grr!"

    return 'dance'


label melonia_button_hottub.suggest:
    anon f_flirt_low "Ingin berhubungan seks?"

    melonia f_smirk_up "Mmm, kamu membaca pikiranku."

    melonia "Ayo pergi ke kamarku."


    if M_melonia.outfit.is_naked:
        show melonia b_jacuzzi_climb_naked:
            flip
    else:
        show melonia b_jacuzzi_climb:
            flip

    show location_rump_backyard_jacuzzi_overlay as hottub behind melonia
    with dissolve
    pause
    show layer master:
        ease 1.6 xpos 485
    with None

    if M_melonia.outfit.is_naked:
        show melonia b_naked_pulling_anon f_smirk:
            flip
            offset (-960, 0)
    else:
        show melonia b_swimsuit_hatless_pulling_anon o_pulling_anon_hat f_smirk:
            flip
            offset (-960, 0)

    show anon b_empty f_flirt o_melonia_pulling:
        flip
        xoffset -530
    with dissolve
    anon "Ya, Bu."


    scene location_rump_bedroom_bed_closeup

    if M_melonia.outfit.is_naked:
        show melonia f_smirk b_naked
        show anon f_flirt_low
    else:
        show melonia f_smirk b_swimsuit_hatless a_hips_no_shall
        show anon f_flirt

    with fade
    melonia "Saya sangat senang suami saya mempekerjakan Anda!"


    if not M_melonia.outfit.is_naked:
        show anon f_flirt_low
        show melonia a_remove1 f_smirk_down
        with dissolve
        pause
        show melonia b_swimsuit_remove2 with dissolve
        pause
        show melonia b_swimsuit_remove3 with dissolve
        show melonia b_swimsuit_remove4 with dissolve
        pause
        show melonia b_swimsuit_bottom a_idle with dissolve
        pause
        show melonia b_swimsuit_bottom a_remove_bottom1 with dissolve
        pause
        show melonia b_swimsuit_bottom_remove2 with dissolve
        pause
        show melonia b_naked_sexy f_smirk with dissolve

    pause
    jump melonia_button_bedroom.sex
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
