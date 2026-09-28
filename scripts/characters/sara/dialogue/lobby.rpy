label sara_button_lobby:
    show anon with dissolve
    sara "Need some help, hun?"

    menu sara_button_lobby.choice:
        "I'm good, thanks!":
            pass

    anon f_normal "I'm good, thanks!"
    sara f_normal "Okie dokie!"
    hide anon with dissolve
    return


label sara_button_lobby.job:
    show anon with dissolve
    anon "Miss {b}Sara{/b}?"
    sara "Hey, {b}[firstname]{/b}!"
    anon "What are you doing here?"
    sara "Watching the front desk, of course..."
    anon "You work here?"
    sara @ -m_talk "Mhmm."
    pause
    sara "The pay isn't much but they only charge us half price for our apartment."
    anon "Well, that's nice."
    sara "Yeah, it's a pretty nice arrangement."
    sara "Let me know if you need help finding someone."
    anon "O-okay, thanks."
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
