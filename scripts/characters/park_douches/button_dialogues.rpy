label park_dewitt_douches_meet_up:
    scene expression player.location.background_closeup
    show eve f_happy zorder 1:
        xoffset -400
    show player 12 at left
    with dissolve
    player_name "Baiklah, aku di sini. Apa ide yang kamu punya?"

    show player 5
    eve "Ya, kita butuh bantuan untuk membersihkan auditorium pertunjukan bakat, bukan?"

    show player 10
    player_name "Ya."

    show player 5
    eve "Ucapkan salam pada bantuannya."

    show tyrone:
        xoffset -50
    show chad:
        xoffset 100
    with dissolve
    tyrone "Ada apa, crackajack?"

    show player 12
    player_name "Wah. Maksudmu orang-orang ini akan membantu kita bersih-bersih?"

    show player 5
    chad @ a_open "Itu benar! Apa, menurutmu hanya karena kita gangster, kita tidak bisa melakukan sedikit kegiatan amal dari waktu ke waktu?"

    show player 10
    player_name "Yah tidak, aku tidak bermaksud-"

    show player 11
    tyrone "Bagus, karena kamu benar! Ha ha ha!"

    show player 12
    player_name "Oke, saya secara resmi bingung."

    show player 5
    eve "Heh, mereka akan membantu kita."

    eve "... Tapi kita juga harus melakukan sesuatu untuk mereka."

    show player 14
    player_name "Oh, begitu."

    show player 12
    player_name "Apa yang mereka inginkan?"

    show player 5
    chad "Kamu harus {b}memberi kami uang empat puluhan{/b}, yo!"

    show player 10
    player_name "Eh, empat puluhan?"

    show player 5 with None
    show eve f_angry:
        flip
        xoffset 250
    with dissolve
    eve "Tidak ada empat puluhan! Sudah kubilang, kaleng!"

    chad "Ssst, baiklah! Apa pun."

    show eve f_happy:
        unflip
        xoffset -400
    with dissolve
    eve "Mereka hanya ingin kita {b}membuat mereka bir{/b}."

    show player 10
    player_name "Apa?! Saya belum cukup umur untuk membeli bir!"

    show player 5
    eve @ f_eyeroll "Ya, ya. Saya tahu itu!"

    eve "Apakah temanmu tidak punya?"

    show player 12
    player_name "Hah?"

    show player 5
    eve f_confused "Pria dengan mesin karaoke itu! {b}Evan{/b}?"

    show player 12
    player_name "Maksudmu {b}Erik{/b}?"

    show player 5
    eve f_happy @ f_laugh "Ya, pria itu!"

    eve "{b}Dia minum banyak bir di tempatnya{/b}!"

    show player 37 with dissolve
    player_name "Ah, kawan."

    show player 38 with dissolve
    player_name "... Mereka akan membantu kita membersihkan semuanya, kan?"

    show player 5 with dissolve
    tyrone "Itu idenya, bodoh."

    show player 4 with dissolve
    player_name "..."
    show player 12 with dissolve
    player_name "Baiklah, saya akan lihat apa yang bisa saya lakukan."

    player_name "Saya akan {b}menemui kalian di auditorium besok{/b} untuk pembersihan!"

    show player 5
    eve "Aku akan memastikan mereka mempertahankan tujuan mereka."

    hide eve
    hide chad
    hide tyrone
    with dissolve
    show player 10
    player_name "Saya harus berbicara dengan {b}Erik{/b} tentang {b}minum bir Tuan Johnson{/b}."

    return

