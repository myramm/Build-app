label pizzeria_lock_check:
    scene expression player.location.background_blur

    if M_maria.sex and motion not in ((L_pizzeria_interior, L_pizzeria_kitchen),
                                      (L_pizzeria_kitchen, L_pizzeria_storage)):
        show anon with dissolve
        anon @ -m_talk "( I can't leave now. )"
        if M_anon.is_state(S_ano11_bone):
            anon f_grin @ -m_talk "( {b}Tony{/b} is counting on me. )"
        else:
            anon f_grin @ -m_talk "( {b}Maria{/b} is waiting for me. )"
        hide anon with dissolve

    elif M_maria.sex:
        return

    elif M_anon.is_state(S_ano27_tony):
        return

    elif game.timer.is_night() and destination != L_pizzeria_exterior:
        show anon f_tired with dissolve
        anon @ -m_talk "( It's pretty late, I should be getting home. )"
        hide anon with dissolve
        $ player.go_to(L_pizzeria_exterior)

    elif game.timer.is_dow(6):
        show anon with dissolve
        anon @ -m_talk "( It's closed. )"
        anon f_sad @ -m_talk "( Summerville's bylaws dictate that no one may consume pizza on Sundays. )"
        hide anon with dissolve

    elif M_anon.is_state(S_ano06_cook) and destination != L_pizzeria_kitchen:
        call tony_button_dialogue

    elif M_anon.is_state(S_ano06_wait):
        show anon f_shy with dissolve
        anon "Nah, I should give them some time alone."
        anon "I'll {b}come back tomorrow{/b}."
        hide anon with dissolve

    elif M_anon.is_state(S_ano11_prep) and destination == L_pizzeria_storage:
        show anon f_worried with dissolve:
            flip
        anon @ -m_talk "( Hmm? )"
        anon @ -m_talk "( It's locked. )"
        tony "Who is it?"
        anon f_normal "{b}Tony{/b}?"
        anon "What are you doing in there?"
        tony "I'm gettin' everything set up for tonight, champ..."
        anon f_flirt "Do you need any help?"
        tony "No, I absolutely do not!"
        tony "I want this to be a surprise for both of ya."
        anon @ f_worried "Oh kay..."
        anon @ -m_talk "( I guess I'll just {b}come back later tonight{/b} then. )"
        hide anon with dissolve

    elif M_anon.is_state(S_ano12_zoom, S_ano12_oops) and destination != L_pizzeria_exterior:
        show anon f_worried with dissolve
        anon @ -m_talk "( No, I don't want {b}Tony{/b} taking unnecessary risks... )"
        anon @ -m_talk "( ... Not with them starting a family and all. )"
        anon @ -m_talk "( I should {b}investigate this address on my own{/b}. )"
        hide anon with dissolve

    elif M_anon.is_state(S_ano20_done, S_ano21_cops, S_ano21_home) and destination != L_pizzeria_exterior:
        show anon f_worried with dissolve
        anon @ -m_talk "( I can't face {b}Tony{/b} right now. I know he disapproved of getting the cops involved... )"
        if M_anon.is_state(S_ano21_home):
            anon f_sad_down @ -m_talk "( ... And he was totally right. I don't know if I'm more mad at myself or the cops... )"
        else:
            anon @ -m_talk "( ... But what was the alternative? I should wait and see how this plays out before visting him again. )"
        hide anon with dissolve

    elif M_anon.is_state(S_ano26_init) and destination != L_pizzeria_exterior and L_bank.is_here(M_tony):
        show anon f_worried with dissolve
        anon @ -m_talk "( Huh... It's locked. That's unusua- )"
        anon f_surprised_teeth @ -m_talk "( Crap! It's Tuesday! I'm meant to be meeting {b}Tony{/b} at the bank! )"
        anon @ -m_talk "( I gotta go! )"
        hide anon with dissolve

    elif M_anon.is_state(S_ano26_done) and destination != L_pizzeria_exterior:
        show anon f_worried with dissolve
        anon @ -m_talk "( {b}Tony{/b} closed down for the day to go see {b}Maria{/b}. )"
        anon @ -m_talk "( I shouldn't bother them. )"
        hide anon with dissolve

    elif M_maria.pregnancy.character_bedridden and destination != L_pizzeria_exterior:
        show anon with dissolve
        anon @ -m_talk "( It's closed. )"
        show anon f_thinking a_thinking with dissolve
        pause
        anon @ -m_talk "( {b}Tony{/b} and {b}Maria{/b} must still be at the {b}hospital{/b} with the baby. )"
        hide anon with dissolve

    elif M_diane.is_state(S_dia03_stow) and destination != L_pizzeria_kitchen:
        call tony_button_dialogue
    else:

        return

    return True
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
