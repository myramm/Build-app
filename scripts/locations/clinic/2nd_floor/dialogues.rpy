label hospital_second_floor_erik_learn_started:
    show player 35
    with dissolve
    player_name "Hmm..."

    player_name "( I wonder where they store all their medicine... )"

    show player 30
    player_name "( I should find the {b}storage room{/b}. )"

    return

label hospital_second_floor_phone_dialogue:
    scene hospital_phone

    if M_roz.is_state(S_roz_access_phone) and L_hospital_lobby.is_here(M_roz):
        call expression game.dialog_select("hospital_second_floor_phone_roz_prank")
        $ M_roz.trigger(T_roz_access_prank)
    else:

        call expression game.dialog_select("hospital_second_floor_phone_nothing")

    $ game.main()

label hospital_second_floor_phone_roz_prank:
    show player 404 with dissolve
    pause
    show player 406 with dissolve
    player_name "Hai!"

    pause
    player_name "I... Umm... There's an emergency on the second floor!!"

    show player 407
    pause
    show player 408
    pause
    show player 407
    pause
    pause
    show player 406
    player_name "Oh, yes, it's about an unregistered patient..."

    show player 407
    pause
    pause
    show player 406
    player_name "Yes, it's urgent!"

    show player 408
    pause
    pause
    show player 407
    pause
    show player 406
    player_name "Terima kasih..."

    show player 407
    pause
    show player 405 with dissolve
    player_name "( Well... That should work... )"

    player_name "( Let's see if she left her desk... )"

    hide player
    with dissolve
    return

label hospital_second_floor_phone_nothing:
    show player 404 with dissolve
    player_name "( I have no reason to call anyone. )"

    hide player
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
