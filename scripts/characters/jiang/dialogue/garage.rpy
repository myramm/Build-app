label jiang_button_garage:
    show anon with dissolve
    anon "Hello."
    show jiang f_suspicious with dissolve:
        unflip
        xoffset 0
    jiang @ -m_talk "Hmm?"
    jiang "You need something?"

    menu jiang_button_garage.choice:
        "Nice garage!":
            jump jiang_button_garage.garage
        "That's a weird car...":

            jump jiang_button_garage.truck
        "Nope.":

            pass

    anon f_normal "Just looking around."
    jiang f_normal @ f_suspicious "Well, go loiter somewhere else."
    jiang "We ain't exactly supposed to have customers back here."
    jiang @ f_suspicious "You know what I'm sayin'?"
    anon @ a_wave "Y-yeah, okay."
    jiang "Thanks."
    hide anon with dissolve
    return


label jiang_button_garage.garage:
    anon f_normal @ f_laugh "Nice garage!"
    jiang f_suspicious "Yeah, thanks... I guess."
    anon "Are you the only mechanic here?"
    jiang f_normal "Nah, I got a few guys workin' under me but they're on call right now..."
    anon "Ah, I see."
    jump jiang_button_garage.choice


label jiang_button_garage.truck:
    anon f_skeptical "That's a weird car..."
    jiang f_normal "Heh, it's a truck actually..."
    anon f_surprised "A truck?"
    jiang "Yeah, it's called a Hypertruck."
    jiang "They're calling it {i}THE{/i} vehicle of the future."
    anon a_thinking f_thinking "Hmm."
    pause
    anon "I didn't imagine the future would be so..."
    jiang "Ugly?"
    anon f_normal a_idle @ f_snarky a_point "... Yeah."
    jiang "Hah, tell me about it..."
    jump jiang_button_garage.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
