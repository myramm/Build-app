label pushups_minigame_win:
    scene gym with fade
    if M_roxxy.is_state(S_roxxy_do_pushups):
        show player 13 at left
        show bridget a_crossed:
            flip
            xoffset 150
        show old_dexter 42 at right
        with dissolve
    else:

        show player 109f at left
        with dissolve

    $ renpy.pause(1, hard = True)

    if M_roxxy.is_state(S_roxxy_do_pushups):
        dexter "{i}*Gasp*{/i} Eugh..."

        show old_dexter 42b
        bridget "You alright, {b}Dexter{/b}?"

        bridget "You don't look so good..."

        hide old_dexter
        show player 106
        dexter "{i}*Gaahhh*{/i}!!!" with hpunch
        show bridget b_bend f_angry_down with dissolve
        dexter "..."
        bridget "... {b}Dexter{/b}?"

        dexter "..."
        show bridget b_dressed a_crossed f_normal with dissolve
        bridget "It looks like {b}[firstname]{/b} is the winner!"

        show old_erik 4 at right with dissolve
        erik "That was awesome, dude!"

        erik "You destroyed him!"

        show old_erik 1
        dexter "..."
        show player 108f
        player_name "... Is he alright?"

        show player 109f
        show old_erik 50
        erik "..."
        bridget "Psh, he'll be fine."

        bridget "You know, {b}[firstname]{/b}, you should really come try out for the basketball team."

        show old_erik 51
        show player 108f
        player_name "Benar-benar?"

        show player 109f
        bridget "Yeah! I could use a player with your... Stamina."

        show player 10
        player_name "Y-yeah... Maybe."

        player_name "I'll think about it, {b}Coach{/b}..."

        show player 5
        bridget "Well, you know where to find me."

        hide bridget with dissolve
        show old_erik 5
        erik "... That was weird."

        show old_erik 1
        show player 14
        player_name "Heh, yeah. {b}Coach Bridget{/b} actually said something nice to me..."

        show player 13
        show old_erik 4
        erik "Well, you did just slay an Ogre..."

        show old_erik 1
        show player 17
        player_name "Ha ha ha!"

        show player 14
        dexter "{i}* Merengek*{/i}"

        show old_erik 50
        erik "..."
        show player 14
        player_name "C'mon, let's get out of these clothes."

        show player 13
        show old_erik 5
        erik "Tepat di belakangmu."

        hide player
        hide old_erik
        with dissolve
        dexter "..."
        $ M_roxxy.trigger(T_roxxy_beaten_dexter_pushups)
    else:

        dexter "..."
        show player 108f
        player_name "{b}Dexter{/b}?"

        show player 109f
        dexter "..."
        show player 109f
        player_name "{i}*Sigh*{/i} I dunno why you do this to yourself..."

        show player 108f
        dexter "{i}* Merengek*{/i}"

        hide player with dissolve
        dexter "..."
    $ game.timer.tick()
    $ player.go_to(L_map)
    $ game.main()

label pushups_minigame_lose:


    scene gym with fade
    if M_roxxy.is_state(S_roxxy_do_pushups):
        show player 25 at left
        show bridget a_crossed:
            flip
            xoffset 150
        show old_dexter 11 at right
        with dissolve
        player_name "{i}*Wheeze*{/i} Can't... Breathe..."

        show old_dexter 12
        dexter "Ha ha ha ha!"

        show old_dexter 11
        bridget "It looks like {b}Dexter{/b} is the winner!"

        show old_dexter 12
        dexter "This little nerd never stood a chance..."

        show old_dexter 11
        bridget "Keep things civil you two!"

        hide bridget with dissolve
        show old_dexter 12
        dexter "Guess I don't have to worry about you and {b}Roxxy{/b}..."

        dexter "... She doesn't date losers."

        show old_dexter 11
        show player 24
        player_name "..."
        show old_dexter 12
        dexter "Ha ha ha ha!"

        show old_dexter 11
        show player 25
        player_name "Whatever, {b}Dexter{/b}. You just got lucky is all..."

        show old_dexter 12
        dexter "Ha ha ha ha!"

        show old_dexter 11
        show player 15
        player_name "Grr... I'll get you next time."

        show player 16
        show old_dexter 28 with dissolve
        dexter "Bring it on, loser!"

        dexter "I'll beat you every time."

        hide old_dexter with dissolve
        show player 5
        player_name "( Crap! This is going to be all over school now. )"

        player_name "( I need to show everyone that I'm not afraid to stand up to {b}Dexter{/b}! )"

        player_name "( ... Otherwise, {b}Roxxy{/b} will never take me seriously. )"

        hide player with dissolve
    else:

        show player 24 at left
        show old_dexter 12 at right
        with dissolve
        dexter "Ya!"

        dexter "I win, loser!"

        show old_dexter 11
        show player 25
        player_name "Psh, who cares?"

        hide player with dissolve
        show old_dexter 12
        dexter "Haha!"

        show old_dexter 15 with dissolve
        dexter "... Wait... What?!"

        dexter "Kemana kamu pergi?!"

        dexter "... Get back here and let me laugh in your face!"

        show old_dexter 14
        dexter "..."
        dexter "Grr..."

        hide old_dexter with dissolve
    $ game.timer.tick()
    $ player.go_to(L_map)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
