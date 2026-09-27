label ano25_find_tony:
    return

label ano25_find_tony.pizzeria:
    show tony f_smirk
    show anon with dissolve:
        flip
    tony "Kamu sudah mendapatkan tasnya?"

    anon f_worried "T-tidak, belum."

    show tony f_normal
    pause
    anon "Dimana itu lagi?"

    tony "{b}Cari tas duffel abu-abu di lemari kamar tidur kami{/b}."

    tony m_talk "Seharusnya cukup mudah dikenali."


    if 'a_baby' not in renpy.get_attributes('tony'):
        show tony a_point with {'master': dissolve}

    tony "Dan jangan biarkan {b}Maria{/b} mengintip apa yang ada di dalamnya, ya?"


    if 'a_baby' not in renpy.get_attributes('tony'):
        show tony a_idle with {'master': dissolve}

    tony -m_talk "Katakan saja padanya ada sesuatu yang rusak di rumahmu dan aku mengirimmu untuk meminjam beberapa peralatan."

    tony "Capiche?"

    anon "{b}Tas ransel abu-abu, lemari kamar tidur.{/b}"

    anon "Saya mengerti."

    pause
    anon "Saya akan kembali."

    hide anon with dissolve
    return


label ano25_find_tony.bank:
    show anon with dissolve:
        flip
    tony "Ya bawa tasnya?"

    anon f_worried "T-tidak, belum."

    pause
    tony f_angry @ a_frustrated "Yesus, juara..."

    tony "...bagaimana kita bisa merampok bank tanpa senjata, ya?!"

    anon "Maaf, {b}Tony{/b}."

    anon "Dimana itu lagi?"

    tony "{b}Cari tas duffel abu-abu di lemari kamar tidur kami{/b}."

    tony "Seharusnya cukup mudah dikenali."

    tony @ -m_talk "Dan jangan biarkan {b}Maria{/b} mengintip apa yang ada di dalamnya, ya?"

    tony "Katakan saja padanya ada sesuatu yang rusak di rumahmu dan aku mengirimmu untuk meminjam beberapa peralatan."

    tony "Capiche?"

    anon "{b}Tas ransel abu-abu, lemari kamar tidur.{/b}"

    anon f_normal "Saya mengerti."

    pause
    anon f_worried a_behind_head "Saya akan kembali."

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
