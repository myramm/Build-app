label mrsj_button_yoga_room_dialogue_pre_first:
    show player 1 at left
    show mrsj 10 at right
    with dissolve
    player_name "Umm-"
    show player 11 at left
    window hide
    pause
    player_name "..."
    show mrsj 11 at right
    window hide
    pause
    show mrsj 12 at right
    window hide
    pause
    show mrsj 13 at right with hpunch
    mrsj "Oh!"
    show player 18 at left
    mrsj "... {b}[firstname]{/b}?"
    show mrsj 14 at right
    show player 17 at left
    player_name "Hi, {b}Mrs. Johnson{/b}!"
    show mrsj 17 at right
    show player 1 at left
    mrsj "What are you doing here?"
    show mrsj 14 at right
    show player 29 at left
    player_name "I... Saw you from the main {b}Gym{/b}!"
    player_name "I just came to say hi!"
    show player 13 at left
    show mrsj 18 at right
    mrsj "That's so sweet!"
    show mrsj 17 at right
    mrsj "So you're working out now, huh?"
    show mrsj 14 at right
    show player 21 at left
    player_name "Haha. Yeah..."
    player_name "... Just started training to get fit!"
    show mrsj 19 at right
    show player 11 at left
    mrsj "And I bet you'll get nice and {i}hard{/i}-"
    mrsj "..."
    show player 13 at left
    show mrsj 18 at right
    mrsj "I mean, {b}strong{/b}!"
    show mrsj 14 at right
    show player 17 at left
    player_name "I hope so..."
    show mrsj 17 at right
    show player 1 at left
    mrsj "Anyway, is there anything you wanted to talk about?"
    return

label mrsj_button_yoga_room_dialogue_pre_repeat:
    show player 14 at left
    show mrsj 14 at right
    with dissolve
    player_name "Hi, {b}Mrs. Johnson{/b}!"
    show player 1 at left
    show mrsj 17 at right
    mrsj "Hi, {b}[firstname]{/b}!"
    show player 11 at left
    show mrsj 18 at right
    mrsj "You're starting to look fit, young man!"
    show player 29 at left
    show mrsj 14 at right
    player_name "Oh. Thanks..."
    player_name "So, are you..."
    show player 1 at left
    show mrsj 17 at right
    mrsj "Is there anything you wanted to talk about?"
    return

label mrsj_button_yoga_room_dialogue_hows_erik:
    show player 10 at left
    show mrsj 14 at right
    player_name "How's {b}Erik{/b} these days?"
    player_name "I hardly see him."
    show mrsj 18 at right
    show player 5 at left
    mrsj "Well... You know how he is!"
    mrsj "He just loves his video games..."
    show player 10 at left
    show mrsj 14 at right
    player_name "Yeah, but it's been even worse lately."
    player_name "I don't even get text messages from him..."
    show mrsj 19 at right
    show player 5 at left
    mrsj "..."
    show mrsj 20 at right
    show player 11 at left
    mrsj "You know, I think he's having problems adjusting to life out on his own."
    mrsj "I worry about him."
    show mrsj 19 at right
    show player 12 at left
    player_name "I had no idea."
    show mrsj 20 at right
    show player 11 at left
    mrsj "He's not used to being the man of the house."
    mrsj "... And he has such a hard time with girls."
    show mrsj 19 at right
    mrsj "The poor thing has to be lonely."
    show mrsj 14 at right
    show player 21 at left
    player_name "... Yeah. I think I understand."
    show mrsj 18 at right
    show player 13 at left
    mrsj "It's a good thing he has a loyal friend like you, {b}[firstname]{/b}!"
    mrsj "He needs you."
    show mrsj 14 at right
    show player 17 at left
    player_name "Well, we've always been friends so..."
    show mrsj 18 at right
    show player 1 at left
    mrsj "I'll tell him to text you more often!"
    show mrsj 14 at right
    show player 14 at left
    player_name "It's alright, I just wanted to make sure he's okay."
    show mrsj 17 at right
    show player 1 at left
    mrsj "Is there anything else you wanted to talk about?"
    return

label mrsj_button_yoga_room_dialogue_poker:
    show mrsj 14 at right
    show player 14 at left
    player_name "I was wondering if you'd like to join {b}Erik{/b} and me for poker?"
    show player 1
    show mrsj 17
    mrsj "I can't right now, I have to teach a class..."
    mrsj "But I'm in my room most {b}evenings{/b}, ask me again then."
    show player 18
    show mrsj 14
    player_name "Thanks, {b}Mrs. Johnson{/b}, I will!"
    return

label mrsj_button_yoga_room_dialogue_what_was_that:
    call expression game.dialog_select("mrsj_button_yoga_room_dialogue_what_was_that_pre")
    if M_anna.is_state(S_anna_start):
        call expression game.dialog_select("mrsj_button_yoga_room_dialogue_what_was_that_anna_intro")
        $ M_anna.trigger(T_anna_intro)
    call expression game.dialog_select("mrsj_button_yoga_room_dialogue_what_was_that_after")
    return

