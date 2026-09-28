label jane_library_dialogue_bissette_find_dictionary:
    show jane:
        flip
        xoffset 100
    show xtra 42
    show player 10f at right
    with dissolve
    player_name "I can't seem to find a {b}French dictionary{/b}."
    show player 5f
    jane "Hmm, let me see..."
    show jane f_normal_down
    pause
    jane "It should be over on there on shelf, next to the back room."
    show jane f_normal
    show player 14f
    player_name "Alright, I'll take a look. Thanks."
    return

label jane_library_dialogue_bissette_get_dictionary:
    show jane f_normal:
        flip
        xoffset 100
    show xtra 42
    show player 504f at right
    with dissolve
    player_name "Well, I found part of a {b}French dictionary{/b}."
    show player 503f
    show jane f_sad
    jane "What?"
    show player 5f
    show jane f_complain_down a_book1
    with dissolve
    jane "Oh no!"
    jane "I'll have to order a new one but it'll take a while to arrive."
    show jane f_sad
    jane "Did you still want to check it out?"
    show player 10f
    player_name "Yeah, I'm pretty desperate. I'll just have to hope I don't need those missing pages..."
    show player 5f
    jane "Okay, well, sorry again!"
    show jane f_normal
    jane "You can just keep it. It won't be much use around here..."
    show jane a_idle with dissolve
    show player 504f with dissolve
    player_name "Thanks!"
    show player 503f
    show jane f_laugh
    jane "No problem, have a nice day!"
    hide player
    hide jane
    with dissolve

    scene library
    show player 34 with dissolve
    player_name "( I guess I should take this to {b}Miss Bissette{/b} and see what she thinks... )"
    return

label jane_library_dialogue_bissette_return_overdue_books:
    show jane f_normal:
        flip
    show xtra 42
    show player 14f at right
    with dissolve
    player_name "I found all the overdue books!"
    show player 239_240f with dissolve
    pause
    show player 507f at Position (xoffset=-9) with dissolve
    jane "Really? Let's see..."
    show player 13f
    show jane a_book3 with dissolve
    jane "You did it! Thanks a lot!"
    jane "I've got something for you too."
    show player 10f
    player_name "You do?"
    show jane a_book2 with dissolve
    jane "Yup, that book you ordered came in."
    pause
    show player 521f
    show jane a_idle
    with dissolve
    player_name "Thanks!"
    player_name "{b}My cheese and me{/b}..." (show_native="{b}Mon fromage et moi{/b}...")
    show player 5f with dissolve
    jane "Will that work?"
    show player 10f
    player_name "Err, I'll have to make do."
    show player 14f
    player_name "Thanks again!"
    show player 13f
    show jane f_laugh
    jane "Come back and see us!"
    return

label jane_library_dialogue_pre:
    show jane:
        flip
        xoffset 100
    show xtra 42
    show player 1f at right
    with dissolve
    jane "Hi! How can I help you?"
    show player 2f
    player_name "Hi, I'm looking for a {b}book{/b}."
    show player 1f
    jane "Sure thing! Do you know the book's name?"
    return

label jane_library_dialogue_production_ask_librarian:
    scene librarydesk
    show jane:
        flip
        xoffset 100
    show xtra 42
    show player 10f at right
    with dissolve
    player_name "You wouldn't happen to have any books on increasing milk production in cows, would you?"
    show player 5f
    show jane f_sad
    jane "Umm, that's a weird question."
    show jane f_normal
    show player 29f with dissolve
    player_name "Ehh, yeah. I suppose it is."
    player_name "It's for my uhh... friend."
    show player 3f at Position (xoffset=-8)
    show jane f_laugh
    jane "Heh, sure it is."
    show jane f_eyeroll a_hand_out with dissolve
    jane "Umm, I don't know."
    jane "I'm sure we have stuff on cows but as far as milking goes..."
    show jane f_normal
    jane "... {b}Try that shelf over there{/b}."
    show jane a_idle
    show player 14f
    with dissolve
    player_name "Thanks!"
    hide player with dissolve
    pause
    show jane f_sad
    jane "What a weirdo."
    hide jane
    with dissolve
    return

label jane_library_dialogue_french_poetry:
    show player 10f
    player_name "Do you have any French poetry?"
    show player 5f
    show jane f_normal_down
    jane "Hmm..."
    show jane f_normal
    jane "Actually..."
    jane "Some girls were here reading something like that {b}yesterday afternoon{/b}."
    show player 10f
    player_name "Really?"
    show player 12f
    player_name "Did they check it out?"
    show player 5f
    jane "No."
    show player 10f
    player_name "Do you know where it is?"
    show player 5f
    show jane f_normal_down
    jane @ -m_talk "..."
    show jane f_sad
    jane "No..."
    jane "But, maybe they'll be here again this {b}afternoon{/b}."
    jane "You could ask one of them where they put it."
    show jane f_normal
    show player 12f
    player_name "Thanks."
    return

