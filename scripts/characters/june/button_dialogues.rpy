label june_dialogue_bissette_fix_printer_repeat:
    scene computer_room_printer_c
    show xtra 40
    show june 17 at right
    show player 10 at left
    with dissolve
    player_name "Hai {b}Juni{/b}! Apakah Anda sudah memperbaiki mesin fotokopinya?"

    show player 5
    show june 19
    june "Tidak, maaf. Saya tidak punya waktu untuk mengacaukannya sama sekali."

    show june 17
    player_name "..."
    show player 12
    player_name "Teknologi bodoh!"

    show player 518 with dissolve
    return

label june_dialogue_bissette_fix_printer_first:
    scene computer_room_c
    show player 10 at left
    show june 1 at right
    with dissolve
    player_name "Hai, {b}Juni{/b}?"

    show player 5
    show june 3
    june "Ya, {b}[firstname]{/b}?"

    show june 2
    show player 12
    player_name "Saya mengalami masalah dengan printer. Apa arti surat pemuatan PC?"

    show player 5
    show june 4
    june "Ugh, apa dia melakukannya lagi?! Benar-benar sampah!"

    show june 2
    show player 10
    player_name "Saya hanya perlu memindai beberapa halaman dari buku ini dan mencetaknya."

    player_name "Bisakah Anda membantu saya?"

    show player 5
    show june 3
    june "Ya tentu saja!"

    june "Bukan untuk menyombongkan diri atau apa pun, tapi aku cukup mahir dalam bidang elektronik."

    show june 2
    show player 14
    player_name "Luar biasa!"

    show player 13
    scene black with fade

    scene computer_room_printer_c
    show xtra 40
    show player 13 at left
    show june 9f at right
    with dissolve
    june "Oh, terkadang Anda hanya perlu memulai ulang. Biarkan saya memutar tenaga."

    show june 10f with dissolve
    show player 108f
    player_name "Benar-benar?"

    show player 5
    show june 9f with dissolve
    june "Ya, teknologi itu pilih-pilih seperti itu."

    june "Tinggal menunggu boot up..."

    show player 10
    player_name "Baiklah."

    show player 5
    pause
    pause
    show june 10f with dissolve
    show player 434
    june "Saya pikir itu seharusnya berhasil, tidak-"

    show june 9f with dissolve
    show player 5
    june "Grr... Kesalahan pemuatan PC?!"

    show june 15 with dissolve
    show player 110f
    june "Kamu bagian yang tidak berharga-"

    show june 16 with vpunch
    pause
    show june 15 with dissolve
    june "Saya kira saya harus membukanya dan memperbaikinya lagi."

    show player 10
    player_name "Berapa lama waktu yang dibutuhkan?"

    show player 5
    show june 19 with dissolve
    june "Ini akan memakan waktu cukup lama, saya tidak punya waktu untuk menghadapinya hari ini."

    show june 17
    show player 10
    player_name "Dengan serius?"

    show player 5
    show june 19
    june "Ya, hal ini benar-benar menyebalkan..."

    show june 17
    show player 12
    player_name "Teknologi bodoh!"

    show player 518 with dissolve
    return

label june_dialogue_bissette_fix_printer_fail:
    show player 519 with vpunch
    player_name "..."
    show player 10 with dissolve
    player_name "{i}*Huh*{/i}"

    player_name "Kurasa aku akan menghubungimu kembali besok kalau begitu..."

    show player 5
    show june 19
    june "Maaf, {b}[firstname]{/b}."

    hide player
    hide june
    with dissolve
    return

label june_dialogue_bissette_fix_printer_pass:
    show player 519 with vpunch
    pause
    show player 11 with dissolve
    player_name "!!!"
    show june 18
    june "... Hai! Itu berhasil!"

    show june 17
    show player 10
    player_name "Benar-benar?"

    show player 5
    show june 18
    june "Ya! Anda harus memiliki sentuhan Midas, {b}[firstname]{/b}!"

    show june 17
    show player 14
    player_name "Hah, ya. Saya kira begitu..."

    show player 13
    show june 18
    june "Nah, Anda dapat menyalin halaman Anda sekarang..."

    show june 17
    show player 14
    player_name "Syukurlah! Saya benar-benar perlu mengembalikan buku ini kepada {b}Judith{/b} sebelum dia marah."

    player_name "Terima kasih atas semua bantuan Anda, {b}Juni{/b}!"

    show player 13
    show june 18
    june "Tidak masalah."

    hide june with dissolve
    show player 518 with dissolve
    player_name "Cetak!"

    show player 519 with vpunch
    show xtra_paper 39 at Position (xoffset=100) with dissolve
    pause .25
    hide xtra_paper 39 with dissolve
    show player 184 with dissolve
    pause
    show player 510 with dissolve
    player_name "Baiklah! {b}Saya akhirnya memiliki kamus bahasa Prancis yang lengkap{/b}."

    player_name "Sekarang saya hanya perlu {b}mengembalikan buku Judith kepadanya{/b} dan saya dapat {b}memulai les privat Nona Bissette{/b}."

    show player 509
    hide player with dissolve
    return

