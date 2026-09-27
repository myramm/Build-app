label donut_buy_dialogue:
    beth @ a_holding_donuts "Ini dia."

    show player 17
    player_name "Terima kasih."

    show player 1
    beth "Enjoy the sweet holes!"

    hide player with dissolve
    call popup ('give', 'donuts_correct')
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
