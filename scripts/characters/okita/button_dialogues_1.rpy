label okita_button_dress_code:
    scene expression player.location.background_closeup
    show okita 1 at right
    show anon f_worried
    with dissolve
    anon "Hai {b}Nona Okita{/b}, saya berharap Anda dapat berbicara dengan {b}Nyonya. Smith{/b} tentang kebijakan aturan berpakaian yang baru..."

    show okita 1
    okita "Hmm!"

    show okita 2
    okita "Aku tidak akan membiarkan diriku tunduk pada wanita busuk itu hanya supaya kalian bisa memakai celana longgar dan rok pendek!"

    anon "Bukan, bukan itu... Aku khawatir dengan bagian yang membatasi pewarna rambut dan aku benar-benar ingin-"

    show okita 10c with dissolve
    okita "Pewarna rambut?"

    show okita 11 with dissolve
    okita "Itu yang kamu khawatirkan?"

    show okita 4
    anon "Y-ya, Bu."

    anon "Teman saya {b}Eve{/b} suka mewarnai rambutnya menjadi biru, dan saya berharap Anda dapat meyakinkan {b}Ny. Smith{/b} ingin mengubah kebijakan?"

    show okita 2
    okita "Ya, itu konyol!"

    okita "Saya punya alat di lantai atas yang mengubah pigmentasi pada folikel rambut."

    show okita 1
    anon f_worried @ f_surprised "Anda melakukannya?"

    show okita 2
    okita "Tentu."

    okita "Maksudku, masih ada beberapa masalah yang perlu kuselesaikan..."

    okita "... Tapi jika teman Anda bersedia menjadi tikus percobaan saya untuk beberapa tes, saya yakin saya bisa menyelesaikannya dalam waktu singkat!"

    show okita 1
    anon f_surprised "Tes-T?"

    pause
    anon f_worried "Menurutku itu bukan ide yang bagus, {b}Nona Okita{/b}..."

    show okita 2
    okita "Oh, ayo sekarang!"

    okita "Itu semua hal-hal non-invasif... Ya, sebagian besar..."

    okita "Ada kemungkinan kecil dia akan kehilangan rambutnya sepenuhnya, tetapi itu adalah skenario terburuk!"

    show okita 1
    anon a_facepalm @ -m_talk "..."
    show okita 2
    okita "Kita berbicara tentang peluang yang kurang dari satu persen!"

    show okita 1
    anon a_idle f_worried @ f_unimpressed_bored "Ehh, aku rasa aku akan mengecek ke guru lain saja dan melihat apakah salah satu dari mereka bisa membantuku..."

    show okita 2
    okita "Baiklah, sesuaikan dirimu."

    show okita 1
    anon "Terima kasih, {b}Nona Okita{/b}."

    hide anon with dissolve
    return

