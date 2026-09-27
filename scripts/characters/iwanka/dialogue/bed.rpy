label iwanka_button_bed:
    show anon b_onbed_back f_shy with dissolve:
        offset (-100, 20)
    iwanka "{i}*Menguap*{/i} Selamat pagi, {b}[firstname]{/b}."

    anon "Selamat pagi."

    iwanka f_smirk "Kamu datang lebih awal..."

    anon f_flirt "Ya, menurutku."

    iwanka f_annoyed "Ibuku tidak membuatmu bekerja terlalu keras, kan?"


    menu iwanka_button_bed.choice:
        "Tidak, tidak apa-apa.":
            jump iwanka_button_bed.mother
        "Anda telanjang.":

            jump iwanka_button_bed.naked
        "Tentang ayahmu...":

            jump iwanka_button_bed.father
        "Seks oral.":

            jump iwanka_button_bed.blowjob
        "Seks.":

            jump iwanka_button_bed.sex
        "Saya tidak bisa tinggal.":

            pass

    anon f_normal "Saya tidak bisa tinggal."

    iwanka f_pouting "Tunggu, kamu sudah berangkat?!"

    anon "Ya, maaf..."

    iwanka "Tapi aku benar-benar akan melompati tulangmu!"

    anon "Mungkin lain kali."

    iwanka f_sad "Aduh..."

    hide anon with dissolve
    return


label iwanka_button_bed.blowjob:
    anon f_normal "Bolehkah memberiku pekerjaan pukulan?"

    iwanka f_smirk "Sebuah pekerjaan pukulan?"

    iwanka "Baiklah, menurutku itu adil setelah semua yang telah kamu lakukan untukku."

    show anon f_flirt
    show iwanka b_naked:
        reset
        offset (0, 0)
    with slowdissolve
    pause
    iwanka "Heh, kenapa kamu menatapku seperti itu?"

    anon @ -m_talk "Hmm?"

    anon f_shy "T-tidak ada, aku hanya-"

    pause
    anon f_flirt "Kamu benar-benar seksi."

    iwanka @ f_eyeroll "Hmm, ya."

    iwanka a_hip "Apakah kita melakukan ini atau apa?"

    anon "Ya, tolong."

    iwanka "Kemudian mendekat ke tepi tempat tidur."

    anon "Y-ya, oke."


    call scene_iwanka_blowjob.bedroom
    $ unlock_scene('iwanka', '01_unlocked', variant='bedroom')

    scene expression background(288, 368, 3.5) as stage
    show iwanka b_magic o_cum f_smirk
    show anon f_flirt
    with fade
    anon "Terima kasih telah melakukan itu."

    iwanka "Tidak masalah."

    iwanka @ f_laugh "Itu menyenangkan!"

    pause
    iwanka "Sekarang, permisi..."

    iwanka "... Aku akan membersihkan diriku sendiri."

    anon "Y-ya, tentu saja."

    anon @ a_wave "Sampai jumpa nanti."

    iwanka "Sampai jumpa, {b}[firstname]{/b}."

    hide anon with dissolve
    return 'afterglow'


label iwanka_button_bed.father:
    anon f_worried "Tentang ayahmu."

    iwanka f_excited @ f_laugh "Ya ampun, sungguh luar biasa dia pergi!"

    iwanka "Saya pada dasarnya dapat melakukan apapun yang saya inginkan sekarang!"

    show iwanka f_smirk
    pause
    show anon f_shy
    iwanka "Omong-omong..."

    iwanka "... Kupikir kau dan aku harus jalan-jalan ke suatu tempat!"

    anon "Oh?"

    iwanka "Apakah Anda pernah ke Prancis?"

    anon f_surprised "Prancis?!"

    iwanka "Ya, seharusnya SUPER romantis di sana!"

    anon "Saya tidak bisa pergi ke Prancis!"

    iwanka "Kenapa tidak?"

    iwanka "Aku akan membayar semuanya dan kita bisa pergi berbelanja dan membelikanmu lemari pakaian baru."

    anon f_worried @ -m_talk "..."
    iwanka "Jika kamu ingin menjadi pacarku, kamu harus berpenampilan seperti itu."

    jump iwanka_button_bed.choice


