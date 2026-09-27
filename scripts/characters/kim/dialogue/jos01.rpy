label jos01_find_kim:
    show kim:
        xoffset 100
    show rump f_angry:
        flip
        xoffset 200
    with fade
    rump "Anda ingin memberi tahu saya mengapa saya mendapat telepon dari rekan saya yang mengatakan Anda tidak menghormati putrinya?"

    kim f_curious @ -m_talk "Hmm?"

    rump "Dia bilang dia datang ke sini beberapa hari yang lalu, ingin membeli mobil, dan kamu tidak mau membantunya?"

    kim f_normal "Itu tidak benar!"

    kim "Saya terr padanya, dia ingin mobil custom, saya harus memesannya."

    kim "Ambil beberapa minggu sebelum datang."

    rump f_normal @ a_hand "Ya, tapi dia bilang kamu sangat kasar padanya..."

    kim f_angry "Ck, dia bayi besar!"

    kim "Membuat ulah di toko, saya tidak punya waktu untuk mengganti popok rittre girr!"

    kim f_smirk @ f_laugh a_rub "Huehuehue!"

    rump f_angry @ a_finger "Ini bukan bahan tertawaan, {b}Kim{/b}."

    show kim f_normal
    rump "Rekan saya adalah orang yang sangat serius dan dia tidak menanggapi rasa tidak hormat dengan baik."

    rump "Dia pasti mengirim orang ke sini untuk mencelakakanmu, kalau saja aku tidak turun tangan."

    kim f_angry @ f_baby_cry "Apa?!"

    kim "Mereka mengancam {b}Kim{/b}?!"

    rump f_normal "Anda beruntung telah membuktikan diri Anda sebagai aset berharga sejauh ini."

    rump "Tapi saya peringatkan Anda sekarang, Anda jauh dari tak tergantikan."

    rump "Apakah kamu mengerti?"

    kim f_normal "Ya, ya... {b}Kim{/b} mengerti."

    kim @ a_wave "Maksudku, tidak ada rasa tidak hormat."

    rump "Gadis itu akan kembali ke sini minggu depan dan Anda AKAN memiliki mobil yang menunggunya, bersama dengan permintaan maaf."

    rump "Apakah saya memperjelas diri saya?"

    kim "Y-ya, tentu saja, {b}Pak. pantat{/b}!"

    kim "{b}Kim{/b} menyiapkan mobil dan membuat permintaan maaf besar-besaran."

    rump "Sangat bagus."

    pause
    rump "Sekarang semuanya sudah beres, saya ingin berbicara dengan Anda tentang meningkatnya kebutuhan perusahaan kami di Summerville."

    rump "Mengapa kamu tidak mampir ke rumahku nanti malam dan kita akan membahas detailnya, hmm?"

    rump f_smirk "Ajaklah istrimu yang cantik itu... Kita semua akan berendam di bak mandi air panas."

    kim f_smirk "Wirr {b}Ny. Rump{/b} akan bergabung dengan kami?"

    rump "Pastinya."

    kim "Oh, {b}Kim{/b} seperti suara itu..."

    kim "Kami datang."

    rump "Luar biasa."

    rump "Aku akan memberi tahu pengawalku bahwa kamu diharapkan."

    show rump f_normal with dissolve:
        unflip
        xoffset -400
    pause
    show rump with dissolve:
        flip
        xoffset 100
    rump @ a_finger "Oh, satu hal lagi..."

    kim f_curious @ -m_talk "Hmm?"

    rump "Kumpulkan dokumen apa pun yang dimiliki bos Anda mengenai urusan kita selama dua belas bulan terakhir, dan buanglah."

    rump "Segalanya akan segera memanas dan saya tidak ingin ada jejak kertas."

    kim f_smirk "Ya, tentu saja."

    kim "{b}Catatan di lantai atas, di kantor{/b}."

    kim "{b}Kim{/b} sayang dengan mereka."

    rump "Jangan mengecewakanku, {b}Kim{/b}."

    show kim b_dressed_bow with dissolve
    kim "Tidak pernah, {b}Bpk. pantat{/b}."

    hide rump
    show kim b_dressed
    with dissolve
    pause .5
    hide kim with dissolve

    scene expression background(560, 480, 3) as stage
    show anon f_worried
    with fade
    anon @ -m_talk "( Hmm, mungkinkah {b}Walikota Rump{/b} berbisnis dengan mafia Rusia? )"

    anon @ -m_talk "(Tentu saja terdengar seperti itu dari percakapan yang baru saja kudengar...)"

    anon @ -m_talk "(Saya harus {b}pergi ke atas ke kantor dan melihat bagaimana menemukan dokumen{/b} yang sedang mereka diskusikan. )"

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
