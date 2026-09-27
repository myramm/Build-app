label button_crystal_preamble:
    show player 5 at left
    show old_crystal 3 at right
    with dissolve
    crystal "Itu pacar gadis kecilku lagi."

    show old_crystal 1 with dissolve
    show player 10
    player_name "Sudah kubilang, kami tidak-"

    show player 5
    show old_crystal 2
    crystal "Apapun yang kamu katakan, anak muda."

    show old_crystal 4 with dissolve
    crystal "{i}*Meneguk*{/i}"

    show old_crystal 2 with dissolve
    crystal "Jadi, apa yang kamu inginkan?"

    return

label button_crystal_roxxys_dad:
    show player 10
    player_name "Dimana {b}Roxxy{/b}... Ayah?"

    show player 11
    show old_crystal 2
    crystal "Hah! Dia tidak punya ayah!"

    crystal "Saya sendiri yang membesarkannya."

    show old_crystal 1
    show player 10
    player_name "Jadi begitu."

    show player 11
    show old_crystal 2
    crystal "Sejujurnya, saya tidak ingat yang mana..."

    show old_crystal 4 with dissolve
    crystal "{i}*Meneguk*{/i}"

    show old_crystal 2 with dissolve
    crystal "... Jadi ayahnya bisa jadi siapa saja, sejauh yang aku tahu."

    show old_crystal 1
    show player 22
    player_name "!!!"
    show old_crystal 2
    crystal "Ada lagi yang ingin Anda bicarakan?"

    show player 5
    show old_crystal 1
    return

label button_crystal_roxxy:
    show player 10
    player_name "Tahukah Anda di mana saya bisa menemukan {b}Roxxy{/b}?"

    show player 5
    show old_crystal 3 with dissolve
    crystal "Hah! Anda pikir saya mengasuh putri saya?"

    show old_crystal 1 with dissolve
    show player 10
    player_name "Hmm..."

    show player 5
    show old_crystal 2
    crystal "Dia selalu keluar melakukan hal-hal..."

    crystal "... Tapi, biasanya dia ada di {b}sekolah{/b} atau di {b}pantai{/b}."

    show old_crystal 1
    show player 14
    player_name "Oh. Jadi begitu. Terima kasih!"

    show player 13
    show old_crystal 2
    crystal "Ada lagi?"

    show old_crystal 1
    return

label button_crystal_nothing:
    show player 10
    player_name "Oh, tidak ada apa-apa."

    player_name "aku baru saja lewat..."

    show player 11
    show old_crystal 2
    crystal "Baiklah, sebentar lagi ada tamu yang datang, jadi kenapa kamu tidak ikut saja."

    show old_crystal 1
    show player 10
    player_name "Saya minta maaf. Kalau begitu aku berangkat."

    player_name "Selamat tinggal!"

    hide player
    hide old_crystal
    with dissolve
    return

label button_crystal_roxxy_go_to_picnic:
    scene expression "backgrounds/location_trailer_night_closeup.jpg"
    show player 5 at left
    show player_wet at left
    show old_crystal 3 at right
    with dissolve
    crystal "Mmm, kamu tahu aku bisa membantumu mengeluarkan pakaian basah itu jika kamu mau?"

    show old_crystal 1 with dissolve
    show player 10
    player_name "Uhh... aku..."

    show player 5
    player_name "..."
    show old_crystal 2
    crystal "Jangan malu sekarang."

    crystal "Pria tampan, seperti dirimu. Anda berhak mendapat perhatian khusus, bukan?"

    show old_crystal 1
    show player 3 with dissolve
    player_name "..."
    roxxy "{b}Bu{/b}, tinggalkan {b}[firstname]{/b} sendiri!"

    show old_crystal 2
    crystal "Hehehe, aku hanya menggodanya sedikit."

    show old_crystal 1
    roxxy "Baiklah, berhenti!"

    show old_crystal 4 with dissolve
    roxxy "{b}[firstname]{/b}, masuk ke sini!"

    show old_crystal 1
    player_name "..."
    hide old_crystal
    hide player
    hide player_wet
    with dissolve
    return

label button_crystal_rox8_11_evening:
    scene expression "backgrounds/location_trailer_closeup01_evening.jpg"
    show player 5 at left
    show old_crystal 6 at right
    with dissolve
    crystal "Kamu kalah, tampan?"

    show old_crystal 5
    show player 10
    player_name "Hah?"

    show player 5
    show old_crystal 6
    crystal "Oh, kamu pria baru {b}Roxxy{/b}."

    show old_crystal 5
    show player 12
    player_name "T-tidak, aku-"

    show player 5
    show old_crystal 6
    crystal "Dia ada di dalam."

    show old_crystal 5
    return

label button_crystal_rox8_11_day:
    scene trailer_interior_c
    show player 5 at left
    show old_crystal 2 at right
    with dissolve
    crystal "Kamu kalah, tampan?"

    show old_crystal 1
    show player 10
    player_name "Hah?"

    show player 5
    show old_crystal 2
    crystal "Oh, kamu pria baru {b}Roxxy{/b}."

    show old_crystal 1
    show player 10
    player_name "T-tidak, aku-"

    show player 5
    show old_crystal 2
    crystal "Dia tidak di sini."

    show old_crystal 4 with dissolve
    return

