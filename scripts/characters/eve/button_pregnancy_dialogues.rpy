label eve_preg_stage_1_intro:
    scene expression player.location.background_closeup
    show eve b_undies
    show anon with dissolve
    anon "Hei kamu."

    eve "Hehe, hai {b}[firstname]{/b}!"

    anon "Lagi sibuk apa?"

    eve "Ah santai saja..."

    return

label eve_preg_stage_1_leave:
label eve_preg_stage_2_leave:
label eve_preg_stage_3_leave:
label eve_preg_stage_4_leave:
    anon @ a_wave "Aku serahkan padamu kalau begitu."

    eve "Baiklah."

    anon "Beri tahu saya jika ada yang bisa saya lakukan, oke?"

    eve "Terima kasih, {b}[firstname]{/b}."

    hide anon with dissolve
    return

label eve_preg_stage_1_feeling:
    eve "Selain sedikit mual di pagi hari, saya merasa luar biasa!"

    anon f_worried "Mual di pagi hari?"

    eve f_happy "Ya, tapi tidak ada yang perlu dikhawatirkan."

    eve "Buku {b}Grace{/b} membuat saya mengatakan itu normal-normal saja."

    anon f_normal "Jadi kalian punya banyak buku kehamilan ya?"

    eve "Yup dan kami telah membacanya bersama di malam hari."

    anon "Kedengarannya menyenangkan."

    eve "Ya, sudah."

    show eve f_normal
    return

label eve_preg_stage_1_doctor:
    anon "Bagaimana kunjungan dokter Anda?"

    eve @ f_eyeroll "Oh, tidak apa-apa."

    eve "Dia melakukan USG dan mengatakan semuanya tampak normal."

    anon "Itu bagus untuk didengar."

    eve "Masih terlalu dini untuk mengetahui apakah itu laki-laki atau perempuan, tetapi {b}Odette{/b} yakin bahwa itu laki-laki."

    anon @ -m_talk "Hmm?"

    anon @ f_confused "Mengapa dia berpikir seperti itu?"

    eve "Karena kamu melakukanku dari belakang ketika kita hamil."

    anon f_worried @ f_surprised "!!!"
    anon "A-dan itu penting?"

    eve "Menurutnya hal itu..."

    anon @ a_behind_head "Aneh."

    eve @ f_laugh "Hehehe!"

    show anon f_normal
    return

label eve_preg_stage_1_grace:
    anon "Bagaimana kabar {b}Grace{/b} dengan semua ini?"

    eve @ f_laugh "Dia luar biasa!"

    eve "Sejujurnya, aku tidak tahu apa yang akan kulakukan tanpa dia."

    anon "Ya?"

    eve "Dia menyuruh saya melakukan diet kehamilan yang ketat dan saya belajar yoga."

    anon @ f_confused "Anda sedang belajar yoga?"

    eve "Hehe, ya!"

    eve "Tampaknya penting untuk menjaga tingkat kecemasan Anda saat hamil."

    eve "Dia bahkan menawarkan untuk mulai memberi saya pijatan setiap hari."

    anon @ f_sad_down "Sial, aku cemburu."

    return

label eve_preg_stage_2_intro:
    scene expression player.location.background_closeup
    show eve f_happy b_pajamas_pregnant_bump
    show anon with dissolve
    anon "Hei kamu."

    eve "Hehe, hai {b}[firstname]{/b}!"

    anon "Lagi sibuk apa?"

    eve @ f_nervous_down "Ah, aku hanya mencoba untuk bersantai.."

    return

label eve_preg_stage_2_feeling:
    anon "Bagaimana perasaanmu?"

    eve "Uhh, lumayan kalau mempertimbangkan semuanya."

    eve "Menurut saya diet, yoga, dan pijat terus-menerus memberikan hasil yang luar biasa!"

    anon "Ya, menurutku begitu."

    show eve f_normal_down a_squeeze1 with dissolve
    show anon f_surprised
    eve "Dan pernahkah kamu melihat payudara ini?!"

    show eve a_squeeze2 with dissolve
    show anon f_flirt
    eve f_happy "Saya sudah menaikkan ukuran cup penuh!"

    anon "{i}*Gulp*{/i} Y-ya?"

    show eve f_sexy a_squeeze with dissolve
    eve "Sebaiknya kamu meminumnya dalam, {b}[firstname]{/b}."

    eve "{b}Odette{/b} mengatakan mereka akan menjadi miring setelah bayinya lahir..."

    show eve f_happy a_idle with dissolve
    show anon f_normal
    return

