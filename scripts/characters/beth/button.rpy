label beth_dialogue:
    call expression game.dialog_select("beth_dialogue_pre")
    menu:
        "Aku tidak tahu." if not M_mia.is_set("buy donuts"):
            call expression game.dialog_select("beth_dialogue_do_not_know")

        "I want donuts!" if M_mia.is_set("buy donuts"):
            call expression game.dialog_select("beth_dialogue_want_donuts")
            call screen donut_minigame
        "Tidak, terima kasih.":

            call expression game.dialog_select("beth_dialogue_leave")

    hide player
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
