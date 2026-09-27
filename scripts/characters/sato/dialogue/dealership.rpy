label sato_button_dealership:
    show anon with dissolve
    if game.timer.is_day():
        sato "Oh, halo lagi, Pak."

        sato "Saya harap Anda mendapatkan pengalaman yang luar biasa di sini, di dealer kecil kami?"

        anon "Ini tentu saja menarik."

        sato "Ada yang bisa saya bantu?"

    else:
        sato "Oh, halo lagi, Pak."

        sato "Aku khawatir kita akan dekat malam ini."

        sato "Apakah ada hal terakhir yang bisa saya bantu?"


    menu sato_button_dealership.choice:
        "Apakah Anda yang bertanggung jawab di sini?":

            jump sato_button_dealership.boss
        "Putrimu.":

            jump sato_button_dealership.josie

        "Karyawan Anda {b}Kim{/b}." if M_kim.state is None:
            jump sato_button_dealership.kim
        "Layanan tambahan?":

            jump sato_button_dealership.service

        "Lihat! Monyet berkepala tiga!" if M_anon.is_state(S_ano05_cell) and player.stats._dex <= 3:
            jump ano05_cell_sato.fail

        "Wah! Pedang keren!" if M_anon.is_state(S_ano05_cell) and player.stats._dex > 3:
            jump ano05_cell_sato.pass
        "Aku baik-baik saja.":

            pass

    anon f_normal "Saya tidak membutuhkan apa pun saat ini."

    sato "Nah, jika Anda sedang ingin membeli kendaraan, silahkan menemui salah satu sales kami."

    sato f_smiling "Saya yakin putri saya {b}Josephine{/b} akan dengan senang hati memenuhi kebutuhan Anda."

    hide anon with dissolve
    return


label sato_button_dealership.boss:
    anon f_normal "Apakah Anda yang bertanggung jawab di sini?"

    sato f_smiling "Ya memang."

    sato "Butuh waktu dua belas tahun bagi saya untuk menaiki tangga tersebut, namun akhirnya saya berada di puncak."

    sato "Satu-satunya pria yang harus aku jawab sekarang, adalah aku!"

    pause
    sato f_confused "Ya, kecuali jika Anda menghitung manajer regional... Secara teknis dia adalah bos saya."

    pause
    sato "Dan presiden perusahaan adalah bosnya..."

    show anon f_worried
    sato "Jadi, saya kira saya juga menjawabnya."

    pause
    sato "Dan kemudian ada pemiliknya."

    anon "Jadi Anda lebih seperti, setengah jalan menaiki tangga?"

    sato f_smiling "Baiklah, sebut saja itu tiga perempat perjalanan ke atas."

    show anon f_unimpressed
    pause
    sato f_normal "Benar."

    jump sato_button_dealership.choice


label sato_button_dealership.josie:
    anon f_normal "Dia sepertinya tidak terlalu suka bekerja di sini."

    sato f_angry "Putriku tidak tahu apa yang baik untuknya."

    sato "Dia tidak punya ambisi!"

    sato "Jika dia mau, dia akan bermalas-malasan di rumah, menonton boobtube atau apa pun yang kalian lakukan saat ini..."

    anon f_shy "Hei, ini bisa jadi lebih buruk."

    sato f_confused "Hehe, aku tidak mengerti bagaimana itu bisa terjadi..."

    anon "Dia bisa saja melakukan camshow demi uang."

    sato "Kamera- Hah?"

    sato "saya tidak mengikuti..."

    anon f_unimpressed "Ehh, sudahlah."

    show sato f_normal
    jump sato_button_dealership.choice


label sato_button_dealership.kim:
    anon f_worried "Karyawan Anda {b}Kim{/b}."

    sato "Bagaimana dengan dia?"

    anon "Dia benar-benar kaktus yang hebat!"

    sato f_confused "Aku tidak yakin aku mendengarmu dengan benar..."

    sato "Apa kamu bilang kaktus pantat?"

    anon "Ya, dia sangat kasar padaku."

    sato "{b}Kim Jun Wang{/b}?"

    anon "Ya, itu dia."

    sato f_smiling "Anda pasti salah, Pak!"

    sato "{b}Kim{/b} adalah salesman dan karyawan terbaik kami bulan ini, selama lima bulan berturut-turut."

    anon f_unimpressed "Anda pasti bercanda."

    sato "Tidak, tidak sama sekali."

    pause
    anon f_skeptical "Berapa banyak salesman yang Anda miliki yang bekerja di sini?"

    sato f_confused "Ya, dua... Jika kamu menghitung putriku."

    sato "Dia belum melakukan penjualan, jadi secara teknis dia masih magang, tapi saya yakin dia akan segera berhasil."

    anon "Eh ya."

    show sato f_normal
    pause
    anon "Saya kira Anda tidak menjual banyak mobil di sini, bukan?"

    sato "Hei, ayolah... Kami memiliki persentase penjualan mobil tertinggi di seluruh Summerville!"

    anon f_unimpressed "Anda satu-satunya dealer di kota ini!"

    sato @ f_confused "Ugh, kalau diutarakan seperti itu, kedengarannya kurang mengesankan..."

    anon "Hanya-"

    anon "Lupakan."

    jump sato_button_dealership.choice


label sato_button_dealership.service:
    anon f_worried "Anda menawarkan layanan tambahan?"

    sato "Tentu saja."

    show anon f_normal
    sato "Kami menawarkan perawatan gratis kepada semua pelanggan kami, selama mobil mereka masih dalam garansi."

    sato "Temui saja kepala mekanik kami di bawah di garasi, dan dia akan segera mengantarkan Anda kembali ke jalan."

    anon "Baiklah."

    anon "Ada lagi?"

    sato "Baiklah, Anda dipersilakan untuk menikmati donat atau kopi gratis, jika Anda mau."

    sato "Anda dapat menemukannya di ruang istirahat kami, tak jauh dari lantai ruang pamer."

    anon @ f_laugh "Oke, saya akan mengingatnya."

    jump sato_button_dealership.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
