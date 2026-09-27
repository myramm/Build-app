label larry_msg_request:
    scene police_cell
    show larry 15 at Position (xpos=351)
    show cell_bars at left
    show larry_hands at Position (xpos=400,ypos=658)
    show player 5f at right with dissolve
    larry "Hai! Anda!"

    show larry 14
    show player 11f
    player_name "!!!"
    show player 12f
    player_name "Umm... Ya?"

    player_name "Apa yang kamu inginkan?"

    show player 16f
    show larry 15
    larry "Dengar, aku tidak marah padamu atas perbuatanmu."

    larry "Saya pantas mendapatkan ini."

    show larry 14
    show player 5f
    player_name "..."
    show larry 15
    larry "Saya tahu apa yang saya lakukan itu buruk, oke?"

    larry "Saya hanya... Saya berharap Anda akan memberikan {b}Tammy{/b} pesan dari saya?"

    show larry 14
    show player 10f
    player_name "Aku tidak yakin itu ide yang bagus..."

    show player 5f
    show larry 15
    larry "Aku ingin kamu memberitahunya bahwa aku minta maaf!"

    larry "aku minta maaf untuk semuanya..."

    show larry 14
    show player 12f
    player_name "Saya tidak tahu apakah saya harus melakukannya."

    show player 5f
    show larry 15
    larry "Silakan!"

    larry "Aku... aku bisa membantumu!"

    show larry 14
    show player 10f
    player_name "Hah?"

    show player 11f
    show larry 15
    larry "Saya menyembunyikan tas penuh barang curian yang saya ambil."

    larry "Aku akan memberitahumu di mana tempatnya jika kamu memberitahu {b}Tammy{/b} aku minta maaf."

    larry "Aku hanya tidak ingin dia membenciku selamanya, tahu?"

    larry "Seharusnya aku tidak meninggalkannya..."

    show larry 14
    show player 34f
    player_name "..."
    show larry 15
    show player 5f
    larry "Anda dapat mengembalikan barang curian tersebut ke polisi, atau menyimpannya! Saya tidak peduli."

    larry "Hanya, tolong katakan padanya aku minta maaf..."

    larry "Mudah-mudahan, dia bisa menemukan dalam hatinya untuk memaafkanku suatu hari nanti..."

    show larry 14
    show player 35f
    player_name "Hmm..."

    show player 12f
    player_name "Saya kira saya bisa. Saya akan melihat apa yang bisa saya lakukan."

    show player 5f
    show larry 15
    larry "Terima kasih nak!"

    hide player with dissolve
    hide larry
    hide cell_bars
    hide larry_hands
    return

label larry_msg_prompt:
    scene police_cell
    show larry 14 at Position (xpos=351)
    show cell_bars at left
    show larry_hands at Position (xpos=400,ypos=658)
    show player 12f at right with dissolve
    player_name "Apa yang kamu ingin aku lakukan lagi untukmu?"

    show player 5f
    show larry 15
    larry "Katakan saja pada {b}Tammy{/b} bahwa saya minta maaf. Seharusnya aku tidak meninggalkannya..."

    larry "Jika ya, saya akan memberi tahu Anda di mana saya menyembunyikan semua barang yang saya curi."

    show larry 14
    show player 10f
    player_name "Saya akan melihat apa yang bisa saya lakukan."

    hide player with dissolve
    hide larry
    hide cell_bars
    hide larry_hands
    return

label larry_msg_reward:
    scene police_cell
    show larry 15 at Position (xpos=351)
    show cell_bars at left
    show larry_hands at Position (xpos=400,ypos=658)
    show player 5f at right with dissolve
    larry "Hai! Itu kamu lagi!"

    larry "Apakah Anda mendapat kesempatan untuk berbicara dengan {b}Tammy{/b}?"

    show larry 14
    show player 12f
    player_name "Saya menyampaikan pesan itu."

    show player 5f
    show larry 15
    larry "Dan apa... Apa yang dia katakan?!"

    show larry 14
    show player 12f
    player_name "Dia tidak melakukannya! Dengar, kawan... Dia menerima pesan seperti yang kamu inginkan."

    show player 10f
    player_name "Anda tidak mengatakan apa pun tentang membawakan Anda pesan kembali!"

    show player 5f
    larry "..."
    show larry 15
    larry "Ya, kamu benar. Maaf."

    larry "Anda menahan tawaran Anda."

    larry "... Baiklah."

    larry "Tentang barang curian yang kusembunyikan."

    larry "Mereka berada {b}di balik semak di taman, di samping pohon putih{/b}."

    show larry 14
    show player 34f
    player_name "Hmm..."

    show player 12f
    player_name "Oke, aku akan pergi melihatnya."

    show player 5f
    show larry 15
    larry "Mendengarkan! Saya akan mencoba mengubah hidup saya!"

    larry "Anda akan lihat!"

    larry "Dan mungkin... Suatu hari nanti... {b}Tammy{/b} akan membawaku kembali!"

    show larry 14
    show player 12f
    player_name "Kita lihat saja nanti."

    show player 5f
    show larry 15
    larry "Terima kasih..."

    hide player with dissolve
    hide larry
    hide cell_bars
    hide larry_hands
    return

label larry_msg_repeat:
    scene police_cell
    show larry 14 at Position (xpos=351)
    show cell_bars at left
    show larry_hands at Position (xpos=400,ypos=658)
    show player 12f at right with dissolve
    player_name "Di mana Anda menyembunyikan barang curian tersebut?"

    show player 5f
    show larry 15
    larry "Mereka berada {b}di balik semak di taman, di samping pohon putih{/b}."

    show larry 14
    show player 12f
    player_name "Oke, aku akan pergi melihatnya."

    hide player with dissolve
    hide larry
    hide cell_bars
    hide larry_hands
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
