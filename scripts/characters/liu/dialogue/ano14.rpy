label ano14_init_liu:
    scene expression background(520, 492, 4.) as stage
    show kim f_angry:
        flip
        xoffset 50
    show liu f_worried
    liu "Saya tidak ingin pergi."

    kim "Apa maksudmu kamu tidak boleh pergi?!"

    liu "Kumohon... Jangan memaksaku."

    liu "Walikota adalah orang tua yang bejat dan dia membuatku sangat tidak nyaman."

    liu f_ashamed_down "Cara dia menatapku..."

    liu "... Seperti dia membuka bajuku dengan matanya."

    kim a_crossed "Pfft, {b}Kim{/b} tidak peduli dengan ini!"

    liu f_worried @ f_surprised "!!!"
    kim "Walikota berjanji kepada {b}Kim{/b}."

    kim "Berikan {b}Kim{/b} kendali atas rasa sayang."

    kim "Dia membuat {b}Kim{/b} menjadi pria yang sangat lelah!"

    liu "Jadi kamu hanya akan melayaniku untuk mencapai ambisimu?!"

    kim a_point "Kamu {b}istri Kim{/b}, bodoh!"

    kim "Tugas Anda adalah mendorong {b}Kim{/b} ambisi lebih lanjut!"

    liu f_ashamed_down @ -m_talk "..."
    kim a_crossed "Jangan lupa, saya membayar banyak uang untuk Anda di Korea!"

    kim "Aku membawamu ke sini dan memberimu senapan yang bagus!"

    kim "Aku bahkan yakin kamu punya pekerjaan di bank."

    kim "Ini ucapan terima kasih yang {b}Kim{/b} dapatkan?!"

    liu f_worried "T-tidak, aku hanya-"

    kim @ a_point "Kamu tidak tahu berterima kasih!"

    pause .3
    kim @ a_point "Kamu istri yang buruk!"

    liu "Apakah tidak ada hal lain yang bisa saya lakukan?"

    kim @ a_cry "Brah, brah, brah... {b}Kim{/b} tidak ingin mencari lagi..."

    kim "Walikota memintamu datang, jadi kamu datang."

    show liu f_worried_down
    show kim f_smirk a_swimsuit
    with dissolve
    pause
    kim "{b}Kim{/b} belikan untukmu."

    liu f_gross @ -m_talk "..."
    kim "Anda memakai."

    liu f_worried "Tolong, {b}Kim{/b}... Jangan membuat-"

    kim f_angry "Tenang!"

    kim "Anda menuruti atau {b}Kim{/b} mengirim Anda kembali ke Korea!"

    liu @ -m_talk "..."
    kim "Katakanlah Anda mengerti!"

    liu "... Saya mengerti."

    kim f_smirk "Bagus."

    kim "Anda ambil!"

    show kim a_idle
    show liu a_swimsuit f_worried_down
    with dissolve
    pause
    show liu f_worried
    kim "{b}Kim{/b} menjemputmu, setelah shift di dearership."

    kim "Kami pergi."

    kim f_angry a_counter_raised "Anda membuat walikota senang, ya?"

    liu "{i}*Mengendus*{/i} Y-ya."

    kim f_smirk a_idle "Bagus."

    kim "Finarry, patuhlah."

    kim @ a_point "Bersiaplah."

    kim a_rub "{b}Kim{/b} tidak ingin dinilai."

    hide kim with dissolve
    pause
    show liu f_worried_down
    pause
    show liu a_swimsuit_drop with dissolve
    pause .2
    liu a_cry f_crying @ -m_talk "{i}*Terisak*{/i}"


    scene expression player.location.background_blur
    show anon f_worried
    with fade
    anon @ -m_talk "(Apa-apaan ini?!)"

    anon @ -m_talk "(Aku tahu {b}Kim{/b} itu brengsek tapi itu menjijikkan!)"

    pause
    anon @ -m_talk "(Bagaimana mungkin ada orang yang memperlakukan istrinya seperti itu?)"

    anon @ -m_talk "(Aku harus memastikan dia baik-baik saja...)"

    hide anon with dissolve
    return


