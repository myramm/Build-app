label button_grace_why_meditate_naked:
    anon f_worried "Mengapa Anda bermeditasi telanjang?"

    grace a_cover "Itu bagian dari teknik relaksasi dalam buku saya."

    grace "Bebas dengan tubuh Anda membantu menghilangkan kecemasan."

    anon f_surprised "Kecemasan menguap?"

    grace @ f_laugh "Hehe, seharusnya..."

    pause
    anon f_worried "Apakah ini berhasil?"

    grace "Ya, menurutku begitu."

    pause
    grace f_uneasy_back "Maaf, aku tahu mungkin aneh melihat adik pacarmu telanjang sepanjang waktu..."

    anon f_flirt a_point "Hehe, aku tidak mengeluh."

    show grace f_uneasy
    anon "Anda memiliki tubuh yang luar biasa!"

    show anon f_flirt_grin a_idle with dissolve
    grace f_uneasy a_idle "O-oh, umm... terima kasih, {b}[firstname]{/b}."

    anon f_flirt "Terima kasih kembali."

    return

label button_grace_is_she_here:
    anon f_worried "Apakah dia di sini?"

    grace "Y-ya."

    grace "{i}*Ahem*{/i} Jika dia tidak ada di kamarnya, dia mungkin ada di atap."

    anon @ f_laugh "Baiklah terima kasih!"

    grace "T-tidak masalah."

    show anon f_flirt_grin
    pause
    show grace f_uneasy_back
    show anon f_normal
    pause
    show grace f_uneasy
    return

label button_grace_just_saying_hi:
    anon "Maaf, saya tidak bisa tinggal."

    anon "Saya baru saja melihat Anda di sini bekerja dan berpikir saya akan menyapa."

    grace f_happy @ f_laugh "O-oh, baiklah, kamu baik sekali!"

    pause
    grace "Anda harus datang nanti."

    anon "Oh?"

    grace "Ya!"

    pause
    grace "K-kamu tahu, untuk menemui adikku."

    anon @ f_laugh "Hehe, cukup!"

    grace "Nanti, {b}[firstname]{/b}."

    hide anon with dissolve
    return

label button_grace_you_and_odette:
    anon "Apakah kamu dan {b}Odette{/b} baik-baik saja?"

    grace f_happy @ f_laugh "Ya, dia sangat membantu akhir-akhir ini!"

    grace "Agak sulit dipercaya, jika saya jujur."

    anon "Saya senang mendengarnya."

    anon @ f_flirt "Kalian berdua adalah pasangan yang serasi."

    if player.location == L_tattooparlor_interior:
        grace a_neck f_uneasy "Oh, uhh... terima kasih, {b}[firstname]{/b}."

    else:
        grace f_uneasy "Oh, uhh... terima kasih, {b}[firstname]{/b}."

    show anon a_point with dissolve
    if player.location == L_tattooparlor_interior:
        show grace f_uneasy a_crossed with dissolve
    else:
        show grace f_uneasy
    anon "Terima kasih kembali."

    show anon a_idle f_normal with dissolve
    return

label button_grace_really:
    anon f_surprised "Benar-benar?"

    grace f_happy "Ya."

    grace "Yang saya dengar saat ini hanyalah, \"{b}[firstname]{/b} ini...\" atau \"{b}[firstname]{/b} itu...\""

    anon f_normal @ f_laugh "Haha!"

    grace "Jangan salah paham, senang sekali kalian berdua menjadi begitu dekat."

    grace "Aku tidak yakin aku pernah melihatnya sebahagia ini sebelumnya."

    anon "Ya, aku juga senang dengan hal itu."

    grace f_laugh @ f_angry a_idea "Pastikan saja kamu merawatnya dengan baik, jika tidak, aku akan {b}Odette{/b} menyerangmu."

    anon @ f_worried a_behind_head "Hehe, aku akan melakukannya."

    show grace f_normal
    return

label button_grace_bike:
    anon "Apakah sepeda Anda masih berjalan dengan baik?"

    grace @ f_proud "Oh, seperti mimpi!"

    grace "Sekali lagi terima kasih telah memperbaikinya."

    anon "Tidak masalah."

    anon "Di mana kamu mendapatkannya?"

    grace "Saya mengeluarkannya dari tumpukan sampah di tempat pembuangan sampah ketika saya berumur sembilan belas tahun."

    anon @ f_surprised "Benar-benar?!"

    grace @ f_proud "Ya."

    grace "Butuh waktu dua tahun bagi saya untuk mendapatkan uang untuk memperbaikinya."

    anon "Itu sepeda yang cantik."

    grace "Ah, terima kasih."

    grace @ f_sexy "Mungkin suatu saat aku akan mengajakmu jalan-jalan?"

    anon @ f_laugh a_cheering "Saya ingin itu!"

    return

label button_grace_eve_around:
    anon "{b}Malam{/b} sekitar?"

    grace "Hmm, saya tidak yakin."

    grace "Jika Anda tidak dapat menemukannya di sekolah, dia mungkin sedang nongkrong di atap."

    grace @ a_idea "Dia menghabiskan waktu luangnya di sana sejak insiden taman."

    anon "Oh baiklah."

    anon @ f_laugh "Terima kasih!"

    return

label button_grace_apologize:
    anon f_worried "Aku ingin meminta maaf atas semua yang terjadi di taman..."

    grace a_hips_mad "Tidak, itu bukan salahmu, {b}[firstname]{/b}."

    anon "Itu benar-benar hanya nasib buruk."

    grace f_tired @ f_eyeroll "Oh, tentu saja... sial."

    grace "Sungguh sial karena saudara perempuan saya mencuri setengah pon ganja dan kemudian menyala-nyala di depan umum."

    show anon f_surprised_teeth
    pause
    anon f_worried @ f_thinking a_thinking "Nah, ketika Anda mengatakannya seperti itu..."

    grace f_normal "Dengar, aku mengerti."

    grace "{b}Odette{/b} dan aku juga melakukan hal-hal bodoh di kampus."

    grace f_sad "Saya hanya berharap {b}Eve{/b} akan bertindak lebih pintar dari kami."

    anon f_worried @ -m_talk "..."
    grace f_suspicious "Bisakah kamu membantuku?"

    anon "T-tentu saja."

    grace f_normal "Awasi adikku dan pastikan dia tidak melakukan hal bodoh seperti itu lagi."

    anon f_normal a_behind_head "Ya, saya akan mencoba."

    grace "Terima kasih, {b}[firstname]{/b}."

    show anon a_idle with dissolve
    return

