label tattoo_parlor_interior_dialogue:
    $ player.go_to(L_tattooparlor_interior)
    if not game.timer.is_dark():
        $ playSound("<loop 7 to 114>audio/ambience_house_entrance.ogg")

    if L_tattooparlor_interior.first_visit:
        $ L_tattooparlor_interior.visited()
        call expression game.dialog_select("tattooparlor_first_visit")

    if M_eve.is_state(S_eve_bike_breakdown_check_bike) and not game.timer.is_night() and game.timer.is_weekend():
        call expression game.dialog_select("tattoo_parlor_interior_eve_bike_breakdown_check_bike")

    elif M_odette.is_state(S_ode01_init) and L_tattooparlor_interior.is_here(M_eve, M_grace, M_odette):
        call ode01_init_tattoo_parlour
        $ game.timer.tick()
        $ player.go_to(L_tattooparlor)
        $ M_odette.trigger(T_ode01_init)
        $ game.main()
        return

    elif M_odette.is_state(S_ode02_warn):
        call ode02_warn_tattoo_parlour
        $ game.timer.tick()
        $ player.go_to(L_tattooparlor)
        $ M_odette.trigger(T_ode02_warn)
        call player_just_wokeup.skip
        $ game.main()
        return

    elif M_mia.is_state(S_mia_get_tattoo) and player.location.is_here(M_mia) and not (
        M_eve.pregnancy.character_bedridden or M_grace.pregnancy.character_bedridden or
        M_grace.pregnancy.stage or L_NULL.is_here(M_grace)):
        call expression game.dialog_select("tattooparlor_mia_get_tattoo")
        $ M_grace.move(L_tattooparlor_interior)
        $ M_mia.trigger(T_mia_visit_tattoo_parlor)

    if not M_eve.pregnancy or M_eve.pregnancy.announced_pregnancy:
        pass
    elif M_eve.pregnancy.stage > 1:
        pass
    elif M_eve.pregnancy.first_baby:
        pass
    else:
        call tattoo_parlor_interior_eve_pregnancy_repeat
        $ M_eve.pregnancy.set('announced_pregnancy')
        $ game.main()

    if not M_grace.pregnancy or M_grace.pregnancy.announced_pregnancy:
        pass
    elif M_grace.pregnancy.stage > 1:
        pass
    elif M_grace.pregnancy.first_baby:
        call expression game.dialog_select("tattoo_parlor_interior_grace_first_baby")
        menu:
            "Agree.":
                call expression game.dialog_select("tattoo_parlor_interior_grace_first_baby_agree")
                $ M_grace.pregnancy.abort_baby()
                $ game.main()
            "No, you should keep it.":

                call expression game.dialog_select("tattoo_parlor_interior_grace_first_baby_keep_it")
                if player.has_required_chr(10):
                    call expression game.dialog_select("tattoo_parlor_interior_grace_first_baby_keep_it_pass")
                    $ M_grace.pregnancy.set('announced_pregnancy')
                else:
                    call expression game.dialog_select("tattoo_parlor_interior_grace_first_baby_keep_it_fail")
                    $ M_grace.pregnancy.abort_baby()
                    $ player.go_to(L_map)
                $ game.timer.tick()
                $ game.main()
    else:
        call expression game.dialog_select("tattoo_parlor_interior_grace_repeat_baby")
        $ M_grace.pregnancy.set('announced_pregnancy')
        $ game.main()

    if not M_odette.pregnancy or M_odette.pregnancy.announced_pregnancy:
        pass
    elif M_odette.pregnancy.stage > 1:
        pass
    elif M_odette.pregnancy.first_baby:
        call expression game.dialog_select("tattoo_parlor_interior_odette_first_baby")
        menu:
            "Yeah, okay.":
                call expression game.dialog_select("tattoo_parlor_interior_odette_first_baby_okay")
                $ M_odette.pregnancy.set('announced_pregnancy')
                $ M_odette.set("gotta_have_that_dick", True)
                jump odette_repeat_sex_bike
            "Not right now!":

                call expression game.dialog_select("tattoo_parlor_interior_odette_first_baby_not_now")
                $ M_odette.pregnancy.set('announced_pregnancy')
                jump odette_pregnancy_have_baby_end
    else:
        call expression game.dialog_select("tattoo_parlor_interior_odette_repeat_baby")
        $ M_odette.pregnancy.set('announced_pregnancy')
        $ game.main()

    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
