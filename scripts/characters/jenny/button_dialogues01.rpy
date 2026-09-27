label button_jenny_eve_party_speak_to_jenny:
    scene expression player.location.background_closeup with None
    show jane b_dance:
        flip
    with dissolve
    random_girl "Wooo!"

    random_guy "Sial, kawan... Cewek-cewek ini seksi sekali!"

    jenny "Ha ha ha!"

    show anon f_confused with dissolve
    anon "{b}[jen_name]{/b}?"

    jenny "Hmm?"

    hide jane
    show jenny b_casual a_sides:
        xoffset 50
    show jane:
        xoffset -250
    with dissolve
    show anon f_worried
    if M_jenny.finished_inclusive(S_jenny_cheerleader_sex):
        show jenny f_surprised
        jane "Bukankah itu teman sekamarmu?"

        jenny f_upset "Y-ya."

        jenny "Apa yang kamu lakukan di sini, {b}[firstname]{/b}?"

        anon "Teman saya tinggal di sini dan dia mengundang saya."

        jane "Anda berteman dengan {b}Grace{/b}?"

        anon "Ya."

        anon "Err, yah, agak..."

        anon "Aku berteman dengan adik perempuannya."

        jane "Oh ya!"

        jane "Anda berdua datang ke perpustakaan beberapa hari yang lalu untuk menggantungkan brosur itu, bukan?"

        jenny @ f_eyeroll "Apa yang kamu, memukulnya juga?"

        anon f_sad_down "T-tidak."

        pause
        anon f_worried "Maksudku, kami seperti sedang berkencan... Menurutku..."

        anon "... Tapi kami belum melakukan hal seperti itu!"

        show jane a_thinking f_sad:
            flip
            xoffset 300
        with dissolve
        jane "Apakah kamu cemburu?"

        show jane f_normal
        jenny f_surprised "A-apa?!"

        jenny f_upset @ f_eyeroll "Tentu saja aku tidak cemburu!"

        jane f_sexy a_idle "Ya Tuhan, kamu cemburu!"

        jenny f_angry a_crossed "Kenapa aku harus peduli dengan siapa teman sekamarku yang pecundang?!"

        jane "Saya tidak tahu, tetapi Anda jelas tahu."

        jenny "Diam!"

        jane @ f_laugh "Ha ha ha!"

        jane "Tumpahkan itu."

        jenny @ f_eyeroll "aku pergi."

        jane f_sad "Apa?!"

        hide jenny with dissolve
        jane "K-kamu akan pergi?!"

        jenny "Pesta ini meledak!"

        jane "{b}[jen_name]{/b}, tunggu!"

        hide jane with dissolve
        anon @ -m_talk "(Hah. Itu aneh...)"

        anon @ -m_talk "(Oh baiklah, sebaiknya lupakan saja.)"

        anon a_thinking f_thinking @ -m_talk "( {b}Grace{/b} berkata {b}Odette{/b} seharusnya ada di sini di suatu tempat... )"

        hide anon with dissolve
    else:
        show jenny f_gross
        jane "Bukankah itu teman sekamarmu?"

        jenny "Cih, apa yang kamu lakukan di sini?"

        anon "Teman saya tinggal di sini dan dia mengundang saya."

        jane "Anda berteman dengan {b}Grace{/b}?"

        anon "Ya."

        anon @ a_behind_head "Err, yah, agak..."

        anon "Aku berteman dengan adik perempuannya."

        jane "Oh ya!"

        jane "Anda berdua datang ke perpustakaan beberapa hari yang lalu untuk menggantungkan brosur itu, bukan?"

        jenny @ f_eyeroll "Ya Tuhan, MENGUAP!"

        show jenny f_angry
        pause
        jenny "Apakah kamu akan tersesat, {b}[firstname]{/b}?!"

        jenny "Kami mencoba menari."

        anon @ f_surprised "Dengan serius?"

        jane "Haha, sial {b}[jen_name]{/b}..."

        jane "Itu agak kasar, bukan begitu?"

        jenny f_upset "Dengar, kamu bilang akan ada pria-pria keren dan kaya di pesta ini dan itulah satu-satunya alasan aku datang."

        jenny "Sebaliknya, itu hanya sekelompok pria malang dan teman sekamarku yang pecundang!"

        jane f_sexy a_thinking "Entahlah, menurutku dia agak manis..."

        jenny @ f_eyeroll "Eugh, kamu tidak hanya mengatakan itu?!"

        show jane f_normal a_idle:
            flip
            xoffset 300
        with dissolve
        jane "Apa?!"

        jenny "Aku keluar dari sini!"

        hide jenny with dissolve
        jane f_sad "K-kamu akan pergi?!"

        jenny "Pesta ini meledak!"

        jane "{b}[jen_name]{/b}, tunggu!"

        hide jane with dissolve
        anon @ -m_talk "(Sheesh, apa yang merayapi pantatnya?)"

        anon @ -m_talk "(Oh baiklah, sebaiknya lupakan saja.)"

        anon f_thinking a_thinking @ -m_talk "( {b}Grace{/b} berkata {b}Odette{/b} seharusnya ada di sini di suatu tempat... )"

        hide anon with dissolve
    return

label jenny_button_gf_experience_stay_in:
    anon f_normal "Tetap di dalam."

    show jenny f_normal
    jenny "Kamu serius hanya ingin jalan-jalan di sini?"

    anon f_worried "Ide buruk?"

    jenny "Kedengarannya agak membosankan..."

    jenny f_grin "... Tapi setidaknya aku tidak perlu khawatir ada orang yang melihat kita bersama."

    anon "Saya cukup yakin tak seorang pun akan peduli, {b}[jen_name]{/b}..."

    jenny "Ya, terserah."

    pause
    jenny @ -m_talk "Hmm."

    hide anon
    show jenny b_dressed_pulling1
    with dissolve
    jenny "Ikutlah denganku."

    show jenny b_dressed_pulling2
    anon "Ke-kemana kita akan pergi?"

    hide jenny with dissolve
    jenny "Di lantai bawah."

    scene black with fade
    pause
    scene expression "backgrounds/location_home_livingroom_couch08.jpg" with None
    show expression "backgrounds/location_home_livingroom_couch08b.png" with None
    show jenny b_front_undies a_lap f_front_left
    show anon b_front f_front_right zorder 1
    with dissolve
    if M_diane.finished_state(S_diane_barn_news):
        jenny "Saya kira {b}Diane{/b} bekerja lembur."

        jenny "Beruntungnya kami, kami memiliki sofa untuk diri kami sendiri."

    else:
        jenny "Sepertinya {b}[deb_name]{/b} sedang tidur."

        jenny "Beruntungnya kami, kami memiliki sofa untuk diri kami sendiri."

    show jenny f_front_forward a_remote with dissolve
    if M_jenny.get("jenny_girlfriend_first_time"):
        anon "Jadi apa yang kita lakukan?"

        show jenny f_front_forward
        jenny "Kamu bilang kamu ingin jalan-jalan, bukan?"

        anon "Ya."

        anon "Anda ingin menonton film kung fu?"

        show jenny f_front_left
        jenny "Saya harap Anda bercanda..."

        anon f_front_shy_right "Kamu tidak suka kungfu?"

        jenny "Heh, tidak ada gadis yang menyukai kungfu, doofus..."

        anon "Itu tidak benar!"

        show jenny f_front_eyeroll a_down with dissolve
        jenny "Percayalah kepadaku."

        jenny "Itu benar."

        show jenny f_front_forward
        pause
        show jenny f_front_left
        jenny "Apa yang kamu lakukan?!"

        anon f_front_right "Saya pikir akan menyenangkan untuk memegang tangan Anda ..."

        jenny "... Kamu ingin memegang tanganku?"

        anon f_front_shy_right "Ya?"

        jenny "Siapa kamu, dua belas tahun?!"

        anon @ f_front_surprised_right -m_talk "..."
        anon "Baiklah, terserah."

        anon "Lupakan saja."

        jenny @ f_front_eyeroll "{i}*Huh*{/i} Tidak, aku minta maaf."

        jenny "Aku tidak pandai dalam urusan pacar ini..."

        show anon a_hold_hands
        show jenny a_empty
        with dissolve
        jenny "Di sana."

        show anon f_front_right
        pause
        jenny "Senang sekarang?"

        anon "Ya."

        show anon a_down
        show jenny f_front_forward a_remote
        with dissolve
        pause
        show anon f_front_forward
        jenny "Oh, ini dia!"

        show anon a_hold_hands
        show jenny a_empty
        with dissolve
        anon @ -m_talk "..."
        anon "Apa ini?"

        jenny "Ini adalah sitkom lama yang berjudul {i}Pals{/i}."

        jenny "{b}[deb_name]{/b} dan saya selalu menontonnya ketika saya masih kecil."

        anon "Tentang apa ini?"

        jenny "Sekelompok enam teman yang tinggal di Manhattan."

        anon "Kedengarannya membosankan."

        jenny @ f_front_laugh "Tidak, ini sangat lucu!"

        anon f_front_right "Kau tahu, karena akulah yang membayar uang untuk ini... Tidakkah menurutmu aku harus mengendalikan remotenya?"

        show jenny f_front_laugh
        jenny "Oke, kamu pasti belum pernah punya pacar sebelumnya..."

        anon @ -m_talk "..."
        jenny "Haha!"

        show jenny f_front_left
        anon "Kamu seharusnya bersikap baik, ingat?"

        jenny "Ya, ya... Oke!"

        show jenny b_front_cuddle a_empty f_front_cuddle_look zorder 2
        show anon f_front_surprised_right a_down
        with dissolve
        anon "!!!"
        show jenny f_front_cuddle_look_up
        jenny "Diam saja dan tonton, {b}[firstname]{/b}."

        jenny "Ini sangat lucu, Anda akan lihat."

        show jenny f_front_cuddle_look
        anon f_front_forward "O-oke..."

        pause
        jenny @ f_front_cuddle_look_up "Oh, di sinilah Matt menaruh kalkun syukur di kepalanya!"

        anon "Apa?"

        anon "Mengapa seseorang menaruh kalkun di kepalanya?"

        jenny @ f_front_cuddle_look_up "Dia mencoba menakuti teman sekamarnya!"

        show jenny f_front_cuddle_look
        pause
        anon "Wah, siapa itu?!"

        jenny @ f_front_cuddle_look_up "Oh, dia?"

        jenny @ f_front_cuddle_look_up "Itu Courtney dan Anda mungkin berpikir dia sangat seksi, kejutan besar..."

        anon "Maksudku, dia cantik..."

        anon f_front_right_low "Tapi tidak secantik kamu."

        show anon f_front_forward
        jenny @ f_front_cuddle_look_up "Oh, muntah!"

        jenny @ f_front_cuddle_look_up "Terkadang kamu mengatakan hal yang paling konyol..."

        anon f_front_gross_down "Maaf."

        jenny @ -m_talk "..."
        jenny @ f_front_cuddle_look_up "Tidak, tidak apa-apa."

        show anon f_front_low
        pause
        jenny @ f_front_cuddle_look_up "Terima kasih, {b}[firstname]{/b}."

        anon f_front_right_low "Terima kasih kembali."

        show anon f_front_forward
        pause
        anon @ f_front_forward_laugh "Ha ha ha!"

        pause
        anon "Oke, kamu benar."

        anon "Itu sangat lucu!"

        show jenny f_front_cuddle_look_up
        jenny "Hehe, sudah kubilang!"

        show jenny f_front_cuddle_look
        anon "Kenapa aku tidak mengingatmu dan {b}[deb_name]{/b} menonton ini?"

        show jenny f_front_cuddle_look_up
        jenny "Mungkin karena kamu selalu tidak melakukan sesuatu dengan ayahmu..."

        anon "Ya, menurutku itu masuk akal."

        jenny "Itu salah satu acara yang lebih asyik untuk ditonton bersama orang lain."

        show jenny f_front_cuddle_look
        anon "Saya bisa melihatnya."

        show jenny f_front_cuddle_look_up with None
        show anon a_empty
        show expression "characters/anon/anon_arms_front_a_cuddle.png" zorder 2
        with dissolve
        pause
        jenny "Ini bagus."

        anon "Ya, benar."

        pause
        hide anon
        show jenny b_front_kiss
        hide expression "characters/anon/anon_arms_front_a_cuddle.png"
        with dissolve
        anon "!!!"
        pause
        show anon b_front_kiss_talk f_front_kiss
        show jenny b_front_kiss_talk f_front_kiss
        with dissolve
        anon "A-untuk apa itu?"

        jenny "Tidak ada alasan."

        jenny "Aku hanya merasa menginginkannya."

        anon "Heh, baiklah, apakah kamu merasa ingin melakukan lebih banyak lagi?"

        jenny "Maaaybe..."

        hide anon
        show jenny b_front_kiss
        with dissolve
        jenny "MM."

        pause
        scene black with fade
        pause
        scene expression "backgrounds/location_home_livingroom_couch08.jpg"
        show expression "backgrounds/location_home_livingroom_couch08b.png"
        show anon b_front a_empty f_front_forward
        show jenny b_front_cuddle f_front_cuddle_look
        show expression "characters/anon/anon_arms_front_a_cuddle.png"
        with fade
        pause
        show jenny f_front_cuddle_look_up
        jenny "Baiklah, aku mulai mengantuk..."

        show jenny b_front_undies a_lap f_front_left
        show anon a_down
        hide expression "characters/anon/anon_arms_front_a_cuddle.png"
        with dissolve
        anon f_front_right @ -m_talk "Hmm?"

        anon "Tidak apa-apa, kamu bisa tidur jika kamu mau."

        anon "Saya tertarik untuk melihat apa yang terjadi selanjutnya."

        show jenny a_remote f_front_forward with dissolve
        jenny "Heh, kita sudah menonton tiga episode..."

        show jenny f_front_left
        jenny "... Dan selain itu, aku pacarmu, ingat?"

        anon "Ya?"

        jenny "Jadi pacarmu memberitahumu sudah waktunya tidur!"

        jenny "Ayo pergi!"

        hide jenny with dissolve
        anon "Oke oke..."

        jenny "Hehehe!"

        anon "(Dia pergi dengan tergesa-gesa...)"

        anon "(Aku harus {b}bergegas mengejarnya{/b}. )"

        hide anon with dissolve
    else:
        anon "Jadi apakah kita akan menonton {i}Pals{/i} lagi?"

        anon "Saya menyukai pertunjukan itu."

        show anon a_hold_hands
        show jenny f_front_left a_empty
        with dissolve
        jenny "Yah, kami pastinya tidak menonton film kung fu..."

        show anon f_front_forward
        show jenny f_front_forward
        pause
        jenny "Ini dia."

        show jenny b_front_cuddle f_front_cuddle_look zorder 2
        show anon f_front_low a_down
        with dissolve
        anon @ -m_talk "!!!"
        show anon f_front_forward a_empty
        show expression "characters/anon/anon_arms_front_a_cuddle.png" zorder 3
        with dissolve
        pause
        show jenny f_front_cuddle_look_up
        jenny "Oh, ini episode bagus lainnya!"

        show jenny f_front_cuddle_look
        scene black with fade
        pause
        scene expression "backgrounds/location_home_livingroom_couch08.jpg"
        show expression "backgrounds/location_home_livingroom_couch08b.png"
        show jenny b_front_kiss
        with fade
        pause
        jenny "Hmm..."

        show anon b_front_kiss_talk f_front_kiss
        show jenny b_front_kiss_talk f_front_kiss
        with dissolve
        jenny "Oke, ayo naik ke atas!"

        anon "Sudah?"

        show jenny b_front_undies a_remote f_front_forward with dissolve
        show anon f_front_right b_front a_down with dissolve
        jenny "Ayo {b}[firstname]{/b}, pacarmu membutuhkan penismu yang sebesar itu!"

        show jenny f_front_left
        anon "Nah, jika Anda mengatakannya seperti itu..."

        jenny "Ayo pergi!"

        hide jenny with dissolve
        anon "Oke oke..."

        jenny "Hehehe!"

        anon "(Aku harus {b}bergegas mengejarnya{/b}. )"

        hide anon with dissolve
    return