label park_douches_intro:
    scene expression player.location.background_blur with None
    show anon f_worried at anon_versus
    show chad f_happy
    show chico f_cocky:
        chico_back
    show tyrone f_smirk:
        flip
        xoffset 200
    with dissolve
    tyrone "Sobat, kamu hanya memikirkan mereka yang bodoh, bukan?"

    chico "Apa yang bisa saya katakan, saya orang yang sederhana."

    tyrone "Seorang pria sederhana yang akan mendapat tepuk tangan..."

    show chico f_normal
    chad @ f_laugh "Haha!!"

    chico "Tidak, kawan. Dia bersih."

    tyrone "Silakan."

    tyrone "Aku kenal perempuan jalang itu dan dia sama sekali tidak bersih!"

    chico @ -m_talk "..."
    tyrone "Aku tidak akan menidurinya dengan penis {b}Chad{/b}..."

    chad @ f_laugh "Haha, ya!"

    chad "Dia bahkan tidak mau menidurinya dengan penisku!"

    tyrone @ f_angry "Diam, {b}Chad{/b}!"

    chad f_normal_down @ -m_talk "..."
    chico f_cocky "Maksudku, gadis itu berbakat."

    chico @ f_laugh "Dia membuatku keluar dalam waktu tiga puluh detik!"

    show chad f_happy
    tyrone "Heh, itu tidak ada hubungannya dengan bakat... Itulah pengalaman, itulah apa adanya!"

    tyrone "Dia tidak mengisap setengah penisnya di kota, kawan!"

    chico "Ck, terserah..."

    pause
    anon @ a_wave "{i}*Ehem*{/i}"

    show tyrone f_angry with dissolve:
        unflip
        tyrone_front
    chico f_angry "Cih, kamu mau apa, brengsek?"

    chad f_normal "Ya, apa yang kamu inginkan?!"

    tyrone "Anda datang untuk bergaul dengan anak-anak keren?"

    show tyrone f_smirk
    anon "Tidak."

    anon "Aku ingin kalian berhenti menyusahkan {b}Eve{/b}."

    tyrone "Ah, benarkah?"

    chico f_cocky "Hah, lihat dia berusaha sekuat tenaga."

    chad f_happy @ f_laugh "Haha!"

    anon f_tired "{i}*Sigh*{/i} Serius, apa yang perlu dilakukan agar kalian mundur?"

    tyrone @ f_normal "Kamu ingin kami meninggalkan pacar kecilmu sendirian?"

    tyrone @ a_point "Anda harus mengalahkan kami dalam pertempuran."

    anon f_worried a_up "Sobat, aku tidak mencoba untuk melawan kalian..."

    tyrone "Saya tidak berbicara tentang tidak adanya pertarungan!"

    tyrone @ f_laugh "Pertarungan rap, astaga!"

    anon a_idle f_surprised @ a_behind_head "Pertarungan rap?!"

    tyrone "Ya itu benar!"

    show tyrone a_mic_throw
    show anon b_dressed_blocking
    with dissolve
    pause
    show tyrone a_idle
    show anon b_dressed f_sad_down
    with dissolve
    anon "!!!"
    show anon f_worried
    anon "Uhh, entahlah..."

    chico f_normal "Yo, ayolah kawan, orang bodoh ini tidak tahu apa-apa tentang sajak!"

    chad "Beneran dawg, scrub ini gak bisa rap."

    tyrone "Tunggu sebentar, dia tidak mau masuk ke sini seperti dia punya bola kuningan besar... Aku ingin melihatnya mendukungnya!"

    anon @ -m_talk "..."
    tyrone @ a_point "Kamu tidak akan marah sekarang, kan?"

    anon f_skeptical "Baiklah, aku akan bertarung denganmu."

    show anon b_dressed_pickup with dissolve
    show chad f_happy
    chico @ f_eyeroll -m_talk "Cih."

    show anon f_worried b_dressed a_mic with dissolve
    tyrone "Heh, nah kawan... Kamu tidak berhak melawanku!"

    tyrone "Kamu harus melewati anak-anakku dulu."

    tyrone a_hands_rub @ a_point "Aku adalah King Kong di jalang ini!"

    chad "Hah ya, Raja Kong sialan!"

    tyrone a_idle f_angry "Bung, tutup mulutmu, {b}Chad{/b}."

    show chad f_normal_down
    tyrone "Sial."

    chad "Ya ampun, sial."

    anon @ f_skeptical "Baiklah, siapa yang pertama?"

    show chad f_happy
    show chico:
        chico_front
    show tyrone f_smirk behind chico:
        tyrone_back
    with dissolve
    chico f_angry @ a_signs "Yo, aku akan mengurus bajingan maaf ini."

    tyrone "Haaaah, sekarang itu yang aku bicarakan!"

    chico a_mic "Perhatikan, jalang!"

    return

label park_douches_greet:
    scene expression player.location.background_blur with None
    show anon f_worried at anon_versus
    show chad
    show chico:
        chico_back
    show tyrone:
        tyrone_front
    with dissolve
    tyrone "Hei, lihat siapa yang kembali."

    if player.stats.chr() > 6:
        tyrone "Anda siap menghadapi tantangan besar?"

        chad "Kau akan terpanggang, kawan."

        anon "saya siap."

    elif player.stats.chr() > 3:
        chad "Sup, sial?"

        chad f_happy "Anda siap bertempur?"

    else:
        chico "Astaga, jangan sebodoh ini lagi..."

        chad "Kamu membuang-buang waktumu, sial!"

    return

label park_douches_rematch_1:
    anon f_normal "Saya memilih untuk Rap Battle!"

    tyrone f_smirk "Itu yang aku bicarakan!"

    tyrone "Anda siap untuk pertandingan ulang, {b}Chico{/b}?"

    show chico f_cocky:
        chico_front
    show tyrone behind chico:
        tyrone_back
    with dissolve
    chico a_mic "Sepotong kue, kawan."

    chico @ a_signs "Cracker ini tidak akan bisa melewatiku!"

    tyrone "Putar itu!"

    return

label park_douches_rematch_2:
    anon "Saya memilih untuk melakukan pertarungan rap!"

    tyrone f_smirk "Anda akan melawan {b}Chad{/b} sekarang."

    show chad:
        chad_front
    show tyrone behind chad:
        tyrone_middle
    show chico behind chad
    with dissolve
    chad @ a_open "Benar sekali, sial!"

    chad "Bersiaplah untuk merasakan kemarahan {b}Chad{/b}!"

    chico @ f_eyeroll "Eugh, anak laki-laki kulit putih sialan..."

    tyrone @ f_laugh "Ha ha ha!"

    chad f_angry a_mic "Pukul itu!"

    return

label park_douches_rematch_3:
    anon "Saya memilih untuk melakukan pertarungan rap!"

    tyrone f_smirk "Mari kita mulai omong kosong ini!"

    tyrone "Anda mungkin ingin membuat catatan..."

    chad "Tangkap dia, {b}Tyrone{/b}!"

    tyrone a_mic "Putar itu!"

    return

label park_douches_rematch_4:
    anon "Saya memilih untuk melakukan pertarungan rap!"

    tyrone f_smirk "Mari kita mulai omong kosong ini!"

    tyrone "Anda mungkin ingin-"

    show tyrone f_surprised
    anon "Aku pergi duluan kali ini."

    show tyrone f_smirk
    chad f_happy @ f_laugh a_open "Oh sial!"

    tyrone "Baiklah, jika itu yang kamu inginkan."

    tyrone "Mari kita dengar apa yang Anda punya."

    return

