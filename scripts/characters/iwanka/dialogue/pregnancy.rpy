label iwanka_pregnancy_notify:
    scene expression player.location.background
    "{i}*Brrrzzzt* *Brrrzzzt*{/i}"


    scene expression background(288, 368, 3.5, l=L_rump_second) as underlay:
        xoffset -400
    show iwanka a_phone f_excited:
        xoffset -500

    $ renpy.dynamic(stage=player.location.background_phone)
    show expression stage as stage
    show anon f_confused with dissolve:
        flip
    anon @ -m_talk "Hmm?"


    if not M_iwanka.once('number_known'):
        anon a_phone f_normal_low "Itu {b}Iwanka{/b}."

        show anon a_phone_talk f_normal with dissolve:
            unflip
            xoffset 500
    else:

        anon a_phone f_thinking_down "Saya tidak mengenali nomor ini..."

        show anon a_phone_talk f_confused with dissolve:
            unflip
            xoffset 500

    show expression stage as stage at phoneleft with phoneleft.show
    anon "Halo?"

    iwanka "Hai, {b}[firstname]{/b}."

    anon "Siapa ini?"

    iwanka @ f_laugh "Ya ampun!"

    iwanka "Apakah kamu tidak mengenali suara pacarmu?"

    anon f_worried "Ehh..."

    iwanka "Ini {b}Iwanka{/b}, bodoh!"

    anon f_surprised "{b}Iwanka{/b}?!"

    pause
    anon f_shy "Itu umm... Maksudku, aku tahu itu kamu..."

    iwanka @ -m_talk "Mhmm."

    iwanka "Apapun, dengarkan..."

    iwanka f_bored "... Anda tahu semua seks luar biasa yang pernah kita lakukan?"

    anon "Ya?"

    iwanka "Yah, aku hamil."

    anon f_surprised @ f_shock "!!!"
    anon "Kamu hamil?!"

    iwanka "Ya."

    pause
    iwanka f_smirk "Tapi jangan panik atau apa pun, saya akan mengurusnya."

    anon f_worried "Tunggu, apa maksudnya?"

    anon "Apakah Anda menyingkirkannya?"

    iwanka @ f_laugh "Ya, ya!"

    iwanka f_bored "aku tidak ingin punya bayi..."


    menu:
        "Oke, fiuh!":
            jump iwanka_pregnancy_notify.relief
        "Kenapa tidak?":

            pass

    anon f_worried "Kenapa tidak?"

    iwanka f_annoyed "Apakah kamu bercanda?"

    iwanka "Pernahkah Anda melihat seorang wanita membawa bayinya di sebuah pesta?"

    anon "Tidak."

    iwanka "Sungguh tragis!"

    iwanka "Saya tidak ingin menjadi seperti itu."

    pause
    iwanka f_concerned "Ditambah lagi, saya tumbuh bersama {b}Melonia{/b}!"

    iwanka "Saya jelas tidak siap menjadi ibu yang baik!"


    menu:
        "Itu keputusanmu.":
            jump iwanka_pregnancy_notify.defer
        "Kamu bersikap konyol.":

            pass

    anon f_shy "Kamu bersikap konyol."

    anon "Kamu akan menjadi ibu yang baik, {b}Iwanka{/b}."

    pause
    iwanka "Bagaimana Anda bisa yakin?"

    anon "Lihatlah seperti ini... {b}Melonia{/b} pada dasarnya mengajarimu segala sesuatu yang tidak boleh dilakukan, bukan?"

    iwanka f_suspicious "Ya?"

    anon "Jadi lakukan saja kebalikan dari apa yang akan dia lakukan."

    pause
    iwanka f_excited "aku tidak pernah berpikir seperti itu..."

    iwanka @ f_laugh "Anda tahu, kentang panggang akan menjadi ibu yang lebih baik daripada dia."

    anon f_normal "Dan saya akan berada di sana untuk membantu kapan pun Anda membutuhkan saya."

    iwanka "Anda berjanji?"

    anon "Tentu saja."


    if not player.has_required_chr(6):
        jump iwanka_pregnancy_notify.later

    iwanka f_normal "Aku tidak percaya aku sedang mempertimbangkan ini..."

    anon "Coba pikirkan, {b}Iwanka{/b}."

    anon "Seorang bayi yang separuh kamu dan separuh aku."

    iwanka f_excited "Akan sangat menyenangkan jika versi kecil diri saya berkeliaran."

    iwanka "Aku bisa mengajaknya berbelanja dan mengajarinya cara memanipulasi laki-laki..."

    anon "Ya, atau bisa juga anak kecil."

    iwanka "Tidak, itu akan menjadi seorang gadis."

    iwanka "saya memutuskan."

    anon "Heh, menurutku cara kerjanya tidak seperti itu..."

    iwanka f_annoyed "Itu perempuan, {b}[firstname]{/b}!"

    iwanka "Akhir cerita."

    anon @ f_worried -m_talk "..."
    anon "Jadi kita melakukan ini?"

    $ display.toast(chr_pass)
    iwanka f_excited @ f_laugh "Ya, Anda meyakinkan saya."

    anon "Luar biasa!"

    iwanka "Temui aku di kapal pesiar nanti untuk merayakannya?"

    anon "Tentu saja!"

    show anon f_looking_down a_phone with dissolve
    show expression stage as stage with {'master': phoneleft.hide}
    "{i}*Bip*{/i}"

    pause
    anon f_grin @ -m_talk "(Saya tidak percaya...)"

    anon @ -m_talk "(Aku akan menjadi seorang ayah!)"

    anon @ -m_talk "(Ini sangat menarik!)"

    hide anon with dissolve
    return True


