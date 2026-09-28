label pool_banned_from_pool_day:
    scene pool
    show player 108f at left with dissolve
    player_name "( I can't stay here. )"
    player_name "( I've been {b}banned{/b} from the pool grounds. )"
    show player 34
    player_name "Hmm..."
    show player 35
    player_name "( Maybe I should come back when {b}nobody is around{/b}... )"
    hide player with dissolve
    return

label pool_cassie_after_fun:
    scene pool
    if wearing_swimsuit:
        show player 53f at left with dissolve
    else:
        show player 1 at left with dissolve
    show ronda b_swim f_upset with dissolve
    ronda "That took you long enough..."
    if wearing_swimsuit:
        show player 51f
    else:
        show player 11
    player_name "..."
    if wearing_swimsuit:
        show player 45
    else:
        show player 21
    player_name "What do you mean?"
    if wearing_swimsuit:
        show player 51f
    else:
        show player 13
    ronda "... Really?"
    ronda "You think I'm stupid?"
    if wearing_swimsuit:
        show player 45
    else:
        show player 21
    player_name "... What?"
    if wearing_swimsuit:
        show player 53f
    else:
        show player 13
    ronda "You just spent an hour in the medic room with {b}Cassie{/b}."
    if wearing_swimsuit:
        show player 45
    else:
        show player 21
    player_name "... And?"
    if wearing_swimsuit:
        show player 53f
    else:
        show player 13
    ronda "Your dramatic performance in the pool earlier, flashing everybody with your... Boner..."
    if wearing_swimsuit:
        show player 45
    else:
        show player 21
    player_name "What are you trying to say?"
    if wearing_swimsuit:
        show player 51f
    else:
        show player 11
    ronda "Everybody knows {b}Cassie{/b} brings guys she likes in her medic room!!!"
    if wearing_swimsuit:
        show player 45
    else:
        show player 37
    player_name "You think she likes me?"
    if wearing_swimsuit:
        show player 51f
    else:
        show player 11
    ronda f_upset_angry "OMG! Stop playing stupid with me!"
    ronda "You don't think she was impressed with your giant cock?!"
    ronda "It's the only reason she took you {i}in there{/i}!!!"
    show ronda f_upset
    if wearing_swimsuit:
        show player 45
    else:
        show player 21
    player_name "... You think my penis is big?"
    if wearing_swimsuit:
        show player 51f
    else:
        show player 22
    ronda f_upset_angry "!!!"
    ronda "That's not-"
    ronda "I ain't saying that!"
    show ronda f_upset
    if wearing_swimsuit:
        show player 51f
    else:
        show player 11
    player_name "..."
    ronda "She's a total slut, okay?"
    if wearing_swimsuit:
        show player 50f
    else:
        show player 17
    player_name "... She was very nice to me, actually."
    if wearing_swimsuit:
        show player 51f
    else:
        show player 11
    ronda @ f_eyeroll "Ugh. You pig..."
    hide player
    hide ronda
    with dissolve
    return

label pool_banned_from_pool_night:
    scene pool_night
    show player 14 at left with dissolve
    player_name "( There we go! )"
    show player 17
    player_name "( I can finally swim in peace! )"
    show player 11
    player_name "{i}*Splashing*{/i}"
    show player 90
    player_name "..."
    show player 127
    player_name "( Is someone in the pool? )"
    player_name "( I can't see that well in the dark... )"
    hide player with dissolve
    scene pool_night02
    with dissolve
    scene pool_night03
    with Dissolve(0.2)
    scene pool_night04
    with Dissolve(0.2)
    scene pool_night05
    with Dissolve(0.2)
    show player 17 at left with dissolve
    player_name "( I guess I wasn't the only one with this idea! )"
    player_name "( I'm going in, too! )"
    show player 8
    player_name "Here I come!!"
    return

label pool_closed_night:
    scene pool_night
    if wearing_swimsuit:
        show player 49f with dissolve
    else:
        show player 2 with dissolve
    player_name @ -m_talk "( The {b}pool{/b} is closed. I don't think I can swim right now. )"
    hide player with dissolve
    return

label poolrules01_dialogue_pre:
    if wearing_swimsuit:
        show player 53f at left
    else:
        show player 1 at left
    show cassie 1 at right
    with dissolve
    cassie "{i}*WHISTLE*{/i}"
    if wearing_swimsuit:
        show player 51f
    else:
        show player 22
    player_name "!!!"
    show cassie 2
    if wearing_swimsuit:
        show player 51f
    else:
        show player 11
    cassie "Hey!"
    cassie "You can't go in the pool dressed like that!"
    cassie "You have to change, first!"
    return

