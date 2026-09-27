label bridget_dialogue_eve_dress_code_intro_repeat:
    anon f_worried "Sebenarnya, saya berharap Anda bisa berbicara dengan {b}Nyonya. Smith{/b} tentang kebijakan aturan berpakaian yang baru..."

    bridget a_crossed "Ah, ah, ah!"

    bridget f_sexy "Anda ingat kesepakatan kita?"

    show bridget b_pickup with dissolve
    show anon f_worried_low
    pause
    show bridget b_dressed a_ropes with dissolve
    show anon f_unimpressed
    bridget "Anda membantu saya..."

    show bridget a_ropes_throw with dissolve
    pause
    show bridget a_idle
    show anon a_ropes_bunch
    with dissolve
    bridget "... Dan aku membantumu."

    anon f_tired "{i}*Huh*{/i} Ya, saya ingat."

    bridget a_hips "Pisahkan itu dan kita akan bicara."

    hide bridget with dissolve
    anon f_sad_down "..."
    scene black with fade
    pause
    return

label bridget_dialogue_eve_dress_code_failure_first:
label bridget_dialogue_eve_dress_code_failure_repeat:
    scene expression player.location.background_closeup
    show anon a_ropes_tangled f_hurt
    show bridget
    with fade
    bridget "Nah, bagaimana perkembangannya di-"

    show bridget f_surprised
    anon f_tired "Ehh, itu tidak berjalan dengan baik..."

    bridget f_normal @ f_laugh a_laugh "Hahahaah!"

    bridget "Bagaimana kamu bisa-"

    anon f_unimpressed "Saya tidak tahu!"

    bridget "Sini, izinkan saya membantu Anda."

    scene black with fade
    pause
    scene expression player.location.background_closeup
    show anon a_rub
    show bridget a_ropes
    with dissolve
    bridget "Di sana."

    anon f_worried "Maaf, {b}Pelatih Bridget{/b}."

    bridget @ f_sexy "Hehe, jangan khawatir..."

    bridget "Anda bisa mencobanya lagi besok."

    anon f_sad_down "..."
    bridget "Kecuali jika Anda tidak lagi membutuhkan bantuan saya dengan apa pun yang Anda keluhkan sebelumnya?"

    anon f_tired "Kebijakan aturan berpakaian."

    bridget "Ya, itu..."

    pause
    bridget a_crossed "Sampai jumpa besok?"

    anon f_sad_down "Ya baiklah."

    hide bridget with dissolve
    anon f_thinking a_thinking @ -m_talk "(Hmm, kalau saja aku tidak terlalu canggung...)"

    anon @ -m_talk "( Mungkin {b}Saya harus berbicara dengan pelatih Muay Thai di Gym{/b}? )"

    hide anon with dissolve
    return


