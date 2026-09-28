label cassie_pool_dialogue_rules:
    scene location_pool_closeup1
    show cassie 2 at right
    if wearing_swimsuit:
        show player 53f at left
    else:
        show player 1 at left
    with dissolve
    cassie "Can I help you with something?"
    show cassie 4
    if wearing_swimsuit:
        show player 45
    else:
        show player 108f
    player_name "Umm... What are the rules again?"
    if wearing_swimsuit:
        show player 53f
    else:
        show player 1
    show cassie 2
    cassie "Well, you can't swim in your clothes..."
    show cassie 3
    cassie "You have to {b}use one of the changing rooms to put on a swimsuit{/b}!"
    if wearing_swimsuit:
        show player 50f
    else:
        show player 17
    show cassie 4
    player_name "Oh. Great! Thanks!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