label button_okita_intro:
    scene location_school_science_closeup
    show anon
    show okita 4 at right
    with dissolve
    anon "Baiklah, {b}Nona Okita{/b}. Apa yang harus saya lakukan agar nilai saya naik?"

    show okita 5
    okita "Anda akan membantu saya membebaskan diri dari pengusiran saya ke negeri yang kekurangan."

    show okita 4
    anon f_worried "Hah? Pembuangan? Apa yang sedang kamu bicarakan?"

    show okita 3
    okita "Apakah Anda benar-benar percaya seseorang dengan kecerdasan saya ada di sini, mengajarkan ilmu dasar kepada sekelompok Neanderthal?"

    show okita 4
    anon "Uhh..."

    show okita 3
    okita "Anda pikir ini adalah cita-cita saya dalam hidup saya?!"

    show okita 4
    anon @ f_skeptical "... Tidak?"

    show okita 11
    okita "Saya pernah menjadi yang terdepan, {b}[firstname]{/b}!"

    okita "Saya bekerja bersama beberapa pemikir paling cemerlang di planet ini, berjuang untuk memajukan umat manusia ke masa depan!"

    show okita 11b
    anon f_normal "Kedengarannya... Intens! Bagaimana kamu bisa sampai di sini?"

    show okita 11
    okita "Suatu hari rekan-rekan saya memaksa saya keluar!"

    show okita 11b
    anon f_surprised "Apa?! Mengapa mereka melakukan itu?"

    show okita 5
    okita "Ya, mereka mengklaim saya kehilangan gambaran yang lebih besar."

    okita "Bahwa aku menjadi begitu peduli dengan kemajuan ilmu pengetahuan sehingga aku lupa akan etika yang telah aku bersumpah untuk menjunjungnya."

    show okita 4
    anon f_worried @ -m_talk "..."
    show okita 11
    okita "Faktanya, mereka hanya terintimidasi oleh kecerdasan saya."

    okita "Mereka tidak bisa mengikuti, jadi mereka bersatu dan memasukkan saya ke daftar hitam!"

    show okita 11b
    anon @ f_confused "Masuk daftar hitam? Maksudnya itu apa?"

    show okita 3
    okita "Itu berarti tidak ada lembaga ilmiah yang berharga yang akan menerima saya!"

    show okita 11
    okita "Aku telah dikucilkan untuk menjalani kehidupan yang membosankan di tempat yang monoton seperti ini..."

    okita "... Dikelilingi oleh anak-anak dan orang bodoh!"

    show okita 11b
    anon "Ya, itu cerita yang menyedihkan, tapi bagaimana saya bisa membantu Anda?"

    show okita 3
    okita "Ya, sebenarnya sederhana saja."

    show okita 5
    okita "Saya hanya perlu menyelesaikan apa yang saya mulai."

    show okita 4
    anon "Hah?"

    show okita 2
    okita "Penemuan saya! Yang saya kerjakan di Cuntech sebelum orang-orang bodoh itu memasukkan saya ke dalam daftar hitam."

    okita "Jika saya bisa membuktikannya berhasil dan menerbitkan salah satunya."

    show okita 1
    anon "Anda pikir itu akan membuat Anda mendapatkan pekerjaan Anda kembali?"

    show okita 11
    okita "... Saya tidak peduli dengan pekerjaan itu!"

    okita "Aku ingin menunjukkan kepada para pengkhianat itu betapa bodohnya mereka, dengan mengabaikan {b}Tori Okita{/b}!"

    show okita 5
    okita "Selain itu, jika salah satu penemuanku berhasil, nilainya akan sangat besar!"

    show okita 2
    okita "Saya akan membeli laboratorium saya sendiri!"

    show okita 1
    anon @ f_skeptical "... Masih belum melihat bagaimana aku bisa menyesuaikan diri dengan semua ini."

    show okita 5
    okita "Baiklah, pertama-tama, saya ingin Anda {b}membantu saya masuk ke kantor saya{/b}."

    show okita 4
    anon f_normal @ f_laugh "Anda terkunci di luar kantor Anda sendiri?"

    show okita 5
    okita "Ya, tiran itu {b}Ny. Smith{/b} mengunci saya di luar!"

    show okita 4
    anon "Kepala Sekolah?!"

    anon "Kenapa dia melakukan itu?"

    show okita 5
    okita "Dia tidak ingin aku meneruskan proyek kesayanganku selama masa sekolah."

    show okita 9
    okita "... Katanya saya harus tetap fokus seratus persen pada kurikulum."

    show okita 11
    okita "Itu benar-benar tidak masuk akal!"

    show okita 4
    anon f_worried @ f_confused "... Bagaimana aku bisa mengajakmu masuk?"

    show okita 5
    okita "Dengan {b}kode kunci{/b} tentunya. {b}Ny. Smith{/b} akan menyimpannya {b}disimpan di suatu tempat di kantornya{/b}, saya yakin."

    show okita 4
    anon "Kamu ingin aku {b}mendobrak kantor kepala sekolah dan mencuri darinya{/b}?!"

    show okita 5
    okita "Ini sebenarnya bukan mencuri... Saya hanya ingin Anda mengetahui kodenya."

    show okita 3
    okita "Selain itu, Anda tidak akan rugi apa-apa... Ingat?"

    show okita 4
    anon @ a_point f_skeptical "Dia bisa mengusirku!"

    show okita 5
    okita "Apakah itu penting? Anda akan terjebak di sini selama satu tahun lagi terlepas dari apakah Anda gagal di kelas saya..."

    show okita 4
    anon "Ya, tapi..."

    show okita 3
    okita "Jangan bodoh. Ini bagus sekali! Jika Anda mendapatkan cetak birunya dari kantor saya, bantu saya membuat apa yang ada di dalamnya, dan jalankan beberapa tes untuk membuktikan bahwa cetak biru tersebut berhasil..."

    show okita 5
    okita "... Aku akan memberimu nilai A+ di kelasku."

    show okita 4
    anon f_normal "Nilai A+?!"

    anon a_thinking f_thinking "Hmm..."

    anon "Jadi, pada dasarnya, apakah saya membantu Anda melakukan ini atau saya terjebak dengan nilai yang gagal?"

    show okita 3
    okita "Ya. Tanpa bantuan saya, saya menghitung peluang Anda untuk lulus kelas saya adalah sekitar 3.720 berbanding 1."

    show okita 4
    anon a_idle f_worried @ f_skeptical "Sheesh, yah, sepertinya aku tidak punya banyak pilihan kalau begitu."

    show okita 7
    okita "Anda akhirnya mulai memahami situasinya!"

    show okita 6
    anon "Jadi, bagaimana cara {b}mendapatkan kode kunci dari kantor Ny. Smith{/b}?"

    show okita 5
    okita "Itu masalahmu."

    show okita 4
    anon f_sad_down "..."
    anon "Luar biasa."

    show anon f_tired
    show okita 7
    okita "Semoga beruntung, {b}[firstname]{/b}!"

    show okita 5
    okita "... Oh dan selagi Anda berada di kantor saya, kenapa Anda tidak {b}mengambil jas lab dan kacamata pengaman{/b}."

    okita "Anda akan membutuhkannya."

    hide okita with dissolve
    anon f_sad_down "Ugh..."

    anon @ -m_talk "( Saya harus menunggu {b}Nyonya Smith meninggalkan kantornya jika saya ingin mencarinya dengan benar{/b}. )"

    hide anon with dissolve
    return

