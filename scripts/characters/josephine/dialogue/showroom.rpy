label josie_button_showroom:
    show josephine b_dressed_bored
    show anon f_worried_low with dissolve

    if M_anon.finished_state(S_ano09_blow):
        anon "{b}Yosephine{/b}?"

        show josephine b_dressed f_sexy
        show anon f_normal
        with dissolve
        josephine "Hai, {b}[firstname]{/b}."

        josephine "Anda di sini untuk menemani saya?"

    else:
        anon "Permisi?"

        josephine "..."
        anon "{b}Yosephine{/b}?"

        josephine "..."
        anon "HALO?!"

        show josephine b_dressed f_bored a_phone
        show anon f_skeptical
        with dissolve
        josephine @ -m_talk "Hmm?"

        josephine "Itu kamu."

        josephine f_normal_down "Ada apa?"


    label josie_button_showroom.choice:
    menu:
        "Beli kendaraan." if M_anon.is_state(S_ano05_sale):
            jump ano05_sale_josie.anon

        "Foto pribadi." if M_anon.between_states(S_ano07_mech, S_ano07_give):
            jump ano07_hint_josie

        "Beli kendaraan." if M_anon.is_state(S_ano07_sale):
            jump ano07_sale_josie.anon

        "Beli kendaraan." if M_anon.is_state(S_ano09_sale):
            jump ano09_sale_josie.anon

        "Bagaimana kabar pekerjaannya?" if M_anon.finished_state(S_ano05_sale):
            jump josie_button_showroom.work

        "Selfie telanjang?" if M_anon.finished_state(S_ano07_perk):
            jump josie_button_showroom.nudes

        "Rusia?" if M_anon.finished_state(S_ano09_brat) and not M_josie.finished_state(S_jos01_find):
            jump josie_button_showroom.russians

        "Apakah kamu tidak punya passion?" if not M_anon.finished_state(S_ano09_blow):
            jump josie_button_showroom.passion
        "Kamu ingin bermesraan?":

            if M_anon.finished_state(S_ano09_blow):
                jump josie_button_showroom.kiss
            jump josie_button_showroom.flirt

        "Seks oral?" if M_anon.finished_state(S_ano09_blow):
            jump josie_button_showroom.blowjob

        "Seks." if M_josie.finished_state(S_jos02_init):
            jump josie_button_showroom.sex

        "{b}Kim{/b}." if M_kim.state is None:
            jump josie_button_showroom.kim

        "{b}Kim{/b}." if M_kim.state is not None:
            jump josie_button_showroom.yoyo
        "Sudahlah.":

            pass

    if M_anon.finished_state(S_ano09_blow):
        anon f_normal @ a_wave "Saya akan menemuimu nanti, {b}Josephine{/b}."

        josephine f_normal "Nanti, {b}[firstname]{/b}."

    else:
        anon f_normal @ a_wave "Saya akan menemuimu nanti, {b}Josephine{/b}."

        josephine "Nanti, potong mangkuk."

        show anon f_unimpressed
        pause

    hide anon with dissolve
    return


label josie_button_showroom.blowjob:
    anon f_flirt @ -m_talk "..."
    josephine f_concerned @ -m_talk "..."
    pause
    josephine f_sexy @ f_eyeroll "Baiklah baiklah."

    anon @ f_laugh "Manis!"

    pause
    josephine "Anda masih memiliki rompi itu?"

    anon "Saya bersedia."

    josephine "Baiklah, pakailah dan datanglah ke belakang meja."

    anon f_worried "Tunggu sebentar, bisakah kita ke kamar mandi atau apalah?"

    josephine "Di mana kesenangannya?"

    anon @ -m_talk "..."
    josephine "Ayo cepat."

    anon "Oke oke..."


    call scene_josie_blowjob.repeat from josie_button_showroom.blowjob_resume
    $ unlock_scene('josie', '01_unlocked')

    call josie_button_stage
    show anon b_jacket f_flirt_low behind josephine:
        flip
    show josephine b_dressed:
        flip
        offset (400, 300)
    with fade
    anon "Fiuh."

    anon "Itu luar biasa!"

    show anon f_flirt with dissolve:
        xoffset 100
    show josephine f_sexy o_cum with dissolve:
        offset (350, 0)
    pause
    josephine @ a_fingerlick "Asin."

    josephine "Ya, itu pengalihan yang menyenangkan."

    anon @ f_laugh "Hehe, ya."

    anon f_worried @ a_schmutz "Kau tahu, kau punya sesuatu yang kecil..."

    josephine "Ya, tidak apa-apa."

    josephine "Kawan, kamu selalu mendapatkan sperma dalam jumlah yang gila-gilaan!"

    anon f_flirt "Maaf."

    pause
    anon f_worried "Apakah kamu ingin aku mengambilkanmu handuk atau apa?"

    josephine "Tidak, aku akan meninggalkannya untuk sementara waktu."

    anon f_surprised "Benar-benar?"

    josephine "Ya, lucu melihat reaksi pelanggan."

    anon @ -m_talk "..."
    anon f_worried "Kamu gadis yang aneh, kamu tahu itu?"

    josephine @ f_laugh "Haha!"

    hide anon with dissolve
    return 'blowjob'


