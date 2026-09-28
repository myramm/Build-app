label consuela_button_pregnant:
    show anon with dissolve
    consuela "Hola, papi."
    anon "Hey, {b}Consuela{/b}."

    menu consuela_button_pregnant.choice:
        "How are you feeling?":
            if M_consuela.pregnancy.stage < 2:
                jump consuela_button_pregnant.nausea
            if M_consuela.pregnancy.stage < 3:
                jump consuela_button_pregnant.kick
            jump consuela_button_pregnant.poop
        "{b}Martinez{/b}.":

            jump consuela_button_pregnant.camila
        "I'll leave you to it then.":

            pass

    anon f_normal "I'll leave you to it then."
    consuela "Si."
    consuela "I clean."
    anon @ a_point "Yup, you clean."
    hide anon with dissolve
    return


label consuela_button_pregnant.nausea:
    anon f_normal "How are you feeling?"
    consuela @ -m_talk "Hmm?"
    consuela "Oh, I okay."
    consuela "Just a little morning sickness, not too bad." (show_native="Solo un poco de náuseas matutinas, no tan mal.")
    anon "Alright."
    anon "Can I do anything for you?"
    consuela "Do for me?"
    consuela @ f_laugh "No, papi... I do for you!"
    anon "Heh, I know that but you're pregnant now and-"
    pause
    anon "Ehh, never mind."
    anon "Just let me know if you need anything, okay?"
    consuela "Si."
    consuela "Gracias, papi."
    jump consuela_button_pregnant.choice


label consuela_button_pregnant.kick:
    anon "How are you feeling?"
    consuela @ -m_talk "Hmm?"
    consuela "Oh, I okay."
    consuela f_normal_down "Our little one is starting to kick." (show_native="Nuestro pequeño está empezando a patear.")
    anon @ f_laugh "I'm not sure what that means."
    consuela "Eh, he make kick."
    consuela f_normal "Inside."
    anon f_surprised "{i}He{/i}?"
    anon "You mean, it's a boy?"
    consuela "Si, es boy."
    anon f_normal "Heh, how do you know that?"
    consuela @ a_boobs "Because my right breast is bigger than my left." (show_native="Porque mi seno derecho es más grande que el izquierdo.")
    anon f_worried @ f_shock "!!!"
    anon "Umm, okay."
    anon f_confused "Something to do with your boobs?"
    consuela "Si, boobs."
    show anon f_normal
    consuela "One es big."
    consuela "One es, umm..."
    anon "Small?"
    consuela "Yes, small." (show_native="Si, pequeña.")
    anon "Right."
    anon @ f_shy a_behind_head "I guess I'll just have to take your word for it."
    jump consuela_button_pregnant.choice


label consuela_button_pregnant.poop:
    anon "How are you feeling?"
    consuela f_sad "Ugh, not so good..." (show_native="Ugh, no tan bien...")
    consuela "I'm so incredibly constipated!" (show_native="¡Estoy tan increíblemente estreñido!")
    anon f_worried "I don't know what you're saying but it doesn't sound good..."
    consuela f_surprised "I haven't pooped in five days!" (show_native="¡No he defecado en cinco días!")
    anon "Maybe you should come lie down..."
    consuela f_sad @ -m_talk "Ehh?"
    anon "You should be in bed."
    consuela "No bed."
    consuela "I clean."
    anon "{b}Consuela{/b}..."
    consuela "I'm going to scrub the floors." (show_native="Voy a fregar el piso.")
    consuela "Maybe that will jar something loose..." (show_native="Tal vez eso sacudirá algo suelto...")
    anon @ -m_talk "..."
    jump consuela_button_pregnant.choice


label consuela_button_pregnant.camila:
    anon f_worried "Have you told your daughter about the baby yet?"
    consuela "{b}Camila{/b}?"
    consuela "What about her?" (show_native="¿Que hay de ella?")
    anon @ -m_talk "..."
    anon "The baby."
    consuela @ f_surprised "Oh!"
    consuela @ f_laugh "Si, {b}Camila{/b} es good."
    consuela f_smirk "You go date now?"
    anon "No, that's not what I-"
    show anon f_unimpressed
    pause
    anon "Ehh, never mind."
    jump consuela_button_pregnant.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
