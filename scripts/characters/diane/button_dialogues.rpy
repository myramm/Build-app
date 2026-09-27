label dianes_dialogue_daisy:
    show player 14 at left
    show diane f_normal b_naked a_idle
    player_name "Bagaimana kabar {b}Daisy{/b}?"

    show player 13
    diane "Oh, dia sudah beradaptasi dengan baik!"

    diane "Agak lucu kalau seorang peternak sapi perah menemukan gadis sapi ajaib, bukan?"

    diane "Untung saja aku membangun gudang itu..."

    pause
    diane @ f_laugh "Dia gadis yang manis."

    show player 14
    player_name "Ya, benar."

    show player 13
    diane "Saya sangat senang kami menemukannya."

    return

label dianes_dialogue_cow_girl:
    scene expression player.location.background_blur with None
    show player 10 at left
    show diane b_naked
    with dissolve
    player_name "Ada kemajuan dengan teman baru kita?"

    show player 5
    show diane f_shamed_smile
    diane "{i}*Huh*{/i} Kasihan sekali."

    diane "Dia masih setengah yakin tuannya akan muncul dan menghukumnya karena membiarkan kita menemuinya."

    diane "Apa pun yang dilakukan pria jahat itu padanya, dia belum siap membicarakannya."

    show diane f_shamed
    show player 10
    player_name "Apakah dia setidaknya sudah memberitahumu namanya?"

    show player 5
    show diane f_shamed_smile
    diane "Tidak, belum."

    diane "Tapi dia sudah sadar."

    diane "Saya membayangkan itu tidak akan lama sampai dia siap berbicara dengan Anda."

    show diane f_shamed
    show player 10
    player_name "Oke."

    show player 5
    return

label dianes_dialogue_milk_sample:
    scene expression player.location.background_blur with None
    show diane b_naked
    show player 14 at left
    player_name "Bolehkah saya minta sedikit sampel susu Anda?"

    show player 13
    show diane f_smirk
    diane "Hehe, merasa haus ya?"

    show player 29 with dissolve
    player_name "T-tidak, aku benar-benar hanya butuh sampel."

    show player 13 with dissolve
    show diane f_surprised
    pause
    show diane f_shamed
    diane "Oh."

    diane "Uhh, tentu saja. Beri aku waktu sebentar."

    if M_diane.outfit.get == "shirtless":
        show diane b_topless
    show diane a_squeeze3 f_down_front
    with dissolve
    pause
    show diane f_normal a_bottle1 with dissolve
    diane "Akankah ini berhasil?"

    show diane b_naked a_idle with dissolve
    show player 713
    with dissolve
    player_name "Ya, ini sempurna!"

    player_name "Terima kasih, {b}Diane{/b}!"

    hide player with dissolve
    diane "Tidak ada pro-"

    show diane f_surprised
    pause
    show diane f_shamed_front
    diane "(Apa yang dia lakukan?)"

    hide diane with dissolve
    call popup ('give', 'milk_sample')
    return

label dianes_dialogue_hows_baby_doing_boy:
    show player 14 at left
    show diane b_casual a_baby
    player_name "Bagaimana kabarnya?"

    show player 13
    show diane f_normal
    diane "Oh, dia luar biasa!"

    diane "Saya tidak pernah ingin menjatuhkannya."

    show player 14
    player_name "Yah, pada akhirnya kau harus menurunkannya..."

    show player 13
    show diane f_laugh
    diane "Tidak, eh!"

    show diane f_cheese
    show player 17
    player_name "Hehehe."

    show player 13
    return

label dianes_dialogue_hows_baby_doing_twins:
    show player 14 at left
    show diane b_casual a_baby
    player_name "Bagaimana kabar mereka?"

    show player 13
    show diane f_normal
    diane "Oh, mereka sungguh luar biasa!"

    diane "Saya tidak pernah ingin meletakkannya."

    show player 14
    player_name "Yah, pada akhirnya Anda harus meletakkannya..."

    show player 13
    show diane f_laugh
    diane "Tidak, eh!"

    show diane f_cheese
    show player 17
    player_name "Hehehe."

    show player 13
    return

label dianes_dialogue_hows_baby_doing_girl:
    show player 14 at left
    show diane b_casual a_baby
    player_name "Bagaimana kabarnya?"

    show player 13
    show diane f_normal
    diane "Oh, dia luar biasa!"

    diane "Saya tidak pernah ingin menurunkannya."

    show player 14
    player_name "Yah, pada akhirnya kau harus menurunkannya..."

    show player 13
    show diane f_laugh
    diane "Tidak, eh!"

    show diane f_cheese
    show player 17
    player_name "Hehehe."

    show player 13
    return

label dianes_dialogue_get_anything_baby:
    show player 14 at left
    show diane b_casual a_baby
    player_name "Ada yang bisa kuberikan padamu?"

    show player 13
    show diane f_normal
    diane "Tidak, aku baik-baik saja."

    diane "Terima kasih, kawan."

    show player 14
    player_name "Terima kasih kembali."

    show player 13
    show diane f_shamed_smile
    diane "Tidak juga, terima kasih, {b}[firstname]{/b}."

    diane "Untuk semuanya."

    show diane f_shamed
    show player 14
    player_name "Dengan senang hati, {b}Diane{/b}."

    show player 13
    return

label dianes_dialogue_baby_leave:
    show player 14 at left
    show diane b_casual a_baby
    player_name "Aku akan meninggalkan kalian."

    show player 13
    show diane f_normal
    diane "Baiklah."

    show diane f_laugh
    diane "Ucapkan, \"Sampai jumpa, Ayah.\""

    show diane f_cheese
    show player 17
    player_name "hehe."

    show player 36 with dissolve
    if M_diane.pregnancy.baby_gender == "twins":
        player_name "Selamat tinggal, anak-anak kecil."

    else:
        player_name "Selamat tinggal, si kecil."

    hide player
    hide diane
    with dissolve
    return

