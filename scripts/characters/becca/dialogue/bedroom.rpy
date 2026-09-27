label becca_button_bedroom:
    pause
    show anon b_dressed_tall:
        offset (-110, 35)
    with dissolve
    show becca a_front b_home_bed f_confused
    with {'master': dissolve}
    becca "{b}[firstname]{/b}?"

    show anon a_wave
    with {'master': dissolve}
    anon "Hai, {b}Becca{/b}."

    becca "Apa yang kamu lakukan di sini?"

    show anon a_sides
    with {'master': dissolve}

    menu becca_button_bedroom.choice:
        "Saya berada di lingkungan itu.":
            jump becca_button_bedroom.area
        "Apa yang sedang kamu kerjakan?":

            jump becca_button_bedroom.work
        "Seks.":

            jump becca_button_bedroom.sex
        "Hanya menyapa.":

            pass

    anon "Anda akan berada di pantai akhir pekan ini, bukan?"

    becca f_confused "Hmm, ya?"

    becca "Mengapa saya tidak berada di sana?"

    anon f_shy "Entahlah, aku hanya memastikan saja."

    pause
    show anon a_shy_neck f_shy_left
    show becca a_front f_surprised
    with {'master': dissolve}
    pause
    anon "Aku sangat menantikannya, tahu?"

    show becca a_front f_shy_down o_blush
    with {'master': dissolve}
    becca "Oh, um..."

    show anon f_shy
    show becca b_home_bed_back f_shy_low
    with {'master': dissolve}
    pause
    show becca f_shy_down
    becca "... Y-ya, aku juga."

    show anon a_cheering f_grin
    with {'master': dissolve}
    pause
    show anon a_surprised_shoulders f_surprised_teeth
    with {'master': dissolve}
    pause
    show anon a_sides f_shy
    with {'master': dissolve}
    anon "C-keren!"

    anon f_happy "Kurasa, sampai jumpa di sana!"

    show becca b_home_bed f_shy_happy
    with {'master': dissolve}
    becca "Sampai jumpa, {b}[firstname]{/b}."

    hide anon
    show becca f_concerned_lipbite
    with {'master': dissolve}
    pause
    return


label becca_button_bedroom.area:
    anon "Kupikir aku akan mampir dan menyapa."

    show becca a_crossed
    with {'master': dissolve}
    becca @ -m_talk "Mhmm."

    becca f_annoyed "Sebaiknya kau tidak melakukan hal-hal buruk lagi dengan ibuku."

    show anon a_behind_head f_worried
    with {'master': dissolve}
    anon "Oh, ehh..."


    menu:
        "Tentu saja tidak.":
            pass
        "Saya tidak akan menyebutnya jahat...":

            jump becca_button_bedroom.troll

    anon f_shy "Sudah kubilang, itu hanya kesalahpahaman sederhana."

    becca f_eyeroll "Ya, terserah."

    show becca a_front f_annoyed
    with {'master': dissolve}
    becca "Hanya... diam."

    anon "Baiklah."

    show anon a_sides
    with {'master': dissolve}
    jump becca_button_bedroom.choice


