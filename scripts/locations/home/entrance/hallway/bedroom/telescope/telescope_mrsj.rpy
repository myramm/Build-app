label erikmom_bedroom:
    if M_jenny.is_state(S_jenny_perv_on_tammy) and game.timer.is_morning():
        call expression game.dialog_select("telescope_jenny_perv_on_tammy")
        $ persistent.cookie_jar["Mrs Johnson"]["unlocked"] = True
        $ persistent.cookie_jar["Mrs Johnson"]["gallery"]["02_unlocked"] = True
        $ M_jenny.trigger(T_jenny_spied_on_tammy)
        jump bedroom_jenny_give_cunni
    else:
        call expression game.dialog_select(game.telescope.mrsj)

    $ M_player.set("telescope active", True)
    show screen telescope
    call screen telescope_fake

label telescope_jenny_perv_on_tammy:
    if M_mrsj.finished_state(S_mrsj_cupid_report):
        label mrsj_private_yoga_perv_jenny_replay:
        scene windowmrsjday 3a with dissolve
        anon "( There she is... )"
        anon "( Whoa, she's completely naked! )"
        pause
        scene windowmrsjday 3b with dissolve
        anon "( What is she- )"
        scene windowmrsjday 3c-d
        anon "( !!! )" with hpunch
        anon "( Holy crap! )"
        pause
        anon "( Does she know I'm watching?! )"

        hide screen telescope
        scene expression "backgrounds/location_home_bedroom_caught_01.jpg"
        with fade
        anon "Whoaaaa!"

        scene expression "backgrounds/location_home_bedroom_caught_02.jpg" with dissolve
        pause

        scene expression "backgrounds/location_home_bedroom_caught_03.jpg" with dissolve
        pause

        scene expression "backgrounds/location_home_bedroom_caught_04.jpg" with dissolve
        pause

        scene expression "backgrounds/location_home_bedroom_telescope_window.jpg"
        show anon b_telescope_peeking
        show jenny b_telescope_standing f_grin zorder 1
        with fade
        jenny "Spying on the neighbor girl again?"
        show anon b_telescope_laying_back f_surprised zorder 0
        with hpunch
        anon "N-no, I'm not-"
        show anon f_worried
        jenny "Yeah, right."
        jenny "Don't lie."
        show jenny b_telescope_look with dissolve
        jenny "What's she doing now?"
        anon @ -m_talk "..."
        jenny "Holy shit!"

        scene windowmrsjday 3c-d with fade
        jenny "Isn't that your friend's landlady?"
        jenny "What's his name again?"
        anon "{b}Erik{/b}."
        jenny "Yeah, {b}Erik{/b}."
        pause
        jenny "Hah, what's she doing with that exercise ball?!"

        scene expression "backgrounds/location_home_bedroom_telescope_window.jpg"
        show anon b_telescope_laying_back f_worried
        show jenny b_telescope_look
        with fade
        anon "I don't-"
        show jenny f_telescope_surprised b_telescope a_down with dissolve
        jenny "Wait a minute..."
        show jenny f_telescope_normal
        jenny "Does she know you're watching her?!"
        anon "..."
        show jenny f_telescope_laugh
        jenny "No fucking way!"
        show jenny f_telescope_normal
        anon "..."
        jenny "You're fucking {b}Mrs. Johnson{/b}, {b}[firstname]{/b}?!"
        anon "Maybe... Just a little..."
        show jenny b_telescope_look with dissolve
        jenny "Hahahahaah!"
        pause
        jenny "I have to give it to you, {b}[firstname]{/b}."
        jenny "She's really good-looking for her age."
        anon "Y-yeah."
        jenny "I mean, she's nowhere near as hot as me, but still-"
        anon "..."
        show jenny b_telescope_rub a_idle with dissolve
        anon f_surprised @ -m_talk "( !!! )"
        jenny "Damn, look at her go..."
        jenny "You think she's imagining your dick inside her, right now?"
        pause
        $ persistent.cookie_jar["Mrs Johnson"]["unlocked"] = True
        $ persistent.cookie_jar["Mrs Johnson"]["gallery"]["02_unlocked"] = True
        $ renpy.end_replay()
    else:
        label mrsj_erik_cunni_perv_jenny_replay:
        scene windowmrsjday 4a with dissolve
        pause
        anon "( Hmm, she's just talking to {b}Erik{/b}. )"
        anon "( I guess there's not going to be a show today... )"
        pause
        scene windowmrsjday 4b with dissolve
        anon "( Wait a minute, is she- )"
        scene windowmrsjday 4c
        anon "( !!! )" with hpunch
        anon "( He's going down on her! )"
        pause
        anon "( Way to go {b}Erik{/b}! )"

        hide screen telescope
        scene expression "backgrounds/location_home_bedroom_caught_01.jpg"
        with fade
        anon "Whoaaaa!"

        scene expression "backgrounds/location_home_bedroom_caught_02.jpg" with dissolve
        pause

        scene expression "backgrounds/location_home_bedroom_caught_03.jpg" with dissolve
        pause

        scene expression "backgrounds/location_home_bedroom_caught_04.jpg" with dissolve
        pause

        scene expression "backgrounds/location_home_bedroom_telescope_window.jpg"
        show anon b_telescope_peeking
        show jenny b_telescope_standing f_grin zorder 1
        with fade
        jenny "Spying on the neighbor girl again?"
        show anon b_telescope_laying_back f_surprised zorder 0
        with hpunch
        anon "!!!"
        anon f_worried "N-no, I'm not-"
        jenny "Yeah, right."
        jenny "Don't lie."
        show jenny b_telescope_look with dissolve
        jenny "What's she doing now?"
        anon @ -m_talk "..."
        jenny "Holy shit!"

        scene windowmrsjday 4c with fade
        jenny "Isn't that your friend's landlady?"
        jenny "What's his name again?"
        anon "{b}Erik{/b}."
        jenny "Yeah, {b}Erik{/b}."
        pause
        jenny "Hah, she must be desperate if she's turning to that fat ass for some release!"

        scene expression "backgrounds/location_home_bedroom_telescope_window.jpg"
        show anon b_telescope_laying_back f_worried
        show jenny b_telescope_look
        with fade
        anon "Hey, be nice!"
        anon "{b}Erik{/b} is a good guy."
        show jenny f_telescope_laugh b_telescope a_down with dissolve
        jenny "Pfft, yeah whatever."
        show jenny f_telescope_normal
        jenny "Nobody cares!"
        show jenny b_telescope_look with dissolve
        jenny "Well, she seems to be enjoying herself..."
        show jenny b_telescope_rub a_idle with dissolve
        anon @ -m_talk "( !!! )"
        jenny "I guess tubbo really knows what he's doing."
        pause
        $ persistent.cookie_jar["Mrs Johnson"]["unlocked"] = True
        $ persistent.cookie_jar["Mrs Johnson"]["gallery"]["03_unlocked"] = True
        $ renpy.end_replay()
    return