label dianes_dialogue_gave_birth_intro:
    show player 14 at left
    show diane b_casual a_baby
    with dissolve
    player_name "Hai, {b}Diane{/b}."

    show player 13
    if M_diane.pregnancy.baby_gender == "boy":
        diane "Ssst, dia sedang tidur."

    elif M_diane.pregnancy.baby_gender == "twins":
        diane "Ssst, mereka sedang tidur."

    else:
        diane "Ssst, dia sedang tidur."

    show player 14
    player_name "Oh maaf."

    show player 13
    return

label dianes_dialogue_intro_kitchen:
    scene expression player.location.background_blur
    show player 14 at left
    show diane b_nightgown a_water
    player_name "Hai, {b}Diane{/b}."

    show player 13
    diane "Hai, {b}[firstname]{/b}."

    show player 10
    player_name "Kamu baik-baik saja?"

    show player 5
    diane "Hmm?"

    diane "Ya, aku baik-baik saja."

    show player 13
    diane "Saya hanya haus, jadi saya masuk ke sini untuk minum segelas air."

    pause
    diane "Sekarang aku hanya berpikir..."

    show player 14
    player_name "Memikirkan tentang apa?"

    show player 13
    diane @ f_laugh "Hehe, entahlah, sepertinya urusan pekerjaan..."

    show player 14
    player_name "O-oke."

    show player 13
    return

label dianes_dialogue_hows_business:
    show player 14 at left
    show diane a_idle
    player_name "Apakah Anda lebih mudah menyelesaikan semua pesanan Anda sekarang?"

    show player 13
    show diane f_laugh
    diane "Ya ampun, ya!"

    show diane f_normal
    diane "Saya rasa persediaan ASI saya meningkat lebih dari dua kali lipat sejak melahirkan!"

    diane "Produksi berjalan sangat lancar sekarang."

    if M_diane.pregnancy.number_of_babies == 1:
        diane "Saya hanya harus memastikan saya meninggalkan susu untuk si kecil."

        show diane f_laugh
        diane "Anak kita itu sangat lapar!"

    else:
        diane "Saya hanya harus memastikan saya meninggalkan susu untuk anak-anak kecil."

        show diane f_laugh
        diane "Anak-anak kita itu sangat lapar!"

    show diane f_normal
    show player 17
    player_name "Haha."

    show player 14
    player_name "Yah, susumu itu enak sekali... Aku tidak bisa menyalahkan mereka!"

    show player 13
    return

label dianes_dialogue_goodnight_1:
    show player 14 at left
    show diane f_normal a_idle
    player_name "Aku baru saja hendak tidur."

    player_name "Anda butuh sesuatu?"

    show player 13
    diane @ -m_talk "Hmm?"

    diane "Oh, aku baik-baik saja."

    diane "Terima kasih sudah bertanya."

    show player 14
    player_name "Baiklah kalau begitu, selamat malam."

    show player 13
    diane "Selamat malam."

    hide player
    hide diane
    with dissolve
    return

label dianes_dialogue_goodnight_2:
    show player 14 at left
    show diane f_normal a_idle
    player_name "Ya, semuanya baik-baik saja."

    player_name "Maaf membangunkanmu."

    show player 13
    diane "Tidak apa-apa."

    show player 14
    player_name "Selamat malam."

    show player 13
    diane "Selamat malam, kawan."

    hide player
    hide diane
    with dissolve
    return

label dianes_dialogue_what_up_to:
    show player 14 at left
    show diane f_normal b_naked a_idle
    player_name "Lagi sibuk apa?"

    show player 13
    diane "Oh, aku hanya duduk di sini karena bosan."

    diane "TV larut malam menyebalkan."

    show player 14
    player_name "Hehe, itu terlalu benar!"

    show player 13
    show diane f_smirk
    diane "Anda ingin melakukan sesuatu yang menyenangkan?"

    show player 10
    player_name "Apa yang ada dalam pikiranmu?"

    show player 13
    diane "Mmm, aku bisa memikirkan beberapa hal..."

    return

label dianes_dialogue_on_my_way_debbie:
    show player 14 at left
    show diane f_normal b_naked a_idle
    player_name "Saya sedang dalam perjalanan untuk melihat {b}[deb_name]{/b}."

    show player 13
    diane "Ah, oke."

    diane "Dia ada di kamarnya."

    show player 14
    player_name "Aku akan bicara denganmu nanti, oke?"

    show player 13
    diane "Baiklah."

    hide player with dissolve
    pause
    show diane f_smirk
    diane "Kalian berdua bersenang-senang."

    show diane f_laugh
    diane "Hehehe."

    hide diane with dissolve
    return

label dianes_dialogue_leave_d19_d20_day:
    show player 14 at left
    show diane f_normal b_naked a_idle
    player_name "Aku harus memeriksa taman."

    show player 13
    diane "Oke."

    diane "Jangan lupa bahwa aku butuh bantuanmu untuk memompa juga!"

    show player 14
    player_name "saya tidak akan melakukannya."

    hide player
    hide diane
    with dissolve
    return

label dianes_dialogue_hows_the_business:
    show player 13 at left
    show diane f_normal b_naked a_idle
    diane "Bisnis sedang booming!"

    diane "Saya hampir tidak bisa memenuhi semua pesanan!"

    show player 14
    player_name "Itu bagus, bukan?"

    show player 13
    diane "Itu sangat bagus."

    show diane f_laugh
    diane "Saya harus segera mulai mempekerjakan lebih banyak payudara."

    show diane f_cheese
    return

