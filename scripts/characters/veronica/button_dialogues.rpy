label veronica_dialogue_pre_d05:
    show player 13 at left
    show vero
    with dissolve
    vero "Selamat datang di Consum-R, di mana semua kebutuhan Anda hanya berjarak dekat."

    vero "Apa yang bisa saya bantu hari ini?"

    return

label veronica_dialogue_pre_d11:
    show player 5 at left
    show vero
    vero "Selamat datang di {b}Consum-R{/b}, di mana semua kebutuhan Anda hanya-"

    vero "{b}[firstname]{/b}?"

    show player 12
    player_name "Hai {b}Veronica{/b}."

    show player 5
    vero "Apa yang membawamu hari ini?"

    return

label veronica_dialogue_pre_d20:
    show player 5 at left
    show vero
    with dissolve
    vero "Selamat datang di {b}Consum-R{/b}, di mana semua kebutuhan Anda hanya-"

    vero "Oh."

    vero f_sexy "Hai, tampan!"

    show player 10
    player_name "Hai {b}Veronica{/b}."

    show player 5
    vero "Apa yang membawamu hari ini?"

    return

label veronica_dialogue_vegatable_stock:
    show player 2
    show vero f_normal
    player_name "Saya {b}mencari stok sayuran{/b}. Apakah kalian punya?"

    show player 1
    vero "Saya khawatir kita semua terjual habis saat ini."

    show player 10
    player_name "Ya ampun..."

    show player 11
    vero "Apakah kaldu ayam akan berhasil? Kami punya banyak hal."

    show player 10
    player_name "Saya tidak tahu..."

    player_name "Apakah akan ada pengiriman segera atau bagaimana?"

    show player 11
    vero "Kami menerima pengiriman setiap hari tetapi saya tidak tahu kapan barang tersebut akan diisi ulang."

    show player 10
    player_name "Sial..."

    player_name "Baiklah, terima kasih."

    hide vero with dissolve
    show player 10 with dissolve
    player_name "Hmm, kurasa kaldu ayam cukup."

    show player 2
    player_name "Saya harus {b}membelinya dan membawanya ke Nona Okita{/b}."

    return

label veronica_dialogue_bug_spray:
    show player 4
    player_name "eh..."

    show player 12
    player_name "Saya mencari pestisida?"

    show vero f_laugh
    show player 1
    vero "Ah ya! Kami memiliki berbagai produk pengusir hama!"

    show vero f_normal
    show player 2
    player_name "Hmm... Bagaimana dengan serangga?"

    show vero f_thinking
    show player 1
    vero "Nah… Pestisida untuk serangga ada banyak jenisnya…"

    show vero f_normal
    show player 11
    vero "Tahukah Anda jenis bug apa yang Anda hadapi?"

    show player 10
    player_name "Saya tidak begitu yakin jenis apa itu..."

    show vero f_thinking
    show player 13
    vero "Nah, seperti apa bentuknya?"

    show vero f_normal
    return

label veronica_dialogue_bug_spray_large_wings:
    show player 35
    player_name "Ia memiliki satu set sayap besar..."

    show vero f_thinking
    show player 11
    vero "Hmm... Bisa jadi {b}belalang{/b}..."

    show vero f_laugh
    show player 1
    vero "Ambil kaleng semprot dengan {b}tutup merah{/b}. Ini disebut {b}Pembasmi Bug{/b}."

    show vero f_normal
    vero "Itu seharusnya berhasil!"

    show player 17
    player_name "Baiklah terima kasih!"

    return

label veronica_dialogue_bug_spray_pincers:
    show player 35
    player_name "Itu memiliki penjepit besar..."

    show vero f_thinking
    show player 11
    vero "Hmm... Bisa jadi {b}earwigs{/b}... Pengacau jahat!"

    show vero f_laugh
    show player 1
    vero "Ambil kaleng penyemprot dengan {b}tutup hijau{/b}. Ini disebut {b}Pembasmi Bug{/b}."

    show vero f_normal
    vero "Itu seharusnya berhasil!"

    show player 17
    player_name "Baiklah terima kasih!"

    return

