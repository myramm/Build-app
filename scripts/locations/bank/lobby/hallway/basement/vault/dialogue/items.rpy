label bank_vault_case_dialogue:
    scene expression player.location.background_blur
    show anon f_unimpressed with dissolve
    anon @ -m_talk "( This is neither the time nor the case! )"
    anon f_worried @ -m_talk "( What sort of bank orders their safe deposit boxes randomly anyway?! )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