label becca_button_bedroom.sex:
    show anon a_shy_neck f_shy_left
    with {'master': dissolve}
    anon "Katakanlah, ingat suatu hari ketika kita uhh... kamu tahu?"

    becca f_confused @ -m_talk "Hmm?"

    anon f_shy "Saat kami melakukan facetime {b}Roxxy{/b}..."

    show anon of_blush
    with {'master': dissolve}
    anon "... Jadi dia bisa mengawasi kita... uhh..."

    show becca a_front f_shy_down o_blush
    with {'master': dissolve}
    becca "Oh itu."

    show anon a_sides
    with {'master': dissolve}
    anon "Y-ya."

    becca f_shy "Anda ingin melakukannya lagi?"

    anon f_worried "Maksudku, jika kamu tidak mau, aku mengerti-"

    becca f_concerned "T-tidak, aku bersedia!"

    show becca b_home_bed_back f_shy_low
    with {'master': dissolve}
    becca "Atau, uhh... Maksudku, kita bisa..."

    becca f_shy_happy_down @ f_shy_down "... K-karena, kamu tahu, itu lebih baik daripada mengerjakan pekerjaan rumah."

    anon f_shy "Benar."

    show becca b_home_bed f_concerned_lipbite_low
    with {'master': dissolve}
    pause
    show anon f_normal -of_blush
    show becca f_concerned -o_blush
    with {'master': dissolve}
    becca "Mari kita lihat apakah {b}Roxxy{/b} ada di rumah terlebih dahulu."

    show anon a_surprised_shoulders f_surprised_down behind becca:
        xoffset -150
    show becca b_home_bed_reach
    hide books
    with {'master': dissolve}
    pause
    show anon a_sides f_shy
    show becca a_phone b_home_bed f_normal_down:
        xoffset 100
        xzoom -1
    with {'master': dissolve}
    pause
    show anon a_down b_dressed_floor_barefeet f_normal:
        offset (-85, -35)
    show becca a_phone_talk f_shy
    with {'master': dissolve}
    "{i}*Dering* *Dering*{/i}"

    pause
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

    becca "Hei, ini aku."

    roxxy "Oh, hei... ada apa?"

    show becca f_shy_back o_blush
    with {'master': dissolve}
    becca "Umm, jadi... pacarmu ada di sini lagi dan kami berpikir-"

    roxxy f_annoyed "{b}[firstname]{/b} ada di sana lagi?!"

    show anon f_worried_surprised
    becca f_concerned "Ya, ya... Maksudku, dia hanya ada di lingkungan sekitar dan mampir untuk menyapa, kau tahu?"

    show anon f_worried
    roxxy f_suspicious "Eh ya."

    pause
    roxxy f_smug "Dan coba kutebak, kamu mau mencicipi lagi penis lezat itu?"

    show anon f_flirt_grin
    becca f_shy_back "Umm... m-agak..."

    show roxxy b_nails_phone f_bored_down
    with {'master': dissolve}
    roxxy "Ya, kedengarannya tidak terlalu meyakinkan."

    show anon f_worried
    becca f_concerned "Tolong, {b}Roxxy{/b}?"

    roxxy f_smug_out "Ayolah, kamu tahu apa yang ingin aku dengar..."

    show anon f_shy
    show becca f_shy_down
    pause
    becca "Aku seorang jalang beta yang terangsang..."

    show roxxy f_horny_lipbite_out
    becca "... Dan kamu adalah alfaku..."

    pause
    becca "... Maukah kamu mengizinkan pacarmu melakukan apa yang diinginkannya bersamaku?"

    show anon f_grin
    show roxxy f_horny_lipbite_close
    pause
    show roxxy b_phone f_smug
    with {'master': dissolve}
    roxxy "Ha ha ha!"

    show anon f_happy
    roxxy f_horny "Baiklah, baiklah..."

    roxxy f_smug "... Tapi tatap aku lagi supaya aku bisa menonton."

    becca f_shy "Y-ya, oke."

    hide becca
    with {'master': dissolve}
    anon "Jadi kita melakukan ini?"


    scene location_tina_becca_bedroom_evening:
        anchor (712, 400)
        pos (.5, .5)
        transform_anchor True
        zoom 2.5
    show anon b_onbed_back f_happy:
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
    roxxy "Ya, Anda bisa melakukannya..."

    show anon f_shy
    show becca b_home_bed f_concerned_lipbite o_blush behind cam:
        offset (175, 170)
        zoom .9
    with {'master': dissolve}
    roxxy "... Tapi saya harap Anda menghargai betapa luar biasa pacar yang Anda miliki!"

    anon f_flirt "Tentu saja saya mengapresiasi {b}Roxxy{/b}..."

    show becca b_home_bed_undress a_remove_top01
    with {'master': dissolve}
    anon "... Kamu yang terbaik!"

    show anon f_flirt_low
    show becca a_remove_top02 -o_blush
    with {'master': dissolve}
    roxxy f_smug_out "Bagus."

    show anon a_side
    show becca a_remove_top03
    with dissolve
    show becca a_remove_top04
    with {'master': dissolve}
    roxxy "Sekarang cepatlah berangkat karena ibuku akan segera pulang dan aku tidak ingin dia mengganggu acaranya!"

    show becca a_sides b_pants_bed
    with {'master': dissolve}
    anon "{i}*Gulp*{/i} Y-ya, oke."

    show anon b_onbed_sit_changing3 -of_blush:
        offset (-330, 28)
        yalign 1.
        xzoom -1
    show becca b_home_bed_remove_bottom01
    show roxxy f_horny_lipbite_out
    with {'master': dissolve}
    pause
    show anon a_towel b_shorts f_flirt_down:
        reset
        offset (-500, 0)
        xzoom -1
        yalign 1.
        zoom .95
    show becca b_home_bed_remove_bottom02
    show roxxy b_lolipop f_curious_lolipop_out
    with {'master': dissolve}
    pause
    show anon b_dressed_changing2:
        offset (0, 0)
        xzoom 1
        yalign 1.
    show anon_overlay_o_underwear_boner1 as boner behind cam:
        offset (30, 75)
        zoom .95
    show becca b_naked_bed a_sides f_shy_happy_down o_blush
    with {'master': dissolve}
    pause
    hide boner
    show anon b_naked_undress_bottom o_boner
    show becca f_shocked_down
    show roxxy b_facetime f_happy_out m_talk
    with {'master': dissolve}
    pause
    show anon a_sides b_naked f_shy od_naked_dick3 -o_boner
    show becca f_sexy_low
    show roxxy f_smug_out -m_talk
    with {'master': dissolve}
    roxxy "Kamu mau penis itu, {b}Becca{/b}?"

    show anon a_behind f_flirt_low
    with {'master': dissolve}
    becca f_sexy_low "Y-ya."

    roxxy "Aku tidak bisa mendengarmu!"

    show anon f_shy of_blush
    with {'master': dissolve}
    becca "Ya, saya menginginkannya!"

    roxxy f_horny_out "Siapa itu kontolnya?"

    show anon f_brag
    becca f_thinking @ f_exhausted_closed -m_talk "Milikmu."

    roxxy f_smug_out "Lebih keras!"

    show anon f_surprised
    show becca b_naked_bed_back f_annoyed
    with {'master': fastdissolve}
    becca @ f_annoyed_surprised "Itu penismu, {b}Roxxy{/b}!"

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
    roxxy "Panas sekali, {b}[firstname]{/b}!"

    show becca b_naked_disheveled_bed_belly behind anon
    anon "!!!" with hpunch
    show anon b_sit_naked f_surprised_low od_dick1:
        offset (-250, 15)
    with {'master': dissolve}
    roxxy "Apa lagi?!"

    show anon b_sit_naked_check f_surprised_low od_naked_dick1 behind becca:
        offset (0, -30)
    with {'master': dissolve}
    anon "{b}Becca{/b}?"

    show anon f_surprised_down
    show becca a_shoo
    with {'master': dissolve}
    becca @ -m_talk "*Bergumam tak jelas*"

    show anon f_worried_low
    show becca -a_shoo
    with {'master': dissolve}
    show anon b_liu_naked -od_naked_dick1:
        offset (-300, -50)
    with {'master': dissolve}
    roxxy "Bagaimana kamu masih bisa berkutat dengan penis pacarku yang besar?"

    show anon f_flirt_low of_blush
    show becca a_reach f_thinking
    with {'master': dissolve}
    becca "Ugh... diamlah, {b}Roxxy{/b}!"

    show becca a_phone f_shy o_blush
    with dissolve
    show expression stage as stage at local with {'master': local.show}
    roxxy "{i}*Mendengus*{/i} Maaf tapi ini lucu..."

    if M_missy.taken_dick:
        show anon f_surprised_low
        roxxy f_smug "... Bahkan {b}Missy{/b} menganggapnya lebih baik dari Anda!"

    show anon f_worried_low -of_blush
    with {'master': dissolve}
    becca f_upset "Grr!"

    show roxxy f_annoyed_right
    with {'master': dissolve}
    crystal "{b}Roxanne{/b}, aku pulang!!"

    show becca f_concerned
    roxxy f_annoyed "Oh sial!"

    roxxy "Aku harus pergi."

    roxxy f_suspicious "Maukah kamu mampir dan menemuiku nanti, {b}[firstname]{/b}?"

    show becca f_shy_back_low
    anon f_confused_low @ -m_talk "Hmm?"

    roxxy f_horny_lipbite @ f_horny "Menonton kalian berdua memang menyenangkan, tapi aku lebih suka kalian berdua untuk sementara waktu."

    show becca f_shy_back_low
    show anon f_thinking_down

    menu:
        "Tentu.":
            anon f_normal_low "Ya, sepenuhnya."

            show becca f_shy_back_down
            show roxxy f_horny_lipbite_close
            anon "Aku akan segera menemuimu, oke?"

            roxxy f_horny "Bagus."

            show anon f_grin
            show becca f_surprised
            roxxy f_smug "Aku akan memberimu seks terbaik dalam hidupmu saat kau di sini lagi, aku janji!"

        "Ya, mungkin...":

            anon f_worried_low "Jika ada waktu."

            roxxy f_suspicious "Ayo, {b}[firstname]{/b}..."

            roxxy "... Tidak bisakah kamu meluangkan waktu?"

            anon "Saya akan mencoba, oke?"

            show becca f_shy
            roxxy f_bored_down "{i}*Huh*{/i} Baiklah."

            roxxy "Hanya-"

            pause
            roxxy f_bored "Aku merindukanmu."

            show becca f_sad
            anon "Aku tahu."


    crystal "Dimana sih kamu, {b}Roxanne{/b}?!"

    show anon f_surprised_low
    show becca f_surprised
    show roxxy f_annoyed_right
    crystal "Saya butuh bantuan!"

    show anon f_worried_low
    show becca f_concerned
    show roxxy b_hangup c_hangup
    with {'master': dissolve}
    roxxy "Ugh, aku- ... Ayo... tunggu dulu!!"

    show anon f_surprised_low
    show becca f_surprised
    roxxy f_eyeroll "Bodoh, mabuk, tidak ada gunanya..."

    show roxxy b_stomach c_stomach f_bored
    with {'master': dissolve}
    roxxy "... Aku akan bicara dengan kalian nanti."

    anon f_normal_low "Y-ya, oke."

    show roxxy f_angry_right
    becca f_happy "Nanti, {b}Roxxy{/b}."

    show anon f_surprised_low
    show becca f_surprised
    hide roxxy
    with {'master': dissolve}
    roxxy "Kamu sangat memalukan-"

    show expression stage as stage with {'master': local.hide}
    "{i}*Bip*{/i}"

    show becca a_reach f_shy with {'master': dissolve}
    anon f_surprised_low "Oh oke..."

    show anon a_surprised b_sit_naked_up f_normal_low od_naked_dick1 behind becca:
        offset (-30, -30)
    show becca a_down
    with {'master': dissolve}
    anon "...Saya kira, saya mungkin harus pergi juga."

    show anon f_flirt_low
    show becca b_naked_disheveled_bed_up f_thinking
    with {'master': dissolve}
    becca "Ya baiklah."

    anon f_shy_low "Sampai jumpa nanti?"

    becca f_shy_happy_up @ -m_talk "Mhmm,"

    becca "Saya akan berada di sini."

    anon f_flirt_low "Dingin."

    hide anon
    show becca f_sexy_low
    with {'master': dissolve}
    anon "Sampai jumpa lagi, {b}Becca{/b}."

    becca "Nanti."

    show becca f_concerned_lipbite
    with {'master': dissolve}
    pause
    return 'afterglow'


