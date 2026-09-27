label tuuku_button_dialogue:
    if M_eve.is_state(S_eve_party_speak_to_tuuku):
        call expression game.dialog_select("tuuku_button_eve_party_speak_to_tuuku")
        $ M_eve.trigger(T_eve_party_end)
        $ player.go_to(L_map)
        $ game.main()
    elif M_eve.is_state(S_eve_make_up_extort_tuuku):
        call expression game.dialog_select("tuuku_button_eve_make_up_extort_tuuku")
        $ M_eve.trigger(T_eve_got_wine)
        $ L_pizzeria_exterior.unlock()
        $ game.main()

    if L_tattooparlor_roof.is_here(M_tuuku):
        call expression game.dialog_select("button_tuuku_intro_roof")
    elif L_tattooparlor_alley.is_here(M_tuuku):
        call expression game.dialog_select("button_tuuku_intro_alley")
    menu menu_tuuku_dialogue:
        "Tanaman Anda." if L_tattooparlor_roof.is_here(M_tuuku):
            call expression game.dialog_select("button_tuuku_your_plants")
            jump menu_tuuku_dialogue
        "Dikenal gadis-gadis lama?" if L_tattooparlor_roof.is_here(M_tuuku):
            call expression game.dialog_select("button_tuuku_known_the_girls_long")
            jump menu_tuuku_dialogue
        "Anda berjualan di sini?" if L_tattooparlor_alley.is_here(M_tuuku):
            call expression game.dialog_select("button_tuuku_youre_selling_here")
            jump menu_tuuku_dialogue
        "Kenapa kamu pergi seperti itu malam itu?" if M_eve.finished_state(S_eve_police_trouble):
            call expression game.dialog_select("button_tuuku_why_take_off")
            jump menu_tuuku_dialogue
        "Hanya melihat sekeliling." if L_tattooparlor_roof.is_here(M_tuuku):
            call expression game.dialog_select("button_tuuku_just_looking_around")
        "Tidak, terima kasih." if L_tattooparlor_alley.is_here(M_tuuku):
            call expression game.dialog_select("button_tuuku_no_thanks")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
