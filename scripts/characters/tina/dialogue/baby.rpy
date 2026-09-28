label tina_button_baby:
    show anon with dissolve
    tina "That's right, you were a miracle!"
    tina "Yes, you were..."
    tina "Mommy had an implant to keep her from getting pregnant but you wanted to be born so bad that it didn't matter!"
    tina "That's why Mommy spared no expense, making sure you could have the best life possible."

    menu tina_button_baby.choice:
        "How's everything going?":

            jump tina_button_baby.status
        "I'll leave you be.":

            pass

    anon f_normal "I'll leave you be."
    if M_tina.pregnancy.baby_gender == 'boy':
        tina f_normal "Yeah, I should really get him down for a nap anyways..."
    elif M_tina.pregnancy.baby_gender == 'girl':
        tina f_normal "Yeah, I should really get her down for a nap anyways..."
    else:
        tina f_normal "Yeah, I should really get them down for a nap anyways..."
    anon "I'll see you soon, okay?"
    tina f_normal_down @ -m_talk "Mhmm."
    hide anon with dissolve
    return


label tina_button_baby.status:
    anon f_normal "How's everything going?"
    tina f_normal_down @ f_normal "Great!"
    if M_tina.pregnancy.baby_gender == 'boy':
        tina "Isn't he wonderful, {b}[firstname]{/b}?"
    elif M_tina.pregnancy.baby_gender == 'girl':
        tina "Isn't she wonderful, {b}[firstname]{/b}?"
    else:
        tina "Aren't they wonderful, {b}[firstname]{/b}?"
    pause
    tina f_normal "How did we get so lucky?"
    if M_tina.pregnancy.baby_gender == 'boy':
        anon "He came from good stock, on his mother's side."
    elif M_tina.pregnancy.baby_gender == 'girl':
        anon "She came from good stock, on her mother's side."
    else:
        anon "They come from good stock, on their mother's side."
    tina @ f_laugh "Heh, you flatterer..."
    if M_tina.pregnancy.baby_gender == 'boy':
        tina "... His father's side isn't too shabby either, you know?"
    elif M_tina.pregnancy.baby_gender == 'girl':
        tina "... Her father's side isn't too shabby either, you know?"
    else:
        tina "... Their father's side isn't too shabby either, you know?"
    pause
    tina "You've made me a very happy woman, {b}[firstname]{/b}."
    tina "I hope you know that?"
    anon "Thanks, {b}Tina{/b}."
    jump tina_button_baby.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
