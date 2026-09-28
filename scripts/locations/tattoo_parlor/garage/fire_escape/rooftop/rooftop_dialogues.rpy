label tattoo_parlor_roof_eve_party_speak_to_jenny:
    scene expression player.location.background_blur with None
    show anon f_surprised a_behind_head with dissolve
    anon @ -m_talk "( This is nuts! )"
    pause
    anon a_salute f_skeptical @ -m_talk "( Wait a second, is that {b}[jen_name]{/b}?! )"
    anon a_idle f_worried @ -m_talk "( What is she doing here? )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
