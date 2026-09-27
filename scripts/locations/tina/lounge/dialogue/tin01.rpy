label tin01_init_tina_lounge:
    scene location_apt_hall3_301_closeup as stage
    show location_apt_hall3_301_closeup_door1 as door behind stage
    show location_apt_hall3_301_closeup as doorframe:
        crop (768, 0, 256, 768)
        right
    show anon a_knock with dissolve
    "{i}*Ketuk* *Ketuk*{/i}"

    show anon a_sides with dissolve
    pause
    show location_apt_hall3_301_closeup_door2 as door with dissolve
    show tina b_magic f_surprised behind doorframe with dissolve
    tina "{b}[firstname]{/b}?"

    show tina f_sad:
        xoffset -200
    show location_apt_hall3_301_closeup_door1 as door behind stage
    with dissolve
    tina "Apa yang kamu lakukan di sini?"


    menu:
        "I wanted to see you.":
            pass

    anon "I wanted to see you."

    tina f_sexy "Oh, kamu anak nakal..."

    tina "... We can't do that right now!"

    anon f_flirt "Tidak?"

    tina "Not while {b}Becca{/b}'s here."

    anon f_shy "Oh, right... I understand."

    tina "Come see me at work and we'll schedule something, okay?"

    anon f_flirt "Y-ya, oke."

    pause
    anon @ f_confused "Umm, where do you work again?"

    show tina f_laugh

    if M_anon.finished_state(S_ano13_tina):
        tina "Heh, did you forget?"

        tina f_normal "I'm the manager down at {b}Saga Financial{/b}."

        anon f_shy "Oh benar!"

        anon "Maaf."

    else:
        tina "Oh, I haven't told you yet, have I?"

        tina f_normal "I'm the manager down at {b}Saga Financial{/b}."

        anon f_shy "You work at the bank?"

        tina @ -m_talk "Mhmm."


    anon "Alright, I'll swing by sometime."

    tina f_sexy "I'm looking forward to it."

    pause
    becca "{b}Mom{/b}, who's at the door?!"

    tina f_surprised @ -m_talk "!!!"
    show tina f_sad:
        flip
        xoffset 450
    show location_apt_hall3_301_closeup_door2 as door behind stage
    with dissolve
    tina "Umm, no one sweetie..."

    tina "... Just some Jehovah's Witnesses."

    show tina f_sad:
        unflip
        xoffset -200
    show location_apt_hall3_301_closeup_door1 as door behind stage
    with dissolve
    tina f_sexy "You'd better go."

    anon "Ya baiklah."

    anon "Sampai berjumpa lagi."

    tina "So long, babyface."

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
