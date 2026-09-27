label backroom_dialogue:
    $ player.go_to(L_library_backroom)
label library_backroom_dialogue:
    if _in_replay or M_jane.get("couple_backroom_sex"):
        call expression game.dialog_select("backroom_dialogue_backroom_count")
        call screen backroom_couple_sex
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
