label ano14_tony_tony_lockbox:
    anon f_unimpressed "So I went to the bank and had a look at that lockbox..."
    tony f_normal "Oh, yeah?"
    tony @ f_smirk_wink "Was it a buttload of cash?"
    anon "No."
    anon "The dumb thing was empty!"
    tony f_question "Empty?"
    tony "Why would your pa hide a key to an empty lockbox?"
    anon f_worried @ f_sad_down "{i}*Sigh*{/i} I have no idea..."
    tony f_suspicious "Tell me somethin', your old man... Was he soft in the head or somethin'?"
    anon @ f_skeptical -m_talk "Hmm?"
    tony "You know, a few toppings short of a pizza?"
    anon @ -m_talk "..."
    tony "His oven light was on but there was nothin' in there?"
    anon @ f_skeptical "What the heck are you talking about?"
    tony @ f_eyeroll "Heh, never mind."
    pause
    tony f_normal "So what are you gonna do now?"
    anon "I was hoping you might have an idea?"
    tony "Well, the only other lead we have is {b}Mayor Rump{/b}."
    tony "We know he's involved but not how or why."
    tony "I'd start lookin' into him."
    anon "What do you mean?"
    tony "You live near his mansion, don't ya?"
    anon "Yeah, but it's loaded with security guards."
    anon "I'll never get inside."
    tony "Heh, never say never, champ..."
    tony "If he's their political and financial backing, then it's as good a place to hit 'em as any."
    anon "Yeah, okay."
    tony "{b}I'd start snoopin' around his place{/b} if I was you."
    tony "There's gotta be {b}someone on the inside{/b} we could coerce into helpin' us?"
    tony "Think you can handle that?"
    anon "I'll try."

    if L_pizzeria_interior.is_here(M_tony):
        show tony a_mc_hip_single f_laugh:
            xoffset 32
        show tony_arms_dressed_a_mc_shoulder_single:
            flip
            xoffset 32
    else:
        show tony a_mc_hip_single f_laugh:
            xoffset -32
        show tony_arms_dressed_a_mc_shoulder_single:
            xoffset -32

    with dissolve
    tony "Attaboy!"
    show tony a_idle f_normal:
        xoffset 0
    hide tony_arms_dressed_a_mc_shoulder_single
    with dissolve

    $ M_anon.trigger(T_ano14_tony)
    jump tony_button_pizzeria.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
