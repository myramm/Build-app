label harold_police_office_dialogue_mia_route:
    show old_harold 1 at right
    show player 14 at left
    with dissolve
    player_name "Hai, {b}Harold{/b}!"

    show player 13
    show old_harold 2
    harold "Itu laki-lakiku!"

    show old_harold 1
    show player 14
    player_name "Bagaimana kabarnya akhir-akhir ini?"

    show player 13
    show old_harold 2
    harold "Tidak pernah lebih baik! Keluarga kami adalah yang paling bahagia yang pernah ada!"

    harold "{b}Helen{/b} benar-benar berubah. Sungguh... Berubah."

    harold "Segalanya menjadi sangat panas di tempat tidur-"

    show old_harold 4
    harold "Bagaimanapun, Anda tahu apa yang saya maksud."

    show old_harold 1
    show player 21
    player_name "Heh heh... Ya, menurutku..."

    show player 13
    show old_harold 2
    harold "Saya harus kembali bekerja."

    harold "Jangan ragu untuk mampir ke rumah kapan saja ya, Nak!"

    show old_harold 1
    show player 14
    player_name "Terima kasih, {b}Harold{/b}!"

    player_name "Sampai jumpa lagi."

    return

label harold_police_office_dialogue_helen_route_split:
    show player 22f at right
    show old_harold 51 at left
    with dissolve
    pause
    show old_harold 52
    show old_yumi 12f at Position (xpos=395)
    with dissolve
    yumi "!!!"
    show player 5f
    yumi "Oh! aku tidak melihatmu di sana..."

    show old_yumi 14f at Position (xpos=382) with dissolve
    show old_harold 53
    harold "Jangan khawatir, {b}Yumi{/b}, itu hanya teman kecil putriku."

    show old_harold 52
    show player 10f
    player_name "Halo..."

    show player 5f
    show old_yumi 13f
    yumi "Hai... Oh! Aku lupa aku punya sesuatu yang... Perlu aku urus di kantorku."

    hide old_yumi
    show old_harold 54
    with dissolve
    harold "..."
    show old_harold 55
    harold "Maaf kamu harus melihatnya, Nak."

    harold "{b}Yumi{/b} lebih merupakan pasangan yang siap sedia..."

    harold "Kupikir aku akan mencoba dan mengajarinya beberapa hal..."

    show old_harold 54
    show player 11f
    player_name "..."
    show player 10f
    player_name "Jadi Anda dan {b}Helen{/b}..."

    show player 5f
    show old_harold 55
    harold "Lihat. Kapal itu telah berlayar, Nak. {b}Helen{/b} sepertinya sudah menerima perpisahan kami."

    harold "Saya pikir sebaiknya saya melanjutkan juga."

    harold "Sejujurnya."

    harold "Saya tidak pernah sebahagia ini, dan saya mulai berkencan dengan orang lain."

    show old_harold 54
    show player 12f
    player_name "Aku ingin tahu siapa..."

    show player 10f
    player_name "Setidaknya kamu bahagia..."

    show player 5f
    pause
    show player 10f
    player_name "Namun bagaimana {b}Mia{/b} menangani hal ini? Apakah dia akan baik-baik saja?"

    show player 5f
    show old_harold 55
    harold "Saya tidak akan menyerah pada {b}Mia{/b}."

    harold "Saya mengunjunginya setiap hari. Dia gadis kecilku yang tangguh."

    harold "Dia selalu begitu, setelah harus menghadapi {b}Helen{/b} dan aku."

    harold "Dia akan baik-baik saja."

    show old_harold 54
    show player 12f
    player_name "Bagus."

    show player 5f
    show old_harold 55
    harold "Kamu anak yang baik, {b}[firstname]{/b}. Sekali lagi terima kasih karena telah peduli pada putriku."

    harold "Saya menghargai Anda dan dia yang mencoba mendapatkan saya kembali dengan {b}Helen{/b}..."

    harold "Hanya saja ada beberapa hal yang tidak berhasil..."

    show old_harold 54
    show player 21f
    player_name "Hehehe..."

    player_name "Terima kasih kembali."

    show player 5f
    show old_harold 55
    harold "Jangan takut untuk mengunjungi saya jika ada sesuatu yang memerlukan bantuan."

    show old_harold 54
    show player 36f with dissolve
    player_name "Akan dilakukan. Selamat tinggal, {b}Harold{/b}."

    return

