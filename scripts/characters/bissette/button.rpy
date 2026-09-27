label bissette_button_dialogue:
    scene french_class_c
    if M_bissette.is_set("meet in office"):
        call expression game.dialog_select("bissette_dialogue_meet_in_office")

    elif M_bissette.is_state(S_bissette_check_dictionary):
        call expression game.dialog_select("bissette_dialogue_check_dictionary")
        $ M_bissette.trigger(T_bissette_missing_pages)
    else:

        call expression game.dialog_select("bissette_dialogue_intro")
        menu bissette_button_menu:
            "Kode Pakaian." if M_eve.is_state(S_eve_dress_code_ask_teachers):
                call expression game.dialog_select("bissette_dialogue_dress_code")

            "Tugas makanan." if M_bissette.between_states(S_bissette_find_food_book, S_bissette_french_food_assignment):
                call expression game.dialog_select("bissette_dialogue_food_assignment_intro")
                if not M_bissette.is_state(S_bissette_french_food_assignment):
                    call expression game.dialog_select("bissette_dialogue_food_assignment_prepare_assignment")
                else:

                    call expression game.dialog_select("bissette_dialogue_food_assignment_do_assignment")

            "tugas puisi." if M_bissette.between_states(S_bissette_find_poem_reference_book, S_bissette_print_poem_assignment):
                if M_bissette.between_states(S_bissette_find_poem_reference_book, S_bissette_do_poem_assignment):
                    call expression game.dialog_select("bissette_dialogue_poem_assignment_intro")
                    if M_bissette.is_state(S_bissette_do_poem_assignment):
                        call expression game.dialog_select("bissette_dialogue_poem_assignment_do_assignment")
                else:

                    call expression game.dialog_select("bissette_dialogue_poem_assignment_print_assignment")

            "Les privat." if M_bissette.is_state(S_bissette_end) and not M_bissette.is_set("night visit"):
                call expression game.dialog_select("bissette_dialogue_private_tutoring")
                $ M_bissette.set("night visit", True)

            "bimbingan belajar." if M_bissette.between_states(S_bissette_tutoring, S_bissette_fix_printer):
                if M_bissette.is_state(S_bissette_tutoring):
                    call expression game.dialog_select("bissette_dialogue_tutoring")
                    $ M_bissette.trigger(T_bissette_require_dictionary)

                elif M_bissette.is_state([S_bissette_find_dictionary, S_bissette_get_dictionary]):
                    call expression game.dialog_select("bissette_dialogue_get_dictionary")
                else:

                    call expression game.dialog_select("bissette_dialogue_replace_missing_pages")
            "Mengobrol.":

                call expression game.dialog_select("bissette_dialogue_chat")
            "Tidak juga.":

                call expression game.dialog_select("bissette_dialogue_leave")

    hide player
    hide teacher
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
