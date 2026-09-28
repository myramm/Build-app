label beach_house_entrance_mysterious_statue_3:
    scene expression player.location.background_blur with None
    show player 5 at left
    show consuela f_unsure
    with dissolve
    consuela "Eh, excuse me... {b}Mister [firstname]{/b}."
    show consuela f_normal
    player_name "Hmm?"
    show player 10
    player_name "Oh, hey {b}Consuela{/b}."
    show player 5
    show consuela a_statue with dissolve
    consuela "I find."
    show player 11
    player_name "!!!"
    show player 10
    player_name "Y-you found this?"
    show player 11
    consuela "Sí, I find."
    player_name "This looks like the final piece of that statue!"
    show player 14
    player_name "The one that belonged to {b}Clyde{/b}'s grandfather."
    player_name "It was in the house?"
    show player 13
    show consuela f_unsure
    consuela "Ehh..."
    consuela "I find... Bed."
    consuela "You want?"
    show consuela f_normal
    show player 14
    player_name "Oh, yes please."
    show consuela a_idle
    show player 714
    with dissolve
    pause
    show player 714b
    player_name "Thank you, {b}Consuela{/b}."
    show player 714
    show consuela f_laugh
    consuela "Si, {b}Mister [firstname]{/b}."
    hide consuela with dissolve
    consuela "I wouldn't sleep here with such strange things under the bed..." (show_native="No dormiría aquí con cosas tan extrañas debajo de la cama...")
    player_name "( Hmm. )"
    player_name "( I wonder how it got under the bed? )"
    pause
    player_name "( Well, regardless... I have all three pieces now. )"
    pause
    player_name "( I bet {b}Diane{/b} would be interested in this statue. )"
    player_name "( {b}I should show it to her the next time I'm working at her place{/b}. )"
    hide player with dissolve
    return

label beach_house_first_time:
    scene expression player.location.background_blur
    show player 14
    with dissolve
    player_name "Whoa, this is awesome!"
    player_name "There's so much space!"
    show player 1
    pause
    show player 14
    player_name "I can't believe it's really mine!"
    show player 1
    pause
    show player 14
    player_name "I guess I should start looking into {b}buying some furnishings{/b}."
    player_name "... Really fix this place up nice!"
    return

label beachhouse_weekday_just_wokeup:
    scene expression L_beachhouse_bedroom.background_blur with fade
    show player 7 with dissolve
    player_name "{i}*Yawn*{/i}"
    show player 8
    window hide
    pause
    show player 9
    player_name "( I should get ready for school... )"
    hide player with dissolve
    return

label beachhouse_weekend_just_wokeup:
    scene expression L_beachhouse_bedroom.background_blur with fade
    show player 7 with dissolve
    player_name "{i}*Yawn*{/i}"
    show player 8
    window hide
    pause
    show player 9
    player_name "( What should I do this weekend... )"
    hide player with dissolve
    return

label beach_house_future:
    scene expression player.location.background_blur
    show anon f_surprised with dissolve
    anon @ -m_talk "( This place looks amazing! )"
    anon f_grin @ -m_talk "( I'd love to live on the beach {b}one day{/b}. )"
    anon a_thinking f_thinking @ -m_talk "( Maybe when the current owner wants to sell I could come back... )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
