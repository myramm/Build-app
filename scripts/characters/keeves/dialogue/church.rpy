label keeves_button_church:
    show anon with dissolve:
        xoffset -50
    anon "Halo, {b}Pastor Keeves{/b}."

    keeves "Heeey, apa kabar, kawan kecil?!"

    keeves "Bisakah saya membantu Anda dengan sesuatu?"


    menu keeves_button_church.choice:
        "{b}Consuela{/b}." if M_consuela.is_state(S_con02_init):
            jump con02_init_keeves
        "Anda terlihat sangat akrab.":

            jump keeves_button_church.glitch
        "Bagaimana kabarmu?":

            jump keeves_button_church.excellent
        "Sudahlah.":

            pass

    anon f_normal @ a_wave "Sampai jumpa, {b}Pastor Keeves{/b}."

    keeves @ a_point "Hehe, bagus sekali."

    keeves @ f_laugh a_rock "Nanti, kawan kecil!"

    hide anon with dissolve
    return


label keeves_button_church.glitch:
    show anon f_thinking a_thinking with dissolve
    pause
    anon a_idle f_skeptical "Anda terlihat sangat akrab."

    keeves f_happy @ f_brag "Ah ya?"

    keeves "Saya sangat mengerti."

    keeves @ a_point "Kau tahu, karena kakakku terkenal dan sebagainya."

    anon f_surprised "Benar-benar?"

    anon f_laugh @ a_point "Apakah kakakmu seorang aktor atau semacamnya?"

    keeves "Nah, dia anggota dewan kota."

    anon f_unimpressed @ -m_talk "..."
    keeves "Di Dakota Utara."

    anon f_skeptical "Kau tahu, menurutku bukan itu..."

    keeves @ -m_talk "Hmm?"

    keeves @ a_raise "Kurasa itu sebuah misteri, kawan kecil."

    jump keeves_button_church.choice


label keeves_button_church.excellent:
    anon f_normal "Bagaimana kabarmu?"

    keeves f_confused "Ugh, {b}Suster Angelica{/b} akhir-akhir ini benar-benar membuatku kedinginan..."

    keeves "Aku tidak tahu kenapa dia selalu begitu tegang tapi itu benar-benar palsu!"

    anon "Oh?"

    keeves @ a_raise "Ya, aku terus mengatakan padanya untuk tidak mengenakan pajak pada pertunjukanku, tapi dia benar-benar kejam."

    anon "kerak?"

    show keeves f_normal a_raise with dissolve
    pause
    show keeves a_idle with dissolve
    anon "Kamu pria yang sangat aneh {b}Pastor Keeves{/b}, kamu tahu itu?"

    keeves @ f_confused "Saya?"

    anon "Ya, tapi itu keren."

    anon @ f_laugh "Kamu juga sangat luar biasa!"

    keeves @ f_laugh a_rock "Hehe, luar biasa!"

    jump keeves_button_church.choice


