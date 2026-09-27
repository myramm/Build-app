label tired_training_dialogue:
    scene expression game.timer.image("training{}_b")
    show player 5 with dissolve
    player_name "( I'm tired, I should go home and sleep. )"

    hide player with dissolve
    return


label solo_lift:
    scene expression background(0, 440, 2.5) as stage

    if player.stats.str() < 1:
        show anon with dissolve
        anon @ -m_talk "( Time to get strong! )"

        anon @ -m_talk "( How hard can it be? )"

        hide anon with dissolve
        jump weightlifting

    elif game.timer.is_day():
        show player 11 at left with dissolve
        player_name "( I can't do that on my own. )"

        player_name "( I need someone to spot me! )"

        hide player with dissolve
    else:

        call expression game.dialog_select("tired_training_dialogue")

    $ game.main()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
