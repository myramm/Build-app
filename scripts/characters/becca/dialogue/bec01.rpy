label bec01_talk_becca:
    pause
    show anon b_dressed_tall:
        offset (-110, 35)
    with dissolve
    show anon f_surprised
    show becca a_front b_home_bed f_surprised
    with {'master': fastdissolve}
    becca "{b}[firstname]{/b}?!"

    show anon a_wave
    with {'master': dissolve}
    pause
    becca "Apa yang kamu lakukan di sini?!"

    show anon a_behind_head f_shy
    with {'master': dissolve}
    anon "H-hei, {b}Becca{/b}."

    show becca a_crossed f_annoyed
    with {'master': dissolve}
    becca "Tidak, biar kutebak..."

    becca "... Kamu di sini untuk meniduri ibuku lagi."

    anon f_surprised @ -m_talk "!!!"
    show anon a_surprised_up_both
    with {'master': dissolve}
    anon "Ap- Tidak!!"

    pause
    anon f_worried "Hei, ayolah..."

    show anon a_sides
    with {'master': dissolve}
    anon "... Itu bukan apa-apa-"

    show becca b_home_bed_back
    with {'master': dissolve}
    becca "Simpan saja, aku melihatmu!"

    pause
    becca f_eyeroll "Eugh, dan yang lebih parah... {b}Nona{/b} melihatmu!"

    show becca b_home_bed
    with {'master': dissolve}
    becca f_annoyed "Wanita jalang itu tidak akan pernah membiarkanku melupakannya."

    anon f_shy "Dengar, aku benar-benar minta maaf... Aku tidak berniat berhubungan seks dengan ibumu, sungguh..."

    show becca a_hips f_disgusted
    with {'master': dissolve}
    becca "Oh, jadi itu hanya kecelakaan?!"

    anon f_worried "Yah, ehh... T-tidak, sebenarnya itu bukan kecelakaan..."

    anon "... Aku sebenarnya seharusnya mengantarkan pizza dan kemudian-"

    becca f_annoyed "Lalu apa, {b}[firstname]{/b}?!"

    becca "Kamu tersandung dan penismu jatuh terlebih dahulu ke dalam vagina ibuku?!"

    anon f_confused "Salah..."

    anon "... Tidak?"

    show anon f_worried
    show becca f_confused
    pause
    anon "Begini, bosku, {b}Tony{/b}..."

    anon "... Dia bilang ibumu adalah pelanggan yang sangat istimewa dan kepuasannya harus menjadi prioritas nomor satu saya."

    show becca f_shocked
    pause
    show anon a_shy_neck f_shy_down
    with {'master': dissolve}
    anon "Jadi, aku uhh... k-kita agak-"

    show anon a_surprised_up f_surprised
    show becca a_angry f_disgusted
    becca "EWWWW!!!" with hpunch
    show anon f_worried
    becca "Pamanku {b}Tony{/b} yang mengatur semua ini?!"

    show anon a_facepalm f_disgusted_wince
    with {'master': dissolve}
    pause
    show anon a_sides f_worried
    show becca a_front f_sad_down
    with {'master': dissolve}
    becca @ f_exhausted_closed -m_talk "{i}*Huh*{/i} Tolong, berhenti bicara."

    anon f_sad_down "Benar, maaf."

    pause
    show anon a_point_back f_worried
    with {'master': dissolve}
    anon "aku akan pergi saja..."

    show anon a_sides
    with {'master': dissolve}
    anon "... Dan uhh..."

    pause
    anon f_confused "... Semoga sampai jumpa akhir pekan ini di pantai?"

    show becca a_crossed b_home_bed_back f_annoyed
    with {'master': dissolve}
    becca "Pfft, kenapa harus?"

    becca f_upset "Jadi kalian semua bisa mengolok-olokku karena situasi kacau ini?"

    anon f_sad "{b}Becca{/b}..."

    pause
    show anon a_liu_shoulder f_worried:
        xoffset -50
    show becca f_glaring_back
    with dissolve
    anon "... Aku tidak akan pernah melakukan itu padamu."

    show becca b_home_bed f_sad
    with {'master': dissolve}
    pause
    show anon a_sides
    with {'master': dissolve}
    becca "Apakah kamu benar-benar peduli jika aku datang?"

    anon f_confused "Hah?"

    show becca a_front b_home_bed_back f_shy_low
    with {'master': dissolve}
    becca "Maksudku, aku cukup yakin {b}Roxxy{/b} jatuh cinta padamu..."

    show anon a_surprised_up_both f_surprised
    with {'master': dissolve}
    anon -m_talk "!!!"
    show anon a_up f_shock
    with {'master': fastdissolve}
    becca f_shy_down "... Dan {b}Missy{/b} naksir kamu sejak, misalnya, kelas tiga."

    anon f_surprised "S-dia punya?"

    show anon a_point_self
    show becca b_home_bed f_confused
    with {'master': dissolve}
    becca @ -m_talk "..."
    show becca f_eyeroll
    pause
    show becca a_hips f_annoyed
    with {'master': dissolve}
    becca "Jadi untuk apa kamu membutuhkanku, ya?!"

    show anon a_sides f_confused
    with {'master': dissolve}
    becca "Itu tidak cukup untukmu?"


    menu:
        "Kamu tidak suka menghabiskan waktu bersamaku?":
            call bec01_talk_becca.like
        "Tidak, aku menginginkanmu.":

            call bec01_talk_becca.want

    show anon a_up f_worried -of_blush
    with {'master': dissolve}
    anon "Tentu saja, apa saja... sebutkan saja."

    show anon a_sides
    show becca f_annoyed a_finger01
    with {'master': dissolve}
    becca "Pertama..."

    becca "... Aku tidak ingin lagi menginjakmu dan ibuku!"

    anon f_normal "Tidak masalah."

    show becca a_hips f_upset
    with {'master': dissolve}
    becca "Saya bersungguh-sungguh, {b}[firstname]{/b}!"

    show anon a_salute
    show becca f_glaring
    with {'master': dissolve}
    anon "Anggap saja sudah selesai."

    show anon f_worried
    pause
    show anon a_sides f_normal
    show becca f_annoyed a_finger02
    with {'master': dissolve}
    becca "Kedua..."

    becca "... Kamu harus bicara dengan {b}Nona{/b} dan katakan padanya dia tidak boleh mengungkitnya atau menggosok wajahku lagi!"

    show becca a_front
    with {'master': dissolve}
    anon f_worried "Itu-"

    anon @ f_skeptical "Bagaimana saya bisa mengaturnya?"

    becca f_annoyed "Jangan bodoh!"


    if M_missy.taken_dick:
        becca "Pelacur itu akan melakukan apa pun yang Anda perintahkan padanya... selama Anda berjanji untuk terus memberinya pukulan sesekali."

        anon f_confused "Memberinya tulang?"

    else:

        becca "Pelacur itu akan melakukan apa pun yang Anda perintahkan... selama Anda berjanji untuk memberinya tulang sesekali."

        anon f_confused "Lemparkan dia tulang?"


    becca f_normal "Ya, kamu tahu..."

    show becca a_finger_sex
    with {'master': dissolve}
    pause
    anon f_confused "Eh?"

    show becca a_hips f_annoyed
    with {'master': dissolve}
    becca "Seks, bodoh!"

    show anon f_thinking_down
    with {'master': dissolve}
    anon "Oh."

    show anon a_surprised_up f_surprised
    anon "OH!" with hpunch
    show anon a_sides f_shy_low
    with {'master': dissolve}
    anon "Benar."

    anon f_shy "Mengerti."

    becca @ f_eyeroll "Wow."

    pause
    show becca a_finger03 f_normal
    with {'master': dissolve}
    becca "Dan terakhir..."

    becca "... Saya ingin Anda mengatakan yang sebenarnya."

    anon f_confused "Kebenaran tentang apa?"

    show becca a_hips f_annoyed
    with {'master': dissolve}
    becca "Siapa di antara kita yang lebih baik?"

    show anon f_confused
    pause
    anon "Lebih baik?"

    show becca a_front
    with {'master': dissolve}
    becca "Ya."


    if M_missy.taken_dick:
        becca "Misalnya, dengan siapa Anda paling menikmati berhubungan seks?"

    else:
        becca "Misalnya, dengan siapa Anda paling menantikan untuk berhubungan seks?"


    anon f_worried "Oh, uhh..."


    $ renpy.dynamic(choice=set())

    menu bec01_talk_becca.choice:
        set choice
        "{b}Roxxy{/b} adalah yang terbaik.":

            $ choice.add("{b}Tina{/b} is best.")
            jump bec01_talk_becca.roxxy
        "{b}Becca{/b} adalah yang terbaik.":

            call bec01_talk_becca.becca
        "{b}Nona{/b} adalah yang terbaik.":

            call bec01_talk_becca.missy
        "{b}Tina{/b} yang terbaik.":

            jump bec01_talk_becca.tina

    anon f_confused "Hmm?"

    becca f_sexy "Tunggu."

    show anon a_surprised_shoulders f_surprised_down behind becca:
        xoffset -150
    show becca b_home_bed_reach
    hide books
    with {'master': dissolve}
    pause
    show anon a_sides f_surprised
    show becca a_phone b_home_bed f_sexy_low:
        xoffset 100
        xzoom -1
    with {'master': dissolve}
    anon "Apa yang sedang kamu lakukan?"

    show anon f_confused
    becca "Mengambil ponselku agar kita bisa menelepon {b}Roxxy{/b}."

    anon f_normal "Oh baiklah."

    anon f_surprised "Tunggu, apa?!"

    anon f_worried "Mengapa kita perlu menelepon {b}Roxxy{/b}?"

    show becca a_phone b_home_bed_back f_sexy
    with {'master': dissolve}
    becca "Karena kamu dan aku akan berhubungan seks dan {b}Roxxy{/b} ingin menonton..."

    anon a_surprised_up_both f_surprised "!!!"
    show becca b_home_bed f_sexy_low
    with {'master': dissolve}
    becca "... Dia sangat jelas tentang hal itu."

    show anon a_down b_dressed_floor_barefeet f_worried:
        offset (-85, -35)
    show becca a_phone_talk b_home_bed f_sexy as becca_head behind anon:
        crop (0, 0, 1024, 250)
        xoffset 100
        xzoom -1
    show becca a_phone_talk f_sexy:
        align (0., 1.)
        crop (0, 250, 1024, 768 - 250)
    with {'master': dissolve}
    "{i}*Dering* *Dering*{/i}"

    anon "Y-ya, oke... tapi-"

    show becca a_phone b_home_bed_back f_annoyed m_talk as becca_head
    show becca a_phone b_home_bed_back f_annoyed
    with {'master': dissolve}
    becca "Ssst!"

    show anon f_surprised
    show becca f_surprised -m_talk as becca_head
    show becca f_surprised
    with {'master': fastdissolve}
    "{i}*Dering* *Dering*{/i}"

    show anon f_surprised_left_low of_blush
    show becca f_shy_back_low o_blush
    show becca f_shy_back_low o_blush as becca_head
    with {'master': dissolve}
    pause
    show anon f_worried_low
    show becca b_home_bed f_shy_down:
        crop None
    hide becca_head
    with {'master': dissolve}
    "{i}*Dering* *Dering*{/i}"


    $ renpy.dynamic(local=ComposeTransition(phoneleft.show,
        before=MoveTransition(.7, time_warp=_warper.easein_cubic)))

    show location_tina_becca_bedroom_bed:
        xoffset 300
    show anon:
        xoffset 300 + -85
    show becca:
        xoffset 300 + 100
    show roxxy bed b_phone f_bored at Split(-15, 'left', offset=300).new:
        xoffset -300
    show expression phoneleft.core_bar as split
    with {'master': local}
    roxxy "Halo?"

    show anon f_worried
    show becca a_phone_talk f_shy
    with {'master': dissolve}
    becca "Hei, ini aku."

    roxxy "Oh, hei... ada apa?"

    becca f_shy_happy "Anda ingat apa yang kita bicarakan kemarin?"

    roxxy f_disgusted_out "Ugh, bukan soal bajingan yang diputihkan itu lagi..."

    show anon f_surprised -of_blush
    show becca f_disgusted -o_blush
    with {'master': dissolve}
    roxxy f_eyeroll "... {b}Nona{/b} sangat menjijikkan!"

    becca "Eww, tidak!"

    show anon f_confused
    show roxxy f_bored
    becca f_normal "Hal lainnya..."

    show becca f_shy_down o_blush
    with {'master': dissolve}
    becca "Anda tahu, tentang kami berhubungan seks dengan pacar Anda dan Anda menontonnya?"

    show anon f_shock
    roxxy f_smug "Oh ya."

    show anon f_worried
    show roxxy b_nails_phone f_horny_down
    with {'master': dissolve}
    roxxy "Bagaimana dengan itu?"

    show becca f_shy_back
    pause
    becca "Tunggu."

    show becca a_phone f_normal_down -o_blush
    with {'master': dissolve}
    roxxy f_suspicious "... Umm, oke?"

    show becca a_phone_facetime f_normal
    show roxxy f_bored_down
    with {'master': dissolve}
    becca "Di sana."

    becca "Bisakah kamu melihat kami?"

    show roxxy b_hangup f_suspicious
    with {'master': dissolve}
    roxxy "Hah?"

    show anon f_grin
    becca f_laugh "Heh, lihat ponselmu, dasar pelacur bodoh!"

    show anon f_normal
    show becca f_happy
    show roxxy b_facetime
    with {'master': dissolve}
    roxxy "Oh."

    show anon f_worried_surprised
    roxxy f_annoyed "Hei, apa yang {b}[firstname]{/b} lakukan di sana?!"

    becca f_happy "Tenang, dia bekerja untuk pamanku {b}Tony{/b}..."

    show anon f_worried
    becca "... Kamu tahu, orang yang tinggal di seberang aula dariku?"

    roxxy f_suspicious "Pria gendut berkumis?"

    show becca f_annoyed
    pause
    becca "{b}Tony{/b} tidak gemuk, dia hanya berperawakan besar."

    roxxy f_smug "Ya benar."

    roxxy "Itu hanya perkataan orang gemuk untuk membuat dirinya merasa lebih baik."

    show anon f_surprised
    show becca f_upset
    pause
    becca f_annoyed "Ugh, terserahlah... itu tidak penting."

    show anon f_worried
    becca f_normal "Begini, {b}Tony{/b} mengirimnya untuk membantu ibuku melakukan sesuatu."

    roxxy f_suspicious @ -m_talk "Mhmm?"

    becca f_shy_down "Tapi dia sudah selesai dengan itu sekarang dan aku agak berpikir... kau tahu... karena dia ada di sini dan sebagainya..."

    roxxy f_horny @ f_smug "Oh, kamu jalang yang haus!"

    show anon f_brag
    becca f_shy_happy "Maksudku, mengapa menyia-nyiakan kesempatan ini?"

    show roxxy f_horny_lipbite
    pause
    roxxy f_eyeroll "Baiklah baiklah."

    roxxy f_horny "Tapi kamu harus mengatakannya!"

    show becca f_concerned
    anon f_confused "Apa yang terjadi saat ini?"

    becca "Aww, kamu serius tentang itu?"

    show anon f_surprised
    show becca a_phone_facetime b_home_bed_back f_concerned_lipbite as becca_head behind anon:
        crop (0, 0, 1024, 250)
        xoffset 100 + 300
        xzoom -1
    show becca a_phone_facetime b_home_bed_back f_concerned_lipbite:
        align (0., 1.)
        crop (0, 250, 1024, 768 - 250)
    with {'master': dissolve}
    pause
    show becca o_blush as becca_head
    show becca o_blush
    with {'master': dissolve}
    roxxy @ f_annoyed "{b}Becca{/b} katakan!"

    show anon f_confused
    show becca b_home_bed f_shy_low:
        crop None
    hide becca_head
    with {'master': dissolve}
    pause
    becca f_shy_down "Aku seorang jalang beta yang terangsang..."

    show anon f_surprised
    show roxxy f_horny_lipbite
    becca "... Dan kamu adalah alfaku..."

    pause
    show roxxy b_rub
    with {'master': dissolve}
    becca "... Maukah kamu mengizinkan pacarmu melakukan apa yang diinginkannya bersamaku?"

    show roxxy f_horny_lipbite_close
    anon f_shock "..."
    roxxy f_smug "Hehehe!"

    show anon f_surprised
    roxxy f_horny "Persetan, itu panas!"

    show roxxy b_facetime
    with {'master': dissolve}
    roxxy "Baiklah, silakan."

    becca f_shy_happy "Terima kasih!"

    show anon f_brag
    roxxy "Tapi sebaiknya Anda mencari tempat yang bagus untuk telepon!"

    roxxy "Aku ingin bisa melihat semuanya."

    becca "Ya, aku akan... tunggu."

    hide becca
    with {'master': dissolve}
    anon f_worried "Apakah ini serius terjadi?"


    scene location_tina_becca_bedroom_evening:
        anchor (712, 400)
        pos (.5, .5)
        transform_anchor True
        zoom 2.5
    show anon b_onbed_back:
        offset (105, 28)
        yalign 1.
        zoom .85
    show cam
    show roxxy bed b_facetime f_horny_out:
        align (1., 0.)
        crop (275, 90, 1 / .7 * 1024 / 4.2, 1 / .7 * 768 / 4.2)
        offset (-45, 35)
        xzoom -1
        zoom .7
    with fade
    roxxy "Ya, ini sedang terjadi."

    roxxy "Membuktikan sekali lagi bahwa saya adalah pacar terhebat di dunia {i}dan{/i} sahabat!"

    show anon f_shy
    show becca b_home_bed f_concerned_lipbite o_blush behind cam:
        offset (175, 170)
        zoom .9
    show roxxy b_nails f_bored_down
    with {'master': dissolve}
    roxxy "Ditambah lagi, aku agak terjebak di kamarku sekarang dan bosan sekali."

    show becca b_home_bed_undress a_remove_top01
    with {'master': dissolve}
    pause
    show anon f_flirt_low
    show becca a_remove_top02 -o_blush
    show roxxy b_facetime f_annoyed_right
    with {'master': dissolve}
    roxxy "Ibuku mengundang sepupuku yang bodoh lagi dan mereka duduk di luar sambil minum dan membersihkan senjatanya."

    show becca a_remove_top03
    with dissolve
    show becca a_remove_top04
    with {'master': dissolve}
    anon "Ehh, {b}Roxxy{/b}?"

    show anon a_side
    show becca a_sides b_pants_bed
    show roxxy b_nails f_bored_down
    with {'master': dissolve}
    roxxy "Aku bersumpah, aku tidak sabar untuk mendapatkan tempatku sendiri..."

    show anon f_surprised_low
    show becca b_home_bed_remove_bottom01
    with {'master': dissolve}
    roxxy "... Di mana pun pasti lebih baik daripada trailer kumuh ini, bahkan seperti-"

    show becca b_home_bed_remove_bottom02
    with {'master': dissolve}
    anon "{b}Roxxy{/b}?!!"

    show anon f_surprised
    show becca b_naked_bed a_front f_shy_happy_down o_blush
    show roxxy b_lolipop f_horny_lolipop
    with {'master': dissolve}
    roxxy @ -m_talk "Hmm?"

    show roxxy f_curious_lolipop_out
    with {'master': dissolve}
    anon f_flirt "A-apakah menurutku-"

    show roxxy b_facetime f_happy_out
    with {'master': dissolve}
    roxxy "Oh, dia SANGAT menginginkan penis itu, haha..."

    anon "{i}*Gulp*{/i} K-kamu ingin aku-"

    roxxy f_horny_out "... Persetan dengannya, {b}[firstname]{/b}."

    roxxy "Dan saya akan menonton."

    show roxxy f_horny_lipbite_out
    anon f_surprised "Sungguh?"

    roxxy @ f_horny_out -m_talk "Mhmm."

    show anon f_flirt of_blush
    with {'master': dissolve}
    anon "Itu yang kamu inginkan, {b}Becca{/b}?"

    show becca f_concerned_lipbite_low
    pause
    becca f_shy_happy "Ya."

    roxxy f_curious_out "Ayo sayang... tunggu apa lagi?!"

    roxxy f_horny_out "Lepaskan pakaian itu dan hancurkan dia!"

    show becca f_concerned_lipbite
    show roxxy f_horny_lipbite_out
    anon "Y-ya, oke."

    show anon b_onbed_sit_changing3 -of_blush:
        offset (-330, 28)
        yalign 1.
        xzoom -1
    with {'master': dissolve}
    pause
    show anon a_towel b_shorts f_flirt_down:
        reset
        offset (-500, 0)
        xzoom -1
        yalign 1.
        zoom .95
    show becca a_sides
    with {'master': dissolve}
    pause
    show anon b_dressed_changing2:
        offset (0, 0)
        xzoom 1
        yalign 1.
    show anon_overlay_o_underwear_boner1 as boner behind cam:
        offset (30, 75)
        zoom .95
    show becca f_concerned_lipbite_low
    with {'master': dissolve}
    pause
    hide boner
    show anon b_naked_undress_bottom o_boner
    show becca f_shocked_down
    show roxxy f_happy_out m_talk
    with {'master': dissolve}
    pause
    show anon a_sides b_naked f_shy od_naked_dick3 -o_boner
    show becca a_front f_concerned_low m_talk
    show roxxy f_horny_lipbite_close -m_talk
    with {'master': dissolve}
    roxxy @ -m_talk "MM."

    show anon a_behind f_shy_left
    with {'master': dissolve}
    roxxy f_horny_out "Ya, kamu menginginkan penis itu, bukan {b}Becca{/b}?"

    show anon of_blush
    show becca f_sexy_low -m_talk
    with {'master': dissolve}
    pause
    becca f_sexy_low "Y-ya."

    roxxy "Siapa itu kontolnya?"

    show becca b_naked_bed_back f_annoyed
    with {'master': dissolve}
    becca "Milikmu."

    roxxy f_smug_out "Lebih keras!"

    becca @ f_annoyed_surprised "Itu penismu, {b}Roxxy{/b}!"

    show anon f_surprised
    roxxy f_happy_out "Hehe, gadis baik..."

    show anon f_happy
    show becca b_naked_bed f_concerned_lipbite_low
    with {'master': dissolve}
    roxxy f_smug_out "... Sekarang tidurlah, {b}[firstname]{/b}."

    roxxy "Aku ingin dia menunggangimu."

    show anon a_sides f_shy
    with {'master': dissolve}
    anon "B-benar, um..."

    anon f_flirt "... Ini luar biasa!"

    show anon f_grin
    roxxy f_laugh "hehe!"


    call scene_becca_sex_bedroom.repeat
    $ unlock_scene('becca', '03_unlocked')

    scene location_trailer_bedroom_facetime as underlay:
        yoffset -90
    show roxxy bed b_stomach c_stomach f_horny o_wet:
        yoffset -90

    $ renpy.dynamic(local=Split(10.5, 'top', offset=-55),
                    stage='location_tina_becca_bedroom_bed')
    show expression stage as stage
    show anon b_naked_bed_mount
    show becca b_naked_disheveled_bed_mount f_exhausted_closed
    with fade
    becca @ -m_talk "*Bergumam tak jelas*"

    show becca b_naked_disheveled_bed_belly behind anon
    roxxy "!!!" with hpunch
    roxxy "Um, apakah dia baik-baik saja?"

    anon @ -m_talk "Hmm?"

    show anon b_sit_naked f_shock_low od_dick1:
        offset (-250, 15)
    with {'master': dissolve}
    anon "!!!"
    show anon b_sit_naked_check f_surprised_teeth_low od_naked_dick1 behind becca:
        offset (0, -30)
    with {'master': dissolve}
    roxxy "Ya Tuhan, kamu membunuhnya dengan penismu!"

    anon f_worried "T-tidak..."

    anon f_worried_low "... Dia masih bergerak-gerak..."

    roxxy "Hahahaah!"

    anon f_confused_low "... menurutku?"

    pause
    anon "... {b}Becca{/b}?"

    show anon f_surprised_down
    show becca a_shoo
    with {'master': dissolve}
    becca @ -m_talk "{i}* Merengek*{/i}"

    show anon f_worried_low
    show becca -a_shoo
    with {'master': dissolve}
    pause
    show anon b_liu_naked f_confused_low -od_naked_dick1:
        offset (-300, -50)
    with dissolve
    roxxy "Panas sekali, {b}[firstname]{/b}..."

    roxxy "... Aku suka melihatmu bercinta dengan teman-temanku!"

    anon "Um, ya... baiklah..."

    anon f_worried "... Haruskah kita lebih mengkhawatirkannya?"

    roxxy "Tidak, dia baik-baik saja..."

    show anon f_worried_low
    roxxy "... Bukankah begitu, pelacur bodoh?!"

    becca f_thinking "Ugh... diamlah, {b}Roxxy{/b}..."

    show anon f_worried
    roxxy "Lihat!"

    show becca a_reach f_upset with {'master': dissolve}
    anon f_flirt_low "Kupikir kami kehilanganmu sebentar."

    becca f_shy_back_low "T-tidak."

    becca "Itu hanya, sungguh..."

    show anon f_grin
    show becca f_shy_back_down o_blush
    with {'master': dissolve}
    becca "... {i}sungguh{/i}, intens."

    show becca a_phone f_shy
    with dissolve
    show expression stage as stage at local with {'master': local.show}
    roxxy "hehe!"

    roxxy "{b}Becca{/b}, lucu sekali melihatmu mencoba mengambil penis besar pacarku..."

    show anon f_surprised_low of_blush
    show roxxy f_horny_lipbite
    with {'master': dissolve}
    becca f_surprised @ -m_talk "..."
    roxxy f_happy "Dia benar-benar menidurimu tanpa alasan dengan itu!"

    show anon f_flirt_low
    becca f_annoyed "Tidak, dia tidak melakukannya!"

    roxxy f_smug "Ya, benar!"

    roxxy "Heh, kamu baru saja jatuh ke dalam kekacauan yang gagap..."

    show anon f_worried_low -of_blush
    with {'master': dissolve}
    becca f_upset "Grr!"

    roxxy f_laugh m_talk "Hahahaah!"

    anon "Baiklah, itu sudah cukup."

    show becca f_shy_back_low
    anon "Tidak ada alasan untuk-"

    roxxy f_horny -m_talk "{i}*Mendengus*{/i} Maaf tapi ini lucu..."

    show becca f_upset
    if M_missy.taken_dick:
        show anon f_surprised_teeth_low
        roxxy f_smug "... Bahkan {b}Missy{/b} menganggapnya lebih baik darinya!"

    show roxxy f_laugh m_talk
    becca "Persetan denganmu, {b}Roxxy{/b}!!"

    crystal "{b}Roxanne{/b}, sepupumu akan pergi!!"

    show anon f_surprised_low
    show becca f_surprised
    roxxy f_annoyed_right -m_talk @ f_bored "Oh, tidak... jangan sekarang."

    pause
    show anon f_worried_low
    show becca f_concerned
    crystal "Ya, dengar aku?"

    roxxy "Ya, aku mendengarmu!"

    crystal "Baiklah, ayo... bangunlah dan ucapkan selamat tinggal padanya sebelum dia pergi!"

    show anon f_confused_low
    show becca f_confused
    roxxy f_eyeroll "Eh, tidak, terima kasih."

    crystal "Ngomong-ngomong, dengan siapa kamu di sini mengobrol?"

    roxxy f_annoyed_right "Bukan urusanmu, Bu..."

    show anon f_surprised_low
    show becca f_surprised
    crystal "Sekarang jangan bicara padaku, nona muda!"

    show becca f_smug
    roxxy b_hangup c_hangup f_annoyed "Pergilah!!"

    crystal "Aku bersumpah, aku akan memilihkan tombol untukku dan menghajarmu habis-habisan!"

    show anon f_surprised_teeth_low
    show becca f_laugh
    roxxy f_angry "Grr!!"

    hide roxxy
    with {'master': fastdissolve}
    roxxy "Kenapa kamu selalu harus membuatku malu di depan teman-temanku, kamu-"

    show expression stage as stage with {'master': local.hide}
    "{i}*Bip*{/i}"

    show becca f_smug
    anon f_surprised_low "Oh oke..."

    show becca a_reach with {'master': dissolve}
    becca "Heh, layani dia dengan benar!"

    show anon a_surprised b_sit_naked_up f_normal_low od_naked_dick1 behind becca:
        offset (-30, -30)
    show becca a_down
    with {'master': dissolve}
    anon "...Saya kira, saya mungkin harus pergi juga."

    show anon f_surprised_low
    show becca b_naked_disheveled_bed_up f_thinking
    with {'master': dissolve}
    becca "Ya baiklah."

    anon f_shy_low "Anda akan berada di pantai akhir pekan ini, bukan?"

    becca f_shy_happy_up @ -m_talk "Mhmm."

    becca "Saya akan berada di sana."

    anon f_flirt_low "Dingin."

    hide anon
    show becca f_concerned
    with {'master': dissolve}
    anon "Nanti, {b}Becca{/b}."

    show becca f_concerned_lipbite
    with {'master': dissolve}
    pause

    scene expression background(512, 368, 2) as stage
    show anon a_towel b_shorts f_looking_down:
        xoffset -250
        xzoom -1
    with fade
    pause
    show anon b_dressed_changing
    show becca b_naked_disheveled f_concerned
    with {'master': dissolve}
    becca "Tunggu!"

    show anon a_sides b_dressed f_surprised:
        xoffset 250
        xzoom 1
    with {'master': dissolve}
    anon @ -m_talk "Hmm?"

    hide anon
    show becca b_naked_disheveled_kiss:
        xoffset 150
    with {'master': dissolve}
    anon "Mmmm!"

    pause
    show anon a_sides f_surprised behind becca:
        xoffset 75
    show becca b_naked_disheveled f_shy o_blush:
        xoffset -225
    with dissolve
    anon "A-untuk apa itu?"

    becca @ f_shy_down "Tidak ada alasan, aku hanya-"

    becca f_shy_happy "Ini menyenangkan."

    show anon a_handshake f_shy
    with {'master': dissolve}
    anon "Ya, benar."

    becca "Kita harus melakukannya lagi suatu saat nanti."

    anon "Benar-benar?"

    becca "Ya."

    becca f_shy_down "Hanya, um..."

    becca "... Jangan beritahu siapa pun, oke?"

    anon @ f_happy "Heh maksudnya selain {b}Roxxy{/b} dan {b}Missy{/b}."

    becca f_concerned @ f_annoyed "Ya, ya... tentu saja."

    anon "Baiklah."

    show becca f_shy_happy
    anon "Tidak masalah."

    becca "Terima kasih, {b}[firstname]{/b}."

    show anon a_sides with {'master': dissolve}
    anon "Sampai jumpa lagi."

    hide anon
    with {'master': dissolve}
    becca "Nanti."

    show becca f_sexy_low
    with {'master': dissolve}
    pause
    show becca a_squeeze f_sexy_lipbite
    with dissolve
    pause

    scene expression background(l=L_apt_hall3) as stage with fade
    show anon f_happy with dissolve:
        xoffset 250
    anon @ -m_talk "(Yah, menurutku ini berarti aku bisa mampir ke {b}Tina{/b} dan jalan-jalan dengan {b}Becca{/b} kapan pun aku mau sekarang... )"

    anon f_grin @ -m_talk "(... Betapa hebatnya itu?! )"

    pause
    anon f_thinking @ -m_talk "(Aku hanya harus berhati-hati saat berada di dekat ibunya.)"

    anon f_thinking_down @ -m_talk "( Siapa yang tahu bagaimana reaksi {b}Tina{/b} jika dia mengetahui apa yang kita lakukan... )"

    hide anon with dissolve
    return 'afterglow'


