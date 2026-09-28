label ano04_late_tony:
    show tony f_suspicious
    show anon behind tony with dissolve
    tony "I needed you, kid."
    show anon f_worried
    tony "Where were you?"
    show anon f_sad_down
    pause
    tony "Ah, don't look like that, come back tomorrow."
    tony "We'll try again, eh?"
    anon f_worried "Sorry To--"
    tony "Just show up this time. Go on, I'll see you tomorrow."
    anon a_salute "Yessir!"
    hide anon with dissolve
    return


label ano04_test_tony:
    show anon with dissolve:
        flip
    tony "You get that bike yet?"

    if player.transport_level:
        anon "Yup, I got it."
        tony "Glad to hear it."
        tony "Take these pizzas and see they get delivered to the right place."
        tony @ f_suspicious "Don't go screwing around now, you hear me?"
        anon "I won't."
        tony "When you get back, I'll pay you real nice."
        anon "Thanks, {b}Tony{/b}."
        anon "I'll be back in a flash, you'll see."
        tony @ f_laugh "Ahh, get out of here, ya knucklehead!"
    else:
        anon f_worried "Not yet, sir."
        tony f_suspicious "Well, what are you waitin' for?!"
        tony "I need these pizzas delivered today, ya knucklehead!"
        anon "I'll go {b}down to the mall and buy a bicycle{/b} right now."

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
