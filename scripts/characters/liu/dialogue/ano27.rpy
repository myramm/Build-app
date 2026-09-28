label ano27_lock_liu:
    show anon with dissolve
    liu "Welcome to {b}Saga Financial{/b}."
    liu "How can I help-"
    liu a_mouth_cover f_surprised "{b}[firstname]{/b}?!"
    anon a_wave "Hey, {b}Liu{/b}."
    show anon a_sides with {'master': dissolve}
    liu a_nervous f_shocked "Y-you shouldn't be here..."
    liu "... The police are still lurking around, investigating the bank robbery."
    anon f_surprised "Oh, right."
    anon f_worried "I uhh..."

    menu ano27_lock_liu.choice:
        "Just wanted to check on you.":
            jump ano27_lock_liu.check
        "I'll talk with you later.":

            pass

    liu f_frightened "Quickly, before they come back!"
    anon "Alright."
    anon "I'll see you after this all blows over, I promise."
    hide anon with dissolve
    return


label ano27_lock_liu.check:
    liu f_frightened "Yes, yes, I'm fine..."
    liu "... But you must go, hurry!"
    liu "I can't have you getting arrested on my account!"
    jump ano27_lock_liu.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
