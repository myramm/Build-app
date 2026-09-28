label nadya_button_recovery:
    show anon f_worried with dissolve
    nadya f_sleep @ -m_talk "..."
    anon f_confused "Is she sleeping?"
    show svetlana:
        xoffset -100
        xzoom 1
    with {'master': dissolve}
    svetlana "Da."
    anon f_normal "Good, she could use the break."
    anon "I know you Russian girls are tough but it's okay to be vulnerable once in a while too."
    pause
    svetlana f_happy "You make nice match for {b}Miss Chernyshevksy{/b} I think..."
    anon f_surprised "Oh?"
    svetlana "... Is good that she chose you."
    show anon f_shy
    show svetlana f_happy_down
    pause
    svetlana "And you make beautiful baby together."
    anon f_shy_low "Heh, yeah... we really did."
    pause
    show anon f_shy

    if M_nadya.pregnancy.baby_gender == 'boy':
        anon "You're okay watching him?"
    else:
        anon "You're okay watching her?"

    svetlana f_happy "Da, I watch."
    anon "Thanks, {b}Svet{/b}."
    svetlana "Is no problem."
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