label park_douches_respect:
    scene expression player.location.background_blur with None
    show anon at anon_versus
    show chad f_happy
    show chico f_cocky:
        chico_back
    show tyrone:
        tyrone_front
    with dissolve
    tyrone "Yo, ada apa?"

    chico "Sup, kawan?"

    tyrone f_smirk @ a_point "Anda di sini untuk berperang?"

    anon @ f_laugh "Hehe, tidak."

    chad "Aww, ayolah... Kamu harus mempertahankan gelar itu!"

    anon "Mungkin lain kali."

    tyrone "Sesuaikan dirimu."

    return

label park_douches_dismiss:
    if player.stats.chr() < 10:
        anon "Sudahlah."

        show tyrone f_normal
        chico f_angry "Itulah yang saya pikirkan!"

        chico @ a_signs "Tersesat, puta!"

        chad f_angry "Ya, tersesat!"

        hide anon with dissolve
    else:
        anon @ a_wave "Aku akan menangkap kalian nanti."

        tyrone "Baiklah, sial."

        tyrone "Perdamaian."

    return

label park_douches_battle_1:
    chico f_angry a_mic_speak "{i}Kamu pikir kamu bisa melawanku dengan roti putih?{/i}"

    chico "{i}Kami bahkan belum memulai dan kamu sudah mati!{/i}"

    chico "{i}Kamu datang ke sini, mengira kamu tangguh;{/i}"

    chico "{i}Mari kita dengarkan, jalang, aku hanya menggertakmu!{/i}"

    chico f_cocky "{i}Kamu tidak punya sajak dan sekarang pantatmu tergoreng;{/i}"

    chico "{i}Aku akan mengirimmu pulang ke mamamu sambil menangis!{/i}"

    show anon f_worried
    show tyrone f_smirk
    show chad f_happy
    show chico a_mic
    with dissolve
    chad "Oooh, harium!"

    tyrone "Baiklah, baiklah... Cukup bagus, sebagai permulaan."

    tyrone "Anda harus mengatasinya sekarang, Anda siap?"

    anon "Y-ya, oke."

    tyrone "Putar omong kosong itu!"

    return

label park_douches_battle_1_pass:
    show anon f_snarky a_mic_speak
    show chad f_normal
    show chico f_cocky
    show tyrone f_normal
    with fade
    anon "{i}Hanya itu yang kamu punya {b}Chico{/b}, mengolok-olok balapanku?{/i}"

    anon "{i}Ini bukan pertarungan bagiku, kamu bahkan tidak bisa mengimbanginya!{/i}"

    anon "{i}Sulit mendengarkan kata-katamu, ketika kamu berpakaian seperti badut...{/i}"

    anon "{i}... Dan roti putih ini akan membakar pantatmu.{/i}"

    anon "{i}Jadi berlarilah pulang sekarang, dasar skater brengsek...{/i}"

    anon "{i}... Dan beritahu ibumu untuk tidak khawatir, aku akan datang nanti.{/i}"

    show chad f_happy
    show chico f_angry
    show tyrone f_smirk
    show anon f_normal a_mic with dissolve
    chad @ f_laugh "HAHAHAH!"

    tyrone "Lumayan, boi putih."

    chad "Dia benar-benar menangkapmu, dawg!"

    chico "Astaga, diamlah, {b}Chad{/b}!"

    chico "Dia hanya beruntung, itu saja..."

    tyrone "Nah, itu sah!"

    anon "Terima kasih kawan."

    tyrone "Jalanmu masih panjang jika ingin menantangku, tetapi ini adalah permulaan."

    tyrone "{b}Mampirlah satu malam lagi dan kita akan pergi lagi{/b}."

    anon "Baiklah."

    hide anon with dissolve
    return

label park_douches_battle_2:
    chico f_angry a_mic_speak "{i}Apa yang kamu lakukan di sini, jalang? Bukankah pantatmu sudah cukup?{/i}"

    chico "{i}Lebih baik berpegang pada sesuatu, ini akan menjadi sulit.{/i}"

    chico "{i}Ini wilayah kami, bodoh dan Anda tidak bisa bergaul dengan merek kami.{/i}"

    chico "{i}Sajakku mengiris begitu dalam, hingga kau tak sanggup berdiri.{/i}"

    chico "{i}Entah apa yang ada di pikiranmu, jauh di luar jangkauan pikiranmu.{/i}"

    chico f_cocky "{i}Celanamu penuh dengan kotoran, kawan, menurutku sudah waktunya kamu melarikan diri.{/i}"

    show anon f_worried
    show tyrone f_smirk
    show chad f_happy
    show chico a_mic with dissolve
    chad "Oooh, harium!"

    tyrone "Baiklah, baiklah... Cukup bagus, sebagai permulaan."

    tyrone "Anda harus mengatasinya sekarang, Anda siap?"

    anon "Y-ya, oke."

    tyrone "Putar omong kosong itu!"

    return

label park_douches_battle_2_pass:
    show anon f_snarky a_mic_speak
    show chad f_normal
    show chico f_cocky
    show tyrone f_normal
    with fade
    anon "{i}Aku benci membocorkannya padamu, sial, tapi aku akan tetap di sini.{/i}"

    anon "{i}Jadi belajarlah menerimanya atau menyingkirlah!{/i}"

    anon "{i}Kamu terus mencoba melontarkan sajak-sajak yang sangat menusuk ini...{/i}"

    anon "{i}... Tapi semua kata-katamu keluar dengan sederhana dan murahan.{/i}"

    anon "{i}Pelajari tempatmu, {b}Chico{/b} cepat dan ingatlah untuk membungkuk.{/i}"

    show chad f_happy
    anon "{i}Kenali keahlian saya, inilah taman saya sekarang.{/i}"

    show tyrone f_smirk
    show chico f_angry
    show anon f_normal a_mic with dissolve
    chad "Yo, itu menyala!"

    tyrone "Lumayan, boi putih."

    chico "Tidak apa-apa."

    tyrone "Nah, itu sah!"

    anon "Terima kasih kawan."

    tyrone "Jalanmu masih panjang jika ingin menantangku, tapi kamu semakin dekat."

    tyrone "{b}Mampirlah satu malam lagi dan kita akan pergi lagi{/b}."

    anon "Baiklah."

    hide anon with dissolve
    return

