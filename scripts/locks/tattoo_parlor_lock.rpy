label tattoo_parlor_lock_check:
    scene expression player.location.background_blur

    if game.timer.is_night() and destination != L_tattooparlor:
        show anon f_tired with dissolve
        anon @ -m_talk "( It's pretty late, I should be getting home. )"

        hide anon with dissolve
        $ player.go_to(L_tattooparlor)

    elif game.timer.is_weekend() and game.timer.is_morning() and not M_eve.finished_state(S_eve_voyeurism_follow_roof) and destination == L_tattooparlor_bedroom:
        show anon a_thinking f_thinking
        anon @ -m_talk "( I don't think I'm close enough with {b}Eve{/b} to go barging into her bedroom while she's sleeping... )"

        anon @ -m_talk "( ... It might creep her out and ruin our friendship. )"

        pause
        anon a_pocket f_normal @ -m_talk "(Saya akan kembali lagi nanti dan berbicara dengannya.)"

        hide anon with dissolve

    elif M_odette.is_state(S_ode02_warn) and destination != L_tattooparlor_interior:
        show anon f_worried with dissolve
        anon @ -m_talk "( I don't want to miss {b}Eve{/b}. I should check the shop before going upstairs. )"

        hide anon with dissolve

    elif M_eve.is_state(S_eve_visit_garage) and destination != L_tattooparlor_garage:
        show anon with dissolve
        anon @ -m_talk "( {b}Eve{/b} said she wanted to show me around and then headed towards {b}the garage{/b}. )"

        anon @ -m_talk "( I should {b}follow her{/b}. )"

        hide anon with dissolve

    elif M_eve.is_state(S_eve_visit_roof) and destination != L_tattooparlor_fire_escape:
        show anon with dissolve
        anon @ -m_talk "( {b}Eve{/b} said she wanted to show me around and then headed {b}up the ladder{/b}. )"

        anon @ -m_talk "( I should {b}follow her{/b}. )"

        hide anon with dissolve

    elif M_eve.is_state(S_eve_visit_apartment) and destination != L_tattooparlor_apartment:
        show anon with dissolve
        anon @ -m_talk "( {b}Eve{/b} said she wanted to show me around and then headed towards {b}her apartment{/b}. )"

        anon @ -m_talk "( I should {b}follow her{/b}. )"

        hide anon with dissolve

    elif M_eve.is_state(S_eve_visit_bedroom) and destination != L_tattooparlor_bedroom:
        show anon with dissolve
        anon @ -m_talk "( {b}Eve{/b} said she wanted to show me around and then headed towards {b}her bedroom{/b}. )"

        anon @ -m_talk "( I should {b}follow her{/b}. )"

        hide anon with dissolve

    elif M_eve.is_state(S_eve_big_sis_check_garage) and destination not in (L_tattooparlor_garage, ):
        show anon with dissolve
        anon @ -m_talk "( There's nobody in there and {b}Eve was headed towards the garage{/b}... )"

        anon @ -m_talk "( I should {b}follow her{/b}. )"

        hide anon with dissolve

    elif M_eve.is_state(S_eve_big_sis_talk_odette):
        show anon with dissolve
        anon @ -m_talk "( We should check on {b}Odette{/b} first. )"

        hide anon with dissolve

    elif M_eve.is_state(S_eve_big_sis_check_apartment) and destination not in (L_tattooparlor_fire_escape, L_tattooparlor_apartment):
        show anon with dissolve
        anon @ -m_talk "( {b}Eve's already headed to her apartment, I should follow{/b}. )"

        hide anon with dissolve

    elif M_eve.is_state(S_eve_distract_grace) and destination not in (L_tattooparlor_apartment, ):
        show anon f_worried
        anon @ -m_talk "( I can't do that now. )"

        anon f_flirt @ -m_talk "( I'm supposed to be {b}distracting Eve's sister{/b}! )"

        hide anon with dissolve

    elif M_eve.is_state(S_eve_bathroom_break) and destination not in (L_tattooparlor_bedroom, ) and player.location != L_tattooparlor_bedroom:
        show anon o_boner f_worried with dissolve
        anon "( I can't just leave. )"

        anon "( Man, {b}I really hope Eve has finished changing{/b}... )"

        hide anon with dissolve

    elif M_eve.is_state(S_eve_bathroom_break) and destination not in (L_tattooparlor_bathroom, ) and player.location == L_tattooparlor_bedroom:
        show anon o_boner with dissolve
        anon @ -m_talk "( I might as well use the bathroom while I'm in here. )"

        hide anon with dissolve

    elif M_eve.is_state(S_eve_bathroom_embarassed) and destination in (L_tattooparlor_bathroom, ):
        show anon f_surprised o_boner with dissolve
        anon @ -m_talk "( No way! )"

        anon @ -m_talk "( I'm too embarrassed to go back in there! )"

        hide anon with dissolve

    elif M_eve.is_state(S_eve_voyeurism_follow_roof) and destination not in (L_tattooparlor_fire_escape, L_tattooparlor_roof):
        show anon with dissolve
        anon "( I should {b}follow Eve up to the roof{/b}. )"

        hide anon with dissolve

    elif M_eve.is_state(S_eve_voyeurism_follow_tent) and destination not in (L_tattooparlor_tent, ):
        show anon
        anon @ -m_talk "( {b}Eve{/b} is inside the tent already. )"

        anon @ -m_talk "( I should {b}follow her{/b}. )"

        hide anon with dissolve

    elif M_eve.is_state(S_eve_bike_breakdown_repair) and game.timer.is_weekend() and not game.timer.is_night() and destination != L_tattooparlor_garage:
        show anon f_thinking a_thinking with dissolve
        anon @ -m_talk "( {b}Odette{/b} said {b}Eve and her sister are in the garage{/b}. )"

        anon @ -m_talk "( I should head there. )"

        hide anon with dissolve

    elif M_eve.is_state(S_eve_talk_to_girls, S_eve_talked_to_grace, S_eve_talked_to_eve) and player.location == L_tattooparlor_roof and game.timer.is_dark():
        show anon f_tired with dissolve
        anon @ -m_talk "( Nah, I should {b}check on Eve and Grace{/b}. )"

        hide anon with dissolve

    elif M_eve.is_state(S_eve_clients_wake_up_grace) and game.timer.is_day() and destination not in (L_tattooparlor_fire_escape, L_tattooparlor_apartment, L_tattooparlor_bedroom) and player.location != L_tattooparlor_apartment:
        show anon with dissolve
        anon @ -m_talk "( {b}Odette asked me to go upstairs and wake the girls up{/b}. )"

        anon @ -m_talk "( I should do that now. )"

        hide anon with dissolve

    elif M_eve.is_state(S_eve_clients_wake_up_grace) and game.timer.is_day() and destination != L_tattooparlor_bedroom and player.location == L_tattooparlor_apartment:
        show anon with dissolve
        anon @ -m_talk "( They are not here. )"

        anon @ -m_talk "( I should {b}check the bedroom{/b}. )"

        hide anon with dissolve

    elif M_eve.is_state(S_eve_clients_take_care_clients) and destination != L_tattooparlor_interior and game.timer.is_day():
        show anon with dissolve
        anon @ -m_talk "( It's too crowded. )"

        anon @ -m_talk "( I can't get through to the garage. )"

        hide anon with dissolve

    elif M_eve.party_in_progress and destination == L_tattooparlor_interior and game.timer.is_date(tod=(2, 3), dow=5):
        show anon with dissolve
        anon @ -m_talk "( This is all locked up. )"

        anon @ -m_talk "( I should head {b}through the garage{/b}. )"

        hide anon with dissolve

    elif M_eve.party_in_progress and destination == L_map and game.timer.is_date(tod=(2, 3), dow=5):
        show anon a_thinking f_thinking with dissolve
        anon @ -m_talk "( I can't leave yet, the party isn't over. )"

        hide anon with dissolve

    elif M_eve.party_in_progress and destination == L_tattooparlor_apartment and game.timer.is_date(tod=(2, 3), dow=5):
        if M_eve.party_in_progress_apartment_first:
            show anon with dissolve
            anon @ -m_talk "( Hmm, it's locked. )"

            random_brit "'Ey watch it, will ya?!"

            random_brit "I'm tryin' to use the loo!"

            anon f_skeptical "Umm, I think that's a flower box..."

            random_brit "Awright, awright... No need to get narky!"

            random_brit "You got a fag I can bum?"

            anon f_surprised "A-apa?"

            random_brit "A cigarette?!"

            random_brit "Mine are downstairs and I can't be arsed."

            anon f_worried "I don't smoke."

            random_brit "Well, that figures dunnit?"

            anon f_confused "Eh?"

            random_brit "Fucking Americans..."

            show anon f_surprised
            pause
            anon @ -m_talk "( What a strange girl... )"

            hide anon with dissolve
            $ M_eve.set("party_in_progress_apartment_first", False)
        else:
            show anon with dissolve
            anon @ -m_talk "( I should {b}head upstairs{/b}. )"

            hide anon with dissolve

    elif M_eve.is_state(S_eve_make_up_dress_table) and destination == L_tattooparlor_interior:
        show anon a_lasagna with dissolve
        anon @ -m_talk "( I should {b}get this upstairs{/b} before {b}Grace{/b} sees it. )"

        anon @ -m_talk "( Don't wanna spoil the surprise. )"

        hide anon with dissolve
    else:

        return

    return True
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
