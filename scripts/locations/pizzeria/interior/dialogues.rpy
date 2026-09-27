label pizza_interior_diane_delivery_1:
    call tony_button_stage
    show player 13f at right with dissolve
    tony "Well, hey there, kiddo."

    tony "Apa yang membawamu hari ini?"

    show player 14f
    player_name "I have a delivery for you."

    show player 13f
    show tony f_suspicious
    tony "Delivery, eh?"

    show tony f_normal
    tony "... Oh, from the milk place!"

    show player 14f
    player_name "Itu benar."

    show player 239_240f with dissolve
    pause
    show player 163df with dissolve
    tony "Bagus sekali!"

    tony "I dunno what kind of cows you're using, but this milk is amazing!"

    tony "It really takes our pizza dough to a whole 'nother level!"

    show player 163ef
    player_name "Hehe, I'm sure {b}Diane{/b} will be happy to hear that."

    show player 163df
    tony "I'm not joking, kiddo."

    tony "You tell her that next time, I'm gonna triple my order."

    show player 163ef
    player_name "Hehe, oke."

    player_name "Umm, where should I put this?"

    show player 163df
    tony "Oh, right. One second..."

    show tony f_suspicious with dissolve:
        unflip
        xoffset -400
    tony "Hey, {b}Maria{/b}!"

    tony "Getcha butt up here for a second!"

    show tony f_normal with dissolve:
        flip
        xoffset 0
    pause
    show maria a_back behind counter:
        flip
        xoffset -200
    with dissolve
    maria "{i}*Sigh*{/i} What's the matter now, {b}Tony{/b}?"

    show tony f_question
    tony "Ain't nothing the matter, the milk order is here."

    tony "Why don't you take the kid in the back and show him where you keep it?"

    show tony f_normal
    maria @ f_shy "{i}*Sigh*{/i} Yeah, yeah... Alright."

    maria "What's your name, kid?"

    show player 163ef
    player_name "{b}[firstname]{/b}."

    show player 163df
    maria "Oh, that's a nice name!"

    maria "Follow me {b}into the back{/b}, {b}[firstname]{/b}."

    hide maria with dissolve
    player_name "..."
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
