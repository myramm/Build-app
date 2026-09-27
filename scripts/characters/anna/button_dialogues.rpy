label anna_dialogue_anna_dog_hunt:
    show player 11 at left with dissolve
    show old_anna 5 at right with dissolve
    anna "Hai {b}[firstname]{/b}, pernahkah Anda melihat {b}anjing kecil{/b} tanpa tali??"

    show old_anna 4
    show player 10
    player_name "Saya kira tidak demikian..."

    show old_anna 5
    show player 11
    anna "Saya pikir saya kehilangan dia."

    anna "Aku sedang berlari di sepanjang jalan setapak di {b}hutan{/b}, dan ketika aku menoleh ke belakang, dia sudah hilang!!"

    show old_anna 4
    show player 10
    player_name "Pernahkah Anda melihat ke sepanjang jalan setapak?"

    show old_anna 5
    show player 11
    anna "Tentu saja! Saya mencari kemana-mana!"

    anna "Tapi saya tidak bisa melewati jalan setapak dan {b}hutan{/b} sendirian..."

    show old_anna 4
    show player 10
    player_name "Seperti apa rupanya?"

    show player 11
    show old_anna 6 at Position(xpos=1002)
    anna "Oh benar. Dia {b}pug{/b}, sebesar ini!"

    show old_anna 5 at right
    anna "Namanya {b}Awesomo{/b}."

    anna "Dia agak kelebihan berat badan, jadi dia tidak bisa pergi jauh."

    anna "Silakan! Maukah kamu membantuku menemukannya?"

    show old_anna 4
    return

label anna_dialogue_anna_dog_hunt_yes:
    show player 14
    player_name "Tentu. Aku akan mencarinya."

    player_name "Apakah ada sesuatu yang perlu saya ketahui tentang dia?"

    player_name "Sesuatu yang akan membantuku menemukannya?"

    show player 1
    show old_anna 5
    anna "Yah... Dia sangat suka makan {b}kue{/b}."

    anna "Jika Anda punya, saya yakin dia akan menciumnya dan keluar..."

    show old_anna 11
    show player 14
    player_name "Oke! Aku akan datang menemuimu jika aku menemukannya!"

    show old_anna 12
    show player 1
    anna "Terima kasih banyak!"

    return

label anna_dialogue_anna_dog_hunt_no:
    show player 10
    player_name "Saya ingin membantu, tetapi ada beberapa hal yang perlu saya urus..."

    show player 11
    show old_anna 5
    anna "Oh, maaf mengganggumu..."

    return

label anna_dialogue_anna_find_dog_have_dog:
    scene expression player.location.background_closeup
    show player 247 at left with dissolve
    show old_anna 4 at right with dissolve
    player_name "Tebak siapa yang saya temukan?"

    show old_anna 5 with vpunch
    anna "!!!"
    show old_anna 12
    anna "{b}Luar Biasa{/b}!!!"

    show player 1
    show old_anna 9
    with dissolve
    anna "Di mana kamu menemukannya?!"

    show old_anna 8
    show player 14
    player_name "Dia berada di hutan terdekat, tak jauh dari jalan setapak..."

    player_name "Dan Anda benar! Beberapa kue berhasil."

    show old_anna 10
    show player 1
    anna "Terima kasih {i}sangat{/i} banyak!"

    show old_anna 9
    anna "Aku pasti akan membalas budimu bagaimanapun juga."

    show old_anna 7
    anna "Aku harus membawanya pulang sekarang. Dia mungkin lapar setelah semua ini."

    show old_anna 10
    anna "Sampai jumpa!"

    return

label anna_dialogue_anna_find_dog_do_not_have_dog:
    show player 11 at left with dissolve
    show old_anna 5 at right with dissolve
    anna "Apakah kamu sudah menemukannya??"

    show old_anna 4
    show player 10
    player_name "Belum..."

    player_name "Bisakah Anda menjelaskannya lagi kepada saya? Dan di mana saya bisa menemukannya?"

    show player 11
    show old_anna 6 at Position(xpos=1002)
    anna "Dia {b}sebesar ini, dan dia seekor anjing pesek{/b}!"

    show old_anna 5 at right
    anna "Dia seharusnya berada {b}di suatu tempat di dekat jalan setapak di tepi hutan{/b}..."

    anna "... Dan dia suka kue!"

    anna "Mungkin Anda bisa {b}menggunakan beberapa cookie{/b} untuk memancingnya keluar."

    show old_anna 11
    show player 14
    player_name "Oke! Aku akan pergi mencarinya!"

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