label button_grace_how_work_going_e6:
    anon "Bagaimana kabar pekerjaannya?"

    grace f_sad a_neck "Lambat."

    anon "Tidak banyak pelanggan ya?"

    grace "Tidak."

    pause
    grace f_normal a_idle "Anda tahu, mengingat kami satu-satunya salon tato di kota ini, Anda mungkin mengira kami punya lebih banyak bisnis."

    anon "Ya, tapi sekali lagi, ini adalah kota yang sangat kecil."

    grace "BENAR."

    grace "Saya mungkin seharusnya membeli tempat di kota..."

    pause
    grace @ f_sad_down "{i}*Huh*{/i} Sudah terlambat sekarang."

    return

label button_grace_how_work_going_e18:
    grace @ f_laugh "Segalanya menjadi lebih baik, berkat {b}Eve{/b} dan Anda!"

    anon "Itu bagus untuk didengar."

    grace @ f_eyeroll "Ya, ceritakan padaku tentang hal itu."

    grace "Saya sangat khawatir saya akan kehilangan toko."

    grace "Sekarang, satu-satunya hal yang saya khawatirkan adalah menemukan waktu untuk semua pelanggan ini!"

    anon @ f_laugh "Haha!"

    anon @ f_snarky a_point "Hanya saja, jangan terlalu memaksakan diri, oke?"

    grace "Oh, aku baik-baik saja."

    grace "Tidak perlu khawatir tentang saya."

    return

label button_grace_odette_and_tuuku:
    anon f_skeptical "Jadi, apakah {b}Odette{/b} dan {b}Tuuku{/b} tinggal di sini bersama {b}Eve{/b} dan kamu?"

    grace @ f_eyeroll "Uhh, ya dan tidak."

    grace "Mereka punya tempat sendiri, tapi sebagian besar waktunya dihabiskan di sini."

    grace "{b}Odette{/b} tidur di sofa kami hampir setiap malam dan {b}Tuuku{/b} memiliki tenda di atap kami."

    anon f_surprised "Dia tidur di atap rumahmu?"

    grace "Ya, terkadang."

    pause
    anon f_confused "Apakah mereka membayar Anda sewa atau semacamnya?"

    grace @ f_laugh "Oh tidak!"

    grace "Saya tidak bisa meminta mereka melakukan itu."

    anon f_surprised "Kenapa tidak?"

    grace "Kami sudah berteman sejak kami masih kecil, mereka bisa dibilang keluarga!"

    anon f_normal "Kamu baik sekali."

    grace @ f_happy "Ya, saya tahu."

    grace "Jangan beri tahu mereka aku mengatakan ini, tapi senang rasanya ada mereka."

    grace @ f_eyeroll "Aku mungkin akan menjadi gila, terjebak di sini sepanjang hari sendirian."

    return

label button_grace_yup:
    anon "Dia ada di sekitar?"

    show grace f_thinking
    pause
    grace f_normal "Hmm, aku tidak yakin..."

    grace "Jika Anda tidak dapat menemukannya di sekolah, dia mungkin sedang nongkrong di taman."

    grace "Dia suka menggambar di sana."

    anon "Oh baiklah."

    anon @ f_laugh "Terima kasih!"

    return

label button_grace_nevermind:
    anon "Saya hanya melihat-lihat, terima kasih."

    grace "Oke."

    grace @ a_idea "Semua pekerjaan saya sebelumnya ada di buku dekat pintu, jika Anda ingin memeriksanya."

    anon "Baiklah, cukup."

    hide anon with dissolve
    return

label button_grace_i_should_go:
    anon "Sebenarnya, aku hanya ingin mampir dan menyapa."

    anon "Bisakah Anda memberi tahu {b}Eve{/b} saya mampir?"

    grace "Tentu."

    anon @ a_wave "Terima kasih, {b}Grace{/b}."

    grace "Sampai jumpa, {b}[firstname]{/b}."

    hide anon with dissolve
    return

label button_grace_tattoo:
    grace "Anda tertarik untuk mendapatkan tinta?"

    anon @ f_surprised -m_talk "Hmm?"

    anon "Oh, heh... tidak, terima kasih."

    anon f_unimpressed "Itu akan menjadi terlalu banyak pekerjaan yang harus dilakukan oleh pengembang... Maksudku, aset seninya saja yang akan-"

    grace f_suspicious "Hah?"

    pause
    anon a_behind_head f_grin @ f_surprised "Maksudku, induk semangku akan membunuhku!"

    grace "O-oh."

    grace f_normal "Ya, saya bisa memahaminya."

    grace "Ibuku juga sama ketika aku seusiamu."

    pause
    grace "Beri tahu saya jika Anda berubah pikiran."

    show anon a_idle with dissolve
    return

label grace_button_intro_e1e5:
    scene expression player.location.background_closeup with None
    show anon
    show grace
    with dissolve
    grace "Selamat datang di {b}Gula Tats{/b}."

    grace "Apa yang bisa saya bantu?"

    return

label grace_button_intro_e5e14:
    scene expression player.location.background_closeup with None
    show anon
    show grace
    with dissolve
    grace "Selamat datang di {b}Gula Tats{/b}."

    grace "Bagaimana aku bisa-"

    grace "Oh, hai {b}[firstname]{/b}."

    anon @ a_wave "Hai, {b}Rahmat{/b}."

    grace @ f_suspicious "Kamu di sini untuk menemui adikku?"

    return

