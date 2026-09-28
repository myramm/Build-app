label basketball_minigame_prepare_but_with_a_background_this_time:
    scene basketball_b
label basketball_minigame_prepare:
    if M_roxxy.get("basketball unlocked"):
        if game.cheat_mode:
            menu:
                "Skip minigame. (Cheat)":
                    jump basketball_success
                "Play minigame.":

                    call screen basketball_minigame
        else:

            call screen basketball_minigame
    else:

        scene expression L_basketball_court.background_blur
        show player 16 at left
        show old_dexter 4 at right
        dexter "What do you think you're doing?!"
        dexter "This court is for men, not skinny little losers!"
        show old_dexter 6
        dexter "Get lost!"
        player_name "( Grr, he's such an asshole! )"
        player_name "( One day, he's gonna get what's coming to him... )"
    $ player.go_to(L_basketball_court)
    $ game.main()

label basketball_success:
    if M_roxxy.is_state(S_roxxy_basketball_challenge) and (game.timer.is_afternoon() or not M_roxxy.is_set("done basketball")):
        scene location_basketball_cutscene02
        show text _ ("I was on fire!\nPractically running circles around {b}Dexter{/b}...") as caption
        with fade
        pause
        hide caption with dissolve
        show text _ ("Swiping the ball and sinking threes before he could even take a step.") as caption with dissolve
        pause

        scene location_basketball_cutscene03
        show text _ ("... And then it happened.") as caption
        with fade
        pause
        hide caption with dissolve
        show text _ ("I faked left, then faked right, and then blew past him!\n{b}Dexter{/b} grunted, stumbling over his own feet and crashing to the ground.") as caption with dissolve
        pause
        hide caption with dissolve
        show text _ ("I've no idea how he managed to lose his pants though...") as caption with dissolve
        pause

        scene basketball_b
        show chad f_happy:
            flip
            xoffset 225
        show tyrone:
            flip
        show old_dexter 43b at right
        show old_kevin 35f at left
        with fade
        tyrone "Oh, shit son!"
        tyrone "{b}[firstname]{/b} just juked that fool so hard his pants came off!"
        chad "That was doooope, yo!"
        show old_kevin 36f with dissolve
        kevin "... What the hell is that?"
        chad f_normal_down "Huh?"
        show tyrone f_surprised_down
        kevin "What is that?!"
        tyrone f_uneasy_down a_hands_rub @ a_idle "... Is that his dick?!"
        show old_dexter 43
        kevin "I dunno bro, I can't tell..."
        show old_kevin 36bf
        kevin "... Did anybody bring a magnifying glass?!"
        chad f_laugh "Hahahaha! It looks like a belly button!"
        tyrone f_smirk a_idle @ f_laugh "Hahaha, yeah man! With two tiny little nuts hanging off it!"
        show chad f_normal
        show old_dexter 43c
        dexter "Shut up, you guys!"
        show old_dexter 43b with hpunch
        show old_kevin 32f with dissolve
        kevin "Hahaha, {b}Dexter{/b} has a tiny penis!"
        bridget "Alright, that's enough!"
        hide old_kevin
        hide chad
        hide tyrone
        with dissolve
        tyrone "He's smaller than tiny, dawg..."
        tyrone "That's a straight up {i}micropenis{/i}!"
        show bridget a_crossed f_normal:
            flip
            xoffset 100
        with dissolve
        bridget "What's all the commotion abo-"
        bridget f_laughing_hold a_laugh "!!!"
        show old_dexter 44 with dissolve
        dexter "!!!"
        bridget "..."
        show old_dexter 44c
        dexter "Stop laughing!"
        dexter "Don't you know who I am?!"
        dexter "Nobody laughs at me!"
        show old_dexter 45
        show player 649 at left with dissolve
        player_name "Hey, {b}Dexter{/b}..."
        player_name "Your ball, bitch!"
        show player 664
        show old_dexter 45b
        with dissolve
        pause
        show player 91
        bridget f_laugh a_hips "PFFFT, HAHAHAHAHA!"
        hide bridget with dissolve
        show old_dexter 45c
        dexter "GRR, FUCK ALL OF YOU!" with hpunch
        show player 11
        dexter "{b}[firstname]{/b}, you are fucking dead!"
        dexter "YOU HEAR ME?!" with hpunch
        dexter "DEAD!"
        show old_dexter 46 with dissolve
        pause 1
        hide old_dexter with dissolve
        pause
        show old_kevin 32 at Position (xpos=700)
        show old_erik 1 at right
        with dissolve
        kevin "Yo, {b}Dexter{/b}! You forgot your pants, bro!!"
        kevin "Hahaha!"
        erik "..."
        kevin "{b}[firstname]{/b} that was the funniest thing I've ever seen!"
        show old_kevin 23
        show player 14
        player_name "Heh, yeah?"
        show player 13
        show old_kevin 9b
        kevin "For real, bro!"
        show old_kevin 23
        show old_erik 5
        erik "... It was so tiny."
        show old_erik 1
        show old_kevin 32
        kevin "Hahaha, yeah it was!"
        kevin "Oh my god! This is gonna spread like wildfire!"
        show old_kevin 23
        show player 12
        player_name "... Yeah."
        player_name "{i}*Sigh*{/i} There's no way to avoid it now."
        show player 5
        show old_erik 5
        erik "What do you mean?"
        show old_erik 52
        show player 10
        player_name "{b}Dexter{/b}'s gonna want blood after this..."
        player_name "I'll have to fight him next time for sure."
        show player 5
        show old_erik 5
        erik "Yeah, I think you're right about that."
        show old_erik 52
        show old_kevin 24
        kevin "You better {b}hit the gym and prepare yourself{/b}."
        show old_kevin 23
        show player 12
        player_name "That's a good idea."
        show player 5
        show old_kevin 24
        kevin "You let me know if you need some help, yeah?"
        show old_kevin 23
        show player 14
        player_name "Thanks, {b}Kevin{/b}."
        show player 13
        show old_kevin 24
        kevin "No problem, bro."
        hide old_kevin with dissolve
        show old_erik 5
        erik "... C'mon, let's hit the showers."
        show old_erik 3
        erik "I think I need to change my pants after all that!"
        show old_erik 2 with dissolve
        show player 17
        player_name "Haha, right behind you."
        hide player
        hide old_erik
        with dissolve
        call popup ('minigame', 'basketball')
        $ M_roxxy.trigger(T_roxxy_humiliated_dexter)
        $ M_roxxy.set("done basketball", True)
    else:

        scene basketball_b
        show player 10
        player_name "That wasn't too bad... I should probably train some more to get even better at this."
    $ game.timer.tick()
    $ player.go_to(L_basketball_court)
    $ game.main()

