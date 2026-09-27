label button_cedric_about_jenny:
    show player 10
    player_name "Kamu tahu dia sedang berusaha menghubungimu, kan?"

    show player 5
    show cedric
    cedric "Ya, percayalah... Aku tahu."

    cedric "Aku tidak ingin ada hubungannya dengan wanita jalang gila itu!"

    show player 12
    player_name "Itu sedikit kasar."

    show player 5
    cedric "Anda tahu dia terlibat dalam film porno atau semacamnya?"

    show player 10
    player_name "Y-ya, aku tahu."

    show player 5
    cedric "Sekarang dia mencoba membujukku untuk melakukannya juga!"

    show player 10
    player_name "Eh ya?"

    show player 5
    cedric "Apa aku terlihat seperti pria yang suka melakukan film porno?!"

    show player 29 with dissolve
    player_name "Err, entahlah... Agak?"

    show player 3
    cedric "Ya, baiklah... aku tidak!"

    cedric "Dia hanya perlu mencari orang lain untuk menancapkan cakarnya."

    cedric "Aku sudah selesai dengannya."

    show player 5 with dissolve
    player_name "..."
    show player 10
    player_name "Setidaknya maukah kamu menelepon dan memberitahunya hal itu?"

    show player 5
    cedric "Kenapa, supaya dia bisa membentak dan memanggilku dengan nama buruk?"

    cedric "Tidak, terima kasih."

    cedric "Katakan padanya."

    hide cedric with dissolve
    pause
    show player 37 with dissolve
    player_name "{i}*Huh*{/i} Sial."

    player_name "( {b}[jen_name]{/b} tidak akan menyukai ini... )"

    player_name "(Sebaiknya aku pergi dan memberi tahu dia.)"

    hide player with dissolve
    return

label button_cedric_see_ya:
    show player 14
    player_name "Saya harus pergi."

    show player 13
    show cedric f_normal
    cedric "Ya baiklah."

    cedric "Sampai jumpa, sobat kecil."

    hide player with dissolve
    pause
    cedric "Jangan melewatkan hari leg sekarang, heh!"

    hide cedric with dissolve
    return

label button_cedric_can_you_spot_me:
    show player 10
    player_name "Bisakah kamu melihatku?"

    show player 13
    show cedric f_normal a_reject with dissolve
    cedric "Tidak bisa, sobat kecil."

    show player 5
    cedric "Anda belum siap untuk berolahraga dengan orang-orang besar."

    show cedric a_idle with dissolve
    player_name "..."
    show cedric a_point with dissolve
    cedric "Aku tidak ingin melihatmu terjatuh atau o-ringmu meledak."

    show cedric a_idle with dissolve
    show player 10
    player_name "Uh huh, terima kasih untuk apa pun."

    show player 5
    cedric "Ah, tidak perlu pusing memikirkan hal itu."

    cedric "Anda akan segera sampai di sana."

    cedric "Lihat ini!"

    show cedric a_flex with dissolve
    show player 13
    pause
    cedric "Aku menjadi sangat terkoyak, ya?"

    show player 14
    player_name "Tentu, {b}Cedric{/b}..."

    show player 13
    show cedric a_idle with dissolve
    cedric "Hehe, oh ya!"

    return

label button_cedric_what_have_you_been_up_to:
    show player 14
    player_name "Apa yang sedang kamu lakukan?"

    show player 13
    show cedric f_normal
    cedric "Oh, semuanya luar biasa!"

    cedric "Karena aku akhirnya berhasil menyingkirkan teman sekamarmu yang harpy itu, aku akhirnya bisa fokus pada latihanku."

    show player 4
    player_name "Hah."

    show player 14 with dissolve
    player_name "Yah, itu bagus... kurasa."

    show player 13
    cedric "Ini sangat bagus, sobat kecil!"

    show cedric a_point_himself with dissolve
    cedric "Kau mau datang melihatku melakukan dead lift?"

    cedric "Berat badan saya mencapai empat ratus lima pon!"

    show cedric a_idle with dissolve
    show player 29 with dissolve
    player_name "Eh, mungkin lain kali..."

    show player 13 with dissolve
    cedric "Sesuaikan dirimu."

    return

label button_cedric_intro_repeat:
    scene expression player.location.background_closeup with None
    show player 13 at left
    show cedric
    cedric "Ada apa, sobat kecil?"

    show player 14
    player_name "Oh, hai {b}Cedric{/b}."

    show player 13
    cedric "Anda di sini untuk menambah jumlah?"

    return

label button_cedric_intro_first:
    scene expression player.location.background_closeup with None
    show cedric
    show player 13 at left
    cedric "Wah, {b}[firstname]{/b}?"

    show player 14
    player_name "Oh, hai {b}Cedric{/b}."

    show player 13
    cedric "Aku sudah lama tidak bertemu denganmu, sobat kecil."

    show player 14
    player_name "Eh ya."

    show player 13
    show cedric a_point with dissolve
    cedric "Anda akhirnya memutuskan untuk pergi ke gym dan menambah berat badan?"

    show cedric a_idle with dissolve
    show player 29 with dissolve
    player_name "Y-ya, sesuatu seperti itu..."

    show player 13 with dissolve
    cedric "Bagaimana {b}[jen_name]{/b}?"

    show player 12
    player_name "Umm, entahlah... Judes?"

    show player 13
    cedric "Hahaha, bagus!"

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
