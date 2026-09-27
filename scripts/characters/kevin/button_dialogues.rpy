label k01_intro:
    scene cafeteria_b
    show player 2 at left with dissolve
    show old_kevin 1 at right with dissolve
    player_name "Hai, {b}Kevin{/b}!"

    show player 1 at left
    show old_kevin 2 at right
    kevin "Hei, kawan..."

    show old_kevin 1 at right
    show player 10 at left
    player_name "Kamu sedang bertugas di kantin ya..."

    show old_kevin 2 at right
    show player 13 at left
    kevin "Ya! Aku punya dua bulan lagi dari omong kosong ini."

    show old_kevin 1 at right
    show player 17 at left
    player_name "Itu menyebalkan."

    show old_kevin 2 at right
    show player 1 at left
    kevin "Ya, tapi apa yang bisa kulakukan?"

    kevin "Ngomong-ngomong, apakah {b}Dexter{/b} membuat kalian kesulitan di lorong?"

    show old_kevin 1 at right
    show player 24 at left
    player_name "Ya, dia dan {b}Roxxy{/b} selalu menangani kasus kami..."

    show player 26 at left
    player_name "Tapi itu bukan apa-apa. Saya tidak terlalu peduli dengan apa yang mereka katakan."

    show old_kevin 3 at right
    show player 11 at left
    kevin "Bung. Anda harus membela diri sendiri."

    show old_kevin 1 at right
    show player 10 at left
    player_name "Aku lebih suka menghindarinya, kau tahu?"

    player_name "Tidak ada gunanya bertengkar dengan pria yang ukurannya dua kali lipat dariku."

    show old_kevin 3 at right
    show player 11 at left
    kevin "Anda tidak bisa membiarkan dia menginjak-injak Anda. Bagaimana Anda bisa bertahan kuliah seperti itu?"

    show old_kevin 1 at right
    show player 24 at left
    player_name "Yah, aku terlalu lemah untuk berbuat apa pun."

    show old_kevin 4 at right
    show player 11 at left
    kevin "Hmm... Mungkin kita bisa melakukan sesuatu."

    show old_kevin 1 at right
    show player 10 at left
    player_name "Apa maksudmu?"

    show old_kevin 4 at right
    show player 1 at left
    kevin "Baiklah, saya bisa {b}membantu Anda berolahraga di Gym{/b}..."

    kevin "Seperti melihat Anda saat Anda sedang mengangkat beban, dan menunjukkan beberapa trik."

    show player 13
    show old_kevin 2
    kevin "Aduh, ini akan membuatku depresi..."

    kevin "Kau tahu aku ingin berada di sana membantu saudaraku terkoyak!"

    show old_kevin 1
    pause
    show old_kevin 4
    kevin "Ck, kamu tahu apa..."

    show old_kevin 2
    kevin "Aku ingin tahu apakah aku bisa menyelinap keluar dari sini?"

    show old_kevin 1
    show player 5
    player_name "Hmm?"

    show old_kevin 2
    kevin "Maksudku, jika kita bisa {b}menemukan seseorang untuk membagi pekerjaan{/b}..."

    kevin "... Saya bisa pergi ke gym di pagi hari."

    kevin "Bisa banget berhasil gan!"

    show old_kevin 1
    show player 10
    player_name "Apa maksudmu?"

    show player 5
    show old_kevin 2
    kevin "Baiklah, {b}Ny. Smith{/b} tidak pernah datang ke sini di pagi hari."

    kevin "Jadi selama pekerjaan itu selesai, tidak masalah siapa yang melakukannya."

    show old_kevin 1
    show player 14
    player_name "Jadi kami hanya perlu {b}menemukan seseorang untuk membagi pekerjaan dengan Anda{/b}?"

    show player 13
    show old_kevin 2
    kevin "Ya, Anda punya ide?"

    show old_kevin 1
    show player 4
    pause
    show player 14
    player_name "Hmm, saya mungkin bisa meyakinkan {b}Erik{/b} untuk melakukannya."

    show player 13
    show old_kevin 2
    kevin "Oh, itu akan luar biasa, kawan!"

    show old_kevin 1
    show player 14
    player_name "Saya akan {b}bertanya padanya{/b} tentang hal itu."

    show player 13
    show old_kevin 2
    kevin "Ya, ya!"

    show old_kevin 1
    return

