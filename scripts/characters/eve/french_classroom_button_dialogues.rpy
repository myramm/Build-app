label eve_classroom_dialogue_eve_intro:
    scene expression player.location.background_blur with None
    show eve b_desk_look_left f_normal:
        xoffset 500
    show anon b_desk
    with {'master': dissolve}
    eve "Hei, selamat datang kembali!"

    anon "Hai, {b}Hawa{/b}."

    anon "Wow, saya sangat suka warna rambut baru!"

    show eve a_hair f_laugh with dissolve
    eve "Ya?"

    show eve f_normal a_idle with dissolve
    eve "Aku sedikit khawatir aku tidak bisa melakukannya..."

    anon @ f_laugh "Oh, kamu pasti berhasil!"

    eve @ f_laugh "Hehe terima kasih, {b}[firstname]{/b}..."

    show eve f_nervous
    pause
    eve f_sad "... turut prihatin mendengar tentang ayahmu."

    show anon f_worried
    eve "Saya tahu ini sulit."

    anon "Ya."

    eve "Jika kau perlu bicara atau apalah..."

    anon "Nah, senang sekali Anda menawarkannya, tetapi saya baik-baik saja."

    anon "Aku hanya berusaha untuk tidak memikirkannya."

    anon "Berfokuslah untuk kembali melakukan sesuatu, Anda tahu?"

    eve "Ya, percayalah, {b}[firstname]{/b}... Saya mengerti."

    show eve f_sad_down
    pause
    eve f_nervous_down "Kau tahu, terkadang saat aku sedang merasa sedih atau apalah..."

    eve f_nervous "... Aku mengambil kertas gambarku dan duduk di dekat air mancur besar ini, di taman."

    anon f_shy "Oh ya?"

    eve "Di sana sangat damai, terutama di malam hari..."

    anon "Kedengarannya bagus."

    eve "Dia."

    eve "Anda harus {b}datang memeriksanya{/b}, kapan-kapan."

    anon f_normal "Baiklah, mungkin aku akan melakukannya."

    eve f_laugh "Dingin."

    show eve f_nervous_down
    pause
    anon f_worried "Jadi, apakah Anda akan mengikuti {b}Nona Bissette{/b} untuk les privatnya?"

    eve f_confused "Pelajaran privat?"

    anon "Ya, yang dia bicarakan di awal kelas..."

    anon "Apakah kamu tidak memperhatikan?"

    eve f_laugh "Aku mungkin tertidur sebentar, haha."

    show eve f_normal
    anon "Benar-benar?!"

    eve "Ya, sebagian besar kelas ini membuatku tertidur..."

    anon f_shock "Tapi bukankah Anda memiliki salah satu IPK tertinggi di sekolah?"

    eve f_nervous "Y-ya, agak..."

    anon f_worried "Bagaimana Anda mengaturnya?"

    eve @ f_eyeroll "Oh, entahlah... Hanya beruntung, kurasa..."

    anon f_shy "Apa, itu gila..."

    eve @ f_laugh "Tidak, aku serius!"

    eve "Aku selalu pandai di sekolah."

    eve "Itu seperti hadiah atau semacamnya, aku tidak bisa menjelaskannya."

    anon "Ya, itu hadiah yang luar biasa."

    eve f_eyeroll "Ya, menurutku..."

    show eve f_nervous_down
    pause
    show anon f_normal
    pause
    anon "Aku bisa mengeritingkan lidahku."

    eve f_confused "Hmm?"

    show eve f_nervous
    show anon f_unimpressed_tongue
    pause
    anon @ -m_talk "kamu?"

    eve @ f_laugh "hehe!"

    show eve f_happy
    show anon f_grin
    pause
    anon f_normal "Itu benar-benar satu-satunya hadiahku."

    anon "Aku akan menukarmu?"

    eve @ f_laugh "Heh, mmm... Menggiurkan tapi tidak."

    anon "Sial."

    show eve f_nervous_down
    show anon f_shy_down
    pause
    show eve f_nervous
    pause
    eve "Serius {b}[firstname]{/b}, jika kamu butuh jemput aku... {b}Ayo temui aku di taman{/b}."

    show anon f_normal zorder 3
    eve @ f_wink "Bawalah selera humor itu bersama Anda."

    anon "Ya baiklah."

    anon "{b}Taman di malam hari{/b} ya?"

    eve f_laugh "Ya!"

    show expression "characters/eve/eve_overlay_o_chair.png" zorder 0:
        xpos 450
    show eve f_happy b_dressed zorder 1:
        xoffset -100
    show expression "characters/eve/eve_overlay_o_desk.png" zorder 2:
        xpos 500
    with {'master': dissolve}
    eve "Saya harus pergi."

    eve "{b}Nona Ross{/b} mempunyai proyek seni yang ingin dia bicarakan dengan saya..."

    anon "Baiklah."

    show eve a_wave with {'master': dissolve}
    eve "Nanti, {b}[firstname]{/b}!"

    anon @ f_laugh "Sampai jumpa!"

    hide eve
    with {'master': dissolve}
    return

