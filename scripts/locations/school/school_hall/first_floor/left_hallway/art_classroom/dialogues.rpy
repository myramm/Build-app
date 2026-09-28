label art_classroom_ross_start:
    scene location_school_art_day_closeup
    show player 2f at right
    show old_ross 1 at left
    player_name "Hey, {b}Miss Ross{/b}."
    show player 1f
    show old_ross 2
    ross "Well, hello there, {b}[firstname]{/b}!"
    show old_ross 25 with dissolve
    ross "I heard about your father passing..."
    ross "You poor thing, I've been praying for you."
    show old_ross 24
    show player 2f
    player_name "Uhh, thanks!"
    show player 1f
    show old_ross 25
    ross "Oh, it's no problem, honey."
    ross "You let me know if there's ever anything I can do for you."
    show player 2f
    show old_ross 24
    player_name "Well, actually, there might be something you can do."
    player_name "I need a way to {b}improve my art grade{/b}."
    show player 1f
    show old_ross 25
    ross "Oh yes, it dropped quite a bit during your absence."
    ross "It's really too bad. You were top of the class before you left..."
    show player 10f
    show old_ross 24
    player_name "I was?!"
    show player 11f
    show old_ross 11
    ross "Aww, don't be modest, {b}[firstname]{/b}! You have such a talent for art!"
    show player 2f
    show old_ross 10
    player_name "Heh, yeah, I guess..."
    show player 1f
    show old_ross 11
    ross "I'm certain we can come up with some way to improve your grade."
    show old_ross 2 with dissolve
    ross "Hmm, why don't we talk about it after class today?"
    show player 2f
    show old_ross 1
    player_name "That sounds great! Thanks so much, {b}Miss Ross{/b}!"
    show player 1f
    show old_ross 2
    ross "Well, go {b}grab a slab of clay{/b}, and take a seat, so we can start the pre-class meditation."
    show player 10f
    show old_ross 1
    player_name "Meditation?"
    show player 11f
    show old_ross 2
    ross "Of course! We have to relax our minds and align our chakras if we want our creativity to flow correctly!"
    show player 10f
    show old_ross 1
    player_name "Ugh. Yes, ma'am."
    return

label art_classroom_mia_find_easel:
    scene art_classroom_b
    show player 4 with dissolve
    player_name "Hmm..."
    show player 12 with dissolve
    player_name "Let's see if I can {b}find an easel{/b} I could use to draw some tattoo ideas..."
    hide player with dissolve
    return

label easel_dialogue_mia_show_tattoo:
    show player 14 with dissolve
    player_name "( I should show the drawing I made to {b}Mia{/b} first, before I make another one. )"
    hide player with dissolve
    return

label easel_dialogue_mia_draw_tattoo_intro:
    scene school_art_tattoos
    player_name "Hmm..."
    player_name "( What should I draw for {b}Mia{/b}... )"
    return

label easel_dialogue_mia_draw_tattoo_drawn:
    scene school_art_cs01
    show text _ ("I've drawn so many pictures before...\nBut, doing something like this for {b}Mia{/b} made me super nervous!\nI hope it's what she wants...") as caption
    with fade
    pause

    scene art_classroom_b
    show player 381
    with fade
    player_name "Not bad!"
    show player 386
    player_name "( I should go and show {b}Mia{/b} what I made. )"
    player_name "( Hopefully, she'll like it... )"
    hide player with dissolve
    return

