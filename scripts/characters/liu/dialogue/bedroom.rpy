label liu_button_bedroom:
    show anon a_wave with dissolve
    anon "Hai, {b}Liu{/b}."

    show anon a_sides f_worried_surprised
    show liu b_robe_hair f_happy behind anon
    with {'master': dissolve}
    liu "Hai, {b}[firstname]{/b}."

    anon f_worried -m_talk "M- Maaf, aku tidak bermaksud membuatmu bangun!"

    liu "Jangan khawatir, sudah waktunya aku meregangkan kakiku."

    show anon a_idle f_normal with dissolve

    menu liu_button_bedroom.choice:
        "uang ayah." if M_anon.is_state(S_ano28_cash):
            jump ano28_cash_liu_money
        "Apa yang kamu baca?":

            jump liu_button_bedroom.novels
        "Saya suka apa yang telah Anda lakukan dengan tempat itu.":

            jump liu_button_bedroom.decor
        "Seks":

            jump liu_button_bedroom.sex
        "Sampai jumpa nanti.":

            pass

    show liu a_sides f_worried with {'master': dissolve}
    liu "Berangkat begitu cepat?"

    show anon a_behind_head f_shy with {'master': dissolve}
    anon "Ya, ada yang harus kulakukan."

    liu f_worried_down "Ah, oke..."

    show liu b_robe_hug
    show anon b_empty f_surprised
    with dissolve
    pause
    show anon f_shy
    liu "Anda akan kembali lagi, ya?"

    show anon a_beer_cheer b_dressed behind liu
    show liu a_cover b_robe_hair f_worried:
        xoffset -300
    with {'master': dissolve}
    anon "Tentu saja."

    liu "Sampai jumpa, {b}[firstname]{/b}."

    anon "Nanti, {b}Liu{/b}."

    hide anon with dissolve
    return


