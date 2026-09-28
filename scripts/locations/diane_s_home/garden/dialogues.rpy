label dianes_garden_diane_find_carpenter:
    scene garden
    show player 14 at left
    show diane b_shirtless
    with dissolve
    player_name "Hey, {b}Diane{/b}!"
    show player 13
    diane "Hey, {b}[firstname]{/b}!"
    show player 14
    player_name "Have you spoken with {b}Annie{/b}'s dad yet?"
    player_name "You know, about building your barn?"
    show player 13
    diane "Oh, yes."
    diane "I spoke with him over the phone this morning."
    diane "He'll do it and for a good price too."
    show player 17
    player_name "That's great news!"
    show player 14
    player_name "When's he gonna start?"
    show player 13
    show diane f_sad
    diane "Well, that's the problem."
    show player 5
    diane "He was very noncommittal over the phone."
    show player 10
    player_name "Oh?"
    show player 5
    diane "I told him I needed it completed ASAP, but he needed to take care of a few odd jobs around his house first."
    diane "I was kinda hoping you could-"
    pause
    show diane f_normal
    diane "Oh, never mind. It's silly."
    show player 14
    player_name "No, go ahead."
    show player 13
    diane "Well... Do you think you could go over there and give him a hand?"
    show player 12
    player_name "Really?"
    show player 5
    diane "Yeah."
    diane "Just see if there's anything you can do to help him out, you know?"
    diane "Anything to get him over here and building as soon as possible."
    show player 10
    player_name "Hmm, I guess it couldn't hurt to check it out..."
    show player 5
    diane "I would really appreciate it, handsome."
    hide player
    show diane b_kiss_shirtless
    with dissolve
    pause
    hide diane
    show player 29 at left
    show diane b_shirtless
    with dissolve
    player_name "Heh, no problem!"
    show player 13 with dissolve
    diane "I'll be in the shed pumping if you need me."
    hide diane with dissolve
    pause
    show player 12
    player_name "Hmm, I guess I should {b}head over to Annie's house and speak with her father{/b}."
    hide player with dissolve
    return

label garden_diane_drunken_splur_aftermath:
    scene garden
    show player 35 with dissolve
    player_name "No use working on the garden today..."
    player_name "... I'll have to come back another time."
    hide player with dissolve
    $ game.main()
    return

label garden_diane_gardening_help:
    scene expression "backgrounds/location_diane_garden_closeup.jpg"
    show player 684
    player_name "( Phew, it's really cooking outside today... )"
    pause
    show player 685
    player_name "( I hope {b}Diane{/b} is doing alright in the shed. )"
    player_name "( She's been keeping her distance these past couple- )"
    diane "OOOWWWW!!!" with hpunch
    show player 23 with dissolve
    player_name "{i}*Gasp*{/i} {b}Diane{/b}?!"
    show player 22
    diane "OW! OW! OW!"
    show player 12
    player_name "I'm coming!!!"
    hide player with dissolve
    return

label dianes_garden_diane_drunk_like_a_sailor:
    scene expression "backgrounds/location_diane_garden_close_day_blur.jpg"
    show diane_chair up zorder 1
    show diane b_laying_back_shirtless a_wave f_laugh zorder 2:
        yoffset 20
    with dissolve
    diane "Yoo hoo, {b}[firstname]{/b}!!!"
    show diane f_smirk
    diane "Could you lend me a hand?"
    player_name "Coming!"
    show diane a_drink_sip f_drinking with dissolve
    pause
    show diane a_drink f_smirk_up
    show player 429 zorder 0 at Position (xpos=175,ypos=648)
    with dissolve
    player_name "How can I help, {b}Diane{/b}?"
    show player 426
    show diane f_smirk_up
    diane "I'm just worried I'm gonna burn, sitting out here in the sun like this..."
    show diane a_wave with dissolve
    diane "... Think you could help me out?"
    show player 435
    player_name "Y-you want me to put sunscreen on your back?"
    show player 434
    show diane f_laugh a_single_bottle with dissolve
    diane "For starters, yes!"
    show diane f_smirk_up
    show player 435
    player_name "{i}*Gulp*{/i} Y-yeah, okay."
    show player 434
    show diane f_smirk_up b_laying_sitting_topless zorder 2
    with dissolve
    diane "Let me get myself situated."
    show diane_chair down
    show diane b_laying1 zorder 2:
        yoffset 0
    with dissolve
    pause
    show player 426 at Position (xpos=387,ypos=648) with dissolve
    pause
    show player 427
    player_name "Should I go under these straps?"
    show player 426
    diane "Well, yeah!"
    diane "Go ahead and undo them for me."
    show player 429g
    player_name "!!!"
    hide player
    show diane b_laying_remove1
    with dissolve
    pause
    show diane b_laying_remove2 with dissolve
    pause
    show player 429 zorder 0 at Position (xpos=560,ypos=798)
    show diane b_laying2
    with dissolve
    player_name "Like this?"
    show player 426
    diane "Just like that."
    diane "Have at it, stud!"
    player_name "..."
    show player massage 2 with dissolve
    pause
    show player massage 3 with dissolve
    pause
    hide player
    show diane b_laying_massage_back
    with dissolve
    diane "Mmm, that feels wonderful!"
    diane "Make sure you don't miss a spot."
    show player 429b zorder 0 at Position (xpos=560,ypos=798)
    show diane b_laying2
    with dissolve
    player_name "Mmmhmm."
    hide player
    show diane b_laying_massage_back
    with dissolve
    pause
    pause
    show player massage 3 zorder 0 at Position (xpos=560,ypos=798)
    show diane b_laying2
    with dissolve
    diane "Oh, that's really nice..."
    pause
    show player massage 5
    show diane b_laying3
    with dissolve
    pause
    show diane b_laying4 with dissolve
    pause
    show player massage 4
    show diane b_laying5
    with dissolve
    player_name "!!!"
    player_name "( Does she really want me to rub lotion down there too? )"
    pause
    show player massage 5
    diane "Keep going, {b}[firstname]{/b}."
    show player 429h with dissolve
    player_name "Heh, o-okay."
    hide player
    show diane b_laying_massage_naked_back
    with dissolve
    pause
    pause
    player_name "Here goes..."
    show diane b_laying_massage_butt with dissolve
    pause
    diane "Mmm."
    pause
    show player 429h zorder 0 at Position (xpos=560,ypos=798)
    show diane b_laying5
    with dissolve
    player_name "I umm... Think I got it all, {b}Diane{/b}."
    show player 429d
    diane "Oh?"
    diane "Are you sure you didn't miss a spot?"
    show player 429g
    player_name "..."
    diane "Hehehe, I'm just teasing you, handsome."
    show player 429b
    player_name "I should get back to work."
    show player 429g
    show diane b_laying_getup with dissolve
    diane "Well, hold on!"
    player_name "!!!"
    show diane b_laying_kick:
        yoffset -5
    show diane_chair up
    with dissolve
    diane "You've got a whole other side to work on."
    show diane b_laying_back_naked a_laydown f_smirk_up:
        yoffset 20
    show player 429b at Position (xpos=355,ypos=648)
    with dissolve
    player_name "{i}*Gulp*{/i} R-really?"
    show player 429c
    diane "Mhmm."
    diane "You don't want me to burn, now do you?"
    show player 429b
    player_name "N-no, of course not."
    show player 429c
    diane "Why don't you start with my chest?"
    show diane a_cream with dissolve
    show player 429b
    player_name "Y-your chest?"
    show player 429c
    diane "Here, I'll show you."
    show diane a_laydown
    show player 429i at Position (xpos=387,ypos=648)
    with dissolve
    diane "Just put your hand..."
    hide player
    show diane b_laying_grope1
    with dissolve
    diane "... Right here."
    show diane b_laying_grope f_explain with dissolve
    pause
    diane "Oooh, this is just what I needed {b}[firstname]{/b}!"
    pause
    diane "My breasts are so sore from all this milking..."
    player_name "Mmmhmm."
    pause
    diane "Nngghh!"
    diane "Be careful with my nipples, they're very tender right now..."
    pause
    show diane b_laying_back_naked
    show player 81 at Position (xpos=403,ypos=648)
    with dissolve
    player_name "( Oh no, not again! )"
    show player 78
    diane "Hmm?"
    show diane f_smirk_up
    diane "Why did you stop?"
    show diane f_surprised_down
    diane "!!!" with hpunch
    show player 426e with dissolve
    player_name "Sorry, {b}Diane{/b}!"
    player_name "This is so embarrassing, I can't-"
    show diane f_smirk_up
    diane "Shh!"
    diane "It's alright, {b}[firstname]{/b}."
    diane "You just got a little excited helping me out."
    diane "It's perfectly natural."
    show player 427b with dissolve
    player_name "Yeah, but-"
    show player 78 with dissolve
    diane "Let me help you."
    show player 427b with dissolve
    player_name "Help me?"
    show player 427c
    player_name "!!!" with hpunch
    show player 427d_e
    pause
    diane "That feels good, doesn't it?"
    player_name "Y-yeah..."
    player_name "... That feels really good!"
    show diane f_laugh
    diane "Hehe, see?"
    show diane f_smirk_up
    diane "There's nothing to be embarrassed about."
    pause
    diane "I haven't felt one of these in a very loooong time."
    player_name "..."
    pause
    show diane f_laugh
    diane "I can't believe it's so big!"
    show diane f_smirk_up
    player_name "I-"
    player_name "Umm, t-thanks."
    show diane f_laugh
    diane "Hehehe!"
    show diane f_smirk_up
    pause
    player_name "{b}Diane{/b}, I'm gonna-"
    diane "Let it out, stud."
    pause
    show player 426b
    player_name "HNNGGG!!!" with flash
    pause
    player_name "Haaah... Haaah..."
    player_name "!!!"
    show player 426g
    player_name "Oh my gosh, {b}Diane{/b}, I'm sorry!"
    player_name "I didn't mean to-"
    show player 426h
    diane "Hehe, you didn't do anything to be sorry about, {b}[firstname]{/b}!"
    diane "C'mon, let's go inside and get you cleaned up."
    show player 426g
    player_name "O-okay."
    hide player
    hide diane
    hide diane_chair
    with dissolve
    scene expression "backgrounds/location_diane_kitchen_closeup.jpg"
    show player 139 at left
    show diane b_shirtless f_smirk
    with dissolve
    player_name "..."
    diane "Mmm, see? Just a quick- {i}*Hic*{/i}"
    diane "Just a quick clean up and you're good as new!"
    show player 140
    player_name "Y-yeah..."
    show player 139
    diane "Ooh, I think I drank too much again."
    diane "I should go lie down."
    diane "Thanks so much for my day off, {b}[firstname]{/b}!"
    show diane f_laugh
    diane "It was just what the doctor ordered."
    show diane f_smirk
    show player 140
    player_name "I'm glad you enjoyed it."
    show player 139
    show diane f_laugh
    diane "Hehe, very much!"
    hide player
    show diane b_kiss_mouth
    with dissolve
    player_name "!!!"
    show player 3 at left
    show diane b_shirtless f_smirk
    with dissolve
    diane "Goodnight, stud!"
    hide diane with dissolve
    show player 29
    player_name "G-goodnight."
    $ renpy.end_replay()
    show player 3
    player_name "..."
    player_name "( I can't believe that just happened! )"
    player_name "( {b}Diane{/b} just- )"
    show player 18 with dissolve
    player_name "( ... )"
    player_name "( Wow! )"
    show player 13
    player_name "( I hope she doesn't regret this once she sobers up. )"
    player_name "( I should get home. )"
    hide player with dissolve
    $ persistent.cookie_jar["Diane"]["unlocked"] = True
    $ persistent.cookie_jar["Diane"]["gallery"]["02_unlocked"] = True
    return