label iwanka_button_bed.mother:
    anon f_normal "Tidak, tidak apa-apa."

    iwanka f_smirk "Heh, pekerjaanmu saat ini kebanyakan hanya menidurinya, ya?"

    anon f_worried "Ehh, ya... Bisa dibilang begitu."

    iwanka f_disgusted "Bruto."

    pause
    iwanka "Yah, setidaknya itu menjauhkan dia dari rambutku."

    iwanka f_smirk "Cobalah untuk tidak mematahkan pinggulnya, ya?"

    jump iwanka_button_bed.choice


label iwanka_button_bed.naked:
    anon f_shy "Anda telanjang."

    iwanka f_smirk "Ya, baiklah..."

    iwanka "Saya pikir ibu saya yang melakukannya, jadi mengapa saya tidak juga?"

    iwanka "Aku tidak akan membiarkan dia bersenang-senang."

    anon @ a_take "Hei, aku tidak mengeluh."

    jump iwanka_button_bed.choice

label iwanka_button_bed.sex:
    anon f_flirt "Ingin melakukannya?"

    iwanka f_excited @ f_laugh "Tentu saja!"

    show iwanka f_lipbite
    show anon b_dressed_changing3 f_flirt:
        align (0., 1.)
        offset (-80, 0)
        zoom 1.05
    with dissolve
    pause
    show iwanka f_smirk_down
    show anon b_dressed_changing2
    with dissolve
    pause
    show anon b_naked_undress_bottom with dissolve
    pause
    show iwanka f_lipbite
    show anon b_naked od_naked_dick1
    with dissolve
    pause
    iwanka f_excited "Pastikan saja kamu benar-benar meniduriku kali ini!"

    iwanka "Dan mungkin membuatku sedikit tersedak."

    anon f_surprised "Hah?!"

    iwanka "Ayolah!"


    call scene_iwanka_sex.bedroom
    $ unlock_scene('iwanka', '02_unlocked', variant='bedroom')

    scene location_rump_iwanka_bed_closeup
    show iwanka b_onbed_cuddle_naked f_content_closed
    show anon b_empty f_flirt_low:
        xzoom -1
        offset (84, -17)
    show anon_overlay_dick_onbed_naked_od_dick1
    with fade
    iwanka "Hmm, bagus sekali!"

    anon "Y-ya, kamu juga."

    pause
    show iwanka f_excited_up
    iwanka "Aku yakin ibuku tidak akan bercinta seperti itu..."

    anon @ f_laugh "Tidak, dia tidak melakukannya."

    iwanka @ f_laugh "hehe!"

    iwanka f_content_closed "Kau tahu, kau bisa jalan-jalan sebentar..."

    iwanka "... Jika kamu mau."

    anon "Oh?"

    iwanka "Ya, aku suka berbaring di sini bersamamu."

    iwanka "Itu ummm, entahlah..."

    anon "Bagus?"

    iwanka @ f_excited_up "... Ya."

    iwanka "Bagus."

    anon "Baiklah, tapi hanya sebentar."

    iwanka "Mm, oke."

    pause
    iwanka "Terima kasih, {b}[firstname]{/b}."


    scene expression background(288, 368, 3.5, o=1) as stage
    show anon
    show iwanka b_naked f_excited
    with slowfade
    iwanka "Itu menyenangkan!"

    anon "Ya, benar."

    hide anon
    show iwanka b_naked_kiss:
        xoffset -200
    with dissolve
    pause
    show iwanka b_naked:
        xoffset 0
    show anon f_shy
    with dissolve
    iwanka "Ayo segera lakukan lagi, oke?"

    anon "Tentu saja."

    hide anon with dissolve
    return 'afterglow'
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
