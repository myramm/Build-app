label priya_button_dialogue:
    call expression game.dialog_select("priya_button_intro")
    menu priya_menu_dialogues:
        "Tidak.":
            call expression game.dialog_select("priya_button_menu_no")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
