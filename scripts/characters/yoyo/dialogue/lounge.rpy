label yoyo_button_lounge:
    show anon f_worried with dissolve
    anon @ -m_talk "( Oh no, I'm so not getting into it with her right now. )"
    pause
    anon f_worried_surprised @ -m_talk "( The last thing I need is a bowl of noodles for a hat... )"
    anon f_surprised_teeth @ -m_talk "( ... Josie would never let me hear the end it. )"
    hide anon with dissolve
    return


label yoyo_button_lounge.unknown:
    show anon f_confused with dissolve
    anon @ -m_talk "( Hmm... I wonder who that girl is? )"
    pause
    anon f_surprised @ -m_talk "( She's really going at those noodles... )"
    anon f_worried @ -m_talk "( ... Maybe I'll come back when she's less occupied. )"
    hide anon with dissolve
    return


label yoyo_button_lounge.unsure:
    show anon a_sides f_confused with dissolve
    anon @ -m_talk "( She seemed so sincere about that \"appology pie\"... )"
    anon f_thinking @ -m_talk "( ... And I do love banana cream. )"
    pause
    show anon a_rub f_confused
    with {'master': dissolve}
    anon @ -m_talk "( Hmm. I should sleep on it, and maybe find her in the showroom tomorrow. )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
