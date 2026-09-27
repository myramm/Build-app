label anna_button_dialogue:
    scene expression player.location.background_closeup
    if M_anna.is_state(S_anna_dog_hunt):
        call expression game.dialog_select("anna_dialogue_anna_dog_hunt")
        menu:
            "Ya.":
                call expression game.dialog_select("anna_dialogue_anna_dog_hunt_yes")
                $ M_anna.trigger(T_anna_find_awesomo)
            "Tidak.":

                call expression game.dialog_select("anna_dialogue_anna_dog_hunt_no")

    elif M_anna.is_state(S_anna_find_dog):
        if player.has_item("dog"):
            call expression game.dialog_select("anna_dialogue_anna_find_dog_have_dog")
            $ player.remove_item("dog")
            $ M_anna.trigger(T_anna_found_dog)
        else:

            call expression game.dialog_select("anna_dialogue_anna_find_dog_do_not_have_dog")
    hide player
    hide old_anna
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
