label yoyo_button_showroom:
    show anon a_point f_annoyed with {'master': dissolve}
    anon "Baiklah, nona gila, aku punya masalah serius yang harus kuambil bersamamu!"

    yoyo f_eyeroll "Ugh, pergilah, pria bodoh..."

    show anon a_sides
    with {'master': dissolve}
    yoyo f_normal "... {b}Kim{/b} selesai denganmu."

    anon f_skeptical "Hah?!"

    anon "saya-"

    pause
    anon f_annoyed "Yah, aku belum selesai!"

    show anon a_frustrated
    with {'master': dissolve}
    anon "Saya terbangun di tempat sampah!"

    yoyo f_normal "Ya, {b}Kim{/b} membawamu ke sana."

    show anon a_sides
    with {'master': dissolve}
    anon @ -m_talk "..."
    show yoyo a_point_under
    with {'master': dissolve}
    yoyo "Kamu termasuk dalam sampah, kamu tidak berharga."

    anon "Hei, persetan, nona!"

    show yoyo a_gimme
    with {'master': dissolve}
    yoyo "Benteng, sudah jelas kamu tidak tahu koordinatnya..."

    yoyo "... Anda melanggar rike rittre girr selama interogasi."

    show anon a_crossed f_unimpressed
    show yoyo a_sides
    with {'master': dissolve}
    anon "Saya tidak melakukannya."

    yoyo "Melakukannya."

    anon "Tidak, aku tidak melakukannya."

    show yoyo a_tantrum f_annoyed
    with {'master': dissolve}
    yoyo "Ya, benar!"

    anon "Tidak, aku tidak melakukannya!"

    show yoyo a_frustrated f_angry
    with {'master': dissolve}
    yoyo "YA, KAMU MELAKUKANNYA!!"

    show anon a_tantrum f_annoyed
    with {'master': dissolve}
    anon "Tidak!"

    yoyo "TELAH MELAKUKAN!!"

    show anon a_angry f_angry
    with {'master': dissolve}
    anon "TIDAK!!"

    yoyo f_scary @ f_angry_teeth "TELAH MELAKUKAN!!!"

    pause
    show anon a_sides f_tired
    with {'master': dissolve}
    pause
    anon "Nona, Anda tidak dapat memecahkan angin di pabrik kacang-kacangan."

    show yoyo f_annoyed
    with {'master': dissolve}
    yoyo f_cynical "Bisa juga."

    anon "Seks bukanlah alat interogasi yang efektif."

    show yoyo a_crossed
    with {'master': dissolve}
    yoyo "Juga."

    yoyo "Kembali ke Korea, {b}Kim{/b} saudara laki-lakinya mendobrak wanita bangsawan dengan ancaman seks."

    show anon a_facepalm f_disgusted
    with {'master': dissolve}
    anon "Eugh, tidak... Aku tidak membutuhkan gambaran mental itu!"

    show anon f_disgusted_wince
    pause
    show anon a_sides f_tired
    with {'master': dissolve}
    anon "{i}*Huh*{/i}"

    anon f_worried "Dengar, mungkin kakakmu bisa... dia pada dasarnya adalah seorang goblin tapi kamu..."

    show yoyo f_confused
    anon "...Yah, kamu-"

    show anon f_disgusted
    pause
    anon f_worried "Tidak, aku tidak sanggup mengatakannya."

    show yoyo a_point_under f_smirk
    with {'master': dissolve}
    yoyo "Akui saja kamu putus!"

    show anon a_crossed f_unimpressed
    with {'master': dissolve}
    anon "Umm, tidak... karena aku tidak melakukannya."

    show yoyo a_sides f_angry
    with {'master': dissolve}
    yoyo "Grr, oke, pria bodoh..."

    yoyo "... Kita lanjutkan lagi dan kali ini {b}Kim{/b} menghancurkanmu dua kali lebih keras!"

    show anon f_surprised

    menu yoyo_button_showroom.choice:
        "Persetan!":

            jump yoyo_button_showroom.nah
        "Ayo!":

            pass

    anon f_annoyed "Anda tahu, baiklah!"

    show anon a_sides f_grumpy
    with {'master': dissolve}
    anon "Selain taser, menurut saya teknik interogasi Anda sangat menyenangkan..."

    anon "... Setelah melewati rasa jijik awal saat kau menyentuhku, tentu saja."

    yoyo f_annoyed "Orang cabul."


    if 'counter' not in renpy.get_showing_tags():
        show anon a_point_back
        with {'master': dissolve}

    anon f_annoyed "Diam dan masuk ke garasi!"

    hide yoyo
    with {'master': dissolve}
    yoyo "Hmph!"


    if 'counter' not in renpy.get_showing_tags():
        show anon a_sides:
            xoffset -500
            xzoom -1
        with {'master': dissolve}

    pause
    show anon a_frustrated f_eyeroll
    with {'master': dissolve}
    anon "{b}Kim{/b}yang aneh dan omong kosong gila mereka."

    hide anon with dissolve

    call scene_yoyo_truck_cowgirl.repeat
    $ unlock_scene('yoyo', '01_unlocked', variant='repeat')

    scene location_dealership_alley
    with fade
    anon "Uh, tidak..."

    anon "... Tidak lagi."


    scene location_dealership_alley_garbage
    with fade
    pause
    show anon a_up f_disgusted_low o_sewage of_banana:
        offset (-200, 140) xzoom -1
    show location_dealership_alley_garbage_overlay as dumpster
    with {'master': dissolve}
    pause
    anon f_tired "Ahh, kawan..."

    anon "... Aku hanya menyalahkan diriku sendiri dalam hal ini."

    show anon a_sides:
        yoffset 0
    with {'master': dissolve}
    pause
    show anon f_tired_up
    pause
    show anon a_banana_grab -of_banana
    with {'master': dissolve}
    pause
    show anon a_banana f_tired_low
    with {'master': dissolve}
    anon "{i}*Huh*{/i} Aneh {b}Kim{/b}s."

    show anon a_sides f_disgusted_low
    with {'master': dissolve}
    pause
    hide anon with dissolve
    return 'dumpster'


