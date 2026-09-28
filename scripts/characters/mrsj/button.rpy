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
        "What did you need me to do?" if M_mrsj.is_state(S_mrsj_yoga_class, S_mrsj_yoga_retry):
            call expression game.dialog_select("button_mrsj_yoga_help_repeat")

        "Breastfeeding." if M_erik.between_states(S_erik_feed_done, S_erik_fork_choice):
            call expression game.dialog_select("button_mrsj_breastfeeding")

        "About {b}Erik{/b}..." if M_erik.is_state(S_erik_fork_choice):
            call screen popup_branch
            if not _return:
                jump mrsj_button_dialogue_repeat
            call mrsj_erik_fork
            menu:
                "Sex education.":
                    call mrsj_erik_fork_teach
                    $ M_erik.trigger(T_erik_fork_teach)
                "Get him a girlfriend.":

                    call mrsj_erik_fork_match
                    $ M_erik.trigger(T_erik_fork_match)

        "Sex education." if M_erik.between_states(S_erik_learn_fetch, S_erik_learn_acquired):
            call expression game.dialog_select("button_mrsj_erik_learn_fetch_prompt")




        "Sex education." if (M_erik.finished_state(S_erik_learn_prep) and
                             game.timer.is_dark() and
                             player.location is L_erikhouse_mrsjroom):
            jump mrsj_3some

        "Girlfriend." if M_mrsj.is_state(S_mrsj_fork_meet):
            call expression game.dialog_select("button_mrsj_erik_introduce_june")
            jump mrsj_button_dialogue_repeat

        "Girlfriend." if M_mrsj.is_state(S_mrsj_cupid_report):
            call expression game.dialog_select("button_mrsj_erik_got_gf")
            $ M_mrsj.trigger(T_mrsj_cupid_news)
            if game.timer.is_dark():
                call mrsjroom_mrsj_private_yoga_shortcircuit
                jump mrsj_private_yoga

        "Private yoga." if game.timer.is_dark() and M_mrsj.finished_state(S_mrsj_cupid_report):
            call mrsjroom_mrsj_private_yoga_intro
            jump mrsj_private_yoga

        "Where's {b}Erik{/b}?" if not game.timer.is_dark():
            show player 14
            if game.timer.is_morning() and not game.timer.is_weekend():
                player_name "Do you know where I could find {b}Erik{/b}?"
                show player 1
                show mrsj 17
                mrsj "Well, he should be at {b}school{/b} right now."
            else:

                show mrsj 14
                player_name "Do you know where I could find {b}Erik{/b}?"
                show player 1
                show mrsj 17
                mrsj "Well, I think I saw him go into the {b}basement{/b}."
                mrsj "If he's not down there, he might be in his room."
                show mrsj 14
                show player 17
                player_name "Thanks, {b}Mrs. Johnson{/b}!"
            show mrsj 14
            jump mrsj_button_dialogue_repeat

        "Invite to poker." if (M_erik.finished_state(S_erik_poker_ready) and
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

        "You're so fit!" if not L_erikhouse_mrsjroom.is_here(M_mrsj):
            call expression game.dialog_select("button_mrsj_youre_so_fit")
            jump mrsj_button_dialogue_repeat
        "I have to go!":

            call expression game.dialog_select("button_mrsj_leave")

    hide player
    hide old_erik
    hide mrsj
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