label poolrules01_dialogue_after:
    if wearing_swimsuit:
        show player 51f
    else:
        show player 29
    show cassie 4
    player_name "Sorry! It's my first time here..."
    if wearing_swimsuit:
        show player 51f
    else:
        show player 13
    show cassie 2
    cassie "Just use one of the {b}three changing rooms{/b}..."
    show cassie 3
    cassie "... And if you don't have a {b}swimsuit{/b}, then I can't let you in!"
    show cassie 4
    if wearing_swimsuit:
        show player 50f
    else:
        show player 17
    player_name "Right! Gotcha!"
    return

label poolrules02_dialogue:
    if wearing_swimsuit:
        show player 53 at left
    else:
        show player 1 at left
    show cassie 1 at right
    with dissolve
    cassie "{i}*WHISTLE*{/i}"
    if wearing_swimsuit:
        show player 51f
    else:
        show player 22
    player_name "!!!"
    show cassie 2
    if wearing_swimsuit:
        show player 51f
    else:
        show player 11
    cassie "Hey! {b}[firstname]{/b}!!"
    cassie "Did you forget to change again?"
    cassie "You know you have to change first..."
    if wearing_swimsuit:
        show player 51f
    else:
        show player 29
    show cassie 4
    player_name "Oh, hey, {b}Cassie{/b}!"
    player_name "Sorry, I forgot!"
    if wearing_swimsuit:
        show player 51f
    else:
        show player 13
    show cassie 2
    cassie "You should use the medic room... No one else is using it..."
    show cassie 4
    if wearing_swimsuit:
        show player 50f
    else:
        show player 17
    player_name "Okay! Thanks..."
    return

label pool_cutscene01:
    $ M_player.set("first swim", False)
    call expression game.dialog_select("pool_cutscene01_dialogue")
    $ changing_count = 0
    return

label pool_cutscene01_dialogue:
    scene poolcutscene01
    show text _ ("It's my first time in the pool since I was in grade school.\nI'm only a few laps into my training and I'm tired!\nOnly a few more laps...") as caption
    with fade
    pause

    scene poolcutscene01b
    show text _ ("What's happening...\nI don't have the strength... So heavy...\nI can't-") as caption
    with fade
    pause
    return

label pool_cutscene02:
    scene poolcutscene01
    show text _ ("It's not my first time in the pool anymore, and I've learned to pace myself.\nI'm able to do a few laps without issues and finish my training!") as caption
    with fade
    pause
    return

label ronda_after_swimming:
    scene pool
    show player 46 at left
    show ronda b_swim
    with dissolve
    ronda "Not bad!"
    ronda "At least you didn't drown this time..."
    show player 47
    player_name "Uhh... Thanks?"
    show player 48
    ronda f_upset "Don't be too flattered. I've seen dogs swim better..."
    hide player
    hide ronda
    with dissolve
    return

label poolrules03_dialogue:
    scene pool
    if wearing_swimsuit:
        show player 53f at left
    else:
        show player 1 at left
    show cassie 1 at right
    with dissolve
    cassie "{i}*WHISTLE*{/i}"
    if wearing_swimsuit:
        show player 51f
    else:
        show player 22
    player_name "!!!"
    show cassie 2
    if wearing_swimsuit:
        show player 51f
    else:
        show player 11
    cassie "Hey!"
    cassie "That's the medic room!"
    cassie "You can't go in there. It's for staff only."
    if wearing_swimsuit:
        show player 51f
    else:
        show player 29
    show cassie 4
    player_name "Sorry! It's my first time here..."
    if wearing_swimsuit:
        show player 51f
    else:
        show player 13
    show cassie 2
    cassie "Just use one of the {b}three changing rooms{/b}..."
    show cassie 4
    if wearing_swimsuit:
        show player 50f
    else:
        show player 17
    player_name "Right! Gotcha!"
    hide player
    hide cassie
    with dissolve
    $ game.main()

label changing_dialogue_wearing_swimsuit:
    show player 45 with dissolve
    player_name "Uhm..."
    player_name "( I've already changed... I don't need to be here. )"
    hide player 45 with dissolve
    return