label button_okita_get_keycode:
    scene location_school_science_closeup
    show anon
    show okita 3 at right
    with dissolve
    okita "Adakah yang beruntung mendapatkan {b}kode kunci{/b} itu?"

    show okita 4
    anon "Saya masih mengerjakannya."

    show okita 3
    okita "Ya, waktu terus berjalan."

    show okita 4
    anon f_worried "saya tahu..."

    show okita 9
    okita "Cih..."

    hide okita with dissolve
    show anon f_sad_down
    anon "Ugh..."

    anon @ -m_talk "( Saya harus menunggu {b}Nyonya Smith meninggalkan kantornya jika saya ingin mencarinya dengan benar{/b}. )"

    hide anon with dissolve
    return

label button_okita_foam_misshap:
    scene location_school_science_closeup
    show anon
    show okita 5 at right
    with dissolve
    okita "Bagus, kamu di sini. Kita bisa memulainya."

    show okita 4
    anon "Ya baiklah."

    anon "Jadi apa yang pertama kita bangun?"

    show okita 5
    okita "akan kutunjukkan padamu."

    hide anon
    show player 109f zorder 0 at Position(xpos=0.25, ypos=1.0)
    show okita 12 zorder 1 at Position(xpos=0.85, ypos=1.0)
    with dissolve
    okita "Saya menyebut keindahan ini, Okitatron Oculars."

    show bp 1 zorder 2 at Position(xpos=0.5, ypos=0.95) with dissolve
    pause
    anon "Kacamata?"

    okita "Hah, bukan kacamata..."

    hide bp with dissolve
    show player 109f
    show okita 12
    okita "Ini adalah layar optik yang dipasang di kepala, komputer yang benar-benar ada di mana-mana."

    show anon f_worried
    hide player
    with dissolve
    show okita 13
    anon "Saya tidak mengerti."

    show okita 9 at right
    with dissolve
    okita "Tentu saja tidak. Kamu bodoh."

    show okita 5
    okita "Biar saya jelaskan begini, Okitatron Oculars akan segera menggantikan setiap ponsel cerdas di planet ini."

    show okita 4
    anon "Jadi itu telepon?"

    show okita 3
    okita "{i}*Huh*{/i}"

    show okita 5
    okita "Mari kita fokus membangunnya, dan setelah selesai, saya akan menunjukkan kepada Anda apa fungsinya..."

    show okita 4
    anon f_normal @ f_laugh "Bekerja untuk saya."

    anon "Bagaimana kita memulainya?"

    show okita 10b with dissolve
    okita "Hmm."

    show okita 10c
    okita "Ya, saya kehilangan beberapa komponen..."

    show okita 10b
    okita "..."
    show okita 5 with dissolve
    okita "Saya dapat mengumpulkan sebagian besar dari apa yang kami butuhkan sendiri."

    show okita 3
    okita "Bisakah Anda {b}mencarikan saya sepasang lensa{/b}?"

    show okita 4
    anon @ f_thinking "{b}Lensa{/b}? Seperti di teleskop?"

    show okita 5
    okita "Bukan dari teleskop. Saya memerlukan {b}lensa dari kacamata. Khususnya, lensa varifokal{/b}."

    show okita 4
    anon @ f_confused "{b}Varifokal{/b}?"

    show okita 3
    okita "Ya, itu berarti {b}lensa{/b} dengan dua resep berbeda; atas dan bawah."

    show okita 4
    anon f_surprised "Seperti untuk seseorang yang menderita rabun jauh dan rabun jauh?"

    show okita 2
    okita "Dengan tepat!"

    show okita 1
    anon f_normal "Hmm, saya mungkin bisa melacak hal seperti itu."

    show okita 3
    okita "Mungkin?"

    show okita 1
    anon "Maksudku, aku kenal beberapa orang yang memakai kacamata. Mungkin salah satu dari mereka punya set cadangan."

    show okita 2
    okita "Sangat bagus. {b}Laporkan kembali kepada saya di sini, di laboratorium sains, setelah Anda memilikinya{/b}."

    show okita 1
    anon "Baiklah."

    hide anon with dissolve
    return

