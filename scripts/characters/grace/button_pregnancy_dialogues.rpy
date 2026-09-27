label button_grace_pregnancy_need_anything_babies:
    anon "Kalian butuh sesuatu?"

    grace "Tidak, semuanya luar biasa!"

    grace f_happy_down "Kami baik-baik saja, bukan?"

    grace "Ya, benar!"

    pause
    grace "Mmm, cantik sekali anak kita, {b}[firstname]{/b}!"

    anon @ f_laugh "hehe!"

    return

label button_grace_pregnancy_gave_birth_intro:
    scene expression player.location.background_closeup with None
    show anon
    show grace a_baby f_happy_down
    with dissolve
    grace "{b}Mama{/b} sangat menyayangimu..."

    grace "Ya, benar!"

    grace @ f_laugh "Hehehe!"

    anon "Hai."

    grace f_happy "Hai, {b}[firstname]{/b}."

    grace "Saya sangat senang Anda membujuk saya melakukan hal ini!"

    anon "Oh ya?"

    grace "Ya!"

    return

label button_grace_pregnancy_bedridden_yup:
    anon "Ya, bagaimana kabar kalian?"

    grace f_happy_down @ f_tired "{i}*Menguap*{/i} Mengantuk."

    if M_grace.pregnancy.baby_gender == "boy":
        anon "Apakah kamu ingin aku membawanya?"

    elif M_grace.pregnancy.baby_gender == "twins":
        anon "Apakah Anda ingin saya mengambilnya?"

    else:
        anon "Apakah kamu ingin aku membawanya?"

    grace "Tidak, tidak apa-apa."

    if M_grace.pregnancy.baby_gender == "boy":
        grace "Dia anak yang baik, tahu?"

    elif M_grace.pregnancy.baby_gender == "twins":
        grace "Mereka sangat bagus, Anda tahu?"

    else:
        grace "Dia gadis yang baik, kamu tahu?"

    grace "Selalu begitu tenang dan santai."

    anon "Oh ya?"

    if M_grace.pregnancy.baby_gender == "boy":
        grace "Aku tidak yakin dia pernah menangis sekali pun sejak ruang bersalin."

    elif M_grace.pregnancy.baby_gender == "twins":
        grace "Saya tidak yakin mereka pernah menangis sejak ruang bersalin."

    else:
        grace "Aku tidak yakin dia pernah menangis sekali pun sejak ruang bersalin."

    pause
    if M_grace.pregnancy.baby_gender == "boy":
        grace "Pasti datangnya darimu karena dia pasti tidak mendapatkan sifat itu dariku!"

    elif M_grace.pregnancy.baby_gender == "twins":
        grace "Pasti datangnya darimu karena mereka pasti tidak mendapatkan sifat itu dariku!"

    else:
        grace "Pasti datangnya darimu karena dia pasti tidak mendapatkan sifat itu dariku!"

    anon @ f_laugh "hehe!"

    pause
    grace f_happy "Saya ingin tahu apakah Anda dapat membantu saya, {b}[firstname]{/b}?"

    anon "Tentu, apa saja!"

    grace "Intip {b}Odette{/b} dan pastikan dia baik-baik saja selama aku terjebak di sini, ya?"

    anon "Saya bisa melakukan itu."

    grace "Terima kasih, {b}[firstname]{/b}."

    pause
    if M_grace.pregnancy.baby_gender == "twins":
        anon f_shy_low "Sampai jumpa lagi, anak-anak kecil."

    else:
        anon f_shy_low "Sampai jumpa, anak kecil."

    grace @ f_laugh "hehe!"

    hide anon with dissolve
    return

label button_grace_pregnancy_bedridden_intro:
    scene expression game.timer.image("location_hospital_baby_bed{}")
    show grace b_gown_bed
    show anon with dissolve
    grace "Hai, {b}[firstname]{/b}."

    grace "Anda datang untuk memeriksa kami lagi?"

    return

label button_grace_ill_leave_you_be_baby:
    anon "Aku akan meninggalkanmu."

    grace f_happy "Kembalilah dan temui kami segera, oke?"

    anon "Akan dilakukan."

    hide anon with dissolve
    return

label button_grace_ill_leave_you_be:
    anon "Aku akan meninggalkanmu."

    grace "Baiklah."

    anon "Saya di sini jika Anda membutuhkan saya, oke?"

    grace f_normal "Terima kasih telah melapor masuk, {b}[firstname]{/b}."

    hide anon with dissolve
    return

label button_grace_get_you_something_0:
label button_grace_get_you_something_1:
    anon f_normal "Bolehkah aku memberimu sesuatu?"

    grace f_normal "Tidak, aku baik-baik saja."

    grace "Terima kasih telah menawarkan."

    anon "Apakah {b}Odette{/b} telah membantu Anda?"

    grace @ f_sad_down "Ya."

    grace "Dia sebenarnya sangat hebat sejauh ini!"

    anon "Itu bagus untuk didengar."

    return

label button_grace_get_you_something_2:
label button_grace_get_you_something_3:
    anon "Ada yang bisa kuberikan padamu?"

    grace "Tidak, aku baik-baik saja."

    pause
    grace f_sad_down @ f_sad "Pastikan saja kamu merawat adikku dengan baik, ya?"

    grace "Seluruh situasi dengan bayi ini membuatku merasa tidak enak."

    anon "Anda tidak perlu terlalu khawatir."

    anon "Saya selalu menjaga {b}Hawa{/b}."

    grace "Saya tidak bisa menahannya."

    return