label park_douches_battle_3:
    chico f_angry a_mic_speak "{i}Oh, kamu pikir kamu keren, karena kamu mengalahkanku dua kali?{/i}"

    chico "{i}Apa yang tidak kamu sadari adalah, aku hanya bersikap baik.{/i}"

    chico "{i}Tapi sarung tangannya sudah dilepas sekarang dan saya siap bergemuruh.{/i}"

    chico "{i}Saat aku memberi tekanan, kamu hanya akan hancur.{/i}"

    chico "{i}Jadi, angkat adipatimu, jalang, dan cobalah untuk tidak menolak keras.{/i}"

    chico f_cocky "{i}Saat aku selesai, gadismu akan menghisap penisku.{/i}"

    show anon f_worried
    show tyrone f_smirk
    show chico a_mic with dissolve
    chad f_happy @ f_laugh "Oooh, harium!"

    tyrone "Baiklah, baiklah... Cukup bagus, sebagai permulaan."

    tyrone "Anda harus mengatasinya sekarang, Anda siap?"

    anon "Y-ya, oke."

    tyrone "Putar omong kosong itu!"

    return

label park_douches_battle_3_pass:
    show anon f_snarky a_mic_speak
    show chad f_normal
    show chico f_cocky
    show tyrone f_normal
    with fade
    anon "{i}Aku tidak hanya mengalahkanmu, aku membuatmu berantakan.{/i}"

    anon "{i}Meludah sajak yang tidak bisa Anda tangani.{/i}"

    anon "{i}Kamu pikir kamu bisa membuatku takut, jalang? Cobalah.{/i}"

    anon "{i}Teruslah mencoba melawanku, tapi maaf, aku tidak memukul perempuan.{/i}"

    anon "{i}Sekarang lihat dirimu meringkuk, terlepas dari jahitannya...{/i}"

    anon "{i}Kamu tidak bisa bersama gadisku, bahkan dalam mimpi basahmu!{/i}"

    show chad f_happy
    show chico f_angry
    show tyrone f_smirk
    show anon f_normal a_mic with dissolve
    chad @ f_laugh "HAHAHAH!"

    chico "sial..."

    tyrone "Heh, sepertinya dia punya nomor teleponmu {b}Chico{/b}."

    chico "Tidak, sial,..."

    chico "Aku akan mendapatkan pengecut ini lain kali!"

    tyrone "Pfft, kalau kamu bilang begitu..."

    tyrone "Jalanmu masih panjang jika ingin menantangku, tapi kamu semakin dekat."

    tyrone "{b}Mampirlah satu malam lagi dan kita akan pergi lagi{/b}."

    anon "Baiklah."

    hide anon with dissolve
    return

label park_douches_battle_4:
    chico f_angry a_mic_speak "{i}Aku muak denganmu, kawan... Aku akan merokok kamu malam ini!{/i}"

    chico "{i}Gulung kamu dengan kertas dan bakar kamu!{/i}"

    chico "{i}Lirik ini sangat tajam dan rapku sangat berdarah!{/i}"

    chico "{i}Lari kecilmu di sini lucu tapi ini adalah akhir dari cerita itu.{/i}"

    chico "{i}Kau tidak akan bisa melewatiku, jalang! Singkirkan itu dari kepalamu.{/i}"

    chico "{i}Sebaiknya kamu pulang sekarang, sebelum kamu mati.{/i}"

    show anon f_worried
    show tyrone f_smirk
    show chico a_mic with dissolve
    chad f_happy "Oooh, harium!"

    tyrone "Baiklah, baiklah... Cukup bagus, sebagai permulaan."

    tyrone "Anda harus mengatasinya sekarang, Anda siap?"

    anon "Y-ya, oke."

    tyrone "Putar omong kosong itu!"

    return

label park_douches_battle_4_pass:
    show anon f_snarky a_mic_speak
    show chad f_normal
    show chico f_cocky
    show tyrone f_normal
    with fade
    anon "{i}Lagi dengan ancamannya? Tampaknya semua yang ingin Anda lakukan adalah memo...{/i}"

    anon "{i}Tapi menurutku itu masuk akal, karena jelas kamu tidak bisa nge-rap.{/i}"

    anon "{i}Aku senang ini sudah berakhir, aku tidak bisa mengintipnya lagi...{/i}"

    anon "{i}Sajakmu jelek sekali hingga membuatku tertidur!{/i}"

    anon "{i}Kamu seharusnya malu, dawg. Itu saja yang ingin saya katakan...{/i}"

    anon "{i}Ini bukan pertarungan, ini permainan anak-anak.{/i}"

    show chico f_angry
    show tyrone f_smirk
    show anon f_normal a_mic with dissolve
    chad f_happy @ f_laugh "HAHAHAH!"

    chico "Yo, persetan denganmu yang berkulit putih!"

    tyrone f_normal "Hei, jangan seperti itu..."

    tyrone "Ambil L-mu dengan bermartabat, kawan."

    chico "Cih, terserah..."

    tyrone f_smirk "{b}[firstname]{/b} siap naik peringkat!"

    tyrone "Anda masih harus melewati {b}Chad{/b} sebelum Anda dapat menghadapi saya..."

    chad "Ya, selanjutnya kamu harus melewatiku, dawg!"

    tyrone "{b}Mampirlah satu malam lagi dan kita akan pergi lagi{/b}."

    anon "Baiklah."

    hide anon with dissolve
    return

