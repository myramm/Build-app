label eve20_tony_lasagna:
    show anon with dissolve:
        flip
    anon "Tolong, saya ambil satu lasagna ukuran besar."

    tony "Sekarang kita bicara!"

    tony "Anda ingin stik roti dengan itu?"


    menu:
        "Tentu saja!":
            jump eve20_tony_lasagna.breadsticks
        "Setelah dipikir-pikir...":
            pass

    anon @ f_thinking a_thinking "Uhh, sebenarnya... Sudahlah."

    anon "Saya tidak membutuhkannya sekarang, saya akan kembali lagi nanti."

    tony @ f_suspicious "Tidak?"

    tony @ f_smirk_closed a_frustrated "Baiklah, juara."

    pause
    tony @ a_point "Kembalilah jika Anda berubah pikiran."

    hide anon with dissolve
    return

label eve20_tony_lasagna.breadsticks:
    anon @ f_snarky "Anda harus punya stik roti!"

    tony @ f_laugh a_belly "Haha, attaboy!"

    tony "Bagaimana kalau saya menambahkan keju Parmesan dan paprika juga?"

    anon "Oh ya, tolong!"

    tony "Itu akan menjadi $20."


    if player.has_money(20):
        jump eve20_tony_lasagna.lasagna

    anon f_worried @ f_surprised "Oh sial."

    anon "Saya tidak punya cukup uang."

    tony f_suspicious "Ya, Anda tidak bisa mendapatkan lasagna tanpa uang."

    tony @ a_fists "Apa yang kamu pikirkan, orang bodoh?"

    anon f_sad_down "Hehe, maaf."

    tony f_normal @ f_smirk a_point "Kembalilah ketika kamu punya uang tunai, oke?"

    anon "Akan dilakukan."

    hide anon with dissolve
    return

label eve20_tony_lasagna.lasagna:
    anon "Ini dia."

    show anon a_money with dissolve
    pause
    show tony f_suspicious a_whisper:
        unflip
        xoffset -400
    show anon a_idle
    with dissolve
    tony "'Eh, {b}Maria{/b}!"

    tony "Ada yang memesan lasagna di sini!"

    show tony a_idle with dissolve
    show anon f_worried
    maria "Ya?"

    maria "Yah, itu bukan alasan untuk membentakku!"

    tony "Cih, aku tidak berteriak..."

    tony "Aku hanya mencoba memesannya!"

    maria "Jadi berbaliklah dan lakukan dengan baik, jika tidak, Anda bisa memasak lasagna Anda sendiri!"

    hide tony with dissolve
    show anon f_sad_down
    tony "Ya Tuhan, {b}Maria{/b}... Kamu tidak harus seperti itu!"

    tony "Anda tahu lasagna saya tidak bisa menandingi lasagna Anda!"

    show anon f_worried
    maria "Hah, tentu saja aku tahu itu."

    maria "Aku hanya memastikan kamu juga melakukan hal yang sama."

    tony "Oh, sekarang itu kejam sekali!"

    tony "Haha!"

    maria "Haha!"

    show anon f_normal
    maria "Ya, ya... Ayo, beri aku ciuman, dasar bodoh."

    tony "Ah baiklah, siapa yang bisa menolaknya?"

    pause
    tony "Hehehe."

    show tony behind counter with dissolve:
        flip
    tony "{i}*Ahem*{/i} Dia akan segera mengeluarkannya."

    anon "Tidak masalah."

    pause
    show maria a_lasagna behind counter with dissolve:
        flip
        xoffset -150
    maria "Ini makananmu."

    show anon a_lasagna
    show maria a_back
    with dissolve
    anon "Terima kasih!"

    maria f_angry "Kamu bisa melakukan itu di sini untukku, tahu?"

    show tony f_suspicious with dissolve:
        unflip
        xoffset -200
    anon f_brag_closed @ -m_talk "(Oh, baunya enak sekali.)"

    anon @ -m_talk "(Saya harap gadis-gadis menyukainya.)"

    show anon f_worried
    tony "Anda tidak mengatakan apa pun tentang membutuhkan bantuan!"

    maria "Yah, seharusnya aku tidak perlu melakukannya, bukan?"

    maria "Suami yang baik akan menawarkan bantuan kepada istrinya tanpa diminta!"

    tony "Apa aku terlihat seperti pembaca pikiran bagimu?!"

    tony @ f_eyeroll "Untuk apa kamu menghancurkan keberanianku, ya?"

    anon @ -m_talk "( Hmm, sepertinya mereka akan berdebat sebentar. )"

    maria "Mungkin jika Anda melakukan sesuatu dengan benar sesekali..."

    tony "Ah, jangan pergi ke sana!"

    anon @ -m_talk "(Saya harus {b}kembali ke tempat Eve{/b}. )"

    hide anon with dissolve
    return 'lasagna'
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