label eve_classroom_dialogue_talent_show_help:
    show eve b_desk_look_left:
        xoffset 500
    show anon b_desk f_normal
    anon "Apakah Anda memainkan instrumen apa pun?"

    eve "Tidak, saya tidak memainkan alat musik apa pun. Saya selalu ingin belajar tetapi saya tidak punya waktu, Anda tahu?"

    anon f_worried "Oke, bagaimana kalau bernyanyi?"

    eve f_nervous_down "Oh, um..."

    eve "Ya, aku suka menyanyi, kurasa... Tapi aku tidak tahu apakah aku pandai."

    if M_eve.finished_state(S_eve_visit_bedroom):
        anon f_normal "Oh, ayolah! Aku pernah mendengarmu bernyanyi di taman sebelumnya, kamu hebat!"

        anon "Kami sangat membutuhkan lebih banyak sukarelawan."

        eve "K-kamu benar-benar berpikir aku penyanyi yang baik?"

        pause
        eve f_nervous "Saya tidak tahu apakah saya bisa bernyanyi di depan seluruh sekolah? Kedengarannya cukup memalukan..."

        eve f_nervous_down @ a_hair "Saya belum pernah bernyanyi untuk orang banyak sebelumnya."

    else:
        anon f_normal "Saya yakin Anda memang demikian! Anda harus mendaftar untuk pertunjukan bakat bersama saya!"

        anon "Kami sangat membutuhkan lebih banyak sukarelawan."

        eve "Ya, entahlah."

        eve f_nervous "Anda ingin saya bernyanyi di depan seluruh sekolah? Kedengarannya cukup memalukan..."

        eve f_nervous_down @ a_hair "... Dan aku sudah lama tidak bernyanyi. Tidak sejak mesin karaokeku rusak."

    eve "Aku sudah kehabisan latihan."

    anon @ f_thinking -m_talk "Hmm..."

    anon "Anda tahu, saya pikir teman saya {b}Erik{/b} memiliki {b}mesin karaoke{/b} di ruang bawah tanahnya."

    eve f_nervous "Oh ya?"

    anon "Benar sekali!"

    if M_eve.finished_state(S_eve_visit_bedroom):
        anon "Anda bisa berlatih di sana dan membangun kepercayaan diri Anda!"

    else:
        anon "Anda harus datang kapan-kapan dan berlatih!"

    eve @ f_laugh "Heh, kamu ingin aku bernyanyi untukmu dan temanmu?"

    anon "Nah, kita semua bisa bernyanyi bersama! Ayo, kita akan melakukannya malam ini, pasti menyenangkan!"

    eve f_nervous_down @ -m_talk "..."
    eve f_nervous "Baiklah, kurasa aku bisa mampir sebentar."

    anon @ f_laugh "Luar biasa!"

    anon "{b}Sampai jumpa di rumah Erik malam ini{/b}."

    return

label eve_classroom_dialogue_adehsive:
    show eve b_desk_look_left f_normal:
        xoffset 500
    show anon b_desk f_normal
    anon "Apa rencananya lagi?"

    eve "Anda seharusnya {b}bertemu Kevin di laboratorium sains setelah kelas{/b}."

    eve "Ingat?"

    anon "Oh, benar. Terima kasih, {b}Hawa{/b}!"

    return

label eve_classroom_dialogue_bissettes_reward:
    show eve b_desk_look_left f_normal:
        xoffset 500
    show anon b_desk f_normal
    anon "Apakah Anda akan mendaftar untuk dibimbing oleh {b}Nona Bissette{/b}?"

    eve "Saya sudah melakukannya dengan cukup baik, jadi tidak ada gunanya mencoba."

    anon "Kenapa tidak?"

    eve f_confused "Ya, Anda tidak bisa benar-benar meningkatkan nilai A+."

    eve f_nervous "Kemungkinan besar dia akan memilih seseorang sepertimu..."

    anon "Aku?"

    eve "Ya, ya... Anda sedang gagal saat ini, bukan?"

    eve "Anda punya banyak ruang untuk perbaikan."

    eve "Ditambah lagi, {b}Nona Bissette{/b} menyukai laki-laki."

    eve "Anda harus mempertimbangkannya dengan serius."

    return

label eve_classroom_dialogue_hang_out:
    show eve b_desk_look_left f_nervous:
        xoffset 500
    show anon b_desk f_normal
    if M_eve.finished_state(S_eve_pot_cheerup):
        anon "Apakah kamu masih nongkrong di taman?"

        eve "Tidak, {b}Sekarang saya kebanyakan berkeliaran di rumah pada malam hari{/b}."

    else:
        anon "Tadi kamu bilang kamu nongkrong di mana?"

        eve "{b}Saya biasanya nongkrong di taman pada malam hari{/b}."

    eve "Anda harus mampir kapan-kapan."

    anon "Baiklah, aku akan melakukannya."

    eve f_nervous_down "Hehe, keren!"

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