label garden_diane_check_up:
    scene garden
    show player 14 with dissolve
    player_name "I should look for {b}Diane{/b}."
    show player 35
    player_name "{b}... Maybe she's inside{/b}?"
    hide player with dissolve
    return

label dianes_garden_diane_clear_bug_infested_garden:
    scene garden_dead
    show player 14 at left
    show diane b_casual
    with dissolve
    player_name "Hmm, looks like I missed a few of the nests..."
    show player 13
    diane "Don't worry, the {b}pesticide{/b} will take care of them."
    diane "You go ahead and start spraying while I get changed."
    diane "When I get back, we can start replanting."
    show player 14
    player_name "Sounds good."
    hide player
    hide diane with dissolve
    return

label diane_garden_first_time:
    scene location_diane_garden_cutscene05
    show text _ ("I didn't know the first thing about gardening but it was nice to see {b}Diane{/b}.\nI always liked her when I was a kid.") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("She was just a fun person to be around!\nKind-hearted and supportive.\nA great sense of humor and full of warmth.") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("I really hope I don't disappoint her...") as caption with dissolve
    pause

    scene garden
    show anon
    show diane a_shovel
    with fade
    diane "Well, there's a handsome young man..."
    show diane f_laugh
    diane "You've grown so much, I hardly recognized you at the funeral."
    show diane f_normal
    anon @ f_laugh "Heh, hi {b}Diane{/b}."
    show diane f_surprised
    anon "Wow! You look so much like {b}[deb_name]{/b}..."
    show diane f_thinking
    diane "Oh, come now. I'm not nearly as pretty as {b}[deb_name]{/b}..."
    show diane f_surprised
    anon @ f_brag_closed "Well, I think you look great, {b}Diane{/b}!"
    show diane a_blush f_laugh_blush with dissolve
    diane "Aww, aren't you just a little charmer?!"
    show diane f_surprised
    diane "..."
    show diane f_laugh_blush with dissolve
    diane "You here to do some work for me?"
    show diane f_normal
    diane "I'm guessing {b}[deb_name]{/b} told you I'm looking for someone to help me this summer?"
    anon "Yeah, she told me to come see you. I could definitely use the money for tuition."
    diane "Wonderful!"
    diane "I was hoping to get you started today but I'm afraid I ran into a problem..."
    show diane f_shamed_look a_broken with dissolve
    diane "My old shovel finally quit on me."
    show diane f_shamed
    anon f_worried_low "Oh! Yeah, that looks pretty bad."
    show diane f_shamed_smile
    diane "We may have to wait until I can replace it..."
    diane "I'm sorry, {b}[firstname]{/b}."
    show diane f_shamed a_shovel with dissolve
    anon f_normal "It's okay, {b}Diane{/b}."
    show diane f_normal with dissolve
    anon "Is there any way we can continue the work without it?"
    diane "Well, we can't really dig up a garden without a shovel, can we?"
    diane "I'll just have to pick up a new one next time I'm at the store."
    show diane f_teasing
    diane "Unless..."
    show diane f_normal
    anon @ f_skeptical "Unless?"
    diane "... You wouldn't happen to have one at home?"
    anon @ f_thinking a_thinking -m_talk "Hmm..."
    anon "We might {b}have a shovel in our garage{/b}!"
    anon "I'll go check and come back if I find something."
    show diane f_laugh
    diane "That would be great!"
    show diane f_normal
    diane "Come on back if you find one, and we'll get started."
    hide diane
    hide anon
    with dissolve
    return

label diane_garden_need_shovel_has_shovel:
    scene garden
    show diane
    show anon a_backpack f_looking_down
    with dissolve
    anon @ -m_talk "Hmm..."
    show anon a_backpack_shovel1 with dissolve
    pause
    show anon a_backpack_shovel2 with dissolve
    pause
    show anon f_normal a_shovel with dissolve
    anon "Here it is!"
    show diane f_laugh
    diane "Ohh! Wonderful!"
    show diane f_normal
    diane "See, you've been a big help already!"
    show diane a_shovel_give
    show anon a_idle
    with dissolve
    diane "Alright, before you start, I'll have to show you what to do..."
    show diane a_finger f_explain with dissolve
    diane "Make sure you {b}only keep the vegetables that are long and hard{/b}!"
    diane "Take out everything else... Especially those pesky rats and bugs, got it?"
    show diane a_shovel f_normal with dissolve
    anon "Got it!!"
    diane "You should really {b}take all the money I'm paying you to the bank{/b} too, when you're done!"
    diane "That's your decision though."
    anon @ a_behind_head "Umm, sure. I guess I could do that..."
    show diane f_laugh
    diane "Alright handsome, let's get to work!"
    show anon b_empty f_grin
    show diane b_kiss
    with dissolve
    anon @ -m_talk "..."
    hide anon
    hide diane
    with dissolve
    call popup ('minigame', 'gardening')
    return

label diane_garden_need_shovel_no_shovel:
    scene expression player.location.background_blur with None
    show player 2 at left
    show diane
    with dissolve
    player_name "I still haven't found that {b}shovel{/b}."
    player_name "Is there any way we can continue the work without it?"
    show player 1
    diane "Well, we can't really dig up a garden without a shovel, can we?"
    diane "I'll just have to pick up a new one next time I'm at the store."
    show diane f_teasing
    show player 11
    diane "Unless..."
    show player 10
    show diane f_normal
    player_name "Unless?"
    show player 11
    diane "... You wouldn't happen to have one at home?"
    show player 4
    player_name "Hmm..."
    show player 2
    player_name "We might {b}have a shovel in our garage{/b}!"
    player_name "I'll go check and come back if I find something."
    show player 203
    show diane f_laugh
    diane "That would be great!"
    show diane f_normal
    diane "Come on back if you find one, and we'll get started."
    hide diane
    hide player
    with dissolve
    return

