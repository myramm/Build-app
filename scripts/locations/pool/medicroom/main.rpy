label medic_room_dialogue:
    $ player.go_to(L_pool_medicroom)
    scene expression player.location.background

    if M_cassie.is_state(S_cassie_medic_room) and not M_cassie.get("had sex"):
        label medic_room_cassie_replay:
            if not store._in_replay is None:
                $ player.go_to(L_pool_medicroom)
                scene expression player.location.background
            call expression game.dialog_select("medic_room_dialogue_count_0")
        menu:
            "Ok, let's try it.":
                call expression game.dialog_select("medic_room_dialogue_count_0_lets_try")
                $ M_cassie.set("had sex", True)
                jump expression game.dialog_select("gloryhole_medic")

            "I don't feel like it." if store._in_replay is None:
                call expression game.dialog_select("medic_room_dialogue_count_0_do_not_feel_like_it")

    elif M_cassie.is_state(S_cassie_medic_room) and M_cassie.get("had sex"):
        call expression game.dialog_select("medic_room_dialogue_count_1")
        $ renpy.end_replay()
        $ persistent.cookie_jar["Cassie"]["unlocked"] = True
        $ persistent.cookie_jar["Cassie"]["gallery"]["01_unlocked"] = True
        call popup ('area', L_pool_medicroom)

    elif M_cassie.is_state(S_cassie_end) and not M_cassie.get("had sex"):
        call expression game.dialog_select("medic_room_dialogue_count_2")
        menu:
            "I'd love to.":
                call expression game.dialog_select("medic_room_dialogue_count_2_love_to")
                $ M_cassie.set("had sex", True)
                jump expression game.dialog_select("gloryhole_medic")
            "Just changing.":

                call expression game.dialog_select("medic_room_dialogue_count_2_just_changing")
                if wearing_swimsuit:
                    $ wearing_swimsuit = False
                    $ changing_count = 0
                else:

                    $ wearing_swimsuit = True
                $ used_changing_girls = []
    else:

        call expression game.dialog_select("medic_room_dialogue_count_finished")
        $ M_cassie.set("had sex", False)

    $ game.main()
    return


label medic_room_toolbag:
    call medic_room_toolbag_dialogue
    $ player.get_item('toolbag')
    call popup ('give', 'toolbag')
    $ M_anon.trigger(T_ano07_find)

    $ game.main()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
