label anna_yoga_button_dialogue:
    call anna_button_yoga_room_dialogue_pre

    menu:
        "Where's {b}Mrs. Johnson{/b}?":
            call anna_button_yoga_room_dialogue_wheres_mrsj

        "Yoga." if M_mrsj.finished_state(S_mrsj_yoga_report) or M_mrsj.is_state(S_mrsj_yoga_report):
            call anna_button_yoga_room_dialogue_yoga
            call yoga_minigame
            $ game.timer.tick()
        "Never mind.":

            call anna_button_yoga_room_dialogue_post

    hide player
    hide old_anna
    with dissolve
    $ game.main()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
