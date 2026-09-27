label tony_dialogue_order:
    anon "Tolong, saya ambil satu pizza besar."

    tony f_normal "Sekarang kita bicara!"

    tony "Kue apa yang sedang kamu cari?"


    menu:
        "Pizza vegetarian ($20)." if M_daisy.is_state(S_daisy_get_pizza) and not player.has_item('veggie_pizza'):
            jump dai02_tony_veggie

        "Pizza vegetarian ($20)." if M_daisy.get('veggie pizza') and not player.has_item('veggie_pizza'):
            jump tony_dialogue_order.veggie
        "Sudahlah.":

            pass

    anon "Uhh, sebenarnya... Sudahlah."

    anon "Lagipula aku tidak menginginkannya."

    tony "Tidak?"

    tony "Baiklah, Nak."

    pause
    tony "Kembalilah jika Anda berubah pikiran."

    hide anon with dissolve
    return


label tony_dialogue_order.veggie:
    anon "Bolehkah saya pesan {b}pizza vegetarian{/b} lagi?"

    tony "Tentu saja, Nak."

    tony "Itu akan menjadi $20."


    if player.has_money(20):
        jump tony_dialogue_order.pizza

    anon f_worried "Oh sial."

    anon "Saya tidak punya cukup uang."

    show tony f_question
    tony "Ya, Anda tidak bisa mendapatkan pizza tanpa uang."

    tony "Apa yang kamu pikirkan, orang bodoh?"

    show tony f_suspicious
    anon f_shy @ a_behind_head "Hehe, maaf."

    show tony f_question
    tony "Kembalilah ketika kamu punya uang tunai, oke?"

    show tony f_suspicious
    anon f_worried "Akan dilakukan."

    hide anon with dissolve
    return


label tony_dialogue_order.pizza:
    anon "Ini dia."

    show anon a_money with dissolve
    pause
    show anon a_idle
    show tony f_question a_whisper:
        unflip
        xoffset -400
    with dissolve
    tony "'Eh, {b}Maria{/b}!"

    tony "Satu sayuran dengan jamur dan nanas, siap disajikan."

    maria "Ya, ya..."

    hide tony with dissolve
    maria "Kau tahu, ibuku akan membakar tempat ini hingga rata dengan tanah sebelum dia menaruh nanas di atas pizza..."

    maria "... Itu tidak benar."

    tony "Ya, untung saja aku menikahimu dan bukan ibumu, bukan?"

    maria "Haha!"

    pause
    show tony a_pizza behind counter with dissolve:
        flip
    tony "Ini kuemu, Nak."

    show tony a_idle
    show anon a_pizza
    with dissolve
    anon "Terima kasih, {b}Tony{/b}."

    hide anon with dissolve
    return 'veggie_pizza'
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
