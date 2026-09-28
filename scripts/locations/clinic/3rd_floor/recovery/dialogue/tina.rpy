label hospital_recovery_tina_first:
    scene expression game.timer.image('location_hospital_baby_bed{}')
    show tina b_gown_bed f_normal_down
    with fade
    show anon with dissolve
    tina "{i}*Gasp*{/i} There's your daddy now!"
    tina "See, I told you he was coming..."
    tina f_normal "Hey, {b}[firstname]{/b}."
    anon "Hey."

    if M_tina.pregnancy.baby_gender == 'boy':
        tina "Are you ready to meet your son?"
        anon "M-my son?"
    elif M_tina.pregnancy.baby_gender == 'girl':
        tina "Are you ready to meet your daughter?"
        anon "M-my daughter?"
    else:
        tina "Are you ready to meet your children?"
        anon "M-my children?"

    show anon f_shy_low with dissolve:
        xoffset 200
    tina @ -m_talk "Mhmm."
    anon @ -m_talk "..."

    if M_tina.pregnancy.baby_gender == 'boy':
        anon "He's so beautiful!"
        tina "Heh, isn't he?"
        tina "He's perfect!"
    elif M_tina.pregnancy.baby_gender == 'girl':
        anon "She's so beautiful!"
        tina "Heh, isn't she?"
        tina "She's perfect!"
    else:
        anon "They're so beautiful!"
        tina "Heh, aren't they?"
        tina "They're perfect!"

    pause
    anon f_normal "I'll take it everything went fine with the delivery?"
    tina f_normal "Yes, of course."
    anon "You could have called me, I would have been there holding your hand."
    tina "Oh, that wasn't necessary..."
    tina "I had my OB/GYN and an army of nurses helping."
    anon f_worried @ -m_talk "..."
    tina f_normal_down "This went so much smoother than {b}Becca{/b}'s delivery..."
    anon "Well, that's good I guess."
    anon "How long are they going to keep you?"
    tina "A couple days at most."
    pause
    anon "Can I get you anything?"
    tina "Yes, actually!"
    anon f_normal "Really?!"
    tina "The nurse mentioned something about a lactation specialist earlier..."
    tina "... Could you send her in on your way out?"
    anon f_sad_down @ -m_talk "..."
    anon "Y-yeah, okay."
    tina "Thank you so much, {b}[firstname]{/b}."

    if M_tina.pregnancy.baby_gender == 'twins':
        anon "I guess, I'll see you all later."
    else:
        anon "I guess, I'll see you both later."

    tina @ -m_talk "Mhmm."
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
