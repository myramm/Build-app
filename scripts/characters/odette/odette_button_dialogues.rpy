label button_odette_sex_proposal:
    scene expression player.location.background_closeup with None
    show anon
    show odette
    with dissolve
    anon @ a_wave "Pagi, {b}Odette{/b}."

    odette "Hai, teman besar!"

    odette "Anda datang lebih awal."

    anon "Ya."

    anon "Apakah {b}Hawa{/b} ada di rumah?"

    odette "Saya tidak yakin."

    anon "Bolehkah saya naik dan memeriksanya?"

    odette "Tentu..."

    show odette:
        xoffset -260
    with dissolve
    odette f_smirk "... Tapi sebelum Anda melakukan itu."

    odette "Saya tidak pernah mengucapkan terima kasih yang pantas atas bantuan Anda dengan {b}Grace{/b}."

    anon "Oh, tidak perlu."

    anon "Saya senang semuanya berhasil."

    pause
    anon @ f_skeptical "Semuanya berjalan baik, bukan?"

    odette "Oh ya!"

    odette "{b}Grace{/b} dan saya benar-benar telah mencapai titik balik dalam hubungan kami."

    odette "Segalanya kini lebih baik daripada sebelumnya!"

    anon "Yah, aku senang mendengarnya."

    odette "Kami hampir seperti pasangan."

    anon "Luar biasa sekali, {b}Odette{/b}."

    odette "Dan seksnya, fiuh... Kamu seharusnya mendengar suara-suara yang dibuat gadis itu saat aku menjatuhkannya!"

    anon @ f_surprised "!!!"
    odette "Dia mencicit dan merintih, sungguh menggemaskan!"

    anon f_shy "..."
    odette "{b}Eve{/b} akhir-akhir ini juga hanya tersenyum."

    odette "Anda pasti memberinya nilai D yang bagus, ya?"

    anon "Ehh."

    odette "Ayo, kawan... Beri aku beberapa deet!"

    anon "Hehe, menurutku itu bukan ide yang bagus..."

    odette f_confused "Oh?"

    pause
    odette f_smirk "Mungkin Anda benar."

    odette "Demonstrasi akan jauh lebih mencerahkan."

    show odette b_drop1 with dissolve
    pause
    show odette b_drop2 with dissolve
    show odette b_topless with dissolve
    show anon f_surprised_down o_boner with dissolve
    anon "!!!"
    show odette a_grope with dissolve
    odette @ f_laugh "Hehehe!"

    anon f_worried "Apa yang kamu-"

    odette @ -m_talk "Hmm?"

    anon @ a_behind_head "K-kita tidak bisa-"

    odette "Kenapa tidak?"

    odette "Kau tahu, ada tiga wanita terangsang di rumah ini... Tidak adil bagi {b}Eve{/b} menyimpan penis besar ini sendirian!"

    anon "Bagaimana dengan {b}Rahmat{/b}?"

    odette "Jangan khawatir tentang {b}Grace{/b}."

    odette "Dia tidak akan terganggu dengan kesenangan kecil yang tidak berbahaya."

    anon "Entahlah, {b}Odette{/b}..."

    anon "{b}Eve{/b} dan saya melakukannya dengan sangat baik saat ini-"

    odette "Dia juga tidak akan keberatan, aku janji."

    pause
    odette "Dia bahkan mungkin dibujuk untuk bergabung dengan kami."

    anon a_surprised "Ngh, ini terasa sangat enak."

    odette "Hehe, aku akan membuatmu merasa lebih baik..."

    odette "Apa yang kamu katakan?"

    return

label button_odette_sex_proposal_okay:
    anon f_flirt "Oke."

    odette "Mm, itu yang ingin saya dengar!"

    hide odette
    show odette b_topless f_thinking
    with dissolve
    call odette_1st_sex_bike
    return

label button_odette_sex_proposal_no:
    anon f_sad_down "Saya tidak bisa melakukan itu pada {b}Eve{/b}..."

    odette f_tired a_idle "Cih, itu mengecewakan."

    anon f_tired "Maaf."

    odette "Tidak, tidak apa-apa."

    odette "Saya senang {b}Evie{/b} mendapati dirinya sebagai pria yang begitu berbakti."

    pause
    odette f_pouting "{i}*Sigh*{/i} Tapi kita semua bisa mendapatkan lebih banyak lagi..."

    anon @ -m_talk "..."
    odette "Oh baiklah."

    odette "Anda tahu di mana menemukan saya, jika Anda sadar."

    anon f_worried "Y-ya, terima kasih atas tawarannya."

    odette @ -m_talk "Mmhmm."

    hide anon with dissolve
    return

label button_odette_wanna_fool_around_first_time:
    show anon f_flirt
    odette f_smirk "Oh, berubah pikiran?"

    anon "Y-ya."

    odette "Bagus!"

    odette "Aku tahu kamu akan datang."

    if player.location != L_tattooparlor_garage:
        odette "Biar aku membuang tanda pergi di pintu dan menguncinya, aku akan menemuimu di garasi."

        anon "Oke."

        $ player.go_to(L_tattooparlor_garage)
        scene expression player.location.background_blur with fade
        show anon
        show odette
        with dissolve
    return

label button_odette_refuse_sex:
    anon f_normal "Tidak, terima kasih."

    odette f_smirk "Cih, sayang sekali kalau penis sebesar itu disia-siakan..."

    odette "{b}Evie{/b} dan {b}Grace{/b} tidak keberatan kalau kita bersenang-senang sedikit, tahu?"

    odette "Saya berjanji."

    anon f_thinking a_thinking @ -m_talk "..."
    pause
    odette @ f_pouting "{i}*Huh*{/i} Sesuaikan dirimu."

    show anon f_normal a_idle with dissolve
    return

label button_odette_accept_sex:
    anon f_happy @ a_point "Ya!"

    odette "Hmm, sekarang kita bicara!"

    odette "Bagaimana kamu menginginkanku?"

    return

label button_odette_you_and_grace:
    anon "Bagaimana kabarmu dan {b}Grace{/b}?"

    odette "Ya Tuhan, ini luar biasa!"

    odette "Anda tidak tahu betapa senangnya akhirnya bisa bersamanya setelah bertahun-tahun!"

    odette f_smirk "Pertama kali dia menyerangku, aku datang dalam waktu sepuluh detik..."

    anon f_surprised "!!!"
    odette "... Dan dia sangat menggemaskan saat dia orgasme!"

    anon @ f_confused "{i}*Meneguk*{/i} O-oh?"

    odette "Mungkin aku akan menunjukkannya padamu suatu saat nanti..."

    anon f_shock "Hah?!"

    odette @ f_laugh "Hehehe!"

    show anon f_surprised
    return

label button_odette_i_should_go:
    anon f_normal "Saya harus pergi."

    odette "Ah, begitu cepat?"

    anon "Ya, sampai jumpa {b}Odette{/b}."

    odette "Kembalilah jika Anda berubah pikiran."

    hide anon with dissolve
    return

