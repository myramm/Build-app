label scene_nadya_sex_cargo:

    return


label scene_nadya_sex_cargo.stage:
    scene location_warehouse_storage_sex
    show nadya b_sex_wall_after f_happy
    with fade
    pause
    show anon nadya_sex_cargo with {'master': dissolve}
    return


label scene_nadya_sex_cargo.pre:
    show nadya b_sex_wall_insert_pullout f_sexy with {'master': dissolve}
    return


label scene_nadya_sex_cargo.insert:
    show anon b_insert
    show nadya f_sexy_down
    with {'master': dissolve}
    return


label scene_nadya_sex_cargo.slam:
    hide anon
    hide nadya
    show nadya_sex_wall_anim 9 as animation
    return


label scene_nadya_sex_cargo.animate:
    python:
        anim_toggle = True
        animated = True
        M_nadya.set('sex speed', .1)
    hide anon
    hide nadya
    show nadya_sex_wall_anim as animation
    with dissolve
    return


label scene_nadya_sex_cargo.loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 3:
        if anim_toggle:
            if not animated:
                show nadya_sex_wall_anim as animation with dissolve
                $ animated = True
            pause 5
            call scene_nadya_sex_cargo.dialogue
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8,9]
            $ poses_done = []
            while poses_done != pose_list:
                show expression 'nadya_sex_wall_anim {}'.format(pose_list[pose_counter]) as animation
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call scene_nadya_sex_cargo.dialogue
        $ animcounter += 1
    call screen scene_nadya_sex_cargo_controls
    if not _return:
        jump scene_nadya_sex_cargo.loop
    return _return


label scene_nadya_sex_cargo.dialogue:
    if animcounter == 0 and randomizer() > 75:
        nadya "Ya!{w=1}{nw}"

        pause 1
        nadya "Ya ampun!{w=1}{nw}"

        nadya "Seperti itu saja!{w=1}{nw}"

    elif animcounter == 0 and randomizer() > 75:
        nadya "Persetan dengan vagina kecilku!!{w=1}{nw}"

    elif animcounter == 1 and randomizer() > 75:
        nadya "Lebih sulit!{w=1}{nw}"

        anon "Ya Tuhan!{w=1}{nw}"

        nadya "Banting lebih keras!!{w=1}{nw}"

    elif animcounter == 2 and randomizer() > 75:
        nadya "Ahh!!{w=1}{nw}"

        nadya "Ayam cantikmu besar sekali!!{w=1}{nw}"

        pause 1
        nadya "Saya menyukainya!{w=1}{nw}"

    return


label scene_nadya_sex_cargo.cum(where):
    anon "Apakah kamu dekat?"

    nadya "Ya!!"

    anon "Bagus, aku juga!"

    pause
    nadya "I'm cumming!!" (show_native="Ya konchayu!!")
    nadya "Ahh, I'm cumming!!" (show_native="Ahh, ya konchayu!!")
    if where == 'inside':
        jump scene_nadya_sex_cargo.inside
    jump scene_nadya_sex_cargo.outside


label scene_nadya_sex_cargo.inside:
    nadya "NGGHHH!!!"

    hide animation
    show nadya b_sex_wall_cum
    anon "HNNGGG!!!" with flash
    show xray_nadya_sex_wall with fastdissolve
    pause
    hide xray_nadya_sex_wall with {'master': dissolve}
    anon "Haah... Haah..."

    show anon nadya_sex_cargo b_insert o_after
    show nadya b_sex_wall_insert_pullout f_sexy_close_up
    with dissolve
    pause
    show anon a_after b_pre
    show nadya b_sex_wall_after f_sexy_down
    with {'master': dissolve}
    nadya "Wow!" (show_native="Ukh ty!")
    nadya "Anda menjatuhkan beban besar!"

    anon "Hmm?"


    scene location_warehouse_storage_sex_after
    show nadya_body_b_storage_sex_after
    show nadya_sex_wall_after_overlay_o_cum
    with fade
    nadya "Lihat, terlalu banyak untuk ditampung rahim..."

    anon "!!!"
    nadya "... Anda pasti memasukkan bayi ke dalam!"

    pause
    anon "Apakah itu hal yang buruk?"

    nadya "Of course not!" (show_native="Konechno, nyet!")

    scene location_warehouse_storage_sex
    show anon nadya_sex_cargo a_after b_pre o_after
    show nadya b_sex_wall_pre
    with fade
    nadya "Saya membutuhkan ahli waris untuk mengambil alih Bratva di masa depan."

    pause
    nadya f_happy "Mudah-mudahan itu perempuan."


    call call_pregnancy_minigame (None, M_nadya)
    return 'inside'