label diane_garden_delivery_1_task:
    scene garden
    show diane a_shovel
    show anon
    with dissolve
    diane "Oh, {b}[firstname]{/b}, I'm so glad you came by today!"
    anon f_worried "Uh oh, another garden emergency?"
    show diane f_laugh
    diane "Heh, not exactly..."
    show diane f_normal
    diane "I haven't told you about my side business yet, have I?"
    anon @ f_skeptical "Side business? I thought you just lived off the money you got in your divorce?"
    show diane f_smirk
    diane "Heh, well, I do for the most part. My little startup is more of a pet project than an actual money making endeavor..."
    anon f_normal "Alright, so what is it?"
    show diane f_normal
    diane "I've been packaging and selling milk."
    anon "Milk?! I didn't know you had a cow! That's awesome!"
    diane @ -m_talk "..."
    anon a_salute f_surprised "Where is she? Can I pet her?"
    show diane f_laugh
    diane "Hahaha!"
    show diane f_smirk
    diane "Sorry, handsome. My cow is... Well, let's just say she isn't fond of visitors."
    anon a_idle f_worried "Aww, okay..."
    anon f_normal "So what do you need my help with?"
    show diane f_normal
    diane "A local business placed an order and I need someone to deliver it for me."
    anon "I can do that!"
    diane "You don't mind?"
    diane "It would be a huge help."
    anon "No, I don't mind at all."
    show diane f_laugh
    diane "Oh, wonderful!"
    show anon b_empty f_grin
    show diane b_kiss
    with dissolve
    pause
    show anon b_dressed of_blush f_normal
    show diane b_dressed f_normal
    with dissolve
    diane "I dunno what I'd do without you, {b}[firstname]{/b}!"
    anon @ f_shy a_behind_head "Heh, it's no problem. I love to help!"
    diane "Let me grab the package for you..."
    hide diane with dissolve
    pause
    anon of_empty f_laugh @ -m_talk "( Wow, this is so cool! )"
    anon @ -m_talk "( {b}Diane{/b} really is like a farm girl at heart. )"
    anon f_normal @ a_thinking f_thinking "( I hope she lets me meet her cow some day... )"
    show diane a_milk_package with dissolve
    diane "Here we are."
    anon f_shy_low "Whoa, it has your face on it and everything!"
    show diane f_smirk
    diane "Yup."
    anon "Hmm, {b}\"Auntie Diane's Original\"{/b}."
    diane "Hehehe, you like that?"
    anon f_normal "Yeah, it's got a nice ring to it!"
    diane "I thought so too."
    show diane f_cheese a_shovel
    show anon a_milk_cartons_small
    with dissolve
    anon "So, where am I taking it?"
    show diane f_normal
    diane "Just down the road to a little pizzeria called {b}Tony's Pizza{/b}."
    anon "Hey, I know that place!"
    anon "The owner is a great guy."
    diane "Yeah, and I hear their food is pretty good too."
    diane "Send them my regards, won't you?"
    diane "Oh, and don't forget to collect the payment."
    anon "Sure thing."
    anon @ f_laugh "I'll be back in a flash!"
    hide anon
    hide diane
    with dissolve
    return

label dianes_garden_diane_drunken_splur:
    scene location_diane_garden_close_day_blur with None
    show player 11 at left
    show diane b_shirtless a_drink f_drunk
    with dissolve
    diane "Yoo-hooo! There you are, handsome!"
    show player 5
    diane "How are you- {i}*Hic*{/i} doing today?"
    diane "You here to give me another sh- {i}*Hic*{/i}"
    diane "... Another show?!"
    show diane a_drink_sip with dissolve
    show player 12
    player_name "{b}Diane{/b}? Are you drunk?"
    show player 11
    show diane a_drink with dissolve
    diane "Hehehe, yeeeaaah..."
    diane "Just a little though!"
    diane "It's so hot out here, you know?!"
    diane "I just- {i}*Hic*{/i}"
    diane "I just needed a little something to cool myself off..."
    diane "... And I thought to myself, \"Self,\" {i}*Hic*{/i} \"your side business is really starting to take off!\""
    diane "If that's not a cause for celebration, I don't know what is!"
    show diane a_drink_sip with dissolve
    pause
    show diane b_shirtless_pull a_drink_pull with dissolve
    player_name "!!!"
    diane "You wanna celebrate with me, {b}[firstname]{/b}?"
    show player 22
    pause
    show player 10
    player_name "{b}Diane{/b}, your clothes... They... Umm... Slipped."
    show player 11
    diane "Huh? What are you..."
    show diane a_drink_hand_pull with dissolve
    diane "Oh!!"
    show diane a_reach_pull f_laugh_blush with dissolve
    diane "Hahaha!"
    show player 21
    show diane f_shamed
    player_name "Heh..."
    show player 13
    diane "I guess I shouldn't have taken my shirt off, huh?"
    diane "It doesn't help having these... Massive udders flopping around!!"
    show diane f_laugh_blush
    diane "Haha!"
    show diane b_shirtless a_reach f_shamed with dissolve
    pause
    show player 11
    show diane b_shirtless_pull a_drink_hand_pull with dissolve
    diane "Oops, they keep trying to escape!"
    show diane a_reach_pull f_laugh_blush with dissolve
    diane "Haha!"
    show player 1
    show diane b_shirtless a_drink f_drunk with fastdissolve
    diane "There."
    diane "Have I ever told you how much I dislike {b}[deb_name]{/b}'s daughter?"
    show player 10
    show diane f_drunk
    player_name "Uh, no..."
    player_name "... You mean, {b}[jen_name]{/b}?"
    show player 5
    show diane f_laugh_blush
    diane "Yes! {i}*Hic*{/i} That's the one!"
    show diane f_drunk
    diane "She's such a biiiitch!"
    show player 11
    pause
    diane "I wish I had nice young tits like her though."
    show diane a_drink_sip with dissolve
    pause
    show diane a_drink with dissolve
    diane "What's the matter?"
    diane "You don't like her tits?"
    show diane f_drunk
    show player 24
    player_name "I uhh-"
    show diane a_drink_hand with dissolve
    diane "You're telling me you haven't noticed them?"
    show diane a_drink with dissolve
    show player 10
    player_name "Well, I don't know..."
    show player 11
    diane "Here."
    show diane b_shirtless_pull a_pull with fastdissolve
    show player 22
    pause
    show player 11
    diane "I mean, don't you think they look better than these old things?"
    show player 21
    player_name "No, I think your breasts look great, {b}Diane{/b}!"
    show player 13
    diane "Awww!"
    diane "You're so- {i}*Hic*{/i}"
    diane "... So sweet!"
    pause
    show diane a_reach_pull f_shamed with dissolve
    show player 11
    diane "Hmm..."
    diane "... I don't feel so good all of a sudden."
    diane "I think I need to- {i}*Hic*{/i}"
    diane "I need to lie down for a bit."
    show diane b_sitting_drunk with dissolve
    show player 427
    player_name "Whoa, whoa, whoa!"
    player_name "{b}Diane{/b}, you can't just lie down in the garden!"
    show player 13
    show diane b_shirtless_pull a_reach_pull
    with dissolve
    diane "Hmm?"
    show player 14
    player_name "Lemme help you upstairs to your bed."
    show player 13
    show diane f_drunk
    diane "Aww, would you do that for- {i}*Hic*{/i}"
    diane "... Do that for me?"
    show player 14
    player_name "Of course, here."
    hide player
    show diane b_hold_talk
    with dissolve
    diane "Mmm, such a helpful young man!"
    show diane b_hold_peek
    pause
    show diane b_hold_talk
    diane "You're so much sweeter than all the other worthless men in this town."
    show diane b_hold_peek
    player_name "..."
    diane "..."
    show diane b_hold_talk
    diane "Hehehe, it's on the top floor, stud."
    show diane b_hold
    player_name "!!!"
    player_name "Right, sorry."

    scene location_diane_garden_cutscene07
    show text _ ("I'd never seen {b}Diane{/b} this drunk before!\nI helped her up the stairs to her room, doing my best to listen as she drunkenly poured her heart out.") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("She went on and on about her no good ex-husband and the men she'd seen since they'd divorced.\nI was beginning to suspect there was more to this drunken episode\nthan a simple celebration. ") as caption with dissolve
    pause

    scene location_diane_bedroom_closeup
    show diane b_hold_tired_talk
    with fade
    diane "... He wouldn't even talk with me about children, the worthless prick."
    diane "What kinda man doesn't want to settle down and start a family?!"
    show diane b_hold_tired
    player_name "..."
    show diane b_hold_tired_talk
    diane "Now he's probably off gambling his money away and banging cheap whores!"
    show diane b_hold_tired
    player_name "Okay {b}Diane{/b}, here we are."
    player_name "Let's get you in bed, okay?"
    show diane b_hold_talk
    diane "Pfft, hahaha!"
    diane "{b}[firstname]{/b} wants to get me into bed..."
    diane "... No one's tried to do that for a loooooong time!"
    show diane b_hold
    player_name "!!!"
    show diane b_hold_talk
    diane "Hahaha!"
    diane "Oh, I'm just- {i}*Hic*{/i}"
    diane "I'm just teasing you, stud..."
    diane "... I think I can take it from here."
    show diane b_shirtless_pull a_tired f_drunk
    show player 13 at left
    with dissolve
    diane "Why don't you go and {b}fetch me a glass of water from the kitchen{/b}?"
    show player 14
    player_name "Y-yeah, okay."
    show player 13
    diane "Good boy."
    hide diane
    hide player
    with dissolve
    return

