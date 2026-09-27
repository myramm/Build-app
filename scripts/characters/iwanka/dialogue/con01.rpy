label con01_init_iwanka:
    anon f_worried "Bolehkah saya bertanya sesuatu?"

    iwanka f_annoyed "Ini bukan tentang ayahku lagi, kan?"

    anon "T-tidak, bukan seperti itu..."

    anon "Kuharap aku bisa berbicara denganmu tentang pembantu yang bekerja di bawah?"

    iwanka @ f_eyeroll "Pembantu itu?"

    anon "Ya."

    iwanka "Saya mencoba untuk tidak bersosialisasi dengan bantuan..."

    pause
    anon "Hanya saja, orang tuamu agak kejam padanya, dan aku berharap-"

    iwanka f_bored "Aku harus jujur padamu saat ini, {b}[firstname]{/b}, ini sungguh membosankan..."

    anon "Oh."

    pause
    anon @ a_behind_head "Hmm..."

    iwanka f_suspicious "Hei, pernahkah kamu berpikir untuk memperbarui penampilanmu?"

    anon f_confused "Hah?"

    iwanka f_normal "Maksudku, penampilan yang kamu kembangkan ini... Yah, lucu.. kurasa..."

    iwanka "... Dalam arti tertentu, batak menaiki rel."

    anon f_unimpressed "{b}Iwanka{/b}, saya sangat ingin kembali ke masalah {b}Consuela{/b} ini..."

    iwanka "Ya, ya, ya... Tunggu sebentar sementara aku mengerjakan sihirku!"

    iwanka f_thinking "Hmm."

    iwanka f_smirk "Saya pikir Anda akan terlihat AMA-ZING di beberapa Huge-Go Boss atau Coochie!"

    iwanka "Apakah ada tempat untuk membeli merek-merek tersebut di sekitar sini?"

    anon "Eh, tidak."

    iwanka @ f_eyeroll "Eh, tentu saja tidak ada!"

    iwanka f_annoyed "Kota ini seperti penjara yang menakutkan..."

    iwanka "... Omong kosong di planet ini."

    anon f_worried @ -m_talk "Kamu tidak akan membantuku, kan?"

    iwanka f_thinking "Saya ingin tahu apakah ada produk yang setara di luar merek?"

    anon f_sad_down "{i}*Huh*{/i} Lupakan saja."

    iwanka "Mungkin kami bisa memesankan Anda sesuatu secara online?"

    hide anon with {'master': dissolve}
    iwanka f_excited "Saya pikir Barmani melakukan penjualan online."

    iwanka @ f_laugh "Seperti, oh ya ampun!"

    iwanka "Kalau ada cowok ganteng masuk pakai Barmani... Celana dalamku langsung jatuh ke lantai!"

    iwanka @ f_laugh "Hehe, tahu maksudku?"

    iwanka f_normal @ -m_talk "Hmm?"

    iwanka f_suspicious "Kemana dia pergi?"

    hide anon with dissolve

    $ player.go_to(L_rump_lobby)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
