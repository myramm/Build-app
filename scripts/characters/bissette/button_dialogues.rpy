label bissette_dialogue_dress_code:
    hide player
    hide bissette
    show teacher 1 at right
    show anon f_worried
    anon "Actually, I was hoping you could talk to {b}Mrs. Smith{/b} about the new dress code policy..."
    show teacher 5
    bissette "Quoi?"
    show teacher 2
    bissette "The dress code?"
    show teacher 1
    anon "Yeah."
    show teacher 2
    bissette "I have not heard of this before?"
    show teacher 1
    anon f_unimpressed_bored "Well, {b}Mrs. Smith{/b} just implemented it and it's really very silly..."
    anon f_worried @ f_unimpressed_bored "It forbids us from dying our hair and I just thought-"
    show teacher 2
    bissette "You are thinking of dying the hairs?"
    show teacher 1
    anon @ f_surprised "Hmm?"
    anon @ f_normal "Oh, no... Not me."
    anon "I was worried about {b}Eve{/b}, you know?"
    show teacher 2
    bissette "Ah, yes... The blue hairs."
    show teacher 1
    anon "Yeah, she really likes it and I just thought-"
    show teacher 5
    bissette "I'm sorry, {b}[firstname]{/b}..."
    bissette "I wish to be helpful but I have too much trouble with the principal already..."
    show teacher 4
    anon "It's okay, {b}Miss Bissette{/b}."
    anon "I understand."
    show teacher 2
    bissette "Perhaps one of the other teachers could be helping you?"
    show teacher 1
    anon "Yeah, I'll ask one of them."
    hide anon with dissolve
    return

label bissette_dialogue_meet_in_office:
    hide anon
    show player 10 at left
    show teacher 1 at right
    with dissolve
    player_name "{b}Miss Bissette{/b}, what did you need me to do?"
    show player 5
    show teacher 12
    bissette "Oh, {b}[firstname]{/b}. Not here. {b}Come see me in my office after school{/b}, yes?"
    show teacher 13
    show player 14
    player_name "Okay, I'll meet you there."
    return

label bissette_dialogue_check_dictionary:
    hide anon
    show teacher 1 at right
    show player 10 at left
    with dissolve
    player_name "Hey, {b}Miss Bissette{/b}. I found a {b}dictionary{/b} at the library but it's missing a few pages."
    show player 239_240 with dissolve
    pause
    show player 503 with dissolve
    pause
    show player 5
    show teacher 22b
    with dissolve
    bissette "Oh, my!"
    bissette "This will make things very difficult, I think."
    bissette "The French to English section is intact but you are missing many words..."
    bissette "I'm afraid some of them might be crucial to the subjects we are to be studying."
    show teacher 21b
    show player 10
    player_name "Ugh, I was afraid of that..."
    show player 5
    show teacher 21
    bissette "Hmm, perhaps all is not lost. I'm sure {b}a classmate of yours would be willing to let you copy the missing pages from their dictionary{/b}."
    bissette "You can {b}use the photocopier in the computer lab{/b}."
    show teacher 22
    show player 14
    player_name "That's a good idea!"
    show player 13
    show teacher 2 with dissolve
    bissette "Tu es le bienvenu, {b}[firstname]{/b}."
    bissette "Be sure to get English words beginning with the letter \"B\" for our next lesson."
    show teacher 1
    show player 14
    player_name "Alright, {b}time to track down another dictionary{/b}..."
    show player 13
    show teacher 12
    bissette "Working so hard already. I can tell you are desiring the special reward, very much, yes?"
    show teacher 13
    show player 10
    player_name "Any thoughts on whose {b}dictionary{/b} I should be asking to borrow?"
    show player 13
    show teacher 11
    bissette "Hmm..."
    show teacher 2
    bissette "Perhaps {b}Judith{/b}?"
    bissette "She shows much talent for the French tongue..."
    show teacher 1
    show player 14
    player_name "Okay, {b}I'll start with Judith then{/b}."
    return