label grace_button_intro_e14e20:
    scene expression player.location.background_closeup with None
    show anon
    show grace
    with dissolve
    anon @ a_wave "Hai, {b}Rahmat{/b}."

    grace "Hai, {b}[firstname]{/b}!"

    grace f_happy "Senang bertemu denganmu!"

    anon "Y-ya, kamu juga."

    return

label grace_button_intro_final_apartment:
    scene expression player.location.background_closeup with None
    if M_grace.get("nude_meditation_first"):
        show anon f_shock with dissolve
    else:
        show anon f_worried a_behind_head with dissolve
    anon "{b}G-Grace{/b}?"

    grace "!!!"
    show grace f_uneasy b_naked a_cover with dissolve
    grace "H-hei, {b}[firstname]{/b}..."

    if M_grace.get("nude_meditation_first"):
        $ M_grace.set("nude_meditation_first", False)
        show anon f_worried a_behind_head with dissolve
    anon "Saya minta maaf mengganggu Anda."

    grace "Tidak apa-apa, beri aku waktu sebentar untuk memakai pakaian..."

    anon f_flirt a_idle "Jangan khawatir, saya tidak keberatan."

    grace f_uneasy a_idle @ f_uneasy_back "Heh, umm... {b}Eve{/b} tidak memberitahuku kalau kamu akan mampir?"

    return

label grace_button_intro_final_tattoo:
    scene expression player.location.background_closeup with None
    show anon
    show grace
    with dissolve
    anon "Hai, {b}Rahmat{/b}."

    grace "Hai, {b}[firstname]{/b}!"

    grace "Mencari saudara perempuanku?"

    grace @ f_eyeroll "Kau tahu, dia tidak bisa diam tentangmu..."

    return

label grace_button_massage_sex_proposal:
    scene location_tattoo_apartment_oil
    show odette b_massage_leaning f_smirk_down
    show grace b_massage_laying
    show odette_arms_massage_leaning_a_rub1_2
    with dissolve
    grace "Saya tidak percaya tindikan itu menghasilkan begitu banyak uang..."

    odette "Hehe, sudah kubilang itu akan membuat perbedaan."

    grace "Ya, tapi pada akhirnya pasti akan menurun."

    odette "Bisakah kamu bersantai?"

    odette "Kami mencoba melepaskan ketegangan Anda, bukan menciptakan lebih banyak ketegangan!"

    grace "Anda benar, saya minta maaf."

    pause
    grace "Ini memang terasa sangat enak..."

    odette "Nikmati saja, sayang."

    odette "Anda telah bekerja terlalu keras."

    grace "Hmm, aku tahu."

    hide odette_arms_massage_leaning_a_rub1_2
    show odette b_massage a_bottle1
    with dissolve
    odette "Tutup matamu dan biarkan aku melakukan sihirku."

    show odette a_bottle2 with dissolve
    pause
    show odette b_massage_leaning
    show odette_arms_massage_leaning_a_rub1_2
    with dissolve
    pause
    odette "Biarkan semua kekhawatiranmu sirna..."

    odette "... {b}Odette{/b} akan menangani semuanya."

    grace "Aneh sekali mendengarmu mengatakan hal seperti itu."

    odette "Ssst!"

    grace "Hehehe!"

    pause
    grace "{b}Eve{/b} nampaknya sangat bahagia akhir-akhir ini, bukan?"

    odette "Tentu saja."

    grace "Menurutku hubungan yang dia mulai {b}[firstname]{/b} memberikan banyak manfaat baginya."

    odette "Kontolnya yang besar itulah yang menguntungkannya..."

    grace "{b}Odette{/b}!!"

    odette "... Jangan berpura-pura tidak penasaran!"

    grace "..."
    grace "Menurutmu itu sebesar yang {b}Tuuku{/b} katakan?"

    odette "Yah, dia dikenal melebih-lebihkan..."

    odette "...Tetapi jika itu benar...bisakah anda bayangkan?"

    grace "Hmm?"

    odette "{b}[firstname]{/b} penisnya."

    grace "..."
    odette "Sudah lama sekali kamu tidak punya yang asli, ya?"

    grace "Hehe, itu pernyataan yang meremehkan."

    odette "Bayangkan saja betapa menyenangkan rasanya setelah sekian lama..."

    hide odette_arms_massage_leaning_a_rub1_2
    show odette_arms_massage_leaning_a_rub3_4
    with dissolve
    grace "{i}*Terkesiap*{/i}"

    odette "Tangannya yang kekar, membelai pahamu."

    grace "{b}Odette{/b}..."

    odette "Mulutnya yang hangat menggoda putingmu."

    grace "Kita tidak seharusnya membicarakan tentang-"

    odette "Besarnya."

    odette "Tebal."

    grace "Ahhh!"

    odette "Ayam yang berdenyut... meluncur di dalam dirimu."

    grace "Ngh!"

    odette "Menabrakmu."

    show expression "characters/grace/grace_sex_mc_foreground.png" with dissolve
    odette "Semakin sulit."

    grace "Ya Tuhan."

    anon "Ehh, h-hei kalian berdua..."

    grace "!!!"
    grace "OH SIALAN!!"

    show odette b_massage a_idle f_smirk
    hide odette_arms_massage_leaning_a_rub3_4
    show grace b_massage f_sad a_cover
    with dissolve
    grace "{b}[firstname]{/b}?!"

    odette @ f_laugh "Hehehe!"

    grace "B-berapa lama kamu-"

    odette "Tenang, dia baru saja sampai."

    anon "Maaf, saya tidak bermaksud menyela."

    anon "Saya di sini hanya untuk menemui {b}Eve{/b}."

    grace "O-oh."

    grace "Dia di kamarnya, bermain game."

    show grace f_sad_down
    anon "Baiklah, aku akan membiarkan kalian berdua kembali ke-"

    odette "Baiklah, tunggu sebentar."

    odette "Kau tahu, terpikir olehku bahwa kami tidak pernah mengucapkan terima kasih yang pantas atas semua yang telah kau lakukan untuk kami..."

    anon "Hmm?"

    odette "... Setidaknya aku merasa kamu pantas mendapatkan pijatan atau semacamnya."

    anon "!!!"
    grace f_sad_back "{b}Odette{/b}, kita tidak bisa begitu saja-"

    odette "Pikirkanlah, sayang!"

    odette "Maksudku, dia memang membantu mengembangkan bisnismu dengan ide pamflet itu..."

    odette "... Dan dia menginspirasi saya untuk membantu di sekitar sini..."

    odette "... DAN dia mengubah kehidupan kecil {b}Evie{/b} kami dengan cara yang positif dan bermakna!"

    grace "Y-ya, tapi-"

    odette "Anda sendiri yang mengatakannya, Anda belum pernah melihatnya begitu bahagia."

    grace f_sad_down "..."
    odette "Mengapa kamu tidak membuka pakaian dan berbaring di sini?"

    odette "{b}Grace{/b} memiliki tangan yang paling luar biasa."

    grace f_angry_back "{b}ODETTE{/b}!!!"

    odette "Apa?"

    grace "Dia adalah pacar {b}Eve{/b}!"

    odette "Saya tahu itu."

    odette "Itu hanya pijatan kecil yang polos, dasar pemalu..."

    grace a_idle f_tired_back "Sialan, berhentilah menyebutku pemalu!"

    odette @ f_eyeroll "Aku akan berhenti jika kamu berhenti bersikap seperti itu."

    grace f_sad_down @ f_eyeroll "Ugh."

    pause
    odette "Lihat, dia bersedia."

    grace f_tired_back "Hei, aku tidak mengatakan itu!"

    odette "Hehehe!"

    odette "Bagaimana menurutmu, kawan?"

    odette "{b}Evie{/b} bisa menunggu lebih lama lagi, bukan?"

    show grace f_sad
    return

