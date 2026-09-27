label angelica_button_dialogue:
    if player.location == L_church_angelica:
        jump angelica_room_button_dialogue
    else:
        jump angelica_default_button_dialogue
    $ game.main()

label angelica_default_button_dialogue:
    if M_ross.is_state(S_ross_get_linens) and not player.has_item("linens"):
        call expression game.dialog_select("angelica_dialogue_ross_get_linens_pre")
        menu:
            "Linen.":
                call expression game.dialog_select("angelica_dialogue_ross_get_linens")
                $ player.get_item("linens")

    elif M_mia.is_set("helen dialogue change"):
        call expression game.dialog_select("angelica_dialogue_change_pre")
        menu:
            "Bicara.":
                call expression game.dialog_select("angelica_dialogue_change_talk")
            "kuburan.":

                call expression game.dialog_select("angelica_dialogue_change_graveyard")
            "Sudahlah.":

                call expression game.dialog_select("angelica_dialogue_change_leave")
    else:

        call expression game.dialog_select("angelica_dialogue_pre")
    $ game.main()

label angelica_room_button_dialogue:
    if M_helen.is_set("helen route"):
        call expression game.dialog_select("angelicas_room_dialogue_helen_route_pre")
        menu angelicas_room_dialogue_helen_route_options:
            "Memukul.":
                call expression game.dialog_select("angelicas_room_dialogue_helen_route_spanking")
                jump expression game.dialog_select("sacrament_complete")
            "Benih suci.":

                call expression game.dialog_select("angelicas_room_dialogue_helen_route_holy_seed")
                jump expression game.dialog_select("helen_mc_churchsex")
            "Sebarkan {b}Helen{/b}.":

                call expression game.dialog_select("angelicas_room_dialogue_helen_route_spread_helen")
                jump expression game.dialog_select("sacrament_complete")
            "Apakah kamu sudah berdosa?":

                call popup ('alpha')
                jump expression game.dialog_select("angelicas_room_dialogue_helen_route_options")
            "Tidak ada apa-apa.":

                call expression game.dialog_select("angelicas_room_dialogue_helen_route_leave")
                $ game.main()

    elif M_mia.is_set("mia route"):
        call expression game.dialog_select("angelicas_room_dialogue_mia_route")

    elif M_mia.is_state(S_mia_harolds_thoughts):
        call expression game.dialog_select("angelicas_room_dialogue_mia_harolds_thoughts")

    elif M_mia.is_state(S_mia_find_sinners):
        call expression game.dialog_select("angelicas_room_dialogue_mia_find_sinners_pre")
        menu:
            "Temukan orang berdosa.":
                call expression game.dialog_select("angelicas_room_dialogue_mia_find_sinners")

    elif M_mia.is_state(S_mia_angelicas_whip):
        call expression game.dialog_select("angelicas_room_dialogue_mia_angelicas_whip_pre")
        menu:
            "Cambuk.":
                if player.has_item("whip"):
                    $ player.remove_item("whip")
                    jump expression game.dialog_select("helen_sacrement_training_part2")
                call expression game.dialog_select("angelicas_room_dialogue_mia_angelicas_whip")
            "Tidak ada apa-apa.":

                call expression game.dialog_select("angelicas_room_dialogue_mia_angelicas_whip_leave")
    else:

        if M_mia.is_state([S_mia_harolds_thoughts, S_mia_angelicas_final_request]):
            call expression game.dialog_select("angelicas_room_dialogue_mia_angelicas_final_request_pre")
            $ game.main()
        else:
            call expression game.dialog_select("angelicas_room_dialogue_default_pre")
            $ player.go_to_previous()
            $ game.main()
        menu:
            "Diikat." if M_mia.is_state([S_mia_harolds_thoughts, S_mia_angelicas_final_request]) and not player.has_item("strapon"):
                call expression game.dialog_select("angelicas_room_dialogue_mia_angelicas_final_request_strap_on")

            "Tidak ada apa-apa." if M_mia.is_state([S_mia_harolds_thoughts, S_mia_angelicas_final_request]):
                call expression game.dialog_select("angelicas_room_dialogue_mia_angelicas_final_request_leave")
                $ game.main()

            "Tidak ada apa-apa." if not M_mia.is_state([S_mia_harolds_thoughts, S_mia_angelicas_final_request]):
                call expression game.dialog_select("angelicas_room_dialogue_default_leave")
                $ game.main()
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