label k01_prompt:
    show old_kevin 2
    kevin "Anda {b}berbicara dengan Erik{/b} tentang membantu saya?"

    show old_kevin 1
    show player 29 with dissolve
    player_name "Tidak, belum."

    show player 3
    show old_kevin 2
    kevin "Ugh, kamu harus cepat, kawan!"

    show old_kevin 2b with dissolve
    kevin "Otot-ototku melemah di sini!"

    show old_kevin 1 with dissolve
    show player 14 with dissolve
    player_name "Hehe, santai saja."

    player_name "Saya akan berbicara dengannya."

    show player 13
    return

label k01_outro:
    show old_kevin 2
    kevin "Anda {b}berbicara dengan Erik{/b} tentang membantu saya?"

    show old_kevin 1
    show player 17
    player_name "Ya."

    player_name "Dia akan melakukannya."

    show player 13
    show old_kevin 2b with dissolve
    kevin "NERAKA!"

    kevin "YA!"

    kevin "KAWAN!"

    show old_kevin 2c with dissolve
    kevin "Anda adalah pria yang aneh!"

    show old_kevin 6 with dissolve
    kevin "Akhirnya, saya bisa kembali ke aktivitas dua hari saya!"

    show old_kevin 5
    show player 14
    player_name "Heh, jadi aku rasa aku akan menemuimu di gym pada {b}Pagi{/b}?"

    show player 13
    show old_kevin 9b with dissolve
    kevin "Anda tahu itu, kawan!"

    hide old_kevin
    hide player
    with dissolve
    return

label kevin_greeting_sad:
    scene expression player.location.background_blur with None
    show player 13 at left
    show old_kevin 2 at right
    with dissolve
    kevin "Sup, kawan?!"

    show old_kevin 1
    show player 14
    player_name "Hai, {b}Kevin{/b}."

    show player 13
    show old_kevin 2
    kevin "Anda di sini untuk menggosok beberapa pot?"

    show old_kevin 1
    show player 17
    player_name "Heh, tidak mungkin kawan!"

    show player 13
    show old_kevin 2
    kevin "Ugh, tugas kantin ini menyebalkan, kawan!"

    show old_kevin 1
    pause
    show old_kevin 2
    kevin "... Dan bukan tipe yang keren juga."

    show old_kevin 1
    show player 29 with dissolve
    player_name "Eh, benar..."

    show player 5 with dissolve
    return

label kevin_greeting_happy:
    show old_kevin magic 1 at right
    show player 14 at left
    with dissolve
    player_name "Hai, {b}Kevin{/b}!"

    show player 13
    show old_kevin magic 2
    kevin "Halo, {b}[firstname]{/b}."

    show old_kevin magic 1
    show player 14
    player_name "Ada apa?"

    show player 13
    show old_kevin magic 2
    kevin "Tidak banyak. Kemarin adalah hari glutes bagi saya."

    kevin "Pantatku sakit!"

    kevin "Rasakan betapa ketatnya itu!"

    show old_kevin magic 1
    show player 10
    player_name "Uhhh... Tidak, terima kasih kawan."

    show player 13
    show old_kevin magic 2
    kevin "Kerugianmu!"

    return