label button_odette_wanna_fool_around:
    anon f_shy "Ingin bermain-main?"

    odette f_smirk "Apa, di toko ini?"

    anon f_worried_surprised "T-tidak, pikirku di garasi... Mungkin memasang tanda di pintu atau semacamnya?"

    odette f_pouting "Oh, tapi itu tidak terlalu menarik..."

    anon f_confused @ -m_talk "Hmm?"

    show odette a_sides:
        xoffset -140
    with {'master': dissolve}
    odette "... Ayolah, saat ini tidak ada siapa pun di sini dan {b}Grace{/b} sedang sibuk di lantai atas."


    menu:
        "Apa kamu yakin?":
            jump button_odette_wanna_fool_around.blowjob
        "Mustahil!":

            pass

    anon f_unimpressed "Mustahil."

    pause
    show odette a_shrug f_eyeroll
    with {'master': dissolve}
    odette "Bagus."

    show odette a_sides f_normal
    with {'master': dissolve}
    odette "Biar aku membuang tanda pergi di pintu dan menguncinya, aku akan menemuimu di garasi."

    show anon f_shy:
        xoffset -500
        xzoom -1
    hide odette
    with {'master': dissolve}
    anon "Baiklah."

    hide anon with dissolve

    scene expression background(l=L_tattooparlor_garage) as stage
    show anon at flip
    with fade
    show odette f_smirk at flip
    with {'master': dissolve}
    odette "Mmm, kamu punya penis yang terbaik {b}[firstname]{/b}..."

    anon @ a_behind_head "Hehe, terima kasih."

    odette "Bagaimana kamu menginginkanku?"

    return True

label button_odette_wanna_fool_around.blowjob:
    anon "Apakah kamu-"

    show anon a_sides f_surprised behind odette
    show odette f_tired_happy:
        xoffset -250
    with {'master': dissolve}
    anon @ -m_talk "Uhh..."

    show anon a_surprised_up f_surprised
    show odette a_excited
    with {'master': dissolve}
    odette "Ayo nakal!"

    show anon a_surprised
    show odette f_tired_happy_lipbite
    with {'master': dissolve}
    anon "A-apa yang ada dalam pikiranmu?"

    show odette f_tired_happy
    with {'master': dissolve}
    odette "Hehe, akan kutunjukkan padamu..."

    show anon a_empty b_empty f_surprised_teeth:
        xoffset 150
    show odette b_dressed_pull_anon behind anon:
        xoffset 186
        xzoom -1
    with {'master': dissolve}
    odette "...Ikuti aku kawan."

    hide anon
    hide odette
    with {'master': dissolve}
    pause

    call scene_odette_blowjob.repeat
    $ unlock_scene('Odette', '04_unlocked', variant='shop')

    scene expression player.location.background_closeup
    show odette a_wipe
    show anon a_sides f_flirt_grin
    with fade
    odette @ -m_talk "MM."

    show odette a_hips f_smirk
    with {'master': dissolve}
    odette "Ya, itu menyenangkan."

    anon @ f_flirt "Fiuh, ya benar!"

    odette "Terima kasih sudah mampir sobat besar..."

    show odette a_kiss f_moo
    with {'master': dissolve}
    odette @ -m_talk "Muah!"

    show odette a_sides f_smirk
    with {'master': dissolve}
    odette "... Aku harus mulai menutup diri."

    anon @ f_flirt "Y-ya, oke."

    show anon a_wave
    hide odette
    with {'master': dissolve}
    anon @ f_flirt "Sampai jumpa, {b}Odette{/b}."

    show anon a_sides
    with {'master': dissolve}
    pause
    anon f_grin @ -m_talk "(Wah!)"

    hide anon with dissolve
    return

label button_odette_intro_garage_e21:
    scene expression player.location.background_closeup with None
    show odette
    show anon
    with dissolve
    anon "Selamat pagi, {b}Odette{/b}."

    odette "Hai, teman besar."

    odette f_smirk "Ingin pergi jalan-jalan?"

    return

label button_odette_intro_interior_e21:
    scene expression player.location.background_closeup with None
    show odette
    show anon
    with dissolve
    anon @ a_wave "Hai, {b}Odette{/b}."

    odette "Hai, teman besar."

    return

