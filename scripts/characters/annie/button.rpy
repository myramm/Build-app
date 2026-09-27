label annie_button_dialogue:
    if L_annie_livingroom.is_here(M_annie):
        jump annie_button_home_dialogues

    if player.location == L_school_musicclassroom:
        scene music_classroom_c
    else:
        scene location_school_second_closeup
    show player 13 at left
    show old_annie 1 at right
    with dissolve

    if player.location == L_school_musicclassroom:
        call expression game.dialog_select("annie_dialogue_music_classroom_intro")
        $ game.main()

    menu:
        "Model." if M_ross.is_state(S_ross_ask_model):
            call expression game.dialog_select("annie_dialogue_ross_ask_model")
        "Hai!":

            call expression game.dialog_select("annie_dialogue_leave")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