label bec01_talk_becca.like:
    anon f_worried "Kamu tidak suka menghabiskan waktu bersamaku?"

    becca f_concerned "Entahlah..."

    show becca a_crossed b_home_bed_back f_shy_low
    with {'master': dissolve}
    pause
    show anon f_shy
    becca "... Mungkin sedikit..."

    pause
    show anon a_surprised_up_both f_surprised_teeth
    show becca b_home_bed f_glaring
    becca @ f_upset "... Before you started boning my mom, you jerk!" with hpunch
    anon f_surprised "Aku bilang aku minta maaf, bukan?"

    show anon a_sides
    with {'master': dissolve}
    pause
    anon f_worried "Serius, {b}Becca{/b}... jika aku tahu dia adalah ibumu, aku tidak akan pernah-"

    becca f_eyeroll "Ya, terserah."

    show becca a_front f_sad_down
    with {'master': dissolve}
    becca @ -m_talk "{i}*Huh*{/i}"

    pause
    becca f_annoyed "Kurasa... Aku akan mempertimbangkan untuk terus hadir di permainan kecil kita di pantai..."

    show becca a_hips
    with {'master': dissolve}
    becca "...Tetapi hanya jika Anda menyetujui tiga syarat!"

    return


label bec01_talk_becca.want:
    anon "Tidak."

    anon f_shy "Aku datang ke pantai untukmu."

    show becca a_angry f_surprised
    with {'master': fastdissolve}
    becca @ -m_talk "!!!"
    show becca a_front f_shy_down
    with {'master': dissolve}
    becca "K-kamu hanya mempermainkanku..."

    anon f_worried "Tidak, aku serius!"

    anon "Dengar, {b}Roxxy{/b} dan aku punya barang spesial kami sendiri... dan itu bagus sekali..."

    anon "... Dan {b}Missy{/b} bagus dan semuanya..."

    show anon a_liu_shoulder f_shy
    with {'master': dissolve}
    anon "... Tapi kaulah orang yang paling aku nantikan untuk bertemu di malam-malam itu."

    show becca f_shy o_blush
    with {'master': dissolve}
    becca "Anda melakukannya?"

    anon "Ya."

    pause
    show anon a_behind_head of_blush
    with {'master': dissolve}
    anon "Kamu benar-benar seksi, tahu?"

    show becca a_crossed b_home_bed_back f_shy_down
    with {'master': dissolve}
    becca "Itu-"

    show becca f_shy_low
    pause
    show anon a_sides
    with {'master': dissolve}
    becca "aku uhh-"

    show becca b_home_bed f_shy_happy_down
    with {'master': dissolve}
    pause
    show becca a_front f_exhausted_closed
    with {'master': dissolve}
    becca @ -m_talk "{i}*Huh*{/i}"

    becca f_shy "Kurasa... Aku bisa terus muncul di permainan kecil kita di pantai..."

    show becca -o_blush
    with {'master': dissolve}
    becca "... T-tapi hanya jika kamu menyetujui tiga syarat!"

    return


