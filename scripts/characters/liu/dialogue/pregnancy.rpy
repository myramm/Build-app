label liu_pregnancy_summon:
    scene expression player.location.background
    "{i}*Brrrzzzt* *Brrrzzzt*{/i}"


    scene expression background(768, 384, 2, l=L_liu_lounge) as underlay:
        xoffset -400
    show liu a_phone_talk b_robe_hair f_nervous:
        xoffset -500

    $ renpy.dynamic(stage=player.location.background_phone)
    show expression stage as stage
    show anon f_confused with dissolve:
        xzoom -1
    anon @ -m_talk "Hmm?"

    anon a_phone f_normal_low "{b}Liu{/b} menelepon saya."

    show anon a_phone_talk f_normal with dissolve:
        xoffset 500
        xzoom 1
    show expression stage as stage at phoneleft with phoneleft.show
    anon "{b}Liu{/b}?"

    liu "H-hei, {b}[firstname]{/b}."

    liu "aku um..."

    liu f_frightened "... S-sesuatu telah terjadi, dan... Aku uhh... perlu bertemu denganmu."

    anon f_worried "Sesuatu telah terjadi?"

    show liu f_ashamed_down
    pause
    anon "Apakah kamu baik-baik saja?"

    liu f_nervous_down "Y-ya, aku-"

    liu f_worried_down "Err, tidak... aku tidak... sungguh..."

    anon f_confused "Apa yang terjadi, {b}Liu{/b}?"

    liu f_worried "Bisakah kamu datang ke apartemenku... kumohon?"

    liu "Aku benar-benar perlu bertemu denganmu."

    anon f_worried "Ya, tentu saja!"

    anon "Saya akan segera ke sana."

    liu "Terima kasih."

    show anon a_phone f_worried_low
    show liu a_phone f_worried_down
    with dissolve
    show expression stage as stage with {'master': phoneleft.hide}
    "{i}*Bip*{/i}"

    anon @ -m_talk "(Astaga, sepertinya dia hampir menangis...)"

    anon f_worried @ -m_talk "(... Apa yang mungkin terjadi?! )"

    show anon a_idle with {'master': dissolve}:
        xoffset 0
        xzoom -1
    anon @ -m_talk "( {b}Sebaiknya aku segera ke apartemen Liu{/b} dan mencari tahu apa yang terjadi. )"

    hide anon with dissolve
    return


label liu_pregnancy_summon.repeat:
    scene expression player.location.background
    "{i}*Brrrzzzt* *Brrrzzzt*{/i}"


    scene expression background(768, 384, 2, l=L_liu_lounge) as underlay:
        xoffset -400
    show liu a_phone_talk b_robe_hair f_nervous:
        xoffset -500

    $ renpy.dynamic(stage=player.location.background_phone)
    show expression stage as stage
    show anon f_confused with dissolve:
        xzoom -1
    anon @ -m_talk "Hmm?"

    anon a_phone f_normal_low "{b}Liu{/b} menelepon saya."

    show anon a_phone_talk f_normal with dissolve:
        xoffset 500
        xzoom 1
    show expression stage as stage at phoneleft with phoneleft.show
    anon "{b}Liu{/b}?"

    liu "H-hei, {b}[firstname]{/b}."

    liu f_nervous_down "Kami um..."

    liu f_nervous "... T-perlu membicarakan sesuatu?"

    anon f_worried "Apakah semuanya baik-baik saja?"

    liu "Y-ya, semuanya baik-baik saja... Hanya saja..."

    liu f_worried "...Yah, lebih baik mengatakannya secara langsung."

    liu "{b}Bisakah kamu datang ke apartemenku?{/b}"

    anon "Ya, tentu saja!"

    anon "Saya akan segera ke sana."

    liu f_nervous "Terima kasih."

    show anon a_phone f_worried_low
    show liu a_phone f_worried_down
    with dissolve
    show expression stage as stage with {'master': phoneleft.hide}
    "{i}*Bip*{/i}"

    anon f_confused @ -m_talk "(Hmm, aku ingin tahu tentang apa itu?)"

    show anon a_idle f_worried with {'master': dissolve}:
        xoffset 0
        xzoom -1
    anon @ -m_talk "( {b}Sebaiknya aku segera ke apartemen Liu{/b} dan mencari tahu apa yang terjadi. )"

    hide anon with dissolve
    return


label liu_pregnant_announcement_2:
    scene expression player.location.background_blur
    if player.location != L_map:
        show anon with dissolve
    anon @ -m_talk "( Sebaiknya {b}cepat ke apartemen Liu{/b} dan mencari tahu apa yang terjadi. )"

    if player.location != L_map:
        hide anon with dissolve
    return


label liu_pregnant_labor_1:
    scene expression player.location.background_blur
    show anon f_normal with dissolve
    anon "Sepertinya aku mendapat pesan teks."

    hide anon with dissolve
    return


label liu_pregnant_labor_2:
    scene expression player.location.background_blur
    if player.location != L_map:
        show anon f_surprised a_phone with dissolve
    anon "{b}Liu{/b} akan melahirkan?!"

    anon "Sialan!"

    pause
    anon "Sebaiknya saya {b}pergi ke rumah sakit{/b} untuk memeriksanya."

    if player.location != L_map:
        hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