label button_odette_eve_make_up_grace_upset:
    scene expression player.location.background_closeup with None
    show odette f_sad a_cover_face:
        xoffset 100
    show anon f_worried
    with dissolve
    anon "{b}Odette{/b}?"

    odette a_cheeks @ -m_talk "Hmm?"

    odette a_sides "Oh, hai {b}[firstname]{/b}."

    anon "Apakah kamu baik-baik saja?"

    odette "Y-ya, aku baik-baik saja."

    anon "{b}Grace{/b} masih kesal padamu ya?"

    odette "Ya."

    odette "Dia hampir tidak mengucapkan tiga patah kata pun kepadaku sejak pesta itu."

    odette "Itu bukan salahku Teman bodoh {b}Tuuku{/b} membawa narkoba."

    odette "Jika aku tahu, aku sendiri yang akan mengusirnya!"

    anon "{b}Odette{/b}, dia sejak awal menentang pesta itu..."

    odette "{i}*Huh*{/i} Ya, saya tahu."

    pause
    odette "Aku hanya tidak yakin apa yang dia inginkan dariku."

    odette "Semua orang tahu aku hanya pandai dalam dua hal, berpesta dan bercinta."

    odette "Saat ini, sepertinya dia tidak tertarik pada keduanya."

    anon f_normal "Oh ayolah... Pasti kamu punya bakat lain selain itu."

    odette "Saya rasa tidak, {b}[firstname]{/b}."

    show anon f_worried
    pause
    odette a_cover_face "Ugh, ini jadi berantakan."

    anon @ -m_talk "..."
    eve "{b}[firstname]{/b}?"

    show odette a_head with dissolve
    show eve:
        xoffset -300
    with dissolve
    show anon f_normal
    eve "Hai."

    show odette a_sides with dissolve
    eve f_happy "Apa yang kamu lakukan di sini?"

    anon "Hei kamu."

    hide anon
    show eve b_dressed_kiss1
    with dissolve
    pause
    show anon
    show eve b_dressed
    with dissolve
    anon "Saya datang untuk menemui Anda dan saya bertemu dengan {b}Odette{/b}."

    anon f_worried "Kami sedang membicarakan situasinya dengan adikmu."

    eve f_normal "Oh, begitu."

    eve "Ya, keadaan di sini pasti menjadi sedikit tegang sejak pesta..."

    show eve f_normal_right
    pause
    eve f_confused_right "Yesus, apakah kamu menangis?"

    odette "T-tidak."

    eve f_normal_right "Ya, benar!"

    odette f_angry a_idle "Diam!"

    eve "Sialan."

    eve "Kurasa aku belum pernah melihatmu menjadi emosional tentang apa pun sebelumnya..."

    odette "Saya baik-baik saja!"

    anon "Saya pikir kita harus membantunya."

    show odette f_sad
    eve f_normal "Ya?"

    anon "Ayo, lihat dia."

    show eve:
        flip
        xoffset 300
    with dissolve
    eve "..."
    eve @ f_eyeroll "{i}*Huh*{/i} Entahlah..."

    eve "Apakah kamu benar-benar mencintai adikku?"

    odette "Apa?"

    odette @ f_eyeroll "Tentu saja aku tahu, dia adalah sahabatku!"

    eve "Tidak, Anda tahu apa yang saya tanyakan, {b}Odette{/b}."

    eve "Kalau ini hanya soal membuat dia kesal, aku keluar."

    eve "Tetapi jika Anda benar-benar mencintainya, kami akan membantu Anda."

    odette f_surprised a_sides "saya-"

    odette f_sad @ f_sad_back "Uhh, maksudku-"

    eve "Itu pertanyaan ya atau tidak, {b}Odette{/b}."

    odette f_disgusted "Ya."

    eve @ -m_talk "Hmm?"

    odette f_shy "Saya bersedia."

    odette f_normal "Aku mencintai adikmu."

    anon "Aduh!"

    odette f_sad "Tapi percayalah, dia tidak tertarik."

    eve "Itu karena menurutnya Anda bertingkah dan tidak dewasa."

    odette @ f_eyeroll "Wow, jangan melapisinya dengan gula atau apa pun..."

    eve f_happy @ f_laugh "Haha, aku serius!"

    eve "Pikirkan tentang hal ini."

    eve "Anda tidak pernah mempunyai pekerjaan, pada dasarnya Anda tinggal di sini tanpa membayar sewa, Anda makan makanan kami, menggunakan kamar mandi kami-"

    odette f_normal @ f_angry "Oke, oke, saya mengerti!"

    odette "Apa yang Anda usulkan agar saya lakukan?"

    eve "Nah, Anda bisa mulai dengan membantu di sini."

    odette @ f_eyeroll "Cih, setiap kali aku bertanya apakah aku bisa membantu, dia bilang tidak!"

    anon "Itu masalahnya, di sana."

    odette f_confused @ -m_talk "Hmm?"

    show eve f_normal_right
    anon "Jangan tanya dia, lakukan saja."

    anon "Jika dia mengeluh, katakan, \"Saya membantu, suka atau tidak suka.\""

    eve f_normal "Dia benar."

    eve "{b}Grace{/b} menghabiskan seluruh waktunya menjaga kami."

    eve "Yang dia butuhkan adalah seseorang yang menjaganya."

    odette @ -m_talk "..."
    eve "Jadi, jika Anda benar-benar mencintainya, majulah dan lakukanlah."

    odette f_thinking @ -m_talk "Hmm."

    odette f_normal "Saya kira saya bisa melakukan itu."

    anon "Mungkin dimulai dengan permintaan maaf."

    eve "Ya, dan mungkin makan malam."

    odette f_thinking @ f_surprised "Baiklah, baiklah, pelan-pelan saja!"

    pause
    odette f_normal "Sepertinya aku punya ide tapi aku harus menemui {b}Ayah{/b}..."

    eve f_disgusted "Eugh, berhenti memanggilnya seperti itu!"

    odette "Jika aku memberi kalian sejumlah uang, bisakah kalian menyiapkan makan malam?"

    show eve f_normal
    menu:
        "Tentu.":
            anon f_normal "Kami bisa mengatasinya."

            odette "Bagus."

            show odette a_money zorder 1 with dissolve
            odette "Di Sini."

            show odette a_idle
            show anon a_money
            with dissolve
            pause
            odette "Dapatkan favorit {b}Grace{/b}, oke?"

            show anon a_idle with dissolve
            odette "Saya akan kembali untuk makan malam."

            eve "Oke."

            $ player.get_money(200)
        "Anda tidak perlu memberi kami uang.":

            anon f_normal @ a_wave "Saya bisa mengatasinya."

            odette f_smirk @ f_confused "Benar-benar?"

            odette "Aku tidak sadar kamu begitu memerah, {b}[firstname]{/b}."

            eve f_happy_right "Itu laki-laki saya!"

            show eve b_dressed_kiss1:
                unflip
                xoffset -300
            hide anon
            with dissolve
            anon "!!!"
            show eve b_dressed
            show anon
            with dissolve
            odette @ f_laugh "hehe."

            odette "Pastikan saja kamu mendapatkan favorit {b}Grace{/b}, oke?"

            eve "Oke."

            odette "Terima kasih!"

            odette "Saya akan kembali untuk makan malam."

            $ M_eve.dating.increment(5)

    hide odette with dissolve
    anon f_snarky "Saya kira kita memiliki banyak pekerjaan yang harus dilakukan."

    show eve f_happy:
        unflip
        xoffset -300
    eve "Sepertinya begitu."

    anon f_thinking "Apa sih favorit {b}Grace{/b}?"

    eve "Lasagna."

    anon f_worried "Oh, bisakah kamu membuatnya?"

    eve @ f_laugh "Heh, tidak!"

    eve "Saya hampir tidak bisa merebus air."

    anon f_sad_down a_behind_head @ -m_talk "..."
    eve "Hehe, jangan khawatir!"

    eve "Kita bisa mendapatkannya di {b}Tony's Pizza{/b}."

    anon f_normal a_idle @ f_skeptical "Oke."

    eve "Kita mungkin harus membeli lilin dan anggur juga."

    eve "Buatlah menjadi romantis, lho?"

    anon "Selesai."

    anon "Kita harus mendapatkan {b}Grace{/b} sesuatu yang bagus juga."

    anon @ a_thinking f_thinking "Bunga, mungkin?"

    eve "Ya, dia akan menyukainya!"

    eve @ f_surprised "Oh, kita bisa membelikannya coklat!"

    eve "Dia baru saja mengatakan beberapa hari yang lalu bahwa dia menginginkan coklat."

    anon f_flirt "Cokelat, kalau begitu."

    hide anon
    show eve b_dressed_kiss:
        xoffset -400
    with dissolve
    anon "!!!"
    pause
    show anon
    show eve b_dressed:
        xoffset 0
    with dissolve
    eve "Ini akan sangat menyenangkan!"

    eve "Ayo {b}pergi ke mal{/b} dan memulai."

    anon "Tepat di belakangmu."

    hide anon
    hide eve
    with dissolve
    return

label button_odette_progress_with_eve_no_way:
    anon f_skeptical "Saya tidak akan mencoba membujuknya melakukan sesuatu yang tidak diinginkannya."

    odette @ f_eyeroll "Siapa bilang dia tidak menginginkannya?"

    anon @ -m_talk "..."
    odette @ f_angry "Baiklah, jadilah seperti itu."

    show anon f_normal
    return

label button_odette_progress_with_eve_think_about_it:
    anon f_flirt "Saya akan memikirkannya."

    odette f_smirk "Hmm, kamu melakukan itu."

    odette "Bayangkan tubuh kami yang panas dan berkeringat bergesekan satu sama lain saat Anda bepergian bersama kami..."

    anon f_flirt_grin @ -m_talk "!!!"
    odette "Saya tahu saya akan melakukannya."

    odette @ f_laugh "Hehehe!"

    show anon f_normal
    return