label harold_police_office_dialogue_mia_harold_backup:
    show old_harold 1 at Position (xpos=762)
    show player 23 at left
    with dissolve
    player_name "{b}Harold{/b}!!"

    show player 22
    show old_harold 6
    harold "Apa yang terjadi? Apakah Anda menemukan {b}Yumi{/b}?"

    show old_harold 1
    show player 38 with dissolve
    player_name "Ya! Tapi dia membutuhkan bantuanmu, sekarang!!"

    show player 3 with dissolve
    show old_harold 3
    harold "Apa?!"

    show old_harold 1
    show player 10 with dissolve
    player_name "Di dalam sel! {b}Yumi{/b}... Dia berjuang dengan seorang narapidana!!"

    show player 5
    show old_harold 29
    harold "!!!"
    show old_harold 30 at right with dissolve
    harold "Aku... Aku harus meminta bantuan lagi. Mungkin aku harus memberitahu {b}Earl{/b} dulu-"

    show player 12
    player_name "{b}Harold{/b}! Tidak ada waktu!"

    hide old_harold
    show old_harold 25 at Position (xpos=762)
    with dissolve
    player_name "Anda harus mengendalikan situasi."

    show player 11
    show old_harold 26
    harold "Tapi aku harus memberitahu {b}Earl{/b} dulu..."

    harold "...Aku sudah lama tidak berurusan dengan narapidana dan-"

    show old_harold 25
    show player 15
    player_name "{b}Yumi{/b} adalah partnermu dan membutuhkan bantuanmu!"

    player_name "Anda harus pergi! SEKARANG!!!"

    show player 16
    show old_harold 24
    harold "..."
    show old_harold 6
    harold "Anda benar. Saya harus mengambil tindakan."

    harold "Ayo pergi."

    return

label harold_police_office_dialogue_mia_harolds_thoughts:
    show old_harold 1 at right
    show player 36 at left
    with dissolve
    player_name "Hai, {b}Harold{/b}."

    show player 13 with dissolve
    show old_harold 2
    harold "Halo lagi, Nak."

    show old_harold 1
    show player 14
    player_name "Kupikir aku akan mampir dan melihat bagaimana makan malam bersama {b}Mia{/b} dan {b}Helen{/b}."

    show player 13
    show old_harold 6
    harold "Oh... Umm... Kurasa tidak apa-apa. Makanannya sangat enak."

    show old_harold 1
    show player 10
    player_name "Apakah menurut Anda segalanya... Menjadi lebih baik antara {b}Helen{/b}... Dan Anda?"

    show player 5
    show old_harold 4
    harold "..."
    show old_harold 6
    harold "Saya tahu {b}Mia{/b} sedang mencoba untuk mendapatkan {b}Helen{/b} dan saya kembali bersama."

    harold "Anda telah membantunya juga. Kamu anak yang baik."

    show old_harold 1
    harold "..."
    show old_harold 6
    harold "Saya kira hal-hal antara {b}Helen{/b} dan saya lebih baik daripada saat Anda melihat kami saling bertengkar."

    show old_harold 4
    pause
    harold "Aku... Tapi aku tidak tahu..."

    show old_harold 1
    pause
    show player 10
    player_name "Kenapa kamu tidak tahu?"

    show player 5
    show old_harold 26
    harold "Oh, Nak."

    harold "Hubungan kami mungkin baik-baik saja sekarang, tapi kami bisa saja kembali bertengkar lagi."

    harold "Untuk kali ini, aku berpikir mungkin aku akan lebih bahagia jika sendirian."

    harold "Pernikahan saya mungkin lebih baik ditinggalkan."

    harold "Mungkin... Jika {b}Helen{/b} benar-benar berubah selamanya."

    harold "Ada kemungkinan bagi kita untuk kembali bersama."

    show old_harold 1
    show player 14
    player_name "Aku... aku mengerti."

    show player 13
    show old_harold 6
    harold "Sebaiknya aku kembali bekerja. Saya baru saja mendapat terobosan lain dalam sebuah kasus."

    show old_harold 2
    harold "Sampai jumpa lagi, {b}[firstname]{/b}."

    show old_harold 1
    show player 14
    player_name "Sampai jumpa, {b}Harold{/b}."

    show player 13
    hide old_harold with dissolve
    pause
    show player 14
    player_name "( Kedengarannya seperti {b}Harold{/b} memberitahuku bahwa ada kemungkinan dia akan kembali dengan {b}Helen{/b}. )"

    show player 35
    player_name "( Mungkin pelatihan {b}Sister Angelica{/b} sebenarnya membantunya dan {b}Harold{/b}. )"

    show player 10
    player_name "( Tapi... Dia nampaknya bahagia saat ini tanpa {b}Helen{/b}... )"

    player_name "( {b}Mia{/b} akan hancur jika dia tidak kembali dengan {b}Helen{/b}. )"

    show player 5
    player_name "..."
    show player 12
    player_name "(Saya kira itu bukan terserah saya pada saat ini...)"

    player_name "(Sebaiknya selesaikan membantu {b}Suster Angelica{/b}. )"

    show player 35
    player_name "(Apa yang dia inginkan lagi?)"

    hide player with dissolve
    return