label changing_dialogue_occupied_pre:
    if rand_girl not in used_changing_girls:
        show expression "changing {}".format(rand_girl) as rand_girl_img at right with dissolve
        show player 1 at left with dissolve
        window hide
        pause
        show player 23 with hpunch
        player_name "..."
        hide rand_girl_img
        show expression "changing {}b".format(rand_girl) at right
    else:
        jump expression game.dialog_select("changing_dialogue")
    return

label changing_dialogue_occupied_after:
    if rand_girl == 1:
        emma "Hey! Get out of here!!!"

    elif rand_girl == 2:
        sue "What are you doing, you creep?!"

    elif rand_girl == 3:
        olivia "Hey, you should buy me a drink first!"

    elif rand_girl == 4:
        ivy "Hey, you should buy me a drink first!"

    elif rand_girl == 5:
        amelie "Hey! Get out of here!!!"

    elif rand_girl == 6:
        sammy "What are you doing, you creep?!"

    show player 42
    player_name "Oops!"
    player_name "... Sorry!"
    hide player with dissolve
    return

label changing_dialogue_change:
    show player 43 with dissolve
    player_name "Finally! A free room!"
    show player 35
    player_name "( They should really add signs to let you know when it's busy... )"
    show player 8
    window hide
    pause
    hide player 8
    show player 44
    player_name "( There we are! All ready! )"
    hide player with dissolve
    return

label changing_caught:
    scene changeroom01
    show player 5f at right
    show cassie 61 at left
    with dissolve
    cassie "What's going on in here?!"
    show cassie 60
    show player 22f
    player_name "!!!"
    show cassie 59
    show player 13f
    cassie "{b}You{/b} again?!"
    cassie "I just got a harassment complaint-"
    show cassie 60
    show player 10f
    player_name "No, it's not what it looks like!!"
    show player 11f
    show cassie 59
    cassie "To me, it looks like you're trying to watch girls changing..."
    show player 10f
    show cassie 60
    player_name "I was just trying to find a room-"
    show player 5f
    show cassie 59
    cassie "And you didn't think to check first??"
    show player 10f
    show cassie 60
    player_name "But, there's no door to knock on-"
    show player 11f
    show cassie 59
    cassie "Save your excuses for someone else."
    show player 23f with hpunch
    cassie "You're {b}banned from the pool grounds{/b}."
    show player 10f
    show cassie 60
    player_name "What?!"
    player_name "But I need to train for my school trial-"
    show player 5f
    show cassie 61
    cassie "And that's my problem, how?"
    cassie "I'm gonna have to ask you to {i}leave now{/i}."
    show player 10f
    show cassie 60
    player_name "..."
    hide player
    hide cassie
    with dissolve
    return

label pool_banned_from_pool_night_swim:
    scene pool_water_night
    show cassie 62 zorder 2 at right
    with fade
    window hide
    pause
    show player 115 zorder 1 at Position(xpos = 230, ypos = 470) with Dissolve(0.3)
    window hide
    show player 116 zorder 1 at left
    show cassie 63 zorder 2
    with Dissolve(0.4)
    cassie "!!!"
    show player 123 with dissolve
    player_name "OH! SHIT!"
    show cassie 73
    player_name "You're {i}naked{/i}?!"
    show cassie 67
    show player 125
    cassie "WHAT ARE YOU DOING HERE?!"
    show player 120
    show cassie 73
    player_name "Hey! You're the lifeguard who works here during the day!"
    show player 121
    show cassie 72
    cassie "..."
    show player 124
    show cassie 67
    cassie "Wait... You're that pervert spying on the girls!"
    show player 125
    cassie "Didn't I say you're not allowed here anymore?!"
    show player 120
    show cassie 66
    player_name "Hey!! That's NOT what I was doing!"
    show player 126
    player_name "And I'm not allowed here during the day, so I had to come at night!"
    show player 120
    player_name "... Wait a second..."
    show cassie 73
    player_name "What are {i}YOU{/i} doing here naked at night anyway?!"
    show player 121
    show cassie 64
    cassie "I... Ugh... Just don't tell anyone!"
    show player 124
    cassie "We can both get in trouble for being here after hours..."
    show cassie 65
    show player 126
    player_name "Well... I won't tell anyone but you have to let me train again!"
    show cassie 64
    show player 122
    cassie "Ugh... Just get me a towel..."
    show cassie 65
    show player 118
    window hide
    pause
    show player 119
    player_name "Here."
    show player 117
    show cassie 68
    with dissolve
    cassie "Thanks."
    show cassie 69
    cassie "..."
    show player 124
    show cassie 68
    cassie "Sorry about kicking you out of the pool grounds..."
    cassie "I'll let you in next time, I promise."
    show player 122
    show cassie 70
    player_name "Sweet! Thanks!"
    player_name "I'll do a few laps now If you don't mind."
    show player 124
    show cassie 71
    cassie "Are you crazy?! We're both leaving now before someone sees us!"
    show player 126
    show cassie 70
    player_name "Okay, okay!"
    hide cassie
    hide player
    with dissolve
    return