label bridget_dialogue_eve_dress_code_success_first:
label bridget_dialogue_eve_dress_code_success_repeat:
    scene expression player.location.background_closeup
    show anon a_ropes f_grin
    show bridget
    with fade
    bridget "Nah, bagaimana perkembangannya di-"

    show bridget f_surprised
    anon @ f_laugh "Aku baru saja menguraikan yang terakhir!"

    bridget f_sexy "Wow, kerja bagus {b}[firstname]{/b}!"

    bridget f_normal a_hips "Saya pikir itu akan memakan waktu berminggu-minggu bagi Anda untuk menyelesaikannya..."

    anon f_normal "Yah, aku senang sekali hal itu tidak terjadi!"

    anon "Maukah kamu membantuku soal aturan berpakaian sekarang?"

    bridget "Itu tergantung pada apa sebenarnya yang Anda ingin saya lakukan?"

    bridget "Kalian harus tahu bahwa aku tidak terlalu peduli dengan apa yang kalian kenakan saat berada di sekolah."

    anon f_worried "Itu bukan bagian yang menggangguku..."

    anon "Tahukah Anda {b}Ny. Smith{/b} melarang pewarna rambut?"

    show bridget f_surprised
    pause
    bridget f_angry "Apa?!"

    anon "Ya, baik untuk mahasiswa maupun dosen..."

    bridget "Dia berada di atas mayatku!"

    hide bridget with dissolve
    anon f_confused "Jadi, kamu akan berbicara dengannya tentang-"

    anon f_worried @ -m_talk "(Whoa, dia buru-buru pergi...)"

    anon @ -m_talk "(Saya mungkin harus mengikutinya.)"

    scene black with fade
    pause
    scene expression "backgrounds/location_school_third_sideview_day.jpg" with None
    show anon b_dressed_bending1:
        flip
        xoffset -200
    with dissolve
    pause
    scene expression "backgrounds/location_school_office_spying.jpg"
    show bridget f_angry:
        flip
    show smith
    with fade
    bridget "Di atas mayatku, kamu melarang pewarna rambut!"

    smith "Oh, ayolah, {b}Bridget{/b}..."

    smith "Lagi pula, kamu terlalu tua untuk mengecat rambutmu!"

    bridget "Usiaku bukan urusanmu!"

    bridget "Aku suka rambutku dan tak seorang pun memaksaku mengubahnya, apalagi kamu!"

    smith "Anda tidak dapat berbicara kepada saya seperti itu!"

    bridget "Sialnya aku tidak bisa!"

    bridget "Anda melanggar hak saya, dan saya tidak akan membelanya!"

    smith "Astaga, tenanglah!"

    smith "{i}*Huh*{/i} Aku akan minta {b}Annie{/b} menyimpan kebijakan bodoh itu besok, oke?!"

    smith "Lagipula itu semua adalah ide bodohnya..."

    smith @ f_eyeroll "Gadis itu bahkan tidak bisa menulis kebijakan aturan berpakaian sederhana tanpa membuatku pusing..."

    bridget "Lagipula, kita tidak memerlukan aturan berpakaian, ini sekolah negeri!"

    smith "Ya, ya, kamu sudah menang, {b}Bridget{/b}..."

    smith "Keluar saja sebelum aku kehilangan kesabaran."

    bridget "Cih, terserah."

    hide bridget
    show bridget f_eyeroll:
        xoffset -400
    with dissolve
    bridget "... Dasar jalang tua."

    hide bridget with dissolve
    smith "..."
    scene expression "backgrounds/location_school_third_sideview_day.jpg" with None
    show anon b_dressed_bending1:
        flip
        xoffset -200
    with dissolve
    anon "(Whoa, dia benar-benar membohonginya!)"

    pause
    anon "(Oh sial, dia keluar!)"

    hide anon
    show anon f_surprised_teeth b_dressed a_rub:
        flip
    show bridget:
        flip
    with dissolve
    bridget @ -m_talk "..."
    anon a_idle f_worried @ a_rub "J-jadi... {i}*Ahem*{/i} B-bagaimana hasilnya?"

    bridget "Semuanya sudah diurus."

    anon f_surprised @ f_shock "Dengan serius?!"

    bridget "Ya."

    bridget "Anda dapat memberi tahu teman Anda atau apa pun bahwa tidak ada yang perlu dikhawatirkan."

    anon f_normal "Terima kasih, {b}Pelatih Bridget{/b}!"

    bridget @ -m_talk "Mhmm."

    hide bridget with dissolve
    anon f_grin "( Wow, {b}Pelatih Bridget{/b} sama sekali tidak takut pada {b}Nyonya Smith{/b}! )"

    anon "( Saya tidak sabar untuk memberi tahu {b}Eve{/b} kabar baik besok! )"

    hide anon with dissolve
    return

label bridget_dialogue_eve_dress_code_intro_first:
    scene expression player.location.background_blur with None
    show anon f_worried_low
    show bridget b_pickup with dissolve
    bridget "Ugh, kemana perginya makhluk-makhluk sialan itu?!"

    anon "B-permisi, Bu?"

    bridget "Ya, ya... Tunggu sebentar, ya!"

    bridget "{i}*Sigh*{/i} Aku tahu aku melemparkannya ke sini di suatu tempat!"

    anon "Dapatkah saya membantu Anda menemukan sesuatu?"

    bridget "Tidak, aku hanya mencari lompat tali..."

    bridget "Saya ingin menggunakannya di kelas berikutnya dan-"

    bridget "Itu dia!"

    show bridget b_dressed a_ropes f_angry_down with dissolve
    show anon f_worried
    bridget "Ya Tuhan!"

    anon f_surprised_teeth "!!!"
    bridget "Lihatlah bencana ini!"

    show anon f_worried
    bridget f_angry "Aku butuh waktu berhari-hari untuk mengungkap kekacauan ini!"

    anon "Ya, itu sungguh menyebalkan..."

    anon f_surprised @ f_confused "Bagaimanapun, aku sangat berharap kamu bisa membantuku dengan-"

    bridget f_sexy "Tidak uh!"

    anon f_worried "T-tapi aku bahkan belum memberitahumu apa yang kubutuhkan!"

    bridget "Jika kamu ingin bantuanku, kamu akan membantuku terlebih dahulu."

    anon f_unimpressed "Ah, kawan..."

    show bridget a_ropes_throw with dissolve
    bridget "Ini dia, selamat menikmati!"

    show bridget a_idle
    show anon f_surprised_teeth_down a_ropes_bunch
    with dissolve
    bridget f_normal "Ayo temui saya setelah Anda selesai dan MUNGKIN saya akan membantu Anda."

    anon f_tired "Y-ya, Bu..."

    hide bridget with dissolve
    anon f_sad_down "..."
    scene black with fade
    pause
    return

