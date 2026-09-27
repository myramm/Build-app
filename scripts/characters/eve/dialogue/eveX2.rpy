label eveX2_bath_eve:
    scene location_tattoo_bathroom_shower
    show eve a_empty b_naked_shower f_normal_down:
        xoffset 250
        xzoom -1

    if M_eve.get('biggus_dickus'):
        show eve od_dick01
    else:
        show eve od_scar

    show eve_arms_naked_shower_a_scrub as eve_arms:
        xoffset 250
        xzoom -1
    show location_tattoo_bathroom_shower_steam as steam
    pause
    show anon b_naked f_flirt_grin od_naked_dick1 behind eve
    with {'master': dissolve}
    pause
    show anon a_empty f_flirt:
        xoffset 90
    show anon_arms_naked_a_hips_eve as anon_arms behind eve_arms:
        xoffset 90
    with {'master': dissolve}
    anon "Hai, cantik-{w=.25{nw}"

    hide eve_arms
    show eve a_surprised f_surprised_right m_talk
    extend "" with hpunch
    show anon a_surprised f_worried_surprised
    show eve a_cover f_surprised_sad -m_talk:
        xoffset -250
        xzoom 1
    hide anon_arms
    with {'master': dissolve}
    anon "A-wah, santai saja..."

    show eve f_confused
    show anon a_sides f_happy
    with {'master': dissolve}
    anon "... Ini hanya aku."

    eve f_angry "Ya Tuhan, kamu membuatku takut!"

    anon f_brag "Ya, aku memperhatikan..."

    anon "... Heh, kamu hampir melompat keluar dari kulitmu."

    show anon f_laugh
    pause
    show anon a_sides_nervous f_hurt
    show eve a_punch:
        xoffset -310
    eve "It's not funny!" with hpunch
    show anon a_defensive f_worried:
        xoffset 60
    show eve a_cover:
        xoffset -250
    with {'master': dissolve}
    anon "Aduh, aku minta maaf!"

    eve f_concerned "Apakah kamu mencoba memberiku serangan jantung?!"

    anon "T-tidak."

    show anon a_sides
    with {'master': dissolve}
    anon "Aku tidak bermaksud menakutimu, jujur..."

    anon "... Aku hanya ingin bergabung denganmu."

    eve "Baiklah, tidak apa-apa... hanya saja, mungkin lain kali jangan menyelinap ke arahku!"

    anon "Baiklah, catat."

    pause
    show eve a_crossed f_thinking_down
    with {'master': dissolve}
    eve "Cih, sekarang sabunnya turun ke mana?"

    pause
    show eve behind anon
    show anon a_point_down_other f_normal_low:
        xoffset 80
    with {'master': dissolve}
    anon "Saya pikir itu jatuh di sana."

    show anon a_sides behind eve
    show eve a_hip:
        xoffset 350
        xzoom -1
    with {'master': dissolve}
    pause
    eve "Ah."

    show anon a_surprised f_surprised_down
    show eve b_naked_shower_pickup02:
        xoffset 150
    with {'master': dissolve}
    pause
    show anon a_sides f_flirt_down
    show eve b_naked_shower_pickup
    with {'master': dissolve}
    eve "Ya ampun licin banget.."

    show anon od_naked_dick_grow
    with {'master': dissolve}
    pause
    show eve a_scrub b_naked_shower f_normal_down:
        xoffset 350
    with {'master': dissolve}
    eve "... Jadi, hei, bagaimana perasaanmu saat keluar untuk sarapan atau apalah?"

    pause
    eve "{b}[firstname]{/b}?"

    show eve a_scrub02 f_confused_right
    pause
    show eve a_crossed_soap f_confused:
        xoffset -250
        xzoom 1
    with {'master': dissolve}
    eve "Apakah kamu mendengarkanku?"

    pause
    show eve a_hip f_nervous_down
    with {'master': dissolve}
    eve "Ya Tuhan, lagi?!"

    show anon a_defensive f_surprised od_naked_dick3
    with {'master': dissolve}
    anon "Hah?!"

    eve f_sexy "Kamu susah lagi!"

    anon f_confused_down "Oh, uhh..."

    anon "... Ya."

    show anon a_rub f_happy of_blush
    with {'master': dissolve}
    anon "Maaf, menurutku... kamu hanya memberikan efek seperti itu padaku."

    show eve a_crossed f_happy
    with {'master': dissolve}
    eve "Aduh."

    pause
    eve f_nervous_right "Baiklah, kita bisa melakukannya lagi."

    show anon a_sides f_surprised -of_blush
    with {'master': dissolve}
    anon "Benar-benar?"

    eve f_drawing_look_anon @ -m_talk "Mhmm."

    show anon f_happy
    show eve f_nervous_right:
        xoffset 350
        xzoom -1
    with {'master': dissolve}
    eve "Bersikaplah lembut saja, oke?"

    eve "Aku masih cukup sakit sejak pagi ini."

    anon "Luar biasa."

    hide anon
    show eve b_naked_shower_kiss f_thinking_lip:
        xoffset 59
    with {'master': dissolve}
    eve @ -m_talk "MM."

    show eve f_happy_closed
    with {'master': dissolve}
    eve "Ya Tuhan, kamu pandai dalam hal itu!"


    if M_eve.get('biggus_dickus'):
        show eve od_dick_grow
        pause 1.5
        show eve od_dick03
        eve f_confused_low "Haah!"

    else:

        pause

    eve f_nervous "Masukkan ke dalam diriku, {b}[firstname]{/b}!"


    $ renpy.dynamic(gender='trans' if M_eve.get('biggus_dickus') else 'cis')
    call scene_eve_sex_shower.repeat (gender)
    $ unlock_scene('Eve', '08_unlocked', variant=gender)

    scene expression background(512, 280, 2.4, l=L_tattooparlor_bathroom) as stage
    show anon a_towel b_shorts f_looking_down:
        xoffset -75
    show eve a_dry_hair b_naked_shower f_happy_closed:
        xoffset 350
        xzoom -1

    if M_eve.get('biggus_dickus'):
        show eve od_dick01
    else:
        show eve od_scar

    with fade
    pause
    show anon b_dressed_changing
    with {'master': dissolve}
    pause
    show anon a_sides b_dressed f_happy
    with {'master': dissolve}
    anon "Ya, itu menyenangkan!"

    show eve f_nervous:
        xoffset -250
        xzoom 1
    with {'master': dissolve}
    eve "Ya, benar."

    pause
    eve "Aku mungkin harus memeriksa hujan untuk sarapan itu..."

    show eve a_towel_wrap01 b_naked
    with {'master': dissolve}
    eve f_normal "... Heh, sepertinya aku tidak bisa duduk di bilik saat ini."

    show eve a_towel_wrap02
    with {'master': dissolve}
    anon "Ah, tidak apa-apa."

    show eve a_sides b_towel
    with {'master': dissolve}
    anon "Aku ragu kita akan menemukan tempat yang masih menyajikan sarapan selarut ini..."

    anon "... Kami tidur sampai hampir jam satu!"

    eve f_sad "Oh."

    show anon f_worried
    show eve f_pouting
    pause
    anon f_normal "Tapi, aku bisa keluar dan membelikan kami burger atau apalah!"

    eve f_surprised "Benar-benar?"

    anon "Ya."

    anon "Ini bisa jadi seperti sarapan di tempat tidur..."

    anon "... Anda tahu, hanya saja ini akan menjadi makan siang."

    eve f_happy "Hehe, kedengarannya luar biasa!"

    anon "Dingin."

    anon "Kamu mau kentang goreng atau nah?"

    eve f_thinking_down "Ehh..."

    eve f_normal "... Tidak. Hanya burgernya untukku."

    anon f_confused @ f_skeptical "Anda yakin?"

    eve f_happy @ -m_talk "Mhmm."

    anon f_normal "Baiklah kalau begitu."

    anon "Santai saja... dan saya akan segera kembali membawa kudapan!"

    eve f_sexy "Oh, jangan khawatir... Aku pasti akan bersantai."

    eve "Di tempat tidur..."

    show eve f_confused_low

    if gender == 'trans':
        eve "... Dengan sekantong es di bajinganku."

    else:
        eve "... Dengan sekantong es di antara kedua kakiku."


    show eve f_nervous
    anon f_happy "Hehe!"

    eve "Ini hari yang sibuk, tahu?"

    anon f_flirt "Mmm, hari ini belum berakhir..."

    eve f_surprised "Oh ya, benar!"

    show eve a_finger f_concerned
    with {'master': dissolve}
    eve "Jangan pernah memikirkannya, {b}[firstname]{/b}..."

    eve "... Aku akan menutup toko hari ini!"

    anon f_happy "Aduh."

    show eve a_hip f_happy
    with {'master': dissolve}
    eve "Heh, ambil saja makanannya, Harimau!"

    show anon a_salute
    with {'master': dissolve}
    anon "Ya, Bu!"

    eve f_laugh "hehe!"

    show anon a_sides:
        xoffset 600
    show eve a_sides f_happy:
        xoffset 375
        xzoom -1
    with {'master': dissolve}
    eve "Hai, {b}[firstname]{/b}?"

    show anon f_normal:
        xoffset 100
        xzoom -1
    with {'master': dissolve}
    anon @ -m_talk "Hmm?"

    eve f_nervous "Kamu adalah pacar terbaik yang bisa diminta oleh seorang gadis, tahu?!"

    show anon f_happy

    menu:
        "Dan kamu adalah pacar terbaik!":
            anon "Segera kembali padamu, cantik!"

            show eve f_nervous_right o_blush
        "Duh.":

            show anon a_frustrated
            with {'master': dissolve}
            anon "Saya tahu, kan?"

            show eve f_normal_up

    hide anon
    with {'master': dissolve}
    pause

    scene location_tattoo_bedroom_cutscene07 as cutscene
    show text "It was wonderful seeing Eve so happy and full of life. We joked and laughed and she filled me in on all the latest gossip from around school and the tattoo shop." as caption
    with fade
    pause
    hide caption with dissolve
    show text "It was one of the best lunches I ever had...\n" as caption with dissolve
    pause
    show location_tattoo_bedroom_cutscene07b as cutscene
    show text "\n... I didn't even mind when she ate all my french fries." as caption2
    with dissolve
    pause

    scene location_tattoo_bedroom_cutscene08
    show text "Afterwards we cuddled in bed and watched scary movies." as caption
    with fade
    pause
    hide caption with dissolve
    show text "Time always seemed to fly when I was with her and before we knew it, the time had come to say good night." as caption with dissolve
    pause
    hide caption with dissolve
    show text "Not a bad way to spend a day." as caption with dissolve
    pause

    scene expression background(l=L_tattooparlor_bedroom, o=1) as stage
    show anon
    show eve b_undies f_happy
    with fade
    eve "aku berharap kamu bisa tinggal..."

    anon "Ya, aku juga."

    pause
    anon "Sampai jumpa besok, oke?"

    eve "Y-ya, oke."

    hide anon
    show eve b_undies_kiss:
        xoffset -250
    with dissolve
    pause
    show anon:
        xoffset 100
    show eve b_undies f_happy:
        xoffset -100
    with dissolve
    eve "Selamat malam, {b}[firstname]{/b}."

    anon a_wave "Selamat malam, {b}Malam{/b}."

    hide anon with dissolve
    return


