label judith_dialogue_start:
    scene lefthall_c
    show anon
    show judith
    with dissolve
    judith "Hai {b}[firstname]{/b}!"

    anon "Hai {b}Judith{/b}, bagaimana kabarmu?"

    judith "Oh, aku hebat!"

    judith f_sad @ f_sad_down "Aku... aku hanya ingin mengucapkan terima kasih."

    anon @ f_confused "Oh. Untuk apa?"

    judith "Di {b}ruang ganti putra{/b}... Kamu membuatku merasa... Aman."

    show judith f_normal
    anon f_shy a_behind_head "Oh..."

    judith "Dan tahukah Anda... Anda melawan {b}Annie{/b}. Menurutku itu sangat berani."

    anon a_idle "Tidak apa-apa, {b}Judith{/b}. Saya hanya mencoba melakukan hal yang benar."

    anon f_worried_low "Seharusnya akulah yang minta maaf... Karena menunjukkan padamu... Kau tahu..."

    judith "Oh, tidak apa-apa!! saya menikmati-"

    judith f_sad "Maksudku... aku tidak keberatan sama sekali."

    show anon f_normal
    judith f_normal "Kita baru saja... Mengenal satu sama lain sedikit lebih baik!"

    anon @ f_laugh "Ha ha. Ya. Saya kira begitu..."

    judith "Saya harus pergi! Sampai jumpa di kelas kalau begitu!"

    anon a_wave "Sampai jumpa lagi!"

    return

label judith_dialogue_left_hallway_intro:
    scene lefthall_c
    show judith
    show anon with dissolve
    anon "Hai, {b}Judith{/b}!"

    judith "Oh, hai, {b}[firstname]{/b}."

    judith "Apa kabarmu?"

    anon "Cukup bagus. Apa kabarmu?"

    judith f_sad @ f_sad_down -m_talk "..."
    judith "Baiklah, menurutku."

    return

label judith_dialogue_art_classroom_intro:
    scene art_classroom_c
    show old_judith 1 at right
    show player 14 at left
    show xtra 22 as table zorder 0
    show xtra 23 as basket zorder 0 at Position (ypos = 635)
    show xtra 24 as fruit zorder 0 at Position (ypos = 565)
    with dissolve
    player_name "Menikmati seni, {b}Judith{/b}?"

    show player 13
    show old_judith 5
    judith "Ya!"

    judith "Itu salah satu mata pelajaran favorit saya."

    show old_judith 4
    show player 14
    player_name "Ya, milikku juga!"

    show player 13
    show old_judith 5
    judith "Saya menyukainya karena seburuk apa pun gambar saya, tetap dianggap seni!"

    show old_judith 4
    show player 17
    player_name "Hehe, bagus."

    show old_judith 1
    return

label judith_dialogue_bathroom_fun:
    anon f_normal "Katakanlah, maukah kamu menyelinap ke ruang ganti perempuan sebentar... Kamu tahu?"

    judith f_normal "... Anda benar-benar ingin..."

    judith "... A-denganku?"

    anon "Maksudku, ya!"

    anon "Jika tidak apa-apa?"

    judith "Tentu saja!"

    judith "Ayo pergi!"

    return

label judith_dialogue_dictionary_return:
    hide anon
    hide judith
    show old_judith 1 at right
    show player 14 at left
    player_name "Hai, {b}Judith{/b}! Ini bukumu kembali."

    show player 239_240 with dissolve
    pause
    show player 522 with dissolve
    player_name "Terima kasih lagi!"

    show player 13
    show old_judith 43
    with dissolve
    judith "Oh bagus, aku mulai khawatir.."

    show old_judith 4 with dissolve
    show player 14
    player_name "Tidak perlu khawatir. Ini dalam kondisi prima... Lihat."

    show player 13
    show old_judith 5
    judith "Terima kasih telah berhati-hati, {b}[firstname]{/b}."

    judith "Entah kenapa aku begitu khawatir..."

    show old_judith 4
    show player 14
    player_name "Terima kasih telah mengizinkan saya meminjamnya!"

    show player 13
    show old_judith 5
    judith "Apapun untukmu-"

    show old_judith 3
    judith "Maksudku... S-kapan saja!"

    show old_judith 1
    show player 10
    player_name "Baiklah, sampai jumpa."

    show player 5
    show old_judith 3
    judith "Sampai jumpa, {b}[firstname]{/b}."

    return

