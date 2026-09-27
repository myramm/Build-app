label bank_lock_check:
    scene expression player.location.background_blur

    if game.timer.is_night() and destination != L_bank:
        show anon f_tired with dissolve
        anon @ -m_talk "( It's pretty late, I should be getting home. )"

        hide anon with dissolve
        $ player.go_to(L_bank)

    elif game.timer.is_dark() and destination != L_bank:
        show anon f_unimpressed with dissolve
        anon @ -m_talk "( The bank isn't open in the evening. )"

        hide anon with dissolve
        $ player.go_to(L_bank)

    elif game.timer.is_dow(6) and destination != L_bank:
        show anon f_unimpressed with dissolve
        anon @ -m_talk "( Oh no! It's {b}Sunday{/b}. )"

        if not M_player.once('sunday_egg'):
            anon f_surprised_left_low @ -m_talk "( Oh no! It's {b}Sunday{/b}. ){fast}\n{size=-3}\n( What a lazy cat! ){/size}{w=2}{nw}"

        anon -f_surprised_left_low @ -m_talk "( The bank is closed on Sunday. )"

        hide anon with dissolve
        $ player.go_to(L_bank)

    elif M_anon.is_state(S_ano14_sobs) and player.location == L_bank_lobby:
        show anon f_surprised with dissolve
        anon @ -m_talk "( I can barely believe what I just witnessed! )"

        anon f_worried @ -m_talk "( I should {b}find out if Liu is OK{/b}. )"

        hide anon with dissolve

    elif M_anon.is_state(S_ano14_meet) and motion in route(L_bank_lobby,
                                                           L_bank_hallway,
                                                           L_bank_basement):
        return

    elif M_anon.is_state(S_ano14_meet) and motion in route(L_bank_basement,
                                                           L_bank_vault):
        call ano14_meet_bank_basement
        $ M_anon.trigger(T_ano14_meet)

    elif M_anon.is_state(S_ano14_meet) and motion in route(L_bank_basement,
                                                           L_bank_hallway):
        scene expression background(832, 464, 4.) as stage
        show anon a_thinking f_thinking with dissolve:
            xoffset 500
        anon @ -m_talk "( {b}Liu{/b} said she'd meet me here... )"

        show anon a_idle f_grin with dissolve:
            flip
            xoffset 0
        anon @ -m_talk "( ... And in the meantime... That {b}vault door{/b} looks pretty impressive... )"

        hide anon with dissolve

    elif M_anon.is_state(S_ano14_meet):
        show anon with dissolve
        anon @ -m_talk "( {b}Liu{/b} asked me to {b}meet her downstairs{/b}. )"

        anon @ -m_talk "( I should head there now. )"

        hide anon with dissolve

    elif M_anon.is_state(S_ano14_find) and player.location == L_bank_vault:
        show anon a_thinking f_thinking with dissolve
        anon @ -m_talk "( Just need to find the right numbered box... )"

        anon @ -m_talk "( What was the number..? Hmm, maybe I should look at the photo again. )"

        hide anon with dissolve

    elif M_anon.is_state(S_ano14_find) and motion not in route(L_bank_basement,
                                                               L_bank_vault):
        show anon f_surprised with dissolve
        anon @ -m_talk "( No! I'm going to find out what {b}Dad{/b} left in the vault! )"

        hide anon with dissolve

    elif M_anon.is_state(S_ano14_find) and motion in route(L_bank_basement, L_bank_vault):
        return

    elif M_anon.is_state(S_ano23_help) and motion not in route(L_bank_lobby,
                                                               L_bank_hallway):
        show anon f_worried with dissolve
        anon @ -m_talk "( No, I need to make sure {b}Liu{/b} is okay. )"

        anon @ -m_talk "( {b}Kim{/b} dragged her into that hallway over there. )"

        hide anon with dissolve

    elif M_anon.is_state(S_ano23_help) and motion in route(L_bank_lobby,
                                                           L_bank_hallway):
        return

    elif M_anon.is_state(S_ano26_talk):
        show anon of_ski_mask with dissolve
        anon @ -m_talk "(Saya harus mulai dengan membuat pertunjukan dengan {b}Liu{/b} untuk kamera. )"

        anon @ -m_talk "( {b}Saya harus memaksanya turun ke bawah ke dalam brankas{/b}. )"

        hide anon with dissolve

    elif M_anon.is_state(S_ano26_move) and motion in route(L_bank_basement,
                                                           L_bank_hallway):
        scene expression background(832, 464, 4.) as stage
        show anon f_surprised of_ski_mask with dissolve:
            xoffset 500
        anon @ -m_talk "( Not before we get what we need from {b}the vault{/b}! )"

        hide anon with dissolve

    elif M_anon.is_state(S_ano26_move) and motion == (L_bank_basement, L_bank_vault):
        return

    elif M_anon.is_state(S_ano26_move) and motion not in route(L_bank_lobby,
                                                               L_bank_hallway,
                                                               L_bank_basement):
        show anon of_ski_mask with dissolve
        anon @ -m_talk "( {b}I should hurry and get Liu down to the vault{/b}. )"

        hide anon with dissolve

    elif M_anon.is_state(S_ano26_move) and motion in route(L_bank_lobby,
                                                           L_bank_hallway,
                                                           L_bank_basement):
        return

    elif M_anon.is_state(S_ano26_take):
        show anon of_ski_mask_pulled a_tiny_gun_down with dissolve
        anon @ -m_talk "( {b}I can't leave without the briefcase!{/b} )"

        anon @ -m_talk "( It's gotta be in here somewhere. )"

        hide anon with dissolve

    elif L_bank_hallway.locked and motion == (L_bank_lobby, L_bank_hallway):
        show anon with dissolve
        anon @ -m_talk "( I'm not allowed to go back there. )"

        anon @ -m_talk "( It's employees only, I'll get in trouble. )"

        if M_tina.is_state(S_tin02_init):
            anon f_thinking @ -m_talk "( Perhaps I should {b}ask for Tina at the desk{/b}... )"

        hide anon with dissolve

    elif motion in route(L_bank_basement, L_bank_vault):
        scene expression background(512, 512, 4.6) as stage
        show anon with dissolve:
            flip
            xoffset -500
        anon @ -m_talk "( I feel like I'm stating the obvious a bit here, but... )"

        anon f_unimpressed @ -m_talk "( It's locked. )"

        hide anon with dissolve
    else:

        return

    return True
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