label josie_button_showroom.flirt:
    anon f_flirt "Kamu ingin bermesraan?"

    josephine f_pouting "Eww, tidak."

    anon f_worried "Apa?"

    anon "Kita melakukannya sebelumnya, bukan?"

    josephine f_normal "Ya, tapi itu untuk suatu tujuan..."

    josephine "Saya mencoba untuk dipecat, ingat?"

    anon f_flirt @ f_laugh "Jadi, kita bisa mencobanya lagi!"

    anon "Apa yang kamu katakan?"

    josephine f_normal_down "Bagaimana kalau tidak."

    anon f_worried "Aww, ayolah... Tak seorang pun pernah dipecat hanya dengan duduk-duduk sambil melihat ponselnya sepanjang hari."

    show josephine f_concerned
    pause
    anon f_shy "Baiklah, jadi mungkin banyak orang dipecat karena melakukan hal itu."

    anon @ f_laugh "Tapi menurut saya Anda bisa melakukannya jauh lebih baik!"

    show josephine f_normal_down
    pause
    anon f_worried "Mungkin hanya sedikit?"

    josephine @ f_angry_down "Bermimpilah, potong mangkuk."

    anon f_unimpressed "Uh, baiklah."

    jump josie_button_showroom.choice


label josie_button_showroom.kim:
    anon f_worried "Ada apa dengan pria {b}Kim{/b} itu?"

    josephine "Dia kano yang bodoh."

    josephine "Itulah yang terjadi padanya."

    anon "Bagaimana dia mempertahankan pekerjaannya?"

    josephine @ f_eyeroll "Dia memiliki banyak pelanggan tetap yang membeli mobil mahal dalam jumlah yang mengejutkan."

    anon f_surprised "Benar-benar?"

    josephine "Termasuk {b}Pantat Walikota{/b}."

    anon f_surprised @ f_shock "Walikota membeli mobilnya di sini?"

    josephine "Ya."

    josephine "Dan dia secara khusus meminta {b}Kim{/b}, setiap saat."

    anon f_confused "Mengapa?"

    josephine f_normal "Oh, Anda belum pernah melihat seperti apa dia di sekitar pelanggan pilihannya."

    josephine "Dia berubah menjadi orang yang hidung coklat terbesar di planet ini."

    show anon f_worried
    josephine f_normal_down "Itu menjijikkan."

    anon "Saya bisa membayangkan."

    pause
    anon f_unimpressed "Ugh, aku benci pria itu."

    jump josie_button_showroom.choice


label josie_button_showroom.kiss:
    anon f_flirt "Kamu ingin bermesraan?"

    josephine f_concerned "Bercumbu?"

    pause
    josephine "Bukankah Anda lebih suka melakukan sesuatu yang lebih menyenangkan?"

    anon @ f_laugh "Menurutmu berciuman itu tidak menyenangkan?"

    josephine @ f_eyeroll "Maksudku, kurasa..."

    anon "Lebih menyenangkan daripada duduk di sini seharian bosan, bukan?"

    josephine "BENAR."

    pause
    josephine f_sexy "Baiklah, persetan."

    anon "Luar biasa!"

    anon "aku tahu kamu-"

    show josephine b_dressed_kiss_lips:
        xoffset -300
    hide anon
    anon "!!!" with hpunch
    pause
    show anon f_surprised behind josephine
    show josephine b_dressed f_angry a_gimme
    with dissolve
    josephine "Ayo kawan, perbanyak lidah!"

    anon f_worried "M-maaf."

    show josephine b_dressed_kiss:
        xoffset -300
    hide anon
    with dissolve
    pause
    show anon f_shy
    show josephine b_dressed f_laugh -a_gimme:
        xoffset 0
    with dissolve
    josephine "Lumayan, potongan mangkuk."

    anon f_unimpressed a_sides "Serius, kamu masih memanggilku potongan mangkuk?!"

    josephine f_sexy "Heh, potong rambut dan aku akan berhenti."

    anon a_idle "Sangat lucu."

    jump josie_button_showroom.choice


