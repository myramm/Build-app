label dai02_tony_veggie:
    anon "Can I get one with all the vegetables?"
    tony "Sure thing, champ!"
    tony @ a_point "You want mushrooms and pineapple too?"
    anon @ f_laugh "Oh, yes please!"
    tony @ f_smirk_wink "That'll be $20."

    if player.has_money(20):
        jump dai02_tony_veggie.pizza

    anon f_worried "Oh, crap."
    anon "I don't have enough money on me."
    tony f_question "Well, you can't get no pizza without money."
    tony "What are you thinkin' knucklehead?"
    show tony f_suspicious
    anon f_normal @ f_shy a_behind_head "Heh, sorry."
    tony f_normal @ a_frustrated "Just come back when you got some cash on ya, alright?"
    anon "Will do."
    hide anon with dissolve
    return

label dai02_tony_veggie.pizza:
    anon "Here ya go."
    show anon a_money with dissolve
    pause
    show anon a_idle
    show tony f_question:
        unflip
        xoffset -400
    with dissolve
    tony "'Ey, {b}Maria{/b}!"
    tony "We got a customer 'ere!"
    show tony f_suspicious
    maria "I know you ain't yellin' orders at me now, {b}Tony{/b}!"
    maria "You can turn your fat ass around and ask politely."
    show tony f_normal a_heart with dissolve
    tony "Ah, sheesh."
    tony "Can you believe this woman?"
    show anon f_looking_down a_phone with dissolve
    tony "Tch, the balls on her..."
    hide tony with dissolve
    tony "Now you look here woman..."
    tony "It should be you up here dealin' with the customers."
    tony "God knows, we'd be bringing in a lot more business if they saw your pretty face 'ere instead of this ugly mug."
    maria "Yeah, but they'd never come back after they tasted your cookin'!"
    tony "Oh, now that's just mean!"
    tony "Haha!"
    maria "Haha!"
    maria "Yeah, yeah... Come gimme a kiss and take your pie."
    tony "Ah well, who could refuse that?"
    pause
    tony "Hehehe."
    show tony a_pizza behind counter with dissolve:
        flip
    tony "{i}*Ahem*{/i} Uhh, sorry about all that."
    anon f_normal a_idle "No problem."
    tony "Here's your pie."
    show tony a_idle
    show anon a_pizza
    with dissolve
    tony "Enjoy!"
    anon f_brag_closed @ -m_talk "( Oh, this smells really good. )"
    anon @ -m_talk "( I hope {b}Daisy{/b} likes it. )"
    hide anon with dissolve
    return 'veggie_pizza'
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