label pool_rescued_dialogue:
    scene rescued
    show cassie 6 at Position (xpos = 564, ypos = 768) with dissolve
    cassie "OKAY, LISTEN EVERYONE!!!"
    cassie "YOU HAVE TO MAKE SOME ROOM!"
    show cassie 7
    cassie "I have to perform CPR!"
    show cassie 8
    window hide
    pause
    show cassie 8
    cassie "Okay, this should work..."
    show cassie 9
    window hide
    pause
    show cassie 8
    cassie "Come on..."
    show cassie 9
    window hide
    pause
    show cassie 10
    window hide
    pause
    show cassie 11
    window hide
    pause
    show cassie 12 with hpunch
    window hide
    pause
    show cassie 12
    cassie "..."
    show cassie 13
    cassie "Nothing to see here folks!!!"
    cassie "You can go back in the pool now..."
    show cassie 15
    player_name "{i}*Cough*{/i}"
    show cassie 14
    cassie "... All right, you're causing way too much trouble around here..."
    cassie "I'm taking you in my medical room until you're fit to go."
    return

label medic_room_dialogue_count_0:
    scene expression player.location.background_blur
    show cassie 36 with dissolve
    cassie "How are you feeling?"
    show cassie 38
    player_name "{i}*Cough*{/i}"
    show cassie 37
    player_name "I think I'm alright..."
    show cassie 36
    cassie "Well, I'm just glad that you're alive..."
    show cassie 41
    cassie "... And don't you know how to swim?!"
    show cassie 38
    player_name "{i}*Cough*{/i} It's not like that..."
    show cassie 37
    player_name "... I was {i}*Cough*{/i} training..."
    player_name "... And I ran out of stamina."
    show cassie 41
    cassie "Look, it's great that you're training, but you have to start slow."
    cassie "I don't mind you staying at the pool and continuing your training, but..."
    cassie "... I can't let you walk around like that..."
    show cassie 38
    player_name "I'm {i}*Cough*{/i} so sorry about that."
    show cassie 39
    player_name "When I felt you touching me, your lips... I..."
    player_name "... I don't know why this keeps happening lately..."
    show cassie 40
    cassie "Haha!"
    cassie "Hmmm... Well..."
    show cassie 41
    cassie "Have you ever been... You know, with a girl?"
    show cassie 44
    player_name "Yeah... Obviously! Like, so many times..."
    show cassie 41
    cassie "... Really?"
    show cassie 39
    player_name "{i}*Sigh*{/i}"
    player_name "I almost dated a girl once..."
    show cassie 40
    cassie "Haha!"
    cassie "That's it??"
    show cassie 39
    player_name "Well! ... We touched hands and stuff..."
    player_name "... But then, {b}this{/b} happened... And she screamed, and..."
    player_name "Anyway, it was a long time ago so."
    show cassie 41
    cassie "Wow... So, you're like a virgin?"
    show cassie 39
    player_name "I-I guess so?"
    show cassie 40
    cassie "You're cute."
    show cassie 45
    player_name "..."
    show cassie 46
    cassie "Do you mind If I have a look at this problem we have here?"
    player_name "Uhh... Sure."
    show cassie 42 with hpunch
    window hide
    pause
    show cassie 43 with hpunch
    window hide
    pause
    show cassie 42 with hpunch
    window hide
    pause
    show cassie 46
    cassie "Okay, I know how to fix this."
    cassie "Listen carefully now..."
    show cassie 47 at Position (xpos=447)
    cassie "All you have to do, is place your dick in that hole on the wall."
    cassie "It's gonna feel nice and warm on the other side..."
    show cassie 49
    cassie "... And then, you will feel {i}much{/i} better after. Trust me..."
    show cassie 48
    player_name "You mean... I have to put my penis in that hole?!"
    show cassie 49
    cassie "That's right! Simple, right?"
    return