label bec01_talk_becca.becca:
    anon f_normal "Tentu saja kamu yang terbaik."

    show becca a_front f_shy_happy o_blush
    with {'master': dissolve}
    becca "Saya?"

    anon "Oh, ya... tidak ada kontes."

    becca f_happy @ f_laugh -m_talk "Hehe, aku tahu itu!"

    becca "Aku tahu aku lebih baik dari bajingan kecil kurus itu!"

    anon f_shy "Di sana, lihat..."

    anon "... kamu merasa lebih baik sekarang, kan?"

    show anon f_happy
    becca @ f_laugh -m_talk "Ya, jauh lebih baik."

    anon @ f_laugh -m_talk "Bahagia {b}Becca{/b} yang terbaik {b}Becca{/b}."

    becca @ f_laugh -m_talk "hehe!"

    anon f_normal "Jadi kita baik-baik saja sekarang?"

    anon "Anda akan berada di pantai akhir pekan ini bersama yang lain?"

    becca f_shy_happy "Ya, saya kira."

    show becca f_shy_happy_up -o_blush
    with {'master': dissolve}
    becca "Meskipun..."

    becca f_sexy "... Sekarang setelah kamu mengatakan aku yang terbaik, aku ingin merayakannya!"

    return


label bec01_talk_becca.missy:
    show anon a_fists f_normal
    with {'master': dissolve}
    anon "Saya harus memilih {b}Missy{/b}."

    becca f_concerned "A-apa?!"

    anon "Ya."

    show anon a_sides f_worried
    show becca a_front f_sad_down
    with {'master': dissolve}
    pause
    anon "Maksudku, jangan salah paham... kamu dan {b}Roxxy{/b} sangat seksi..."

    anon f_shy "... Seperti {i}super duper{/i} panas!"

    becca f_confused "Super duper?"

    show anon f_normal

    if M_missy.taken_dick:
        anon "Tapi {b}Missy{/b} benar-benar melakukan upaya ekstra saat kami berhubungan seks..."

    else:
        anon "Tapi {b}Missy{/b} sangat antusias dengan hal itu..."


    anon f_happy "... Dan dia membuatku tertawa...."

    becca @ f_eyeroll "Ya."

    show anon a_shy_neck f_shy_high
    with {'master': dissolve}
    anon "... Dan ya Tuhan, kaki itu..."

    show anon a_cold of_blush
    show becca f_disgusted
    with {'master': dissolve}
    anon "... Terkadang aku hanya ingin dia melingkarkannya di kepalaku dan memeras kehidupan keluar dari diriku."

    becca "Baiklah, baiklah, aku mengerti..."

    show anon a_shy_neck f_worried
    show becca a_crossed
    with {'master': dissolve}
    becca f_annoyed "... Diamlah, astaga!"

    show becca f_thinking
    pause
    show anon a_sides f_confused -of_blush
    show becca a_front f_normal
    with {'master': dissolve}
    becca "Mungkin aku hanya perlu berusaha lebih keras?"

    return