label button_okita_get_bifocal_lenses:
    scene location_school_science_closeup
    show anon
    show okita 3 at right
    with dissolve
    okita "Apakah Anda menemukan apa yang kami butuhkan?"

    show okita 4
    anon "Apa yang kamu ingin aku temukan lagi?"

    show okita 3
    okita "Pfft, kamu punya satu tugas yang harus diselesaikan dan kamu lupa?"

    show okita 4
    anon f_sad_down "A-kurasa begitu..."

    show okita 9
    okita "Khas."

    show okita 5
    okita "Saya ingin Anda {b}menemukan sepasang lensa varifokal{/b}."

    show okita 4
    anon f_normal @ f_laugh a_point "Oh benar! Baik rabun jauh maupun rabun jauh."

    show okita 5
    okita "Benar."

    show okita 3
    okita "Mungkin sebaiknya aku menulisnya terbalik di dahimu, agar kamu tidak lupa?"

    show okita 4
    anon f_worried "... Tidak, tidak apa-apa. Aku sudah mendapatkannya sekarang."

    okita "Mmmhmm."

    hide okita with dissolve
    anon f_thinking a_thinking @ -m_talk "( Hmm, saya harus {b}memeriksa sekolah dan melihat apakah ada yang punya lensa varifokal cadangan{/b}. )"

    hide anon with dissolve
    return