label june_dialogue_okita_faptic_engine:
    scene location_school_computer_day_blur
    show player 2 at left
    show june 2 at right
    with dissolve
    player_name "{b}Nona Okita{/b} ingin saya {b}membelikannya sesuatu yang disebut mesin faptic{/b}. Dia bilang padaku kamu bisa membantu?"

    show player 1
    show june 4
    june "Apa yang dia inginkan dengan salah satu dari itu?"

    show player 2
    show june 2
    player_name "Dia bilang dia membutuhkannya untuk penemuan terbarunya."

    show player 1
    show june 4
    june "Hah. Hal gila apa yang dia lakukan kali ini?"

    show player 2
    show june 2
    player_name "Kedengarannya cukup rapi sebenarnya, itu a-"

    show player 1
    show june 3
    june "Tidak, jangan beritahu aku! Aku yakin aku tidak ingin tahu."

    show player 11
    show june 2
    player_name "..."
    show player 10
    player_name "Bisakah Anda membantu saya atau tidak?"

    show player 11
    show june 4
    june "Saya meragukannya. Apakah itu harus asli?"

    show player 10
    show june 2
    player_name "Eh, menurutku begitu."

    show player 11
    show june 4
    june "Yah, itu akan sulit didapat."

    show player 10
    show june 2
    player_name "Apa itu {b}mesin faptic{/b}?"

    show player 11
    show june 3
    june "Oh, kamu tidak tahu?"

    june "Ini adalah mesin kecil yang memberikan sensasi sentuhan. Mereka baru saja mulai menempatkannya di smartphone terbaik."

    show player 10
    show june 2
    player_name "Sensasi sentuhan?"

    show player 11
    show june 4
    june "Sensasi yang Anda rasakan dengan kulit Anda. Dalam hal ini, getaran."

    show player 2
    show june 2
    player_name "Oh, aku mengerti sekarang."

    player_name "Lalu mengapa sangat sulit mendapatkannya?"

    show player 1
    show june 3
    june "Yah, kesampingkan fakta bahwa ponsel itu sangat mahal..."

    show player 11
    show june 4
    june "Saat ini sudah terjual habis, seperti di tempat lain!"

    show player 10
    show june 2
    player_name "Seberapa mahal yang kita bicarakan?"

    show player 11
    show june 4
    june "Sekitar dua ribu dolar."

    show player 23
    show june 2
    player_name "!!!" with hpunch
    show player 10
    player_name "Apa?! Untuk telepon?!"

    show player 11
    show june 4
    june "Sudah kubilang mereka adalah yang terbaik."

    show june 3
    june "Tapi itu tidak masalah, apa kau tidak mendengarku? Semuanya sudah terjual habis."

    show player 10
    show june 2
    player_name "Ayo tembak! Apa yang harus kukatakan {b}Nona Okita{/b}?"

    show player 11
    show june 3
    june "Sayang sekali dia menginginkan yang asli. Ada beberapa versi tiruan dengan kualitas cukup bagus yang mungkin bisa Anda dapatkan."

    show player 10
    show june 2
    player_name "Hmm, apakah akan berfungsi sebaik yang asli?"

    show player 11
    show june 4
    june "Ya, tidak, tapi cukup dekat. Itu tergantung pada tujuan Anda menggunakannya."

    show june 3
    june "Dalam kebanyakan kasus, menurut saya tiruannya akan berhasil."

    show june 2
    player_name "..."
    show player 10
    player_name "Baiklah, di mana saya bisa mendapatkan versi tiruannya?"

    show player 11
    show june 3
    june "Ya, mereka memasukkannya ke dalam pengontrol {b}Master Blaster{/b} beberapa tahun yang lalu."

    show player 10
    show june 2
    player_name "{b}Master Blaster{/b}? Suka video gamenya?"

    show player 11
    show june 3b
    june "Ya! Saya selalu menginginkannya tetapi orang tua saya tidak mampu membelinya."

    show player 2
    show june 2
    player_name "Anda tahu apa? Teman saya {b}Erik{/b} dulu punya salah satunya!"

    show player 1
    show june 6
    june "Apakah dia masih memilikinya?"

    show player 2
    show june 5
    player_name "Tidak tahu."

    show player 1
    show june 6
    june "Nah, jika Anda berhasil mendapatkannya, saya dapat mengeluarkan {b}mesin faptic{/b} untuk Anda."

    show player 2
    show june 2
    player_name "Besar! Saya akan berbicara dengan {b}Erik{/b} dan melihat apakah dia masih memilikinya."

    player_name "Terima kasih atas infonya, {b}Juni{/b}."

    show player 1
    show june 3
    june "Semoga beruntung!"

    return

