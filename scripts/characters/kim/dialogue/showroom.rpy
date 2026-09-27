label kim_button_showroom:
    show anon f_worried with dissolve
    kim "Apa yang kamu inginkan, anak malang?"

    kim f_normal "aku tidak punya waktu untukmu..."


    menu kim_button_showroom.choice:

        "Bolehkah saya melihat ponsel Anda?" if M_anon.between_states(S_ano07_mech, S_ano07_give):
            jump ano07_hint_kim
        "Kamu sangat kasar, kamu tahu itu?":

            jump kim_button_showroom.rude

        "Karyawan bulan ini?" if M_kim.eotm:
            jump kim_button_showroom.employee

        "Rusia?" if M_kim.russians:
            jump kim_button_showroom.russians
        "Kamu payah. aku pergi.":

            pass

    anon "Kamu payah. aku pergi."

    kim "Ya, kamu pulang ke keluarga miskin."

    kim "Kembalilah ketika Anda punya uang."

    kim @ f_laugh "Rona rona rona!!"

    hide anon with {'master': dissolve}
    kim @ a_wave "Sampai jumpa, anak malang!"

    return


label kim_button_showroom.employee:
    anon f_worried @ f_skeptical "Karyawan bulan ini?"

    kim @ a_counter_raised "Ya, {b}Kim{/b} adalah saresman mobil terbaik nomor satu!"

    kim "Segera, saya memiliki prace ini."

    anon "Saya meragukan hal itu."

    kim @ f_curious "Oh, prese... Apa yang kamu tahu, anak malang?!"

    anon @ f_skeptical "Aku tahu kamu brengsek dan orang-orang tidak menyukainya..."

    kim @ f_laugh "Rona rona rona!"

    kim "{b}Kim{/b} taklukkan rasa sayang terhadap mobil!"

    kim "Tunggu dan lihat."

    anon f_surprised "Menaklukkan?"

    kim a_counter_raised "Ya, {b}Kim{/b} menjadi bos."

    show anon f_unimpressed
    kim "Kemudian {b}Kim{/b} berekspansi ke jaringan nasional!"

    kim "Tutupi seluruh bangsa dengan kasih sayang!!"

    anon @ -m_talk "..."
    kim "Bangsa pertama, lalu pranet!"

    kim a_idle @ f_laugh "Rona rona rona rona!"

    kim @ a_rub "{b}Kim{/b} jadilah kekasih TUHAN!!!"

    anon "Apa-apaan ini?"

    kim @ f_laugh "HUE HUE HUE!!!"

    jump kim_button_showroom.choice


label kim_button_showroom.rude:
    anon f_worried "Kamu sangat kasar, kamu tahu itu?"

    kim f_curious "Aww, kamu akan menangis, bocah malang?"

    anon "T-tidak."

    kim f_baby_cry a_cry "Boo hoo, aku sangat malang..."

    anon f_sad "Diam!"

    kim f_normal a_idle @ f_laugh "Rona rona rona!"

    show anon a_thinking f_thinking with dissolve
    pause
    anon f_skeptical a_idle "Aku akan memberitahu atasanmu tentang caramu memperlakukanku!"

    kim "Teruskan."

    kim "Mereka tidak tertarik padamu."

    show anon f_worried
    kim @ a_counter_raised "{b}Kim{/b} adalah penjual terbaik!"

    kim "Karyawan bulan ini, selama lima bulan berturut-turut."

    $ M_kim.set('eotm', True)
    kim "Aku menghasilkan banyak uang."

    kim "Dasar anak malang yang bodoh."

    anon "Kita akan lihat mengenai hal itu..."

    kim @ f_curious "{i}*Menguap*{/i}"

    kim "Anda mengaduk-aduk?"

    kim @ a_wave "Pergilah, anak malang."

    kim "Kamu membuat {b}Kim{/b} sangat menyeramkan."

    jump kim_button_showroom.choice


label kim_button_showroom.russians:
    anon f_worried "Saya dengar Anda punya pelanggan tetap Rusia yang membeli banyak mobil?"

    kim f_curious "Di mana kamu mendengar ini, bocah malang?!"

    anon "{b}Yosephine{/b}."

    kim @ -m_talk "Hmm."

    kim "Jadi bagaimana jika saya melakukannya?"

    kim f_normal "Itu bukan urusanmu!"

    anon "Baiklah, saya berharap Anda dapat memberi saya beberapa informasi tentang mereka?"

    kim "Pfft!"

    kim f_angry @ a_point "Anda berharap di satu sisi dan kotoran di sisi lain, lihat mana yang lebih dulu."

    anon f_unimpressed "Ayolah, kawan."

    anon "Ini sangat penting..."

    kim "{b}Kim{/b} tidak ada apa-apanya!"

    kim "Kamu pergi sekarang!"

    anon @ -m_talk "..."
    hide anon with {'master': dissolve}
    kim f_smirk a_wave "Sampai jumpa, anak malang!"

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
