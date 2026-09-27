label shooting_range_dialogue:
    if M_roxxy.finished_state(S_roxxy_beat_clyde) and L_trailer_tractor.is_here(M_clyde):
        show player 14f at right
        player_name "Ingin mencapai jangkauannya?"

        show player 13f
        show clyde 4 at left
        clyde "Psh, you know I do!"

        clyde "I'm always in the mood to drink beer and shoot stuff!"

        show clyde 9 with dissolve
        clyde "You wanna make it interestin'?"

        show clyde 3 with dissolve
        menu:
            "$100." if player.has_money(100):
                show clyde 4
                clyde "No problem, brother!"

                clyde "Get that wallet ready, now!"

                clyde "Wooooo!"

                show clyde 8 with dissolve
                $ player.spend_money(100)
                $ player.earnings = 100
                jump shooting_minigame_prepare
            "$200." if player.has_money(200):
                show clyde 4
                clyde "No problem, brother!"

                clyde "Get that wallet ready, now!"

                clyde "Wooooo!"

                show clyde 8 with dissolve
                $ player.spend_money(200)
                $ player.earnings = 200
                jump shooting_minigame_prepare
            "$400." if player.has_money(400):
                show clyde 4
                clyde "Uh oh, we got a big spender here!"

                clyde "Look out ladies, {b}[firstname]{/b} is flush and lookin' fer action!"

                show clyde 3
                show player 14f
                if M_clyde.get("cletus"):
                    player_name "Heh, shut up and shoot, {b}Cletus{/b}!"

                else:
                    player_name "Heh, shut up and shoot, {b}Clyde{/b}!"

                show player 13f
                show clyde 4
                clyde "Hahaha, you got it, brother!"

                show clyde 8 with dissolve
                $ player.spend_money(400)
                $ player.earnings = 400
                jump shooting_minigame_prepare
            "Sudahlah.":
                show player 12f
                player_name "Sebenarnya, sudahlah."

                show player 10f
                player_name "Maybe some other time?"

                show player 5f
                show clyde 4
                clyde "Psh, hell yeah!"

                clyde "Anda tahu di mana menemukan saya."

                hide player
                hide clyde
                hide clyde_hat
                with dissolve
                $ game.main()
    else:
        $ pass
    $ game.main()

label shooting_minigame_prepare:
    $ game.failed_minigame_counter = 0
    if not game.cheat_mode:
        if not renpy.variant("mobile"):
            $ config.mouse = {"default": [("buttons/shooting_cursor.png", 48, 49)]}
        call screen shooting_minigame
    else:
        menu:
            "Play minigame.":
                if not renpy.variant("mobile"):
                    $ config.mouse = {"default": [("buttons/shooting_cursor.png", 48, 49)]}
                call screen shooting_minigame
            "Skip minigame. (Cheat)":
                $ M_roxxy.set("lost shooting", True)
                jump shooting_range_success


label shooting_range_fail:
    $ config.mouse = None
    $ game.failed_minigame_counter += 1
    if M_roxxy.is_state(S_roxxy_beat_clyde):
        if M_roxxy.get("lost shooting"):
            call expression game.dialog_select("shooting_range_fail_repeat")
        else:
            call expression game.dialog_select("shooting_range_fail_first")
            $ M_roxxy.set("lost shooting", True)
        if game.failed_minigame_counter <=3:
            jump shooting_minigame_prepare
        else:
            menu:
                "Retry.":
                    jump shooting_minigame_prepare
                "Skip.":
                    jump shooting_range_success
    elif player.earnings != 0:
        show player 5f at right
        show clyde 4 at left
        if M_clyde.get("cletus"):
            show clyde_hat at left
        with dissolve
        clyde "Tough luck, brother..."

        if M_clyde.get("cletus"):
            clyde "... But you shoulda known better than to test yer might against {b}Cletus Delmont{/b}!!!"

        else:
            clyde "... But you shoulda known better than to test yer might against {b}Clyde Delmont{/b}!!!"

        clyde "Hahaha, now pay up!"

        show clyde 3
        show player 174bf with dissolve
        player_name "..."
        show player 5f with dissolve
        show clyde 4
        clyde "Wanna go again?"

        show clyde 3
        menu:
            "Ya.":
                show player 14f
                if M_clyde.get("cletus"):
                    player_name "You're going down, {b}Cletus{/b}!"

                else:
                    player_name "You're going down, {b}Clyde{/b}!"

                show player 13f
                show clyde 4
                clyde "Heh, this is gon' be the easiest money I ever made!"

                show clyde 3
                jump shooting_range_dialogue
            "Tidak.":
                show player 12f
                player_name "Nah. Maybe some other time."

                show player 5f
                show clyde 4
                clyde "Heh, throwin' in the towel, huh?!"

                clyde "Maybe next time we can skip the shootin' and you can just give me yer money..."

                show clyde 9 with dissolve
                clyde "Whatchu say?"

                show clyde 3 with dissolve
                show player 12f
                if M_clyde.get("cletus"):
                    player_name "Shut up, {b}Cletus{/b}."

                else:
                    player_name "Shut up, {b}Clyde{/b}."

                show player 90f
                show clyde 4
                clyde "Ha ha ha!"

                hide player
                hide clyde
                hide clyde_hat
                with dissolve
                $ game.main()
    $ game.main()