label jenny_button_gf_experience_start:
    show anon f_flirt a_money with dissolve
    anon "Di Sini."

    show anon a_idle
    show jenny f_sexy_down a_money b_dressed
    with dissolve
    if M_jenny.get("jenny_girlfriend_first_time"):
        jenny "Hehe, aku tidak percaya aku melakukan ini..."

    else:
        jenny "Heh, itu yang ingin kulihat!"

    show jenny f_sexy a_hips with dissolve
    jenny @ -m_talk "..."
    show jenny f_eyeroll
    jenny "{i}*Huh*{/i} Jadi, apa yang ingin kamu lakukan?"

    show jenny f_normal
    return

label jenny_button_gf_experience_no_money_repeat:
    anon f_flirt "Ya... Tidak semuanya."

    show jenny f_upset
    jenny "Sejak kapan kamu bangkrut?!"

    anon f_normal "Entahlah..."

    jenny @ f_eyeroll "{i}*Sigh*{/i} Baiklah, berikan saja apa pun yang kamu punya dan ayo lakukan ini..."

    anon f_confused "B-benarkah?"

    show anon f_surprised
    jenny "Ya!"

    return

label jenny_button_gf_experience_no_money_first:
    anon f_flirt "Ya... Tidak semuanya."

    show jenny f_upset
    jenny @ -m_talk "..."
    jenny "Sudah kubilang lima ratus dolar!"

    anon f_worried "T-tapi aku tidak punya sebanyak itu..."

    show jenny f_eyeroll
    jenny "Aww, itu sangat menyedihkan bagimu."

    show jenny f_grin
    jenny "{b}Kembalilah ketika kamu punya uang{/b}, bodoh."

    anon f_sad_down "{i}*Huh*{/i} Baik."

    show anon f_tired
    return

label jenny_button_gf_experience_nevermind:
    anon f_worried "Setelah dipikir-pikir, saya tidak tertarik saat ini."

    show jenny f_upset
    jenny "Cih, jangan buang waktuku, {b}[firstname]{/b}!"

    return

label jenny_button_gf_experience_evening:
    anon f_flirt "Ingin melakukan hal itu?"

    show jenny f_grin
    jenny "Oh, kamu ingin pengalaman pacar malam ini ya?"

    jenny "Saya harap Anda membawa uang..."

    return

label jenny_button_gf_experience_day:
    anon f_flirt "Ingin melakukan hal itu?"

    show jenny f_upset
    jenny "Jangan sekarang, bodoh!"

    anon f_worried @ -m_talk "Hmm?"

    show jenny f_grin
    jenny "Beritahu saya tentang hal itu {b}nanti malam{/b}!"

    anon f_normal "Oh benar."

    jenny "Jangan lupa {b}membawa lima ratus dolar{/b} juga!"

    return

label button_jenny_have_a_surprise_no:
    anon f_worried "Tidak, aku ingin yang asli."

    show jenny f_eyeroll
    jenny "Ya, tidak terjadi, pecundang."

    show jenny f_upset
    jenny "Beritahu aku jika kamu sudah sadar..."

    show jenny b_magic_sit_stand_dressed a_idle with dissolve
    return

label button_jenny_have_a_surprise_yes:
    anon f_normal "Ya."

    show jenny f_grin
    jenny "Kalau begitu kita sepakat!"

    jenny "{b}Kembalilah malam ini dengan lima ratus dolar{/b} dan aku milikmu sepenuhnya."

    anon f_worried "Mengapa kita tidak bisa memulainya sekarang?"

    show jenny f_upset
    jenny "Uhh, karena ini waktunya pertunjukan kamera dan bayarannya jauh lebih dari lima ratus dolar, bodoh!"

    anon f_sad_down "... Bagus."

    show anon f_tired
    show jenny b_magic_sit_stand_dressed a_idle with dissolve
    return

