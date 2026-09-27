label mrsj_button_dialogue:
    if player.location == L_erikhouse_entrance:
        scene expression game.timer.image("erik_entrance{}_c")

    elif player.location == L_erikhouse_mrsjroom:
        if game.timer.is_dark() and M_erik.finished_state(S_erik_learn_prep):
            call expression game.dialog_select("button_mrsj_sex_ed_intro")
            jump mrsj_button_dialogue_repeat

        elif game.timer.is_dark() and M_mrsj.finished_state(S_mrsj_cupid_report):
            call expression game.dialog_select("button_mrsj_private_yoga_intro")
            jump mrsj_button_dialogue_repeat

        scene erik_house_upstairs_night_c01

    call expression game.dialog_select("button_mrsj_greetings")
    menu mrsj_button_dialogue_repeat:
        "Apa yang perlu saya lakukan?" if M_mrsj.is_state(S_mrsj_yoga_class, S_mrsj_yoga_retry):
            call expression game.dialog_select("button_mrsj_yoga_help_repeat")

        "Menyusui." if M_erik.between_states(S_erik_feed_done, S_erik_fork_choice):
            call expression game.dialog_select("button_mrsj_breastfeeding")

        "Tentang {b}Erik{/b}..." if M_erik.is_state(S_erik_fork_choice):
            call screen popup_branch
            if not _return:
                jump mrsj_button_dialogue_repeat
            call mrsj_erik_fork
            menu:
                "Pendidikan seks.":
                    call mrsj_erik_fork_teach
                    $ M_erik.trigger(T_erik_fork_teach)
                "Carikan dia pacar.":

                    call mrsj_erik_fork_match
                    $ M_erik.trigger(T_erik_fork_match)

        "Pendidikan seks." if M_erik.between_states(S_erik_learn_fetch, S_erik_learn_acquired):
            call expression game.dialog_select("button_mrsj_erik_learn_fetch_prompt")




        "Pendidikan seks." if (M_erik.finished_state(S_erik_learn_prep) and
                             game.timer.is_dark() and
                             player.location is L_erikhouse_mrsjroom):
            jump mrsj_3some

        "Pacar perempuan." if M_mrsj.is_state(S_mrsj_fork_meet):
            call expression game.dialog_select("button_mrsj_erik_introduce_june")
            jump mrsj_button_dialogue_repeat

        "Pacar perempuan." if M_mrsj.is_state(S_mrsj_cupid_report):
            call expression game.dialog_select("button_mrsj_erik_got_gf")
            $ M_mrsj.trigger(T_mrsj_cupid_news)
            if game.timer.is_dark():
                call mrsjroom_mrsj_private_yoga_shortcircuit
                jump mrsj_private_yoga

        "Yoga pribadi." if game.timer.is_dark() and M_mrsj.finished_state(S_mrsj_cupid_report):
            call mrsjroom_mrsj_private_yoga_intro
            jump mrsj_private_yoga

        "Dimana {b}Erik{/b}?" if not game.timer.is_dark():
            show player 14
            if game.timer.is_morning() and not game.timer.is_weekend():
                player_name "Tahukah Anda di mana saya bisa menemukan {b}Erik{/b}?"

                show player 1
                show mrsj 17
                mrsj "Yah, dia seharusnya berada di {b}sekolah{/b} sekarang."

            else:

                show mrsj 14
                player_name "Tahukah Anda di mana saya bisa menemukan {b}Erik{/b}?"

                show player 1
                show mrsj 17
                mrsj "Yah, sepertinya aku melihatnya masuk ke {b}ruang bawah tanah{/b}."

                mrsj "Jika dia tidak di bawah sana, dia mungkin ada di kamarnya."

                show mrsj 14
                show player 17
                player_name "Terima kasih, {b}Ny. Johnson{/b}!"

            show mrsj 14
            jump mrsj_button_dialogue_repeat

        "Undang ke poker." if (M_erik.finished_state(S_erik_poker_ready) and
                               L_erikhouse_mrsjroom.is_here(M_mrsj) and
                               M_erik.where in (L_erikhouse_erikroom,
                                                L_erikhouse_basement)):
            if player.stats.chr() < 5:
                $ display.toast(chr_fail)
                call mrsj_erik_poker_invite_fail

            elif game.timer.is_day():
                call mrsj_erik_poker_invite_early
            else:

                if M_erik.finished_state(S_erik_poker_invite):
                    call mrsj_erik_poker_invite_repeat
                else:
                    $ display.toast(chr_pass)
                    call mrsj_erik_poker_invite_pass
                $ player.go_to(L_erikhouse_basement)
                call poker_mrsj
                if _return:
                    python:
                        M_erik.trigger(T_erik_poker_win)
                        M_mrsj.set('poker_after_party', True)
                else:
                    jump resume_sleeping_bedroom

        "Kamu sangat bugar!" if not L_erikhouse_mrsjroom.is_here(M_mrsj):
            call expression game.dialog_select("button_mrsj_youre_so_fit")
            jump mrsj_button_dialogue_repeat
        "Saya harus pergi!":

            call expression game.dialog_select("button_mrsj_leave")

    hide player
    hide old_erik
    hide mrsj
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
