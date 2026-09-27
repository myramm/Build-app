label roz_button_dialogue:
    if M_consuela.is_state(S_con02_job3):
        call con02_job3_roz
        $ M_roz.set("fun time", True)
        $ M_consuela.trigger(T_con02_job3)
        $ game.main()

    if M_roz.is_state(S_roz_access_phone):
        call roz_phone_prompt
        $ game.main()

    call expression game.dialog_select("roz_dialogue_intro")
    menu roz_dialogue_options:
        "Ruang bawah tanah?" if L_hospital_basement.locked:
            if M_priya.is_state(S_priya_talk_to_roz):
                call expression game.dialog_select("roz_dialogue_basement_priya")
                $ M_priya.trigger(T_priya_talked_to_roz)
                $ game.main()
            else:
                call expression game.dialog_select("roz_dialogue_basement")
                jump roz_dialogue_options
            $ game.main()
        "Lantai pertama?":

            call expression game.dialog_select("roz_dialogue_1st_floor")
            jump expression game.dialog_select("roz_dialogue_options")
        "Lantai dua?":

            call expression game.dialog_select("roz_dialogue_2nd_floor")
            jump expression game.dialog_select("roz_dialogue_options")
        "Lantai tiga?":

            call expression game.dialog_select("roz_dialogue_3rd_floor")
            jump expression game.dialog_select("roz_dialogue_options")

        "Jadwal." if M_roz.is_state(S_roz_access_enquire):
            call expression game.dialog_select("roz_dialogue_schedule")
            $ M_roz.trigger(T_roz_access_ask)

        "Keturunan." if (M_aqua.is_state(S_aqua_boatsmith_search) and
                       M_roz.is_state(S_roz_start) and
                       not M_roz.finished_state(S_roz_obits_collect)):
            call expression game.dialog_select("roz_dialogue_ancestory")
            $ M_roz.trigger(T_roz_obits_ask)
            $ M_roz.set("fun time", True)

        "Istirahatlah." if ((M_consuela.finished_state(S_con02_scam) or
                           M_roz.finished_state(S_roz_obits_collect)) and
                          not M_roz.is_set("fun time")):
            call expression game.dialog_select("roz_dialogue_go_on_break")
            $ M_roz.set("fun time", True)
        "Tidak ada apa-apa.":

            call expression game.dialog_select("roz_dialogue_nothing")

    hide player
    hide old_roz
    hide xtra 35
    hide roz_desk
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
