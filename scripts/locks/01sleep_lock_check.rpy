label sleep_lock_check():
    if M_anon.is_state(S_ano21_home) and player.location == L_home_bedroom:
        pause

        scene location_home_bedroom_cutscene01 with fade
        unknown "... You're watching an SNN News Special Report!"


        scene location_home_bedroom_cutscene03 with dissolve
        jon "Good evening, I'm Jon Gurbendy, and this is what's happening in your world tonight! ..."


        scene location_home_bedroom_cutscene04
        anon "What the--"


        scene location_home_bedroom_cutscene03
        anon @ -m_talk "( Who could be watching TV at this hour?! )"


        scene expression background(560, 320, 2.5, t=3) with fade
        show anon b_dressed_changing2 with dissolve:
            flip
        pause
        show anon b_dressed_changing with dissolve
        pause
        anon a_sides b_dressed f_squint @ -m_talk "( I'm going to kill {b}[jen_name]{/b}... )"

        anon @ -m_talk "( It must be her {b}in the living room{/b}. )"

        hide anon with dissolve

        $ game.timer.tick(3)
        $ M_anon.trigger(T_ano21_home)

    elif M_anon.is_state(S_ano21_home) and player.location == L_beachhouse_bedroom:
        scene expression player.location.background_blur
        show anon f_worried_surprised with dissolve
        anon @ -m_talk "( I'm not staying here tonight. )"

        anon @ -m_talk "( The mayor might be done, but the Russians are still out there. )"

        anon @ -m_talk "( I need to be around people. )"

        hide anon with dissolve

    elif M_anon.is_state(S_ano27_done) and player.location == L_home_bedroom:
        $ game.sleep()
        return

    elif M_mia.is_state(S_mia_strip_aftermath, S_mia_midnight_call) and player.location != L_home_bedroom:
        scene expression player.location.background_blur
        show player 35 at left with dissolve
        player_name "( I feel like sleeping at {b}[deb_name]{/b}'s house tonight... )"

        hide player with dissolve

    elif M_mia.is_state(S_mia_midnight_help, S_mia_locked_room) and player.location != L_home_bedroom:
        scene expression player.location.background_blur
        show player 35 at left with dissolve
        player_name "( {b}Mia{/b} needs my help! I should get over to {b}her house{/b}! )"

        hide player with dissolve

    elif M_consuela.is_state(S_con03_door):
        scene expression player.location.background_blur
        show anon with dissolve
        anon @ -m_talk "( I should probably get the door, it might be important. )"

        hide anon with dissolve

    elif M_consuela.is_state(S_con04_wake):
        scene expression player.location.background_blur
        show anon with dissolve
        anon @ -m_talk "( I can't even think about sleep with that racket going on downstairs! )"

        hide anon with dissolve

    elif game.sleep_lock and M_erik.finished_state(S_erik_intro_met):
        scene expression player.location.background_blur
        show player 35 at left with dissolve
        player_name "( I still have some things to do today... )"

        hide player with dissolve

    elif game.sleep_lock:
        scene expression player.location.background_blur
        show player 35 at left with dissolve
        player_name "( Can't sleep right now. I should {b}go to school{/b} before I'm late. )"

        hide player with dissolve
    else:

        $ game.sleep()
        return

    $ game.main()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