label park_douches_battle_5:
    chad f_angry a_mic_speak "{i}Saya tahu kita baru saja bertemu, dan Anda akan mendapatkan perhatian saya,{/i}"

    chad "{i}Tapi tolong tunggu dulu, sementara saya melanggar konvensi.{/i}"

    show chad with dissolve:
        flip
        xoffset 260
    chad "{i}Apa yang terjadi {b}Chico{/b}? Kamu harus mengakhiri orang ini,{/i}"

    show chico f_angry
    chad "{i}Tahu apa? Sudahlah. Duduk, dengarkan, dapatkan petunjuk.{/i}"

    show chad with dissolve:
        unflip
        chad_front
    chad "{i}Terima kasih sudah menunggu, sekarang tolong cepat?{/i}"

    chad a_open "{i}Tunggu, apa yang aku katakan? Tidak tertarik. *Klik!*{/i}"

    show tyrone f_smirk
    show chad f_happy a_idle with dissolve
    chico f_normal "Sobat, aku tidak tahu betapa pandainya kamu dalam berima, tapi kamu tidak bisa membuang sampah sembarangan..."

    tyrone "Tenang, {b}Chico{/b}... Dia baru saja memulai."

    chico f_cocky "Pfft, terserah homie."

    tyrone f_normal "Anda harus mengatasinya sekarang, Anda siap?"

    anon "Y-ya, oke."

    tyrone f_smirk "Putar omong kosong itu!"

    return

label park_douches_battle_5_pass:
    show anon f_snarky a_mic_speak
    show chad f_normal
    show chico f_cocky
    show tyrone f_smirk
    with fade
    anon "{i}Ada apa dengan sandiwara itu? Anda perwakilan pusat panggilan?{/i}"

    anon "{i}Kamu tahu kamu sedang melawanku, kan? Oke? Ya?{/i}"

    anon "{i}Tidak akan berusaha menyangkalnya, permainan rimamu kuat,{/i}"

    anon "{i}Aku hampir mengerti bagaimana orang bodoh ini menganggapmu.{/i}"

    anon "{i}Tapi pembicaraan sampah tingkat sampah itu, saya tidak bisa memaafkannya.{/i}"

    anon "{i}Punya teguran? Simpan itu. Biarkan setelah nada.{/i}"

    show chico f_cocky
    show anon f_normal a_mic with dissolve
    chad a_crossed "Sial."

    tyrone "Baiklah baiklah."

    chico "Dia menangkapmu, {b}Chad{/b}."

    tyrone "Ya, jaraknya cukup dekat tetapi saya harus memberikan kemenangan kepada darah baru."

    chad f_normal_down a_idle @ a_open "Astaga, itu buruk!"

    chico "Kamu seharusnya mengelap lantai bersamanya, kawan..."

    chad "Ya, saya tahu..."

    chad "Cih, sial!"

    tyrone "{b}Mampirlah satu malam lagi dan kita akan pergi lagi{/b}."

    anon "Baiklah."

    hide anon with dissolve
    return

label park_douches_battle_6:
    chad f_angry a_mic_speak "{i}Sekolah kembali aktif, sekarang bawa ke kelas,{/i}"

    chad "{i}Kamu gagal lebih keras dariku, dan aku berada jauh di atas rumput!{/i}"

    chad "{i}Apa yang mencuri fokus Anda? Apa yang ada di pikiranmu?{/i}"

    chad "{i}Kerudung kecil berwarna biru dan bagian belakangnya yang mengecewakan?{/i}"

    chad "{i}Tarik napas, lihat sekeliling, saya pikir Anda mungkin menemukannya,{/i}"

    chad "{i}Tanganmu terkunci, dan kamu mulai menjadi buta!{/i}"

    show chad f_happy a_mic with dissolve
    chico f_cocky "Sobat, aku tidak tahu betapa pandainya kamu dalam bersajak, tetapi kamu tidak bisa membuang sampah sembarangan..."

    tyrone "Tenang, {b}Chico{/b}... Dia baru saja memulai."

    chico "Pfft, terserah homie."

    tyrone f_normal "Anda harus mengatasinya sekarang, Anda siap?"

    anon "Y-ya, oke."

    tyrone f_smirk "Putar omong kosong itu!"

    return

label park_douches_battle_6_pass:
    show anon f_snarky a_mic_speak
    show chad f_normal
    show chico f_cocky
    show tyrone f_smirk
    with fade
    anon "{i}Mendengar itu, saya tidak yakin, saya yang tunanetra,{/i}"

    anon "{i}Tapi mungkin Anda juga tidak, dengan cara Anda menatap.{/i}"

    anon "{i}Perkataan dan tindakan yang bertentangan, pikiranmu kacau balau,{/i}"

    anon "{i}Bagaimana Anda berhasil sejauh ini dalam hidup, tidak ada yang bisa menebaknya.{/i}"

    anon "{i}Dan jangan khawatir {b}Chad{/b}, tentang sel otak, saya punya banyak,{/i}"

    anon "{i}Aduh, kamu akan terlambat, ini hampir jam 4:20!{/i}"

    show chico f_cocky
    show anon f_normal a_mic with dissolve
    chad f_normal_down a_crossed "Sial."

    tyrone "Baiklah baiklah."

    chico "Keduanya menyebalkan... Kalau boleh jujur."

    show chad f_angry
    tyrone "Ya, itu cukup dekat."

    tyrone "Saya akan memberikan kemenangan kepada darah baru."

    chad f_normal a_idle @ a_open "Astaga, itu buruk!"

    chico "Kamu seharusnya mengelap lantai bersamanya, kawan..."

    chad f_normal_down "Ya, saya tahu..."

    chad "Cih, sial!"

    tyrone "{b}Mampirlah satu malam lagi dan kita akan pergi lagi{/b}."

    anon "Baiklah."

    hide anon with dissolve
    return