label judith_dialogue_bissette_find_full_dictionary:
    hide anon
    hide judith
    show old_judith 1 at right
    show player 14 at left
    player_name "Hai, {b}Judith{/b}! Ada waktu sebentar?"

    show player 13
    show old_judith 5
    judith "Tentu, {b}[firstname]{/b}."

    show old_judith 4
    show player 14
    player_name "Saya berharap bisa {b}meminjam kamus bahasa Prancis Anda{/b}."

    player_name "Saya perlu membuat salinan cepat beberapa halaman dan saya akan mengembalikannya."

    show player 13
    show old_judith 3
    judith "{b}Kamus Bahasa Perancis{/b} saya?"

    show old_judith 5
    judith "Sangat! Selama Anda berjanji untuk berhati-hati?"

    show old_judith 4
    show player 11
    player_name "( Ada apa dengan wanita dan kamus bahasa Perancis mereka? )"

    show player 10
    player_name "Ya, saya akan sangat berhati-hati dan Anda bahkan tidak akan menyadarinya."

    show player 13
    show old_judith 5
    judith "Oke, saya percaya padamu, {b}[firstname]{/b}."

    pause
    show old_judith 43 with dissolve
    judith "Ini dia..."

    show old_judith 4
    show player 522
    with dissolve
    player_name "Terima kasih, {b}Judith{/b}! Aku benar-benar berhutang budi padamu!"

    hide old_judith with dissolve
    show player 13
    player_name "( Baiklah, sekarang {b}pergi ke lab komputer dan salin halaman yang hilang ini{/b}. )"

    return

label judith_dialogue_dewitt_find_flute:
    hide anon
    hide judith
    show old_judith 1 at right
    show player 10 at left
    player_name "Apakah kamu masih memiliki seruling sekolah?"

    player_name "Saya membutuhkannya untuk pertunjukan bakat."

    show player 5
    show old_judith 2
    judith "Oh, um..."

    show old_judith 1
    show player 10
    player_name "Lembar tanda keluar instrumen bertuliskan nama Anda di sebelah seruling."

    show player 5
    show old_judith 2
    judith "{i}*Huh*{/i}"

    show old_judith 3
    judith "Saya memilikinya. Ada di lokerku."

    show old_judith 1
    show player 12
    player_name "Saya merasa akan ada \"tetapi\" yang akan datang?"

    show player 5
    show old_judith 3
    judith "TAPI, aku agak merusaknya..."

    show old_judith 1
    show player 1
    player_name "Kamu memecahkannya?!"

    player_name "Bagaimana hal itu bisa terjadi?"

    show player 5
    show old_judith 5
    judith "Heh, baiklah, aku tidak sengaja..."

    show old_judith 6
    show player 11
    player_name "..."
    show old_judith 2
    judith "... Duduk di atasnya."

    show old_judith 1
    show player 10
    player_name "Anda duduk di atasnya?"

    show player 11
    show old_judith 3
    judith "... Ya."

    show old_judith 5
    judith "Itu menyebalkan karena aku sangat menikmatinya!"

    show old_judith 4
    show player 10
    player_name "Aku tidak tahu kamu bisa memainkan seruling?"

    show player 5
    show old_judith 5
    judith "Ah, aku tidak bisa memainkannya."

    show old_judith 4
    show player 12
    player_name "Kalau begitu, saya tidak mengerti bagaimana Anda menikmatinya?"

    show player 5
    judith "..."
    show old_judith 5
    judith "Hehe, sudahlah."

    show old_judith 2
    judith "Aku berharap tidak ada yang bertanya tentang hal itu..."

    show old_judith 1
    show player 10
    player_name "Mungkin saya bisa memperbaikinya?"

    show player 5
    show old_judith 4
    judith "..."
    show old_judith 5
    judith "Anda dapat mencoba."

    show old_judith 4
    show player 12
    player_name "Apakah masih ada di lokermu?"

    show player 5
    show old_judith 5
    judith "Ya."

    show old_judith 4
    show player 10
    player_name "Baiklah, terima kasih, {b}Judith{/b}."

    return

