label yoga_minigame:
    scene yoga_front
    show old_anna 14
    show player 411 at left
    with dissolve
    player_name "Hmm..."

    show player 412
    player_name "Okay, we have to do three consecutive positions, in the right order..."

    show player 411
    show old_anna 13
    anna "Ummm... Are you ready?"

    show old_anna 14
    show player 414 with dissolve
    player_name "I think so?"

    show player 413
    show old_anna 13
    anna "Well, which pose do we start with first?"

    show old_anna 14
    show player 412 with dissolve

    menu:
        player_name "The first position is..."

        "Happy Baby.":
            player_name "Umm... I think {i}Happy Baby{/i} is the next position."

            jump yoga_minigame_fail
        "Plow Position.":
            player_name "Umm... I think {i}Plow Position{/i} is the next position."

            jump yoga_minigame_fail
        "Downward Dog.":
            player_name "We need to do the {i}Downward Dog{/i}?"

        "End Lesson." if store._in_replay == None and M_mrsj.finished_state(S_mrsj_yoga_report):
            jump yoga_minigame_quit



    show player 413
    show old_anna 15
    anna "Oh, right. I love that position!"

    show old_anna 18 with dissolve
    anna "Why don't I get myself on the mat and you help me stretch?"

    show old_anna 17
    show player 416
    player_name "Uhh... Okay."

    hide player
    show old_anna 19
    with dissolve
    pause
    pause
    anna "Don't hesitate to add some force to your push!"

    show old_anna 19_20
    pause
    show player 411 at left
    show old_anna 18
    with dissolve
    anna "That was good! I already feel more limber!"

    show old_anna 17
    show player 412

    menu:
        player_name "Okay, for the second position, I think we should try..."

        "Happy Baby.":
            player_name "... The {i}Happy Baby{/i}?"

        "Plow Position.":
            player_name "Umm... I think {i}Plow Position{/i} is the next position."

            jump yoga_minigame_fail
        "Downward Dog.":
            player_name "Umm... I think {i}Downward Dog{/i} is the next position."

            jump yoga_minigame_fail
        "End Lesson." if store._in_replay == None and M_mrsj.finished_state(S_mrsj_yoga_report):
            jump yoga_minigame_quit

    show player 413 with dissolve
    show old_anna 18
    anna "Tentu saja!"

    anna "It's one of my favorites."

    anna "Let me get on my back so you can push on my legs to stretch..."

    show old_anna 21 with dissolve
    show player 416
    player_name "!!!"
    hide player
    show old_anna 23
    with dissolve
    player_name "Push on your legs?"

    show old_anna 24
    anna "Ya!"

    anna "Just push them back so I can stretch..."

    show old_anna 25 with dissolve
    pause
    pause
    pause
    show old_anna 27 with dissolve
    anna "That felt great..."

    show old_anna 28
    player_name "..."
    anna "Oh!!"

    show old_anna 26
    player_name "Haha! I think we are ready for the last position!"


    menu:
        player_name "The last position should follow up this one..."

        "Happy Baby.":
            player_name "Umm... I think {i}Happy Baby{/i} is the next position."

            jump yoga_minigame_fail_hard
        "Plow Position.":
            player_name "... The {i}Plow Position{/i}?"

        "Downward Dog.":
            player_name "Umm... I think {i}Downward Dog{/i} is the next position."

            jump yoga_minigame_fail_hard
        "End Lesson." if store._in_replay == None and M_mrsj.finished_state(S_mrsj_yoga_report):
            jump yoga_minigame_quit_hard

    show old_anna 27
    anna "Sempurna!"

    show player 420 at left
    show old_anna 29
    with dissolve
    pause
    show old_anna 30
    anna "All you have to do is press your... Pelvis against my butt."

    show old_anna 29
    show player 421
    player_name "Umm... Okay..."

    hide player
    show old_anna 31
    with dissolve
    pause
    show old_anna 32
    anna "Ah, ya!"

    hide old_anna
    show old_anna_slow 31_32
    pause
    anna "Just a bit more!!"

    hide old_anna_slow 31_32
    show old_anna_fast 31_32
    pause
    hide old_anna_fast 31_32

    show player 420 at left
    show old_anna 22
    with dissolve
    anna "That was... Excellent!"

    show old_anna 21
    show player 419
    player_name "I... I'm sorry about..."

    show player 420
    show old_anna 15 with dissolve
    anna "Oh! Haha!"

    show old_anna 13
    anna "It's fine!"

    anna "That always happens to guys who come to our class!"

    show old_anna 16
    anna "And I didn't mind the extra... Push..."


    scene yoga_room_night
    show player 82 at left
    show old_anna 2 at right
    with dissolve
    anna "I'm impressed!"

    anna "You did such a great job..."

    show old_anna 3
    anna "... And I really enjoyed being your assistant!"

    show old_anna 1
    show player 83
    player_name "I was just trying to help {b}Mrs. Johnson{/b}."

    show player 79 with dissolve
    player_name "It was kinda fun."

    show player 82 at left with dissolve
    show old_anna 2
    anna "Hopefully, you can come by again soon to teach the class... With my help?"

    anna "That is... If you'd like to..."

    show old_anna 1
    show player 79 with dissolve
    player_name "That might be fun!"

    show player 82 at left with dissolve
    show old_anna 2
    anna "Just make sure you come at night."

    anna "It's when {b}Tammy{/b} is away and I need the help..."

    show old_anna 1
    show player 83
    player_name "Umm... Sure."

    hide player
    hide old_anna
    with dissolve
    return True