label park_douches_battle_7:
    chad f_angry a_mic_speak "{i}Aku meningkatkan rapnya, kamu tidak bisa memegang lilin,{/i}"

    chad "{i}Lihat orang bodoh ini, berdiri di sana dengan sandalnya.{/i}"

    chad "{i}Sungguh menyedihkan, kamu terlihat terjebak dalam kebiasaan,{/i}"

    chad "{i}Sendiri, tragisnya merindukan, mengejar pantat Blue.{/i}"

    chad "{i}Jika wajahmu tidak terlalu serius, mungkin malah lucu,{/i}"

    chad "{i}Saat ini ini tidak menyenangkan, rasanya seperti menendang kelinci.{/i}"

    show chad f_happy a_mic with dissolve
    chico f_cocky "Sobat, aku tidak tahu betapa pandainya kamu dalam bersajak, tetapi kamu tidak bisa membuang sampah sembarangan..."

    tyrone @ f_laugh "Ha ha ha!"

    chico "Sungguh menyakitkan melihat omong kosong ini..."

    tyrone f_normal "Anda harus mengatasinya sekarang, Anda siap?"

    anon "Y-ya, oke."

    tyrone f_smirk "Putar omong kosong itu!"

    return

label park_douches_battle_7_pass:
    show anon f_snarky a_mic_speak
    show chad f_normal
    show chico f_cocky
    show tyrone f_smirk
    with fade
    anon "{i}{b}Chad{/b}, tolong. Demi kebaikan kita semua, berhentilah.{/i}"

    anon "{i}Di sini, izinkan saya menghibur Anda: hop, hop-hop.{/i}"

    anon "{i}Aku merasa tidak enak karena kamu tidak bisa bersantai, jadilah lebih laissez-faire,{/i}"

    anon "{i}Dan hilangkan obsesi aneh ini dengan bokong {b}Eve{/b}.{/i}"

    anon "{i}Dan sandalku? Benar-benar? Saya pikir Anda akan membidik lebih tinggi,{/i}"

    anon "{i}Daripada serangan terakhir yang putus asa pada pakaian musimanku.{/i}"

    anon "{i}Jadi kelasmu menyenangkan, sayangnya rapmu jelek,{/i}"

    anon "{i}Saya lulus sekolah ini, sudah berakhir, selamat tinggal {b}Chad{/b}.{/i}"

    show chico f_cocky
    show anon f_normal a_mic with dissolve
    chad f_normal_down "Sial."

    tyrone "Baiklah baiklah."

    chico "Saya tidak tahan lagi dengan hal ini."

    tyrone "Ya, saya pikir ini saatnya mengeluarkan senjata besar."

    tyrone "Kamu akan menghadapiku lain kali, gosok!"

    chad f_happy @ a_open "Wah, kamu dalam masalah sekarang {b}[firstname]{/b}..."

    tyrone "{b}Datanglah satu malam lagi, dan kita akan memulainya{/b}!"

    anon "Baiklah."

    hide anon with dissolve
    return

label park_douches_battle_8:
    tyrone f_angry a_mic_speak "{i}Berhenti di tempat Anda berada! Hei, bekukan! Ambil posisi!{/i}"

    tyrone "{i}Anda akan ditangkap, dituduh memiliki ambisi yang tidak semestinya!{/i}"

    tyrone "{i}Kamu ingin bergabung, mengunyah kruku?{/i}"

    tyrone @ f_smirk "{i}Dan semua yang kamu lakukan, jadi kita berhenti mengganggu Blue?{/i}"

    tyrone "{i}Rasa hormat yang luar biasa, tapi hal itu tidak akan terjadi,{/i}"

    tyrone "{i}Ini taman kami, dan Anda tidak sanggup bertempur.{/i}"

    show chad f_happy
    show tyrone f_smirk a_mic with dissolve
    chico f_cocky "Dayum!"

    chad @ a_open "Itu mematikan, sial!"

    tyrone "Anda pikir Anda bisa mengatasinya?"

    anon "Y-ya, oke."

    tyrone "Mari kita dengarkan!"

    return

label park_douches_battle_8_pass:
    show anon f_snarky a_mic_speak
    show chad f_normal
    show chico f_normal
    show tyrone f_smirk
    with fade
    anon "{i}Saya mengharapkan yang terburuk, berharap yang terbaik,{/i}"

    anon "{i}Tapi itu hanya lelucon, warnai aku: tidak terkesan.{/i}"

    anon "{i}{b}Chico{/b}? {b}Anak{/b}? Ada apa? Orang ini pemimpinmu?{/i}"

    anon "{i}Apa saja persyaratannya? Pemberi dan penerima?{/i}"

    anon "{i}Taman ini sudah menjadi milikku, pertarungan ini sangat seru,{/i}"

    anon "{i}Saya akan meninggalkan kalian sendirian untuk pertandingan tiga arah berikutnya!{/i}"

    show chico f_cocky
    show chad f_happy
    show anon f_normal a_mic with dissolve
    chad @ a_open "Wah!"

    chico "Baiklah, itu cukup bagus..."

    tyrone "Ya, tidak buruk sama sekali, Nak!"

    tyrone "Saya ingin mendengar lebih banyak!"

    tyrone "{b}Mampirlah satu malam lagi dan kita akan pergi lagi{/b}."

    anon "Baiklah."

    hide anon with dissolve
    return