label dianes_garden_diane_mouse_attack_not_known:
    scene garden with None
    show player 1f with dissolve
    pause
    show player 32f at Position(xoffset=-69)
    player_name "Huh?"
    player_name "Where's {b}Diane{/b}?"
    player_name "She's usually out here working on her garden..."
    show player 31 at Position(xoffset=68)
    pause
    show player 30
    player_name "... It doesn't look like she's in her shed either."
    show player 12
    player_name "She must be inside."
    player_name "It's really hot outside today!"
    show player 5
    player_name "..."
    show player 10
    player_name "Maybe I should check up on her before I start working."
    hide player with dissolve
    return

label dianes_garden_diane_need_shovel_remove_waste:
    scene expression player.location.background_blur with None
    show player 203 at left
    show diane a_shovel
    with dissolve
    diane "Oh, there you are. Thank goodness!"
    diane "I was starting to think you weren't coming by today."
    show player 2
    player_name "Hi, {b}Diane{/b}!"
    player_name "Is everything alright?"
    show player 203
    diane "Everything's fine. You've been doing a great job with my garden, {b}[firstname]{/b}!"
    diane "In fact, you're doing so well, that we have a ton of leftover waste!"
    show player 17
    player_name "Sorry about that. Haha."
    show player 203
    diane "No need to be sorry, handsome!"
    diane "I just need help moving it."
    diane "I loaded it all up in this wheelbarrow..."
    diane "... But I'm afraid it's too much for my poor back."
    diane "Do you think you could help me out?"
    show player 14
    player_name "Of course!"
    player_name "That's why I'm here!"
    show player 13
    diane "Just be careful, it's really heavy!"
    show player 2
    player_name "No problem!"
    player_name "I'll take care of it!"
    return

label dianes_garden_diane_need_shovel_remove_waste_repeat:
    scene expression player.location.background_blur with None
    show player 203 at left
    show diane a_shovel
    with dissolve
    diane "I was starting to think you weren't coming by today."
    show player 2
    player_name "Hi, {b}Diane{/b}!"
    player_name "Is everything alright?"
    show player 203
    diane "Everything's fine. I just need {b}help moving this wheelbarrow{/b}..."
    diane "... I'm afraid it's too much for my poor back."
    diane "Do you think you could help me out?"
    show player 14
    player_name "Of course!"
    player_name "That's why I'm here!"
    show player 13
    diane "Just be careful, it's really heavy!"
    show player 2
    player_name "No problem!"
    player_name "I'll take care of it!"
    return

label dianes_garden_diane_need_shovel_remove_waste_pass:
    scene expression player.location.background_blur with None
    show player 255 at left
    show diane a_shovel
    with dissolve
    player_name "There we go."
    player_name "See, I can handle it!"
    show player 254
    show diane f_laugh_blush
    diane "!!!" with hpunch
    diane "Wow... You lifted it like it was nothing!"
    show diane f_smirk
    pause
    show player 254
    diane "Strong and handsome..."
    diane "I bet you have to fight those young girls at school off with a stick, don't you?!"
    show player 255
    player_name "Hah, no... Not really."
    show player 254
    show diane f_laugh
    diane "Oh, come now! I don't believe that for one second!"
    show diane f_smirk
    diane "In my younger years, I'd have been all over you in an instant!"
    show player 255
    show xtra 21 at Position (xpos=88) with dissolve
    player_name "Hehe."
    player_name "I uhh..."
    player_name "... Where would you like me to dump this?"
    show player 254
    diane "Hmm?"
    show diane f_lookup
    diane "Oh, right!"
    show diane f_normal
    diane "Just follow me, handsome."
    diane "I keep a compost heap just over here, behind the house."
    show player 255
    hide xtra with dissolve
    player_name "Compost?"
    player_name "Like, garbage?"
    show player 254
    show diane f_laugh
    diane "What? Hehe, no!"
    show diane f_normal
    diane "Compost is a valuable resource for a gardener, {b}[firstname]{/b}!"
    diane "All that organic matter decomposes and creates a nutrient rich fertilizer for the soil."
    show player 255
    player_name "Really? So it helps the plants grow?"
    show player 254
    diane "That's right!"
    diane "It's what makes my vegetables so..."
    show diane f_smirk
    diane "Girthy."
    show player 255
    player_name "Awesome!"
    player_name "I'm learning so much from you, {b}Diane{/b}!"

    scene location_diane_garden_cutscene04
    show text _ ("The compost pile behind her house was so far!\nI barely made it; the wheelbarrow kept slipping out of my hands.") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("It felt good though, moving all that waste for {b}Diane{/b}.\n... And I was learning a lot about gardening!") as caption with dissolve
    pause

    scene location_diane_garden_day_blur
    show player 18 at left
    show diane a_shovel f_laugh_blush
    with fade
    diane "I can't believe you did it with such ease!"
    show diane f_normal
    show player 17
    player_name "It was pretty hard, actually. Haha!"
    show player 203
    diane "Well, I sure am glad you were here..."
    diane "I don't know what I would have done without you!"
    show player 2
    player_name "It's no big deal."
    player_name "I like the exercise!"
    show player 203
    show diane f_teasing
    diane "I bet you do..."
    diane "... You must exercise all the time."
    show diane f_smirk
    show player 11
    player_name "..."
    show player 21
    player_name "What do you mean?"
    show player 13
    show diane f_laugh
    diane "C'mon, what's your secret? You're so lean and fit!"
    show diane f_thinking
    show player 11
    diane "I try to stay active as often as possible but I can't seem to get rid of all this fat."
    show diane f_normal
    show player 10
    player_name "Fat?! What fat?"
    show diane f_surprised
    show player 29 with dissolve
    player_name "You look great, {b}Diane{/b}."
    show diane a_blush f_laugh_blush with dissolve
    show player 13 with dissolve
    diane "Aww. You say that now. But if you saw me without clothes on, you'd be singing a different tune!"
    show diane f_surprised
    show player 11
    player_name "..."
    show diane a_shovel f_laugh_blush with dissolve
    diane "Err... Anyway!"
    show diane f_teasing
    diane "... You gonna tell me your trick or not?"
    diane "Have you been working out?"
    show diane f_smirk
    show player 21
    player_name "A little."
    show player 35
    player_name "I try going to the gym sometimes."
    show player 13
    show diane f_normal
    diane "Really?!"
    diane "That's great!"
    show diane a_finger f_explain with dissolve
    diane "You know, there are many good advantages to staying in shape."
    show diane a_shovel f_teasing with dissolve
    show player 11
    diane "Women love guys who are lean, strong, and full of vigor."
    show diane f_smirk
    player_name "..."
    diane "Let's see that six-pack!"
    show player 22
    player_name "!!!" with hpunch
    show player 21
    player_name "You want to see my..."
    show player 11
    diane "Your abs! Yes."
    diane "Give this old lady a show!"
    show player 10
    player_name "O-okay..."
    show diane f_surprised
    show player 249 with dissolve
    show diane a_blush f_laugh_blush with dissolve
    diane "Whooo!"
    show diane a_shovel f_smirk with dissolve
    diane "Look at that sexy body!"
    show diane f_teasing
    diane "How can you not be popular with the girls at school?"
    show diane f_smirk
    show player 250
    player_name "Heh, I dunno..."
    show diane f_surprised
    show player 108f with dissolve
    player_name "There are guys much bigger than me at school."
    player_name "I'm definitely not one of the cool guys..."
    show player 109f
    show diane f_teasing
    diane "Aww, well, that's okay, {b}[firstname]{/b}."
    show diane f_thinking
    show player 13
    diane "The girls will grow out of that phase sooner than you think..."
    show diane f_laugh_blush
    diane "... Just give it some time!"
    show diane f_eyes_closed
    show player 17
    player_name "Thanks, {b}Diane{/b}."
    show diane f_smirk
    show player 203
    diane "No problem, stud!"
    show xtra 21 at left with dissolve
    player_name "..."
    show diane f_normal
    diane "..."
    show diane f_thinking a_blush with dissolve
    diane "Boy, it sure is hot out here, isn't it?"
    show diane f_normal
    show player 14
    hide xtra with dissolve
    player_name "Heh, yeah. I'm sweating like crazy!"
    show player 13
    show diane a_finger with dissolve
    diane "Well, I bet I can come up with a solution to that..."
    show diane b_hose with dissolve
    show player 10
    player_name "Oh?"
    show player 12
    player_name "What are you-"
    show diane b_dressed a_hose f_cheese with dissolve
    show player 11
    player_name "..."
    show player 10
    player_name "You aren't gonna-"
    show diane a_hose_shoot
    show player 668
    player_name "!!!" with hpunch
    pause
    player_name "Whoa! That's freezing!"
    show player 669f with dissolve
    show diane f_laugh
    diane "Oh, no you don't! You aren't getting away that easily!"
    hide player with dissolve
    show diane b_hose_chase with dissolve
    diane "Hahaha!"

    scene location_diane_garden_cutscene06
    show text _ ("{b}Diane{/b} and I wrestled with that hose, spraying one another and giggling like school children.") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("We didn't get a lot accomplished in the garden that day but we did have a lot of fun!") as caption with dissolve
    pause

    scene location_diane_garden_night_blur
    show player 677 at left
    show diane b_dressed_wet f_laugh a_blush
    with fade
    diane "Okay, okay! I submit!"
    show diane f_normal
    diane "I can't keep up with you..."
    show diane f_cheese a_shovel with dissolve
    show player 678
    player_name "I win?!"
    show player 677
    show diane f_normal
    diane "Yeah, yeah... You win!"
    show player 679 with dissolve
    player_name "Hahaha! Victory!"
    show diane f_laugh
    diane "Hehehe!"
    show player 677 with dissolve
    show diane f_lookup
    pause
    diane "Sheesh, is it getting dark already?"
    show diane f_normal
    diane "You should get on home, {b}[firstname]{/b}."
    diane "I have some other work to do tonight."
    show player 678
    player_name "Anything I can help with?"
    show player 677
    show diane f_surprised
    diane "Hmm?"
    show diane f_smirk
    diane "Nah, I think not. I appreciate the offer, but this is work I'm better off doing alone..."
    show player 678
    player_name "O-okay..."
    show player 677
    show diane f_normal
    diane "Thanks again for all your help today, stud!"
    diane "Tell {b}[deb_name]{/b} I said, \"Hi.\""
    show player 678
    player_name "Alright."
    player_name "See ya soon, {b}Diane{/b}."
    hide player
    hide diane
    with dissolve
    return

