label tony_button_pizzeria:
    if game.timer.is_day():
        show anon with dissolve:
            flip
        if randomizer() > 75:
            show tony a_fists
        elif randomizer() > 50:
            show tony a_frustrated
        elif randomizer() > 25:
            show tony a_wave
        else:
            show tony a_point
        with dissolve
        if M_anon.finished_state(S_ano11_bone):
            tony "'Ey, itu temanku!"

            show anon f_grin
            tony a_idle "Bagaimana kabarmu, juara?!"

        else:
            tony "'Hei, jagoan!"

            show anon f_grin
            tony a_idle "Anda siap mengantarkan pizza?"

        show anon f_normal
    else:
        show anon with dissolve
        if M_anon.finished_state(S_ano11_bone) and not M_maria.pregnancy:
            tony "'Hei, jagoan!"

            tony "Jika Anda mencari {b}Maria{/b}, dia ada di ruang toko."

        else:
            tony "Kamu masih di sini?"

            tony "Anda harus pulang."


    label tony_button_pizzeria.choice:
    if M_anon.finished_state(S_ano11_bone):
        menu:
            "Kotak kunci." if M_anon.is_state(S_ano14_tony):
                jump ano14_tony_tony_lockbox

            "Pesan pizza." if game.timer.is_day():
                jump tony_dialogue_order

            "Butuh bantuan?" if game.timer.is_dark():
                jump tony_button_pizzeria.help
            "Tatomu?":

                jump tony_button_pizzeria.tattoo

            "{b}Maria{/b} di sekitar?" if game.timer.is_day():
                jump tony_button_pizzeria.curious

            "{b}Maria{/b} di sekitar?" if game.timer.is_dark() and M_maria.pregnancy.stage > 4:
                jump tony_button_pizzeria.babies
            "Bagaimana Anda dan {b}Maria{/b} bertemu?":

                jump tony_button_pizzeria.maria

            "Saya harus pergi." if game.timer.is_day():
                pass

            "Baru saja check-in." if game.timer.is_dark():
                pass
    else:

        menu:
            "Anda yakin!" if game.timer.is_day():
                jump tony_button_pizzeria.deliver

            "Pesan pizza." if game.timer.is_day():
                jump tony_dialogue_order

            "Butuh bantuan?" if game.timer.is_dark():
                jump tony_button_pizzeria.help

            "Mafia Italia." if M_anon.finished_state(S_ano06_cook):
                jump tony_button_pizzeria.italians

            "Tatomu?" if not M_anon.finished_state(S_ano06_cook):
                jump tony_button_pizzeria.tattoo
            "Rusia.":

                jump tony_button_pizzeria.russians

            "Bagaimana Anda dan {b}Maria{/b} bertemu?" if M_maria.met:
                jump tony_button_pizzeria.maria

            "Adopsi?" if M_anon.between_states(S_ano08_work, S_ano10_tony):
                jump tony_button_pizzeria.adoption

            "Ada informasi belum?" if M_anon.between_states(S_ano08_work, S_ano10_tony):
                jump tony_button_pizzeria.info

            "Saya harus pergi." if game.timer.is_day():
                pass

            "Selamat malam." if game.timer.is_dark():
                pass

    if game.timer.is_day():
        if M_anon.finished_state(S_ano11_bone):
            anon f_normal "Saya harus pergi."

            tony f_normal "Ahh, baiklah, jagoan."

            anon "Sampai jumpa nanti?"

            tony "Anda yakin."

        else:
            anon f_normal "Sebenarnya, ada beberapa hal lain yang perlu aku urus saat ini..."

            tony f_normal "Apa, kamu akan pergi?"

            anon "Y-ya, tapi aku akan segera kembali."

            anon "Saya berjanji."

            tony "Ck, cepat ya?"

            tony @ f_laugh a_belly "Pizza ini mulai dingin!"

            anon "Ya, tuan!"

    else:
        if M_anon.finished_state(S_ano11_bone):
            anon f_normal "Baru saja check-in."

            tony f_normal "Tidak perlu khawatir tentang saya."

            tony "Pulanglah ke ibumu, ya?"

            tony "Sampai jumpa besok."

        else:
            anon f_normal @ a_wave "Selamat malam."

            tony f_normal a_idle @ a_wave "Sampai jumpa besok, juara."


    hide anon with dissolve
    return