label becca_button_bedroom.troll:
    show anon f_shy_left of_blush
    with {'master': dissolve}
    anon "Saya tidak akan menyebutnya jahat..."

    show becca f_glaring
    anon f_flirt "... Ibumu sangat seksi."

    show becca a_angry f_surprised
    with {'master': dissolve}
    becca @ -m_talk "!!!"
    show becca a_hips f_disgusted
    with {'master': dissolve}
    becca "Eugh, ayolah {b}[firstname]{/b}... Aku tidak ingin mendengar omong kosong itu!!"

    show anon a_cannoli_gobble f_laugh
    show becca f_glaring
    with {'master': dissolve}
    anon "{i}*Mendengus*{/i}"

    show anon a_sides f_happy -of_blush
    with {'master': dissolve}
    anon "Tenang saja, aku hanya mempermainkanmu {b}Becca{/b}..."

    becca f_annoyed "Ya, tidak lucu!"

    anon f_shy "Hehe, maaf."

    jump becca_button_bedroom.choice


label becca_button_bedroom.work:
    show anon a_point_down f_confused_low
    with {'master': dissolve}
    anon "Apa yang sedang kamu kerjakan?"

    show becca f_normal_down
    pause
    becca f_normal "Itu hanya hal yang membosankan untuk kelas {b}Nona Dewitt{/b}."

    show anon a_sides f_normal
    show becca a_front
    with {'master': dissolve}
    anon "Oh ya?"

    becca "Saya seharusnya menjelaskan perbedaan antara kunci musik bass dan kunci musik treble dalam satu paragraf..."

    show anon f_confused
    becca "... Lalu saya harus mengidentifikasi dan memberi label dengan benar semua nilai nada."

    anon "Kedengarannya sulit."

    becca f_concerned "Tidak juga."

    becca "Saya telah membaca lembaran musik sejak saya berusia lima tahun."

    anon "Benar-benar?"

    becca f_normal @ f_eyeroll "Ya, ibuku memaksaku mengambil pelajaran piano."

    anon f_surprised "Anda bisa bermain piano?"

    becca @ -m_talk "Mhmm."

    anon f_happy "Itu luar biasa!"

    becca f_shy_back_low "Ehh, tidak juga..."

    anon f_worried "Tidak?"

    becca f_sad "Itu membosankan dan aku membencinya."

    anon @ f_confused "Kenapa?"

    becca f_annoyed "Karena saya masih kecil dan saya ingin berada di luar bermain-main dengan anak-anak lain!"

    becca "Tidak terkurung di rumah bersama ibuku dan guru musik jompo itu!"

    anon f_thinking_down "Oh."

    pause
    anon f_happy "Yah, menurutku masih keren."

    show becca f_eyeroll
    pause
    show becca f_normal
    jump becca_button_bedroom.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
