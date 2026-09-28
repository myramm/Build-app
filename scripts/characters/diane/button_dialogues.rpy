label dianes_dialogue_daisy:
    show player 14 at left
    show diane f_normal b_naked a_idle
    player_name "How's {b}Daisy{/b} getting on?"
    show player 13
    diane "Oh, she's settling in great!"
    diane "Kinda funny that a dairy farmer would find a magical cow girl, isn't it?"
    diane "It's a good thing I built that barn..."
    pause
    diane @ f_laugh "She's a sweet girl."
    show player 14
    player_name "Yeah, she is."
    show player 13
    diane "I'm so glad we found her."
    return

label dianes_dialogue_cow_girl:
    scene expression player.location.background_blur with None
    show player 10 at left
    show diane b_naked
    with dissolve
    player_name "Any progress with our new friend?"
    show player 5
    show diane f_shamed_smile
    diane "{i}*Sigh*{/i} That poor thing."
    diane "She's still half convinced her master is gonna pop up and punish her for letting us see her."
    diane "Whatever that awful man did to her, she's not ready to talk about it."
    show diane f_shamed
    show player 10
    player_name "Has she at least given you her name?"
    show player 5
    show diane f_shamed_smile
    diane "No, not yet."
    diane "She's coming around though."
    diane "I imagine it won't be long 'til she's ready to speak with you."
    show diane f_shamed
    show player 10
    player_name "Okay."
    show player 5
    return

label dianes_dialogue_milk_sample:
    scene expression player.location.background_blur with None
    show diane b_naked
    show player 14 at left
    player_name "Could I have a small sample of your milk?"
    show player 13
    show diane f_smirk
    diane "Hehe, feeling thirsty, are we?"
    show player 29 with dissolve
    player_name "N-no, I really do just need a sample."
    show player 13 with dissolve
    show diane f_surprised
    pause
    show diane f_shamed
    diane "Oh."
    diane "Uhh, sure. Just give me a second."
    if M_diane.outfit.get == "shirtless":
        show diane b_topless
    show diane a_squeeze3 f_down_front
    with dissolve
    pause
    show diane f_normal a_bottle1 with dissolve
    diane "Will this work?"
    show diane b_naked a_idle with dissolve
    show player 713
    with dissolve
    player_name "Yeah, this is perfect!"
    player_name "Thanks, {b}Diane{/b}!"
    hide player with dissolve
    diane "No pro-"
    show diane f_surprised
    pause
    show diane f_shamed_front
    diane "( What is he up to? )"
    hide diane with dissolve
    call popup ('give', 'milk_sample')
    return

label dianes_dialogue_hows_baby_doing_boy:
    show player 14 at left
    show diane b_casual a_baby
    player_name "How's he doing?"
    show player 13
    show diane f_normal
    diane "Oh, he's just wonderful!"
    diane "I never want to put him down."
    show player 14
    player_name "Well, you'll have to put him down eventually..."
    show player 13
    show diane f_laugh
    diane "Nah uh!"
    show diane f_cheese
    show player 17
    player_name "Hehehe."
    show player 13
    return

label dianes_dialogue_hows_baby_doing_twins:
    show player 14 at left
    show diane b_casual a_baby
    player_name "How are they doing?"
    show player 13
    show diane f_normal
    diane "Oh, they're just wonderful!"
    diane "I never want to put them down."
    show player 14
    player_name "Well, you'll have to put them down eventually..."
    show player 13
    show diane f_laugh
    diane "Nah uh!"
    show diane f_cheese
    show player 17
    player_name "Hehehe."
    show player 13
    return

label dianes_dialogue_hows_baby_doing_girl:
    show player 14 at left
    show diane b_casual a_baby
    player_name "How's she doing?"
    show player 13
    show diane f_normal
    diane "Oh, she's just wonderful!"
    diane "I never want to put her down."
    show player 14
    player_name "Well, you'll have to put her down eventually..."
    show player 13
    show diane f_laugh
    diane "Nah uh!"
    show diane f_cheese
    show player 17
    player_name "Hehehe."
    show player 13
    return

label dianes_dialogue_get_anything_baby:
    show player 14 at left
    show diane b_casual a_baby
    player_name "Can I get you anything?"
    show player 13
    show diane f_normal
    diane "No, I'm okay."
    diane "Thanks, stud."
    show player 14
    player_name "You're welcome."
    show player 13
    show diane f_shamed_smile
    diane "No really, thank you, {b}[firstname]{/b}."
    diane "For everything."
    show diane f_shamed
    show player 14
    player_name "It's my pleasure, {b}Diane{/b}."
    show player 13
    return

label dianes_dialogue_baby_leave:
    show player 14 at left
    show diane b_casual a_baby
    player_name "I'll leave you guys be."
    show player 13
    show diane f_normal
    diane "Alright."
    show diane f_laugh
    diane "Say, \"Bye-bye Daddy.\""
    show diane f_cheese
    show player 17
    player_name "Hehe."
    show player 36 with dissolve
    if M_diane.pregnancy.baby_gender == "twins":
        player_name "Goodbye, little ones."
    else:
        player_name "Goodbye, little one."
    hide player
    hide diane
    with dissolve
    return

