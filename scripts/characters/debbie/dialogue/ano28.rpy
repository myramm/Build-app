label ano28_debt_debbie_debt:
    anon "Aku punya kejutan untukmu."

    debbie f_curious "Oh?"

    debbie "Kejutan seperti apa?"

    anon "Anda tahu hutang Anda pada bank?"

    debbie f_sad "Ya, bagaimana dengan itu?"

    anon f_happy "Itu hilang."

    anon "Saya melunasinya."

    debbie a_sides f_surprised "Apa-"

    debbie "Bagaimana kamu bisa?"

    anon f_normal "Uang yang diburu massa..."

    anon "... Saya menemukannya."

    debbie f_surprised_worried "K-kamu..."

    pause
    anon "Saya serius, {b}[deb_name]{/b}."

    anon "Hutangnya hilang."

    debbie f_surprised "saya-"

    pause
    show anon a_surprised_up_both f_worried_surprised
    show debbie a_mouth_shock f_crying_closed
    with {'master': fastdissolve}
    debbie "Ya Tuhan..."

    anon f_worried "Wah, hei... Ayolah, jangan menangis."

    show debbie b_robe_hug_mc behind anon
    show anon b_empty f_surprised
    with {'master': dissolve}
    debbie "Aku tidak bisa menahannya... itu adalah air mata bahagia!"

    anon f_shy_low "Hehe."

    anon "Di sana, di sana..."

    pause

    if M_debbie.finished_state(S_debbie_night_visit_three):
        hide anon
        show debbie b_robe_kiss_mc:
            xoffset -350
        with dissolve
        debbie "MM."

        pause
        show debbie b_robe_hug_mc:
            xoffset -0
        show anon b_empty f_flirt_low
        with dissolve

    debbie "Kamu anak yang luar biasa!"

    anon "Ya, aku sering mendengarnya akhir-akhir ini."

    debbie "Bagaimana saya bisa seberuntung itu?!"

    anon f_normal "Saya yang beruntung."

    show anon a_idle b_dressed f_normal
    show debbie a_front b_robe f_laugh:
        xoffset -150
    with dissolve
    debbie "hehe!"

    show anon f_normal_left
    show debbie f_normal
    jenny "Apa yang sedang terjadi?"

    show anon b_empty f_shy:
        xoffset 140
        xzoom -1
    show debbie a_idle b_robe_mc_touch f_normal_back:
        xoffset 44
    with dissolve
    pause
    show debbie a_touch f_normal with {'master': dissolve}
    debbie "{b}[jen_name]{/b}, masuk ke sini!"

    show anon a_sides b_dressed f_normal:
        xoffset 50
        xzoom -1
    show debbie a_sides b_robe:
        xoffset -150
    show jenny a_magic b_dressed_magic f_upset:
        xzoom -1
    with {'master': dissolve}
    debbie "Anda tidak akan percaya ini!"

    jenny @ f_eyeroll "Ya Tuhan, sekarang apa yang terjadi?"

    show debbie a_front f_excited
    with {'master': dissolve}
    debbie "Sesuatu yang luar biasa!"

    show anon f_happy
    debbie f_normal "{b}[firstname]{/b} melunasi hutang kita di bank!"

    show jenny a_up_surprised f_surprised with {'master': dissolve}
    jenny "Tunggu, apa?!"

    debbie "Itu benar!"

    show jenny a_sides with {'master': dissolve}
    jenny "Bagaimana?"

    show debbie f_normal_back
    anon "Uang yang dicari massa..."

    pause
    anon f_normal "... Saya menemukannya."

    show debbie f_normal
    jenny "Jadi kita tidak akan kehilangan rumah?!"

    show debbie f_normal_back
    anon f_happy "Tidak."

    show debbie f_normal
    jenny f_happy "Sialan, {b}[firstname]{/b}!!"

    debbie @ f_excited "Bukankah itu bagus?!"

    jenny "Ya!"

    hide jenny
    show debbie b_robe_hug_jenny_front_arm f_normal_back:
        crop (0, 0, 940, 768)
    with dissolve
    hide anon
    show debbie b_robe_hug_jenny_front_anon f_content:
        crop None
    with dissolve
    pause
    debbie "Aku sangat mencintai kalian berdua."

    anon "Aku pun mencintaimu."

    pause
    show jenny a_magic b_dressed_magic f_happy:
        xzoom -1
    show debbie a_front b_robe f_normal
    show anon a_sides b_dressed f_normal:
        xoffset 50
        xzoom -1
    with dissolve
    debbie "Kita harus merayakannya!"

    show debbie f_normal_back
    anon "Oh?"

    debbie f_excited_back "Aku sedang memikirkan es krim dan film!"

    show anon f_confused
    show debbie f_normal
    jenny f_concerned "Es krim dan film?"

    show jenny a_crossed
    with {'master': dissolve}
    jenny "Siapakah kita, yang berumur dua belas tahun?"

    debbie "Oh, ayolah!"

    anon f_normal "aku terjatuh."

    jenny f_eyeroll "Eugh, tentu saja."

    show anon f_worried
    debbie f_sad "Tolong, ini akan menjadi seperti malam keluarga!"

    jenny f_upset @ f_upset_back_low "{i}*Huh*{/i} Baik."

    show anon f_normal
    debbie f_normal "Itu gadisku!"

    pause
    show jenny a_sides f_grin with {'master': dissolve}
    jenny "Tapi aku memilih filmnya!"

    show debbie f_normal_back
    anon f_worried "Oh tidak!"

    anon "Ide buruk."

    show jenny f_upset
    anon f_disgusted "Kalau menurutmu aku sedang menonton lagi film vampir gemerlap itu, ada hal lain yang akan datang!"

    show anon f_surprised
    show jenny behind debbie
    show debbie a_hips f_surprised:
        xoffset 350
        xzoom -1
    with {'master': fastdissolve}
    debbie "{b}[firstname]{/b}, bahasa!"

    anon f_shy "Maaf, {b}[deb_name]{/b}."

    show anon f_unimpressed
    show debbie a_facepalm f_sad_closed:
        xoffset -150
        xzoom 1
    show jenny a_upset f_angry
    with {'master': dissolve}
    jenny "Hei, itu bukan omong kosong!"

    jenny f_upset "Ini adalah franchise film terhebat di generasi kita."

    anon f_annoyed "Kamu monster."

    show debbie a_sides f_laugh
    show jenny a_sides f_laugh
    with {'master': dissolve}
    jenny "Ha ha ha!"

    show anon f_normal
    show jenny f_happy
    debbie f_normal @ f_excited "Aku akan ambilkan es krimnya!"

    hide debbie
    show jenny a_magic:
        xoffset -500
        xzoom 1
    with dissolve
    anon f_worried "Tolong, jangan memaksaku menonton omong kosong itu, {b}[jen_name]{/b}."

    show jenny with {'master': dissolve}:
        xoffset 0
        xzoom -1

    if M_jenny.finished_state(S_jenny_cheerleader_sex) and M_jenny.get("dominance") > 0:
        jenny f_eyeroll "{i}*Huh*{/i} Oke."

        jenny f_normal "Sekali ini saja, karena Anda mendapatkan rumah itu kembali kepada kami... Anda boleh memilih!"

        anon f_laugh "Ya!!"

        show anon f_normal
        jenny f_upset "Jangan mengacaukannya dengan memilih film aksi murahan!"

        anon f_brag "Oh, jangan pernah takut!"

        anon "Aku tahu satu-satunya."

        anon f_normal "Marty Pythin dan Keju Suci!"

        jenny f_happy "Baiklah, aku bisa menerimanya."

        pause
        hide jenny with dissolve
        show anon a_cheering f_laugh with {'master': dissolve}
        anon "Ah ya!"

        hide anon with {'master': dissolve}
        jenny "Ayo duduk di sampingku."

    else:

        jenny f_grin "Terlambat."

        jenny "Kami sedang menontonnya."

        anon f_frown_down "Aduh, bung..."

        show anon f_annoyed
        jenny f_normal "Bersyukurlah aku menghabiskan waktu bersamamu... lubang kecil."

        hide jenny with dissolve
        anon "Ya, terserah."

        pause
        anon f_sad_smile_down "{i}*Huh*{/i} Setidaknya akan ada es krim."

        show anon f_surprised
        jenny "Jika kamu anak yang baik, aku mungkin akan membiarkanmu mengecat kukuku."

        show anon f_unimpressed with {'master': dissolve}:
            xoffset -250
        anon "Ya, benar...kenapa aku ingin-"

        show anon f_thinking
        pause
        hide anon with {'master': dissolve}
        anon "Tunggu, kuku tangan atau kuku kaki?"

        jenny "Kamu mesum sekali."

        jenny "Ha ha ha!"


    scene expression background(l=L_home_bedroom, t=3) with longfade
    show anon f_tired_happy with dissolve:
        xoffset 250
    anon @ -m_talk "(Hari yang menyenangkan!)"

    anon @ -m_talk "( {b}[deb_name]{/b} akhirnya bisa berhenti stres tentang uang... )"

    anon f_grin @ -m_talk "(...Dan rekening bankku penuh!)"

    anon a_yawn f_yawn @ -m_talk "{i}*Menguap*{/i}"

    anon a_sides f_tired_happy @ -m_talk "(Sobat, aku ingin tahu petualangan apa yang akan terjadi besok?)"

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
