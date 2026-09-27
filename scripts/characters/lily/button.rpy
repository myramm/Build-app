label lily_button_dialogue:
    call expression game.dialog_select("lily_dialogue_pre")
    menu tatiana_options:
        "Anda tampak familier.":
            call expression game.dialog_select("lily_dialogue_familiar")
            jump expression game.dialog_select("tatiana_options")
        "Ada saran?":

            call expression game.dialog_select("lily_dialogue_suggestions")
            jump expression game.dialog_select("tatiana_options")
        "Saya menemukan apa yang saya butuhkan.":

            call expression game.dialog_select("lily_dialogue_leave")

    hide lily
    hide player
    hide xtra
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
