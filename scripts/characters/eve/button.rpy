label eve_button_dialogue:
    if M_eve.pregnancy:
        jump eve_preg_button_dialogue

    scene expression player.location.background_closeup

    if game.timer.is_weekend() and game.timer.is_morning() and player.location == L_tattooparlor_bedroom:
        if M_eve.pregnancy.stage > 1 or not M_eve.finished_state(S_eve_sexy_time):
            call eveX1_lewd.fail
        else:
            call eveX1_lewd
            $ game.timer.tick()
            $ M_eve.move(L_tattooparlor_bathroom)
        $ game.main()

    elif L_tattooparlor_bathroom.is_here(M_eve) and M_eve.finished_state(S_eve_sexy_time):
        call eveX2_bath_eve
        $ M_eve.set('shower', True)
        $ player.go_to(L_tattooparlor_fire_escape)
        $ game.timer.tick(3)

    elif M_roxxy.is_state(S_roxxy_meeting_buyer) and player.location == L_park and game.timer.is_evening():
        call eve_button_heisenberg
        $ game.main()
    elif M_eve.is_state(S_eve_pranking_douches) and player.location == L_park and game.timer.is_evening():
        call expression game.dialog_select("eve_button_prank_douches_park")
        $ M_eve.trigger(T_eve_douches_prank_plan)
        $ game.main()
    elif M_eve.is_state(S_eve_police_trouble) and game.timer.is_dark():
        call expression game.dialog_select("eve_button_police_trouble")
        $ M_eve.trigger(T_eve_police_trouble_resolved)
        $ game.timer.tick()
        $ player.go_to(L_map)
        $ game.main()
    elif M_eve.is_state(S_eve_park_hangout) and L_park.is_here(M_eve):
        call expression game.dialog_select("eve_button_park_hangout")
        $ M_eve.trigger(T_eve_bullied_by_douches)
    elif M_eve.is_state(S_eve_ross_argument) and game.timer.is_day():
        call expression game.dialog_select("eve_button_ross_argument")
        $ M_eve.trigger(T_eve_ross_argument)
    elif M_eve.is_state(S_eve_auditorium_bummed) and game.timer.is_day() and L_school_assemblyhall.is_here(M_eve):
        call expression game.dialog_select("eve_button_auditorium_bummed")
        $ M_eve.trigger(T_eve_auditorium_bummed)
        $ game.timer.tick()
    elif M_eve.is_state(S_eve_roxxy_bullying_upset) and game.timer.is_day() and L_school_assemblyhall.is_here(M_eve):
        call expression game.dialog_select("eve_button_roxxy_bullying_upset")
        $ M_eve.trigger(T_eve_dress_code_change)
        $ player.go_to(L_school_righthallway)
        $ game.main()
    elif M_eve.is_state(S_eve_school_dress_code):
        call expression game.dialog_select("eve_button_school_dress_code")
        $ game.main()
    elif M_eve.is_state(S_eve_dress_code_ask_teachers):
        call expression game.dialog_select("eve_button_dress_code_ask_teachers")
    elif M_eve.is_state(S_eve_bridgets_help) and game.timer.is_day():
        call expression game.dialog_select("eve_button_bridgets_help")
        $ M_eve.trigger(T_eve_announced_bridget_help)
        $ player.go_to(L_map)
        $ game.main()
    elif M_eve.is_state(S_eve_pranking_roxxy) and game.timer.is_day():
        call expression game.dialog_select("eve_button_prank_roxxy")
        $ M_eve.trigger(T_eve_pranked_roxxy)
        $ player.go_to(L_school_lefthallway)
        $ game.main()
    elif M_eve.is_state(S_eve_pranking_douches) and L_school_front.is_in_children(M_eve):
        call expression game.dialog_select("eve_button_prank_douches_school")
    elif M_eve.is_state(S_eve_voyeurism_start) and L_school_front.is_in_children(M_eve):
        call expression game.dialog_select("eve_button_voyeurism_start")
        $ M_eve.trigger(T_eve_voyeurism_meetup)
    elif M_eve.is_state(S_eve_voyeurism_meetup) and L_school_front.is_in_children(M_eve):
        call expression game.dialog_select("eve_button_voyeurism_meetup")
    elif M_eve.is_state(S_eve_voyeurism_follow_roof) and player.location == L_tattooparlor_roof:
        call screen popup_branch
        if not _return:
            $ game.main()
        call expression game.dialog_select("eve_button_voyeurism_follow_roof")
        $ M_eve.trigger(T_eve_voyeurism_follow_tent)
    elif M_eve.is_state(S_eve_detention) and L_school_front.is_in_children(M_eve):
        call expression game.dialog_select("eve_button_detention")
        $ M_eve.trigger(T_eve_got_detention)
        $ player.go_to(L_map)
        $ game.main()
    elif M_eve.is_state(S_eve_bike_breakdown_start) and L_school_front.is_in_children(M_eve):
        call expression game.dialog_select("eve_button_bike_breakdown_start")
        $ M_eve.trigger(T_eve_bike_breakdown_started)
        $ game.main()
    elif M_eve.is_state(S_eve_bike_breakdown_check_bike, S_eve_bike_breakdown_repair, S_eve_bike_breakdown_repair_again) and L_school_front.is_in_children(M_eve):
        call expression game.dialog_select("eve_button_bike_breakdown_started")
    elif M_eve.is_state(S_eve_talk_to_girls, S_eve_talked_to_grace):
        call expression game.dialog_select("eve_button_eve_talk_to_girls")
        if M_eve.is_state(S_eve_talked_to_grace):
            call expression game.dialog_select("eve_button_eve_talked_to_both_girls")
            $ game.timer.tick(3)
            $ player.go_to(L_map)
        hide anon with dissolve
        $ M_eve.trigger(T_eve_talked_to_eve)
        $ game.main()
    elif M_eve.is_state(S_eve_talked_to_eve):
        call expression game.dialog_select("eve_button_talked_to_eve")
        $ game.main()
    elif M_eve.is_state(S_eve_six6nine9_time) and player.location == L_tattooparlor_bedroom and game.timer.is_evening():
        call expression game.dialog_select("eve_button_eve_six6nine9_time")
        menu:
            "I'll do it.":
                anon "I'll do it."
                eve "You will?"
                anon "Sure."
                eve "Hehe, okay!"
                jump eve_69
            "Nah, I don't want to.":

                anon "Nah, I don't want to."
                eve f_thinking_down "O-oh, okay."
                pause
                anon "Sorry, I just don't think I'm ready for that."
                eve "No, it's fine... I get it."
                eve "We'll just stick to hand stuff."
                anon "Come here!"
                eve f_happy @ -m_talk "!!!"
                jump eve_handjob
    elif M_eve.is_state(S_eve_sexy_time) and player.location == L_tattooparlor_bedroom and game.timer.is_evening():
        $ M_eve.trigger(T_eve_had_sexy_time)
        call expression game.dialog_select("button_eve_sexy_time")
    else:
        if player.location == L_school_frenchclassroom:
            if M_eve.between_states(S_eve_start, S_eve_pot_cheerup):
                call expression game.dialog_select("eve_dialogue_intro_classroom_e1e12")
            elif M_eve.between_states(S_eve_pot_cheerup, S_eve_make_up_dress_table):
                call expression game.dialog_select("eve_dialogue_intro_classroom_e13e20")
            else:
                call expression game.dialog_select("eve_dialogue_intro_classroom_e21")
        elif player.location in (L_school_righthallway, L_school_lefthallway):
            if M_eve.between_states(S_eve_start, S_eve_pot_cheerup):
                call expression game.dialog_select("eve_dialogue_intro_hallway_e1e12")
            elif M_eve.between_states(S_eve_pot_cheerup, S_eve_make_up_dress_table):
                call expression game.dialog_select("eve_dialogue_intro_hallway_e13e20")
            else:
                call expression game.dialog_select("eve_dialogue_intro_hallway_e21")
        elif player.location == L_park:
            call expression game.dialog_select("eve_dialogue_intro_park_e1e12")
        elif player.location == L_tattooparlor_bedroom:
            call expression game.dialog_select("eve_dialogue_intro_bedroom")
        elif player.location == L_tattooparlor_roof:
            call expression game.dialog_select("eve_dialogue_intro_roof")


        menu eve_button_menu:
            "Talent show." if M_dewitt.is_state([S_dewitt_talent_show_ask, S_dewitt_talent_show_ask_eve]) or M_dewitt.is_set("talent helping kevin") and player.location == L_school_frenchclassroom:
                if M_dewitt.is_set("talent helping kevin"):
                    call expression game.dialog_select("dewitt_talent_show_helping_kevin")

                elif player.location == L_school_frenchclassroom:
                    call expression game.dialog_select("eve_classroom_dialogue_talent_show_help")
                    $ M_dewitt.trigger(T_dewitt_eves_agreement)
                else:
                    call expression game.dialog_select("button_eve_talent_show_help")
                    $ M_dewitt.trigger(T_dewitt_eves_agreement)

            "Adhesive." if M_dewitt.is_state(S_dewitt_science_adhesive) and player.location == L_school_frenchclassroom:
                call expression game.dialog_select("eve_classroom_dialogue_adehsive")

            "{b}Miss Bissette{/b}'s reward." if player.location == L_school_frenchclassroom:
                call expression game.dialog_select("eve_classroom_dialogue_bissettes_reward")
                jump eve_button_menu

            "Party." if M_eve.is_state(S_eve_party_start) and game.timer.is_weekday() and player.location == L_school_frenchclassroom:
                call expression game.dialog_select("eve_button_party_start")
                jump eve_button_menu

            "The crypt?" if M_odette.finished_state(S_ode02_warn):
                call eve_button_crypt
                jump eve_button_menu

            "Hang out." if player.location == L_school_frenchclassroom:
                call expression game.dialog_select("eve_classroom_dialogue_hang_out")
                jump eve_button_menu

            "Art Pad." if M_ross.is_state(S_ross_find_art_pad) and player.location == L_school_righthallway:
                call expression game.dialog_select("button_eve_ross_find_art_pad")
                $ M_ross.trigger(T_ross_find_eve_backpack)
                jump eve_button_menu

            "Backpack." if M_ross.is_state(S_ross_find_eve_backpack) and player.location == L_school_righthallway:
                if player.has_item("eve_backpack"):
                    call expression game.dialog_select("button_eve_ross_find_eve_backpack_have_backpack")
                    $ player.remove_item("eve_backpack")
                    $ M_ross.trigger(T_ross_got_eve_backpack)
                else:

                    call expression game.dialog_select("button_eve_ross_find_eve_backpack_no_backpack")
                jump eve_button_menu

            "Drawing." if M_ross.is_state(S_ross_get_eve_drawing) and player.location == L_school_righthallway:
                call expression game.dialog_select("button_eve_ross_get_eve_drawing")
                jump eve_button_menu

            "Model." if M_ross.is_state(S_ross_ask_model) and player.location == L_school_righthallway:
                call expression game.dialog_select("button_eve_ask_model")
                jump eve_button_menu

            "Paint." if M_ross.is_state(S_ross_get_paint) and player.location == L_school_righthallway:
                call expression game.dialog_select("button_eve_ross_get_paint")
                $ L_tattooparlor.unlock()
                $ M_ross.trigger(T_ross_talk_to_grace)
                jump eve_button_menu

            "Paint." if M_ross.is_state(S_ross_get_paint_grace) and player.location == L_school_righthallway:
                call expression game.dialog_select("button_eve_ross_get_paint_grace")
                jump eve_button_menu

            "Love the hair!" if player.location == L_school_frenchclassroom:
                call expression game.dialog_select("button_eve_love_the_hair")
                jump eve_button_menu

            "You look nice today!" if player.location == L_school_frenchclassroom and M_eve.between_states(S_eve_pot_cheerup, S_eve_make_up_dress_table):
                call expression game.dialog_select("button_eve_you_look_nice_today")
                jump eve_button_menu

            "Something simple?" if player.location in (L_school_lefthallway, L_school_righthallway) and M_eve.between_states(S_eve_pot_cheerup, S_eve_make_up_dress_table):
                call expression game.dialog_select("button_eve_something_simple")
                jump eve_button_menu

            "How come you're not at the park?" if player.location == L_tattooparlor_roof and M_eve.between_states(S_eve_pot_cheerup, S_eve_make_up_dress_table):
                call expression game.dialog_select("button_eve_how_come_not_at_the_park")
                jump eve_button_menu

            "How's everyone at home?" if player.location in (L_school_frenchclassroom, L_school_lefthallway, L_school_righthallway) and M_eve.between_states(S_eve_pot_cheerup, S_eve_make_up_dress_table):
                call expression game.dialog_select("button_eve_hows_everyone_at_home")
                jump eve_button_menu

            "Art Project." if player.location in (L_school_frenchclassroom, L_school_lefthallway, L_school_righthallway, L_tattooparlor_roof) and M_eve.between_states(S_eve_detention, S_eve_make_up_dress_table):
                call expression game.dialog_select("button_eve_art_project")
                jump eve_button_menu

            "Business doing any better?" if player.location in (L_school_frenchclassroom, L_school_lefthallway, L_school_righthallway, L_tattooparlor_roof) and M_eve.between_states(S_eve_clients_take_care_clients, S_eve_make_up_dress_table):
                call expression game.dialog_select("button_eve_business_doing_any_better")
                jump eve_button_menu

            "How are {b}Odette{/b} and {b}Grace{/b}?" if player.location in (L_school_frenchclassroom, L_school_lefthallway, L_school_righthallway) and M_eve.finished_state(S_eve_make_up_dress_table):
                call expression game.dialog_select("button_eve_how_are_odette_and_grace")
                jump eve_button_menu

            "I'll be there." if player.location in (L_school_lefthallway, L_school_righthallway) and M_eve.finished_state(S_eve_make_up_dress_table):
                call expression game.dialog_select("button_eve_ill_be_there")
                jump eve_button_menu

            "Really?" if player.location in (L_school_righthallway, L_school_lefthallway) and M_eve.between_states(S_eve_start, S_eve_pot_cheerup):
                call expression game.dialog_select("button_eve_hallway_really")
                jump eve_button_menu

            "You should find a new spot?" if player.location == L_park:
                call expression game.dialog_select("button_eve_should_find_a_new_spot")
                jump eve_button_menu

            "You still drawing?" if player.location in (L_school_frenchclassroom, L_school_righthallway, L_school_lefthallway) and M_eve.between_states(S_eve_park_hangout, S_eve_pot_cheerup):
                call expression game.dialog_select("button_eve_you_still_drawing")
                jump eve_button_menu

            "{i}Street Kombat{/i} rematch!" if player.location in (L_school_frenchclassroom, L_school_righthallway, L_school_lefthallway) and M_eve.between_states(S_eve_visit_bedroom, S_eve_pot_cheerup):
                call expression game.dialog_select("button_eve_street_kombat_rematch")
                jump eve_button_menu

            "How are things at the shop?" if player.location in (L_school_frenchclassroom, L_school_righthallway, L_school_lefthallway) and M_eve.between_states(S_eve_visit_bedroom, S_eve_pot_cheerup):
                call expression game.dialog_select("button_eve_how_are_things_at_the_shop")
                jump eve_button_menu

            "Fool around." if player.location in (L_tattooparlor_bedroom, L_tattooparlor_roof) and M_eve.finished_state(S_eve_six6nine9_time):
                if player.location == L_tattooparlor_roof:
                    $ player.go_to(L_tattooparlor_tent)
                call expression game.dialog_select("button_eve_fool_around")

            "Shower?" if player.location in (L_tattooparlor_bedroom, L_tattooparlor_roof) and M_eve.shower:
                call eveX2_post_eve
                $ game.timer.tick()
                $ player.go_to(L_tattooparlor_fire_escape)








            "Maybe another time." if player.location in (L_school_frenchclassroom, L_school_lefthallway, L_school_righthallway) and M_eve.finished_state(S_eve_make_up_dress_table):
                call expression game.dialog_select("button_eve_maybe_another_time")
                jump eve_button_menu

            "Never mind." if player.location in (L_school_frenchclassroom, L_school_righthallway, L_school_lefthallway):
                call expression game.dialog_select("button_eve_nevermind_school")

            "Never mind." if player.location == L_park:
                call expression game.dialog_select("button_eve_nevermind_park")

            "Never mind." if player.location == L_tattooparlor_roof:
                call expression game.dialog_select("button_eve_nevermind_roof")

            "Actually, I should go." if player.location == L_tattooparlor_bedroom:
                call expression game.dialog_select("button_eve_i_should_go")
    $ game.main()


