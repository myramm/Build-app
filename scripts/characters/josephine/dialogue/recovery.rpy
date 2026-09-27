label josie_button_recovery:
    show anon with dissolve
    josephine f_sexy "Hai, {b}[firstname]{/b}."

    josephine "Anda datang untuk memeriksa kami lagi?"


    menu josie_button_recovery.choice:
        "Ya.":
            pass

    anon f_normal "Ya."

    josephine f_sexy "Anda terlalu khawatir."

    josephine "Kami baik-baik saja."

    anon "Ya, saya tahu."

    anon "Aku hanya ingin memastikan..."

    pause
    anon "... Dan mungkin melihat sekilas tentang menyusui."

    josephine @ f_laugh "Hah!"

    josephine "Sangat lucu."

    josephine "Anda seharusnya mengoleskan minyak lanolin ke puting saya setiap kali selesai menyusui, Anda tahu?"

    anon "Oh, kalau begitu, lupakan saja!"

    josephine @ f_laugh "hehe!"

    anon "Aku akan membiarkan kalian kembali beristirahat, oke?"

    josephine f_sexy_down @ -m_talk "Mhmm."

    anon @ f_laugh a_wave "Sampai jumpa, si kecil."

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