label tony_button_pizzeria.adoption:
    anon f_normal "Jadi, Anda sedang memikirkan tentang adopsi?"

    tony f_suspicious @ f_eyeroll a_frustrated "Oh bagus, sekarang kamu akan mulai membuat keberanianku tentang adopsi juga?"

    anon @ f_worried "Tidak, menurutku {b}Tina{/b} membuat beberapa poin bagus..."

    anon "Anda akan tahu persis apa yang mereka alami."

    tony f_sad "Ya, aku tidak tahu tentang itu..."

    tony "Saya yakin sistemnya telah banyak berubah selama tiga puluh tahun terakhir ini..."

    tony "... Dan bahkan jika belum, itu tidak mengubah fakta bahwa saya lebih suka membesarkan anak-anak {b}Maria{/b} daripada anak-anak orang asing yang belum pernah saya temui."

    pause
    tony "Mungkin itu membuatku menjadi orang jahat tapi itulah yang aku rasakan."

    anon "Tidak, itu tidak membuatmu menjadi orang jahat, {b}Tony{/b}."

    pause
    anon @ f_confused "Jadi Anda lebih memilih jalur bank sperma?"

    tony "Ya tapi {b}Maria{/b} tidak ingin mendengar apa pun tentang itu."

    pause
    anon "Jadi apa yang akan kamu lakukan?"

    tony "Kalahkan aku."

    tony "Itu adalah sesuatu yang dia dan aku harus pikirkan setelah kita menyelesaikan masalah kecilmu di Rusia..."

    jump tony_button_pizzeria.choice


label tony_button_pizzeria.babies:
    anon f_normal "Dimana {b}Maria{/b}?"

    show tony f_normal
    if M_maria.pregnancy.baby_gender == 'boy':
        tony "Si kecil mulai rewel jadi dia membawanya pulang."

        tony "Aku hanya berharap dia tidur sepanjang malam kali ini..."

    elif M_maria.pregnancy.baby_gender == 'girl':
        tony "Si kecil mulai rewel jadi dia membawanya pulang."

        tony "Aku hanya berharap dia tidur sepanjang malam kali ini..."

    else:
        tony "Anak-anak kecil mulai rewel jadi dia membawanya pulang."

        tony "Aku hanya berharap mereka tidur sepanjang malam kali ini..."

    jump tony_button_pizzeria.choice


label tony_button_pizzeria.curious:
    anon f_normal "{b}Maria{/b} di sekitar?"

    tony f_suspicious "Ya, tentu saja."

    tony @ a_point_back "Dia ada di dapur, seperti biasa."

    tony f_smirk @ a_frustrated "Kenapa kamu bertanya?"

    anon f_shy @ a_behind_head "Oh, aku... Uhh-"

    anon "{i}*Ahem*{/i} Penasaran saja."

    tony @ a_belly f_laugh "Hah, penasaran katanya..."

    tony "Hanya saja, jangan terlalu keras, ya?"

    tony @ a_point f_smirk_wink "Tidak ingin pelanggan mendengarnya."

    anon @ -m_talk "..."
    jump tony_button_pizzeria.choice


label tony_button_pizzeria.deliver:
    anon f_normal "Anda yakin!"

    tony f_normal @ f_laugh "Itu yang ingin saya dengar!"

    tony @ a_point "Aku punya beberapa pai yang ada di konter; dimasak dengan baik dan siap untuk dibawa pergi!"

    tony @ f_smirk "Pastikan kamu menempatkannya di tempat yang benar, capisce?"

    anon @ a_salute f_grin "Ya, tuan!"

    hide anon with dissolve
    tony "Attaboy!"

    tony @ a_finger_up "Anda akan langsung ke puncak, jagoan."

    return


label tony_button_pizzeria.help:
    anon f_normal "Butuh bantuan?"

    tony f_normal "Nah, menyapu membuatku rileks."

    tony "Saya mengerti."

    anon "Baiklah."

    jump tony_button_pizzeria.choice


