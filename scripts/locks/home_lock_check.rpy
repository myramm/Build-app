label home_lock_check:
    scene expression player.location.background_blur

    if M_anon.is_state(S_ano02_food) and motion not in route(L_home_bedroom,
                                                             L_home_hallway,
                                                             L_home_entrance,
                                                             L_home_kitchen):
        show anon with dissolve
        anon @ -m_talk "( That smell is coming {b}from the kitchen{/b}! I can almost taste it! )"
        hide anon with dissolve

    elif M_anon.is_state(S_ano02_thug) and motion not in route(L_home_entrance,
                                                               L_home):
        scene expression player.location.background_blur
        show anon with dissolve:
            xoffset 300
        "{i}*Ding Dong*{/i}"
        anon @ -m_talk "( I should answer the door. )"
        hide anon with dissolve

    elif M_anon.is_state(S_ano03_done):
        scene expression player.location.background_blur
        show anon f_tired a_sides with dissolve
        anon @ -m_talk "( I'm too tired to think, I'll just crash for tonight. )"
        anon @ -m_talk "( Everything can wait until tomorrow. )"
        hide anon with dissolve

    elif M_anon.is_state(S_ano12_done) and motion not in route(L_home_hallway,
                                                               L_home_bedroom):
        scene expression player.location.background_blur
        show anon f_tired a_sides with dissolve
        anon @ -m_talk "( I'm exhausted and I have a splitting headache... )"
        anon @ -m_talk "( I should just head to bed. )"
        hide anon with dissolve

    elif M_anon.is_state(S_ano21_news) and motion not in route(L_home_bedroom,
                                                               L_home_hallway,
                                                               L_home_entrance,
                                                               L_home_livingroom):
        show anon f_worried with dissolve
        anon @ -m_talk "( I should {b}head to the living room{/b} and see what's going on. )"
        hide anon with dissolve

    elif M_anon.is_state(S_ano21_done) and motion not in route(L_home_entrance,
                                                               L_home_hallway,
                                                               L_home_bedroom):
        show anon a_sides f_tired with dissolve
        if destination == L_home_livingroom:
            anon @ -m_talk "( Nah, I'm sick of seeing {b}Rump{/b}'s ugly mug... )"
        anon @ -m_talk "( I just wanna head to bed. )"
        hide anon with dissolve

    elif M_anon.is_state(S_ano27_yumi) and motion not in route(L_home,
                                                               L_home_entrance):
        show anon a_sides f_worried with dissolve
        anon @ -m_talk "( No time for that! I need to see if {b}Debbie{/b} and {b}Jenny{/b} are OK! )"
        hide anon with dissolve

    elif M_anon.is_state(S_ano27_tony):
        show anon a_sides f_worried with dissolve
        anon @ -m_talk "( {b}Tony{/b}'s waiting for me. There's no time to waste!. )"
        hide anon with dissolve

    elif M_anon.is_state(S_ano28_food) and motion not in route(L_home_bedroom,
                                                               L_home_hallway,
                                                               L_home_entrance,
                                                               L_home_kitchen):
        show anon with dissolve
        anon @ -m_talk "( {b}I should hurry to the kitchen{/b}... )"
        anon f_grin @ -m_talk "( ... {b}[deb_name]{/b}'s got breakfast going. )."
        hide anon with dissolve

    elif M_nadya.is_state(S_nad01_thug) and motion not in route(L_home_bedroom,
                                                                L_home_hallway,
                                                                L_home_entrance):
        show anon f_worried with dissolve
        anon @ -m_talk "( {b}I should get downstairs quickly{/b}! )"
        anon @ -m_talk "( It sounds like {b}[deb_name]{/b} is in trouble! )"
        hide anon with dissolve

    elif M_jenny.is_state(S_jen0m_food) and motion not in route(L_home_bedroom,
                                                                L_home_hallway,
                                                                L_home_entrance,
                                                                L_home_kitchen):
        show anon f_worried with dissolve
        anon @ -m_talk "( {b}Jenny{/b} knows where I sleep. )"
        anon f_tired @ -m_talk "( Probably best if I just go to breakfast in the {b}dining room{/b}. )"
        hide anon with dissolve

    elif M_debbie.is_state(S_debbie_start) and motion not in route(L_home_bedroom,
                                                                   L_home_hallway,
                                                                   L_home_entrance,
                                                                   L_home_kitchen):
        show anon with dissolve
        debbie "{b}[firstname]{/b}, what's taking so long?!"
        debbie "You're going to be late!"
        anon "Coming {b}[deb_name]{/b}!"
        anon @ -m_talk "( I should head to {b}the kitchen{/b} and say good morning before I leave. )"
        hide anon with dissolve

    elif M_debbie.is_state(S_debbie_relaxing) and motion not in route(L_home_kitchen,
                                                                      L_home_entrance,
                                                                      L_home):
        show anon with dissolve
        anon @ -m_talk "( I should {b}head next door and pick up Erik{/b}. )"
        anon @ -m_talk "( I hope he's not still sleeping... )"
        hide anon with dissolve

    elif M_diane.is_state(S_dia01_find) and destination != L_home_garage:
        show anon with dissolve
        if player.location is not L_home_garage:
            anon @ -m_talk "( This isn't the way to the {b}garage{/b}! I can just lift the door. )"
            anon @ -m_talk "( With any luck, the {b}shovel{/b} will be waiting for me. )"
        else:
            anon @ -m_talk "( There it is! Hanging on the wall. I knew I remembered seeing it! )"
        hide anon with dissolve

    elif M_diane.is_state(S_dia01_give) and destination != L_home:
        show anon with dissolve
        anon @ -m_talk "( It'll be getting dark soon... )"
        anon @ -m_talk "( I should {b}get back to Diane{/b} as soon as possible! )"
        hide anon with dissolve

    elif M_debbie.is_state(S_debbie_overheard) and destination != L_home_entrance and game.timer.is_evening():
        show anon f_tired with dissolve
        anon @ -m_talk "( That's not the way inside. )"
        hide anon with dissolve

    elif M_debbie.is_state(S_debbie_debt_call) and destination != L_home_kitchen:
        show anon f_surprised with dissolve
        anon @ -m_talk "( Better check on {b}[deb_name]{/b} before bed... )"
        hide anon with dissolve

    elif M_debbie.is_state(S_debbie_lawn_delay) and motion not in route(L_home_kitchen,
                                                                        L_home_entrance,
                                                                        L_home_hallway,
                                                                        L_home_bedroom):
        show anon f_tired with dissolve
        anon @ -m_talk "( I don't have energy for anything but {b}sleep{/b} right now. )"
        hide anon with dissolve

    elif M_debbie.is_set("bedroom locked") and destination == L_home_mombedroom:
        scene expression player.location.background_blur
        if not game.timer.is_dark():
            if M_erik.finished_state(S_erik_intro_met):
                show anon f_worried with dissolve
                anon @ -m_talk "( I shouldn't snoop around {b}[deb_name]{/b}'s bedroom. )"
                hide anon
            else:
                show anon f_surprised
                show debbie
                with dissolve
                debbie "{b}[firstname]{/b}? Are you looking for something in my room?"
                anon f_shy "I was... Umm... Looking for my phone!"
                anon f_surprised @ f_laugh a_phone "But it's right here in my pocket actually!"
                debbie "Isn't {b}Erik{/b} waiting for you?"
                anon f_normal "Yeah, I'm on my way!"
                hide anon
                hide debbie
        else:
            if M_debbie.is_state(S_debbie_debt_call):
                show anon f_worried with dissolve
                anon @ -m_talk "( I should see go see if {b}[deb_name]{/b} is alright. )"
                hide anon
            else:
                show anon f_worried with dissolve
                anon @ -m_talk "( I really shouldn't disturb {b}[deb_name]{/b} when she's sleeping. )"
                hide anon

        with dissolve

    elif M_debbie.is_state(S_debbie_romance_movie_two) and player.location == L_home_livingroom:
        show anon with dissolve
        anon @ -m_talk "( I shouldn't keep {b}[deb_name]{/b} waiting... )"
        hide anon with dissolve

    elif M_jenny.get("girlfriend_in_progress") and destination in (L_home_sisbedroom, L_home_mombedroom):
        scene expression player.location.background_blur
        show anon with dissolve
        anon @ -m_talk "( No, {b}[jen_name]{/b} went {b}into my room{/b}, I think... )"
        anon @ -m_talk "( I should {b}follow her{/b}. )"
        hide anon with dissolve

    elif M_mia.is_state(S_mia_midnight_call, S_mia_urgent_message) and game.new_message and player.location == L_home_bedroom:
        scene expression player.location.background_blur
        if not game.timer.is_dark():
            show player 12 with dissolve
        else:
            show player 101 with dissolve
        player_name "I should check my text messages."

    elif M_bissette.is_state(S_bissette_roxxy_jenny_spying) and destination not in [L_home_hallway, L_home_sisbedroom]:
        scene expression player.location.background_blur
        show player 10 with dissolve
        player_name "I should go check on {b}Roxxy{/b} and {b}[jen_name]{/b}..."
        hide player with dissolve

    elif not ( L_home_sisbedroom.is_here(M_jenny) or not L_home_sisbedroom.locked ) and destination == L_home_sisbedroom:
        scene expression player.location.background_blur
        show anon f_skeptical with dissolve:
            xoffset 250
        play audio sfxDoor(True)
        anon @ -m_talk "( Her door is locked... )"
        hide anon with dissolve

    elif M_jenny.is_state(S_jenny_pissed_at_handjob, S_jenny_pissed_at_blowjob) and destination == L_home_sisbedroom and not M_bissette.is_state(S_bissette_roxxy_jenny_spying):
        $ player.go_to(L_home_hallway)
        show expression player.location.background_blur with None
        show anon f_worried with dissolve
        anon @ -m_talk "( It's locked. )"
        anon "{b}[jen_name]{/b}?"
        jenny "Go away, asshole!"
        anon @ -m_talk "( Hmm, I guess she's still pissed at me. )"
        pause
        anon @ -m_talk "( I should try {b}talking to her in the morning while she's eating breakfast{/b}. )"
        hide anon with dissolve

    elif M_diane.is_state(S_diane_peeking_masturbate):
        scene expression player.location.background_blur
        show player 427b at Position (xoffset=50) with dissolve
        player_name "I can't go out there with this thing."
        player_name "I should {b}jerk off and clear my head{/b}."
        hide player with dissolve

    elif M_diane.is_state(S_diane_get_dirty_with_debbie) and destination not in [L_home_bedroom, L_home_hallway, L_home_entrance, L_home_livingroom, L_home_mombedroom]:
        scene expression player.location.background_blur
        show player 10 with dissolve
        player_name "I should {b}follow [deb_name]{/b}."
        player_name "I think she went into her room."
        hide player with dissolve

    elif M_diane.is_state(S_diane_3way_aftermath) and destination not in [L_home_mombedroom, L_home_livingroom, L_home_entrance, L_home_kitchen]:
        scene expression player.location.background_blur
        show player 14 with dissolve
        player_name "I should go see what {b}[deb_name]{/b} is cooking {b}in the kitchen{/b}."
        hide player with dissolve

    elif destination == L_home_sisbedroom and M_jenny.get('photo_reaction') == game.timer._game_day * 4 + game.timer._tod:
        scene expression player.location.background_blur
        show anon f_thinking a_thinking with dissolve
        anon @ -m_talk "( No, I shouldn't bother her right now. )"
        anon f_normal a_idle @ -m_talk "( I'll just come back later. )"
        hide anon with dissolve

    elif destination == L_home_attic:
        jump attic_entry_dialogue
    else:
        if player.location == L_home and destination in [L_home_entrance, L_home_garage]:
            $ playSound()
            play audio sfxDoor()
        if player.location in [L_home_entrance, L_home_hallway]:
            $ playSound()
        if destination in [L_home_mombedroom, L_home_sisbedroom, L_home_shower, L_home_bedroom]:
            play audio sfxDoor()
        if player.location in [L_home_bedroom, L_home_sisbedroom, L_home_shower, L_home_mombedroom] and destination in [L_home_hallway, L_home_livingroom]:
            play audio sfxDoor()
        return

    hide anon
    hide player
    with dissolve

    return True

label attic_entry_dialogue:
    if not L_home_attic.locked:
        $ player.location.hide_screen()
        $ player.go_to(L_home_attic)
        $ L_home_attic.call()

    elif player.has_picked_up_item("attic_key") and player.has_picked_up_item("stool"):
        scene expression player.location.background_blur
        $ player.remove_item("attic_key")
        $ player.remove_item("stool")
        $ L_home_attic.unlock()
        call popup ('area', L_home_attic)
        jump expression game.dialog_select("attic_entry_dialogue")
    else:

        scene expression player.location.background_blur
        show player 34 with dissolve
        player_name "Hmm..."
        show player 35
        if not player.has_picked_up_item("stool"):
            player_name "( I need something to {b}stand on{/b} to reach the opening... )"
        else:
            player_name "( That small trap door is {b}locked{/b}. )"
        $ player.location.call()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
