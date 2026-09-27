label hospital_recovery_josie_first:
    scene expression game.timer.image('location_hospital_baby_bed{}')
    show josephine b_gown_bed f_sexy_down
    with fade
    show anon with dissolve
    anon "Hei kamu."

    josephine "Hai."

    anon "Bagaimana perasaanmu?"

    josephine f_bored "Tired."

    anon "Yeah, I bet."

    pause
    josephine f_sexy_down @ f_sexy "Come look at our child."

    if M_josie.pregnancy.baby_gender == 'boy':
        josephine "He's so cool!"

        anon "Dia?"

    else:
        josephine "She's so cool!"

        anon "Dia?"

    josephine @ -m_talk "Mhmm."

    show josephine f_sexy
    if M_josie.pregnancy.baby_gender == 'boy':
        josephine "Little Gaylord."

        anon f_angry "You are so not naming him that!"

    else:
        josephine "Little Phelony."

        anon f_angry "You are so not naming her that!"

    josephine @ f_laugh "Haha!"

    anon "Seriously, over my dead body!"

    josephine "I'm just joking..."

    show josephine f_sexy_down
    show anon f_shy_low with dissolve:
        xoffset 200
    if M_josie.pregnancy.baby_gender == 'boy':
        anon "Hi there, little guy."

    else:
        anon "Hi there, little girl."

    anon "I'm your daddy."

    pause
    show anon f_normal
    if M_josie.pregnancy.baby_gender == 'boy':
        anon "Wow, he's beautiful!"

        anon "You want me to take him?"

    else:
        anon "Wow, she's beautiful!"

        anon "You want me to take her?"

    josephine "Tidak, tidak apa-apa."

    show anon f_shy_low
    if M_josie.pregnancy.baby_gender == 'boy':
        josephine "It feels good having him in my arms."

    else:
        josephine "It feels good having her in my arms."

    pause
    anon f_normal "Do you need anything?"

    anon "Food?"

    anon "Water?"

    anon "Your phone, maybe?"

    josephine "No, I'm good."

    anon f_surprised "Wah benarkah?"

    pause
    anon "You don't want your phone?"

    josephine "Heh, I don't need it."

    anon @ -m_talk "..."
    anon f_normal @ f_laugh "Somewhere pigs are flying..."

    josephine @ f_laugh "Hehe, diamlah!"

    anon @ f_laugh "hehe."

    pause
    anon "So, how long will you be in here?"

    josephine "A few days."

    anon "Ya, itu bagus."

    pause
    anon "I should probably let you rest, huh?"

    josephine "Mm, yeah..."

    josephine "That sounds like a good idea."

    anon "Sampai jumpa lagi, oke?"

    josephine @ -m_talk "Mhmm."

    anon f_shy_low "Sampai jumpa, si kecil."

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
