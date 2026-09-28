label yoga_room_mrsj_yoga_class:
    scene yoga_room_night
    show player 380 at left with dissolve
    show old_anna 12 at right with dissolve
    anna "Excuse me?"
    show player 385
    anna "Have you seen {b}Tammy{/b} around lately?"
    show old_anna 11
    show player 384
    player_name "Actually, she won't be able to make it tonight."
    show player 386
    player_name "She sent me to help teach her class..."
    show player 385
    show old_anna 12
    anna "Oh, has she told you what to do?"
    show old_anna 11
    show player 386
    player_name "Well, {b}Mrs. Johnson{/b} gave me this list of instructions."
    show player 381
    player_name "I looked over them a bit... I think I can manage."
    if M_anna.is_state(S_anna_start):
        show player 384
        player_name "Have you seen a girl named, {b}Anna{/b}?"
        player_name "{b}Mrs. Johnson{/b} said she'd be able to assist me."
        show player 385
        show old_anna 3 with dissolve
        anna "I'm {b}Anna{/b}!!"
        show old_anna 1
        show player 386
        player_name "Oh!!"
        show player 385
        show old_anna 3
        anna "I hope you know what you're doing!"
        show old_anna 2
        anna "I'll be there to help you through the moves, don't worry."
    else:
        show player 386
        player_name "She said you could maybe help me?"
        show player 385
        show old_anna 2 with dissolve
        anna "Of course I'll help you!"
        anna "And don't worry! You just tell me which positions and I'll follow your lead."
    hide player
    hide old_anna
    scene black
    with fade
    return

label yoga_room_mrsj_yoga_retry:
    scene yoga_room_night
    show player 385 at left with dissolve
    show old_anna 2 at right with dissolve
    anna "Ready to try again?"
    show old_anna 1
    show player 386
    player_name "I think I've got the positions memorized this time."
    show player 385
    anna "Just tell me which positions to get into and I'll follow your lead."
    hide player
    hide old_anna
    scene black
    with fade
    return

label yoga_room_strangers_only:
    scene expression game.timer.image("yoga_room{}")
    show player 12
    with dissolve
    player_name "( There's no one I know here... )"
    show player 35
    player_name "( I should come back another time, perhaps... )"
    hide player 35 with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
