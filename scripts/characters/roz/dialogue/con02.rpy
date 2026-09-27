label con02_job3_roz:
    scene hospital_desk
    show roz:
        flip
        xoffset -200
    show roz_desk as desk at left
    show consuela b_casual:
        xoffset 100
    show anon:
        flip
        xoffset -100
    with dissolve
    anon "B-permisi?"

    roz "Apa yang kamu inginkan, Nak?"

    anon "Teman saya di sini sedang mencari pekerjaan..."

    anon "Anda tidak akan merekrut karyawan, bukan?"

    roz @ -m_talk "..."
    roz "Dia tidak terlihat seperti dokter bagiku..."

    anon @ f_surprised "Dokter?!"

    anon @ f_laugh "Tidak, tidak, dia bukan seorang dokter."

    anon "Umm, kami berharap kamu mendapat lowongan untuk staf kebersihanmu?"

    roz @ -m_talk "Hmm."

    roz "Ya, kebetulan saja kita melakukannya."

    anon @ f_surprised "Benar-benar?"

    roz "Ya, salah satu petugas kebersihan malam kami secara tidak sengaja masuk ke ruang isolasi minggu lalu..."

    roz "Mendapat kasus demam kuning yang parah."

    anon f_shock "!!!"
    roz "Dan saya tidak berbicara tentang fetish Asia..."

    anon f_worried "O-oh?"

    roz "Apakah teman Anda berbicara bahasa Inggris?"

    show anon with dissolve:
        unflip
        xoffset 400
    anon "Ehh..."

    consuela f_annoyed "What is she asking?" (show_native="¿Qué está preguntando ella?")
    show anon with dissolve:
        flip
        xoffset -100
    anon "Tidak juga."

    roz @ -m_talk "..."
    anon "Namun dia adalah seorang pekerja keras, dan dia sangat membutuhkan pekerjaan itu!"

    roz "Tidak bisa membantumu."

    anon "Ah, ayolah!"

    roz "Kita tidak bisa begitu saja mempekerjakan orang di luar jalan untuk masuk ke sini, kau tahu?"

    roz "Bagaimana saya bisa memberinya arahan jika dia tidak bisa berbahasa Inggris?!"

    anon @ f_normal "Dia cukup baik dengan perintah sederhana dan gerakan tangan..."

    roz "Pfft, kuharap kamu bercanda!"

    pause
    anon f_sad "Tolong, punya hati!"

    roz "Saya tidak punya waktu untuk ini."

    anon "Dengar, ini salahku dia dipecat dari pekerjaan terakhirnya dan dia punya keluarga yang harus dinafkahi..."

    roz @ -m_talk "..."
    anon "Tolong, aku akan melakukan apa saja!"

    show roz f_smirk
    pause
    roz "Apa pun?"

    anon f_normal "Ya."

    pause
    roz "Berputar ke arahku dengan sangat cepat."

    anon f_worried @ -m_talk "Hmm?"

    roz "Ayolah, aku ingin melihatmu dengan baik."

    show anon f_worried_left a_up with dissolve:
        unflip
        xoffset 400
    anon "Seperti ini?"

    pause
    roz "Ya, begitu saja."

    consuela "This is getting weird..." (show_native="Esto está raro...")
    roz @ -m_talk "Hmm."

    roz "Baiklah, menurutku kita bisa menyelesaikan sesuatu."

    show anon f_worried -a_up with dissolve:
        flip
        xoffset -100
    anon "Ya?"

    roz "{b}Kita harus naik ke ruang penyimpanan lantai dua{/b} dan mengambil seragam dan lencananya."

    show anon f_normal a_idle with dissolve:
        unflip
        xoffset 400
    anon "Anda dengar itu?"

    consuela "saya membersihkan?"

    anon @ f_laugh "Ya, kamu bersih-bersih!"

    show consuela f_normal
    anon "Ikuti dia ke atas dan ambil seragammu."

    consuela "Seragam?"

    anon "Ya."

    consuela "Oke, aku pergi."

    roz @ a_stop "Ah, ah, ah!"

    roz "Ikuti saja, Nak."

    show consuela f_annoyed
    show anon f_worried with dissolve:
        flip
        xoffset -100
    anon "Hah?"

    roz "Dia tetap di sini."

    anon @ -m_talk "..."
    roz "Ayo."

    hide roz with dissolve
    consuela "saya pergi?"

    show anon f_worried with dissolve:
        unflip
        xoffset 400
    anon "Uhh, t-tidak..."

    anon @ a_point_self "saya pergi."

    anon "Anda tinggal."

    consuela "saya tinggal?"

    anon "Y-ya."

    anon f_thinking @ -m_talk "(Aku ingin tahu apa yang dia ingin aku lakukan?)"

    roz "Kamu datang atau apa?"

    anon f_surprised "!!!"
    show consuela f_sad a_cross with dissolve
    anon f_worried_left "Y-ya, Bu."

    anon f_normal "Aku akan segera kembali, oke?"

    consuela "O-oke."

    hide anon with dissolve
    consuela f_sad_down @ -m_talk "..."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