label bissette_dialogue_intro:
    show anon
    show bissette
    with dissolve
    bissette "Hi, {b}[firstname]{/b}!"
    anon @ f_laugh "Hi, {b}Miss Bissette{/b}!"
    bissette @ a_finger "Have you been able to catch up on your studies?"
    bissette "I really hope you do!"
    bissette "Now, is there something you wanted to talk about?"
    return

label bissette_dialogue_food_assignment_intro:
    hide anon
    hide bissette
    show teacher 1 at right
    show player 10 at left
    player_name "What's my next assignment?"
    show player 5
    show teacher 2
    bissette "I want you to {b}write a few paragraphs about your favorite food, en Français{/b}."
    bissette "Then we will go over it together, yes?"
    show teacher 1
    show player 14
    player_name "Oh, yeah!"
    return

label bissette_dialogue_food_assignment_prepare_assignment:
    anon "I should visit that librarian again. Maybe she could find a book about {b}French food{/b} for me."
    anon "Then I can type something up at my computer."
    anon "Thanks, {b}Miss Bissette{/b}!"
    return

label bissette_dialogue_food_assignment_do_assignment:
    anon "I should type something up at my computer."
    anon "Thanks, {b}Miss Bissette{/b}!"
    return

label bissette_dialogue_poem_assignment_intro:
    hide anon
    hide bissette
    show teacher 1 at right
    show player 10 at left
    player_name "Remind me, what was the assignment again?"
    show player 5
    show teacher 2
    bissette "Lequel? Tu as déjà oublié?"
    bissette "You are to be {b}writing a romantic poem en Français{/b}!"
    show teacher 1
    show player 14
    player_name "Oh, right!"
    player_name "Thanks, {b}Miss Bissette{/b}."
    show player 13
    show teacher 2
    bissette "{b}Return to me once it's complete{/b}."
    bissette "Don't keep me waiting, mon bel homme."
    return

label bissette_dialogue_poem_assignment_do_assignment:
    hide anon
    show player 14 at left
    player_name "I should type something up at my computer."
    return

label bissette_dialogue_poem_assignment_print_assignment:
    hide anon
    hide bissette
    show teacher 1 at right
    show player 14 at left
    player_name "I finished the poem, {b}Miss Bissette{/b}."
    show player 13
    show teacher 2
    bissette "Great, let me see!"
    show teacher 1
    show player 10
    player_name "Oh, I need to print it out first..."
    show player 5
    show teacher 2
    bissette "Well, the printer is in the {b}computer lab{/b}, yes?"
    show teacher 1
    show player 14
    player_name "Yup, be right back!"
    return

label bissette_dialogue_private_tutoring:
    hide anon
    hide bissette
    show teacher 1 at right
    show player 10 at left
    player_name "Do you think we could meet in your office tonight?"
    show player 26
    player_name "You know, for some... Tutoring?"
    show player 13
    show teacher 12
    bissette "Oh, tutoring. Oui!"
    bissette "I'll see you tonight for some one-on-one time, yes?"
    show teacher 13
    show player 33
    player_name "Oui!"
    show player 13
    show teacher 12
    bissette "Très bien, mon bel homme!"
    return