label art_classroom_ross_molding_clay_cutscene:
    scene location_school_art_cutscene03
    show text _ ("It was nice to be back in art class again.") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("I always had a bit of a knack for it.") as caption with dissolve
    pause

    scene location_school_art_cutscene04
    show text _ ("Sadly, the same couldn't be said for my friends...") as caption
    with fade
    pause

    scene location_school_art_day_closeup
    show player 547f at right
    show old_ross 27 zorder 1 at left
    with fade
    ross "Goodness, what a cute little giraffe, {b}[firstname]{/b}!"
    show player 548f
    show old_ross 26
    player_name "You think so?"
    show player 547f
    show old_ross 27
    ross "Simply adorable!"
    show old_ross 13 with dissolve
    ross "It's certainly very... Gifted. Isn't it?"
    show player 10f with dissolve
    show old_ross 12
    player_name "Huh?"
    show player 11f
    show old_ross 13
    ross "I just mean it's so {i}long{/i} and {i}thick{/i}..."
    show player 2f
    show old_ross 12
    player_name "... Oh, you mean the neck!"
    show player 1f
    show old_ross 11
    ross "Hehe, yeah that too. It's very well done!"
    show old_ross 10
    player_name "..."
    show old_ross 11
    ross "So, what are we going to do about these low grades of yours?"
    show old_ross 13
    ross "I can think of more than a few uses for those talented hands..."
    show player 11f
    show old_ross 12
    player_name "..."
    show old_ross 13
    ross "Maybe we should start with a little after scho-"
    show old_ross 12
    smith "{b}Ross{/b}!!!" with hpunch
    show old_ross 24
    show player 22f
    smith "Where are you, you quack?!"
    show player 11 zorder 0 at Position(xpos=0.45, ypos=1.0)
    show principal 2 at Position(xpos=0.75, ypos=1.0)
    with dissolve
    smith "You'd better not be doing naked meditation agai-"
    show principal 3b at Position(xpos=0.8, ypos=1.0) with dissolve
    pause
    show principal 27 at Position(xpos=0.75, ypos=1.0) with dissolve

    smith "Oh, there you are!"
    show old_ross 23
    show principal 26
    ross "Excuse me, I'm with a student right now..."
    show old_ross 22
    show principal 27
    smith "Pfft. He's just gonna have to wait."
    smith "I need to talk to you about all this stuff you ordered."
    show old_ross 25
    show principal 26
    ross "You mean the art supplies?"
    show old_ross 24
    show principal 27
    smith "I don't know! Whatever this stuff is, it's not happening!"
    show old_ross 25b
    show principal 26
    ross "B-but..."
    show old_ross 24
    show principal 27
    smith "Look, it's just not in the budget, {b}Barbara{/b}."
    smith "You're going to have to make do without this stuff."
    show old_ross 25
    show principal 26
    ross "{b}Mrs. Smith{/b}, we need those supplies! Our equipment is in shambles!"
    show old_ross 24
    show principal 27
    smith "I can't give you what I don't have, now can I?"
    show principal 26
    ross "..."
    show principal 28 at Position(xpos=0.7, ypos=1.0) with dissolve
    smith "Just be thankful you still have any {b}budget{/b} at all."
    smith "Do you have any idea how hard it is to sell this hippie crap you teach to the school board?"
    show old_ross 25b
    show principal 26 at Position(xpos=0.75, ypos=1.0) with dissolve
    ross "... But art is important to an individual's growth!"
    show old_ross 24
    show principal 27
    smith "Yeah, sure it is..."
    smith "The answer is NO, {b}Barbara{/b}!"
    smith "You're just gonna have to tough it out."
    hide principal
    with dissolve
    pause
    hide player
    show player 11f zorder 1 at right
    show old_ross 23
    with dissolve

    ross "Arrghh!"
    ross "Every year it gets worse and worse!"
    show old_ross 22
    pause
    show old_mia 12b zorder 0 at Position(xpos=0.65, ypos=1.0) with dissolve

    mia "You alright, {b}Miss Ross{/b}?"
    show old_ross 11
    show old_mia 8b
    ross "Oh, hello, {b}Mia{/b} dear."
    show old_ross 10
    show old_mia 12b
    mia "I heard {b}Mrs. Smith{/b} yelling at you..."
    show old_mia 8b
    show player 10f
    player_name "Yeah, it definitely didn't sound good."
    show player 11f
    show old_ross 25
    ross "There's just so little budget for art."
    show old_ross 25b
    ross "It gets smaller and smaller each year."
    show old_ross 25
    ross "I'm afraid I might not have a job soon..."
    show old_ross 24
    show old_mia 12b
    mia "Seriously?"
    mia "They can't just cut art class, can they?"
    show old_ross 25
    show old_mia 8b
    ross "I wouldn't put it past {b}Mrs. Smith{/b}. She has no respect for the things I teach."
    show old_ross 25b
    ross "If only I could find a way to increase the funding a little..."
    show old_ross 24
    show player 10f
    player_name "Hmm, how much money would you need?"
    show old_ross 25
    show player 11f
    ross "I'm not sure."
    show old_ross 24
    pause
    show old_mia 12b
    mia "Would a thousand dollars help?"
    show old_mia 8b
    show old_ross 25
    ross "Huh? Yeah, that would be plenty to order new equipment, restock the art shelves, and maybe even hire some real models for you kids to paint."
    ross "... But where would we get that kind of money?"
    show old_ross 24
    show old_mia 62 at Position(xpos=0.585, ypos=1.0) with dissolve

    mia "You could {b}enter the mayor's art contest{/b}!"
    show old_mia 63
    show old_ross 11
    ross "{b}Mayor Rump{/b} is hosting an art contest?"
    show old_mia 62
    show old_ross 10
    mia "Yeah, take a look."
    show flyer 1 zorder 3 with dissolve
    show old_mia 63
    pause
    hide flyer with dissolve

    show player 10f
    player_name "First place is a thousand dollars, huh?"
    show player 2f
    player_name "{b}Miss Ross{/b}, you should enter!"
    show player 1f
    show old_ross 27 with dissolve
    ross "Oh heavens, no! I wouldn't have a chance of winning something like that..."
    show old_ross 26
    show old_mia 7 at Position(xpos=0.65, ypos=1.0) with dissolve
    ross "..."
    show old_ross 27
    ross "... But {b}[firstname]{/b} might."
    show old_ross 26
    show player 10f
    player_name "What?!"
    player_name "No way! I'm not talented enough for something like that."
    show old_ross 11 with dissolve
    show player 11f
    ross "Nonsense! You're the most talented student I've had in a long time!"
    ross "With me guiding you, it's practically a sure thing!"
    show old_ross 10
    show old_mia 9
    mia "Hehe, this is so exciting!"
    show old_mia 10b
    mia "You can do it, {b}[firstname]{/b}!"
    show old_mia 7
    show old_ross 11
    ross "See, {b}Mia{/b} here believes in you! Let's give it a shot!"
    show player 10f
    show old_ross 10
    player_name "I dunno..."
    show player 11f
    show old_ross 27 with dissolve
    ross "What if I promised to raise your grades?"
    show player 10f
    show old_ross 26
    player_name "You'd raise my grades?"
    show player 11f
    show old_ross 27
    ross "All you have to do is stay late to practice your techniques with me for a few weeks and enter something into the contest."
    ross "You do that and I'll give you an A+!"
    show player 10f
    show old_ross 26
    player_name "An A+?!"
    player_name "Just for entering?"
    show player 11f
    show old_ross 27
    ross "That's right. Do we have a deal?!"
    show old_ross 26
    pause
    show player 2f
    player_name "Yeah, okay. I'll do it!"
    show player 1f
    show old_mia 9
    mia "Yay!"
    show old_mia 7

    hide player
    show old_ross 21 at Position(xpos=0.15, ypos=1.0) with dissolve
    ross "Oh, I knew you wouldn't let me down, {b}[firstname]{/b}!"
    ross "Come back here {b}tomorrow after class{/b}, and we'll get started!"
    show old_ross 11 at left
    show player 11f at right
    with dissolve
    ross "Alright, {b}[firstname]{/b}?"
    show old_ross 10
    show player 10f
    player_name "Okay, {b}Miss Ross{/b}. I'll see you tomorrow then."

    $ game.timer.tick()
    $ M_ross.trigger(T_ross_molded_clay)
    $ game.main()

