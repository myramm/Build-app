label melonia_button_garden:
    return


label melonia_button_garden.intro0:
    show anon f_worried with dissolve
    anon "Permisi, {b}Ny. Bokong{/b}?"

    melonia f_annoyed "Apakah Anda sudah selesai membersihkan bak mandi air panas?"

    anon "Tidak, Bu."

    melonia @ f_eyeroll "Ugh, lalu apa yang kamu inginkan?"

    return


label melonia_button_garden.intro1:
    show anon f_worried with dissolve
    melonia "Apakah Anda sudah selesai membersihkan bak mandi air panas?"

    anon "Tidak, Bu."

    show melonia f_annoyed
    pause
    melonia "Anda tahu, {b}Hector{/b}..."

    melonia "Hanya karena saya membayar Anda untuk seks sekarang, bukan berarti Anda bisa mengabaikan tanggung jawab Anda yang lain."

    show anon f_unimpressed
    pause
    anon "Kupikir kita sudah selesai dengan semua omong kosong \"Hector\" itu?"

    melonia f_smirk "Heh, jaga kebersihan bak mandi air panas ini dan aku akan meneleponmu sesukamu."

    return


label melonia_button_garden.outro0:
    jump melonia_button_common.outro0


label melonia_button_garden.outro1:
    jump melonia_button_common.outro1


label melonia_button_garden.suggest:
    anon f_flirt "Ingin berhubungan seks?"

    melonia f_smirk "Mmm, kamu membaca pikiranku."

    melonia "Ayo pergi ke kamarku."

    show layer master:
        ease 1.6 xpos 485
    with None
    show melonia b_swimsuit_pulling_anon:
        flip
        xoffset -960
    show anon b_empty f_flirt o_melonia_pulling:
        flip
        xoffset -530
    with dissolve
    anon "Ya, Bu."


    scene location_rump_bedroom_bed_closeup
    show melonia f_smirk b_swimsuit_hatless
    show anon f_flirt
    with fade
    melonia "Saya sangat senang suami saya mempekerjakan Anda!"

    show anon f_flirt_low
    show melonia f_smirk_down a_remove_shall1
    with dissolve
    pause
    show melonia a_remove_shall2 with dissolve
    pause
    show melonia a_remove_shall3 with dissolve
    pause
    show melonia a_remove1 f_smirk_down with dissolve
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
