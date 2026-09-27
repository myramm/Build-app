label consumr_eve_get_candle_owned:
    scene expression player.location.background_blur with None
    anon @ -m_talk "( I already have some candles... )"

    if not player.has_item("chocolates"):
        anon @ -m_talk "( I should {b}get some chocolates from Cupid next{/b}. )"

    else:
        anon @ -m_talk "( I have everything I need. I should {b}get back to Eve's place{/b}. )"

    $ game.main()

label consumr_eve_get_candle_bought:
    scene expression player.location.background_blur with None
    show anon a_candles
    show eve
    with dissolve
    anon "These should work, right?"

    eve "Yeah, those are perfect!"

    anon @ f_laugh "Luar biasa!"

    hide anon
    hide eve
    with dissolve
    if player.has_item("chocolates"):
        jump mall_eve_make_up_go_to_mall_has_chocolates_candles
    $ game.main()

label consumr_diane_get_milk_jug_bought:
    scene expression "backgrounds/location_mall_consumr_closeup.jpg"
    show player 173 with dissolve
    player_name "Alright, that should work fine for the jug {b}Diane{/b} wanted."

    label consumr_diane_get_milk_jug_bought.tail:
    show player 172
    pause
    player_name "( Hmm, I wonder if I should speak with {b}Diane{/b} about the stuff {b}Veronica{/b} told me? )"

    player_name "( I'm not sure it applies to her particular problem but it couldn't hurt to look into it. )"

    player_name "( {b}I should head to the library{/b} and see about finding one of those milking books {b}Veronica{/b} mentioned. )"

    hide player with dissolve
    $ M_diane.trigger(T_diane_bought_milk_jug)
    $ game.main()

label consumr_diane_get_milk_jug_owned:
    scene expression "backgrounds/location_mall_consumr_closeup.jpg"
    show player 173 with dissolve
    player_name "Hey! I already had one of these!"

    player_name "This should work fine for the jug {b}Diane{/b} wanted."

    jump consumr_diane_get_milk_jug_bought.tail

