label map_lock_check:
    scene expression L_map.background_blur

    if M_anon.is_state(S_ano02_warn) and destination in (L_home, L_home_bedroom) and game.timer.is_morning():
        $ player.go_to(L_home)
        jump home_front_dialogue

    elif M_anon.is_state(S_ano03_init) and game.timer.is_day() and not game.timer.is_dow(5):
        call ano03_init_town_map
        $ M_player.set('mugged', game.timer._game_day)
        $ player.spend_money(500)
        $ M_anon.trigger(T_ano03_init)

    elif (M_anon.between_states(S_ano04_test, S_ano08_done) or
          M_anon.between_states(S_ano09_wage, S_ano20_done)) and game.timer.is_day() and game.timer._game_day - M_player.mugged - 2 > random.randint(0, 199):
        call town_map_mugging
        $ M_player.set('mugged', game.timer._game_day)
        $ player.spend_money(5000)

    elif M_anon.is_state(S_ano12_dark, S_ano12_oops, S_ano12_done) and game.timer.is_day() and destination == L_warehouse:
        anon "( No way I'm going near that place while the sun is up... )"
        anon "( I should {b}come back once it's dark{/b}. )"

    elif M_anon.is_state(S_ano12_zoom) and destination == L_warehouse:
        anon "( I'll need {b}binoculars{/b} if I want to do proper recon. )"
        anon "( Pretty sure there's a pair {b}in that old tree house Erik and I built{/b}. )"

    elif M_anon.is_state(S_ano22_ally):
        call ano22_ally_town_map
        $ game.timer.tick(3)
        $ M_anon.trigger(T_ano22_ally)

    elif M_anon.is_state(S_ano26_done) and destination == L_bank:
        anon "( I should steer clear of the bank for today. )"
        anon "( I'm sure it's swarming with cops after the robbery. )"

    elif M_anon.is_state(S_ano27_home) and destination not in (L_home, L_home_bedroom):
        anon "( Sounds like tomorrow's gonna be a busy day. )"
        anon "( I should head home and get some rest. )"

    elif M_anon.is_state(S_ano27_tony) and destination != L_pizzeria_exterior:
        anon "( {b}Tony{/b}'s meeting me at the {b}pizzeria{/b}! )"
        anon "( I need to get there right now! )"

    elif M_anon.is_state(S_ano27_plan) and destination != L_warehouse:
        anon "( {b}Nadya is gonna be waiting for us in front of the warehouse{/b}... )"
        anon "( ... We need to hurry. )"

    elif M_iwanka.is_state(S_iwa01_pier) and destination != L_pier:
        iwanka "Do you know where you're going?"
        anon "Yes."
        iwanka "Okay."
        "..."
        iwanka "Because one would assume that {b}the pier{/b} is near the water..."
        iwanka "... And you're going the wrong direction."
        anon "Trust me."
        anon "I know what I'm doing, okay?"
        "..."
        iwanka "Mhmm."

    elif M_anon.is_state(S_ano20_cops) and destination != L_police_front:
        anon "( I can't do that. )"
        anon "( I need to get this evidence over to {b}Harold{/b} at the {b}police station{/b}! )"

    elif M_anon.is_state(S_ano20_done) and destination == L_rump_front:
        anon "( {b}Harold{/b} will kill me if I show up! )"
        anon "( I have to trust him to take care of things for now. )"

    elif M_odette.is_state(S_ode02_warn) and destination != L_tattooparlor:
        anon "( But {b}Odette{/b}! I have to find {b}Eve{/b} right away! )"
        anon "( It's so early, she probably hasn't left the tattoo parlor yet. )"

    elif M_erik.is_state(S_erik_start) and destination in (L_home, L_home_bedroom):
        anon "( That's {b}[deb_name]{/b}'s house! I just came from there! )"
        anon "( {b}Erik{/b} lives next door. )"

    elif M_erik.is_state(S_erik_intro_met) and destination != L_school_front:
        erik "We should get moving, you remember what {b}Mrs. Smith{/b} is like!"
        anon "{i}*Gulp!*{/i} Right!"
        anon "( The {b}school{/b} is the {b}big building in the middle of town{/b}. )"

    elif M_diane.is_state(S_dia01_init) and destination != L_diane_yard and game.timer.is_afternoon():
        anon "( I should hurry to {b}Diane's house{/b} and see about this gardening job. )"
        anon "( The extra money could really come in handy. )"
        anon "( If I remember correctly she lives {b}due north from the school{/b}. )"

    elif M_diane.is_state(S_dia01_find) and destination != L_home:
        anon "( {b}The shovel should be in the garage at home{/b}. )"
        anon "( All the way back to {b}south-east Summerville{/b}, I guess. )"

    elif M_diane.is_state(S_dia01_give) and destination != L_diane_yard:
        anon "( {b}Diane{/b} is waiting on me. )"
        anon "( I should {b}get this shovel back to her{/b} immediately. )"

    elif M_debbie.is_state(S_debbie_overheard) and destination not in (L_home, L_home_bedroom) and game.timer.is_evening():
        anon "( So tired, I just want to go home. )"

    elif game.timer.is_night() and destination == L_lair:
        anon "( {b}Aqua{/b} will be sleeping... Like I should be! )"

    elif game.timer.is_night() and destination == L_pier:
        anon "( I'll see the Captain tomorrow, I need some sleep! )"

    elif M_roxxy.is_state(S_roxxy_sneak_into_smith) and not M_iwanka.is_state(S_iwa01_pier) and destination != L_smith_front and game.timer.is_dark():
        anon "( I should {b}go to Mrs. Smith's house{/b} now. )"

    elif M_roxxy.is_state(S_roxxy_sneak_into_smith) and destination == L_smith_front and not game.timer.is_dark():
        anon "( I can't go there right now! )"
    else:

        $ playMusic()
        if destination in [L_school_front, L_diane_yard, L_pool, L_mall_parking_lot, L_bank,
                             L_pier, L_forest, L_police_front, L_beach, L_hospital]:
            $ playSound()
        if destination == L_pool:
            $ wearing_swimsuit = False
            $ changing_count = 0
        return

    return True
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
