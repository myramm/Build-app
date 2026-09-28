label tina_button_recovery:
    show anon with dissolve
    if M_tina.pregnancy.baby_gender == 'twins':
        anon "Hey, you three."
    else:
        anon "Hey, you two."
    tina @ f_normal "Hey there, {b}[firstname]{/b}."
    tina "You come by to check on us again?"

    menu tina_button_recovery.choice:
        "Yup.":
            pass

    anon "Yeah, how are you guys doing?"
    tina @ f_laugh "We're doing great!"
    if M_tina.pregnancy.baby_gender == 'boy':
        tina "You should see how much our little guy eats!"
    elif M_tina.pregnancy.baby_gender == 'girl':
        tina "You should see how much our little girl eats!"
    else:
        tina "You should see how much our little ones eat!"
    tina f_normal "That lactation specialist is really gonna pay off!"
    anon "Well, that's good."
    pause
    anon "Is there anything I can do?"
    tina f_normal_down @ f_laugh "Hmm, not that I can think of..."
    anon f_sad_down @ -m_talk "..."
    tina "We'll be heading home soon and then you can come and visit, okay?"
    anon "Yeah, okay."
    tina "Thanks, {b}[firstname]{/b}."
    if M_tina.pregnancy.baby_gender == 'twins':
        anon "I guess, I'll see you all later."
    else:
        anon "I guess, I'll see you both later."
    tina @ -m_talk "Mhmm."
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