label dianes_dialogue_call_veronica:
    show player 10 at left
    show diane f_normal b_naked a_idle
    player_name "Apakah Anda sudah berbicara dengan {b}Veronica{/b}?"

    show player 13
    diane @ f_sad "Tidak, belum."

    diane "Tapi aku akan melakukannya."

    show player 14
    player_name "Dia sangat ingin bekerja untukmu."

    show player 13
    show diane f_laugh
    diane "Ya, kita akan lihat."

    show diane f_cheese
    return

label dianes_dialogue_what_are_you_up_to:
    show player 14 at left
    show diane f_normal b_nightgown a_idle
    player_name "Apa yang sedang kamu lakukan?"

    show player 13
    diane "Oh, hanya menonton TV dan menyeruput anggur lezat {b}[deb_name]{/b}."

    diane "Senang sekali memiliki teman sekamar lagi."

    show player 14
    player_name "Apakah itu?"

    show player 13
    diane "Tentu saja!"

    diane "Aku sangat kesepian di sana, di rumah besar itu sendirian."

    show player 14
    player_name "Ya, saya bisa membayangkannya."

    show player 13
    diane "Sekarang saya merasa seperti menjadi bagian dari sebuah keluarga lagi."

    show player 14
    player_name "Anda adalah bagian dari keluarga kami {b}Diane{/b}."

    show player 13
    diane "Ah, terima kasih ganteng."

    return

label dianes_dialogue_wheres_debname:
    show player 10 at left
    show diane f_normal b_nightgown a_idle
    player_name "Bukankah dia biasanya duduk di sini bersamamu?"

    show player 13
    diane "Dia pergi tidur lebih awal malam ini..."

    diane "... Katanya dia lelah."

    show player 14
    player_name "Oh, begitu."

    show player 13
    diane "Anda masih bisa pergi dan menemuinya jika Anda mau, saya yakin dia tidak akan keberatan."

    show player 14
    player_name "Y-ya, mungkin..."

    show player 13
    return

label dianes_dialogue_love_that_nightgown:
    show player 14 at left
    show diane f_normal b_nightgown a_idle
    player_name "Itu terlihat luar biasa untukmu!"

    show player 13
    show diane f_laugh a_hip with dissolve
    diane "Hehe, terima kasih!"

    show diane f_reading_intrigued
    diane "Saya khawatir ini mungkin sedikit tidak pantas tetapi mengingat apa yang {b}[deb_name]{/b} dan {b}[jen_name]{/b} berjingkrak-jingkrak di..."

    show diane f_normal
    show player 14
    player_name "Hehe, y-ya."

    show player 426
    pause
    show diane f_smirk
    diane "Hehe, kamu masih bersamaku tampan?"

    player_name "Hmm?"

    show player 29 with dissolve
    player_name "Oh, m-maaf!"

    show player 3
    diane "Haha, tidak apa-apa."

    diane "Anda bisa melihat."

    show player 426 with dissolve
    pause
    pause
    show player 403
    show diane a_idle with dissolve
    return

label dianes_dialogue_goodnight:
    show player 14 at left
    show diane f_normal b_nightgown a_idle
    player_name "Saya mungkin harus tidur."

    show player 13
    diane "Ya, aku juga."

    show player 14
    player_name "Selamat malam, {b}Diane{/b}."

    show player 13
    diane "Selamat malam, tampan."

    hide player
    hide diane
    with dissolve
    return

label dianes_dialogue_hows_the_couch:
    show player 14 at left
    show diane f_normal b_shirtless a_idle
    player_name "Kamu tidur baik-baik saja?"

    show player 13
    diane "Oh, tidak apa-apa."

    diane "Agak kental tapi saya akan mengaturnya."

    pause
    diane "Anda ingin mendengar sesuatu yang aneh?"

    show player 14
    player_name "Tentu."

    show player 13
    diane "{b}[jen_name]{/b} terus turun di tengah malam dan terengah-engah saat dia menemukanku terbaring di sana."

    diane "Lalu ketika saya menanyakan apa yang dia butuhkan, dia memutar matanya dan langsung menggumamkan sesuatu tentang membuang-buang uang."

    diane "Tahu tentang apa itu?"

    show player 29 with dissolve
    player_name "aku uhh..."

    show player 3
    diane "Apa yang mungkin dia inginkan di ruang tamu di tengah malam?"

    pause
    show player 10 with dissolve
    player_name "Tidak tahu."

    show player 5
    diane @ f_thinking "{i}*Sigh*{/i} Mungkin hanya caranya mencoba menggangguku."

    show player 14
    player_name "Hehe iya, mungkin..."

    show player 13
    show diane f_annoyed
    diane "Dia menyebalkan."

    show diane f_cheese
    return

label dianes_dialogue_feeling_better:
    show player 14 at left
    show diane f_normal
    player_name "Bagaimana perasaanmu?"

    show player 13
    show diane f_laugh
    diane "Oh, jauh lebih baik sekarang karena kamu membantuku memompa!"

    show diane f_smirk
    diane "Terima kasih untuk itu, {b}[firstname]{/b}."

    show player 14
    player_name "Terima kasih kembali."

    player_name "Pastikan Anda banyak istirahat, oke?"

    show player 13
    show diane f_laugh
    diane "Haha, oke, Ayah!"

    show diane f_cheese
    show player 17
    player_name "Haha!"

    show player 13
    show diane f_smirk
    return