label dianes_dialogue_gave_birth_intro:
    show player 14 at left
    show diane b_casual a_baby
    with dissolve
    player_name "Hey, {b}Diane{/b}."
    show player 13
    if M_diane.pregnancy.baby_gender == "boy":
        diane "Shh, he's sleeping."
    elif M_diane.pregnancy.baby_gender == "twins":
        diane "Shh, they're sleeping."
    else:
        diane "Shh, she's sleeping."
    show player 14
    player_name "Oh, sorry."
    show player 13
    return

label dianes_dialogue_intro_kitchen:
    scene expression player.location.background_blur
    show player 14 at left
    show diane b_nightgown a_water
    player_name "Hey, {b}Diane{/b}."
    show player 13
    diane "Hey, {b}[firstname]{/b}."
    show player 10
    player_name "You alright?"
    show player 5
    diane "Hmm?"
    diane "Yeah, I'm okay."
    show player 13
    diane "I was just thirsty, so I came in here for a glass of water."
    pause
    diane "Now I'm just thinking..."
    show player 14
    player_name "Thinking about what?"
    show player 13
    diane @ f_laugh "Hehe, I dunno, work stuff I guess..."
    show player 14
    player_name "O-okay."
    show player 13
    return

label dianes_dialogue_hows_business:
    show player 14 at left
    show diane a_idle
    player_name "Have you had an easier time keeping up with all your orders now?"
    show player 13
    show diane f_laugh
    diane "Oh my, yes!"
    show diane f_normal
    diane "I think my milk supply has more than doubled since the birth!"
    diane "Production is going very smoothly now."
    if M_diane.pregnancy.number_of_babies == 1:
        diane "I just have to make sure I leave some milk for the little one."
        show diane f_laugh
        diane "That child of ours is so hungry!"
    else:
        diane "I just have to make sure I leave some milk for the little ones."
        show diane f_laugh
        diane "Those children of ours are so hungry!"
    show diane f_normal
    show player 17
    player_name "Haha."
    show player 14
    player_name "Well, that milk of yours is so delicious... I can't blame them!"
    show player 13
    return

label dianes_dialogue_goodnight_1:
    show player 14 at left
    show diane f_normal a_idle
    player_name "I was just heading to bed."
    player_name "You need anything?"
    show player 13
    diane @ -m_talk "Hmm?"
    diane "Oh, I'm fine stud."
    diane "Thanks for asking."
    show player 14
    player_name "Alright then, goodnight."
    show player 13
    diane "Goodnight."
    hide player
    hide diane
    with dissolve
    return

label dianes_dialogue_goodnight_2:
    show player 14 at left
    show diane f_normal a_idle
    player_name "Yeah, everything's fine."
    player_name "Sorry to wake you."
    show player 13
    diane "That's okay."
    show player 14
    player_name "Goodnight."
    show player 13
    diane "Goodnight, stud."
    hide player
    hide diane
    with dissolve
    return

label dianes_dialogue_what_up_to:
    show player 14 at left
    show diane f_normal b_naked a_idle
    player_name "What are you up to?"
    show player 13
    diane "Oh, I'm just sitting here bored."
    diane "Late night TV sucks."
    show player 14
    player_name "Heh, that's too true!"
    show player 13
    show diane f_smirk
    diane "You wanna do something fun?"
    show player 10
    player_name "What did you have in mind?"
    show player 13
    diane "Mmm, I can think of a few things..."
    return

label dianes_dialogue_on_my_way_debbie:
    show player 14 at left
    show diane f_normal b_naked a_idle
    player_name "I was on my way to see {b}[deb_name]{/b}."
    show player 13
    diane "Ahh, okay."
    diane "She's in her room."
    show player 14
    player_name "I'll talk to you later, okay?"
    show player 13
    diane "Alright."
    hide player with dissolve
    pause
    show diane f_smirk
    diane "You two have fun."
    show diane f_laugh
    diane "Hehehe."
    hide diane with dissolve
    return

label dianes_dialogue_leave_d19_d20_day:
    show player 14 at left
    show diane f_normal b_naked a_idle
    player_name "I should check on the garden."
    show player 13
    diane "Okay."
    diane "Just don't forget that I need your help pumping too!"
    show player 14
    player_name "I won't."
    hide player
    hide diane
    with dissolve
    return

label dianes_dialogue_hows_the_business:
    show player 13 at left
    show diane f_normal b_naked a_idle
    diane "Business is booming!"
    diane "I can barely keep up with all the orders!"
    show player 14
    player_name "That's good, right?"
    show player 13
    diane "It's very good."
    show diane f_laugh
    diane "I'll have to start hiring more boobs soon."
    show diane f_cheese
    return