label shooting_range_success:
    $ config.mouse = None
    if M_roxxy.is_state(S_roxxy_beat_clyde):
        if M_roxxy.get("lost shooting"):
            call expression game.dialog_select("shooting_range_success_failed")
        else:
            call expression game.dialog_select("shooting_range_success_first")
        call expression game.dialog_select("shooting_range_success_outro")
        $ game.timer.tick(1)
        $ M_roxxy.trigger(T_roxxy_beaten_clyde)
    elif player.earnings != 0:
        show player 91f at right
        show clyde 26 at left
        if M_clyde.get("cletus"):
            show clyde_hat at left
        with dissolve
        clyde "Dag nabbit!"

        clyde "Yer cheatin' somehow!"

        clyde "I just know it..."

        show clyde 25
        show player 92f
        player_name "Ya benar."

        if M_clyde.get("cletus"):
            player_name "Pay up, {b}Cletus{/b}."

        else:
            player_name "Pay up, {b}Clyde{/b}."

        show player 91f
        show clyde 22
        clyde "{i}*Huh*{/i}"

        show clyde 16 at Position (xoffset=96) with dissolve

        pause
        show clyde 22 with dissolve
        clyde "How 'bout we go again?!"

        show clyde 21
        menu:
            "Ya.":
                show clyde 4 with dissolve
                clyde "Ya, ya!"

                show clyde 26 with dissolve
                clyde "Yer goin' down this time, brother!"

                show clyde 3 with dissolve
                $ player.get_money(player.earnings * 2)
                jump shooting_range_dialogue

            "Double or nothing!" if random.randint(1, 100) <= 10:
                show clyde 4 with dissolve
                clyde "Double or nothing? Count me in!"

                show clyde 26 with dissolve
                clyde "Yer goin' down this time, brother!"

                show clyde 3 with dissolve
                $ player.earnings *= 2
                jump shooting_minigame_prepare
            "Tidak.":

                show clyde 26
                clyde "You ain't even gonna give me the chance to win mah money back?!"

                clyde "Psh, dat's messed up!"

                show clyde 25
                show player 92f
                if M_clyde.get("cletus"):
                    player_name "Better luck next time, {b}Cletus{/b}..."

                else:
                    player_name "Better luck next time, {b}Clyde{/b}..."

                show player 91f
                show clyde 22
                clyde "{i}*Sigh*{/i} Yeah, yeah..."

                clyde "Don't go spendin' it all in one place!"

                hide player
                hide clyde
                hide clyde_hat
                with dissolve
                $ player.get_money(player.earnings * 2)
                $ game.main()
    $ game.main()