label dianes_dialogue_like_working_for_you:
    show player 14 at left
    show diane f_normal
    player_name "Tahukah Anda, saya sangat menikmati karya ini {b}Diane{/b}."

    show player 13
    show diane f_laugh
    diane "Hah, aku yakin kamu juga begitu!"

    if M_diane.outfit.get == "dressed":
        show diane f_smirk a_finger with dissolve
    else:
        show diane f_smirk
    diane "Pria muda mana yang tidak senang memegang payudara sepanjang hari?"

    if M_diane.outfit.get == "dressed":
        show diane a_shovel with dissolve
    show player 14
    player_name "Bukan itu yang aku..."

    player_name "Heh, maksudku... Bagian itu cukup mengagumkan."

    show player 401
    player_name "Anda memiliki payudara yang bagus."

    show player 403
    diane "Eh ya."

    show player 14
    player_name "... Tapi bukan hanya itu!"

    player_name "Senang rasanya menjagamu."

    player_name "Saya menyukainya."

    show player 13
    if M_diane.outfit.get == "dressed":
        show diane a_blush with dissolve
    diane "Aduh."

    diane "Saya juga menyukainya, {b}[firstname]{/b}."

    if M_diane.outfit.get == "dressed":
        show diane a_shovel with dissolve
    pause
    diane "Hanya saja, jangan beri tahu {b}[deb_name]{/b}!"

    show player 14
    player_name "Jangan khawatir, saya tidak akan melakukannya."

    show player 403
    return

label dianes_dialogue_leave_d12b:
    show player 14 at left
    show diane f_normal b_naked a_idle
    player_name "Sebaiknya aku kembali melakukannya."

    show player 13
    diane "Baiklah."

    diane "Jika Anda butuh sesuatu, Anda tahu di mana menemukan saya."

    hide player
    hide diane
    with dissolve
    return

label dianes_dialogue_have_you_spoken_with_debname:
    show player 14 at left
    show diane f_tired b_naked a_shovel_sides
    player_name "Anda berbicara dengan {b}[deb_name]{/b} akhir-akhir ini?"

    show player 13
    diane "Oh, sepanjang waktu!"

    diane "Kami kembali melakukan panggilan telepon setiap hari."

    show player 14
    player_name "Itu bagus."

    show player 13
    diane "Sungguh luar biasa!"

    diane "Aku sangat merindukannya!"

    show player 14
    player_name "Yah, dia juga merindukanmu."

    player_name "Kita semua melakukannya, sungguh."

    show player 13
    diane "Aduh."

    hide player
    if M_diane.outfit.get == "dressed":
        show anon b_empty f_grin
        show diane b_kiss
    else:
        show diane b_kiss_shirtless
    with dissolve
    pause
    hide anon
    show player 13 at left
    show diane b_naked a_shovel_sides
    with dissolve
    return

label dianes_dialogue_about_veronica:
    show player 12 at left
    show diane f_tired b_naked a_shovel_sides
    player_name "Jadi bagaimana kamu bisa bertemu gadis itu {b}Veronica{/b}?"

    show player 13
    diane "Maksudmu {b}Vee{/b}?"

    diane "Oh, aku suka gadis itu!"

    diane "Kami bertemu di bagian berkebun di Consum-R, beberapa tahun lalu."

    diane "Dia baru saja pindah ke sini dari desa dan tidak mengenal siapa pun."

    show player 14
    player_name "Saya yakin itu kasar."

    show player 13
    diane "Oh, tentu saja."

    diane "Dia berantakan!"

    diane "Saya menawarkan untuk mengajak orang miskin berkeliling kota dengan imbalan nasihat berkebun, dan kami langsung cocok."

    show player 14
    player_name "Kamu baik sekali."

    show player 13
    diane "Ya, menurutku."

    diane "Sejujurnya, aku juga membutuhkan seorang teman."

    diane "Bagaimana dengan {b}[deb_name]{/b} terlalu sibuk dengan ayahmu dan semuanya."

    show player 5
    player_name "..."
    pause
    diane "Oh, maafkan aku tampan!"

    diane "Saya tidak bermaksud agar terdengar seperti hal yang buruk."

    show player 10
    player_name "Ya, aku tahu kamu tidak melakukannya."

    show player 5
    diane "Ayahmu adalah pria yang baik, aku selalu menyukainya."

    show player 10
    player_name "Terima kasih."

    show player 5
    return

label dianes_dialogue_hows_the_garden_2:
    show player 14 at left
    show diane f_tired b_naked a_shovel_sides
    player_name "Jadi aku baik-baik saja dengan tamannya?"

    show player 13
    diane "Anda melakukannya lebih baik daripada baik-baik saja!"

    diane "Saya belum pernah melihat taman saya terlihat sebagus ini!"

    diane "Saya mungkin memiliki mentimun terbaik di seluruh negeri!"

    show player 14
    player_name "Hah, aku tidak tahu tentang itu..."

    player_name "Saya senang hasilnya berjalan baik."

    show player 13
    return

label dianes_dialogue_take_it_easy:
    show player 14 at left
    show diane f_tired b_naked a_shovel_sides
    player_name "Baiklah, kurasa aku harus kembali bekerja."

    show player 10
    player_name "Tenang saja, oke?"

    player_name "Saya khawatir Anda bekerja terlalu keras."

    show player 5
    diane "Psh, suaramu seperti {b}[deb_name]{/b}..."

    diane "aku akan baik-baik saja."

    show player 10
    player_name "Oke..."

    hide player
    hide diane
    with dissolve
    return

