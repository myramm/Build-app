label police_office_dialogue:
    $ player.go_to(L_police_office)

    if M_anon.is_state(S_ano21_cops):
        call ano21_cops_police_office
        $ player.go_to(L_police_front)
        $ M_anon.trigger(T_ano21_cops)
        $ M_rump.move(L_police_basement, (
            14 - M_melonia.pregnancy.days_elapsed) * 4 - game.timer._tod)

    elif M_mia.is_set("questioned yumi") and M_mia.is_set("questioned earl"):
        call expression game.dialog_select("police_office_mia_clues_summary")
        $ M_mia.trigger(T_mia_clues_summary)

    elif M_mia.is_state(S_mia_harold_gift):
        call expression game.dialog_select("police_office_mia_harold_gift")
        $ player.remove_item("aviators")
        $ M_mia.trigger(T_harold_glasses)

    elif M_mia.is_state(S_mia_convince_harold):
        call expression game.dialog_select("police_office_mia_convince_harold")
        $ M_mia.trigger(T_harold_find_goods)

    elif M_mia.is_state(S_mia_return_goods):
        call expression game.dialog_select("police_office_mia_return_goods")
        $ M_mia.trigger(T_harold_promotion)

    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