label liu_button_bedroom.book:
    anon "Tentang apa ini?"

    show liu a_sides f_surprised with {'master': dissolve}
    liu "Anda benar-benar ingin tahu?"

    anon "Ya, benar."

    show liu f_nervous o_blush with {'master': dissolve}
    liu "Oh, umm... Oke."

    show liu f_nervous_down with dissolve:
        xoffset 575
        xzoom -1
    pause .3
    show anon a_surprised f_surprised_low
    show liu b_robe_bend
    with dissolve
    pause
    show anon a_sides f_flirt
    show liu a_book b_robe_hair f_happy_down_back
    with dissolve
    pause .3
    show anon f_normal
    show liu f_nervous:
        xoffset 0
        xzoom 1
    with {'master': dissolve}
    liu "Ini tentang putri pembuat roti di Tiongkok abad kedelapan belas, yang memiliki hasrat untuk membuat kue."

    liu "Dan orang-orang datang dari seluruh negeri untuk mencicipi roti manisnya yang lezat."

    anon f_happy "Mmm, aku suka roti manis!"

    liu "Hehe, aku juga."

    pause
    show liu f_worried -o_blush with {'master': dissolve}
    liu "Tapi suatu hari ayahnya terkena serangan jantung dan meninggal..."

    anon f_surprised "Oh tidak!"

    liu "... Dan ibu tirinya yang jahat menjual tangannya untuk dinikahkan dengan pembuat roti saingannya."

    liu f_annoyed "Pria babi besar dan gemuk yang menjijikkan ini, bernama Dong Zhuo."

    anon f_thinking_down @ -m_talk "(Hmm, ini mulai mengingatkanku pada seseorang...)"

    liu "Dia terus merantainya ke oven di dapurnya dan memaksanya memanggang roti manis sepanjang hari, tanpa istirahat."

    show anon f_shock with hpunch
    pause
    anon f_worried "Itu mengerikan!"

    liu "Ya."

    liu "Dia menjadi sangat kaya karena roti lezatnya dan setiap malam, wanita malang ini menangis hingga tertidur, memimpikan hari dimana dia akan terbebas darinya."

    anon "Lalu apa yang terjadi?"

    liu f_normal "Suatu hari, orang asing misterius tiba di kota dan bertanya kepada tukang roti apakah dia bersedia menjual resepnya kepadanya."

    liu f_worried "Tentu saja, tukang roti menolak dan mengolok-olok orang asing itu... \"Apa yang bisa ditawarkan orang malang sepertimu kepada orang sepertiku?\""

    anon f_surprised "Dia menghina orang asing itu?!"

    liu @ -m_talk "Mhmm."

    show anon f_worried
    liu "Orang asing itu berkata, \"Memang, saya tidak memiliki apa pun yang dapat menandingi nilai resep roti manis lezat Anda...\""

    liu f_happy "Namun dia tahu bahwa si tukang roti mempunyai keserakahan yang besar, jadi dia malah menawarinya taruhan."

    show anon f_confused
    liu "\"Jika kamu bisa menjatuhkanku, aku akan memberimu pedangku...\""

    liu "Orang asing itu mengangkat katananya, terbuat dari baja terbaik; pegangannya dibungkus dengan sutra mewah."

    liu "\"...dan jika tidak bisa, kamu akan membagikan rahasiamu.\""

    show anon f_disgusted
    liu f_gross "Pria gemuk itu menjilat bibirnya dengan lapar."

    liu f_curious "\"Yang perlu kulakukan hanyalah menjatuhkanmu?\""

    show anon f_happy
    liu f_nervous "Dia tertawa, mengetahui bahwa beratnya melebihi orang asing itu tiga kali lipat... dan menerima taruhannya."

    anon f_normal "Saya merasa dia akan menyesali hal itu."

    liu f_happy "Memang."

    liu "Ternyata, orang asing misterius itu tidak lain adalah Zhang Yan, seorang raja bandit terkenal, dan salah satu pejuang terhebat di wilayah tersebut."

    anon f_worried "Uh oh."

    liu "Tukang roti mencoba dan mencoba menjatuhkan pria itu, tetapi dia tidak pernah berhasil."

    show anon a_pocket with {'master': dissolve}
    liu "Beberapa jam kemudian, dengan bermandikan keringat, si tukang roti akhirnya mengaku kalah."

    liu f_annoyed "\"Tetapi tawa terakhir adalah milikku!\" teriaknya. \"Seperti yang Anda lihat, rahasia saya adalah saya tidak tahu resepnya!\""

    show anon f_surprised
    liu f_confused "\"Bagaimana ini bisa terjadi?\" tanya orang asing itu."

    liu f_ashamed_down "Tukang roti memintanya masuk ke dapurnya dan memandangi wanita malang itu, yang dirantai di ovennya."

    liu f_normal "Segera, Zhang Yan berlutut, terpesona oleh kecantikan dan keterampilan membuat kuenya."

    liu f_happy "\"Nona manis, saya merasa terhormat berada di hadapan Anda!\""

    liu "\"Roti manismu yang lezat membuat iri semua makanan panggang lainnya!\""

    liu "Tukang roti mengejek tampilan itu, dan Zhang Yan berbalik, marah pada keadaan wanita malang itu."

    show anon f_shock
    liu "Dia membenamkan katananya di dada pria gendut itu sebelum membawa wanita itu keluar dari sana."

    anon f_brag "Wah, luar biasa!"

    show liu a_mouth_cover f_laugh with {'master': dissolve}
    liu "Hehe, ya."

    show liu a_book f_happy with {'master': dissolve}
    liu "Itu bagian favoritku!"

    anon "Lalu apa yang terjadi?"

    liu f_normal "Saya belum yakin."

    liu "Saat ini, mereka baru saja tiba di kamp banditnya dan..."

    show anon f_confused
    show liu f_nervous_down o_blush:
        xoffset 575
        xzoom -1
    with {'master': dissolve}
    liu "... Ummm..."

    show anon f_confused_low
    show liu b_robe_bend
    with dissolve
    show anon f_confused
    show liu a_sides b_robe_hair f_nervous_lipbite_back
    with dissolve
    pause
    show liu a_shy with {'master': dissolve}:
        xoffset 0
        xzoom 1
    liu f_nervous "... Mereka baru saja bercinta... untuk pertama kalinya."

    anon f_normal "Baiklah, saya mengerti mengapa Anda menyukainya."

    liu f_happy "Anda bisa?"

    anon "Ya."

    anon "Anda harus memberi tahu saya bagaimana ini berakhir."

    liu f_happy_excited_closed "O-oke, aku akan melakukannya!"

    liu f_nervous_down "Kamu pria yang luar biasa, {b}[firstname]{/b}!"

    anon "Dan Anda adalah wanita yang luar biasa, {b}Liu{/b}."

    show liu f_happy -o_blush with {'master': dissolve}
    jump liu_button_bedroom.choice