label button_grace_get_you_something_4:
    anon "Ada yang bisa kuberikan padamu?"

    grace "Ehh, tidak... menurutku tidak."

    pause
    grace "Apakah Anda gugup menjadi seorang ayah?"

    anon @ a_behind_head "Ya, sedikit."

    anon "Tapi lebih bersemangat dari apapun."

    grace @ f_laugh "Hehe, aku juga."

    pause
    grace "Ingat saja, kami tidak boleh membiarkan {b}Eve{/b} mengetahui bahwa Anda adalah ayahnya."

    anon "saya ingat."

    grace "Terima kasih, {b}[firstname]{/b}."

    return

label button_grace_pregnancy_bathroom_4:
    scene expression background(544, 288, 2.) as stage at flip
    show layer master at flip
    show grace b_naked_pregnant_belly a_cover f_sad
    show anon f_flirt_low with dissolve
    grace "Kamu tidak mungkin begitu menyukai perutku..."

    anon "Oh, benar."

    anon "Saya sungguh, BENAR-BENAR melakukannya."

    grace f_happy @ f_laugh "Hehehe!"

    anon "Bisakah Anda melakukan pose seksi itu lagi?"

    grace a_shy @ f_sexy "Maksudmu seperti ini?"

    anon "Sama seperti itu!"

    pause
    anon f_flirt "Kamu cantik sekali."

    grace @ f_eyeroll "Oh, ayolah... Hentikan."

    anon "Maksudku!"

    grace @ f_laugh "Hehehe!"

    pause
    hide anon with dissolve
    $ game.main()
    return

label button_grace_pregnancy_intro:
    scene expression player.location.background_closeup with None
    show anon
    show grace b_magic
    with dissolve
    anon "Halo, {b}Rahmat{/b}."

    grace "Hai, {b}[firstname]{/b}."

    return

label button_grace_pregnancy_how_are_you_feeling_0:
label button_grace_pregnancy_how_are_you_feeling_1:
    anon "Bagaimana perasaanmu?"

    grace f_sad "Khawatir, takut, berkonflik..."

    show anon f_worried
    grace "Silakan pilih."

    anon "Semuanya akan baik-baik saja, aku janji."

    grace f_normal @ f_laugh "Heh, saya menghargai Anda mengatakan itu, {b}[firstname]{/b}."

    anon "Tapi itu hanya harapan buta, tidak ada cara untuk memastikan apapun."

    show grace f_sad_down
    anon f_normal "Aku yakin apa pun yang terjadi, aku akan selalu ada untukmu dan anak kita."

    grace f_normal "Aww, kamu seperti, pria paling manis yang pernah ada!"

    grace "Adikku sangat beruntung memilikimu."

    anon "Dan aku beruntung memilikinya."

    return

label button_grace_pregnancy_how_are_you_feeling_2:
label button_grace_pregnancy_how_are_you_feeling_3:
    anon "Bagaimana perasaanmu?"

    grace f_sad @ f_eyeroll "Ah, menyedihkan..."

    anon f_worried @ -m_talk "Hmm?"

    grace "Itu hal yang paling bodoh!"

    grace "Aku lapar, sepertinya, sepanjang waktu!"

    grace f_sad_down "Tapi kemudian separuh waktu saya makan, saya sakit dan muntah-muntah lagi..."

    anon "Kedengarannya tidak bagus."

    grace "{i}*Huh*{/i} Ya, {b}Odette{/b} merasa aku perlu mengubah pola makanku."

    grace f_sad "Dia bersikeras agar kami menemui dokter tentang hal itu besok dan memeriksa ulang apakah semuanya baik-baik saja."

    anon f_normal "Sepertinya dia benar-benar menguasai segalanya."

    grace f_normal "Hehe, ya."

    grace "Dia penuh kejutan, ya?"

    anon "Aku harus berterima kasih padanya karena telah merawatmu dengan baik."

    return

label button_grace_pregnancy_how_are_you_feeling_4:
    anon "Bagaimana perasaanmu?"

    grace f_normal @ f_eyeroll "Sepertinya aku akan meledak!"

    grace "Sebenarnya, sebaiknya Anda menjaga sepatu Anda..."

    anon @ f_laugh "hehe!"

    grace "Kupikir aku akan lebih cemas saat ini, tahu?"

    grace "Tapi entah kenapa, aku merasa tenang."

    grace "Heh, mungkin aku hanya tidak bisa mendengar kegugupan atas suara kakiku yang menggonggong."

    anon @ f_confused "Kakimu sakit?"

    anon "Saya bisa menggosokkannya untuk Anda, jika Anda mau?"

    grace "Tidak, tidak apa-apa {b}[firstname]{/b}..."

    grace "{b}Odette{/b} telah memberi saya pijatan seluruh tubuh setiap malam."

    grace "Dia luar biasa dengan semua ini."

    anon f_grumpy "Cih, dia memonopoli semua pekerjaan..."

    grace "Hehehe, apakah itu membuatmu kesal?"

    anon "Tidak, saya rasa tidak..."

    anon "Selama kamu bahagia, aku pun bahagia."

    grace @ f_laugh "Manis sekali, {b}[firstname]{/b}."

    show anon f_normal
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