label dianes_dialogue_call_veronica:
    show player 10 at left
    show diane f_normal b_naked a_idle
    player_name "Have you talked with {b}Veronica{/b} yet?"
    show player 13
    diane @ f_sad "No, not yet."
    diane "I will though."
    show player 14
    player_name "She'd really like to work for you."
    show player 13
    show diane f_laugh
    diane "Yeah, we'll see."
    show diane f_cheese
    return

label dianes_dialogue_what_are_you_up_to:
    show player 14 at left
    show diane f_normal b_nightgown a_idle
    player_name "What are you doing?"
    show player 13
    diane "Oh, just watching some TV and sipping some of {b}[deb_name]{/b}'s delicious wine."
    diane "It's so nice having roommates again."
    show player 14
    player_name "Is it?"
    show player 13
    diane "Of course!"
    diane "I was so lonely over there in that big house by myself."
    show player 14
    player_name "Yeah, I can imagine."
    show player 13
    diane "Now I feel like I'm part of a family again."
    show player 14
    player_name "You are part of our family {b}Diane{/b}."
    show player 13
    diane "Aww, thanks handsome."
    return

label dianes_dialogue_wheres_debname:
    show player 10 at left
    show diane f_normal b_nightgown a_idle
    player_name "Doesn't she usually sit out here with you?"
    show player 13
    diane "She went to bed early tonight..."
    diane "... Said she was tired."
    show player 14
    player_name "Oh, I see."
    show player 13
    diane "You can still go and see her if you'd like, I'm sure she wouldn't mind."
    show player 14
    player_name "Y-yeah, maybe..."
    show player 13
    return

label dianes_dialogue_love_that_nightgown:
    show player 14 at left
    show diane f_normal b_nightgown a_idle
    player_name "It looks amazing on you!"
    show player 13
    show diane f_laugh a_hip with dissolve
    diane "Hehe, thanks!"
    show diane f_reading_intrigued
    diane "I was worried it might be a little inappropriate but given what {b}[deb_name]{/b} and {b}[jen_name]{/b} prance around in..."
    show diane f_normal
    show player 14
    player_name "Heh, y-yeah."
    show player 426
    pause
    show diane f_smirk
    diane "Hehe, you still with me handsome?"
    player_name "Hmm?"
    show player 29 with dissolve
    player_name "Oh, s-sorry!"
    show player 3
    diane "Haha, it's alright."
    diane "You can look."
    show player 426 with dissolve
    pause
    pause
    show player 403
    show diane a_idle with dissolve
    return

label dianes_dialogue_goodnight:
    show player 14 at left
    show diane f_normal b_nightgown a_idle
    player_name "I should probably get to bed."
    show player 13
    diane "Yeah, me too."
    show player 14
    player_name "Goodnight, {b}Diane{/b}."
    show player 13
    diane "Goodnight, handsome."
    hide player
    hide diane
    with dissolve
    return

label dianes_dialogue_hows_the_couch:
    show player 14 at left
    show diane f_normal b_shirtless a_idle
    player_name "You sleeping alright?"
    show player 13
    diane "Oh, it's fine."
    diane "A little lumpy but I'll manage."
    pause
    diane "You wanna hear something weird?"
    show player 14
    player_name "Sure."
    show player 13
    diane "{b}[jen_name]{/b} keeps coming down in the middle of the night and huffing when she finds me laying there."
    diane "Then when I ask her what she needs, she rolls her eyes and storms off muttering something about wasting money."
    diane "Any idea what that's about?"
    show player 29 with dissolve
    player_name "I uhh..."
    show player 3
    diane "What could she possibly want in the living room in the middle of the night?"
    pause
    show player 10 with dissolve
    player_name "No idea."
    show player 5
    diane @ f_thinking "{i}*Sigh*{/i} Probably just her way of trying to get under my skin."
    show player 14
    player_name "Heh yeah, probably..."
    show player 13
    show diane f_annoyed
    diane "She's such a bitch."
    show diane f_cheese
    return

label dianes_dialogue_feeling_better:
    show player 14 at left
    show diane f_normal
    player_name "How are you feeling?"
    show player 13
    show diane f_laugh
    diane "Oh, much better now that you're helping me pump!"
    show diane f_smirk
    diane "Thank you for that, {b}[firstname]{/b}."
    show player 14
    player_name "You're welcome."
    player_name "Just make sure you get lots of rest, okay?"
    show player 13
    show diane f_laugh
    diane "Haha, okay, Dad!"
    show diane f_cheese
    show player 17
    player_name "Haha!"
    show player 13
    show diane f_smirk
    return

