label yoyo_button_lounge:
    show anon f_worried with dissolve
    anon @ -m_talk "(Oh tidak, aku tidak mau membahasnya sekarang.)"

    pause
    anon f_worried_surprised @ -m_talk "( Hal terakhir yang saya perlukan adalah semangkuk mie untuk topi... )"

    anon f_surprised_teeth @ -m_talk "(... Josie tidak akan pernah membiarkanku mendengar bagian akhirnya.)"

    hide anon with dissolve
    return


label yoyo_button_lounge.unknown:
    show anon f_confused with dissolve
    anon @ -m_talk "(Hmm... Aku penasaran siapa gadis itu?)"

    pause
    anon f_surprised @ -m_talk "(Dia benar-benar ingin makan mie itu...)"

    anon f_worried @ -m_talk "( ... Mungkin aku akan kembali ketika dia sudah tidak terlalu sibuk. )"

    hide anon with dissolve
    return


label yoyo_button_lounge.unsure:
    show anon a_sides f_confused with dissolve
    anon @ -m_talk "(Dia tampak begitu tulus tentang \"kue aplikasi\" itu... )"

    anon f_thinking @ -m_talk "( ... Dan aku sangat menyukai krim pisang. )"

    pause
    show anon a_rub f_confused
    with {'master': dissolve}
    anon @ -m_talk "(Hmm. Aku harus tidur di sana, dan mungkin menemukannya di ruang pamer besok.)"

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
