label eveX1_lewd:
    scene location_tattoo_bedroom_bed_side
    show eve b_pajamas_sleeping01 f_calm_close
    show anon a_empty b_empty f_normal_back_low:
        offset (-266.5, 45.5) subpixel True xzoom -.78 yzoom .78
    pause
    hide anon
    show eve b_pajamas_sleeping02
    with dissolve
    pause
    show eve b_pajamas_sleeping03 with dissolve
    pause
    eve @ -m_talk "MM."

    eve "{b}[firstname]{/b}?"

    anon "Selamat pagi, tukang tidur."

    eve f_happy_close "Hehe!"


    scene location_tattoo_bedroom_bed_top
    show eve a_belly b_pajamas_bed_back f_yawn m_talk
    show anon a_down b_sleep_side_eve f_sleep_side_normal
    show eve_overlay_o_blanket as blanket
    with fade
    eve -m_talk "{i}*Menguap*{/i}"

    eve a_belly b_pajamas_bed_side f_happy "Jam berapa sekarang?"

    anon "Entahlah, sepertinya jam sepuluh?"

    eve f_concerned "Uh, pagi sekali?"

    eve "Mari kita kembali tidur."

    anon f_sleep_side_sexy "Apa, apakah kamu berencana untuk tidur sepanjang hari?"

    eve f_happy "Ya."

    show eve b_pajamas_bed_back f_calm with {'master': dissolve}
    eve "Apalagi sekarang kamu di sini untuk memelukku."

    anon f_sleep_side_normal "Oh, jadi itu akan menjadi alasanmu, ya?"

    show anon a_hold b_sleep_side_eve_cuddle f_sleep_side_sexy
    show eve a_empty
    show eve_arms_pajamas_bed_back_a_belly as eve_arm_left behind blanket:
        crop (680, 0, 344, 768) xalign 1.
    show eve_arms_pajamas_bed_back_a_belly as eve_arm_right behind anon:
        crop (0, 0, 680, 768)
    with {'master': dissolve}
    eve f_laugh @ -m_talk "hehe!"

    show anon f_sleep_side_normal_closed
    show eve f_calm
    pause
    anon "Rasanya menyenangkan."

    eve "Benar?"

    pause
    anon "Kamu lembut sekali, {b}Eve{/b}."

    pause
    anon "Dan hangat."

    eve @ -m_talk "Mhmm."

    pause
    anon "Astaga, kamu juga wangi!"

    anon f_sleep_side_normal "Seperti kue yang baru dipanggang."

    eve "Heh, kurangi bicara, perbanyak tidur!"

    anon f_sleep_side_sexy "Saya bisa memikirkan sesuatu yang lebih menyenangkan daripada tidur."

    eve "Tidak ada yang lebih menyenangkan daripada tidur."

    anon "Anda yakin tentang itu?"

    eve "Ya."

    hide eve_arm_left
    hide eve_arm_right
    show anon b_sleep_side_eve_kiss
    eve a_down f_gasping "{i}*Terkesiap*{/i}"

    eve f_calm "Ah, itu tidak adil..."

    anon b_sleep_side_eve_cuddle f_sleep_side_normal "Mmm, kamu juga enak."

    show anon b_sleep_side_eve_kiss with dissolve
    eve "... Heh, kamu bertarung kotor."

    show eve f_lipbite
    pause
    eve @ -m_talk "Ngh!"

    pause
    show anon b_sleep_side_eve_cuddle
    show eve a_empty b_pajamas_bed_side f_sexy
    show eve_arms_pajamas_bed_side_a_belly as eve_arm_left behind blanket:
        crop (680, 0, 344, 768) xalign 1.
    show eve_arms_pajamas_bed_side_a_belly as eve_arm_right behind anon:
        crop (0, 0, 680, 768)
    with dissolve
    pause
    hide anon
    hide eve_arm_left
    hide eve_arm_right
    show eve b_pajamas_bed_side_kiss
    with dissolve
    eve @ -m_talk "MM."

    pause
    show anon a_touch b_sleep_side_eve f_sleep_side_sexy behind blanket
    show eve a_belly b_pajamas_bed_side f_happy
    with {'master': dissolve}
    eve "Penipu."

    anon "Masih ingin kembali tidur?"

    eve "Tidak."

    anon "Hehe."

    hide anon
    show eve b_pajamas_bed_side_kiss
    with dissolve
    eve "MM."

    pause
    show anon a_touch b_sleep_side_eve f_sleep_side_normal behind blanket
    show eve a_belly b_pajamas_bed_side f_happy
    with dissolve
    eve "Bantu aku melepas celana piyama ini."

    anon "Dengan senang hati!"


    $ renpy.dynamic(gender='trans' if M_eve.get('biggus_dickus') else 'cis',
                    anal=not M_eve.get('sex_front_1st_time'))
    call scene_eve_sex_wake.repeat (gender, anal)
    $ unlock_scene('Eve', '07_unlocked', variant=gender)
    if gender == 'cis' and anal:
        $ unlock_scene('Eve', '07_unlocked', variant='cis anal')

    scene location_tattoo_bedroom_bed_side
    show eve b_pajamas_sleeping03 f_happy_close
    with fade
    eve @ -m_talk "MM."

    eve "Aku bisa terbiasa bangun seperti itu..."

    anon "Ya?"

    pause
    anon "Yah, aku bisa terbiasa tertidur seperti ini."

    eve "Saya juga."

    pause
    eve "Aku cinta kamu, {b}[firstname]{/b}."


    menu:
        "Aku pun mencintaimu.":
            anon "Aku pun mencintaimu."

            eve "Kamu adalah hal terbaik yang pernah terjadi padaku."

            anon "Begitu pula {b}Evie{/b}."

        "Tidur.":

            pause
            eve f_curious_back "Apakah kamu mendengarku, {b}[firstname]{/b}?"

            anon "Zzz..."

            show eve f_sad_down
            pause
            show eve f_calm_close

    pause

    scene expression background(440, 304, 3.2, o=1) as stage with longfade
    show anon a_rub b_shirt f_yawn with {'master': dissolve}:
        xoffset -250 xzoom -1
    anon @ -m_talk "{i}*Menguap*{/i}"

    show anon b_shirt_undress_bottom with dissolve
    pause
    show anon a_sides b_dressed f_happy_back_low with {'master': dissolve}
    anon "{b}Malam{/b}?"

    show anon f_confused_low with {'master': dissolve}:
        xoffset 250 xzoom 1
    pause
    anon a_thinking f_thinking_down @ -m_talk "(Hmm, dia pasti sudah bangun sebelum aku...)"

    show anon a_sides f_confused with {'master': dissolve}:
        xoffset -250 xzoom -1
    anon @ -m_talk "( ... Dan sepertinya {b}pancuran sedang berjalan{/b}. )"

    pause
    anon f_grin @ -m_talk "(Saya ingin tahu apakah dia tertarik pada perusahaan kecil?)"

    hide anon with dissolve
    return


label eveX1_lewd.fail:
    scene location_tattoo_bedroom_bed_side
    show eve b_pajamas_sleeping01 f_calm_close
    show anon a_empty b_empty f_happy_back_low:
        offset (-266.5, 45.5) subpixel True xzoom -.78 yzoom .78
    anon @ -m_talk "(Aww, dia terlihat sangat damai dan manis...)"

    anon @ -m_talk "(Saya tidak ingin merusaknya.)"

    pause
    anon f_normal_back_low @ -m_talk "(Saya akan kembali lagi nanti dan berbicara dengannya.)"

    anon f_happy_back_low @ -m_talk "( Mimpi indah, {b}Malam{/b}. )"


    scene black with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
