label josie_button_recovery:
    show anon with dissolve
    josephine f_sexy "Hey, {b}[firstname]{/b}."
    josephine "You come by to check on us again?"

    menu josie_button_recovery.choice:
        "Yup.":
            pass

    anon f_normal "Yup."
    josephine f_sexy "You worry too much."
    josephine "We're fine."
    anon "Yeah, I know."
    anon "I just wanna make sure..."
    pause
    anon "... And maybe catch a glimpse of some breastfeeding."
    josephine @ f_laugh "Hah!"
    josephine "Very funny."
    josephine "You're supposed to rub lanoline oil on my nipples after each feeding, you know?"
    anon "Oh, well in that case, forget it!"
    josephine @ f_laugh "Hehe!"
    anon "I'll let you guys get back to resting, okay?"
    josephine f_sexy_down @ -m_talk "Mhmm."
    anon @ f_laugh a_wave "Bye bye, little one."
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
