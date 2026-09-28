label park_bushes_loot_located:
    scene expression game.timer.image("park_bushes{}_b")
    show player 4 with dissolve
    player_name "Hmm..."
    show player 12 with dissolve
    if M_larry.finished_state(S_larry_msg_given):
        player_name "( Looks like a pretty well-hidden spot in here. )"
        show player 14
        player_name "( Maybe {b}Mr. Johnson{/b} was telling the truth. )"
    else:
        player_name "( This looks like a good hiding spot. )"
        show player 14
    player_name "( Let's look around. )"
    hide player with dissolve
    return

label park_bushes_loot_bag:
    scene expression player.location.background
    show expression "objects/object_key_02.png" at Position(xpos = 594, ypos = 473)
    player_name "Woaa!"
    player_name "( So many things are in here! )"
    if M_larry.finished_state(S_larry_msg_given):
        player_name "( {b}Mr. Johnson{/b} must've been collecting these items for a while. )"
    else:
        player_name "( This must be where the burglar kept his stolen goods. )"
        player_name "( He must have been collecting these items for a while. )"
    player_name "Hmm..."
    player_name "( That's a strange looking key... )"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
