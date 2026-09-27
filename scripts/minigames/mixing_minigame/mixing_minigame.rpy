label shaking_minigame_win:
    show player 135 with dissolve
    player_name "I hope I did this right!"

    player_name "I don't want to disappoint {b}Diane{/b}."

    hide player with dissolve
    scene black with fade
    scene expression L_diane_garden.background_blur
    show player 137 zorder 0 at Position (xpos=222,ypos=648)
    show diane_chair up zorder 1
    show diane b_laying_back_shirtless a_laydown f_explain zorder 2
    with dissolve
    pause
    show diane f_smirk_up
    with dissolve
    diane "Mmm, that looks delicious!!"

    show player 426 at Position (xpos=175,ypos=648)
    show diane a_drink_sip f_drinking
    with dissolve
    pause
    show diane a_drink f_laugh with dissolve
    diane "Thanks, {b}[firstname]{/b}!!!"

    show diane f_smirk_up
    show player 429
    player_name "Dengan senang hati!"

    player_name "Now you just relax, while I work on your garden."

    show player 426
    diane "Hehe, yes sir!"

    $ M_diane.trigger(T_diane_made_drink)
    $ player.go_to(L_diane_garden)
    $ M_diane.trigger(T_diane_gave_drink)
    $ game.main()

label shaking_minigame_fail:
    show player 135 with dissolve
    player_name "I hope I did this right!"

    player_name "I don't want to disappoint {b}Diane{/b}."

    hide player with dissolve
    scene black with fade
    scene expression L_diane_garden.background_blur
    show player 137 zorder 0 at Position (xpos=222,ypos=648)
    show diane_chair up zorder 1
    show diane b_laying_back_shirtless a_laydown f_shamed zorder 2
    with dissolve
    pause
    diane "Umm, that's not what I ordered..."

    show player 136
    player_name "It isn't?"

    player_name "Whoops!"

    show player 137
    show diane f_smirk_up
    diane "You want me to show you?"

    show player 136
    player_name "Tidak!"

    player_name "I'll make it right. Just one second..."

    $ player.go_to(L_diane_garden)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
