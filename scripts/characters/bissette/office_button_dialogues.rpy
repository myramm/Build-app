label bissette_dialogue_office_bissette_roxxy_exam_convince:
    show teacher 1 at right
    show player 10 at left
    with dissolve
    player_name "Apa yang harus saya lakukan lagi?"

    show player 5
    show teacher 5
    bissette "As-tu oublié?"

    bissette "Anda harus {b}meyakinkan Roxxy untuk hadir dalam ujian{/b}."

    bissette "Jika tidak, nilai rata-rata seluruh kelas akan menurun."

    show teacher 4
    show player 14
    player_name "Oh benar!"

    player_name "Jangan khawatir, {b}Nona Bissette{/b}! Saya ikut!"

    return

label bissette_dialogue_office_bissette_roxxy_convinced:
    show teacher 1 at right
    show player 10 at left
    with dissolve
    player_name "{b}Nona Bissette{/b}?"

    show player 13
    show teacher 5
    bissette "Ya?"

    show teacher 4
    show player 14
    player_name "Saya meyakinkan {b}Roxxy{/b} untuk hadir dalam ujian!"

    show player 13
    show teacher 2
    bissette "Sungguh-sungguh?!"

    show teacher 1
    show player 17
    player_name "Ya!"

    show teacher 25 zorder 1 with dissolve

    bissette "Tu aku sauve la vie!"

    show teacher 26 with dissolve
    bissette "Apapun yang akan aku lakukan tanpamu?!"

    show teacher 27 with dissolve
    show player 29 with dissolve
    player_name "Hehe, itu bukan masalah besar..."

    show player 13
    show teacher 16
    with dissolve
    bissette "Sekarang pastikan untuk mempelajari kata-kata yang kami pelajari dari tugas Anda sebelumnya, ya?"

    show teacher 17
    show player 14
    player_name "Saya akan! Jangan khawatir!"

    show player 13
    show teacher 16
    bissette "Sangat bagus! Kelas berikutnya kita akan mengadakan tes."

    show teacher 17
    show player 14
    player_name "Baiklah, {b}Nona Bissette{/b}!"

    return

label bissette_dialogue_office_intro:
    show teacher 3 at right
    show player 13 at left
    with dissolve
    bissette "Halo, {b}[firstname]{/b}!"

    show teacher 1
    show player 14
    player_name "Halo, {b}Nona Bissette{/b}."

    show player 13
    show teacher 2
    bissette "Apa yang bisa saya bantu?"

    show teacher 1
    return

label bissette_dialogue_office_bissette_wine_sampling:
    player_name "Saya sangat bersemangat untuk mencicipi anggur itu, {b}Nona Bissette{/b}."

    show player 13
    show teacher 12
    bissette "Aku benci hal yang sama!"

    bissette "Anda akan mencicipi banyak hal malam ini, bukan?"

    show teacher 13
    show player 29 with dissolve
    player_name "{i}*Gulp*{/i} Y-ya..."

    show player 14
    show teacher 3
    bissette "Très bien, sampai jumpa di kantorku malam ini."

    show teacher 13
    show player 14 with dissolve
    player_name "Sampai jumpa di sana!"

    return

label bissette_dialogue_office_leave:
    show player 14
    player_name "Kurasa aku tidak membutuhkan apa pun saat ini."

    show player 13
    show teacher 2
    bissette "Sangat bagus!"

    show teacher 1
    show player 36 with dissolve
    player_name "Selamat tinggal!"

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