label button_jenny_have_a_surprise_necklace:
    anon f_normal "Aku punya kejutan untukmu!"

    show jenny f_eyeroll
    jenny "Yah, sebaiknya itu sesuatu yang menyenangkan!"

    show jenny f_upset
    show anon f_shy_down a_backpack with dissolve
    pause
    if player.has_item("crystal_necklace"):
        show anon f_laugh a_necklace1 with dissolve
    elif player.has_item("pearl_necklace"):
        show anon f_laugh a_necklace3 with dissolve
    else:
        show anon f_laugh a_necklace2 with dissolve
    anon "Ta-da!"

    show anon f_normal
    show jenny f_surprised
    jenny "..."
    show jenny f_gross
    jenny "eh!"

    anon f_worried "K-kamu tidak menyukainya?"

    show anon f_tired
    show jenny b_dressed a_crossed with dissolve
    jenny "Eh, tidak!"

    anon "..."
    jenny "Kenapa kamu membelikanku itu?!"

    anon "Aku hanya berpikir, mungkin itu akan meyakinkanmu untuk-"

    show anon f_worried
    jenny @ f_upset "Ya Tuhan, apa kau mencoba membujukku untuk berkencan lagi?!"

    show anon f_tired a_idle with dissolve
    anon @ -m_talk "..."
    show jenny f_eyeroll
    jenny "Apa-apaan ini, {b}[firstname]{/b}?!"

    show jenny f_upset
    jenny "{i}*Huh*{/i} Oke, pertama-tama, seleramu jelek..."

    jenny "Kalung itu terlihat murahan sekali!"

    anon @ -m_talk "..."
    jenny "Maksudku, sejujurnya, jika suatu keajaiban kamu benar-benar mendapatkan pacar suatu hari nanti... Kamu harus memberinya uang tunai dan biarkan dia-"

    show jenny f_surprised
    jenny "..."
    anon f_worried "Biarkan dia apa?"

    show jenny f_grin a_hips with dissolve
    jenny "Ya Tuhan, aku baru saja mendapat ide cemerlang!"

    anon @ -m_talk "..."
    jenny "Aku berpikir, karena kamu jelas-jelas menyedihkan dan sangat membutuhkan pacar..."

    anon f_skeptical "Hei, itu bukan-"

    show anon f_worried
    jenny "Saya {i}mungkin{/i} bersedia {b}bertindak seperti itu{/b}... Tentu saja dengan biaya yang murah."

    anon f_skeptical "Tunggu sebentar."

    anon "Apakah kamu serius menyarankan agar aku membayarmu untuk menjadi pacarku?"

    jenny "Tidak, aku menyarankanmu membayarku untuk {i}berpura-pura{/i} menjadi pacarmu..."

    anon @ -m_talk "..."
    anon "Mengapa saya melakukan itu?"

    show jenny f_laugh
    jenny "Karena seperti yang kubilang, kamu menyedihkan dan putus asa."

    show jenny f_grin
    anon "Saya tidak!"

    show jenny f_laugh
    jenny "Hahahaah, kamu juga begitu!"

    show jenny f_grin
    anon @ -m_talk "..."
    jenny "Ditambah lagi, ini akan memberiku kesempatan untuk mengembangkan aktingku!"

    anon "Ya, kamu adalah aktris yang buruk..."

    show jenny f_angry
    jenny "{i}*Terkesiap*{/i} Persetan!"

    jenny "Saya seorang aktris yang luar biasa!"

    anon f_sad_down "Ya benar."

    show anon f_sad
    show jenny f_grin a_hips_touch1:
        xoffset -100
    with dissolve
    jenny "Ayolah, ini akan menjadi alasan yang tepat bagi kita untuk menghabiskan lebih banyak waktu bersama."

    anon f_worried "A-apa yang kamu lakukan?"

    show jenny a_hips_touch2 with dissolve
    jenny "Saya benar-benar ingin melakukan ini, {b}[firstname]{/b}..."

    jenny "Izinkan saya menunjukkan kepada Anda bagaimana perasaan saya yang sebenarnya terhadap Anda."

    anon @ -m_talk "..."
    jenny "aku tidak ingin menyembunyikannya lagi..."

    show anon f_surprised
    jenny "Aku ingin memberitahu seluruh dunia betapa aku peduli padamu!"

    jenny "Bagaimana aku memikirkanmu sepanjang waktu..."

    jenny "Wajahmu yang tampan, lenganmu yang kuat... Potongan rambut kecilmu yang menggemaskan!"

    anon f_worried "B-benarkah?"

    jenny "Mhmm."

    jenny "Aku ingin menggenggam tanganmu, {b}[firstname]{/b}!"

    anon f_normal @ -m_talk "..."
    jenny "aku ingin mencicipi bibirmu..."

    jenny "... Tertidur dalam pelukanmu."

    anon @ -m_talk "..."
    jenny "Aku ingin memberitahumu bahwa aku mencintaimu!"

    anon "Aku juga menginginkannya!"

    pause
    hide jenny
    show jenny f_laugh
    with dissolve
    jenny "Pfft, HAHAHAHAHAHAAAH!!"

    anon f_surprised @ -m_talk "..."
    anon f_angry "Itu tidak lucu, {b}[jen_name]{/b}!"

    jenny "Kamu seharusnya melihat wajahmu!!"

    jenny "HAHAHAH! {i}*Mendengus*{/i}"

    anon "Kamu menyebalkan!"

    show jenny f_grin
    jenny "Kaulah yang bilang aku tidak bisa berakting!"

    jenny "Akui saja, aku sangat baik!"

    anon f_tired @ -m_talk "..."
    jenny "Aku bisa menjadi pacarmu... Dengan harga yang tepat."

    anon "{i}*Huh*{/i} Berapa yang kamu inginkan?"

    jenny "Mmm, katakanlah lima ratus dolar untuk satu malam."

    anon f_surprised "Lima ratus!!"

    anon "Banyak sekali, {b}[jen_name]{/b}!"

    jenny @ f_eyeroll "Oh, tolong... Ini perubahan bodoh."

    jenny "Begini saja, aku akan mampir besok pagi juga."

    anon f_normal "K-maksudmu kamu akan tinggal bersamaku sepanjang malam?"

    jenny "Itu yang Anda inginkan, bukan?"

    return

label jenny_button_what_are_you_writing:
    anon f_worried "Apa yang kamu tulis?"

    show jenny f_upset
    jenny "Bukan urusanmu, bodoh!"

    anon "aku hanya penasaran-"

    show anon f_surprised_teeth a_up
    show jenny f_angry a_crossed
    with dissolve
    jenny "KELUAR!!!"

    hide anon with dissolve
    return

label jenny_button_what_are_you_writing_2:
    anon f_worried "Apa yang kamu tulis?"

    show jenny f_upset
    jenny "Bukan urusanmu."

    anon f_normal "Aduh, ayolah... aku penasaran."

    jenny "Tidak mungkin, {b}[firstname]{/b}!"

    show anon f_worried
    jenny "Ini adalah pemikiran pribadi saya!"

    show anon a_up with dissolve
    anon f_skeptical "Baiklah, baiklah... Astaga!"

    show anon a_idle with dissolve
    return

label jenny_button_nevermind_evening:
    anon f_worried "Kurasa aku akan pergi saja kalau begitu..."

    show jenny f_eyeroll
    jenny "Ya Tuhan, kamu benar-benar pecundang."

    show jenny f_upset
    show anon f_skeptical a_thinking with dissolve
    anon @ -m_talk "..."
    show jenny f_angry a_crossed with dissolve
    jenny "Tersesat!!"

    hide anon with dissolve
    return

label jenny_button_nevermind_evening_2:
    anon f_skeptical "Hmm, lupakan saja."

    anon f_laugh "Aku punya hal lain yang harus dilakukan hari ini."

    show anon f_normal
    show jenny f_eyeroll
    jenny "Ya benar!"

    show jenny f_grin
    jenny "Apa yang pernah kamu lakukan?"

    show jenny f_laugh
    show anon f_tired
    jenny "Selain duduk di kamar dan bermain dengan dingus kecilmu?"

    if M_jenny.get("dominance") <= 0:
        anon @ -m_talk "..."
        jenny "Ha ha ha!"

        show jenny f_grin
        show anon a_wave with dissolve
        anon "Terserahlah, aku akan pergi."

        show anon a_idle with dissolve
        jenny "Sampai jumpa, pecundang!"

        hide anon with dissolve
    else:
        anon f_skeptical @ -m_talk "..."
        show jenny f_grin
        show anon f_flirt a_point with dissolve
        anon "Ini tidak terlalu kecil dan Anda harus tahu."

        anon "Kamu lebih sering bermain dengannya daripada aku akhir-akhir ini..."

        show anon a_idle with dissolve
        show jenny f_surprised
        jenny "!!!"
        show jenny f_surprised_down_back
        jenny "Itu bukan-"

        show jenny f_angry a_crossed with dissolve
        jenny "Persetan denganmu!"

        anon f_laugh "Haha!"

        jenny "Pergi!"

        anon f_flirt "Dengan senang hati."

        hide anon with dissolve
    return

label jenny_button_fool_around_evening:
    show anon f_flirt a_point with dissolve
    anon "Ingin bermain-main?"

    show anon a_idle with dissolve
    show jenny f_normal
    jenny "Nah, {b}Jane{/b} seharusnya menelepon sebentar lagi."

    anon "Jadi?"

    show jenny f_upset
    jenny "Jadi tidak sekarang, {b}[firstname]{/b}..."

    show jenny f_normal
    jenny "... Tanya saya lagi {b}nanti{/b}."

    anon f_tired "Oke."

    return

label button_jenny_fool_around_pool_repeat:
    anon f_normal "Ingin bermain-main?"

    show jenny f_grin
    jenny "Kamu ingin meniduriku di kolam renang lagi?"

    anon f_skeptical "Ehh, entahlah... Terakhir kali kamu hampir menenggelamkanku!"

    anon "Ayo naik ke atas dan lakukan di kamarmu."

    show anon f_normal
    jenny "Tidak, aku ingin melakukannya di sini!"

    show anon f_worried
    pause
    anon "Lalu kursinya?"

    show jenny f_upset
    jenny "Apakah kamu bercanda?! {b}[deb_name]{/b} akan benar-benar melihat kita!!"

    anon "Y-ya, tapi..."

    show jenny f_grin
    jenny "Kamu akan baik-baik saja, sayang besar!"

    jenny "Ayolah!"

    hide jenny with dissolve
    pause
    anon f_tired "{i}*Huh*{/i} Sial..."

    hide anon with dissolve
    jump jenny_pool_sex_intro

label button_jenny_fool_around_pool_first:
    if store._in_replay is not None:
        $ player.location = L_home_backyard
        scene expression player.location.background_closeup
        show jenny f_upset b_swimsuit a_hips
    show anon f_normal
    anon "Ingin bermain-main?"

    show jenny f_normal b_swimsuit a_hips
    jenny "Tidak, aku sedang sibuk."

    anon f_confused "Sibuk dengan apa?"

    show jenny f_upset
    jenny "Ini waktuku sendiri, twerp."

    anon "Waktumu sendirian?"

    show jenny f_normal
    jenny "Ya, saya terhubung kembali dengan alam!"

    anon f_worried @ -m_talk "..."
    anon f_skeptical "{b}[jen_name]{/b}, kamu sedang duduk di halaman belakang kami sambil memotret payudaramu..."

    show jenny f_grin
    jenny "Mereka tampak hebat dalam bikini ini, bukan?"

    anon f_tired "{i}*Huh*{/i} Jadi, kamu aneh!"

    show anon f_skeptical
    show jenny f_upset
    jenny "Persetan, {b}[firstname]{/b}!"

    anon "Kenapa kamu tidak suka, berenang atau apalah?"

    jenny "Kenapa aku ingin pergi-"

    show jenny f_surprised
    pause
    show jenny f_grin
    jenny "Tunggu sebentar, apa yang {b}[deb_name]{/b} lakukan saat ini?"

    anon f_worried "Uhh, entahlah?"

    anon "Mungkin membersihkan rumah atau mencuci pakaian."

    show jenny f_sexy
    jenny @ -m_talk "Hmm."

    anon "Kenapa kamu menatapku seperti itu?"

    show jenny f_grin
    jenny "Ayo berenang."

    anon f_confused "Benar-benar?!"

    jenny "Ya, ayolah..."

    anon f_normal "Luar biasa, biarkan aku lari ke atas dan ambil baju renangku!"

    show jenny f_laugh
    jenny "Kamu tidak perlu baju renang, bodoh!"

    show jenny f_grin
    jenny "Buka saja pakaianmu dan masuk!"

    anon f_worried "Y-maksudmu, skinny dipping?"

    show jenny f_eyeroll
    jenny "Duh."

    show jenny f_grin
    anon "Bagaimana jika {b}[deb_name]{/b} muncul di sini?!"

    show jenny f_laugh
    jenny "Heh, nanti dia akan tahu betapa mesumnya dirimu.."

    show jenny f_grin
    anon f_angry @ -m_talk "..."
    jenny "Jangan banci, dia sibuk membersihkan rumah!"

    anon f_worried "Baiklah, tapi hanya jika kamu melepas pakaianmu juga!"

    jenny "Bagus."

    jenny "Kamu yang pertama."

    anon "Bagus."

    show anon b_dressed_changing with dissolve
    pause
    show anon b_dressed_changing2 with dissolve
    pause
    show anon b_underwear a_sides f_skeptical with dissolve
    anon "Apakah kamu tidak akan mulai membuka baju?"

    jenny "Mmm, naaah."

    anon "Apa?!"

    show jenny f_laugh
    jenny "Ha ha ha!"

    scene expression "backgrounds/location_home_backyard_pool_day_closeup.jpg"
    show jenny b_pool_enter with dissolve
    pause
    show jenny b_pool_edge f_normal
    with dissolve
    anon "Hei, kamu bilang kamu akan telanjang juga!"

    show jenny f_grin
    jenny "Ya baiklah, aku berbohong."

    anon @ -m_talk "..."
    jenny "Berhentilah merengek dan masuklah ke sini..."

    show anon b_pool_undress with dissolve
    anon "Baiklah baiklah!"

    show jenny b_pool f_surprised with dissolve
    jenny "Wah, jangan berani-"

    show anon b_pool_jumping1
    show jenny b_pool_cover f_nipple2
    with dissolve
    anon "BOLA MERAI!!!"

    jenny "{b}[firstname]{/b}!!!"

    show anon b_pool_jumping2 with dissolve
    pause
    show jenny b_pool f_angry
    show anon b_pool_under
    with dissolve
    jenny "Dasar brengsek!"

    show anon b_pool f_laugh
    with dissolve
    anon "Hahahahaaah!"

    show anon f_normal
    jenny "Grrr, kamu sungguh menyebalkan!"

    anon "Kamu pantas mendapatkannya, kamu pembohong."

    show jenny b_pool_hair with dissolve
    jenny "..."
    show jenny b_pool with dissolve
    anon "Jadi sekarang bagaimana?"

    show jenny f_upset
    jenny "Baiklah, tadinya aku akan menidurimu, tetapi setelah peluru meriam itu, aku berubah pikiran..."

    if M_jenny.get("dominance") <= 0:
        anon f_surprised @ -m_talk "!!!"
        anon f_worried "B-benarkah?"

        jenny "{i}*Huh*{/i} Ya, tapi sekarang kamu harus memohon..."

        show jenny f_angry
        anon "Silakan?"

        show jenny f_grin
        jenny "Ayolah, kamu tahu apa yang ingin aku dengar..."

        anon "{i}*Huh*{/i} Tolong, {b}Putri [jen_name]{/b}?"

        jenny "Tolong apa?"

        anon "Silakan berhubungan seks dengan saya?"

        jenny "Hmm, baiklah... Sudah cukup."

    else:
        anon f_skeptical "Ya benar."

        show jenny f_angry
        jenny "Aku serius, aku ingin meminta maaf!"

        anon "Oke, beritahu Anda apa."

        anon "Anda meminta maaf karena berbohong kepada saya dan kemudian saya akan meminta maaf karena telah memercik Anda."

        show jenny f_angry_pouting
        jenny "..."
        anon f_laugh "Lalu kita akan berhubungan seks, setuju?"

        show anon f_normal
        show jenny f_angry
        jenny "Persetan denganmu!"

        anon "Ya, itulah idenya."

        show jenny f_upset
        jenny "TIDAK, maksudku-"

        anon f_laugh "hehe!"

        show anon f_normal
        jenny @ f_eyeroll "Ugh, kamu sangat, tidak lucu..."

        anon "Baiklah, kita bisa melewatkan permintaan maaf dan langsung berhubungan seks?"

        jenny "Bagus."

    show jenny b_pool_plunge1 f_grin with dissolve
    pause
    hide anon
    show jenny b_pool_plunge2 f_sexy_down
    with dissolve
    pause
    jump jenny_pool_sex_intro

