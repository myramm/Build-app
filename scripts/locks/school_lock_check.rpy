label school_lock_check:
    scene expression player.location.background_blur

    if M_dewitt.is_state(S_dewitt_smith_office_trap) and game.timer.is_dark() and player.location == L_school_floor3 and destination != L_school_smithoffice:
        show anon a_surprised_up_both f_worried_surprised with dissolve
        anon @ -m_talk "( We need to hurry up and {b}get to Mrs. Smith's office{/b}! )"
        hide anon with dissolve

    elif M_dewitt.is_state(S_dewitt_smith_office_trap) and game.timer.is_dark() and player.location == L_school_floor3:
        return

    elif game.timer.is_night() and player.location == L_school_floor3 and destination != L_school_floor2:
        show anon f_tired with dissolve
        anon @ -m_talk "( I should go home and get some sleep. )"
        hide anon with dissolve

    elif M_smith.is_state(S_smith_go_to_athletics) and destination not in (L_school_lefthallway, L_school_boysroom, L_school_shower):
        show anon with dissolve
        anon @ -m_talk "( I should {b}hit the boys' locker room{/b} and get changed for athletics class. )"
        anon @ -m_talk "( It's {b}in the left hall{/b}. )"

    elif M_smith.is_state(S_smith_go_to_athletics) and destination in (L_school_shower, ):
        show anon b_jersey f_worried with dissolve
        anon @ -m_talk "( I should {b}go to the field{/b} for my Athletics class... )"

    elif M_smith.is_state(S_smith_intro) and destination not in (L_school_hall, L_school_floor2, L_school_floor3, L_school_smithoffice):
        show anon f_worried with dissolve
        anon "{b}Mrs. Smith{/b} wanted to see me {b}in her office, up on the third floor{/b}."
        anon "I'd better get there quick if I don't want detention."

    elif M_smith.is_state(S_smith_go_to_locker) and destination not in (L_school_hall, L_school_floor2, L_school_floor3, L_school_smithoffice, L_school_locker_MC):
        show anon with dissolve
        anon "I'm supposed to wait for {b}Annie{/b} by my locker..."

    elif M_bridget.get_state() == S_bridget_intro and destination not in (L_school_hall, L_school_track):
        show anon b_jersey f_worried with dissolve
        anon @ -m_talk "( I should {b}go to the field{/b} for my Athletics class. )"

    elif M_bissette.get_state() == S_bissette_intro and destination not in (L_school_frenchclassroom, ):
        show anon f_thinking with dissolve
        anon @ -m_talk "( I should {b}go to Miss Bissette's class{/b} now. )"

    elif M_dewitt.is_state(S_dewitt_paint_trail) and destination not in (L_school_righthallway, L_school_hall, L_school_floor2, L_school_floor3, L_school_smithoffice):
        show anon f_skeptical with dissolve
        anon @ -m_talk "( The trail doesn't lead that way. )"

    elif M_dewitt.is_state(S_dewitt_check_up) and motion not in route(L_school_floor3,
                                                                      L_school_floor2,
                                                                      L_school_hall,
                                                                      L_school_musicclassroom):
        show anon f_thinking with dissolve
        anon @ -m_talk "( I should {b}check on Miss Dewitt{/b}. )"

    elif M_dewitt.is_state(S_dewitt_school_sneak_mission) and destination not in (L_school_lefthallway, L_school_hall) and player.location != L_school_front and game.timer.is_dark():
        show anon f_skeptical with dissolve
        anon @ -m_talk "( I wonder where those hooded figures were going? They headed {b}left{/b}! )"

    elif M_dewitt.is_state(S_dewitt_smith_office_trap) and motion not in route(L_school_lefthallway,
                                                                               L_school_hall,
                                                                               L_school_floor2,
                                                                               L_school_floor3,
                                                                               L_school_smithoffice):
        show anon f_skeptical with dissolve
        anon @ -m_talk "( No time to mince about, we still need to {b}hit Mrs. Smith's office{/b}! )"

    elif M_dewitt.is_state(S_dewitt_attend_talent_show, S_dewitt_talent_show) and player.location is L_school_assemblyhall:
        show anon f_surprised with dissolve
        anon @ -m_talk "( This is no time to leave, everyone's waiting! )"
        hide anon with dissolve

    elif M_okita.is_state(S_okita_get_ingredients) and game.timer.is_afternoon() and not player.has_item('tissue') and player.location is L_school_smithoffice:
        show anon f_worried with dissolve
        anon @ -m_talk "( I can't leave without that DNA, who knows when I'll get another shot... )"
        hide anon with dissolve

    elif M_diane.is_state(S_diane_delivery_3_drop_off_goods):
        jump smith_office_smith_delivery_3_dialogue

    elif M_eve.is_state(S_eve_auditorium_bummed) and player.location is L_school_assemblyhall:
        show anon f_worried with dissolve
        anon @ -m_talk "( {b}Eve{/b} looks bummed, I should see what's up. )"
        hide anon with dissolve

    elif M_eve.is_state(S_eve_auditorium_bummed) and destination not in (L_school_assemblyhall,):
        show anon f_worried with dissolve
        anon @ -m_talk "( {b}Eve{/b} snuck into the auditorium, I should check on her. )"
        hide anon with dissolve

    elif L_school_girlsroom.locked and destination == L_school_girlsroom:
        show anon with dissolve
        anon @ -m_talk "( The girls' locker room is under construction right now... )"

    elif M_roxxy.is_state(S_roxxy_lolipop_for_lolipop, S_roxxy_lolipop_just_once) and destination not in (L_school_frenchclassroom, L_school_hall, L_school_locker_MC) and game.timer.is_day():
        if player.has_item("roxxy_homework"):
            show anon f_worried with dissolve
            anon "I should {b}get this homework to Roxxy{/b}."
            hide anon with dissolve
        else:
            show anon f_worried with dissolve
            anon "I should {b}get my French homework out of my locker for Roxxy{/b}."
            hide anon with dissolve

    elif destination == L_school_utilitycloset:
        show anon f_thinking a_thinking with dissolve
        anon @ -m_talk "( The utility closet is locked. )"

    elif destination == L_school_okitaoffice:
        jump okita_office_door

    elif (M_okita.is_state(S_okita_get_ingredients) and game.timer.is_afternoon() and not player.has_item("tissue")) and not M_dewitt.is_state([S_dewitt_paint_trail, S_dewitt_check_up]) and destination == L_school_smithoffice:
        jump annie_enter_office_dialogue

    elif M_okita.is_state(S_okita_get_items_from_office) and player.location == L_school_okitaoffice and destination == L_school_floor3:
        show anon with dissolve
        anon "I can't leave yet. {b}Miss Okita{/b} said I needed {b}a lab coat, safety glasses, and her blueprints{/b}."
    elif destination == L_school_hall and player.location == L_school_front and not player.has_item('master_key') and game.timer.is_dark():
        show anon f_worried with dissolve
        anon "I can't go to school at night!"
        anon "Maybe if I {i}borrowed{/i} that {b}master key{/b} {b}Annie{/b} used on my locker..."
    else:
        if player.location == L_school_floor2 and destination in [L_school_computerlab, L_school_teacherslounge]:
            $ playSound()
            play audio sfxDoor()
        if player.location == L_school_floor2 and destination == L_school_cafeteria:
            $ playSound()
        if player.location == L_school_floor3 and destination != L_school_floor2:
            $ playSound()
            play audio sfxDoor()
        if destination in (L_school_girlsroom, L_school_assemblyhall):
            $ playSound()
        if destination == L_school_bridgetoffice:
            $ playSound()
            play audio sfxDoor()
        return
    hide anon
    with dissolve

    return True
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
