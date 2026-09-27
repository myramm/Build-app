label mrsj_button_yoga_room_dialogue_pre_first:
    show player 1 at left
    show mrsj 10 at right
    with dissolve
    player_name "Umm-"

    show player 11 at left
    window hide
    pause
    player_name "..."
    show mrsj 11 at right
    window hide
    pause
    show mrsj 12 at right
    window hide
    pause
    show mrsj 13 at right with hpunch
    mrsj "Oh!"

    show player 18 at left
    mrsj "... {b}[firstname]{/b}?"

    show mrsj 14 at right
    show player 17 at left
    player_name "Hai, {b}Ny. Johnson{/b}!"

    show mrsj 17 at right
    show player 1 at left
    mrsj "Apa yang kamu lakukan di sini?"

    show mrsj 14 at right
    show player 29 at left
    player_name "Aku... Melihatmu dari {b}Gym{/b} utama!"

    player_name "Saya datang hanya untuk menyapa!"

    show player 13 at left
    show mrsj 18 at right
    mrsj "Manis sekali!"

    show mrsj 17 at right
    mrsj "Jadi kamu sedang berolahraga sekarang, ya?"

    show mrsj 14 at right
    show player 21 at left
    player_name "Ha ha. Ya..."

    player_name "... Baru saja mulai berlatih untuk menjadi bugar!"

    show mrsj 19 at right
    show player 11 at left
    mrsj "Dan saya yakin Anda akan menjadi baik dan {i}keras{/i}-"

    mrsj "..."
    show player 13 at left
    show mrsj 18 at right
    mrsj "Maksudku, {b}kuat{/b}!"

    show mrsj 14 at right
    show player 17 at left
    player_name "Saya harap begitu..."

    show mrsj 17 at right
    show player 1 at left
    mrsj "Ngomong-ngomong, adakah yang ingin kamu bicarakan?"

    return

label mrsj_button_yoga_room_dialogue_pre_repeat:
    show player 14 at left
    show mrsj 14 at right
    with dissolve
    player_name "Hai, {b}Ny. Johnson{/b}!"

    show player 1 at left
    show mrsj 17 at right
    mrsj "Hai, {b}[firstname]{/b}!"

    show player 11 at left
    show mrsj 18 at right
    mrsj "Anda mulai terlihat bugar, anak muda!"

    show player 29 at left
    show mrsj 14 at right
    player_name "Oh. Terima kasih..."

    player_name "Jadi, apakah kamu..."

    show player 1 at left
    show mrsj 17 at right
    mrsj "Apakah ada sesuatu yang ingin Anda bicarakan?"

    return

label mrsj_button_yoga_room_dialogue_hows_erik:
    show player 10 at left
    show mrsj 14 at right
    player_name "Bagaimana kabar {b}Erik{/b} hari ini?"

    player_name "Saya jarang melihatnya."

    show mrsj 18 at right
    show player 5 at left
    mrsj "Yah... Kamu tahu bagaimana keadaannya!"

    mrsj "Dia hanya menyukai video game-nya..."

    show player 10 at left
    show mrsj 14 at right
    player_name "Ya, tapi akhir-akhir ini keadaannya menjadi lebih buruk."

    player_name "Aku bahkan tidak menerima pesan teks darinya..."

    show mrsj 19 at right
    show player 5 at left
    mrsj "..."
    show mrsj 20 at right
    show player 11 at left
    mrsj "Anda tahu, menurut saya dia mengalami masalah dalam menyesuaikan diri dengan kehidupannya sendiri."

    mrsj "Saya khawatir tentang dia."

    show mrsj 19 at right
    show player 12 at left
    player_name "Saya tidak tahu."

    show mrsj 20 at right
    show player 11 at left
    mrsj "Dia tidak terbiasa menjadi tuan rumah."

    mrsj "... Dan dia mengalami kesulitan dengan perempuan."

    show mrsj 19 at right
    mrsj "Yang malang pasti kesepian."

    show mrsj 14 at right
    show player 21 at left
    player_name "... Ya. Saya rasa saya mengerti."

    show mrsj 18 at right
    show player 13 at left
    mrsj "Untung dia punya teman setia sepertimu, {b}[firstname]{/b}!"

    mrsj "Dia membutuhkanmu."

    show mrsj 14 at right
    show player 17 at left
    player_name "Yah, kami selalu berteman jadi..."

    show mrsj 18 at right
    show player 1 at left
    mrsj "Aku akan menyuruhnya untuk mengirimimu pesan lebih sering!"

    show mrsj 14 at right
    show player 14 at left
    player_name "Tidak apa-apa, aku hanya ingin memastikan dia baik-baik saja."

    show mrsj 17 at right
    show player 1 at left
    mrsj "Apakah ada hal lain yang ingin Anda bicarakan?"

    return