label june_dialogue_okita_get_controller_info:
    scene location_school_computer_day_blur
    show player 2 at left
    show june 2 at right
    with dissolve
    player_name "Apa nama pengontrol itu lagi?"

    show player 1
    show june 4
    june "{b}Master Blaster{/b}."

    show june 3
    june "Bukankah kamu bilang temanmu {b}Erik{/b} punya satu?"

    show player 2
    show june 2
    player_name "Ya, dia dulu..."

    player_name "Aku akan bertanya padanya tentang hal itu."

    player_name "Terima kasih, {b}Juni{/b}."

    show player 1
    show june 3
    june "Semoga beruntung!"

    return

label june_dialogue_okita_has_controller:
    scene location_school_computer_day_blur
    show player 502 at left
    show june 2 at right
    with dissolve
    player_name "Apakah ini hal yang kamu bicarakan?"


    show player 1
    show june 11
    with dissolve
    june "Hei, kamu benar-benar mendapatkannya. Luar biasa!"

    show player 2
    show june 12
    player_name "Jadi, Anda dapat menghilangkan {b}mesin faptic{/b} dari sini?"

    show player 1
    show june 11
    june "Sangat."

    june "Beri saya waktu beberapa menit untuk membongkarnya."

    show player 2
    show june 12
    player_name "Baiklah."

    show player 1
    show june 11

    june "Ini sangat keren!"


    pause
    scene location_school_computer_day_blur
    show player 1 at left
    show june 13 at right
    with dissolve
    june "Ini dia, satu {b}mesin faptic{/b} tiruan."

    show player 2
    show june 14
    player_name "Itu saja? Ini sangat kecil..."

    show player 505
    show june 18
    with dissolve
    june "Yup, hal kecil tapi berdampak besar."

    show player 506
    show june 17
    player_name "Baiklah, sebaiknya saya antarkan ini ke {b}Nona Okita{/b}."

    show player 505
    show june 19
    june "Katakan, {b}[firstname]{/b}?"

    june "Apakah Anda keberatan jika saya menyimpan pengontrolnya?"

    show player 2 with dissolve
    show june 17
    player_name "Tidak, tidak sama sekali. Hancurkan dirimu!"

    show player 1
    show june 18
    june "Manis! Terima kasih, {b}[firstname]{/b}!"

    return

label june_intro:
    if player.location.is_here(M_erik):
        show old_erik 1b at Position (xpos=700)
    show june 1 at right
    show player 14 at left
    with dissolve
    player_name "Hai!"

    show june 3
    show player 1
    june "Oh, eh, hai?"

    june "Ada apa?"

    show june 2
    return

label june_intro_intimate:
    show player 14 at left
    show june 5 at right
    with dissolve
    player_name "Hai, {b}Juni{/b}!"

    show player 1
    show june 6
    june "Hai, {b}[firstname]{/b}!"

    june "Ada apa?"

    show june 5
    return