label grace_button_massage_sex_proposal_yeah:
    anon "Ya, menurutku..."

    anon "... Selama kita cepat."

    odette @ f_laugh "Hehehe!"

    odette "Yah, semoga tidak TERLALU cepat."

    grace f_tired_back "{b}Odette{/b}!!"

    odette "Tenang, aku bercanda..."

    grace @ -m_talk "..."
    odette "Buka baju itu dan berbaring disini, {b}[firstname]{/b}."

    show grace f_sad
    return

label grace_button_massage_sex_proposal_dunno:
    anon "Dia agak mengharapkanku."

    grace f_sad_back "Lihat, dia bahkan tidak tertarik."

    odette "Ck, tentu saja!"

    odette "{b}Eve{/b} bahkan tidak akan menyadari bahwa kamu terlambat; dia berada di dunia kecilnya sendiri saat dia bermain game."

    grace f_tired_back "{b}Odette{/b}..."

    odette "Ini hanya akan memakan waktu sekitar lima belas menit dan kemudian Anda dapat langsung menemuinya."

    anon "..."
    show grace f_sad
    odette "Ayo kawan, bagaimana menurutmu?"

    anon "Hanya lima belas menit?"

    odette "Ya, kurang lebih..."

    grace "{b}[firstname]{/b}, Anda sebenarnya tidak perlu melakukan ini jika tidak ingin-"

    odette "Kamu diam!"

    odette "Tidak apa-apa, kemarilah."

    return

label grace_button_party_speak_to_tuuku:
    scene expression player.location.background_closeup with None
    show anon:
        xoffset -100
    show eve b_dress:
        flip
        xoffset 200
    show grace a_beer
    with dissolve
    grace "Kalian berdua bersenang-senang?"

    anon "Ya."

    grace f_sad "Anda tidak minum terlalu banyak, bukan?"

    eve f_angry @ f_eyeroll "Tidak, {b}Kak{/b}... Sejauh ini aku baru minum satu bir."

    grace f_normal "Bagus."

    pause
    eve "Anda tahu, sebagian besar pestanya ada di lantai atas, bukan?"

    grace @ f_eyeroll "Ya, saya tahu."

    eve "Jadi kenapa kamu merajuk di sini, di garasi?"

    grace f_angry "Aku tidak merajuk!"

    grace @ f_tired "Aku hanya merasa tidak nyaman dengan semua orang asing di rumah kami."

    grace "Mereka bisa saja merampok kita secara buta."

    eve @ f_eyeroll "Psh, tidak mungkin."

    hide anon with dissolve
    return

label grace_button_party_generic:
    scene expression player.location.background_closeup with None
    show anon
    show grace a_beer
    with dissolve
    grace "Lanjutkan dan maju, {b}[firstname]{/b}."

    grace "Saya akan memberi tahu {b}Eve{/b} bahwa Anda ada di sini."

    anon "Terima kasih."

    random_guy "Sial, sepeda ini bos!"

    grace f_angry "Hei, hati-hati dengan itu!"

    show anon f_surprised_teeth
    grace "Saya baru saja mengaktifkannya dan menjalankannya kembali!"

    hide anon with dissolve
    return