label judith_dialogue_talent_show_help:
    hide anon
    hide judith
    show old_judith 1 at right
    show player 10 at left
    player_name "Saya ingin tahu apakah Anda ingin berpartisipasi dalam pertunjukan bakat mendatang?"

    show player 5
    show old_judith 3
    judith "Tidak, terima kasih, {b}[firstname]{/b}. Saya tidak begitu tahu cara memainkan alat musik."

    show old_judith 2
    judith "... Dan aku terlalu malu untuk naik ke panggung di depan seluruh sekolah."

    show old_judith 1
    show player 10
    player_name "Bagaimana kalau kita bermain bersama?"

    show player 5
    show old_judith 5
    judith "Anda dan saya?"

    show old_judith 4
    show player 14
    player_name "Tentu, kenapa tidak?"

    show player 13
    show old_judith 6
    judith "Hmm..."

    show old_judith 2
    judith "Tidak, maaf, {b}[firstname]{/b}."

    show old_judith 3
    judith "Aku sama senangnya bermain denganmu; hanya membayangkan menjadi sorotan seperti itu..."

    show old_judith 8f at Position (xoffset=2) with dissolve
    show player 11
    judith "..."
    show old_judith 9f at Position (xoffset=-4) with dissolve
    judith "Permisi, saya perlu ke kamar kecil!"

    hide old_judith with dissolve
    show player 12
    player_name "Sial, aku berpikir sejenak dia akan setuju."

    show player 10
    player_name "Kurasa sebaiknya aku terus mencari..."

    return

label judith_dialogue_okita_get_bifocal_lenses:
    hide anon
    hide judith
    show old_judith 1 at right
    show player 2 at left
    player_name "{b}Judith{/b}, apakah kamu rabun jauh atau rabun jauh?"

    show player 1
    show old_judith 2
    judith "Uhh, baiklah."

    show old_judith 3
    judith "Keduanya..."

    show player 2
    show old_judith 1
    player_name "Benar-benar?!"

    show player 1
    show old_judith 2
    judith "Ya. Aku buta tanpa kacamataku..."

    show old_judith 3
    judith "Cukup norak. saya tahu..."

    show player 2
    show old_judith 1
    player_name "Tidak, itu bagus!"

    show player 1
    show old_judith 3
    judith "Dia?"

    show player 29 with dissolve
    show old_judith 1
    player_name "Maksudku, tidak. Sungguh menyedihkan bahwa Anda tidak dapat melihat tanpa mereka."

    show player 2 with dissolve
    player_name "... Tapi itu juga bagus, karena saya sedang mencari sepasang {b}lensa varifokal{/b}."

    show player 1
    show old_judith 5
    judith "Oh. Nah, Anda menemukan beberapa."

    show player 2
    show old_judith 4
    player_name "Anda tidak akan memiliki satu set cadangan, bukan?"

    show player 1
    show old_judith 5
    judith "Tentu."

    show player 2
    show old_judith 4
    player_name "Luar biasa! Bisakah saya memilikinya?"

    show player 1
    show old_judith 2
    judith "Hmm, kamu ingin aku memberikan set cadanganku saja?"

    show player 10
    show old_judith 1
    player_name "... Ya?"

    show player 11
    show old_judith 3
    judith "Bagaimana dengan perdagangan?"

    show player 2
    show old_judith 1
    player_name "Ya baiklah. Apa yang kamu inginkan?"

    show player 1
    show old_judith 2
    judith "Umm, itu agak memalukan..."

    show old_judith 1
    player_name "..."
    show old_judith 2
    judith "Begini, beberapa gadis lain telah menyusahkanku..."

    show old_judith 3
    judith "... Karena aku belum pernah punya pacar."

    show player 10
    show old_judith 1
    player_name "Itu menyebalkan."

    show player 11
    show old_judith 2
    judith "Ya."

    judith "Aku agak bertanya-tanya..."

    show old_judith 3
    judith "... Yah, aku berharap kamu berpura-pura menjadi pacarku."

    show player 23
    show old_judith 1
    player_name "( !!! )" with hpunch
    show player 10
    player_name "Kamu ingin aku berpura-pura menjadi pacarmu?"

    show player 11
    show old_judith 3
    judith "Just long enough to take a couple pictures!"

    show player 10
    show old_judith 1
    player_name "Pictures?!"

    show player 11
    show old_judith 2
    judith "Ya."

    show old_judith 3
    judith "You meet me in the park, we take a couple pictures like we're boyfriend and girlfriend, and then I'll give you my spare set."

    judith "Deal?"

    show player 10
    show old_judith 1
    player_name "aku uhh..."

    show player 11
    show old_judith 3
    judith "Pleeeease? It would be such a huge help!"

    show player 2
    show old_judith 1
    player_name "Yeah, alright, I suppose I can do that."

    show player 1
    show old_judith 5
    judith "You will?!"

    judith "Okay, meet me at the park! I'll be there in the {b}afternoons{/b}."

    show player 2
    show old_judith 4
    player_name "{b}The park, in the afternoon{/b}. Got it!"

    show player 1
    show old_judith 5
    judith "Great! See you there!"

    return