label dianes_dialogue_like_working_for_you:
    show player 14 at left
    show diane f_normal
    player_name "You know, I really enjoy this work {b}Diane{/b}."
    show player 13
    show diane f_laugh
    diane "Hah, I bet you do!"
    if M_diane.outfit.get == "dressed":
        show diane f_smirk a_finger with dissolve
    else:
        show diane f_smirk
    diane "What young man wouldn't enjoy handling breasts all day?"
    if M_diane.outfit.get == "dressed":
        show diane a_shovel with dissolve
    show player 14
    player_name "That's not what I..."
    player_name "Heh, I mean... That part is pretty awesome."
    show player 401
    player_name "You have great boobs."
    show player 403
    diane "Uh huh."
    show player 14
    player_name "... But it's not just that!"
    player_name "It feels nice taking care of you."
    player_name "I like it."
    show player 13
    if M_diane.outfit.get == "dressed":
        show diane a_blush with dissolve
    diane "Aww."
    diane "I like it too, {b}[firstname]{/b}."
    if M_diane.outfit.get == "dressed":
        show diane a_shovel with dissolve
    pause
    diane "Just don't tell {b}[deb_name]{/b}!"
    show player 14
    player_name "Don't worry, I won't."
    show player 403
    return

label dianes_dialogue_leave_d12b:
    show player 14 at left
    show diane f_normal b_naked a_idle
    player_name "I'd better get back to it."
    show player 13
    diane "Alright."
    diane "If you need anything, you know where to find me."
    hide player
    hide diane
    with dissolve
    return

label dianes_dialogue_have_you_spoken_with_debname:
    show player 14 at left
    show diane f_tired b_naked a_shovel_sides
    player_name "You talked with {b}[deb_name]{/b} lately?"
    show player 13
    diane "Oh, all the time!"
    diane "We're back to daily phone calls again."
    show player 14
    player_name "That's nice."
    show player 13
    diane "It's been wonderful!"
    diane "I missed her so much!"
    show player 14
    player_name "Well, she missed you too."
    player_name "We all did, really."
    show player 13
    diane "Aww."
    hide player
    if M_diane.outfit.get == "dressed":
        show anon b_empty f_grin
        show diane b_kiss
    else:
        show diane b_kiss_shirtless
    with dissolve
    pause
    hide anon
    show player 13 at left
    show diane b_naked a_shovel_sides
    with dissolve
    return

label dianes_dialogue_about_veronica:
    show player 12 at left
    show diane f_tired b_naked a_shovel_sides
    player_name "So how did you meet that girl {b}Veronica{/b}?"
    show player 13
    diane "You mean {b}Vee{/b}?"
    diane "Oh, I love that girl!"
    diane "We met in the gardening section of Consum-R, a couple years ago."
    diane "She had just moved up here from the country and didn't know anybody."
    show player 14
    player_name "I bet that was rough."
    show player 13
    diane "Oh, it certainly was."
    diane "She was a mess!"
    diane "I offered to show the poor dear around town in exchange for some gardening advice, and we just sorta hit it off."
    show player 14
    player_name "That was nice of you."
    show player 13
    diane "Yeah, I guess."
    diane "Truthfully, I was in need of a friend too."
    diane "What with {b}[deb_name]{/b} being so wrapped up with your dad and all."
    show player 5
    player_name "..."
    pause
    diane "Oh, I'm sorry handsome!"
    diane "I didn't mean that to sound like a bad thing."
    show player 10
    player_name "Yeah, I know you didn't."
    show player 5
    diane "Your father was a good man, I always liked him."
    show player 10
    player_name "Thanks."
    show player 5
    return

label dianes_dialogue_hows_the_garden_2:
    show player 14 at left
    show diane f_tired b_naked a_shovel_sides
    player_name "So I'm really doing okay with the garden?"
    show player 13
    diane "You're doing better than okay!"
    diane "I've never seen my garden looking this good!"
    diane "I might have the finest cucumbers in all the land!"
    show player 14
    player_name "Hah, I dunno about that..."
    player_name "I'm glad it's turning out so well though."
    show player 13
    return

label dianes_dialogue_take_it_easy:
    show player 14 at left
    show diane f_tired b_naked a_shovel_sides
    player_name "Alright, I guess I should get back to work."
    show player 10
    player_name "Take it easy, okay?"
    player_name "I worry about you working yourself too hard."
    show player 5
    diane "Psh, you sound just like {b}[deb_name]{/b}..."
    diane "I'll be fine."
    show player 10
    player_name "Okay..."
    hide player
    hide diane
    with dissolve
    return

label dianes_dialogue_about_debname:
    show player 14 at left
    show diane f_normal
    player_name "I'm glad you're spending time with {b}[deb_name]{/b} again."
    player_name "I know she's been missing your company."
    show player 13
    show diane a_blush with dissolve
    diane "Aww, and I missed hers!"
    show diane a_shovel with dissolve
    diane "We were inseparable in our younger years, you know?"
    show player 14
    player_name "Yeah, I've heard the stories."
    show player 13
    show diane f_laugh
    diane "Hah!"
    show diane f_smirk a_finger with dissolve
    diane "Well, I hope she hasn't told you all the stories!"
    show diane a_shovel with dissolve
    show player 10
    player_name "Huh?"
    show player 13
    show diane f_laugh
    diane "Hehe, never mind."
    show diane f_normal
    show player 14
    player_name "I still can't get over how much you two look alike..."
    show player 13
    diane "Yeah, we used to get that all the time."
    diane "They called us twins in college."
    show player 14
    player_name "I can see that."
    show player 13
    diane "I was the wild one, and she was the pretty one!"
    show player 29 with dissolve
    player_name "I think you're both pretty, {b}Diane{/b}."
    show player 3
    show diane f_shamed_smile a_blush with dissolve
    diane "Aww, thanks handsome."
    show diane f_normal a_shovel with dissolve
    show player 13 with dissolve
    return

