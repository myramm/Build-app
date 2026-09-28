label movie_theatre_movie_select_after(movie="foxxy_roxxy"):
    if player.has_money(50):
        if movie == 'bitch_perfect':
            $ player.spend_money(50)
            $ game.timer.tick()
        call expression game.dialog_select("movie_theatre_watch_movie_{}".format(movie))
    else:
        call expression game.dialog_select("movie_theatre_watch_movie_no_money")
    if game.timer.is_night():
        $ player.go_to(L_map)
    else:
        $ player.go_to(L_movie_theatre)
    $ game.main()

label movie_theatre_movie_select_after_dialogue:
    scene movie_lobby
    show bubbles o_desk:
        flip
    show anon f_normal at flip
    with fade
    bubbles "Good pick!"
    show bubbles a_tickets with dissolve
    bubbles "Here's your ticket."
    show bubbles a_idle with dissolve
    anon "Thanks."
    bubbles @ f_worried "Just don't make a mess on the seats."
    bubbles "I hate cleaning that stuff off!"
    anon f_surprised_teeth "..."
    bubbles "Enjoy!"
    return

label movie_theatre_watch_movie_foxxy_roxxy:
label movie_theatre_watch_movie_dirty_harold:
label movie_theatre_watch_movie_its_a_trap:
    scene movie_lobby
    if M_bubbles.get("unavailable_movie_first"):
        $ M_bubbles.set("unavailable_movie_first", False)
        show bubbles o_desk at flip
        show anon f_normal at flip
        with fade
        anon "What's this movie? I haven't even heard of it."
        show bubbles f_worried
        bubbles "Oh, that one? That movie is actually sold out at the moment."
        anon f_worried "When's the next available showing?"
        show bubbles f_normal
        bubbles "Let me see..."
        bubbles "...{w}...{w}..."
        bubbles "It appears it's sold out all day today."
        anon f_surprised @ -m_talk "!!!"
        anon f_skeptical "Really?"
        show anon f_thinking a_thinking with dissolve
        anon @ -m_talk "( He didn't even look... )"
        show anon f_skeptical a_idle with dissolve
        anon "Alright, I guess I'll pick a different movie then."
    else:
        show bubbles o_desk at flip
        show anon f_worried at flip
        with fade
        anon "Is that movie still sold out?"
        bubbles "I'm afraid so."
        anon f_skeptical "Alright, I guess I'll pick a different movie then."
    return

label movie_theatre_watch_movie_bitch_perfect:
    show anon f_normal
    anon "How about... {b}Bitch Perfect{/b}."
    show bubbles f_worried
    bubbles "Ehh, are you sure you wanna see that one?"
    anon f_worried @ -m_talk "Hmm?"
    show bubbles f_normal
    bubbles "Heh, never mind..."
    anon f_normal @ -m_talk "..."
    show bubbles a_tickets with dissolve
    bubbles "Here you go, enjoy the movie!"
    show bubbles a_idle
    show anon a_ticket
    with dissolve
    anon "Thanks."
    scene black with fade
    pause
    scene expression "backgrounds/location_mall_movie_cutscene03.jpg" with fade
    "... And remember to check out our snack bar."
    "We've got everything a moviegoer could want!"
    "Popcorn, nachos, hotdogs, candy... Even delicious Slurpees!"
    scene expression "backgrounds/location_mall_movie_cutscene02.jpg" with fade
    "Thank you for choosing {b}CineSaga Theater{/b}!"
    "Please remember to be courteous. The feature is on the BIG SCREEN."
    "Don't talk, don't text, don't ruin the movie!"
    scene expression "backgrounds/location_mall_movie_cutscene_bitch01.jpg" with fade
    pause
    scene expression "backgrounds/location_mall_movie_cutscene_bitch02.jpg" with fade
    pause
    scene expression "backgrounds/location_mall_movie_cutscene_bitch03.jpg" with fade
    pause
    scene black with fade
    return

label movie_theatre_watch_movie_no_money:
    show anon f_worried
    anon "Hmm, I guess I don't have enough money..."
    show bubbles f_worried
    bubbles "Oh, ehh..."
    bubbles "Sorry, I can't let people in for free."
    anon f_tired "Yeah, I understand."
    show bubbles f_normal
    bubbles "Don't worry though."
    bubbles "We don't cycle our movies out that often..."
    show bubbles f_worried
    bubbles "... Or ever, really, heh..."
    show bubbles f_normal
    anon f_worried @ -m_talk "..."
    bubbles "You can always come back and see it another time."
    anon "Thanks, will do."
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