label dianes_dialogue_about_debname:
    show player 14 at left
    show diane f_normal
    player_name "Saya senang Anda menghabiskan waktu bersama {b}[deb_name]{/b} lagi."

    player_name "Aku tahu dia merindukan kehadiranmu."

    show player 13
    show diane a_blush with dissolve
    diane "Aww, dan aku merindukan miliknya!"

    show diane a_shovel with dissolve
    diane "Kami tidak dapat dipisahkan di masa muda kami, Anda tahu?"

    show player 14
    player_name "Ya, saya pernah mendengar ceritanya."

    show player 13
    show diane f_laugh
    diane "Hah!"

    show diane f_smirk a_finger with dissolve
    diane "Yah, kuharap dia belum menceritakan semua ceritanya padamu!"

    show diane a_shovel with dissolve
    show player 10
    player_name "Hah?"

    show player 13
    show diane f_laugh
    diane "Hehe, sudahlah."

    show diane f_normal
    show player 14
    player_name "Aku masih belum bisa melupakan betapa miripnya kalian berdua..."

    show player 13
    diane "Ya, kami biasa mendapatkannya sepanjang waktu."

    diane "Mereka menyebut kami kembar di perguruan tinggi."

    show player 14
    player_name "Saya bisa melihatnya."

    show player 13
    diane "Aku yang liar, dan dia yang cantik!"

    show player 29 with dissolve
    player_name "Menurutku kalian berdua cantik, {b}Diane{/b}."

    show player 3
    show diane f_shamed_smile a_blush with dissolve
    diane "Ah, terima kasih ganteng."

    show diane f_normal a_shovel with dissolve
    show player 13 with dissolve
    return

label dianes_dialogue_hows_the_garden:
    show player 14 at left
    show diane f_normal
    player_name "Jadi, bagaimana kabar tamanmu?"

    show player 13
    show diane f_sad
    diane "Ini pasti terlihat hari yang lebih baik..."

    diane "Akhir-akhir ini aku begitu sibuk dengan pekerjaan sampingan, aku khawatir tamanku tidak mendapat perhatian yang layak."

    show diane f_normal
    diane "Itu sebabnya saya sangat bersemangat ketika {b}[deb_name]{/b} mengatakan Anda mungkin bisa membantu saya musim panas ini."

    show player 14
    player_name "Saya senang membantu, {b}Diane{/b}!"

    show player 13
    return

label dianes_dialogue_what_have_you_been_up_to:
    show player 14 at left
    show diane f_normal
    player_name "Jadi, apa yang Anda lakukan dengan diri Anda sendiri beberapa tahun terakhir ini?"

    show player 13
    diane "Oh, sebenarnya tidak banyak..."

    show player 14
    player_name "Tidak banyak?!"

    player_name "Saya pikir Anda di luar sana berpesta gila-gilaan dan dikejar oleh orang kaya?"

    show player 13
    show diane f_laugh a_blush with dissolve
    diane "Haha, ya ampun tidak!"

    diane "Apa yang memberi Anda ide itu?"

    show diane f_normal a_shovel with dissolve
    show player 14
    player_name "Ya, {b}[deb_name]{/b} selalu bilang kamulah yang paling liar."

    show player 13
    show diane f_smirk a_finger with dissolve
    diane "Yah, mungkin di masa mudaku..."

    show diane f_normal a_shovel with dissolve
    diane "Sejujurnya, sejak perceraian, saya menghabiskan sebagian besar waktu saya di sini, di taman ini."

    show player 14
    player_name "Maksudmu, kamu tidak keluar sama sekali lagi?"

    show player 13
    diane "Kadang-kadang saya pergi keluar untuk minum bersama teman saya {b}Veronica{/b}."

    diane "Tidak ada yang terlalu menarik."

    show player 14
    player_name "Apakah kamu tidak melewatkannya?"

    show player 13
    diane "Hmm, terkadang."

    diane "Aku sudah terlalu tua untuk menjalani kehidupan seperti itu sekarang."

    show diane f_smirk
    diane "Lagi pula, tidak ada lagi orang baik yang tersisa di kota ini."

    show player 12
    player_name "Benar-benar?!"

    show player 13
    diane @ f_laugh "Hehe, percayalah padaku."

    diane "Di usia saya, yang tersisa hanyalah ampasnya."

    show player 10
    player_name "Sayang sekali."

    show player 5
    return

label dianes_dialogue_intro_d1_d6:
    show player 13 at left
    show diane
    with dissolve
    diane "Halo, {b}[firstname]{/b}!"

    diane "Saya sangat senang Anda memutuskan untuk datang dan membantu saya."

    show player 14
    player_name "Ya, tidak masalah {b}Diane{/b}."

    player_name "Terima kasih telah membayar saya!"

    show player 13
    diane @ f_laugh "Hehe, dengan senang hati ganteng."

    return

label dianes_dialogue_intro_d7_d12:
    show player 5 at left
    show diane f_tired b_naked a_shovel_sides
    with dissolve
    diane "Hai, {b}[firstname]{/b}."

    diane "Tamanku terlihat sangat-"

    diane "{i}*Menguap*{/i}"

    diane "... Sangat bagus."

    show player 10
    player_name "Kamu baik-baik saja, {b}Diane{/b}?"

    show player 5
    diane "Ya, aku baik-baik saja."

    diane "Hanya lelah."

    return

label dianes_dialogue_intro_d12b_d15:
    show player 13 at left
    show diane b_naked
    diane "Hai, tampan!"

    show player 14
    player_name "Hai, {b}Diane{/b}."

    show player 13
    diane "Anda butuh sesuatu?"

    return

label dianes_dialogue_intro_d16_d18_barn:
    show player 13 at left
    show diane b_shirtless
    with dissolve
    diane "Hai, kawan!"

    show player 14
    player_name "Hai, {b}Diane{/b}."

    show player 13
    diane "Anda siap bekerja?"

    return

