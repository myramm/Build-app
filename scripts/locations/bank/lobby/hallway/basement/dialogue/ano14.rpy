label ano14_meet_bank_basement:
    scene expression background(512, 512, 4.6) as stage
    show anon f_normal with dissolve:
        flip
        xoffset -500
    pause
    anon @ -m_talk "( Man, I wonder what my dad could have stashed away in there? )"
    anon @ f_laugh -m_talk "( It's gotta be cash, right? )"
    anon @ -m_talk "( I bet it's the money these Russian assholes keep saying he stole. )"
    show anon f_thinking
    pause
    anon a_thinking @ -m_talk "( Hmm. )"
    anon @ -m_talk "( Then again, he was working with the mafia, so... It could be anything really! )"
    anon a_idle f_laugh @ -m_talk "( Maybe it's diamonds! )"
    anon @ -m_talk "( Or deeds to a bunch of local land!! )"
    show anon f_thinking a_thinking with dissolve
    pause
    anon f_surprised "{i}*Gasp*{/i}"
    anon f_grin @ -m_talk "( Or keys to a giant yacht!!! )"
    show liu with dissolve
    liu "{b}[firstname]{/b}?"
    anon "( {b}Dad{/b} always used to talk about wanting a yacht. )"
    anon "( That's totally what it's going to be, I just know it! )"
    liu f_worried "{b}[firstname]{/b}?"
    show anon f_normal with {'master': dissolve}:
        unflip
        xoffset 0
    anon f_normal @ -m_talk "Hmm?"
    liu "Are you okay?"
    anon a_idle "Yeah, I'm fine!"
    liu f_normal "Sorry I took so long."
    anon "No worries."
    anon "I was just admiring your vault."
    liu @ f_laugh "Pretty neat, huh?"
    anon "Heh, yeah!"
    anon @ f_laugh "It's awesome!"
    anon f_thinking "Concrete reinforced I assume?"
    liu @ f_curious "Ehh."
    liu "I have no idea, to be honest."
    anon f_normal "Right."
    anon @ f_laugh "Heh, why would you?"
    pause
    liu "What's the number?"
    anon @ -m_talk "Hmm?"
    liu "The number for the lockbox."
    anon @ f_laugh "Oh, right!"
    anon f_shy_down a_backpack "The number is..."
    if player.has_item('picture4'):
        show anon f_shy_low a_box_attic_photo
    else:
        show anon f_shy_low a_paper_tony
    anon "{b}11082{/b}."
    show anon f_normal
    liu "Alright."
    liu "Come on inside and you can help me look for it."
    anon "Sure thing!"
    hide liu
    show anon a_sides:
        flip
        xoffset -500
    with {'master': dissolve}
    liu f_worried "I don't know why no one has ever organized these lockboxes..."
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