label shooting_range_fail_first:
    scene expression "backgrounds/location_trailer_tractor_day_blur.jpg"
    show player 5 at Position (xpos=500)
    show clyde 3 at left
    show old_roxxy 3c at right
    with dissolve
    roxxy "Apakah kamu bercanda?!"

    show old_roxxy 3b
    show player 10
    player_name "Sorry, {b}Roxxy{/b}..."

    show player 5
    show clyde 9 with dissolve
    clyde "Hell yeah! Let's see them beautiful things!"

    show clyde 3 with dissolve
    show old_roxxy 3c
    roxxy "I thought you said you were a good shot?!"

    show old_roxxy 3d
    show player 10
    player_name "... Well, I'm not used to using that rifle!"

    show player 5
    show old_roxxy 30
    roxxy "Ugh... I don't want to do this!"

    show old_roxxy 29
    show clyde 2 with dissolve
    clyde "Hey now! You promised me five seconds!"

    clyde "A deals, a deal and you dun lost!"

    show clyde 4 with dissolve
    clyde "So whip 'em out, girlie!"

    show clyde 3
    roxxy "..."
    show old_roxxy 3
    roxxy "... God, I'm never gonna forgive you for this {b}[firstname]{/b}..."

    show old_roxxy 51
    show old_roxxy_head 55c at right
    with dissolve
    pause
    show old_roxxy 52 with dissolve
    pause
    show old_roxxy 53 with dissolve
    show player 109f
    pause
    show old_roxxy 54 with dissolve
    pause
    hide old_roxxy_head
    show old_roxxy 56c
    with dissolve
    show clyde 4
    clyde "Sweet Jesus!"

    clyde "That's just the pertiest damn thing I ever seen!"

    show clyde 18 with dissolve
    show old_roxxy 56b
    roxxy "Oh. My. God!"

    show old_roxxy 51
    show old_roxxy_head 55c at right
    with dissolve
    show player 5
    pause
    hide old_roxxy_head
    show old_roxxy 31
    with dissolve
    roxxy "That's just disgusting, {b}Clyde{/b}!"

    show old_roxxy 3b
    show player 109 with dissolve
    show clyde 20
    clyde "Ain't mah fault! Dem sweet boobies dun it!"

    show player 22f at Position (xpos=600) with dissolve
    show clyde 19
    show old_roxxy 3
    roxxy "Ugh, I feel like I need a shower now..."

    show old_roxxy 3d
    show clyde 20
    clyde "Welp, I'm happier than a woodpecker in a lumber yard!"

    show clyde 19
    show old_roxxy 3c
    roxxy "Great. Can I have my {b}uniform{/b} now?"

    show old_roxxy 3d
    show clyde 20
    clyde "Nah, I don't think so."

    clyde "Now, if you all could kindly get outta here?"

    clyde "I've got some practicing to do!"

    show clyde 19
    roxxy "..."
    show player 12f
    player_name "Double or nothing!"

    show player 90f
    show old_roxxy 2c
    roxxy "Apa?!"

    show old_roxxy 2b
    show player 12f
    player_name "Double or nothing!"

    player_name "{b}If I win we get the uniform{/b}!"

    show player 90f
    show clyde 20
    clyde "... And when I win?"

    show clyde 19
    show player 12f
    player_name "{b}Roxxy{/b} will let you look for ten seconds!"

    show player 114f
    show old_roxxy 31
    roxxy "Apa-apaan ini, {b}[firstname]{/b}?!"

    show old_roxxy 3b
    show player 113f
    player_name "He's already seen them once..."

    show player 5f
    show clyde 20
    clyde "I like yer style, {b}[firstname]{/b}!"

    clyde "I'm in fer double!"

    show clyde 19
    show old_roxxy 3
    roxxy "... You guys are both assholes!"

    show old_roxxy 3d
    show player 113f
    player_name "I won't lose twice."

    show player 114f
    show old_roxxy 30
    roxxy "... Ugh, whatever."

    hide old_roxxy
    hide player
    hide clyde
    with dissolve
    return

label shooting_range_fail_repeat:
    scene expression "backgrounds/location_trailer_tractor_day_blur.jpg"
    show player 5 at Position (xpos=500)
    show clyde 3 at left
    show old_roxxy 51 at right
    show old_roxxy_head 55c at right
    with dissolve
    pause
    show old_roxxy 52 with dissolve
    pause
    show old_roxxy 53 with dissolve
    show player 109f
    pause
    show old_roxxy 54 with dissolve
    pause
    hide old_roxxy_head
    show old_roxxy 56c
    show clyde 20
    with dissolve
    clyde "Best. Day. Ever!"

    show clyde 19
    player_name "..."
    show clyde 20
    clyde "I swear, I could go blind right now and I wouldn't even care!"

    show clyde 19
    show old_roxxy 51
    show old_roxxy_head 55c at right
    with dissolve
    show player 5
    pause
    hide old_roxxy_head
    show old_roxxy 3
    with dissolve
    roxxy "A million showers won't be enough to wash this away..."

    show old_roxxy 3d
    show player 10
    player_name "... Sorry, {b}Roxxy{/b}."

    show player 5
    show old_roxxy 3
    roxxy "I'm not gonna forget this, {b}[firstname]{/b}!"

    show old_roxxy 3d
    show clyde 20
    show player 114
    clyde "Me neither!"

    show old_roxxy 14
    clyde "Ha ha ha!"

    show clyde 19
    show old_roxxy 3c
    show player 5
    roxxy "Ya Tuhan..."

    show old_roxxy 3d
    show player 114
    show clyde 20
    clyde "We going again?"

    show old_roxxy 2b
    clyde "Double or nothing!"

    show clyde 19
    show player 113
    player_name "Ya!"

    hide old_roxxy
    hide player
    hide clyde
    with dissolve
    return