label mrsj_button_yoga_room_dialogue_poker:
    show mrsj 14 at right
    show player 14 at left
    player_name "Saya ingin tahu apakah Anda ingin bergabung dengan {b}Erik{/b} dan saya untuk bermain poker?"

    show player 1
    show mrsj 17
    mrsj "Saya tidak bisa sekarang, saya harus mengajar kelas..."

    mrsj "Tapi aku berada di kamarku hampir setiap {b}malam hari{/b}, kalau begitu tanyakan lagi padaku."

    show player 18
    show mrsj 14
    player_name "Terima kasih, {b}Ny. Johnson{/b}, saya akan melakukannya!"

    return

label mrsj_button_yoga_room_dialogue_what_was_that:
    call expression game.dialog_select("mrsj_button_yoga_room_dialogue_what_was_that_pre")
    if M_anna.is_state(S_anna_start):
        call expression game.dialog_select("mrsj_button_yoga_room_dialogue_what_was_that_anna_intro")
        $ M_anna.trigger(T_anna_intro)
    call expression game.dialog_select("mrsj_button_yoga_room_dialogue_what_was_that_after")
    return

label mrsj_button_yoga_room_dialogue_what_was_that_pre:
    show mrsj 14 at right
    show player 14 at left
    player_name "Apa pose yoga yang Anda lakukan sebelumnya?"

    show mrsj 13 at right
    show player 13 at left
    show player 1 at left
    mrsj "Oh, akan kutunjukkan padamu!"

    show mrsj 12 at right
    show player 11 at left
    mrsj "Anda mulai seperti ini!"

    show mrsj 11 at right
    window hide
    pause
    show player 21 at left
    show mrsj 10 at right
    window hide
    pause
    mrsj "Berlutut!"

    window hide
    pause
    show player 21 at left
    player_name "Uhhh..."

    player_name "... Ya..."

    show player 11 at left
    mrsj "Ini disebut \"Kucing Sapi\"!"

    show mrsj 11 at right
    window hide
    pause
    show mrsj 12 at right
    window hide
    pause
    show mrsj 13 at right
    show player 18 at left
    mrsj "Tidak buruk, bukan?"

    return

