label veronica_dialogue_pre_d05:
    show player 13 at left
    show vero
    with dissolve
    vero "Welcome to Consum-R, where all your needs are just an aisle away."
    vero "How can I help you today?"
    return

label veronica_dialogue_pre_d11:
    show player 5 at left
    show vero
    vero "Welcome to {b}Consum-R{/b}, where all your needs are just-"
    vero "{b}[firstname]{/b}?"
    show player 12
    player_name "Hey {b}Veronica{/b}."
    show player 5
    vero "What brings you in today?"
    return

label veronica_dialogue_pre_d20:
    show player 5 at left
    show vero
    with dissolve
    vero "Welcome to {b}Consum-R{/b}, where all your needs are just-"
    vero "Oh."
    vero f_sexy "Hey there, handsome!"
    show player 10
    player_name "Hey {b}Veronica{/b}."
    show player 5
    vero "What brings you in today?"
    return

label veronica_dialogue_vegatable_stock:
    show player 2
    show vero f_normal
    player_name "I'm {b}looking for vegetable stock{/b}. Do you guys have any?"
    show player 1
    vero "I'm afraid we're all sold out at the moment."
    show player 10
    player_name "Oh man..."
    show player 11
    vero "Would chicken stock work? We have plenty of that."
    show player 10
    player_name "I don't know..."
    player_name "Is there a delivery coming soon or something?"
    show player 11
    vero "We get deliveries daily but I have no idea when that particular item will be restocked."
    show player 10
    player_name "Crap..."
    player_name "Alright, thank you."
    hide vero with dissolve
    show player 10 with dissolve
    player_name "Hmm, I guess chicken stock will have to do."
    show player 2
    player_name "I should {b}buy some and take it to Miss Okita{/b}."
    return

label veronica_dialogue_bug_spray:
    show player 4
    player_name "Uh..."
    show player 12
    player_name "I'm looking for pesticide?"
    show vero f_laugh
    show player 1
    vero "Ah, yes! We have a variety of pest repellent products!"
    show vero f_normal
    show player 2
    player_name "Hmm... How about for insects?"
    show vero f_thinking
    show player 1
    vero "Well... There are many types of pesticides for insects..."
    show vero f_normal
    show player 11
    vero "Do you know what type of bug you're dealing with?"
    show player 10
    player_name "I'm not quite sure what kind it is..."
    show vero f_thinking
    show player 13
    vero "Well, what does it look like?"
    show vero f_normal
    return

label veronica_dialogue_bug_spray_large_wings:
    show player 35
    player_name "It had a set of large wings..."
    show vero f_thinking
    show player 11
    vero "Hmm... Could be {b}grasshoppers{/b}..."
    show vero f_laugh
    show player 1
    vero "Get the spray can with a {b}red cap{/b}. It's called the {b}Bug Exterminator{/b}."
    show vero f_normal
    vero "It should do the trick!"
    show player 17
    player_name "Alright, thanks!"
    return

label veronica_dialogue_bug_spray_pincers:
    show player 35
    player_name "It had large pincers..."
    show vero f_thinking
    show player 11
    vero "Hmm... Could be {b}earwigs{/b}... Nasty buggers!"
    show vero f_laugh
    show player 1
    vero "Get the spray can with a {b}green cap{/b}. It's called the {b}Bug Annihilator{/b}."
    show vero f_normal
    vero "It should do the trick!"
    show player 17
    player_name "Alright, thanks!"
    return

label veronica_dialogue_bug_spray_white_spots:
    show player 35
    player_name "It had white spots on its shell..."
    show vero f_thinking
    show player 11
    vero "Hmm... Could be {b}beetles{/b}..."
    show vero f_laugh
    show player 1
    vero "Get the spray can with a {b}blue cap{/b}. It's called the {b}Bug Eradicator{/b}."
    show vero f_normal
    vero "It should do the trick!"
    show player 17
    player_name "Alright, thanks!"
    return

label veronica_dialogue_leave:
    show player 10 at left
    show vero f_normal
    player_name "I'm just looking around, thanks."
    show player 5
    vero "No problem."
    vero "Lemme know if you need help with anything."
    show player 10
    player_name "Will do."
    hide player
    hide vero
    with dissolve
    return

label veronica_dialogue_what_do_you_sell:
    show player 10 at left
    show vero f_normal
    player_name "What do you sell here?"
    show player 5
    vero @ f_laugh "It would probably be faster to tell you things we don't sell."
    vero "We carry pretty much everything a person needs to get by."
    show player 10
    player_name "So I can buy tools here?"
    show player 5
    vero "Of course."
    show player 10
    player_name "How about groceries?"
    show player 5
    vero "Uh huh."
    show player 401
    player_name "Computer parts?!"
    show player 403
    vero "We got 'em."
    show player 402
    player_name "Clothes?"
    show player 403
    show vero
    vero @ f_laugh "In all sizes."
    show player 402
    player_name "Kitchen appliances?!"
    show player 403
    vero "Aisle 12."
    show player 4 with dissolve
    player_name "Hmm."
    show player 401 with dissolve
    player_name "How about bicycles?"
    show player 403
    show vero f_thinking
    vero "Mountain bikes or BMX?"
    show vero f_sexy
    vero "'Cause we have both."
    show player 402
    player_name "Wow, you guys really do carry everything."
    show player 403
    vero "I told you."
    show vero f_normal
    return

label veronica_dialogue_you_look_nice:
    show player 14 at left
    show vero f_normal
    player_name "You look nice today."
    show player 13
    show vero f_eyeroll
    vero "Oh, stop it."
    show vero f_sexy_down
    vero "Nobody could look nice wearing this ridiculous uniform..."
    show vero f_sexy
    show player 10
    player_name "You do."
    show player 5
    vero "Aww, that's really sweet of you to say."
    vero "Even if I don't believe you."
    vero "Thanks, {b}[firstname]{/b}."
    show player 10
    player_name "You're welcome."
    show player 5
    return

label veronica_dialogue_spoken_with_diane_lately:
    show player 10 at left
    show vero f_normal
    player_name "Have you spoken with {b}Diane{/b} lately?"
    show player 5
    vero "Yeah, over the phone."
    vero "I'm dying to learn more about this side business she has going!"
    vero "You know anything about it?"
    show player 10
    player_name "N-nope."
    player_name "Not a thing."
    show player 5
    show vero f_sexy
    vero "Oh, c'mon!"
    vero "You can tell me."
    show player 14
    player_name "Hehe, I really don't know anything about it!"
    show player 10
    player_name "Sorry."
    show player 5
    show vero f_eyeroll
    vero "{i}*Sigh*{/i} It's killing me not knowing!"
    show vero f_normal
    show player 10
    player_name "I'm sure {b}Diane{/b} will tell you all about it soon enough."
    show player 5
    vero "I hope so."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
