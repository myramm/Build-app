label maria_button_lounge:
    show anon f_flirt_low with dissolve
    pause
    anon "Hey, {b}Maria{/b}."

    show maria b_casual
    show anon f_normal
    with dissolve
    maria @ -m_talk "Hmm?"

    maria @ f_laugh "Oh, hey there, handsome."

    maria f_sexy "What are you doin' here?"


    menu maria_button_lounge.choice:
        "I love your house.":

            jump maria_button_lounge.house

        "Seks." if M_anon.finished_state(S_ano11_bone):
            jump maria_button_lounge.sex
        "Hanya menyapa.":

            pass

    anon f_normal "Hanya menyapa."

    if M_anon.finished_state(S_ano11_bone):
        maria f_normal "Alright, handsome."

    else:
        maria f_normal "Alright, kid."

    maria "Be careful out there."

    anon @ a_wave "Aku akan menjadi."

    hide anon with dissolve
    return


label maria_button_lounge.house:
    anon f_normal "I love your house."

    maria f_normal @ f_eyeroll "Aww, c'mon... It's a mess."

    anon @ f_shy "Apa?"

    anon "No it's not."

    pause
    anon "Everything looks so fancy..."

    maria "You're just bein' nice."

    anon "No, I'm serious."

    anon @ f_laugh "If you think this is a mess, you should see my room!"

    maria "Heh, you're such a sweet kid!"

    jump maria_button_lounge.choice


label maria_button_lounge.sex:
    anon f_flirt "Ingin berhubungan seks?"

    maria f_surprised "What, now?"

    anon "Ya kenapa tidak?"

    maria f_sexy @ f_sexy_lipbite -m_talk "MM."

    maria "I'd love to, but I have some things I need to get done."

    maria f_sexy "Ask me again this evening?"

    pause
    anon @ f_grin "Tentu saja."

    jump maria_button_lounge.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
