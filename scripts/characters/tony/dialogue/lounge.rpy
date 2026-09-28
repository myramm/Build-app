label tony_button_lounge:
    show anon behind tony with dissolve:
        flip
        xoffset 100
    tony @ a_frustrated "'Ey there, champ!"
    anon "Hey, {b}Tony{/b}."
    tony "You wanna watch the game with me?"
    anon @ -m_talk "Hmm?"
    tony "Pop a squat and grab a slice, it's just startin'."
    tony @ a_point "You want a beer?"

    menu tony_button_lounge.choice:
        "What game?":

            jump tony_button_lounge.game
        "No work today?":

            jump tony_button_lounge.work
        "I can't stay.":

            pass

    anon f_normal "I can't stay."
    tony f_suspicious "No?"
    tony f_normal "Well, that's a shame."
    anon "Maybe another time."
    tony f_laugh a_pizza "I guess that means I gotta eat this whole pizza by myself then, eh?"
    hide anon with dissolve
    return


label tony_button_lounge.game:
    anon f_normal "What game?"
    tony f_surprised "You're kiddin' right?"
    anon f_worried "Ehh, no?"
    tony f_normal @ f_laugh "The baseball game, champ!"
    anon f_normal @ f_skeptical "Wait, you're a baseball fan?"
    tony @ a_point_back "Of course I am."
    tony "Hot dogs, Cracker Jacks, and grown men smashin' stuff with wooden bats..."
    tony @ a_frustrated "... What's not to like?!"
    anon "Heh, I guess that does sound like something you'd enjoy."
    tony f_smirk "Ya damn right."
    tony "It's America's favorite pastime, you know?"
    show anon f_thinking
    pause
    anon f_skeptical "Aren't you Italian though?"
    tony a_point f_angry "Ah!"
    show anon f_worried
    tony "Watch that shit."
    tony f_normal a_idle @ f_laugh a_point_back "I'm Italian-American."
    anon f_shy "Right."
    anon "Sorry."
    tony f_smirk "Ahh, forghedaboudit!"
    jump tony_button_lounge.choice


label tony_button_lounge.work:
    anon f_normal "No work today?"
    tony f_normal "You ain't supposed to work on Sundays, champ..."
    tony @ f_question "... Didn't nobody ever teach you that?"
    anon "No."
    pause
    anon "How come?"
    tony @ a_frustrated "It's in the bible, ya knucklehead."
    anon "Huh?"
    tony @ a_finger_up "And on the seventh day, God rested."
    anon f_worried "That's in the bible?"
    tony f_smirk "You better believe it."
    anon f_normal "I had no idea."
    tony "Heh, you learn somethin' new everyday when ya hangin' out with {b}Uncle Tony{/b}, eh?"
    anon "Y-yeah, I guess so..."
    jump tony_button_lounge.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