label medic_room_dialogue_count_0_lets_try:
    show cassie 37 at center
    player_name "Uhmm... Okay, but you can't look."
    show cassie 46
    cassie "Oh, don't you worry about that..."
    show cassie 44
    player_name "Why? You're leaving?"
    show cassie 40
    cassie "Of course! I'll be right back..."
    hide cassie with dissolve
    return

label medic_room_dialogue_count_0_do_not_feel_like_it:
    show cassie 39 at center
    player_name "I don't know... I don't really feel comfortable with this."
    show cassie 41
    cassie "..."
    show cassie 41
    cassie "No wonder you've never been with a girl..."
    show cassie 44
    player_name "I'll just wait here for a bit, until it goes away..."
    player_name "Thanks for saving me earlier..."
    show cassie 41
    cassie "... Sure, no problem."
    hide cassie with dissolve
    return

label medic_room_dialogue_count_1:
    show player 49 at right
    show cassie 58 at left
    with dissolve
    player_name "Woah... That was..."
    show cassie 50
    show player 53
    cassie "... Amazing huh?"
    show player 52
    show cassie 53
    player_name "Yeah..."
    show cassie 52
    show player 51
    cassie "Listen, this medic room is not open to the public, okay?"
    cassie "So I can't just let anyone come in here at all times..."
    show cassie 54
    cassie "... But for you I'll make an exception."
    show cassie 53
    show player 52
    player_name "Really?"
    show cassie 52
    show player 51
    cassie "Just don't tell anyone, alright?"
    show cassie 53
    show player 50
    player_name "Sure thing {b}Cassie{/b}!"
    show cassie 55
    show player 52
    cassie "Alright, see ya next time... My big man!"
    hide player
    hide cassie
    with dissolve
    return

label medic_room_dialogue_count_2:
    if wearing_swimsuit:
        show player 51 at right
    else:
        show player 1f at right
    show cassie 52 at left
    with dissolve
    cassie "I thought I saw you walk in here..."
    show cassie 53
    if wearing_swimsuit:
        show player 49
    else:
        show player 14f
    player_name "Hey {b}Cassie{/b}!"
    show cassie 52
    if wearing_swimsuit:
        show player 51
    else:
        show player 1f
    cassie "Let me guess..."
    cassie "You're having some issues down there again big man?"
    show cassie 54
    cassie "You need some... Relief?"
    if wearing_swimsuit:
        show player 51
    else:
        show player 29f
    show cassie 53
    player_name "Well..."
    return

label medic_room_dialogue_count_2_love_to:
    if wearing_swimsuit:
        show player 52
    else:
        show player 21f
    show cassie 53
    player_name "Yeah, actually I do..."
    show cassie 52
    if wearing_swimsuit:
        show player 53
    else:
        show player 13f
    cassie "That's what I thought..."
    show cassie 53
    if wearing_swimsuit:
        show player 52
    else:
        show player 21f
    player_name "You think I can do that thing again? And... Put it in the hole?"
    show cassie 55
    if wearing_swimsuit:
        show player 53
    else:
        show player 13f
    cassie "Of course! Just stick it in there and I'll come back in a minute..."
    hide player
    hide cassie
    with dissolve
    return

label medic_room_dialogue_count_2_just_changing:
    if wearing_swimsuit:
        show player 50
    else:
        show player 17f
    show cassie 53
    player_name "Actually, I just needed to change in here..."
    show cassie 57
    if wearing_swimsuit:
        show player 51
    else:
        show player 11f
    cassie "..."
    show cassie 56
    cassie "Well, that's unfortunate..."
    show cassie 57
    if wearing_swimsuit:
        show player 52
    else:
        show player 10f
    player_name "Sorry..."
    player_name "I'd love to spend some time here, but I have to get back to my training!"
    show cassie 55
    if wearing_swimsuit:
        show player 53
    else:
        show player 1f at right
    cassie "... It's okay. You get back out there, then."
    hide cassie with dissolve
    if wearing_swimsuit:
        show player 33f
    else:
        show player 44f
    player_name "There we are! All ready!"
    hide player with dissolve
    return

