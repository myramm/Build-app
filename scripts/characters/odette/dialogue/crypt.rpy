label odette_button_crypt:
    scene odette b_vamp_front
    odette "Jadi kamu memutuskan untuk kembali, ya?"


    scene black with fasteyeshut
    pause .05

    scene odette b_vamp_front_normal with fasteyeopen
    anon "Umm... {i}*Gulp*{/i} Y-ya."

    odette "Dimana {b}Evie{/b}?"

    anon "Dia terlalu takut untuk datang."

    odette "Ah, sayang sekali."

    odette "Kita bisa bersenang-senang bersama."


    scene location_crypt_side
    show odette b_vamp_sitting_cape_normal f_smirk
    show anon f_worried:
        xoffset -150
    with fade
    odette "Kalau begitu, aku harus puas hanya denganmu, bukan?"

    anon "Y-ya, menurutku..."

    odette "Tidak apa-apa."

    show anon f_surprised_teeth a_surprised_up
    show odette b_vamp_normal f_smirk:
        xoffset -480
    odette "You're quite delicious, you know?" with hpunch
    anon f_worried a_neck_hurt "D-enak?"

    show odette f_laugh:
        xoffset -225
    with dissolve
    odette "Hehehe!"

    show anon a_sides behind odette
    show odette f_smirk
    with {'master': dissolve}
    odette "Ini, minumlah."

    anon a_behind_head "Oh, entahlah..."

    anon "... Terakhir kali itu benar-benar-"

    show odette a_blood_cup_force
    show anon f_smoke a_up
    with dissolve
    anon "!!!"
    odette "Ssst."

    odette "Percayalah, {b}[firstname]{/b}."

    show odette a_idle
    show anon f_disgusted a_sides
    with dissolve
    anon "Hmm, kali ini agak manis..."

    odette "Ya, semakin banyak Anda meminumnya, semakin baik."

    show anon f_skeptical
    show odette f_drink a_blood_cup_drink with {'master': dissolve}
    anon "Benar-benar?"

    anon "Agak aneh... Bukan?"

    odette a_idle f_smirk "Anda banyak bertanya, bukan?"

    anon a_behind_head f_shy "Hehe, maaf..."

    show odette f_drink a_blood_cup_drink with dissolve
    anon "Saya pada dasarnya hanyalah orang yang ingin tahu-"

    show odette a_blood_cup_force f_smirk
    show anon f_smoke a_up
    with dissolve
    anon "!!!"
    odette "Itu saja."

    odette "Minumlah dalam-dalam, kawan."

    pause
    show odette a_idle
    show anon f_disgusted a_sides
    with dissolve
    anon "Eh, kawan..."

    anon "Ini sangat tebal."

    odette @ -m_talk "Mhmm."

    show odette f_drink a_blood_cup_drink behind anon
    show anon a_surprised_hands f_surprised_low
    with dissolve
    pause
    anon "Aduh, kawan... Jangan lagi."

    show odette a_idle f_smirk o_blood
    with dissolve
    odette "Ada apa?"

    anon a_surprised_lips f_surprised_down "Mah robek ahr mati rasa gin..."

    show odette a_blood_cup_throw f_laugh with dissolve
    odette "hehe!"

    show anon f_surprised a_sides
    show odette a_blood_wipe o_empty f_smirk
    with {'master': dissolve}
    anon "Bagaimana kabarmu joo dun feer ini?"

    show odette a_undress1
    with dissolve
    pause
    show anon f_surprised_low
    show odette b_naked a_vamp_undress2
    with {'master': dissolve}
    odette "Saya kira, efeknya terhadap setiap orang berbeda-beda."

    show anon f_surprised
    show odette a_idle
    with dissolve
    pause
    label odette_button_crypt.resume:
    hide anon
    show odette b_kiss_anon:
        xoffset -500
    with dissolve
    anon "!!!"
    pause
    odette "MM."

    pause

    scene odette b_vamp_bite f_normal:
        xoffset 0
    show location_crypt_bite_overlay
    with fade
    odette "Baumu enak!"

    anon "Mati menggambar?"

    odette f_lip_normal @ -m_talk "Mhmm!"


    scene location_crypt_side
    show odette b_kiss_anon:
        xoffset -500
    with fade
    pause
    anon "Ngh!"

    pause

    scene odette b_vamp_bite f_fangless:
        xoffset 0
    show location_crypt_bite_overlay
    with fade
    odette "Anda merasa lebih enak!"

    odette "Begitu penuh kehidupan dan semangat..."


    if M_odette.is_state(S_ode02_tomb):
        anon "Apa yang selalu kudengar dari korar itu?"

        odette f_curious -m_talk "Hmm?"

    else:
        anon "Telinga Joo sedang direkatkan!"

        odette "Telingaku?"

        show odette f_curious

    anon "Joo dengar..."

    anon "Grr... {i}MATA{/i}!"

    show odette f_fangless

    if M_odette.is_state(S_ode02_tomb):
        odette "Mataku?"

        odette "Bagaimana dengan mereka?"

        anon "Merekatkannya."


    odette f_laugh "Hehe, kamu sangat menggemaskan."


    scene location_crypt_side
    show odette b_kiss_anon:
        xoffset -500
    with fade
    pause
    anon "Hngggh!!"

    pause

    scene odette b_vamp_bite f_bite:
        xoffset 0
    show location_crypt_bite_overlay
    with fade

    if M_odette.is_state(S_ode02_tomb):
        odette "Mmm, aku bisa saja memakanmu..."

        show odette f_tongue
        anon "!!!" with hpunch
        show odette f_lip
        anon "Apakah itu taringnya?!"

    else:
        odette "Aku berharap {b}Eve{/b} ada di sini untuk membantuku melahapmu..."

        show odette f_tongue
        anon "!!!" with hpunch
        show odette f_lip
        anon "Ang!"

        anon "Ah tahu identitasnya!!"


    odette f_bite "... Aku ingin kamu di dalam diriku!"

    anon "Hmm?!"


    scene location_crypt_side
    show odette b_naked_vamp f_smirk:
        xoffset -400
    show anon f_worried o_boner a_surprised behind odette:
        xoffset -150
    with fade

    if M_odette.is_state(S_ode02_tomb):
        anon "T-tunggu, ahm nut zhur dis-"

    else:
        anon "T-tunggu, ah hab kuestins..."


    show anon f_surprised_down
    odette f_teeth_look a_grope "Saya membutuhkannya sekarang!"

    show anon f_worried

    if M_odette.is_state(S_ode02_tomb):
        anon "Mah bahdie mengucapkan kata-kata!"

    else:
        anon "Sebuah juh-"


    show anon f_surprised_teeth
    odette f_smirk a_hips "Mengupas."

    show odette f_laugh behind anon
    show anon b_dressed_pickup f_worried -o_boner:
        offset (-250, 50)
    with {'master': dissolve}
    anon "Uh-uh! Uh-uh!"

    show odette f_teeth_look
    show anon a_sides b_shirt f_worried_surprised od_dick2:
        offset (-150, 0)
    with dissolve
    pause
    show odette b_naked_pull_anon f_smirk:
        xoffset -150
    show anon b_empty:
        xoffset -125
    with {'master': dissolve}
    odette "Buru-buru!"

    show odette b_vamp_sitting_up:
        xoffset 0
    show anon f_side_shy b_empty:
        xoffset 216
    with {'master': dissolve}
    odette "Persetan denganku di sini, di singgasanaku!"

    anon "Mah, tidak tahu apa-apa!"


    call scene_odette_sex_crypt.repeat
    $ unlock_scene('Odette', '03_unlocked')

    scene odette b_vamp_bite f_bite
    show location_crypt_bite_overlay as overlay
    with fade
    anon "Apa yang diperas dengan mer?"

    odette "Benih kehidupan, dianugerahkan kepada yang tidak suci."

    anon "Belum selesai?!"

    odette "Sebuah ritual kegelapan!"

    odette "Sebuah kontrak yang ditempa dengan penuh semangat dan disegel dengan darah!"

    anon "Saudara?"

    anon "Ke-kemana ah joo-"

    odette "Penghuni malam!"

    odette "Ayo maju dan layani aku!"

    anon "Kun kita suka cudder?"

    show location_crypt_bite02 behind overlay
    anon "!!!" with hpunch
    show location_crypt_bite03 behind overlay with dissolve
    anon "Ooh, itu terasa..."

    show location_crypt_bite04 behind overlay with dissolve
    anon "...Reer..."

    pause
    anon "... Ya ampun."

    show location_crypt_bite04 behind overlay

    scene black with {'master': dissolve}
    odette "Hehehe!"

    "..."
    return 'sleep'
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
