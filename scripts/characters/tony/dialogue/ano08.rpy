label ano08_late_tony:
    show tony f_suspicious
    show anon with dissolve
    tony "You {b}get that flour out of the back{/b} for {b}Maria{/b}?"
    anon "Not yet."
    tony "Well, it'll have to be tomorrow now."
    tony "Don't let her down, champ."
    anon @ f_grin a_salute "Yes, sir."
    hide anon with dissolve
    return


label ano08_sack_tony:
    show tony f_suspicious
    show anon with dissolve:
        flip
    tony "You {b}get that flour out of the back{/b} for {b}Maria{/b}?"
    anon "Not yet."
    tony @ a_frustrated "Well, you betta get to it, champ!"
    tony "She's in there waitin'."
    anon @ f_grin a_salute "Yes, sir."
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
