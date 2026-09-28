label melonia_button_baby(low=False):
    if low:
        show anon f_worried_low with dissolve
    else:
        show anon f_worried with dissolve
    anon "{b}Melonia{/b}?"
    melonia "Hey, {b}[firstname]{/b}."
    anon "Why is the robot holding our child?"
    melonia "You mean the maid?"
    anon "Yeah, the {i}robot{/i} maid."
    melonia "It's fine, {b}[firstname]{/b}."

    menu melonia_button_baby.choice:
        "It's not fine!":

            jump melonia_button_baby.thotbot
        "Warm up to our child?":

            jump melonia_button_baby.effort
        "Enjoy your {i}me{/i} time, I guess.":

            pass

    if low:
        show anon f_worried_low
    else:
        show anon f_worried
    anon "Enjoy your {i}me{/i} time, I guess."
    if low:
        show melonia f_smirk_up
    else:
        show melonia f_smirk
    melonia "Oh, don't be so morose."
    melonia "I'll be back to one hundred percent before you know it."
    anon "What does that mean?"
    melonia "It means, you'd better clear your schedule."
    if low:
        show melonia f_relax
    else:
        show melonia f_smirk
    melonia "Because you owe me a monumental orgasm after all this baby stuff and I'm damn sure going to collect!"
    anon f_sad_down "{i}*Sigh*{/i} Yeah, okay."
    hide anon with dissolve
    return


label melonia_button_baby.effort:
    if low:
        show anon f_worried_low
    else:
        show anon f_worried
    anon "You have to at least make an effort to bond with our child."
    if low:
        show melonia f_relax
    else:
        show melonia f_normal
    anon "Okay, but when?"
    melonia "When it's older..."
    melonia "... And less prone to soiling itself."
    anon "{b}Melonia{/b}..."
    melonia "Maybe we'll get lucky and this one will leave the nest at a normal age instead of mooching off me its entire life..."
    melonia "... Like a certain other child whose name I won't mention."
    jump melonia_button_baby.choice


label melonia_button_baby.thotbot:
    if low:
        show anon f_worried_low
    else:
        show anon f_worried
    anon "It's not fine!"
    anon "I don't like you leaving our baby with that thing."
    if low:
        show melonia f_relax
    else:
        show melonia f_normal
    melonia "Why not?"
    melonia "I put it in childcare mode."
    anon "Because it's-"
    if low:
        show anon f_surprised_low
    else:
        show anon f_surprised
    pause
    anon @ a_point_back "Wait, it has a childcare mode?"
    melonia "Of course."
    show anon f_thinking
    pause
    if low:
        show anon f_worried_low
    else:
        show anon f_worried
    anon "No, no... I still don't like it."
    if low:
        show melonia f_annoyed_up
    else:
        show melonia f_annoyed
    melonia "Well, then watch it yourself!"
    melonia "I spent nine months carrying that thing around and now I want some {i}me{/i} time!"
    jump melonia_button_baby.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