label tony_button_pizzeria.info:
    anon f_normal "Ada informasi belum?"

    tony f_suspicious "Dengar, aku tahu kamu sangat bersemangat..."

    tony "... Tapi Eddie bisa menjadi bajingan yang sangat licin jika dia tidak ingin ditemukan."

    anon f_worried @ -m_talk "..."
    tony "Saya berjanji, Anda akan menjadi orang pertama yang mengetahuinya begitu saya mendengar kabar darinya."

    tony f_normal @ a_point "Terus lakukan apa yang sedang kamu lakukan, jagoan."

    tony "Setiap pizza yang Anda kirimkan membantu {b}Maria{/b} dan saya lebih dari yang Anda tahu."

    anon f_normal "Ya baiklah."

    jump tony_button_pizzeria.choice


label tony_button_pizzeria.italians:
    anon f_worried "Apa yang Anda ketahui tentang Mafia Italia?"

    tony f_sad a_sides "Heh, {b}Maria{/b} memperingatkanku bahwa dia membocorkan rahasia itu."

    anon "Jadi itu benar kan?"

    tony "Ya itu benar."

    pause
    anon "Bagaimana Anda bisa terlibat dengan massa, {b}Tony{/b}?"

    tony f_suspicious "Yah, sepertinya tidak banyak peluang di luar sana untuk anak yatim piatu yang tidak berpendidikan..."

    tony "Setelah panti asuhan mengirim kami berkemas, kami terpaksa melakukan apa pun yang kami bisa untuk menjaga tempat tinggal dan makanan di perut kami."

    anon @ -m_talk "..."
    tony "Hanya masalah waktu sampai kita terjerumus ke dalam kejahatan."

    anon @ -m_talk "..."
    tony f_sad "Jadi, apa yang ingin kamu ketahui?"


    menu tony_button_pizzeria.mob:
        "Bagaimana Anda bergabung?":

            jump tony_button_pizzeria.join
        "Apakah kamu sudah membunuh orang?":

            jump tony_button_pizzeria.kill
        "Tatonya?":

            jump tony_button_pizzeria.trinacria
        "Mengapa kamu berhenti?":

            jump tony_button_pizzeria.quit
        "Itu sudah cukup.":

            pass

    anon f_normal "Saya tidak perlu mendengar lagi."

    tony f_normal a_idle "Baiklah, bagus."

    jump tony_button_pizzeria.choice


label tony_button_pizzeria.join:
    anon f_worried "Bagaimana Anda bergabung?"

    tony f_suspicious "Oh, itu yang dilakukan Luigi."

    tony "Dia biasa naik kereta bawah tanah bolak-balik, pencopet."

    tony "Dan suatu hari dia tertangkap tangannya di saku Lorenzo Rossi."

    anon @ f_confused "Siapa Lorenzo Rossi?"

    tony "Dia adalah bandar untuk bos mafia."

    anon "Oh."

    tony @ a_frustrated "Ya, Luigi mengira dia sudah mati, pastinya..."

    tony "... Tapi kemudian pria itu bangkit dan menawarinya pekerjaan!"

    anon "Benar-benar?"

    tony "Ya."

    tony "Luigi memutuskan dia lebih suka menjadi karyawan daripada mati, jadi dia menerimanya."

    anon "Masuk akal."

    pause
    tony "Lalu beberapa minggu kemudian, dia mengajakku bergabung."

    anon @ f_surprised "Begitu saja?"

    tony "Ya, kurang lebih."

    tony "Saya harus membuktikan bahwa saya bisa menangani diri saya sendiri terlebih dahulu; tapi kamu kenal aku..."

    tony f_normal @ f_smirk_wink a_fists "Itu tidak masalah."

    pause
    anon "Anda tidak ragu untuk bergabung?"

    tony f_suspicious "Oh, aku punya banyak sekali!"

    tony "Tapi kemudian Anda melihat sekilas betapa menguntungkannya kejahatan terorganisir dan keraguan Anda langsung hilang begitu saja, tahu apa yang saya maksud?"

    anon @ -m_talk "..."
    tony "Aku tahu ini adalah kesempatanku untuk mengukir sesuatu yang baik untuk {b}Maria{/b} dan diriku sendiri."

    tony "Buatlah kehidupan yang layak untuk kami dan kami, lho?"

    jump tony_button_pizzeria.mob