label button_jenny_wanna_watch_porn:
    anon f_normal "Anda ingin menonton film porno bersama?"

    show jenny f_grin
    jenny "Oh, kamu menyukainya, ya?"

    anon "Tentu saja."

    anon "Kupikir mungkin malam ini kita bisa-"

    jenny "Pfft!"

    show jenny f_eyeroll
    jenny "Ya, saya tahu persis apa yang bisa kami lakukan..."

    show jenny f_grin
    anon f_worried "Apakah itu ya?"

    show jenny f_upset
    jenny "Tidak, itu mungkin... Jika aku menginginkannya."

    anon "... Dan jika tidak?"

    show jenny f_laugh
    jenny "Kalau begitu, kurasa kau harus menyelesaikannya sendiri, bukan, pecundang kecil?"

    jenny "Hahahaah!"

    show jenny f_grin
    anon @ -m_talk "..."
    return

label button_jenny_fool_around_diningroom_first:
    if store._in_replay is not None:
        $ player.location = L_home_diningroom
    scene expression game.timer.image("dining_room{}")
    show jenny b_breakfast_dressed a_phone f_upset_down zorder 1
    show anon b_dinner_sitting_look_left f_worried zorder 0
    show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
    with dissolve
    pause
    anon f_normal "Ingin bermain-main?"

    show jenny f_upset
    jenny "Apa disini?"

    anon f_worried "T-tidak!"

    anon "Maksudku, ayo naik ke atas, dan kita bisa-"

    show jenny f_grin a_rub with dissolve
    anon f_surprised @ -m_talk "!!!" with hpunch
    jenny "Bagaimana jika saya ingin melakukannya di sini?"

    anon f_worried "K-kamu tidak mungkin serius!!"

    jenny "Kenapa tidak?"

    anon "{b}[deb_name]{/b} sedang memasak di kamar sebelah!"

    jenny "Jadi?"

    anon "Jadi, dia akan membunuh kita!"

    jenny "Dia tidak perlu tahu..."

    anon "Ya benar!"

    show jenny f_eyeroll a_crossed with dissolve
    jenny "Kamu sungguh menyebalkan..."

    show jenny f_upset
    anon "Tidak, bukan aku!"

    show jenny f_grin
    jenny "Lalu buktikan!"

    anon "Hah?"

    show jenny a_yell with dissolve
    jenny "Hai, {b}[deb_name]{/b}?!"

    show jenny a_crossed with dissolve
    debbie "Hah?"

    anon "Apa yang kamu-"

    if store._in_replay is not None:
        jump jenny_dining_room_sex_intro
    return

label button_jenny_fool_around_diningroom_repeat:
    anon f_normal "Ingin bermain-main?"

    show jenny f_grin
    jenny "Anda ingin bersenang-senang?"

    anon "Ya, ayo ke atas-"

    show anon f_surprised
    jenny "Hai, {b}[deb_name]{/b}?!"

    debbie "Hah?"

    anon f_worried "Tidak, aku tidak ingin-"

    return

label jenny_button_leave_final_morning:
    anon f_worried "Aku akan menemuimu nanti... Oke?"

    show jenny f_upset
    jenny "Ya, terserah."

    jenny "Sampai jumpa."

    hide anon with dissolve
    return

label jenny_button_leave_final_bedroom:
    anon f_normal "Maaf."

    show jenny f_upset
    jenny "Ugh, apa-apaan ini, {b}[firstname]{/b}?!"

    jenny "Anda membuat saya kehilangan uang!"

    show jenny f_gross
    anon f_confused "Tidak bisakah kamu melakukannya tanpa aku?"

    show jenny f_eyeroll
    jenny "Ya..."

    show jenny f_upset
    jenny "... Tapi mereka membayar lebih jika penis besarmu itu terlibat!"

    anon f_normal "Aku akan kembali besok, oke?"

    jenny "Sebaiknya kau, brengsek."

    hide anon with dissolve
    return

label jenny_button_ask_movie_date:
    scene expression player.location.background_closeup with None
    show anon f_normal
    show jenny f_normal
    with dissolve
    anon "Hei, kamu harus berpakaian."

    show jenny f_gross
    jenny "Berpakaian?!"

    show jenny f_grin
    jenny "Anda biasanya ingin saya melepas pakaian, bukan memakainya..."

    anon f_laugh "Hah, ya, aku tahu, tapi aku punya kejutan untukmu."

    show anon f_normal
    show jenny f_sad
    jenny "Hah?"

    anon "Saya menemukan pria yang memata-matai Anda."

    jenny "Benar-benar?"

    anon "Ya, dia meminta maaf dan menawari kami tiket film gratis!"

    show jenny f_surprised
    jenny @ -m_talk "..."
    jenny "Kamu ingin aku menonton film... Bersamamu?"

    show jenny f_sad
    anon "Ya?"

    jenny "Di depan umum..."

    anon f_worried "Iya?!"

    jenny @ -m_talk "..."
    show jenny f_upset a_crossed
    jenny "{i}*Huh*{/i} Apakah kita harus melakukannya?"

    anon f_normal "Ayolah, itu akan menyenangkan!"

    show jenny f_eyeroll
    jenny "Uh, baiklah."

    show jenny f_upset
    jenny "Tapi aku memilih filmnya!"

    anon "Oke."

    jenny "Dan saya ingin popcorn!"

    anon f_surprised @ -m_talk "..."
    jenny "Dan cacing bergetah!"

    anon f_skeptical "Oke, sialan!"

    show jenny f_eyeroll
    pause
    hide anon with dissolve
    return

label jenny_button_movie_date:
    scene expression player.location.background_closeup with None
    show anon f_skeptical
    show jenny f_normal
    with dissolve
    anon "Cepatlah berpakaian, {b}kita punya film untuk ditonton{/b}."

    show anon f_normal
    show jenny f_upset
    jenny "Ugh, aku mendengarmu pertama kali!"

    hide anon with dissolve
    return

label jenny_button_come_to_my_room:
    anon f_flirt "Mengapa kamu tidak datang ke kamarku malam ini?"

    show jenny f_sexy
    jenny "Heh, oh kamu pasti menyukainya, bukan?"

    if M_jenny.get("dominance") <= 0:
        anon f_worried "Y-ya."

        show jenny f_grin b_dressed a_crossed with dissolve
        jenny "Kamu akan memohon padaku untuk itu?"

        anon "Saya rasa..."

        anon "I-jika kamu mau."

        show jenny f_laugh
        jenny "Hahahaah!"

    else:
        anon f_flirt "Ya... aku bertanya, bukan?"

        show jenny f_laugh
        jenny "Hehehe!"

        show jenny f_sexy
        anon "Anda juga menyukainya dan Anda mengetahuinya."

        show anon f_grin
        show jenny f_eyeroll
        jenny "Ya, terserah."

        show jenny f_sexy
        pause
        anon f_flirt "Kaulah yang selalu pingsan karena penisku..."

        show jenny f_upset b_dressed a_crossed with dissolve
        jenny "Saya tidak!"

        anon f_laugh "Hah, kamu benar-benar melakukannya!"

        show jenny f_angry_pouting
        pause
        anon f_flirt "Hanya... Berhenti bersikap keras kepala dan datanglah ke kamarku malam ini!"

    show jenny f_sexy
    jenny "Ya, aku mungkin akan mampir..."

    show jenny f_grin
    pause
    jenny "... {b}{i}JIKA{/i}{/b} Saya menginginkannya."

    show jenny b_magic_sit_stand_dressed a_idle with dissolve
    return