label harold_police_office_dialogue_roxxy_ask_earl_release:
    scene police_c_2
    show old_harold 1 at right
    show old_roxxy 1of at Position (xpos=400)
    show player 10 at left
    with dissolve
    player_name "Hei, um..."

    player_name "Ibu teman saya ditahan hari ini, dan kami perlu mencari tahu apa yang terjadi."

    show player 5
    show old_harold 2
    harold "Hmm?"

    show old_harold 2
    harold "Oh, kamu pasti putri {b}Crystal{/b}!"

    show old_harold 1
    show old_roxxy 33f
    roxxy "... Ya."

    show old_roxxy 32f
    show old_harold 2
    harold "Sheesh, kamu adalah gambarannya di masa mudanya!"

    show old_harold 1
    roxxy "..."
    show player 10
    player_name "Uhh, bisakah kamu memberi tahu kami mengapa kamu memegangnya?"

    show player 5
    show old_harold 2
    harold "Maaf, Nak."

    harold "Penggerebekan narkoba sebesar ini jauh di atas nilai gajiku."

    harold "Anda harus berbicara dengan kepala suku jika Anda menginginkan detailnya."

    show old_harold 1
    show player 10
    player_name "... Oh."

    player_name "Baiklah terima kasih."

    show player 5
    hide old_harold with dissolve
    pause
    show old_roxxy 2c at center
    show old_roxxy 2c at Position (xoffset=-33)
    with dissolve
    roxxy "Ya Tuhan... Mereka pasti telah menemukan seluruh simpanan {b}Clyde{/b}!"

    show old_roxxy 2b at Position (xoffset=-33)
    show player 12
    player_name "Berapa banyak sabu yang dimiliki sepupumu?!"

    show player 5
    show old_roxxy 1j with dissolve
    roxxy "..."
    show old_roxxy 1l
    roxxy "aku... uhh..."

    roxxy "... Saya tidak yakin."

    show old_roxxy 1j
    show player 12
    player_name "Baiklah, menurutku sebaiknya kita {b}bicara dengan ketua{/b}."

    hide player
    hide old_roxxy
    with dissolve
    return

label harold_police_office_dialogue_pre:
    show player 1 at left
    show old_harold 2 at right
    with dissolve
    harold "Oh, hei, itu kamu lagi. Butuh sesuatu?"

    show old_harold 1
    show player 14
    player_name "Hai, saya baru saja punya beberapa pertanyaan."

    show player 1
    return

label harold_police_office_dialogue_wheres_mia:
    show player 14
    player_name "Saya hanya ingin tahu: apakah Anda tahu di mana {b}Mia{/b} berada?"

    show player 11
    show old_harold 2
    harold "Maaf, saya tidak dapat membantu Anda saat ini; kami sedang sibuk dengan kasus baru..."

    harold "Tapi, dia harusnya ada di sekolah atau di rumah."

    show old_harold 1
    show player 14
    player_name "Oke. Terima kasih tuan!"

    return

label harold_police_office_dialogue_the_chief:
    show player 12
    player_name "Siapa ketuanya?"

    show player 5
    show old_harold 2
    harold "Oh, Anda ingin {b}Earl{/b}."

    show player 13
    harold "Dia ada di sana, di sisi lain kantor."

    show old_harold 1
    show player 14
    player_name "Oke, terima kasih!"

    return

label harold_police_office_dialogue_larry:
    show player 10
    player_name "Apa yang perlu saya tanyakan {b}Larry{/b}?"

    show player 5
    show old_harold 6
    harold "{b}Larry{/b} tidak memberikan lokasi barangnya."

    show old_harold 1
    show player 33
    player_name "Oh ya!"

    show player 12
    player_name "Saya akan berbicara dengannya. Saya kenal istrinya."

    player_name "Jika saya tidak bisa mengetahui lokasinya, mungkin saya bisa menghubungi {b}Ny. Johnson{/b} untuk membantu kami."

    show player 5
    show old_harold 2
    harold "Terima kasih, {b}[firstname]{/b}."

    return

label harold_police_office_dialogue_thief:
    show player 10
    player_name "Apa yang perlu saya lakukan jika saya melihat pencuri itu lagi?"

    show player 5
    show old_harold 6
    harold "Jika Anda memperhatikannya, hubungi saya langsung."

    show old_harold 1
    show player 12
    player_name "Tentu saja! Aku akan mengawasinya."

    player_name "Dia selalu menyelinap ke rumah tetanggaku, {b}Ny. Johnson{/b}'s, halaman di malam hari."

    show player 5
    show old_harold 6
    harold "Ada juga laporan tentang dia di dekat taman. Jika Anda kebetulan melihatnya di sana, terus kabari saya."

    show old_harold 1
    show player 12
    player_name "Oke, saya akan memeriksa petunjuknya juga."

    show player 5
    show old_harold 2
    harold "Terima kasih, {b}[firstname]{/b}."

    return