label button_crystal_final_evening:
    scene expression "backgrounds/location_trailer_closeup01_evening.jpg"
    show player 13 at left
    show old_crystal 6 at right
    with dissolve
    crystal "Mmm, sekarang ada pria yang baik dan cakap!"

    show old_crystal 5
    show player 14
    player_name "Heh, hai {b}Kristal{/b}..."

    show player 13
    show old_crystal 6
    crystal "Mengapa kamu tidak minum bir dan duduk bersamaku, Romeo?"

    crystal "Anda bisa memamerkan lidah perak itu lagi..."

    show old_crystal 5
    show player 14
    player_name "Oh, entahlah... {b}Roxxy{/b} tidak akan-"

    show player 5
    show old_crystal 6
    crystal "Kamu di sini untuk menelepon {b}Roxxy{/b}?"

    show old_crystal 5
    return

label button_crystal_final_day:
    scene trailer_interior_c
    show player 13 at left
    show old_crystal 2 at right
    with dissolve
    crystal "Mmm, sekarang ada pria yang baik dan cakap!"

    show old_crystal 1
    show player 14
    player_name "Heh, hai {b}Kristal{/b}..."

    show player 13
    show old_crystal 2
    crystal "Mengapa kamu tidak minum bir dan duduk bersamaku, Romeo?"

    crystal "Anda bisa memamerkan lidah perak itu lagi..."

    show old_crystal 1
    show player 14
    player_name "Oh, entahlah... {b}Roxxy{/b} tidak akan-"

    show player 5
    show old_crystal 2
    crystal "{b}Roxxy{/b} tidak ada di sini."

    show old_crystal 1
    return

label button_crystal_sorry_to_bother:
    show player 10
    player_name "Maaf mengganggumu."

    show player 5
    show old_crystal 6
    crystal "Psh, ngomong-ngomong, jangan ganggu aku..."

    crystal "... Sebenarnya, kenapa kamu tidak pergi ke toko dan membelikanku dua belas bungkus yang baru?"

    crystal "Lakukan itu dan kita bisa bicara sampai telingamu lepas."

    show old_crystal 5
    show player 17
    player_name "Hehe, tidak apa-apa."

    player_name "Saya harus masuk ke dalam dan melihat {b}Roxxy{/b}."

    show player 13
    show old_crystal 6
    crystal "Cocokkan dirimu."

    hide player
    hide old_crystal
    with dissolve
    return

label button_crystal_roxxy_rox8_rox11:
    show old_crystal 1 with dissolve
    show player 10
    player_name "Tahukah kamu dimana dia?"

    show player 5
    show old_crystal 2
    crystal "Psh, aku tidak tahu..."

    crystal "... Aku tidak bisa selalu melacak gadis itu."

    show old_crystal 1
    show player 10
    player_name "Benar-benar?"

    show player 5
    show old_crystal 2
    crystal "Anak nakal yang tidak tahu berterima kasih, jangan beritahu aku apa pun."

    crystal "Dia butuh teriakan! Apa yang dia butuhkan..."

    show old_crystal 1
    player_name "..."
    return

label button_crystal_roxxy_final:
    show old_crystal 4 with dissolve
    show player 12
    player_name "Di mana dia berada?"

    show player 5
    show old_crystal 2 with dissolve
    crystal "Sial kalau aku tahu."

    crystal "Jika dia tidak di sekolah, maka menurutku dia mungkin ada di pantai."

    crystal "Sumpah, gadis itu setengah putri duyung!"

    show old_crystal 1
    show player 17
    player_name "Hehe, ya mungkin..."

    show player 13
    return

label button_crystal_roxxys_mom:
    show old_crystal 1 with dissolve
    show player 10
    player_name "Jadi kamu {b}ibunya Roxxy{/b}?"

    show player 5
    show old_crystal 2
    crystal "Itu benar."

    crystal "Tidak bisakah kamu melihat kemiripannya?"

    show old_crystal 1
    menu:
        "Ya, saya kira.":
            show player 12
            player_name "Sekarang setelah kamu menyebutkannya, kalian berdua memang sangat mirip."

            show player 5
            show old_crystal 2
            crystal "Ya, dia benar-benar beruntung, mengejarku."

            crystal "Ayahnya jelek sekali!"

            show old_crystal 1
            player_name "..."
            show old_crystal 2b
            crystal "Ha ha ha!"

            show old_crystal 1
            jump roxmom_dialogue_repeat
        "Tapi kamu terlihat sangat muda!":
            show player 12
            player_name "Aku melihat kemiripannya tapi kamu terlihat terlalu muda untuk menjadi ibu {b}Roxxy{/b}."

            show player 10
            player_name "Apakah kamu yakin kamu bukan saudara perempuannya?"

            show player 5
            show old_crystal 2
            crystal "Nah sekarang, jika Anda tidak punya lidah perak!"

            crystal "Kurasa begitulah caramu tidak menarik perhatian putriku, ya?"

            show old_crystal 1
            show player 10
            player_name "Yah, aku-"

            show player 5
            show old_crystal 2
            crystal "Aku benci membocorkannya padamu, Romeo... Tapi butuh lebih dari sekadar pembicaraan mewah untuk mempertahankannya."

            crystal "Saya membesarkannya dengan benar, Anda paham?"

            crystal "Tunjukkan padanya bahwa nilai seorang pria terletak pada tindakannya dan bukan kata-katanya!"

            show old_crystal 1
            player_name "..."
            show old_crystal 2
            crystal "Jika kamu tidak bisa merawat gadisku dengan baik, sebaiknya kamu pergi saja, Nak."

            show old_crystal 1
            jump roxmom_dialogue_repeat
    return