label button_odette_progress_with_eve:
    odette f_smirk "Jadi, bagaimana kabarmu dan {b}Evie{/b}?"

    anon @ -m_talk "Hmm?"

    if M_eve.biggus_dickus:
        odette "Apakah kamu sudah mencoba gadis itu?"

    else:
        odette "Apakah kamu sudah mencoba memek itu?"

    anon f_surprised "!!!"
    anon f_worried "Umm, itu bukan hal yang nyaman untuk kubicarakan, {b}Odette{/b}..."

    odette f_confused "Kenapa tidak?"

    odette "Tidak ada yang perlu dipermalukan."

    anon f_sad_down "..."
    odette f_smirk "Saya tahu Anda menginginkannya."

    anon f_skeptical "Apa yang membuatmu mengatakan itu?"

    odette "Yah, kamu pasti bodoh jika tidak..."

    odette "{b}Eve{/b} seperti, gadis yang sempurna!"

    anon f_surprised "Menurutmu dia seksi?"

    odette @ f_eyeroll "Duh!"

    if M_eve.biggus_dickus:
        odette "Payudara yang lucu dan gagah serta ayam yang berdenyut-denyut?"

        odette @ f_laugh "Itu yang terbaik dari kedua dunia!"

        anon f_snarky @ -m_talk "..."
        odette "Aku yakin dia mengeluarkan suara yang paling menggemaskan saat kamu menempelkannya di pantatnya..."

        anon f_shock @ -m_talk "..."
        odette "Apakah Anda sudah mencicipinya?"

    else:
        odette "Tipe imut, pemalu, dan tidak berpengalaman itu selalu membuatku seksi."

        pause
        odette "Aku yakin dia mengeluarkan suara paling menggemaskan saat dia orgasme..."

        anon f_surprised_teeth @ -m_talk "..."
        odette "Apakah Anda sudah mencicipinya di selatan perbatasan?"

    anon f_unimpressed @ -m_talk "..."
    odette "Oh ayolah, beri aku sesuatu?!"

    anon "Seorang pria sejati tidak membicarakan hal-hal seperti itu."

    odette @ f_eyeroll "Ugh, tuan-tuan membosankan."

    anon "Jika Anda begitu tertarik, kenapa Anda tidak mencoba dan bergaul dengannya?"

    odette "Oh percayalah, saya sudah mencobanya."

    show anon f_surprised
    odette "Dia hanya menaruh perhatian padamu, kawan."

    pause
    odette f_confused "Anda tahu, Anda bisa mengatakan kepadanya bahwa akan sangat menyenangkan melihatnya bersama gadis lain..."

    odette "Jika kita bekerja sama, siapa yang tahu apa yang bisa kita capai?"

    return

label button_odette_big_fella:
    anon f_worried "Kenapa kamu terus memanggilku seperti itu?"

    odette "Oh ayolah, kamu tahu kenapa..."

    anon f_confused "Tidak juga."

    odette "{b}Tuuku{/b} bilang padaku kamu, {i}*Ahem*{/i}, \"berbakat...\""

    anon f_worried @ -m_talk "..."
    odette @ a_point "... Di bawah garis khatulistiwa."

    show anon f_looking_down
    pause
    anon f_surprised "!!!"
    anon f_shy "O-oh."

    odette @ f_laugh "Ha ha ha!"

    odette "{b}Evie{/b} tidak akan membocorkan apakah itu benar atau tidak."

    anon @ -m_talk "..."
    odette "Jika ya, saya mungkin harus bertanya padanya apakah dia mengizinkan saya memainkannya sesekali."

    anon f_worried @ a_behind_head "Ehehe..."

    return

label button_odette_are_you_alright_2:
    anon f_worried "Apakah kamu baik-baik saja?"

    odette "Ya, aku baik-baik saja."

    odette "Sungguh, sungguh, BENAR-BENAR mabuk..."

    pause
    odette f_tired_happy "Kamu mau ikut tidur siang denganku?"

    anon f_surprised_teeth "!!!"
    anon f_worried "Uhh, menurutku itu bukan ide yang bagus..."

    odette f_smirk a_idle "Aduh, ayolah... Aku akan membiarkanmu menjadi sendok kecilnya?"

    anon f_normal "Hehe, tidak."

    odette @ f_pouting "Aww, kamu tidak menyenangkan."

    return

label button_odette_grace_and_tuuku:
    anon "Jadi sudah berapa lama Anda mengenal {b}Grace{/b}?"

    odette "Dia dan aku telah berteman baik sejak taman kanak-kanak."

    anon "Benar-benar?"

    odette "Yup, dia menukar pisangnya dengan cangkir pudingku dan itu saja."

    odette @ f_laugh "Sahabat seumur hidup!"

    anon "Hehe, itu lucu!"

    pause
    anon f_worried "Bagaimana dengan {b}Tuuku{/b}?"

    odette @ -m_talk "Hmm?"

    odette @ f_eyeroll a_mock "Oh, {b}Grace{/b} naksir {b}Tuuku{/b} saat SMP, dan mereka mulai berkencan."

    anon f_surprised "Mereka berkencan?"

    odette "Ya, selama seminggu."

    odette "Kemudian dia menyadari betapa pecundangnya dia."

    anon f_confused "Pecundang?"

    odette "Hehe, aku bercanda."

    show anon a_thinking with dissolve
    pause
    odette "Ya, sebagian besar..."

    odette "Bagaimanapun, dia telah mengikuti {b}Grace{/b} dan saya sejak saat itu."

    odette "Dia seperti anak anjing kecil kami."

    anon f_worried a_idle "Anak anjing?"

    odette @ f_laugh "Ditambah lagi dia menanam rumput liar yang LUAR BIASA!"

    odette "Ini seperti bom, sungguh!"

    anon "Jadi begitu."

    return

label button_odette_what_are_you_reading:
    anon "Apa yang kamu baca?"

    odette @ a_shrug "Oh, hanya katalog pakaian dalam yang jelek."

    anon "L-pakaian dalam?"

    odette f_smirk "Ya, seorang gadis tidak akan pernah punya cukup pakaian dalam... Setuju kan?"

    anon f_worried @ a_behind_head "{i}*Gulp*{/i} Ya, tentu saja."

    odette @ f_laugh "Ha ha ha!"

    return

label button_odette_nevermind_generic:
    anon "Sampai jumpa."

    odette "Saya akan berada di sini."

    hide anon with dissolve
    return

label button_odette_nevermind_morning:
    odette f_confused "Apakah {b}Grace{/b} ada di toko?"

    anon "Ya, menurutku begitu."

    odette f_tired @ f_yawn a_stretch "{i}*Menguap*{/i} Oke, bagus."

    anon "Aku mungkin harus membiarkanmu kembali tidur, ya?"

    odette f_tired_happy "Entah itu atau masakkan aku sarapan?"

    anon "Ehh, mimpi indah {b}Odette{/b}."

    odette @ f_laugh "Haha!"

    hide anon with dissolve
    return

label button_odette_have_you_seen_eve:
    anon "Pernahkah Anda melihat {b}Hawa{/b}?"

    odette "Um, bukan?"

    odette @ a_point "Saya lagi tidur."

    anon @ a_behind_head "Benar."

    odette "Jika dia tidak {b}di sekolah{/b} maka dia mungkin masih {b}di tempat tidur{/b}."

    anon "Ah, oke."

    odette "Anda dapat {b}naik ke atas{/b} dan membangunkannya jika Anda benar-benar menginginkannya."

    anon "Terima kasih."

    odette @ -m_talk "Mmhmm."

    return

label button_odette_are_you_alright_1:
    anon f_worried "Apakah kamu baik-baik saja?"

    odette "Ya, aku baik-baik saja."

    odette "Sungguh, sungguh, BENAR-BENAR mabuk..."

    pause
    odette f_confused "... Dan sepertinya celana dalamku hilang."

    anon f_surprised @ f_shock "!!!"
    anon "K-celana dalammu?"

    odette f_smirk @ a_shrug "Jangan khawatir, mereka akan muncul di suatu tempat."

    anon f_worried "Apakah ini sering terjadi?"

    odette f_thinking "Mmm, hanya setiap kali aku minum..."

    odette f_tired @ f_laugh "Ha ha ha!"

    return