label grace_button_party_speak_to_grace:
    scene expression player.location.background_closeup with None
    show anon
    show grace a_beer f_tired:
        flip
        xoffset 500
    with dissolve
    grace "Hei, ayolah, kawan... berhentilah bermalas-malasan di sofaku!"

    show anon f_worried
    random_girl "Oh, uhh... salahku."

    grace "Aku tahu itu sampah, tapi aku lebih memilihnya daripada setumpuk kayu bakar..."

    anon "{b}Rahmat{/b}?"

    show grace f_tired a_beer:
        unflip
        xoffset 0
    with dissolve
    grace "Hah?"

    grace "Oh, hai {b}[firstname]{/b}."

    anon f_normal "Bersenang-senang?"

    grace @ f_eyeroll "Oh ya, banyak sekali..."

    anon "Apa yang kamu lakukan di bawah sini?"

    grace "Memastikan tidak ada yang kabur membawa omong kosong kita."

    anon f_worried "Oh, um... baiklah."

    grace "Aku tidak percaya {b}Odette{/b} menganggap ini ide yang bagus..."

    anon "Ya, dimana dia?"

    grace "Di atas atap, menurutku."

    anon "Oh baiklah."

    pause
    anon "Apakah {b}Eve{/b} juga ada di sana?"

    grace f_sexy "Saya pikir dia masih di dalam bersiap-siap."

    grace f_normal "Mengapa kamu tidak pergi ke sana dan aku akan mengirimnya ke tempatmu?"

    anon f_normal "Ya baiklah."

    anon "Terima kasih!"

    grace "Tidak masalah."

    show anon:
        xoffset 500
    show grace:
        xoffset -500
    with MoveTransition(2)
    pause
    show grace with dissolve:
        flip
        xoffset 0
    grace f_normal "Oh, hai {b}[firstname]{/b}?"

    show anon:
        flip
        xoffset 0
    with dissolve
    anon @ -m_talk "Hmm?"

    grace f_happy "Saya sangat senang Anda ada di sini."

    anon @ f_laugh "Y-ya, aku juga."

    grace f_tired "Beritahu {b}Odette{/b} dia itu pelacur busuk bagiku."

    anon @ a_behind_head "Haha, oke."

    hide anon with dissolve
    return

label grace_button_party_start:
    scene expression player.location.background_closeup with None
    show anon
    show grace f_tired
    with dissolve
    grace "Oh benar, pesta bodoh itu."

    show anon f_worried
    grace "{i}*Huh*{/i} Aku bahkan tidak mau memikirkannya!"

    grace "Itu urusan {b}Odette{/b} dan aku serahkan padanya."

    anon "Anda tampak sangat kesal karenanya?"

    grace f_angry "Tentu saja aku kesal!"

    show anon f_surprised_teeth
    grace "Hal terakhir yang ingin kulakukan setelah shift dua belas jam adalah mengasuh sekelompok orang idiot yang mabuk!"

    show grace f_tired
    anon f_worried @ a_behind_head "Saya yakin semuanya akan baik-baik saja."

    grace @ f_eyeroll "Ya benar."

    pause
    grace f_sad "Bantulah aku {b}Sabtu{/b} dan awasi adikku, ya?"

    grace "Saya khawatir dia akan minum terlalu banyak dan sakit lagi."

    anon "Saya bisa melakukan itu."

    grace f_normal "Terima kasih, {b}[firstname]{/b}."

    return


label grace_button_talked_to_grace:
    scene expression player.location.background_closeup with None
    show anon a_beer
    show grace f_happy a_beer
    with dissolve
    grace "Aku sangat berharap {b}Odette{/b} tidak terlalu gila malam ini..."

    anon @ f_skeptical "Seberapa gilakah {b}Odette{/b} saat dia minum?"

    grace "Jangan khawatir."

    grace "Saya yakin Anda akan mengetahuinya..."

    hide anon with dissolve
    return

label grace_button_eve_talk_to_girls:
    scene expression player.location.background_closeup with None
    show anon a_beer
    show grace f_happy
    with dissolve
    anon "Ini dia."

    show anon a_idle
    show grace a_beer
    with dissolve
    grace "Terima kasih."

    anon "Tidak masalah."

    show grace a_beer_drink f_proud m_talk with dissolve
    pause
    show anon b_dressed_pickup with dissolve
    show grace f_happy a_beer -m_talk with dissolve
    grace @ -m_talk "Hmm!"

    show anon b_dressed a_beer with dissolve
    anon "Anda yakin apinya menyala dengan cepat."

    grace "Ya, menurutku enam tahun di pramuka putri benar-benar membuahkan hasil, ya?"

    anon "Hehe, sepertinya begitu."

    pause
    grace "Hei, ngomong-ngomong..."

    grace "... Kamu melakukan pekerjaan dengan baik malam itu."

    anon @ -m_talk "Hmm?"

    grace "Kau tahu, saat adikku terbuka padamu..."

    grace "Tentang dia... kamu tahu."

    show grace a_beer_drink f_proud m_talk with dissolve
    if M_eve.biggus_dickus:
        anon f_worried @ f_surprised "Penisnya?"

        show grace a_beer f_happy -m_talk with dissolve
        grace "Y-ya."

        grace "Sungguh luar biasa bahwa Anda baik-baik saja dengan itu."

        anon f_snarky "Why wouldn't I be?"

        anon f_normal "Your sister is a wonderful person and I enjoy hanging out with her so much..."

        anon "... That other stuff isn't important, you know?"

        grace f_uneasy "Well, yeah... I know..."

        grace "... But not everybody thinks that way and {b}Eve{/b} has faced a lot of adversity, just from trying to be herself."

        grace "So, she's pretty self-conscious about it."

        anon "I think she's beautiful."

    else:
        anon f_worried @ f_surprised "The scar?"

        show grace a_beer f_sad -m_talk with dissolve
        grace "Well, that... and all the emotional baggage."

        grace "She was a wreck for a long time after our parents died."

        grace "Actually, we both were."

        anon f_worried "I understand, believe me."

        grace @ f_surprised "Oh benar!"

        grace "{b}Eve{/b} told me, you just lost your dad..."

        anon "Y-ya."

        grace "... I'm really sorry, {b}[firstname]{/b}."

        grace @ f_eyeroll "Here I am complaining about our problems from years ago, and your wounds are fresh-"

        anon "No, really... it's fine."

        anon "I'm getting through it."

        pause
        anon f_normal "Honestly, I think talking about it and trading painful experiences with others really helps heal, you know?"

    show grace f_happy
    pause
    grace "You're a really great guy, {b}[firstname]{/b}!"

    grace "I'm glad {b}Eve{/b} found you."

    anon @ f_laugh "Aku juga."

    pause
    show anon a_beer_drink f_smoke
    show grace a_beer_drink f_proud m_talk
    with dissolve
    pause
    show anon a_beer f_normal
    show grace a_beer f_happy -m_talk
    with dissolve
    grace "Man, I wish someone felt that way about me!"

    anon "Are you sure somebody doesn't?"

    grace f_uneasy @ -m_talk "Hmm?"

    anon "Nothing... never mind."

    pause
    anon a_beer_cheer "Cheers?"

    pause
    grace f_happy a_beer_cheer "Bersulang!"

    "{i}*Clink*{/i}"

    show anon a_beer_drink f_smoke
    show grace a_beer_drink f_proud m_talk
    with dissolve
    pause
    show anon a_beer f_normal
    show grace a_beer f_happy -m_talk
    with dissolve
    return

