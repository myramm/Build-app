label iwanka_button_baby:
    show iwanka a_baby f_smirk_down
    show anon with dissolve
    iwanka "Aksesoris sangatlah penting."

    iwanka "Tidak ada pakaian yang lengkap tanpanya dan harus serasi!"

    anon "Apa yang terjadi?"

    iwanka f_normal "Aku bersiap-siap mengajak si kecil berbelanja."


    menu iwanka_button_baby.choice:
        "Lagi?!":

            jump iwanka_button_baby.invite
        "Apakah kamu tidak berlebihan?":

            jump iwanka_button_baby.excess
        "Selamat bersenang-senang, menurutku.":

            pass

    anon f_shy "Selamat bersenang-senang, menurutku."

    iwanka f_smirk_down "Tentu saja kita akan bersenang-senang, bukan?"

    iwanka "Tidak ada yang mengalahkan belanja!"

    iwanka "Itu hal paling menyenangkan yang bisa Anda lakukan!"

    hide anon with dissolve
    return


label iwanka_button_baby.excess:
    anon f_worried "Apakah kamu tidak berlebihan?"

    iwanka f_normal "Apa maksudmu?"

    anon "Itu bayi, {b}Iwanka{/b}..."

    anon "Anda sebenarnya tidak perlu membeli semua barang mahal itu."

    iwanka f_annoyed "Apakah kamu bercanda?"

    iwanka "Bayi saya hanya mendapatkan akhir cerita yang terbaik."

    anon "Y-ya, tapi ini bukan-"

    iwanka "Akhir cerita, {b}[firstname]{/b}!"

    iwanka "Aku punya semua uang yang {b}ayahku{/b} tinggalkan untukku dan aku akan membelanjakannya sesukaku."

    anon f_sad_down "{i}*Huh*{/i} Cukup adil."

    jump iwanka_button_baby.choice


label iwanka_button_baby.invite:
    anon f_surprised "Lagi?!"

    anon "Bukankah kamu pergi kemarin?"

    show anon f_worried
    iwanka f_normal @ f_annoyed "Jadi?"

    if M_iwanka.pregnancy.baby_gender == "boy":
        iwanka "Dia akan segera mulai tumbuh dan saya ingin mulai membangun lemari pakaiannya."

        anon "Y-ya, tapi kamu sudah membelikannya banyak barang..."

    else:
        iwanka "Dia akan segera mulai tumbuh dan saya ingin mulai membangun lemari pakaiannya."

        anon "Y-ya, tapi kamu sudah membelikannya banyak barang..."

    iwanka @ f_eyeroll "Anda tidak akan pernah memiliki terlalu banyak pakaian, {b}[firstname]{/b}!"

    iwanka f_excited "Sebenarnya, kenapa kamu tidak ikut dengan kami dan kami akan membelikanmu beberapa barang juga?"

    anon "Tidak, tidak apa-apa."

    anon "Aku baik-baik saja dengan lemari pakaianku."

    iwanka f_annoyed "Lemari apa?!"

    iwanka "Anda benar-benar mengenakan pakaian yang sama setiap hari."

    anon f_unimpressed "Hei, itu penampilan yang bagus untukku!"

    iwanka f_smirk @ f_laugh "{i}*Mendengus*{/i} Tentu saja..."

    jump iwanka_button_baby.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