label button_odette_intro_garage_e15e20:
    scene expression player.location.background_closeup with None
    show odette f_tired a_cheeks
    show anon
    with dissolve
    anon "Selamat pagi, {b}Odette{/b}."

    odette @ -m_talk "Hmm?"

    odette "Oh, hai teman besar."

    odette a_sides @ a_stretch f_yawn "{i}*Menguap*{/i}"

    odette "Apa yang kamu lakukan di sini sepagi ini?"

    return

label button_odette_intro_garage_e6e14:
    scene expression player.location.background_closeup with None
    show odette a_head f_tired
    show anon
    with dissolve
    anon @ a_wave "Selamat pagi, {b}Odette{/b}."

    odette "Eh, {b}[firstname]{/b}?"

    odette "Jam berapa sekarang?"

    anon "Saya tidak yakin."

    odette "Kepalaku membunuhku..."

    anon @ f_snarky "Maaf membangunkanmu."

    odette "Tidak, tidak apa-apa."

    odette "Apa yang kamu inginkan?"

    show odette a_idle with dissolve
    return

label button_odette_intro_interior_e15e20:
    scene expression player.location.background_closeup with None
    show odette
    show anon
    with dissolve
    anon "Hai, {b}Odette{/b}."

    odette "Hai, teman besar."

    return

label button_odette_intro_interior_e6e14:
    scene expression player.location.background_closeup with None
    show odette
    show anon
    with dissolve
    anon "Hai, {b}Odette{/b}."

    odette "Hai, tampan."

    return

label button_odette_intro_interior_e1e5:
    scene expression player.location.background_closeup with None
    show odette
    show anon
    with dissolve
    odette "Pemiliknya ada di sana, tampan."

    anon "O-oh, oke."

    anon @ a_wave "Terima kasih."

    odette @ -m_talk "Mhmm."

    hide anon with dissolve
    return

label button_odette_eve_party_speak_to_tuuku:
    scene expression player.location.background_closeup with None
    show anon:
        xoffset -100
    show eve b_dress:
        flip
        xoffset 200
    show odette
    with dissolve
    odette "{b}Tuuku{/b} pasti sedang keluar, aku tidak bisa menemukannya dimanapun..."

    eve "Kami akan menemukannya."

    show odette f_smirk
    if M_eve.biggus_dickus:
        odette "K-kamu tahu, aku yakin {b}[firstname]{/b} bisa menemukannya sendiri... Jika kamu ingin menutup telepon bersamaku {b}Evie{/b}?"

    else:
        odette "K-kamu tahu, aku yakin {b}Evie{/b} bisa menemukannya sendiri... Jika kamu ingin menutup telepon bersamaku {b}[firstname]{/b}?"

    eve @ -m_talk "Hmm?"

    odette "Bantu aku menggaruk sedikit rasa gatal yang aku rasakan saat ini?"

    show odette a_suck_fingers with dissolve
    show anon f_confused
    eve f_surprised "!!!"
    if M_eve.biggus_dickus:
        eve "T-tidak, tidak apa-apa..."

        show eve f_normal
        odette a_idle "Anda yakin?"

        odette "{b}[firstname]{/b} tidak keberatan, maukah kalian?"

    else:
        eve "T-tidak, dia ikut denganku!"

        show eve f_normal
        odette a_idle "Aduh, jangan serakah {b}Evie{/b}..."

        odette "Anda dapat kembali dan bergabung dengan kami setelah selesai."

    anon "Eh?"

    show anon b_empty f_surprised_left zorder 1:
        flip
        xoffset -744
    show eve a_grab_mc f_normal_right:
        unflip
        xoffset -400
    eve "Kami akan tetap bersatu, terima kasih!"

    hide anon
    hide eve
    with dissolve
    odette @ f_laugh "Hahaha, aku suka membuatnya tersipu!"

    return