label josie_button_showroom.nudes:
    anon f_normal @ f_confused "Apa sih yang dilakukan selfie telanjang itu di ponselmu?"

    josephine f_bored "{i}*Huh*{/i} Saya lebih suka tidak mengatakannya."

    anon "Ah, ayolah... Tidak ada yang perlu dipermalukan."

    josephine @ f_eyeroll "Uh, baiklah."

    josephine "Saya mencoba masuk ke dalam video game."

    anon f_confused "Hah?"

    josephine "Ya, ada orang yang membuat video game crowdfunded dan mengalirkan dirinya sendiri untuk menggambar karya seninya."

    josephine "Namanya adalah {b}DarkCookie{/b}."

    josephine "Aku mengawasinya sepanjang waktu saat istirahat makan siang."

    anon "Oh oke?"

    anon "Apa hubungannya dengan selfie telanjang?"

    josephine "Ya, dia mengadakan kontes di mana dia menawarkan untuk memasukkan orang ke dalam permainannya jika mereka mengiriminya gambar payudara atau penis mereka dengan tulisan, \"I Love Summertime Saga.\""

    anon f_surprised "Sungguh?"

    josephine "Ya."

    josephine "Dia pria yang aneh."

    anon f_sad_down a_facepalm "Kedengarannya seperti itu."

    pause
    anon f_worried a_idle "Jadi kamu mengirimkan foto-foto itu padanya?"

    josephine "Tidak, saya tidak bisa melakukannya."

    anon "Kenapa tidak?"

    josephine "Aku ketakutan, oke?!"

    anon f_normal @ f_laugh "Kamu ketakutan?!"

    josephine "Diam, kamu juga akan ketakutan!"

    anon "Ya, mungkin..."

    anon "Aku hanya terkejut saja."

    josephine "Mengapa demikian?"

    anon f_flirt "Yah, berbicara sebagai seseorang yang telah melihat sekilas apa yang kamu sembunyikan di balik pakaian itu..."

    josephine "Jangan menyeramkan."

    anon "Heh, aku hanya bilang... Tidak ada yang perlu membuatmu malu."

    josephine @ -m_talk "..."
    anon "Kamu cantik."

    josephine "Ya, baiklah..."

    josephine "Terima kasih, kurasa."

    anon @ a_point "Terima kasih kembali."

    josephine "Bisakah saya kembali tidak bekerja sekarang?"

    jump josie_button_showroom.choice


label josie_button_showroom.passion:
    anon f_normal "Apakah kamu tidak punya passion?"

    josephine "Pertanyaan macam apa itu?"

    anon "Entahlah."

    anon "Saya hanya mencoba mencari tahu jenis pekerjaan apa yang lebih cocok untuk Anda..."

    josephine @ f_eyeroll "Umm, coba apa saja?"

    anon "Ayolah, serius... Apa passionmu?"

    josephine @ f_angry "Ah, aku tidak tahu."

    josephine "Sepertinya aku suka pakaian..."

    anon "Oke, itu permulaan."

    josephine "Dan sepatu."

    anon "Apa lagi?"

    josephine f_sexy "Oh, saya suka menonton video di internet dan mengolok-olok orang di bagian komentar."

    anon f_skeptical @ -m_talk "..."
    anon "Ya, saya tidak yakin itu keterampilan yang dapat dipasarkan..."

    show anon f_normal
    josephine f_normal_down "Ya, seharusnya begitu!"

    josephine "Dibutuhkan banyak kerja keras untuk mencapai level trolling saya."

    anon "saya yakin."

    jump josie_button_showroom.choice