label park_douches_battle_9:
    tyrone a_mic_speak "{i}Sial, kawan. aku salah menilai kamu. Saya akan memberikan konsesi itu,{/i}"

    tyrone f_angry "{i}Tapi kamu sudah keluar dari kemampuanmu, ini bukan sesi membanting puisi.{/i}"

    tyrone "{i}Pemilik rumah itu cukup menarik, tapi sepertinya dia sendirian,{/i}"

    tyrone f_smirk "{i}Menurutmu dia akan tergoda untuk merendahkanku?{/i}"

    tyrone "{i}Dan cewek yang tinggal bersamamu itu? Ya, dia memiliki penampilan seperti itu,{/i}"

    tyrone "{i}Kamu tahu yang satu itu. Anda bisa menjadi orang yang tidak berguna bagi diri kita sendiri.{/i}"

    tyrone "{i}Goreng kami sesuatu yang enak, di Sabtu pagi yang cerah,{/i}"

    tyrone "{i}Kalau begitu duduklah di pojok, dan saksikan kami membuat film porno.{/i}"

    show chad f_happy
    show tyrone a_mic with dissolve
    chico f_cocky "Dayum!"

    chad "Itu mematikan, sial!"

    tyrone f_normal "Anda pikir Anda bisa mengatasinya?"

    anon "Y-ya, oke."

    tyrone f_smirk "Mari kita dengarkan!"

    return

label park_douches_battle_9_pass:
    show anon f_snarky a_mic_speak
    show chad f_normal
    show chico f_normal
    show tyrone f_smirk
    with fade
    anon "{i}Rasakan baja dinginku, kamu membuatku terpicu secara lirik,{/i}"

    anon "{i}Apa pun yang Anda harapkan, itu tidak seperti yang Anda bayangkan.{/i}"

    anon "{i}Perasaan itu sendirian? Tidak, sial, itu kamu. Anda memproyeksikan,{/i}"

    anon "{i}Sangat tidak ingin merasakan apa yang Anda curigai.{/i}"

    anon "{i}Bahwa kamu duduk di sini, di taman ini, hari demi hari,{/i}"

    anon "{i}Berjuang sekuat tenaga, untuk mengusir kebosanan.{/i}"

    anon "{i}Mencoba untuk tidak menyerah pada ketakutan eksistensial itu,{/i}"

    anon "{i}Bahwa kamu sendirian, tidak ada yang peduli, lebih baik kamu mati saja.{/i}"

    anon "{i}Kamu berharap ada satu orang saja yang peduli,{/i}"

    anon "{i}Tapi apakah mengherankan jika kamu bertingkah seperti ini?{/i}"

    anon "{i}Kecemburuan itu terlihat jelas, sungguh menyesakkan,{/i}"

    anon "{i}Namun kamu membongkar barang-barang kesayanganmu seperti barang sepele berisi jeli.{/i}"

    anon "{i}Trio kecil yang menyedihkan ini, mengejek orang lain,{/i}"

    anon "{i}Terjebak dalam keadaan statis, sendirian; kelompok yang paling tragis.{/i}"

    anon "{i}Tidak pernah melakukan apa pun selain nongkrong di taman ini,{/i}"

    anon "{i}Bertanya-tanya apa yang harus dilakukan dengan masa depan yang begitu sulit.{/i}"

    pause
    anon "{i}Lampu padam, pikiranmu jurang menganga,{/i}"

    anon "{i}Berdiri di sana, tegak tak dapat membayangkan.{/i}"

    anon "{i}Izinkan saya membantu dengan sederhana, \"Oh ya, benar!\"{/i}"

    anon "{i}Tapi hei, tenang saja, tidak ada personel{#sic}, Nak.{/i}"

    show chico f_cocky
    show anon f_normal a_mic with dissolve
    chad f_happy @ f_laugh "Wah!"

    chico "Baiklah, itu cukup bagus..."

    tyrone "Ya, tidak buruk sama sekali, Nak!"

    tyrone "Saya ingin mendengar lebih banyak!"

    tyrone "{b}Mampirlah satu malam lagi dan kita akan pergi lagi{/b}."

    anon "Baiklah."

    hide anon with dissolve
    return

label park_douches_battle_10:

    return

