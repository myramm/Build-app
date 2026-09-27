label maria_pregnancy_summon:
    scene expression player.location.background
    "{i}*Brrrzzzt* *Brrrzzzt*{/i}"


    scene expression L_pizzeria_interior.background_closeup
    show tony a_phone_talk:
        unflip
        xoffset -450
    show expression game.timer.image('char_xtra_12{}') as counter

    $ renpy.dynamic(stage=player.location.background_phone)
    show expression stage as stage
    show anon f_confused with dissolve:
        flip
    anon @ -m_talk "Hmm?"

    show anon a_phone f_worried_low with dissolve
    pause
    anon f_shy_low "It's {b}Tony{/b}."

    show anon a_phone_talk f_normal with dissolve:
        unflip
        xoffset 500
    show expression stage as stage at phoneleft with phoneleft.show
    anon "Halo?"

    tony "Hey, champ!"

    tony "I need you down here at the pizzeria ASAP!"

    anon f_worried "Apakah semuanya baik-baik saja?"

    anon "Did something happen?"

    tony f_smirk "Yeah, I'll explain when you get here."

    show anon f_normal
    tony "Just get ya butt down here, capisce?"

    anon "B-baiklah."

    show anon f_shy_low a_phone with dissolve
    show expression stage as stage with {'master': phoneleft.hide}
    "{i}*Bip*{/i}"

    anon @ -m_talk "(Hmm, aku ingin tahu apa yang terjadi?)"

    anon @ -m_talk "( I should {b}swing by the pizzeria{/b} and find out. )"

    hide anon with dissolve
    return


label maria_pregnancy_summon.repeat:
    scene expression player.location.background
    "{i}*Brrrzzzt* *Brrrzzzt*{/i}"


    scene expression L_pizzeria_interior.background_closeup
    show tony a_phone_talk:
        unflip
        xoffset -450
    show expression game.timer.image('char_xtra_12{}') as counter

    $ renpy.dynamic(stage=player.location.background_phone)
    show expression stage as stage
    show anon f_confused with dissolve:
        flip
    anon @ -m_talk "Hmm?"

    show anon a_phone f_worried_low with dissolve
    pause
    anon f_shy_low "It's {b}Tony{/b}."

    show anon a_phone_talk f_normal with dissolve:
        unflip
        xoffset 500
    show expression stage as stage at phoneleft with phoneleft.show
    tony "Hey, champ?"

    tony "I need you down here at the pizzeria ASAP!"

    anon "Tentu saja."

    anon "Saya akan segera ke sana."

    show anon f_shy_low a_phone with dissolve
    show expression stage as stage with {'master': phoneleft.hide}
    "{i}*Bip*{/i}"

    anon @ -m_talk "(Hmm, aku ingin tahu apa yang terjadi?)"

    anon @ -m_talk "( I should {b}swing by the pizzeria{/b} and find out. )"

    hide anon with dissolve
    return


label maria_pregnant_announcement_2:
    scene expression player.location.background_blur
    if player.location != L_map:
        show anon with dissolve
    anon @ -m_talk "(Hmm, aku ingin tahu apa yang terjadi?)"

    anon @ -m_talk "( I should {b}swing by the pizzeria{/b} and find out. )"

    if player.location != L_map:
        hide anon with dissolve
    return


label maria_pregnant_labor_1:
    scene expression player.location.background_blur
    show anon f_normal with dissolve
    anon "Sepertinya aku mendapat pesan teks."

    hide anon with dissolve
    return


label maria_pregnant_labor_2:
    scene expression player.location.background_blur
    if player.location != L_map:
        show anon f_surprised a_phone with dissolve
    anon "{b}Maria{/b} had the baby?!"

    anon "Sialan!"

    anon "Sebaiknya saya {b}pergi ke rumah sakit{/b} untuk memeriksanya."

    if player.location != L_map:
        hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
