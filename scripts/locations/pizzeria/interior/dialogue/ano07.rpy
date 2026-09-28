label ano07_init_pizzeria_interior:
    call tony_button_stage
    show anon with dissolve:
        flip
    tony @ a_point "Hey there, champ."
    tony "How's your bank account lookin' these days?"
    anon f_worried @ -m_talk "Hmm?"
    anon "I dunno, why?"
    tony "'Cause we're startin' to get some real big orders and that little scooter of yours ain't gonna cut it."
    tony "You need somethin' with four wheels and cargo space..."
    tony @ f_smirk_wink "... And maybe a back seat, if you know what I mean?"
    anon f_skeptical "Eh?"
    tony f_suspicious @ a_frustrated "C'mon, {b}get ya butt down to the dealership and see what they got in your price range{/b}!"
    anon "Y-yeah, okay."
    tony f_normal "Attaboy!"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