label veronica_dialogue_bug_spray_white_spots:
    show player 35
    player_name "Ada bintik-bintik putih di cangkangnya..."

    show vero f_thinking
    show player 11
    vero "Hmm... Bisa jadi {b}kumbang{/b}..."

    show vero f_laugh
    show player 1
    vero "Ambil kaleng semprot dengan {b}tutup biru{/b}. Namanya {b}Pembasmi Bug{/b}."

    show vero f_normal
    vero "Itu seharusnya berhasil!"

    show player 17
    player_name "Baiklah terima kasih!"

    return

label veronica_dialogue_leave:
    show player 10 at left
    show vero f_normal
    player_name "Saya hanya melihat-lihat, terima kasih."

    show player 5
    vero "Tidak masalah."

    vero "Biar saya tahu jika Anda memerlukan bantuan apa pun."

    show player 10
    player_name "Akan dilakukan."

    hide player
    hide vero
    with dissolve
    return

label veronica_dialogue_what_do_you_sell:
    show player 10 at left
    show vero f_normal
    player_name "Apa yang kamu jual di sini?"

    show player 5
    vero @ f_laugh "Mungkin akan lebih cepat jika kami memberi tahu Anda barang-barang yang tidak kami jual."

    vero "Kami membawa hampir semua yang dibutuhkan seseorang untuk bertahan hidup."

    show player 10
    player_name "Jadi saya bisa membeli alat di sini?"

    show player 5
    vero "Tentu saja."

    show player 10
    player_name "Bagaimana dengan bahan makanan?"

    show player 5
    vero "Eh ya."

    show player 401
    player_name "Bagian komputer?!"

    show player 403
    vero "Kami mendapatkannya."

    show player 402
    player_name "Pakaian?"

    show player 403
    show vero
    vero @ f_laugh "Dalam semua ukuran."

    show player 402
    player_name "Peralatan dapur?!"

    show player 403
    vero "Lorong 12."

    show player 4 with dissolve
    player_name "Hmm."

    show player 401 with dissolve
    player_name "Bagaimana dengan sepeda?"

    show player 403
    show vero f_thinking
    vero "Sepeda gunung atau BMX?"

    show vero f_sexy
    vero "Karena kita punya keduanya."

    show player 402
    player_name "Wow, kalian benar-benar membawa semuanya."

    show player 403
    vero "Aku sudah bilang padamu."

    show vero f_normal
    return

label veronica_dialogue_you_look_nice:
    show player 14 at left
    show vero f_normal
    player_name "Kamu terlihat cantik hari ini."

    show player 13
    show vero f_eyeroll
    vero "Hentikan."

    show vero f_sexy_down
    vero "Tidak ada seorang pun yang terlihat cantik mengenakan seragam konyol ini..."

    show vero f_sexy
    show player 10
    player_name "Anda melakukannya."

    show player 5
    vero "Aww, manis sekali ucapanmu."

    vero "Bahkan jika aku tidak mempercayaimu."

    vero "Terima kasih, {b}[firstname]{/b}."

    show player 10
    player_name "Terima kasih kembali."

    show player 5
    return

label veronica_dialogue_spoken_with_diane_lately:
    show player 10 at left
    show vero f_normal
    player_name "Apakah Anda pernah berbicara dengan {b}Diane{/b} akhir-akhir ini?"

    show player 5
    vero "Ya, melalui telepon."

    vero "Saya sangat ingin mempelajari lebih lanjut tentang bisnis sampingan yang dia jalani!"

    vero "Anda tahu sesuatu tentang hal itu?"

    show player 10
    player_name "T-tidak."

    player_name "Tidak apa-apa."

    show player 5
    show vero f_sexy
    vero "Oh, ayolah!"

    vero "Anda bisa memberitahu saya."

    show player 14
    player_name "Hehe, aku benar-benar tidak tahu apa-apa tentang itu!"

    show player 10
    player_name "Maaf."

    show player 5
    show vero f_eyeroll
    vero "{i}*Huh*{/i} Sungguh membuatku tidak menyadarinya!"

    show vero f_normal
    show player 10
    player_name "Saya yakin {b}Diane{/b} akan segera menceritakan semuanya kepada Anda."

    show player 5
    vero "Saya harap begitu."

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