label kevin_somrak_first:
    show player 10 at left
    show old_kevin magic 1 at right
    player_name "Jadi saya bertemu dengan pelatih {b}Muay Thai{/b} baru yang Anda bicarakan."

    show player 5
    show old_kevin magic 2
    kevin "Langsung saja, kawan!"

    kevin "Dia cukup hebat, kan?!"

    show old_kevin magic 1
    show player 12
    player_name "Dia benar-benar gila!"

    show player 5
    show old_kevin magic 2
    kevin "Hah?"

    show old_kevin magic 1
    show player 12
    player_name "Ya, dia bilang dia tidak akan mengajariku kecuali aku membawakannya {b}celana bekas{/b}!"

    show player 5
    show old_kevin magic 2
    kevin "Oh, itu..."

    show old_kevin magic 3 with dissolve
    kevin "Hmm."

    show old_kevin magic 4
    show player 10
    player_name "Tunggu sebentar..."

    show player 14
    player_name "Kamu membawakannya sepasang, bukan?!"

    show player 13
    show old_kevin magic 3
    kevin "Eh, ya."

    show old_kevin magic 4
    show player 14
    player_name "Bung, serius?"

    show player 13
    show old_kevin magic 2 with dissolve
    kevin "Ya, saya mendengar semua hal luar biasa tentang dia, dan saya penasaran..."

    kevin "Setelah Anda melewati masalah celana dalam, dia benar-benar sah!"

    show old_kevin magic 1
    show player 11
    player_name "..."
    show old_kevin magic 2
    kevin "aku serius!"

    kevin "Dia benar-benar tahu apa yang dia lakukan, kawan."

    show old_kevin magic 1
    show player 14
    player_name "Di mana Anda mendapatkan {b}celana bekas{/b}?"

    show player 13
    show old_kevin magic 3 with dissolve
    kevin "Oh, eh... Aku agak... Mengambil sepasang milik ibuku, dari keranjang pakaian kotor."

    show old_kevin magic 4
    show player 12
    player_name "Bung..."

    show player 5
    show old_kevin magic 2 with dissolve
    kevin "Apa?!"

    kevin "Ini tidak aneh."

    kevin "Saya hanya mengambil satu pasang dan bukan berarti saya mengambilnya untuk saya."

    kevin "Saya memberikannya kepada {b}Master Somrak{/b}."

    show old_kevin magic 1
    show player 14
    player_name "Cukup aneh {b}Kevin{/b}."

    show player 13
    show old_kevin magic 2
    kevin "Tidak, kawan."

    kevin "Anda terpaku pada hal-hal sepele..."

    kevin "Anda punya beberapa gadis di rumah Anda, bukan?"

    show old_kevin magic 1
    show player 10
    player_name "Ya, tapi-"

    show player 11
    show old_kevin magic 2
    kevin "Baiklah, ini dia! Ambil saja satu pasang dan Anda sudah masuk!"

    kevin "Sebenarnya bukan masalah besar, kawan."

    show old_kevin magic 1
    show player 35
    player_name "Hmm, entahlah..."

    show player 34
    show old_kevin magic 2
    kevin "Lakukan saja, {b}[firstname]{/b}."

    kevin "{b}Ajaran Guru Somrak{/b} akan mengubah hidup Anda, saya beri tahu ya!"

    show old_kevin magic 1
    show player 33
    player_name "Saya kira saya bisa mengambil satu pasang..."

    show player 13
    show old_kevin magic 2
    kevin "Lihat, ini dia!"

    show old_kevin magic 1
    show player 14
    player_name "Saya akan {b}memeriksa sekeliling rumah saya{/b} dan melihat apakah saya dapat {b}menemukan sepasang celana dalam [deb_name] atau [jen_name]{/b}."

    show player 13
    return

label kevin_somrak_repeat:
    show player 10
    player_name "Aku tidak percaya orang ini menyuruhku mencuri {b}celana bekas{/b}..."

    show player 5
    show old_kevin magic 2
    kevin "Itu bukan masalah besar, kawan!"

    kevin "Cukup gesek sepasang dari rumah."

    show old_kevin magic 1
    show player 37 with dissolve
    player_name "Ya, ya."

    player_name "Saya akan {b}memeriksa sekeliling rumah saya{/b} dan melihat apakah saya dapat {b}menemukan sepasang [deb_name] atau [jen_name]{/b}."

    show player 13 with dissolve
    return

