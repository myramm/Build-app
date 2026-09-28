label consuela_button_recovery:
    show anon with dissolve
    consuela "Hola, papi."
    consuela "You come see baby?"

    menu consuela_button_recovery.choice:
        "Yup.":
            pass

    anon "Yeah, how are you guys doing?"
    consuela "Es good."
    consuela f_normal_down "Sleep much."
    anon "Yeah, I'm sure you're exhausted."
    consuela "Si, exhausted."
    consuela f_normal "And hungry!" (show_native="¡Y hambriento!")
    anon @ -m_talk "Hmm?"
    consuela "Ehh, food?"
    anon @ f_surprised "Oh, you're hungry?"
    consuela "Si, hungry."
    anon @ f_laugh "I'll let the nurses know, okay?"
    consuela "Gracias, papi."
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
