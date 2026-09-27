label ano17_porn_iwanka:
    scene expression background(768, 400, b=.75) as stage:
        anchor (1., 400 / 768.)
        pos (1., .5)
        zoom 2
    show iwanka b_club_back
    show anon f_shy with dissolve:
        xoffset -100
    anon "Apakah musik ini oke?"

    show iwanka b_club with dissolve
    iwanka @ -m_talk "Hmm?"

    iwanka "Ya, tidak apa-apa."

    show iwanka b_club_back with dissolve
    show anon f_flirt_low
    iwanka "Apakah ini ikan asli?"

    anon "Ya."

    iwanka "Sangat keren!"

    show iwanka b_club
    show anon f_shy
    with dissolve
    iwanka "Saya selalu menginginkan akuarium tetapi ibu saya tidak mengizinkan saya memilikinya."

    anon "Kenapa?"

    iwanka @ f_eyeroll "Karena dia hampir tenggelam di kolam koi saat aku masih kecil."

    anon f_surprised "Apa?!"

    iwanka @ f_laugh "Hehe, ya!"

    anon "Bagaimana hal itu bisa terjadi?"

    iwanka f_smirk "Kami dulu punya satu di halaman belakang rumah lama kami."

    iwanka "Dan suatu malam, yah... Dia terlalu banyak minum dan terjatuh."

    anon "Anda bercanda!"

    iwanka @ f_laugh "Tidak."

    iwanka "Rupanya, bagian bawahnya sangat licin karena lumut atau semacamnya dan dia tidak bisa berdiri dengan sepatu hak tingginya."

    anon f_worried "Bagaimana dia keluar?"

    iwanka @ f_laugh "Heh, salah satu kepala pelayan harus melompat dan menyelamatkannya..."

    iwanka "... Itu lucu sekali!"

    anon "Dan itulah alasan dia tidak mengizinkan Anda memiliki akuarium?"

    iwanka "Ya, itulah alasan utamanya."

    iwanka "Dia tidak pernah benar-benar melihat betapa menariknya memiliki hewan peliharaan."

    iwanka @ f_drunk a_point "\"Ajak saja salah satu pelayan jalan-jalan jika kamu sangat membutuhkan hewan peliharaan, {b}Iwanka{/b}!\""

    show anon f_surprised_teeth
    iwanka "Yang mana, tidak berhasil. FYI."

    iwanka f_snob "Lupe memang mengeluh saat aku memasangkan tali itu padanya..."

    show erik a_glass behind iwanka:
        flip
        xoffset 50
    show anon f_shock
    with dissolve
    pause
    iwanka f_smirk @ f_laugh "... Dan dia tidak pandai melakukan trik."

    anon f_surprised @ -m_talk "..."
    erik f_woozy "{i}*Ahem*{/i} Minuman Anda, Nyonya."

    show erik a_idle
    show iwanka a_glass f_laugh
    show anon f_normal
    with dissolve
    iwanka "hehe!"

    iwanka a_glass_drink f_drink @ f_smirk a_glass_cheer "Terima kasih, tuan yang baik hati!"

    pause
    iwanka f_drunk a_glass_empty "Mmm, ini enak sekali!"

    iwanka "Apakah kamu suka, cahaya bulan sebagai bartender atau semacamnya, bintik-bintik?"

    erik f_shy "Aku?"

    erik "T-tidak, aku belum pernah merawat bar seumur hidupku..."

    iwanka "Anda harus memeriksanya!"

    show iwanka a_glass_empty_give with dissolve
    erik f_normal "Maksudku, aku memang menghabiskan sedikit waktu untuk meningkatkan skill alkimiaku tapi itu hanya untuk sebuah pencapaian."

    show iwanka f_laugh a_idle
    show erik a_glass_empty
    with dissolve
    iwanka "Hehe, apa?!"

    show iwanka f_drunk
    erik "Saya agak terlalu komplet dalam hal {i}Dunia Orcette{/i}."

    iwanka @ f_disgusted "Saya tidak tahu apa yang Anda bicarakan."

    iwanka @ a_point "Fiuh, sepertinya minuman ini mulai menarik perhatianku!"

    show erik f_woozy
    anon f_worried "Mungkin sebaiknya kita duduk..."

    iwanka "Hehe, oke."

    anon "... Anda dapat bercerita lebih banyak tentang keluarga Anda."

    iwanka f_disgusted "Eww, tunggu... Tidak."

    anon @ -m_talk "Hmm?"

    iwanka "Aku tidak mau bicara tentang keluargaku, mereka payah!"

    anon "Itu-"

    iwanka f_drunk @ f_laugh "Ayo menari!"

    anon f_shy "Ehh, aku bukan penari yang hebat..."

    show layer master:
        ease 1.6 xpos 685
    with None
    show iwanka b_club_pulling_mc:
        xoffset -690
    show anon b_empty f_surprised:
        flip
        xoffset -650
    show erik a_idle:
        unflip
        xoffset -450
    with {'master': MultipleTransition((False, Pause(.2), False, slowdissolve, True))}
    iwanka "Ayo, ini akan menyenangkan!"

    show iwanka b_club:
        flip
        xoffset -685
    show anon b_dressed f_shy:
        flip
        xoffset -885
    with {'master': dissolve}
    iwanka "Jika Anda memainkan kartu Anda dengan benar, saya mungkin akan membiarkan Anda merasakannya."

    show erik f_nervous
    show anon f_surprised
    pause
    show anon f_normal behind iwanka with {'master': dissolve}:
        unflip
        xoffset -550
    iwanka "Bagaimana menurutmu, bintik-bintik?"

    iwanka @ a_point "Anda ingin berdansa dengan kami?"

    erik "Ehh."

    show erik a_whisper f_thinking with dissolve:
        flip
        xoffset -80
    erik "Apa itu, {b}Tam{/b}?"

    show erik f_worried_right
    pause
    show anon f_worried
    show iwanka f_disgusted
    erik f_thinking "Tentu, saya akan segera ke sana!"

    show erik a_idle f_nervous with dissolve:
        unflip
        xoffset -450
    erik "Kalian berdua silakan saja, dia memanggilku."

    iwanka "Aku tidak mendengar apa pun..."

    hide erik with {'master': dissolve}
    erik "Aku akan memberimu isi ulang dalam perjalanan pulang!"

    iwanka f_smirk @ f_excited "Buatlah menjadi ganda!!"

    erik "Saya tidak tahu apa artinya tapi oke!"

    iwanka "Menurutku, hanya kamu dan aku saja, ya?"

    show anon f_shy with dissolve:
        flip
        xoffset -785
    anon "Y-ya, menurutku..."

    $ M_iwanka.set('sex speed', .3)
    show iwanka b_club_dance with dissolve
    show anon f_surprised a_surprised_up_both with dissolve
    pause
    anon f_flirt_low a_sides "Wah, kamu um..."

    anon "... Sangat pandai dalam hal ini."

    iwanka @ -m_talk "hehe!"

    pause
    show iwanka b_club with dissolve
    show anon f_shy
    iwanka "Nah, tunggu apa lagi?"

    anon "Hmm."

    anon "O-oke."

    show anon b_dressed_dance_shy with dissolve
    show iwanka f_disgusted
    pause
    iwanka f_smirk @ a_point "Wow, kamu payah dalam hal ini..."

    show anon b_dressed f_unimpressed with fastdissolve
    anon "Sudah kubilang!"

    iwanka @ f_laugh "Hahahaah!"

    pause
    iwanka "Masalahmu adalah kamu terlalu minder."

    anon f_worried @ -m_talk "Hmm?"

    iwanka "Anda perlu sedikit rileks."

    iwanka "Menari adalah tentang bersenang-senang dan tidak mengkhawatirkan apa yang dipikirkan orang lain."

    show iwanka b_club_dance_back behind anon
    show anon f_flirt_low
    with dissolve
    pause
    iwanka @ -m_talk "Melihat?"

    anon "Eh ya."

    pause
    iwanka @ -m_talk "Itu mudah."

    iwanka @ -m_talk "Pindah saja ke musik dan lakukan apa yang terasa alami."

    show anon behind iwanka
    show iwanka b_club_dance with dissolve
    anon "Eh ya."

    pause
    show iwanka b_club
    show anon f_shy a_behind_head
    with dissolve
    iwanka "Ayo goyangkan pinggulmu {b}[firstname]{/b}!"

    anon "Ehh, menurutku lebih baik aku menonton saja..."

    iwanka "Cih, jangan jadi pengacau pesta!"

    show iwanka b_club_dance_back behind anon with dissolve
    iwanka @ -m_talk "Diam saja dan menari!"

    pause
    anon "Eh, benar..."

    show anon b_dressed_dance_flirt_low with dissolve
    pause
    anon @ -m_talk "(Ya ampun, lihat pinggulnya...)"

    anon b_dressed_dance_unimpressed @ -m_talk "( ... Dan di sini aku terlihat seperti orang idiot. )"

    pause
    iwanka @ -m_talk "Bagaimana kabarnya kembali ke sana?"

    anon b_dressed_dance_flirt_low @ b_dressed_dance_shy_talk "Hanya menikmati pemandangan."

    iwanka @ -m_talk "hehe!"

    anon @ -m_talk "(Tolong jangan berbalik!)"

    pause
    erik "Oke, siapa yang siap minum lagi?!"

    show erik a_glass:
        unflip
        xoffset -450
    show iwanka b_club f_laugh
    show anon a_sides b_dressed behind iwanka:
        unflip
        xoffset -400
    with {'master': dissolve}
    iwanka "{i}*Terkesiap*{/i} Aku!!"

    hide iwanka
    hide erik
    show anon b_dressed_catch_breath:
        flip
        xoffset -785
    with slowdissolve
    anon @ -m_talk "(Oh, syukurlah.)"

    anon @ -m_talk "(Saya harus berterima kasih kepada {b}Erik{/b} atas penyelamatannya setelah dia pergi... )"

    erik "Ayo duduk di sofa dan bantu aku memilih permainan papan!"

    iwanka "Permainan papan?"

    show anon f_surprised b_dressed a_surprised_up_both with dissolve
    pause
    anon a_fists f_unimpressed "(... Dan setelah aku selesai membunuhnya!)"


    scene location_erik_basement_back_couch
    show iwanka b_sidebed_right a_glass f_disgusted
    show erik b_sidebed a_orcette_figure
    with fade
    iwanka "Dan permainan ini disebut {i}Orcette Party{/i}?"

    erik @ -m_talk "Mhmm!"

    erik "Ini Orcette di sini, dia adalah pemimpin faksi Orc."

    iwanka f_smirk "Dia seksi!"

    erik "Oh, tentu saja!"

    erik "Dia juga sangat kuat!"

    erik "Anda setidaknya harus berada di level tujuh puluh lima sebelum Anda dapat memberikan tantangan padanya."

    iwanka f_disgusted "Um, oke..."

    show anon b_sit f_worried with dissolve:
        xoffset -250
    iwanka "... Tapi apa itu Orc?"

    erik f_surprised "Hah?"

    erik f_worried "Kamu tidak serius, kan?"

    anon "{b}Erik{/b}, tidak semua orang menyukai permainan peran fantasi..."

    erik "Y-ya, oke."

    erik f_normal "Orc adalah suku humanoid hijau yang tinggal di gua."

    iwanka f_suspicious "Humanoid?"

    erik "Artinya mereka memiliki ciri-ciri manusia."

    erik "Tahukah Anda, bipedal, dua lengan, relatif tinggi dibandingkan lebar..."

    iwanka f_disgusted @ -m_talk "..."
    anon f_unimpressed "Katanya mereka mirip seperti kita, tapi hijau."

    iwanka b_sidebed_left f_normal "Oh baiklah!"

    iwanka "Itu masuk akal."

    show iwanka b_sidebed_right with {'master': dissolve}
    erik "Yah, secara teknis mereka memiliki lebih banyak kesamaan dengan elf daripada manusia, tapi menurutku kita tidak perlu membahasnya..."

    show iwanka a_glass_orcette f_smirk_down
    show erik a_idle
    with dissolve
    pause
    iwanka @ f_suspicious "Apakah payudaranya seharusnya asli?"

    iwanka @ f_laugh "Karena saya dapat memberitahu Anda dari pengalaman bahwa dibutuhkan banyak uang untuk membuat mereka berdiri seperti itu!"

    show iwanka f_drink a_glass_drink b_sidebed_left
    show erik a_orcette_figure
    with dissolve
    erik "Ehh, mereka mungkin ditingkatkan secara ajaib atau semacamnya?"

    show iwanka a_glass f_suspicious b_sidebed_right with dissolve
    iwanka @ f_suspicious "Ditingkatkan secara ajaib?"

    anon "Tahukah kamu, kita sebenarnya tidak perlu membicarakan hal ini, {b}Iwanka{/b}."

    show iwanka b_sidebed_left f_normal with dissolve
    iwanka "Tidak, tidak apa-apa."

    iwanka @ f_suspicious "Itu umm... Menarik... menurutku."

    show iwanka b_sidebed_right a_glass_orcette
    show erik a_idle
    with dissolve
    iwanka "Jadi bisakah aku menjadi Orcette?"

    erik @ f_laugh "Tentu!"

    iwanka @ f_suspicious_down "Apakah dia mendapatkan pedang atau semacamnya?"

    erik "Sebenarnya dia menggunakan tombak yang terbuat dari tulang ular raksasa."

    iwanka @ f_laugh "Bagus sekali!"

    iwanka f_smirk "Oke, berikan tombakku, aku ingin mengacau!"

    erik "Lihat, aku tahu dia akan terlibat dalam hal ini!"

    anon @ -m_talk "..."
    erik "Aku akan mengambil sisanya."

    erik "{b}[firstname]{/b}, apakah kamu ingin menjadi Ivar yang Tak Puas atau Joxer yang Berkah?"

    anon @ f_skeptical "Apakah itu penting?"

    show iwanka b_sidebed_left with dissolve
    iwanka "Pergilah bersama yang berkekuatan besar, lalu kita lihat siapa yang memiliki tombak lebih besar."

    show erik f_worried
    show anon f_shy of_blush
    with {'master': dissolve}
    anon f_shy "Ehh."

    show anon -of_blush with {'master': slowdissolve}
    iwanka @ f_laugh "Hehehe!"

    show iwanka b_sidebed_right with {'master': dissolve}
    erik "Tidak tidak tidak!"

    erik f_normal "Joxer tidak menggunakan tombak."

    erik "Dia seorang penyair, jadi dia menggunakan kecapinya untuk melawan kejahatan!"

    iwanka f_smirk @ f_laugh "Oh, seorang musisi, bahkan lebih baik lagi!"

    iwanka "Mereka seperti, sangat seksi."

    erik @ f_laugh "Saya akan segera kembali!"

    iwanka a_glass_finger "Tunggu, bintik-bintik."

    show iwanka a_glass_drink f_drink b_sidebed_left with dissolve
    pause
    show iwanka a_idle f_drunk b_sidebed_right with dissolve
    iwanka @ -m_talk "Hmm!!!"

    iwanka "Pukul aku lagi!"

    erik a_thumbs "O-oke."

    hide erik
    show iwanka b_sidebed_left f_smirk
    with dissolve
    show anon f_shy
    pause
    anon "Jadi..."

    iwanka f_drunk "Bolehkah saya memberi tahu Anda sebuah rahasia, {b}[firstname]{/b}?"

    anon "B-yakin?"

    iwanka "Saya seperti, sangat terbuang saat ini."

    anon f_worried "Ya, saya bisa melihatnya."

    iwanka @ f_laugh "Hehehe!"

    anon f_shy "Apakah kamu minum seperti ini di pesta orang tuamu?"

    iwanka @ f_eyeroll "Ah, andai saja..."

    iwanka "... Mereka tidak mengizinkan saya minum selama pesta mereka."

    iwanka @ f_bored "Sebenarnya, menurutku aku belum pernah mabuk seperti ini sejak aku lulus kuliah."

    anon "Oh?"

    iwanka "Ya."

    iwanka "Sangat menyenangkan di sana!"

    iwanka f_sad "Saya berharap saya bisa kembali."

    pause
    iwanka f_drunk "Ya ampun, kali ini, tahun pertama..."

    iwanka "... Kami sedang berkendara dengan limusin pesta teman saya Damian dan saya merasa sangat terpukul dengan jello shot, bukan?"

    anon f_worried "Eh ya."

    iwanka "Dan teman saya yang lain, Macy, berkata, \"Kita harus mengerjakan tiang penari telanjang itu bersama-sama!\""

    iwanka "Kedengarannya sangat menyenangkan... Tapi kami sangat terbuang, kami hanya berakhir dalam kekacauan di lantai!"

    iwanka @ f_laugh "Hahahaah!"

    anon f_tired "Eh ya."

    iwanka "Dia hanya berkata, \"Ya ampun, kenapa kamu jadi wanita jalang mabuk yang bodoh?\""

    iwanka "Dan aku seperti, \"Ck, kamulah yang tidak bisa berdiri!\""

    anon @ -m_talk "..."
    iwanka @ f_laugh "Lalu kami bermesraan sementara semua orang di limusin menonton."

    anon "Eh ya."

    pause
    anon f_surprised "Tunggu-"

    anon "Apa bagian terakhir itu?"

    iwanka "Lalu dia menyerangku."

    anon f_shock "..."
    iwanka @ a_shrug "Ya, aku jadi agak jorok saat minum."

    anon f_shy "Lalu apa yang terjadi?"

    iwanka "Aku muntah di dompetnya."

    anon f_disgusted @ -m_talk "!!!"
    iwanka "Dan itu bukan metafora, aku benar-benar muntah di dompet Vispucci seharga sebelas ratus dolar."

    iwanka @ f_laugh "Dia sangat marah!"

    anon "Y-ya, aku bisa membayangkannya."

    iwanka "Itu menyenangkan!"

    iwanka f_annoyed "Sampai staf ayah saya menemukan videonya secara online."

    anon f_shy "Oh?"

    iwanka "Dia membuatku pulang dan menghabiskan sisa liburan musim semi di resor pulau ini bersama ibuku..."

    anon "Kedengarannya tidak terlalu buruk bagi saya."

    iwanka f_disgusted "Ugh, itu karena kamu tidak mengenal ibuku..."

    anon "Itu benar."

    iwanka "... Yang dia lakukan sepanjang perjalanan hanyalah mengeluh tentang ayahku!"

    pause
    iwanka "Oh, dan persetan dengan anak cabana itu!"

    anon @ f_surprised "!!!"
    iwanka @ f_eyeroll "Aku bersumpah, tidak ada terapi yang cukup di dunia ini untuk membantuku mengatasi hal-hal yang kudengar dari kamar hotelnya!"

    anon "Apakah ayahmu dan dia sering bertengkar?"

    iwanka f_suspicious @ -m_talk "Hmm?"

    iwanka "Um, kurasa..."

    anon "Apa yang mereka pertengkarkan?"

    iwanka "Ck, kenapa kamu begitu tertarik dengan orang tuaku?"

    anon f_worried "Apakah saya?"

    iwanka "Anda terus bertanya tentang mereka, setiap lima menit!"

    anon "Maafkan aku, aku tidak bermaksud-"

    iwanka f_annoyed "Apa menurutmu aku jelek atau apa?"

    anon "T-tidak, tentu saja tidak!"

    anon "aku hanya... um..."

    anon f_shy "... Mencoba mempelajari lebih lanjut tentang Anda..."

    show iwanka f_suspicious
    pause
    anon "... Karena aku sangat menyukaimu!"

    iwanka f_drunk "Ah, benarkah?!"

    anon "Ya?"

    iwanka @ f_laugh "Kamu manis sekali, {b}[firstname]{/b}!"

    anon @ f_grin -m_talk "Mhmm."

    iwanka "Saya pikir kita harus suka, jalan-jalan lagi kapan-kapan!"

    anon "Ya, tentu saja."

    pause
    anon "Mungkin Anda bisa mengundang saya ke tempat Anda?"

    iwanka f_annoyed "Eh, tidak..."

    anon f_worried "Tidak?"

    iwanka "Yah, itu agak memalukan tapi..."

    iwanka "... Ayahku tidak mengizinkanku mengundang anak laki-laki kemari."

    anon "Benar-benar?"

    iwanka "Ya, itu sudah menjadi peraturan sejak aku berumur tiga belas tahun."

    anon f_confused "Tapi kamu sudah menjadi wanita dewasa..."

    iwanka @ f_drunk "Aku tahu, kan?!"

    iwanka "Ini sangat konyol!"

    anon f_worried "Apakah ada cara agar aku bisa menyelinap masuk atau apa?"

    iwanka f_smirk "Anda ingin mencoba dan menyelinap ke tanah milik ayah saya?"

    anon f_shy "Jika itu berarti aku bisa bertemu denganmu, tentu saja!"

    iwanka f_drunk @ f_laugh "Aduh!!"

    anon "Ide buruk?"

    iwanka @ a_shrug "Ya, tidak jika Anda menikmati disetrum..."

    anon @ f_surprised_teeth "!!!"
    anon "{i}*Ahem*{/i} Saya tidak."

    iwanka @ f_laugh "hehe!"

    anon "Ada ide lain?"

    iwanka f_thinking "Nah, ada satu hal yang mungkin berhasil..."

    anon f_normal "Oh?"

    iwanka f_smirk "... Kamu ingin tahu?"

    anon f_shy "Saya bersedia."

    iwanka "Anda {i}benarkah{/i} ingin tahu?"

    anon "Ya, tolong!"

    iwanka f_drunk "Sederhana saja."

    iwanka "Yang harus Anda lakukan adalah-"

    erik "aku kembali!"

    show iwanka b_sidebed_right
    anon f_hurt @ f_surprised "!!!" with hpunch
    show erik b_sidebed a_glass f_woozy with dissolve
    erik "Apakah kamu merindukanku?"

    anon "(Tidaaaak!!!)"

    iwanka @ f_laugh "Oh, apakah itu minumanku?"

    erik "Tentu saja, Nyonya."

    show anon f_unimpressed
    iwanka "Beri aku, beri aku!"

    show iwanka a_glass
    show erik a_box
    with dissolve
    erik "Oke, jadi mungkin perlu waktu beberapa saat untuk memahami semua peraturan..."

    show iwanka a_glass_drink f_drink b_sidebed_left with dissolve
    pause
    show iwanka a_glass f_drunk b_sidebed_right with dissolve
    erik f_worried "... Dan beberapa bagian permainannya agak... Umm, lengket."

    anon f_worried "{i}*Huh*{/i} Tentu saja mereka..."

    erik f_normal "Tapi tidak ada yang perlu dikhawatirkan."

    erik "Hanya sesuatu yang terjadi pada action figure seiring berjalannya waktu."

    anon f_angry "{b}Erik{/b}, kita sedang ngobrol!"

    erik f_worried "O-oh?"

    anon f_shy "Apa yang kamu katakan, {b}Iwanka{/b}?"

    iwanka b_sidebed_left @ f_laugh "Aku ingin menari lagi!"

    anon f_worried "Hah?"

    hide iwanka with dissolve
    anon "Tapi bagaimana dengan-"

    pause
    anon f_angry "Sial, {b}Erik{/b}!!"

    erik "Saya pikir kita akan bermain?"

    anon "Tidak ada yang mau bermain permainan papan!"

    erik f_sad "Maafkan aku, {b}[firstname]{/b}... Aku-"

    iwanka "Apakah kalian datang?!"

    anon f_tired @ f_worried_forward "Ya, sebentar."

    anon "Bung, dia baru saja hendak memberitahuku cara masuk ke dalam perkebunan!"

    erik f_angry "Yah, aku tidak tahu itu..."

    erik "Saya hanya mencoba membantu!"

    anon "{i}*Huh*{/i} Kamu baru saja membuatku sangat kacau!"

    erik "Aku bilang aku minta maaf!"

    iwanka "Ahhh!!!"

    "{i}*Crash*{/i}" with hpunch
    show anon f_surprised_low
    show erik f_surprised_down a_idle with dissolve:
        flip
        xoffset 550
    erik "Oh sial!"

    hide anon with dissolve
    anon "{b}Iwanka{/b}!!!"


    scene location_erik_basement_back_floor with fade
    iwanka "Pffft, hahahah!!"

    anon "Apakah kamu baik-baik saja?!"

    iwanka "Saya pikir saya punya oopsi."

    anon "Ya, benar."

    iwanka "Aku sangat terbuang saat ini!!"

    iwanka "Hahahaah!"

    pause
    anon "Biarkan aku membantumu berdiri..."

    show iwanka_face_f_floor_surprised
    iwanka "Hmm?"

    hide iwanka_face_f_floor_surprised
    iwanka "Apa ini?"

    show iwanka_face_f_floor_surprised
    erik "Ehh, itu bukan apa-apa!"

    erik "Jangan melihat-"

    hide iwanka_face_f_floor_surprised
    iwanka "{i}Warcock{/i}?"

    erik "!!!"

    scene expression background(424, 400, 2.) as stage
    show erik f_worried:
        flip
        xoffset 100
    show anon f_worried:
        xoffset -100
    with fade
    iwanka "{i}Peri Menjadi Liar{/i}?"

    erik "Salah satu teman guildku meninggalkan itu di sini..."

    anon "Kamu tidak terluka, kan?"

    show iwanka b_club f_disgusted a_dvd_show with dissolve:
        xoffset 50
    iwanka "{i}Putri Nelayan{/i}?"

    iwanka a_dvd "Apakah ini DVD porno?"

    erik "T-tidak..."

    iwanka "Yang ini dianimasikan!"

    erik "Ya, itu disebut hentai."

    show iwanka f_suspicious
    show anon f_confused
    pause
    erik f_nervous @ f_worried_right "Maksudku, itulah yang diberitahukan kepadaku..."

    erik "... Oleh orang-orang yang menonton hal itu..."

    pause
    erik f_sad_down "... Teman-teman, bukan aku."

    iwanka @ -m_talk "Mhmm."

    iwanka f_smirk_down "\"Kano sang nelayan dan keluarganya selalu sangat mencintai laut... Namun bagi putrinya yang menggairahkan, Hamako, cinta itu berjalan dua arah!\""

    iwanka "\"Bisakah nafsunya yang besar terhadap penghuni lautan terpuaskan?\""

    iwanka "\"Apakah kebejatannya tidak mengenal batas?!\""

    anon f_surprised "Kawan, apakah itu tentakel porno?"

    erik @ f_worried_right "Itu bukan milikku, aku bersumpah!"

    iwanka f_suspicious "Jadi dia suka, berhubungan seks dengan ikan atau apa?"

    erik @ -m_talk "..."
    iwanka f_drunk @ f_laugh "Ya ampun, bolehkah kita menontonnya?!"

    show erik f_surprised m_talk
    anon f_surprised "APA?!"

    erik -m_talk "!!!"
    iwanka "Aku ingin melihatnya bercinta dengan ikan!"

    erik f_normal @ f_eyeroll "Cih, dia tidak bercinta dengan ikan..."

    anon f_worried "Saya pikir Anda bilang Anda belum pernah melihatnya!"

    show erik f_nervous with {'master': dissolve}:
        unflip
        xoffset -350
    erik "Yah, yang jelas aku berbohong!"

    erik "{i}*Huh*{/i} Dia meniduri gurita..."

    pause
    show erik f_sad_down with dissolve:
        flip
        xoffset 100
    erik "... Lalu cumi-cumi."

    show anon f_hurt a_facepalm with dissolve
    pause
    erik f_woozy "Lalu keduanya."

    iwanka @ f_laugh "Oh, kami sangat menonton ini!!"

    show anon f_surprised a_sides with dissolve
    erik f_worried "Kamu serius?"

    iwanka "Ya, cepatlah!"

    show erik a_dvd
    show iwanka a_idle
    with dissolve
    erik f_normal "B-baiklah."

    hide erik with dissolve
    anon f_worried "Anda benar-benar ingin melihat seorang wanita berhubungan seks dengan cumi-cumi?"

    iwanka "Dan seekor gurita!"

    anon f_tired -m_talk "..."
    iwanka f_suspicious "Jangan dibuat aneh-aneh, {b}[firstname]{/b}."

    hide iwanka
    show anon f_surprised:
        flip
        xoffset -550
    with {'master': dissolve}
    iwanka "Ayo duduk bersamaku!"

    anon f_eyeroll "Ya, akulah yang membuatnya aneh."

    hide anon with dissolve

    scene location_erik_basement_back_couch
    show iwanka b_sidebed_right_shy f_drunk
    with fade
    show anon b_sit f_worried behind iwanka with {'master': dissolve}:
        xoffset -250
    anon "Ini sebaiknya tidak membangkitkan sesuatu dalam diriku..."

    show iwanka b_sidebed_left_shy f_laugh with dissolve
    iwanka "Hah, santai saja!"

    iwanka f_drunk "Dengan premis seperti ini, pasti cheesy dan jenaka."

    show erik b_sidebed with dissolve
    show iwanka b_sidebed_right_shy
    erik "Anda salah."

    erik "Ini sebenarnya ditulis dengan sangat baik dan cukup erotis."

    iwanka @ f_laugh "Kamu sangat kenyang!"

    erik "aku serius!"

    show anon f_tired
    iwanka "Ssst!!"

    iwanka "Ini dimulai."

    show erik behind iwanka with dissolve:
        flip
        xoffset 550
    pause
    iwanka f_suspicious @ f_disgusted "Apa yang-"

    iwanka "Apakah ini semua dalam bahasa Jepang?"

    erik "Ya, Anda harus membaca subtitlenya."

    iwanka f_disgusted "Dengan serius?"

    iwanka "Jika saya ingin membaca, saya akan membeli buku!"

    iwanka f_drunk "Ceritakan saja apa yang terjadi dan lanjutkan ke bagian yang menarik."

    erik f_worried_right "Benar-benar?"

    iwanka "Aku ingin melihatnya disetubuhi oleh tentakel!"

    show anon f_surprised_teeth
    erik "Oke oke..."

    show anon f_tired
    hide erik
    with dissolve
    pause
    erik "Pada dasarnya, ayahnya adalah seorang nelayan dan suatu hari seekor bayi gurita tertangkap jaringnya."

    show anon f_tired with {'master': dissolve}
    erik "Dia membawanya pulang, berniat mengubahnya menjadi tako; tapi Hamako menghentikannya karena itu sangat lucu."

    iwanka @ f_laugh "Ah, aku ingin melihat bayinya!"

    erik "Tunggu."

    pause
    erik "Di sana."

    show anon f_tired_happy
    iwanka "Ya ampun, itu menggemaskan!!!"

    show iwanka b_sidebed_left_shy with dissolve
    iwanka "Lihatlah mata kecilnya yang sedih!!!"

    show iwanka b_sidebed_right_shy with dissolve
    anon "Eh ya."

    show anon f_tired
    iwanka "Oke, lalu apa yang terjadi!"

    erik "Nah, Hamako memohon kepada ayahnya untuk membiarkan dia memelihara bayi gurita itu sebagai hewan peliharaan..."

    erik "... Dan selama bertahun-tahun, pertumbuhannya menjadi sangat besar."

    erik "Saking besarnya, dia harus melepaskannya kembali ke laut."

    iwanka f_pouting "Ah, itu menyedihkan!"

    label ano17_porn_iwanka.replay:
    erik "Tapi dia kembali setiap malam dan menunggu di dermaga hingga dia mengunjunginya."

    erik "Kalau begitu, baiklah..."

    erik "... Anda akan lihat."

    iwanka f_smirk @ f_laugh "Ayo, ayo, ayo!"

    show erik b_sidebed behind iwanka with dissolve:
        flip
        xoffset 550
    pause
    iwanka "Oke, jadi itu memeluknya..."

    pause

    scene location_erik_basement_back_hentai_pre with fade
    iwanka "Wah, lihat semua tentakel itu!"

    pause
    iwanka "Sepertinya itu akan menggelitik..."

    pause

    scene location_erik_basement_back_couch
    show anon b_sit f_skeptical:
        xoffset -250
    show erik b_sidebed f_woozy o_boner:
        flip
        xoffset 550
    show iwanka b_sidebed_right_shy f_smirk
    with fade
    anon f_tired @ f_skeptical "Pastinya pakaian tidak meledak begitu saja..."

    iwanka "Ssst!!"

    pause
    iwanka @ f_suspicious "Bagaimana cara berhubungan seks dengan gurita?"

    erik "Mereka memiliki kelenjar seks di tentakelnya."

    iwanka "Benar?"

    erik "Setidaknya di film."

    pause
    show iwanka f_concerned
    pause
    iwanka "Tidak mungkin itu bisa muat di dalam-"

    show anon f_surprised_down o_sit_boner with {'master': dissolve}
    iwanka f_surprised "Oh, sudahlah... Ini dia."


    $ M_iwanka.set('sex speed', 1 / 12.)

    scene location_erik_basement_back_hentai_sex
    show iwanka_sex_hentai
    with fade
    iwanka "Wah, di pantatnya juga ya?"

    erik "Yah, hanya satu untuk saat ini."

    iwanka "Satu saja sudah cukup, percayalah..."

    iwanka "... Dan lihat betapa tebalnya mereka!"

    pause

    scene location_erik_basement_back_couch
    show anon b_sit f_worried o_sit_boner:
        xoffset -250
    show erik b_sidebed f_woozy o_boner:
        flip
        xoffset 550
    show iwanka b_sidebed_right_shy f_suspicious
    with fade
    iwanka "Benda biru apa itu?"

    erik "Sperma."

    iwanka f_surprised "Sial, itu banyak sekali spermanya!"

    pause
    iwanka f_annoyed "Dia tidak bisa menelan semua itu!"

    show anon f_shy
    erik "Tidak, tapi dia pasti mencoba..."

    pause

    scene location_erik_basement_back_hentai_sex
    show iwanka_sex_hentai_cum
    with fade
    iwanka "Ini umm... sedikit intens."

    iwanka "Dia seperti boneka tak berdaya bagi makhluk ini..."

    erik "Ya, cukup banyak."

    pause
    iwanka "... Agak panas."

    pause

    scene location_erik_basement_back_couch
    show anon b_sit f_shy o_sit_boner:
        xoffset -250
    show erik b_sidebed f_woozy o_boner:
        flip
        xoffset 550
    show iwanka b_sidebed_right_shy f_smirk
    with fade
    pause
    show iwanka b_sidebed_left_shy with dissolve
    pause .4
    show iwanka f_smirk_down
    show anon of_blush
    with dissolve
    pause
    show iwanka b_sidebed_right_shy f_lipbite with dissolve
    pause
    show iwanka f_drunk a_rub with dissolve
    pause

    scene location_erik_basement_back_hentai_sex
    show iwanka_sex_hentai_cum
    with fade
    iwanka "Ya ampun!"

    iwanka "Lihat semua air mani yang dipompa ke dalam vaginanya..."

    iwanka "... Itu keluar dari dirinya!"

    pause

    scene location_erik_basement_back_couch
    show anon b_sit f_shy o_sit_boner:
        xoffset -250
    show erik b_sidebed f_woozy o_boner:
        flip
        xoffset 550
    show iwanka a_rub b_sidebed_right_shy f_drunk
    with fade
    iwanka @ f_content_closed -m_talk "MM."

    anon f_surprised_low "!!!"
    anon @ -m_talk "(Apakah dia... Sedang melakukan masturbasi?)"

    show anon f_flirt_low
    pause
    iwanka "Berapa banyak tentakel yang bisa muat di sana?!"

    erik "Oh, ini bukan apa-apa."

    erik "Tunggu saja sampai Anda melihat adegan threesome dengan cumi-cumi..."

    iwanka "Nghh, kurasa aku tidak akan bertahan selama itu!"

    pause

    python:
        renpy.end_replay()
        unlock_scene('iwanka', '03_unlocked')

    show iwanka a_touch b_sidebed_left_shy
    show anon f_surprised_down o_empty
    with dissolve
    anon "!!!"
    anon @ f_surprised "A-wah, apa yang kamu lakukan?!"

    show erik b_sidebed f_worried with dissolve:
        unflip
        xoffset 0
    iwanka "Bukankah sudah jelas?"

    show anon o_sit_boner
    show erik f_surprised
    show iwanka b_kneeling a_idle:
        xoffset -146
    with dissolve
    iwanka "Ini membuatku terangsang sekali, {b}[firstname]{/b}!"

    erik @ f_surprised_down "Sialan, kawan!"

    iwanka "Bisakah saya melihatnya?"

    anon "Oh, entahlah..."

    iwanka "Mmm, tolong?"

    anon "{b}Erik{/b} sedang duduk di sana!"

    iwanka "Dia tidak akan keberatan..."

    iwanka "Anda tidak akan keberatan, bukan, bintik-bintik?"

    show anon f_surprised
    show erik a_thumbs f_laugh with dissolve
    pause
    show erik f_woozy a_idle with dissolve
    iwanka "Melihat."

    show anon b_sit_back f_flirt_low
    show iwanka a_undress1
    with dissolve
    anon "Ini meningkat dengan sangat cepat..."

    show anon b_sit_back_shirt o_empty od_empty
    show iwanka a_undress2
    with dissolve
    iwanka "hehe!"

    show iwanka a_undress3 with dissolve
    show iwanka a_undress4 with dissolve
    anon "Ya ampun..."

    erik @ f_laugh "Terhebat... Pesta... PERNAH!"

    erik a_phone "Ini yang terjadi di papan pesan guildku!"


    call scene_iwanka_blowjob
    $ unlock_scene('iwanka', '01_unlocked', variant='basement')

    scene location_erik_basement_back_couch
    show anon b_sit f_shy:
        xoffset -250
    show iwanka b_sidebed_left f_drunk o_cum
    show erik b_sidebed f_woozy
    with fade
    iwanka "Itu menyenangkan!"

    anon "Y-ya, benar."

    show iwanka b_sidebed_right with dissolve
    iwanka "Bisakah saya mendapatkan handuk atau sesuatu?"

    erik @ -m_talk "Hmm?"

    erik "Tentu saja!"

    hide erik with dissolve
    pause
    show iwanka b_sidebed_left with dissolve
    iwanka "Sekarang aku sudah menjagamu, mungkin kamu bisa membalas budi?"

    anon f_flirt "Uhh, ya... Kurasa aku bisa."

    iwanka "Bagus sekali."

    show iwanka b_sidebed_left_shy with dissolve
    iwanka "Berhati-hatilah karena dengan semua kegembiraan ini, di bawah sana seperti badai tropis!"

    "{i}*Selamat datang*{/i}"

    anon @ f_confused "Apa itu?"

    "{i}*Selamat datang*{/i}"

    iwanka f_annoyed "Ugh, itu ponselku yang bodoh..."

    show iwanka b_sidebed_left with dissolve
    iwanka "... Tunggu."

    iwanka a_phone f_suspicious_down "Aww, kawan... Ini ayahku."

    show anon f_worried
    iwanka a_phone_talk f_annoyed "Halo?"

    pause
    iwanka "Saya di rumah teman."

    pause
    iwanka "Umm, karena kamu sibuk mendisiplinkan pelayan?"

    pause
    iwanka "{b}Ayah{/b}, umurku dua puluh tujuh..."

    pause
    iwanka "Jadi aku bisa menjaga diriku sendiri!"

    pause
    iwanka "Ya, sekedar informasi, teman saya laki-laki."

    pause
    iwanka "Tidak, kami tidak berhubungan seks!"

    iwanka @ f_eyeroll "Yesus!"

    show iwanka f_drunk
    pause
    iwanka f_annoyed "Aku akan pulang sebentar lagi."

    pause
    iwanka "Tidak bisakah menunggu?"

    pause
    iwanka "Grr, aku benar-benar muak dengan ini!"

    pause
    iwanka "Halo?"

    iwanka a_phone @ f_suspicious_down "Brengsek!"

    anon "Apa yang terjadi?"

    iwanka f_sad "{i}*Huh*{/i} Aku harus pergi..."

    anon "Apa sekarang?"

    iwanka "Ya."

    iwanka "Ayah saya mengirim mobil untuk menjemput saya."

    anon "Hah?"

    anon "Bagaimana mereka tahu di mana Anda berada?"

    iwanka "Mereka melacak telepon saya."

    pause
    anon "Baiklah, bolehkah aku bertemu denganmu lagi?"

    iwanka f_surprised "Anda serius tentang hal itu?"

    anon "Hmm, ya?"

    iwanka f_drunk "Hah."

    anon "Tadinya kau akan memberitahuku cara menyelinap ke rumah ayahmu agar kita bisa jalan-jalan, ingat?"

    iwanka "Heh, kamu tidak perlu menyelinap masuk..."

    anon @ f_confused "saya tidak?"

    iwanka "Tidak."

    iwanka "Katakan saja pada penjaga di gerbang depan bahwa kamu ada janji dengan saya..."

    iwanka "... Dan ketika dia menanyakan tujuannya apa, katakan padanya untuk wawancara sebagai asisten baruku."

    anon "Asistenmu, serius?"

    iwanka "Apakah kamu ingin datang menemuiku atau tidak?"

    anon f_shy "Tentu saja."

    iwanka "Nah, itulah satu-satunya cara Anda masuk ke dalam."

    iwanka "Bertingkahlah percaya diri dan Anda akan baik-baik saja."

    anon "O-oke."

    iwanka a_idle f_eyeroll "Ugh, semuanya menjadi menyenangkan juga."

    hide iwanka with dissolve
    pause
    erik "Ini derekmu-"

    erik "T-tunggu, kamu mau kemana?"

    iwanka "Ayahku mengirim mobil untuk menjemputku."

    erik "Oh."

    iwanka "Terima kasih untuk pestanya."

    erik "Y-ya, tidak masalah."

    erik "Tahan!"

    iwanka "Hmm?"

    erik "Anda mungkin ingin menghapus wajah Anda."

    show anon f_laugh
    iwanka "Oh benar."

    show anon f_shy
    pause
    iwanka "Terima kasih."

    pause
    show erik b_sidebed f_woozy with dissolve
    pause
    erik "Jadi..."

    erik "... Apakah itu luar biasa atau apa?!"

    anon f_normal @ f_flirt "Ya, memang begitu."

    erik "Sayang sekali Anda tidak mendapatkan info yang Anda inginkan, tetapi pekerjaan pukulan dari {b}Iwanka Rump{/b} adalah hadiah hiburan yang cukup bagus!"

    anon @ f_laugh "Sebenarnya, dia memberiku jalan masuk ke dalam kawasan walikota sebelum dia pergi."

    erik f_normal "Ah, benarkah?"

    anon "Ya."

    erik "Kacang keren, kawan!"

    erik "Saya kira malam ini sukses besar, ya?"

    anon "Anehnya, ya."

    erik "Bagus."

    pause
    erik a_phone @ f_laugh "Jadi, bolehkah saya mengupload video ini sekarang?"

    anon "Hehe, ya, silakan."

    erik "Luar biasa!"

    hide erik with dissolve
    erik "Ini benar-benar akan memaksimalkan status popularitasku di guildku!"

    show anon f_laugh
    pause
    anon f_normal @ -m_talk "(Saya benar-benar mengira malam ini akan menjadi bencana...)"

    anon @ f_flirt -m_talk "(... Tapi semuanya berhasil pada akhirnya.)"

    anon @ f_laugh -m_talk "( Sekarang, langkah selanjutnya adalah {b}menyusup ke rumah Walikota Rump{/b}! )"

    anon @ -m_talk "(Saya harus {b}berbicara dengan keamanannya{/b} besok dan melihat apakah info {b}Iwanka{/b} bagus. )"

    hide anon with dissolve

    scene black with slowdissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
