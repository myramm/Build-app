label tina_button_bank:
    $ renpy.dynamic(schedule=M_tina.sex != game.timer._game_day)

    if L_bank_lobby.is_here(M_tina):
        show tina f_laugh
        show anon with dissolve:
            flip
        tina "Selamat pagi, tuan!"

        tina "Selamat datang di-"

        tina f_normal "Itu kamu."

        pause
        tina f_sexy "Apa yang membawamu ke sini, {b}[firstname]{/b}?"

    else:
        show anon with dissolve
        anon "Hai, {b}Tina{/b}."

        tina @ -m_talk "Hmm?"

        tina f_sexy "Wajah sayang?!"

        tina "Apa yang membawamu ke kantorku hari ini?"


    menu tina_button_bank.choice:
        "Jadi, Anda manajer banknya?":

            jump tina_button_bank.manager
        "Tahukah kamu ayahku?":

            jump tina_button_bank.frank
        "Bagaimana kabar {b}Becca{/b}?":

            jump tina_button_bank.becca

        "Jadwalkan seks?" if schedule and player.location == L_bank_cubicle:
            jump tina_button_bank.schedule

        "Jadwalkan seks?" if schedule and player.location == L_bank_lobby:
            jump tina_button_bank.rendezvous

        "Seks kantor?" if M_tina.sexfriend and player.location == L_bank_cubicle:
            if not M_tina.once('office_sex'):
                jump tina_button_bank.suggest
            else:
                jump tina_button_bank.sex
        "Saya harus pergi.":

            pass

    anon f_normal @ a_wave "Saya harus pergi."

    tina f_normal "Ya, aku harus kembali bekerja sendiri."

    anon "Senang bertemu denganmu."

    tina @ f_laugh "Anda juga, {b}[firstname]{/b}."

    tina "Segera kembali."

    hide anon with dissolve
    return


label tina_button_bank.becca:
    anon f_normal "Bagaimana kabar {b}Becca{/b}?"

    tina f_normal @ -m_talk "Hmm?"

    tina @ f_eyeroll "Ah, siapa tahu..."

    tina f_suspicious "Dia benar-benar banyak berubah sejak ayahnya meninggal."

    tina "Aku hampir tidak bisa mengeluarkan satu kalimat pun darinya saat ini..."

    tina f_annoyed "... Dan teman-temannya itu memberi pengaruh buruk!"

    anon "Oh?"

    tina "Gadis {b}Missy{/b} itu adalah orang paling ceroboh yang pernah kutemui!"

    tina "Dia tidak punya filter apa pun!"

    anon @ f_laugh "Hehe, itu benar."

    tina "Lalu ada {b}Roxxy{/b}."

    pause
    tina f_suspicious "Tahukah Anda dia tinggal di taman trailer?"

    tina "Eugh, jika aku tahu putriku akan mulai membawa pulang sampah putih, aku akan tetap tinggal di kota."

    anon f_worried @ f_surprised -m_talk "..."
    jump tina_button_bank.choice


label tina_button_bank.frank:
    anon f_normal "Tahukah kamu ayahku?"

    show tina f_normal
    anon "Dia dulu bekerja di sini."

    tina "Tidak bercanda?"

    tina "Siapa namanya?"

    anon "{b}Frank Cummings{/b}."

    tina f_surprised "!!!"
    tina "Apakah kamu serius?!"

    anon f_surprised "Jadi, kamu sudah mengenalnya?"

    tina f_sad "Tidak, tidak secara pribadi."

    tina "Dia dilepaskan oleh manajer sebelumnya..."

    tina "... Tapi polisi di sini menanyakan banyak pertanyaan tentang dia."

    show anon f_worried
    tina f_annoyed "Saya harus menghabiskan waktu dua minggu untuk memeriksa catatan bank karena kekacauan itu!"

    anon f_sad_down "Oh, begitu."

    tina f_sad "Err, aku tidak bermaksud-"

    pause
    tina "Ah, maafkan aku, Nak."

    tina "Itu tidak pantas untuk..."

    anon f_worried "Tidak, tidak apa-apa."

    anon "Aku juga sudah menangani kekacauannya."

    jump tina_button_bank.choice


label tina_button_bank.manager:
    anon f_normal "Jadi, Anda manajer banknya?"

    tina f_normal @ -m_talk "Mhmm."

    tina "Saya sedang belajar untuk menjadi seorang akuntan ketika saya bertemu Luigi dan dia mendorong saya untuk terus melakukannya."

    anon "Benar-benar?"

    tina "Dia bahkan melunasi pinjaman sekolahku."

    anon @ f_laugh "Itu luar biasa!"

    tina @ f_sad "Saya tidak mengerti mengapa hal itu begitu penting baginya saat itu..."

    tina "… Tapi sekarang setelah dia pergi, aku bersyukur karenanya."

    tina "Ini memberi saya tujuan, Anda tahu?"

    anon "Ya, saya mengerti."

    tina "Jika bukan karena pekerjaan ini, saya mungkin hanya akan duduk diam di rumah sepanjang hari."

    jump tina_button_bank.choice