label button_odette_eve_party_speak_to_odette:
    scene expression player.location.background_closeup with None
    show anon
    show odette f_smirk
    with dissolve
    odette "Hai, teman besar!"

    anon @ a_wave "H-hei, {b}Odette{/b}."

    odette "Apa aku baru saja melihatmu berdebat dengan Thundercunt?"

    anon f_confused "Petir?"

    odette "Ya, gadis yang baru saja pergi dengan gusar."

    show anon f_normal
    odette "Aku satu sekolah dengannya, kamu tahu?"

    anon "Maksud Anda {b}[jen_name]{/b}?"

    odette @ f_laugh "Hehe, ya."

    anon "Dia teman sekamarku."

    odette f_surprised "Thundercunt adalah teman sekamarmu?!"

    anon f_sad_down "..."
    odette f_smirk "Sialan, dasar anak malang."

    anon f_skeptical "Kenapa kamu terus memanggilnya seperti itu?"

    odette "Petir?"

    odette "Begitulah semua orang memanggilnya di sekolah menengah."

    anon f_normal @ f_laugh "Sungguh?"

    anon "Saya pikir dia populer di sekolah menengah?"

    odette @ f_eyeroll "Ya, dia, agak..."

    odette "Dia berlari bersama regu pemandu sorak dan semua orang bodoh, tapi hampir semua orang membencinya."

    anon "Saya tidak tahu."

    odette "Dia sangat menyebalkan saat itu..."

    anon f_normal @ f_flirt "Oh, dia masih begitu."

    odette @ f_laugh "Ha ha ha!"

    pause
    anon "Jadi sepertinya saya ingat Anda menyebutkan kejutan untuk saya?"

    odette "Oh, maksudmu kamu belum melihatnya?"

    anon "T-tidak?"

    odette "Sayang sekali."

    odette "Butuh waktu berjam-jam untuk menyelesaikan semuanya dan terlihat cantik untuk Anda."

    odette @ f_laugh "Hehehe!"

    anon f_worried "Saya tidak mengerti."

    odette @ f_surprised "{i}*Terkesiap*{/i} Bicara tentang iblis..."

    anon @ -m_talk "Hmm?"

    show odette a_point with dissolve
    pause
    show anon:
        flip
        xoffset -500
    with dissolve
    show odette a_idle with dissolve
    pause
    anon f_shock "!!!"

    scene location_tattoo_rooftop_cutscene02
    show text _ ("My breath caught in my throat as {b}Eve{/b} ascended the stairs onto the rooftop.\nI don't know how {b}Odette{/b} had managed this but it was more than\nI could have hoped for!") as caption
    with fade
    pause

    scene location_tattoo_rooftop_cutscene03
    show text _ ("She looked so, incredibly, beautiful!") as caption
    with fade
    pause

    scene expression player.location.background_closeup
    show anon f_shock:
        flip
        xoffset -500
    show odette f_smirk
    with fade
    odette "Hehe, sebaiknya kamu angkat rahangmu, {b}[firstname]{/b}..."

    anon "..."
    odette "Kamu berhutang banyak padaku untuk ini, kamu tahu?"

    anon f_flirt "Y-ya..."

    hide anon
    show anon:
        xoffset -100
    show eve f_nervous b_dress:
        xoffset -400
    with dissolve
    eve "Hai."

    anon "H-hei."

    odette "Mengapa aku tidak membelikan kalian beberapa gelas bir, ya?"

    hide odette with dissolve
    odette "Sial, aku baik-baik saja!"

    eve "..."
    anon f_normal "Anda terlihat..."

    eve f_sad_down "Apakah itu buruk?"

    anon f_shock "T-tidak!"

    anon f_worried "Itu-"

    eve "{b}Odette{/b} berhasil."

    anon f_normal "Kamu adalah gadis tercantik yang pernah kulihat!"

    eve f_happy "B-benarkah?"

    anon "Tentu saja."

    eve @ f_nervous_down "Hehe, aku sedikit khawatir..."

    eve "Saya belum pernah memakai pakaian seperti ini sebelumnya."

    anon "aku hanya-"

    show anon f_flirt
    pause
    anon "Wah!"

    eve @ f_laugh "hehe!"

    anon f_normal "Anda harus berpakaian seperti ini setiap hari."

    eve @ f_nervous_down "Ah, menurutku tidak..."

    eve @ f_surprised "Apakah Anda tahu berapa lama waktu yang dibutuhkan?"

    anon @ f_laugh "Tidak, beritahu aku."

    eve "Riasannya saja memakan waktu lebih dari satu jam!"

    anon f_worried "Wah benarkah?"

    eve @ f_eyeroll "Ya, dan itu terjadi setelah {b}Odette{/b} menyuruhku mencoba ratusan pakaian berbeda!"

    anon f_normal "Nah, kalian berdua pasti memilih yang bagus..."

    eve "Hehe, aku senang kamu menyukainya."

    pause
    eve "Saya kira itu menyenangkan, mencoba semua pakaian itu..."

    eve "... Tapi aku pastinya tidak bisa memakai sesuatu seperti ini ke sekolah!"

    eve f_sad_down "Gadis-gadis lain akan-"

    anon "Menjadi sangat cemburu?"

    eve f_normal @ f_surprised "Apa?!"

    show odette a_beers with dissolve
    show eve f_normal_right
    odette "Baiklah, aku membelikanmu masing-masing."

    show anon a_beer
    show eve a_beer
    show odette a_idle f_smirk
    with dissolve
    odette "Jadi, apa yang kalian bicarakan, para sejoli?"

    show eve f_normal
    anon "Betapa irinya semua gadis di sekolah jika dia selalu berpakaian seperti ini."

    eve f_normal_right @ f_laugh "Oh, diamlah!"

    odette "Dia benar, kamu tahu."

    odette "Separuh orang di pesta ini sedang memeriksa Anda saat ini."

    eve f_angry_right "T-tidak, sebenarnya tidak!"

    odette "Oh ya, mereka..."

    eve f_nervous_down @ -m_talk "..."
    odette "Oh, lihat dia menjadi cemas sekarang."

    odette "Jangan pikirkan itu, {b}Evie{/b}!"

    odette "Minumlah bir itu dan bawalah {b}[firstname]{/b} ke lantai dansa."

    show eve a_beer_drink f_drink with dissolve
    anon f_worried "Ehh, aku bukan penari yang hebat..."

    show eve a_beer f_nervous_down with dissolve
    odette "Percayalah, tidak ada yang akan peduli."

    odette "Tidak ketika Anda memiliki gadis terpanas di pesta bersama Anda."

    eve f_nervous "K-kamu mau, {b}[firstname]{/b}?"

    anon f_confused "Ehh."

    odette "Ayo, kawan."

    odette "Membuat semua orang iri."

    anon f_worried "Y-ya, oke."


    scene location_tattoo_rooftop_cutscene04
    show text _ ("I was nervous as hell about dancing in front of everyone but as I looked at {b}Eve{/b}'s\nbeautiful face and saw how much fun she was having; the butterflies in my stomach went away.") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("What did I care what other people thought?\nThe only person that mattered was her and she was having the time of her life.") as caption with dissolve
    pause

    scene expression player.location.background_closeup
    show anon b_dressed_catch_breath
    show eve f_laugh b_dress
    with fade
    eve "Hehehehe!"

    show anon
    anon "Fiuh, aku mulai lelah."

    eve f_happy "Y-ya, aku juga."

    eve "Kamu ingin istirahat sebentar?"

    anon "Tentu."


    scene location_tattoo_rooftop_ledge with slowfade
    show eve b_dress_sidebed:
        yoffset 10
    show anon b_sit zorder 1:
        yoffset 10
    with dissolve
    eve "Kamu tahu, kamu sebenarnya tidak terlalu buruk dalam menari..."

    anon @ f_surprised "bukan aku?"

    eve @ f_laugh "Hehe, tidak."

    eve @ f_eyeroll "Maksud saya, Anda tidak akan memenangkan kontes menari apa pun, tetapi Anda melakukannya dengan baik."

    anon f_grumpy "Cih, aduh kawan... Cara menghancurkan impian seorang pria, {b}Eve{/b}!"

    eve @ f_laugh "Ha ha ha!"

    show anon f_flirt
    pause
    anon "Aku tidak bisa melupakan betapa menakjubkannya penampilanmu malam ini..."

    eve f_nervous_down "Kamu sangat menyukainya?"

    anon "Saya bersedia."

    anon "Kamu sangat cantik!"

    eve f_nervous "Hehe, terima kasih."

    pause
    anon @ f_surprised "Maksudku, tidak masalah apa yang kamu kenakan... Kamu selalu cantik!"

    anon "Tapi ini hanya-"

    pause
    anon "Ini sungguh kejutan yang luar biasa."

    eve f_sexy "Ya, tahukah Anda, saya mungkin bisa diyakinkan untuk berpakaian seperti ini lagi..."

    anon "Oh?"

    eve "Mungkin, berkencan atau apa?"

    anon f_normal "Itu ide yang bagus!"

    eve f_normal "Ya?"

    anon "Sangat!"

    anon "Kita bisa pergi menonton film atau keluar makan malam atau-"

    hide eve
    show anon b_sit_kiss_eve1
    with dissolve
    anon "!!!"
    pause
    show anon b_sit_kiss_eve
    pause
    show eve b_dress_sidebed f_sexy zorder 0:
        yoffset 10
    show anon b_sit f_surprised
    with dissolve
    eve "Ya Tuhan, kamu pencium yang baik!"

    anon f_flirt "Heh, t-terima kasih."

    hide eve
    show anon b_sit_kiss_eve
    with dissolve
    pause
    pause
    eve "MM."

    pause
    show eve b_dress_sidebed f_sexy zorder 0:
        yoffset 10
    show anon b_sit f_flirt a_touch_eve
    with dissolve
    eve "K-kamu tahu, jika kamu mau..."

    eve "Kita bisa turun ke kamarku dan-"

    show anon f_surprised
    show eve f_surprised
    odette "HEI, {b}EVIE{/b}!"

    show eve f_sad_down
    odette "KAMU DIMANA?!"

    eve f_normal @ f_eyeroll "{i}*Huh*{/i} Kita sudah sampai..."

    odette "Oh, ini dia!"

    scene expression player.location.background_blur with None
    show anon o_boner:
        xoffset -100
    if M_eve.biggus_dickus:
        show eve b_dress_boner a_cover:
            flip
            xoffset 200
    else:
        show eve b_dress a_cover:
            flip
            xoffset 200
    show odette
    with dissolve
    if M_eve.biggus_dickus:
        odette "Maaf mengganggu kalian berdua tapi-"

        odette f_surprised_down "!!!"
        pause
        eve "A-apa?"

        show eve f_normal_down
        pause .5
        eve f_surprised "!!!" with hpunch
        show eve
        eve a_idle "EEEEEEP!"

        show eve f_nervous_down zorder 0:
            xoffset -100
        show anon f_surprised_left zorder 1:
            xoffset 50
        with dissolve
        pause
        show anon f_normal
        odette f_normal "{i}*Ahem*{/i} Aku uhh, maukah kalian membantuku?"

        anon "Tentu, ada apa?"

        odette "Bisakah kamu lari keluar dan menyuruh {b}Tuuku{/b} untuk membawanya ke sini?"

        odette "Orang-orang mulai mencicipi dagangannya dan saya yakin dia tidak ingin mereka menghisap semuanya."

        anon "Ya, kita bisa melakukan itu."

        odette "Saya akan sangat menghargainya."

        show odette f_smirk
        pause
        odette "Sekali lagi maaf atas gangguannya."

        eve "I-tidak apa-apa."

        odette @ f_laugh "Heh, kalian sungguh menggemaskan, sumpah..."

        hide odette with dissolve
        pause
        show anon f_worried:
            flip
            xoffset -350
        with dissolve
        anon "Kamu baik-baik saja?"

        eve @ f_nervous "Umm, y-ya..."

        eve "Aku hanya butuh waktu sebentar."

        anon "Tentu."

    else:
        odette "Maaf mengganggu kalian berdua tapi-"

        odette f_surprised "!!!"
        pause
        eve "A-apa?"

        eve f_surprised_right "!!!" with hpunch
        show eve f_surprised a_idle:
            xoffset 100
        with dissolve
        eve "EEEEEEP!"

        anon f_worried @ -m_talk "Hmm?"

        pause
        odette "{i}*Ahem*{/i} Aku uhh, maukah kalian membantuku?"

        anon "Tentu, ada apa?"

        odette "Bisakah kamu lari keluar dan menyuruh {b}Tuuku{/b} untuk membawanya ke sini?"

        odette "Orang-orang mulai mencicipi dagangannya dan saya yakin dia tidak ingin mereka menghisap semuanya."

        anon "Ya, kita bisa melakukan itu."

        odette "Saya akan sangat menghargainya."

        show odette f_smirk
        pause
        odette "Sekali lagi maaf atas gangguannya."

        eve "I-tidak apa-apa."

        odette @ f_laugh "Heh, dasar gadis yang beruntung, kamu..."

        hide odette with dissolve
        pause
        show eve f_nervous:
            unflip
            xoffset -400
        with dissolve
        anon f_confused "Ada apa?"

        eve "K-kamu umm... Sulit."

        anon f_surprised_down "!!!"
        show anon a_cover_boner
        show expression "characters/anon/anon_arms_dressed_a_cover_boner.png":
            xpos -100
        with dissolve
        anon f_worried "Wah!"

        anon "M-maaf tentang itu..."

        eve @ f_laugh "Hehe, tidak apa-apa."

        hide anon
        hide expression "characters/anon/anon_arms_dressed_a_cover_boner.png"
        with dissolve
    return

