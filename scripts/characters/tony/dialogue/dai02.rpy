label dai02_tony_veggie:
    anon "Bisakah saya mendapatkannya dengan semua sayuran?"

    tony "Tentu saja, jagoan!"

    tony @ a_point "Anda ingin jamur dan nanas juga?"

    anon @ f_laugh "Oh ya, tolong!"

    tony @ f_smirk_wink "Itu akan menjadi $20."


    if player.has_money(20):
        jump dai02_tony_veggie.pizza

    anon f_worried "Oh sial."

    anon "Saya tidak punya cukup uang."

    tony f_question "Ya, Anda tidak bisa mendapatkan pizza tanpa uang."

    tony "Apa yang kamu pikirkan, orang bodoh?"

    show tony f_suspicious
    anon f_normal @ f_shy a_behind_head "Hehe, maaf."

    tony f_normal @ a_frustrated "Kembalilah ketika kamu punya uang tunai, oke?"

    anon "Akan dilakukan."

    hide anon with dissolve
    return

label dai02_tony_veggie.pizza:
    anon "Ini dia."

    show anon a_money with dissolve
    pause
    show anon a_idle
    show tony f_question:
        unflip
        xoffset -400
    with dissolve
    tony "'Eh, {b}Maria{/b}!"

    tony "Kami mendapat pelanggan di sini!"

    show tony f_suspicious
    maria "Aku tahu kamu tidak berteriak kepadaku sekarang, {b}Tony{/b}!"

    maria "Anda bisa membalikkan badan dan bertanya dengan sopan."

    show tony f_normal a_heart with dissolve
    tony "Ah, sial."

    tony "Bisakah kamu mempercayai wanita ini?"

    show anon f_looking_down a_phone with dissolve
    tony "Cih, bola di tubuhnya..."

    hide tony with dissolve
    tony "Sekarang kamu lihat di sini wanita..."

    tony "Seharusnya kamu yang di sini berurusan dengan pelanggan."

    tony "Tuhan tahu, kami akan mendatangkan lebih banyak bisnis jika mereka melihat wajah cantikmu di sini, bukannya mug jelek ini."

    maria "Ya, tapi mereka tidak akan pernah kembali setelah mencicipi masakanmu!"

    tony "Oh, sekarang itu kejam sekali!"

    tony "Haha!"

    maria "Haha!"

    maria "Ya, ya... Ayo, beri aku ciuman dan ambil paimu."

    tony "Ah baiklah, siapa yang bisa menolaknya?"

    pause
    tony "Hehehe."

    show tony a_pizza behind counter with dissolve:
        flip
    tony "{i}*Ahem*{/i} Uhh, maaf soal itu semua."

    anon f_normal a_idle "Tidak masalah."

    tony "Ini kuemu."

    show tony a_idle
    show anon a_pizza
    with dissolve
    tony "Menikmati!"

    anon f_brag_closed @ -m_talk "(Oh, baunya enak sekali.)"

    anon @ -m_talk "(Saya harap {b}Daisy{/b} menyukainya. )"

    hide anon with dissolve
    return 'veggie_pizza'
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
