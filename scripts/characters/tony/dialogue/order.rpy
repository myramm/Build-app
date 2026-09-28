label tony_dialogue_order:
    anon "I'll take one large pizza, please."
    tony f_normal "Now we're talkin'!"
    tony "What kinda pie are you lookin' for?"

    menu:
        "Veggie pizza ($20)." if M_daisy.is_state(S_daisy_get_pizza) and not player.has_item('veggie_pizza'):
            jump dai02_tony_veggie

        "Veggie pizza ($20)." if M_daisy.get('veggie pizza') and not player.has_item('veggie_pizza'):
            jump tony_dialogue_order.veggie
        "Never mind.":

            pass

    anon "Uhh, actually... Never mind."
    anon "I don't want one after all."
    tony "No?"
    tony "Alright, kiddo."
    pause
    tony "Come back if you change your mind."
    hide anon with dissolve
    return


label tony_dialogue_order.veggie:
    anon "Could I get another {b}veggie pizza{/b}?"
    tony "Sure thing, kiddo."
    tony "That'll be $20."

    if player.has_money(20):
        jump tony_dialogue_order.pizza

    anon f_worried "Oh, crap."
    anon "I don't have enough money on me."
    show tony f_question
    tony "Well, you can't get no pizza without money."
    tony "What are you thinkin' knucklehead?"
    show tony f_suspicious
    anon f_shy @ a_behind_head "Heh, sorry."
    show tony f_question
    tony "Just come back when you got some cash on ya, alright?"
    show tony f_suspicious
    anon f_worried "Will do."
    hide anon with dissolve
    return


label tony_dialogue_order.pizza:
    anon "Here ya go."
    show anon a_money with dissolve
    pause
    show anon a_idle
    show tony f_question a_whisper:
        unflip
        xoffset -400
    with dissolve
    tony "'Ey, {b}Maria{/b}!"
    tony "One vegetable with mushrooms and pineapple, to go."
    maria "Yeah, yeah..."
    hide tony with dissolve
    maria "You know, my mother would burn this place to the ground before she'd put pineapple on a pizza..."
    maria "... It just ain't right."
    tony "Yeah well, it's a good thing I married you and not your mother then, ain't it?"
    maria "Haha!"
    pause
    show tony a_pizza behind counter with dissolve:
        flip
    tony "Here's your pie, kiddo."
    show tony a_idle
    show anon a_pizza
    with dissolve
    anon "Thanks, {b}Tony{/b}."
    hide anon with dissolve
    return 'veggie_pizza'
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
