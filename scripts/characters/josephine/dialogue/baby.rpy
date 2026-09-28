label josie_button_baby:
    show anon with dissolve
    anon "Hey there, you two."
    josephine @ -m_talk "..."
    if M_josie.pregnancy.baby_gender == 'boy':
        anon "How's my little guy doing?"
    else:
        anon "How's my little girl doing?"
    pause
    anon f_worried "Hello?"
    josephine @ -m_talk "..."
    anon f_sad_down "Seriously?!"
    josephine f_normal @ -m_talk "Hmm?"
    josephine "Oh, hey {b}[firstname]{/b}!"
    josephine "What's going on?"

    menu josie_button_baby.choice:
        "The baby really takes after you, huh?":

            jump josie_button_baby.phone
        "You guys need anything?":

            jump josie_button_baby.need
        "I'll leave you be.":

            pass

    anon f_normal @ a_wave "I'll leave you be."
    show josephine f_normal_down
    if M_josie.pregnancy.baby_gender == 'boy':
        anon "Don't let him stare at that thing too long."
        anon "It'll rot his brain."
    else:
        anon "Don't let her stare at that thing too long."
        anon "It'll rot her brain."
    josephine @ -m_talk "Mhmm."
    hide anon with dissolve
    return


label josie_button_baby.need:
    anon f_normal "You guys need anything?"
    josephine f_normal "You any good at Candy Smash?"
    anon f_worried @ f_confused "I don't even know what that is..."
    josephine f_normal_down "Yeah, I figured."
    pause
    josephine "We're good, thanks."
    jump josie_button_baby.choice


label josie_button_baby.phone:
    anon f_normal "The baby really takes after you, huh?"
    josephine f_normal_down @ f_eyeroll "Duh."
    pause
    josephine "You should be grateful."
    josephine "I dunno if you know this, but I'm pretty much the coolest person you know."
    anon @ f_laugh "Heh, yeah... Okay."
    josephine @ f_laugh "Hehe!"
    jump josie_button_baby.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