label shooting_range_success_failed:
    scene expression "backgrounds/location_trailer_tractor_day_blur.jpg"
    show player 13f at Position (xpos=600)
    show old_roxxy 1 at right
    show clyde 4 at left
    with dissolve
    clyde "Daaaaang!"

    clyde "You finally got me!"

    show clyde 3
    show old_roxxy 3c
    roxxy "Sudah waktunya!"

    show old_roxxy 3d
    return

label shooting_range_success_first:
    scene expression "backgrounds/location_trailer_tractor_day_blur.jpg"
    show player 13f at Position (xpos=600)
    show old_roxxy 1 at right
    show clyde 4 at left
    with dissolve
    clyde "Daaaang!"

    clyde "Nice shootin' buddy!"

    show clyde 3
    show old_roxxy 4
    roxxy "Oh, thank god!"

    show old_roxxy 2
    roxxy "I owe you big time for this, {b}[firstname]{/b}!"

    show old_roxxy 1
    return

label shooting_range_success_outro:
    show clyde 4
    clyde "I reckon I gotta pay up now..."

    show old_roxxy 1
    show clyde 7 with dissolve
    show player 110
    clyde "Sorry, girl."

    clyde "I'll have to find you something else to-"

    show clyde 5b
    pig "{i}*Oink*{/i}!"

    clyde "!!!"
    show clyde 2 with dissolve
    show player 11f
    clyde "Now you dun gon and made mah dog run off!"

    show clyde 1
    show player 114f
    show old_roxxy 3c
    roxxy "Ugh, you can't be serious!"

    roxxy "It's got my {b}uniform{/b}!"

    show old_roxxy 3d
    show player 5f
    show clyde 2
    clyde "I told ya she wouldn' be inclined to givin' it back..."

    clyde "Dun worry... She probably just ran on home..."

    show clyde 1
    show player 12f
    player_name "I'll get her."

    show player 5f
    show clyde 2
    clyde "Well, you best be careful naw..."

    clyde "My dog ain't particularly fond of strangers."

    show clyde 1
    show player 14f
    player_name "Heh, I'll be okay."

    player_name "I'm good with animals."

    show player 13f
    show clyde 2
    clyde "How 'bout dat."

    show clyde 9 with dissolve
    clyde "Yer datin' Doctor Dolittle!"

    show clyde 3 with dissolve
    show old_roxxy 3c
    show player 114f
    roxxy "We aren't dating!"

    show old_roxxy 3b
    show player 5f
    show clyde 4
    clyde "Heh, whatever you say, {b}Roxanne{/b}."

    clyde "You just make sure that new boyfriend of yours doesn't do no shootin' at the fair this year!"

    clyde "That stuffed beaver is mine, ya hear?!"

    show clyde 3
    show player 14f
    player_name "Tidak masalah."

    show player 114f
    show old_roxxy 3c
    roxxy "Ugh, how many times do I have to say, he isn't my boyfriend?!"

    show old_roxxy 31
    roxxy "... And don't call me {b}Roxanne{/b}!"

    show old_roxxy 3d
    show player 5f
    show clyde 4
    clyde "Whatever you say, Cuz..."

    show clyde 8 with dissolve
    pause
    hide clyde with dissolve
    show old_roxxy 3
    roxxy "... I can't believe I'm related to that moron!"

    show old_roxxy 3d
    show player 113f
    player_name "He's certainly a colorful fellow..."

    show player 114f
    show old_roxxy 3c
    roxxy "C'mon, let's go find that stupid pig."

    show old_roxxy 3d
    show player 113f
    player_name "Tentu saja."

    hide old_roxxy
    hide player
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
