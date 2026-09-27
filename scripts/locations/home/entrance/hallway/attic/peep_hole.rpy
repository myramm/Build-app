label peep_hole_dialogue:
    if M_player.get("peep_hole_first"):
        scene expression player.location.background_blur
        player_name "( That's one ugly rug... )"

        player_name "( I wonder why it's up here? )"

        scene expression game.timer.image("backgrounds/location_home_attic_cutscene01{}.jpg")
        player_name "(Hmm?)"

        player_name "( There's a little hole in the floorboards here... )"

        pause
        player_name "( I-is that- )"

        $ M_player.set("peep_hole_first", False)
        call expression game.dialog_select("peep_hole_{}_first".format(game.timer._tod))
    else:
        scene expression game.timer.image("backgrounds/location_home_attic_cutscene01{}.jpg")
        pause
        player_name "( Let's see what {b}[jen_name]{/b} is up to? )"

        call expression game.dialog_select("peep_hole_{}".format(game.timer._tod))
    $ game.main()

label peep_hole_0_first:
label peep_hole_1_first:
    scene expression "backgrounds/location_home_attic_peep_morning.jpg"
    pause
    player_name "( !!! )" with hpunch
    player_name "( It's a peephole, right over {b}[jen_name]{/b}'s bed! )"

    pause
    player_name "( Well, that's convenient... )"

    player_name "( I wonder how it got here? )"

    return

label peep_hole_2_first:
label peep_hole_3_first:
    scene expression "backgrounds/location_home_attic_peep_night.jpg"
    pause
    player_name "( !!! )" with hpunch
    player_name "( It's a peephole, right over {b}[jen_name]{/b}'s bed! )"

    pause
    player_name "( Well, that's convenient... )"

    player_name "( I wonder how it got here? )"

    return

label peep_hole_0:
    scene expression "backgrounds/location_home_attic_peep_morning.jpg"
    pause
    player_name "( Hmm, just an empty bed... )"

    player_name "( I wonder where she's at? )"

    return

label peep_hole_1:
    scene expression "backgrounds/location_home_attic_peep_day_01.jpg"
    pause
    player_name "( Hmm, she's just lying around, writing in her diary... )"

    scene expression "backgrounds/location_home_attic_peep_day_02.jpg"
    pause
    player_name "( Booooring!! )"

    return

label peep_hole_2:
    if M_jenny.once('peephole'):
        jump peep_hole_2.repeat

    scene location_home_attic_peep_evening_01 with fade
    player_name "( I-is she- )"

    scene location_home_attic_peep_evening_02 with dissolve
    player_name "( !!! )" with hpunch
    scene location_home_attic_peep_evening_03 with dissolve
    player_name "( She's masturbating! )"

    scene location_home_attic_peep_evening_04 with dissolve
    player_name "( Oh, this is awesome!! )"


    $ renpy.dynamic(subject='anon' if M_jenny.finished_state(S_jenny_start_camshow_blowjob) else 'daddy')
    call scene_jenny_solo_peephole.repeat (subject)
    $ unlock_scene('Jenny', '20_unlocked', variant=subject)

    scene expression background()
    show anon f_shock_down:
        xzoom -1
    if subject == 'anon':
        show anon f_flirt_grin o_boner
    with fade
    anon @ -m_talk "( Oh kay... )"

    if subject == 'daddy':
        anon f_worried @ -m_talk "( ... That's kinda messed up... )"

    else:
        anon @ -m_talk "( ... That's a little disturbing... )"

    show anon a_thinking f_thinking
    with {'master': dissolve}
    pause
    show anon a_sides f_grin
    with {'master': dissolve}
    anon f_grin @ -m_talk "( ... But still hot. )"

    anon @ -m_talk "( Thank you, peephole! )"

    hide anon with dissolve
    return

label peep_hole_2.repeat:
    scene location_home_attic_peep_evening_04 with fade
    anon "( Looks like she's going to be going at it for a while... )"

    anon "( ... Best move on before I get a cramp. )"

    pause
    scene expression background()
    show anon a_shy_neck f_hurt:
        xzoom -1
    with fade
    anon @ -m_talk "( It's super uncomfortable leaning over this hole. )"

    hide anon with dissolve
    return

label peep_hole_3:
    scene expression "backgrounds/location_home_attic_peep_night.jpg"
    pause
    player_name "( Aww, she's already gone to bed for the night. )"

    pause
    player_name "( Heh, she looks kinda cute and innocent when she's sleeping... )"

    player_name "( ... Not at all like the bitchzilla she really is! )"

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