label yoyo_button_showroom.nah:
    anon f_annoyed "Ya, dalam mimpimu aku melakukan itu lagi."

    hide anon
    with {'master': dissolve}
    yoyo "Hei, mau kemana?!"

    anon "Sejauh mungkin darimu, nona gila!"

    show yoyo a_hips:
        xoffset -250
    with {'master': dissolve}
    yoyo "Anda datang ke sini sekarang dan berhubungan seks dengan {b}Kim{/b}!"

    anon "Tidak."

    yoyo "Maksudku!!"

    anon "Tidak dapat mendengarmu!"

    hide yoyo
    with {'master': dissolve}
    yoyo "Kembali ke sini, bocah nakal!!"

    return L_dealership


label yoyo_button_showroom.repeat:
    show anon a_sides with {'master': dissolve}
    yoyo f_laugh_low "Warna warna warna."

    show anon f_unimpressed
    show yoyo a_point_under f_smirk
    with {'master': dissolve}
    yoyo "{b}Kim{/b} membuatmu sangat sedih..."

    anon "Umm, tidak, kamu tidak melakukannya."

    show yoyo a_sides
    with {'master': dissolve}
    yoyo "Melakukannya."

    anon "Tidak, kamu tidak melakukannya."

    show yoyo a_tantrum f_annoyed
    with {'master': dissolve}
    yoyo "Melakukannya!"

    show anon a_tantrum f_annoyed
    with {'master': dissolve}
    anon "Tidak, kamu tidak melakukannya!"

    show yoyo a_frustrated f_angry
    with {'master': dissolve}
    yoyo "TELAH MELAKUKAN!!"

    show anon a_angry f_angry
    with {'master': dissolve}
    anon "TIDAK!!"

    yoyo f_scary @ f_angry_teeth "TELAH MELAKUKAN!!!"

    pause
    show anon a_sides f_tired
    with {'master': dissolve}
    anon "{i}*Huh*{/i}"

    anon f_grumpy "Berdebat denganmu tidak ada gunanya..."

    show yoyo a_crossed f_annoyed
    with {'master': dissolve}
    yoyo "Akui saja kamu putus!"

    show anon a_pocket f_unimpressed
    with {'master': dissolve}
    anon "Umm, tidak... karena aku tidak melakukannya."

    show yoyo a_sides f_angry
    with {'master': dissolve}
    yoyo "Grr, oke, pria bodoh..."

    yoyo "... Kita lanjutkan lagi dan kali ini {b}Kim{/b} menghancurkanmu dua kali lebih keras!"

    jump yoyo_button_showroom.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
