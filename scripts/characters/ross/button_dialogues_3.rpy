label button_ross_ask_model:
    scene expression player.location.background_closeup
    show old_ross 25 at left
    show player 1f at right
    ross "Ada keberuntungan?"

    show player 2f
    show old_ross 24
    player_name "Belum."

    show player 1f
    show old_ross 25
    ross "Baiklah, pastikan kamu {b}bertanya kepada semua teman sekelasmu{/b}."

    show old_ross 25b
    ross "Mudah-mudahan, seseorang akan cukup berani untuk menjadi model bagi kita..."

    return

label button_ross_found_model:
    scene expression player.location.background_closeup
    show player 2f zorder 1 at right
    show old_judith 1 zorder 2 at Position(xpos=0.65, ypos=1.0)
    show old_ross 10 zorder 2 at left
    with dissolve
    player_name "Saya kembali {b}Nona Ross{/b} dan saya menemukan seorang model untuk kami!"

    show player 1f
    show old_ross 11
    ross "{i}*Terkesiap*{/i} {b}Judith{/b}!"

    show old_ross 27 with dissolve
    ross "Ini sempurna! Dia punya tubuh yang luar biasa untuk ini!"


    show old_ross 26
    show old_judith 4
    pause
    show old_judith 5
    judith "Oh umm, {b}Nona Ross{/b} akan hadir juga ya?"

    show player 10f
    show old_judith 1
    player_name "Ya, apakah tidak apa-apa?"

    show player 11f
    show old_judith 3
    judith "Entahlah..."

    show old_judith 6
    show old_ross 27
    ross "Oh lihat dia memerah, sungguh menyenangkan!"

    show old_ross 60 with dissolve
    ross "Ini, sayang, ambil ini dan ganti baju itu."


    ross "Kami akan menunggumu di sini."

    show old_ross 59
    show old_judith 3
    judith "Hmm..."

    show old_ross 60
    show old_judith 6
    ross "Jangan membuang waktu, kami ingin waktu sebanyak mungkin bersama Anda."


    hide old_judith
    show old_ross 11
    with dissolve
    ross "Kerja bagus, {b}[firstname]{/b}! Dia akan menjadi model yang hebat!"

    show old_ross 10
    show player 1f
    pause
    show old_mia 8b zorder 0 at Position(xpos=0.65, ypos=1.0) with dissolve
    pause
    show old_ross 11

    ross "... Dan inilah kue kecil manis kami, tepat pada waktunya!"

    show old_ross 10
    show old_mia 12b
    mia "Ya, saya tidak dapat menemukan siapa pun. Maafkan aku teman-teman..."

    show old_ross 11
    show old_mia 8b
    ross "Oh, jangan khawatir! {b}[firstname]{/b} tampil seperti biasanya."

    show old_ross 10
    show old_mia 10b
    mia "Benar-benar? Anda benar-benar meminta seseorang untuk menjadi sukarelawan?"

    show old_mia 9
    mia "Luar biasa, {b}[firstname]{/b}!"

    show old_mia 11
    show player 2f
    player_name "... Ya, {b}Judith{/b} setuju untuk-"

    show old_judith 59f zorder 0 at Position(xpos=0.35, ypos=1.0)
    show player 11f
    with dissolve
    pause
    show old_judith 44f
    show old_judithr 1f zorder 1 at Position(xpos=0.35, ypos=1.0)
    with dissolve
    show old_mia 7
    pause
    show old_judith 45f
    judith "... Apa yang {b}Mia{/b} lakukan di sini?!"

    show old_judith 44f
    show old_ross 11
    ross "Dia akan menggambarmu juga, sayang."

    show old_judith 45f
    show old_ross 10
    judith "Aku berubah pikiran tentang semua ini..."

    show old_judith 52f
    judith "Kukira hanya kamu dan aku saja, {b}[firstname]{/b}!"

    show old_judith 51f
    show old_ross 25
    ross "Tenang, {b}Judith{/b}... Semuanya akan baik-baik saja sayang."

    show old_ross 11
    ross "Anda tidak perlu merasa malu. Apakah dia laki-laki?"

    show old_ross 10
    show player 2f
    player_name "Sama sekali tidak."

    show player 1f
    show old_mia 10
    mia "Ya, jangan khawatir, {b}Judith{/b}. {b}Nona Ross{/b} telah mengajarkan kita bahwa tubuh setiap orang itu indah."

    show old_mia 7
    show old_ross 11
    ross "Benar sekali, {b}Mia{/b}. Semuanya cantik dengan keunikannya masing-masing."

    ross "Kamu harus bangga dengan tubuhmu, {b}Judith{/b}."

    show old_ross 10
    show old_judith 52f
    judith "Entahlah..."

    show old_judith 51f
    show old_ross 58 with dissolve
    ross "Saya punya ide!"

    hide old_ross with dissolve
    pause
    show old_ross 40 zorder 2 at left with dissolve

    ross "Ini selalu menenangkanku saat aku merasa cemas..."

    ross "Semuanya ambil satu."

    show old_ross 41
    show player 2f
    player_name "Oh, kudengar kamu membuat brownies yang paling enak!"

    show player 1f
    show old_ross 40
    ross "Hehe, sebaiknya kamu percaya!"

    ross "Itu resep rahasiaku..."

    show old_ross 44 with dissolve
    pause
    show old_ross 43 with dissolve
    ross "... Seratus persen semuanya alami."

    hide player
    show player 602 zorder 4 at right
    with dissolve
    show old_ross 42
    pause
    show player 599f with dissolve
    pause
    show player 600f
    show old_mia 73 zorder 3 at Position(xpos=0.55, ypos=1.0)
    with dissolve
    pause
    hide old_judith
    hide old_judithr
    show old_mia 71
    show old_judith 60 zorder 5 at Position(xpos=0.60, ypos=1.0)
    with dissolve
    pause
    hide old_judith
    show old_mia 71 at Position(xpos=0.65, ypos=1.0)
    show old_judith 47f zorder 0 at Position(xpos=0.35, ypos=1.0)
    show old_judithr 1f zorder 1 at Position(xpos=0.35, ypos=1.0)
    with dissolve
    pause
    show old_mia 72

    mia "enak!! Ini enak!"

    show old_mia 71
    show old_judith 48f
    judith "{i}*Nom nom nom*{/i}"

    show old_ross 43
    show old_judith 47f
    ross "Tenang saja, {b}Judith{/b}. Anda tidak ingin memakannya terlalu cepat."

    show old_ross 42
    show old_judith 48f
    judith "Ya ampun! Mereka sangat bagus!"

    show old_judith 49f
    judith "Hmm..."

    show old_mia 74f
    show player 26f
    player_name "Heh, rasanya agak... bersahaja."

    show player 13f
    show old_ross 13
    ross "Bagaimana perasaan semua orang?"

    show old_ross 12
    show player 26f
    player_name "Bagus sekali. Sangat bagus."

    show player 13f
    show old_judith 50f
    judith "Aku juga."

    show old_judith 49f
    show old_mia 75bf at Position(xpos=0.63, ypos=1.0) with dissolve
    mia "Heheheheheheheehee!"

    show old_judith 50f
    show old_mia 74f at Position(xpos=0.65, ypos=1.0) with dissolve
    judith "Jubah ini sangat gatal!"

    show old_judith 49f
    show old_ross 13
    ross "Nah, sekarang kamu sudah merasa lebih rileks, kenapa tidak dilepas saja, sayang."

    ross "Kita bisa menayangkan pertunjukan ini di jalan."

    show old_ross 12
    show old_judith 50f
    judith "Hmm, ya, oke..."

    hide old_judith
    hide old_judithr
    show old_judith 56f zorder 0 at Position(xpos=0.35, ypos=1.0)
    with dissolve
    pause
    show old_judith 49f with dissolve
    pause
    show old_ross 13
    ross "Bagus sekali, sayang."

    show old_ross 11
    ross "Sekarang, {b}[firstname]{/b} dan {b}Mia{/b}, kenapa kalian tidak duduk dan mencari arang kalian."

    show old_ross 10
    show old_mia 75bf at Position(xpos=0.63, ypos=1.0) with dissolve
    mia "Heheheheeahahaha!"

    mia "Semuanya berputar-putar!!"

    show old_mia 74f at Position(xpos=0.65, ypos=1.0) with dissolve
    show old_ross 11
    ross "Ya, tentu saja, kue manis."

    show old_ross 13
    ross "{b}Judith{/b} kamu juga harus melepas celana dalammu, sayang."

    show old_ross 12
    show old_judith 51f
    judith "Hmm?"

    show old_judith 52f
    judith "Maksudmu aku harus menunjukkan..."

    judith "Saya..."

    judith "... vagina?"

    show old_judith 51f
    show old_mia 75bf at Position(xpos=0.63, ypos=1.0) with dissolve
    mia "Pffftt!!! Ahahahah! Itu kata yang lucu!"

    mia "Puuuusssy! HahahaaH!"

    show old_mia 74f at Position(xpos=0.65, ypos=1.0) with dissolve
    show old_ross 11
    ross "Heh, tenanglah, {b}Mia{/b}!"

    show old_ross 25
    ross "Kamu masih merasa minder, {b}Judith{/b}?"

    show old_ross 24
    judith "Mmmhmm..."

    show old_ross 11
    ross "Nah, bagaimana jika kita semua juga dilucuti?"

    show old_ross 10
    show old_judith 54f
    pause
    show old_judith 55f
    judith "... Ya! Itu ide yang bagus!"

    show old_judith 54f
    show player 26f
    player_name "Anda ingin kami telanjang juga?"

    show player 13f
    show old_ross 11
    ross "Kami hanya akan membuka pakaian dalam kami."

    ross "Itu seharusnya cukup bagus, bukan {b}Judith{/b}?"

    show old_ross 10
    show old_judith 55f
    judith "... Ya! Saya ingin melihat pakaian dalam {b}[firstname]{/b}!"

    show old_judith 54f
    show old_ross 11
    ross "Bagus sekali kalau begitu..."

    hide old_ross
    show old_ross 14 at Position(xpos=0.15, ypos=1.0)
    with dissolve
    pause
    show old_ross 15 at Position(xpos=0.14, ypos=1.0) with dissolve
    pause
    show old_ross 16 at Position(xpos=0.13, ypos=1.0) with dissolve
    pause
    show old_ross 17 with dissolve
    pause
    show old_ross 36 at Position(xpos=0.15, ypos=1.0) with dissolve
    ross "Silakan kalian berdua..."

    show old_ross 37
    show old_mia 75f with dissolve
    mia "... Tunggu! Aku?"

    show old_mia 74f
    show old_ross 36
    ross "Terutama kamu, kue manis!"

    show old_ross 37
    show old_mia 75bf at Position(xpos=0.63, ypos=1.0) with dissolve
    mia "Heheheheheeeh, okey dokey!"

    show old_mia 76f at Position(xpos=0.62, ypos=1.0) with dissolve
    pause
    show old_mia 77f at Position(xpos=0.64, ypos=1.0) with dissolve
    pause
    show old_mia 78f at Position(xpos=0.66, ypos=1.0) with dissolve
    pause
    show old_mia 79f at Position(xpos=0.66, ypos=1.0) with dissolve
    pause
    show old_mia 80f at Position(xpos=0.66, ypos=1.0) with dissolve
    pause
    show old_mia 81f at Position(xpos=0.65, ypos=1.0) with dissolve
    show old_ross 36
    ross "Kamu tidak perlu melepas bramu, pai manis!"

    show old_mia 82f
    show old_ross 37
    mia "bukan?"

    show old_mia 81f
    show old_ross 36
    ross "Hehe, tidak, aku berkata, \"Turun ke celana dalam kita.\""

    show old_mia 82f
    show old_ross 37
    mia "Oooh..."

    mia "Okey-dokey!"

    show old_mia 82bf at Position(xpos=0.635, ypos=1.0) with dissolve
    mia "Ini menyenangkan!"

    show old_mia 81f at Position(xpos=0.65, ypos=1.0) with dissolve
    show old_ross 36
    ross "Ya, tentu saja, sayang."

    ross "Kita tunggu, {b}[firstname]{/b}."

    show old_ross 37
    show player 21f
    player_name "Y-ya. Oke!"

    show player 8f with dissolve
    pause
    show player 265f with dissolve
    pause
    show old_judith 53f
    pause
    show player 267f
    player_name "( !!! )" with hpunch
    judith "... Wah!"

    show old_mia 82bf at Position(xpos=0.635, ypos=1.0) with dissolve
    mia "Kelihatannya agak marah! Pffft, hahahahaa!!!"

    show old_mia 81f at Position(xpos=0.65, ypos=1.0) with dissolve
    show old_judith 55f
    judith "Ini sangat besar..."

    show old_judith 54f
    show player 265bf
    show old_ross 36
    ross "Tentu saja, sayang."

    ross "... Kamu masih harus melepas celana dalam itu sebelum kami dapat menggambarmu."

    show old_ross 37
    show old_judith 55f
    judith "... Dan merah muda."

    show old_judith 54f
    show old_ross 36
    ross "Sini, aku akan membantu!"

    hide old_ross
    show old_judith 61f at Position(xpos=0.22, ypos=1.0) with dissolve
    pause 
    show old_judith 62f with dissolve
    pause
    hide old_judith
    show old_judith 66f zorder 1 at Position(xpos=0.35, ypos=1.0)
    show old_ross 36 zorder 0 at left
    with dissolve
    ross "Ada seorang gadis yang baik."

    ross "Sekarang, berdirilah di sana, di atas tumpuan itu untukku, oke?"

    show old_ross 37
    show old_judith 66f
    judith "..."
    show old_ross 36
    hide old_judith with dissolve

    ross "Kalian berdua mulai menggambar."

    show old_ross 37
    show player 265cf
    player_name "Ya, Bu."


    scene location_school_art_cutscene08
    show text _ ("I could tell {b}Judith{/b} was still really nervous as {b}Miss Ross{/b} helped her up onto the pedestal.") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("It was very brave of her to model for an audience.") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("... But she wasn't exactly striking an inspirational pose up there.") as caption with dissolve
    pause

    scene expression player.location.background_closeup
    show old_judith 65b zorder 1 at Position(xpos=0.5, ypos=1.0)
    show old_ross 37 zorder 0 at left
    with fade
    pause
    show old_ross 36
    ross "Sayang? Kamu harus sedikit santai..."

    show old_ross 37
    show old_judith 66
    judith "saya tidak..."

    judith "Maksudku, aku..."

    hide old_ross
    show old_ross 36f zorder 0 at Position(xpos=0.7, ypos=1.0)
    with dissolve
    show old_judith 65b
    ross "Ssst."

    ross "Tidak apa-apa, {b}Judith{/b}."

    hide old_ross
    show old_judithross 2 zorder 0 at Position(xpos=0.685, ypos=1.0)
    with dissolve
    ross "Tarik nafas saja dalam-dalam..."

    show old_judith 66
    pause
    show old_judith 65b
    ross "... Itu dia."

    show old_judithross 1
    pause
    show old_judithross 2
    ross "Kamu bidadari yang cantik, {b}Judith{/b}."

    show old_judithross 1
    show old_judith 66
    judith "... Saya?"

    show old_judithross 2
    show old_judith 65b
    ross "Oh ya! Kamu menakjubkan, sayang!"

    show old_judithross 1
    pause
    hide old_judithross
    show old_judith 67 at Position(xpos=0.4, ypos=1.0)
    with dissolve
    ross "Lebarkan sayapmu, {b}Judith{/b}."

    ross "Biarkan dunia melihatmu terbang!"

    show old_judith 68b
    show old_ross 36f at Position(xpos=0.65, ypos=1.0)
    with dissolve
    ross "{i}*Terkesiap*{/i} Kesempurnaan!"

    show old_judith 69
    show old_ross 37f
    judith "... Kamu pikir aku sempurna?"

    show old_judith 68
    show old_ross 36f
    ross "Tentu saja sayang!"

    ross "Lihat saja tubuh montok itu..."

    ross "Bagaimana mungkin ada orang yang menolaknya?"

    show old_ross 37f
    pause
    show old_ross 36f
    ross "Sekarang, jangan bergerak sedikit pun!"

    ross "Berikan kesempatan kepada para seniman untuk mengabadikan kecantikan Anda!"

    show old_ross 37f
    show old_judith 69b
    judith "O-oke..."


    scene location_school_art_cutscene07
    show text _ ("{b}Miss Ross{/b} had definitely made {b}Judith{/b} more comfortable.") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("... And she had given me the perfect inspiration for my drawing!") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("Though it was little hard to concentrate on my work with {b}Miss Ross{/b} hovering over my shoulder...") as caption with dissolve
    pause

    scene expression player.location.background_closeup
    show old_judith 68 zorder 1 at Position(xpos=0.4, ypos=1.0)
    show old_ross 36f zorder 0 at Position(xpos=0.65, ypos=1.0)
    with fade
    ross "Itu sangat bagus, {b}[firstname]{/b}, tapi menurut saya Anda bisa melakukannya lebih baik."

    ross "Saya tidak yakin Anda benar-benar menangkap lekuk tubuh lezatnya."

    show old_ross 37f
    player_name "Apa maksudmu?"

    show old_ross 36f
    ross "Coba lihat!"

    ross "Terkadang Anda harus benar-benar menguasai subjek Anda dan merasakan bentuknya."

    ross "... Dan {b}Judith{/b} di sini memiliki kontur yang sangat bagus!"

    hide old_ross
    show old_judith 70
    with dissolve
    pause
    show old_judith 71 with dissolve
    pause
    show old_judith 72 with dissolve
    pause
    show old_judith 72b
    judith "( !!! )" with hpunch
    judith "AAAhh!"

    show old_judith 72e
    ross "... Nah, lihat siapa yang keluar untuk bermain!"

    show old_judith 72c_72d
    pause
    judith "Hmm..."

    show old_judith 72e
    ross "Bagaimana rasanya, sayang?"

    show old_judith 72
    judith "Sungguh..."

    judith "Ahhh, bagus sekali!"

    show old_judith 72e
    ross "Ya, nikmati saja sayang."

    show old_judith 72c_72d
    judith "NNGGHH!"

    pause
    show old_judith 72
    judith "Haaah!"

    show old_judith 72e
    ross "Cantik!"

    show old_judith 72
    judith "OH, AKU TIDAK BISA!"

    show old_judith 73 zorder 1 at Position(xpos=0.45, ypos=1.0)
    show old_ross 37f zorder 0 at Position(xpos=0.65, ypos=1.0)
    with dissolve
    judith "( !!! )" with hpunch
    judith "AAAHHH!"

    show old_judith 66
    judith "Haaah... Haaah..."

    show old_judith 65
    show old_ross 36f
    ross "Bagus sekali, sayang!"


    show old_judith 58f zorder 0 at left
    show old_ross 37f
    with dissolve
    judith "Itu tadi..."

    show old_judith 57f
    judith "..."
    show old_judith 58f
    judith "... Bisakah kita melakukannya lagi?"

    show old_judith 57f
    show old_ross 36f
    ross "... Mungkin nanti, sayang."

    show old_ross 36 at Position(xpos=0.60, ypos=1.0)
    with dissolve
    ross "Sekarang pahamkah kamu apa yang saya maksud dengan merasakan bentuk, {b}[firstname]{/b}?"

    show old_ross 37
    player_name "Saya tidak yakin..."

    show old_mia 82 zorder 1 at Position(xpos=0.35, ypos=1.0) with dissolve

    mia "Saya rasa saya mengerti, {b}Nona Ross{/b}!"

    show old_mia 81
    show old_ross 36f with dissolve
    ross "Bagus, kalau begitu kamu bisa membantuku menunjukkannya."

    show old_ross 36 with dissolve
    ross "Datang ke sini dan bergabunglah dengan kami, {b}[firstname]{/b}!"

    show old_ross 37
    player_name "Benar-benar?"

    show old_ross 36
    ross "Ya, ini adalah sesuatu yang perlu dipahami oleh setiap seniman yang baik."

    hide old_mia
    hide old_ross
    show old_rossg 3 at Position(xpos=0.60, ypos=1.0)
    with dissolve
    player_name "O-oke."

    show old_rossg 1
    ross "Sekarang, silakan."

    show old_rossg 2
    ross "Kalian berdua..."

    show old_rossg 1
    ross "... Rasakan bentuknya."

    show old_rossg 4
    mia "Hehehe, oke!"

    show old_rossg 5_6 with dissolve
    pause
    show old_rossg 3 with dissolve
    player_name "... Seperti itu?"

    show old_rossg 1
    ross "Mmmhmm... Begitu saja..."

    show old_rossg 4
    mia "Hehehee, kuharap Tuhan tidak memperhatikan..."

    show old_rossg 2
    ross "Anda berdua melakukan pekerjaan dengan baik!"

    show old_rossg 1
    ross "Terus berlanjut."

    show old_rossg 5_6 with dissolve
    pause
    ross "Hmm..."

    pause
    show old_rossg 1 with dissolve
    ross "Bagus sekali, {b}[firstname]{/b}!"

    show old_rossg 2
    ross "Sekarang coba rasakan, bentuk {b}Mia{/b}."

    show old_rossg 3
    player_name "aku uhh..."

    show old_rossg 4
    mia "Tidak apa-apa!"

    mia "Rasakan bentuknya, {b}[firstname]{/b}!"

    show old_rossg 7_8 at Position(xpos=0.59, ypos=1.0) with dissolve
    pause
    show old_rossg 4 at Position(xpos=0.6, ypos=1.0) with dissolve
    mia "Klakson klakson!"

    show old_rossg 9 with dissolve
    mia "Pfft, hahahahahaha!!"

    show old_rossg 2 with dissolve
    ross "Oh, bukankah dia adalah hal yang paling menggemaskan?!"

    ross "Baiklah, sekarang rasakan milikku lagi..."

    show old_rossg 5_6 with dissolve
    pause
    show old_judith 58f
    judith "... Kalian bisa merasakan bentukku jika kalian mau."

    show old_judith 57f
    show old_rossg 2 with dissolve
    ross "Ya ampun! Lihat siapa yang akhirnya keluar dari cangkangnya!"

    ross "Kami akan menemuimu sebentar lagi, sayang. Mengapa kamu tidak memeriksa lemari persediaan untukku..."

    ross "Seharusnya ada dupa dan lilin di sana untuk membantu kita mengatur suasana hati."

    show old_judith 58f
    show old_rossg 5_6 with dissolve
    judith "... Ya, Bu."

    hide old_judith
    with dissolve
    pause
    show old_rossg 10 with dissolve
    smith "WHAT IN THE WORLD IS GOING ON IN HERE?!" with hpunch
    smith "KENAPA KALIAN SEMUA TELANJANG?!"

    hide old_rossg
    show old_mia 83 zorder 2 at left
    show old_ross 39 zorder 1 at Position(xpos=0.25, ypos=1.0)
    show player 100 zorder 0 at Position(xpos=0.35, ypos=1.0)
    show principal 3 at right
    with dissolve
    ross "{b}Ny. Smith{/b}! Saya baru saja mengajari siswa beberapa teknik seni..."

    show old_ross 38
    show principal 38
    smith "TEKNIK SENI?! APAKAH AKU TERLIHAT SEPERTI IDIOT BAGIMU?!"

    show old_ross 39
    show principal 3
    ross "Tentu saja tidak, kami hanya-"

    show principal 28
    show old_ross 38
    smith "APAKAH SAYA PERLU MENGINGATKAN ANDA BAHWA INI ADALAH SEKOLAH DAN BUKAN BORTHEL!"

    show old_ross 39
    show principal 3
    ross "Anda bersikap konyol, saya hanya mencoba membantu mereka meningkatkan seni mereka."

    hide principal
    show principal 34 zorder 3 at Position(xpos=0.65, ypos=1.0)
    with dissolve
    show old_ross 38
    smith "JUST GET SOME CLOTHES ON, ALL OF YOU!" with hpunch

    hide old_mia
    hide player
    show principal 29 at right
    show old_ross 17 at Position(xpos=0.25, ypos=1.0)
    with dissolve
    pause
    show old_ross 16 at Position(xpos=0.25, ypos=1.0) with dissolve
    pause
    show old_ross 15 at Position(xpos=0.26, ypos=1.0) with dissolve
    pause
    show old_ross 14 at Position(xpos=0.26, ypos=1.0) with dissolve
    pause
    show old_ross 24 zorder 1 at Position(xpos=0.25, ypos=1.0)
    show old_mia 41 zorder 2 at left
    show player 8 zorder 0 at Position(xpos=0.35, ypos=1.0)
    with dissolve
    show principal 27
    smith "Anda sebaiknya memiliki penjelasan yang bagus untuk ini, {b}Barbara{/b}!"

    show old_mia 45
    show player 11 at Position(xpos=0.38, ypos=1.0)
    with dissolve
    show old_ross 25
    show principal 29
    ross "{b}Mia{/b} dan saya membantu {b}[firstname]{/b} di sini latihan."

    ross "Mencoba mempersiapkan dia untuk-"

    show old_ross 24
    ross "..."
    show principal 27
    smith "Persiapkan dia untuk apa?!"

    show principal 29
    show old_mia 46
    mia "Ini adalah-"

    show old_mia 45
    show old_ross 25
    ross "Hadiah!"

    ross "... Dia akan melukis sesuatu untuk Anda, {b}Ny. Smith{/b}!"

    show old_ross 24
    pause
    show old_ross 25
    ross "Hadiah, untuk digantung di kantor Anda!"

    show old_ross 24
    show principal 27
    smith "Hadiah?! Untukku?! Apa, seperti potret?"

    show principal 29
    show old_ross 25
    ross "Tentu saja! Jika itu yang kamu inginkan..."

    show principal 27
    show old_ross 24
    smith "Apakah dia baik?"

    show old_ross 25
    show principal 29
    ross "Bagus sekali, ayo lihat sendiri!"

    show principal 41 with dissolve
    pause
    show principal 42
    smith "Apa ini?"

    show principal 41
    show old_mia 46
    mia "Oh, itu umm... Itu punyaku, Bu."

    mia "... Aku tidak terlalu baik."

    show old_mia 45
    smith "..."
    show principal 42
    smith "Lalu kenapa kamu ada di sini, sepulang sekolah, mengambil kursus privat?"

    show principal 41
    show old_ross 25
    ross "Kelas saya bukan hanya untuk seniman berbakat."

    ross "Mereka terbuka bagi siapa saja yang ingin mengekspresikan diri melalui seni."

    ross "... Dan {b}Mia{/b} di sini memiliki kecintaan yang besar terhadap seni."

    show old_ross 24
    show principal 42
    smith "Eh ya..."

    smith "Kenyataannya, Anda baru saja menemukan paket kecil yang lucu, bukan?"

    show principal 41
    show old_ross 25b
    ross "Itu bukan..."

    show old_ross 24
    show principal 42
    smith "... Dan sekarang kamu hanya berusaha membukanya, ya?"

    smith "Apakah kamu punya sedikit rasa?"

    smith "... Saya sangat mengetahui metode Anda {b}Barbara{/b}."

    hide principal
    show principal 43 at Position(xpos=0.7, ypos=1.0)
    with dissolve
    pause
    show principal 44 at Position(xpos=0.72, ypos=1.0) with dissolve
    smith "Hmm."

    show principal 45
    smith "Anak laki-laki itu melukis ini?"

    show principal 44
    show player 10
    player_name "Ya, Bu."

    show player 11
    show principal 45
    smith "Yah, sepertinya aku salah tentangmu, {b}[firstname]{/b}."

    smith "Lagipula, kamu sebenarnya bagus untuk sesuatu..."

    show principal 44
    show old_ross 11
    ross "Dia sangat berbakat, bukan?"

    show old_ross 24
    hide principal
    show principal 27 at right
    with dissolve
    smith "Oh, diamlah!"

    smith "Aku harus memecatmu, sekarang juga!"

    smith "Di sini diraba oleh siswa telanjang..."

    hide principal
    show principal 35b at Position(xpos=0.83, ypos=1.0)
    with dissolve
    smith "..."
    show principal 35c
    smith "Ini adalah pekerjaan yang mengesankan."

    show principal 35
    smith "Hmm..."

    hide principal
    show principal 27 at right
    with dissolve
    smith "Aku merasa bermurah hati, jadi aku {i}MUNGKIN{/i} membiarkan kejadian ini berlalu begitu saja!"

    show old_ross 25
    show principal 26
    ross "Itu akan menjadi keajaiban-"

    show old_ross 24
    show principal 27
    smith "... Tapi hanya jika murid Anda di sini dapat menciptakan kembali kualitas ini pada potret saya!"

    show principal 26
    show old_ross 25
    ross "Oh, itu seharusnya tidak menjadi masalah. Benar, {b}[firstname]{/b}?"

    show old_ross 24
    show player 10
    player_name "Uhh..."

    show player 11
    show principal 27
    smith "Dan itu harus sesuai dengan spesifikasi saya!"

    smith "Bukan urusan yang lucu!"

    show principal 29
    show old_ross 25
    ross "Oh tentu! Apa pun yang Anda inginkan, Bu."

    show principal 27
    show old_ross 24
    smith "Benar sekali, apapun yang kuinginkan!"

    show principal 27
    smith "Sekarang kalian, anak-anak, pulanglah sebelum aku berubah pikiran dan mengusir kalian berdua!"

    show principal 29
    show old_ross 25
    ross "Ayo kalian berdua. Sampai jumpa besok."

    return

label button_ross_found_model.replay:
    $ player.go_to(L_school_artclassroom)
    jump button_ross_found_model
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
