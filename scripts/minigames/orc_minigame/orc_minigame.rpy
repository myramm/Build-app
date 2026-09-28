label orc_battle_start:
    call screen orc_battle

label orc_battle_finish:
    $ player.go_to(L_home_bedroom)
    scene expression "backgrounds/location_erik_minigame07b.jpg"
    scene expression "backgrounds/location_erik_minigame07c.jpg" with dissolve
    pause .7
    scene expression "backgrounds/location_erik_minigame07d.jpg" with dissolve
    pause 1
    scene expression Animation("backgrounds/location_erik_minigame07e.jpg", 0.5, "backgrounds/location_erik_minigame07f.jpg", 0.5) with fade
    pause
    $ game.timer.tick()
    if not M_june.finished_state(S_june_date_done):
        scene bedroom_sex2
        if M_june.finished_state(S_june_date_shame):
            show june_sitting 9 at center
            with fade
            player_name "..."
            show june_sitting 13 at Position(xpos=300,ypos=787)
            show player_sitting 4 at right
            with dissolve
            player_name "Uhh..."
            show june_sitting 12
            show player_sitting 5
            june "Looks like we got the same ending again."
            show player_sitting 3
            june "Sorry..."
            show june_sitting 13
            show player_sitting 4
            player_name "Nah, it's okay!"
            show june_sitting 12
            show player_sitting 5
            june "Do you still think it's weird?"
            show june_sitting 13
        else:

            show june_sitting 9 at center
            with fade
            player_name "..."
            show june_sitting 13 at Position(xpos=300,ypos=787)
            show player_sitting 4 at right
            with fastdissolve
            player_name "Uhh..."
            show june_sitting 12
            show player_sitting 5
            june "I... I didn't know that's how the game ends, I swear!"
            show june_sitting 13
            show player_sitting 4
            player_name "That was... Unexpected?"
            show june_sitting 12
            show player_sitting 3
            june "This is so embarrassing..."
            show june_sitting 13
            show player_sitting 4
            player_name "Nah, it's okay!"
            show june_sitting 12
            show player_sitting 5
            june "You didn't find that too weird?"
            show june_sitting 13

        menu:
            "It's gross." if not M_june.finished_state(S_june_date_shame):
                $ M_june.trigger(T_june_date_lame)
                show june_sitting 13 at Position(xpos=300,ypos=787)
                show player_sitting 4 at right
                player_name "I dunno... It's kind of gross?"
                show player_sitting 5
                june "..."
                show player_sitting 6
                player_name "But, whatever, it's fine."
                show player_sitting 1
                show june_sitting 12
                june "I'm sorry... If I had known..."
                june "Do you still want to play the game with me though?"
                show player_sitting 2
                show june_sitting 13
                player_name "Yeah, it's fun!"
                show player_sitting 1
                show june_sitting 12
                june "Thanks... Anyway, I really should get going, it's getting late."
                show player_sitting 2
                show june_sitting 11
                player_name "Okay!"
                player_name "Have a good night!"
                show player_sitting 1
                show june_sitting 10
                june "You too, {b}[firstname]{/b}."

            "Do you?" if M_june.finished_state(S_june_date_shame):
                show player_sitting 4 at right
                player_name "What did you think of it?"
                show player_sitting 3
                show june_sitting 13
                june "..."
                show player_sitting 4
                player_name "It sort of felt like perhaps you liked it?"
                show player_sitting 3
                player_name "..."
                show player_sitting 4
                player_name "A bit?"
                show player_sitting 3
                show june_sitting 12
                june "A bit... I mean... I kinda..."
                show june_sitting 13
                jump orc_shame_redemption

            "It's hot!" if not M_june.finished_state(S_june_date_shame):
                show player_sitting 2 at right
                show june_sitting 11 at Position(xpos=300,ypos=787)
                player_name "Nah, it's actually kind of funny..."
                player_name "... And kind of hot."
                show june_sitting 10
                show player_sitting 1
                june "Really? You... Think so?"
                show june_sitting 11
                show player_sitting 2
                player_name "Yeah, I guess orcs can be pretty sexy!"
                label orc_shame_redemption:
                show player_sitting 1
                june "..."
                show june_sitting 10
                june "I... I love orcs..."
                show player_sitting 5
                june "In fact, I was actually planning on cosplaying as one soon..."
                show player_sitting 2
                show june_sitting 11
                player_name "An orc costume? What for?"
                show player_sitting 1
                show june_sitting 10
                june "I was planning on going to a comic convention dressed as an orc..."
                show june_sitting 12
                june "... But there's a problem."
                june "I don't think I can find all the costume pieces in time."
                show player_sitting 2
                show june_sitting 11
                player_name "That sounds cool!"
                show player_sitting 1
                show june_sitting 10
                june "You think so?"
                show player_sitting 2
                show june_sitting 11
                player_name "What is it you're missing?"
                show player_sitting 1
                show june_sitting 10
                june "I have the body paint... But I need the fake ears, the teeth and... The belt."
                show player_sitting 2
                show june_sitting 11
                player_name "I bet I could find those for you!"
                show player_sitting 1
                show june_sitting 10
                june "Really? You would do that for me??"
                show player_sitting 2
                show june_sitting 11
                player_name "I can try!"
                show player_sitting 6
                player_name "I think you'd look amazing as an orc!"
                show player_sitting 1
                june "..."
                show player_sitting 3
                show june_sitting 10
                june "That's really sweet. Thanks, {b}[firstname]{/b}."
                show player_sitting 2
                show june_sitting 11
                player_name "Well, I should probably go to bed..."
                show player_sitting 1
                show june_sitting 10
                june "Yeah, I should get home too..."
                june "Thanks for having me over! It was fun."
                show player_sitting 6
                show june_sitting 11
                player_name "Yeah, it really was."
                show player_sitting 1
                show june_sitting 10
                june "Let me know if you ever find those costume parts!"
                june "See you tomorrow?"
                show player_sitting 2
                show june_sitting 11
                player_name "Sure!"
                player_name "Come on, I'll see you out."
                scene bedroom_night
                show player 35
                with fade
                player_name "Hmm... I wonder where I could find those {b}costume parts{/b}."
                player_name "Maybe I should {b}go check at the mall{/b}?"
                show player 55 at Position(xoffset=12)
                player_name "{i}*Yawn*{/i}"
                show player 56
                player_name "I'll go tomorrow, I need some sleep..."
                hide player with dissolve
                $ M_june.trigger(T_june_date_request)
    else:

        scene bedroom_sex2
        show june_sitting 2 at Position(xpos=300,ypos=787)
        show player_sitting 1 at right
        with fade
        june "Finally! I've been trying to beat this one for days..."
        show june_sitting 3
        june "You're getting really good at this."
        show june_sitting 4
        show player_sitting 6
        player_name "Yeah, I guess that game really is addicting!"
        show june_sitting 1
        show player_sitting 2
        player_name "Hey, what's the time?"
        show june_sitting 5
        show player_sitting 5
        june "Oh crap, it's past midnight..."
        show june_sitting 6
        show player_sitting 4
        player_name "Oh, we've been here longer than I thought..."
        player_name "Looks like we lost track of time."
        show june_sitting 5
        show player_sitting 1
        june "I should get home, my parents are probably worried sick."
        show june_sitting 3
        june "Thanks for the evening, {b}[firstname]{/b}."
        show june_sitting 4
        show player_sitting 2
        player_name "See you at school?"
        show player_sitting 1
        show june_sitting 3
        june "You bet!"

    jump resume_sleeping_bedroom

label orc_battle_fail:
    $ M_june.trigger(T_june_date_lost)
    $ player.go_to(L_home_bedroom)
    $ game.timer.tick()
    scene bedroom_sex2
    show june_sitting 4 at Position(xpos=300,ypos=787)
    show player_sitting 4 at right
    with fade
    player_name "Oops..."
    show player_sitting 3
    show june_sitting 3
    june "Huh, I guess we'll need to practice a bit."
    show player_sitting 4
    show june_sitting 4
    player_name "Haha, sorry."
    show player_sitting 3
    show june_sitting 3
    june "It's okay, I'm sure we'll beat it eventually!"
    show player_sitting 6
    show june_sitting 4
    player_name "I hope so! Otherwise, I'm a terrible teammate..."
    show player_sitting 1
    show june_sitting 3
    june "Anyway, I should get going, it's starting to get pretty late."
    june "Let me know if you want to play again tomorrow!"
    show player_sitting 2
    show june_sitting 4
    player_name "Okay!"
    player_name "Have a good night!"
    show player_sitting 1
    show june_sitting 3
    june "You too, {b}[firstname]{/b}."
    jump resume_sleeping_bedroom
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
