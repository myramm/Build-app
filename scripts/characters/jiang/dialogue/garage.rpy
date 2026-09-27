label jiang_button_garage:
    show anon with dissolve
    anon "Halo."

    show jiang f_suspicious with dissolve:
        unflip
        xoffset 0
    jiang @ -m_talk "Hmm?"

    jiang "Anda butuh sesuatu?"


    menu jiang_button_garage.choice:
        "Garasi yang bagus!":
            jump jiang_button_garage.garage
        "Itu mobil yang aneh...":

            jump jiang_button_garage.truck
        "Tidak.":

            pass

    anon f_normal "Hanya melihat sekeliling."

    jiang f_normal @ f_suspicious "Baiklah, pergilah berkeliaran di tempat lain."

    jiang "Kita tidak seharusnya menerima pelanggan kembali ke sini."

    jiang @ f_suspicious "Anda tahu apa yang saya katakan?"

    anon @ a_wave "Y-ya, oke."

    jiang "Terima kasih."

    hide anon with dissolve
    return


label jiang_button_garage.garage:
    anon f_normal @ f_laugh "Garasi yang bagus!"

    jiang f_suspicious "Ya, terima kasih... kurasa."

    anon "Apakah Anda satu-satunya mekanik di sini?"

    jiang f_normal "Nah, ada beberapa orang yang bekerja di bawahku tapi mereka sedang dihubungi sekarang..."

    anon "Ah, begitu."

    jump jiang_button_garage.choice


label jiang_button_garage.truck:
    anon f_skeptical "Itu mobil yang aneh..."

    jiang f_normal "Heh, sebenarnya itu truk..."

    anon f_surprised "Sebuah truk?"

    jiang "Ya, itu disebut Hypertruck."

    jiang "Mereka menyebutnya {i}THE{/i} kendaraan masa depan."

    anon a_thinking f_thinking "Hmm."

    pause
    anon "Aku tidak menyangka masa depan akan seperti ini..."

    jiang "Jelek?"

    anon f_normal a_idle @ f_snarky a_point "... Ya."

    jiang "Hah, ceritakan padaku tentang hal itu..."

    jump jiang_button_garage.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