label eveX2_post_eve:
    show anon f_worried

    if game.timer.is_afternoon():
        anon @ f_worried_left "Aku berpikir, mungkin kita bisa turun ke bawah dan eh..."

    else:
        anon @ f_worried_left "Aku berpikir, mungkin kita bisa, eh..."


    show eve f_confused
    pause

    if game.timer.is_afternoon():
        eve "Dan apa?"

    else:
        eve "Apa?"


    anon f_normal "... Yah, aku tidak tahu tentangmu tapi aku bisa mandi."

    eve f_sexy "Oh, kamu mau mandi ya?"

    anon f_flirt @ -m_talk "Mhmm."

    eve f_confused "Atau mungkin akulah yang kamu inginkan..."

    show anon f_flirt_grin
    show eve a_thinking_sexy f_pouting
    with {'master': dissolve}
    eve "... telanjang dan basah?"

    show anon a_point f_surprised
    show eve a_hip f_laugh
    with {'master': dissolve}
    anon "Ya itu!"

    anon f_happy "Pastinya itu!"

    show anon a_sides
    with {'master': dissolve}
    eve "hehe!"

    eve f_sexy "Baiklah, ayo pergi."

    show anon a_surprised f_surprised
    with {'master': dissolve}
    anon "Benar-benar?"

    hide eve
    with {'master': dissolve}
    eve "Ya!"

    show anon a_cheering f_grin
    with {'master': dissolve}
    pause
    hide anon
    with {'master': dissolve}
    anon "Wooo!"


    if game.timer.is_afternoon() and not M_eve.once('shower_grace'):
        jump eveX2_post_eve.grace

    scene expression background(512, 280, 2.4, l=L_tattooparlor_bathroom) as stage
    show eve b_naked_shower_pickup01:
        xoffset -150

    if M_eve.get('biggus_dickus'):
        show eve od_dick01
    else:
        show eve od_scar

    with fade
    pause
    show anon a_towel b_shorts f_shy_down:
        xzoom -1
    with {'master': dissolve}
    anon "Ini luar biasa!"

    show anon a_sides
    with {'master': dissolve}
    show anon f_flirt_grin
    show eve a_hip b_naked f_happy:
        xoffset 100
        xzoom -1
    eve "hehe!"

    pause
    hide eve
    with {'master': dissolve}
    eve "Ayo, {b}[firstname]{/b}!"

    anon f_worried_surprised "aku datang!"

    show anon b_naked_undress_bottom
    with {'master': dissolve}
    pause

    label eveX2_post_eve.resume:
    scene location_tattoo_bathroom_shower
    show eve a_empty b_naked_shower f_normal_down:
        xoffset 250
        xzoom -1

    if M_eve.get('biggus_dickus'):
        show eve od_dick01
    else:
        show eve od_scar

    show eve_arms_naked_shower_a_scrub as eve_arms:
        xoffset 250
        xzoom -1
    show location_tattoo_bathroom_shower_steam as steam
    with fade
    pause
    show anon b_naked f_flirt_grin od_naked_dick1 behind eve
    with {'master': dissolve}





    show anon a_empty f_flirt:
        xoffset 90
    show anon_arms_naked_a_hips_eve as anon_arms behind eve_arms:
        xoffset 90
    show eve f_surprised_right
    show eve_arms_naked_shower_a_scrub02 as eve_arms
    with {'master': dissolve}
    eve "{i}*Terkesiap*{/i}"

    hide anon
    hide anon_arms
    show eve b_naked_shower_kiss f_happy_closed:
        xoffset -41
    hide eve_arms
    with {'master': dissolve}
    eve "Ya Tuhan, kamu pandai dalam hal itu!"


    if M_eve.get('biggus_dickus'):
        show eve od_dick_grow
        pause 1.5
        show eve od_dick03
        eve f_confused_low "Haah!"

    else:

        pause

    eve f_nervous "Masukkan ke dalam diriku, {b}[firstname]{/b}!"


    $ renpy.dynamic(gender='trans' if M_eve.get('biggus_dickus') else 'cis')
    call scene_eve_sex_shower.repeat (gender)
    $ unlock_scene('Eve', '08_unlocked', variant=gender)

    scene expression background(512, 280, 2.4, l=L_tattooparlor_bathroom) as stage
    show anon a_towel b_shorts f_looking_down:
        xoffset -75
    show eve a_dry_hair b_naked_shower f_happy_closed:
        xoffset 350
        xzoom -1

    if M_eve.get('biggus_dickus'):
        show eve od_dick01
    else:
        show eve od_scar

    with fade
    pause
    show anon b_dressed_changing
    with {'master': dissolve}
    pause
    show anon a_sides b_dressed f_happy
    with {'master': dissolve}
    anon "Ya, itu menyenangkan!"

    show eve f_nervous:
        xoffset -250
        xzoom 1
    with {'master': dissolve}
    eve "Ya, benar."

    pause
    anon "Kita harus melakukannya lagi suatu saat nanti."

    show eve a_towel_wrap01 b_naked f_normal
    with {'master': dissolve}
    eve "Hehe, benar sekali!"

    show eve a_towel_wrap02
    with {'master': dissolve}
    pause
    show eve a_sides b_towel f_sexy
    with {'master': dissolve}
    eve "Kemarilah."

    hide anon
    show eve b_towel_kiss:
        xoffset -350
    with {'master': dissolve}
    eve "MM."

    pause
    show anon a_sides f_shy:
        xoffset -75
    show eve b_towel f_confused:
        xoffset -250
    with {'master': dissolve}
    anon "Sebaiknya kau hentikan itu..."

    anon f_happy "... Atau kita mungkin akan kembali mandi lagi."

    eve f_happy @ f_laugh "hehe!"

    pause
    eve "Kurasa, sampai jumpa nanti?"

    show anon a_wave
    with {'master': dissolve}
    anon "Anda yakin."

    hide anon
    show eve a_hip:
        xoffset 375
        xzoom -1
    with {'master': dissolve}
    eve "Nanti, {b}[firstname]{/b}."

    anon "Sampai jumpa, {b}Malam{/b}."

    return