label telescope_mrsj_morning_1:
    scene windowmrsjmorning01
    player_name "( ... Is that {b}Erik{/b}'s landlady?! )"
    scene windowmrsjmorning01b
    player_name "( Oh wow! She's getting dressed... )"
    scene windowmrsjmorning01c
    player_name "( No! Just a little bit longer! )"
    scene windowmrsjmorning01d
    player_name "( Damn! Show's over... )"
    return

label telescope_mrsj_morning_2:
    scene windowmrsjday02
    player_name "( Her blinds are closed. She's probably not home. )"
    return

label telescope_mrsj_afternoon_1:
    scene windowmrsjday01
    player_name "( She's not home. )"
    return

label telescope_mrsj_afternoon_2:
    show windowmrsjday 3a
    player_name "( Woah... She's completely naked!! )"
    show windowmrsjday 3b with fastdissolve
    player_name "( Is that a bouncing ball... With a dildo on it?! )"
    show windowmrsjday 3c with fastdissolve
    player_name "( Why didn't she close the blinds? )"
    show windowmrsjday 3c-d
    player_name "( It's like she wants to be seen... )"
    player_name "( I think she knows... )"
    player_name "( She's staring right at me. )"
    return

label telescope_mrsj_afternoon_3:
    scene windowmrsjday02
    player_name "( Her blinds are closed. She's probably not home. )"
    return

label telescope_mrsj_night_1:
    scene windowmrsjnight03
    player_name "( ... Is she practicing yoga? )"
    player_name "( ... On her bed? )"
    scene windowmrsjnight04
    player_name "..."
    player_name "( {b}Erik{/b}'s landlady is so fit... )"
    player_name "( ... She really does have a great body... )"
    return

label telescope_mrsj_night_2:
    scene windowmrsjnight01
    player_name "( She's not in her room. )"
    return

label telescope_mrsj_night_3:
    scene windowmrsjnight02
    player_name "( She must be sleeping. )"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
