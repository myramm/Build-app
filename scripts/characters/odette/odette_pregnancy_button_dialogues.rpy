label button_odette_pregnancy_leave_stage_0:
label button_odette_pregnancy_leave_stage_1:
    anon @ a_wave "Aku akan meninggalkanmu."

    odette "Baiklah."

    odette "Berikan {b}Evie{/b} ciuman untukku, oke?"

    anon "Akan dilakukan."

    hide anon with dissolve
    return

label button_odette_pregnancy_leave_stage_2:
label button_odette_pregnancy_leave_stage_3:
    anon f_normal "Aku akan meninggalkanmu."

    odette f_normal "Baiklah."

    odette f_smirk "Berikan {b}Evie{/b} ciuman untukku, oke?"

    anon "Akan dilakukan."

    hide anon with dissolve
    return

label button_odette_pregnancy_bathroom_stage_4:
    scene expression background(544, 288, 2.) as stage at flip
    show layer master at flip
    show odette f_smirk b_naked_pregnant_belly a_towel
    show anon f_flirt with dissolve
    odette "Kembali lagi?"

    anon "Saya tidak bisa menahannya."

    anon "Kamu sangat seksi saat ini..."

    odette @ f_laugh "Hehe, tidak apa-apa."

    show odette a_remove1 with dissolve
    pause
    show odette a_remove2 with dissolve
    show anon f_flirt_low
    odette "Saya tidak keberatan."

    odette a_squeeze "Lihatlah selama yang kamu mau, kawan."

    pause
    hide anon with dissolve
    $ game.main()
    return

label button_odette_pregnancy_leave_stage_4:
    anon "Aku akan meninggalkanmu."

    odette "Baiklah."

    odette "Berikan {b}Evie{/b} ciuman untukku, oke?"

    anon "Akan dilakukan."

    hide anon with dissolve
    return

label button_odette_pregnancy_get_anything_0:
label button_odette_pregnancy_get_anything_1:
    anon "Bolehkah aku memberimu sesuatu?"

    odette f_smirk "Yah, penis dalam yang bagus pasti menyenangkan..."

    odette @ f_eyeroll a_shrug "... Tapi aku sudah berjanji pada {b}Grace{/b} Aku tidak akan melakukannya, setidaknya sampai bayinya lahir."

    anon @ f_sad_down "Oh."

    odette @ f_sad "Ya..."

    odette "... Tapi percayalah, begitu aku bisa, kita akan kesulitan... Mengerti?"

    anon f_normal @ f_flirt "Hehe, oke."

    return

label button_odette_pregnancy_get_anything_2:
label button_odette_pregnancy_get_anything_3:
    anon "Ada yang bisa kuberikan padamu?"

    odette "Heh, kecuali Anda tahu suatu tempat di sekitar kota yang menjual kue corong?"

    anon f_skeptical "kue corong?"

    odette "Ya Tuhan, aku sangat menginginkannya!"

    odette @ f_eyeroll "Anda tidak tahu."

    show anon f_normal
    pause
    odette "Mungkin dengan saus keju nacho..."

    pause
    odette f_surprised "{i}*Terkesiap*{/i} Atau salsa!"

    anon f_disgusted_down "Oke, baru saja."

    odette f_sad "Ya, saya tahu itu menjijikkan... Saya tidak bisa menjelaskannya."

    pause
    odette "Ugh, mulutku berair hanya dengan memikirkannya!"

    anon "Uhh, aku tidak tahu ada tempat di sekitar sini yang menjual kue corong..."

    anon f_worried "Aku bisa membelikanmu donat?"

    odette "Ugh, tidak... Tidak apa-apa."

    anon "Anda yakin?"

    odette "Ya."

    odette "Terima kasih."

    return

label button_odette_pregnancy_get_anything_4:
    anon "Ada yang bisa kuberikan padamu?"

    odette f_tired "Ya ampun jangan kesana {b}[firstname]{/b}..."

    odette "Aku ingin kontol, sayang sekali!"

    anon f_disgusted_down "Ehh."

    odette "Semua mainan di dunia tidak dapat menggantikan mainan asli."

    anon f_worried "Kami selalu bisa-"

    odette f_surprised "Tidak, jangan goda aku!"

    odette "{b}Grace{/b} bilang kita bisa bercinta semau kita setelah bayinya lahir dan aku ingin menepati janjiku."

    anon f_surprised "Baiklah."

    odette f_tired "Saya hanya berharap itu terjadi segera, saya sekarat di sini..."

    odette f_tired_down "Kamu dengar itu, dasar brengsek?!"

    odette "Waktunya habis, keluarlah dari sana!"

    anon f_worried @ f_worried_left "hehe!"

    return

label button_odette_pregnancy_how_feeling_0:
label button_odette_pregnancy_how_feeling_1:
    anon "Bagaimana perasaanmu?"

    odette @ f_confused "Uhh, baiklah?"

    pause
    odette "Mengapa kamu bertanya?"

    anon @ a_point "Kau tahu, karena bayinya..."

    odette "Oh benar!"

    odette "Bayi itu."

    odette "Ya, aku baik-baik saja sejauh ini."

    odette "Jangan khawatir."

    anon "Baiklah."

    return

label button_odette_pregnancy_how_feeling_2:
label button_odette_pregnancy_how_feeling_3:
    anon f_worried "Bagaimana perasaanmu?"

    odette @ f_tired "Ehh, oke, menurutku..."

    odette "Morning Sickness itu menyebalkan!"

    anon "Oh?"

    odette f_sad "Ya, dan payudaraku juga membunuhku!"

    anon "Itu menyebalkan..."

    odette f_smirk @ f_eyeroll "{i}*Huh*{/i} Ya."

    odette "Saya sangat senang {b}Grace{/b} membujuk saya untuk tidak melakukan tindik di puting..."

    odette @ f_laugh "Hehehe!"

    odette "Tapi serius, aku baik-baik saja."

    show anon f_normal
    odette "Dia telah merawatku dengan baik."

    anon "Yah, aku senang mendengarnya."

    odette "Ya."

    return