label dianes_dialogue_intro_d16_d18_couch:
    show player 13 at left
    show diane b_nightgown
    with dissolve
    diane "Hai, kawan!"

    show player 14
    player_name "Hai, {b}Diane{/b}."

    show player 13
    diane "Kamu mau tidur?"

    show player 14
    player_name "Ya, dalam beberapa menit."

    show player 13
    return

label dianes_dialogue_intro_d19_d20_barn:
    show player 13 at left
    show diane b_naked
    with dissolve
    diane "Hai, kawan!"

    show player 14
    player_name "Hai, {b}Diane{/b}."

    show player 13
    diane "Anda siap bekerja?"

    return

label dianes_dialogue_intro_d19_couch:
    show player 13 at left
    show diane f_smirk b_nightgown
    with dissolve
    diane "Hai, kawan!"

    show player 14
    player_name "Hai, {b}Diane{/b}."

    show player 13
    show diane f_normal
    diane "Anda mencari saya atau {b}[deb_name]{/b}?"

    return

label dianes_dialogue_intro_d20_couch:
    show player 13 at left
    show diane b_nightgown
    with dissolve
    diane "Hmm, {b}[firstname]{/b}?"

    show player 14
    player_name "Hai, {b}Diane{/b}."

    show player 13
    diane "Semuanya baik-baik saja?"

    return

label dianes_dialogue_ready_to_pump:
    show player 14 at left
    show diane f_normal
    with dissolve
    player_name "Anda siap untuk memompa?"

    show player 13
    diane "Sangat!"

    diane "Beri saya waktu satu detik untuk mengatur segalanya."

    hide diane with dissolve
    show player 14
    player_name "Dingin."

    return

label dianes_dialogue_hows_the_baby_pregnancy_1:
    show player 13 at left
    show diane b_naked a_idle f_normal
    with dissolve
    diane "Oh, belum banyak yang bisa dilaporkan."

    diane "Kecuali Anda tertarik mendengar tentang mual di pagi hari saya?"

    show player 10
    player_name "Nah, jika Anda ingin membicarakannya, kita bisa?"

    show player 13
    diane @ f_laugh "Haha, ya ampun tidak!"

    diane "Saya menghargai Anda bertanya."

    diane "Terima kasih, {b}[firstname]{/b}."

    return

label dianes_dialogue_hows_the_baby_pregnancy_2:
    show player 13 at left
    show diane b_naked a_idle f_normal
    with dissolve
    diane "Oh, belum banyak yang bisa dilaporkan."

    diane "Kecuali Anda tertarik mendengar tentang mual di pagi hari saya?"

    show player 10
    player_name "Nah, jika Anda ingin membicarakannya, kita bisa?"

    show player 13
    diane @ f_laugh "Haha, ya ampun tidak!"

    diane "Saya menghargai Anda bertanya."

    diane "Terima kasih, {b}[firstname]{/b}."

    return

label dianes_dialogue_hows_the_baby_pregnancy_3:
    show player 13 at left
    show diane f_normal b_naked a_idle
    with dissolve
    diane "Heh, payudaraku bengkak sekali!"

    diane "Apakah mereka terlihat lebih besar bagi Anda?"

    show player 26
    player_name "Entahlah, awalnya mereka cukup besar..."

    show player 18
    diane "Oh, ayolah!"

    show player 13
    diane "Pastinya lebih besar!"

    pause
    show player 14
    player_name "Aku suka benjolan bayi kecilmu!"

    show player 13
    show diane f_laugh a_touch_belly with dissolve
    diane "Hehe, aku tahu!"

    show diane f_normal
    diane "Bukankah itu menggemaskan?"

    pause
    show diane f_normal a_idle with dissolve
    diane "Terima kasih telah menghubungi saya, {b}[firstname]{/b}."

    show player 14
    player_name "Tentu saja."

    player_name "Saya tidak sabar untuk bertemu bayi kami, {b}Diane{/b}!"

    show player 13
    diane "Aww, kamu pria termanis di dunia!"

    return

label dianes_dialogue_hows_the_baby_pregnancy_4:
    show player 13 at left
    show diane f_tired b_naked a_idle
    with dissolve
    diane "Ah, aku kelelahan..."

    show player 5
    diane "Kakiku membuatku sakit, aku terlihat seperti ikan paus, dan payudaraku tidak pernah berhenti bocor!"

    show player 10
    player_name "... Oh."

    show player 5
    show diane f_laugh
    diane "Hehe, tapi tidak apa-apa."

    show diane f_normal a_touch_belly with dissolve
    diane "Aku akan segera menjadi seorang ibu!"

    show player 14
    player_name "Itu benar, kamu benar!"

    show player 13
    diane "Saya sangat bersemangat, {b}[firstname]{/b}!"

    diane "Saya tidak sabar untuk menggendong anak kami!"

    show player 14
    player_name "Ya, aku juga."

    show player 13
    show diane a_idle
    with dissolve
    return

label dianes_dialogue_breeding_session:
    show player 13 at left
    show diane b_naked a_idle f_smirk
    with dissolve
    diane "Anda siap untuk memulai?"

    show player 14
    player_name "T-tentu saja."

    show player 13
    diane "Untunglah!"

    diane "Aku jadi basah kuyup hanya memikirkan penis besarmu yang memasukkan bayi ke dalam diriku..."

    show player 10
    player_name "Anda?!"

    hide player
    show diane b_pull_mc_naked
    with dissolve
    diane "Mmm, aku sangat membutuhkannya, {b}[firstname]{/b}!"

    hide diane
    with dissolve
    scene expression "backgrounds/location_barn_sex_back_day.jpg"
    show diane_sex_breed pre_talk
    show diane_sex_breed_mc
    with dissolve
    diane "Itu dia, kawan."

    diane "Berikan padaku."

    hide diane_sex_breed_mc
    show diane_sex_breed insert_and_pullout
    with dissolve
    pause
    show diane_sex_breed creampie_pullout with dissolve
    pause 1
    show diane_sex_breed creampie
    diane "Ahh!!"

    return