label leave_art_classroom:
    if not M_ross.is_state(S_ross_grab_clay):
        jump school_left_hallway_dialogue
    else:

        scene location_school_art_day_closeup
        show player 2 with dissolve
        player_name "{b}Miss Ross{/b} wants me to grab a slab of clay and take my seat."
        $ game.main()

label player_ross_magazines_3_left:
    show player 14 with dissolve
    player_name "I found one stack of magazines!"
    player_name "If I can find two more stacks this size, I should have enough to make that art collage."
    hide player with dissolve
    $ player.get_item("magazines1")
    call popup ('give', 'magazines1')
    $ M_ross.trigger(T_ross_found_magazines)
    return

label player_ross_magazines_2_left:
    show player 14 with dissolve
    player_name "Now, I just need to {b}find one more stack of magazines{/b} for {b}Miss Ross{/b}."
    hide player with dissolve
    $ player.remove_item("magazines1")
    $ player.get_item("magazines2")
    call popup ('give', 'magazines2')
    $ M_ross.trigger(T_ross_found_magazines)
    return

label player_ross_magazines_1_left:
    show player 14 with dissolve
    player_name "That's it! I should have plenty of magazines to start working on the art collage for {b}Miss Ross{/b}!"
    hide player with dissolve
    $ player.remove_item("magazines2")
    $ player.get_item("magazines")
    call popup ('give', 'magazines')
    $ M_ross.trigger(T_ross_found_magazines)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
