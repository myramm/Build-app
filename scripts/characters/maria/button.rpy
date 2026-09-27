label maria_button_dialogue:
    call maria_button_stage

    if M_maria.is_state(S_mar01_tour):
        call mar01_tour_maria

    elif M_anon.is_state(S_ano08_sack) and game.timer.is_day():
        call ano08_sack_maria

    elif M_anon.is_state(S_ano08_sack):
        call ano08_late_maria

    elif M_anon.is_state(S_ano11_prep):
        if not M_anon.once('ano11_maria'):
            call ano11_prep_maria
        else:
            call ano11_prep_maria.repeat

    elif M_anon.is_state(S_ano11_bone):
        call ano11_bone_maria
        $ M_anon.trigger(T_ano11_bone)
        $ M_maria.set('sex', False)

    elif M_anon.is_state(S_ano25_find, S_ano25_done):
        call ano25_find_maria

    elif 0 < M_maria.pregnancy.stage < 5:
        call maria_button_pregnant

    elif M_maria.pregnancy.character_bedridden:
        call maria_button_recovery

    elif M_maria.pregnancy.stage > 4 and not game.timer.is_morning():
        call maria_button_baby

    elif L_pizzeria_kitchen.is_here(M_maria):
        call maria_button_pizzeria

    elif L_pizzeria_storage.is_here(M_maria):
        if M_maria.sex:
            call maria_button_sex
        else:
            call maria_button_pizzeria

    elif L_maria_lounge.is_here(M_maria):
        if game.timer.is_evening():
            call maria_button_couch
        else:
            call maria_button_lounge

    elif L_maria_bedroom.is_here(M_maria):
        call maria_button_bedroom

    if _return == 'blowjob':
        pass

    elif _return == 'sex':
        if L_maria_lounge.is_here(M_maria):
            $ M_maria.move(L_maria_bedroom, 1)
        else:
            $ M_maria.move(L_pizzeria_storage, 1)
        $ M_maria.set('sex', True)

    elif _return == 'afterglow':
        if L_maria_bedroom.is_here(M_maria):
            $ player.go_to(L_apt_hall3)
        elif game.timer.is_dark():
            $ player.go_to(L_pizzeria_exterior)
        $ game.timer.tick()
        $ M_maria.set('sex', False)

    $ game.main()
    return

label maria_button_stage:
    if L_pizzeria_kitchen.is_here(M_maria):
        scene expression background(720, 400, 3.2) as stage
        if M_anon.is_state(S_ano06_cook):
            show maria
        elif M_maria.pregnancy.stage > 4 and game.timer.is_afternoon():
            show maria a_baby f_normal_down
        elif M_maria.pregnancy.stage in (3, 4):
            show maria b_magic:
                flip
                xoffset 500
        elif 1 < M_maria.pregnancy.stage < 5:
            show maria b_magic
        else:
            show maria a_spoon_taste f_taste:
                flip
                xoffset 500
    elif L_pizzeria_storage.is_here(M_maria):
        if M_maria.sex:
            scene expression background(536, 400, 2.) as stage
            show maria b_lingerie:
                offset (100, 100)
        else:
            scene location_pizza_storage_shelf_closeup as stage
            show maria b_dressed_back_reach
    elif L_maria_lounge.is_here(M_maria):
        if game.timer.is_evening():
            scene expression background(384, 376, 3.5) as stage
            show maria b_casual at flip
        else:
            scene expression background(584, 376, 3.8) as stage
            if 4 < M_maria.pregnancy.stage:
                show maria b_casual
            else:
                show maria b_casual_behind
        if 1 < M_maria.pregnancy.stage < 5:
            show maria b_casual_magic
    elif L_maria_bedroom.is_here(M_maria):
        scene expression background(600, 400, 2) as stage
        if randomizer() > 50:
            show maria b_naked_shy2 f_shy at flip
        else:
            show maria b_naked_shy1 f_shy at flip
    elif M_maria.pregnancy.character_bedridden:
        scene expression game.timer.image('location_hospital_baby_bed{}')
        show maria b_gown_bed f_normal_down
    else:
        scene expression player.location.background_blur
        show maria
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