label button_jenny_pool_talk:
    scene expression player.location.background_closeup with None
    show jenny b_swimsuit a_hips
    show anon f_normal
    with dissolve
    anon "Selamat pagi."

    jenny "Hai."

    show jenny f_normal_low
    pause
    anon "Anda ingin saya memindahkan payung itu agar Anda bisa mendapatkan sinar matahari?"

    show jenny f_normal
    jenny "Apa?"

    jenny "Oh, tidak..."

    anon f_worried "T-tapi-"

    show jenny f_laugh
    jenny "Aku di sini bukan untuk berjemur, bodoh..."

    show jenny f_normal
    jenny "Hanya mencoba untuk bersantai."

    anon f_normal "Oh."

    show jenny f_eyeroll
    jenny "Selain itu, saya tidak berjemur."

    show jenny f_normal
    anon f_worried "T-tidak?"

    jenny "aku hanya terbakar."

    anon f_laugh "Hehe, aku juga."

    show anon f_normal
    show jenny f_normal_low
    pause
    anon f_worried "Jadi, uhh... {b}[deb_name]{/b} ingin aku bertanya padamu-"

    show anon f_surprised
    show jenny f_normal
    anon "..."
    show anon f_skeptical a_point with dissolve
    show jenny f_upset_down
    jenny "Apa yang kamu-"

    show jenny f_upset
    anon "Siapa itu?"

    show anon a_idle
    show jenny f_upset:
        flip
        xoffset 500
    with dissolve
    jenny @ -m_talk "Hmm?"


    scene location_home_backyard_cutscene01
    show text _ ("The interloper in the hedge seemed visibly alarmed as Jenny turned to focus on him.") as caption
    with fade
    pause

    scene expression player.location.background_closeup
    show anon f_surprised
    show jenny b_swimsuit a_hips f_angry:
        flip
        xoffset 475
    with fade
    jenny "Sekali lagi, kamu bajingan yang menyeramkan?!"

    jenny "Ini ketiga kalinya, bulan ini!"

    jenny "Pacarku akan menghajar penguntitmu!"


    scene location_home_backyard_cutscene02
    show text _ ("His alarm rapidly turned to panic, and he started to flee!") as caption
    with fade
    pause

    scene expression player.location.background_closeup
    show jenny f_angry b_swimsuit a_crossed
    show anon f_worried
    with fade
    jenny "Jangan hanya berdiri disana, pukul orang itu!"

    anon "A-apa kamu baru saja memanggilku pacarmu?"

    show jenny f_gross
    jenny "Dengan serius?!"

    show jenny f_angry
    jenny "Ada orang mesum yang memata-mataiku dan kamu khawatir tentang itu?!"

    anon "B-benar... Maaf."

    jenny "Cepat sebelum dia pergi!"

    hide anon with dissolve

    scene location_home_backyard_cutscene03
    show text _ ("I rushed to the spot where the stalker had been, but he was already well on his way.") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("He was faster than he looked... and there was no way I was going to catch him.") as caption with dissolve
    pause

    scene expression player.location.background_closeup with fade
    show anon b_dressed_catch_breath with dissolve
    anon "Haah... Haah..."

    show jenny f_angry b_swimsuit a_crossed with dissolve
    jenny "Dimana bajingan itu?!"

    anon f_tired b_dressed "Dia melepas..."

    show jenny f_eyeroll
    jenny "Ugh, sial!"

    show jenny f_upset
    anon f_confused "Siapa pria itu?!"

    jenny "Entahlah, hanya orang aneh yang terus memata-mataiku saat aku berada di tepi kolam renang..."

    show anon f_normal
    pause
    jenny "Sobat, aku ingin memberi pelajaran pada bajingan itu!"

    show jenny f_angry_pouting
    show anon f_grin
    pause
    show jenny f_gross
    pause
    show jenny f_upset
    jenny "Kenapa kamu menatapku seperti itu?!"

    anon f_laugh "Kamu memanggilku pacarmu."

    show anon f_grin
    jenny "Ya Tuhan..."

    jenny "Aku hanya mencoba menakuti orang itu!"

    show jenny f_gross
    anon @ f_laugh "Hehe, tentu saja kamu..."

    show jenny f_eyeroll
    jenny "Ugh, dalam mimpimu, pecundang."

    hide jenny with dissolve
    anon f_laugh "Yah, itu bukan hal yang baik untuk dikatakan pada pacarmu..."

    jenny "Persetan, {b}[firstname]{/b}!"

    anon "Hahahaah!"

    anon f_surprised_down "(Hmm?)"

    show anon b_dressed_pickup with dissolve
    pause
    show anon a_ticket b_dressed f_surprised_down with dissolve
    anon "( Ini adalah {b}tiket film dari teater lokal{/b}... )"

    anon @ f_skeptical -m_talk "(Saya ingin tahu apakah orang itu menjatuhkannya?)"

    pause
    anon "(Ini untuk nanti hari ini.)"

    anon "( Mungkin, {b}Saya akan menemukannya di sana{/b}? )"

    hide anon with dissolve
    return

label jenny_button_fool_around:
    anon f_worried "Ingin bermain-main?"

    show jenny f_normal
    jenny "Ya, benar!"

    show anon f_normal
    show jenny f_grin_down b_pull1 with dissolve
    pause
    show jenny b_pull2 with dissolve
    pause
    show jenny b_pull3 with dissolve
    show jenny b_pull4 with dissolve
    show anon f_surprised
    pause
    show jenny f_grin_down b_naked a_panties_remove with dissolve
    pause
    show jenny b_naked_panties_remove_down with dissolve
    pause
    show jenny b_naked a_hips f_grin with dissolve
    pause
    jenny "Apa yang kamu tunggu?"

    hide anon
    show jenny b_groping_naked_suck_pre a_up with dissolve
    show jenny b_groping_naked_suck a_up_clench f_surprised with dissolve
    jenny "!!!"
    pause
    show jenny f_nipple3
    jenny "Hmm..."

    pause
    show jenny b_groping_naked_touch_talk with dissolve
    anon "Anda memiliki payudara terbaik yang pernah ada!"

    show jenny b_groping_naked_touch_look a_hips f_laugh
    jenny "Hehe, aku tahu."

    show jenny b_groping_naked_suck_pre a_up f_nipple3 with dissolve
    pause
    show jenny b_groping_naked_suck a_up_clench f_nipple1 with dissolve
    jenny "Haah!"

    jenny "Rasanya luar biasa..."

    show jenny f_nipple3
    pause
    show jenny b_groping_naked_finger with dissolve
    jenny "Ngghhh..."

    pause
    show jenny f_nipple2
    jenny "Fuuuuck..."

    show jenny f_nipple3
    pause
    show jenny f_nipple2
    jenny "Apakah kamu hanya akan menggodaku?"

    jenny "Ayo lakukan pertunjukan kamera!"

    show jenny f_nipple3
    return

label jenny_button_fool_around_not_today:
    show jenny b_groping_naked_touch_talk f_surprised with dissolve
    anon "Maaf, saya tidak punya waktu hari ini."

    show jenny b_groping_naked_touch_look a_hips f_upset
    jenny "Hmm, serius?!"

    jenny "Lalu kenapa kita-"

    show jenny b_groping_naked_finger a_up_clench f_nipple1 with dissolve
    jenny "Haaah!"

    show jenny f_nipple2
    jenny "Astaga!"

    show jenny f_nipple3
    pause
    show jenny f_nipple2
    jenny "aku akan-"

    show jenny f_nipple3
    pause
    show jenny b_groping_naked_squirt f_nipple2
    jenny "NGGHHH!!!" with flash
    pause
    show jenny b_groping_naked_orgasm f_nipple3
    show anon
    with dissolve
    jenny "Haah... Haah..."

    show jenny f_grin
    jenny "Brengsek."

    anon @ f_grin -m_talk "hehe."

    show jenny b_naked a_sides f_normal with dissolve
    jenny "Fiuh, aku harus berbaring..."

    anon "Sampai jumpa lagi, {b}[jen_name]{/b}."

    jenny "Sampai jumpa."

    hide anon with dissolve
    return

label jenny_button_really_staying:
    if player.location == L_home_diningroom:
        show anon f_worried b_dinner_sitting_look_left
    else:
        show anon f_worried
    with dissolve
    anon "Kamu benar-benar tinggal?"

    show jenny b_magic_sit_stand_dressed a_idle f_upset with dissolve
    jenny "Itu yang saya katakan, bukan?"

    anon "Ya, tapi menurutku kamu benci di sini?"

    jenny "Mmm, tidak terlalu buruk... Sekarang aku punya uang yang masuk."

    jenny "{b}[deb_name]{/b} saya tidak lagi kesulitan mencari pekerjaan dan saya mendapat makan gratis tiga kali sehari..."

    show jenny f_grin
    pause
    jenny "... Dan semua kebutuhan seksual saya terpenuhi."

    anon f_normal "Oh ya?"

    show jenny f_upset
    jenny "Jangan berpikir aku pacarmu atau semacamnya!"

    anon f_worried @ -m_talk "..."
    jenny "Kamu punya penis yang bagus tapi hanya itu yang membuatku tertarik..."

    jenny "Mengerti?!"

    anon "Kukira."

    show jenny f_grin
    jenny "Bagus."

    return

label jenny_button_nevermind_2:
    anon f_skeptical "Hmm, lupakan saja."

    anon "Aku punya hal lain yang harus dilakukan hari ini."

    show jenny f_eyeroll
    jenny "Ya benar!"

    show jenny f_grin
    jenny "Apa yang pernah kamu lakukan?"

    show jenny f_laugh
    jenny "Selain duduk di kamar dan bermain dengan dingus kecilmu?"

    show jenny f_grin
    if M_jenny.get("dominance") <= 0:
        anon f_worried @ -m_talk "..."
        show jenny f_laugh
        jenny "Ha ha ha!"

        anon @ f_skeptical "Terserahlah, aku akan pergi."

        show jenny f_grin
        jenny "Sampai jumpa, pecundang!"

        hide anon with dissolve
    else:
        anon f_angry @ -m_talk "..."
        anon "Ini tidak terlalu kecil dan Anda harus tahu."

        anon f_laugh "Kamu lebih sering bermain dengannya daripada aku akhir-akhir ini..."

        show anon f_grin
        show jenny f_surprised
        jenny "!!!"
        jenny "Itu bukan-"

        show jenny f_angry a_crossed with dissolve
        jenny "Persetan denganmu!"

        show jenny f_angry_pouting
        anon f_laugh "Haha!"

        show anon f_normal
        show jenny f_angry
        jenny "Pergi!"

        anon "Dengan senang hati."

        hide anon with dissolve
    return

label jenny_button_nothing_2:
    anon f_worried "Hanya membuat percakapan."

    show jenny f_upset_down
    jenny "Benar sekali."

    hide anon with dissolve
    return

label jenny_button_warming_up:
    if player.location == L_home_diningroom:
        show anon f_normal b_dinner_sitting_look_left
    else:
        show anon f_normal
    with dissolve
    anon "Akhirnya bersikap hangat padaku?"

    show jenny b_magic_sit_stand_dressed a_idle f_eyeroll with dissolve
    jenny "Pfft, sial tidak!"

    show jenny f_upset
    anon f_worried @ -m_talk "..."
    jenny "... Tapi kamu menghasilkan banyak uang untukku, jadi aku bersedia bertahan denganmu."

    anon "Ya benar."

    jenny "Namun itu tidak berarti Anda akan mendapat potongan keuntungan yang lebih besar!"

    anon "Oh, aku tidak akan pernah berani berpikir seperti itu..."

    jenny "Jangan jadi orang yang pintar!"

    anon "Mengapa kamu tidak bisa mengakui saja kalau kamu sedang bersikap hangat padaku."

    show jenny f_laugh
    jenny "Hah!"

    show jenny f_upset
    jenny "Teruslah bermimpi, brengsek!"

    pause
    anon "Apa pun."

    return

label button_jenny_not_swimming:
    anon f_worried "Tidak berenang?"

    show jenny f_upset
    jenny "Uhh, tidak."

    jenny "Airnya sangat dingin!"

    anon "Ah, ayolah."

    anon "Apa gunanya memiliki kolam jika tidak pernah digunakan?!"

    show jenny f_eyeroll
    jenny "Kamu hanya ingin melihatku basah kuyup."

    show jenny f_upset
    anon f_laugh "Ya, kamu menangkapku."

    show anon f_normal
    show jenny f_gross
    jenny "Perv."

    return