label liu_button_bedroom.decor:
    show anon f_normal_high with dissolve
    pause
    anon "Anda benar-benar meningkatkan suasana di sini!"

    show anon f_normal
    liu f_happy "Hehe, terima kasih!"

    show liu a_hips f_annoyed
    with {'master': dissolve}
    liu "Semoga suatu hari aku bisa menyingkirkan patung bodoh itu juga..."

    show anon f_disgusted with {'master': dissolve}:
        xoffset -500
        xzoom -1
    liu "... Ini sangat berat!"

    show anon f_confused with {'master': dissolve}:
        xoffset 0
        xzoom 1
    anon "Saya bisa mencoba memindahkannya, jika Anda mau?"

    show liu a_sides f_normal with {'master': dissolve}
    liu "Tidak, tidak... Aku akan memanggil beberapa tukang pindahan atau semacamnya."

    show anon with dissolve:
        xoffset -500
        xzoom -1
    pause
    anon "Ya, setidaknya Anda melakukan beberapa perbaikan."

    show anon f_laugh
    liu f_laugh "Hehehe!"

    anon "Ha ha ha!"

    show anon f_normal with dissolve:
        xoffset 0
        xzoom 1
    liu f_happy "Ya, senang sekali semua mainannya hilang..."

    liu f_gross "... Dan replika bom yang mengerikan itu, eugh!"

    jump liu_button_bedroom.choice


label liu_button_bedroom.novels:
    show anon a_point f_normal with {'master': dissolve}
    anon "Apa yang sedang kamu baca?"

    show anon a_idle
    show liu f_nervous_back o_blush
    with {'master': dissolve}
    liu "Oh, umm... heh, tidak apa-apa."

    anon f_confused @ -m_talk "Hah?"

    liu f_nervous "Saya lebih suka tidak mengatakannya."

    anon "Kenapa?"

    liu a_shy "Karena... itu memalukan!"

    anon "Memalukan?"

    pause
    anon f_brag "Ah, ayolah... Kamu bisa memberitahuku."

    show liu f_nervous_lipbite
    pause
    liu f_nervous "Anda berjanji tidak akan tertawa?"

    anon "Saya berjanji."

    show liu f_nervous_lipbite
    pause
    liu f_nervous "Saya suka membaca..."

    pause
    liu f_nervous_back "... Novel roman murahan."

    anon a_behind_head f_confused "Novel roman murahan?"

    liu f_nervous "Y-ya."

    show liu -o_blush
    show anon a_sides f_normal
    with dissolve

    menu:
        "Tentang apa ini?":
            jump liu_button_bedroom.book
        "Tidak ada yang salah dengan itu.":

            pass

    anon "Banyak orang menikmatinya."

    show liu a_mouth_cover f_laugh with {'master': dissolve}
    liu "Ya, tapi aku SANGAT menikmatinya..."

    anon "Oh?"

    show liu a_sides f_worried_down with {'master': dissolve}
    liu "Heh, bertahun-tahun tinggal bersama {b}Kim{/b}..."

    show liu a_cover f_worried
    with {'master': dissolve}
    liu "... Buku-buku ini adalah satu-satunya kegembiraan yang pernah saya alami."

    anon f_worried "Ya, itu tidak mengherankan."

    liu f_ashamed_down @ -m_talk "..."
    anon a_idle f_normal "Anda harus memberi tahu saya tentang hal itu suatu saat nanti."

    show liu a_shy f_surprised with {'master': dissolve}
    liu "Benar-benar?"

    anon "Tentu, saya tertarik untuk mempelajari lebih lanjut tentang mereka."

    liu f_nervous "Y-ya, oke."

    liu f_happy "Saya ingin itu."

    jump liu_button_bedroom.choice