label button_eve_fool_around:
    anon f_flirt "You wanna mess around a little?"
    eve f_sexy "Definitely!"
    pause
    if player.location == L_tattooparlor_tent:
        eve "Follow me into the tent."
    else:
        eve "Come lay on the bed."

    anon "Okay."
    if player.location == L_tattooparlor_tent:
        scene expression player.location.background_blur with None
        show eve b_onbed_dressed f_sexy
    else:
        scene expression player.location.background_closeup with None
        show eve b_onbed_tanktop f_sexy
    show anon b_onbed_sit f_flirt
    with dissolve
    eve "I should probably take off these clothes, huh?"
    anon @ -m_talk "Mmhmm."
    eve @ f_laugh "Hehe!"
    if player.location == L_tattooparlor_tent:
        show eve f_normal_down b_onbed_topless a_remove2 with dissolve
        pause
        show eve b_onbed_tanktop_remove1 with dissolve
        pause
        show eve b_onbed_tanktop_remove2 with dissolve
        pause
    show eve b_onbed_top_remove3 with dissolve
    pause
    show eve b_onbed_top_remove4 with dissolve
    pause
    show eve f_sexy b_onbed_nude with dissolve
    eve "You like?"
    anon "Oh, me like!"
    eve @ f_laugh "Hehe, your turn!"
    show anon b_onbed_sit_changing3 with fastdissolve
    pause .5
    hide anon
    show eve b_onbed_cuddle_naked_kiss o_dick a_idle
    with dissolve
    anon "!!!"
    eve "Mmm."
    pause
    show eve b_onbed_cuddle_naked f_happy
    show anon b_empty_eve_onbed_cuddle f_flirt_low zorder 1
    with dissolve
    pause
    eve "So, here we are again..."
    $ M_eve.set('sex speed', .4)
    show eve a_jerk o_empty with dissolve
    anon "Mmhmm."
    pause
    eve "What did you have in mind?"
    menu:
        "Handjob.":
            jump eve_handjob
        "Sixty-nine.":

            eve "You wanna sixty-nine again?"
            anon "Sure."
            eve "I wasn't sure if you liked it the first time..."
            anon "Well, wonder no more."
            eve "Hehe!"
            jump eve_69
        "Let's just cuddle for a while.":

            anon "Let's just cuddle for a while."
            eve a_chest o_dick "Oh, I'm down for that!"
            eve f_happy_closed "I love it when you hold me like this..."
            anon "Yeah, me too."
            jump eve_HJ_end

        "Sex." if M_eve.is_state(S_eve_end):
            anon "Sex, please!"
            eve "Mmm, I was hoping you'd say that!"
            eve "How do you want me?"
            menu:
                "Top!":
                    jump eve_sex_front_intro
                "Bottom!":

                    jump eve_sex_back_intro
    return