label eve_preg_stage_2_anything:
    anon "Ada yang bisa kuberikan padamu?"

    eve "Ciuman akan menyenangkan."

    anon "Saya bisa melakukan itu."

    hide anon
    show eve b_pajamas_kiss:
        xoffset 50
    with dissolve
    eve "MM."

    pause
    hide eve
    show anon
    show eve f_happy b_pajamas_pregnant_bump
    with dissolve
    eve "Kamu berjanji akan tetap mencintaiku saat aku gemuk dan mudah tersinggung?"

    anon f_thinking "Hmm, entahlah..."

    anon "Seberapa gemuk sebenarnya yang kita bicarakan?"

    eve f_surprised "{i}*Terkesiap*{/i}"

    anon f_normal @ f_laugh a_point "Hehe, aku bercanda!"

    anon "Tentu saja aku akan tetap mencintaimu."

    eve f_happy @ f_angry "Anda sebaiknya!"

    return

label eve_preg_stage_3_intro:
label eve_preg_stage_4_intro:
    scene expression player.location.background_closeup
    show eve f_sad b_pajamas_pregnant_belly
    show anon with dissolve
    anon "Hei kamu."

    eve "Hehe, hai {b}[firstname]{/b}!"

    anon f_worried "Lagi sibuk apa?"

    eve "Ah, aku hanya mencoba untuk bersantai.."

    return

label eve_preg_stage_3_feeling:
label eve_preg_stage_4_feeling:
    anon "Bagaimana perasaanmu?"

    eve f_sad_down "Gemuk dan mudah tersinggung."

    anon "Uh oh."

    eve "Aku merasa sangat tidak nyaman, sepanjang waktu..."

    eve f_sad "Dan payudaraku membunuhku!"

    anon "Tidak bisakah kamu memompa atau apalah?"

    eve "Tidak, saya tidak bisa."

    eve "Buku-buku mengatakan hal itu mungkin menyebabkan persalinan prematur."

    anon f_surprised "Benar-benar?"

    eve "{i}*Huh*{/i} Ya."

    show anon f_worried
    return

label eve_preg_stage_3_anything:
label eve_preg_stage_4_anything:
    anon "Ada yang bisa kuberikan padamu?"

    eve "Ya, kamu pikir kamu bisa menggendong anak ini di dalam dirimu sebentar, jadi aku bisa tidur nyenyak?"

    anon "Anda mengalami masalah tidur?"

    eve f_angry "Ya, ada bola bowling yang melekat pada saya, bagaimana menurut Anda?"

    anon "Maaf."

    anon "Apakah ada yang bisa saya lakukan untuk membantu?"

    eve f_sad "Tidak, aku minta maaf..."

    eve "Aku tidak bermaksud membentakmu, {b}[firstname]{/b}."

    eve "Aku hanya ingin hal ini keluar dari diriku, kau tahu?"

    anon "Itu akan segera terjadi, kamu hanya perlu bertahan lebih lama lagi, oke?"

    eve f_sad_down "{i}*Huh*{/i} Saya tahu."

    show eve f_sad
    return

label eve_preg_stage_4_bathroom:
    scene expression background(544, 288, 2.) as stage at flip
    show layer master at flip
    show eve b_naked_pregnant_belly f_happy a_towel_back
    show anon f_flirt with dissolve
    eve "Cih, apa kamu belum cukup melihatnya?"

    anon "Tentu saja tidak!"

    anon "Aku tidak akan pernah cukup melihatmu, sayangku."

    eve "Bagus, Casanova... Meletakkannya agak tebal, bukan?"

    anon "Tidak jika itu berhasil."

    eve @ f_laugh "Hehehe!"

    anon "Ayo, lihat sekali lagi?"

    eve "{i}*Huh*{/i} Baiklah, kamu menang."

    show eve a_remove1 with dissolve
    pause
    show eve a_remove2 with dissolve
    anon @ f_laugh "Aku sangat mencintaimu!"

    eve "Aku pun mencintaimu."

    show anon f_flirt_low
    pause
    show eve a_remove1 with dissolve
    show anon f_flirt
    eve "Sekarang keluar dari sini supaya aku bisa menyelesaikan rambutku."

    anon "Baiklah baiklah."

    hide anon with dissolve
    $ game.main()
    return