label jane_library_dialogue_french_food_find_books:
    show player 10f
    player_name "I was wondering if you had any books in French about food?"
    show player 13f
    show jane f_laugh
    jane "That's an interesting subject..."
    show jane f_normal
    show player 14f
    player_name "Yeah, I need it for a school assignment."
    show player 13f
    jane "Alright, let me look and see what we have."
    show jane f_normal_down
    jane @ -m_talk "..."
    show player 11f
    player_name "..."
    show player 5f
    jane "Hmm, we don't appear to have anything like that."
    show jane f_normal
    show player 12f
    player_name "Nothing?"
    show player 5f
    show jane f_normal_down
    jane "No... Oh, wait a second!"
    jane "It's saying our sister branch has a French book about cheese."
    show jane f_normal
    jane "Would that work?"
    show player 14f
    player_name "Sure, I love cheese! Where do I need to pick it up?"
    show player 13f
    jane "I can request them to send it here. Should only take a few days..."
    jane "In the meantime, I wonder if you could you help me out with something?"
    show player 10f
    player_name "... Sure, I suppose. What is it you need?"
    show player 5f
    jane "{b}Some of your classmates have overdue books{/b} I'd like returned."
    jane "I've been sending letters to their homes but that doesn't seem to be working."
    jane "I'd hate to lose the books."
    show player 10f
    player_name "Yeah, I could try {b}speaking with them{/b}. What are their names?"
    show player 5f
    show jane f_normal_down
    jane "Hmm, the first is a {b}Miss Martinez{/b}."
    jane "The second is a {b}Mr. Erik J{/b}-"
    show jane f_normal
    show player 14f
    player_name "{b}Erik{/b} has a book out?!"
    player_name "Those should be easy."
    show player 13f
    show jane f_normal_down
    jane "... And finally..."
    jane "Huh. It just says {b}Dexter{/b}."
    jane "Ring any bells?"
    show jane f_normal
    show player 12f
    player_name "Oh man, not {b}Dexter{/b}... You're sure?"
    show player 11f
    jane "That's what the log says..."
    show player 12f
    player_name "Crap! Alright, I'll see what I can do."
    show player 5f
    show jane f_laugh
    jane "Thanks, I really appreciate this!"
    hide jane with dissolve
    show player 12 at center with dissolve
    player_name "Ugh, why did it have to be {b}Dexter{/b}?"
    return

label jane_library_dialogue_french_food_book_holders:
    show player 10f
    player_name "What were the students names again?"
    player_name "You know, the ones with the overdue books."
    show player 5f
    show jane f_normal
    jane "One second..."
    show jane f_normal_down
    jane "Hmm, {b}Miss Martinez{/b}, {b}Mr. Erik{/b}, and a {b}Dexter{/b}."
    show jane f_normal
    show player 12f
    player_name "Ugh, I forgot about {b}Dexter{/b}..."
    player_name "Alright, I'm on it."
    return

label jane_library_dialogue_magazines_first:
    show player 2f
    player_name "I'm making a collage for art class and I need some old magazines."
    player_name "Could you show me where to find some?"
    show player 1f
    show jane f_normal
    jane "You're out of luck I'm afraid. We stopped carrying those a few months ago."
    show player 10f
    player_name "You don't have any?"
    show player 1f
    jane "I'm afraid not. We sent all the ones we had off to be recycled."
    show player 10f
    player_name "Oh man..."
    player_name "Thanks anyways."
    show player 11f
    jane "Sorry."
    hide jane
    hide xtra
    hide player
    with dissolve
    show player 10 with dissolve
    player_name "What am I gonna do now?"
    show player 11
    player_name "..."
    show player 10
    player_name "I guess {b}I'll head back to school and look around{/b}."
    player_name "There's gotta be some magazines somewhere."
    return

label jane_library_dialogue_magazines_repeat:
    show player 10f
    player_name "So you don't have a single magazine around here?"
    show player 11f
    show jane f_normal
    jane "Nope."
    jane "We canceled the subscriptions and tossed what we had out."
    show player 10f
    player_name "Okay, thanks anyways."
    hide jane
    hide xtra
    hide player
    with dissolve
    show player 10 with dissolve
    player_name "{i}*Sigh*{/i}"
    player_name "I guess I should {b}head back to school and look around there{/b}."
    player_name "... Maybe I'll get lucky?"
    return

label jane_library_dialogue_return_books_pre:
    show player 14f
    player_name "I'd like to return a book."
    show player 13f
    show jane f_laugh
    jane "Great!"
    return

label jane_library_dialogue_return_books_first:
    show jane f_normal
    jane "Not many people do."
    show player 10f
    player_name "What happens then?"
    show player 5f
    show jane f_mad
    jane "I hunt them down and break one of their legs, so they don't do it again."
    show player 22f
    player_name "!!!"
    show jane f_laugh
    jane "Just kidding!"
    show jane f_normal
    show player 29f with dissolve
    player_name "Oh."
    show player 3f at Position (xoffset=-8)
    return

label jane_library_dialogue_return_books_after:
    show jane f_normal
    jane "Just set the books you want to return on the counter and I'll take care of it."
    show jane f_laugh
    jane "And come back soon!"
    return

label jane_library_dialogue_leave:
    show player 24f
    show jane f_sad
    player_name "Sorry. I'll return once I remember the book's name."
    show player 5f
    show jane f_normal
    jane "See you then."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
