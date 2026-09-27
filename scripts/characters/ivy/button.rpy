label ivy_button_dialogue:
    call ivy_button_stage

    if M_jenny.is_state(S_jenny_buy_vibrator):
        call jenXX_vibe_ivy
        $ game.main()
        return

    if M_ivy.is_state(S_ivy_start):
        call ivy_button_greet
        $ M_ivy.trigger(T_ivy_intro)
    else:
        call ivy_button_greet_repeat

    menu:
        "Layanan tata graha." if M_consuela.is_state(S_con01_idea):
            call con01_idea_ivy
            $ M_consuela.trigger(T_con01_idea)
            call con01_deal_ivy.choice

        "bot itu" if M_consuela.is_state(S_con01_deal):
            call con01_deal_ivy

        "bot itu" if M_consuela.is_state(S_con01_take) is False:
            call con01_take_ivy.check

        "bot itu" if M_consuela.is_state(S_con01_take):
            call con01_take_ivy
            call popup ('give', 'thotbot')
            $ player.get_item('thotbot')
            $ M_consuela.trigger(T_con01_take)

        "bot itu" if M_consuela.bot_return:
            call con01_skip_ivy
            $ player.remove_item('thotbot')
            $ player.get_money(800)
            call popup ('earn', 800)
            $ M_consuela.set('bot_return', False)

        "Oke." if M_ivy.is_state(S_ivy_start):
            call expression game.dialog_select("button_ivy_massage_first")
            call screen pamphlet

        "Pijat." if not M_ivy.is_state(S_ivy_start):
            call expression game.dialog_select("button_ivy_massage")
            scene expression background(840, 472, 7., t=0)
            show screen pamphlet
            with fade
            call screen empty
            hide screen pamphlet
            if player.has_money(_return[1]):
                $ player.spend_money(_return[1])
                jump expression 'ivy_{}'.format(_return[0])
            else:
                jump ivy_no_money
        "Hanya berbelanja.":

            call expression game.dialog_select("button_ivy_just_shopping")

    $ game.main()
    return


label ivy_button_stage:
    if L_pink.is_here(M_ivy):
        scene location_pink_any_closeup
        show ivy
        show location_pink_any_closeup_counter as counter
    else:
        scene expression player.location.background_blur
        show ivy
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
