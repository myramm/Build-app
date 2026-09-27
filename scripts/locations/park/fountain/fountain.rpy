label park_fountain_dialogue:
    $ player.go_to(L_park_fountain)
    scene expression player.location.background
    if not player.has_item("weird_coin"):
        if game.timer.is_dark():
            show expression "objects/object_coin_01_night.png" at Position(xalign = 0.44, yalign = 0.81)
        else:
            show expression "objects/object_coin_01.png" at Position(xalign = 0.44, yalign = 0.81)
    player_name "( I can see a lot of coins in there. )"

    $ game.main(call_screen_args=[False, False])
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