label judith_dialogue_okita_take_picture_judith:
    hide anon
    hide judith
    show old_judith 1 at right
    show player 2 at left
    player_name "Where did you want to take that picture again?"

    show player 1
    show old_judith 3
    judith "Oh umm, at the park."

    show player 2
    show old_judith 1
    player_name "Baiklah."

    show player 1
    show old_judith 3
    judith "You aren't having second thoughts, are you?"

    show old_judith 2
    judith "'Cause it's okay, we don't hav-"

    show player 2
    show old_judith 1
    player_name "No, {b}Judith{/b}. It's fine, really!"

    show old_judith 4
    player_name "I'll meet you there!"

    show player 1
    show old_judith 5
    judith "... Thanks, {b}[firstname]{/b}."

    return

label judith_dialogue_ross_ask_model:
    hide anon
    hide judith
    show old_judith 1 at right
    show player 2 at left
    player_name "Saya sedang mengerjakan proyek untuk {b}Miss Ross{/b} dan itu memerlukan model langsung."

    player_name "Apakah Anda tertarik?"

    show player 1
    show old_judith 5
    judith "You want me to model for you?"

    show player 2
    show old_judith 4
    player_name "Ya, itu akan luar biasa!"

    show player 10
    player_name "It's nude modeling though..."

    show player 11
    show old_judith 3
    judith "... Oh."

    show old_judith 1
    judith "..."
    show old_judith 3
    judith "... You really want me to?"

    show player 10
    show old_judith 1
    player_name "Tentu saja!"

    show player 11
    show old_judith 5
    judith "Then I'll do it! For you, {b}[firstname]{/b}!"

    show player 2
    show old_judith 4
    player_name "Thanks, {b}Judith{/b}! That's really awesome of you!"

    player_name "Just meet me in art class."

    show player 1
    show old_judith 5
    judith "Baiklah."

    return

label judith_dialogue_left_hallway_leave:
    hide player
    hide old_judith
    show judith
    show anon
    anon f_worried @ -m_talk "..."
    judith f_sad_down @ -m_talk "..."
    anon a_behind_head f_normal "Well... I'd better get going!"

    judith f_normal "Sampai jumpa lagi, {b}[firstname]{/b}."

    return

label judith_dialogue_art_classroom_leave:
    hide player
    hide old_judith
    show anon
    show judith
    anon f_normal "See you later, {b}Judith{/b}."

    judith f_normal "Sampai jumpa, {b}[firstname]{/b}."

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
