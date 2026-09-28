label kevin_gym_take_it_easy:
    show player 14
    player_name "I'm gonna get out of here man."
    show player 13
    show old_kevin 11b with dissolve
    kevin "Already, bro?"
    show old_kevin 11c
    show player 14
    player_name "Yeah, I've got some other stuff I need to do."
    show player 13
    show old_kevin 9 with dissolve
    kevin "Ah, alright."
    show old_kevin 8
    show player 14
    player_name "Catch you later, {b}Kevin{/b}."
    hide old_kevin
    hide player
    with dissolve
    return

label kevin_gym_lets_lift:
    show player 14
    player_name "Let's just lift."
    show player 13
    show old_kevin 9
    kevin "Oh, you're ready to pump some iron?"
    show old_kevin 10 with dissolve
    kevin "Right on, bro."
    kevin "Let's do this!"
    hide old_kevin
    hide player
    with dissolve
    return

label kevin_gym_intro:
    scene expression background(0, 440, 2.5) as stage
    show player 13 at left
    show old_kevin 9 at right
    with dissolve
    kevin "Hey, bro!"
    show old_kevin 8
    show player 14
    player_name "What's up, {b}Kevin{/b}?"
    show player 13
    show old_kevin 9
    kevin "I've been working on my glutes all morning!"
    show old_kevin 13b with dissolve
    kevin "Feel how tight these bad boys are!"
    show player 10b with dissolve
    player_name "Eh, no thanks..."
    show player 5b
    kevin "You sure, bro?"
    kevin "You don't know what you're missing!"
    show old_kevin 8 with dissolve
    show player 29 with dissolve
    player_name "Heh."
    show player 5 with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