label button_okita_get_faptic_engine:
    scene location_school_science_closeup
    show anon
    show okita 4 at right
    with dissolve
    anon "Hai, {b}Nona Okita{/b}. Apakah Anda sudah mengatasi masalah kacamata tersebut?"

    show okita 3
    okita "Maksudmu Okitatron Oculars?"

    show okita 4
    anon "Ya maaf. I-itulah yang kumaksud."

    show okita 5
    okita "Ya, saya menyelesaikannya. Saya sedang dalam proses mematenkannya sekarang."

    show okita 4
    anon "Itu kabar baik, bukan?"

    show okita 5
    okita "Ini bagus untuk permulaan."

    show okita 3
    okita "... Tapi jangan pedulikan Oculars, {b}[firstname]{/b}!"

    okita "Berita kemarin!"

    show okita 1
    anon @ f_laugh "... O-oke."

    show okita 2
    okita "Hari ini saya punya sesuatu yang benar-benar inovatif!"

    show okita 1
    anon f_flirt "Lebih inovatif dari kacamata X-ray?"

    show okita 3
    okita "Bisa aja. Teknologi sinar-X belum inovatif sejak tahun 1980an."

    show okita 1
    anon f_flirt_grin @ -m_talk "..."
    hide anon
    show player 109f zorder 0 at Position(xpos=0.25, ypos=1.0)
    show okita 12 zorder 1 at Position(xpos=0.85, ypos=1.0)
    with dissolve
    okita "Saya menyebutnya Sabuk Okitatron."

    show bp 2 zorder 2 at Position(xpos=0.5, ypos=0.95) with dissolve
    pause
    anon "... Sabuk?"

    okita "Ya, nama itu mungkin memerlukan beberapa pekerjaan..."

    hide bp with dissolve
    show player 109f
    show okita 12
    okita "Tapi aku akan mengkhawatirkannya nanti!"

    okita "Untuk saat ini, mari fokus pada fungsi perangkat."

    hide player
    show anon f_worried
    show okita 2 at right
    with dissolve
    okita "Sabuk Okitatron akan merevolusi cara orang menjaga bentuk tubuh!"

    show okita 1
    anon @ -m_talk "..."
    anon "Maksudmu itu perangkat olahraga?"

    show okita 2
    okita "Tidak. Ini akan menjadikan olahraga sebagai masa lalu!"

    okita "Ini menargetkan semua kelompok otot utama dengan getaran mikro yang tidak terdeteksi!"

    okita "Ini merangsang pertumbuhan otot sehingga Anda tidak perlu berolahraga lagi!"

    show okita 1
    anon f_normal "Kedengarannya luar biasa!"

    show okita 9
    okita "Ya, tentu saja luar biasa! Menurut Anda, dengan siapa Anda sedang berbicara?"

    show okita 1
    anon @ -m_talk "..."
    show okita 2
    okita "Namun, saya kehilangan komponen kuncinya."

    show okita 1
    anon @ f_laugh "... Di sinilah saya masuk?"

    show okita 2
    okita "Dengan tepat!"

    show okita 3
    okita "Getaran mikro ini harus disesuaikan dengan frekuensi yang sangat spesifik, jika tidak maka getaran tersebut tidak akan berhasil."

    show okita 1
    anon "Oke, jadi bagaimana kita melakukannya."

    show okita 2
    okita "Kita memerlukan {b}mesin faptic{/b}."

    show okita 1
    anon f_worried @ f_skeptical "... Hah?"

    show okita 3
    okita "{b}mesin faptik{/b}."

    show okita 1
    anon f_hurt a_thinking @ -m_talk "..."
    show okita 9
    okita "{i}*Huh*{/i}"

    show okita 5
    show anon f_worried a_idle with dissolve
    okita "{b}Cari June{/b}. Dia pernah membantu saya menyelesaikan proyek-proyek sulit di masa lalu."

    okita "{b}Katakan padanya aku mengirimmu untuk mesin faptic{/b}."

    okita "Dia akan tahu apa yang harus dilakukan."

    show okita 4
    anon f_normal @ a_point "{b}Mesin Faptik{/b}. Baiklah, aku akan kembali."

    hide anon with dissolve
    show okita 9
    okita "Anak malang itu lebih bodoh dari sekotak batu..."

    return

label button_okita_get_faptic_engine_repeat:
    scene location_school_science_closeup
    show anon
    show okita 5 at right
    with dissolve
    okita "Sudah kembali? Apakah kamu memilikinya?"

    show okita 4
    anon f_worried "Di mana saya bisa mendapatkan {b}mesin faptic{/b} ini lagi?"

    show okita 9
    okita "{i}*Huh*{/i}"

    show okita 5
    okita "{b}bicara saja dengan June{/b}, dia akan menjelaskan."

    show okita 4
    anon f_normal @ f_laugh "Oh benar! Saya akan segera kembali."

    hide anon with dissolve
    return

