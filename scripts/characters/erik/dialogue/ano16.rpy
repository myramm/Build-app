label ano16_init_erik:
    show erik
    show anon with dissolve
    anon "Baiklah, {b}Erik{/b}, kita berada di rumah pohon lama kita..."

    anon "... Bisakah Anda menjelaskan apa yang kami lakukan sekarang?"

    erik @ f_laugh "Itu akan menjadi kesenangan saya!"

    erik "Tapi pertama-tama, kita harus mendaki."

    anon f_confused "{b}Erik{/b}, tidak bisakah kamu memberitahuku di sini saja?"

    erik f_woozy "Percayalah padaku, kawan!"

    erik "Anda akan menyukai ini!"

    hide erik
    show anon f_unimpressed:
        flip
        xoffset -500
    with dissolve
    anon @ -m_talk "..."
    anon f_sad_down a_rub "{i}*Huh*{/i}"

    hide anon with dissolve
    return


label ano16_tree_erik:
    show erik b_knees a_sonar oh_headset:
        xoffset 120
    show anon f_surprised_low b_onbed_back with dissolve
    erik @ f_laugh "Coba lihat!"

    anon f_confused "Benda apa itu?"

    erik "Itu adalah alat pendengar."

    anon "Perangkat mendengarkan?"

    erik "Ya, itu memperkuat suara yang jauh."

    erik "Kita bisa menggunakannya untuk menguping percakapan yang terjadi di kediaman walikota."

    anon f_normal @ f_surprised "Wah, benarkah?"

    erik f_woozy "Cukup keren, ya?"

    anon "Ini sangat keren!"

    pause
    anon "Tapi, umm... Bagaimana tepatnya cara kerjanya?"

    erik f_normal "Ini sangat sederhana, kawan."

    erik "Anda cukup mengarahkan pistol ke apa pun yang ingin Anda dengarkan..."

    erik a_sonar_point "... Dan perangkat akan memperkuatnya dan kemudian memutarnya kembali melalui headset ini."

    anon f_shy "Oke, tapi saya hanya punya satu pertanyaan..."

    erik a_sonar "Tembak."

    anon "Mengapa kamu memiliki benda itu?"

    erik f_worried "Oh."

    erik f_worried_down "Eh, karena..."

    pause
    anon f_snarky "Karena?"

    erik @ f_worried "... Karena aku membutuhkannya..."

    pause
    erik "... Untuk um..."

    erik f_surprised "... Mengamati burung!"

    anon f_skeptical "Mengamati burung, ya?"

    erik @ f_normal "Ya."

    anon f_snarky @ f_laugh "Pembohong."

    erik f_nervous "Tidak, aku serius!"

    anon @ -m_talk "Mhmm."

    anon "Jenis burung apa yang kamu perhatikan, {b}Erik{/b}?"

    erik "Saya tidak tahu..."

    erik "... Yang berbulu?"

    anon @ -m_talk "..."
    erik f_worried "Apakah kita akan melakukan hal ini atau tidak?"

    anon "{i}*Huh*{/i} Ya..."

    anon "... Tapi kita akan membahasnya lagi nanti!"

    pause
    anon f_normal "Sekarang, bagaimana kita tahu ke mana harus mengarahkan benda itu?"

    erik "Ya, {b}Rump estate{/b} terlalu jauh untuk melihat percakapan tanpa teropong, jadi..."

    erik "... Kita harus bekerja sebagai sebuah tim."

    erik "Ambil teropong di dalam koper di sana dan kami akan menggunakannya untuk menunjukkan dengan tepat orang-orang yang sedang melakukan percakapan."

    anon a_binoculars @ f_brag_closed "Maksudmu ini?"

    erik "Oh, Anda sudah mendapatkannya."

    anon a_idle "Ya."

    erik f_worried_down "Sekarang jika saya bisa membuat hal bodoh ini berhasil..."

    anon f_worried "Ini tidak berfungsi?"

    erik @ f_worried "Tidak saat ini."

    pause
    erik "Itu tidak masuk akal, kemarin berfungsi dengan baik!"

    anon "Suatu hari?"

    erik f_normal @ f_laugh "Ya, aku sedang mengamati sepasang payudara bagus di pantai."

    anon f_grin @ f_laugh "Lihat, aku tahu kamu punya hal yang mesum pada perempuan!"

    erik f_worried "T-tidak!"

    pause
    erik "Burung boobies berkaki biru adalah burung pelaut yang ditemukan di sepanjang garis pantai Amerika Utara, Selatan, dan Tengah!"

    anon f_unimpressed @ -m_talk "..."
    show erik f_woozy
    pause
    anon "Sejujurnya saya tidak tahu apakah Anda bercanda atau tidak."

    erik "Apa yang bisa kukatakan, aku menyukainya..."

    pause
    erik f_normal @ f_laugh "... Dan itulah yang menginspirasi fanfic {i}World of Orcette{/i} saya yang sangat sukses."

    anon f_worried "Fiksi penggemar?"

    erik f_normal @ f_woozy "Ya, mereka menceritakan petualangan erotis karakter saya di pegunungan Kol'gath yang dipenuhi harpy!"

    show anon f_shock
    erik "Harpy adalah ras betina mirip burung yang harus mencari manusia jantan untuk menghasilkan dan membuahi telur mereka..."

    erik f_woozy "... Dan saya yakin saya tidak perlu memberi tahu Anda, mereka sangat seksi!"

    pause
    anon f_normal @ f_laugh "Aku bahkan tidak tahu bagaimana harus menanggapinya..."

    erik f_worried_down @ f_angry "Grr, ada apa dengan benda ini?!"

    anon "Apakah baterainya mati?"

    erik f_bored "Tentu saja baterainya belum mati, itu yang pertama saya periksa."

    erik "Menurutmu betapa bodohnya aku?"

    anon @ -m_talk "..."
    pause
    anon a_take "Biarkan saya melihatnya."

    erik "Tidak, aku mengerti..."

    anon f_unimpressed "Bung, berikan padaku!"

    show anon behind erik
    erik a_sonar_give f_angry "Baiklah, ambillah!"

    show erik a_idle
    show anon a_sonar f_disgusted_low
    with dissolve
    pause
    anon "Apa yang-"

    anon f_unimpressed "Kenapa semuanya lengket?!"

    erik f_worried_down "Aku tidak tahu."

    pause
    erik "Mungkin hanya sisa kepulan keju..."

    pause
    erik "... Atau pelumas."

    anon f_disgusted_low a_sonar_drop1 "Eugh!{p=1}{nw}"

    show anon f_surprised_low a_sonar_drop2
    show erik behind anon
    with dissolve
    erik f_surprised "!!!"
    erik f_angry "Apa-apaan ini, {b}[firstname]{/b}!"

    show anon f_worried a_idle behind erik
    show erik a_sonar_broken f_worried_down
    with dissolve
    pause
    erik f_sad_down "Saya membayar tujuh puluh dolar untuk ini."

    anon "Maafkan aku, {b}Erik{/b}..."

    erik "{i}*Sigh*{/i} Saya rasa itulah akhir dari fase mengamati burung saya..."

    anon "Aku tidak bermaksud-"

    erik a_idle f_sad "Tidak apa-apa."

    erik f_normal @ f_laugh "Saya berpikir sudah waktunya untuk beralih ke kuda."

    show anon f_unimpressed
    erik "Sudahkah saya memberi tahu Anda tentang suku prajurit centaur yang akan mereka tambahkan di patch berikutnya?"

    anon "{b}Erik{/b}, kita pakai teropong saja dan lihat apa yang bisa kita simpulkan ya?"

    erik "Ya baiklah..."


    scene location_treehouse_window_behind
    show erik f_normal:
        flip
        xoffset 125
        yoffset -100
    show anon a_binocular:
        flip
        xoffset -115
        yoffset -75
    show location_treehouse_window
    with fade
    erik "Kamu ingin aku pergi dulu?"

    anon "Tidak, aku pergi dulu."

    pause
    erik f_bored "Cobalah untuk tidak merusaknya juga."

    anon f_unimpressed "Har... Har... Lucu sekali."

    show erik f_normal:
        unflip
        xoffset -280
    show anon f_normal_out a_binocular_look
    with dissolve
    pause
    anon f_worried "Apa yang-"

    erik "Anda melihat sesuatu?"

    anon "Uhh... Ya."

    pause
    erik f_surprised "Apakah itu walikota?!"


    scene location_rump_backyard_spy02 with fade
    pause
    anon "Ya Tuhan, kuharap tidak..."

    pause
    erik "Apa yang kamu lihat, {b}[firstname]{/b}?"

    anon "Sebagai permulaan, penyalahgunaan bendera Amerika..."

    pause
    erik "Bisakah Anda lebih spesifik?"

    anon "Tunggu."


    scene location_rump_backyard_spy01 with fade
    pause
    anon "Itu adalah pria Hispanik berotot yang mengenakan celana dalam."

    erik "Hah?"

    anon "Dan dia sedang berbicara dengan seorang wanita berbikini."

    erik "Bagus sekali!"

    erik "Apakah dia seksi?!"

    anon "Ehh, dia jelas tidak jelek."

    erik "Saya yakin itu putri walikota."

    erik "Dia seperti, super-duper seksi!"


    scene location_rump_backyard_spy03 with fade
    pause
    anon "Hmm, mungkin saja."

    pause
    anon "Dia sepertinya sangat tertarik dengan celana dalam pria ini."

    erik "Apa maksudmu?"

    anon "Dia hanya menatap ke arah mereka."

    erik "Aduh, bung... Kuharap itu bukan putrinya."


    scene location_treehouse_window_behind
    show erik f_worried:
        xoffset -280
        yoffset -100
    show anon a_binocular f_confused:
        flip
        xoffset -115
        yoffset -75
    show location_treehouse_window
    with fade
    anon "Hah?"

    erik f_worried_right "Apakah wanita itu berambut pirang?"

    anon "Tidak."

    erik f_normal @ f_laugh "Fiuh, oke."

    erik "Putrinya berambut pirang."

    pause
    erik f_woozy "Dan semoga lajang!"

    show anon f_eyeroll
    pause
    show anon f_normal_out a_binocular_look with dissolve
    pause
    anon f_shock "!!!"

    scene location_rump_backyard_spy05 with fade
    erik "Apa yang kamu lihat?"

    anon "Seorang gadis muda, cantik, berambut pirang."

    erik "{i}*Terkesiap*{/i} Anda menemukannya!"

    anon "Saya kira demikian."

    erik "Apa yang dia lakukan?!"

    anon "Dia tampak sedang berjemur."

    erik "Wah benarkah?!"


    scene location_treehouse_window_behind
    show erik f_surprised:
        flip
        xoffset 125
        yoffset -100
    show anon f_flirt a_binocular_look:
        flip
        xoffset -115
        yoffset -75
    show location_treehouse_window
    with fade
    erik "Coba lihat!!"

    anon "Tunggu."

    erik f_bored "Tidak mungkin, kawan!"

    anon f_angry "Hentikan, {b}Erik{/b}!"

    erik "Sekarang giliranku!"

    show anon a_idle f_unimpressed behind erik
    show erik a_binocular f_normal
    with dissolve
    anon "Baiklah, tenang!"

    show erik f_woozy a_binocular_look with dissolve:
        unflip
        xoffset -225
    anon "Astaga."

    erik "Oh ya!"

    pause
    erik "Itu calon istriku!"

    anon f_snarky @ f_laugh "Pfft, dalam mimpimu!"

    anon "Kamu harusnya tahu sekarang bahwa gadis seperti itu tidak tertarik pada pria seperti kita..."

    show erik f_worried a_binocular with dissolve:
        flip
        xoffset 125
    erik "Ah, jangan katakan itu."

    anon f_normal "Lihatlah faktanya, kawan."

    anon "Dia sangat cantik, bertubuh seperti model runway, kaya raya, berpendidikan tinggi..."

    erik f_worried_down "Ya, oke... Tapi-"

    anon "Gadis seperti itu hanya berkencan dengan atlet atau musisi terkenal."

    erik f_woozy "Saya bisa menjadi seorang musisi."

    anon @ f_skeptical "Sobat, seriuslah."

    erik "Saya serius!"

    show erik a_binocular_look with dissolve:
        unflip
        xoffset -225
    erik "Menghormati karakterku dan menjadi seorang bard adalah hal yang sederhana."

    anon f_unimpressed @ -m_talk "..."
    show erik f_normal a_binocular with dissolve:
        flip
        xoffset 125
    erik "Bard tidak memiliki daya tarik seks maskulin seperti paladin tetapi mereka mendapatkan nilai karisma yang lebih tinggi..."

    erik f_thinking "Menurutmu apakah aku punya peluang lebih besar untuk merayunya dengan kecapi atau harpa?"

    pause
    show anon a_binocular
    show erik a_idle behind anon
    with dissolve
    anon "Beri aku itu!"

    erik f_worried "Hai!!"

    anon a_binocular_look f_normal_out "Anda benar-benar harus berhenti berbicara tentang video game..."

    erik f_angry "Mungkin dia suka video game... Pernahkah kamu mempertimbangkannya?!"

    anon "Tidak."


    scene location_rump_backyard_spy06 with fade
    pause
    anon "Hah."

    erik "Bagaimana sekarang?!"

    anon "Tidak ada apa-apa, hanya seorang pelayan yang membawakannya minuman."

    pause
    anon "Hmm, penasaran apakah seragam itu wajib?"

    erik "Seragam?"

    anon "Ya, dia mengenakan seragam pelayan yang sangat minim."

    erik "Ya ampun... Benarkah?!"

    erik "Karena aku punya barang ini untuk pelayan seksi, kawan!"


    scene location_treehouse_window_behind
    show erik:
        xoffset -280
        yoffset -100
    show anon a_binocular f_snarky:
        flip
        xoffset -115
        yoffset -75
    show location_treehouse_window
    with fade
    anon "Untuk apa Anda tidak mempunyai \"sesuatu\"?"

    erik @ f_laugh "Hehe, benar."

    show anon a_binocular_look f_normal_out with dissolve
    pause
    erik "Minuman apa yang dia bawakan untuknya?"

    anon "Saya tidak tahu."

    anon "Mengapa itu penting?"

    erik f_thinking "Karena, jika aku ingin memenangkan hatinya, penting bagiku untuk mengetahui apa yang dia suka dan tidak suka..."

    anon @ -m_talk "Mhmm."

    pause
    erik f_normal "Apa yang dia lakukan sekarang?"

    anon "Aku tidak tahu."

    erik f_worried "Bagaimana mungkin kamu tidak tahu?"

    anon "Karena aku sudah move on!"

    anon "Kami mencoba mengintip walikota, ini... Ingat?"

    erik f_sad_down "Aduh."

    pause
    anon f_shock "!!!"

    scene location_rump_backyard_spy04 with fade
    anon "Itu dia!"

    erik "Anda menemukannya?"

    erik "Apa yang dia lakukan?"

    pause
    anon "Aduh, kawan... Gadis malang itu."

    erik "Hah?"

    anon "Dia berendam di bak mandi air panas bersama gadis yang baru kukenal dan suaminya yang SANGAT menyebalkan..."

    erik "Oh."

    pause
    erik "Apakah dia seksi?"


    scene location_treehouse_window_behind
    show erik f_woozy:
        xoffset -280
        yoffset -100
    show anon a_binocular f_confused:
        flip
        xoffset -115
        yoffset -75
    show location_treehouse_window
    with fade
    anon "Apa bedanya?"

    erik "Menurutku, tidak..."

    show anon a_binocular_look f_normal_out with dissolve
    pause
    erik @ f_laugh "Tapi sebenarnya, apakah dia seksi?"

    anon f_worried "... Dia terlihat menyedihkan!"

    show erik f_worried with dissolve:
        flip
        xoffset 125
    erik "Benar-benar?"

    anon a_binocular "Ya, kawan... Aku merasa kasihan padanya."

    erik "Dapatkah saya melihat?"

    show erik a_binocular
    show anon a_idle behind erik
    with dissolve
    erik f_normal "Terima kasih."

    show erik a_binocular_look with dissolve:
        unflip
        xoffset -225
    pause
    erik @ -m_talk "Hmm."

    pause
    anon "Anda melihatnya?"

    erik f_woozy "Oh, aku melihatnya!"

    pause
    erik "Kawan, aku rela memberikan apa pun demi mendapat kesempatan mendapatkan barang rampasan itu..."

    anon f_confused "Hah?"

    show erik f_normal_right a_binocular with dissolve
    erik "Mereka bilang itulah penyebab mata merahmu; tapi baginya, aku berani mengambil risiko!"

    show erik f_woozy a_binocular_look with dissolve
    anon f_unimpressed "Apakah kamu membohongi putri walikota lagi?!"

    erik "Tidak."

    anon f_angry "Baiklah, kembalikan."

    erik "Tunggu."

    anon "{b}Erik{/b}, aku serius!"

    erik "Mmm, itu seperti sebuah karya seni..."

    pause
    erik "... Beri aku tiga setengah menit... Bahkan mungkin empat--OH SIALAN!"

    show erik f_surprised a_idle with dissolve:
        xoffset -315
        yoffset 225
    anon f_surprised_low "Apa yang-"

    erik "Oh sial, oh sial, oh sial!"

    anon f_worried_low "Kenapa kamu ada di lantai?"

    erik "Saya pikir dia melihat saya!"

    anon f_shy_low "Apa maksudmu dia melihatmu?!"

    erik "Maksudku, dia menatap langsung ke arahku!"

    erik "Dengan matanya!!"

    anon @ f_eyeroll "Tidak uh."

    erik "Bung, aku tidak bercanda!"

    anon a_binocular_look f_normal_out "Kami seperti seratus meter jauhnya dari-"


    scene location_rump_backyard_spy07 with fade
    anon "Hah."

    pause
    anon "Anda benar, dia sedang menatap ke arah kita."

    erik "Sudah kubilang!!"

    pause

    scene location_treehouse_window_behind
    show anon a_binocular f_surprised_low:
        flip
        xoffset -115
        yoffset -75
    show erik f_surprised:
        xoffset -315
        yoffset 225
    show location_treehouse_window
    with fade
    erik "Apa yang kita lakukan?"

    anon f_surprised "Aku tidak tahu!"

    pause
    anon a_binocular_look f_worried "Sekarang dia bangun."

    erik "Apakah dia terlihat marah?"

    anon "Dia terlihat sangat marah."

    erik "Ya Tuhan!"

    pause
    anon "Umm, dia datang ke sini..."

    erik "Haruskah kita lari?"

    erik "Aku merasa kita harus lari!"

    hide erik
    show anon f_worried_low a_binocular
    with {'master': dissolve}
    anon "Kemana kita akan lari?!"

    show anon a_sides with {'master': dissolve}:
        unflip
        xoffset 230
    anon "kita berada di pohon..."

    hide anon with {'master': dissolve}
    anon "... Dan kamu butuh waktu sekitar lima belas menit untuk mendaki ke sini."


    scene location_treehouse_floor_day
    show erik b_knees f_worried:
        flip
        xoffset -150
    show anon b_onbed_back f_worried behind erik:
        flip
    erik "Hey, don't poke fun!" with fade
    erik "Anda tahu saya menderita aritmia jantung!"

    anon "Tidak, jangan!"

    erik "Yah, aku bisa saja... Kamu tidak tahu!"

    anon "Nyonya rumahmu mengarang cerita itu untuk mengeluarkanmu dari kelas olahraga!"

    erik "Apakah kamu yakin dia datang ke sini?!"

    erik "Mungkin dia melupakan kita?"

    anon "Saya meragukannya."

    anon "Angkat kepalamu dan lihat!"

    erik "Tidak mungkin, kawan!"


    scene location_treehouse_cutscene01
    show text _ ("She had, indeed, not forgotten about us.") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("The mayor's daughter was marching her way over and she was none too pleased that we'd been spying.") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("My mind was racing, trying to come up with some way to get out of this...") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("... Meanwhile, Erik was having a panic attack.") as caption with dissolve
    pause

    scene location_treehouse_floor_day
    show anon b_onbed_back f_worried:
        flip
    show erik b_knees f_worried:
        flip
        xoffset -100
    with fade
    erik "Aduh, kawan... Kenapa aku tidak membawa inhalerku!"

    anon "Tenang aja."

    erik f_surprised "Tenang?!"

    erik "Dia putri walikota, kawan!"

    erik f_worried "Kita akan berakhir di bunker di suatu tempat, terkena waterboarding oleh Secret Service!"

    anon @ f_laugh "Tidak, kami tidak."

    anon "Hanya berjongkok dan diam."

    anon "Mungkin dia akan mengira kita kabur."

    erik "Maksudmu bersembunyi?!"

    anon "Ya, sembunyikan."

    erik "Tapi aku payah dalam bersembunyi!"

    anon @ f_confused "Hah?"

    erik "Skor ketangkasanku minus empat!"

    show anon f_unimpressed
    erik "Dan armorku dipenuhi dengan cahaya suci!"

    anon "Ssst!!"

    erik f_surprised "Aku bersinar dalam gelap, kawan!"

    erik f_worried_down "Ya ampun."

    erik f_worried a_cover_face "Aku tidak terlihat, aku tidak terlihat, aku tidak terlihat!"

    anon f_angry "{b}Erik{/b}, diam!"

    erik "Berhentilah berteriak padaku!"

    anon f_unimpressed @ -m_talk "..."
    erik a_idle "{i}*Huh*{/i} Seharusnya aku menjadi seorang penyihir..."

    erik "... Seorang penyihir bisa memindahkan kita keluar dari kekacauan ini."

    iwanka "Aku tahu kamu di atas sana, cabul!"

    show erik f_surprised
    show anon f_surprised
    iwanka "Aku bisa mendengarmu berbisik pada dirimu sendiri!"

    erik a_cover_face "Eee!"

    anon f_worried "Sial, {b}Erik{/b}..."

    iwanka "Ayo tunjukkan dirimu!"

    pause
    anon "Haruskah kita mengatakan sesuatu?"

    erik "Bung, tidak!"

    erik "Abaikan saja dia dan mudah-mudahan dia akan pergi."

    pause
    iwanka "Aku tidak akan pergi sampai kamu menunjukkan dirimu!"

    anon f_unimpressed "Ada ide cemerlang lainnya?"

    erik a_idle f_worried_down "Mungkin ini hanya mimpi buruk?"


    scene location_treehouse_cutscene02
    show text _ ("It was not.") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("As we tentatively crept to the edge of the hatch, the mayor's daughter came into view.") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("Looking quite livid in her skimpy teal swimsuit.") as caption with dissolve
    pause

    scene location_treehouse_floor_day
    show anon b_onbed_back f_worried:
        flip
    show erik b_knees f_worried_down a_cover_face:
        flip
        xoffset -100
    with fade
    erik "Ugh, aku akan muntah."

    anon f_surprised "Jangan muntah!"

    erik "Kawan, mau bagaimana lagi... Itu adalah mekanisme pertahanan!"

    anon f_worried "Saya yakin kita bisa meminta maaf dan semuanya akan baik-baik saja..."

    iwanka "Turunkan dirimu ke sini, sekarang juga!"

    erik a_idle f_worried "Oke, rencana baru."

    erik "Anda turun dan meminta maaf ..."

    erik "... Aku akan tetap di sini dan mengawasi."

    anon f_unimpressed @ -m_talk "..."
    erik f_surprised "Apa?!"

    erik "Tidak ada alasan kami berdua harus mati!"

    iwanka "Baiklah, itu saja, brengsek..."

    iwanka "... aku datang!"

    anon f_surprised "!!!"
    erik "!!!"
    pause
    erik f_worried a_cover_face "D-dia bercanda, kan?"


    scene location_treehouse_cutscene03
    show text _ ("She was not.") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("In fact, she was ascending our makeshift ladder with surprising speed.") as caption with dissolve
    pause

    scene location_treehouse_cutscene04
    show text _ ("I swallowed hard and looked at my friend, wondering exactly what it felt like to be waterboarded...") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("Surely, it wouldn't come to that... Right?") as caption with dissolve
    pause

    scene location_treehouse_floor_day
    show anon b_onbed_sit f_worried:
        xoffset 200
    show erik b_knees f_surprised m_talk:
        flip
        xoffset -100
    with fade
    show iwanka b_knees_standing:
        xoffset 100
    show erik f_thinking
    show anon f_worried_high
    with dissolve
    iwanka "Oh, jadi kalian berdua ya?"

    anon "Dengar, aku tidak tahu apa yang menurutmu kamu lihat, tapi kami-"

    show iwanka b_knees f_annoyed:
        xoffset 200
    show erik f_surprised
    show anon f_worried
    with dissolve
    iwanka "Saya tahu persis apa yang saya lihat!"

    iwanka @ a_point "Anda memata-matai saya dengan teropong!"

    anon "Y-ya, oke... Aku menggunakan teropong tapi aku tidak memata-mataimu, aku bersumpah!"

    iwanka "Eh ya."

    iwanka "Apakah ini bagian di mana kamu memberitahuku bahwa kamu hanya mengamati burung?"

    anon "T-tidak."

    iwanka "Karena aku pernah mendengar kalimat omong kosong itu sebelumnya!"

    anon "Saya mencoba memata-matai walikota!"

    iwanka f_disgusted "Eugh, kamu punya fetish orang tua atau semacamnya?"

    anon f_surprised "Apa?!"

    anon f_disgusted @ a_scared "Eww, tidak!"

    anon "Itu bukan hal seksual!"

    iwanka f_thinking "Eh ya."

    anon f_worried "Sebenarnya, ini agak rumit."

    anon "Begini, menurutku ayahku mungkin bekerja di perusahaanmu dan-"

    iwanka "Apakah lampu ini berfungsi?"

    anon @ f_confused "Hah?"

    iwanka f_annoyed "Lampu Natal, apakah berfungsi?"

    anon "Ya, kenapa?"

    iwanka f_normal "Aku hanya tidak menyangka tempat ini akan begitu..."

    anon "Norak?"

    iwanka @ f_laugh "Rumah pertanian yang cantik!"

    anon "Saya tidak tahu apa maksudnya."

    iwanka "Itu seperti, menawan... Tapi dengan cara yang sederhana dan sederhana."

    anon "Oh?"

    iwanka "Ya, saya agak menyukainya."

    anon "I-itu bagus, menurutku..."

    iwanka f_suspicious "Siapa kalian?"

    anon @ -m_talk "Hmm?"

    iwanka "Misalnya, siapa namamu?"

    anon f_normal @ f_surprised "Oh!"

    anon @ a_wave "Ehh, namaku {b}[firstname]{/b}."

    show iwanka f_normal
    anon @ f_normal_left a_nudge "Dan ini sahabatku {b}Erik{/b}."

    pause
    iwanka f_suspicious "Apakah dia baik-baik saja?"

    anon f_worried_left "Y-ya, dia kadang-kadang mengunci diri..."

    anon f_shy "... Saat dia berada di dekat gadis-gadis cantik."

    iwanka "Aneh."

    anon f_worried "Ya."

    pause
    anon "Um, siapa namamu?"

    iwanka f_surprised "Maksudmu, kamu tidak tahu?"

    anon "T-tidak, maaf."

    iwanka "Itu mengejutkan."

    iwanka f_normal "Biasanya saat aku bertemu orang baru, mereka tahu lebih banyak tentangku daripada orang tuaku yang ketakutan..."

    anon "Ehh, ya... Maafkan saya, saya tidak terlalu tertarik dengan politik."

    iwanka a_hand "Saya {b}Iwanka{/b}."



    show iwanka a_hand_shake
    show anon a_empty f_normal
    with dissolve
    anon "{b}Iwanka{/b} ya?"

    anon "Itu nama yang unik."

    show iwanka a_idle
    show anon a_idle
    with dissolve
    iwanka @ f_bored "Ya, menurutku."

    anon "Dan Anda putri walikota?"

    iwanka @ f_snob "Satu-satunya miliknya."

    pause
    iwanka "Jadi apa yang kalian lakukan untuk bersenang-senang di sini?"

    anon @ -m_talk "Hmm?"

    iwanka @ f_eyeroll "Aku sudah terjebak di sini selama beberapa minggu dan aku benar-benar sekarat karena bosan!"

    anon "Oh?"

    iwanka @ f_eyeroll "Sama sekali tidak ada apa pun di sini!"

    iwanka "Hanya sebuah mal kecil dengan satu bioskop dan tidak ada pusat perbelanjaan yang layak..."

    anon @ -m_talk "..."
    iwanka "Tidak ada klub dansa, tidak ada bar... Bahkan tempat tari telanjang pun tidak ada!"

    anon f_shy "Ya, yang terakhir ini mengejutkan bukan?"

    iwanka "Serius, pasti ada sesuatu yang menyenangkan untuk dilakukan di kota ini!"

    iwanka "Dan tolong jangan katakan tip sapi."

    anon f_normal "Ya, saya kira kebanyakan orang seusia kita mengadakan pesta."

    iwanka f_surprised "Ya!"

    iwanka f_normal @ f_laugh "Pesta!"

    iwanka "Sekarang kita sampai di suatu tempat!"

    iwanka @ f_suspicious "Di mana saya dapat menemukan salah satu pesta ini?"

    anon @ f_thinking "Ehh, aku tidak yakin..."

    iwanka "Kamu tidak yakin, misalnya, kamu khawatir mereka tidak menginginkanku di sana atau semacamnya?"

    anon f_worried "T-tidak."

    anon f_sad_down "Aku hanya tidak diundang ke banyak pesta... Itu saja."

    iwanka f_pouting "Oh."

    iwanka f_annoyed "Sial!"

    iwanka f_normal "Anda satu-satunya orang seusia saya yang saya temui sejak saya berada di sini..."

    anon f_normal @ f_surprised "Oh?"

    iwanka f_pouting "Ya, ayahku jarang mengizinkanku keluar."

    iwanka @ f_eyeroll "Dia sangat kesal karena aku gagal lulus kuliah dan dia suka, ingin aku terjun ke dunia politik dan mungkin menjadi presiden wanita pertama atau semacamnya..."

    iwanka "... Tapi aku semua berpikir, \"Bagaimana dengan mimpiku, ayah?!\""

    iwanka @ f_suspicious "Bukankah orang tualah yang terburuk?"

    anon "Uhh."

    iwanka a_mime "Itu saja, \"Kamu tidak bisa lepas begitu saja, {b}Iwanka{/b}...\""

    iwanka "Dan, \"Berhentilah bersikap pelacur di depan umum!\""

    iwanka @ f_eyeroll "Bla, bla, bla..."

    iwanka f_annoyed a_idle "Sementara itu, dia dan {b}Ibu{/b} saling membantu dan mengadakan pesta pesta seks..."

    anon f_surprised "O-pesta pesta seks?"

    iwanka f_disgusted "Eugh, kamu tidak ingin tahu, percayalah."

    iwanka "Ini sangat menjijikkan!"

    iwanka "Sekelompok lelaki tua kaya yang menukar istri piala mereka."

    iwanka "Setengahnya bahkan tidak bisa berbahasa Inggris!"

    anon @ -m_talk "..."
    iwanka "Anda seharusnya melihat pria Rusia yang dia temui terakhir kali..."

    iwanka "... Dia tampak seperti goblin!"

    anon @ f_surprised_teeth "!!!"
    anon "Anda tidak mengatakannya!"

    anon "Apa lagi yang bisa kamu ceritakan tentang dia?"

    iwanka f_normal "Apa, si goblin?"

    anon "Apakah namanya {b}Raz Chernyshevsky{/b}?"

    iwanka f_disgusted b_knees_back @ f_eyeroll a_wave "Um, siapa yang peduli?!"

    iwanka "Dia menjijikkan!"

    anon f_worried "Ya, tapi-"

    iwanka "Dia mencoba mengangkat tangannya ke atas rokku dan aku bilang padanya aku akan lebih cepat bercinta dengan keledai daripada dia!"

    anon "Apakah Anda yakin dia orang Rusia?"

    iwanka f_normal "Tidak."

    pause
    iwanka @ f_eyeroll "Bisakah kita membicarakan hal lain?"

    anon @ -m_talk "..."
    iwanka f_suspicious "Anda benar-benar tidak tahu ada pesta apa pun?"

    show anon f_thinking
    pause
    anon f_normal "Anda tahu, saya pikir saya mungkin tahu satu hal..."

    iwanka f_surprised "Benar-benar?"

    anon f_normal_left "Bagaimana menurut anda {b}Erik{/b}?"

    erik "..."
    show iwanka f_suspicious
    anon f_worried_left "{b}Erik{/b}?"

    show anon a_nudge with dissolve
    erik -m_talk @ -m_talk "!!!"
    show anon a_idle with dissolve
    erik "H-hah?"

    erik f_worried "Dimana saya?"

    anon "Bolehkah kami mengadakan pesta untuk putri walikota di ruang bawah tanahmu?"

    erik f_surprised m_talk "I-Walikota... Putri..."

    show iwanka f_laugh a_wave with dissolve
    iwanka "Halo!"

    show iwanka f_normal a_idle with dissolve
    erik "..."
    anon f_normal @ f_laugh "Cukup yakin itu adalah ya."

    iwanka @ f_laugh "Luar biasa!"

    anon "Ini mungkin bukan jenis pesta yang biasa Anda lakukan, tetapi-"

    iwanka @ f_eyeroll "Jangan khawatir, semuanya lebih baik daripada duduk-duduk bersama orang tuaku!"

    pause
    iwanka f_suspicious "Kecuali..."

    iwanka "... Akan ada alkohol di pestamu, kan?"

    anon "Tentu saja."

    iwanka f_normal @ f_laugh "Oke bagus!"

    anon "Rumahnya yang hijau, di sebelah sana."

    iwanka "Ya Tuhan, rasanya menyenangkan jika dilepaskan lagi!"

    iwanka "... Aku benar-benar akan menjadi gila jika berdiam diri di rumah itu."

    anon "Sampai jumpa malam ini?"

    iwanka f_smirk "Ya, aku akan menyelinap ke sekitar jam sepuluh."

    show iwanka b_knees_standing:
        xoffset 100
    show anon f_normal_high
    with dissolve
    pause
    iwanka "Oh!"

    show iwanka b_knees_back_pull f_normal:
        xoffset 150
    show anon f_normal
    with dissolve
    iwanka "Apa aturan berpakaiannya?"

    anon f_worried "Kode berpakaian?"

    iwanka f_smirk "Ya, apakah kamu berpikir seperti, gaun koktail?"

    anon f_shy "Ehh, masuk saja sesukamu yang membuatmu nyaman."

    iwanka "Menarik..."

    show iwanka b_knees_back with dissolve
    iwanka f_normal "Oke, aku akan memikirkan sesuatu."

    iwanka @ a_wave "Sampai jumpa malam ini!"

    anon f_normal "Nanti, {b}Iwanka{/b}."

    hide iwanka with dissolve
    pause
    anon f_normal_left "Fiuh, itu tidak terduga!"

    anon "Dia akhirnya menjadi sangat keren."

    anon "Agak terlalu cerewet tapi... Sepertinya dia punya informasi tentang bos mafia Rusia itu."

    anon "Bukankah begitu?"

    erik "..."
    anon f_worried_left "Bung, serius?!"

    show anon a_nudge with dissolve
    erik -m_talk @ -m_talk "!!!"
    show anon a_idle with dissolve
    erik "H-hah?"

    erik f_worried "Dimana saya?"

    anon f_sad_down "{i}*Huh*{/i}"


    $ player.go_to(L_treehouse)
    scene expression background(512, 576, 7.) as stage
    show anon
    show erik f_surprised
    with slowfade
    erik "Jadi putri walikota yang sangat seksi akan datang ke rumahku malam ini?!"

    anon "Ya."

    erik "... Untuk pesta?"

    anon "Ya."

    erik f_worried "Tapi aku belum pernah mengadakan pesta sebelumnya..."

    anon "Tenang, itu tidak harus menjadi pesta yang bagus."

    anon "Kami hanya akan menyalakan musik dan menari atau semacamnya... Cobalah untuk menunjukkan padanya saat-saat yang menyenangkan, Anda tahu?"

    erik f_surprised "Menari?"

    erik "Saya tidak menari, {b}[firstname]{/b}."

    anon "Tidak apa-apa."

    anon "Pastikan saja ada banyak alkohol, ya?"

    erik f_normal @ f_laugh "Oh, saya bisa mendapatkan {b}Ny. Johnson{/b} buatlah knish!"

    anon "Tidak!"

    erik f_worried "Tidak ada knish?"

    anon "Itu hanya akan membuatnya aneh."

    anon "Makanan biasa, seperti keripik kentang atau kue atau apalah..."

    erik f_normal @ f_laugh "Oh baiklah!"

    anon "Luar biasa."

    erik f_worried "Umm, kamu akan berada di sana sebelum dia muncul, kan?"

    anon "Heh iya {b}Erik{/b}."

    erik "B-bagus."

    erik "Karena aku tidak yakin bisa berbicara dengannya."

    anon "Apa yang terjadi dengan pembicaraan \"Dia calon istriku!\"?"

    erik "Ya..."

    erik @ f_normal "... Maksudku, di {i}jauh{/i} masa depan."

    erik "Tidak malam ini."

    anon "Cobalah untuk tidak mengunci lagi."

    anon "Saya mungkin memerlukan bantuan untuk menggali informasi darinya."

    erik f_worried_down @ -m_talk "..."
    anon "Sampai jumpa {b}malam ini{/b}, oke?"

    erik f_worried "Ya baiklah."

    hide erik with dissolve
    pause
    anon @ f_thinking -m_talk "(Hmm, saya harap ini berhasil...)"

    anon a_thinking @ -m_talk "(Saya tidak akan pernah masuk ke dalam rumah {b}Rump{/b} sendirian dan {b}Iwanka{/b} adalah satu-satunya petunjuk yang saya miliki... )"

    anon a_idle f_worried @ -m_talk "( ... {b}Malam ini{/b} di {b}rumah Erik{/b} mungkin satu-satunya kesempatanku! )"

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
