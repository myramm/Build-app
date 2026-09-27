label sara_button_lobby:
    show anon with dissolve
    sara "Butuh bantuan, ya?"


    menu sara_button_lobby.choice:
        "Saya baik-baik saja, terima kasih!":
            pass

    anon f_normal "Saya baik-baik saja, terima kasih!"

    sara f_normal "Oke dokie!"

    hide anon with dissolve
    return


label sara_button_lobby.job:
    show anon with dissolve
    anon "Nona {b}Sara{/b}?"

    sara "Hai, {b}[firstname]{/b}!"

    anon "Apa yang kamu lakukan di sini?"

    sara "Menonton meja depan, tentu saja..."

    anon "Anda bekerja di sini?"

    sara @ -m_talk "Mhmm."

    pause
    sara "Bayarannya tidak banyak tetapi mereka hanya menagih setengah harga untuk apartemen kami."

    anon "Ya, itu bagus."

    sara "Ya, itu pengaturan yang cukup bagus."

    sara "Beri tahu saya jika Anda memerlukan bantuan untuk menemukan seseorang."

    anon "O-oke, terima kasih."

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