label kevin_magazines:
    show player 2 at left
    show old_kevin 29b at right
    with dissolve
    player_name "Hai, {b}Kevin{/b}!"

    show player 1
    show old_kevin 30
    kevin "Ada apa, {b}[firstname]{/b}?"

    show player 2
    show old_kevin 29b
    player_name "Tidak banyak. Apa yang kamu baca?"

    show player 1
    show old_kevin 30b
    kevin "Oh, hanya beberapa majalah olahraga yang saya dapatkan dari gym."

    show player 2
    show old_kevin 29b
    player_name "Keren, Anda mencoba olahraga baru atau apa?"

    show player 1
    show old_kevin 30
    kevin "Tidak Memangnya kenapa?"

    show player 11
    show old_kevin 29
    player_name "..."
    show old_kevin 31 with dissolve
    kevin "Ayo lihat beefcake ini, {b}[firstname]{/b}!"

    show player 10
    show old_kevin 31b
    player_name "... kue daging sapi?"

    show player 11
    player_name "..."
    show player 10
    player_name "Uh, benar... Menurutmu aku boleh mengambil beberapa majalah ini?"

    show player 11
    show old_kevin 30 with dissolve
    kevin "Heh, aku tidak tahu kamu adalah sesama penikmat bentuk maskulin..."

    show player 10
    show old_kevin 29
    player_name "Sebenarnya, saya sedang membuat kolase."

    show player 11
    show old_kevin 30b
    kevin "Oh benar. Kolase."

    show old_kevin 31 with dissolve
    kevin "Aku mengerti, kawan! Jangan katakan lagi!"

    kevin "Ambil semua yang Anda butuhkan! Yang ini akan membuatku sibuk untuk sementara waktu."

    show player 2
    show old_kevin 31b
    player_name "Luar biasa! Terima kasih, uh, kawan..."

    show player 1
    show old_kevin 31c
    kevin "Sial, dia berkilau..."

    show player 10
    player_name "..."
    return

label kevin_modeling:
    show player 2 at left
    show old_kevin 1 at right
    player_name "Saya sedang mengerjakan proyek untuk {b}Miss Ross{/b} dan itu memerlukan model langsung."

    player_name "Apakah Anda tertarik?"

    show old_kevin 2
    show player 1
    kevin "Pemodelan. Sepertinya aku harus berdiri di sana?"

    show player 2
    show old_kevin 1
    player_name "Ya, kamu hanya perlu berdiri disana."

    show player 10
    player_name "Telanjang."

    show old_kevin 3
    show player 11
    kevin "Telanjang?!"

    kevin "Ya ampun. Entahlah, kawan."

    kevin "Apakah kamu hanya akan menggambar di sana?"

    show player 10
    show old_kevin 1
    player_name "Baiklah, {b}Mia{/b} dan saya berdua akan menggambar."

    player_name "{b}Nona Ross{/b} akan hadir juga."

    show player 11
    show old_kevin 4
    kevin "Uh, lulus..."

    show old_kevin 3
    kevin "Aku tak mau perempuan melihatku telanjang, kawan. Itu agak menjijikkan."

    show old_kevin 1
    player_name "..."
    show player 10
    player_name "O-oke."

    return

label kevin_guitar_intro:
    show player 10
    player_name "Saya membantu {b}Nona Dewitt{/b} mencari sukarelawan untuk pertunjukan bakat."

    player_name "Bukankah kamu biasa bermain gitar?"

    show player 5
    show old_kevin magic 2
    kevin "Ya, dulu."

    show old_kevin magic 1
    show player 10
    player_name "Apa yang telah terjadi?"

    show player 5
    show old_kevin magic 2
    kevin "Ah, mantanku agak menghancurkannya setelah aku putus dengannya."

    show old_kevin magic 1
    show player 12
    player_name "Dia?"

    show player 11
    show old_kevin magic 3 with dissolve
    kevin "Apakah aku mengatakannya padanya? Maaf, maksudku dia."

    kevin "... Ya, DIA menghancurkannya berkeping-keping."

    show old_kevin magic 1 with dissolve
    show player 14
    player_name "Hah, kamu punya sesuatu untuk gadis-gadis gila, ya?"

    show player 13
    show old_kevin magic 3 with dissolve
    kevin "Hehe, kamu tahu itu! Gadis-gadis gila, aku suka sekali dengan mereka! Benar-benar..."

    show old_kevin magic 1 with dissolve