label yoga_minigame_fail(hard=False):
    if hard:
        show player 419 at left
        show old_anna 21
    else:
        show player 418 at left
    with dissolve
    player_name "I'm not really sure though."

    player_name "I can't remember..."

    if hard:
        show player 420
    else:
        show player 417
    show old_anna 13 with dissolve
    if not M_mrsj.is_state(S_mrsj_yoga_class, S_mrsj_yoga_retry):
        anna "It's probably best if we just skip this class for now."

    anna "We can try again tomorrow."

    if hard:
        show player 419
    else:
        show player 418
    show old_anna 14
    player_name "Ya..."

    player_name "Maaf."

    if hard:
        show player 420
    else:
        show player 417
    show old_anna 13
    anna "Just {b}look over Tammy's notes and be sure to memorize them{/b} for next time."

    if hard:
        show player 419
    else:
        show player 418
    show old_anna 14
    player_name "Alright. I'll do my best..."

    hide old_anna
    hide player
    with dissolve
    scene yoga_room_night
    show player 24 with dissolve
    player_name "Damn... I couldn't do it."

    if M_mrsj.finished_state(S_mrsj_yoga_class) and not M_mrsj.is_state(S_mrsj_yoga_retry):
        player_name "I should memorize the moves and try again."

    else:
        player_name "I should memorize the moves and try again tomorrow."

        show player 25
        player_name "I can't let {b}Mrs. Johnson{/b} and {b}Anna{/b} down like that..."

    hide player with dissolve
    return False


label yoga_minigame_fail_hard:
    call yoga_minigame_fail (hard=True)
    return _return


label yoga_minigame_quit(hard=False):
    scene yoga_room_night
    if hard:
        show player 82 at left
        show player 79
    else:
        show player 14 at left
    show old_anna 1 at right
    with dissolve
    player_name "Itu menyenangkan!"

    if hard:
        show player 82 at left with dissolve
    else:
        show player 13
    show old_anna 3
    anna "Ya!"

    show old_anna 2
    anna "You sure did good this time. I'm impressed!"

    show old_anna 1
    if hard:
        show player 79 with dissolve
    else:
        show player 14
    player_name "Terima kasih!"

    player_name "I was just trying to help."

    if hard:
        show player 82 at left with dissolve
    else:
        show player 13
    show old_anna 2
    anna "I wouldn't mind doing it again with you..."

    anna "... If you'd like."

    show old_anna 1
    if hard:
        show player 79 with dissolve
    else:
        show player 14
    player_name "Tentu saja!"

    if hard:
        show player 82 at left with dissolve
    else:
        show player 13
    show old_anna 2
    anna "Great! See you next time..."

    hide player
    hide old_anna
    with dissolve
    return


label yoga_minigame_quit_hard:
    call yoga_minigame_quit (hard=True)
    return _return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