label dianes_dialogue_hows_the_garden:
    show player 14 at left
    show diane f_normal
    player_name "So how's your garden doing?"
    show player 13
    show diane f_sad
    diane "It's definitely seen better days..."
    diane "I've been so preoccupied with side work lately, I'm afraid my garden just doesn't get the attention it deserves."
    show diane f_normal
    diane "That's why I was so excited when {b}[deb_name]{/b} said you might be able to help me this summer."
    show player 14
    player_name "I'm happy to help, {b}Diane{/b}!"
    show player 13
    return

label dianes_dialogue_what_have_you_been_up_to:
    show player 14 at left
    show diane f_normal
    player_name "So what have you been doing with yourself these past few years?"
    show player 13
    diane "Oh, not much really..."
    show player 14
    player_name "Not much?!"
    player_name "I thought you were out there partying like crazy and getting chased by rich men?"
    show player 13
    show diane f_laugh a_blush with dissolve
    diane "Haha, goodness no!"
    diane "Whatever gave you that idea?"
    show diane f_normal a_shovel with dissolve
    show player 14
    player_name "Well, {b}[deb_name]{/b} always says you're the wild one."
    show player 13
    show diane f_smirk a_finger with dissolve
    diane "Well, perhaps in my younger days..."
    show diane f_normal a_shovel with dissolve
    diane "Honestly, since the divorce, I spend most of my time right here in this garden."
    show player 14
    player_name "You mean, you don't go out at all anymore?"
    show player 13
    diane "Occasionally I'll go out for a drink with my friend {b}Veronica{/b}."
    diane "Nothing too exciting."
    show player 14
    player_name "Don't you miss it?"
    show player 13
    diane "Hmm, sometimes."
    diane "I'm too old for that kind of life now."
    show diane f_smirk
    diane "Besides, there's no good men left in this town."
    show player 12
    player_name "Really?!"
    show player 13
    diane @ f_laugh "Heh, trust me."
    diane "At my age, the only thing left is the dregs."
    show player 10
    player_name "Bummer."
    show player 5
    return

label dianes_dialogue_intro_d1_d6:
    show player 13 at left
    show diane
    with dissolve
    diane "Hey there, {b}[firstname]{/b}!"
    diane "I'm so glad you decided to come and help me."
    show player 14
    player_name "Yeah, it's no problem {b}Diane{/b}."
    player_name "Thanks for paying me!"
    show player 13
    diane @ f_laugh "Hehe, my pleasure handsome."
    return

label dianes_dialogue_intro_d7_d12:
    show player 5 at left
    show diane f_tired b_naked a_shovel_sides
    with dissolve
    diane "Hey, {b}[firstname]{/b}."
    diane "My garden is looking really-"
    diane "{i}*Yawn*{/i}"
    diane "... Really nice."
    show player 10
    player_name "You alright, {b}Diane{/b}?"
    show player 5
    diane "Yeah, I'm okay."
    diane "Just tired."
    return

label dianes_dialogue_intro_d12b_d15:
    show player 13 at left
    show diane b_naked
    diane "Hey there, handsome!"
    show player 14
    player_name "Hey, {b}Diane{/b}."
    show player 13
    diane "You need something?"
    return

label dianes_dialogue_intro_d16_d18_barn:
    show player 13 at left
    show diane b_shirtless
    with dissolve
    diane "Hey there, stud!"
    show player 14
    player_name "Hey, {b}Diane{/b}."
    show player 13
    diane "You ready to work?"
    return

label dianes_dialogue_intro_d16_d18_couch:
    show player 13 at left
    show diane b_nightgown
    with dissolve
    diane "Hey there, stud!"
    show player 14
    player_name "Hey, {b}Diane{/b}."
    show player 13
    diane "You heading to bed?"
    show player 14
    player_name "Yeah, in a couple minutes."
    show player 13
    return

label dianes_dialogue_intro_d19_d20_barn:
    show player 13 at left
    show diane b_naked
    with dissolve
    diane "Hey there, stud!"
    show player 14
    player_name "Hey, {b}Diane{/b}."
    show player 13
    diane "You ready to work?"
    return

label dianes_dialogue_intro_d19_couch:
    show player 13 at left
    show diane f_smirk b_nightgown
    with dissolve
    diane "Hey there, stud!"
    show player 14
    player_name "Hey, {b}Diane{/b}."
    show player 13
    show diane f_normal
    diane "You looking for me or {b}[deb_name]{/b}?"
    return