label dianes_garden_diane_need_shovel_remove_waste_fail:
    scene location_diane_garden_day_blur
    show player 253 at left with dissolve
    pause
    show player 256 at Position(xpos=0.0322,ypos=1.0000)
    show diane a_shovel
    with dissolve
    player_name "Ughhh...!"
    player_name "Ghhh..."
    show player 27 with dissolve
    player_name "I... I can't do it..."
    player_name "I'm sorry..."
    show player 3
    diane "Oh..."
    diane "It's... Okay. I really did pack it way too full..."
    diane "I'll just take some out, and we can do it little by little."
    show player 23
    player_name "No, wait... I can do it!"
    show player 256 with dissolve
    diane "..."
    show player 10 with dissolve
    player_name "I'm just tired today, that's all..."
    player_name "Let me rest and get some {b}strength{/b}. I'll come back and do it another day, I promise."
    show player 3
    diane "..."
    show diane f_laugh
    show player 5
    diane "Oh? Well, if you say so..."
    show diane f_normal
    diane "I'll see you again soon?"
    show player 2
    player_name "Yeah, I'll be back real soon."
    player_name "Thanks, {b}Diane{/b}!"
    hide player
    hide diane
    with dissolve
    return

label dianes_garden_diane_delivery_3_task_week:
    scene garden
    show player 13 at left
    show diane b_shirtless
    with dissolve
    diane "Hey there, stud!"
    diane "You ready to make another delivery?"
    show player 17
    player_name "Oh, so that's the big job you were talking about!"
    show player 13
    diane "Well, of course."
    diane "What did you think it was?"
    show player 29 with dissolve
    player_name "I..."
    player_name "I dunno."
    show player 3
    show diane f_smirk
    diane "Mmhmm."
    diane "Naughty boy..."
    diane "This is my biggest customer yet, {b}[firstname]{/b}."
    diane "Do a good job and you can help me with my pumping when you get back, deal?"
    show player 17 with dissolve
    player_name "Deal!"
    show player 13
    show diane f_laugh
    diane "Hehe."
    show diane f_smirk
    show player 14
    player_name "So where is the package going this time?"
    show player 13
    show diane f_normal
    diane "Just {b}deliver it to the cafeteria at your school{/b}."
    show player 22
    player_name "!!!"
    show player 10
    player_name "My school?"
    show player 11
    diane "That's right!"
    show player 10
    player_name "You mean the students at school will be drinking-"
    show player 11
    diane "You'd better hurry, handsome."
    diane "I told your principal to expect delivery ASAP."
    player_name "..."
    show player 10
    player_name "Okay."
    show player 5
    diane "{b}The package is in the shed{/b}."
    show player 10
    player_name "Got it."
    hide player
    hide diane
    with dissolve
    return

label dianes_garden_diane_delivery_3_done:
    scene garden
    show player 640e at left
    show diane b_shirtless
    with dissolve
    player_name "Hey, {b}Diane{/b}."
    player_name "I delivered that package to my school for you."
    show player 13
    show diane a_money f_shamed_smile
    with dissolve
    diane "Yeah, I just got off the phone with the cafeteria guy."
    show diane a_idle with dissolve
    diane "He's already placed another order."
    diane "Even bigger than the last."
    show diane f_shamed
    show player 14
    player_name "That's a good thing, right?"
    show player 13
    show diane f_shamed_smile
    diane "{i}*Sigh*{/i} Yeah, I'm just worried about meeting the demand is all."
    diane "I need to find a better work place soon!"
    diane "Otherwise, I might lose customers..."
    show diane f_shamed
    show player 10
    player_name "Anything I can do to help?"
    show player 5
    show diane f_shamed_smile
    diane "Hmm, I'm afraid not."
    diane "I just have to hope a vacant barn becomes available."
    show diane f_shamed
    show player 10
    player_name "It's a shame you don't have more land here. You could just build a new barn."
    show player 5
    show diane f_normal
    diane "Yeah, that would be nice, wouldn't it?"
    diane "I could design it to fit my business perfectly!"
    show diane f_thinking
    diane "... You know what?!"
    diane "You might actually be on to something {b}[firstname]{/b}..."
    show player 14
    player_name "Really?"
    show player 13
    show diane f_normal
    diane "Yeah!"
    diane "Why don't you {b}get started on the gardening{/b} and let me think on this for a while."
    show player 14
    player_name "Sure thing!"
    show player 13
    show diane f_smirk
    diane "Come and see me when you're done."
    diane "We can have some fun."
    show player 29 with dissolve
    player_name "O-okay."
    show player 3
    show diane f_laugh
    diane "Hehehe, thanks stud!"
    hide player
    show diane b_kiss_shirtless
    with dissolve
    pause
    hide diane with dissolve
    return

