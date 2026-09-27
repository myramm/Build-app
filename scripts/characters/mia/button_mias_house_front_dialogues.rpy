label mia_dialogue_mias_house_front_intro:
    scene location_mia_closeup
    show player 14 at left
    show old_mia 1 at right
    with dissolve
    player_name "Hai {b}Mia{/b}!"

    show old_mia 4
    show player 1
    mia "Hai {b}[firstname]{/b}!"

    mia "Apa yang kamu lakukan di sini?"

    show old_mia 1
    show player 29
    player_name "Umm... aku ingin menanyakan sesuatu padamu!"

    return

label mia_dialogue_mias_house_front_homework:
    show player 21
    player_name "Apakah Anda masih memerlukan bantuan belajar untuk ujian?"

    show old_mia 3
    show player 13
    mia "Tentu saja! Aku sedang mencari seseorang untuk belajar bersama..."

    show old_mia 6
    show player 11
    mia "... Tapi apakah kamu sudah mengikuti kelas?"

    show old_mia 2
    show player 10
    player_name "Oh! Benar! Saya mungkin harus {b}mendapatkan les privat dari Nona Bissette{/b} untuk mengejar ketinggalan..."

    show old_mia 6
    show player 13
    mia "Ya, Anda mungkin harus melakukannya dulu!"

    show old_mia 4
    mia "Lalu kamu bisa datang ke rumahku... Dan kita akan belajar di kamarku!"

    show old_mia 1
    show player 14
    player_name "Kamu... Ya?"

    show old_mia 3
    show player 1
    mia "Tentu! Ini akan menyenangkan!"

    show old_mia 1
    show player 17
    player_name "Baiklah... Saya akan memberi tahu Anda jika saya sudah selesai menggunakannya!"

    show old_mia 4
    show player 1
    mia "Sampai berjumpa lagi!"

    hide old_mia with dissolve
    show player 5 with dissolve
    player_name "(Saya harus mencoba dan {b}menyelesaikan pekerjaan rumah bahasa Prancis saya{/b}, sehingga saya bisa belajar dengan {b}Mia{/b}. )"

    show player 4
    pause
    player_name "(Saya bertanya-tanya mengapa dia memilih saya untuk membantunya belajar.)"

    player_name "(Dia biasanya belajar dengan {b}Judith{/b}, dan dia sangat pandai dalam bahasa Prancis... )"

    player_name "(Saya tidak yakin bagaimana saya bisa membantunya.)"

    show player 13
    player_name "(Setidaknya kita bisa jalan-jalan, dan dia sangat manis...)"

    hide player with dissolve
    return

label mia_dialogue_mias_house_front_leave:
    show player 4
    player_name "Hmm... Iya, tapi aku lupa!"

    show old_mia 3
    show player 11
    mia "Ha ha! Kamu lucu~."

    show old_mia 1
    show player 17
    player_name "Maaf! Saya tidak ingat apa yang ingin saya katakan!"

    show player 14
    player_name "Saya harus pergi."

    show old_mia 4
    show player 1
    mia "Selamat malam!"

    hide player
    hide old_mia
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
