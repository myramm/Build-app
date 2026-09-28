label helens_locked_room_mia_locked_room:
    scene mia_house_locked_night_b
    show object_bed_11 at Position (xpos=527,ypos=765)
    show player 23 at left with dissolve
    player_name "{b}MIA{/b}!"
    player_name "You're tied up?!"
    show player 10
    player_name "Hold on, let me help you..."
    hide player with dissolve
    return

label mia_tied_up:
    call expression game.dialog_select("mia_tied_up_dialogue")
    $ game.timer.tick(3)
    $ M_mia.trigger(T_mia_rescue)
    $ player.go_to(L_miahouse)
    $ game.main()

label mia_tied_up_dialogue:
    scene mia_house_cs01
    show text _ ("{b}Mia{/b} seemed to be tied up on a bed, in a locked room.\nThere was no time to process what I was seeing...\n... I had to do something!") as caption
    with fade
    pause

    scene mia_house_locked_c
    show player 5 at left
    show old_mia 40f at right
    with fade
    pause
    show old_mia 41f with dissolve
    pause
    show old_mia 42f at Position (xoffset=-15) with dissolve
    mia "Ow..."
    show old_mia 43f at Position (xpos=500) with dissolve
    mia "{b}[firstname]{/b}!!!"
    show old_mia 44f
    show player 10
    player_name "{b}Mia{/b}! What's going on?!"
    player_name "I got your text message on my phone and-"
    show player 11
    show old_mia 43f
    mia "We have to go, quick!"
    show old_mia 44f
    show player 12
    player_name "Wait {b}Mia{/b}, what's going on?"
    show player 11
    show old_mia 43f
    mia "My mom is becoming INSANE!!"
    mia "She's been locking me up in here..."
    mia "... Forcing me to read the Bible and pray all day..."
    show player 22
    mia "... TIED TO THIS BED!!!"
    show old_mia 44f
    show player 23
    player_name "What?! That's crazy!"
    show player 11
    show old_mia 43f
    mia "There's no time to talk about it now."
    mia "We need to leave!!!"
    show old_mia 44f
    show player 10
    player_name "Now?!"
    show player 11
    show old_mia 46f
    mia "YES!"
    show old_mia 45f
    show player 10
    player_name "Wait but, where?!"
    show player 5
    show old_mia 46f
    mia "I don't care, I can't stay here any-"
    hide player
    show player 22 at left
    show old_mia 45 at Position (xpos=420)
    show helen 6 at right
    with dissolve
    player_name "!!!"
    show helen 7 with dissolve
    helen "How DARE you come back here... INTO MY HOUSE!"
    show helen 8
    show player 24
    show old_mia 47 at Position (xpos=465) with dissolve
    mia "{b}Mom{/b}! STOP!!!"
    show old_mia 48
    show helen 7
    helen "I won't let this evildoer take you away from me..."
    show helen 10 at Position (xpos=950) with dissolve
    helen "... THIS is the only thing that matters..."
    show player 22
    helen "... It will SAVE YOU!!!"
    show helen 11
    pause.5
    show helen 8 at Position (xpos=750)
    show old_harold 12 at right
    with dissolve
    harold "{b}Helen{/b}, what's with all the screaming?!"
    show old_harold 14
    show helen 7b
    helen "Go back downstairs, {b}Harold{/b}."
    show helen 8b
    show old_harold 13
    show player 11
    harold "No, wait a minute {b}Helen{/b}!"
    harold "This is too much, this has gone too far!!"
    show old_harold 14
    show helen 7b
    show player 22
    helen "SILENCE!"
    helen "I've had enough of your lousy parenting..."
    helen "... You were NEVER able to control our daughter!"
    show helen 8
    show player 11
    hide old_mia
    show old_mia 46 at Position (xpos=425) with dissolve
    mia "{b}Dad{/b}!"
    show helen 8b
    hide old_mia
    show old_harold 15
    with dissolve
    mia "Please make it stop!"
    harold "..."
    show helen 7b
    helen "She needs to stay here."
    show helen 8b
    show old_harold 17
    harold "No."
    show old_harold 16
    helen "..."
    show old_harold 17
    harold "This is enough!"
    pause
    show player 22
    harold "And you!"
    show old_harold 16
    show helen 8
    player_name "???"
    show old_harold 17
    harold "You shouldn't be here."
    harold "Go home and let me deal with this!"
    show old_harold 16
    show player 10
    player_name "Yes, sorry, I'll... I'm on my way out."
    hide player with dissolve
    show helen 7b
    helen "We're going to have a talk, {b}Harold{/b}."
    show helen 8b
    show old_harold 17
    harold "I don't think so, {b}Helen{/b}."
    harold "There's nothing left to discuss here."
    harold "{b}Mia{/b} is going to her room, and we deal with this tomorrow!"
    hide old_harold
    hide helen
    scene black
    with fade
    pause

    scene expression L_miahouse.background_blur
    show player 12 with dissolve
    player_name "{b}Helen{/b} is out of her MIND!!"
    player_name "I didn't think it was that bad with {b}Mia{/b}'s parents..."
    player_name "... To the point of tying her up?! That's crazy!"
    show player 24
    player_name "{i}*Sigh*{/i}"
    player_name "I feel bad for {b}Mia{/b}..."
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