label tony_button_pizzeria.kill:
    anon f_worried "Apakah kamu sudah membunuh orang?"

    tony f_suspicious "Sheesh, kamu baru saja menebaknya, ya?"

    tony "Kau tahu, urusan mafia bukan soal membunuh orang, jagoan."

    tony "Ini lebih tentang memeras mereka."

    tony @ a_money "Mereka menginginkan uang; bukan darah."

    anon @ -m_talk "..."
    tony @ a_fists "Kekerasan hanyalah produk sampingan."

    anon "Jadi, apakah itu jawaban ya?"

    tony f_sad "{i}*Sigh*{/i} Nak, aku melakukan apa yang harus kulakukan untuk bertahan hidup."

    tony "Itu adalah bisnis yang buruk dan saya telah mengalami hal yang sangat buruk."

    tony f_sad_down "Hal-hal yang harus saya jalani selama sisa hari-hari saya."

    pause
    tony f_sad "Hal-hal yang mungkin Anda pikir ingin Anda ketahui... Tapi percayalah, jagoan... Anda tidak tahu."

    anon @ -m_talk "..."
    tony "Bisakah kamu mengerti apa yang aku katakan?"

    anon "Y-ya, menurutku..."

    tony f_suspicious @ a_point_under "Bagus, karena aku benar-benar tidak ingin membicarakan hal itu denganmu."

    jump tony_button_pizzeria.mob


label tony_button_pizzeria.maria:
    anon f_normal "Bagaimana Anda dan {b}Maria{/b} bertemu?"

    tony f_normal a_heart @ f_laugh a_point "Ahh, sekarang ada cerita yang layak diceritakan!"

    tony "{b}Maria{/b} dan saya bertemu ketika kami masih kecil di Brooklyn."

    anon "Kalian dari Brooklyn?"

    tony a_idle @ a_finger_up "Ya itu benar."

    tony "Soalnya, dia berasal dari keluarga berada."

    tony "Ayahnya memiliki restoran mewah di sisi timur dan ibunya pernah menjadi sukarelawan di panti asuhan tempat saya dibesarkan."

    anon "Oh?"

    tony "Kau tahu, menyajikan makanan untuk kita semua tikus jalanan dan menambal pakaian kita."

    tony "Hal semacam itu."

    tony @ f_smirk_wink a_frustrated "Dia adalah wanita yang benar-benar murah hati, ibu {b}Maria{/b} dan apelnya tidak jatuh jauh dari pohonnya."

    pause
    tony "Jadi begini, suatu hari dia membawa {b}Maria{/b} ke panti asuhan bersamanya..."

    tony "Dan mereka berdua membuat keributan, membuat seluruh tempat berbau harum."

    pause
    tony "Maksudku, usianya belum lebih dari tiga belas tahun saat itu, tapi dia sangat pandai di dapur, bahkan saat itu!"

    tony f_smirk_closed a_heart "Fiuh, biar kuberitahu ya... Aku langsung jatuh cinta saat melihatnya."

    tony f_normal a_idle @ f_smirk_wink "Lalu aku mencicipi cannolisnya."

    tony "Aku memberitahunya saat itu juga aku akan menikahinya suatu hari nanti."

    anon f_surprised "Benar-benar?!"

    tony @ -m_talk "Mhmm."

    anon f_normal "Apa yang dia katakan?"

    tony "Ahh, dia menjadi merah seperti bit dan kemudian menyuruhku menutup lubang paiku."

    anon "Maksudmu, dia tidak juga menyukaimu?"

    tony "Nah, dia hanya... Ya-"

    pause
    tony "Yang bagus membuatmu bekerja untuk itu, jagoan."

    tony @ f_smirk_wink "Ingat itu."

    pause
    anon "Jadi kalian berdua sudah lama bersama?"

    tony "Hampir tiga puluh tahun."

    anon "Itu luar biasa, {b}Tony{/b}."

    tony "Bukan?"

    tony @ a_point_back "{i}*Huh*{/i} Wah, butuh waktu lama untuk meyakinkan ayahnya bahwa aku berharga..."

    anon "Dia tidak menyetujuinya?"

    tony f_suspicious @ a_wave "Ahh, tentu saja tidak!"

    tony "Saya hanyalah seorang bukan siapa-siapa tanpa satu sen pun di saku saya."

    tony "Dia tahu aku tidak cukup baik untuk putrinya."

    anon "Tapi Anda membuktikan dia salah?"

    tony f_normal @ f_smirk_wink "Yah, bisa dibilang begitu..."

    tony "Aku mendapatkan pekerjaan, menghasilkan uang yang lumayan, dan menabung setiap sen yang kumiliki selama tiga tahun."

    tony "Kemudian saya membeli sebuah tempat kecil yang bagus di sisi timur dan meminta persetujuan ayahnya."

    anon "Dan?"

    tony @ f_laugh a_belly "Heh, tua tangguh itu mematahkan dua tulang rusukku dan mematahkan rongga mataku."

    anon f_surprised "!!!"
    anon "Sungguh?!"

    tony f_sad "aku tak pernah cukup baik untuknya..."

    show anon f_worried
    tony f_normal @ a_finger_up "... Tapi aku cukup baik untuknya, dan itulah yang penting."

    tony @ f_smirk_wink "Ingat itu, jagoan."

    anon f_normal "Y-ya, oke {b}Tony{/b}."

    pause
    tony @ a_frustrated "Sheesh, dengarkan aku."

    tony "Bergaul seperti wanita tua di salon rambut."

    tony "Bagaimana menurutmu kita akan mengantarkan pizza itu, ya?"

    jump tony_button_pizzeria.choice


