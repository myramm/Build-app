label anna_button_yoga_room_dialogue_pre:
    scene yoga_room_night
    show old_anna 2 at right
    show player 13 at left
    with dissolve
    anna "Hello, {b}[firstname]{/b}."
    show old_anna 1
    show player 14
    player_name "Hi, {b}Anna{/b}."
    show player 13
    show old_anna 2
    anna "What's up?"
    show old_anna 1
    return

label anna_button_yoga_room_dialogue_wheres_mrsj:
    show player 14
    player_name "I'm looking for {b}Mrs. Johnson{/b}."
    show player 30
    player_name "Do you know where I could find her?"
    show player 5
    show old_anna 2
    anna "She usually teaches during the day."
    anna "She must be home by now..."
    show old_anna 1
    show player 14
    player_name "Oh. I see. Thanks!"
    show player 13
    show old_anna 3
    anna "No problem!"
    return

label anna_button_yoga_room_dialogue_yoga:
    show player 10
    player_name "Do you want to practice some yoga poses with me?"
    show player 5
    show old_anna 3
    anna "Of course!!"
    show old_anna 2
    anna "I like when someone can help me reach those... Hard postures..."
    show old_anna 1
    show player 33
    player_name "Right, you're quite flexible as I remember."
    show player 13
    show old_anna 2
    anna "Alright, let's find a yoga mat..."
    hide old_anna
    scene location_gym_yoga_front
    with fade
    show player 413 at left
    show old_anna 13
    with dissolve
    anna "Which position should we practice?"
    return

label anna_button_yoga_room_dialogue_post:
    show player 36 with dissolve
    player_name "Actually, never mind, see you later."
    show player 1
    show old_anna 2
    with dissolve
    anna "Oh, okay, have a nice evening!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
