label smith_button_teachers_lounge:
    show player 22 at left
    show principal 33 at right
    with dissolve
    player_name "(Aduh! {b}Nyonya Smith{/b} ada di sini! )"

    show player 11
    show principal 31 with dissolve
    player_name "( ... )"
    show principal 32
    smith "{b}[firstname]{/b}?"

    smith "Apa yang kamu lakukan di ruang guru?!"

    show player 10
    show principal 31
    player_name "aku hanya-"

    show player 11
    show principal 32
    smith "Siswa tidak diperbolehkan berada di sini!"

    smith "Segera kembali ke kelasmu atau aku akan mengeluarkanmu!"

    show player 10
    show principal 31
    player_name "Y-ya, Bu!"

    return

label smith_button_eve_school_dress_code:
    show smith
    show anon f_worried
    with dissolve
    anon "E-permisi, {b}Ny. Smith{/b}?"

    smith "Apa yang kamu lakukan di sini?!"

    anon "Saya benar-benar perlu berbicara dengan Anda."

    smith "Tentang apa?!"

    smith "Saya seorang wanita yang sangat sibuk, Anda tahu?!"

    anon "Y-ya, aku tahu."

    pause
    smith "Baiklah, cepatlah, keluarlah!"

    anon "Ini tentang kebijakan aturan berpakaian yang baru..."

    smith f_confused "Kebijakan aturan berpakaian?!"

    pause
    anon "Ya, {b}Annie{/b} mengatakan Anda akan menerapkan kebijakan baru dan-"

    smith f_normal "Oh itu."

    smith "Saya menugaskan gadis itu untuk bertanggung jawab atas hal itu, itu proyeknya."

    anon "T-tapi dia menyuruhku datang dan bicara denganmu!"

    anon "Kebijakan baru melarang pewarna rambut, lho... Dan salah satu teman saya adalah-"

    smith @ f_eyeroll "Ck, aku tidak mau mendengarnya!"

    smith "Aku bilang pada {b}Annie{/b} bahwa dia bisa melakukan apa pun yang dia mau selama itu tidak membuatku kerepotan..."

    smith f_angry "Apakah kamu di sini untuk menimbulkan masalah?!"

    anon "saya-"

    smith "Karena aku dengan senang hati memberimu detensi karena menggangguku dengan masalah kecil ini!"

    anon f_surprised "T-tidak, Bu!"

    anon "aku tidak-"

    smith "Bagus!"

    smith f_scream "Sekarang keluar!"

    anon f_sad_down @ -m_talk "..."
    hide anon with dissolve
    $ player.go_to_previous()
    scene expression player.location.background_blur
    show anon f_sad_down
    with fade
    anon @ -m_talk "( {i}*Sigh*{/i} Ya, itu bisa saja lebih baik. )"

    anon @ -m_talk "(Bagaimana saya bisa memperbaikinya sekarang?)"

    anon @ -m_talk "( Tidak mungkin saya akan meminta {b}Annie{/b} untuk mengubahnya dan {b}Mrs. Smith{/b} sepertinya tidak peduli... )"

    show anon f_thinking a_thinking with dissolve
    pause
    anon @ -m_talk "(Hmm, saya ingin tahu apakah ada guru yang mau membantu saya?)"

    anon f_grin a_idle "(Saya harus {b}bertanya pada mereka{/b}! )"

    hide anon with dissolve
    return

label smith_button_intro:
    show anon f_worried
    show smith:
        xoffset -100
    show annie:
        xoffset 100
    with {'master': dissolve}
    anon "Anda ingin bertemu dengan saya, {b}Ny. Smith{/b}?"

    smith "Memang benar, {b}[firstname]{/b}."

    smith "Kami perlu mendiskusikan nilai Anda dan apakah Anda berniat untuk lulus atau tidak."

    anon f_surprised "Apakah seburuk itu?"

    smith a_grades "Coba lihat sendiri..."

    show screen school_locker_report()
    anon a_surprised f_shock "( !!! )" with hpunch
    pause
    hide screen school_locker_report with {'master': dissolve}
    show smith a_idle with {'master': dissolve}
    anon a_rub f_worried "Ya ampun, aku gagal dalam segalanya?!"

    smith "sudah kubilang..."

    annie f_annoyed "Itulah yang terjadi jika kamu bolos sekolah selama sebulan!"

    anon a_sides "Aku tidak melewatkannya! Ayahku meninggal!"

    smith a_hips @ f_eyeroll "Diam, {b}Annie{/b}!"

    annie @ f_curious "M-maaf, Bu."

    show annie f_normal
    smith "... Terlepas dari situasinya."

    smith "Anda harus {b}menemukan cara untuk menaikkan nilai ini{/b} jika Anda tidak ingin mengulanginya tahun depan."

    smith "Saya sarankan Anda {b}berbicara dengan guru Anda{/b} tentang memperbaiki pekerjaan yang Anda lewatkan."

    smith "Mungkin mereka bisa memberikan tugas kredit tambahan atau semacamnya?"

    anon a_idle "Y-ya, oke."

    smith "Lakukan apa pun!"

    anon "Ya, Bu."

    smith "Bagus, sekarang masuk ke kelas."

    anon f_shy "... Sebenarnya, Bu?"

    smith "Ya?"

    anon "Saya lupa kode sandi loker saya. Bisakah Anda membantu saya membukanya?"

    show smith f_confused
    annie f_angry "Apa maksudmu kamu lupa?!"

    show anon f_surprised
    annie "Setiap orang diberitahu di awal tahun untuk menuliskan kombinasinya!"

    anon f_shy "aku um..."

    anon "Saya kehilangannya!"

    annie f_normal @ f_gross "Pfft, tipikal."

    smith f_normal "Sangat mengecewakan, {b}[firstname]{/b}."

    smith "Kami harus memberi Anda kunci baru."

    anon @ -m_talk "..."
    smith "Saya akan mengirimkan {b}Annie{/b} dengan kunci masternya sebentar lagi..."

    smith "Saya sarankan Anda mengeluarkan semua yang Anda butuhkan sekarang."

    smith "Mungkin perlu beberapa saat sebelum kunci baru tiba."

    anon f_normal "Ya, Bu."

    smith "Pergilah ke sana sekarang dan pergilah ke kelas setelah selesai!"

    return

label smith_button_go_to_locker:
    show anon f_surprised
    show smith:
        xoffset -100
    show annie f_angry:
        xoffset 100
    with {'master': dissolve}
    annie "Bukankah {b}Ny. Smith{/b} menyuruhmu mengalahkannya?!"

    annie f_normal "{b}Pergilah ke lokermu{/b} dan aku akan menemuimu sebentar lagi!"

    return

label smith_button_get_out:
    show player 11 at left
    show principal 1 zorder 0 at Position(xpos=0.65, ypos=1.0)
    with dissolve
    smith "Apa yang sedang kamu lakukan?"

    show principal 2
    smith "Get the hell out of my office!" with hpunch
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
