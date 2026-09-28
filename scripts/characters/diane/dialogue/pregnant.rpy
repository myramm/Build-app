label diane_button_event_pregnancy:
    $ M_diane.pregnancy.set('announced_pregnancy')


    scene expression player.location.background_blur
    show diane b_naked

    if not M_diane.pregnancy.number_of_babies:
        jump diane_button_event_pregnancy.initial
    jump diane_button_event_pregnancy.repeat


label diane_button_event_pregnancy.initial:
label diane_button_event_pregnancy.repeat:
    show diane f_cheese
    show player 13 at left with dissolve
    show diane f_laugh
    diane "{b}[firstname]{/b}!!"
    show player 10
    show diane f_cheese
    player_name "What's the big emergency?!"
    show player 5
    show diane f_laugh
    diane "We did it!"
    diane "I'm pregnant!"
    show diane f_cheese
    show player 14
    player_name "You are?!"
    player_name "Are you sure?!"
    show player 13
    show diane f_laugh
    diane "I'm positive!"
    diane "You're gonna be a daddy!"
    show diane f_cheese
    show player 14
    player_name "I'm gonna-"
    show player 18
    show diane f_normal
    pause
    diane "You alright?"
    show player 14
    player_name "Hmm?"
    player_name "Y-yeah!"
    player_name "This is great news, {b}Diane{/b}!"
    player_name "I'm so happy!"
    hide player
    show diane b_kiss_naked
    with dissolve
    pause
    show player 13 at left
    show diane b_naked f_laugh
    with dissolve
    diane "Mmm, me too!"
    diane "Oh, this is so exciting!"
    show diane f_normal
    diane "I never thought I would have this opportunity!"
    pause
    show diane f_laugh
    diane "Oh, thank you, {b}[firstname]{/b}!"
    diane "Thank you, thank you, thank you!!!"
    hide player
    show diane b_kiss_naked
    with dissolve
    pause
    show player 14 at left
    show diane b_naked f_cheese
    with dissolve
    player_name "Heh, you're welcome..."
    show player 13
    show diane f_normal
    pause
    show player 14
    player_name "So what should I..."
    player_name "{i}*Ahem*{/i} Is there anything I can do for you?"
    show player 13




    diane "Hmm?"
    diane "Oh, no!"
    diane "Just keep doing everything you've been doing."
    diane "Keep being wonderful, {b}[firstname]{/b}!"
    show player 14
    player_name "That, I can definitely do!"
    show player 13
    show diane f_laugh
    diane "Hehe!"
    hide player
    hide diane
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