label dianes_dialogue_intro_d20_couch:
    show player 13 at left
    show diane b_nightgown
    with dissolve
    diane "Hmm, {b}[firstname]{/b}?"
    show player 14
    player_name "Hey, {b}Diane{/b}."
    show player 13
    diane "Everything alright?"
    return

label dianes_dialogue_ready_to_pump:
    show player 14 at left
    show diane f_normal
    with dissolve
    player_name "You ready to pump?"
    show player 13
    diane "Absolutely!"
    diane "Just give me one second to set things up."
    hide diane with dissolve
    show player 14
    player_name "Cool."
    return

label dianes_dialogue_hows_the_baby_pregnancy_1:
    show player 13 at left
    show diane b_naked a_idle f_normal
    with dissolve
    diane "Oh, there's not much to report yet."
    diane "Unless you're interested in hearing about my morning sickness?"
    show player 10
    player_name "Well, if you want to talk about it, we can?"
    show player 13
    diane @ f_laugh "Haha, oh goodness no!"
    diane "I appreciate you asking though."
    diane "Thanks, {b}[firstname]{/b}."
    return

label dianes_dialogue_hows_the_baby_pregnancy_2:
    show player 13 at left
    show diane b_naked a_idle f_normal
    with dissolve
    diane "Oh, there's not much to report yet."
    diane "Unless you're interested in hearing about my morning sickness?"
    show player 10
    player_name "Well, if you want to talk about it, we can?"
    show player 13
    diane @ f_laugh "Haha, oh goodness no!"
    diane "I appreciate you asking though."
    diane "Thanks, {b}[firstname]{/b}."
    return

label dianes_dialogue_hows_the_baby_pregnancy_3:
    show player 13 at left
    show diane f_normal b_naked a_idle
    with dissolve
    diane "Heh, my tits are so swollen!"
    diane "Do they look bigger to you?"
    show player 26
    player_name "I dunno, they were pretty big to begin with..."
    show player 18
    diane "Oh, c'mon!"
    show player 13
    diane "They're definitely bigger!"
    pause
    show player 14
    player_name "I just love your little baby bump!"
    show player 13
    show diane f_laugh a_touch_belly with dissolve
    diane "Hehe, I know!"
    show diane f_normal
    diane "Isn't it adorable?"
    pause
    show diane f_normal a_idle with dissolve
    diane "Thanks for checking in with me, {b}[firstname]{/b}."
    show player 14
    player_name "Of course."
    player_name "I can't wait to meet our baby, {b}Diane{/b}!"
    show player 13
    diane "Aww, you're the sweetest man in the world!"
    return

label dianes_dialogue_hows_the_baby_pregnancy_4:
    show player 13 at left
    show diane f_tired b_naked a_idle
    with dissolve
    diane "Ugh, I'm exhausted..."
    show player 5
    diane "My feet are killing me, I look like a whale, and my tits never stop leaking!"
    show player 10
    player_name "... Oh."
    show player 5
    show diane f_laugh
    diane "Hehe, but it's okay."
    show diane f_normal a_touch_belly with dissolve
    diane "I'm gonna be a mommy very soon!"
    show player 14
    player_name "That's right, you are!"
    show player 13
    diane "I'm so excited, {b}[firstname]{/b}!"
    diane "I can't wait to hold our child in my arms!"
    show player 14
    player_name "Yeah, me too."
    show player 13
    show diane a_idle
    with dissolve
    return

label dianes_dialogue_breeding_session:
    show player 13 at left
    show diane b_naked a_idle f_smirk
    with dissolve
    diane "You ready to get started?"
    show player 14
    player_name "S-sure."
    show player 13
    diane "Thank goodness!"
    diane "I'm getting so wet just thinking about that big dick of yours putting a baby inside me..."
    show player 10
    player_name "You are?!"
    hide player
    show diane b_pull_mc_naked
    with dissolve
    diane "Mmm, I need it so bad, {b}[firstname]{/b}!"
    hide diane
    with dissolve
    scene expression "backgrounds/location_barn_sex_back_day.jpg"
    show diane_sex_breed pre_talk
    show diane_sex_breed_mc
    with dissolve
    diane "That's it, stud."
    diane "Give it to me."
    hide diane_sex_breed_mc
    show diane_sex_breed insert_and_pullout
    with dissolve
    pause
    show diane_sex_breed creampie_pullout with dissolve
    pause 1
    show diane_sex_breed creampie
    diane "Ahh!!"
    return