label odette_button_party_start:
    scene expression player.location.background_closeup with None
    show anon
    show odette
    with dissolve
    odette "Kamu datang kan?"

    anon "Ya, aku datang."

    odette f_smirk "Bagus, karena saya punya rencana istimewa dan Anda pasti akan menyukainya!"

    anon f_worried "B-benarkah?"

    odette @ f_laugh "Ya!"

    pause
    anon "Apa-"

    odette @ a_mock "Ah, ah, ah!"

    odette "Ini kejutan!"

    anon @ -m_talk "..."
    odette "Anda tinggal menunggu dan melihatnya pada {b}Sabtu{/b}."

    odette f_normal @ f_laugh "Ini akan menjadi epik!"

    return

label button_odette_eve_clients_wake_up_grace:
    scene expression player.location.background_closeup with None
    show anon f_worried
    show odette a_head f_tired b_wakeup
    with dissolve
    odette "Eugh, kepalaku rasanya mau meledak!"

    anon @ a_behind_head -m_talk "(Saya mungkin harus membiarkannya...)"

    hide anon with dissolve
    return

label button_odette_eve_bike_breakdown_check_bike:
    scene expression player.location.background_closeup with None
    show anon
    show odette
    with dissolve
    odette "Baiklah... Lihat siapa yang datang!"

    anon "H-hai."

    odette f_smirk "{b}Tuuku{/b} menceritakan padaku semua tentangmu dan {b}Evie{/b} kecil kita di tenda."

    anon f_worried "Dia melakukannya?"

    odette @ -m_talk "Mmhmm."

    odette "Saya sangat senang untuk kalian!"

    anon f_normal "Hehe, terima kasih."

    pause
    odette "Dan kudengar dia gadis yang cukup beruntung..."

    anon f_confused "Eh, beruntung?"

    anon "Apa maksudmu?"

    odette @ f_wink "Oh ayolah, kamu tahu maksudku!"

    odette @ a_point "Tidak perlu malu, kawan!"

    anon f_normal @ f_grin a_behind_head -m_talk "..."
    odette @ f_laugh "Ha ha ha!"

    odette f_normal "Anda mencarinya?"

    anon "Y-ya."

    odette "Saya pikir dia membantu {b}Grace{/b} dengan sepedanya."

    odette "Di garasi."

    anon "Baiklah terima kasih!"

    hide anon with dissolve
    odette f_smirk "Sama-sama, kawan."

    pause
    odette "Mmm, sungguh gadis yang beruntung!"

    odette @ f_laugh "hehe!"

    hide odette with dissolve
    return

label button_odette_eve_big_sis_check_apartment:
    scene expression player.location.background_blur with None
    show anon f_surprised
    show odette b_wakeup f_yawn a_stretch
    with dissolve
    odette "{i}*Menguap*{/i} Kamu kembali..."

    show anon f_flirt
    odette f_tired_happy a_sides "Anda berubah pikiran di sana, tampan?"

    anon @ -m_talk "Hmm?"

    odette "Anda bisa menjadi sendok kecil jika Anda mau?"

    anon f_shy_down a_behind_head "Menurutku, itu bukan ide yang bagus..."

    odette f_laugh "Hehe, sesuaikan dirimu.."

    hide odette with dissolve
    anon a_idle f_worried @ -m_talk "( Hmm, aku mungkin harus mengikuti {b}Eve{/b} ke atas dan memastikan dia baik-baik saja... )"

    hide anon with dissolve
    return

