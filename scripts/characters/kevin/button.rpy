label kevin_button_dialogue:
    scene cafeteria_b
    if M_ross.is_state(S_ross_find_magazines) and not M_ross.get("magazine kevin"):
        call expression game.dialog_select("kevin_magazines")
        call expression "player_ross_magazines_{}_left".format(M_ross.get("magazines remaining"))
        $ M_ross.set("magazine kevin", True)

    elif M_ross.is_state(S_ross_ask_model):
        call expression game.dialog_select("kevin_modeling")

    elif M_kevin.is_state(S_kevin_on_duty):
        call expression game.dialog_select("k01_intro")
        $ M_kevin.trigger(T_kevin_request_spot)
    else:

        if M_kevin.finished_state(S_kevin_erik_agreed):
            call expression game.dialog_select("kevin_greeting_happy")
        else:
            call expression game.dialog_select("kevin_greeting_sad")
        menu kevin_menu_dialogue:

            "Someone to help you out." if M_kevin.between_states(S_kevin_convince_erik, S_kevin_erik_agreed):
                if M_kevin.is_state(S_kevin_erik_agreed):
                    call expression game.dialog_select("k01_outro")
                    $ M_kevin.trigger(T_kevin_help_found)
                else:
                    call expression game.dialog_select("k01_prompt")
                    jump kevin_menu_dialogue

            "Talent show." if M_dewitt.between_states(S_dewitt_talent_show_ask, S_dewitt_replace_guitar) or M_dewitt.is_set("talent helping eve"):
                if M_dewitt.is_set("talent helping eve"):
                    call expression game.dialog_select("dewitt_talent_show_helping_eve")

                elif M_dewitt.is_state([S_dewitt_talent_show_ask, S_dewitt_talent_show_ask_kevin]):
                    call expression game.dialog_select("kevin_guitar_intro")
                    $ M_dewitt.trigger(T_dewitt_kevins_agreement)
                else:

                    call expression game.dialog_select("kevin_guitar_prompt")

            "Guitar." if M_dewitt.is_state(S_dewitt_kevin_give_guitar):
                call expression game.dialog_select("kevin_guitar_outro")
                $ player.remove_item("guitar")
                if M_dewitt.is_set("talent ask eve"):
                    $ M_dewitt.trigger(T_dewitt_find_last_talent)
                else:
                    $ M_dewitt.trigger(T_dewitt_give_fender_guitar)

            "Used panties." if M_somrak.finished_state(S_somrak_start):
                if M_somrak.get("asked kevin panties"):
                    call expression game.dialog_select("kevin_somrak_repeat")
                else:
                    call expression game.dialog_select("kevin_somrak_first")
                    $ M_somrak.set("asked kevin panties", True)
                jump kevin_menu_dialogue

            "Adhesive." if M_dewitt.is_state(S_dewitt_science_adhesive):
                call expression game.dialog_select("kevin_adhesive_prompt")
            "Never mind.":

                call expression game.dialog_select("kevin_goodbye")

    hide old_kevin
    hide player
    with dissolve
    $ game.main()

label kevin_button_dialogue_gym:
    if game.timer.is_day():
        call expression game.dialog_select("kevin_gym_intro")
    else:
        call expression game.dialog_select("tired_training_dialogue")
        $ game.main()
    menu:
        "Let's just lift.":
            call expression game.dialog_select("kevin_gym_lets_lift")
            jump weightlifting
        "Take it easy.":
            call expression game.dialog_select("kevin_gym_take_it_easy")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