label harold_police_office_dialogue_donuts:
    show player 14
    player_name "Apa {i}barang{/i} dari... Donat, err... Apakah kamu suka?"

    show player 11
    show old_harold 3
    harold "Permisi?"

    show player 14
    show old_harold 1
    player_name "Hanya ingin tahu!"

    show player 11
    show old_harold 2
    harold "Dengar, aku tidak punya waktu untuk ngobrol sekarang, aku sibuk dengan pekerjaan..."

    harold "Mengapa kamu tidak lari ke sekolah, oke?"

    show player 10
    show old_harold 1
    player_name "Tapi-"

    show player 5
    show old_harold 2
    harold "Aku harus pergi, maaf."

    return

label harold_police_office_dialogue_donuts_wrong:
    show player 437 at left with fastdissolve
    player_name "Aku salah, aku membawakanmu sesuatu."

    show player 1
    show player 436
    harold "..."
    show player 437
    player_name "Ini untukmu!"

    show old_harold 8
    show player 1
    with fastdissolve
    harold "Kamu membawakanku sekotak... Donat?!"

    show player 14
    show old_harold 7
    player_name "Ya! Saya pikir mungkin Anda ingin mengemilnya di tempat kerja..."

    show player 1
    show old_harold 9
    harold "Oh..."

    harold "Sejujurnya, saya bukan penggemar berat hal semacam itu."

    show player 11
    show old_harold 10
    player_name "..."
    show old_harold 11
    harold "Tapi saya salah... Saya menghargai pemikiran itu!"

    harold "Saya yakin {b}Earl{/b} akan sangat senang memilikinya..."

    show player 10
    show old_harold 10
    player_name "Baiklah."


    show player 5
    hide old_harold with dissolve
    pause
    show player 10
    player_name "(Sial!)"

    player_name "(Saya pasti membeli jenis yang salah.)"

    player_name "(Saya harus memastikan saya mendapatkan bahan yang tepat...)"

    return

label harold_police_office_dialogue_donuts_correct:
    show player 437 at left with fastdissolve
    player_name "Aku salah, aku membawakanmu sesuatu."

    show player 1
    show player 436
    harold "..."
    show player 437
    player_name "Ini untukmu!"

    show old_harold 8
    show player 1
    with fastdissolve
    harold "Kamu membawakanku sekotak... Donat?!"

    show player 14
    show old_harold 7
    player_name "Ya! Saya pikir mungkin Anda ingin mengemilnya di tempat kerja..."

    show player 1
    show old_harold 9
    harold "Biarkan aku melihat..."

    harold "Astaga... [harold_glaze]... Dengan... [harold_topping]?!"

    show player 14
    show old_harold 7
    player_name "Saya pikir Anda akan menyukainya!"

    show player 1
    show old_harold 8
    harold "Ini adalah favoritku... Bagaimana kabarmu..."

    show player 17
    show old_harold 44
    player_name "Saya beruntung, saya kira."

    show player 1
    show old_harold 45
    harold "{i}*Nomor nom*{/i}"

    show old_harold 46
    harold "Baiklah, Nak, kamu melakukannya dengan baik."

    show player 17
    show old_harold 45
    player_name "Senang Anda menyukainya!"

    show player 1
    harold "..."
    show player 11
    show old_harold 46
    harold "Tunggu, sebelum kamu pergi..."

    show player 1
    harold "Aku tahu kamu dan {b}Mia{/b} suka... Nongkrong, dan sebagainya."

    harold "Kamu tampak seperti anak yang baik, jadi aku akan berbicara dengan istriku dan melihat apakah dia bisa memberhentikannya sedikit."

    show player 14
    show old_harold 45
    player_name "Maksudmu, aku bisa mengunjunginya sekarang?"

    show player 1
    show old_harold 46
    harold "Tidak terlalu cepat!"

    harold "Aku tidak mengatakan itu... Tapi... Kamu mungkin bisa menyelinap masuk seperti sebelumnya, dan aku akan mencoba mengalihkan perhatian istriku, oke?"

    show player 14
    show old_harold 45
    player_name "Benar-benar?"

    show player 1
    show old_harold 46
    harold "Aku bilang aku akan mencoba, aku tidak bisa menjanjikan apa pun padamu."

    show player 14
    show old_harold 45
    player_name "Terima kasih, {b}Harold{/b}."

    show player 1
    show old_harold 46
    harold "Baiklah, sekarang keluar dari sini sebelum bosku melihat kita membawa donat ini!"

    show player 17
    show old_harold 45
    player_name "Haha."

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
