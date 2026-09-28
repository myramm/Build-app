label consuela_button_baby:
    show consuela a_baby f_normal_down
    show anon with dissolve
    consuela "Hola, papi."
    if M_consuela.pregnancy.baby_gender == 'twins':
        anon "Hey, you three."
    else:
        anon "Hey, you two."
    anon "Are you helping Mommy clean?"
    consuela f_normal @ f_laugh "Hehe, si."
    consuela "Good help."

    menu consuela_button_baby.choice:
        "Can I convince you to stop cleaning?":
            jump consuela_button_baby.stop
        "You guys need anything?":

            jump consuela_button_baby.need
        "I'll leave you to it then.":

            pass

    anon "I'll leave you be."
    consuela "Si, papi."
    consuela "I clean now."
    hide anon with dissolve
    return


label consuela_button_baby.stop:
    anon "Can I convince you to stop cleaning?"
    if M_consuela.pregnancy.baby_gender == 'twins':
        anon "At least while the babies are here?"
    else:
        anon "At least while the baby is here?"
    consuela f_sad "¿Qué?"
    consuela "No clean?"
    anon "Yeah, no clean."
    if M_consuela.pregnancy.baby_gender == 'twins':
        anon "Play with babies."
    else:
        anon "Play with baby."
    consuela "No, my children must learn that work comes first." (show_native="No, mis hijos deben aprender que el trabajo es lo primero.")
    consuela f_normal_down "I want them to be responsible people." (show_native="Quiero que sean personas responsables.")
    anon f_worried @ -m_talk "..."
    consuela f_normal "Es okay."
    consuela @ f_laugh "I clean."
    anon "{i}*Sigh*{/i} Alright, if you insist."
    jump consuela_button_baby.choice


label consuela_button_baby.need:
    anon f_normal "You guys need anything?"
    consuela "No, es good."
    consuela f_normal_down "I teach."
    consuela "Work hard."
    if M_consuela.pregnancy.baby_gender == 'twins':
        anon "You're teaching our babies to work hard?"
        consuela "You will be great workers someday, right?" (show_native="Serán grandes trabajadores algún día, ¿verdad?")
    else:
        anon "You're teaching our baby to work hard?"
        consuela "You will be a great worker someday, right?" (show_native="Serás un gran trabajador algún día, ¿no?")
    anon @ -m_talk "..."
    anon "Alright, just don't push yourself too hard..."
    consuela f_normal "Okay, papi."
    jump consuela_button_baby.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
