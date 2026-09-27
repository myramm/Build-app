label melonia_pregnancy_summon:
    scene expression player.location.background
    "{i}*Brrrzzzt* *Brrrzzzt*{/i}"


    scene expression background(288, 368, 3.5, l=L_rump_second) as underlay:
        xoffset -400
    show iwanka b_dressed_magic a_phone f_bored:
        xoffset -500

    $ renpy.dynamic(stage=player.location.background_phone)
    show expression stage as stage
    show anon f_confused with dissolve:
        flip
    anon @ -m_talk "Hmm?"


    if not M_iwanka.once('number_known'):
        anon a_phone f_thinking_down "Itu {b}Iwanka{/b}."

        show anon a_phone_talk f_normal with dissolve:
            unflip
            xoffset 500
    else:

        anon a_phone f_thinking_down "Saya tidak mengenali nomor ini..."

        show anon a_phone_talk f_skeptical with dissolve:
            unflip
            xoffset 500

    show expression stage as stage at phoneleft with phoneleft.show
    anon "Halo?"

    iwanka "Hai, {b}[firstname]{/b}."

    anon f_skeptical "{b}Iwanka{/b}?"

    iwanka "Ya, dengarkan..."

    iwanka "... Anda harus segera ke sini secepatnya."

    anon f_worried "Apakah semuanya baik-baik saja?"

    iwanka "Ada yang salah dengan {b}ibuku{/b}... Dia seperti pingsan total."

    anon "{b}Melonia{/b} terbalik?"

    anon "Apa terjadi sesuatu pada bak mandi air panas?"

    iwanka f_annoyed "Entahlah, hanya... Kemarilah, ya?"

    anon "Y-ya, oke."

    show anon f_sad_down a_phone with dissolve
    show expression stage as stage with {'master': phoneleft.hide}
    "{i}*Bip*{/i}"

    pause
    anon f_tired @ -m_talk "( Sepertinya sebaiknya aku {b}cepat ke perkebunan Rump{/b} dan memeriksa {b}Melonia{/b}. )"

    hide anon with dissolve
    return


label melonia_pregnancy_summon.repeat:
    scene expression player.location.background
    "{i}*Brrrzzzt* *Brrrzzzt*{/i}"


    scene expression background(288, 368, 3.5, l=L_rump_second) as underlay:
        xoffset -400
    show iwanka b_dressed_magic a_phone f_bored:
        xoffset -500

    $ renpy.dynamic(stage=player.location.background_phone)
    show expression stage as stage
    show anon f_confused with dissolve:
        flip
    anon @ -m_talk "Hmm?"

    anon a_phone f_thinking_down "Itu {b}Iwanka{/b}."

    show anon a_phone_talk f_normal with dissolve:
        unflip
        xoffset 500
    show expression stage as stage at phoneleft with phoneleft.show
    anon "Halo?"

    iwanka "Kawan, apakah kamu memukul ibuku lagi?!"

    anon f_worried "Hah?"

    iwanka "Dia benar-benar terbalik di sini!"

    anon "Aduh, bung..."

    anon "Saya akan segera ke sana."

    iwanka f_normal @ f_laugh "Hehe, kamu sangat kacau..."

    show anon f_sad_down a_phone with dissolve
    show expression stage as stage with {'master': phoneleft.hide}
    "{i}*Bip*{/i}"

    pause
    anon f_tired @ -m_talk "( Sepertinya sebaiknya aku {b}cepat ke perkebunan Rump{/b} dan memeriksa {b}Melonia{/b}. )"

    hide anon with dissolve
    return


label melonia_pregnant_announcement_2:
    scene expression player.location.background_blur
    if player.location != L_map:
        show anon with dissolve
    anon @ -m_talk "(Hmm, aku ingin tahu apa yang terjadi?)"

    anon @ -m_talk "( Sebaiknya aku {b}cepat ke perkebunan Rump{/b} dan memeriksa {b}Melonia{/b}. )"

    if player.location != L_map:
        hide anon with dissolve
    return


label melonia_pregnant_labor_1:
    scene expression player.location.background_blur
    show anon f_normal with dissolve
    anon "Sepertinya aku mendapat pesan teks."

    hide anon with dissolve
    return


label melonia_pregnant_labor_2:
    scene expression player.location.background_blur
    if player.location != L_map:
        show anon f_surprised a_phone with dissolve
    anon "{b}Melonia{/b} akan melahirkan?!"

    anon "Sialan!"

    pause
    anon "Sebaiknya saya {b}pergi ke rumah sakit{/b} untuk memeriksanya."

    if player.location != L_map:
        hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