label eve_preg_stage_5_bedridden:
    scene expression game.timer.image('location_hospital_baby_bed{}')
    show grace f_happy:
        crop (0, 0, 1024, 650)
        flip
        xoffset 200
        zoom .9
    show eve b_gown_bed
    with None
    show grace:
        unflip
        xoffset -100
    show anon
    with dissolve
    eve "Hai, {b}[firstname]{/b}."

    eve "Anda datang untuk memeriksa kami lagi?"

    anon "Ya, bagaimana kabar kalian?"

    eve "Kami semua sangat ingin keluar dari sini dan kembali ke rumah."

    grace "Seharusnya tidak lebih lama lagi sekarang."

    eve "Saya harap Anda benar, saya sangat ingin makanan sungguhan!"

    show grace f_laugh:
        flip
        xoffset 400
    with dissolve
    grace "Hehe, iya... Makanan rumah sakit tidak pernah ada gunanya."

    grace f_happy "Mungkin kita akan memesan makanan Cina atau sesuatu untuk merayakannya?"

    eve f_happy "Ya Tuhan, kedengarannya luar biasa!"

    show grace:
        unflip
        xoffset -100
    with dissolve
    eve "Bukankah itu terdengar bagus, {b}[firstname]{/b}?"

    anon "Ya, tentu saja."

    show grace:
        flip
        xoffset 200
    hide anon
    with dissolve
    $ game.main()
    return

label eve_preg_stage_5_intro:
label eve_preg_stage_6_intro:
    scene expression player.location.background_closeup
    show eve b_pajamas a_baby f_happy_down
    show anon with dissolve
    eve "♪ {i}Tidurkan bayiku di dadaku?{/i} ♪"

    eve "♪ {i}Apakah akan terasa hangat dan nyaman?{/i} ♪"

    eve "♪ {i}Lengan ibumu terlipat?{/i} ♪"

    eve "♪ {i}Dalam hatinya ada cinta seorang ibu?{/i} ♪"

    eve "♪ {i}Tidak akan ada orang yang datang menyakitimu?{/i} ♪"

    eve "♪ {i}Tidak ada yang akan merusak istirahatmu?{/i} ♪"

    eve "♪ {i}Tidurlah sayangku dengan tenang?{/i} ♪"

    eve "♪ {i}Tidur di dada ibu yang lembut?{/i} ♪"

    return

label eve_preg_stage_5_singing:
label eve_preg_stage_6_singing:
    anon "Apa yang kamu nyanyikan?"

    eve f_happy @ -m_talk "Hmm?"

    eve "Oh, itu hanya lagu yang biasa dinyanyikan ibuku untuk {b}Grace{/b} dan aku ketika kami masih kecil."

    eve "Selalu menidurkanku."

    anon "Sungguh indah!"

    eve @ f_laugh "Hehe, terima kasih."

    show eve f_happy_down
    return

label eve_preg_stage_5_anything:
label eve_preg_stage_6_anything:
    anon "Kalian butuh sesuatu?"

    eve f_happy "Tidak, kami baik-baik saja."

    eve f_happy_down "Keluar seperti cahaya, bukankah kamu anak kecil?"

    eve "Ya, benar!"

    pause
    anon "Mmm, aku sangat mencintai kalian berdua."

    eve @ f_happy "Hehe, kami juga mencintaimu!"

    return

label eve_preg_stage_5_leave:
label eve_preg_stage_6_leave:
    anon "Aku akan meninggalkanmu."

    eve f_happy "Sudah berangkat?"

    anon "Ya, aku akan segera kembali."

    eve "Baiklah."

    eve f_happy_down "Cepat kembali ke kami."

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
