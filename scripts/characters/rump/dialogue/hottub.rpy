label rump_button_hottub:
    $ renpy.dynamic(stage=background(840, 408, 2.85, b=.6))

    scene expression stage as stage:
        align (.5, .5)
        offset (-60, 100)
        zoom 1.75
    show rump b_jacuzzi f_smirk:
        yoffset 0
    show location_rump_backyard_jacuzzi_overlay_evening as hottub:
        offset (-205, -220)
        zoom 1.4
    show anon b_telescope_peeking_caught with dissolve:
        offset (-580, 140)
        zoom 1.4
    rump "Nuh uh, aku tidak akan menerima jawaban tidak!"

    pause
    rump "Yah, tentu saja Bill akan berada di sana..."

    rump "Kamu pikir dia akan melewatkan kesempatan untuk berpesta dengan {b}Rump{/b}-meister?!"

    pause
    rump "Ya, aku bisa memberi kita pukulan."

    pause
    rump @ -m_talk "Mhmm."

    rump "Tidak masalah!"

    pause
    rump @ f_normal "Ya, gadis-gadis itu orang Rusia."

    pause
    rump "Nah, mereka sangat jinak."

    rump "Dan sangat ingin menyenangkan, sebaiknya Anda mempercayainya!"

    pause
    rump "Pastikan saja kamu membawa Michelle bersamamu."

    rump "{b}Melonia{/b} mencintainya."

    rump "Ditambah lagi, aku sangat ingin melihatnya mengenakan bikini!"

    pause
    rump @ f_laugh "Heh, kamu anjing kamu!"

    show rump f_suspicious_down
    pause
    rump f_normal "Permisi sebentar."

    rump a_phone_down f_angry "Hei kamu!"

    anon f_surprised @ -m_talk "Hmm?"

    rump "Ini adalah percakapan pribadi!"

    show layer master:
        linear .9 yoffset 155
    show expression stage as stage:
        linear .9 offset (0, 0) zoom 1.55
    show location_rump_backyard_jacuzzi_overlay_evening as hottubback behind rump:
        offset (-205, -220)
        zoom 1.4
        linear .9 offset (0, -15) zoom 1.
    show rump:
        linear .9 xoffset 100
    show location_rump_backyard_jacuzzi_overlay_evening as hottub:
        linear .9 offset (0, 0) zoom 1.
    show anon b_dressed_pickup with dissolve:
        offset (-200, -80)
        zoom 1.1
    pause .2
    show anon a_point_self b_dressed f_surprised_low with dissolve:
        offset (-100, -155)
        zoom 1.
    anon "Oh, aku tidak bermaksud-"

    rump "Keluar dari sini sebelum aku menelepon keamanan!"

    anon a_wave "Y-ya, tuan!"

    hide anon with fastdissolve

    scene expression background(400, 392, 5.) as stage with fade
    show anon f_surprised a_sides with dissolve
    anon @ -m_talk "(Hampir saja!)"

    anon @ -m_talk "(Saya mungkin harus menjaga jarak darinya untuk saat ini.)"

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
