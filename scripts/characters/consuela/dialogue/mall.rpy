label consuela_button_mall:
    show anon f_worried with dissolve:
        flip
    anon @ -m_talk "..."
    anon "E-excuse me, {b}Consuela{/b}?"
    consuela @ -m_talk "Hmm?"
    consuela f_annoyed "Oh, it's you..." (show_native="Oh, eres tú...")
    consuela "Have you found me a job?" (show_native="¿Me has encontrado un trabajo?")
    anon @ f_sad_down a_behind_head "Ehh."

    menu consuela_button_mall.choice:
        "Can you understand me?":
            jump consuela_button_mall.comprende
        "Your sign is misspelled.":

            jump consuela_button_mall.sign
        "Never mind.":

            pass

    anon @ a_wave "I'm going to go find you a job, okay?"
    anon "I promise."
    consuela "Y-yes."
    consuela "Find job."
    consuela "I clean."
    show anon f_unimpressed
    anon @ -m_talk "..."
    consuela @ -m_talk "..."
    anon "Right."
    anon @ a_wave "I'll be back."
    hide anon with dissolve

    scene expression player.location.background_blur with fade
    show anon with dissolve
    anon a_thinking f_thinking @ -m_talk "( Hmm, I need to find {b}Consuela{/b} a job. )"
    anon @ -m_talk "( I should {b}start at the church{/b}, I'm sure the people there will be willing to help {b}Consuela{/b} in her time of need. )"
    hide anon with dissolve
    return


label consuela_button_mall.comprende:
    anon @ a_point_self "Can you understand me?"
    consuela f_sad @ -m_talk "..."
    consuela "What?" (show_native="¿Qué?")
    show anon f_hurt a_facepalm with dissolve
    pause
    anon a_idle f_worried @ f_angry "CAN. YOU. UNDERSTAND. ME?"
    consuela f_annoyed "I. DON'T. SPEAK. ENGLISH." (show_native="NO. HABLO. INGLES.")
    consuela "Idiot." (show_native="Idiota.")
    anon @ a_thinking f_thinking "Hmm, I guess not."
    jump consuela_button_mall.choice


label consuela_button_mall.sign:
    anon @ a_point "Your sign is misspelled."
    consuela f_sad @ -m_talk "..."
    anon "It's supposed to be C-L-E-A-N."
    anon "Not C-L-E-E-N."
    show consuela f_sad_down
    pause
    consuela f_sad "What?" (show_native="¿Qué?")
    anon @ -m_talk "..."
    consuela "I do not understand you..." (show_native="No te entiendo...")
    anon @ f_sad_down "Never mind."
    jump consuela_button_mall.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
