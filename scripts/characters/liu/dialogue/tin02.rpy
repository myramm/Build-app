label tin02_init_liu:
    anon f_normal "Is Tina around?"
    liu f_normal "Yeah, in her office."
    pause
    liu f_curious "Is she expecting you?"
    anon f_worried "Expecting me?"
    liu "Yeah, do you have an appointment?"
    anon "Umm..."
    pause
    anon f_shy "... Yes?"
    pause
    liu f_normal @ f_laugh "Okay, you can head on back."
    anon f_surprised "I can?"

    if M_anon.finished_state(S_ano14_find):
        show anon a_wave with {'master': dissolve}
        anon f_normal "Thanks, {b}Liu{/b}!"
    else:
        anon f_shy "Err, I mean, thanks!"
        liu "Thanks for banking with us, have a pleasant day!"
        anon "Y-yeah, you too."

    hide anon with dissolve
    return 'office'
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
