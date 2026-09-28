label thotbot_button_baby:
    show anon behind thotbot with dissolve
    anon "Hey there, {b}Rosita{/b}."
    show thotbot with dissolve:
        flip
        xoffset 0
    thotbot "Greetings, fellow employee!"
    thotbot "Regretfully, I am in childcare mode and cannot render you assistance at this time."
    anon @ f_confused "Huh?"
    anon "O-oh, that's alright."
    anon "I'm was just checking in to see how things were going with the little one."
    thotbot "{b}Mrs. Melonia{/b}'s child is well."
    thotbot "Its nutrient storage systems are near capacity and its emotional needs are currently satisfied."
    anon f_shy "Wow, umm... Okay."
    thotbot "Did you have a question regarding its care?"

    menu thotbot_button_baby.choice:
        "Are you sure you can handle this?":

            jump thotbot_button_baby.concern
        "Need some help?":

            jump thotbot_button_baby.lullaby
        "I'll leave you to it.":

            pass

    anon f_normal "I'll leave you to it."
    thotbot "Best of luck with your duties, fellow employee!"
    anon f_worried "Yeah, umm..."
    pause
    anon f_shy @ a_wave "... Thanks."
    hide anon with dissolve
    return


label thotbot_button_baby.concern:
    anon f_worried "Are you sure you can handle this?"
    anon "Babies can be a handful..."
    thotbot "There is no need for concern, fellow employee."
    thotbot "This unit was recently awarded an A+ rating in child rearing and nurturing by Robot Quarterly Magazine."
    anon f_skeptical "Robot Quarterly Magazine?"
    thotbot "My programming allows me to properly care for up to eight children at once."
    anon f_normal "Really?"
    anon "That's umm... Neat, I guess..."
    thotbot "I assure you, this child has been left in good metallic appendages."
    anon f_worried @ -m_talk "..."
    thotbot "Did you have any other questions?"
    jump thotbot_button_baby.choice


label thotbot_button_baby.lullaby:
    anon f_normal "Need some help?"
    thotbot "It is kind of you to offer but that will not be necessary."
    show anon f_sad
    pause
    thotbot "I was about to commence with the traditional lullaby before placing the child into REM mode."
    anon f_worried "REM mode?"
    thotbot "I believe you humans refer to it as, \"Nap time\"."
    anon "Oh, I see."
    thotbot "Would you like to choose a song from my pre-approved library?"
    anon "Library?"
    thotbot "I am currently equipped with over three hundred lullabys."
    anon f_surprised "Whoa, three hundred?!"
    thotbot "Might I recommend, {i}Baby Robot Shark{/i}?"
    anon f_disgusted "Ehh..."
    thotbot "Or perhaps, {i}What Would the Robot Fox Say?{/i}"
    anon @ -m_talk "..."
    thotbot "{i}Five Little Robot Ducks{/i}?"
    anon f_worried "Do you have anything without robots?"
    show thotbot f_error
    pause
    thotbot f_normal "You have selected, {i}Down by the Mechanical Bay{/i}."
    anon f_skeptical "What the-"
    thotbot "♪ Down by the mechanical bay. ♪"
    thotbot "♪ Where the CPUs provide appropriate output responses to external stimuli. ♪"
    show anon f_worried
    thotbot "♪ Back to my charging station. ♪"
    thotbot "♪ My batteries will be fed electrical current from a constant DC or pulsed DC power source. ♪"
    show anon f_sad_down
    thotbot "♪ For if I don't. ♪"
    thotbot "♪ The result will most definitely be... ♪"
    thotbot "♪ Catastrophic power failure leading to a complete system shutdown and possible memory loss. ♪"
    anon "That was really, umm..."
    thotbot "♪ Down by the mechanical bay!! ♪"
    anon @ f_hurt a_facepalm -m_talk "..."
    jump thotbot_button_baby.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
