label mrs_ross_office_dialogue:
    $ player.go_to(L_school_rossoffice)

    if L_school_rossoffice.first_visit and not game.timer.is_dark():
        call expression game.dialog_select("ross_office_first_visit")
        $ L_school_rossoffice.visited()

    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