label dianes_dialogue_cow_suit:
    show player 14 at left
    show diane f_normal b_naked a_idle
    player_name "I wanted to talk to you about your cow outfit..."
    show player 13
    diane "Oh?"
    menu:
        "Put it back on." if M_diane.outfit.get == "naked":
            show player 14 at left
            player_name "I want you to wear it while I breed you."
            player_name "It's so sexy!"
            show player 13
            diane @ f_laugh "Oh, I'm so happy you think so!"
            diane "I love it too!"
            show diane f_smirk
            diane "It just feels right, you know?"
            diane "Wearing it in here."
            show player 14
            player_name "Yeah, totally."
            hide diane
            with dissolve
            $ M_diane.outfit.is_naked = 0
            $ M_diane.outfit.set_default_outfit_schedule([["cow","cow","nightgown","nightgown"]])

        "Could you remove it?" if not M_diane.outfit.get == "naked":
            show player 14 at left
            player_name "I'd rather have you completely naked."
            show player 13
            show diane f_smirk
            diane "You would?!"
            diane "Mmm, you naughty boy..."
            pause
            diane "I can take it off, if that's what you really want."
            diane "Whatever helps you put a baby in my belly."
            hide diane
            with dissolve
            $ M_diane.outfit.set_default_outfit_schedule([["naked","naked","nightgown","nightgown"]])
    return

label dianes_dialogue_dump_pump:
    scene garden
    show player 10 at left
    show diane b_shirtless
    with dissolve
    player_name "What did I need to do again?"
    show player 13
    diane "Hmm?"
    diane "Oh, just {b}head into the shed and dump what's in the pump into a storage jug{/b}."
    show player 14
    player_name "Right!"
    player_name "I'm on it!"
    hide player
    hide diane with dissolve
    return

label dianes_dialogue_daylight_drinking:
    scene expression "backgrounds/location_diane_garden_close_day_blur.jpg"
    show player 429 zorder 0 at Position (xpos=175,ypos=648)
    show diane_chair up
    show diane b_laying_back_shirtless f_smirk_up
    with dissolve
    player_name "How are you doing over here?"
    show player 426
    diane @ f_laugh "Mmm, fantastic!"
    show player 429
    player_name "Can I get you anything?"
    show player 426
    diane "I wouldn't say no to a drink."
    show player 429
    player_name "Your wish is my command!"
    player_name "What kind of drink do you want?"
    show player 426
    $ randomdrink = M_diane.get("random drink")
    diane @ f_thinking "How about a {b}[randomdrink]{/b}?"
    show player 427
    player_name "{b}[randomdrink]{/b}?!"
    player_name "I've never made anything like that before..."
    show player 426
    show diane f_laugh
    diane "Hehe, no worries. I'll do it."
    show diane f_smirk_up
    show player 429
    player_name "No! I can figure it out."
    player_name "You just relax on your day off!"
    show player 426
    diane "You're sure?"
    show player 429
    player_name "Positive!"
    show player 426
    diane "Okay. Well, {b}the recipe is inside on a notepad next to the mixer{/b}."
    show player 429
    player_name "Got it!"
    player_name "One {b}[randomdrink]{/b}, coming right up!"
    hide player
    hide diane
    hide diane_chair
    with dissolve
    return

label dianes_dialogue_make_drink:
    $ randomdrink = M_diane.get("random drink")
    scene expression "backgrounds/location_diane_garden_close_day_blur.jpg"
    show player 427 zorder 0 at Position (xpos=175,ypos=648)
    show diane_chair up
    show diane b_laying_back_shirtless f_smirk_up
    with dissolve
    player_name "What drink did you want again?"
    show player 426
    diane @ f_thinking "Hmm, a {b}[randomdrink]{/b} would be nice."
    diane "{b}The recipe is inside on a notepad next to the mixer{/b}."
    show player 429
    player_name "One {b}[randomdrink]{/b}, coming right up!"
    hide player
    hide diane
    hide diane_chair
    with dissolve
    return

label dianes_dialogue_diane_fetch_pump:
    show player 10 at left
    show diane f_normal
    with dissolve
    player_name "What did you need me to do again?"
    show player 5
    diane "Just {b}fetch me the tool I left on the kitchen counter{/b}."
    show player 14
    player_name "Oh, right!"
    player_name "I'll be right back!"
    hide player
    hide diane
    with dissolve
    return

label dianes_dialogue_diane_got_pump:
    scene garden
    show player 239_240 at left
    show diane
    with dissolve
    pause
    show player 103 at Position (xoffset=38) with dissolve
    player_name "Is this what you needed?"
    show player 13
    show diane a_pump
    with dissolve
    diane "Yup!"
    show player 10
    player_name "What is this thing anyways?"
    show player 13
    diane "You've never seen a breast pump before?"
    show player 10
    player_name "... No?"
    show player 12
    player_name "It's a pump?"
    show player 5
    diane "Mmmhmm."
    show player 10
    player_name "How does it work?"
    show player 5
    diane @ f_explain "Hehe, well, you put this end over the nipple and then press the lever here, and it sucks the milk out of the teet and into this container."
    show player 14
    player_name "Whoa!"
    show player 10
    player_name "... And it doesn't hurt the cow?"
    show player 13
    show diane f_laugh a_blush with dissolve
    diane "Hahaha!"
    diane "No, handsome."
    show diane f_normal a_shovel with dissolve
    diane "It feels really good!"
    show diane f_shamed_smile
    diane "You know, for the uhh... Cow."
    show diane f_shamed
    show player 14
    player_name "Can I try milking the cow sometime?"
    show player 13
    show diane f_laugh
    diane "Haha, I don't think that's a good idea, handsome."
    show diane f_smirk a_finger with dissolve
    diane "For now, you just work on the garden, okay?"
    show diane a_shovel with dissolve
    show player 14
    player_name "... Okay."
    show player 13
    diane "If you need me, I'll be in here."
    diane "Just knock first, got it?"
    show player 14
    player_name "Yeah, I've got it."
    show player 13
    show diane f_laugh
    diane "Hehe, thanks stud."
    hide player
    hide diane
    with dissolve
    return


