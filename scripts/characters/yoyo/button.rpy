label yoyo_button_dialogue:
    call yoyo_button_stage

    if L_dealership_lounge.is_here(M_yoyo):
        if not M_yoyo.get('met', None):
            call yoyo_button_lounge.unknown
        elif M_yoyo.is_state(S_yoy01_hold):
            call yoyo_button_lounge.unsure
        else:
            call yoyo_button_lounge

    elif not M_yoyo.once('met'):
        call yoyo_event_intro
        $ player.go_to(L_dealership_showroom)
        $ M_kim.set('state', 'jailed')
        $ M_yoyo.trigger(T_yoy00_hook)

    elif M_yoyo.is_state(S_yoy01_wait):
        call yoy01_wait_yoyo

    elif M_yoyo.is_state(S_yoy01_hold):
        call yoy01_hold_yoyo

    elif M_yoyo.finished_state(S_yoy01_lewd):
        if not M_yoyo.once('truck_repeat'):
            call yoyo_button_showroom
        else:
            call yoyo_button_showroom.repeat
    else:

        call yoyo_button_dealership

    if isinstance(_return, Trigger):
        $ M_yoyo.trigger(_return)

    elif isinstance(_return, Location):
        $ player.go_to(_return)

    elif _return == 'dumpster':
        $ player.go_to(L_map)
        $ game.timer.tick(3)

    $ game.main()
    return


label yoyo_button_stage:
    if L_dealership_showroom.is_here(M_yoyo):
        if L_dealership_showroom.is_here(M_josie):
            scene expression background(856, 464, 4.5) as stage
            if M_yoyo.is_state(S_yoy01_hold):
                show yoyo a_clasp f_shy
            else:
                show yoyo a_crossed
        else:
            scene expression background(608, 512, 3.8) as stage
            if M_yoyo.is_state(S_yoy01_hold):
                show yoyo f_shy
            else:
                show yoyo
            show xtra3 as counter at right

    elif L_dealership_lounge.is_here(M_yoyo):
        show expression background(344, 376, 1.5) as stage
        show expression im.Blur(im.Rotozoom('images/characters/yoyo/buttons/character_yoyo_dealership_lounge.png', 0, 1.5), 1.7) as yoyo:
            align (.5, 1.)
            offset (80, 30)
    else:

        scene expression player.location.background_blur as stage
        show yoyo
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