label kee01_keeves_meet:
    show anon with dissolve
    anon "Um, hai."

    keeves f_happy "Heeey, apa kabar, kawan kecil?!"

    keeves @ a_point "Pertama kali ke sini?"

    anon "Y-ya."

    keeves @ f_laugh a_rock "Bagus sekali!"

    pause
    keeves @ a_raise "Disambut di Rumah Tuhan dan yang lainnya."

    keeves "Saya {b}Pastor Keeves{/b}."

    keeves "Dan bayi bertubuh besar di sebelahku dengan dada besar ini adalah {b}Suster Angelica{/b}."

    show angelica f_surprised with easeinright:
        xoffset 100
    show anon f_surprised
    with {'master': hpunch}
    angelica "AYAH!!!"

    show keeves f_confused with {'master': dissolve}:
        flip
        xoffset 300
    angelica "Anda tidak bisa mengatakan hal seperti itu!"

    show anon f_worried
    show angelica f_normal
    keeves "Hah?"

    angelica "Itu tidak pantas."

    keeves "Oh, maaf {b}Kak{/b}... Itu salahku."

    show keeves f_normal with dissolve:
        unflip
        xoffset -100
    keeves "Dia bukan bayi yang bertubuh besar..."

    keeves "... Dia seorang wanita muda yang sangat saleh."

    pause
    keeves f_happy @ a_raise "Dengan bazonga yang luar biasa!"

    show angelica f_normal_close a_facepalm with dissolve
    angelica "{i}*Huh*{/i} Tuhan, beri aku kekuatan."

    anon @ -m_talk "..."
    show angelica f_normal a_idle with dissolve
    keeves "Jadi, apakah Anda menikmati khotbahnya?"

    anon @ -m_talk "Hmm?"

    anon f_normal "Oh, um... Ya."

    anon @ f_skeptical "Itu sangat unik."

    keeves "Luar biasa, ya... Itulah tujuan saya."

    keeves "Anda tahu, saya ingin menciptakan lingkungan yang sejuk bagi jemaat."

    keeves "Ini benar-benar mendekatkan orang-orang."

    anon "Ah, benarkah?"

    keeves "Ya, atau setidaknya, itulah yang pernah Yesus katakan kepada saya."

    anon f_skeptical "Anda sudah berbicara dengan Yesus?"

    anon "Seperti, Yesus?"

    keeves "Oh, tentu saja!"

    keeves "Saya bertemu dengannya di belakang panggung di konser Wyld Stallyns pada tahun '91."

    anon f_surprised "Anda bertemu Yesus Kristus di belakang panggung di sebuah konser rock?"

    keeves "Tidak, kawan, Yesus Jimenez..."

    show anon f_unimpressed
    keeves "Dia berkata, \"Kalian membuatku takjub malam ini!\""

    keeves "Dan saya berkata, \"Tidak, KAMU menakjubkan, Yesus!\""

    keeves "\"KAMU menakjubkan!\""

    keeves "Dan dia berkata, \"Pesta terus, Ted!\""

    keeves "Hehe."

    keeves "Lalu kami menyalakan beberapa doobage dan makan bakso."

    keeves "Itu adalah saat yang paling penuh kemenangan!"

    anon f_skeptical "Jadi tunggu, kamu tergabung dalam sebuah band?"

    keeves @ f_laugh a_rock "Ahh ya, benar sekali!"

    keeves "Aku dan sahabatku, Bill, ditambah sepasang bayi dari tahun 1400-an."

    anon f_unimpressed "Tahun 1400an?"

    keeves "Itu sebelum insiden bus besar..."

    anon f_surprised "Insiden bus?"

    keeves "Ya, ada pekerjaan aneh yang memasang bom di bus kota..."

    keeves @ a_point "... Itu TIDAK luar biasa."

    pause
    keeves "Setelah itu saya pindah ke New York untuk sementara waktu dan Iblis mencuri istri saya..."

    anon f_unimpressed @ -m_talk "..."
    keeves "... Lalu aku menyelamatkan dunia dari robot..."

    keeves "... Menghabiskan satu tahun bermain quarterback dengan Washington Sentinels..."

    anon "Apa yang-"

    keeves "... Tinggal di rumah danau dengan kotak surat ajaib..."

    keeves "... Menjadi pembunuh terkenal di dunia..."

    anon f_worried "Apakah dia sedang serius saat ini?"

    angelica "Saya tidak tahu."

    angelica f_stern "{b}Ayah{/b}, apakah kamu baik-baik saja?"

    show keeves f_confused with dissolve:
        flip
        xoffset 300
    keeves @ -m_talk "Hmm?"

    keeves "Oh, kawan... setelah kamu menyebutkannya, aku agak lapar."

    keeves f_happy "Apakah kita masih punya sisa cangkir puding yang benar?"

    angelica "T-tidak, aku khawatir kamu memakan semuanya tadi malam."

    keeves "Ahh, palsu!"

    hide keeves with {'master': dissolve}
    keeves "Berapa nomor tempat pizza itu lagi?"

    show angelica f_surprised with dissolve:
        flip
        xoffset 700
    angelica "Tunggu sebentar!"

    angelica -f_surprised "Anda harus mengurus pengakuan!"

    keeves "Minum obat penenang, {b}Kak{/b}."

    keeves "Aku butuh bacon dan sosis Kanada di dalam diriku, secepatnya!"

    hide angelica with {'master': dissolve}
    angelica "{b}Ayah{/b}!"

    pause
    anon f_worried @ -m_talk "(Oke, orang itu entah itu mentalnya atau pendeta paling keren di planet ini!)"

    anon f_laugh @ -m_talk "(Bagaimanapun, aku tertarik.)"

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