label june_dialogue_okita_get_bifocal_lenses:
    show player 2
    player_name "Hei, jadi uhh..."

    player_name "Saya sedang membantu {b}Nona Okita{/b} dengan sebuah proyek."

    show player 1
    show june 4
    june "{b}Nona Okita{/b} meminta bantuan Anda dengan desainnya?"

    show player 10
    show june 2
    player_name "Ya."

    player_name "... Dan kita memerlukan beberapa {b}lensa{/b}, misalnya dari kacamata?"

    show player 11
    show june 4
    june "Kamu mau kacamataku?"

    show player 10
    show june 2
    player_name "Baiklah, saya berharap Anda memiliki satu set cadangan?"

    show player 11
    show june 4
    june "Tidak, hanya satu saja."

    show player 10
    show june 2
    player_name "Mungkin aku bisa meyakinkanmu untuk memberiku sepasang itu?"

    show player 11
    show june 4
    june "Saya meragukannya."

    show player 10
    show june 2
    player_name "Hmm, kamu rabun jauh atau rabun jauh?"

    show player 11
    show june 3
    june "Rabun jauh."

    show player 29 with dissolve
    show june 2
    player_name "Oh, sudahlah kalau begitu."

    player_name "Saya membutuhkan sepasang dari seseorang yang keduanya."

    show player 3
    show june 4
    june "Saya tidak percaya {b}Nona Okita{/b} meminta ANDA untuk membantu proyeknya..."

    show player 29
    show june 2
    player_name "Yah, dia agaknya, memaksaku..."

    show player 3
    show june 6
    june "Ya, itu terdengar lebih mirip dengannya."

    show june 3
    june "Semoga beruntung."

    show player 2 with dissolve
    show june 2
    player_name "Ya terima kasih."

    return

label june_dialogue_ross_ask_model:
    show player 2
    player_name "Saya sedang mengerjakan proyek untuk {b}Miss Ross{/b} dan itu memerlukan model langsung."

    player_name "Apakah Anda tertarik?"

    show player 1
    show june 3
    june "Pemodelan?"

    show june 3b
    june "Apakah aku terlihat seperti model bagimu?"

    show player 10
    show june 5
    player_name "Tentu, kenapa tidak?"

    show player 11
    show june 3b
    june "Pfft, usaha yang bagus."

    show june 3
    june "Lagipula aku punya rencana lain..."

    show player 10
    show june 5
    player_name "Anda melakukannya?"

    show june 3
    show player 11
    june "Ya, paket ekspansi untuk {i}Orcette's Dungeon{/i} diluncurkan hari ini."

    june "Anda sebaiknya percaya saya mendapatkan salinannya!"

    show player 10
    show june 5
    player_name "Baiklah, bersenang-senanglah menurutku."

    show player 11
    show june 3b
    june "Oh, aku akan melakukannya!"

    return

label june_date_hang:
    show player 14
    player_name "Saya ingin tahu apakah Anda ingin nongkrong di tempat saya?"

    label june_date_hang_confirm:
    show player 1
    show june 6
    june "Tentu!"

    june "Sepulang sekolah?"

    show player 14
    show june 5
    player_name "Ya."

    label june_date_hang_details:
    show player 1
    show june 6
    june "Jadi, ini kamarmu?"

    show player 10
    show june 5
    player_name "Kamarku?"

    show player 11
    show june 6
    june "Ya! Kami membutuhkan tempat yang tenang dan menyenangkan untuk bersantai dan bermain game."

    show player 14
    show june 5
    player_name "Hehe, oke!"

    show player 1
    show june 6
    june "Luar biasa!"

    june "Aku ada kelas sebentar lagi, aku harus berangkat."

    june "Sampai jumpa sepulang sekolah, {b}[firstname]{/b}!"

    return

label june_date_later:
    show player 14
    player_name "Masih aktif sepulang sekolah?"

    show player 1
    show june 6
    june "Ya! Aku akan menemuimu di tempatmu."

    show june 5
    show player 14
    player_name "Besar! Sampai jumpa lagi, {b}Juni{/b}!"

    return

label june_date_tired:
    show june 1
    show player 10
    player_name "Aku benar-benar minta maaf karena aku sangat lelah terakhir kali, dan akhirnya kita tidak bisa bermain bersama!"

    show player 11
    june "Hmm..."

    show june 4
    june "Apa?"

    show june 6
    june "Maaf, saya agak asyik, apa yang kamu katakan?"

    show june 5
    june "( ... {i}bermain bersama{/i}... )"

    show june 6
    june "Oh, benar, bermain bersama! Tentu, bagaimana kalau sepulang sekolah?"

    show june 5
    show player 29
    with dissolve
    player_name "Errr... Ya, tentu! Kedengarannya bagus."

    show player 1 with dissolve
    jump june_date_hang_details

label june_date_retry:
    show player 14
    player_name "Ingin mencoba mengalahkan bos terakhir itu lagi?"

    jump june_date_hang_confirm