label dianes_dialogue_cow_suit:
    show player 14 at left
    show diane f_normal b_naked a_idle
    player_name "Saya ingin berbicara dengan Anda tentang pakaian sapi Anda..."

    show player 13
    diane "Oh?"

    menu:
        "Pasang kembali." if M_diane.outfit.get == "naked":
            show player 14 at left
            player_name "Aku ingin kamu memakainya saat aku membiakkanmu."

            player_name "Ini sangat seksi!"

            show player 13
            diane @ f_laugh "Oh, aku sangat senang kamu berpikir begitu!"

            diane "Saya juga menyukainya!"

            show diane f_smirk
            diane "Rasanya pas, tahu?"

            diane "Memakainya di sini."

            show player 14
            player_name "Ya, sepenuhnya."

            hide diane
            with dissolve
            $ M_diane.outfit.is_naked = 0
            $ M_diane.outfit.set_default_outfit_schedule([["cow","cow","nightgown","nightgown"]])

        "Bisakah Anda menghapusnya?" if not M_diane.outfit.get == "naked":
            show player 14 at left
            player_name "Aku lebih suka kamu telanjang bulat."

            show player 13
            show diane f_smirk
            diane "Anda akan melakukannya?!"

            diane "Mmm, dasar anak nakal..."

            pause
            diane "Aku bisa melepasnya, jika itu yang kamu inginkan."

            diane "Apapun yang membantumu memasukkan bayi ke dalam perutku."

            hide diane
            with dissolve
            $ M_diane.outfit.set_default_outfit_schedule([["naked","naked","nightgown","nightgown"]])
    return

label dianes_dialogue_dump_pump:
    scene garden
    show player 10 at left
    show diane b_shirtless
    with dissolve
    player_name "Apa yang perlu saya lakukan lagi?"

    show player 13
    diane "Hmm?"

    diane "Oh, cukup {b}masuklah ke dalam gudang dan buang apa yang ada di dalam pompa ke dalam wadah penyimpanan{/b}."

    show player 14
    player_name "Benar!"

    player_name "Saya ikut!"

    hide player
    hide diane with dissolve
    return

label dianes_dialogue_daylight_drinking:
    scene expression "backgrounds/location_diane_garden_close_day_blur.jpg"
    show player 429 zorder 0 at Position (xpos=175,ypos=648)
    show diane_chair up
    show diane b_laying_back_shirtless f_smirk_up
    with dissolve
    player_name "Bagaimana kabarmu di sini?"

    show player 426
    diane @ f_laugh "Hmm, luar biasa!"

    show player 429
    player_name "Ada yang bisa kuberikan padamu?"

    show player 426
    diane "Saya tidak akan mengatakan tidak pada minuman."

    show player 429
    player_name "Keinginanmu adalah perintahku!"

    player_name "Minuman apa yang kamu inginkan?"

    show player 426
    $ randomdrink = M_diane.get("random drink")
    diane @ f_thinking "Bagaimana dengan {b}[randomdrink]{/b}?"

    show player 427
    player_name "{b}[randomdrink]{/b}?!"

    player_name "Aku belum pernah membuat yang seperti itu sebelumnya..."

    show player 426
    show diane f_laugh
    diane "Hehe, jangan khawatir. aku akan melakukannya."

    show diane f_smirk_up
    show player 429
    player_name "TIDAK! Saya bisa mengetahuinya."

    player_name "Anda bersantai saja di hari libur Anda!"

    show player 426
    diane "Anda yakin?"

    show player 429
    player_name "Positif!"

    show player 426
    diane "Oke. Nah, {b}resepnya ada di notepad sebelah mixer{/b}."

    show player 429
    player_name "Mengerti!"

    player_name "Satu {b}[randomdrink]{/b}, segera hadir!"

    hide player
    hide diane
    hide diane_chair
    with dissolve
    return

label dianes_dialogue_make_drink:
    $ randomdrink = M_diane.get("random drink")
    scene expression "backgrounds/location_diane_garden_close_day_blur.jpg"
    show player 427 zorder 0 at Position (xpos=175,ypos=648)
    show diane_chair up
    show diane b_laying_back_shirtless f_smirk_up
    with dissolve
    player_name "Minuman apa yang kamu inginkan lagi?"

    show player 426
    diane @ f_thinking "Hmm, {b}[randomdrink]{/b} akan menyenangkan."

    diane "{b}Resepnya ada di notepad sebelah mixer{/b}."

    show player 429
    player_name "Satu {b}[randomdrink]{/b}, segera hadir!"

    hide player
    hide diane
    hide diane_chair
    with dissolve
    return

label dianes_dialogue_diane_fetch_pump:
    show player 10 at left
    show diane f_normal
    with dissolve
    player_name "Apa yang perlu saya lakukan lagi?"

    show player 5
    diane "{b}ambilkan alat yang saya tinggalkan di meja dapur{/b}."

    show player 14
    player_name "Oh benar!"

    player_name "Saya akan segera kembali!"

    hide player
    hide diane
    with dissolve
    return

