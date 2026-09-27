label somrak_button_dialogue:
    scene expression player.location.background_closeup with None
    if M_somrak.is_state(S_somrak_start):
        call expression game.dialog_select("button_somrak_start")
        $ M_somrak.trigger(T_somrak_hungry)
        $ game.main()
    elif game.timer.is_morning() or game.timer.is_dark():
        call expression game.dialog_select("button_somrak_morning_dialogue")
        $ game.main()

    elif M_somrak.is_state(S_somrak_waiting_a, S_somrak_waiting_b, S_somrak_waiting_c, S_somrak_waiting_d):





        python hide:
            pants = {'debbie_panties': 'Debbie', 'jenny_panties': 'Jenny',      
                     'mia_panties': 'Mia', 'roxxy_panties': 'Roxxy',
                     'eve_panties': 'Eve', 'grace_panties': 'Grace',
                     'odette_panties': 'Odette', 'bridget_panties': 'Bridget'
                     }
            try:
                item = next(item for item in player.inventory.items if item in pants)
                M_somrak.set('delivered_panties', pants[item])
                M_somrak.set("just_delivered_panties", True)
                player.remove_item(item)
            except StopIteration:
                M_somrak.set("just_delivered_panties", False)
        if M_somrak.get('just_delivered_panties'):
            call expression game.dialog_select("button_somrak_panties_story")
            if M_somrak.is_state(S_somrak_waiting_a):
                call expression game.dialog_select("button_somrak_has_panties")
            else:
                call expression game.dialog_select("button_somrak_panties_repeatable")
            $ M_somrak.trigger(T_somrak_fed)
            call muay_thai
            $ game.main()
        elif M_somrak.is_state(S_somrak_waiting_a):
            call expression game.dialog_select("button_somrak_waiting_for_panties")
            $ game.main()

    call expression game.dialog_select("button_somrak_afternoon_dialogue")

    menu somrak_menu_dialogue:
        "More training?":
            call expression game.dialog_select("button_somrak_more_training_not_trained_1")
            if M_somrak.is_state(S_somrak_sated_a, S_somrak_sated_b, S_somrak_sated_c, S_somrak_sated_d):
                call expression game.dialog_select("button_somrak_more_training_not_trained_2")
                call muay_thai
            else:
                call expression game.dialog_select("button_somrak_more_training_not_trained_3")
                jump somrak_menu_dialogue
        "The monkey thing.":
            call expression game.dialog_select("button_somrak_monkey_thing")
            jump somrak_menu_dialogue
        "Panties obsession.":
            call expression game.dialog_select("button_somrak_panties_obsession")
            jump somrak_menu_dialogue
        "Sudahlah.":
            call expression game.dialog_select("button_somrak_nevermind")

    $ game.main()
    return


label muay_thai:
    $ renpy.dynamic(dex=player.stats._dex)

    call combat ('lesson', gui=False, hint='screens', level=3 + (dex + 1) // 2, limit=bisect.bisect((4, 7, 9), dex) + 1, skill=dex)


    $ game.timer.tick()

    if not _return:
        jump muay_thai.fail

    scene expression player.location.background_closeup
    with fade

    if M_somrak.finished_state(S_somrak_sated_a):
        call button_somrak_panties_next_times
    else:
        call button_somrak_panties_first_time

    call button_somrak_panties_repeatable_continue

    $ player.increase_dex()
    call popup ('dex', True)

    $ M_somrak.trigger(T_somrak_trained)
    return


label muay_thai.fail:
    scene expression game.timer.image("training{}_b")
    show masterplayer 27 at left
    show somrak f_angry a_cane_up
    with fade
    somrak "NO, NO, NO!" with vpunch
    somrak "You're attacking like an undisciplined dog!"

    show somrak f_normal
    player_name "I'm sorry, {b}Master{/b}... I-"

    show somrak a_poke f_angry
    show masterplayer 40
    player_name "!!!" with hpunch
    show masterplayer 27
    show somrak f_angry a_point with dissolve
    somrak "Do not be sorry, be better!"

    somrak "Come back tomorrow!"

    show somrak a_idle f_normal with dissolve
    player_name "Y-yes, {b}Master Somrak{/b}..."

    hide masterplayer
    hide somrak
    with dissolve

    call popup ('dex', False)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
