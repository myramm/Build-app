label iwanka_button_baby:
    show iwanka a_baby f_smirk_down
    show anon with dissolve
    iwanka "Accessories are very important."
    iwanka "No outfit is complete without them and they must match!"
    anon "What's going on?"
    iwanka f_normal "I'm getting ready to take the little one shopping."

    menu iwanka_button_baby.choice:
        "Again?!":

            jump iwanka_button_baby.invite
        "Aren't you going a little overboard?":

            jump iwanka_button_baby.excess
        "Have fun, I guess.":

            pass

    anon f_shy "Have fun, I guess."
    iwanka f_smirk_down "Of course we'll have fun, won't we?"
    iwanka "Nothing beats shopping!"
    iwanka "It's the most fun thing you can do!"
    hide anon with dissolve
    return


label iwanka_button_baby.excess:
    anon f_worried "Aren't you going a little overboard?"
    iwanka f_normal "What do you mean?"
    anon "It's a baby, {b}Iwanka{/b}..."
    anon "You really don't need to buy it all these expensive things."
    iwanka f_annoyed "Are you joking?"
    iwanka "My baby only gets the very best, end of story."
    anon "Y-yeah, but this isn't-"
    iwanka "End of story, {b}[firstname]{/b}!"
    iwanka "I've got all this money {b}my father{/b} left me and I'll spend it however I like."
    anon f_sad_down "{i}*Sigh*{/i} Fair enough."
    jump iwanka_button_baby.choice


label iwanka_button_baby.invite:
    anon f_surprised "Again?!"
    anon "Didn't you go yesterday?"
    show anon f_worried
    iwanka f_normal @ f_annoyed "So?"
    if M_iwanka.pregnancy.baby_gender == "boy":
        iwanka "He's going to start growing soon and I want to get a head start on building up his wardrobe."
        anon "Y-yeah, but you've already bought him so many things..."
    else:
        iwanka "She's going to start growing soon and I want to get a head start on building up her wardrobe."
        anon "Y-yeah, but you've already bought her so many things..."
    iwanka @ f_eyeroll "You can never have too many clothes, {b}[firstname]{/b}!"
    iwanka f_excited "In fact, why don't you come with us and we'll get you some stuff too?"
    anon "No, that's okay."
    anon "I'm fine with my wardrobe."
    iwanka f_annoyed "What wardrobe?!"
    iwanka "You literally wear the same outfit every day."
    anon f_unimpressed "Hey, it's a good look for me!"
    iwanka f_smirk @ f_laugh "{i}*Snort*{/i} Sure it is..."
    jump iwanka_button_baby.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
