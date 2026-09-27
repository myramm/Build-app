label dealership_lock_check:
    scene expression player.location.background_blur

    if game.timer.is_night() and destination != L_dealership:
        show anon f_tired with dissolve
        anon @ -m_talk "( It's pretty late, I should be getting home. )"

        hide anon with dissolve
        $ player.go_to(L_dealership)

    elif M_anon.between_states(S_ano05_prat, S_ano05_deal) and player.location is L_dealership_showroom:
        show anon with dissolve
        anon @ -m_talk "( I'm definitely in the right place, I just need to work out who to speak to. )"

        hide anon with dissolve

    elif M_josie.is_state(S_jos01_spot) and player.location is L_dealership_showroom:
        show anon f_confused with dissolve

        if M_rump.state is None:
            anon @ -m_talk "( Curiosity has got the best of me, I simply have to know what the mayor is doing here... )"

            anon a_thinking @ -m_talk "( There's no way he buys his own cars... Right? )"


        elif M_kim.state is None:
            anon @ -m_talk "( Curiosity has got the best of me, I simply have to know what they're arguing about... )"

            anon f_grin @ -m_talk "( Maybe {b}Kim{/b} is finally getting fired! )"

        else:

            anon @ -m_talk "( Curiosity has got the best of me, I simply have to know who that new girl is... )"

            anon a_thinking @ -m_talk "( There's something eerily familiar about her... )"


        hide anon with dissolve

    elif M_josie.is_state(S_jos01_find) and destination is L_dealership:
        show anon f_surprised with dissolve
        anon @ -m_talk "( I can't leave yet, I've not managed to {b}find Josie{/b}! )"

        hide anon with dissolve

    elif M_josie.is_state(S_jos01_done) and destination is L_dealership_showroom:
        show anon f_surprised with dissolve
        anon @ -m_talk "(Tidak mungkin aku akan kembali ke sana!)"

        anon @ -m_talk "( Not after what just happened. )"

        pause
        anon @ -m_talk "( Maybe in a day or two... )"

        hide anon with dissolve

    elif M_josie.sex and destination is L_dealership:
        show anon f_worried with dissolve
        anon @ -m_talk "( Josie's waiting upstairs... )"

        anon f_surprised_forward @ -m_talk "( ... And I have no intention of finding out what she might do if I just leave. )"

        pause
        hide anon with dissolve

    elif M_yoyo.is_state(S_yoy01_lewd) and destination is not L_dealership_garage:
        show anon f_flirt_grin with dissolve
        anon @ -m_talk "( Mmm, banana cream! )"

        anon @ -m_talk "( I should follow Kim into the garage and get a piece of that delicious pie! )"

        hide anon with dissolve
    else:

        if M_player.ano05_continue:
            $ M_player.set('ano05_continue', False)
        if M_player.ano07_continue and destination != L_dealership_showroom:
            $ M_player.set('ano07_continue', False)
        return

    return True
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