label consumr_diane_get_milk_jug:
    scene expression "backgrounds/location_mall_consumr_closeup.jpg"
    show player 13 at left
    show vero f_sexy
    with dissolve
    vero "Well, well, well... Look who's walking into my store!"

    show player 14
    player_name "Hey, {b}Veronica{/b}."

    show player 13
    show vero f_normal
    vero "How's it going, {b}[firstname]{/b}?"

    vero "You still got that green thumb?"

    show player 14
    player_name "Hehe yeah, I guess."

    show player 13
    show vero f_sexy
    vero "Oh, I love a man who knows his way around a garden..."

    show player 29 with dissolve
    player_name "{i}*Gulp*{/i} O-oh, yeah?"

    show player 3
    show vero f_normal
    vero "So what brings you in here?"

    show player 14 with dissolve
    player_name "I need another {b}milk jug for Diane{/b}."

    show player 13
    vero "Ya?"

    vero "How's she doing anyways?"

    vero "I tried to swing by and visit her the other day but there was a bunch of construction going on."

    show player 14
    player_name "Heh, yeah. She knocked down her house and put a barn up."

    show player 13
    show vero f_surprised
    vero "!!!"
    show vero f_normal
    vero "Kamu tidak bilang?!"

    vero "So, I guess she's finally expanding, huh?"

    show player 14
    player_name "Ya, menurutku begitu."

    show player 13
    vero "Has she mentioned hiring additional help at all?"

    show player 14
    player_name "Hmm, a bit..."

    show player 13
    vero "Well, tell her to remember her good friend {b}Veronica{/b} slaving away over here at this dead-end job!"

    show player 17
    player_name "Haha, will do."

    show player 14
    player_name "I think right now she's too busy worrying about producing more milk..."

    show player 13
    vero "Hmm?"

    vero "Her cows are drying up?"

    show player 10
    player_name "I err..."

    show player 5
    vero "Fill me in, {b}[firstname]{/b}."

    vero "I know all there is to know about milking cows."

    show player 10
    player_name "Heh, I dunno... I'm not supposed to talk about it."

    show player 5
    vero "Oh, ayolah!"

    show player 29 with dissolve
    player_name "She just needs her umm... Cow."

    player_name "To... You know, produce more milk."

    show player 3
    vero "Is she impregnating them?"

    show player 11
    player_name "!!!" with hpunch
    show player 10
    player_name "I-impregnating?!"

    show player 11
    vero @ f_laugh "Well, of course!"

    vero "Cows will produce quite a bit of milk on their own but if you really wanna get all you can out of 'em, you gotta knock 'em up."

    show player 29 with dissolve
    player_name "{i}*Gulp*{/i} I don't-"

    show player 3
    vero "It'll double their milk production, easy!"

    vero "Then when the calf is born, you can sell it off for a big profit."

    player_name "..."
    vero "... Or keep it and you got yourself a new worker!"

    vero "It's a great source of extra income."

    show player 29
    player_name "Oh, I don't think she'd want to-"

    show player 3
    vero "Why are you blushing?"

    show player 29
    player_name "aku tidak-"

    show player 3
    vero @ f_laugh "Hehe, what's going on {b}[firstname]{/b}?!"

    show player 12 with dissolve
    player_name "Nothing!"

    show player 10
    player_name "I just... Are you sure?"

    show player 5
    vero "Positive."

    vero "{b}Go to the library and look it up{/b} if you don't believe me, I bet you'll find tons of info about breeding and milking farm animals."

    show player 14
    player_name "Y-ya, oke."

    player_name "I'll do that."

    show player 13
    vero @ f_laugh "Hehe, you're too cute!"

    vero "We've got stainless steel jugs just over there."

    vero "Let me know if you need any more help."

    show player 14
    player_name "Thanks, {b}Veronica{/b}."

    show player 13
    show vero f_sexy
    vero "No problem, stud."

    hide player
    hide vero
    with dissolve
    return

label consumr_okita_get_ingredients:
    call expression game.dialog_select("consumr_okita_get_ingredients_pre")
    if M_okita.get("talked with veronica"):
        call expression game.dialog_select("consumr_okita_get_ingredients_talked_with_veronica")
    return

label consumr_okita_get_ingredients_pre:
    scene expression player.location.background_blur
    show player 2 with dissolve
    player_name "{b}Miss Okita{/b} said that {b}vegetable stock would work best as the base liquid{/b}."

    return

label consumr_okita_get_ingredients_talked_with_veronica:
    show player 10
    player_name "... {b}But they only have chicken stock{/b}."

    player_name "I guess we'll have to make do with the chicken stock."

    show player 2
    player_name "I should {b}buy some and get it back to Miss Okita{/b}."

    hide player with dissolve
    return

