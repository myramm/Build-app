label tin02_init_liu:
    anon f_normal "Apakah Tina ada?"

    liu f_normal "Ya, di kantornya."

    pause
    liu f_curious "Apakah dia mengharapkanmu?"

    anon f_worried "Mengharapkanku?"

    liu "Ya, apakah kamu punya janji?"

    anon "Hmm..."

    pause
    anon f_shy "... Ya?"

    pause
    liu f_normal @ f_laugh "Oke, kamu bisa kembali."

    anon f_surprised "Saya bisa?"


    if M_anon.finished_state(S_ano14_find):
        show anon a_wave with {'master': dissolve}
        anon f_normal "Terima kasih, {b}Liu{/b}!"

    else:
        anon f_shy "Eh, maksudku, terima kasih!"

        liu "Terima kasih telah melakukan perbankan bersama kami, semoga harimu menyenangkan!"

        anon "Y-ya, kamu juga."


    hide anon with dissolve
    return 'office'
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
