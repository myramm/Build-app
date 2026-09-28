label mias_house_is_morning:
    scene miahouse
    show player 12 with dissolve
    player_name "( There's no one here... )"
    show player 35
    player_name "( {b}Mia{/b} probably left for {b}school{/b} already. )"
    hide player 35 with dissolve
    return

label mias_house_mia_concerning_visit:
    scene expression game.timer.image("miahouse{}")
    show old_harold 21 at right
    show player 10 at left
    with dissolve
    player_name "{b}Harold{/b}! Is {b}Mia{/b}-"
    show player 11
    player_name "..."
    show old_harold 23
    harold "Hey..."
    show old_harold 22
    show player 12
    player_name "Are you okay?"
    show player 11
    show old_harold 23
    harold "I've been better."
    show old_harold 22
    show player 10
    player_name "Where are you going?"
    show player 5
    show old_harold 23
    harold "I'm... Not quite sure at the moment."
    show old_harold 22
    show player 10
    player_name "Huh?"
    show player 12
    player_name "So, what's with the box?"
    show player 11
    show old_harold 23
    harold "I'm moving out, {b}[firstname]{/b}..."
    show old_harold 22
    show player 22
    player_name "!!!"
    show old_harold 23
    harold "... I'm sorry you had to see us at our worst."
    show old_harold 21
    harold "See you around, kiddo."
    hide old_harold with dissolve
    show player 10
    player_name "Woah!"
    player_name "I'd better check on {b}Mia{/b} and see if she's okay..."
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
