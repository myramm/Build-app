label mia_dialogue_mias_house_front:
    call expression game.dialog_select("mia_dialogue_mias_house_front_intro")
    menu:
        "Tentang pekerjaan rumah itu.":
            call expression game.dialog_select("mia_dialogue_mias_house_front_homework")
        "saya lupa...":

            call expression game.dialog_select("mia_dialogue_mias_house_front_leave")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