label button_okita_tired_from_belt:
    scene location_school_science_closeup
    show anon
    show okita 1 at right
    with dissolve
    anon @ a_wave "Hai, {b}Nona Okita{/b}! Apakah kamu merasa lebih baik?"

    show okita 2
    okita "Sudahlah, {b}[firstname]{/b}."

    okita "Saya senang Anda di sini, ada pekerjaan yang harus diselesaikan!"

    show okita 1
    anon f_worried @ f_sad_down "{i}*Huh*{/i} Kamu tidak pernah menyerah, kan?"

    show okita 5
    okita "Aku akan menyerah ketika penemuanku diterbitkan dan orang-orang Cuntech itu memakan semangkuk besar burung gagak!"

    show okita 4
    anon "... Bagus."

    anon "Penemuan gila apa yang sedang kita kerjakan kali ini?"

    show okita 10c at Position(xpos=0.98, ypos=1.0) with dissolve
    okita "Hmm, kita harus mengambil jalan memutar dari penemuan untuk saat ini."

    okita "Setidaknya sampai kita mendapatkan {b}Ny. Smith{/b} keluar dari kasusku!"

    show okita 10b
    anon "Bagaimana kita bisa mencapainya?"

    show okita 10c
    okita "Aku sendiri sudah memikirkan hal itu..."

    show okita 2 at right with dissolve
    okita "Saya pikir serum pembersih pikiran yang sederhana adalah solusi terbaik kami."

    show okita 1
    anon f_surprised "{i}Penghapusan pikiran{/i}? Kedengarannya tidak bagus..."

    show okita 2
    okita "Bah, ini sangat aman! Selama Anda mengikuti arahan saya sampai ke surat itu!"

    okita "Satu-satunya hal yang akan dia lupakan adalah keengganannya terhadap eksperimenku."

    show okita 1
    anon f_worried @ f_skeptical "Anda yakin?"

    show okita 3
    okita "Ya, tidak ada cara untuk sepenuhnya yakin tanpa pengujian yang tepat..."

    show okita 4
    anon @ -m_talk "..."
    show okita 9
    okita "Dia akan baik-baik saja!"

    show okita 4
    anon "... Apa yang perlu saya lakukan?"

    show okita 5
    okita "Anda akan memulai dengan {b}mengumpulkan bahan-bahan{/b} yang kami perlukan."

    show okita 4
    anon "Uh, baiklah. Berapa banyak?"

    show okita 5
    okita "Kita memerlukan {b}lima{/b} totalnya."

    show okita 101 at Position(xpos=1.01, ypos=1.0) with dissolve
    okita "Berikut daftarnya."

    hide anon
    show player 556 at left
    show okita 4 at right
    with dissolve
    anon "{b}Jamur Falicum{/b}, {b}Ekstrak Katak Tanduk{/b}, {b}Eufhorbia Psikotropika{/b}, {b}cairan dasar{/b}..."

    show player 557
    anon "Saya belum pernah mendengar hal ini sebelumnya!"

    hide player
    show anon f_worried
    with dissolve
    show okita 2
    okita "Nah, {b}jamur falicum tumbuh di hutan{/b} di sini di Summerville."

    show okita 3
    okita "Mereka mudah dikenali karena bentuknya yang falus."

    show okita 1
    anon "... Bruto."

    show okita 2
    okita "{b}Kodok Tanduk dan Euphorbia Psikotropika juga dapat ditemukan di hutan{/b}."

    show okita 1
    anon "Psikotropika apa?"

    show okita 2
    okita "Ini adalah bunga yang bercahaya... Anda mungkin mengenalnya sebagai bunga \"jangan lupakan saya\"."

    show okita 1
    anon "Tidak, belum pernah mendengarnya."

    show okita 3
    okita "Benar-benar?"

    show okita 2
    okita "Anda hanya akan menemukannya di tempat gelap. {b}taruhan terbaik Anda adalah gua{/b}."

    show okita 1
    anon @ f_surprised "Ada gua di Summerville?"

    show okita 3
    okita "Tentu saja."

    show okita 2
    okita "Adapun {b}Kodok Tanduk{/b}, ini adalah musim kawin mereka. Jadi {b}carilah kolam atau sungai{/b}."

    okita "Mereka seharusnya mudah dikenali dari bagian belakangnya yang berwarna ungu dan menggumpal."

    show okita 1
    anon "Oke, itu tidak terlalu buruk, tapi {b}bagaimana dengan cairan dasar ini{/b}? Apa itu?"

    show okita 2
    okita "Kita hanya perlu sesuatu yang ringan sebagai bahan dasar serum. {b}Kaldu sayuran paling cocok{/b}."

    okita "Anda seharusnya dapat {b}membelinya di Consum-R{/b}."

    show okita 1
    anon f_surprised "Bagaimana dengan bahan terakhir ini?"

    anon "{b}Ny. DNA Smith{/b}?!"

    anon f_confused "Bagaimana aku bisa mendapatkannya?!"

    show okita 3
    okita "... Ya, itu akan menjadi yang sulit."

    show okita 2
    okita "Sampel rambut atau air liur adalah pilihan terbaik."

    okita "Saya yakin Anda akan menemukan sesuatu..."

    show okita 1
    anon f_worried "Hebat..."

    anon "Baiklah, kurasa sebaiknya aku memulainya."

    show okita 2
    okita "Ayo bicara dengan saya jika Anda memerlukan bantuan untuk menemukan bahan apa pun."

    show okita 5
    okita "... Dan cepatlah! Kita harus menyelesaikan ini sebelum {b}Ny. Smith{/b} mengubah kode ke kantor saya lagi!"

    hide anon with dissolve


    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