label ano14_sobs_liu:
    scene expression background(644, 492, 4.) as stage
    show liu a_cry f_crying:
        xoffset -500
    show anon f_worried with dissolve:
        flip
    liu @ -m_talk "{i}*Terisak*{/i}"

    show liu a_wipe_tears b_dressed f_crying with {'master': dissolve}
    anon "{i}*Ehem*{/i} Bu?"

    liu f_surprised a_cover "!!!"
    show liu f_worried with {'master': dissolve}:
        flip
        xoffset 0
    liu @ -m_talk "{i}*Mengendus*{/i}"

    liu a_idle "Oh, maaf soal itu..."

    liu "... Aku akan segera bersamamu."

    show liu b_dressed_bend with {'master': dissolve}:
        unflip
        xoffset -550
    anon "T-tidak, jangan minta maaf."

    show liu b_dressed a_nervous with {'master': dissolve}:
        flip
        xoffset 0
    anon a_behind_head "Aku agak... Yah, aku mendengar apa yang sedang terjadi..."

    pause
    anon a_idle "... Apakah kamu baik-baik saja?"

    liu "{i}*Sniff*{/i} Y-ya, aku akan baik-baik saja."

    show liu f_surprised
    pause
    liu a_behind "Oh, tembak!"

    liu f_worried "Kamu adalah anak {b}Frank{/b}, umm..."

    liu "... {b}[firstname]{/b}, kan?"

    anon "Itu benar."

    anon "Apakah kamu benar-benar menikah dengan pria itu?"

    liu "{i}*Sniff*{/i} Ya, sayangnya."

    anon "Bagaimana hal itu bisa terjadi?"

    liu f_curious @ -m_talk "Hmm?"

    liu f_worried_down "Oh, um..."

    anon @ a_hands_up "Maaf, aku tahu itu bukan urusanku."

    anon "Hanya saja, dia tidak seharusnya bicara seperti itu padamu."

    liu f_worried "Heh, itu hanya apa yang ayahmu katakan."

    anon "Apa maksudmu?"

    liu f_worried_down "{i}*Sniff*{/i} T-tidak, tidak apa-apa."

    pause
    liu "Saya tidak menikah dengannya karena pilihan, jika itu yang Anda minta."

    anon "Oh?"

    liu "Keluarga saya berasal dari desa kecil di perbatasan Tiongkok dekat Korea Utara."

    liu "Kami sangat miskin."

    pause
    liu "Jadi ketika {b}Kim{/b} menawarkan berat badan saya dalam bentuk perak kepada ayah saya, itu bukanlah keputusan yang sulit."

    anon "Ayahmu menjualmu padanya?"

    anon "Itu mengerikan!"

    liu "... Dan uang itu sangat membantu keluarga saya."

    pause
    liu f_worried_down "Dia tidak salah saat mengatakan dia membawaku ke sini dan memberiku kehidupan yang lebih baik juga."

    liu "Aku punya rumah yang bagus dan pekerjaan yang menghasilkan banyak uang... Dia bahkan mengizinkanku menyimpan sedikit gajiku untuk dibelanjakan sesukaku."

    anon @ f_skeptical "Sedikit ya?"

    anon @ f_skeptical "Betapa murah hatinya dia."

    liu "{i}*Sniff*{/i} Sebenarnya tidak terlalu buruk."

    liu "Dia terlalu sibuk di dealer sehingga tidak bisa menggangguku hampir sepanjang waktu..."

    liu "... Selama aku menjaga rumahnya dan membuatkannya makan malam, segalanya akan damai."

    anon "Anda berhak mendapatkan yang lebih baik."

    liu f_worried "I-Anda baik sekali yang mengatakannya."

    pause
    liu "Kamu sangat mirip ayahmu, tahu?"

    liu "aku benar-benar minta maaf atas semua yang terjadi..."

    pause
    liu f_worried_down "... Dia pria yang baik."

    anon @ f_sad_down "Y-ya, aku tahu."

    anon "Aku mencoba yang terbaik untuk mencari tahu apa yang terjadi..."

    anon "... Sebenarnya, itulah alasan saya ada di sini hari ini."

    liu f_curious "Hmm?"

    anon f_normal "Begini, saya menemukan kunci kotak kunci ini."

    liu "Salah satu milik kita, di dalam lemari besi?"

    anon "Ya, itulah yang diberitahukan kepadaku."

    anon "Saya pikir {b}Ayah{/b} mungkin meninggalkan sesuatu di sana."

    pause
    anon "{b}Tina{/b} bilang dia akan membawaku ke bawah untuk memeriksanya."

    liu f_worried "Jadi begitu."

    liu "Sayangnya, dia tidak ada di sini saat ini."

    anon f_worried "Oh?"

    liu "Dia mendapat telepon dari sekolah putrinya dan bergegas pergi."

    liu "Sesuatu tentang kerusakan lemari pakaian saat latihan pemandu sorak."

    anon "Tidak bercanda?"

    pause
    anon f_unimpressed "Ya, sial."

    pause
    anon f_worried "Kurasa, aku harus kembali lagi nanti."

    liu "Aku bisa, mungkin... Membawamu ke sana."

    show anon f_surprised
    pause
    anon @ f_skeptical "Mungkin?"

    liu "T-tidak, aku bisa."

    liu f_worried_down @ f_surprised "Saya akan!"

    anon f_worried "Anda yakin?"

    liu f_worried "Tentu saja!"

    liu a_nervous "Hanya, um..."

    show liu a_swimsuit_show with dissolve
    show anon f_worried_low
    liu "... Beri aku waktu sejenak untuk menyingkirkan bikini bodoh ini."

    show liu f_nervous
    anon f_normal "Tentu saja."

    liu a_behind "Anda akan menemukan tangga menuju lemari besi di ujung lorong sana."

    liu "Aku akan menemuimu sebentar lagi."

    anon "Terima kasih, {b}Liu{/b}."

    liu "Dengan senang hati, {b}[firstname]{/b}."

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
