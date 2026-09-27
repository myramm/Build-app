label kassy_button_dialogue:
    scene expression player.location.background_blur
    if M_kassy.get("kassy_first_visit"):
        $ M_kassy.set("kassy_first_visit", False)
        call expression game.dialog_select("kassy_first_visit")
    else:
        call expression game.dialog_select("kassy_repeat")

    hide kassy
    hide player
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