label button_crystal_roxxy_busy:
    show player 29 with dissolve
    player_name "Apakah {b}Roxxy{/b} sibuk?"

    show player 3
    show old_crystal 6
    crystal "Psh, aku meragukannya..."

    crystal "... Dia mungkin ada di sana sambil mengoceh di telepon sialan itu."

    show old_crystal 5
    show player 12 with dissolve
    player_name "Jadi aku boleh masuk dan menemuinya?"

    show player 5
    show old_crystal 11
    crystal "... Kamu berharap aku menghentikanmu atau apalah?"

    show old_crystal 10
    show player 10
    player_name "aku tidak-"

    show player 11
    show old_crystal 6
    crystal "Astaga, Romeo."

    crystal "Tumbuhkan sepasang dan masuklah ke sana!"

    hide old_crystal
    hide player
    with dissolve
    return

label button_crystal_happy_home:
    show player 10
    player_name "Apakah kamu senang berada di rumah?"

    show player 5
    show old_crystal 2
    crystal "Sialan aku!"

    crystal "Tempat ini mungkin adalah tempat kumuh tapi jauh lebih hebat dari sel penjara itu, aku akan memberitahumu itu secara gratis!"

    crystal "Kurasa, aku harus berterima kasih padamu karena telah mengeluarkanku dari sana, ya?"

    show old_crystal 4 with dissolve
    show player 14
    player_name "Oh, tidak perlu, terima kasih. Saya dengan senang hati membantu."

    show player 13
    show old_crystal 2 with dissolve
    crystal "Heh, ya... Oke."

    crystal "Jika kamu berkata begitu, Romeo."

    crystal "Tawaran itu berlaku jika Anda berubah pikiran."

    crystal "Aku bisa BENAR-BENAR bersyukur...kalau kamu tahu maksudku?"

    show old_crystal 1
    show player 5
    player_name "{i}*Meneguk*{/i}"

    show old_crystal 2
    crystal "Hehehe."

    return

label button_crystal_should_go_evening:
    show player 14
    player_name "Aku mungkin harus masuk ke sana..."

    show player 13
    show old_crystal 6
    crystal "Ya, menurutku kamu benar tentang itu."

    crystal "Jaga baik-baik gadisku sekarang, dengar?"

    show old_crystal 5
    show player 14
    player_name "Ya, Bu."

    hide player with dissolve
    pause
    show old_crystal 6
    crystal "Hahaha, \"Bu\"..."

    crystal "Itu membunuhku setiap saat!"

    hide old_crystal with dissolve
    return

label button_crystal_should_go_day:
    show player 14
    player_name "Saya mungkin harus pergi dan mencari {b}Roxxy{/b}."

    show player 13
    show old_crystal 2
    crystal "Baiklah, kamu tidak perlu kabur sekarang..."

    crystal "... Aku dengan senang hati menemanimu sampai dia pulang."

    show old_crystal 1
    show player 14
    player_name "Hehe, tidak, tidak apa-apa. Aku benci menjadi pengganggu."

    show player 13
    show old_crystal 2
    crystal "Psh, tidak merepotkan."

    crystal "Saya tahu beberapa cara kita bisa menghabiskan waktu..."

    show old_crystal 1
    show player 3 with dissolve
    player_name "{i}*Meneguk*{/i}"

    show player 29
    player_name "Aku uhh... Sampai jumpa lagi, {b}Crystal{/b}."

    show player 3
    show old_crystal 2
    crystal "Cocokkan dirimu."

    hide player
    hide old_crystal
    with dissolve
    return

label button_crystal_she_here:
    show player 14
    player_name "Ya, apakah dia ada di sini?"

    show player 13
    show old_crystal 6
    crystal "Oh ya, dia ada di dalam..."

    show old_crystal 11
    crystal "Mungkin menyalak di ponselnya, seperti biasa."

    crystal "Jika aku tidak mengetahuinya, aku berani bersumpah benda itu menempel di sisi kepala gadis itu!"

    show old_crystal 5
    show player 17
    player_name "Hehe, ya."

    show player 13
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
