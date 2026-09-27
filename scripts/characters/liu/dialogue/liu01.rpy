label liu01_init_liu:
    show anon f_shy with dissolve
    liu "Halo dan selamat datang di {b}Saga Financial{/b}."

    liu "Nama saya {b}Liu Kim{/b}."

    liu "Apa yang bisa saya bantu hari ini?"

    anon "Hai."

    if M_anon.finished_state(S_ano13_tina):
        anon "Saya mencari {b}Tina{/b}."

        liu @ f_worried "Oh, maaf, dia tidak ada di sini sekarang."

        anon f_sad_down "Oh..."

        liu "Bolehkah aku menyampaikan pesan untuknya?"

        anon f_worried "Tidak, tidak apa-apa, saya akan kembali lagi nanti."

        liu "Apakah ada hal lain yang bisa saya bantu?"

        anon "Ooh, sebenarnya, bolehkah saya berbicara dengan Anda tentang pinjaman yang baru-baru ini diambil oleh teman saya?"

    else:
        anon f_worried "Umm, aku berharap bisa berbicara denganmu tentang pinjaman yang baru saja diambil temanku."

    liu "Oke, tentu saja."

    liu "Siapa nama temanmu?"

    anon "{b}[deb_name] Cummings{/b}."

    liu f_surprised @ a_mouth_cover "{i}*Terkesiap*{/i}"

    liu "A-apa kamu anak {b}Frank{/b}?"

    anon f_sad_down @ -m_talk "Mmhmm."

    liu f_worried_down "Oh, aku um-"

    liu f_nervous "{i}*Ahem*{/i} Aku turut berduka cita atas ayahmu..."

    liu "Sungguh mengerikan apa yang terjadi."

    anon "Terima kasih sudah mengatakan itu."

    anon f_worried "Apakah kalian berdua berteman?"

    liu @ f_curious "Teman-teman?!"

    liu "T-tidak, aku hanya-"

    show anon f_skeptical
    liu "Eh, maksudku, ya..."

    liu "Kami berteman."

    anon f_normal "Oh bagus."

    anon "Mungkin Anda bisa membantu saya?"

    liu @ f_nervous_laugh "Heh, umm... Tentu."

    liu "Saya ingin sekali."

    liu f_normal_down a_typing "Izinkan saya menariknya ke sini dan melihat apa yang sedang kita hadapi..."

    anon "Terima kasih."

    pause
    show liu f_surprised
    pause
    liu f_worried_down "Oh oke..."

    liu f_curious "Sepertinya dia mengambil pinjaman sebesar dua ratus lima puluh ribu dengan tingkat bunga tiga persen?"

    anon @ -m_talk "..."
    liu "Yang aneh karena kami biasanya tidak meminjamkan sebanyak itu..."

    anon "Ya, dia menjadikan rumah kami sebagai jaminan."

    liu f_nervous "Oh, um..."

    pause
    liu f_normal_down "Ya, itu menjelaskannya."

    pause
    liu f_curious "Lalu apa masalahnya?"

    anon f_worried "Begini, saat ini kami sedang mengalami krisis keluarga."

    show liu f_nervous
    anon @ f_sad_down "Hmm."

    anon "{i}*Huh*{/i} Saya tidak begitu yakin bagaimana menjelaskannya..."

    pause
    anon "Saya pikir ayah saya mungkin telah mencuri banyak uang dari beberapa penjahat Rusia yang sangat menakutkan."

    show liu f_nervous_lipbite
    pause
    anon "Dan temanku mengambil pinjaman ini untuk memberi kita waktu, paham?"

    pause
    anon "Yang mana, tidak benar-benar berhasil... Sepertinya, sama sekali."

    anon f_sad_down "Faktanya, ancaman mereka semakin agresif."

    pause
    anon "Dan yang terpenting, saya khawatir kami tidak akan dapat melakukan pembayaran dalam waktu dekat."

    pause
    anon f_worried "Jadi, saya berharap ada sesuatu yang bisa Anda lakukan?"

    liu f_ashamed_down "..."
    anon "Aku tahu itu semua terdengar gila tapi itu-"

    liu "Saya tahu {b}Frank{/b} akan melakukan sesuatu yang bodoh..."

    pause
    anon f_surprised_teeth "!!!" with hpunch
    anon f_skeptical "T-tunggu sebentar."

    anon "Tahukah Anda sesuatu tentang semua ini?"

    liu f_nervous @ -m_talk "Hmm?"

    liu "T-tidak, aku-"

    liu "Saya tidak tahu apa-apa."

    anon "Tapi kamu baru saja mengatakan-"

    liu @ f_surprised a_holdup "Lihat!"

    liu f_curious a_idle "Umm, maaf... Aku tidak tahu namamu?"

    anon "{b}[firstname]{/b}."

    liu f_nervous "Benar."

    liu "Maaf, {b}[firstname]{/b}."

    liu "Sepertinya Anda dan teman Anda sedang melalui masa sulit saat ini, dan saya bersimpati, ya."

    liu "Namun, saya tidak begitu yakin seberapa besar bantuan yang dapat saya berikan dengan semua ini..."

    pause
    liu "Maksud saya, saya bisa menghilangkan tingkat bunga dan menunda pembayaran awal Anda selama beberapa bulan, tapi hanya itulah yang bisa saya lakukan."

    anon @ -m_talk "..."
    liu "Apakah itu membantu?"

    anon f_worried "Ya, menurutku itu lebih baik daripada tidak sama sekali."

    liu "Oke, bagus!"

    show liu f_normal_down a_typing with dissolve
    pause
    anon f_thinking @ -m_talk "(Dia pasti tahu lebih banyak tentang {b}Ayah{/b} daripada yang dia ungkapkan. )"

    pause
    anon @ -m_talk "(Aku bertanya-tanya mengapa dia tidak memberitahuku?)"

    liu f_nervous "Apakah ada hal lain yang bisa saya lakukan untuk Anda, {b}[firstname]{/b}?"

    anon f_worried "Uhh, tidak... Kurasa tidak."

    liu "Baiklah, terima kasih atas bantuan perbankan-"

    anon @ f_surprised "Tunggu!"

    anon "Saya hampir lupa; Saya ingin membuka akun saya sendiri selama saya di sini."

    liu f_curious "Oh, kamu tidak punya akun?"

    anon "Tidak."

    liu f_normal "Kalau begitu, kamu benar!"

    liu "Anda pasti harus memulainya."

    liu "Ini adalah hal teraman yang dapat Anda lakukan dengan uang Anda dan Anda akan mendapatkan bunga atas apa pun yang Anda setorkan."

    pause
    liu f_normal_down "Beri saya waktu satu menit di sini untuk menyiapkan semuanya untuk Anda."

    anon "Terima kasih, {b}Liu{/b}."

    liu "Tidak masalah."

    pause
    anon a_thinking f_thinking @ -m_talk "(Pasti ada sesuatu yang bisa kulakukan agar dia terbuka padaku...)"

    pause
    anon f_grin @ -m_talk "(Mungkin aku hanya perlu mencari momen yang tepat?)"

    liu f_normal "Baiklah, {b}[firstname]{/b}."

    show anon f_normal a_idle with dissolve
    liu a_card "Berikut informasi rekening beserta kartu ATM."

    show anon a_card_atm
    show liu a_idle
    with dissolve
    liu "Yang seharusnya bisa digunakan di salah satu cabang kami."

    anon a_idle "Baiklah."

    liu "Apakah ada hal lain yang bisa saya lakukan untuk Anda hari ini?"

    anon "Tidak, menurutku itu saja."

    liu "Baiklah, terima kasih telah melakukan transaksi perbankan dengan kami di {b}Saga Financial{/b}."

    liu @ f_laugh "Semoga harimu menyenangkan!"

    anon "Ya, kamu juga."

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