label liu_button_bedroom.sex:
    $ renpy.dynamic(bedroom=player.location == L_liu_bedroom)

    liu "Apakah ada sesuatu yang ada di pikiranmu?"

    anon f_confused @ -m_talk "Hmm?"

    liu "Kamu sedang memikirkan sesuatu... Aku bisa melihatnya di matamu."

    anon f_shy "Heh, kamu... sebenarnya."

    show liu f_curious o_blush with {'master': dissolve}
    liu "Aku?"

    anon f_flirt "Aku sedang memikirkan betapa aku ingin melepaskanmu dari jubah itu..."

    show liu f_sexy_lipbite
    pause

    if bedroom:
        liu f_sexy a_undress1 "Maksudmu..."

        show anon a_surprised_up f_surprised_low
        show liu a_undress2 b_robe_open
        with dissolve
        pause .1
        show anon f_normal_low m_talk
        show liu a_undress3 b_naked_hair
        with dissolve
        pause .1
        show anon f_flirt_low
        show liu a_undress4
        with dissolve
        pause .1
        show anon a_sides f_shy_low
        show liu a_sides
        with {'master': dissolve}
        liu "... Seperti ini?"

        show liu f_sexy_lipbite
    else:

        show anon f_shy_high
        hide liu
        with {'master': dissolve}
        liu f_sexy "Maksudmu..."


        scene expression background(768, 384, 2) as stage
        show liu a_undress1 b_robe_hair f_sexy_lipbite
        with fade
        pause .1
        show liu a_undress2 b_robe_open with dissolve
        pause .1
        show liu a_undress3 b_naked_hair with dissolve
        pause .1
        show liu a_undress4 with {'master': dissolve}
        liu f_sexy "... Seperti ini?"

        show liu a_sides f_sexy_lipbite
        with dissolve
        pause
        show anon a_sides f_shy_low o_boner of_blush with {'master': dissolve}

    anon f_shy -m_talk @ -m_talk "Mhmm."

    liu a_hips f_sexy "Sekarang apa?"


    menu:
        "Mari kita bawa ini ke kamar tidur." if not bedroom:
            pass
        "Ayo bawa ini ke tempat tidur." if bedroom:
            pass

    show anon behind liu:
        xoffset 350
    show liu f_surprised
    with fastdissolve
    show anon a_empty f_flirt_low o_empty:
        xoffset 500
    show liu b_naked_anon_arms f_shocked:
        xoffset 500
    liu "Oh!" with hpunch
    liu f_laugh "Hehehe!"

    liu f_happy "Saya suka ketika Anda melakukan ini!"

    anon f_shy_low "Ya?"

    liu f_sexy "Itu membuatku sangat basah untukmu."

    show liu f_sexy_lipbite
    anon f_normal_low "Aduh, astaga..."

    show liu f_laugh
    anon f_happy_low "... Untuk bercinta!"

    hide anon
    hide liu
    with {'master': dissolve}
    liu "hehe!"


    scene expression game.timer.image('location_liu_bedroom_bed_after{}')
    show anon b_liu_naked f_shy_high
    show liu b_bed_naked_kiss
    with fade
    pause
    show liu b_bed_naked_sit with dissolve
    liu "Oh, kamu membuatku sangat bahagia, {b}[firstname]{/b}!"

    show liu b_bed_naked_kiss with dissolve
    liu "MM."

    pause
    show liu b_bed_naked_sit with dissolve
    liu "Saya sangat senang Anda datang ke dalam hidup saya!"

    anon "Ya, aku juga."

    show liu b_bed_naked_kiss with dissolve
    pause

    call scene_liu_sex_bedroom.repeat
    $ unlock_scene('liu', '01_unlocked', variant='repeat')

    scene expression background(480, 384, 2.5, l=L_liu_bedroom) as stage
    show anon b_dressed_changing2:
        xoffset -350
        xzoom -1
    with fade
    show anon a_towel b_shorts f_looking_down with dissolve
    show anon b_dressed_changing with dissolve
    show anon a_sides b_dressed f_normal with dissolve
    pause
    show anon a_idle b_dressed with {'master': dissolve}:
        xoffset 150
        xzoom 1
    anon "Saya mungkin harus pergi."

    liu "Sudah?"

    show liu a_undress3 b_naked_disheveled
    with {'master': dissolve}
    anon "Ya, aku punya banyak hal yang masih perlu aku urus..."

    show liu a_undress2 b_robe_disheveled_open f_happy_closed
    with {'master': dissolve}
    anon "... Tapi sampai jumpa lagi."

    show liu a_undress1 b_robe_disheveled f_happy
    with {'master': dissolve}
    liu "Anda berjanji?"

    show anon f_flirt
    show liu a_shy
    with {'master': dissolve}
    anon "Tentu saja."

    hide anon
    show liu b_robe_disheveled_kiss:
        xoffset 75
    with dissolve
    liu "MM."

    pause
    show anon a_sides b_dressed behind liu:
        xoffset 75
    show liu b_robe_disheveled:
        xoffset -225
    with {'master': dissolve}
    liu "aku akan menunggu."

    anon "Sampai jumpa, {b}Liu{/b}."

    hide anon with dissolve
    return 'afterglow'
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