label tony_button_pizzeria.quit:
    anon f_worried "Mengapa kamu berhenti?"

    tony f_sad "Eh, pemerasan selama dua puluh tahun mulai membebani seseorang, kau tahu?"

    tony "Saya tidak dapat melakukannya lagi."

    tony "Kemudian Luigi meninggal dan saya menyadari bahwa semua orang yang saya temui ada di dalam tanah atau di penjara."

    pause
    tony "Kami berkemas, meraih {b}Tina{/b} dan gadisnya, lalu segera keluar dari sana."

    tony "Memutuskan untuk mencoba kehidupan tenang untuk sementara waktu."

    anon f_normal "Jadi Anda membuka restoran pizza?"

    tony f_normal "Hehe, kenapa tidak ya?"

    tony "{b}Maria{/b} suka memasak dan tidak banyak restoran di kota kecil ini."

    anon "Itu benar."

    jump tony_button_pizzeria.mob


label tony_button_pizzeria.russians:
    anon f_worried "Tentang orang-orang Rusia itu..."

    tony f_suspicious "Bagaimana dengan mereka?"

    anon "Saya ingin tahu bagaimana Anda mengenal mereka?"

    tony "Ehh, panjang ceritanya ya jagoan.."

    tony "Anggap saja aku pernah berurusan dengan mereka di masa lalu, oke?"

    anon "Baiklah."

    anon "Anda menyebut seseorang bernama {b}Raz{/b}..."

    anon "Siapa dia?"

    tony "{b}Raz{/b} adalah bos mereka."

    anon "Bagaimana cara kerjanya?"

    tony "Apa maksudmu?"

    anon "Maksudku, sejak kapan penjahat punya bos?"

    tony "Mereka Bratva, Nak."

    anon @ f_skeptical "Bratva?"

    tony "mafia Rusia."

    anon f_surprised "!!!"
    tony "Pastinya kamu sudah tahu kan apa itu mafia?"

    anon f_worried "Y-ya, menurutku begitu."

    pause
    anon "Apa yang dilakukan mafia Rusia di Summerville?"

    tony "Pfft, sial kalau aku tahu..."

    tony "... Tapi apapun yang mereka lakukan, itu tidak baik."

    tony "Aku akan memberitahumu itu secara gratis."

    tony "Anda sebaiknya menghindarinya."

    jump tony_button_pizzeria.choice