label eveX2_post_eve.grace:
    scene expression background(712, 400, 3.5, l=L_tattooparlor_apartment) as stage
    show anon a_surprised f_shy_low:
        xoffset 500
    show eve b_dressed_scared f_thinking_lip:
        xoffset 177
    with fade
    pause
    hide anon
    show eve b_dressed_kiss:
        xoffset 75
    with {'master': dissolve}
    pause
    show anon a_surprised_up f_flirt_low behind eve:
        xoffset 375
    show eve b_dressed_scared f_laugh:
        xoffset 52
    with {'master': dissolve}
    eve "hehe!"

    hide anon
    show eve b_dressed_kiss:
        xoffset -25
    with {'master': dissolve}
    pause
    show grace a_cover b_naked f_surprised:
        xzoom -1
    with {'master': dissolve}
    grace "{b}Malam{/b}!!"

    show anon a_surprised_up_both f_surprised behind eve:
        xoffset -150
        xzoom -1
    show eve b_dressed f_surprised:
        xoffset 0
        xzoom 1
    with {'master': fastdissolve}
    eve "Oh sial!"

    show eve f_nervous_right o_blush
    show grace f_uneasy
    with {'master': dissolve}
    eve @ -m_talk "Hmm..."

    show anon a_sides f_surprised_low
    show eve f_nervous
    with {'master': dissolve}
    eve "... Ups."

    show anon f_surprised_down o_boner
    with {'master': dissolve}
    eve "Maaf, Kak."

    show anon a_cover_boner f_surprised_teeth_down of_blush:
        xoffset -100
    with {'master': dissolve}
    eve "Saya lupa Anda berada di sini bermeditasi."

    show anon f_surprised_left
    show eve a_hoodless_remove1 b_dressed_hoodless
    with {'master': dissolve}
    grace "T-tidak, tidak apa-apa..."

    show anon f_surprised_down
    show eve a_idle
    with {'master': dissolve}
    grace "... lagipula ini rumahmu juga."

    show anon f_surprised
    grace f_embarrassed "Biarkan aku saja, umm-"

    show anon f_surprised_down
    grace "Aku akan memakai beberapa pakaian dan kita bisa-"

    show anon f_worried_left
    show eve f_normal -o_blush
    with {'master': dissolve}
    eve "{i}*Ahem*{/i} Tidak apa-apa, {b}Grace{/b}."

    eve f_happy "Kami hanya... melewatinya..."

    show anon f_shy_left
    show grace f_suspicious
    show eve f_nervous_right o_blush
    with {'master': dissolve}
    eve "... Dalam perjalanan ke... kamar mandi."

    grace f_sad_down "Oh."

    eve f_nervous_down "Yeeeeeah."

    show anon f_surprised_left
    pause
    show anon f_surprised_teeth_left
    eve f_surprised_down @ -m_talk "!!!"
    show anon f_worried_left
    show eve f_worried_back_down
    grace f_uneasy "Baiklah kalau begitu..."

    show anon f_worried
    grace "...Hanya, umm... hati-hati."

    eve @ -m_talk "Mhmm."

    show anon f_worried_left
    show eve a_up f_concerned behind anon:
        xoffset 50
    with {'master': dissolve}
    eve "Ayo, {b}[firstname]{/b}!"

    anon f_worried @ -m_talk "..."
    hide anon
    hide eve
    show grace f_sad:
        xoffset -550
        xzoom 1
    with {'master': dissolve}
    pause
    show grace a_vulnerable f_sad_down
    with {'master': dissolve}
    pause

    scene expression background(512, 280, 2.4, l=L_tattooparlor_bathroom) as stage
    show anon b_dressed_changing3:
        xzoom -1
    show eve b_naked_shower_pickup01:
        xoffset -150
    with fade
    pause
    show anon a_towel b_shorts f_shy_low
    with {'master': dissolve}
    anon "Ya, itu aneh."

    show eve b_naked_shower_pickup02
    with {'master': dissolve}
    eve "Ya."

    show anon a_sides f_worried_low
    with {'master': dissolve}
    pause
    anon "Kamu baik-baik saja?"

    show eve b_naked_shower_pickup01
    with {'master': dissolve}
    eve "Ya."

    pause
    anon f_confused_low "Apa kamu yakin?"

    anon "Karena sepertinya tidak-"

    show anon a_surprised f_surprised
    show eve b_naked f_concerned:
        xoffset 0
        xzoom -1

    if M_eve.get('biggus_dickus'):
        show eve od_dick01
    else:
        show eve od_scar

    with {'master': dissolve}
    eve "Saya bilang, saya baik-baik saja, {b}[firstname]{/b}!"

    pause
    show anon a_sides f_worried
    with {'master': dissolve}
    anon "Oh oke..."

    hide eve
    with {'master': dissolve}
    eve "Cepat buka celanamu."

    anon f_shy "Baiklah."

    show anon b_dressed_changing2
    with {'master': dissolve}
    pause
    jump eveX2_post_eve.resume
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