label bridget_button_dress_code_track:
    anon f_worried "Sebenarnya, saya berharap Anda bisa berbicara dengan {b}Nyonya. Smith{/b} tentang kebijakan aturan berpakaian yang baru..."

    bridget "Jangan sekarang, {b}[firstname]{/b}!"

    bridget "Tidak bisakah kamu melihat kita sedang berada di tengah-tengah kelas di sini?!"

    hide bridget with dissolve
    anon f_confused "O-oh, maaf."

    anon f_thinking a_thinking @ -m_talk "( Hmm, aku harus menunggu dan berbicara dengannya di kantornya {b}sepulang sekolah{/b}. )"

    hide anon with dissolve
    return

label coach_bridget_dialogue_office_intro:
    scene expression game.timer.image("coach_office{}_b")
    show anon f_worried
    show bridget f_angry
    with dissolve
    bridget "{b}[firstname]{/b}!"

    bridget "Apa yang kamu lakukan di sini?"

    show anon f_shock
    show bridget a_crossed with dissolve
    anon "Maaf, Bu!!!"

    anon "Saya baru saja punya beberapa pertanyaan!"

    show anon f_surprised
    bridget "Pertanyaan?!"

    bridget "Seperti apa?"

    return

label coach_bridget_dialogue_courtyard_intro:
    scene expression game.timer.image("backgrounds/location_school_gym{}.jpg")
    show anon f_worried
    show bridget f_angry
    with dissolve
    bridget "{b}[firstname]{/b}!"

    bridget "Sebaiknya kamu {b}berlatihlah di gym{/b}, atau aku akan mendorong kakiku ke pantatmu!!"

    show anon f_shock
    show bridget a_crossed with dissolve
    anon "Ya, Bu!!!"

    show anon f_surprised
    bridget "Ada pertanyaan?!"

    return

label coach_bridget_dialogue_training_advice:
    show anon f_worried
    show bridget a_crossed f_normal
    anon "Aku... Nah, di mana aku harus berlatih?"

    show bridget f_angry
    bridget @ -m_talk "..."
    show anon f_surprised
    bridget "Aku baru saja memberitahumu!"

    bridget @ f_angry_yell "Di GYM!!!"

    anon f_worried "Tapi... Apa yang harus saya latih?"

    bridget "Anda harus melatih {b}kekuatan{/b} dan {b}ketangkasan{/b} Anda jika ingin berhasil!"

    bridget "Anda akan berkompetisi dalam lari gawang 110 meter untuk membuat sekolah ini dan tim Anda lolos ke kejuaraan negara bagian!"

    anon "Itu... Banyak tekanan."

    show anon f_surprised_teeth
    bridget "... Dan sebaiknya kamu TIDAK mengecewakanku!"

    show anon f_surprised
    anon "Ya, Bu!!!"

    hide bridget
    hide anon
    with dissolve
    return

label coach_bridget_dialogue_leave:
    show anon f_worried
    show bridget a_crossed f_normal
    anon "Aku... aku lupa."

    bridget f_angry "Lupa? Wah, kamu adalah potongan daging paling menyedihkan yang pernah kulihat!"

    show anon f_surprised
    bridget @ f_angry_yell "Sekarang keluar dari sini dan mulai BEKERJA!!"

    anon f_shock "Ya, Bu!!!"

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