label jenny_button_nevermind:
    anon f_worried "Kurasa aku akan pergi saja kalau begitu..."

    show jenny f_upset
    jenny "Ya Tuhan, kamu benar-benar pecundang."

    anon f_angry @ -m_talk "..."
    show jenny f_angry
    show anon f_surprised
    jenny "Tersesat!!"

    hide anon with dissolve
    return

label jenny_button_just_saying_hi:
    anon f_worried "Hanya ingin menyapa."

    show jenny f_upset
    jenny "... Dengan serius?!"

    jenny "Jangan buang waktuku, {b}[firstname]{/b}."

    anon "Tidak bisakah kita-"

    show anon f_surprised
    show jenny f_angry
    jenny "NO!!!" with hpunch
    jenny "Kita tidak bisa \"hanya!\""

    jenny "Tunjukkan padaku sejumlah uang atau keluarlah, pecundang!"

    anon f_skeptical "Uh, baiklah..."

    return

label jenny_button_nothing:
    anon f_worried "Hanya berusaha bersikap ramah..."

    show jenny f_upset_down
    jenny "{i}*Mendengus*{/i} Ya, terserah."

    jenny "Aku tidak butuh teman, sialan..."

    jenny "Saya butuh uang!"

    anon f_laugh "Semoga beruntung dengan itu."

    hide anon with dissolve
    return

label jenny_button_you_and_phone:
    anon f_worried "Pernahkah ada yang memberitahumu bahwa menatap ponsel saat mengobrol itu tidak sopan?"

    show jenny f_upset_down
    jenny "Apa yang kamu, ibuku?!"

    jenny @ f_eyeroll "{i}Tidak sopan menatap ponselmu{/i}."

    jenny "Kamu terdengar seperti wanita tua yang pikun..."

    anon f_tired "..."
    show anon m_talk
    jenny "Pecundang."

    return

label jenny_button_just_curious:
    anon f_worried "Hanya ingin tahu bagaimana keadaannya."

    show jenny f_upset
    jenny "Ya, bagus."

    jenny "Kenapa kamu peduli?!"

    anon "Yah, kami seperti... Keluarga, sekarang."

    jenny @ f_eyeroll "Pfft, hampir tidak..."

    jenny "Makan saja sarapanmu dan tinggalkan aku."

    show jenny f_upset_down
    anon f_tired "Cih, baiklah."

    show anon f_shy_down
    return

label jenny_dialogue_make_a_deal_breakfast:
    if player.location == L_home_diningroom:
        show anon f_normal b_dinner_sitting_look_left
    else:
        show anon f_normal
    with dissolve
    anon "Ayo buat kesepakatan."

    show jenny b_magic_sit_stand_dressed a_idle f_upset with dissolve
    jenny "Jangan di sini, dasar brengsek..."

    jenny "{b}[deb_name]{/b} mungkin akan menangkap kita."

    anon f_worried "Oh benar."

    jenny "Ayo temui saya {b}siang ini{/b}."

    show anon f_normal
    pause
    jenny "... Dan bawakan uangnya!"

    hide anon with dissolve
    return

label button_jenny_camshow:
    show jenny f_upset
    jenny "Ayolah, kita ada pertunjukan yang harus dilakukan dan membuang-buang waktu."

    anon f_worried "O-oke."

    return

label button_jenny_start_camshow_handjob:
    if store._in_replay is not None:
        $ player.location = L_home_sisbedroom
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["08_unlocked"] = True
    scene expression player.location.background_closeup with None
    show jenny f_upset
    show anon f_worried
    with dissolve
    jenny "Anda siap melakukan ini?"

    anon "Y-ya, menurutku."

    anon "aku sedikit gugup..."

    jenny "Baiklah, ayo!"

    jenny "Pelanggan saya mengharapkan kinerja yang luar biasa dari Anda dan saya benar-benar bersungguh-sungguh!"

    anon "Aku tahu."

    jenny "Nah, kalau kamu tahu, lalu kenapa bajumu masih dipakai?!"

    anon "Hah?"

    show jenny f_grin_down b_pull1 with dissolve
    pause
    show jenny b_pull2 with dissolve
    pause
    show jenny b_pull3 with dissolve
    show jenny b_pull4 with dissolve
    show anon f_surprised
    anon "!!!"
    show jenny b_panties a_hips f_upset with dissolve
    jenny "Ayo berangkat!"

    show jenny f_grin_down b_naked a_panties_remove with dissolve
    anon f_worried "O-oke."

    show jenny b_naked_panties_remove_down with dissolve
    pause
    scene black with fade
    pause
    scene expression "backgrounds/location_home_jennybedroom_cutscene05.jpg" with dissolve
    jenny "Duduk saja di tempat tidur dan kenakan masker Anda."

    anon "Ya, aku mengerti."

    jenny "Dan jangan melepasnya!"

    anon "Ya, ya..."

    jenny "Saya serius, {b}[firstname]{/b}!"

    anon "Aku tidak akan melepas topengnya!"

    scene black with fade
    pause

    scene expression "backgrounds/location_home_jennybedroom_closeup_peek.jpg" with None
    $ M_jenny.set('cam show mask', True)
    show anon b_bed_jenny_sit f_shy_down of_mask
    show jenny o_under_body_laptop b_naked_bed_belly f_sexy_down
    with dissolve
    jenny "Ingatlah untuk tutup mulut dan biarkan aku menangani semuanya."

    anon @ f_worried "Ya {b}[jen_name]{/b}, saya mengerti."

    jenny @ f_eyeroll "Bagus, jangan lupakan itu!"

    pause
    jenny "Baiklah, ini dia."

    show jenny b_naked_bed_bellytype with dissolve
    pause
    show anon f_worried
    show jenny b_naked_bed_belly with dissolve
    jenny "Halo teman-teman!"

    pause
    jenny @ f_laugh "Hehe, aku juga merindukanmu."

    show anon f_shy_down
    pause
    jenny "Tidak, tentu saja aku tidak bercanda!"

    jenny "Dia duduk tepat di belakangku."

    pause
    jenny "Hmm, entahlah..."

    jenny "Itu tergantung pada seberapa banyak kalian memberi tip kepada saya."

    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"

    jenny @ f_laugh "Hehe, bagus sekali!"

    "{i}*PING*{/i} {i}*PING*{/i}"

    jenny "Kurasa kita harus melihat lebih dekat apa yang kubawa untuk kalian, ya?"

    show jenny o_laptop b_bed_side_laptop a_laptop with dissolve
    show anon f_worried
    pause
    jenny "Tidak, dia tidak punya nama..."

    pause
    jenny @ f_laugh "Haha, karena itu tidak penting!"

    pause
    jenny "Ya, dia sedikit gugup."

    show jenny b_bed_side f_upset with dissolve
    jenny "Apakah kamu sudah santai?!"

    jenny "Bukalah dan biarkan mereka melihat Anda!"

    anon "..."
    show anon b_bed_jenny_sit_back f_worried of_mask with dissolve
    pause
    show jenny f_normal
    jenny "Ini dia!"

    show jenny b_bed_side_laptop f_sexy_down with dissolve
    jenny "Lihat, dia pembelajar yang cepat."

    pause
    jenny "Oh, saya rasa Anda akan terkejut!"

    pause
    jenny "Baiklah, mari kita lihat, ya?"

    show jenny b_bed_side f_normal with dissolve
    jenny "Berbaring kembali."

    show anon b_bed_jenny_laying od_bed_jenny_laying_dick1 of_bed_jenny_laying_mask_X with dissolve
    pause
    show jenny a_pull1 with dissolve
    pause
    show anon od_empty
    show jenny a_pull2
    with dissolve
    pause
    show jenny f_upset a_point
    show anon od_bed_jenny_laying_dick2
    with dissolve
    jenny "Apakah kamu bercanda?"

    jenny "Kenapa kamu tidak keras?!"

    anon "Saya tidak dapat menahannya!"

    show jenny b_bed_side_laptop a_laptop f_sexy_down with dissolve
    jenny "{i}*Sigh*{/i} Tunggu sebentar kawan..."

    show jenny b_bed_side a_balls
    show expression "characters/anon/anon_overlay_dick_od_bed_jenny_laying_dick2.png"
    with dissolve
    anon "!!!"
    pause
    jenny "Ayo, kawan... Saatnya keluar dan bermain!"

    hide expression "characters/anon/anon_overlay_dick_od_bed_jenny_laying_dick2.png"
    show anon od_bed_jenny_laying_dick4
    with dissolve
    show anon od_bed_jenny_laying_dick5 with dissolve
    show anon od_bed_jenny_laying_dick6 with dissolve
    pause
    show jenny b_bed_side_laptop a_laptop with dissolve
    jenny "Lihat, sudah kubilang kalian tidak akan kecewa."

    pause
    jenny "Saya tahu benar!"

    pause
    jenny "Hehe, kalian harusnya sudah tahu sekarang, aku tidak akan menerima apa pun yang kurang dari itu..."

    pause
    jenny "Jadi, apa yang harus saya lakukan selanjutnya?"

    pause
    jenny "Tidak... Saya rasa tidak."

    pause
    jenny "Mmm, tidak..."

    pause
    jenny "Ya Tuhan, tidak mungkin Sam9..."

    jenny "Ini pertama kalinya dia tampil di depan kamera!"

    pause
    jenny "Ya baiklah..."

    jenny "Saya bisa melakukan itu."

    jenny "Tentu saja begitu saya melihat beberapa tipsnya."

    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"

    pause
    show jenny b_bed_side f_normal with dissolve
    jenny "Sepertinya ini hari keberuntunganmu..."

    $ M_jenny.set("sex speed",0.4)
    show jenny a_jerk f_sexy_down
    anon "!!!" with hpunch
    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"

    anon "Sialan!"

    jenny @ f_laugh "hehe!"

    pause
    anon "Rasanya luar biasa!"

    jenny "Duh."

    jenny "Apa, kamu pikir aku tidak tahu apa yang aku lakukan?"

    pause
    scene expression "backgrounds/location_home_jennybedroom_sex_hj.jpg" with None
    $ animated = True
    $ anim_toggle = True
    $ M_jenny.set('sex speed', .1)
    show jenny_hj_mc
    show expression AnimatedImage("jenny_hj", [1,2,3,4,5,4,3,2], M_jenny) as jenny_hj at Position(xalign = 0.0, yoffset = 0)
    jenny "Saya harap kalian menghargai menonton saya membelai BESAR ini..."

    jenny "BERDaging..."

    "{i}*PING*{/i} {i}*PING*{/i}"

    jenny "ayam."

    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"

    jump jenny_hj_loop

label button_jenny_come_back_camshow:
    show anon f_worried
    anon "Jadi tentang camshow itu denganku..."

    show jenny f_upset
    jenny "Sudah kubilang aku harus promosi dulu."

    jenny "{b}Kembalilah besok sore{/b}, bodoh!"

    hide anon
    hide jenny
    with dissolve
    return

