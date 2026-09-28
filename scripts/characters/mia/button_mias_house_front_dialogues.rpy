label mia_dialogue_mias_house_front_intro:
    scene location_mia_closeup
    show player 14 at left
    show old_mia 1 at right
    with dissolve
    player_name "Hey {b}Mia{/b}!"
    show old_mia 4
    show player 1
    mia "Hey {b}[firstname]{/b}!"
    mia "What're you doing here?"
    show old_mia 1
    show player 29
    player_name "Umm... I wanted to ask you something!"
    return

label mia_dialogue_mias_house_front_homework:
    show player 21
    player_name "Do you still need help studying for the exams?"
    show old_mia 3
    show player 13
    mia "Of course! I've been looking for someone to study with..."
    show old_mia 6
    show player 11
    mia "... But have you caught up with class yet?"
    show old_mia 2
    show player 10
    player_name "Oh! Right! I should probably {b}get some private tutoring from Miss Bissette{/b} to catch up..."
    show old_mia 6
    show player 13
    mia "Yeah, you probably should do that first!"
    show old_mia 4
    mia "Then you can come over to my house... And we'll study in my room!"
    show old_mia 1
    show player 14
    player_name "Ye... Yeah?"
    show old_mia 3
    show player 1
    mia "Sure! It'll be fun!"
    show old_mia 1
    show player 17
    player_name "Alright... I'll let you know when I'm done with them!"
    show old_mia 4
    show player 1
    mia "See you soon!"
    hide old_mia with dissolve
    show player 5 with dissolve
    player_name "( I should try and {b}finish my French homework{/b}, so I can study with {b}Mia{/b}. )"
    show player 4
    pause
    player_name "( I wonder why she picked me to help her study. )"
    player_name "( She usually studies with {b}Judith{/b}, and she's really good at French... )"
    player_name "( I'm not sure how I could help her. )"
    show player 13
    player_name "( At least we'll get to hang out, and she's really cute... )"
    hide player with dissolve
    return

label mia_dialogue_mias_house_front_leave:
    show player 4
    player_name "Hmm... Yeah, but I forgot!"
    show old_mia 3
    show player 11
    mia "Haha! You're funny~."
    show old_mia 1
    show player 17
    player_name "Sorry! I can't remember what I wanted to say!"
    show player 14
    player_name "I should get going."
    show old_mia 4
    show player 1
    mia "Have a good night!"
    hide player
    hide old_mia
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
