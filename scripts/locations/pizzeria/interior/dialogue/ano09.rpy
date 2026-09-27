label ano09_init_pizzeria_interior:
    call tony_button_stage
    show tony a_frustrated
    show anon with dissolve:
        flip
    tony "Hey there, champ."

    tony a_idle @ a_point "How's your bank account lookin' these days?"

    anon @ -m_talk "Hmm?"

    anon "I dunno, why?"

    tony f_suspicious @ a_pizza "'Cause the orders are backin' up again..."

    anon f_worried "Well, what am I supposed to do?"

    anon "I already bought a car!"

    tony "You need to get yourself somethin' faster."

    anon f_surprised "Faster?"

    anon "Are you telling me to speed, boss?"

    tony @ f_eyeroll a_frustrated "I ain't sayin' that."

    pause
    tony f_normal @ f_smirk_wink a_finger_up "But I ain't not sayin' that either, capisce?"

    anon f_normal @ f_laugh "Haha!"

    tony "A car with a little flash, maybe?"

    tony "Somethin' that'll drive all the girls wild."

    anon @ f_skeptical "Eh?"

    tony f_suspicious @ a_fists "C'mon, {b}get ya butt down to the dealership and see what they got in your price range{/b}!"

    anon "Y-ya, oke."

    tony f_normal "Attaboy!"

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
