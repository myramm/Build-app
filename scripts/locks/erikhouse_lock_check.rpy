label erikhouse_lock_check:
    scene expression player.location.background_blur

    if M_anon.is_state(S_ano17_erik) and motion not in route(L_erikhouse_basement,
                                                             L_erikhouse_backroom):
        show anon with dissolve
        anon @ -m_talk "( I should speak with {b}Erik{/b}. )"
        hide anon with dissolve

    elif M_anon.is_state(S_ano17_talk):
        show anon f_worried with dissolve
        anon @ -m_talk "( I need to talk to {b}Erik{/b} about those drinks. )"
        hide anon with dissolve

    elif M_anon.is_state(S_ano17_porn) and motion not in route(L_erikhouse_basement,
                                                               L_erikhouse_backroom):
        show anon f_worried with dissolve
        anon @ -m_talk "( I should see what {b}Iwanka{/b} wants. )"
        hide anon with dissolve

    elif M_erik.is_state(S_erik_thief_chase) and destination == L_erikhouse_entrance:
        show player 10 with dissolve
        player_name "( It looked like the thief was trying the backdoor. )"
        player_name "( I should head around the side and confront them! )"
        hide player with dissolve

    elif M_erik.is_state(S_erik_thief_chase) and destination == L_erikhouse_mailbox:
        show player 10 with dissolve
        player_name "( This is no time to be snooping on their mail! )"
        hide player with dissolve

    elif M_erik.is_state(S_erik_thief_chase) and destination == L_erikhouse and player.location == L_erikhouse_backyard:
        scene eriks_backyard_night
        show door_thief_night at Position (xpos=882,ypos=655)
        player_name "( I can't leave just yet. )"
        player_name "( What if he's trying to break in?! )"
        player_name "( I have to make sure nothing bad happens... )"

    elif M_erik.is_state(S_erik_thief_chase):
        return

    elif M_dewitt.is_state(S_dewitt_eve_karaoke) and destination not in (L_erikhouse_entrance, L_erikhouse_basement) and game.timer.is_dark():
        show player 10 with dissolve
        player_name "( {b}Erik{/b} and {b}Eve{/b} are waiting the basement. )"
        player_name "( I should get down there and meet them. )"
        hide player with dissolve

    elif M_dewitt.is_state(S_dewitt_eve_karaoke):
        return

    elif game.timer.is_night() and destination != L_erikhouse:
        show player 10 with dissolve
        player_name "( It's pretty late, I should be getting home. )"
        hide player with dissolve
        $ player.go_to(L_erikhouse)

    elif M_erik.is_state(S_erik_intro_met):
        with None
        show anon f_surprised
        show erik f_worried
        with dissolve
        if destination is L_erikhouse_mailbox:
            erik "Umm... Why are you trying to look at our mail?"
        elif destination is L_erikhouse_backyard:
            erik "Umm... Why are we going to the backyard?"
        else:
            erik "Umm... Why are we going in my house?"
        erik "Shouldn't we be going to {b}school{/b}?"
        anon f_normal "Oh, yeah! You're right..."
        hide anon
        hide erik
        with dissolve

    elif M_erik.is_state(S_erik_cards_ready) and destination is L_erikhouse_basement and not L_erikhouse_basement.is_here(M_erik):
        show player 1 with dissolve
        player_name "( That's been off-limits as long as I can remember. )"
        player_name "( I definitely shouldn't go down without {b}Erik{/b}. )"
        hide player with dissolve

    elif M_erik.is_state(S_erik_orc_done) and destination is L_erikhouse_erikroom and L_erikhouse_erikroom.is_here(M_erik):
        show player 1 with dissolve
        player_name "( {b}Erik{/b}'s probably enjoying some quality time with his new toy. )"
        player_name "( I'm just going to leave him to it. )"
        hide player with dissolve

    elif destination is L_erikhouse_mrsjroom and not M_erik.finished_state(S_erik_feed_ready):
        show player 10 with dissolve
        player_name "( Oops! {b}Mrs. Johnson{/b} must be keeping her door locked... )"
        hide player with dissolve

    elif M_mrsj.get('poker_after_party') and destination is L_erikhouse_entrance:
        with None
        show player 11 at left
        show old_erik 4 at right
        with dissolve
        erik "I thought we were {i}*Hic*{/i} going to the backroom..."
        erik "{b}Mrs. Johnson{/b} is waiting for us, remember?"
        show player 14
        show old_erik 1
        player_name "Oh, riiiight!"
        player_name "Let's go back there and see what she wants."
        show player 1
        show old_erik 4
        erik "I {i}*Hic*{/i} agree."
        hide old_erik
        hide player
        with dissolve

    elif M_mrsj.get('poker_after_party') and destination is L_erikhouse_aquarium:
        scene expression player.location.background_blur
        show character_mrsj_02 at Transform(pos=(0, 315))
        player_name "( It's a cupboard or something? I'm a bit distracted right now... )"

    elif game.timer._game_day == M_erik.get('confessed') and destination not in (L_erikhouse, L_erikhouse_mailbox):
        show anon f_worried_low with dissolve
        anon @ -m_talk "( Probably a good idea to give them a little space right now. )"
        anon @ -m_talk "( I'm sure {b}Erik{/b} will bounce back... )"
        hide anon with dissolve

    elif M_erik.get('in_flagrante') and destination is L_erikhouse_erikroom:
        show player 10 with dissolve
        player_name "( It seems that Erik's otherwise occupied. )"
        player_name "( I can catch up with him tomorrow. )"
        hide player with dissolve
    else:

        return

    return True
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
