label ano17_erik_erik:
    scene expression background(768, 400, 2.) as stage
    show erik b_dressed_back_bending
    show anon f_normal_low with dissolve
    anon "Apa yang kamu lakukan di sini?"

    erik "Menggali permainan papan lama saya."

    anon f_disgusted_low "Hah?"

    anon "Mengapa kamu melakukan itu?"

    show erik b_dressed
    show anon f_normal
    with dissolve
    erik "Karena putri walikota akan datang, bukan?"

    anon @ f_confused "Ya?"

    erik "Yah, kita butuh sesuatu untuk menghiburnya, bukan?"

    anon f_surprised "Dan menurut Anda permainan papan bisa melakukan hal itu?"

    erik "Hmm, ya?"

    anon f_worried @ a_facepalm "{b}Iwanka{/b} adalah seorang mahasiswi, kawan..."

    anon "Dia tidak ingin bermain permainan papan."

    erik f_woozy @ f_laugh "Ah, ayolah!"

    erik "Saya punya semua yang klasik!"

    erik "{i}Lapar, Lapar, Pachydermata.{/i}"

    show anon f_unimpressed
    erik "{i}Unta Cockamamie{/i}."

    erik "{i}Kebun Binatang Mitzvah Moon{/i}."

    anon "Tidak."

    erik f_worried "{i}Siapa yang Merencanakan Kugel{/i}?"

    anon f_disgusted "Eww, tentu saja tidak!"

    erik f_nervous "Yah, aku tidak tahu apa yang akan kita lakukan kalau begitu!"

    erik f_surprised "Dia akan berada di sini sebentar lagi."

    anon a_thinking f_thinking @ f_brag_closed a_wave "Tenang!"

    anon "Mari kita mulai dengan mengatur suasana hati."

    anon "Apakah Anda memiliki musik dansa yang bagus?"

    erik f_worried "Eh, tunggu."

    hide erik
    show anon f_normal a_idle
    with dissolve
    pause
    show anon f_surprised
    pause
    show anon b_dressed_bending1 with dissolve:
        xoffset 400
    pause
    erik "Saya punya Dr. Dreidel baru di sini di suatu tempat..."

    show anon b_dressed f_thinking with {'master': dissolve}:
        flip
        xoffset 0
    anon "Mm, menurutku itu mungkin terlalu agresif."

    show anon f_normal
    erik "Yahudi Tull?"

    anon f_unimpressed "Tidak."

    erik "Sabat Hitam?"

    show anon f_thinking a_thinking with dissolve
    pause
    anon f_worried a_idle "Menurutku {b}Iwanka{/b} tidak menyukai musik rock..."

    erik "Halal Saya Buruk?"

    anon f_disgusted "sial!"

    anon "Mustahil!"

    erik "Barmitzvah Streisand?"

    anon f_confused "Apa yang-"

    anon "Um, kenapa kamu punya itu?"

    erik "Dia favorit induk semangku."

    anon @ f_worried -m_talk "..."
    anon "Apakah Anda tidak punya yang lain selain band-band Yahudi?"

    erik "Tidak juga."

    anon f_sad_down a_sides "{i}*Sigh*{/i} Ini bukan awal yang menjanjikan, {b}Erik{/b}."

    pause
    erik "Putra II Mensch?"

    anon f_unimpressed "Apa itu, R&B Yahudi?"

    erik "Ya."

    anon @ f_shy_cringe a_facepalm "Ugh, itu harus dilakukan."

    erik "Dingin!"

    erik "Biarkan aku mengaturnya."

    pause
    show anon f_normal
    show erik:
        flip
    with dissolve
    erik "Selesai."

    erik "Sekarang apa?"

    anon "Dia secara khusus menyebutkan keinginannya untuk minum alkohol."

    erik f_woozy "Yah, itu tidak masalah!"

    erik "{b}Tuan. Johnson{/b} menjaga standar di sini tetap terisi penuh."

    anon "Setidaknya kita memiliki hal itu untuk kita..."

    anon "Apakah kamu mendapat makanan ringan?"

    erik f_bored "Kawan, menurutmu kamu sedang berbicara dengan siapa?"

    erik f_normal @ f_laugh "Aku membelikan kami tiga setengah kantong kue keju!"

    anon f_worried "Puff keju?"

    erik "Yup, dan semangkuk besar saus keju nacho!"

    anon f_sad_down a_rub "Aduh, bung..."

    erik "Saya sebut dibs pada setengah tas!"

    anon f_worried a_sides "Kami tidak bisa menyajikan kue keju putri walikota..."

    erik f_worried "Kenapa tidak?"

    anon "Karena kita tidak bisa, oke?"

    anon f_normal a_idle "Naik ke atas dan temukan sesuatu yang lain."

    erik f_bored "Saya rasa Anda tidak mengerti betapa lezatnya kue keju, kawan!"

    erik "Mereka benar-benar meleleh di mulut Anda!"

    tammy "{b}Erik{/b} sayang, kamu kedatangan tamu!!"

    show anon f_sad_down a_sides with dissolve
    erik f_nervous @ f_surprised "Ya ampun... Dia di sini!!!"

    erik "Apa yang kita lakukan?!"

    anon "Ugh, ini akan menjadi bencana..."

    erik f_worried "Jangan seperti itu, {b}[firstname]{/b}."

    erik "Anda seharusnya menjadi orang yang percaya diri!"

    anon f_worried "Anda tidak akan mengunci lagi, bukan?"

    erik "T-tidak."

    erik f_woozy @ f_laugh a_whisper "Saya punya rencana, Anda akan lihat nanti."

    tammy "Dimana kalian?"

    anon f_sad_down @ a_rub "Kami datang!"

    hide anon with dissolve
    show erik f_nervous a_faint with dissolve
    pause
    erik a_proud f_worried "Halo, {b}Iwanka{/b}... Nama saya {b}Erik{/b}."

    pause
    erik f_normal "Senang bertemu denganmu!"

    erik a_thinking "Fiuh, oke."

    erik a_idle @ a_facepalm "Saya bisa melakukan ini!"


    scene expression background(560, 440, 3., l=L_erikhouse_basement) as stage
    show tammy a_sides:
        flip
        xoffset 100
    show iwanka b_club a_popsicle f_disgusted:
        flip
        xoffset -120
    with fade
    show anon f_shy with dissolve:
        flip
        xoffset 150
    tammy "Itu dia."

    anon @ a_wave "Hei!"

    tammy f_suspicious "Saya pikir Anda mengatakan seorang gadis akan datang?"

    tammy "Ini adalah wanita dewasa..."

    show iwanka f_smirk
    show erik f_nervous behind tammy:
        xoffset -40
    with dissolve
    anon f_shy @ f_worried "Ehh."

    erik "H-hai."

    show tammy f_normal
    erik a_proud "{i}*Ehem*{/i} Hai loh!"

    show anon f_shy
    iwanka f_disgusted "Uhh?"

    erik a_idle "Senang bertemu denganmu..."

    erik "Saya {b}Iwanka{/b}."

    show tammy f_suspicious
    anon f_worried @ -m_talk "..."
    erik @ a_thinking "Err, maksudku, {b}Erik{/b}!"

    erik "Saya bukan {b}Iwanka{/b}... Anda {b}Iwanka{/b}!"

    show tammy f_sad
    show anon f_tired a_facepalm
    with dissolve
    iwanka "Ya, aku sadar..."

    show anon f_shy a_idle with dissolve
    erik "Kamu terlihat... Umm..."

    erik "I-ini milikku..."

    show erik a_facepalm with dissolve
    pause
    erik a_proud @ f_laugh "Selamat datang!"

    iwanka f_concerned "Apakah dia baik-baik saja?"

    show erik f_sad a_idle
    show anon f_sad_down
    with dissolve
    anon "{i}*Huh*{/i} Mungkin tidak."

    show anon f_shy
    show erik f_nervous
    show tammy f_suspicious a_idle behind erik:
        unflip
        xoffset -300
    with dissolve
    tammy "Berapa umurmu?"

    iwanka f_normal @ -m_talk "Hmm?"

    iwanka "Oh, uhh... Hampir dua puluh tujuh."

    tammy @ f_surprised "Oh ya!"

    tammy "Apakah ibumu tahu kamu berjalan-jalan dengan pakaian seperti ini?"

    show iwanka f_smirk
    erik f_surprised "{b}Tim{/b}!!"

    show tammy f_annoyed with dissolve:
        flip
        xoffset 100
    tammy "Apa?!"

    tammy "Saya tidak diperbolehkan menunjukkan ketertarikan pada gadis yang dibawa pulang oleh anak laki-laki saya?"

    erik f_nervous @ a_whisper "Kamu membuatku malu!"

    show iwanka f_normal
    tammy f_suspicious "Ah, jangan konyol..."

    tammy "... Tidak ada alasan untuk merasa malu."

    tammy f_normal "Saya senang melihat Anda akhirnya mematikan komputer itu."

    show erik behind tammy
    tammy a_pinch @ f_laugh "Tiram kecilku akhirnya tumbuh besar."

    show tammy a_pinch_wave
    show erik a_shoo f_angry
    with dissolve
    erik "Hentikan itu!"

    show erik a_idle
    show tammy a_idle f_laugh
    with dissolve
    tammy "Hehehe!"

    show tammy f_normal a_sides behind erik with dissolve:
        unflip
        xoffset -380
    tammy "Bukankah dia menggemaskan?"

    show tammy with dissolve:
        flip
        xoffset 100
    tammy "Aku bangga padamu, kawan."

    tammy "Kamu {i}seharusnya{/i} keluar mengejar gadis-gadis, daripada duduk-duduk di sini dengan tuchismu sepanjang hari."

    show tammy f_annoyed with dissolve:
        unflip
        xoffset -300
    tammy "Coba saja temukan yang tidak terlalu menyebalkan lain kali, oke?"

    show iwanka f_surprised
    show erik f_surprised
    anon f_surprised_teeth "!!!" with hpunch
    show anon f_hurt
    iwanka f_annoyed a_popsicle_fists "Permisi?!"

    show anon f_worried
    tammy @ f_laugh "Jangan tersinggung, sayang."

    erik @ -m_talk "..."
    anon "Umm, {b}Ny. Johnson{/b}... Bisakah Anda memberi kami sedikit privasi?"

    show tammy f_sad with dissolve:
        flip
        xoffset 100
    tammy @ -m_talk "Hmm?"

    tammy f_normal "Tentu saja."

    tammy "Haruskah saya menghangatkan kantong pizza untuk pesta kecil Anda?"

    erik f_normal @ f_laugh "Oh, kantong pizza!"

    anon @ f_unimpressed "Tidak, kami baik-baik saja..."

    show erik f_sad with {'master': dissolve}:
        flip
        xoffset 380
    erik "Ah, tapi-"

    anon f_normal "Terima kasih."

    tammy a_idle "Baiklah, lakukan sesukamu."

    show erik:
        unflip
        xoffset -20
    show tammy f_laugh
    with {'master': dissolve}
    tammy f_normal @ f_laugh "Kalian anak-anak bermain bagus, oke?"

    show anon f_hurt a_facepalm with dissolve
    pause
    anon a_idle f_tired "{i}*Huh*{/i} Kami akan melakukannya, {b}Ny. Johnson{/b}."

    iwanka @ -m_talk "..."
    show tammy f_annoyed with dissolve:
        unflip
        xoffset -260
    pause
    tammy a_watch @ -m_talk "...{w=.4{nw}"

    show iwanka f_surprised
    show anon f_surprised
    with {'master': fastdissolve}
    tammy @ -m_talk "..."
    hide tammy with dissolve
    anon f_worried "aku benar-benar minta maaf soal itu..."

    show iwanka f_annoyed
    iwanka a_popsicle_wtf @ f_suspicious_down "Ck, ada apa dengan bajuku?!"

    anon f_shy "T-tidak ada apa-apa!"

    anon "Kamu tampak hebat!"

    show iwanka a_popsicle_fists with dissolve
    anon f_normal "Bukankah dia tampak hebat, {b}Erik{/b}?"

    erik @ f_surprised "!!!"
    erik "Uhh..."

    show anon f_shy
    iwanka "Saya tahu saya tampak hebat!"

    iwanka "Ini gaun Poolada seharga tiga puluh lima ratus dolar!"

    anon f_shock "Tiga puluh lima ratus dolar?!"

    iwanka a_popsicle_give "Bisakah seseorang mengambil ini?"

    iwanka "Saya mengatakan kepadanya bahwa saya tidak menginginkannya tetapi dia bersikeras."

    show iwanka a_idle
    show erik a_popsicle f_woozy:
        xoffset -40
    with dissolve
    anon f_shy "Ya, dia melakukan itu."

    show iwanka f_surprised_up
    erik a_popsicle_eat f_eat @ -m_talk "Tidak!"

    iwanka f_disgusted "Jadi, apakah ini pestanya?"

    iwanka "Dimana semua orang?"

    anon f_worried "Oh, umm... Saya yakin akan ada lebih banyak lagi yang akan datang."

    show erik a_whisper f_nervous with {'master': dissolve}:
        flip
        xoffset 400
    erik "Bung, siapa lagi yang kamu undang?"

    anon @ f_worried_low "Tak seorang pun kecuali dia yang tidak mengetahui hal itu..."

    show erik a_idle with {'master': dissolve}:
        unflip
        xoffset -40
    erik @ f_normal_right "Oh benar!"

    anon f_shy @ a_behind_head "Mereka mungkin hanya mencoba untuk datang terlambat, Anda tahu?"

    iwanka f_normal @ f_laugh "Aww, lihat... Aku tahu aku seharusnya melakukan itu!"

    iwanka "Tidak ada seorang pun yang ingin menjadi orang pertama yang tiba di sebuah pesta."

    anon "Bisakah kami membuatkanmu minuman atau apa?"

    iwanka @ f_laugh "Oh, tolong minum!"

    iwanka "Sesuatu yang kuat tapi berbuah."

    anon f_normal "Segera hadir!"

    anon "{b}Erik{/b}, bisakah?"

    erik f_worried_right "Hah?"

    anon f_worried "Ayo buatkan {b}Iwanka{/b} minuman."

    erik f_sad "Ehh..."

    show erik a_whisper with dissolve:
        flip
        xoffset 400
    erik "Saya tidak tahu bagaimana melakukan itu!"

    anon @ f_worried_low "Tidak bisakah kamu mencarinya di ponselmu atau apalah?"

    erik f_laugh @ f_surprised "Oh benar!"

    erik "Ide bagus, {b}[firstname]{/b}."

    hide erik with dissolve
    show anon f_shy
    pause
    anon "Jadi..."

    anon "Ada masalah saat menyelinap keluar?"

    iwanka f_bored "Nah, ibuku pingsan karena mabuk dan ayahku sibuk dengan salah satu pembantu rumah tangga."

    anon f_shy "Jadi begitu."

    pause
    anon "Bukankah kalian punya banyak penjaga keamanan?"

    iwanka f_normal @ f_eyeroll "Pfft, mereka tidak peduli dengan apa yang aku lakukan."

    show erik a_glass f_nervous behind iwanka with dissolve:
        xoffset -40
    pause
    iwanka "Apakah itu untukku?"

    erik "Uhh..."

    anon "Ya, itu pasti milikmu."

    show iwanka a_glass:
        xoffset -20
    show erik a_idle
    with dissolve
    pause
    iwanka f_concerned "Dia tidak banyak bicara, kan?"

    anon @ f_normal "Heh, tidak saat ada gadis cantik, tidak."

    iwanka f_normal @ f_laugh "Oh benar!"

    iwanka "Saya ingat Anda menyebutkan itu di pohon."

    iwanka @ f_laugh "Dia mungkin hanya membutuhkan pelumasan sosial untuk membantunya rileks."

    anon f_confused "Pelumasan sosial?"

    iwanka "Ya, kamu tahu..."

    iwanka a_glass_drink f_drink @ f_smirk a_glass_cheer "... Minuman keras."

    show anon f_shy
    show erik a_whisper with dissolve:
        flip
        xoffset 400
    erik "Apakah itu benar-benar berhasil?"

    anon @ f_worried_low "Bagaimana saya bisa tahu?"

    show erik a_idle with dissolve:
        unflip
        xoffset -40
    iwanka a_glass_empty f_smirk "Mmm, saya suka Obeng!"

    iwanka "Enak sekali, seperti, astaga!"

    show erik a_glass_empty
    show iwanka a_idle
    with dissolve
    iwanka "Biarkan mereka datang, bintik-bintik!"

    pause
    show iwanka f_thinking
    show erik a_whisper with dissolve:
        flip
        xoffset 400
    erik "Saya akan mencobanya!"

    anon @ f_normal_low "Hancurkan dirimu sendiri."

    hide erik with dissolve
    iwanka f_normal "Saya suka di bawah sini."

    anon "Anda melakukannya?"

    iwanka "Ya, semua gitar dan pencahayaannya keren!"

    iwanka "Itu mengingatkan saya pada band yang saya kencani beberapa waktu lalu."

    anon @ f_confused "Band?"

    anon "Maksudmu kamu berkencan dengan pemain gitar atau semacamnya?"

    iwanka "Tidak."

    iwanka "Saya berkencan dengan sebuah band."

    anon f_worried "Misalnya, lebih dari satu orang?"

    show erik a_glass behind iwanka with dissolve:
        xoffset -40
    iwanka "Tiga tepatnya."

    show anon f_surprised
    show erik a_idle
    show iwanka a_glass f_laugh
    with dissolve
    iwanka "Terima kasih!"

    show iwanka f_normal
    anon f_shy @ f_confused "Bagaimana cara berkencan dengan tiga orang sekaligus?"

    show erik a_beer with dissolve
    iwanka "Agar adil... Pemain drum dan bass itu seperti berkencan."

    show erik a_beer_drink f_drink with dissolve
    iwanka "Dan saya berkencan dengan gitaris utama."

    show erik a_beer f_normal with dissolve
    iwanka "Tapi suatu malam kami benar-benar mabuk dan mengadakan pesta seks."

    show erik f_woozy
    anon f_surprised "Benar-benar?!"

    iwanka @ f_laugh "Hehe, ya."

    show iwanka a_glass_drink f_drink with dissolve
    pause
    iwanka a_glass_empty f_smirk "enak!"

    anon f_shy "Jadi kamu berempat dengan tiga orang?"

    iwanka "Hehe, tidak."

    show iwanka
    iwanka a_glass_empty_give "Drummernya adalah seorang gadis."

    show iwanka a_idle
    show erik a_glass_empty f_surprised m_talk
    show anon f_shock
    with dissolve
    anon "!!!"
    erik "!!!"
    pause
    show anon f_normal
    show erik a_whisper f_woozy -m_talk:
        flip
        xoffset 400
    with {'master': dissolve}
    erik "Oh, aku menyukainya!"

    show erik a_idle with dissolve:
        unflip
        xoffset -40
    show anon f_shy
    iwanka "Setelah itu, kami menjalin hubungan quad untuk sementara waktu..."

    hide erik with dissolve
    iwanka @ f_eyeroll "... Tapi kemudian masalah menjadi sangat rumit dan saya harus putus dengan mereka."

    anon "Y-ya, aku yakin."

    pause
    iwanka f_normal "Jadi, apa menunya malam ini?"

    anon f_worried "Menu?"

    show iwanka f_smirk
    anon "Apakah kamu lapar?"

    anon "Karena {b}Erik{/b} memberi kami kue keju dan {b}Ny. Johnson{/b} selalu bisa-"

    iwanka @ f_laugh "Hehe, tidak konyol!"

    iwanka "Maksudku, kegiatan apa yang kamu rencanakan malam ini?"

    anon f_shy @ a_behind_head "Oh!"

    anon f_thinking a_thinking "Hmm..."

    iwanka @ f_laugh "Apa sih kue keju itu?"

    show anon a_idle f_shy
    show erik a_glass behind iwanka:
        xoffset -40
    with {'master': dissolve}
    erik "Hanya camilan terlezat di planet ini."

    iwanka "Wow, itu berbicara!"

    erik "Ya, benar."

    show erik a_idle
    show iwanka a_glass
    with dissolve
    iwanka "Sudah kubilang alkoholnya akan berhasil."

    erik "Ya, saya rasa memang demikian."

    iwanka "Mereka tidak menyebutnya sebagai keberanian cair tanpa alasan."

    iwanka a_glass_cheer f_laugh "Bersulang!"

    erik a_beer_cheer f_laugh "Bersulang!"

    show iwanka f_drink a_glass_drink
    show erik a_beer_drink f_drink
    with dissolve
    pause
    show erik a_beer f_woozy with dissolve
    iwanka f_snob a_glass_empty "Woo!!"

    erik @ f_laugh "hehe!"

    anon f_worried "Mungkin Anda harus memperlambat sedikit?"

    iwanka f_smirk "Psh, itu tidak terjadi!"

    iwanka "Ini pertama kalinya aku keluar dalam beberapa bulan."

    show iwanka a_idle
    show erik a_glass_empty
    with dissolve
    iwanka "Pukul aku lagi, bintik-bintik."

    iwanka @ f_laugh "Aku menjadi sia-sia malam ini!"

    erik @ f_laugh "Segera hadir!"

    hide erik with dissolve
    pause
    iwanka @ a_point "Jadi apa yang ada di ruangan sebelah sana itu?"

    anon f_shy @ f_worried -m_talk "Hmm?"

    anon "Oh, itu hanya ruang kerja."

    anon "Ada sofa dan sistem hiburan..."

    anon "... Saya sebenarnya baru saja hendak menyalakan musik."

    iwanka f_normal @ f_surprised "Itu ide yang luar biasa!"

    iwanka "Ayo pergi."

    hide iwanka
    show anon f_worried a_sides:
        unflip
        xoffset 600
    with dissolve
    anon "T-tunggu aku!"

    pause
    anon f_thinking a_thinking @ -m_talk "(Saya lebih baik berbicara dengan {b}Erik{/b} tentang minuman itu. )"

    hide anon with dissolve
    return