label button_odette_pregnancy_how_feeling_4:
    anon "Bagaimana perasaanmu?"

    odette f_tired "Ugh, aku sangat siap untuk mengeluarkan anak iblis ini dariku..."

    anon f_worried "Seburuk itu, ya?"

    odette "Anda tidak tahu!"

    odette "Bocah kecil itu membuatku terjaga sepanjang malam, menendang!"

    odette "Aku bersumpah demi Tuhan, dia mencoba bermain sepak bola dengan ginjalku."

    anon "Kedengarannya kasar."

    odette "{i}*Huh*{/i} Ya."

    return

label button_odette_pregnancy_intro_4:
    scene expression player.location.background_closeup with None
    show anon
    show odette f_smirk
    with dissolve
    anon "Halo, {b}Odette{/b}."

    odette "Hei, teman besar."

    return

label button_odette_pregnancy_intro_2:
label button_odette_pregnancy_intro_3:
    scene expression player.location.background_closeup with None
    show anon
    show odette f_smirk
    with dissolve
    anon "Halo, {b}Odette{/b}."

    odette "Hei, teman besar."

    return

label button_odette_pregnancy_intro_0:
label button_odette_pregnancy_intro_1:
    scene expression player.location.background_closeup with None
    show anon
    show odette f_smirk
    with dissolve
    anon "Halo, {b}Odette{/b}."

    odette "Hei, teman besar."

    return

label button_odette_pregnancy_gave_birth_leave:
    anon a_idle f_normal "Aku akan meninggalkanmu."

    odette "Berikan {b}Evie{/b} ciuman untukku."

    anon "Akan dilakukan."

    hide anon with dissolve
    return

label button_odette_pregnancy_gave_birth_need_anything:
    anon "Kalian butuh sesuatu?"

    odette "Ya, perawat basah akan menyenangkan."

    anon @ f_worried a_behind_head "Ehh, aku tidak yakin bisa membantumu disana..."

    odette "Hehe, bukan?"

    odette "Cih, harapanku terlalu tinggi."

    anon "Maaf."

    odette "Tidak apa-apa, kamu bisa segera menebusnya."

    anon @ -m_talk "Hmm?"

    odette f_smirk "Memekku sudah membaik dan tak lama lagi, aku akan membutuhkan penis itu."

    anon a_behind_head f_shy "{i}*Meneguk*{/i} O-oke..."

    odette "Saya serius, {b}[firstname]{/b}..."

    show anon f_surprised
    odette "Sebaiknya kau meniduriku dengan keras!"

    anon "Saya mengerti."

    odette @ f_laugh "Hehehe!"

    return

label button_odette_pregnancy_gave_birth_intro:
    scene expression player.location.background_closeup with None
    show odette f_happy_down a_baby
    show anon
    with dissolve
    odette "Kalau tidak memperlambat proses menyusui, payudara {b}ibu{/b} akan lepas..."

    odette "Ya, benar!"

    odette @ f_laugh "Hehehe!"

    anon "Hai."

    odette f_smirk "Hei, teman besar."

    return

label button_odette_pregnancy_yup:
    anon "Ya, bagaimana kabar kalian?"

    odette "Kami berdua baik-baik saja."

    show odette f_happy_down
    if M_odette.pregnancy.baby_gender == "boy":
        odette "Saya baru saja selesai memberinya makan."

        odette "Dia benar-benar pria kecil yang lapar..."

        odette "... Menghabiskan setengah hari dengan putingku di mulutnya."

        anon "Heh, aku tidak bisa menyalahkannya di sana..."

    elif M_odette.pregnancy.baby_gender == "twins":
        odette "Saya baru saja selesai memberi mereka makan."

        odette "Itu pastinya adalah hal-hal kecil yang lapar..."

        odette "... Habiskan setengah hari dengan putingku di mulut mereka."

        anon "Heh, aku tidak bisa menyalahkan mereka di sana..."

    else:
        odette "Saya baru saja selesai memberinya makan."

        odette "Dia benar-benar gadis kecil yang lapar..."

        odette "... Menghabiskan setengah hari dengan putingku di mulutnya."

        anon "Heh, aku tidak bisa menyalahkannya di sana..."

    anon "Saya tidak berpikir payudara itu bisa menjadi lebih besar tetapi entah bagaimana mereka berhasil..."

    odette @ f_laugh "Hehehe!"

    pause
    anon @ a_wave "Kurasa aku harus meninggalkan kalian untuk beristirahat."

    odette f_normal "Intip {b}Grace{/b} dan pastikan dia baik-baik saja selama aku terjebak di sini, ya?"

    anon "Saya bisa melakukan itu."

    odette "Terima kasih, {b}[firstname]{/b}."

    pause
    if M_odette.pregnancy.baby_gender == "twins":
        anon "Sampai jumpa lagi, anak-anak kecil."

    else:
        anon "Sampai jumpa, anak kecil."

    odette @ f_laugh "Hehehe!"

    hide anon with dissolve
    return

label button_odette_pregnancy_bedridden:
    scene expression game.timer.image("location_hospital_baby_bed{}")
    show odette b_gown_bed f_smirk
    show anon with dissolve
    odette "Hei, teman besar."

    odette "Anda datang untuk memeriksa kami lagi?"

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
