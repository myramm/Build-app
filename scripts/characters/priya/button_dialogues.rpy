label priya_button_intro:
    scene expression player.location.background_blur
    show player 5 at left
    show priya f_angry a_point
    with dissolve
    priya "You again?!"
    priya "What are you doing here?!"
    show priya a_crossed with dissolve
    pause
    priya "Do you have some results to report?"
    return

label priya_button_menu_no:
    show priya f_angry a_crossed
    show player 24 at left
    player_name "No, sorry."
    player_name "I was just-"
    show player 5
    show priya a_point with dissolve
    priya "This is a restricted area for a reason!"
    priya "You can't just come and go as you please..."
    show priya a_crossed with dissolve
    show player 10
    player_name "I'm sorry, {b}Priya{/b}."
    show player 24
    player_name "I..."
    player_name "I'll go..."
    show player 5
    show priya f_facepalm a_facepalm with dissolve
    priya "{i}*Sigh*{/i}"
    priya "No, I'm sorry... I'm sorry."
    show priya f_hopeful a_idle with dissolve
    priya "I don't mean to yell at you."
    show priya f_normal
    priya "It's just... It's dangerous for you to be down here."
    priya "So please, don't come back unless you have something to report."
    show player 10
    player_name "O-okay."
    hide player
    hide priya
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