label kevin_guitar_prompt:
    show player 14
    player_name "Jadi, {b}jika kamu punya gitar, apakah kamu akan bermain di acara pencarian bakat{/b}?"

    show player 13
    show old_kevin magic 2
    kevin "Ya, saya tidak keberatan."

    kevin "Tapi di mana aku bisa mendapatkan gitar? Harganya sangat mahal!"

    show old_kevin magic 1
    if M_dewitt.is_state(S_dewitt_replace_guitar):
        show player 34
        player_name "( {b}Saya perlu mengganti gitar buatan saya dengan yang ada di ruang bawah tanah Erik{/b}! )"

    else:
        show player 35
        player_name "Hmm, maybe I can find you one..."

        show player 34
        player_name "( {b}Erik has a bunch in his basement{/b}. Maybe I can borrow one? )"

    show player 14
    player_name "I'll be back!"

    show player 13
    show old_kevin magic 2
    kevin "Baiklah."

    return

label kevin_guitar_outro:
    show player 14
    player_name "I found a guitar for you!"

    show player 13
    show old_kevin 24
    kevin "Benar-benar?"

    show old_kevin 23
    show player 239_240 with dissolve
    pause
    show player 577 with dissolve
    player_name "Bagaimana menurutmu?"

    show player 13 with dissolve
    show old_kevin 16f with dissolve
    kevin "Holy crap! Where did you get this thing?"

    kevin "This thing is really high end!"

    show old_kevin 14f
    show player 10
    player_name "Dia?"

    show player 5
    show old_kevin 15f
    kevin "Uhh, yeah bro!"

    kevin "I hope you didn't steal it or something."

    show old_kevin 14f
    show player 14
    player_name "Borrowed it actually, from a friend of mine. So be careful with it, yeah?"

    hide player
    show old_kevin 27 at left
    with dissolve
    kevin "No problems there!"

    kevin "I'll treat this beauty with the respect it deserves!"

    show old_kevin 28
    player_name "Cool, so you're down to play it for the talent show."

    show old_kevin 27
    kevin "I'm down!"

    show old_kevin 28
    player_name "Awesome! I'll see you in {b}Miss Dewitt{/b}'s class soon for practice then!"

    show old_kevin 27
    kevin "Sounds good, bro!"

    show player 13 at left
    show old_kevin 16 at right
    with dissolve
    kevin "I'm gonna call you... Devin."

    kevin "Would you like that beautiful?"

    show player 11
    hide old_kevin with dissolve
    player_name "..."
    return

label kevin_adhesive_prompt:
    show player 10
    player_name "What do we need for that {b}adhesive{/b} again?"

    show player 13
    show old_kevin 2
    kevin "Just {b}meet me in the science lab after class{/b}."

    kevin "I'll take care of the rest."

    show old_kevin 1
    show player 14
    player_name "Awesome! Thanks, {b}Kevin{/b}!"

    return

label kevin_goodbye:
    show old_kevin 1
    show player 14
    player_name "Anyways, I gotta go."

    if M_kevin.finished_state(S_kevin_erik_agreed):
        show player 13
        show old_kevin 2
        kevin "I'd better see you at the gym tomorrow, bro!"

        kevin "Bright and early! Am I right?"

        show old_kevin 1
        show player 14
        player_name "Mungkin..."

    else:
        player_name "Keep your spirits up, man."

        show player 13
        show old_kevin 2
        kevin "Yeah, alright bro."

        kevin "See ya around."

    hide old_kevin
    hide player
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
