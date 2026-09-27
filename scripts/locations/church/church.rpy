label church_dialogue:
    $ player.go_to(L_church)
    if not game.timer.is_dark():
        if getPlayingSound("<loop 3.9>audio/ambience_church.ogg"):
            $ playSound("<loop 3.9>audio/ambience_church.ogg")

    if L_church.is_here(M_keeves) and M_keeves.is_state(S_kee_intro_ready):
        call expression game.dialog_select("church_first_mass")
        $ L_church.visited()
        $ M_keeves.trigger(T_kee_intro_homily)

    elif L_church.first_visit and not (game.timer.is_weekend() and game.timer.is_morning()):
        call expression game.dialog_select("church_first_visit")
        $ L_church.visited()

    if M_consuela.is_state(S_con02_job1) and L_church.is_here(M_keeves, M_angelica):
        call con02_job1_church
        $ player.go_to(L_school_front)
        $ M_consuela.trigger(T_con02_job1)

    if M_mia.is_state(S_mia_church_plan) and game.timer.is_weekend() and game.timer.is_morning():
        call expression game.dialog_select("church_mia_church_plan")

    elif M_mia.is_state(S_mia_convince_helen):
        call expression game.dialog_select("church_mia_convince_helen")
        $ M_mia.trigger(T_helen_confessional)

    elif M_mia.is_state(S_mia_return_priest_outfit):
        call expression game.dialog_select("church_mia_return_priest_outfit")

    elif M_mia.is_state(S_mia_nun_thoughts):
        call expression game.dialog_select("church_mia_nun_thoughts")
        $ M_mia.trigger(T_mc_nun_thoughts)

    elif M_mia.is_state(S_mia_church_night_visit) and game.timer.is_dark():
        call expression game.dialog_select("church_mia_church_night_visit")

    $ game.main()

label church_front_dialogue:
    $ player.go_to(L_church_front)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