label tina_button_bank.rendezvous:
    anon f_flirt "Ingin berhubungan seks nanti?"

    tina f_surprised "Ssst, jangan terlalu keras!"

    anon f_worried "Oh, um..."

    anon f_shy @ a_behind_head "... Salahku."

    show tina with dissolve:
        unflip
        xoffset -500
    pause
    show tina f_sexy with dissolve:
        flip
        xoffset 0
    tina "Kalau begitu, kamu ada waktu luang malam ini?"

    anon "Ya."

    tina @ f_laugh "Luar biasa!"

    tina "Aku akan mengirim {b}Becca{/b} ke rumah temannya dan kita akan menghabiskan malam itu sendirian."

    anon f_flirt "Saya tidak sabar."

    tina "Mmm, aku juga tidak."

    hide anon with {'master': dissolve}
    anon "Sampai jumpa nanti malam."

    return 'schedule'


label tina_button_bank.schedule:
    anon f_flirt "Ingin berhubungan seks nanti?"

    tina f_sexy "Oh, menurutku itu berarti kamu ada waktu luang malam ini?"

    anon "Ya."

    tina @ f_laugh "Luar biasa!"

    tina "Aku akan mengirim {b}Becca{/b} ke rumah temannya dan kita akan menghabiskan malam itu sendirian."

    anon @ f_laugh a_cheering "Saya tidak sabar."

    tina "Mmm, aku juga tidak."

    hide anon with {'master': dissolve}
    anon "Sampai jumpa lagi."

    return 'schedule'


label tina_button_bank.suggest:
    anon f_shy "Tidak bisakah kita berhubungan seks di sini?"

    tina f_sexy "Oh, kamu anak nakal..."

    tina "... Kita tidak bisa melakukan itu!"

    anon f_worried "Kenapa tidak?"

    tina @ f_laugh "Karena tidak ada kunci di pintuku!"

    tina "Bagaimana jika {b}Liu{/b} masuk?"

    anon f_flirt "Aku yakin dia akan mengetuk terlebih dahulu..."

    pause
    anon @ f_laugh "... Dan jika dia tidak mau, maka kami akan memintanya untuk bergabung dengan kami."

    tina @ f_laugh "Hah!"

    anon "Dia akan menyukainya, bukan begitu?"

    label tina_button_bank.sex:
    tina "Kamu sangat buruk..."

    anon "Ayo, aku akan cepat."

    show tina f_sexy_down_lipbite
    pause
    tina f_sexy "Yah, kuharap tidak terlalu cepat."

    anon f_normal "Apakah itu ya?"

    tina @ f_eyeroll "Saya kira."

    show tina with dissolve:
        xoffset -100
    anon f_shy "Benar-benar?!"

    tina "Cobalah untuk mengecilkan suaramu, oke?"

    pause
    anon "Oh, tentu saja!"

    anon "Bisa!"

    anon "Tidak masalah!"

    tina @ f_laugh "Hehe, kamu terlalu manis!"

    show tina b_dressed_open f_sexy_down_lipbite with dissolve
    pause
    show tina b_dressed_open_boobs_drop01 with dissolve
    pause
    show tina b_dressed_open_boobs_drop02 with dissolve
    show tina b_dressed_open_boobs_drop03 with dissolve
    show tina b_dressed_open_boobs_drop04 with dissolve
    pause
    show tina b_dressed_open_back o_empty with dissolve
    pause
    show tina b_dressed_open_back_undress with dissolve
    pause

    call scene_tina_sex_office.repeat
    $ unlock_scene('tina', '02_unlocked')

    scene expression background(712, 400, 2.5) as stage
    if _return == 'inside':
        show tina b_dressed_open_back
    else:
        show tina f_sexy b_dressed_open_boobs o_glasses
    show anon f_flirt
    with fade
    anon "Aku akan mengambilkanmu tisu dari kamar mandi."

    if _return == 'inside':
        show tina f_sexy b_dressed_open_boobs o_glasses with dissolve
    tina "Tidak apa-apa, aku akan mengurusnya."

    anon f_shy "Apa kamu yakin?"

    tina "Ya."

    show tina b_dressed_open_boobs_kiss o_empty
    hide anon
    with dissolve
    pause
    show tina b_dressed_open_boobs o_glasses
    show anon
    with dissolve
    tina "Berjanjilah padaku, kita akan melakukannya lagi suatu saat nanti..."

    anon f_flirt "Ya?"

    tina @ f_sexy_down_lipbite -m_talk "Mhmm."

    anon "Tentu saja."

    tina "Sampai jumpa lagi, wajah sayang."

    hide tina with dissolve
    pause 0.5
    anon f_laugh @ -m_talk "(Itu luar biasa!)"

    hide anon with dissolve
    return 'afterglow'
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