label consumr_diane_get_bug_spray:
    scene expression "backgrounds/location_mall_consumr_closeup.jpg"
    show diane b_casual:
        flip
        xoffset -100
    show player 13f
    with dissolve
    diane "Alright, the one we need will have a {b}green cap{/b} on it..."

    show vero:
        xoffset 100
    with dissolve
    vero "{b}Diane{/b}?!"

    show player 13 with dissolve
    vero "Long time no see!"

    diane "Hey, {b}Vee{/b}."

    vero "It's nice to see you finally out of your house!"

    vero "You here for more gardening supplies?"

    diane "Heh, yeah. Something like that..."

    vero "It's such a shame you're stuck tending that huge garden all by yourself."

    diane @ -m_talk "..."
    vero "You know, I'd be more than happy to-"

    show player 14
    player_name "Hello, I'm {b}[firstname]{/b}."

    show player 13
    vero "Oh, hi."

    vero "I didn't realize you two were together..."

    show diane f_laugh
    diane "Oh, we aren-"

    show diane f_normal
    vero "I'm {b}Veronica{/b}."

    show player 14
    player_name "Nice to meet you."

    show player 13
    vero "Wow, {b}Diane{/b}!"

    vero "You've been holding out on me."

    show player 11
    vero "Where did you find such a handsome young man?!"

    diane "aku tidak-"

    show player 14
    player_name "I've been helping her with her garden this summer."

    show player 13
    show vero f_sexy
    vero "You don't say..."

    vero "So when did you two start dating?"

    show player 23
    player_name "Dating?!" with hpunch
    show player 22
    show diane f_surprised
    diane "!!!"
    show diane f_smirk
    show player 29 with dissolve
    player_name "Oh, I didn't..."

    show player 3
    vero "Hmm?"

    diane "{b}[firstname]{/b} is just a friend of mine..."

    show player 13 with dissolve
    show vero f_laugh
    vero "Maafkan aku!"

    show vero f_normal
    vero "I didn't mean to jump to conclusions, I just thought..."

    show vero f_thinking
    vero @ -m_talk "..."
    show vero f_laugh
    vero "Hehe, sudahlah."

    diane @ -m_talk "..."
    show vero f_normal
    vero "{i}*Ahem*{/i} Well, can I help you find anything?"

    show diane f_normal
    diane "No, thanks. We know exactly what we need."

    vero "Alright, well, I'll leave you to it..."

    vero "... Call me sometime!"

    show vero f_sexy
    vero "I'd love to hear more about what you've been up to this summer."

    diane "Heh, yeah. Alright."

    diane "See ya, {b}Vee{/b}."

    hide vero with dissolve
    pause
    show player 10f at right with dissolve
    player_name "How do you know her?"

    show player 13f
    show diane f_thinking
    diane "Oh, she used to help me out a lot... You know, with tools and advice on gardening."

    show diane f_normal
    diane "She grew up on a farm, so she knows a lot more than I do."

    show player 14f
    player_name "She seems nice."

    show player 13f
    diane "Yeah, she's a really nice girl."

    diane "A bit ditzy... But certainly well-intentioned and polite."

    show diane f_laugh
    diane "I can't believe she thought we were dating..."

    show diane f_normal
    show player 14f
    player_name "Kenapa tidak?"

    show player 13f
    show diane f_teasing
    diane "Because you're so young and handsome, and I'm so-"

    show diane f_normal
    show player 14f
    player_name "Don't say old. You're not old..."

    show player 17f
    player_name "... And you're really hot, {b}Diane{/b}!"

    show player 13f
    show diane f_laugh_blush
    diane "Oh, stop it!"

    show diane f_normal
    show player 14f
    player_name "aku serius!"

    show player 13f
    show diane f_smirk
    diane "Hehe, well, thanks..."

    diane @ -m_talk "..."
    show diane f_shamed_smile
    diane "{i}*Ahem*{/i} Anyways, the {b}pesticide{/b} should be just over there on the shelf."

    show diane a_money with dissolve
    diane "Here's the money..."

    diane "{b}Look for the one with the green cap{/b}."

    hide player
    hide diane
    with dissolve
    return

label consumr_diane_buy_bug_spray_brought:
    scene expression "backgrounds/location_mall_consumr_closeup.jpg"
    show player 17 with dissolve
    player_name "Alright, now let's {b}get this back to Diane's house and eradicate those bugs{/b}!"

    label consumr_diane_buy_bug_spray_brought.tail:
    hide player with dissolve
    $ M_diane.trigger(T_diane_find_correct_bug_spray)
    $ game.main()

label consumr_diane_buy_bug_spray_owned:
    scene expression "backgrounds/location_mall_consumr_closeup.jpg"
    show player 17 with dissolve
    player_name "Oh, I already had this one!"

    player_name "Better {b}get this back to Diane's house and eradicate those bugs{/b}!"

    jump consumr_diane_buy_bug_spray_brought.tail
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