label dianes_dialogue_diane_got_pump:
    scene garden
    show player 239_240 at left
    show diane
    with dissolve
    pause
    show player 103 at Position (xoffset=38) with dissolve
    player_name "Is this what you needed?"

    show player 13
    show diane a_pump
    with dissolve
    diane "Ya!"

    show player 10
    player_name "What is this thing anyways?"

    show player 13
    diane "You've never seen a breast pump before?"

    show player 10
    player_name "... Tidak?"

    show player 12
    player_name "It's a pump?"

    show player 5
    diane "Mmmhmm."

    show player 10
    player_name "Bagaimana cara kerjanya?"

    show player 5
    diane @ f_explain "Hehe, well, you put this end over the nipple and then press the lever here, and it sucks the milk out of the teet and into this container."

    show player 14
    player_name "Wah!"

    show player 10
    player_name "... And it doesn't hurt the cow?"

    show player 13
    show diane f_laugh a_blush with dissolve
    diane "Ha ha ha!"

    diane "No, handsome."

    show diane f_normal a_shovel with dissolve
    diane "Rasanya sangat enak!"

    show diane f_shamed_smile
    diane "You know, for the uhh... Cow."

    show diane f_shamed
    show player 14
    player_name "Can I try milking the cow sometime?"

    show player 13
    show diane f_laugh
    diane "Haha, I don't think that's a good idea, handsome."

    show diane f_smirk a_finger with dissolve
    diane "For now, you just work on the garden, okay?"

    show diane a_shovel with dissolve
    show player 14
    player_name "... Oke."

    show player 13
    diane "If you need me, I'll be in here."

    diane "Just knock first, got it?"

    show player 14
    player_name "Ya, aku mengerti."

    show player 13
    show diane f_laugh
    diane "Hehe, thanks stud."

    hide player
    hide diane
    with dissolve
    return


label dianes_dialogue_delivery_1_reminder:
    scene garden
    show player 10 at left
    show diane
    with dissolve
    player_name "Where am I supposed to deliver this milk again?"

    show player 5
    diane "You need to {b}take that order to Tony down at Tony's Pizza{/b}."

    show player 14
    player_name "Oh yeah, I know that place!"

    player_name "Alright, I'll be back in a flash."

    show player 13
    diane "Terima kasih, {b}[firstname]{/b}!"

    hide player
    hide diane
    with dissolve
    return

label dianes_dialogue_delivery_1_done:
    scene garden
    show diane
    show anon a_money
    with dissolve
    anon "I made your delivery for you."

    show anon a_idle
    show diane a_money
    with dissolve
    diane "Oh, thank you so much {b}[firstname]{/b}!"

    show diane a_shovel with dissolve
    diane "Did {b}Tony{/b} say anything?"

    anon "Uh huh, he said the milk has really taken their pizzas to a whole new level!"

    diane "{i}*Terkesiap*{/i}"

    diane "So he liked it?"

    anon "Heh, I'd say so."

    anon @ f_laugh "He wants to triple his next order!"

    show diane f_sad
    diane "Triple?!"

    show diane f_surprised_front
    diane "Hmm..."

    anon f_worried @ f_confused "Is that a problem?"

    show diane f_shamed_front
    diane "Huh? Oh... Well, I'm not sure."

    diane "I don't know if I can handle-"

    show diane f_surprised
    pause
    show diane f_smirk
    diane "I mean, my cow..."

    diane "... I don't know if she can handle that much demand."

    anon f_normal "Sounds like you might need to expand and get more cattle."

    show diane f_thinking
    diane "..."
    show diane f_thinking_back
    diane "I'm definitely not ready for that yet."

    diane "I'll just have to push her harder and start stockpiling..."

    show diane f_normal
    anon "Can I do anything to help?"

    diane "Heh, no, that's alright."

    diane "You've helped me plenty already."

    anon @ -m_talk "..."
    diane "Why don't you get back to your garden work?"

    anon "Ya baiklah..."

    show anon with dissolve:
        flip
        xoffset -500
    diane @ f_teasing "Oh!"

    show anon with dissolve:
        unflip
        xoffset 0
    diane "... I almost forgot."

    show diane a_money with dissolve
    diane "This is yours."

    show diane a_shovel
    show anon a_money f_surprised
    with dissolve
    anon "Huh? This is the entire payment from the delivery!"

    diane "Hehe, I told you, {b}[firstname]{/b}. This isn't a money making endeavor for me."

    show diane f_smirk
    diane "At least not for the moment."

    anon f_normal @ -m_talk "..."
    show diane f_normal
    diane "You take it and put it towards your tuition."

    anon "Terima kasih, {b}Diane{/b}!"

    show diane f_laugh
    diane "You're welcome, handsome!"

    show anon b_empty f_grin
    show diane b_kiss
    with dissolve
    pause
    hide diane
    hide anon
    with dissolve
    return

label dianes_dialogue_leave_d1:
    show player 14 at left
    show diane f_normal
    player_name "I should probably get started on the garden."

    show player 13
    diane "Baiklah."

    diane "Thanks again for helping!"

    show player 14
    player_name "Tidak masalah."

    hide player
    hide diane
    with dissolve
    return

label dianes_dialogue_delivery_3_reminder:
    show player 10 at left
    show diane b_naked a_idle:
        xoffset 0
    with dissolve
    player_name "Apa yang harus saya lakukan lagi?"

    show player 13
    show diane f_normal
    diane "{b}Take the package of milk from my shed and deliver it to the cafeteria at your school{/b}."

    show player 14
    player_name "Oh benar."

    player_name "Saya ikut!"

    hide player
    hide diane
    with dissolve
    return

label dianes_dialogue_pre_fun_paint:
    show player 10
    player_name "{b}[deb_name]{/b} said she gave you the old paint in the garage."

    player_name "You still have it right?"

    show player 5
    if L_diane_garden.is_here(M_diane):
        show diane f_laugh
    else:
        show diane b_naked a_idle f_laugh
    diane "Well, sure I do!"

    show diane f_normal
    show player 13
    diane "There should be some left in the shed."

    diane "Help yourself!"

    show player 14
    player_name "Terima kasih!"

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
