label teachers_lounge_first_visit:
    scene expression game.timer.image("backgrounds/location_school_lounge{}_blur.jpg") with fade
    show player 14 with dissolve
    player_name "This must be the teachers' lounge."

    player_name "Their private little getaway from my classmates."

    hide player with dissolve
    return

label teachers_lounge_okita_dose_smith:
    scene location_school_lounge_day_blur
    show player 11
    player_name "( There she is! Drinking coffee just like I thought. )"

    player_name "( I just need to dose the coffee pot! )"

    return

label coffee_pot_dialogue_wrong_time:
    scene location_school_lounge_day_blur
    show player 11
    player_name "( I can't do it while she's sitting there... )"

    return

label coffee_pot_dialogue_right_time:
    scene location_school_lounge_cutscene01
    show text _ ("This seemed like the best course of action.") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("I knew {b}Mrs. Smith{/b} drank coffee from this pot every afternoon.") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("And since it was synthesized using her DNA, it shouldn't affect anybody else.") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("At least, that's what I hoped.") as caption with dissolve
    pause
    return

label coffee_pot_dialogue:
    if M_okita.is_state(S_okita_dose_smith):
        if game.timer.is_afternoon():
            call expression game.dialog_select("coffee_pot_dialogue_wrong_time")

        elif game.timer.is_morning():
            call expression game.dialog_select("coffee_pot_dialogue_right_time")
            $ M_okita.trigger(T_okita_dosed_smith)
    $ player.go_to(L_school_teacherslounge)
    $ game.main()

label microwave_dialogue:
    scene expression game.timer.image("backgrounds/location_school_lounge_microwave{}.jpg")
    player_name "An apple?!" with hpunch
    player_name "Why would anyone cook apples in microwaves..."

    $ A_apple.unlock()
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