label jenny_button_bought_mask:
    scene expression player.location.background_closeup with None
    show anon f_normal
    show jenny f_upset
    with dissolve
    jenny "Apakah kamu mengerti?"

    anon "Ya."

    show anon f_shy_down a_backpack
    pause
    show anon f_normal a_mask with dissolve
    anon "Bagaimana menurutmu?"

    show anon a_idle
    show jenny f_gross_down a_mask
    with dissolve
    jenny "Warnanya merah muda."

    show jenny f_gross_down
    anon "Jadi?"

    show jenny f_upset
    jenny "Itu agak feminin, bukan begitu?"

    anon f_worried "Apakah itu penting?"

    show jenny f_eyeroll
    jenny "Saya kira tidak."

    show jenny f_upset a_mask_throw
    show anon f_normal a_idle
    with dissolve
    anon "Jadi kapan kita mulai?"

    show jenny a_hips with dissolve
    jenny "Saya perlu berpromosi sedikit dulu."

    jenny "Kembalilah {b}besok sore{/b}, oke?"

    anon "Mengerti."

    show jenny f_angry
    jenny "Dan sebaiknya Anda menampilkan pertunjukan yang bagus!"

    jenny "Aku punya banyak hal untuk dilakukan dalam hal ini!"

    anon f_worried "O-oke."

    hide jenny with dissolve
    pause
    anon f_grin @ -m_talk "Saya kira {b}Saya akan kembali besok siang{/b} kalau begitu..."

    hide anon with dissolve
    return

label jenny_button_get_mask:
    scene expression player.location.background_closeup with None
    show anon f_worried
    show jenny f_upset
    with dissolve
    jenny "Apakah kamu mengerti?"

    anon "Apakah saya mendapatkan apa?"

    jenny "{b}Topengnya{/b}, bodoh?!"

    anon "Oh benar."

    anon f_shy "Tidak, saya masih mengerjakannya."

    jenny "Ugh, baiklah, keluarlah dari kamarku!"

    show anon f_worried
    hide jenny with dissolve
    pause
    show anon f_thinking a_thinking with dissolve
    anon @ -m_talk "(Hmm, aku ingin tahu apa yang dia rencanakan untuk streaming?)"

    pause
    anon "(Saya harus {b}mendapatkan masker{/b} jika saya ingin mengetahuinya... )"

    anon "(Saya harus {b}pergi ke mal dan mencarinya{/b}. )"

    hide anon with dissolve
    return

label jenny_button_talked_to_cedric:
    if player.location == L_home_diningroom:
        scene expression game.timer.image("dining_room{}")
        show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 3
        show anon b_dinner_sitting_look_left f_worried a_resting zorder 2
    else:
        scene expression player.location.background_closeup with None
        show anon f_worried zorder 2
    show jenny f_upset b_magic_sit_stand_dressed a_idle zorder 1
    with dissolve
    jenny "Apakah Anda sudah berbicara dengan {b}Cedric{/b}?"

    anon "Ya."

    pause
    anon @ -m_talk "..."
    jenny "Ya?"

    jenny "Kenapa dia belum meneleponku kembali?!"

    anon "Dia tidak akan meneleponmu kembali."

    jenny "Apa?!"

    anon @ f_skeptical "Dia berkata, dan saya kutip, \"Saya tidak ingin berurusan dengan wanita jalang gila itu.\""

    show jenny a_magic_sit_stand_crossed with dissolve
    jenny "Kamu serius?"

    anon "Mmmhmm."

    pause
    anon "Maaf."

    show jenny f_angry
    jenny "Kalau begitu, persetan dengannya!"

    show jenny a_magic_sit_stand_phone f_phone_upset with dissolve
    jenny "Bajingan bodoh."

    pause
    anon @ -m_talk "..."
    show jenny f_angry a_idle with dissolve
    jenny "Grr!!!"

    hide jenny with dissolve
    pause
    anon "... Oke."

    anon @ -m_talk "(Saya mungkin harus memberinya ruang sampai dia tenang.)"

    hide anon with dissolve

    return

label button_jenny_talk_to_cedric:
    show anon f_worried
    anon "Di mana Anda bilang saya bisa menemukan {b}Cedric{/b}?"

    show jenny f_upset
    jenny "Dia mungkin akan berada di {b}Gym{/b}."

    jenny "Orang bodoh itu selalu ada di {b}Gym{/b}."

    anon "Baiklah, aku sedang mengerjakannya."

    hide anon
    hide jenny
    with dissolve
    return

label button_jenny_has_toy_electroclit:
    scene expression player.location.background_closeup with None
    show anon f_normal
    show jenny
    with dissolve
    anon "Aku punya mainanmu."

    show jenny f_upset
    jenny "Sudah waktunya!"

    show anon a_backpack f_shy_down
    pause
    show anon f_normal a_toy1 with dissolve
    anon "Ini dia, kan?"

    jenny "Biar kulihat itu!"

    return

label button_jenny_has_toy_electroclit_submissive:
    show anon f_surprised a_idle
    show jenny f_gross_down a_hips_toy2
    with dissolve
    jenny "..."
    show jenny f_angry
    jenny "Ini adalah Cahaya Klitoris Elektro!"

    anon f_worried "Apakah itu hal yang buruk?"

    jenny "Ya, itu hal yang buruk!"

    jenny "Seberapa bodohnya kamu?"

    anon "aku tidak-"

    jenny "Tidak mungkin hal ini akan membuatku lepas kendali!"

    jenny "Kenapa kamu tidak memberiku model aslinya, idiot?!"

    anon f_tired "Mereka terjual habis..."

    show jenny f_upset
    jenny "Ya benar. Tentu saja."

    show jenny f_angry
    anon f_worried "aku serius!"

    show jenny f_upset a_crossed with dissolve
    jenny "Saya berpikir, kesepakatannya batal..."

    anon "Apa?! Ayolah {b}[jen_name]{/b}, saya menghabiskan banyak uang untuk itu!"

    jenny "Itu bukan masalahku."

    anon b_dressed_bow "Silakan?"

    show jenny f_surprised
    jenny "!!!"
    show jenny f_grin
    jenny "Oh, aku suka itu... Mohon lagi!"

    anon b_dressed "Dengan serius?"

    jenny "Mohon atau kesepakatannya batal."

    anon b_dressed_bow "{i}*Huh*{/i} Tolong, bolehkah aku melihatmu telanjang?"

    jenny "Kamu harus berkata, \"Aku pecundang kecil yang menyedihkan dan aku akan menjadi perawan selamanya.\""

    anon b_dressed f_skeptical "Apa?! aku tidak akan-"

    show anon f_surprised
    show jenny f_angry
    jenny "Lakukan atau keluar!"

    anon f_depressed "..."
    anon "Aku pecundang kecil yang menyedihkan dan aku akan menjadi perawan selamanya."

    show jenny f_laugh
    jenny "Hahahahaha!"

    show anon f_sad
    show jenny f_grin
    jenny "Baiklah, selama kamu mengakuinya."

    jenny "Saya kira Anda telah mendapatkan hadiah."

    show jenny f_upset b_pull1 with dissolve
    show anon f_normal
    jenny "Anda hanya mencari satu menit saja!"

    show jenny b_pull2 with dissolve
    jenny "Membawakanku mainan jelek bodoh ini..."

    show jenny b_pull3 with dissolve
    show jenny b_pull4 with dissolve
    pause
    show jenny b_naked a_panties_remove f_normal_low with dissolve
    pause
    show jenny b_naked_panties_remove_down with dissolve
    pause
    show jenny f_grin a_hips b_naked with dissolve
    jenny "Ini dia, mesum."

    anon f_surprised "!!!"
    show anon f_flirt_low
    show jenny f_upset
    jenny "Cobalah untuk tidak ngiler di permadani saya."

    show jenny f_gross
    anon f_flirt "W-wow, kamu bercukur di bawah sana..."

    show anon f_flirt_low
    show jenny f_upset
    jenny "Tidak apa-apa?"

    jenny "Hanya wanita-wanita tua dan pecundang yang membiarkan kotoran mereka tumbuh liar."

    pause
    show jenny f_grin
    jenny "Apakah ini vagina pertama yang pernah Anda lihat?"

    show anon f_skeptical a_behind_head with dissolve
    anon "Sebenarnya aku-"

    show anon f_flirt_low
    show jenny f_eyeroll
    jenny "Ya, tentu saja. Pertanyaan bodoh untuk ditanyakan."

    show jenny f_grin
    show anon a_idle with dissolve
    jenny "Ini mungkin juga yang terakhir Anda lihat."

    jenny "Pecundang."

    pause
    show jenny f_upset
    jenny "Baiklah, waktunya habis!"

    anon f_worried "Aduh, ayolah {b}[jen_name]{/b}... Sedikit lagi!"

    show jenny f_angry
    jenny "Tidak!"

    show jenny f_upset
    jenny "Mengacaukan seperti Anda tidak bisa meminta lebih banyak!"

    jenny "Lain kali, lakukan apa yang saya perintahkan!"

    anon "{i}*Huh*{/i} Baik."

    show anon f_flirt_low
    pause
    show jenny f_angry
    jenny "Sekarang keluar!"

    hide anon
    hide jenny
    with dissolve
    $ player.go_to(L_home_hallway)
    scene expression player.location.background_closeup with None
    show anon f_confused with dissolve
    anon @ -m_talk "(Sheesh, itu merendahkan...)"

    show anon
    anon @ f_grin -m_talk "(Tapi aku harus melihatnya telanjang.)"

    anon f_flirt_grin @ -m_talk "(Jadi, menurutku itu sepadan?)"

    pause
    show anon f_thinking a_thinking with dissolve
    anon @ -m_talk "(Aku ingin tahu apa yang dia rencanakan demi uang sekarang?)"

    hide anon with dissolve
    return

label button_jenny_has_toy_electroclit_dominant:
    show jenny a_hips_asking f_upset
    show anon a_toy1_protect f_snarky
    with dissolve
    anon "Ah, ah!"

    anon "Kita sudah sepakat, ingat?"

    show jenny a_hips f_angry with dissolve
    jenny "..."
    anon @ f_skeptical "Pakaianmu sedikit berlebihan, bukan?"

    show jenny f_eyeroll
    jenny "{i}*Huh*{/i} Baik."

    show jenny b_pull1 f_grin_down with dissolve
    pause
    show jenny b_pull2 with dissolve
    pause
    show anon f_flirt_low
    show jenny b_pull3 with dissolve
    show jenny b_pull4 with dissolve
    pause
    show jenny b_naked a_panties_remove f_grin_down with dissolve
    pause
    show jenny b_naked_panties_remove_down with dissolve
    pause
    show jenny b_naked f_upset a_hips with dissolve
    jenny "Di sana."

    jenny "Sekarang biarkan aku melihatnya!"

    anon f_flirt "Baiklah, ini mainanmu."

    show jenny f_gross_down a_hips_toy2
    show anon a_idle
    with dissolve
    pause
    show jenny f_gross_down
    jenny "Hei, ini versi ringannya..."

    show jenny f_angry
    jenny "Saya ingin yang asli!"

    anon "Maaf, hanya itu yang mereka punya."

    jenny "Ya ampun {b}[firstname]{/b}!"

    jenny "Hal ini tidak akan pernah membuatku lepas kendali!"

    anon "Seperti yang kubilang tadi, hanya itu yang mereka punya."

    anon "Percayalah, Anda beruntung mendapatkannya."

    anon "Saya harus melewati beberapa rintangan untuk mendapatkannya."

    anon "Sekarang berhentilah mengomel, kamu merusak ini untukku!"

    show anon f_flirt_low
    show jenny f_eyeroll
    jenny "Ah, terserah..."

    show jenny f_upset a_hips with dissolve
    anon @ f_flirt "Aku sangat suka kamu bercukur di bawah sana..."

    show jenny f_happy_down
    jenny "K-kamu yakin?"

    show jenny f_angry
    jenny "Maksudku, diamlah!"

    jenny "Aku tidak peduli apa yang kamu suka, pecundang!"

    show jenny f_angry_pouting
    anon @ f_flirt "Jika kamu berkata begitu..."

    pause
    show anon o_boner with dissolve
    show jenny f_surprised_down
    jenny "!!!"
    jenny "Apakah itu-"

    anon @ -m_talk "Hmm?"

    anon f_flirt "Oh maaf."

    anon "Aku tidak terbiasa-"

    anon "Yah, kamu benar-benar seksi, tahu?"

    jenny "Itu tidak mungkin penismu..."

    anon "Eh, ya?"

    show anon f_grin
    show jenny f_upset
    jenny "Tidak mungkin!"

    jenny "Ini huh-"

    show jenny f_surprised_down_back a_shocked m_talk with dissolve
    pause
    anon f_flirt "Itu apa?"

    show anon f_grin
    show jenny f_angry a_hips -m_talk with dissolve
    jenny "Tidak ada apa-apa."

    jenny "Apakah kita sudah selesai di sini?"

    anon f_flirt "Ya, saya rasa itu sudah cukup."

    show anon f_flirt_low
    show jenny f_eyeroll
    jenny "Terima kasih Tuhan."

    show jenny f_upset
    anon @ f_flirt "Apakah kamu tersipu?"

    show jenny f_angry
    jenny "T-tidak!"

    jenny "Keluar!"

    anon f_flirt "Ya, ya... aku pergi."

    $ player.go_to(L_home_hallway)
    scene expression player.location.background_closeup with None
    show anon f_flirt o_boner with dissolve
    anon @ -m_talk "(Yah, itu panas sekali!)"

    anon @ -m_talk "(Sepertinya dia benar-benar meresponsku saat aku bersikap tegas padanya dan tidak menerima omong kosongnya.)"

    pause
    anon @ -m_talk "(Aku ingin tahu apa yang dia rencanakan untuk mendapatkan uang?)"

    hide anon with dissolve
    return

