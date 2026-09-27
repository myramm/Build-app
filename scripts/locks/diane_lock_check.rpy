label diane_house_lock_check:

    if M_diane.is_state(S_dia01_find) and destination != L_diane_yard:
        call expression game.dialog_select("diane_need_shovel")

    elif M_diane.is_state(S_dia01_give) and destination != L_diane_garden:
        call expression game.dialog_select("diane_wait_shovel")

    elif M_diane.is_state(S_dia01_work):
        call expression game.dialog_select("diane_work_shovel")

    elif M_diane.is_state(S_dia01_done) and destination != L_diane_yard:
        call expression game.dialog_select("diane_done_shovel")

    elif destination.locked:
        if game.timer.is_dark():
            if destination == L_diane_home:
                call expression game.dialog_select("dianes_front_yard_night_locked")
            else:
                call expression game.dialog_select("night_closed_garden")
        else:

            if destination == L_diane_kitchen:
                call expression game.dialog_select("dianekitchen_locked")

            elif destination == L_diane_home:
                call expression game.dialog_select("dianelobby_locked")

            elif destination == L_diane_shed:
                if M_dewitt.is_state(S_dewitt_shed_get_paint):
                    return
                else:
                    call locked_shed_dialogue

    elif M_diane.is_state(S_diane_check_up_on_garden) and destination == L_diane_home:
        call expression game.dialog_select("diane_check_up_on_garden")

    elif M_diane.is_state(S_diane_look_in_kitchen) and player.location == L_diane_garden and destination == L_diane_kitchen:
        call expression game.dialog_select("dianes_kitchen_locked")

    elif M_diane.is_state(S_diane_seen_cucumber) and destination == L_diane_kitchen:
        call expression game.dialog_select("dianes_kitchen_busy_masturbating")

    elif M_diane.is_state(S_diane_work_on_garden) and (destination == L_diane_home or destination == L_diane_kitchen):
        call expression game.dialog_select("diane_attend_to_garden")

    elif M_diane.is_state(S_diane_delivery_2_task, S_diane_delivery_2_fetch_goods, S_diane_delivery_2) and (destination == L_diane_home or destination == L_diane_kitchen):
        call expression game.dialog_select("diane_tired_from_delivery_upkeep")

    elif M_diane.is_state(S_diane_debbie_drop_off) and destination == L_diane_home and game.timer.is_dark():
        call expression game.dialog_select("diane_debbie_drop_off")

    elif M_diane.is_state(S_diane_check_shed_light) and not destination == L_diane_shed:
        call expression game.dialog_select("diane_shed_light_on")

    elif M_diane.is_state(S_diane_drunken_garden_work) and player.location == L_diane_garden:
        call expression game.dialog_select("diane_day_off_gardening")

    elif M_diane.is_state(S_diane_milking_help) and not (destination == L_diane_garden or destination == L_diane_shed):
        call expression game.dialog_select("diane_milk_jug_pain")

    elif game.timer.is_dark() and (destination == L_diane_home or destination == L_diane_kitchen):
        if destination == L_diane_home:
            call expression game.dialog_select("dianes_front_yard_night_locked")
        else:
            call expression game.dialog_select("night_closed_garden")

    elif M_daisy.is_state(S_daisy_awakened_statue) and destination != L_diane_barn_interior:
        scene expression player.location.background_blur
        show anon f_worried with dissolve
        anon @ -m_talk "( I should {b}follow them into the barn{/b} and learn more. )"

        hide anon with dissolve
    else:

        if destination == L_diane_shed:
            play audio "audio/sfx_door_heavy.ogg"

        elif (not ((player.location == L_diane_kitchen and destination == L_diane_home) or
              (player.location == L_diane_home and destination == L_diane_kitchen) or
              (player.location == L_diane_yard and destination == L_diane_garden) or
              (player.location == L_diane_garden and destination == L_diane_yard))):
            play audio sfxDoor()
        return

    return True

label locked_shed_dialogue:
    if M_diane.finished_state(S_diane_fetch_pump):
        scene garden
        show player 10 at left with dissolve
        player_name "{b}Diane{/b}?"

        show player 5
        diane "Just a second!"

        player_name "..."
        show diane b_shirtless
        show player 11
        player_name "!!!"
        diane "What's the matter, handsome?"

        show player 10
        player_name "Where's your shirt?"

        show player 5
        show diane f_surprised_front a_shock with dissolve
        diane "Hmm?"

        show diane f_thinking_back a_idle with dissolve
        diane "Oh, I took it off because... Well..."

        diane "... It's really hot in there."

        show diane f_normal
        show player 14
        player_name "Yeah, I bet!"

        show player 13
        diane "Apakah Anda memerlukan sesuatu?"

        menu diane_shed_locked_menu:
            "Need any help in there?":
                show player 10 at left
                with dissolve
                player_name "Do you need any help in there?"

                show player 13
                show diane f_laugh
                diane "Hehe, no I've got everything handled."

                show diane f_smirk
                diane "Thanks for the offer though, stud."

                show diane f_normal
                jump diane_shed_locked_menu
            "Tidak ada apa-apa.":

                show player 14 at left
                with dissolve
                player_name "I was just checking on you."

                player_name "It's so quiet in there..."

                show player 13
                show diane f_laugh
                diane "Heh, yeah. I'm just focused."

                diane "Ugh, it's like an oven in there!"

                show diane f_normal
                show player 14
                player_name "You know, you can leave the door open if you want..."

                player_name "That would help with the heat."

                show player 13
                show diane f_thinking_back
                diane "Oh, um..."

                diane "No, that's alright."

                show diane f_laugh
                diane "I work better in private."

                show diane f_normal
                show player 14
                player_name "Hmm, oke."

                player_name "I guess I'll leave you too it."

                show player 13
                diane "Terima kasih, {b}[firstname]{/b}."

                hide player
                hide diane
                with dissolve
    else:

        if M_diane.get("seen_shed_locked"):
            call expression game.dialog_select("dianes_shed_seen_shed_locked")
        else:
            call expression game.dialog_select("dianes_shed_not_seen_shed_locked")
            $ M_diane.set("seen_shed_locked", True)

    return