label ano17_talk_erik:
    scene expression background(200, 480, 4.) as stage
    show erik a_glass_empty:
        flip
    show anon f_worried_low with dissolve:
        flip
    anon "Berapa banyak alkohol yang Anda masukkan ke dalam minuman tersebut?"

    show anon f_worried
    erik "Situs webnya menyebutkan lima puluh lima puluh vodka dan jus jeruk."

    anon "Baiklah, baiklah... Mungkin kita harus mengurangi nadanya sedikit."

    erik @ f_sad "Turunkan nadanya?"

    anon "Saya tidak bisa bertanya tentang ayahnya dan orang Rusia jika dia tidak sadarkan diri, bukan?"

    erik f_woozy "Tenang, kawan."

    erik "Ini bukan gadis remaja dari sekolah."

    erik "Aku cukup yakin {b}Iwanka{/b} bisa mengatasi alkoholnya..."

    anon f_sad "{b}Erik{/b}, aku serius!"

    anon "Ini penting."

    erik "Percayalah padaku, kawan!"

    anon @ f_unimpressed -m_talk "..."
    iwanka "{b}[firstname]{/b}!!"

    show anon f_worried with dissolve:
        unflip
        xoffset 500
    anon @ -m_talk "Hmm?"

    iwanka "Apakah kamu datang?"

    anon "Ya, segeralah ke sana!"

    show anon with dissolve:
        flip
        xoffset 0
    erik "Aku akan menangani minumannya."

    erik "Anda hanya fokus untuk mendapatkan jawaban darinya."

    anon f_sad_down a_sides "Uh, baiklah."

    hide anon with dissolve
    return

label ano17_porn_erik:
    scene expression player.location.background_blur
    show anon f_shy with dissolve
    anon @ -m_talk "(Saya harus bergegas ke {b}Iwanka{/b}. )"

    anon @ -m_talk "(Dia ada di ruang kerja.)"

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
