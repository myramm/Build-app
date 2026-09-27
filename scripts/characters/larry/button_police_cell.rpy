label larry_button_dialogue:

    if M_larry.is_state(S_larry_msg_ready):
        call expression game.dialog_select("larry_msg_request")
        $ M_larry.trigger(T_larry_msg_request)

    elif M_larry.is_state(S_larry_msg_sorry):
        call expression game.dialog_select("larry_msg_prompt")

    elif M_larry.is_state(S_larry_msg_given):
        call expression game.dialog_select("larry_msg_reward")
        $ M_larry.trigger(T_larry_msg_reward)

    elif M_larry.finished_state(S_larry_msg_given):
        call expression game.dialog_select("larry_msg_repeat")

    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