label medic_room_dialogue_count_finished:
    show player 17f at right
    show cassie 50 at left
    with dissolve
    player_name "That was... Amazing..."
    show player 13f
    show cassie 51
    cassie "I'm glad you feel better..."
    show player 14f
    show cassie 53
    player_name "Thank you so much..."
    show cassie 54
    show player 1f
    cassie "Just remember to keep this between us, okay?"
    show cassie 53
    show player 18f
    player_name "Yeah, of course!"
    show cassie 55
    show player 1f
    cassie "Alright... I'll see you again soon, then."
    hide player
    hide cassie
    with dissolve
    return

label gloryhole_medic:
    call expression game.dialog_select("gloryhole_medic_dialogue")
    $ game.timer.tick()
    if not store._in_replay == None:
        jump expression game.dialog_select("gloryhole_medic_bj")
    call screen gloryhole_stage01

label gloryhole_medic_dialogue:
    scene changeroom03
    show cassie 16 at Position(xpos = 431, ypos = 768)
    with fade
    window hide
    pause
    show cassie 17
    window hide
    pause
    show cassie 18 with hpunch
    window hide
    pause
    cassie "!!!"
    show cassie 19
    cassie "Oh wow..."
    cassie "( I just love his cock... )"
    show cassie 20 at Position (xpos = 437, ypos = 768)
    cassie "( The length... )"
    show cassie 21 at Position (xpos = 440, ypos = 768)
    cassie "( ... The thickness... )"
    show cassie 20 at Position (xpos = 437, ypos = 768)
    window hide
    pause
    show cassie 21 at Position (xpos = 440, ypos = 768)
    window hide
    pause
    show cassie 20 at Position (xpos = 437, ypos = 768)
    window hide
    pause
    show cassie 22 at Position (xpos = 434, ypos = 768) with hpunch
    window hide
    pause
    show cassie 23 at Position (xpos = 430, ypos = 768)
    cassie "( It just twitched! )"
    show cassie 24 at Position (xpos = 431, ypos = 768)
    cassie "( Let's see... What should I do with this thing? )"

label gloryhole_medic_bj:
    scene changeroom03
    show cassie 24 at Position (xpos = 431, ypos = 768)
    pause .5
    show cassie 26_27 at Position (xpos = 444, ypos = 768)
    pause 4
    show cassie 26_28 at Position (xpos = 444, ypos = 768)
    pause 5
    call screen gloryhole_stage02

label gloryhole_medic_bjfacefinal:
    scene changeroom03
    show cassie 24 at Position (xpos = 431, ypos = 768)
    pause .5
    show cassie 26_28 at Position (xpos = 444, ypos = 768)
    pause 5
    show cassie 29 at Position (xpos = 427, ypos = 768)
    pause .5
    show cassie 30 with hpunch
    pause .3
    show cassie 31:
        xpos 427
    pause .5
    cassie "Wow... So much cum..."
    $ renpy.end_replay()
    jump expression game.dialog_select("medic_room_dialogue")

label gloryhole_medic_bjtitsfinal:
    scene changeroom03
    show cassie 24 at Position (xpos = 431, ypos = 768)
    pause .5
    show cassie 26_28 at Position (xpos = 444, ypos = 768)
    pause 5
    show cassie 32 at Position (xpos = 427, ypos = 768)
    pause .5
    show cassie 33 with hpunch
    pause .3
    show cassie 34:
        xpos 427
    pause .5
    cassie "Wow... That's a lot of cum..."
    $ renpy.end_replay()
    jump expression game.dialog_select("medic_room_dialogue")

label gloryhole_medic_fuck_fail:
    scene changeroom03
    show cassie 35 at Position (xpos = 431, ypos = 768)
    cassie "( I don't know this guy well enough to do that... )"
    call screen gloryhole_stage01

label gloryhole_medic_fuckraw_fail:
    scene changeroom03
    show cassie 35 at Position (xpos = 431, ypos = 768)
    cassie "( That's crazy!!! I can't do that... )"
    call screen gloryhole_stage01

label gloryhole_medic_swallow_fail:
    scene changeroom03
    show cassie 35 at Position (xpos = 431, ypos = 768)
    cassie "( I don't know this guy well enough to do that... )"
    call screen gloryhole_stage02

label locked_door26_dialogue:
    scene pool
    show player 35 with dissolve
    player_name "( I should {b}get a swimsuit{/b} before I can change... )"
    player_name "( ... They should have some at the mall. )"
    hide player with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
