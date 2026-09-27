label crystal_button_dialogue:
    scene expression game.timer.image("trailer_interior_c{}")
    if M_crystal.is_state(S_crystal_start):
        $ M_crystal.trigger(T_crystal_intro)

    if M_roxxy.is_state(S_roxxy_picnic_done):
        call expression game.dialog_select("button_crystal_roxxy_go_to_picnic")
    else:
        if M_roxxy.between_states(S_roxxy_assignment_delay, S_roxxy_hows_it_going_delay):
            if game.timer.is_dark():
                call expression game.dialog_select("button_crystal_rox8_11_evening")
            else:
                call expression game.dialog_select("button_crystal_rox8_11_day")
        elif M_roxxy.finished_state(S_roxxy_hows_it_going_delay):
            if game.timer.is_dark():
                call crystal_button_outside
                if _return:
                    $ M_crystal.set('mood', _return)
                $ game.main()
                return
            else:
                call expression game.dialog_select("button_crystal_final_day")
        else:
            call expression game.dialog_select("button_crystal_preamble")
    show old_crystal 1
    menu roxmom_dialogue_repeat:
        "Dimana {b}Roxxy{/b}?" if not game.timer.is_dark():
            if M_roxxy.between_states(S_roxxy_assignment_delay, S_roxxy_hows_it_going_delay):
                call expression game.dialog_select("button_crystal_roxxy_rox8_rox11")
            elif M_roxxy.finished_state(S_roxxy_hows_it_going_delay):
                call expression game.dialog_select("button_crystal_roxxy_final")
            else:
                call expression game.dialog_select("button_crystal_roxxy")
            jump expression game.dialog_select("roxmom_dialogue_repeat")

        "Jadi kamu ibu {b}Roxxy{/b}?" if not game.timer.is_dark() and M_roxxy.between_states(S_roxxy_assignment_delay, S_roxxy_hows_it_going_delay):
            call expression game.dialog_select("button_crystal_roxxys_mom")

        "Apakah {b}Roxxy{/b} sibuk?" if game.timer.is_dark() and M_roxxy.between_states(S_roxxy_assignment_delay, S_roxxy_hows_it_going_delay):
            call expression game.dialog_select("button_crystal_roxxy_busy")

        "Ya, apakah dia ada di sini?" if game.timer.is_dark() and M_roxxy.finished_state(S_roxxy_hows_it_going_delay):
            call expression game.dialog_select("button_crystal_she_here")
            jump expression game.dialog_select("roxmom_dialogue_repeat")

        "Apakah kamu senang berada di rumah?" if not game.timer.is_dark() and M_roxxy.finished_state(S_roxxy_hows_it_going_delay):
            call expression game.dialog_select("button_crystal_happy_home")
            jump expression game.dialog_select("roxmom_dialogue_repeat")
        "{b}Ayah Roxxy{/b}.":

            call expression game.dialog_select("button_crystal_roxxys_dad")
            jump expression game.dialog_select("roxmom_dialogue_repeat")

        "Menawarkan." if M_crystal.is_set("crystal sex offer") and not M_roxxy.get("roxxy crystal sex"):
            call expression game.dialog_select("trailer_interior_crystal_sex_offer_pre_repeat")
            jump expression game.dialog_select("trailer_interior_crystal_sex_offer_menu")

        "kilat." if M_roxxy.get("roxxy crystal sex") and L_trailer_interior.is_here(M_crystal):
            label crystal_hscene_replay:
                if not store._in_replay == None:
                    scene expression game.timer.image("trailer_interior_c{}")
                    show player 11 at left
                    show old_crystal 2 at right
                    with dissolve
            call expression game.dialog_select("trailer_interior_crystal_sex_repeat_inside")
            call expression game.dialog_select("trailer_interior_crystal_sex_or_anal_menu")
            $ anim_toggle = True
            $ animated = False
            jump expression game.dialog_select("trailer_interior_crystal_sex_loop")

        "Maaf mengganggumu." if M_roxxy.between_states(S_roxxy_assignment_delay, S_roxxy_hows_it_going_delay):
            call expression game.dialog_select("button_crystal_sorry_to_bother")

        "Saya harus pergi." if game.timer.is_dark():
            call expression game.dialog_select("button_crystal_should_go_evening")

        "Saya harus pergi." if not game.timer.is_dark():
            call expression game.dialog_select("button_crystal_should_go_day")

    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
