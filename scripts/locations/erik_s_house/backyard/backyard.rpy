label eriks_backyard_dialogue:
    if M_erik.is_state(S_erik_thief_chase):
        call eriks_backyard_erik_thief_chase

    $ game.main()


label erik_thief:
    call expression game.dialog_select("erik_thief_confront")
    if player.has_required_dex(5):
        call expression game.dialog_select("erik_thief_dex_pass")
        $ M_erik.trigger(T_erik_thief_catch)
        $ L_police_front.unlock()
        jump resume_sleeping_bedroom
    else:
        call expression game.dialog_select("erik_thief_dex_fail")
        jump resume_sleeping_bedroom
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