label tony_button_pizzeria.tattoo:
    anon @ a_point "Tatomu..."

    tony f_suspicious "Anda ingin tahu tentang tatonya, ya?"

    anon "Ya, tuan."

    pause
    anon f_worried "U-kecuali, kamu tidak mau memberitahuku?"

    pause
    anon "Maaf, saya tidak bermaksud mengorek atau tidak-"

    tony f_sad "Ahh, tidak apa-apa, jagoan."

    tony "Aku tidak bisa menyalahkanmu karena penasaran."

    pause
    tony "Ini bukan sesuatu yang biasa saya diskusikan dengan orang yang baru saya kenal."

    anon "Saya mengerti."

    tony f_smirk "Mungkin jika aku mengenalmu lebih baik..."

    anon "Y-ya, oke."

    tony f_normal "Untuk saat ini, anggap saja itu sisa dari kehidupan masa lalu, capisce?"

    anon f_skeptical "Kehidupan masa lalu?"

    tony f_suspicious "Apa, menurutmu aku selalu menjadi penjual pizza?"

    tony a_belly @ f_normal_down a_frustrated "Yesus, lihat aku..."

    tony "Tentu saja Anda berpikir demikian."

    show tony a_idle with dissolve
    anon f_worried "Itu bukan-"

    tony f_smirk "Saya tidak selalu terlihat seperti tukang ledeng Italia yang gemuk, Anda tahu..."

    tony f_normal @ f_laugh "Faktanya, saya dulunya cukup jantan!"

    anon f_normal @ f_laugh "Benar-benar?"

    tony f_suspicious "Ya, sungguh!"

    tony a_fists @ a_point "Asal tahu saja, saya masih punya beberapa pertarungan bagus yang tersisa dalam diri saya."

    tony "Jadi jangan memaksakan keberuntunganmu, kawan bijak."

    anon f_surprised a_up "Wah, aku tidak-"

    tony a_belly f_normal @ f_laugh "Hah!"

    tony a_idle "Tenang, jagoan."

    tony @ f_smirk_wink "Aku hanya ingin menghancurkanmu."

    anon f_worried a_behind_head @ -m_talk "..."
    tony "Kenapa kamu selalu gelisah sepanjang waktu, ya?"

    anon f_sad_down a_idle "Entahlah."

    tony f_suspicious "Kamu seperti kelinci kecil yang ketakutan atau semacamnya..."

    anon "Saya minta maaf."

    tony f_normal @ f_laugh "Dan berhentilah meminta maaf sepanjang waktu!"

    tony "Para wanita benci hal seperti itu, kamu tahu?"

    anon "Y-ya."

    tony f_angry a_fists "Mereka menginginkan pria yang memiliki tulang punggung, ya?!"

    anon @ -m_talk "..."
    tony "Seseorang yang dapat mereka andalkan untuk merawat mereka."

    tony f_suspicious a_idle "Bukankah ayahmu yang mengajarimu hal itu?"

    anon "Tidak juga."

    tony f_sad a_frustrated "Yesus."

    if L_pizzeria_interior.is_here(M_tony):
        show tony a_mc_hip_single:
            xoffset 32
        show tony_arms_dressed_a_mc_shoulder_single:
            flip
            xoffset 32
    else:
        show tony a_mc_hip_single:
            xoffset -32
        show tony_arms_dressed_a_mc_shoulder_single:
            xoffset -32
    with dissolve
    tony "Baiklah, jangan khawatir, jagoan."

    show anon f_shy
    tony f_normal "Paman {b}Tony{/b} akan mengajarimu semua yang perlu kamu ketahui."

    pause
    show tony f_smirk_closed a_finger_up:
        xoffset 0
    hide tony_arms_dressed_a_mc_shoulder_single
    with {'master': dissolve}
    tony "Tapi pertama-tama, Anda harus mengantarkan pizza ini."

    tony f_normal a_frustrated "berubah-ubah?"

    anon @ a_salute "Ya, tuan."

    show tony a_idle with dissolve
    jump tony_button_pizzeria.choice

label tony_button_pizzeria.trinacria:
    anon f_normal "Jadi tentang tato."

    tony f_normal "Oh itu?"

    show tony b_casual a_unbutton1 with dissolve
    pause 1
    tony a_unbutton2 "Heh, itu Trinacria, jagoan."

    tony "Simbol Sisilia yang lebih tua dari tanah."

    tony a_unbutton1 "Banyak orang mafia yang mendapatkannya."

    show tony b_dressed a_idle with dissolve
    anon f_skeptical "Jadi begitu."

    jump tony_button_pizzeria.mob
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