label button_odette_eve_big_sis_talk_odette:
    scene expression player.location.background_blur with None
    show anon f_worried:
        xoffset -100
    show eve a_hip_angry f_sad:
        flip
        xoffset 200
    with dissolve
    eve "{b}Odette{/b}?!"

    odette "Hmm?"

    eve "Apa yang terjadi!"

    show odette b_wakeup f_yawn a_stretch:
        xoffset 100
    with dissolve
    show anon f_surprised
    odette "{i}*Menguap*{/i} Oh, maaaan..."

    show anon f_flirt
    odette f_tired a_sides "Ugh, apa yang kamu lakukan pulang sepagi ini?"

    anon @ -m_talk "..."
    eve f_surprised "Ya Tuhan, {b}Odette{/b}, payudaramu keluar!"

    odette f_tired_down "Apakah itu?"

    odette a_pull_top @ a_grab_top "Ugh, sial..."

    show anon f_unimpressed
    pause
    odette b_dressed f_tired a_sides "Jam berapa sekarang?"

    eve f_sad "Seperti jam dua belas tiga puluh?"

    odette "Apakah kamu bolos kelas lagi?"

    show anon f_surprised_teeth
    eve f_angry a_rossed "Ini bukan masalah besar!"

    odette "Adikmu akan marah..."

    show anon f_worried
    eve "Dimana dia?"

    eve "Kenapa tidak ada yang mengurus tokonya?!"

    odette @ a_shrug "Oke, pertama-tama... Tolong pelankan suaramu, aku menderita migrain yang hebat!"

    eve f_angry "Apa yang kamu, mabuk?!"

    odette @ a_point "Adikmu terjaga setengah malam kemarin mengerjakan cewek yang menginginkan baju berlengan lengkap... Jadi, aku menyuruhnya untuk menutup mata sementara aku mengawasi toko..."

    eve @ a_wtf "... Tapi kamu tidak menjaga toko, kamu pingsan di sini!"

    odette a_head f_yawn "Oww, serius... Tidak terlalu keras..."

    show odette f_tired
    eve "Anda tahu {b}Grace{/b} tidak boleh kehilangan bisnis apa pun, bukan?"

    odette a_sides @ f_yawn "{i}*Menguap*{/i} Beri aku istirahat, {b}Evie{/b}... Lagipula kalian tidak pernah punya pelanggan di pagi hari."

    eve @ f_eyeroll "Yesus Kristus..."

    hide eve with dissolve
    anon @ -m_talk "..."
    odette f_tired_happy "Apa yang kamu lakukan di sini, tampan?"

    anon "Ehh..."

    odette "Kamu mau ikut berbaring bersamaku?"

    anon f_shy "Menurutku, itu bukan ide yang bagus..."

    odette "Aww, ayolah... aku tidak menggigit!"

    odette "... Kecuali kamu menyukainya?"

    show odette f_laugh
    anon f_shy_down a_behind_head "..."
    show odette f_tired_happy
    pause
    odette f_yawn a_stretch "{i}*Menguap*{/i} Sesuaikan dirimu..."

    hide odette with dissolve
    anon a_idle f_worried @ -m_talk "( Hmm, aku mungkin harus mengikuti {b}Eve{/b} ke atas dan memastikan dia baik-baik saja... )"

    hide anon with dissolve
    return

label button_odette_crypt:
    anon f_worried "Mengapa saya terus terbangun di kuburan?"

    odette f_confused "Hah?"

    anon "Saat aku mengunjungimu di ruang bawah tanah..."

    anon "... Setelah kita umm, kamu tahu?"

    odette "Setelah kita apa?"

    anon @ a_whisper_back "Berhubungan seks."

    odette f_smirk "Kami tidak berhubungan seks, {b}[firstname]{/b}."

    anon f_surprised "!!!"
    anon f_worried_left a_sides @ a_whisper_back "Ssst!"

    pause
    anon f_worried "Apa maksudmu kita tidak berhubungan seks?"

    anon "saya ingat-"

    odette "Kami minum anggur dan kamu pergi lagi..."

    anon "Ya?"

    odette "Anda benar-benar tidak bisa menangani alkohol Anda, Anda tahu?"

    anon f_skeptical "Tapi aku-"

    pause
    anon "Aku yakin kita-"

    pause
    odette "Saya merasa seperti asap akan keluar dari telinga Anda atau semacamnya..."

    anon f_sad_down "Ini semua sangat membingungkan."

    odette "Eh ya."

    pause
    odette "Jangan khawatir, saya yakin Anda akan melakukannya lebih baik lain kali."

    anon f_worried @ f_skeptical "Lain kali?"

    odette "{b}temui aku di ruang bawah tanah saat bulan purnama{/b}."


    $ renpy.dynamic(ttl=game.timer.days_until_lunar(.5))
    $ renpy.dynamic(day=game.timer.dayOfWeek(delta=ttl, full=True))

    if game.timer.is_fullmoon():
        show anon f_surprised
        odette @ f_wink "Maksudku malam ini!"

    elif ttl > 21:
        odette @ f_sad "Yang terakhir baru saja berakhir, jadi akan memakan waktu beberapa minggu."

    elif ttl > 14:
        odette @ f_pouting "Yang terakhir baru terjadi sekitar seminggu yang lalu, jadi yang berikutnya belum akan terjadi dalam beberapa minggu."

    elif ttl > 7:
        odette @ f_shy "Yang berikutnya tinggal seminggu lagi, saya sangat bersemangat!"

    elif ttl > 1:
        odette "Yang berikutnya ada di [day], saya harap Anda siap!"

    else:
        show anon f_surprised
        odette @ f_wink "Oh, dan {i}peringatan spoiler{/i}: Itu besok!"


    odette "Dan bawalah {b}Eve{/b}, jika Anda mau..."

    anon f_normal @ f_surprised -m_talk "{i}*Meneguk*{/i}"

    return


label odette_repeat_boobjob:
    anon "Di sofa... dengan payudaramu?"

    odette f_smirk "Oh ho ho!"

    show odette a_pull_top f_happy_down
    with {'master': dissolve}
    odette "Kamu ingin meniduri payudaraku?"

    show anon a_sides f_shy
    show odette f_tired_happy
    with {'master': dissolve}
    anon "{i}*Gulp*{/i} Y-ya, tolong."

    odette "Baiklah, sobat besar..."

    show anon f_shy_low
    show odette b_drop1
    with dissolve
    show anon f_flirt_low
    show odette b_drop2
    with dissolve
    show anon f_flirt_grin
    show odette a_reveal b_topless
    with {'master': dissolve}
    pause
    odette "...Ikuti aku."

    hide odette
    with {'master': dissolve}
    anon f_shy "Manis!"

    hide anon with dissolve

    call scene_odette_paizuri.repeat
    $ unlock_scene('Odette', '05_unlocked')

    scene expression background(l=L_tattooparlor_garage) as stage
    show odette a_hair_cum b_topless f_annoyed_back o_cum_chest:
        xoffset 100
        xzoom -1
    show anon a_sides f_confused at flip
    with fade
    odette "Aduh, aku mendapatkannya lagi di rambutku..."

    show anon a_shy_neck f_worried
    with {'master': dissolve}
    anon "Oh, uhh... Ups?"

    show anon f_surprised_teeth
    with {'master': dissolve}
    odette "... Dasar bajingan."

    show anon a_sides f_sad
    with {'master': dissolve}
    anon "Saya benar-benar minta maaf."

    show odette a_reveal f_shy
    with {'master': dissolve}
    odette "Heh, tidak apa-apa, kawan."

    show anon f_shy
    with {'master': dissolve}
    odette "Aku akan mencucinya."

    show anon f_worried
    show odette a_hips f_thinking:
        xoffset -400
        xzoom 1
    with {'master': dissolve}
    odette "Saya hanya berharap {b}Grace{/b} tidak ada di sana."

    show anon f_worried_high
    hide odette
    with {'master': dissolve}
    anon "Benar, baiklah..."

    show anon a_wave f_shy_high
    with {'master': dissolve}
    anon "... Terima kasih lagi!"

    odette "Terima kasih kembali."

    show anon a_sides f_normal
    with {'master': dissolve}
    pause
    show anon f_grin
    with {'master': dissolve}
    anon @ -m_talk "( Luar biasa. )"

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
