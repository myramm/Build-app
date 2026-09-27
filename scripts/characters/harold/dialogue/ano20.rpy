label ano20_cops_harold:
    show expression background(760, 386, 4.) as stage
    show harold f_surprised
    show anon with dissolve:
        xoffset -100
    harold "{b}[firstname]{/b}?"

    harold f_concerned "Apa yang kamu lakukan di sini selarut ini?"

    anon "Aku punya sesuatu untukmu."

    harold f_suspicious "Untukku?"

    show anon f_looking_down a_backpack with dissolve
    pause
    show anon a_recorder_give_cashless f_normal with dissolve
    harold f_surprised @ -m_talk "!!!"
    anon "Ini adalah bukti yang membuktikan {b}Walikota Rump{/b} bekerja sama dengan Rusia."

    show harold a_recorder_cashless
    show anon a_idle
    with dissolve
    harold "Apa yang-"

    harold "Dimana kamu mendapatkan ini?"

    anon "Saya menemukannya di kantor {b}Walikota Rump{/b}."

    harold f_suspicious "Hah?!"

    harold "Bagaimana kamu bisa masuk ke kantor pribadi walikota?"

    anon "Apakah itu penting?"

    harold f_angry "Tentu saja itu penting!"

    show anon f_worried
    harold "Jika {b}Pantat{/b} berada di tempat tidur dengan orang Rusia seperti yang kami duga, maka Anda harus menjauhi dia."

    harold "Anda akan terbunuh, {b}[firstname]{/b}!"

    anon f_angry "Bisakah Anda melihat buktinya saja?!"

    harold @ -m_talk "..."
    harold f_surprised_down "Benda apa ini?"

    anon f_worried @ a_point "Folder di sana penuh dengan laporan bank untuk sekitar selusin rekening luar negeri."

    anon "Berdasarkan jumlah tersebut, menurut saya, kemungkinan besar dia akan mempertahankan bagian keuntungannya."

    harold f_suspicious "Keuntungan apa?"

    anon "Anda tahu, bagiannya dari apa pun yang dijajakan orang Rusia."

    harold @ -m_talk "Hmm."

    anon "Ada juga banyak akta properti di sini di Summerville."

    anon "Termasuk gudang yang Anda jelajahi tadi malam."

    harold f_surprised "Tunggu sebentar, {b}Rump{/b} pemilik tempat itu?!"

    anon @ -m_talk "Mhmm."

    harold f_concerned "Saya memberi tahu {b}Earl{/b} bahwa nama perusahaan terdengar palsu..."

    harold a_recorder_listen_cashless f_suspicious "... Bagaimana dengan ini?"

    anon "Ini adalah rekaman {b}Rump{/b} dan percakapan orang Rusia."

    anon "Di dalamnya, Anda akan mendengar bos mafia mengaku membunuh dua wanita dan {b}Rump{/b} menertawakannya."

    harold f_concerned "Kamu serius?"

    anon f_angry "Kemudian mereka mendiskusikan pembunuhan ayahku."

    harold @ f_surprised "!!!"
    harold "Itu-"

    pause
    harold "Yesus, Nak..."

    harold "Apakah Anda menemukan hal lain?"

    show anon f_worried

    $ renpy.dynamic(rv=None)
    menu:
        "Ceritakan padanya tentang uang itu. {color=7ff7}[[Honest]{/color}":
            anon "Saya menemukan ini juga."

            show anon a_recorder_give_cash with dissolve
            pause
            show harold a_recorder f_surprised_down
            show anon a_idle
            with dissolve
            harold "Wah, itu uang tunai yang banyak."

            show harold f_concerned
            anon "Ya."

            anon "Beberapa dari hasil haramnya tidak diragukan lagi."

        "Tidak, itu segalanya. {color=f77b}[[Dishonest]{/color}":

            $ rv = True
            anon f_thinking a_thinking @ -m_talk "(Hmm.)"

            anon @ -m_talk "(Tidak ada alasan saya tidak menyimpan uang ini, kan?)"

            anon @ -m_talk "(Maksudku, tidak ada gunanya bagi siapa pun untuk duduk di ruang bukti...)"

            anon f_shy a_behind_head "Eh, tidak."

            anon "Itu semua yang saya temukan."


    anon a_idle "Jumlahnya cukup untuk melakukan penangkapan, bukan?"

    harold "Jika semuanya sudah diperiksa, maka ya."

    harold "Tunggu di sini sebentar sementara aku menyampaikan ini pada bosku, oke?"

    anon "Ya baiklah."

    hide harold
    show anon:
        flip
        xoffset -600
    with dissolve
    harold "Hei {b}Yumi{/b}, bisakah kamu menjaga anak itu sebentar?"

    yumi "Tentu saja, bos."

    show yumi f_concerned with dissolve:
        xoffset -50
    pause
    show anon with dissolve:
        unflip
        xoffset -100
    yumi "Astaga, sepertinya kamu mengalami malam yang berat..."

    pause
    yumi "Lagipula, apa yang kamu lakukan di sini?"

    anon @ f_sad_down "{i}*Huh*{/i} Ceritanya panjang."

    pause
    yumi "Ada hubungannya dengan kasus ayahmu?"

    anon "Ya."

    yumi f_suspicious "Anda tidak mengintip orang-orang Rusia itu lagi, bukan?"

    anon "Tidak."

    yumi f_concerned "Anda sebaiknya tidak melakukannya!"


    if False:
        yumi f_normal @ f_wink "Aku akan memborgolmu ke tempat tidurku dan menyanderamu sampai semua ini selesai..."

        show anon f_surprised
        yumi "Tidakkah menurutmu aku tidak akan melakukannya!"

        anon "Itu-"

        pause
        anon f_normal @ f_laugh "Sebenarnya tidak terdengar terlalu buruk."

        yumi @ f_laugh "Hehe, diamlah!"

    else:

        yumi "Orang-orang itu akan membunuhmu, {b}[firstname]{/b}!"

        yumi "Kurasa aku tidak bisa menghadapi induk semangmu jika itu terjadi..."

        anon "Baiklah, kamu bisa santai."

        anon "Aku belum pernah mendekati mereka sejak kalian menangkapku di gudang."


    yumi f_normal "Kami membuat kemajuan, Anda tahu?"

    anon f_normal @ f_surprised "Oh?"

    yumi "{b}Harold{/b} mampu mengidentifikasi bos mafia."

    anon @ -m_talk "..."
    yumi "{b}Raznikov Putin Chernyshevsky{/b}."

    yumi @ f_eyeroll "Tapi dia singkatnya {b}Raz{/b}."

    anon f_surprised "Tunggu sebentar..."

    anon "Biar kutebak."

    anon f_worried "Pria pendek?"

    anon "Agak terlihat seperti goblin pucat?"

    yumi f_suspicious "Bagaimana Anda mengetahui hal itu?"

    anon "Tebakan yang beruntung."

    yumi f_concerned "Ada sesuatu yang tidak kamu beritahukan padaku!"

    anon f_surprised a_sides "Tidak."

    pause
    yumi "Ya, ada!"

    yumi "Ayo, tumpahkan."

    anon f_worried @ -m_talk "..."

    if False:
        yumi f_concerned "Itu dia, aku akan memborgolnya!"

        anon @ f_laugh "Heh, baiklah... Hanya-"

    else:

        yumi "Apakah saya perlu membawa Anda ke interogasi?!"

        anon @ f_confused "Hah?"

        yumi "Aku tidak suka disimpan-"


    harold "{b}Yumi{/b}, aku ingin kamu mengambil perlengkapan kita dan membawanya ke dalam mobil."

    show anon with dissolve:
        flip
        xoffset -600
    yumi @ -m_talk "Hmm?"

    show anon:
        unflip
        xoffset -100
    show harold behind anon:
        flip
        xoffset 175
    with dissolve
    yumi f_suspicious "Apa yang terjadi, bos?"

    harold "Ketua baru saja memberi wewenang padaku untuk membawa {b}Rump{/b} ke dalam tuduhan."

    yumi f_surprised "Apakah kamu serius?"

    harold "Ya, cepatlah."

    yumi "Y-ya, tuan!"

    hide yumi with dissolve
    pause
    show harold with dissolve:
        unflip
        xoffset -200
    harold f_concerned "Bisakah kamu pulang sendiri dengan baik?"

    anon f_worried a_idle "Baiklah, tunggu sebentar... bolehkah aku ikut denganmu?"

    harold f_concerned "Tidak, kamu tidak boleh ikut dengan kami!"

    anon "Kenapa tidak?!"

    harold "Ini urusan polisi, {b}[firstname]{/b}..."

    harold "Kita tidak bisa membiarkan warga sipil ikut serta demi kesenangan pribadi mereka."

    anon f_angry "Hei, kalau bukan karena buktiku kamu tidak akan-"

    harold "Saya tidak akan berdebat dengan Anda tentang hal ini."

    anon "Bagaimana dengan Rusia?!"

    anon "Anda akan menangkap mereka juga, kan?!"

    harold "Saya tidak tahu, oke?"

    harold "Kita bisa mendiskusikannya besok."

    harold "Untuk saat ini, bisakah kamu pulang saja dan biarkan kami melakukan pekerjaan kami?!"

    anon "Ya, baiklah... Terserah."

    harold "Terima kasih!"

    hide harold with dissolve
    pause
    anon f_disgusted @ -m_talk "(Yah, setidaknya mereka akhirnya melakukan sesuatu...)"

    anon @ -m_talk "(Saya kira tidak ada yang bisa saya lakukan selain pulang dan menunggu.)"

    hide anon with dissolve
    return rv
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