label button_grace_odette_eve_pot_cheerup:
    scene expression player.location.background_closeup with None
    show anon f_worried
    show odette f_smirk:
        xoffset -200
    show grace
    with dissolve
    grace "Any luck cheering her up?"

    anon "T-tidak, belum."

    odette "Well, what are you waiting for Clyde?!"

    odette "Bonnie needs you!"

    grace f_angry "Hentikan itu!"

    odette f_laugh "Ha ha ha!"

    anon "{b}I'll go upstairs and talk to her now{/b}."

    hide anon with dissolve
    return

label button_grace_bathroom_break:
    scene expression player.location.background_closeup with None
    show anon f_confused o_boner a_cover_boner:
        flip
    show expression "characters/anon/anon_arms_dressed_a_cover_boner.png" at flip
    show grace b_shirt f_happy:
        flip
    with dissolve
    anon "W-where did you say the bathroom was again?"

    grace "It's just through {b}Eve{/b}'s bedroom there and it'll be on your right."

    anon f_shy "T-terima kasih."

    hide anon
    hide expression "characters/anon/anon_arms_dressed_a_cover_boner.png"
    with dissolve
    return

label button_grace_distract_grace:
    scene expression player.location.background_closeup
    show anon f_worried a_rub:
        flip
    anon "{i}*Ahem*{/i} E-excuse me, {b}Grace{/b}?"

    grace "Hmm?"

    pause
    show grace b_shirt f_suspicious:
        flip
    grace "{b}[firstname]{/b}?"

    grace "Apa yang kamu lakukan di sini?"

    anon f_shy a_idle @ a_wave "H-hey... there."

    anon "I tried knocking but I guess you couldn't hear me..."

    grace f_happy "Heh, no I didn't hear you... sorry, I was really in the zone."

    anon "What were you doing anyways?"

    grace @ -m_talk "Hmm?"

    grace "Saya baik-baik saja."

    anon "It looked like you were sleeping or something?"

    grace @ f_laugh "Haha, no..."

    grace "I was meditating."

    anon @ f_confused a_thinking "Meditating?"

    grace f_suspicious "You've never heard of meditation?"

    anon "N-no, I guess not..."

    grace f_happy @ f_laugh "Oh, it's wonderful!"

    grace "It really works wonders if you have a lot of stress or anxiety..."

    anon "That sounds really neat."

    grace f_suspicious "Y-yeah, it is..."

    grace "What are you doing here again?"

    anon f_worried "Oh, uhh... {b}Eve{/b} told me to meet her here after school."

    grace "She did?"

    anon "Y-ya."

    grace "Well, where is she?"

    anon "W-where is she?"

    grace "Yeah, have you seen her?"

    anon @ f_thinking a_thinking "She umm... had to speak with {b}Miss Ross{/b} about some project..."

    grace "Oh, she's still struggling with that?"

    anon "Y-yeah, I guess so."

    grace f_sad "Poor thing."

    grace f_happy "I've been meaning to ask if I can help her with it but work keeps getting in the way, you know?"

    anon a_behind_head "Hehe, ya."

    pause
    grace f_suspicious "Sorry I'm not dressed."

    grace "I wasn't expecting company..."

    anon a_idle f_shy "Oh, don't worry about it!"

    anon @ f_laugh "Kamu tampak hebat!"

    grace f_sexy "Hehe, terima kasih."

    pause
    grace f_happy "Can I get you a drink or something?"

    anon f_worried a_behind_head @ f_shock a_surprised_up_both "TIDAK!"

    anon "I mean, n-no, I'm okay... we should stay right here in the living room."

    grace f_suspicious @ a_point "Is everything alright, {b}[firstname]{/b}?"

    anon f_surprised_teeth @ -m_talk "( Shoot, this isn't going very well... I just need to keep her talking! )"

    anon a_rub f_shy "Y-yeah, everything is great!"

    pause
    anon @ f_worried "S-so uhh... what else do you do?"

    anon "You know, to relieve stress?"

    grace f_happy "Heh, oh my..."

    pause
    grace a_hip f_normal @ f_normal_down "... Well, I suppose... I uhh..."

    pause
    grace f_happy @ f_laugh "Oh, I've been learning all about shiatsu massage!"

    anon f_confused "Apa itu?"

    grace "It's a traditional form of Japanese massage that uses acupressure to release tension in your muscles and bring balance to your body."

    anon f_normal "Kedengarannya luar biasa!"

    grace "Yeah, it's really cool!"

    grace @ f_eyeroll "Err, well... at least I think it is..."

    grace "{b}Odette{/b} and I have been trying it, but we aren't very good yet."

    anon "Oh, you're doing it together?"

    grace @ f_laugh "Hehe, ya."

    grace "Though, to be honest, I think {b}Odette{/b} is just using it as an excuse to get naked in our apartment... heh."

    anon f_shock "{i}*Gulp*{/i} N-naked {b}Odette{/b}?"

    show anon f_flirt o_boner with dissolve
    anon @ -m_talk "..."
    anon f_surprised_down @ -m_talk "!!!" with hpunch
    show anon f_surprised a_cover_boner
    show expression "characters/anon/anon_arms_dressed_a_cover_boner.png" at flip
    grace "I've got lots of books about it, if you're interested-"

    anon @ -m_talk "( Oh, crap! )"

    anon @ -m_talk "( Not now!! )"

    anon f_worried "Eh, I... uhh, I should probably-"

    grace f_suspicious @ -m_talk "Hmm?"

    grace "Are you sure you're alright, {b}[firstname]{/b}?"

    grace "You look a little pale."

    anon "Oh, ehh... I'm fine, I just... c-could I use your restroom?"

    grace "Sure, but you'll have to go through {b}Eve{/b}'s bedroom."

    anon "Through her bedroom?"

    pause
    anon "I uhh... on second thought, I should probably just head home..."

    grace f_happy @ f_laugh "Oh, jangan konyol!"

    grace "It's not like she's in there changing or anything!"

    anon @ f_shy "Hehe, y-ya..."

    grace "Just go in and turn right, you can't miss it."

    anon "T-terima kasih."

    hide grace with dissolve
    anon @ -m_talk "( Oh my god, why did she have to mention {b}Odette{/b} naked? )"

    anon @ -m_talk "( I hope she didn't notice! )"

    hide anon
    hide expression "characters/anon/anon_arms_dressed_a_cover_boner.png"
    with dissolve
    return

