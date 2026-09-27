label hospital_recovery_liu_first:
    scene expression game.timer.image('location_hospital_baby_bed{}')
    show liu b_gown_bed
    with fade
    show anon a_sides f_surprised with {'master': dissolve}
    liu f_happy_excited_closed "{b}[firstname]{/b}!"

    show liu f_happy
    anon f_surprised "I-is that?"

    show liu f_happy_baby

    if M_liu.pregnancy.baby_gender == 'boy':
        liu "Our son."

    else:
        liu "Our daughter."


    show anon f_shy_low with dissolve:
        xoffset 208
    liu "Look who's here, little one."

    liu f_happy "It's your daddy."

    show anon a_knock f_flirt_low
    show liu f_happy_baby
    with {'master': dissolve}
    anon "Hey there..."

    show anon f_surprised_low

    if M_liu.pregnancy.baby_gender == 'boy':
        anon "... {i}*Gasp*{/i} Oh, my gosh, he's so beautiful!"

    else:
        anon "... {i}*Gasp*{/i} Oh, my gosh, she's so beautiful!"


    show anon a_sides f_happy
    show liu f_happy
    with {'master': dissolve}

    if M_liu.pregnancy.baby_gender == 'boy':
        liu "He is, isn't he?"

    else:
        liu "She is, isn't he?"


    show liu f_happy_baby
    show anon f_shy_low

    if M_liu.pregnancy.baby_gender == 'boy':
        anon "Look at those tiny little fingers!"

    else:
        anon "Look at those tiny little toes!"


    liu f_laugh "hehe!"

    show liu f_happy
    pause
    anon f_normal "So everything went okay?"

    liu f_normal "Yeah, the doctor said it was one of the easiest babies he's ever delivered."

    anon "Well, I guess your chinese remedies really worked then, huh?"

    liu f_happy "Hehe, ya."


    if M_liu.pregnancy.first_baby:
        liu "I'll have to let my mother know when I write her."

        liu f_happy_excited_closed "She'll be so excited when she learns that she's a grandmother."

        show liu f_happy
        pause

    anon f_confused "How long are they keeping you?"

    show anon f_normal
    liu f_normal "Just a couple more days."

    liu f_happy_baby "Then we'll be back home."

    anon f_happy "Saya tidak sabar."

    show anon f_shy_low
    pause
    anon f_normal "Do you need anything while I'm here?"

    liu "Tidak, kami baik-baik saja."

    show liu f_happy

    if M_liu.pregnancy.baby_gender == 'boy':
        liu "The nurse is supposed to be coming by any second to help me feed him."

    else:
        liu "The nurse is supposed to be coming by any second to help me feed her."


    anon f_confused "Oh?"

    show anon f_worried
    show liu f_nervous_down

    if M_liu.pregnancy.baby_gender == 'boy':
        liu "He's been a little fussy about latching on."

    else:
        liu "She's been a little fussy about latching on."


    show liu f_nervous
    anon "Well, I'll get out of your hair then."

    anon f_normal "Hubungi saya jika Anda butuh sesuatu, ya?"

    liu f_happy "Saya akan."

    liu "Terima kasih, {b}[firstname]{/b}."

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