label dianes_dialogue_delivery_1_reminder:
    scene garden
    show player 10 at left
    show diane
    with dissolve
    player_name "Where am I supposed to deliver this milk again?"
    show player 5
    diane "You need to {b}take that order to Tony down at Tony's Pizza{/b}."
    show player 14
    player_name "Oh yeah, I know that place!"
    player_name "Alright, I'll be back in a flash."
    show player 13
    diane "Thanks, {b}[firstname]{/b}!"
    hide player
    hide diane
    with dissolve
    return

label dianes_dialogue_delivery_1_done:
    scene garden
    show diane
    show anon a_money
    with dissolve
    anon "I made your delivery for you."
    show anon a_idle
    show diane a_money
    with dissolve
    diane "Oh, thank you so much {b}[firstname]{/b}!"
    show diane a_shovel with dissolve
    diane "Did {b}Tony{/b} say anything?"
    anon "Uh huh, he said the milk has really taken their pizzas to a whole new level!"
    diane "{i}*Gasp*{/i}"
    diane "So he liked it?"
    anon "Heh, I'd say so."
    anon @ f_laugh "He wants to triple his next order!"
    show diane f_sad
    diane "Triple?!"
    show diane f_surprised_front
    diane "Hmm..."
    anon f_worried @ f_confused "Is that a problem?"
    show diane f_shamed_front
    diane "Huh? Oh... Well, I'm not sure."
    diane "I don't know if I can handle-"
    show diane f_surprised
    pause
    show diane f_smirk
    diane "I mean, my cow..."
    diane "... I don't know if she can handle that much demand."
    anon f_normal "Sounds like you might need to expand and get more cattle."
    show diane f_thinking
    diane "..."
    show diane f_thinking_back
    diane "I'm definitely not ready for that yet."
    diane "I'll just have to push her harder and start stockpiling..."
    show diane f_normal
    anon "Can I do anything to help?"
    diane "Heh, no, that's alright."
    diane "You've helped me plenty already."
    anon @ -m_talk "..."
    diane "Why don't you get back to your garden work?"
    anon "Yeah, okay..."
    show anon with dissolve:
        flip
        xoffset -500
    diane @ f_teasing "Oh!"
    show anon with dissolve:
        unflip
        xoffset 0
    diane "... I almost forgot."
    show diane a_money with dissolve
    diane "This is yours."
    show diane a_shovel
    show anon a_money f_surprised
    with dissolve
    anon "Huh? This is the entire payment from the delivery!"
    diane "Hehe, I told you, {b}[firstname]{/b}. This isn't a money making endeavor for me."
    show diane f_smirk
    diane "At least not for the moment."
    anon f_normal @ -m_talk "..."
    show diane f_normal
    diane "You take it and put it towards your tuition."
    anon "Thanks, {b}Diane{/b}!"
    show diane f_laugh
    diane "You're welcome, handsome!"
    show anon b_empty f_grin
    show diane b_kiss
    with dissolve
    pause
    hide diane
    hide anon
    with dissolve
    return

label dianes_dialogue_leave_d1:
    show player 14 at left
    show diane f_normal
    player_name "I should probably get started on the garden."
    show player 13
    diane "Alright."
    diane "Thanks again for helping!"
    show player 14
    player_name "No problem."
    hide player
    hide diane
    with dissolve
    return

label dianes_dialogue_delivery_3_reminder:
    show player 10 at left
    show diane b_naked a_idle:
        xoffset 0
    with dissolve
    player_name "What was I supposed to do again?"
    show player 13
    show diane f_normal
    diane "{b}Take the package of milk from my shed and deliver it to the cafeteria at your school{/b}."
    show player 14
    player_name "Oh, right."
    player_name "I'm on it!"
    hide player
    hide diane
    with dissolve
    return

label dianes_dialogue_pre_fun_paint:
    show player 10
    player_name "{b}[deb_name]{/b} said she gave you the old paint in the garage."
    player_name "You still have it right?"
    show player 5
    if L_diane_garden.is_here(M_diane):
        show diane f_laugh
    else:
        show diane b_naked a_idle f_laugh
    diane "Well, sure I do!"
    show diane f_normal
    show player 13
    diane "There should be some left in the shed."
    diane "Help yourself!"
    show player 14
    player_name "Thanks!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