label garden_diane_clean_garden:
    scene expression "backgrounds/location_diane_garden_closeup.jpg"
    show player 10 with dissolve
    player_name "Oh, man..."
    player_name "How did this happen?"
    show player 184 at right with dissolve
    player_name "..."
    show player 672 with dissolve
    player_name "Yuck!"
    player_name "Everything is ruined..."
    show diane f_sad a_shovel with dissolve:
        flip
    player_name "How did this happen-"
    diane "Hi, {b}[firstname]{/b}..."
    show player 22 at Position (xoffset=-131) with dissolve
    player_name "!!!"
    show player 10f with dissolve
    player_name "{b}Diane{/b}, look!"
    show player 671f with dissolve
    show diane f_scared
    diane @ -m_talk "..."
    show player 672f
    player_name "What happened to the garden?"
    player_name "Did I screw something up?"
    show player 5f with dissolve
    show diane a_blush f_shamed_smile with dissolve
    diane "Oh no, handsome..."
    diane "This is all my fault."
    show diane a_shovel with dissolve
    diane "I went with an all natural pesticide this year and it wasn't as effective as I was hoping."
    show diane f_shamed
    show player 12f
    player_name "Pesticide?"
    show player 5f
    show diane f_shamed_smile
    diane "Yeah, you see those critters crawling all over the garden?"
    show diane f_shamed
    show player 10f
    player_name "Yeah..."
    show player 5f
    show diane f_shamed_smile a_finger with dissolve
    diane "Those are {b}earwigs{/b}."
    show diane f_shamed a_shovel with dissolve
    player_name "..."
    show player 12f
    player_name "Why do they call them earwigs?"
    show player 5f
    show diane f_laugh
    diane "Hehe, it's from an old wives tale... People used to believe earwigs would crawl into your ear and lay eggs in your brains."
    show diane f_normal
    show player 11f
    player_name "!!!"
    show player 10f
    player_name "That's not... I mean, they don't really-"
    show player 5f
    show diane f_laugh a_blush with dissolve
    diane "Hahaha! No, of course not!"
    show diane f_normal a_shovel with dissolve
    diane "They prefer moist rich soil, which is why they ended up in our garden here."
    diane "I betcha there are dozens of nests in that soil right now..."
    show player 12f
    player_name "... Gross!!!"
    player_name "So how do we fix it?"
    show player 5f
    show diane a_finger with dissolve
    diane "Hmm, well, for starters, we're gonna have to throw out all these infested crops and destroy as many nests as we can."
    diane "Then we'll need to till the soil and replant."
    diane "Making sure we use a more effective pesticide this time."
    show diane a_shovel with dissolve
    show player 14f
    player_name "Alright."
    player_name "Let's get started!"
    show player 13f
    diane "Hehe, so eager..."
    diane "I can't believe you're enjoying gardening so much!"
    show player 14f
    player_name "It's a lot of fun!"
    show player 13f
    diane "Alright, well, dig in!"
    hide player
    hide diane
    with dissolve
    jump garden_listing
    return

label dianes_garden_diane_bug_infestation:
    scene garden
    show player 10 at left with dissolve
    player_name "{b}Diane{/b}?"
    show player 4 with dissolve
    player_name "..."
    show player 12 with dissolve
    player_name "That's weird."
    player_name "She's usually waiting here to greet me."
    show player 31 with dissolve
    player_name "!!!"
    show player 32
    player_name "Oh, no!"
    player_name "What's wrong with the garden?!"
    hide player with dissolve
    return

label dianes_garden_diane_check_up_on_garden:
    scene garden
    show player 14 with dissolve
    player_name "Hey, {b}Diane{/b}!"
    player_name "How's the-"
    show player 32 at Position (xoffset=68) with dissolve
    player_name "Wow!!!"
    show player 17 with dissolve
    player_name "The garden looks great!"
    show player 14
    player_name "I can't believe everything is growing back so quickly."
    show player 30
    player_name "Hmm..."
    show player 32f with dissolve
    player_name "{b}Diane{/b} is missing again..."
    player_name "I wonder where she's hiding?"
    hide player with dissolve
    return

label dianes_garden_diane_pump_request:
    scene garden
    show player 5 at left
    show diane a_shovel
    with dissolve
    diane "{b}[firstname]{/b}!"
    show player 29 with dissolve
    player_name "Hi, {b}Diane{/b}."
    show player 3
    show diane f_laugh
    diane "Perfect timing!"
    show diane f_normal
    diane "Did {b}[deb_name]{/b} tell you about my new client?"
    show player 29
    player_name "Yeah, she said you landed a big one."
    show player 3
    show diane f_laugh
    diane "You better believe it!"
    show diane f_normal
    diane "I've got a lot of work to do before we can make the delivery."
    diane "I'm afraid I won't really have time to tend the garden..."
    show player 5 with dissolve
    player_name "..."
    diane "Think you can handle it by yourself?"
    show diane f_explain
    diane "I'll give you a bump in pay..."
    show diane f_cheese
    show player 10
    player_name "Yeah, that's fine."
    show player 5
    show diane f_normal
    diane @ -m_talk "..."
    show diane f_shamed_smile
    diane "What's the matter, handsome?"
    diane "You still thinking about the other day?"
    show diane f_shamed
    show player 12
    player_name "Yeah, I'm really sorry..."
    player_name "... That was mortifying."
    show player 11
    show diane f_laugh a_finger with dissolve
    diane "Oh, don't be silly, handsome!"
    show diane f_normal
    diane "You're a young man."
    diane "I know you can't always control those things."
    show diane a_shovel with dissolve
    show player 29 with dissolve
    player_name "Yeah, but still-"
    show player 3
    diane "Don't give it another thought, {b}[firstname]{/b}."
    show player 13 with dissolve
    player_name "..."
    diane "Alright, well, I'd best get started."
    diane "Lots of work to do!"
    diane "I'll be in the shed getting everything ready if you need me, okay?"
    show player 23
    player_name "{i}*Gasp*{/i} Is the cow in there now?"
    show player 14
    player_name "Can I pet it?!"
    show player 13
    diane "Huh?"
    show diane f_lookup
    diane "Oh, right, the cow... Uhh, no."
    show diane f_smirk
    diane @ -m_talk "..."
    diane "I'll go and visit the cow later tonight."
    show player 12
    player_name "So, what are you doing in the shed now?"
    show player 5
    show diane f_surprised_down a_blush with dissolve
    diane "I uhh..."
    show diane f_shamed_smile a_finger with dissolve
    diane "... Cleaning!"
    diane "Yeah, I have to get all the equipment sterilized and make sure all the packaging is ready."
    show diane f_shamed a_shovel with dissolve
    show player 17
    player_name "I see."
    show player 14
    player_name "Do you need any help?"
    show player 13
    show diane f_laugh
    diane "No thanks, handsome."
    diane "You just focus on the gardening for now and I'll-"
    show diane f_explain a_finger with dissolve
    diane "!!!"
    show diane f_normal
    diane "Actually, there is something you can do for me!"
    show diane a_shovel with dissolve
    show player 14
    player_name "Sure, anything."
    show player 13
    show diane f_smirk
    diane "I left {b}one of my tools on the kitchen counter{/b}."
    diane "Could you run and {b}fetch it for me{/b}?"
    show player 14
    player_name "Of course."
    player_name "I'll be right back."
    hide player
    hide diane
    with dissolve
    return

label dianes_garden_diane_delivery_2_task:
    scene garden
    show diane b_shirtless a_tired f_tired_down
    show player 14 at left
    with dissolve
    player_name "Hey, {b}Diane{/b}."
    player_name "How are you today?"
    show player 11
    player_name "!!!"
    show player 10
    player_name "Whoa, are you okay?"
    player_name "You look exhausted."
    show player 5
    show diane f_tired
    diane "Oh, yeah... I'm alright."
    diane "I just haven't gotten much sleep these past few days."
    diane "This latest delivery is killing me!"
    show player 10
    player_name "That's not good."
    player_name "Are you sure I can't help you milk the cow?"
    show player 12
    player_name "I really wouldn't mind."
    show player 5
    diane "Oh, I bet you wouldn't!"
    diane @ f_laugh "Hahahaha!"
    show player 11
    player_name "..."
    diane "Sorry, I'm a little loopy right now."
    show player 5
    diane "There's no need, stud."
    diane "I finished the order last night."
    show player 12
    player_name "Oh."
    show player 14
    player_name "Well, that's good!"
    show player 13
    diane "Would you mind going on another delivery run for me?"
    show player 14
    player_name "Yeah, sure!"
    player_name "I'd love to deliver it for you."
    show player 13
    diane "Oh, you're a lifesaver, handsome!"
    hide player
    show diane b_kiss_shirtless
    with dissolve
    pause
    show player 13 at left
    show diane b_shirtless
    with dissolve
    diane "You won't have far to go; it's for the daycare next door."
    show player 10
    player_name "Next door?"
    player_name "I think {b}Annie{/b} lives next door..."
    show player 5
    show diane f_tired_down
    diane "Hmm?"
    show player 12
    player_name "She's a girl from my class."
    show player 5
    show diane f_tired
    diane "Oh, that must be {b}Lucy's daughter{/b} then."
    show player 12
    player_name "Y-yeah, maybe..."
    show player 5
    diane "Well, if she's anything like her mother, I'm sure she's delightful!"
    show player 12
    player_name "{i}*Snort*{/i} I dunno about that."
    show player 5
    diane "Give them my regards, will you?"
    diane "I've gotta get some sleep."
    diane "Just {b}bring me the money when you're finished{/b}, okay?"
    show player 14
    player_name "Sure thing, {b}Diane{/b}."
    show player 13
    diane "Thanks, stud."
    show diane with dissolve:
        xoffset 450
    show player 10
    player_name "Wait!!"
    show player 5
    diane "Hmm?"
    show player 12
    player_name "Where's the delivery?"
    show player 5
    show diane f_tired_down
    diane @ -m_talk "..."
    show diane f_laugh
    diane "Oh, hahahahaha!!"
    diane "Yeah, you'll probably need that, huh?"
    show diane f_tired
    diane "It's in the shed."
    diane "I left it unlocked for you, handsome."
    show player 17
    player_name "Okay, I'm on it."
    show player 13
    diane "Thanks again, handsome."
    hide diane
    hide player
    with dissolve
    return