label bec01_talk_becca.roxxy:
    anon f_normal "Saya harus memilih {b}Roxxy{/b}."

    becca f_annoyed @ f_eyeroll "Yaa... Tentu saja, {b}Roxxy{/b}..."

    show anon a_behind_head f_shy
    with {'master': dissolve}
    anon "Itu tidak berarti kamu tidak hebat... t-karena kamu benar-benar hebat!!"

    anon "... Hanya saja, {b}Roxxy{/b} dan saya baru saja memiliki koneksi ini, Anda tahu?"

    show becca a_hips
    with {'master': dissolve}
    becca "... Maksudku antara {b}Nona{/b} dan aku!!"

    show anon a_sides f_worried
    with {'master': dissolve}
    anon "Oh."

    pause
    anon f_thinking "Nah, kalau begitu..."

    jump bec01_talk_becca.choice


label bec01_talk_becca.tina:
    show anon a_thinking f_thinking
    with {'master': dissolve}
    pause
    anon "Ibumu, mungkin?"

    becca f_surprised m_talk "!!!"
    anon f_shy_high "Dia sangat agresif pada awalnya, yang sedikit menakutkan..."

    show anon a_sides f_brag
    with {'master': dissolve}
    anon "... Tapi dengan cara yang fantastis dan sangat panas... Anda tahu?"

    show becca a_crossed f_glaring -m_talk
    with {'master': dissolve}
    anon f_happy "... Dan payudara itu... Maksudku, ya Tuhan... itu seperti sepasang kursi bean bag..."

    anon "... Bagaimana dia bisa menemukan bra yang cukup besar untuk-"

    show anon a_surprised_up_both f_surprised_teeth
    show becca a_angry f_upset_yelling
    becca "Okay, you're a fucking asshole!!!" with hpunch
    show becca a_hips f_glaring
    with {'master': dissolve}
    pause
    show anon a_sides f_worried
    with {'master': dissolve}
    anon "Wah santai..."

    anon f_shy "... Aku hanya bercanda."

    show becca a_crossed f_annoyed
    becca "Ya, tidak lucu, {b}[firstname]{/b}."

    show anon a_frustrated f_normal
    with {'master': dissolve}
    anon "Oh, ayolah... Itu sedikit lucu..."

    show becca f_glaring
    pause
    anon f_shy "Tidak?"

    pause
    show anon a_sides f_worried_low
    with {'master': dissolve}
    anon "Oke, oke... Maafkan aku."

    anon f_worried "Sebenarnya, yang terbaik adalah..."

    jump bec01_talk_becca.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
