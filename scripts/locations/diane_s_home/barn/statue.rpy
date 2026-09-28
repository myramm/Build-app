label barn_garden_statue_dialogue:
    $ M_daisy.trigger(T_daisy_view_statue)
    if player.has_item("milk_sample"):
        if game.timer.is_dark():
            call expression game.dialog_select("barn_statue_dark")
        else:
            call expression game.dialog_select("barn_statue_has_milk")
            $ M_daisy.trigger(T_daisy_awaken_statue)
    else:
        call expression game.dialog_select("barn_statue_has_not_milk")
    $ game.main()

label barn_statue_has_milk:
    scene expression "backgrounds/location_diane_garden_closeup.jpg"
    show player 712 at left with dissolve
    player_name "( So, a {b}milk pail{/b}, huh? )"
    pause
    show diane b_shirtless f_shamed_smile:
        xoffset 100
    with dissolve
    diane "What are you doing with that milk, {b}[firstname]{/b}?"
    show diane f_shamed
    show player 713
    player_name "I have an idea."
    show player 184 with dissolve
    show diane f_shamed_look
    diane "You have an idea?"
    hide player with dissolve
    diane "You're not gonna-"

    scene location_diane_garden_cutscene09
    show text _ ("I had to pour milk into that pail.") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("It was like some urge that I couldn't fight.") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("I'm not sure what I was expecting to happen...") as caption with dissolve
    pause

    scene location_diane_garden_cutscene10
    show text _ ("... But I never could have anticipated what I did.") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("The statue started to crack and a strange glow began to emit from it.") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("Before long, it was so bright, {b}Diane{/b} and I had to shield our eyes!") as caption with dissolve
    pause

    scene expression player.location.background_blur
    show player 428 at left
    show diane b_shirtless f_surprised_front:
        xoffset 100
    with fade
    player_name "!!!"
    show diane f_surprised_front
    diane "What in the world-"
    show player 10b
    player_name "It's glowing..."
    show player 428
    pause
    diane "It's so bright!"
    show player 718
    show diane f_scream a_cover
    with dissolve
    diane "Ack!"
    player_name "!!!"
    show daisy b_appear_flash with flash:
        xoffset -200
    pause
    show daisy b_appear with dissolve
    pause
    show player 23 with None
    show daisy f_sad_closed b_naked a_up
    show diane f_scared a_idle
    with dissolve
    cow "No, Master!!!"
    show player 428
    cow "Please, I'll be a good girl!"
    cow "I will, I'll-"
    show player 22
    pause
    show player 5b
    show daisy f_sad
    pause
    show daisy f_scared b_naked a_cover
    cow "AHHHHHHH!!!" with hpunch
    show daisy f_sad_closed
    cow "D-don't look at me!"
    cow "I didn't mean to!!"
    show player 10b
    player_name "What in the hell?"
    show player 5b
    cow "You can't see me!"
    cow "Please, he'll hurt me if he finds out!"
    show player 11
    show diane f_scared
    diane "Who's gonna hurt you, sweetie?"
    show daisy f_sad:
        flip
        xoffset 300
    with dissolve
    cow "Master."
    show player 4 with dissolve
    diane "Who?"
    cow "{i}*Waaaah*{/i}"
    show player 10
    player_name "I think she's talking about {b}Jebadiah Delmont{/b}."
    show player 5
    diane "Who in the heck is {b}Jebadiah Delmont{/b}?"
    show player 12
    player_name "Uhh, it's a long story..."
    show player 5
    pause
    show player 12
    player_name "Let's just say he's the guy who made the statue."
    show player 5
    pause
    show diane f_sad
    diane "Is that who you're talking about, sweetie?"
    cow @ f_sad_closed -m_talk "{i}*Sniff*{/i} Uh huh."
    diane "Aww, you poor thing."
    diane "Don't you worry, he's not gonna hurt you ever again."
    cow "{i}*Sniff*{/i} He will..."
    diane "No, I won't let him."
    show daisy a_wiping_tears with dissolve
    cow "Y-you promise?"
    show daisy b_naked_shy a_idle with dissolve
    show diane f_shamed_smile
    diane "I promise."
    hide daisy
    hide diane
    show daisy b_naked_diane_shirtless_comfort
    show diane b_empty f_shamed_look_closed
    with dissolve
    pause
    show diane f_shamed_look
    diane "Aww, there, there..."
    diane "Everything is gonna be okay."
    diane "Let's get you into the barn and get you covered up, okay?"
    show daisy b_naked_diane_shirtless_comfort2
    show diane f_shamed_look_closed
    cow "{i}*Sniff*{/i} O-okay."
    hide daisy
    hide diane
    with dissolve
    pause
    show player 34
    player_name "( What in the hell just happened?! )"
    player_name "( Was {b}Clyde{/b}'s kooky grandfather really a wizard?! )"
    pause
    show player 37 with dissolve
    player_name "( I should {b}follow them into the barn{/b} and learn more. )"
    hide player with dissolve
    return

label barn_statue_has_not_milk:
    scene expression player.location.background_blur with None
    show player 426 with dissolve
    player_name "( Wow, the statue does look really good in {b}Diane{/b}'s garden! )"
    pause
    player_name "( There is something off about it though. )"
    player_name "( She almost looks like she's afraid... )"
    pause
    show player 4 with dissolve
    player_name "( ... And why does she have a {b}milk pail{/b}, I wonder? )"
    pause
    show player 426 with dissolve
    player_name "( Hmm, strange... )"
    hide player with dissolve
    return

label barn_statue_dark:
    scene expression player.location.background_blur
    show anon f_worried with dissolve
    anon @ -m_talk "( It's pretty dark out here, I don't want to spill any... )"
    pause
    anon @ -m_talk "( Maybe I should wait and {b}try this in the daylight{/b}. )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
