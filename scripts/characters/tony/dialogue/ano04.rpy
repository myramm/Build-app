label ano04_late_tony:
    show tony f_suspicious
    show anon behind tony with dissolve
    tony "Aku membutuhkanmu, Nak."

    show anon f_worried
    tony "Dimana kamu tadi?"

    show anon f_sad_down
    pause
    tony "Ah, jangan terlihat seperti itu, kembalilah besok."

    tony "Kami akan mencoba lagi, ya?"

    anon f_worried "Maaf Untuk--"

    tony "Muncul saja kali ini. Ayolah, sampai jumpa besok."

    anon a_salute "Ya, tuan!"

    hide anon with dissolve
    return


label ano04_test_tony:
    show anon with dissolve:
        flip
    tony "Anda sudah mendapatkan sepeda itu?"


    if player.transport_level:
        anon "Ya, saya mengerti."

        tony "Senang mendengarnya."

        tony "Ambil pizza ini dan lihat pizza tersebut diantar ke tempat yang tepat."

        tony @ f_suspicious "Jangan main-main sekarang, kamu dengar aku?"

        anon "saya tidak akan melakukannya."

        tony "Ketika kamu kembali, aku akan membayarmu dengan sangat baik."

        anon "Terima kasih, {b}Tony{/b}."

        anon "Saya akan kembali dalam sekejap, Anda akan lihat."

        tony @ f_laugh "Ahh, pergi dari sini, dasar bodoh!"

    else:
        anon f_worried "Belum, Pak."

        tony f_suspicious "Nah, tunggu apa lagi?!"

        tony "Aku butuh pizza ini diantar hari ini, dasar bodoh!"

        anon "Saya akan {b}ke mal dan membeli sepeda{/b} sekarang."


    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
