label ano25_find_tony:
    return

label ano25_find_tony.pizzeria:
    show tony f_smirk
    show anon with dissolve:
        flip
    tony "You get the bag yet?"
    anon f_worried "N-no, not yet."
    show tony f_normal
    pause
    anon "Where is it again?"
    tony "{b}Look for a gray duffel bag in our bedroom closet{/b}."
    tony m_talk "It should be pretty easy to spot."

    if 'a_baby' not in renpy.get_attributes('tony'):
        show tony a_point with {'master': dissolve}

    tony "And don't let {b}Maria{/b} get a peek at what's inside, eh?"

    if 'a_baby' not in renpy.get_attributes('tony'):
        show tony a_idle with {'master': dissolve}

    tony -m_talk "Just tell her somethin' broke at your house and I sent ya to borrow some tools."
    tony "Capiche?"
    anon "{b}Gray duffel bag, bedroom closet.{/b}"
    anon "I got it."
    pause
    anon "I'll be back."
    hide anon with dissolve
    return


label ano25_find_tony.bank:
    show anon with dissolve:
        flip
    tony "Ya bring the bag?"
    anon f_worried "N-no, not yet."
    pause
    tony f_angry @ a_frustrated "Jesus, champ..."
    tony "... how are we supposed to rob a bank with no guns, eh?!"
    anon "Sorry, {b}Tony{/b}."
    anon "Where is it again?"
    tony "{b}Look for a gray duffel bag in our bedroom closet{/b}."
    tony "It should be pretty easy to spot."
    tony @ -m_talk "And don't let {b}Maria{/b} get a peek at what's inside, eh?"
    tony "Just tell her somethin' broke at your house and I sent ya to borrow some tools."
    tony "Capiche?"
    anon "{b}Gray duffel bag, bedroom closet.{/b}"
    anon f_normal "I got it."
    pause
    anon f_worried a_behind_head "I'll be back."
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