label josie_button_showroom.russians:
    anon f_worried "Ngomong-ngomong, apakah Anda pernah punya pelanggan Rusia di sini?"

    josephine f_normal "Ya, sebenarnya cukup banyak..."

    josephine "Bagaimana kamu tahu tentang itu?"

    anon "Ehh, anggap saja itu firasat..."

    josephine f_concerned "Oh oke."

    pause
    anon "Bisakah Anda ceritakan sesuatu tentang mereka?"

    josephine f_normal "Mereka membeli banyak mobil dari kami..."

    josephine @ f_surprised "Seperti, banyak sekali!"

    anon @ f_confused "Benar-benar?"

    josephine "Ya."

    josephine @ a_feigning "Selalu hitam juga."

    josephine "Kecuali untuk kali terakhir ini, mereka membawa seorang gadis muda yang menginginkan Baudi B5 berwarna gunmetal dan kemudian membuat ulah ketika kami tidak memilikinya."

    josephine f_bored "Kotoran kecil yang manja."

    anon "Apakah Anda punya nama atau alamat untuk mereka?"

    josephine "Entahlah, mungkin."

    josephine f_normal "{b}Kim{/b}-lah yang selalu berurusan dengan mereka, mereka adalah pelanggannya."

    $ M_kim.set('russians', True)
    anon f_unimpressed "Oh bagus."

    josephine "Anda dapat mencoba berbicara dengannya tentang hal itu?"

    anon "Ya, itu akan bagus, aku yakin..."

    josephine f_sexy @ f_laugh "Hehe."

    jump josie_button_showroom.choice


label josie_button_showroom.sex:
    if game.timer.is_day():
        anon f_shy "Ingin berhubungan seks?"

        josephine f_sexy "Ya, ya!"

        josephine "{b}Temui aku di ruang istirahat{/b} dalam lima menit."

        hide josephine with {'master': dissolve}
        anon f_laugh "Baiklah."

    else:
        anon f_shy "Ingin berhubungan seks?"

        josephine f_sexy "Ya, ya!"

        josephine "{b}Temui aku di kantor ayahku{/b} dalam lima menit."

        anon f_worried "Tunggu sebentar."

        anon "Menurutmu itu ide yang bagus?"

        josephine "Jangan khawatir, dia sedang sibuk menutup sini."

        josephine "Dia tidak akan mengganggu kita."

        anon "Entahlah..."

        josephine "Ayolah, ini membuatku sangat seksi!"

        josephine "Silakan?!"

        pause
        anon "Baiklah, usahakan jangan terlalu berisik, oke?"

        josephine "Berhentilah khawatir!"

        josephine "Ayo."

        hide josephine with {'master': dissolve}
        anon @ a_point "saya-"

        anon "Sudahlah."

    hide anon with dissolve
    return 'sex'


label josie_button_showroom.work:
    anon f_normal "Bagaimana kabar pekerjaannya?"

    josephine @ f_eyeroll "Ugh, menurutmu bagaimana kelanjutannya?"

    anon "Sama seperti biasanya ya?"

    josephine "Pekerjaan ini sama menariknya dengan perjalanan ke praktik dokter gigi."

    anon "Anda tahu, menurut saya hal itu tidak terlalu buruk."

    josephine "Setidaknya aku mendapatkan ponselku kembali sekarang."

    anon "Ya, sama-sama untuk itu..."

    josephine "Hei, sepertinya aku ingat kamu mendapat imbalan yang pantas!"

    anon f_flirt "Ya, diskonnya bagus."

    show josephine f_surprised m_talk
    pause
    josephine f_angry "Heeeey!"

    show josephine a_crossed -m_talk with dissolve
    anon f_normal @ f_laugh "Hahahaah!"

    anon "Saya hanya bercanda."

    josephine "Yah, itu tidak lucu."

    show josephine f_normal_down a_phone with dissolve
    jump josie_button_showroom.choice


label josie_button_showroom.yoyo:
    anon f_worried "Ada apa dengan {b}Kim{/b} yang baru itu?"

    josephine f_normal "Oh, kamu bertemu dengannya, ya?"

    anon "Ya."

    anon f_confused "Bagaimana bisa ada dua di antaranya?"

    josephine f_laugh "Hehehe!"

    anon "Maksudku, serius..."

    anon "... Mereka persis sama."

    josephine f_normal "Setidaknya yang baru tidak berbau busuk."

    anon f_happy "Heh, ya... Kurasa itu sesuatu."

    pause
    anon f_confused "Berhati-hatilah saat berada di dekatnya, ya?"

    anon f_worried "Dia tampaknya lebih mampu daripada kakaknya."

    josephine @ f_eyeroll "Itu tidak berarti banyak."

    jump josie_button_showroom.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