label june_date_sorry:
    show player 10
    player_name "Maaf saya menyebut permainan Anda kotor."

    show player 11
    show june 3b
    june "Itu juga merupakan kejutan bagi saya!"

    show june 4
    june "Tapi menurutku itu tidak menjijikkan..."

    show june 2
    show player 10
    player_name "Mungkin kita bisa memainkannya lagi? Jika Anda mau?"

    show player 11
    show june 3
    june "Benar-benar?"

    show june 4
    june "Sepertinya itu bukan kesukaanmu..."

    show june 1
    show player 10
    player_name "Tapi aku suka bermain denganmu."

    player_name "Dan mungkin ini tidak akan terlalu mengejutkan untuk kedua kalinya."

    show player 40 with dissolve
    player_name "Silakan?"

    show june 3b
    june "Oke! Oke! Hentikan itu! Kita bisa bermain!"

    show june 3
    show player 11
    with dissolve
    june "Aku akan menemuimu di rumahmu sepulang sekolah."

    show june 2
    show player 21
    player_name "Besar! Sampai jumpa lagi!"

    return

label june_dialogue_cosplay_no_costume:
    show player 14
    player_name "Cosplay apa yang ingin kamu buat lagi?"

    show player 1
    show june 3
    june "Oh, itu kostum orcette."

    june "Seharusnya ada gigi, kalung, dan ikat pinggang!"

    show player 14
    show june 2
    player_name "Ah benar!"

    player_name "Kayaknya aku tahu {b}tempat di mall yang punya kostum{/b}..."

    show player 1
    show june 6
    june "Oh ya?"

    show player 14
    show june 5
    player_name "Saya mungkin akan pergi ke sana dan memeriksanya!"

    show player 1
    show june 6
    june "Dingin! Sampai jumpa."

    return

label june_dialogue_cosplay_has_costume:
    show player 17
    player_name "Saya rasa saya menemukan sesuatu yang mungkin Anda sukai!"

    show player 1
    show june 3
    june "Hah?"

    show june 6
    june "Apa itu?"

    show june 5
    show player 423 with fastdissolve
    player_name "Itu kostum orcette!!"

    show player 422
    show june 6
    june "Untuk cosplayku?!"

    show player 1
    show june 7
    with dissolve
    pause
    show player 13
    show june 8
    june "Ya ampun!!"

    june "Ia memiliki semua bagian hilang yang saya butuhkan!"

    june "Itu bahkan terlihat seperti gigi asli!"

    show player 17
    show june 5
    with dissolve
    player_name "Saya senang Anda menyukainya."

    show player 14
    player_name "Ini akan terlihat bagus untukmu!"

    show player 1
    show june 6
    june "Terima kasih banyak, {b}[firstname]{/b}."

    show player 14
    show june 5
    player_name "Saya senang Anda bisa melakukan cosplay keren di comic con."

    show player 11
    show june 6
    june "Saya mungkin akan mendapat banyak perhatian dari orang banyak, saya yakin!"

    show player 10
    show june 5
    player_name "Maksudmu seperti itu, teman-teman?"

    show player 11
    show june 6
    june "Yah, menurutku, ya..."

    show june 5
    player_name "..."
    show june 6
    june "Tapi tahukah Anda?"

    june "Saya pikir saya harus mencoba cosplaynya sebelum saya pergi!"

    june "Mungkin memakainya... Di depan teman?"

    show june 5
    show player 10
    player_name "Seperti siapa?"

    show player 11
    show june 6
    june "Anda!! Konyol..."

    show player 17
    show june 5
    player_name "Oh, haha!"

    show player 14
    player_name "Tentu, saya bisa emm... Memberi Anda masukan!"

    show player 1
    show june 6
    june "Besar! Bagaimana kalau kita bertemu di rumahmu... Seperti terakhir kali?"

    show player 14
    show june 5
    player_name "Baiklah, sampai jumpa sepulang sekolah nanti!"

    show player 1
    show june 6
    june "Sampai jumpa lagi!"

    return

label june_dialogue_ask_about_class:
    show player 14
    player_name "Hei, kamu di kelas apa?"

    player_name "Aku jarang melihatmu di sekolah."

    show player 1
    show june 3
    june "Oh, aku tidak berolahraga."

    june "aku lebih suka berlama-lama di sini..."

    show player 14
    show june 2
    player_name "Apa yang kamu lakukan di lab komputer?"

    show player 1
    show june 3
    june "Anda tahu, hanya sekedar... Seperti browsing internet..."

    june "... Membuka papan pesan, menonton streaming, dan bermain game."

    show june 2
    show player 14
    player_name "Game, ya?"

    show player 1
    show june 3
    june "Ya."

    show june 1
    show player 14
    player_name "Seperti yang kamu pegang?"

    show player 1
    show june 3
    june "Oh, benda ini? Itu hanya permainan konyol..."

    show player 14
    show june 2
    player_name "Apa namanya?"

    show player 1
    show june 3
    june "Namanya {i}Orc Bork{/i}."

    show player 14
    show june 2
    player_name "Sebuah permainan tentang orc?"

    show player 1
    show june 3
    june "Ya."

    show june 4
    june "Ini cukup sulit."

    show player 11
    june "Saya sudah mencoba mengalahkannya selama berbulan-bulan..."

    show player 14
    show june 2
    player_name "Apakah sesulit itu?"

    show player 1
    show june 3
    june "Nah, akan lebih mudah jika Anda bermain dengan dua pemain."

    show june 4
    june "Aku hanya belum menemukan orang yang memainkan permainan semacam ini di sekolah..."

    show june 3
    june "Kecuali, mungkin Anda kenal seseorang?"

    show june 1
    return

