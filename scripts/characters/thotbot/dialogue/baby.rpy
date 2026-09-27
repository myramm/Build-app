label thotbot_button_baby:
    show anon behind thotbot with dissolve
    anon "Halo, {b}Rosita{/b}."

    show thotbot with dissolve:
        flip
        xoffset 0
    thotbot "Salam, rekan karyawan!"

    thotbot "Sayangnya, saya sedang dalam mode penitipan anak dan tidak dapat memberikan bantuan kepada Anda saat ini."

    anon @ f_confused "Hah?"

    anon "O-oh, tidak apa-apa."

    anon "Saya baru saja memeriksa untuk melihat bagaimana keadaan si kecil."

    thotbot "{b}Ny. Anak Melonia{/b} baik-baik saja."

    thotbot "Sistem penyimpanan nutrisinya hampir mencapai kapasitasnya dan kebutuhan emosionalnya saat ini terpenuhi."

    anon f_shy "Wow, umm... Oke."

    thotbot "Apakah Anda memiliki pertanyaan tentang perawatannya?"


    menu thotbot_button_baby.choice:
        "Apakah kamu yakin bisa mengatasi ini?":

            jump thotbot_button_baby.concern
        "Butuh bantuan?":

            jump thotbot_button_baby.lullaby
        "Aku serahkan padamu.":

            pass

    anon f_normal "Aku serahkan padamu."

    thotbot "Semoga sukses dengan tugas Anda, rekan karyawan!"

    anon f_worried "Ya, um..."

    pause
    anon f_shy @ a_wave "... Terima kasih."

    hide anon with dissolve
    return


label thotbot_button_baby.concern:
    anon f_worried "Apakah kamu yakin bisa mengatasi ini?"

    anon "Bayi bisa menjadi segelintir..."

    thotbot "Tidak perlu khawatir, rekan karyawan."

    thotbot "Unit ini baru-baru ini dianugerahi peringkat A+ dalam membesarkan dan mengasuh anak oleh Majalah Robot Quarterly."

    anon f_skeptical "Majalah Robot Triwulanan?"

    thotbot "Pemrograman saya memungkinkan saya merawat hingga delapan anak dengan baik sekaligus."

    anon f_normal "Benar-benar?"

    anon "Itu umm... Rapi, menurutku..."

    thotbot "Saya yakinkan Anda, anak ini ditinggalkan dengan pelengkap logam yang bagus."

    anon f_worried @ -m_talk "..."
    thotbot "Apakah Anda punya pertanyaan lain?"

    jump thotbot_button_baby.choice


label thotbot_button_baby.lullaby:
    anon f_normal "Butuh bantuan?"

    thotbot "Anda baik hati menawarkannya tetapi itu tidak perlu."

    show anon f_sad
    pause
    thotbot "Saya akan memulai dengan lagu pengantar tidur tradisional sebelum menempatkan anak ke mode REM."

    anon f_worried "Modus REM?"

    thotbot "Saya yakin Anda manusia menyebutnya sebagai, \"Waktu tidur siang\"."

    anon "Oh, begitu."

    thotbot "Apakah Anda ingin memilih lagu dari perpustakaan saya yang telah disetujui sebelumnya?"

    anon "Perpustakaan?"

    thotbot "Saat ini saya dilengkapi dengan lebih dari tiga ratus lagu pengantar tidur."

    anon f_surprised "Wah, tiga ratus?!"

    thotbot "Bolehkah saya merekomendasikan, {i}Bayi Robot Hiu{/i}?"

    anon f_disgusted "Ehh..."

    thotbot "Atau mungkin, {i}Apa Kata Robot Rubah?{/i}"

    anon @ -m_talk "..."
    thotbot "{i}Lima Robot Bebek Kecil{/i}?"

    anon f_worried "Apakah Anda punya sesuatu tanpa robot?"

    show thotbot f_error
    pause
    thotbot f_normal "Anda telah memilih, {i}Turun ke Mechanical Bay{/i}."

    anon f_skeptical "Apa yang-"

    thotbot "♪ Di dekat ruang mekanis. ♪"

    thotbot "♪ Dimana CPU memberikan respons keluaran yang sesuai terhadap rangsangan eksternal. ♪"

    show anon f_worried
    thotbot "♪ Kembali ke stasiun pengisian dayaku. ♪"

    thotbot "♪ Baterai saya akan mendapat arus listrik dari sumber listrik DC konstan atau DC berdenyut. ♪"

    show anon f_sad_down
    thotbot "♪ Jika aku tidak melakukannya. ♪"

    thotbot "♪ Hasilnya pasti... ♪"

    thotbot "♪ Kegagalan daya yang sangat besar menyebabkan sistem mati total dan kemungkinan kehilangan memori. ♪"

    anon "Itu sungguh, um..."

    thotbot "♪ Di dekat ruang mekanis!! ♪"

    anon @ f_hurt a_facepalm -m_talk "..."
    jump thotbot_button_baby.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
