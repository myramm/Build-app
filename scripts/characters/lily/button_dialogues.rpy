label lily_dialogue_pre:
    scene expression player.location.background_closeup with None
    show xtra 17 zorder 2
    show lily zorder 1
    show player 1 zorder 3 at left
    with dissolve
    lily "Ada apa?"

    return

label lily_dialogue_familiar:
    show player 4
    player_name "Aku merasa seperti aku pernah melihatmu di suatu tempat."

    show lily f_laugh
    show player 1
    lily "Benar. Nah, Anda mungkin pernah melihat saya di internet..."

    show lily f_normal
    lily "Saya melakukan banyak {b}streaming video game{/b} dan mempostingnya di {b}saluran GooTube{/b} saya."

    show lily f_sexy
    lily "Saya biasanya menggunakan nama {b}VirginLily69{/b}."

    show player 17
    player_name "Oh benar! Temanku {b}Erik{/b} menyukai barang-barangmu!"

    show player 21
    player_name "Dia terus berbicara tentang video Anda dan {b}besar{/b} Anda... Err... Basis penggemar!"

    show lily f_laugh
    show player 1
    lily "Aww... Kalian manis sekali."

    show lily f_normal
    lily "Apakah ada hal lain yang ingin Anda bicarakan?"

    return

label lily_dialogue_suggestions:
    show player 2
    player_name "Apakah Anda punya saran? Produk baru yang Anda rekomendasikan?"

    show player 1
    lily @ -m_talk "Hmm..."

    show lily f_normal
    lily "Yah, aku sangat suka cosplay!"

    show lily f_sexy
    lily "Saya suka memakai {i}pakaian seksi{/i}. Sebenarnya, kami mempunyai rangkaian kostum baru yang baru saja hadir!"

    show player 21
    player_name "Oh ya? Kedengarannya menarik..."

    show player 1
    lily "Terkadang sulit untuk memasukkan... Umm... Formulirku ke dalamnya."

    lily "Mereka membuatnya sangat ketat, Anda tahu?"

    lily @ f_laugh "Tapi para pria biasanya tidak keberatan!"

    show player 29
    player_name "Ha ha. Jadi begitu."

    show player 2
    player_name "Terima kasih, saya akan melihatnya."

    show lily f_normal
    return

label lily_dialogue_leave:
    show player 2
    player_name "Ya, saya pikir saya memiliki semua yang saya butuhkan. Terima kasih!"

    show lily f_normal
    show player 1
    lily "Besar! Terima kasih telah berbelanja di {b}Cosmic Cumics{/b}..."

    show lily f_laugh
    show player 13
    lily "Dan beri tahu teman Anda tentang kami!"

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