label dianes_garden_diane_d9_intro:
    scene garden
    show player 10 at left
    show diane b_shirtless a_tired f_tired
    with dissolve
    player_name "Hey, {b}Diane{/b}."
    player_name "Feeling better today?"
    show player 5
    diane "Hey, handsome."
    diane "I feel fine. Thanks for asking."
    show player 10
    player_name "... You sure? You still look really tired."
    show player 5
    diane "Heh, do I?"
    show player 10
    player_name "How much sleep did you get yesterday?"
    show player 5
    diane "I'm not sure."
    diane "I saw that note you left me about {b}Lucy{/b}'s next order and I've been trying to get a head start on production."
    diane "It's strenuous but I'm just going to have to get used to it, I guess..."
    show player 10
    player_name "What do you mean?"
    show player 5
    diane "Well, my orders aren't slowing down anytime soon."
    diane "As a matter of fact, they're getting bigger."
    show player 10
    player_name "Yeah, but-"
    show player 5
    diane "I've even got a line on another new client."
    diane "My biggest yet."
    show player 10
    player_name "{b}Diane{/b}..."
    player_name "You have to take care of yourself first..."
    player_name "Are you sure you aren't taking on too much, too quickly?"
    player_name "I worry about you."
    show player 5
    diane "Aww."
    diane "I appreciate your concern, {b}[firstname]{/b}, but you don't need to worry about me."
    diane "This business has been a dream of mine for a long time."
    diane "It'll take a lot more than a few sleepless nights to stop me from seeing it through."
    show player 10
    player_name "... Alright, just..."
    show player 14
    player_name "... Remember I'm here to help if you need it."
    show player 13
    diane "Thanks, {b}[firstname]{/b}."
    hide player
    show diane b_kiss_shirtless
    with dissolve
    pause
    show player 13 at left
    show diane b_shirtless a_tired
    with dissolve
    diane "Well, I should get back to it."
    diane "Take good care of my garden, won't you?"
    show player 14
    player_name "Of course."
    hide player
    hide diane
    with dissolve
    return

label dianes_garden_shed_light_on:
    scene expression player.location.background_blur
    show player 4 with dissolve
    player_name "( Hmm? )"
    player_name "( {b}The shed door is open and the light is on{/b}! )"
    player_name "( She can't seriously still be working, can she? )"
    hide player with dissolve
    return

label dianes_garden_diane_missing:
    scene garden
    show player 127 with dissolve
    player_name "Where's {b}Diane{/b}?"
    show player 12
    player_name "She's usually outside around this time..."
    show player 56
    player_name "She must be somewhere."
    hide player 56 with dissolve
    return

label dianes_garden_diane_daylight_drinking:
    return

label dianes_garden_diane_ready_for_day_off:
    scene garden
    show player 14 at left
    show diane b_shirtless
    with dissolve
    player_name "Hey {b}Diane{/b}!"
    player_name "You ready for your day off?"
    show player 13
    diane "Hi, {b}[firstname]{/b}."
    diane "Hehe, yeah I guess..."
    diane "I just need to finish up this last batch I was working on this morning, and-"
    show player 33
    player_name "No, no, no..."
    show player 14
    player_name "You're done working today!"
    show player 13
    diane "... But I have to make sure everything is stored away correctly."
    show player 14
    player_name "Just tell me what to do and I'll handle it."
    show player 17
    player_name "The rest of your day is all about relaxation!"
    show player 13
    show diane f_laugh a_shock with dissolve
    diane "Hahaha. Okay, okay..."
    show diane f_normal a_idle with dissolve
    diane "Just {b}head into the shed and dump what's in the pump into a storage jug{/b}."
    show player 14
    player_name "That sounds easy enough."
    show player 13
    diane "... But you have to make sure you get the cap on tight!"
    show player 14
    player_name "You just take a seat and I'll handle it, okay?"
    $ M_diane.outfit.is_naked = 0
    hide player
    hide diane
    with dissolve
    return

label dianes_garden_diane_return_drink:
    return