label basketball_fail:
    if M_roxxy.is_state(S_roxxy_basketball_challenge) and (game.timer.is_afternoon() or not M_roxxy.is_set("done basketball")):
        if M_roxxy.get("done basketball"):
            scene basketball_b
            show bridget a_crossed:
                flip
                xoffset 100
            show player 24 at left
            show old_dexter 32 at right
            with dissolve
            dexter "Yeah, that's right you little bitch!"
            dexter "You can't hang with {b}Dexter{/b}!"
            dexter "{b}Roxxy{/b} should be embarrassed, kissing a loser like you!"
            show old_dexter 31
            player_name "..."
            show old_dexter 32
            dexter "Hahahahaha!"
            show old_dexter 31
            bridget "Alright, that's enough."
            show old_dexter 29 with dissolve
            bridget "{b}Dexter{/b} you were fouling left and right out there."
            show player 11
            show old_dexter 30
            dexter "What?! Not this again. I wasn't-"
            show old_dexter 29
            bridget @ f_angry "That was clearly charging!"
            show old_dexter 2 with dissolve
            bridget "{i}*Sigh*{/i} Do we have to discuss the rules again?!"
            show old_dexter 8
            dexter "... No."
            show old_dexter 2
            bridget "I'm afraid I'll have to disqualify you and give the win to {b}[firstname]{/b}."
            show old_dexter 8
            dexter "That's bullshit!"
            show old_dexter 2
            show player 10
            player_name "... No."
            show player 12
            player_name "I don't want to win on a technicality."
            show player 90
            show old_dexter 8
            dexter "A techni- Whaaa?"
            show old_dexter 2
            bridget "You're sure, {b}[firstname]{/b}?"
            show player 12
            player_name "I'm sure."
            show player 90
            bridget "Very well."
            bridget "I guess we'll just have to play another game tomorrow."
            show old_dexter 30 with dissolve
            dexter "Pssh, fine with me!"
            show old_dexter 32 with dissolve
            dexter "I could beat this loser blind folded and with one hand tied behind my back..."
            show old_dexter 31
            show player 12
            player_name "Yeah, we'll see..."
            show player 90
            bridget "We'll {b}meet here tomorrow afternoon{/b} for the rematch."
            show old_dexter 32
            dexter "Hah, see you then."
            show player 647
            show old_dexter 33
            with dissolve
            dexter "Bitch."
            hide old_dexter with dissolve
            show player 648 with dissolve
            pause
            hide bridget
            show bridget a_crossed
            with dissolve
            player_name "..."
            bridget "Practice, {b}[firstname]{/b}!"
            bridget "He's not going to keep falling for my excuses..."
            player_name "Hmm?"
            bridget "I expect a better performance tomorrow."
            show player 649
            player_name "Y-yes, ma'am."
            show player 648
            hide bridget with dissolve
            player_name "..."
            show player 649
            player_name "I should probably practice more."
            hide player with dissolve
        else:

            scene location_basketball_cutscene01
            show text _ ("There's a reason {b}Dexter{/b} was made captain of the basketball team.\nHe overpowered me at every turn...") as caption
            with fade
            pause
            hide caption with dissolve
            show text _ ("Defensively he was like a wall, I just couldn't get past him!\nHe was slow though and clumsy if I got a step on him.") as caption with dissolve
            pause
            hide caption with dissolve
            show text _ ("There were opportunities and with a little practice, I'm sure I can beat him!") as caption with dissolve
            pause

            scene basketball_b
            show bridget a_crossed:
                flip
                xoffset 100
            show player 24 at left
            show old_dexter 3 at right
            with fade
            dexter "Yeah, that's right you little bitch!"
            dexter "You can't hang with {b}Dexter{/b}!"
            show old_dexter 6 with dissolve
            dexter "{b}Roxxy{/b} should be embarrassed, kissing a loser like you!"
            show old_dexter 3 with dissolve
            dexter "Hahahahaha!"
            player_name "..."
            show player 27
            bridget "Alright, that's enough."
            show old_dexter 2
            bridget "{b}Dexter{/b} you were fouling left and right out there."
            show player 11
            show old_dexter 8
            dexter "What?! No, I wasn't..."
            show old_dexter 2
            bridget @ f_angry "Yes, you were! I counted no less than a dozen personal fouls and a couple were pretty flagrant."
            bridget "I'm afraid I'll have to disqualify you and give the win to {b}[firstname]{/b}."
            show old_dexter 6 with dissolve
            dexter "That's not fair!"
            show old_dexter 2 with dissolve
            show player 12
            player_name "... No."
            player_name "I don't want to win on a technicality."
            show player 5
            show old_dexter 8
            dexter "A techni- Whaaa?"
            show old_dexter 2
            bridget "You're sure, {b}[firstname]{/b}?"
            show player 10
            player_name "I'm sure."
            show player 5
            bridget "Very well."
            bridget "I guess we'll just have to play another game tomorrow."
            show old_dexter 3
            dexter "Pssh, fine with me!"
            dexter "I could beat this loser blind folded and with one hand tied behind my back..."
            show old_dexter 1
            show player 12
            player_name "Yeah, we'll see..."
            show player 90
            bridget "We'll {b}meet here tomorrow afternoon{/b} for the rematch."
            show old_dexter 3
            dexter "Hah, see you then."
            show player 647
            show old_dexter 33
            with dissolve
            dexter "Bitch."
            hide old_dexter with dissolve
            show player 5 with dissolve
            player_name "..."
            hide bridget
            show bridget a_crossed
            with dissolve
            bridget "I suggest you practice, {b}[firstname]{/b}!"
            bridget "He might not fall for that again..."
            player_name "Hmm?"
            bridget "I expect a better performance tomorrow."
            show player 10
            player_name "Y-yes, ma'am."
            show player 5
            hide bridget with dissolve
            player_name "..."
            show player 109f
            erik "Uuhhhh..."
            show player 108f
            player_name "{i}*Sigh*{/i} I should get him to the locker room."
            player_name "... I hope he's got a change of pants here at school."
            hide player with dissolve
            call popup ('minigame', 'basketball')
            $ M_roxxy.set("done basketball", True)
    else:

        scene basketball_b
        show player 10
        player_name "Damn, I failed again... I should probably train some more to get better at this."
    $ game.timer.tick()
    $ player.go_to(L_basketball_court)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
