label june_bedroom_dialogue:
    $ game.timer.tick()
    if M_june.is_state(S_june_cosplay_demo):
        label june_cosplay_replay:
        call expression game.dialog_select("june_bedroom_dialogue_cosplay_sex_pre")
        call expression game.dialog_select("june_bedroom_dialogue_cosplay_sex_intro")
        $ anim_toggle = True
        $ animated = False
        $ xray = False
        $ M_june.set("sex speed", .3)
        jump expression game.dialog_select("june_bedroom_dialogue_cosplay_sex_loop")

    scene bedroom_sex2
    if M_june.finished_state(S_june_cosplay_demo):
        call expression game.dialog_select("june_bedroom_dialogue_sex_pre_cosplay")
    else:
        call expression game.dialog_select("june_bedroom_dialogue_sex_pre_no_cosplay")

    menu:
        "Sex!" if M_june.finished_state(S_june_cosplay_demo):
            call expression game.dialog_select("june_bedroom_dialogue_sex_normal_pre")
            call expression game.dialog_select("june_bedroom_dialogue_normal_sex_intro")
            $ anim_toggle = True
            $ animated = False
            $ xray = False
            $ M_june.set("sex speed", .3)
            jump expression game.dialog_select("june_bedroom_dialogue_normal_sex_loop")

        "Cosplay sex!" if M_june.finished_state(S_june_cosplay_demo):
            call expression game.dialog_select("june_bedroom_dialogue_sex_cosplay_pre")
            call expression game.dialog_select("june_bedroom_dialogue_cosplay_sex_intro")
            $ anim_toggle = True
            $ animated = False
            $ xray = False
            $ M_june.set("sex speed", .3)
            jump expression game.dialog_select("june_bedroom_dialogue_cosplay_sex_loop")
        "Play games.":

            if M_june.finished_state(S_june_cosplay_demo):
                call expression game.dialog_select("june_bedroom_dialogue_play_games_cosplay_over")
            else:
                call expression game.dialog_select("june_bedroom_dialogue_play_games_cosplay_not_over")
            jump expression game.dialog_select("orc_battle_start")
        "I have to sleep.":

            call expression game.dialog_select("june_bedroom_dialogue_leave")
            jump expression game.dialog_select("sleeping")

    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