label bissette_dialogue_tutoring:
    hide anon
    hide bissette
    show teacher 1 at right
    show player 10 at left
    player_name "I was wondering if you were still offering private tutoring?"
    show player 5
    show teacher 3
    bissette "Oh, oui!"
    show teacher 1
    show player 14
    player_name "Awesome! When would you be availa-"
    show player 11
    show teacher 2
    bissette "Impressionnant! You're the first student to inquire about the tutoring!"
    show teacher 1
    show player 12
    player_name "Really? That's weird..."
    show player 5
    show teacher 5
    bissette "I was beginning to think nobody was interested in the special reward."
    show teacher 1
    show player 12
    player_name "Oh yeah, I forgot about the special reward..."
    show player 5
    show teacher 5
    bissette "Quoi? You are not desiring the reward either?!"
    show teacher 4
    show player 29 with dissolve
    player_name "Err... No, I mean... A-a special reward sounds wonderful, {b}Miss Bissette{/b}."
    show player 3
    show teacher 3
    bissette "Ah superbe!"
    show teacher 2
    bissette "Then we will meet after school for some one-on-one lessons, yes?"
    show teacher 1
    show player 10 with dissolve
    player_name "Umm... Yeah, I think that will-"
    show player 11
    show teacher 2
    bissette "Très bien!"
    bissette "Just be sure to {b}bring your French dictionary{/b} along."
    show teacher 1
    show player 24
    player_name "Ah, crap. About that... {b}Miss Bissette{/b}, I can't seem to find my {b}French dictionary{/b}."
    show player 25
    player_name "It's not in my backpack, my house, or my locker..."
    show player 5
    show teacher 5
    bissette "Oh non, this is not good!"
    bissette "Perhaps you should {b}stop by the library{/b} and see if they have one?"
    show teacher 2
    bissette "I would loan you mine, but I'm afraid I've recently spilled wine upon it."
    show teacher 1
    show player 14
    player_name "Oh yeah, I forgot about the library!"
    show player 13
    show teacher 2
    bissette "Oui, I go there quite often myself."
    show teacher 12
    bissette "I love the feel of a good book in my hands."
    bissette "Cuddled up by the warm fire with some strong wine..."
    bissette "C'est le paradis."
    show teacher 13
    show player 11
    player_name "..."
    show teacher 2
    bissette "Oh, silly me, babbling on and on. Just {b}let me know when you have the dictionary{/b}, yes?"
    show teacher 1
    show player 14
    player_name "Sure thing, {b}Miss Bissette{/b}."
    return

label bissette_dialogue_get_dictionary:
    hide anon
    hide bissette
    show teacher 1 at right
    show player 12 at left
    player_name "Remind me what I need to get before we can study together?"
    show player 5
    show teacher 2
    bissette "You will need a {b}French to English dictionary{/b}."
    bissette "{b}Check the library{/b}, yes?"
    show teacher 1
    show player 14
    player_name "Oh, that's right!"
    player_name "Thanks!"
    return

label bissette_dialogue_replace_missing_pages:
    hide anon
    hide bissette
    show teacher 1 at right
    show player 12 at left
    player_name "What was I supposed to do again?"
    show player 5
    show teacher 2
    bissette "{b}Copy the pages you are missing from a classmate's dictionary{/b}."
    show teacher 1
    show player 14
    player_name "Oh, that's right!"
    show player 13
    show teacher 2
    bissette "Check with {b}Judith{/b}. She is very good with her French."
    show teacher 1
    show player 14
    player_name "And then {b}the computer lab has the copy machine{/b}..."
    player_name "Got it, thanks again!"
    return

label bissette_dialogue_chat:
    hide teacher
    hide player
    show bissette
    show anon f_shy a_behind_head
    anon "{b}Miss Bissette{/b}, I just wanted to say that I really appreciate the help with catching up on my school work!"
    show anon f_normal
    bissette f_sexy @ f_laugh a_hair "It's my pleasure! All I want is to make sure that you are motivated to perform..."
    bissette "... And I love rewarding hardworking students!"
    anon "I'll do my best. I really want to get a good grade..."
    bissette f_normal "That's what I like to hear!"
    bissette "I can {b}review your homework with you{/b} when you hand it in, if you want!"
    anon @ f_laugh "That sounds good, {b}Miss Bissette{/b}! Thank you!"
    return

label bissette_dialogue_leave:
    hide player
    hide teacher
    show anon f_normal
    show bissette
    anon "No. I just wanted to say hello."
    bissette f_normal "Well, take a seat. Class will be starting soon!"
    bissette @ f_laugh "I've got an exciting lesson planned for today!"
    anon "Sounds good, {b}Miss Bissette{/b}."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