label park_douches_battle_10_pass:
    show anon f_snarky a_mic_speak
    show chad
    show chico
    show tyrone f_smirk
    with fade
    anon "{i}Saya akan menghentikan Anda sampai di situ, sudah jelas bahwa Anda sudah selesai.{/i}"

    anon "{i}Kamu langsung keluar dari rap, dan aku mendapat banyak sekali.{/i}"

    anon "{i}Jadi aku akan naik perahumu dan berlayar ke laut rap.{/i}"

    anon "{i}Tak terkalahkan dan tak terbantahkan, MC terbaik.{/i}"

    anon "{i}Saya telah mengalahkan kru Anda dan sekarang Anda tunduk,{/i}"

    anon "{i}Lihat aku jalang, aku kaptennya sekarang.{/i}"

    show chad f_happy
    show chico f_cocky
    show anon f_normal a_mic with dissolve
    tyrone @ f_laugh "Ha ha ha!"

    tyrone "Baiklah, baiklah, kamu menang..."

    chad "Itu obat bius!"

    tyrone "Benar?"

    tyrone "Saya suka anak ini."

    chico @ f_eyeroll "Astaga, dia baik-baik saja..."

    tyrone "Kamu bisa jalan-jalan bersama kami kapan saja kamu mau, kamu mengerti?"

    anon "Apakah itu berarti kalian akan meninggalkan temanku sendirian?"

    tyrone f_normal "Siapa?"

    pause
    tyrone a_hands_rub "Berkerudung biru kecil?"

    chad @ f_laugh "Haha!"

    anon "Namanya {b}Hawa{/b}..."

    tyrone f_smirk a_idle "Ya, siapa pun itu."

    tyrone "Kami akan meninggalkan gadismu sendirian."

    anon "Bagus."

    tyrone "Datang saja dan sampaikan sajak bersama kami lagi kapan-kapan, oke?"

    anon "Kita lihat saja nanti."

    hide anon with dissolve
    return

label park_douches_battle_fail:
    show anon f_sad_down
    show chad f_angry
    show chico f_cocky
    show tyrone f_smirk
    with fade
    anon "Omong kosong."

    chico "Hehe, menyedihkan."

    show anon f_worried
    chad "Lihat, aku tahu ini hanya membuang-buang waktu!"

    if player.stats.chr() < 7:
        show tyrone:
            tyrone_front
        show chad:
            chad_middle
        show chico behind tyrone:
            chico_back
        with dissolve
    tyrone @ a_point "Itu omong kosong yang lemah, kawan..."

    tyrone "Kamu harus segera keluar dari sini!"

    anon @ a_point_self "Tidak, tunggu... Biarkan saya coba lagi!"

    chico f_angry "Anda tidak akan mendapatkan pengulangan dalam pertarungan rap."

    chico "Tersesat!"

    anon f_sad_down @ -m_talk "..."
    anon f_worried "Baiklah, tapi aku akan kembali lagi besok!"

    tyrone f_normal "Cih, siapa pun pria..."

    hide anon with dissolve
    return

label park_douches_eve_tuuku_with_douches_repeat:
    scene expression player.location.background_closeup with None
    show chad
    show chico:
        xoffset 100
    show tyrone:
        xoffset -125
    show anon f_worried:
        xoffset -100
    show tuuku f_confused a_hips:
        flip
        xoffset 100
    with dissolve
    tuuku "Roti Domba?"

    tuuku "Sangat asam?"

    tuuku "Putri Ungu?"

    tuuku "LA Rahasia?"

    chad "Yo, dia pasti mengada-ada!"

    tuuku "Permen Mars?"

    tuuku "Platina Jack?"

    tuuku "Berlian Putih?"

    anon @ -m_talk "(Saya mungkin harus fokus pada peran saya dalam lelucon ini.)"

    anon @ -m_talk "(Sekarang di mana {b}ransel mereka{/b} berada? )"

    hide anon with dissolve
    return

label park_douches_eve_tuuku_with_douches_first:
    scene expression player.location.background_closeup with None
    show chad
    show chico:
        xoffset 100
    show tyrone f_smirk:
        xoffset -125
    show anon f_worried:
        xoffset -100
    show tuuku f_happy:
        flip
        xoffset 100
    with dissolve
    tuuku "Anda benar-benar perlu mengembangkan lebih banyak teman..."

    tyrone "Ck, nah kawan."

    tyrone "Anda tahu saya hanya merokok OG Kryptonite itu!"

    chico "Ya, itu bomnya!!!"

    tuuku "Namun, ada begitu banyak strain lainnya, dan semuanya memberi Anda sensasi yang berbeda!"

    tuuku "Apakah kamu tidak ingin mencoba Cherry Kush atau Blue Haze?"

    chad "Beneran biru?"

    tuuku f_confused @ -m_talk "Hmm?"

    chad "Kamu bilang Blue Haze... Apakah itu benar-benar biru?"

    tuuku "Apa, suka warnanya?"

    chad "Ya?"

    show tyrone f_angry:
        flip
        xoffset 300
    with dissolve
    show tuuku f_happy
    tyrone @ a_point "Ya ampun, tentu saja warnanya bukan biru!"

    tyrone "Apa yang salah denganmu?!"

    chad f_angry "Astaga, bagaimana aku bisa tahu?!"

    show tyrone:
        unflip
        xoffset -150
    tyrone "Apa lagi yang kamu punya?"

    show chad f_normal
    tuuku "Hmm, Cali Emas?"

    tyrone "Ahh, tidak."

    tyrone "Sialan itu membuatku muncrat terakhir kali."

    show tuuku f_laugh
    chad @ f_normal_down "Pfft, aku yakin itu burrito yang kamu dapat di pom bensin, dawg."

    tyrone "Bung, diamlah!"

    tuuku f_confused "Pengendara banteng?"

    tyrone f_normal "Tidak."

    tuuku "Keluaran?"

    tyrone "Tidak uh."

    show anon f_surprised
    tuuku "Fantasi Asia?"

    chico "Astaga, berapa banyak strain yang kamu punya?!"

    tuuku "Kera Anggur?"

    tuuku "Naga Menyala?"

    tuuku "sigung lemon?"

    chad @ f_laugh "Ha ha ha!"

    anon f_worried @ -m_talk "(Saya mungkin harus fokus pada peran saya dalam lelucon ini.)"

    anon @ -m_talk "(Sekarang di mana {b}ransel mereka{/b} berada? )"

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