label button_grace_mia_get_tattoo:
    scene expression player.location.background_closeup
    show old_mia 7f at Position (xpos=400)
    show anon
    show grace f_normal
    show tattoo_desk at right
    with dissolve
    grace "Hai!"

    grace "Are you here for an appointment?"

    return

label button_grace_generic:
    show anon
    show grace f_normal
    show tattoo_desk at right
    with dissolve
    grace "Hai!"

    grace "Are you here for an appointment?"

    return

label button_grace_tattoo_mia:
    show old_mia 10f
    mia "I'd like to get a tattoo... now."

    show old_mia 7f
    show grace f_normal
    grace "Now? I see..."

    grace f_suspicious "Do you have a design in mind?"

    show grace f_normal
    show old_mia 30f at Position (xoffset=64) with dissolve
    mia "My friend here drew this for me, and I'd like it done today!"

    show old_mia 7f
    show grace f_normal_down a_hip_paper
    with dissolve
    grace "Hmm..."

    grace f_normal "Are you sure you want this done?"

    grace "Tattoos are permanent, so I have to make sure my clients know what they're getting into!"

    show old_mia 10f
    mia "I've been thinking about it for a long time and... yes, I do want it."

    show old_mia 7f
    grace "Alright, sweetie. But, it ain't cheap!"

    anon f_normal "How much is it?"

    grace f_normal_down "For that size... With colors... Around {b}four hundred dollars{/b}."

    show grace f_normal
    show anon f_surprised
    show old_mia 12f
    mia "!!!"
    mia "Damn... I think I only have two hundred..."

    show old_mia 8f
    anon f_worried @ -m_talk "..."
    anon "You don't have enough?"

    show old_mia 12 with dissolve
    mia "No, that's all I was able to save up."

    mia "Menurut Anda apa yang harus saya lakukan?"

    show old_mia 8
    return

label button_grace_tattoo_help:
    anon f_normal "I'll cover the rest."

    show old_mia 12
    mia "Benar-benar?!"

    show old_mia 7
    anon "Why not."

    anon "I've been working lately, so I have some money to spend..."

    anon @ f_laugh "... And it's for a good cause!"

    show old_mia 10
    mia "That's really sweet of you..."

    mia "... And I'll make sure to pay you back!"

    show old_mia 7
    anon @ f_laugh "It's alright, haha."

    show grace f_normal
    grace "Jadi?"

    show old_mia 7f with dissolve
    grace "Ready to start?"

    show old_mia 10f
    mia "I'm ready!"


    scene tattoo_cs01
    show text _ ("It took a while for {b}Grace{/b} to finish the work.\nI was really nervous for {b}Mia{/b}...\n... But, she seemed to be fine the whole time!") as caption
    with fade
    pause


    scene tattoo_indoor_b
    show old_mia 7f at Position (xpos=400)
    show anon
    show grace f_normal
    with fade
    grace "All done!"

    grace "I hope you guys like it."

    show old_mia 10f
    mia "It's great! And it didn't hurt as much as I thought..."

    show old_mia 7f
    grace "Make sure you leave the bandage on it for at least a few days."

    show old_mia 10f
    mia "Okay, thank you!"

    show old_mia 7f
    grace "Bye, guys."

    hide grace with dissolve
    pause(.25)
    hide old_mia
    show old_mia 7 at right
    with dissolve
    anon "How does it feel?"

    show old_mia 12
    mia "Tatonya?"

    show old_mia 7
    anon "Ya."

    show old_mia 12
    mia "It's fine... It just has this tingling sensation."

    show old_mia 10
    mia "And I'm glad I did it... I can finally say I did something that I wanted."

    show old_mia 7
    anon f_worried "Are you scared your mom might find out?"

    mia "Hopefully not, but it's in a well-hidden spot, haha."

    show old_mia 9
    show old_mia 7
    anon f_grin @ f_laugh "I think it's cool you did it."

    show old_mia 10
    mia "Thanks, {b}[firstname]{/b}. I'm happy you came with me."

    show anon f_normal
    mia "I should get going, though. Before my mom starts getting suspicious..."

    show old_mia 7
    anon "Okay, see you at school!"

    show old_mia 10
    mia "Selamat tinggal."

    hide anon
    hide old_mia
    with dissolve
    return

label button_grace_tattoo_come_back:
    anon f_worried "Maybe we should come back later?"

    mia "..."
    show old_mia 12
    mia "I suppose we should."

    show old_mia 8
    anon "It's okay. We can always come back another time."

    show old_mia 12
    mia "Anda benar."

    show old_mia 8
    anon "Sorry you couldn't get your tattoo today..."

    show old_mia 12
    mia "It's fine. I should get home now."

    show old_mia 8
    anon "Alright, see you later."

    hide anon
    hide old_mia
    hide grace
    hide tattoo_desk
    with dissolve
    return

