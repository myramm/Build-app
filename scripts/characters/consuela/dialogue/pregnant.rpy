label consuela_button_event_pregnancy:
    $ M_consuela.pregnancy.set('announced_pregnancy')
    if not M_consuela.pregnancy.number_of_babies:
        jump consuela_button_event_pregnancy.initial
    jump consuela_button_event_pregnancy.repeat


label consuela_button_event_pregnancy.initial:
    show consuela b_magic a_hips
    show anon f_worried with dissolve
    consuela "Papi!"
    anon "There you are."
    anon "What's going on?"
    consuela @ a_idle "We're going to have a baby!" (show_native="¡Vamos a tener un bebé!")
    anon f_confused @ -m_talk "Hmm?"
    consuela f_sad "Eh."
    consuela "I"
    consuela "Preglant."
    anon "Preglant?"
    consuela f_normal @ f_laugh "Si, preglant!"
    anon "That's not a word."
    consuela "Preglant, preglant."
    anon f_surprised "Wait a second..."
    anon @ f_surprised_teeth -m_talk "!!!" with hpunch
    anon "Are you trying to say you're preg-NANT?"
    consuela "Si."
    consuela "You."
    consuela "Put baby."
    consuela f_normal_down @ a_idle "Inside."
    anon f_sad_down a_behind_head "Holy crap..."
    show consuela f_sad
    pause
    consuela "You no like, papi?"
    anon f_worried "No, I like."
    anon "I, umm-"
    consuela f_angry "Baby es blessing!"
    anon "Y-yeah, I know."
    anon f_normal a_idle "It's just a little unexpected, that's all."
    show consuela f_normal
    pause
    anon "Wow, I'm going to be a father?"
    consuela "Si, papi."
    consuela "I'm so excited to have your baby!" (show_native="¡Estoy tan emocionada de tener a tu bebé!")
    consuela "I will pray for a boy this time." (show_native="Rezaré por un chico esta vez.")
    anon "Can I get you anything?"
    consuela @ -m_talk "..."
    anon "You know, like a warm beverage or a foot massage or something?"
    consuela @ f_sad "Feet?"
    anon "Yeah."
    consuela "No es okay."
    consuela "I clean."
    anon f_worried @ f_unimpressed "{b}Consuela{/b}..."
    anon "You really shouldn't be doing manual labor while you're pregnant."
    consuela "Es fine, papi."
    consuela "I clean."
    consuela "More monies for baby."
    anon "You're sure?"
    consuela "Si."
    consuela "Don't worry, hard work will strengthen the baby." (show_native="No se preocupe, el trabajo duro fortalecerá al bebé.")
    anon @ -m_talk "Hmm?"
    show consuela b_kiss
    hide anon
    with dissolve
    pause
    consuela "Muah!"
    show consuela b_magic
    show anon
    with dissolve
    consuela "Our baby will be beautiful, daddy." (show_native="¡Nuestro bebé será hermoso, papi.")
    consuela "You'll see." (show_native="Verás.")
    anon @ -m_talk "..."
    consuela "I clean now."
    anon "O-okay."
    hide consuela with dissolve
    anon @ -m_talk "( I'm sure she knows what she's doing... )"
    anon @ -m_talk "( She has done this before after all. )"
    pause
    anon f_worried @ -m_talk "( Man, how are {b}Martinez{/b} and {b}Lopez{/b} going to react to this? )"
    anon f_surprised_teeth @ -m_talk "( I'm afraid to even think about it. )"
    hide anon with dissolve
    return


label consuela_button_event_pregnancy.repeat:
    show consuela b_magic a_hips
    show anon f_worried with dissolve
    consuela "Papi!"
    anon "There you are."
    anon "What's going on?"
    consuela @ a_idle "I'm with child again." (show_native="Estoy con un niño otra vez.")
    anon f_normal @ f_surprised "You're pregnant again?"
    consuela "Si, pregnant."
    anon "That's wonderful!"
    consuela "Si, wonderful."
    show consuela b_kiss
    hide anon
    with dissolve
    pause
    show consuela b_magic
    show anon
    with dissolve
    consuela "It's greedy for me to have more of your children..." (show_native="Es codicioso para mí tener más de tus hijos...")
    consuela "{b}Camila{/b} and you should be giving me grandbabies!" (show_native="¡{b}Camila{/b} y tú deberías darme nietos!")
    anon "Yeah, I have no idea what you're saying."
    consuela "Es okay."
    consuela "I do for you, {b}[firstname]{/b}."
    anon "Thanks, {b}Consuela{/b}."
    anon "I do for you too."
    consuela @ f_laugh "Hehe!"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