label scene_nadya_sex_cargo.outside:
    nadya "Tunggu, berhenti!"

    hide animation
    show nadya b_sex_wall_insert_pullout f_annoyed_down
    show anon nadya_sex_cargo b_insert
    with {'master': dissolve}
    anon "Aku tidak bisa berhenti sekarang, aku akan-"

    nadya f_sexy_down "Sperma di wajah."

    show anon nadya_sex_cargo b_pre
    show nadya f_sexy
    with {'master': dissolve}
    anon "Hmm?!"

    show nadya b_sex_wall_facial f_sexy_up with {'master': dissolve}
    nadya "Sperma di wajahku!"

    show anon b_facial1
    show nadya f_cumshot
    anon "HNNGGG!!!" with flash
    show anon b_cumshot4
    pause
    nadya f_sexy_close_up "Ya ampun!!"

    show anon b_facial2
    show nadya f_cumshot
    anon "HNNGGGUH!!!" with flash
    show anon b_facial2
    show nadya f_sexy_close_up o_storage_sex_facial
    nadya "Cover me in cum!!" with flash
    show anon a_after b_pre with dissolve
    pause
    anon "Haah... Haah..."

    pause
    anon "Sialan... kamu baik-baik saja?"

    nadya @ f_laugh "hehe!"

    nadya "Dasar anak kotor..."

    nadya "... Lihat apa yang kamu lakukan pada wajah cantikku!"

    anon "Heh, aku hanya melakukan apa yang kamu suruh."

    nadya "Apakah benar."

    pause
    nadya "Bayangkan jika papa menemuiku sekarang ya?"

    nadya "Gadis kecilnya berlumuran air mani."

    nadya f_laugh "Haha!"

    anon "Y-ya, dia mungkin akan membunuh kita berdua."

    nadya f_sexy_close_up "Hehe, ya."

    nadya "Aku pasti dia bunuh..."

    show nadya f_eyeroll_close
    pause
    nadya "... Anda dia mungkin menyiksa."

    show nadya f_sexy_close_up
    anon "{i}*Gulp*{/i} Ya, untungnya dia sudah tidak ada lagi saat itu."

    nadya "Ya, ini bagus."

    show nadya a_towel_ask f_worried_close_up
    with {'master': dissolve}
    nadya "Ehh, berikan aku kain lap... kumohon."

    nadya "Untuk menghapus wajah cum."

    anon "Oh benar."

    show anon b_towel_grab
    show nadya a_down f_surprised_close_low
    with dissolve
    pause
    show anon a_towel_give b_pre
    show nadya a_towel_ask f_sexy_close_up
    with {'master': dissolve}
    anon "Ini dia."

    show anon a_after
    show nadya a_towel_hold
    with {'master': dissolve}
    nadya "Thank you." (show_native="Spasibo.")
    show nadya a_empty f_sleep
    show nadya_arms_sex_wall_facial_a_towel_wipe as arms
    with dissolve
    pause
    hide arms
    show nadya_overlay_o_storage_sex_facial as cum behind nadya at right:
        crop (550, 0, 474, 768)
    show nadya a_towel_hold f_worried_up -o_storage_sex_facial
    with {'master': dissolve}
    nadya "Apakah bagus?"

    anon "Y-ya."

    nadya f_sexy_up "Oke."

    show nadya a_towel_throw f_happy_back
    with dissolve
    pause
    show nadya b_sex_wall_pre f_happy with {'master': dissolve}
    nadya "Nah, itu saat-saat seksi yang bagus!"

    anon "Hehe, ya."

    return 'outside'


label scene_nadya_sex_cargo.repeat:
    call scene_nadya_sex_cargo.stage
    anon "Hmm?"

    nadya f_sexy @ f_sexy_down "... Memekku menetes untukmu."

    anon "{i}*Gulp*{/i} Y-ya, aku mengerti."

    pause
    call scene_nadya_sex_cargo.pre
    nadya "Kami bercinta di sini, di dinding."

    call scene_nadya_sex_cargo.insert
    nadya "Berikan padaku dengan sangat keras."

    anon "Oke."

    call scene_nadya_sex_cargo.slam
    nadya "Ngh!!" with hpunch
    pause
    call scene_nadya_sex_cargo.animate
    nadya "Ya!"

    pause
    nadya "Ya ampun!"

    nadya "Sama seperti itu!"

    pause
    nadya "Persetan dengan vagina kecilku!!"

    pause
    nadya "Lebih sulit!"

    anon "Ya Tuhan!"

    nadya "Banting lebih keras!!"

    pause
    nadya "Ahh!!"

    nadya "Ayam cantikmu sangat besar!!"

    pause
    nadya "Saya menyukainya!"

    pause
    call scene_nadya_sex_cargo.loop
    call scene_nadya_sex_cargo.cum (_return)
    return _return


label scene_nadya_sex_cargo.replay:
    jump scene_nadya_sex_cargo.repeat


screen scene_nadya_sex_cargo_controls():
    style_prefix 'sex'

    vbox:

        frame:
            has hbox
            textbutton _('Keep Going') action Return(False)
            textbutton _('Cum Inside') action Return('inside')
            textbutton _('Cum Outside') action Return('outside')

        frame:
            has hbox
            textbutton _('« Slower'):
                action (Function(M_nadya.set,
                                 'sex speed',
                                 M_nadya.get('sex speed') + 0.02),
                        Return(False))
                sensitive M_nadya.get('sex speed') < .1
            textbutton _('Faster »'):
                action (Function(M_nadya.set,
                                 'sex speed',
                                 M_nadya.get('sex speed') - 0.02),
                        Return(False))
                sensitive M_nadya.get('sex speed') > .061
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