label dianes_garden_diane_drunken_shenanigans_apology:
    scene expression "backgrounds/location_diane_garden_closeup.jpg"
    show diane a_shovel:
        flip
        xoffset 250
    show vero b_casual:
        xoffset 100
    with dissolve
    vero "I just can't get over how good your garden is looking nowadays!"
    vero "I remember when it was just a sad little patch of tomatoes..."
    show diane f_laugh
    diane "Haha, thanks {b}Vee{/b}!"
    show diane f_normal
    diane "It certainly has come a long way..."
    vero "It's really gorgeous, {b}Diane{/b}!"
    vero "Wow!!!"
    show vero b_bending
    show diane f_down_front
    with dissolve
    pause
    show vero b_casual a_cucumber1
    show diane f_normal
    with dissolve
    vero "Look at the size of this one!"
    diane "Yeah, I know!"
    show diane f_smirk
    diane "He's a monster."
    show vero a_cucumber2 with dissolve
    vero "I'll say..."
    show diane f_normal
    diane "You wanna take him home with you?"
    show diane f_wink
    show vero f_eyeroll a_cucumber1 with dissolve
    vero "Oh my gosh, I should never have told you about that..."
    show vero f_sexy
    show diane f_laugh a_finger with dissolve
    diane "Hey, I'm not one to judge."
    show diane f_normal a_shovel with dissolve
    show vero f_sexy_down
    vero @ -m_talk "..."
    vero "No, it's way too big for me!"
    show diane f_laugh
    diane "Haha, yeah. Me too."
    show diane f_smirk
    show vero f_surprised_down
    vero "Ahaha, I knew you'd try it!"
    show vero f_sexy a_idle with dissolve
    diane "Yeah, yeah..."
    vero "So what's your secret?"
    vero "You aren't using hormones on them or anything, are you?"
    show diane f_normal
    diane "Psh, of course not!"
    diane "I remember our discussion about that."
    vero "Good."
    diane "To be honest, I've left most of the gardening to my friend this year."
    show vero f_normal
    vero "Oh, you mean that cute one you brought into the store the other day?!"
    diane "Don't get any ideas, {b}Vee{/b}!"
    diane "He's a good kid."
    vero "Yeah, so?"
    show vero f_sexy
    vero "I'm a nice girl..."
    diane "Uh huh."
    show vero f_laugh
    vero "Hehehe!"
    show vero f_sexy
    diane "His guardian would kill me if I let you get your claws on him."
    vero "Aww, c'mon."
    show diane a_finger with dissolve
    diane "Absolutely not, {b}Vee{/b}."
    show diane a_shovel with dissolve
    vero "Tsk, you're no fun."
    pause
    show vero f_thinking
    vero "... Arrghh..."
    vero "Sometimes I really regret moving to this town."
    vero "The men here suck!"
    show vero f_normal
    diane "You don't have to tell me."
    pause
    diane "You're not thinking about moving back to the farm, are you?"
    show vero f_laugh
    vero "Oh, heck no!"
    show vero f_normal
    vero "If I went back there with my tail between my legs, I'd never hear the end of it!"
    vero "{i}*Sigh*{/i}"
    vero "I can't believe I've been working at Consum-R for five years!"
    vero "It's so depressing..."
    pause
    vero "Oh, that reminds me!"
    vero "I wanted to ask you how the new business is going?"
    show diane a_blush with dissolve
    diane "Oh, uhh..."
    show diane a_shovel with dissolve
    diane "It's going well, so far."
    vero "You're still not ready to give me the details?"
    diane "Mmm, not quite yet..."
    show vero f_eyeroll
    vero "Ugh, fiiiine."
    show vero f_normal
    vero "Just don't forget about me when you start making the big bucks!"
    vero "I'm a quick learner and I'll work hard for you {b}Diane{/b}."
    diane "Heh, I know that {b}Vee{/b}..."
    diane "I just don't have enough work to warrant hiring an extra hand at the moment."
    diane "I promise I'll call you as soon as I do."
    show player 13 at left with dissolve
    vero "You had better."
    show player 14
    player_name "Hello ladies."
    show player 13
    show vero f_sexy
    vero "Uh oh, your boyfriend is here..."
    diane "Tch, shuddup {b}Vee{/b}!"
    show diane:
        unflip
        xoffset -250
    with dissolve
    diane "Ignore her, {b}[firstname]{/b}."
    vero "Oh, he knows I'm only teasing..."
    show vero f_normal
    vero "We were just talking about this beautiful garden you've been working on."
    show player 17
    player_name "It looks pretty good, huh?"
    show player 18
    vero "It looks better than good."
    vero "What's your secret?"
    show player 10
    player_name "Huh?"
    show player 5
    vero "You've gotta be doing something special to get results like this."
    show player 35
    player_name "Hmm, not really."
    show player 14
    player_name "I just till it, sow it, and water it."
    player_name "Like {b}Diane{/b} taught me."
    show player 13
    vero "That's it?"
    show player 14
    player_name "Yup."
    show player 13
    pause
    show player 35
    player_name "Oh!"
    show player 14
    player_name "I have been fertilizing it with compost..."
    show player 10
    player_name "... Maybe that's my secret?"
    show player 13
    show diane f_laugh
    diane "Hahaha!"
    show vero f_laugh
    vero "Hehe, maybe..."
    show diane f_normal
    show vero f_normal
    pause
    vero "Well, I should probably get going..."
    hide diane
    show diane a_shovel:
        flip
        xoffset 250
    with dissolve
    diane "So soon?"
    vero "Heh, yeah. Those groceries at Consum-R aren't going to sell themselves you know?"
    diane "Hah, I suppose not."
    hide vero
    show diane b_hug_vero_talk:
        xoffset 200
    with dissolve
    diane @ -m_talk "Swing by anytime, alright?"
    show diane b_dressed a_shovel:
        xoffset 250
    show vero b_casual:
        xoffset 100
    vero "Will do."
    show player 14
    player_name "Bye {b}Veronica{/b}."
    player_name "Nice seeing you again."
    show player 13
    vero "Yeah, you too handsome."
    show vero f_sexy
    pause
    vero "You know what?"
    vero "I think I'll take that cucumber after all..."
    show vero b_bending:
        flip
        xoffset 450
    show diane f_down_front
    with dissolve
    pause
    show player 426
    vero "Hmm, now where did I put it..."
    show diane f_lookup
    diane "Oh, good grief!"
    diane f_normal @ f_laugh "Haha, would you get out of here already!"
    show vero b_casual a_cucumber1:
        unflip
        xoffset 50
    with dissolve
    show player 13
    vero "Hehe, thanks again, {b}Diane{/b}!"
    hide vero with dissolve
    player_name "..."
    hide diane
    show diane a_shovel
    with dissolve
    diane "You ready to get to work, {b}stud{/b}?"
    show player 10
    player_name "Hmm?"
    show player 14
    player_name "Oh!"
    player_name "Yup, I'm ready."
    show player 13
    diane "Glad to hear it."
    show diane f_shamed_smile
    diane "... But uhh, before you get started..."
    show diane f_shamed
    show player 14
    player_name "Yeah?"
    show player 13
    show diane f_shamed_smile a_blush with dissolve
    diane "I think I should apologize."
    show diane f_shamed a_shovel with dissolve
    show player 10
    player_name "Apologize?"
    show player 5
    show diane f_shamed_smile
    diane "You know, the other day..."
    diane "... With the... Uhh..."
    diane "{i}*Ahem*{/i} I just had too much to drink and things got a little... Umm... Inappropriate."
    show diane f_shamed
    player_name "..."
    show diane f_shamed_smile
    diane "It's just been a long while since anyone has shown me that kind of attention, and I've been lonely a lot recently and-"
    diane "Ugh, no. Damn it, that's no excuse... I..."
    show diane f_sad
    diane "Look, I took advantage of you, {b}[firstname]{/b}, and I'm really sorry... I-"
    show player 14
    player_name "You didn't take advantage of me!"
    show player 13
    diane "Huh?"
    show player 17
    player_name "It was awesome!"
    player_name "I was kinda hoping we could do it again sometime?"
    show player 13
    show diane f_shamed_smile a_blush with dissolve
    diane "You wanna do it again?!"
    show diane f_shamed
    show player 26
    player_name "Of course. You're a beautiful woman, {b}Diane{/b}!"
    show player 13
    show diane f_shamed_smile a_shovel with dissolve
    diane "O-okay, but..."
    diane "{b}[deb_name]{/b} trusted me to look after you and it wasn't right of me to-"
    show diane f_shamed
    show player 14
    player_name "I'm not a child, {b}Diane{/b}. And besides, it was fun!"
    show player 13
    show diane f_shamed_smile
    diane "... And {b}[deb_name]{/b} would kill me if she found out."
    show diane f_shamed
    show player 14
    player_name "She doesn't have to know."
    show player 13
    diane @ -m_talk "..."
    show player 14
    player_name "I mean, we're just having a little fun."
    player_name "I don't see the harm in it."
    show player 13
    show diane f_shamed_smile
    diane "Hmm."
    diane "Wouldn't you rather do that stuff with girls your own age?"
    show diane f_shamed
    show player 14
    player_name "Are you kidding?!"
    player_name "You're like a million times hotter than the girls at my school, {b}Diane{/b}!"
    show player 13
    show diane f_laugh a_blush with dissolve
    diane "Oh, I am not!"
    show player 17
    player_name "Heh, it's true."
    show player 18
    show diane f_smirk a_shovel with dissolve
    pause
    show diane f_lookup
    diane "Alright, Mr. Charmer..."
    show diane f_smirk
    diane "We're clearly not in the right mindset to have this conversation."
    diane "So, let's just focus on work, shall we?"
    show player 12
    player_name "Seriously?"
    show player 5
    diane "Yes, seriously!"
    show diane f_normal
    diane "I'll be in the shed if you need something."
    show player 26
    player_name "You sure I can't give you a hand?"
    show player 13
    show diane f_laugh
    diane "Haha, no. I don't need a hand..."
    show diane f_smirk
    diane "Nice try."
    show player 14
    player_name "What?!"
    show player 13
    diane "Just get started on your garden work."
    show player 14
    player_name "Alright."
    show player 13
    hide diane with dissolve
    pause
    show player 5
    player_name "( Hmm, I hope I didn't upset her... )"
    player_name "( I should probably {b}leave her be for now, and just focus on my work in the garden{/b}. )"
    hide player with dissolve
    return

label dianes_garden_diane_do_not_disturb:
    scene expression L_map.background_blur
    player_name "I should visit {b}Diane{/b} another time..."
    return

label dianes_garden_diane_shed_still_open:
    show player 12 with dissolve
    player_name "That's strange..."
    show player 30
    player_name "{b}Diane{/b}'s shed is {b}still open{/b}..."
    hide player 30 with dissolve
    return

label drink_offered:
    scene garden
    if M_diane.get("aunt_drink_made"):
        show player 137 with dissolve
    else:

        show player 12 with dissolve
    player_name "I should {b}give Diane her drink{/b} before I get back to work..."
    $ game.main()

label aunt_masturbate_not_seen:
    show diane_masturbate 1_2
    player_name "!!!"
    player_name "( ... What is she... )"
    window hide
    pause 2
    player_name "( WOW... )"
    player_name "( She's playing with her vegetables... )"
    player_name "( A whole cucumber! )"
    player_name "( ... )"
    player_name "( I should leave before I get caught. )"
    scene garden
    with dissolve
    show player 113 with dissolve
    player_name "I can't believe I caught her masturbating!"
    show player 114
    player_name "... Or that she's horny enough to do it with veggies!"
    show player 113
    player_name "Is that why she only wants {i}long{/i} and {i}hard{/i} ones?"
    show player 109f
    player_name "Hmm..."
    show player 108f
    player_name "I guess she has been lonely lately..."
    player_name "I should get back to work and pretend I didn't see anything..."
    hide player 108f with dissolve
    $ renpy.end_replay()
    return

label find_shovel:
    scene expression game.timer.image("garden{}")
    show anon with dissolve
    if player.has_item("shovel"):
        anon "I should let {b}Diane{/b} know that I'm ready to start working."
    else:
        anon "I need to {b}find a shovel{/b} before I can help with the garden..."
    hide anon with dissolve
    $ game.main()


label before_masturbation:
    scene expression game.timer.image("garden{}")
    show player 34 with dissolve
    player_name "Hmmm..."
    show player 12
    player_name "I should find out if {b}Diane{/b} is home first."
    $ game.main()

label after_masturbation:
    scene expression game.timer.image("garden{}")
    show player 34 with dissolve
    player_name "Hmmm..."
    show player 12
    player_name "Maybe not right now."
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
