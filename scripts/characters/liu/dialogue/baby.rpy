label liu_button_baby:
    show anon with dissolve
    anon "Hey, how's it going?"
    liu f_happy "Hey, {b}[firstname]{/b}."
    liu f_happy_baby "Isn't our baby wonderful?"
    show anon f_shy_low

    menu liu_button_baby.choice:
        "The best.":

            jump liu_button_baby.best
        "How are you feeling?":

            jump liu_button_baby.feeling
        "I'll let you get back to it.":

            pass

    show liu f_happy
    anon f_normal "I'll let you get back to it."
    liu f_happy_baby "Say bye to Daddy."
    anon f_shy_low "Heh, goodbye little one."
    show anon a_wave
    with {'master': dissolve}
    anon "Take care of your mommy for me."
    hide anon with dissolve
    return


label liu_button_baby.best:
    anon @ f_happy "The best!"

    if M_liu.pregnancy.baby_gender == 'boy':
        liu "He's hardly fusses at all!"
    else:
        liu "She's hardly fusses at all!"

    show liu f_happy
    anon f_confused "Sleeping through the night okay?"
    show anon f_normal
    liu "Yeah, so far."
    anon "Well that's good."
    anon "Hopefully it keeps up."
    liu "It will."
    liu "I know it will."
    show anon f_shy_low
    show liu f_happy_baby

    if M_liu.pregnancy.baby_gender == 'boy':
        liu "He's perfect."
    else:
        liu "She's perfect."

    jump liu_button_baby.choice


label liu_button_baby.feeling:
    show liu f_normal
    anon f_confused "Enjoying your time off?"
    show anon f_normal
    liu f_worried "Yeah, why?"
    liu "Is everything okay at the bank?!"
    anon f_surprised "Huh?!"
    anon f_worried "Y-yeah everything's fine."
    liu "You've been checking in on {b}Tina{/b} and keeping her company like I asked, right?"
    anon f_normal "Yes, of course."
    liu f_ashamed_down "I'm serious, {b}[firstname]{/b}."
    liu f_worried "You have no idea how lonely it gets when you're there all by yourself."
    anon "Heh, I'll go spend some time with {b}Tina{/b}, I promise."
    liu f_normal "Hmm, okay."
    liu f_happy_baby "We'll be fine here, won't we little one?"
    show anon f_shy_low
    liu "Yes, we will."
    jump liu_button_baby.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