init python:
    def eve_preg_label(label):
        label = 'eve_preg_stage_{}_{}'.format(M_eve.pregnancy.stage, label)
        if renpy.has_label(label):
            return label


label eve_preg_button_dialogue:
    if M_eve.pregnancy.character_bedridden:
        jump eve_preg_stage_5_bedridden

    if L_tattooparlor_bathroom.is_here(M_eve):
        jump eve_preg_stage_4_bathroom

    call expression eve_preg_label('intro')
    menu eve_preg_menu:
        "How are you feeling?" if eve_preg_label('feeling'):
            call expression eve_preg_label('feeling')

        "Doctor's visit." if eve_preg_label('doctor'):
            call expression eve_preg_label('doctor')

        "{b}Grace{/b}." if eve_preg_label('grace'):
            call expression eve_preg_label('grace')

        "What's that you're singing?" if eve_preg_label('singing'):
            call expression eve_preg_label('singing')

        "Can I get you anything?" if eve_preg_label('anything'):
            call expression eve_preg_label('anything')

        "I'll leave you to it then." if M_eve.pregnancy.stage <= 4:
            call expression eve_preg_label('leave')
            $ game.main()

        "I'll leave you be." if M_eve.pregnancy.stage > 4:
            call expression eve_preg_label('leave')
            $ game.main()

    jump eve_preg_menu
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