label june_dialogue_erik_help:
    show player 14
    player_name "Sebenarnya, aku tahu!"

    player_name "Teman baikku {b}Erik{/b} MENCINTAI game yang mengandung Orc!"

    player_name "Terutama... Orcette."

    player_name "Menurutku kalian berdua harus bermain bersama!"

    show player 1
    show june 3
    june "{b}Erik{/b}?"

    show player 11
    june "sepertinya aku tidak mengenalnya..."

    show player 10
    show june 1
    player_name "Dia bilang kamu pernah meminjam salah satu pensilnya."

    show player 1
    show june 4
    june "Hah..."

    show player 14
    show june 5
    player_name "Yah, dia menghabiskan banyak waktu di kamarnya... Bermain game..."

    show player 1
    show june 6
    june "Dengan serius?"

    show player 14
    show june 5
    player_name "Saya pikir dia bisa membantu Anda mengalahkan permainan itu."

    show player 1
    show june 6
    june "Itu akan luar biasa."

    june "Beri tahu saya jika dia bersedia melakukannya!"

    show player 17
    show june 5
    player_name "Manis!!"

    show player 14
    player_name "Saya pasti akan memberi tahu dia."

    return

label june_dialogue_mc_help:
    show player 14
    player_name "Aku tidak begitu pandai dalam permainan itu... Tapi aku akan mencobanya!"

    show player 1
    show june 4
    june "Kamu... Ingin bermain denganku?"

    june "Apakah Anda yakin akan menyukainya?"

    show player 14
    show june 2
    player_name "Tentu, kenapa tidak?"

    show player 11
    show june 3
    june "Yah, hanya saja belum pernah ada yang bertanya sebelumnya..."

    show player 17
    show june 2
    player_name "Saya dengan senang hati akan menjadi yang pertama bagi Anda!"

    show player 21
    show june 5
    player_name "Err... maksudku... Tidak seperti-"

    show player 11
    show june 6
    june "Haha, kamu lucu."

    show june 5
    player_name "..."
    show player 14
    player_name "Jadi... Kamu ingin bermain sekarang?"

    show player 11
    show june 6
    june "Umm... Bagaimana kalau kita bermain di tempat lain?"

    june "Aku sedikit lelah menghabiskan seluruh waktuku di lab komputer ini..."

    show player 14
    show june 5
    player_name "Oke, lalu di mana?"

    show player 10
    player_name "Jika kita bermain di lorong, {b}Annie{/b} akan memberi kita detensi..."

    show player 11
    show june 6
    june "Hmm... Bagaimana kalau kita bermain di rumahmu?"

    show player 12
    show june 5
    player_name "Saya... Rumah saya?!"

    show player 11
    show june 6
    june "Ya!"

    june "Sepulang sekolah?"

    show player 10
    show june 5
    player_name "Uhh... kurasa kita bisa?"

    show player 11
    show june 6
    june "Luar biasa!"

    june "Terima kasih sudah mau bermain denganku..."

    show player 13
    june "Itu... Kamu baik sekali!"

    show player 14
    show june 5
    player_name "Oh, haha. Bukan apa-apa..."

    show player 1
    show june 6
    june "Sampai jumpa malam ini!"

    june "Aku akan menunggumu di dalam."

    show player 17
    show june 5
    player_name "Tentu!"

    return

label june_dialogue_leave:
    show june 2 at right
    show player 14
    player_name "Oh, tidak ada apa-apa!"

    player_name "Hanya menyapa."

    show player 1
    show june 4
    june "Oh, baiklah kalau begitu..."

    show june 1
    show player 29
    with dissolve
    player_name "Err... Sampai jumpa lagi!"

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
