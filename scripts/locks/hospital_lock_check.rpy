label hospital_lock_check:
    scene expression player.location.background_blur

    if L_hospital_storagecabinet in (player.location, destination):
        return

    elif game.timer.is_night() and destination != L_hospital:
        show player 11 with dissolve
        player_name "( It's pretty late, I should be getting home. )"
        hide player with dissolve
        $ player.go_to(L_hospital)

    elif destination is L_hospital_basement and L_hospital_basement.locked:
        scene expression player.location.background_closeup
        show player 427g
        player_name "( I have no reason to go to the basement. )"
        player_name "( Besides, the floor description just says it's some sort of lab anyway. )"

    elif destination != L_hospital_lobby and M_consuela.is_state(S_con02_job3):
        show anon with dissolve
        anon @ -m_talk "( I should {b}ask the receptionist about a job for Consuela{/b}. )"
        hide anon with dissolve

    elif destination == L_hospital_storageroom and M_consuela.is_state(S_con02_scam):
        return

    elif destination not in (L_hospital_elevator, L_hospital_floor2) and M_consuela.is_state(S_con02_scam):
        show anon with dissolve
        anon @ -m_talk "( I should {b}follow that old lady to the second floor storage room{/b}... )"
        anon @ -m_talk "( {b}Consuela{/b} is counting on me. )"
        hide anon with dissolve

    elif destination not in (L_hospital_elevator, L_hospital_lobby) and M_consuela.is_state(S_con02_ptsd):
        show anon f_worried a_sides with dissolve
        anon @ -m_talk "( I- I... )"
        anon f_cough -m_talk "{i}*Huff*{/i}..."
        extend "......"
        anon f_disgusted_wince -m_talk "{i}*Puff*{/i}..."
        extend "......"
        anon f_worried -a_sides @ -m_talk "( I should meet {b}Consuela{/b} back at {b}reception{/b}. )"
        hide anon with dissolve

    elif destination not in (L_hospital_elevator,) and M_priya.is_state(S_priya_roz_camera_check):
        show anon f_worried a_sides with dissolve
        anon @ -m_talk "( Roz asked me to follow her {b}into the elevator{/b}. )"
        anon @ -m_talk "( It's the only chance I have at getting to the basement. )"
        hide anon with dissolve

    elif destination is L_hospital_storageroom and M_roz.is_state(S_roz_obits_collect):
        return

    elif destination is L_hospital_storageroom and not (player.has_item("hospital_access_card") or M_roz.get('fun time')):
        scene hospital_lock
        player_name "( Damn, it's locked! )"
        player_name "( It looks like I need an {b}access card{/b} to unlock this door... )"
        player_name "( The receptionist probably has duplicates of all the keys... )"
        player_name "( Perhaps I could find some at her desk? )"
        $ M_roz.trigger(T_roz_access_denied)
    else:

        return

    return True
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