label button_grace_paint:
    scene expression player.location.background_closeup
    show anon f_worried zorder 3
    show xtra 26 zorder 1 at Position(xpos=0.65, ypos=1.0)
    show grace f_normal zorder 0
    anon "Boleh saya bertanya sesuatu?"

    grace "Tentu!"

    anon "Well, you see..."

    pause
    anon "The thing is..."

    grace "..."
    anon "... Here's the thing..."

    show eve f_normal_right zorder 2:
        flip
        xoffset 200
    with dissolve
    eve "Jeez, spit it out already, {b}[firstname]{/b}!"

    eve f_happy "What up, Raggedy Ann?"

    grace @ f_laugh "Heh, not much."

    grace "You staying outta trouble, punk?"

    eve "Tentu saja tidak."

    show anon f_normal
    grace @ f_laugh "hehe."

    eve "Look, {b}[firstname]{/b} here needs some ink."

    grace "Oh, you thinking of getting a tattoo?"

    anon @ -m_talk "..."
    eve f_happy_right @ f_laugh "No, no, no. He needs actual ink! Like in bottles, ya dummy!"

    eve "Sorry, she can be a little slow."

    show eve f_happy
    grace @ f_suspicious "Hey! I heard that!"

    eve "Yeah, I said it loud..."

    grace @ f_laugh "Haha, smart ass."

    eve @ f_laugh "Looove ya, Sis!"

    grace "Yeah, yeah. You're lucky you're cute."

    eve "Diam!"

    grace @ f_laugh "Haha!"

    grace "So, how much ink do you need, {b}[firstname]{/b}?"

    show eve f_happy_right
    anon "Umm, I'm not sure."

    anon "Just enough to do one painting."

    show eve f_happy
    grace "Ahhh, an artist, huh?"

    grace @ f_laugh "Figures, the first guy {b}Eve{/b} brings home is an artist."

    show anon f_worried
    eve @ f_eyeroll "Tch, better than that biker freak you were dating in high school."

    grace @ f_laugh "Heh, you'll get no arguments there..."

    grace "Would one bottle of each primary color be enough?"

    grace @ f_suspicious "I assume you know how to mix?"

    anon "Mix?"

    eve f_happy_right "Yeah, you know? Blue and red make purple."

    eve "Yellow and blue make green."

    anon "Oh yeah, like color wheel stuff, right?"

    show eve f_happy
    grace "Yeah, exactly."

    grace @ f_suspicious "I guess the only question now, is what are you gonna do for me?"

    show eve f_happy_right
    anon "Oh, uhh. I dunno? What do you want me to do?"

    show eve f_happy
    grace @ f_suspicious "Hmm, did you happen to notice the graffiti on the side of the building when you came in?"

    show eve f_happy_right
    anon "... Yeah, it's pretty hard to miss."

    show eve f_happy
    grace "I'll give you the inks if you can wash it off for me."

    eve f_confused @ f_surprised "Sungguh?"

    anon f_normal "I can do that!"

    eve "Pfft, what a waste of time!"

    anon f_worried @ -m_talk "..."
    eve "It's just gonna get tagged again..."

    show grace f_angry a_hips_mad
    with dissolve
    grace "Well, it's that stupid fucking rap gang in the park that keep doing it!"

    grace "You need to tell those little bitches that I'll whoop their fucking asses if it happens again!"

    anon "Daaang, I didn't know your sister was such a badass!"

    eve f_normal @ f_happy_right "Heh, you have no idea."

    grace "I dunno why those douchebags can't just leave our shop alone..."

    eve "... If you're going to blackmail {b}[firstname]{/b} into doing chores, you could at least have him do something useful."

    eve "Like maybe moving all that heavy shit you ordered into the back room?"

    show grace f_normal a_hip with dissolve
    eve f_happy @ f_laugh "I don't wanna bust my ovaries carrying that shit!"

    grace @ f_suspicious "Hmm, I suppose that's not a bad idea..."

    grace @ f_laugh "... Especially if it gets you to shut up about your ovaries! Ugh!"

    eve @ a_flip "... Bitch."

    grace @ f_laugh "Hahaha, don't pretend like you don't love the abuse."

    eve @ f_eyeroll "Ya, ya..."

    eve f_happy_right "If you'll excuse me, {b}[firstname]{/b}."

    show anon f_normal
    eve "I'm going upstairs to \"accidentally\" drop all of my sister's makeup in the toilet."

    show eve f_happy
    grace @ f_laugh "{i}*Gasp*{/i} Don't even think about it!"

    eve @ a_wave "See ya, Sis!"

    grace f_suspicious "{b}Eve{/b}, I'm serious!"

    hide eve with dissolve
    eve "Ha ha ha!"

    grace f_uneasy "She's joking..."

    anon @ -m_talk "..."
    grace f_normal "The {b}boxes are right in front of the counter{/b}. Just {b}move them{/b} into the back for me and the ink is yours."

    anon "Sounds good!"

    return

label button_grace_you_look_familiar:
    anon f_worried @ f_skeptical "You know... I think..."

    anon "Uhh."

    show anon f_thinking a_thinking with dissolve
    grace @ f_suspicious "Apakah semuanya baik-baik saja?"

    anon a_idle "Sorry, but you look... Familiar."

    show anon f_worried
    grace @ f_suspicious "Hah?"

    grace "Hmm... Maybe you're thinking of my sister?"

    anon "Saudari?"

    grace @ f_suspicious "My little sister? {b}Eve{/b}?"

    anon f_normal @ f_laugh "Oh! Of course!"

    anon "I can see the connection, now."

    grace @ f_laugh "Haha."

    grace "Anyway, is there anything I can do for you?"

    return

label button_grace_nothing:
    anon f_normal "I'm just looking around."

    grace "Cool! Have a look."

    grace "I do all styles and designs showcased in my shop!"

    grace "Just let me know if you ever think about getting something, and we can make an appointment!"

    anon "Okay, thanks!"

    grace "Sampai jumpa."

    hide grace
    hide old_mia
    hide anon
    hide tattoo_desk
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
