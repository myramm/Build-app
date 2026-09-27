label nadya_button_baby:
    if L_warehouse_depot.is_here(M_nadya):
        jump nadya_button_baby_depot
    jump nadya_button_baby_office


label nadya_button_baby_depot:
    pause .1
    show nadya f_surprised
    show svetlana f_surprised
    "{i}*Pekerja mengobrol*{/i}"

    show svetlana a_crossed
    show nadya f_angry:
        xoffset 675
        xzoom -1
    with {'master': dissolve}
    nadya "Hei, berhentilah berkeliaran!"

    show svetlana:
        xoffset 450
    with {'master': dissolve}
    nadya "Kembali bekerja, kalian semua!"

    show anon f_worried behind nadya with dissolve:
        xoffset -100
    nadya "Apa, menurutmu karena aku punya bayi, aku tidak akan berjalan dan menjadikanmu teladan?!"

    show anon f_worried_surprised
    nadya "Aku memasukkanmu ke dalam karung kentang dan mengirimmu kembali ke Rusia!"

    show anon f_worried
    anon "Ehh, {b}Nadya{/b}?"

    show anon a_surprised_up_both f_worried_surprised
    show nadya f_frowning:
        xoffset 100
        xzoom 1
    show svetlana a_sides f_curious:
        xoffset -100
        xzoom 1
    with {'master': dissolve}
    nadya "Apa?!"

    show svetlana f_normal
    nadya f_normal "Oh."

    show anon a_sides f_worried
    with {'master': dissolve}
    nadya "Sorry, {b}[firstname]{/b}." (show_native="Izvinite, {b}[firstname]{/b}.")
    nadya "Hormon-hormon menjadi gila dalam diriku..."

    show anon f_shy
    nadya f_annoyed_down "... Dan payudaraku tidak berhenti bocor..."

    nadya "... Seperti musim hujan."

    show nadya f_normal

    menu nadya_button_baby_depot.choice:
        "Bagaimana kabar si kecil kita?":
            if not M_nadya.once('baby_vodka'):
                jump nadya_button_baby_depot.vodka
            jump nadya_button_baby_depot.sleep
        "Saya harus pergi.":

            pass

    anon "Beritahu aku jika kamu butuh sesuatu, oke?"

    show svetlana f_happy
    nadya f_happy "Jangan khawatir."

    nadya "Semuanya terkendali."

    svetlana "Ya."

    svetlana "Tidak masalah."

    hide anon with dissolve
    return


label nadya_button_baby_depot.vodka:
    anon "Bagaimana kabar si kecil kita?"

    nadya "Bagus."

    show anon f_normal
    nadya "Sedikit kesulitan tidur tetapi tidak ada yang tidak bisa diperbaiki dengan beberapa tetes vodka."

    anon f_surprised "vodka?!"

    anon "Anda tidak bisa memberi bayi vodka!!"

    show svetlana f_curious
    nadya f_frowning @ -m_talk "Hmm?"

    nadya "Kenapa tidak?!"

    anon f_worried_surprised "Karena... itu buruk bagi mereka!"

    show nadya f_normal
    svetlana f_smirk "Tidak buruk untuk bayi Rusia."

    show svetlana a_hips
    with {'master': dissolve}
    svetlana "Vodka membuat mereka kuat."

    nadya "Lihat, sudah diketahui!"

    svetlana "Hal ini diketahui."

    anon f_annoyed "Tidak, itu tidak diketahui!"

    show nadya f_angry
    show svetlana f_glaring
    pause
    anon "Jangan beri aku hal yang mencolok, itu tidak akan berhasil!"

    anon "Aku akan menurunkan kakiku!"

    anon "Tidak ada vodka untuk bayi kami!"

    nadya f_pouting "Hanya sedikit untuk membantu tidur."

    nadya "Itu tidak akan merugikan-"

    anon "Aku bilang tidak!"

    pause
    anon "Aku serius, {b}Nadya{/b}."

    pause
    nadya f_frowning "Hmph, baiklah."

    show svetlana a_surprised f_surprised with {'master': dissolve}:
        xoffset 450
        xzoom -1
    svetlana "You're conceding to him?" (show_native="Vy yemu ustupayete?")
    show svetlana a_sides
    with {'master': dissolve}
    nadya f_worried "He is good father." (show_native="On khoroshiy otets.")
    show svetlana f_timid
    nadya "I owe him a lot." (show_native="Ya yemu mnogim obyazan.")
    anon f_unimpressed "Tolong, bahasa Inggris."

    nadya "Menurutku kamu menang."

    show svetlana f_timid:
        xoffset -100
        xzoom 1
    with {'master': dissolve}
    nadya "Tidak ada vodka untuk bayi."

    anon "Dan kamu?"

    svetlana f_normal "{b}Nona Chernyshevsky{/b} membayar saya untuk mengikuti perintah."

    svetlana "Jika dia mengatakan tidak ada vodka untuk bayi, maka tidak ada vodka untuk bayi."

    anon f_shy "Syukurlah untuk itu!"

    jump nadya_button_baby_depot.choice


