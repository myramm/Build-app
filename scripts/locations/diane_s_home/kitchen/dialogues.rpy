label dianes_kitchen_diane_look_in_kitchen:
    $ M_diane.set("sex speed",0.4)
    show diane_masturbate 1_2
    player_name "( !!! )" with hpunch
    pause
    diane "Ngghhh!"
    player_name "( {b}Diane{/b} is- )"
    player_name "( She's- )"
    pause
    player_name "( W-with a cucumber?! )"
    diane "Mmm, that's it!"
    $ M_diane.set("sex speed",0.3)
    show diane_masturbate 1_2
    player_name "( Is this really happening? )"
    diane "Fuck me harder, stud!"
    player_name "( Who is she imagining? )"
    pause
    player_name "( I'd better get out of here before she sees me. )"
    pause
    hide diane_masturbate with dissolve
    $ persistent.cookie_jar["Diane"]["unlocked"] = True
    $ persistent.cookie_jar["Diane"]["gallery"]["01_unlocked"] = True
    $ renpy.end_replay()
    return

label dianes_kitchen_diane_clean_garden_report:
    scene expression "backgrounds/location_diane_kitchen_closeup.jpg"
    show player 5f with dissolve
    player_name "..."
    show player 10f
    player_name "... Hello?!"
    show player 22f
    diane "EEEEKKK!!!" with hpunch
    player_name "!!!"
    show player 23f
    player_name "{b}Diane{/b}?!"
    show player 22f
    diane "{b}[firstname]{/b}! Help!!!"
    show player 23f
    player_name "Where are you?!"
    show player 22f
    diane "AAHHHH!!!" with hpunch
    show player 23f
    player_name "It sounds like she's upstairs!"
    hide player with dissolve
    scene black with dissolve
    scene expression "backgrounds/location_diane_bedroom_closeup.jpg"
    show diane b_pole f_scream
    show player 11 at left
    with dissolve
    diane "HELP!!!"
    show player 10
    player_name "{b}Diane{/b}?!"
    player_name "What's the mat-"
    show player 11
    diane "M-MM-MM-MOUSE!"
    show player 12
    player_name "Huh, mouse?"
    show player 14
    player_name "Is that what's got you so scared?"
    show player 13
    diane "..."
    show player 14
    player_name "Where is it?"
    show player 13
    show diane b_pole_point f_scared_back with dissolve
    diane "C-closet!"
    show diane f_scared
    show player 10
    player_name "You saw a mouse in your closet?"
    show diane b_pole with dissolve
    show player 14
    player_name "I'll check it out."
    show diane f_scared_back
    show player 108f at right with dissolve
    player_name "I don't-"
    show player 670 with dissolve
    player_name "..."
    "{i}*Thud*{/i}"
    show player 22 at left
    player_name "!!!" with hpunch
    show diane f_scream
    diane "EEEEKKK!!!"
    hide player
    show diane b_pickup
    player_name "HRRGGG!!!" with hpunch
    player_name "..."
    show diane b_pickup_scared
    diane "Was that the mouse?!"
    show diane b_pickup
    player_name "I... I don't know..."
    show diane b_pickup_talk
    diane "I hate mice!"
    show diane b_pickup_laugh
    player_name "Hehe, you deal with dirt and bugs all the time but mice freak you out?"
    show diane b_pickup_talk
    diane "YES!!!"
    show diane b_pickup_scared
    diane "Do you see it?!"
    show diane b_pickup
    player_name "Err... No?"
    show diane b_pickup_talk
    diane "I see it!"
    show diane b_pickup
    player_name "... Where?"
    show diane b_pickup_scared
    diane "RIGHT THERE!!"
    diane "See its tail?!"
    show diane b_pickup
    player_name "..."
    player_name "I think that's a shoe lace..."
    show diane b_pickup_talk
    diane "What?! NO!!!"
    show diane b_pickup_scared
    diane "That's a mouse!"
    player_name "..."
    show diane b_pickup
    player_name "It's kinda hard to see with you squeezing my head..."
    show diane b_pickup_talk
    diane "Hmm?"
    diane "Oh, I'm sorry, {b}[firstname]{/b}!"
    show diane b_pole f_scared
    show player 17 at left
    with dissolve
    player_name "Heh, it's alright."
    show player 14
    player_name "Now, let me take care of that shoe lace for you..."
    hide player with dissolve
    show diane f_scared_back
    diane "I'm telling you, it's a mouse!"
    show diane f_scream
    diane "Ugh, be careful, {b}[firstname]{/b}!!!"
    player_name "..."
    show diane f_scared
    show player 682 at left with dissolve
    player_name "..."
    show player 683
    player_name "{i}*Ahem*{/i}"
    show player 682
    show diane f_scared
    diane @ -m_talk "..."
    diane "It's a shoe lace."
    show player 683
    player_name "Heh, I told you!"
    show player 682
    show diane b_lingerie
    with dissolve
    diane "Are you sure there isn't a mouse in there?"
    show player 683
    player_name "Pretty sure."
    show player 13 at left with dissolve
    show diane f_laugh
    diane "Phew!"
    show diane f_scared
    diane "I almost had a heart attack..."
    show diane f_normal
    show player 14
    player_name "Yeah, I've never seen you so worked up before."
    player_name "You alright, now?"
    show player 13
    diane "Yeah, I think so."
    diane @ -m_talk "..."
    show player 17
    player_name "... I can't believe you were screaming at a shoe lace!"
    player_name "Hahaha!"
    show diane f_laugh
    diane "Oh, shut up!"
    show diane f_normal
    show player 13
    show diane f_surprised_front
    pause
    show diane a_cover with dissolve
    diane "... I'm... Naked..."
    show diane f_shamed
    show player 10
    player_name "Well, not really naked..."
    show player 5
    diane "I might as well be."
    diane "I'm sorry, {b}[firstname]{/b}."
    diane "I'm embarrassed."
    show player 10
    player_name "Hmm?"
    player_name "There's no need to be embarrassed..."
    show player 14
    player_name "You look fantastic!"
    show player 13
    show diane a_shock f_laugh
    with dissolve
    diane "{b}[firstname]{/b}!!!"
    show diane f_smirk
    show player 17
    player_name "What? You do."
    show player 13
    show diane a_idle with dissolve
    diane "{b}[deb_name]{/b} would throw a fit if she knew you saw me like this."
    show player 14
    player_name "Well, I'm not going to tell her..."
    show player 13
    diane @ -m_talk "..."
    show diane f_normal
    diane "You really think I look good?"
    show player 14
    player_name "Of course!"
    player_name "You're beautiful!"
    show player 13
    diane @ -m_talk "..."
    hide player
    show diane b_lingerie_kiss
    with dissolve
    diane "You're so sweet!"
    show player 13 at left
    show diane b_lingerie f_smirk
    with dissolve
    diane "Thank you, handsome!"
    player_name "..."
    diane "I should finish getting dressed."
    diane "You wanna go with me to pick up the {b}pesticide{/b}?"
    player_name "Y-yeah, okay."
    show diane f_laugh
    diane "Great!"
    show diane f_smirk
    diane "You should wait downstairs."
    diane "I'll just be a minute or two."
    hide player
    hide diane
    with dissolve
    scene expression "backgrounds/location_diane_kitchen_closeup.jpg"
    show player 13f at right
    with dissolve
    player_name "( Wow, I can't believe I got to see {b}Diane{/b} like that! )"
    player_name "( She has such a great body! )"
    show diane b_casual f_smirk:
        flip
    with dissolve
    diane "Ready to go, stud?"
    show player 11f
    player_name "!!!"
    show player 14f
    player_name "Y-yeah..."
    player_name "Nice outfit!"
    show player 13f
    show diane f_laugh
    diane "Heh, thanks!"
    show diane f_normal
    diane "We should be able to {b}find the pesticide we need at Consum-R{/b}."
    show player 14f
    player_name "Alright, let's go."
    hide player
    hide diane
    with dissolve
    return

label dianes_kitchen_diane_mouse_attack_started:
    scene dianekitchen with None
    show player 10 with dissolve
    player_name "Weird. She's not in here either."
    player_name "( I thought for sure... )"
    show player 11
    diane "EEEEEEKKKKKKK!"
    show player 23f
    player_name "What the..."
    player_name "( Is that {b}Diane{/b} screaming?! )"
    hide player with dissolve
    return

label dianes_kitchen_diane_drunken_splur_not_known:
    scene dianekitchen1
    player_name "( There's no one here. )"
    player_name "( {b}Diane{/b} is outside by the garden. )"
    return

label mouse_attack:
    scene dianekitchen with None
    show player 10 with dissolve
    player_name "( I can't just leave, {b}Diane{/b} might be in trouble. )"
    hide player with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
