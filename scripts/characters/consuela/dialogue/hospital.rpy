label consuela_button_hospital:
    if not M_consuela.finished_state(S_con03_door):
        jump consuela_button_hospital.debt

    show anon with dissolve
    if M_consuela.finished_state(S_con03_done):
        consuela "Buenas noches, papi."
    else:
        consuela "Buenas noches, {b}Mister [firstname]{/b}."
    anon @ a_wave "Hello, {b}Consuela{/b}."

    menu consuela_button_hospital.choice:
        "Working hard?":
            jump consuela_button_hospital.working

        "Working alone?" if M_consuela.pregnancy.stage > 4:
            jump consuela_button_hospital.alone
        "I should go.":

            pass

    anon "I'll see you at my place later, yeah?"
    consuela "Si, your place."
    consuela "I do for you."
    consuela "You say, I do."
    anon @ a_wave "Bye, {b}Consuela{/b}."
    consuela "Adiós, {b}Mister [firstname]{/b}."
    hide anon with dissolve
    return

label consuela_button_hospital.working:
    anon "Working hard?"
    consuela "Oh, si {b}Mister [firstname]{/b}."
    consuela "I work hard."
    consuela "Clean good."
    anon "Well, I'm sure everyone here appreciates it."
    anon "And it's gotta be better than working for {b}Mayor Rump{/b}, right?"
    consuela "Oh, si!"
    consuela f_annoyed "{b}Mayor Rump{/b}, bad man."
    consuela "I no do for him!"
    consuela "He ask but I no do."
    show consuela f_normal
    jump consuela_button_hospital.choice

label consuela_button_hospital.alone:
    if M_consuela.pregnancy.baby_gender == 'twins':
        anon "No little ones today?"
    else:
        anon "No little one today?"
    consuela f_sad @ -m_talk "Hmm?"
    if M_consuela.pregnancy.baby_gender == 'twins':
        anon "Where are the babies?"
    else:
        anon "Where's the baby?"
    consuela f_normal "Oh, {b}Camila{/b} watch."
    anon f_worried "Your daughter is babysitting?"
    consuela "Si, babysitting."
    consuela "The old lady at reception told me I can't bring children to work." (show_native="La anciana de recepción me dijo que no puedo traer niños al trabajo.")
    anon f_skeptical "Is she a good babysitter?"
    consuela "Oh, si."
    consuela "{b}Camila{/b} good big sister."
    show anon f_normal
    consuela @ f_laugh "Much love."
    anon "I'd definitely like to see that!"
    jump consuela_button_hospital.choice

label consuela_button_hospital.debt:
    show anon with dissolve
    anon "Hey there {b}Consuela{/b}."
    anon "How are you doing?"
    consuela "Oh, I good, {b}Mister [firstname]{/b}."
    consuela "You find job."
    consuela "Good man."
    consuela "I do for you now?"
    anon @ -m_talk "Hmm?"
    consuela "I do for you?"
    anon "No, no, you don't have to do anything for me..."
    consuela "Yes, I do for you!"
    consuela "You say, I do."
    anon "Heh, don't worry about it."
    anon "I'm good."
    consuela @ f_eyeroll "Tsk."
    consuela "There must be something I can do for you?" (show_native="Debe haber algo que pueda hacer por ti?")

    menu:
        "I should go.":
            pass

    anon "I'll let you get back to it."
    consuela "Wait, {b}Mister [firstname]{/b}..."
    consuela "I do for you, okay?"
    consuela "You good man."
    anon "Heh, alright... Alright."
    anon "If I think of something, I'll let you know, okay?"
    consuela "Si."
    consuela "You say, I do."
    anon @ a_wave "Bye, {b}Consuela{/b}."
    consuela "Adiós, {b}Mister [firstname]{/b}."
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
