label trailer_lock_check:
    scene expression player.location.background_blur

    if game.timer.is_night() and destination in (L_trailer_shack_interior, L_trailer_interior):
        show anon f_worried with dissolve
        anon @ -m_talk "( They're probably sleeping, I'll come back tomorrow. )"

        hide anon with dissolve

    elif M_roxxy.is_state(S_roxxy_studying_at_roxxys) and not game.timer.is_dark() and destination == L_trailer:
        show player 34 with dissolve
        player_name "( I'm supposed to {b}meet Roxxy there this evening{/b}. I should wait 'til then. )"

        hide player with dissolve

    elif M_roxxy.is_state(S_roxxy_studying_at_mcs) and destination not in [L_trailer, L_trailerpark]:
        if destination == "trailer_interior" and not M_roxxy.get("heard clyde in trailer"):
            $ M_roxxy.set("heard clyde in trailer", True)
            scene expression game.timer.image("trailer_interior_c{}")
            show old_crystal 12 at right
            show clyde 17 at left
            with dissolve
            clyde "Jesus, {b}Auntie{/b}... ya gotta slow down a bit!"

            show clyde 16
            show old_crystal 13
            crystal "Don't you go worryin' about me!"

            crystal "I been doin' this since before you was born."

            show old_crystal 12
            show clyde 17
            clyde "I'm just sayin', yer gonna screw up the count 'iffin ya keep goin' dat fast!"

            show clyde 16
            show old_crystal 13
            crystal "Why don't ya just sit your butt over there and look perty while your auntie does her thing?!"

            show old_crystal 12
            player_name "( Hmm, are they... )"

            player_name "( Wow, that's a big stack of money! )"

            player_name "( Where the heck did they get that I wonder? )"

            pause
            player_name "( I should probably get out of here before they see me. )"

            scene black with fade
        else:

            scene expression player.location.background_blur
            show player 34 with dissolve
            player_name "( Hmm, no... )"

            player_name "( I need to catch up with {b}Roxxy{/b}! )"

            hide player with dissolve

    elif M_roxxy.is_state(S_roxxy_get_uniform_on_doggo):
        if not player.has_item("roxxy_uniform") and destination not in [L_trailerpark, L_trailer_shack]:
            if destination == L_trailer_shack_interior:
                scene expression player.location.background_blur
                player_name "( Hmm, that {b}pig{/b} should be around here somewhere... )"

                return
            else:
                show player 12 with dissolve
                player_name "I'm supposed to {b}look for Clyde's pig{/b}."

                show player 10
                player_name "I should probably check around his {b}Shack{/b}."

                hide player with dissolve
        elif destination not in [L_trailerpark, L_trailer] and player.has_item("roxxy_uniform"):
            show player 10 with dissolve
            player_name "I'm supposed to follow {b}Roxxy{/b} back to {b}her trailer{/b}."

            hide player with dissolve
        else:
            if destination in [L_trailer_interior, L_trailer_bedroom, L_trailer_shack_interior]:
                $ playSound()
                play audio sfxDoor()
            return
    elif M_roxxy.is_state(S_roxxy_beat_clyde) and destination not in [L_trailerpark, L_trailer_tractor]:
        show player 10 with dissolve
        player_name "Hmm, I should {b}follow Roxxy{/b}..."

        player_name "She said something about a {b}Tractor{/b}?"

        hide player with dissolve
    elif M_roxxy.is_state(S_roxxy_wait_in_her_room) and destination not in [L_trailer, L_trailer_interior, L_trailer_bedroom]:
        if destination == "roxxy_trailer_button":
            show player 5 at left
            show old_roxxy 1 at right
            with dissolve
            player_name "..."
            show old_roxxy 3c
            roxxy "Seriously, quit staring at me and go wait in my room!"

            show old_roxxy 1b
            roxxy "I'll be there in a minute."

            show old_roxxy 1
            show player 10
            player_name "Ya baiklah."

            hide old_roxxy
            hide player
            with dissolve
        else:
            show player 14 with dissolve
            player_name "I'm supposed to wait for {b}Roxxy{/b} in her room."

            hide player with dissolve
    elif M_roxxy.is_state(S_roxxy_confront_clyde) and destination not in (L_trailerpark, L_trailer_tractor, L_trailer_shack):
        show player 10 with dissolve
        player_name "( {b}Roxxy{/b} took off after {b}Clyde{/b}! )"

        player_name "( I should find them before {b}Roxxy{/b} murders him! )"

        hide player with dissolve
    elif M_roxxy.is_state(S_roxxy_picnic_done) and destination != L_trailer_bedroom:
        show player 13 at left
        show player_wet at left
        with dissolve
        player_name "( I should go dry off with {b}Roxxy{/b} inside her room! )"

        hide player
        hide player_wet
        with dissolve
    elif L_trailer_shack_interior.locked and destination == L_trailer_shack_interior:
        player_name "I can't go there now."

    else:
        if destination in [L_trailer_interior, L_trailer_bedroom, L_trailer_shack_interior]:
            $ playSound()
            play audio sfxDoor()
        return

    return True
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