label nadya_button_baby_depot.sleep:
    anon "Bagaimana kabar si kecil?"

    nadya f_normal "Bagus."

    show svetlana f_normal
    nadya f_worried "Masih sulit tidur sepanjang malam, tapi kita akan segera melewati masa terburuknya."

    svetlana "Ya, ada peningkatan setiap hari."

    pause
    show svetlana f_smirk_back
    nadya "Saya senang memiliki {b}Svetlana{/b}, dia sangat baik dengan bayi."

    show svetlana a_crossed f_normal with {'master': dissolve}
    svetlana "Bayi bukanlah hal baru bagi saya."

    svetlana "Saya sudah mengurus banyak hal."

    anon "Yah, aku bersyukur kami memilikimu juga."

    show svetlana a_sides f_happy with {'master': dissolve}
    svetlana "Heh, senang sekali diapresiasi."

    svetlana "Thank you." (show_native="Spasibo.")
    jump nadya_button_baby_depot.choice


label nadya_button_baby_office:
    nadya "Ssst, sayang akhirnya tidur."

    show anon b_sit with dissolve:
        xoffset -250
    pause
    show anon f_shy_low

    if M_nadya.pregnancy.baby_gender:
        anon "Dia sangat cantik."

    else:
        anon "Dia sangat cantik."


    nadya f_sexy_down "Ya."

    pause
    nadya "Apalagi saat tidur."


    menu nadya_button_baby_office.choice:
        "Butuh sesuatu?":
            jump nadya_button_baby_office.anything
        "Hati-hati di jalan.":

            pass

    anon f_shy "Hati-hati di jalan."

    nadya f_normal "Beritahu {b}Svetlana{/b} untuk mengambilkan selimut bedong baru saat Anda keluar."

    anon "Bisa."

    nadya f_happy "Thank you." (show_native="Spasibo.")
    pause
    anon "Selamat malam, {b}Nadya{/b}."

    anon f_shy_low "Selamat malam, si kecil."

    nadya "Good night, {b}[firstname]{/b}." (show_native="Spokoynoy nochi, {b}[firstname]{/b}.")
    hide anon with dissolve
    return


label nadya_button_baby_office.anything:
    anon f_normal "Butuh sesuatu?"

    nadya f_normal "No." (show_native="Nyet.")
    nadya "Bayi akan tidur tiga puluh menit..."

    nadya "... Kalau begitu aku akan memberi makan."

    nadya "Setelah itu, {b}Svetlana{/b} akan membacakan cerita bayi sambil saya beristirahat."

    anon f_shy "Sepertinya kalian berdua memiliki segalanya dengan baik."

    nadya f_happy "Ya."

    jump nadya_button_baby_office.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
