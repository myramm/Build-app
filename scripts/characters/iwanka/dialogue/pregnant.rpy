label iwanka_button_pregnant:
    if M_iwanka.pregnancy.stage == 1 and not game.timer.is_morning():
        if player.location == L_boat_bridge:
            show anon b_onbed_back with dissolve:
                flip
                offset (100, 110)
        else:
            show anon b_onbed_back with dissolve:
                offset (-100, 20)
    else:
        show anon with dissolve

    if M_iwanka.pregnancy.stage < 3:
        anon "Hai, {b}Iwanka{/b}."

        iwanka f_excited "Itu ayah bayiku!"

        anon @ f_surprised "!!!"
        anon "Sepertinya memang begitu, ya?"

        iwanka @ f_laugh "hehe!"

    else:

        iwanka "Ah, jangan lihat aku..."

        anon f_worried "Hah?"

        iwanka "aku mengerikan!"

        anon "Tidak, kamu tidak."

        anon f_shy "Kamu tampak hebat!"

        iwanka "Jangan bohong padaku, {b}[firstname]{/b}..."

        iwanka "Sepertinya aku menelan bola pantai."


    menu iwanka_button_pregnant.choice:
        "Bagaimana perasaanmu?":

            if M_iwanka.pregnancy.stage == 1:
                jump iwanka_button_pregnant.advice
            elif M_iwanka.pregnancy.stage == 2:
                jump iwanka_button_pregnant.bulemia
            else:
                jump iwanka_button_pregnant.horny

        "Ada yang bisa kuberikan padamu?" if not M_iwanka.pregnancy.stage < 3:
            jump iwanka_button_pregnant.cheese
        "{b}Melonia{/b}.":

            if M_iwanka.pregnancy.stage == 1:
                jump iwanka_button_pregnant.grandma
            elif M_iwanka.pregnancy.stage == 2:
                jump iwanka_button_pregnant.clueless
            else:
                jump iwanka_button_pregnant.parents
        "Saya harus pergi.":

            pass

    if M_iwanka.pregnancy.stage < 3:
        anon f_normal "Saya harus pergi."

        iwanka f_normal "Apakah ibuku masih membersihkan barang-barangmu?"

        anon "Ya, tapi tidak apa-apa."

        anon "Saya butuh uangnya."

        iwanka f_disgusted "Eugh, sepertinya menidurinya saja tidak cukup..."

        anon "Sampai jumpa lagi, oke?"

        iwanka "Ya baiklah."

    else:

        anon f_normal @ a_wave "Saya harus pergi."

        iwanka f_normal "Baiklah, tapi bawalah ponselmu."

        iwanka "Bayi ini akan jatuh kapan saja sekarang."

        anon "Saya akan berada di sana."


    hide anon with dissolve
    return


label iwanka_button_pregnant.advice:
    anon f_normal "Bagaimana perasaanmu?"

    iwanka f_excited "Temanku Chelsea bilang aku seharusnya mengalami banyak mual di pagi hari saat ini..."

    iwanka "... Tapi sejauh ini bagus."

    anon "Chelsea?"

    iwanka "Ya, dia adalah teman lama semasa kuliah."

    iwanka "Ayahnya juga seorang walikota di kota kecil."

    iwanka "Jadi kami seperti, entahlah, cocok."

    anon @ f_laugh "Itu luar biasa!"

    iwanka "Dia punya banyak bayi jadi saya telah meminta nasihatnya."

    anon "Baiklah, saya senang mendengar ada seseorang yang menasihati Anda."

    jump iwanka_button_pregnant.choice


label iwanka_button_pregnant.bulemia:
    anon f_normal "Bagaimana perasaanmu?"

    iwanka f_normal "Saya baik-baik saja."

    anon "Apa kamu yakin?"

    anon "Masih belum merasakan mual di pagi hari?"

    iwanka "Ya, benar, tapi tidak terlalu buruk."

    anon "Benar-benar?"

    iwanka @ f_eyeroll "Tolong, {b}[firstname]{/b}, saya mengalami fase bulimia di sekolah menengah..."

    iwanka "... Muntah bukanlah hal baru bagiku."

    anon f_worried "Itu-"

    anon "Hmm, oke."

    iwanka "Chelsea bilang aku akan segera mengidam makanan aneh."

    anon f_normal "Oh ya?"

    iwanka "Dia bilang untuknya, biasanya kue keju yang dicelupkan ke dalam sirup maple."

    anon f_disgusted "Eww, itu menjijikkan!"

    iwanka @ f_laugh "Haha!"

    iwanka "Jangan khawatir, saya tidak akan ketahuan memakan sesuatu yang menjijikkan."

    jump iwanka_button_pregnant.choice


