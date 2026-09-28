label dianes_shed_diane_delivery_2_fetch_goods:
    scene shed
    show player 14 with dissolve
    player_name "Whoa!!!"
    player_name "Look at all the milk jugs!"
    show player 4 with dissolve
    player_name "..."
    show player 12 with dissolve
    player_name "Did {b}Diane{/b} really fill all of those by herself?!"
    player_name "It would take forever, especially if she's hauling them out to the cow one by one..."
    show player 4 with dissolve
    player_name "Hmm."
    show player 33 with dissolve
    player_name "Well, I guess it explains why she spends so much time in here."
    show player 13
    player_name "..."
    show player 14
    player_name "I should {b}get started with the delivery{/b}."
    hide player with dissolve
    return

label dianes_shed_diane_fetch_pump:
    show player 35 at left with dissolve
    player_name "Woah..."
    show player 34
    player_name "... What a strange looking shed."
    player_name "What's up with all the containers... And those chains?!"
    show player 43
    player_name "Anyway, let's try and {b}find that pump{/b}..."
    hide player 43 with dissolve
    return

label dianes_shed_milking_help:
    scene expression "backgrounds/location_diane_shed_closeup.jpg"
    $ M_diane.outfit.is_naked = 1
    show player 10 at left
    show diane b_topless_blank a_pump1 f_surprised_front
    with dissolve
    player_name "{b}Diane{/b}?!"
    player_name "What's going on in here?"
    player_name "Are you okay?"
    show player 5
    show diane f_sad
    diane "Arrgh, no!"
    diane "I'm clogged up again and this stupid pump is stuck!"
    show player 10
    player_name "Clogged up?"
    show player 5
    diane @ -m_talk "..."
    show player 10
    player_name "So wait, you can't get it off?"
    show player 5
    show diane f_surprised_down a_pump_stuck with dissolve
    pause
    show diane f_scream
    diane "{i}*Iiitthhh*{/i} This really hurts!"
    show diane a_pump1 f_tired_down with dissolve
    show player 10
    player_name "Here, let me see it."
    show player 5
    show diane f_sad
    diane "No!"
    diane "I can do it."
    show diane f_surprised_down a_pump_stuck with dissolve
    pause
    show diane a_pump1 f_scream with dissolve
    diane "Arrghh!"
    show diane f_tired_down
    show player 10
    player_name "C'mon, {b}Diane{/b}..."
    player_name "... Just let me help."
    show player 5
    show diane f_sad
    diane "Fine."
    show diane f_surprised_front
    show player 670b at Position (xoffset=100)
    with dissolve
    pause
    show diane f_surprised_down
    diane "Just, please be careful."
    show diane f_surprised_front
    player_name "I will, I promise."
    pause
    player_name "Hmm."
    show player 670c zorder 1 at Position (xoffset=46)
    show diane f_surprised_down a_pump_stuck
    with dissolve
    pause
    player_name "Got it!"
    show player 13
    show diane a_ouch f_surprised_front
    with dissolve
    diane "Oh, thank goodness!"
    player_name "Are you alright?"
    diane "Phew, I'm a lot better now that you got that stupid pump off me."
    show diane b_topless a_idle f_smirk with dissolve
    diane "Thank you, {b}[firstname]{/b}."
    show player 429
    player_name "You're welcome."
    show player 426
    pause
    show player 14
    player_name "You mentioned something about a clog?"
    show player 13
    diane @ -m_talk "Hmm?"
    show diane f_sad
    diane "Oh, yeah..."
    diane "... It's something that happens to lactating women occasionally."
    diane "A duct gets backed up and becomes inflamed."
    show player 10
    player_name "Oh, that sounds complicated."
    player_name "Should I get you to the clinic?"
    show player 5
    show diane f_laugh
    diane "Oh, heavens no!"
    diane "It's nothing so serious as that."
    show diane f_smirk
    show player 10
    player_name "Oh."
    player_name "Well, how do we fix it?"
    show player 5
    diane a_ouch b_topless_blank "I usually just put on a hot compress on and massage it."
    show diane a_idle b_topless with dissolve
    show player 12
    player_name "So, massaging can unclog it?"
    show player 5
    diane "Yeah, if you know what you're doing."
    show player 429
    player_name "Will you show me?"
    show player 426
    show diane f_surprised
    diane @ -m_talk "..."
    show diane f_shamed_smile
    diane "I'm not sure that's a good idea."
    show diane f_shamed
    show player 10
    player_name "I'd like to help, {b}Diane{/b}."
    player_name "Please, let me."
    show player 5
    show diane f_smirk
    diane @ -m_talk "..."
    show diane f_explain
    diane "Yeah, okay."
    show diane a_ouch b_topless_blank f_smirk
    show player 426
    with dissolve
    diane "Just press in here with your thumb and knead downward towards my nipple."
    show player 17
    player_name "Alright."
    hide player
    show diane b_topless_blank2 a_waiting f_down_front
    with dissolve
    pause
    show diane a_squeeze1 with dissolve
    player_name "Like this?"
    diane f_explain a_squeeze @ a_squeeze1 f_shamed_look "Try a little more pressure."
    pause
    diane "Yeeeah, just like that."
    pause
    diane "Mmm."
    diane "Seems like my breasts are always sore nowadays."
    player_name "That's not good, {b}Diane{/b}."
    show diane f_laugh
    diane "Heh, yeah I know."
    show diane f_explain
    diane "I need to find better equipment."
    show diane f_lip_bite
    pause
    player_name "Is this helping?"
    show diane f_explain
    diane "Ahh, definitely..."
    diane "... Your hands feel amazing, {b}[firstname]{/b}!"
    show diane f_down_front
    pause
    show diane f_explain
    diane "You sure you haven't done this before?"
    show diane f_lip_bite
    pause
    player_name "How will I know when it's fixed?"
    show diane f_laugh a_squeeze_milk
    diane "Haaah!" with hpunch
    show diane f_down_front
    pause
    show diane a_squeeze1 with dissolve
    player_name "Oh!"
    show diane a_squeeze_milk with dissolve
    player_name "Heh, nevermind."
    show diane f_laugh
    diane "Haaah... Haaah..."
    diane "Phew, thank you!"
    show player 83b at left
    show diane b_topless a_idle f_smirk
    with dissolve
    player_name "Hehe, you're welcome!"
    player_name "I'm just happy I could help you for once."
    show player 83c
    diane "But you do help me, {b}[firstname]{/b}..."
    diane "... My garden has never-"
    show diane f_surprised_down
    diane "!!!"
    pause
    show player 83
    player_name "Never?"
    show player 82
    show diane f_smirk
    diane @ -m_talk "Hmm?"
    show player 83
    player_name "You were saying something about your garden."
    show player 82
    show diane f_teasing_look
    diane "Was I?"
    diane "I completely forgot."
    show diane f_smirk
    show player 83b
    player_name "Heh, sorry."
    show player 83c
    diane "No, it's alright {b}[firstname]{/b}..."
    show diane f_teasing_look
    diane "... I just-"
    show player 78
    show diane b_jerk_pre f_down_front
    player_name "!!!" with hpunch
    hide player
    show diane b_jerk2:
        xoffset -110
    with dissolve
    player_name "{b}Diane{/b}?"
    player_name "I thought you didn't want to-"
    show diane f_teasing_look
    diane "I know."
    diane "Truthfully, I'm not sure what I want..."
    show diane b_jerk f_down_front
    player_name "That feels really good."
    pause
    show diane f_smirk_up
    diane "... You promise you won't tell {b}[deb_name]{/b}?"
    player_name "Oh, I promise!"
    pause
    show diane b_jerk2
    diane "You wanna try my milk again?"
    show diane f_down_front
    player_name "Hmm?"
    player_name "Umm, yeah... Okay, sure."
    pause
    show diane b_topless a_idle f_smirk:
        xoffset 0
    show player 10 at left
    with dissolve
    player_name "Should I get the pump?"
    show player 5
    diane "No."
    diane "I thought, maybe you'd like to..."
    diane "... You know, try it directly from the tap?"
    pause
    show player 10
    player_name "You mean-"
    show player 29 with dissolve
    player_name "Y-yeah, definitely!"
    show player 3
    show diane a_invite with dissolve
    diane "Come sit here."
    show player 29
    player_name "On your lap?"
    show player 3
    diane "Mmmhmm."
    diane "Don't be shy."
    show player 29
    player_name "O-okay."
    hide player
    hide diane
    with dissolve

    scene expression "backgrounds/location_diane_shed_hay_stack.jpg"
    show diane b_hay_feeding_shirtless1 f_explain
    with dissolve
    diane "Go ahead, handsome."
    show diane b_hay_feeding_shirtless f_lip_bite
    diane "Mmm."
    pause
    show diane f_explain
    diane "Oh my god, that feels so good!"
    pause
    diane "How's it taste?"
    show diane f_lip_bite
    player_name "Delicious!"
    show diane f_laugh
    diane "Hehe!"
    diane a_shirtless_stroke f_shamed_look "You've got such a nice dick, {b}[firstname]{/b}."
    diane "Have I mentioned that before?"
    show diane f_smirk_down
    player_name "Heh, yeah."
    show diane f_laugh
    diane "Haha!"
    show diane f_lip_bite
    pause
    show diane f_explain
    diane "Mmm, oh yeah... Keep doing that with your tongue."
    diane "Your mouth feels amazing on my nipple!"
    show diane f_lip_bite
    pause
    show diane b_hay_feeding_shirtless1 with dissolve
    diane "Nngghh!"
    show diane f_shamed_look
    diane "Alright, we'd better stop before you drink me dry, stud."
    show diane f_smirk_down
    player_name "Aww."
    show diane f_explain
    diane "I know..."
    hide diane with dissolve
    $ M_diane.outfit.is_naked = 1
    scene expression player.location.background_blur with None
    show player 13 at left
    show diane b_topless f_smirk
    with dissolve
    diane "... We'll do it again another day, alright?"
    show player 14
    player_name "Yeah, okay."
    show player 13
    diane "You can't be too greedy though."
    show diane f_laugh
    diane "Remember, I've got a business to run!"
    show diane f_smirk
    show player 17
    player_name "Heh, I know."
    show player 13
    diane "Now get your cute butt back to work!"
    show player 14
    player_name "Yes, ma'am!"
    hide player
    hide diane
    with dissolve
    return

