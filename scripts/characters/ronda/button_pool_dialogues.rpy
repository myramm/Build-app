label ronda_pool_dialogue_pre_cassie_fun:
    show ronda b_swim
    if wearing_swimsuit:
        show player 53f at left
    else:
        show player 1 at left
    with dissolve
    ronda @ -m_talk "..."
    ronda "What are you even doing here?"
    if wearing_swimsuit:
        show player 50f
    else:
        show player 17
    player_name "Just getting some exercise!"
    player_name "I figured I had to start somewhere, and it can help me get ready for the qualifiers!"
    if wearing_swimsuit:
        show player 51
    else:
        show player 11
    ronda "Look, I ain't helping you, let alone getting in the water at the same time as you... So forget it, okay?"
    if wearing_swimsuit:
        show player 53
    else:
        show player 26
    player_name "That's fine!"
    player_name "I can manage on my own..."
    if wearing_swimsuit:
        show player 51
    else:
        show player 11
    ronda @ f_eyeroll "Ugh... Whateva."
    return

label ronda_pool_dialogue_after_cassie_fun:
    show ronda b_swim f_upset
    if wearing_swimsuit:
        show player 53f at left
    else:
        show player 1 at left
    with dissolve
    ronda "Here to pay {b}Cassie{/b} a little visit?"
    if wearing_swimsuit:
        show player 51f
    else:
        show player 12
    player_name "Uhh... I'm just here to swim?"
    if wearing_swimsuit:
        show player 51f
    else:
        show player 11
    ronda "You can stop pretending..."
    ronda "... You ain't here to train, like I am."
    if wearing_swimsuit:
        show player 51f
    else:
        show player 12
    player_name "Uhh... Okay?"
    if wearing_swimsuit:
        show player 51f
    else:
        show player 11
    ronda @ f_upset_angry "Ugh... You're pathetic."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