label button_jenny_get_toy_electroclit:
    show anon f_worried
    anon "Mainan apa yang kamu ingin aku belikan untukmu lagi?"

    show jenny f_upset
    jenny "Apakah kamu lupa atau apa?!"

    anon "T-tidak, aku tidak untuk-"

    pause
    anon f_skeptical "Uh, katakan saja padaku!"

    jenny "Kamu tidak berharga, kamu tahu itu?"

    show jenny f_gross
    show anon f_worried
    pause
    show jenny f_upset
    jenny "{b}Pergi ke Pink di lantai dua mall{/b}, dan {b}cari Electro Clit{/b}."

    anon "Baiklah."

    jenny "Apakah aku perlu menulisnya terbalik di dahimu agar kamu tidak lupa lagi?"

    anon f_brag_closed "Tidak, aku mendapatkannya kali ini."

    show anon f_normal
    show jenny f_eyeroll
    jenny "Psh, ya benar."

    show jenny f_upset
    return

label jenny_dialogue_make_a_deal:
    menu:
        "payudara.":

            if M_jenny.get("dominance") <= 0:
                show anon f_worried
                anon "Bolehkah aku melihat payudaramu?"

                show jenny f_upset
                jenny "Saya tidak tahu, apakah Anda punya dua ratus dolar?"

                if player.has_money(200):
                    anon f_normal "Ya."

                    jenny @ f_eyeroll "{i}*Huh*{/i} Baiklah, serahkan."

                    show anon a_money with dissolve
                    pause
                    show anon a_idle
                    show jenny f_grin_down a_money_counting b_dressed
                    with dissolve
                    pause
                    show jenny f_upset
                    $ player.spend_money(200)
                    jump repeat_boobies
                else:
                    jump player_no_money
            else:
                show anon f_worried
                anon "Bolehkah aku melihat payudaramu?"

                show jenny f_upset
                jenny "Saya tidak tahu, apakah Anda punya dua ratus dolar?"

                if player.has_money(200):
                    $ player.spend_money(200)
                    anon "Ya."

                    jenny "{i}*Huh*{/i} Baiklah, serahkan."

                    jump jenny_bedroom_jenny_go_to_her_room_dominant_has_money
                else:
                    anon "Aku bahkan tidak punya dua ratus!"

                    jenny "Yah, aku tidak akan menunjukkan payudaraku padamu dengan harga kurang dari dua ratus."

                    jenny "Jadi sebaiknya Anda pergi dan mengambilnya jika Anda ingin melihat hal-hal ini..."

                    anon f_tired "{i}*Huh*{/i} Baik."

                    anon "{b}Saya akan kembali dengan uangnya{/b}."

                    jenny "Cepatlah, pecundang."

                    jenny "Saya butuh uang itu!"

                    anon "Ya, ya."

                    hide anon
                    hide jenny
                    with dissolve
        "Sudahlah.":
            label player_no_money:
            show anon f_worried
            anon "Sudahlah."

            show jenny f_upset
            jenny "Berhenti main-main, {b}[firstname]{/b}!"

            jenny "Jika Anda tidak punya uang, keluarlah."

            anon f_skeptical "Bagus."

            hide anon
            hide jenny
            with dissolve
    return

label jenny_dialogue_roxxy_pre:
    anon f_worried "Jadi, tentang rutinitas {b}Roxxy{/b}..."

    show jenny f_upset
    jenny "Apakah Anda {b}membawa uang{/b}?"

    return

label jenny_dialogue_roxxy_pay:
    anon f_skeptical "Di Sini."

    show anon a_money with dissolve
    pause
    if M_jenny.pregnancy.stage > 1:
        show jenny f_grin
    else:
        show jenny f_grin a_money
    show anon a_idle
    with dissolve
    jenny "Sempurna."

    jenny "Beritahu {i}Siapa Nama{/i} dia bisa datang menemuiku sepulang sekolah besok."

    anon f_skeptical "Namanya {b}Roxxy{/b}."

    show jenny f_gross
    jenny "Apa pun."

    return

label jenny_dialogue_roxxy_do_not_pay:
    anon f_worried "Saya belum memilikinya."

    show jenny f_upset
    jenny "Kalau begitu, kalahkan saja, aku sedang sibuk."

    return

label jenny_button_old_photo:
    anon f_worried a_backpack "Aku punya sesuatu untukmu."

    show anon a_box_attic_pic2_look with dissolve
    jenny f_normal @ -m_talk "Hmm?"

    anon a_box_attic_pic2_give "Di Sini."

    pause
    show anon a_idle
    show jenny a_attic_box_pic1 f_gross
    with dissolve
    pause
    jenny f_sad a_attic_box_pic1_sad "Dimana kamu menemukan ini?"

    anon "Benda itu ada di dalam kotak berisi barang milik {b}Ayah{/b} yang polisi berikan kembali kepada kami."

    anon "Dia pasti menyimpannya di meja kerjanya."

    jenny @ -m_talk "..."
    pause

    if M_jenny.finished_state(S_jenny_cheerleader_sex):
        anon f_shy "Apakah kamu ingat hari itu?"

        jenny f_normal_low "Ya."

        pause
        jenny "{b}Frank{/b} memberi kami permen kapas, yang biru dan merah muda..."

        anon f_worried "Tunggu, apa?"

        jenny f_happy "... Tapi kamu ingin terus menaiki bianglala dengan {b}[deb_name]{/b} jadi dia membiarkanku memakan keduanya."

        anon f_shy "Saya tidak mengetahuinya."

        jenny @ f_laugh "Anda tidak ingat saya memuntahkan semuanya di mobil dalam perjalanan pulang?"

        jenny "Warnanya bercampur dan hasilnya ungu."

        anon f_normal "Oh ya!!"

        anon @ f_laugh "Heh, itu yang kamu dapat dengan memakan permenku!"

        jenny @ f_laugh "Terserahlah, kalian menaiki bianglala bodoh itu sebanyak dua belas kali... Kami menunggu selamanya!"

        anon @ a_point_back "Apa yang bisa saya katakan, saya suka kincir ria..."

        jenny f_normal_low @ f_eyeroll "Kamu konyol."

        pause
        jenny "Itu adalah hari yang baik."

        pause
        show jenny f_sad
        pause
        anon f_confused "Kenapa kamu menatapku seperti-"

        show anon b_empty f_surprised
        show jenny b_dressed_hug_mc1 behind anon
        with dissolve
        anon "!!!"
        pause
        jenny "Terima kasih... Untuk umm..."

        jenny "... Memberiku ini."

        pause
        show jenny b_dressed_hug_mc2
        anon f_shy_low "Y-ya, tidak masalah."

        pause
        show anon b_dressed f_shy
        show jenny b_dressed f_normal_low:
            flip
            xoffset 500
        with dissolve
        jenny "Aku perlu mencari tempat untuk menaruhnya."

        anon @ a_behind_head "Y-ya, oke."

        hide jenny with dissolve
        anon "Aku hanya akan, umm... Biarkan saja... Kurasa."

        pause
        anon "... Benar."

        anon "Sampai jumpa nanti."

        hide anon with dissolve

        $ player.go_to(L_home_hallway)
        scene expression background(360, 360, 4.) as stage with fade
        show anon with dissolve:
            flip
            xoffset -200
        anon @ -m_talk "(Yah, itu tidak terduga...)"

        pause
        anon f_grin @ -m_talk "( Mungkin segalanya mulai membaik antara {b}[jen_name]{/b} dan saya? )"

    else:
        anon "Saya pikir Anda mungkin menginginkannya?"

        jenny f_upset "Mengapa saya menginginkan ini?"

        anon "Umm, karena itu menggambarkan kenangan indah tentangmu dan ayahku?"

        jenny @ f_eyeroll "Cih, itu bodoh..."

        anon f_unimpressed @ -m_talk "..."
        anon a_reach "Baiklah, berikan kembali."

        show jenny with dissolve:
            xoffset 50
        jenny "Apa, tidak!"

        jenny "Itu milikku!"

        anon f_surprised a_idle "Tapi kamu baru saja mengatakan-"

        jenny a_idle "Diam!"

        anon f_unimpressed "Terkadang kamu sangat aneh..."

        jenny f_angry @ a_point_out "Keluar dari kamarku!"

        anon f_worried "Dengan serius?!"

        jenny "{b}[deb_name]{/b}!!!"

        anon f_angry "Baiklah, aku pergi... Astaga!"

        anon "Aku hanya mencoba melakukan sesuatu yang baik untukmu..."

        hide anon with dissolve
        pause .6
        show jenny a_sides f_sad with dissolve
        pause
        show jenny a_attic_box_pic1_sad f_sad_down with dissolve:
            flip
            xoffset 500
        pause

        $ player.go_to(L_home_hallway)
        scene expression background(360, 360, 4.) as stage with fade
        show anon f_unimpressed with dissolve:
            flip
            xoffset -200
        anon @ -m_talk "(Yah, aku sama sekali tidak mengharapkan hal itu terjadi...)"

        show anon f_surprised
        jenny "{i}*Mengendus*{/i}"

        anon f_worried @ -m_talk "(Tunggu sebentar.)"

        show anon:
            unflip
            xoffset 300
        pause
        anon @ -m_talk "(Apakah dia... Menangis?)"

        jenny "{i}*Suara isakan*{/i}"

        anon f_surprised "Hah."

        pause
        anon f_thinking a_thinking @ -m_talk "( I guess she didn't want me to see her upset. )"

        anon @ -m_talk "( Typical {b}[jen_name]{/b}. )"


    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