label dianes_shed_diane_check_shed_light:
    scene expression "backgrounds/location_diane_shed_closeup.jpg"
    show diane b_topless_blank a_pump f_tired
    diane @ -m_talk "..."
    diane "{i}*Yawn*{/i}"
    show diane f_tired_down
    pause
    player_name "{b}Diane{/b}??"
    show player 10 at left with dissolve
    player_name "Are you in here?"
    show player 14
    player_name "I brought you some-"
    show player 23
    player_name "{i}*Gasp*{/i}"
    show diane f_sad
    diane "{b}[firstname]{/b}!!!" with hpunch

    scene location_diane_garden_cutscene08
    show text _ ("I couldn't believe what I was seeing!\n{b}Diane's{/b} breasts were fully exposed and she was holding the milker to her nipple!") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("Is this what she'd been doing in the shed the entire time?!") as caption with dissolve
    pause

    scene expression "backgrounds/location_diane_shed_closeup.jpg"
    show diane b_topless a_covering f_surprised
    show player 428 at left
    with fade
    player_name "!!!"
    diane f_sad "What are you-"
    show player 10
    player_name "... Is that..."
    player_name "You're..."
    show player 11
    show diane f_scared
    diane @ -m_talk "..."
    show player 12
    player_name "Why are you using the cow's breast pump on yourself?"
    show player 5
    show diane f_sad
    diane "I'm sorry, I never meant for you to... Wait, what?!"
    diane @ -m_talk "..."
    diane "{b}[firstname]{/b}, there is no cow."
    show player 10
    player_name "... There is no cow?"
    player_name "But then, where is all that milk-"
    show player 11
    pause
    show player 37 with dissolve
    player_name "... Oh."
    show player 38 with dissolve
    player_name "OOOH!!!"
    player_name "You mean, all of this was-"
    show player 3 with dissolve
    diane "It's breast milk."
    diane "It's MY breast milk."
    show player 11 with dissolve
    player_name "!!!"
    show player 17
    player_name "That's so awesome!"
    show player 18
    show diane f_shamed_smile
    diane "... Awesome?"
    show diane f_shamed
    show player 14
    player_name "Yeah!!"
    player_name "I had no idea people could make this much!"
    show player 13
    show diane f_shamed_look
    diane "Uhh..."
    show diane f_shamed
    show player 22
    player_name "{i}*Gasp*{/i}"
    show player 14
    player_name "I just realized!"
    player_name "... {b}Tony{/b}'s making pizza with milk from your boobs!!"
    show player 17
    player_name "That's so cool!"
    show player 13
    show diane f_shamed_smile
    diane "Hehe, I really didn't think you would take it this well..."
    diane "It doesn't bother you?"
    show diane f_shamed
    show player 12
    player_name "No, why would it?"
    show player 13
    diane @ -m_talk "..."
    show player 14
    player_name "Can I try some?"
    show player 13
    show diane f_surprised_front
    diane "You wanna try some?!"
    show diane f_shamed_smile
    diane "Really?"
    show diane f_shamed
    pause
    show diane f_shamed_smile
    diane "Umm, sure. I guess..."
    show diane f_shamed a_milk_cover with dissolve
    pause
    show diane a_covering
    show player 104
    with dissolve
    pause
    show player 105 with dissolve
    pause
    show player 34 with dissolve
    player_name "Hmm."
    show diane f_shamed_smile
    diane "What do you think?"
    show diane f_shamed
    show player 33
    player_name "It's really creamy!"
    show player 34
    pause
    show player 33
    player_name "... And it's kinda got a... Sweetness to it."
    show player 34
    pause
    show player 14
    player_name "I like it!"
    show player 13
    show diane f_shamed_smile
    diane "You do?"
    show diane f_shamed
    show player 14
    player_name "Yeah."
    player_name "I can't believe you've been making all this yourself!"
    show player 13
    show diane f_laugh
    diane "Heh, yeah. It hasn't been easy."
    show diane f_shamed_smile
    diane "I've been milking myself around the clock for weeks now..."
    show diane f_shamed
    show player 14
    player_name "Oh, right!"
    player_name "{b}[deb_name]{/b} sent you this."
    show player 239_240 with dissolve
    pause
    show player 674 with dissolve
    player_name "She's worried you aren't eating enough."
    show player 673
    show diane f_shamed_smile
    diane "Oh, is that apple?"
    show diane f_shamed
    player_name "Mmmhmm."
    show diane f_shamed_smile
    diane "It looks delicious!"
    show diane f_tired
    diane "And she's right, I haven't eaten all day."
    show player 675
    player_name "That's not good, {b}Diane{/b}..."
    player_name "You've gotta take care of yourself!"
    show player 676
    diane "{i}*Sigh*{/i} I know, I'm pushing myself too hard."
    show player 674
    player_name "How about the next time I come over, you take the day off?"
    show player 673
    show diane f_sad
    diane "A whole day?"
    show diane f_tired
    diane "I dunno..."
    show player 674
    player_name "Oh, c'mon!"
    player_name "I'll take care of the garden and get you anything you need."
    player_name "You can just lay back and relax."
    player_name "Doesn't that sound nice?"
    show player 673
    diane "Hmm."
    show diane f_shamed_smile
    diane "It does sound really nice..."
    show diane f_shamed
    show player 674
    player_name "It's a date then!"
    show player 673
    show diane f_surprised
    diane "!!!"
    show diane f_shamed_smile
    diane "You're so sweet, {b}[firstname]{/b}."
    show diane f_shamed
    show player 674
    player_name "It's no problem at all."
    show player 673
    show diane f_shamed_smile
    diane "You're not gonna tell anybody, are you?"
    show diane f_shamed
    show player 676
    player_name "Hmm?"
    show diane f_shamed_smile
    diane "You know, about the milk..."
    show diane f_shamed
    show player 674
    player_name "Oh, no. I won't tell anybody."
    show player 673
    show diane f_shamed_smile
    diane "Thank you, handsome!"
    show diane f_shamed
    show player 674
    player_name "Now, let's get inside and eat {b}[deb_name]{/b}'s warm pie!"
    show diane f_lookup
    diane "Phew!"
    show diane f_shamed_smile
    diane "I was so worried you'd think it was gross..."
    diane "... Or that I was a terrible person."
    show diane f_shamed
    show player 674
    player_name "Not at all!"
    show player 673
    show diane f_shamed_smile
    diane "I was using cows originally but my breast milk has been such a hit..."
    show diane f_shamed
    show player 674
    player_name "Yeah, it tastes really good!"
    player_name "I'm not surprised they like it so much."

    scene expression "backgrounds/location_diane_front_night_blur.jpg" with fade
    show player 13 with dissolve
    player_name "( Wow, she was nodding off the entire time she ate. )"
    player_name "( I barely managed to get her in bed. )"
    player_name "( It's hard to believe all that milk came from {b}Diane{/b}. )"
    show player 18
    player_name "( That's so cool! )"
    show player 13
    player_name "( She's working herself to the bone though! )"
    player_name "( ... Maybe, I can help her get a better routine going? )"
    player_name "( For now though, I'll just have to make sure her day off is really special and that she gets plenty of rest. )"
    hide player with dissolve
    return