label mrsj_button_yoga_room_dialogue_what_was_that_pre:
    show mrsj 14 at right
    show player 14 at left
    player_name "What was that yoga pose you were doing earlier?"
    show mrsj 13 at right
    show player 13 at left
    show player 1 at left
    mrsj "Oh, I'll show you!"
    show mrsj 12 at right
    show player 11 at left
    mrsj "You start like this!"
    show mrsj 11 at right
    window hide
    pause
    show player 21 at left
    show mrsj 10 at right
    window hide
    pause
    mrsj "All the way down on your knees!"
    window hide
    pause
    show player 21 at left
    player_name "Uhhh..."
    player_name "... Yeah..."
    show player 11 at left
    mrsj "It's called the \"Cat Cow\"!"
    show mrsj 11 at right
    window hide
    pause
    show mrsj 12 at right
    window hide
    pause
    show mrsj 13 at right
    show player 18 at left
    mrsj "Not bad, right?"
    return

label mrsj_button_yoga_room_dialogue_what_was_that_anna_intro:
    show old_anna 12f at Position (xpos=600)
    show mrsj 13 at right
    show player 13
    with dissolve
    anna "Hello, {b}Tammy{/b}."
    show old_anna 5f
    anna "Don't tell me you started without me."
    show old_anna 4f
    show mrsj 18
    mrsj "Of course not! I'm just chatting with a friend of my tenant, {b}Erik{/b}!"
    show old_anna 11 at Position (xpos=700) with dissolve
    show mrsj 17b
    mrsj "{b}Anna{/b}, this is {b}[firstname]{/b}. {b}[firstname]{/b}, this is my friend, {b}Anna{/b}."
    show mrsj 14
    show player 36 with dissolve
    player_name "Hi!"
    show player 13 with dissolve
    show mrsj 14b
    show old_anna 12
    anna "You're a friend of {b}Erik{/b}?"
    show old_anna 11
    show player 14
    show mrsj 14
    player_name "Yeah. We've been friends for a long time."
    show player 12
    player_name "Are you a trainer here too?"
    show player 5
    show old_anna 2 with dissolve
    show mrsj 14b
    anna "Oh, no. I'm just a student."
    show old_anna 1
    show player 13
    show mrsj 17
    mrsj "{b}Anna{/b} is one of my best. She could teach here if she wanted to!"
    show mrsj 14b
    show old_anna 3
    anna "Oh, I don't think so! Haha!"
    show old_anna 2
    anna "She's a great teacher and I'm just a novice."
    show old_anna 1
    show mrsj 17
    mrsj "{b}Anna{/b}, is just being humble."
    show mrsj 17b
    mrsj "She might be a beginner, but she is very talented... And extremely flexible."
    show mrsj 14b
    show old_anna 3
    anna "Haha."
    show old_anna 2
    anna "I've gotta go now and get ready for my next lesson."
    show old_anna 3
    anna "Goodbye, {b}Tammy{/b}!"
    show old_anna 1
    show mrsj 17b
    mrsj "See you soon."
    show mrsj 14b
    show old_anna 2
    anna "It was a pleasure meeting you, {b}[firstname]{/b}."
    show old_anna 1
    show player 14
    show mrsj 14
    player_name "Bye!"
    hide old_anna with dissolve
    return

label mrsj_button_yoga_room_dialogue_what_was_that_after:
    show mrsj 17 at right
    show player 1 at left
    mrsj "Is there anything else you wanted to talk about?"
    return

label mrsj_button_yoga_room_dialogue_youre_so_fit:
    show mrsj 14 at right
    show player 29 at left
    player_name "I have to say, {b}Mrs. Johnson{/b}, you are really fit!"
    player_name "Do you exercise a lot?"
    show mrsj 18 at right
    show player 13 at left
    mrsj "Aw... You're so nice!"
    show mrsj 17 at right
    mrsj "Well, I come here as often as I can and try to use the gym..."
    mrsj "... I also go jogging! And I do yoga in my room at night as well..."
    show mrsj 19 at right
    show player 21 at left
    player_name "Well, it's working!"
    show player 13 at left
    mrsj "You think?"
    show mrsj 15 at right
    show player 11 at left
    mrsj "My butt is still a bit big..."
    show mrsj 16 at right
    show player 23 at left
    mrsj "... And my boobs are not like they used to be..."
    player_name "..."
    show player 28 at left
    show mrsj 19 at right
    player_name "{i}*Gulp*{/i}"
    show player 1 at left
    show mrsj 18 at right
    mrsj "Is there anything else you wanted to talk about?"
    return

label mrsj_button_yoga_room_dialogue_have_to_train:
    show mrsj 14 at right
    show player 14 at left
    player_name "I should get back to my training!"
    show mrsj 18 at right
    show player 1 at left
    mrsj "Okay, then!"
    show mrsj 14 at right
    show player 17 at left
    player_name "Bye, {b}Mrs. Johnson{/b}!"
    hide player 17 at left with dissolve
    hide mrsj 14 at right with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
