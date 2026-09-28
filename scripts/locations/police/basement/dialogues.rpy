label police_basement_roxxy_ask_earl_release:
    scene expression player.location.background_blur
    show player 12 with dissolve
    player_name "We need to {b}find an officer to ask about Roxxy's mom{/b}."
    hide player with dissolve
    return

label police_basement_first_visit:
    scene expression player.location.background_blur
    pause .4
    scene police_c_3
    show player 1
    with dissolve
    player_name "( This must be the \"drunk tank\" people talk about... )"
    hide player with dissolve
    return

label police_basement_mia_clues_summary:
    scene expression player.location.background_blur
    show player 35 with dissolve
    player_name "( Okay, so he's taking time off and took off for a drive this morning... )"
    player_name "( ... And he's drunk. )"
    show player 12
    player_name "Hmm..."
    player_name "( I need more {b}clues{/b}. )"
    player_name "( Maybe I should {b}check his desk{/b}... )"
    hide player with dissolve
    return

label police_basement_mia_inmate_status:
    scene expression player.location.background_blur
    show player 4 at Position (xoffset=6) with dissolve
    player_name "Hmm..."
    show player 12 with dissolve
    player_name "( I don't see {b}Yumi{/b} anywhere, maybe I should- )"
    "{i}*Shouting*{/i}" with hpunch
    show player 11
    player_name "..."
    show player 10
    player_name "( Is that coming from one of the cells?! )"
    hide player with dissolve
    return

label police_basement_mia_harold_backup:
    scene expression player.location.background_blur
    show player 10 with dissolve
    player_name "( I have to {b}find Harold{/b} quickly! )"
    hide player with dissolve
    return

label police_cell_mia_inmate_status:
    scene police_cell_inside_fight1
    yumi "Hey, stop!!!!"
    scene police_cell_inside_fight2
    crystal "Arhh!!"
    scene police_cell_inside_fight1
    yumi "... Help!! Get some backup!!"
    player_name "!!!"
    scene police_cell_inside_fight2
    player_name "I'll get {b}Harold{/b}!"
    scene police_cell_inside_fight1
    yumi "Go! Quickly!"
    return

label police_cell_mia_harold_backup:
    scene expression player.location.background_blur
    show player 10 with dissolve
    player_name "( I have to {b}find Harold{/b} quickly! )"
    hide player with dissolve
    return

label police_cell_mia_harold_to_the_rescue:
    scene police_cell_inside_cs1
    show text _ ("{b}Harold{/b} and I rushed to the basement.\nWhen {b}Harold{/b} walked into the cell, he froze for a moment...\n... But realized he had to find the courage to step in and help {b}Yumi{/b}.") as caption
    with fade
    pause

    scene police_cell_inside_cs2
    show text _ ("Inside the cell was {b}Crystal{/b}...\n... {b}Roxxy{/b}'s mom, notorious for causing trouble when drunk.\nIt turns out, she is quite a fighter after a few drinks...") as caption
    with fade
    pause

    scene police_cell_inside_cs3
    show text _ ("{b}Harold{/b} had quite a bit of trouble at first...\n... But he soon found his old form.\nI could tell that despite the trouble, he enjoyed getting some action.") as caption
    with fade
    pause

    scene police_cell_c_02
    show old_harold 39 at Position (xpos=158)
    show old_yumi 5 at Position (xpos=855)
    with fade
    harold "Now, STAY there!!"
    show old_harold 38
    show old_yumi 7
    yumi "..."
    show old_harold 37
    harold "Are you okay?"
    show old_harold 36
    show old_yumi 6
    yumi "Yeah, I just... I've never seen you like this before."
    show old_yumi 5
    show old_harold 37
    harold "Oh, it's just, you know... These type of people get on your nerves..."
    show old_harold 36
    show old_yumi 6
    yumi "No, I meant like... Taking action like this."
    yumi "It was really nice! It's a side of you I haven't seen before."
    show old_yumi 5
    show old_harold 37
    harold "You know what, I kind of missed that. The action."
    show old_harold 36
    show old_yumi 6
    yumi "Thanks for having my back..."
    show old_yumi 5
    show old_harold 37
    harold "Oh, come on. I would do anything for my partner!"
    show old_harold 36
    show old_yumi 6
    yumi "Ugh! I should have been more careful..."
    yumi "... It was stupid of me and everyone at work will find out, I'm sure..."
    show old_yumi 5
    show old_harold 37
    harold "Well, {b}Yumi{/b}..."
    harold "I wouldn't worry too much about it..."
    show old_harold 42 at Position (xoffset=32) with dissolve
    pause
    show old_harold 43 at Position (xpos=195) with dissolve
    pause
    scene police_cell_inside_zoom
    pause
    scene police_cell_inside_splash with flash
    pause
    scene police_cell_c_02
    show old_harold 41 at Position (xpos=158)
    show old_yumi 7 at Position (xpos=855)
    with fade
    harold "... Because I'll take care of it."
    harold "Now, let's get out of here!"
    hide old_harold
    hide old_yumi
    with dissolve
    scene black with fade
    pause
    scene expression player.location.background_blur
    show player 10f at right
    show old_harold 40 at left
    show old_yumi 5f at Position (xpos=550)
    with dissolve
    player_name "... {b}Harold{/b}?"
    show player 11f
    show old_harold 41
    harold "Hey, kid."
    show old_harold 40
    show player 10f
    player_name "Are you okay? Your shirt is ripped."
    show player 11f
    show old_harold 41
    harold "It's fine, just a scratch."
    show old_harold 40
    show player 12f
    player_name "Looks like your partner had a rough time as well..."
    show player 11f
    show old_yumi 6f
    yumi "Oh, yeah... MY hair's a mess."
    show old_yumi 5 with dissolve
    show old_harold 41
    harold "Actually, I kind of like your hair this way. Keep it."
    show player 13f
    show old_harold 40
    show old_yumi 7
    yumi "..."
    show old_harold 41
    harold "How about we go for a drive?"
    show old_harold 40
    show old_yumi 8
    yumi "You mean, now?!"
    show old_yumi 9
    show old_harold 41
    harold "Yeah, it's nice out... And I'm thirsty."
    show old_harold 40
    show old_yumi 8
    yumi "Haha. Fine. If you insist."
    show old_yumi 9
    show old_harold 41
    harold "Hop in the car, I'll meet you outside."
    show old_harold 40
    hide old_yumi with dissolve
    show player 14f
    player_name "I should let you go then."
    show player 13f
    show old_harold 41
    harold "Wait..."
    show old_harold 40
    show player 11f
    player_name "..."
    show old_harold 41
    harold "Thanks for all your... Help."
    show old_harold 40
    show player 14f
    player_name "Oh, I... It's nothing, sir."
    show player 13f
    show old_harold 41
    harold "See ya, kiddo!"
    hide old_harold
    hide player
    with dissolve
    return

label police_cell_empty:
    scene police_cell
    show xtra 13 zorder 1 at left
    show player 10f zorder 2
    with dissolve
    player_name "( I wouldn't want to end up in there. Sheesh! )"
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
