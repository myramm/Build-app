label bubbles_button_intro:
    scene movie_lobby with None
    show bubbles o_desk:
        flip
    show anon at flip
    with dissolve
    bubbles "Welcome to CineSaga Theater, my name is {b}Bubbles{/b}."
    bubbles "How can I help you?"
    return

label bubbles_movie_select_pre:
    anon f_normal "I'd like to see a movie."
    show bubbles f_normal
    bubbles "Sure."
    bubbles "{b}Tickets are fifty dollars{/b} and all you have to do is select the one you want to see..."
    anon "Cool!"
    return

label bubbles_button_nevermind:
    anon f_normal "I'm just looking around, thanks."
    show bubbles f_normal
    bubbles "Alright."
    bubbles "Just let me know if you wanna watch something."
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
