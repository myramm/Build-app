label erik_button_dialogue:
    call erik_button_stage

    if M_anon.is_state(S_ano16_init) and game.timer.is_afternoon():
        call ano16_init_erik
        $ M_anon.trigger(T_ano16_init)

    elif M_anon.is_state(S_ano16_tree):
        call ano16_tree_erik
        $ M_anon.trigger(T_ano16_tree)

    elif M_anon.is_state(S_ano17_erik) and game.timer.is_evening():
        call ano17_erik_erik
        $ M_anon.trigger(T_ano17_erik)
        $ player.go_to(L_erikhouse_basement)

    elif M_anon.is_state(S_ano17_talk):
        call ano17_talk_erik
        $ M_anon.trigger(T_ano17_talk)

    elif M_anon.is_state(S_ano17_porn):
        call ano17_porn_erik
    else:

        if M_bissette.get_state() in [S_bissette_jane_return_books, S_bissette_got_dexters_book,
                                      S_bissette_got_dexters_martinez_books, S_bissette_got_martinez_book,
                                      S_bissette_got_martinez_dexters_books
                                     ] and not M_bissette.is_set("eriks book search"):
            call erik_book_return
            $ M_bissette.set("eriks book search", True)
            $ game.main()

        if player.location == L_erikhouse_erikroom:
            if M_mrsj.is_state(S_mrsj_cupid_date):
                scene expression game.timer.image("erik_house_bedroom{}_b")
                show player 14
                with dissolve
                player_name "Dia terlihat sangat bahagia sekarang."

                show player 17
                player_name "Saya harus {b}memberi tahu Nyonya Johnson kabar baik ini{/b}!"

                hide player with dissolve
                $ game.main()
            scene expression game.timer.image("eriks_room{}_c")

        show old_erik 1 at right
        if player.location == L_school_scienceclassroom:
            show old_erikl 1f at right
        show player 2 at left
        with dissolve
        player_name "Hai {b}Erik{/b}!"

        show player 1 at left
        show old_erik 5 at right
        erik "Hai {b}[firstname]{/b}! Ada apa?"

        label erik_talk:
            menu:
                "Tugas Kafetaria." if L_school_cafeteria.is_here(M_erik) and M_kevin.finished_state(S_kevin_gym_tomorrow):
                    call erik_cafeteria_duty

                "Lensa." if M_okita.is_state(S_okita_get_bifocal_lenses):
                    call expression game.dialog_select("button_erik_lenses")

                "Tuan Peledakan." if M_okita.is_state(S_okita_get_controller_info):
                    call expression game.dialog_select("button_erik_master_blaster")
                    $ M_okita.trigger(T_okita_got_master_blaster_info)

                "Tuan Peledakan." if M_okita.is_state(S_okita_get_controller):
                    call expression game.dialog_select("button_erik_master_blaster_again")

                "seruling." if M_dewitt.is_state(S_dewitt_make_new_flute):
                    call expression game.dialog_select("button_erik_make_flute")

                "Pertunjukan bakat." if M_dewitt.is_set("talent ask erik"):
                    if M_dewitt.is_set("talent helping kevin"):
                        call expression game.dialog_select("dewitt_talent_show_helping_kevin")

                    elif M_dewitt.is_set("talent helping eve"):
                        call expression game.dialog_select("dewitt_talent_show_helping_eve")
                    else:

                        call expression game.dialog_select("button_erik_talent_show")
                        $ M_dewitt.set("talent ask erik", False)

                "Gitar." if M_dewitt.is_state([S_dewitt_erik_borrow_guitar, S_dewitt_garage_find_paint, S_dewitt_ask_deb_paint, S_dewitt_ask_diane_paint, S_dewitt_shed_get_paint, S_dewitt_make_replacement_guitar]):
                    if M_dewitt.is_state(S_dewitt_erik_borrow_guitar):
                        call expression game.dialog_select("button_erik_borrow_guitar")
                        if not L_diane_shed.locked:
                            $ M_dewitt.trigger(T_dewitt_eriks_agreement_shed)
                        else:
                            $ M_dewitt.trigger(T_dewitt_eriks_agreement_no_shed)
                    else:

                        call expression game.dialog_select("button_erik_make_guitar")
                        if not L_diane_shed.locked:
                            $ M_dewitt.trigger(T_dewitt_eriks_agreement_shed)
                        else:
                            $ M_dewitt.trigger(T_dewitt_eriks_agreement_no_shed)

                "Bir." if M_dewitt.is_state([S_dewitt_erik_get_beer, S_dewitt_clean_graffiti]) and not player.has_item("beer"):
                    call expression game.dialog_select("button_erik_ask_beer")
                    $ M_dewitt.trigger(T_dewitt_erik_deal)

                "Minuman untuk {b}Roxxy{/b}." if M_roxxy.get("talked to roxxy booze"):
                    call expression game.dialog_select("button_erik_talked_to_roxxy_booze")
                    $ M_roxxy.trigger(T_roxxy_get_beer)

                "Buku perpustakaan." if M_bissette.is_set("eriks book search"):
                    call erik_book_return

                "Butuh bantuan Anda." if M_dewitt.is_state(S_dewitt_school_sneak_mission_help):
                    call expression game.dialog_select("button_erik_school_sneak_mission_help")
                    $ M_dewitt.trigger(T_dewitt_erik_deal)

                "Model." if M_ross.is_state(S_ross_ask_model):
                    call expression game.dialog_select("button_erik_ask_model")

                "Kartu-kartu." if M_erik.is_state(S_erik_cards_lost):
                    call expression game.dialog_select("erik_cards_prompt")

                "Kartu-kartu." if M_erik.is_state(S_erik_cards_found):
                    call expression game.dialog_select("erik_cards_found")
                    $ player.remove_item("eriks_cards")
                    $ M_erik.trigger(T_erik_cards_return)
                    if player.has_item('card02'):
                        jump erik_card_done

                "Ayam Mahkota Duri." if M_erik.is_state(S_erik_card_needed):
                    call erik_card_prompt

                "Ayam Mahkota Duri." if M_erik.is_state(S_erik_card_acquired):
                    call erik_card_present
                    label erik_card_done:
                    $ player.remove_item("card02")
                    $ player.get_item("card03")
                    $ M_erik.trigger(T_erik_card_given)

                "Turnamen." if M_erik.is_state(S_erik_card_done):
                    call erik_card_epilogue

                "Turnamen." if M_erik.finished_state(S_erik_card_done) and not M_erik.get('card_outcome'):
                    call erik_card_outcome
                    $ M_erik.set('card_outcome', True)

                "Paketnya." if M_erik.is_state(S_erik_orc_order):
                    call erik_orc_prompt

                "Paketnya." if M_erik.is_state(S_erik_orc_wait):
                    call erik_orc_ordered

                "Paketnya." if M_erik.is_state(S_erik_orc_arrived):
                    call erik_orc_arrived

                "Paketnya." if M_erik.between_states(S_erik_orc_acquired, S_erik_orc_inspected) and player.location != L_erikhouse_erikroom:
                    call erik_orc_awkward

                "Paketnya." if M_erik.is_state(S_erik_orc_inspected) and player.location == L_erikhouse_erikroom:
                    call erik_orc_present
                    $ M_erik.trigger(T_erik_orc_given)
                    $ player.go_to(L_erikhouse_entrance)

                "Headset VR." if M_erik.is_state(S_erik_vr_needed, S_erik_vr_buy_headset, S_erik_vr_buy_game):
                    call erik_vr_prompt

                "Headset VR." if M_erik.is_state(S_erik_vr_acquired):
                    call erik_vr_present
                    label erik_vr_done:
                    $ player.remove_item("game02")
                    $ player.remove_item("virtualsaga")
                    $ M_erik.trigger(T_erik_vr_given)

                "Pesan dari {b}Bpk. Johnson{/b}." if M_larry.is_state(S_larry_msg_sorry):
                    call expression game.dialog_select("button_erik_message_from_dad")
                    $ M_larry.trigger(T_larry_msg_relayed)

                "Poker." if M_erik.is_state(S_erik_poker_invite):
                    call erik_poker_prompt

                "{b}Ny. Johnson{/b}." if M_erik.between_states(S_erik_feed_search, S_erik_poker_done):
                    call erik_feed_react

                "{b}Ny. Johnson{/b}." if M_erik.is_state(S_erik_fork_ready, S_erik_fork_talk):
                    if L_erikhouse_erikroom.is_here(M_erik):
                        call erik_fork_talk
                        $ M_erik.trigger(T_erik_fork_feedback)
                    else:
                        call erik_fork_talk_public

                "{b}Ny. Johnson{/b}." if M_erik.is_state(S_erik_fork_choice):
                    call expression game.dialog_select("erik_fork_talk_prompt")
                    jump erik_talk

                "{b}Ny. Johnson{/b}." if M_erik.between_states(S_erik_fork_done, S_erik_learn_ready):
                    call erik_learn_preamble
                    $ M_erik.once('learn_limbo')

                "Pendidikan seks." if M_erik.between_states(S_erik_learn_fetch, S_erik_learn_acquired):
                    call expression game.dialog_select("erik_learn_fetch_prompt")

                "Pacar perempuan." if M_mrsj.is_state(S_mrsj_fork_meet):
                    call expression game.dialog_select("erik_mrsj_fork_prompt")
                    jump erik_talk

                "Pacar perempuan." if M_mrsj.is_state(S_mrsj_cupid_ready):
                    call expression game.dialog_select("erik_mrsj_cupid_intro")
                    $ M_mrsj.trigger(T_mrsj_cupid_tell)

                "Saya butuh bantuan." if M_kevin.is_state(S_kevin_convince_erik):
                    $ M_kevin.trigger(T_kevin_eriks_demand)
                    call expression game.dialog_select("button_erik_ask_favor")
                    if M_kevin.is_state(S_kevin_bribe_erik):
                        $ player.remove_item("game")
                        $ M_kevin.trigger(T_kevin_bribed_erik)
                    jump erik_talk

                "Permainan apa yang kamu inginkan?" if M_kevin.is_state(S_kevin_get_seadogs):
                    call expression game.dialog_select("button_erik_ask_favor_repeat")
                    jump erik_talk

                "Saya punya permainannya!" if M_kevin.is_state(S_kevin_bribe_erik):
                    call expression game.dialog_select("button_erik_favor_completed")
                    $ player.remove_item("game")
                    $ M_kevin.trigger(T_kevin_bribed_erik)
                    jump erik_talk
                "Dimana {b}Ny. Johnson{/b}?":

                    call expression game.dialog_select("button_erik_where_is_mrsj")
                "Tidak banyak.":

                    call expression game.dialog_select("button_erik_not_much")

                "Saya butuh bantuan." if False:
                    call expression game.dialog_select("button_erik_webcam_help")
                    $ M_erik.set("webcam help", True)
        hide old_erikl

    $ game.main()
    return


label erik_button_stage:
    if L_treehouse.is_here(M_erik):
        scene expression background(888, 592, 5.4468) as stage

    elif L_treehouse_interior.is_here(M_erik):
        scene location_treehouse_floor_day
    else:

        scene expression player.location.background_closeup

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
