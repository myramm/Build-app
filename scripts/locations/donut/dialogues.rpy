label donut_buy_dialogue:
    beth @ a_holding_donuts "Here ya go."
    show player 17
    player_name "Thank you."
    show player 1
    beth "Enjoy the sweet holes!"
    hide player with dissolve
    call popup ('give', 'donuts_correct')
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
