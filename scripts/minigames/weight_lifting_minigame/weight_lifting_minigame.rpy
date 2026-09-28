label weightlifting_dialogue:
    if player.location.is_here(M_kevin):
        scene expression background(0, 440, 2.5) as stage
        show player 1 at left with dissolve
        show old_kevin 9 at right with dissolve
        kevin "Hey there, bud!"
        show old_kevin 8 at right
        show player 14 at left
        player_name "Hey {b}Kevin{/b}!"
        show old_kevin 10 at right
        show player 11 at left
        kevin "You ready to lift some lead, bro?"
        menu:
            "Yeah, bro!":
                show player 17 at left
                show old_kevin 8 at right
                player_name "Yeah, bro!"
                show old_kevin 9 at right
                show player 11 at left
                kevin "You have to start with some light reps!"
                show old_kevin 8 at right
                show player 12 at left
                player_name "What exercise are we doing?"
                show old_kevin 13 at right
                show player 24 at left
                kevin "Take those light dumbbells..."
                show old_kevin 9 at right
                show player 85 at left
                if player.stats.str() < 3:
                    show player 85 at left
                elif player.stats.str() < 7:
                    show player 307 at left
                else:
                    show player 308 at left
                kevin "We're gonna do some {b}shoulder presses{/b}!!"
                hide player 85 at left
                hide player 307 at left
                hide player 308 at left
                hide old_kevin 9 at right
                with dissolve
                jump weightlifting
            "Can't right now.":

                show player 10 at left
                show old_kevin 8 at right
                player_name "I can't, right now."
                player_name "I gotta do something else first..."
                show old_kevin 9 at right
                show player 1 at left
                kevin "No worries, bro!"
                show old_kevin 11 at right
                show player 84 at left
                kevin "I'll see you next time, bro!"
                player_name "See ya!"
                hide player 84 at left with dissolve
                hide old_kevin 11 at right with dissolve
                jump gym_dialogue


            "Skip minigame. (Cheat)" if game.cheat_mode:
                call popup ('str', True)
                $ player.increase_str()
                $ game.timer.tick()
                jump gym_dialogue
    else:
        scene expression game.timer.image("training{}_b")
        show player 3 at left with dissolve
        player_name "( Oh man, {b}Kevin{/b} isn't here. )"
        show player 34 at left
        if game.timer.is_weekend():
            player_name "( Perhaps he is at home... )"
        else:
            player_name "( I bet {b}he's hanging out at the cafeteria{/b}. )"
        hide player with dissolve
        $ game.main()

label weightlifting:
    call screen weightlifting with fade
    return

label weightlifting_done:
    scene weightlifting03
    $ renpy.checkpoint()
    $ renpy.pause()
    scene expression background(0, 440, 2.5) as stage
    show anon

    if player.location.is_here(M_kevin):
        show old_kevin 10 at right
        with fade
        kevin "Way to go, bro!"
        show old_kevin 8 with dissolve
        anon "Phew, that was tough!"
        show old_kevin 9
        kevin "You're looking stronger already!"
        show old_kevin 8
        anon @ f_laugh "Heh, thanks, {b}Kevin{/b}."
        show old_kevin 9
        kevin "Come back tomorrow, and we'll up the weight a bit."
        show old_kevin 8
    else:
        with fade
        anon @ -m_talk "( Turns out, pretty hard! )"
        anon f_surprised @ f_grin "( I definitely feel stronger though! )"
        anon @ -m_talk "( I'll need to find someone to spot me in future. )"
        anon @ -m_talk "( Don't want any accidents! )"

    hide anon with dissolve
    call popup ('str', True)
    $ player.increase_str()
    $ game.timer.tick()

    jump gym_dialogue

label weightlifting_fail:
    scene weightlifting04
    $ renpy.checkpoint()
    $ renpy.pause()
    scene expression background(0, 440, 2.5) as stage
    show anon f_tired

    if player.location.is_here(M_kevin):
        show old_kevin 11b at right
        with fade
        kevin "Whoa!"
        kevin "You alright, bro?!"
        show old_kevin 8 with dissolve
        anon "Y-yeah, I think so."
        anon "Sorry, I don't know what happened..."
        show old_kevin 9
        kevin "I can back you down a few pounds..."
        show old_kevin 8
        anon f_skeptical "No, I can do it!"
        show old_kevin 9
        kevin "You're sure?"
        show old_kevin 8
        anon f_normal "I'm positive!"
        show old_kevin 9
        kevin "Heh, right on bro!"
        show old_kevin 10 with dissolve
        kevin "You're gonna be a beefcake in no time with an attitude like that!"
        show old_kevin 8
    else:
        with fade
        anon @ -m_talk "( Turns out, pretty hard... )"
        anon @ -m_talk "( Maybe if I keep trying... )"

    hide anon with dissolve
    call popup ('str', False)
    $ game.timer.tick()

    jump gym_dialogue
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
