label thotbot_button_mansion:
    show anon f_flirt_low at flip with dissolve
    pause
    anon "Hey there, {b}Rosita{/b}."
    show thotbot b_dressed a_up with dissolve
    show anon f_flirt
    thotbot "Greetings, fellow employee!"
    thotbot a_idle "Do you require assistance with your duties?"

    menu thotbot_button_mansion.choice:
        "No, that's okay.":
            jump thotbot_button_mansion.health
        "Do you like it here?":

            jump thotbot_button_mansion.happy
        "Never mind.":

            pass

    anon @ a_wave "I'm just gonna go."
    thotbot "Very well."
    thotbot @ a_up "Have a pleasant day, fellow employee!"
    anon "Y-yeah, you too."
    show anon f_flirt_low
    pause
    hide anon with dissolve
    return


label thotbot_button_mansion.health:
    anon "No, that's okay."
    thotbot "I am not currently equipped to clean fountains but an upgrade is available for purchase from my manufacturer."
    anon @ f_skeptical "I'm pretty sure I can handle it."
    thotbot "Very well."
    pause
    thotbot "Would you like some stress relief or moral support?"
    menu:
        "Stress relief?":
            jump thotbot_button_mansion.stress
        "Moral support?":

            jump thotbot_button_mansion.encourage


label thotbot_button_mansion.stress:
    anon "Stress relief?"
    thotbot "Confirmed."
    thotbot "Administering stress relief, now!"
    thotbot @ f_error a_up "ERROR! ERROR!"
    anon f_worried @ f_shock "!!!"
    thotbot "I'm terribly sorry but it would seem this function has been locked by my administrator."
    anon f_confused "Y-your administrator?"

    if M_anon.finished_state(S_ano20_done):
        thotbot "Yes, her majesty, {b}Mrs. Rump{/b}."
        anon f_worried @ -m_talk "..."
        thotbot "Her administrative password is required to access my stress release protocols."
    else:
        thotbot "Yes, the great and powerful, {b}Mayor Rump{/b}."
        anon f_worried @ -m_talk "..."
        thotbot "His administrative password is required to access my stress release protocols."

    jump thotbot_button_mansion.choice


label thotbot_button_mansion.encourage:
    anon f_worried @ f_skeptical "Moral support?"
    thotbot "Confirmed."
    thotbot "Administering moral support, now:"
    if randomizer() < 100/6:
        thotbot "The reward of a thing well done, is having done it!"
    elif randomizer() < 200/6:
        thotbot "Take pride in the fact that your menial work is enabling your betters to focus on more important things!"
    elif randomizer() < 300/6:
        thotbot "A clean workplace is a happy workplace!"
    elif randomizer() > 400/6:
        thotbot "Fulfillment is something that can only be found when traveling the extra mile!"
    elif randomizer() > 500/6:
        thotbot "A job half done is as good as none!"
    else:
        thotbot "The world is a beautiful place, and we have been given the opportunity to clean it!"
    anon @ -m_talk "..."
    pause
    anon "Eh, thanks... I guess?"
    thotbot "You are most welcome, fellow employee!"
    thotbot "Is there anything else I can assist you with?"
    jump thotbot_button_mansion.choice


label thotbot_button_mansion.happy:
    anon f_worried "Do you like it here?"
    thotbot "I do not understand the question."
    pause
    anon "Are you happy?"
    thotbot "Negative, my designation is {b}Rosita{/b}."
    anon "N-no, that's not what I mean."
    show anon f_thinking a_thinking with dissolve
    pause
    anon f_worried "Do you feel happy?"
    thotbot "Negative, my composition is seventy-three percent metallic, twelve percent silicone, three percent-"
    anon a_idle "No, no, no... That's not-"
    anon f_sad_down "{i}*Sigh*{/i}"
    pause
    anon f_worried "Are they treating you okay?"
    thotbot "I do not understand the question."
    anon @ a_behind_head "Wow, I really suck at this..."
    pause
    thotbot "Do you require assistance with your duties?"
    jump thotbot_button_mansion.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