label mrsj_button_yoga_room_dialogue_what_was_that_anna_intro:
    show old_anna 12f at Position (xpos=600)
    show mrsj 13 at right
    show player 13
    with dissolve
    anna "Halo, {b}Tammy{/b}."

    show old_anna 5f
    anna "Jangan bilang kamu memulainya tanpa aku."

    show old_anna 4f
    show mrsj 18
    mrsj "Tentu saja tidak! Saya baru saja ngobrol dengan teman penyewa saya, {b}Erik{/b}!"

    show old_anna 11 at Position (xpos=700) with dissolve
    show mrsj 17b
    mrsj "{b}Anna{/b}, ini {b}[firstname]{/b}. {b}[firstname]{/b}, ini temanku, {b}Anna{/b}."

    show mrsj 14
    show player 36 with dissolve
    player_name "Hai!"

    show player 13 with dissolve
    show mrsj 14b
    show old_anna 12
    anna "Anda adalah teman {b}Erik{/b}?"

    show old_anna 11
    show player 14
    show mrsj 14
    player_name "Ya. Kami sudah berteman sejak lama."

    show player 12
    player_name "Apakah Anda juga seorang pelatih di sini?"

    show player 5
    show old_anna 2 with dissolve
    show mrsj 14b
    anna "Oh tidak. Saya hanya seorang pelajar."

    show old_anna 1
    show player 13
    show mrsj 17
    mrsj "{b}Anna{/b} adalah salah satu yang terbaik. Dia bisa mengajar di sini jika dia mau!"

    show mrsj 14b
    show old_anna 3
    anna "Ah, menurutku tidak! Ha ha!"

    show old_anna 2
    anna "Dia seorang guru yang hebat dan saya hanyalah seorang pemula."

    show old_anna 1
    show mrsj 17
    mrsj "{b}Anna{/b}, hanya bersikap rendah hati."

    show mrsj 17b
    mrsj "Dia mungkin seorang pemula, tapi dia sangat berbakat... Dan sangat fleksibel."

    show mrsj 14b
    show old_anna 3
    anna "Haha."

    show old_anna 2
    anna "Aku harus pergi sekarang dan bersiap untuk pelajaran berikutnya."

    show old_anna 3
    anna "Selamat tinggal, {b}Tammy{/b}!"

    show old_anna 1
    show mrsj 17b
    mrsj "Sampai berjumpa lagi."

    show mrsj 14b
    show old_anna 2
    anna "Senang bertemu dengan Anda, {b}[firstname]{/b}."

    show old_anna 1
    show player 14
    show mrsj 14
    player_name "Selamat tinggal!"

    hide old_anna with dissolve
    return

label mrsj_button_yoga_room_dialogue_what_was_that_after:
    show mrsj 17 at right
    show player 1 at left
    mrsj "Apakah ada hal lain yang ingin Anda bicarakan?"

    return

label mrsj_button_yoga_room_dialogue_youre_so_fit:
    show mrsj 14 at right
    show player 29 at left
    player_name "Saya harus mengatakan, {b}Ny. Johnson{/b}, kamu benar-benar bugar!"

    player_name "Apakah Anda banyak berolahraga?"

    show mrsj 18 at right
    show player 13 at left
    mrsj "Ah... Kamu baik sekali!"

    show mrsj 17 at right
    mrsj "Ya, saya datang ke sini sesering mungkin dan mencoba menggunakan gym..."

    mrsj "... Saya juga pergi jogging! Dan saya juga melakukan yoga di kamar saya pada malam hari..."

    show mrsj 19 at right
    show player 21 at left
    player_name "Ya, itu berhasil!"

    show player 13 at left
    mrsj "Menurutmu?"

    show mrsj 15 at right
    show player 11 at left
    mrsj "Bokongku masih agak besar..."

    show mrsj 16 at right
    show player 23 at left
    mrsj "... Dan payudaraku tidak seperti dulu lagi..."

    player_name "..."
    show player 28 at left
    show mrsj 19 at right
    player_name "{i}*Meneguk*{/i}"

    show player 1 at left
    show mrsj 18 at right
    mrsj "Apakah ada hal lain yang ingin Anda bicarakan?"

    return

label mrsj_button_yoga_room_dialogue_have_to_train:
    show mrsj 14 at right
    show player 14 at left
    player_name "Saya harus kembali ke pelatihan saya!"

    show mrsj 18 at right
    show player 1 at left
    mrsj "Baiklah kalau begitu!"

    show mrsj 14 at right
    show player 17 at left
    player_name "Sampai jumpa, {b}Ny. Johnson{/b}!"

    hide player 17 at left with dissolve
    hide mrsj 14 at right with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
