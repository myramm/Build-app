label debbie_dialogue_master_room_pre:
    scene debbie_bedroom_closeup2
    show old_debbie 55 at left
    show player 110 at right
    with dissolve
    debbie "Hi, sweetie..."
    debbie "Were you looking for me?"
    show old_debbie 54
    show player 111
    player_name "Yeah..."
    show player 110
    show old_debbie 55
    debbie "Is there something you wanted from me?"
    show old_debbie 54
    return

label debbie_dialogue_master_room_after_kiss_dialogue:
    debbie "Now, is there anything else you wanted?"
    show old_debbie 54
    return

label debbie_dialogue_master_room_kiss:
    show player 111 at right
    show old_debbie 54 at left
    player_name "Can I have a kiss?"
    show player 110
    show old_debbie 55
    debbie "Of course, sweetie! Come here."
    scene debbie_bedroom
    show old_debbie 79
    with fade
    debbie "Mmmm..."
    show old_debbie 80_79
    pause 3
    show old_debbie 75 at Position(xpos=750)
    show player 227 at Position(xpos=200)
    with fastdissolve
    debbie "You're getting better at this!"
    scene debbie_bedroom_closeup2
    show old_debbie 55 at left
    show player 110 at right
    with fade
    return

label debbie_dialogue_master_room_shower:
    show player 111
    player_name "Hey, {b}[deb_name]{/b}!"
    player_name "Want to take a shower with me?"
    show player 110
    show old_debbie 55
    debbie "It is getting pretty hot in the house..."
    debbie "Sure! A shower sounds lovely right now."
    debbie "You go ahead, sweetie. I'll be there in a minute."
    scene shower_closeup
    show debbies 27
    with dissolve
    pause
    show debbies 28 at Position(xpos=487,ypos=768) with dissolve
    pause
    show debbies 34 with dissolve
    debbie "Sorry to keep you waiting, sweetie..."
    return

label debbie_dialogue_master_room_sex_random_true:
    show old_debbie 54 at left
    show player 111 at right
    player_name "I feel like... Doing it with you again."
    show player 110
    show old_debbie 55
    debbie "That's okay!"
    debbie "I was hoping you'd want to..."
    show player 111
    show old_debbie 54
    player_name "Really?"
    show player 110
    show old_debbie 58 with dissolve
    debbie "Of course! You're my man, after all."
    show old_debbie 57
    player_name "!!!"
    show old_debbie 58
    debbie "Take your clothes off, sweetie."
    show old_debbie 57
    show player 8f
    pause
    show player 261
    pause
    show player 263
    pause
    show old_debbie 103
    debbie "Mmm, come get me, sweetie!"
    show player 262 at right
    show old_debbie 102 at left
    player_name "Don't have to tell me twice..."
    return

label debbie_dialogue_master_room_sex_random_false:
    show old_debbie 54 at left
    show player 111 at right
    player_name "{b}[deb_name]{/b}, want to have some fun?"
    show player 110
    show old_debbie 54
    debbie "Oh?"
    show old_debbie 56 with dissolve
    debbie "Like... This kinda fun?"
    show old_debbie 57
    show player 111
    player_name "Of course..."
    show player 110
    show old_debbie 58
    debbie "Let me see that cock of yours..."
    show old_debbie 57
    show player 8f with dissolve
    pause
    show old_debbie 101
    show player 261 with dissolve
    pause
    show player 263 with dissolve
    pause
    show old_debbie 58
    debbie "It looks like you are ready!"
    show old_debbie 57
    show player 262
    player_name "I've been looking forward to this since I woke up this morning."
    show player 263
    show old_debbie 58
    debbie "Me too."
    show old_debbie 102 with dissolve
    pause
    show old_debbie 103
    debbie "Come and get it, sweetie."
    return

label debbie_dialogue_master_room_sex_after:
    hide player
    show old_debbie 104 at left
    with dissolve
    pause
    hide old_debbie
    hide player
    with dissolve
    scene debbie_bedroom_closeup_sex
    return

label debbie_dialogue_master_room_laundry_sex:
    show old_debbie 54
    show player 111
    player_name "I was wondering if you wanted some help in the basement."
    show player 110
    show old_debbie 55
    debbie "In the basement? What for?"
    show player 111
    show old_debbie 54
    player_name "Maybe I can help you with laundry... Like we did last time?"
    show player 110
    show old_debbie 55
    debbie "Oh, I see... I know exactly what you want!"
    debbie "Give me a minute to get ready."
    debbie "I'll meet you down there..."
    hide old_debbie
    hide player
    with dissolve
    return

label debbie_dialogue_master_room_watch_movie:
    show player 111
    player_name "I was thinking, we should watch another movie tonight. Interested?"
    show player 110
    show old_debbie 55
    debbie "Mmm, a movie night, huh?"
    debbie "That sounds like a great idea, sweetheart!"
    show player 111
    show old_debbie 54
    player_name "Awesome!"
    player_name "I'll see you tonight in the living room then?"
    show player 110
    show old_debbie 55
    debbie "I can't wait..."
    return

label debbie_dialogue_master_room_leave:
    show old_debbie 54
    show player 111
    player_name "Nothing, {b}[deb_name]{/b}."
    player_name "Just wanted to say hi."
    show player 110
    show old_debbie 55
    debbie "Oh, okay..."
    debbie "Well, come back if you'd like... I'm a bit bored..."
    debbie "We can have fun whenever you'd like."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