label iwanka_button_pregnant.cheese:
    anon f_normal "Ada yang bisa kuberikan padamu?"

    iwanka f_normal "Sebenarnya, sekarang kamu menyebutkannya."

    iwanka "Bisakah kamu mengambilkanku beberapa kue keju itu?"

    anon "Anda ingin kue keju?"

    iwanka "Ya."

    pause
    iwanka "Dan beberapa sirup maple."

    anon f_disgusted "Tunggu sebentar..."

    iwanka f_annoyed "Jangan menilai saya!"

    jump iwanka_button_pregnant.choice


label iwanka_button_pregnant.clueless:
    anon f_worried "Apakah kamu sudah memberi tahu {b}Melonia{/b}?"

    iwanka f_normal "Tidak."

    anon "{b}Iwanka{/b}, dia akan mencari tahu..."

    iwanka "Saya meragukannya."

    anon "Anda sudah mulai menunjukkannya dan kali ini minggu depan Anda akan-"

    iwanka f_surprised "Oh."

    iwanka "Em."

    iwanka "Aduh!!!"

    iwanka f_annoyed "Maksudmu aku gendut?!"

    anon f_worried @ f_shock "Apa?!"

    anon "T-tidak, itu bukan-"

    iwanka "Sebaiknya kamu tidak bilang aku gendut!"

    iwanka "Aku benar-benar akan kehilangan akal sehatku!"

    anon f_shy "Serius, kamu tampak hebat, {b}Iwanka{/b}!"

    iwanka @ -m_talk "Mhmm."

    jump iwanka_button_pregnant.choice


label iwanka_button_pregnant.grandma:
    anon f_worried "Sudahkah kamu memberi tahu {b}Melonia{/b} dia akan menjadi seorang nenek?"

    iwanka f_normal "Apakah kamu bercanda?"

    iwanka @ f_eyeroll "Dia hanya akan menceramahiku tentang sikap tidak bertanggung jawab dan kemudian menyuruhku membuangnya."

    anon "Menurutmu begitu?"

    iwanka "Saya tahu begitu."

    anon "Yah, pada akhirnya kamu harus memberitahunya..."

    iwanka "Itu pendapat Anda."

    jump iwanka_button_pregnant.choice


label iwanka_button_pregnant.horny:
    anon f_worried "Bagaimana perasaanmu?"

    iwanka f_bored "Terangsang."

    iwanka "Dan tidak seperti, terangsang biasa juga..."

    iwanka "... Aneh sekali."

    anon "Hah?"

    iwanka "Saya terus mengalami mimpi jernih yang melibatkan gurita."

    anon f_surprised_teeth @ f_shock "Gurita?!"

    iwanka "Anda tahu, seperti... Melakukan sesuatu..."

    anon f_worried "Hal-hal?"

    iwanka "... Dengan tentakel mereka."

    anon "Anda mengalami mimpi seks tentang gurita?!"

    iwanka "Aku tidak bisa menghilangkannya dari kepalaku!"

    pause
    iwanka "Sudah kubilang itu aneh."

    jump iwanka_button_pregnant.choice


label iwanka_button_pregnant.parents:
    anon f_worried "{b}Melonia{/b} pasti sudah mengetahuinya sekarang, kan?"

    iwanka f_bored "Tidak."

    anon @ f_surprised "Dengan serius?!"

    anon "Bagaimana mungkin dia tidak memperhatikan perutnya?"

    iwanka "Umm, karena dia tidak memperhatikanku..."

    iwanka f_annoyed "Sudah kubilang itu padamu!"

    anon "Namun tetap saja."

    anon "Itu cucunya, kita harus memberitahunya."

    iwanka "Saya kira Anda ingin pergi ke penjara dan memberi tahu ayah saya juga?"

    anon @ -m_talk "..."
    iwanka "Ya, menurutku tidak."

    iwanka "Orangtuaku payah, {b}[firstname]{/b}."

    iwanka "Saya sudah menerimanya sejak lama dan tidak ada alasan bagi Anda untuk merasa terganggu karenanya."

    jump iwanka_button_pregnant.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