label iwanka_pregnancy_notify.defer:
    anon f_worried "Itu keputusanmu."

    anon "Jika Anda yakin?"

    iwanka f_excited "Saya."

    pause
    iwanka "Aku akan mengurusnya dan kamu bisa menemuiku di kapal pesiar nanti, oke?"

    anon "{i}*Huh*{/i} Ya, oke."

    iwanka "Selamat tinggal, {b}[firstname]{/b}."

    show anon f_looking_down a_phone with dissolve
    show expression stage as stage with {'master': phoneleft.hide}
    "{i}*Bip*{/i}"

    pause
    anon f_sad_down @ -m_talk "(Sial.)"

    hide anon with dissolve
    return


label iwanka_pregnancy_notify.later:
    iwanka f_concerned "T-tidak, ini terlalu cepat!"

    anon f_worried "{b}Iwanka{/b}, menurutku-"

    $ display.toast(chr_fail)
    iwanka "Maaf, {b}[firstname]{/b}."

    iwanka "Aku sudah mengambil keputusan."

    anon @ -m_talk "..."
    iwanka "Mungkin suatu saat nanti tapi tidak sekarang."

    anon "Baiklah."

    iwanka f_normal "Aku akan mengurusnya dan kamu bisa menemuiku di kapal pesiar nanti, oke?"

    anon "{i}*Huh*{/i} Ya, oke."

    iwanka "Selamat tinggal, {b}[firstname]{/b}."

    show anon f_looking_down a_phone with dissolve
    show expression stage as stage with {'master': phoneleft.hide}
    "{i}*Bip*{/i}"

    pause
    anon f_sad_down @ -m_talk "(Sial.)"

    hide anon with dissolve
    return


label iwanka_pregnancy_notify.relief:
    anon f_shy "Oke, fiuh!"

    anon "Ya, kami pasti belum siap menjadi orang tua!"

    iwanka f_excited "Saya setuju."

    pause
    iwanka f_smirk "Mari kita pertahankan apa adanya, ya?"

    anon "Kedengarannya bagus."

    iwanka "Dan mungkin menarik diri mulai sekarang?"

    anon "Hehe, kamu mengerti."

    iwanka "Temui aku di kapal pesiar nanti?"

    anon "Tentu saja."

    show anon f_looking_down a_phone with dissolve
    show expression stage as stage with {'master': phoneleft.hide}
    "{i}*Bip*{/i}"

    pause
    anon @ -m_talk "(Itu membereskannya.)"

    hide anon with dissolve
    return


label iwanka_pregnancy_notify.repeat:
    scene expression player.location.background
    "{i}*Brrrzzzt* *Brrrzzzt*{/i}"


    scene expression background(288, 368, 3.5, l=L_rump_second) as underlay:
        xoffset -400
    show iwanka a_phone f_excited:
        xoffset -500

    $ renpy.dynamic(stage=player.location.background_phone)
    show expression stage as stage
    show anon f_confused with dissolve:
        flip
    anon @ -m_talk "Hmm?"

    anon a_phone f_normal_low "Itu {b}Iwanka{/b}."

    show anon a_phone_talk f_normal with dissolve:
        unflip
        xoffset 500
    show expression stage as stage at phoneleft with phoneleft.show
    anon "Halo?"

    iwanka "Hai, {b}[firstname]{/b}."

    anon f_worried "Apakah semuanya baik-baik saja?"

    iwanka "Yah, agak..."

    pause
    iwanka f_bored "... Anda tahu bagaimana kami melakukan hubungan seks yang luar biasa dan kemudian saya hamil?"

    anon "Ya?"

    iwanka "Ya, itu terjadi lagi."

    anon f_surprised "!!!"
    anon "Kamu hamil?!"

    iwanka "Ya."

    anon f_normal "Kita akan punya bayi lagi?!"

    iwanka "Maksudku, kecuali kamu tidak ingin yang lain..."

    anon f_shy "T-tidak, aku pasti ingin yang lain!"

    anon "Ini adalah berita yang luar biasa!"

    iwanka "Ya, aku pikir kamu akan bahagia."

    anon "Bukan?"

    iwanka "Psh, ya... Benar-benar..."

    iwanka @ f_eyeroll "Saya bisa menghabiskan sembilan bulan lagi tanpa mabuk... Luar biasa!"

    show anon f_worried
    pause
    iwanka "Jadi, saya akan menemui Anda nanti di {b}kapal pesiar{/b}?"

    anon "Ya, aku akan berada di sana."

    show anon f_looking_down a_phone with dissolve
    show expression stage as stage with {'master': phoneleft.hide}
    "{i}*Bip*{/i}"

    pause
    anon f_grin @ -m_talk "(Saya tidak percaya...)"

    anon @ -m_talk "(Aku akan menjadi seorang ayah!)"

    anon @ -m_talk "(Ini sangat menarik!)"

    hide anon with dissolve
    return True


label iwanka_pregnant_labor_1:
    scene expression player.location.background_blur
    show anon f_normal with dissolve
    anon "Sepertinya aku mendapat pesan teks."

    hide anon with dissolve
    return


label iwanka_pregnant_labor_2:
    scene expression player.location.background_blur
    if player.location != L_map:
        show anon f_surprised a_phone with dissolve
    anon "{b}Iwanka{/b} akan melahirkan?!"

    anon "Sialan!"

    pause
    anon "Sebaiknya saya pergi ke {b}klinik{/b} untuk memeriksanya."

    if player.location != L_map:
        hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