label dianes_front_yard_night_locked:
    scene expression player.location.background_blur
    show player 10 with dissolve
    player_name "{b}Diane{/b} is probably asleep..."

    hide player with dissolve
    return

label dianes_kitchen_locked:
    scene expression player.location.background_blur
    show player 30 with dissolve
    player_name "Hmm?"

    player_name "It's locked."

    player_name "{b}Diane{/b} never locks this door during the day..."

    show player 34
    player_name "..."
    show player 35
    player_name "I should go try the {b}front door{/b}."

    hide player with dissolve
    return

label dianes_kitchen_busy_masturbating:
    $ M_diane.set("sex speed",0.4)
    show diane_masturbate 1_2
    diane "Ngghhh..."

    diane "Don't stop, stud!"

    pause
    player_name "( I should get out of here before she sees me. )"

    pause
    return

label diane_need_shovel:
    scene expression player.location.background_blur
    show anon with dissolve
    anon @ -m_talk "( Hmm, {b}Diane{/b} needs a new shovel for her garden... )"

    anon @ -m_talk "( I'm pretty sure I saw one hanging up {b}in the garage back home{/b}. )"

    hide anon with dissolve
    return

label diane_wait_shovel:
    scene expression player.location.background_blur
    show anon with dissolve
    anon @ -m_talk "( {b}Diane{/b}'s waiting for me in {b}the garden{/b}. )"

    hide anon with dissolve
    return

label diane_work_shovel:
    scene expression background(464, 456, 4.75)
    show diane a_shovel
    diane "Well, don't be timid {b}[firstname]{/b}."

    show anon with dissolve
    show diane a_shovel_give with dissolve
    diane @ f_laugh "Dig in!"

    show diane a_idle
    show anon a_shovel
    with dissolve
    anon "B-benar."

    anon @ -m_talk "( I can do this! )"

    hide anon with dissolve
    return

label diane_done_shovel:
    scene expression player.location.background_blur
    show anon f_tired with dissolve
    anon @ -m_talk "( No, I'm too worn out for that... )"

    anon @ -m_talk "( I should {b}head home and get some sleep{/b}. )"

    hide anon with dissolve
    return

label diane_check_up_on_garden:
    scene expression player.location.background_blur
    show player 30 with dissolve
    player_name "I should {b}check up on the garden{/b}."

    hide player with dissolve
    return

label diane_attend_to_garden:
    scene expression player.location.background_blur
    show player 79 with dissolve
    player_name "I should {b}get started on the garden{/b}."

    hide player with dissolve
    return

label diane_tired_from_delivery_upkeep:
    scene expression player.location.background_blur
    show player 10 with dissolve
    player_name "I should let her rest..."

    show player 17
    player_name "... Besides, I have a delivery to make!"

    show player 14
    player_name "I should {b}get the package out of Diane's shed and deliver it next door{/b}."

    hide player with dissolve
    return

label diane_debbie_drop_off:
    scene expression player.location.background_blur
    show player 13 with dissolve
    player_name "( ... )"
    pause
    show player 5
    player_name "( Hmm, why isn't she answering the door? )"

    player_name "( Surely she's not still working... )"

    player_name "( ... )"
    player_name "( I'd better {b}check the shed{/b}. )"

    hide player with dissolve
    return

label diane_shed_light_on:
    scene expression player.location.background_blur
    show player 12 with dissolve
    player_name "I need to find {b}Diane{/b}."

    hide player with dissolve
    return

label diane_day_off_gardening:
    scene expression player.location.background_blur
    show player 14 with dissolve
    player_name "I should {b}get started on the garden{/b}."

    hide player with dissolve
    return

label diane_milk_jug_pain:
    scene expression player.location.background_blur
    show player 10 with dissolve
    player_name "Something is wrong with {b}Diane{/b}!"

    player_name "I've gotta {b}check on her in the shed{/b} immediately!"

    hide player with dissolve
    return

label night_closed_garden:
    scene expression player.location.background_blur
    show anon f_worried with dissolve
    if not M_diane.get("breed first time") and not game.timer.is_night():
        anon "{b}Diane{/b} said she would be {b}in the barn{/b}."

    else:
        anon "{b}Diane{/b} is probably asleep... I don't think I can work on the garden right now."

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