label dianes_shed_seen_shed_locked:
    if M_diane.between_states(S_diane_bug_infested_garden, S_diane_clear_bug_infested_garden):
        scene expression game.timer.image("location_diane_garden_dead{}_blur")
    else:
        scene expression player.location.background_blur
    show player 34 with dissolve
    player_name "Hmm..."
    show player 35
    player_name "The door's locked."
    hide player 35 with dissolve
    return

label dianes_shed_not_seen_shed_locked:
    if M_diane.between_states(S_diane_bug_infested_garden, S_diane_clear_bug_infested_garden):
        scene expression game.timer.image("location_diane_garden_dead{}_blur")
    else:
        scene expression player.location.background_blur
    show player 35 with dissolve
    player_name "Hmm... The shed is locked. I wonder what's in there?"
    hide player
    hide diane
    with dissolve
    return

label dianes_shed_dewitt_paint:
    scene location_diane_shed01_night_closeup
    show player 588
    with dissolve
    player_name "Finally found the paint!"
    player_name "If I {b}bring this and some lumber to the work bench in the garage{/b}, I can make a fake guitar, no problem."
    hide player with dissolve
    $ M_dewitt.trigger(T_dewitt_shed_find_paint)
    $ player.get_item("paint")
    call popup ('give', 'paint')
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
