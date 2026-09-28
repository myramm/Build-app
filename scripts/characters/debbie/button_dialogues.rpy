label debbie_dialogue_jenny_pool_talk:
    scene expression player.location.background_closeup with None
    show anon f_normal
    show debbie
    debbie "So, what did she say?"
    anon f_worried @ -m_talk "Hmm?"
    anon "Oh, I haven't asked her yet..."
    show anon f_normal
    debbie "Heh, what are you waiting for silly?"
    anon "I'll go right now."
    debbie "Thanks, sweetie."
    anon "No problem."
    hide debbie
    show anon f_thinking a_thinking
    with dissolve
    anon @ -m_talk "( Hmm, I think {b}[jen_name] is lounging out by the pool{/b}... )"
    hide anon with dissolve
    return

label debbie_dialogue_mom_relaxing:
    scene expression player.location.background_closeup
    show debbie
    show anon with dissolve
    debbie "Hey, sweetie! Shouldn't you get going?"
    anon "Yeah. I was on my way."
    hide anon with dissolve
    return

label debbie_dialogue_mom_not_revealing_kitchen:
    $ player.go_to(L_home_kitchen)
    scene expression player.location.background_closeup with None
    show old_debbie 47 at Position(xpos=656,ypos=768)
    with dissolve
    pause
    show old_debbie 48 at Position(xpos=660,ypos=768) with dissolve
    debbie "( !!! )"
    show old_debbie 48c
    debbie "Sweetie, what are you doing back there?"
    show old_debbie 50j
    player_name "Mmm, noooothing..."
    show old_debbie 50k
    debbie "Sweetie!"
    debbie "What if {b}[jen_name]{/b} comes in?"
    debbie "She'd have a cow!"
    show old_debbie 50j
    player_name "Heh, don't worry, she's up in her room."
    player_name "... And besides..."
    player_name "... This will only take a moment."
    show old_debbie 50k
    debbie "You're such a bad b-"
    debbie "Ahh!"
    debbie "... Alright! Just be quick!"
    show old_debbie 49_50_50b at Position(xpos=660,ypos=768) with dissolve
    pause
    pause
    show old_debbie 48c with dissolve
    debbie "Okay, okay! We have to stop!"
    show old_debbie 50k
    debbie "Anymore and I'll have to go change my panties!"
    show player 1 at left
    show old_debbie 52 at right
    with dissolve
    debbie "What else can I help you with?"
    show old_debbie 1
    return

label debbie_dialogue_mom_fetch_lotion:
    show player 13 at left
    show old_debbie 2 at right
    with dissolve
    debbie "Did you {b}find my lotion in my bedroom dresser{/b}?"
    show old_debbie 1
    show player 10
    player_name "No, not yet."
    show player 5
    show old_debbie 2
    debbie "Well, what are you waiting for?"
    return

label debbie_dialogue_mom_car_condition:
    scene expression player.location.background_blur
    show debbie
    show anon f_worried with dissolve
    anon "Well, I looked at the engine..."
    debbie "And?"
    anon "It's really bad, {b}[deb_name]{/b}..."
    anon "There's no way I can fix it on my own."
    debbie f_sad "Oh, dear..."
    anon "Yeah, in fact, I think you might have to replace the whole thing."
    anon "It's really busted up bad!"
    debbie @ f_surprised "B-but, I can't afford to replace the engine!"
    anon "I know."
    pause
    debbie "What about the warranty?!"
    anon "Warranty?"
    debbie "Yeah, your father paid extra for a five year warranty when he bought the car for me."
    anon @ f_normal "That could work."
    anon "It hasn't been more than five years, has it?"
    debbie "I don't know."
    show anon f_normal
    debbie "Do you think they'll cover the repairs?"
    anon "Maybe."
    debbie "Oh, this is bad..."
    debbie "What are we gonna do without that car, {b}[firstname]{/b}?"
    anon "Don't worry, {b}[deb_name]{/b}."
    anon @ f_laugh "I'll {b}call and speak with them{/b}."
    debbie f_normal "You will?"
    anon "Of course."
    debbie "Oh, sweetie..."
    anon "I'm sure they'll be able to help us."
    debbie "I hope you're right."
    anon "I'll {b}head back to the car and call them now{/b}."
    anon "In case they need details."
    hide anon with dissolve
    return

label debbie_dialogue_mom_revealing_kitchen_pre:
    scene expression player.location.background_blur
    show old_debbieobj 2 at Position(xpos=590,ypos=768)
    return

label debbie_dialogue_mom_revealing_feel_ass_sex_pre:
    $ player.go_to(L_home_kitchen)
    scene expression player.location.background_closeup with None
    show old_debbie 47 at Position(xpos=656,ypos=768)
    with dissolve
    pause
    show old_debbie 48 at Position(xpos=660,ypos=768) with dissolve
    debbie "( !!! )"
    show old_debbie 48c
    debbie "Sweetie?"
    debbie "What are you doing back there?"
    show old_debbie 50j
    player_name "Mmm, noooothing..."
    show old_debbie 50k
    debbie "Ahh..."
    debbie "What if {b}[jen_name]{/b} comes in?"
    debbie "She'd have a cow!"
    show old_debbie 50j
    player_name "Heh, don't worry. She's up in her room."
    show old_debbie 49_50_50b at Position(xpos=660,ypos=768) with dissolve
    pause
    pause
    pause
    show old_debbie 50j with dissolve
    player_name "Does that feel good?"
    show old_debbie 50k
    debbie "Of course it does..."
    debbie "Mmm, you're making me so wet!"
    debbie "Ahh!"
    show old_debbie 50j
    player_name "What if I pulled these panties down and fucked you right here?"
    show old_debbie 50k
    debbie "Oh god..."
    debbie "Okay, do it! Take me right here! Just be quick, sweetie!"
    show old_debbie 50j
    player_name "Mmm, you better hold on to that cabinet tight!"
    show old_debbie 50c with dissolve
    pause
    show old_debbie 50d with dissolve
    pause
    hide old_debbie
    show old_debbie 50e at right
    with dissolve
    pause
    show old_debbie 50g with dissolve
    debbie "Oh, yes!"
    hide old_debbie
    show debbies 164 at right
    with dissolve
    debbie "Ahhh!"
    player_name "Wow, you're dripping..."
    return

label debbie_dialogue_mom_revealing_feel_ass_sex_after:
    show expression AnimatedImage("debbies", [164,165,166,167,168], M_debbie) as debbies at right with dissolve
    debbie "Oh, fuck me!"
    return

label mom_kitchen_fuck_loop:
    show screen sex_anim_buttons 
    pause
    hide screen sex_anim_buttons 
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("debbies", [164,165,166,167,168], M_debbie) as debbies
                $ animated = True
            pause 4
            if animcounter in [1,3]:
                call expression game.dialog_select("debbie_kitchen_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [164,165,166,167,168]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "debbies {}".format(pose_list[pose_counter]) as debbies
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            if animcounter in [1,3]:
                call expression game.dialog_select("debbie_kitchen_hscene_dialog")
        $ animcounter += 1
    call screen mom_kitchen_fuck_options

label debbie_kitchen_hscene_dialog:
    if animcounter == 1:
        if randomizer() <= 50:
            debbie "Oh!!!{p=1}{nw}"
        else:
            debbie "AHHH!!!{p=1}{nw}"

    elif animcounter == 3:
        if randomizer() <= 50:
            debbie "Did you cum, yet?{p=2}{nw}"
            player_name "Not yet...{p=2}{nw}"
            debbie "Hurry, sweetie... I don't think... I can take... Much more!{p=3}{nw}"
    return

label mom_kitchen_fuck_cum:
    call expression game.dialog_select("mom_kitchen_fuck_cum_dialogue")
    $ renpy.end_replay()
    $ persistent.cookie_jar["Debbie"]["unlocked"] = True
    $ persistent.cookie_jar["Debbie"]["gallery"]["09_unlocked"] = True
    $ game.timer.tick()
    $ game.main()

label mom_kitchen_fuck_cum_dialogue:
    player_name "( !!! )"
    player_name "Oh, {b}[deb_name]{/b}!"
    player_name "I'm-"
    debbie "Shhhh!"
    show debbies 169 with flash
    player_name "UHH!!!"
    hide debbies
    show old_debbie 50h at right
    with dissolve
    pause
    debbie "Oh, I love it when you take charge!"
    player_name "Did you cum?"
    debbie "Oh, yeah!"
    show old_debbie 50i at right
    show player 434 at left
    with dissolve
    debbie "Phew, my legs are still shaking..."
    debbie "... Wow, you came a lot!"
    pause
    show old_debbie 61 with dissolve
    show player 10
    player_name "Sorry."
    show player 13
    show old_debbie 62
    debbie "No, I love it! It feels nice inside me."
    show old_debbie 61
    show player 14
    player_name "Heh, I love it when you say things like that."
    show player 13
    show old_debbie 62
    debbie "Hehe, well, it's the truth..."
    hide player
    hide old_debbie
    with dissolve
    return

label debbie_dialogue_mom_revealing_feel_ass_no_sex:
    scene expression player.location.background_closeup with None
    hide old_debbieobj
    show old_debbie 47 at Position(xpos=656,ypos=768)
    with dissolve
    pause
    show old_debbie 50k at Position(xpos=660,ypos=768) with dissolve
    debbie "Well, hello to you too, sweetie..."
    show old_debbie 50j
    player_name "Hey, {b}[deb_name]{/b}..."
    show old_debbie 50k
    debbie "Just be careful."
    show old_debbie 49_50_50b at Position(xpos=660,ypos=768) with dissolve
    pause
    pause
    show old_debbie 50k with dissolve
    debbie "Okay, okay! We have to stop!"
    debbie "Anymore and I'll have to go change my panties!"
    show player 1 at left
    show old_debbie 52 at right
    with dissolve
    debbie "What else can I help you with?"
    show old_debbie 1
    return

label debbie_dialogue_mom_revealing_talk:
    scene expression player.location.background_closeup with None
    hide old_debbieobj
    show old_debbie 1 at right
    show player 2 at left
    with dissolve
    player_name "Hey {b}[deb_name]{/b}, got a minute?"
    show old_debbie 2
    show player 1
    debbie "Need something, {b}[firstname]{/b}?"
    show old_debbie 1
    return

label debbie_dialogue_mom_revealing:
    show player 1 at left
    show old_debbie 2 at right
    with dissolve
    if randomizer() <= 10:
        debbie "There's my big man..."
    elif randomizer() <= 20:
        debbie "Hey there, sweetie."
        debbie "What can I do for you?"
    elif randomizer() <= 30:
        debbie "Awww..."
        debbie "No hello squeeze?"
    elif randomizer() <= 70:
        debbie "Looking for me, I hope."
    elif randomizer() <= 80:
        debbie "Need something, sweetie?"
        debbie "Or can I do something for you?"
    elif L_home_shower.is_here(M_jenny):
        debbie "{b}[jen_name]{/b} is in the shower."
        debbie "In case you needed me for a quick sec."
    else:
        debbie "I was hoping I'd see you today."
    show old_debbie 1
    show player 14
    if randomizer() <= 50:
        player_name "Hello, {b}[deb_name]{/b}."
    else:
        player_name "You're looking good today."
    show player 13
    return

label debbie_dialogue_mom_not_revealing:
    show player 1 at left
    show old_debbie 2 at right
    with dissolve
    debbie "Hi, sweetie!"
    debbie "Is everything okay at school?"
    show player 14 at left
    show old_debbie 1 at right
    player_name "Yeah..."
    show player 13 at left
    show old_debbie 13 at right
    debbie "I hope you didn't fall too far behind, what with all that's happened?"
    show old_debbie 14 at right
    show player 14 at left
    player_name "Nah, I'll catch up."
    show player 13 at left
    show old_debbie 13 at right
    debbie "Just let me know if there is ever anything I can do to help?"
    show player 21 at left
    show old_debbie 14 at right
    player_name "Okay, {b}[deb_name]{/b}..."
    player_name "I should go."
    show player 13 at left
    show old_debbie 3 at right
    debbie "Don't stay out too late!"
    show old_debbie 1
    return

label debbie_dialogue_ask_about_dad:
    show player 10 at left
    show old_debbie 1 at right
    player_name "{b}[deb_name]{/b}, do you know what happened to dad?"
    show player 11
    show old_debbie 60 at Position (xoffset=-28) with dissolve
    debbie "Oh... Sweetie, I..."
    show old_debbie 59 at Position (xoffset=-28)
    show player 10
    player_name "Please, I want to know the truth!"
    show player 11
    show old_debbie 60 at Position (xoffset=-28)
    debbie "I'm sorry, sweetie. I don't have any answers for you."
    debbie "The police investigation hasn't turned up anything yet..."
    show old_debbie 59 at Position (xoffset=-28)
    show player 10
    player_name "Do you think they'll find anything?"
    show player 11
    show old_debbie 60 at Position (xoffset=-28)
    debbie "I hope so."
    show old_debbie 59 at Position (xoffset=-28)
    pause
    show old_debbie 60 at Position (xoffset=-28)
    debbie "Sweetie..."
    debbie "I want closure on this whole thing too..."
    debbie "... But your father wouldn't want us obsessing over this."
    show old_debbie 63 at Position (xoffset=-28)
    debbie "You're a young man and you need to focus on living your life."
    debbie "Do it for your dad."
    show player 10
    show old_debbie 59 at Position (xoffset=-28)
    player_name "Yeah. I'll try."
    show player 14
    show old_debbie 61 at Position (xoffset=-28)
    player_name "Thanks, {b}[deb_name]{/b}."
    show player 1
    show old_debbie 2 with dissolve
    debbie "Anything else you need?"
    show old_debbie 1
    show player 1
    return

label debbie_dialogue_ask_about_money_problems:
    show old_debbie 13
    show player 11
    debbie "I told you not to worry about that."
    debbie "Everything is going to be fine!"
    show old_debbie 14
    show player 14
    player_name "Okay, but what if I wanted to help you?"
    player_name "What if I got a real job?"
    show player 10
    player_name "I feel somewhat responsible for all this stress..."
    show old_debbie 52 at Position (xoffset=1)
    show player 11
    debbie "You can help me by staying in school!"
    debbie "Your father would roll over in his grave if I let you get a full time job..."
    debbie "He wanted you to finish your education."
    show old_debbie 51 at Position (xoffset=1)
    show player 10
    player_name "But I can work after school and on the weekends..."
    show old_debbie 53 at Position (xoffset=-18) with dissolve
    show player 13
    debbie "{i}*Sigh*{/i} You're so stubborn, just like your father..."
    show old_debbie 59 at Position (xoffset=-28) with dissolve
    debbie "Hmm..."
    show old_debbie 61 at Position (xoffset=-28)
    debbie "Focus on getting your grades up first, okay?"
    debbie "Then maybe you can get a job."
    show old_debbie 61 at Position (xoffset=-28)
    show player 18
    player_name "Y-yeah, okay."
    show old_debbie 62 at Position (xoffset=-28)
    show player 1
    debbie "Anything else you want to talk about, sweetie?"
    show old_debbie 1 with dissolve
    return

label debbie_dialogue_ask_about_men_in_suits:
    show player 10
    player_name "{b}[deb_name]{/b}, I wanted to talk about what that guy in the suit said..."
    show old_debbie 59 at Position (xoffset=-28) with dissolve
    player_name "Was dad involved with them?"
    show player 11
    show old_debbie 53 at Position (xoffset=-18) with dissolve
    debbie "{i}*Sigh*{/i} Honestly, I don't know, sweetie.."
    debbie "Your father was a good man, {b}[firstname]{/b}."
    debbie "It's hard to imagine him getting mixed up with a bunch of thugs like that..."
    debbie "... But now he's gone and it seems there's a lot he didn't share with me."
    show old_debbie 60 at Position (xoffset=-28) with dissolve
    debbie "Those men think your father owed them money, and now that he's dead they want us to cover his debt."
    show player 10
    show old_debbie 59 at Position (xoffset=-28)
    player_name "Why aren't the police doing anything to stop them?!"
    show player 11
    show old_debbie 60 at Position (xoffset=-28)
    debbie "It's not that simple, sweetie..."
    show player 10
    show old_debbie 59 at Position (xoffset=-28)
    player_name "Why not?!"
    show player 11
    show old_debbie 60 at Position (xoffset=-28)
    debbie "{i}*Sigh*{/i} It just isn't."
    show old_debbie 59
    pause
    show old_debbie 53 at Position (xoffset=-18) with dissolve
    debbie "Sometimes I think we should just grab {b}[jen_name]{/b} and disappear for a while..."
    show player 1
    show old_debbie 63 at Position (xoffset=-28) with dissolve
    debbie "Heh, that would be an adventure, wouldn't it?"
    show old_debbie 51 at Position (xoffset=1)
    show player 2
    player_name "Yeah, I suppose."
    show old_debbie 2 with dissolve
    show player 1
    debbie "Is there anything else you wanted to talk about?"
    show old_debbie 1
    return

label debbie_dialogue_paint:
    show player 10
    player_name "Wasn't there some paint in the garage?"
    show player 5
    show old_debbie 13
    debbie "Paint? What do you want with old paint?"
    show old_debbie 1
    show player 10
    player_name "I was going to try and make... Something."
    show player 5
    show old_debbie 2
    debbie "Oh, well, {b}Diane{/b} said she'd get rid of them for me."
    show old_debbie 1
    show player 12
    player_name "Really?"
    player_name "Well, I'd better see if I can pick them up before she throws them away!"
    player_name "Thanks, {b}[deb_name]{/b}! Bye, {b}[deb_name]{/b}!"
    hide player with dissolve
    show old_debbie 2
    debbie "Bye!"
    return

label debbie_dialogue_help_mow_lawn:
    show player 10
    player_name "Did you need help with anything?"
    show player 5
    show old_debbie 2
    debbie "Did you finish mowing the yard?"
    show old_debbie 1
    show player 10
    player_name "Oh, right!"
    player_name "I'll get on that."
    show player 13
    show old_debbie 2
    debbie "I'd really appreciate it, sweetie."
    show old_debbie 1
    show player 14
    player_name "No problem!"
    hide player
    hide old_debbie
    with dissolve
    return

label debbie_dialogue_help_fix_broken_pipe:
    show player 4
    player_name "( I gotta fix the {b}bathroom sink{/b} somehow... )"
    return

label debbie_dialogue_help_chores_pre:
    show player 14
    player_name "Anything else you need help with?"
    show player 13
    show old_debbie 2
    return

label debbie_dialogue_help_chores_later:
    debbie "No. Not right now, sweetie."
    debbie "Maybe later, if you're still available."
    return

label debbie_dialogue_help_chores_tomorrow:
    debbie "No. Not today, sweetie."
    debbie "Maybe tomorrow, if you're still available."
    return

label debbie_dialogue_help_chores_after:
    show old_debbie 3
    debbie "Thanks for asking!"
    show old_debbie 1
    show player 14
    player_name "You're welcome, {b}[deb_name]{/b}."
    return

label debbie_dialogue_help_check_car:
    show player 4
    player_name "( I should {b}go check the car{/b} like {b}[deb_name]{/b} asked me to. )"
    return

label debbie_dialogue_help_fix_car:
    scene expression player.location.background_closeup
    show debbie
    show anon with dissolve
    debbie "Any luck with the dealership, sweetie?"
    anon @ -m_talk "Hmm?"
    anon @ f_brag_closed "Oh, right!"
    debbie "Did you forget?"
    anon "Nope, I'll take care of it right now."
    anon "I'll {b}call from near the car{/b} in case they need any details."
    debbie "Thanks, sweetheart."
    hide anon with dissolve
    return

label debbie_dialogue_mech_en_route:
    scene expression player.location.background_closeup
    show debbie
    show anon with dissolve
    debbie "Any luck with the dealership, sweetie?"
    anon "They're sending someone over as soon as possible."
    debbie "Oh wonderful! Thanks, sweetheart."
    hide anon with dissolve
    return

label debbie_dialogue_help_nothing:
    show player 2
    player_name "Hey, {b}[deb_name]{/b}, anything I can do to help around the house?"
    show player 1
    debbie "Hmm..."
    show old_debbie 2
    debbie "Nothing I can think of right now, no."
    show old_debbie 1
    show player 2
    player_name "Cool. Let me know if something comes up."
    return

label debbie_dialogue_lotion_fun_had_sex:
    show player 14
    player_name "Need me to rub some more lotion on... Your legs?"
    show player 13
    show old_debbie 2
    debbie "That sounds wonderful, sweetie."
    debbie "I could really use your gentle touch right about now."
    return

label debbie_dialogue_lotion_fun:
    show player 10
    player_name "Need me to rub some more lotion on... Your legs?"
    show player 5
    show old_debbie 13
    debbie "Oh... Again? Well, I..."
    show old_debbie 14
    show player 10
    player_name "Did I do a bad job?"
    show player 5
    show old_debbie 13
    debbie "Oh, no, sweetie. It was... Really good."
    show old_debbie 14
    pause
    show old_debbie 13
    debbie "Sure, I guess I could use a break."
    show old_debbie 1
    show player 14
    player_name "Great!"
    show player 13
    show old_debbie 2
    return

label debbie_dialogue_lotion_fun_after:
    debbie "Go and grab the {b}lotion from my bedroom dresser{/b}."
    show old_debbie 1
    show player 14
    player_name "Alright!"
    return

label debbie_dialogue_shopping:
    scene location_home_kitchen_day_blur
    show player 2 at left
    show old_debbie 1 at right
    player_name "Remember when you asked me to go shopping with you?"
    show player 1
    show old_debbie 2
    debbie "Yeah."
    show player 2
    show old_debbie 1
    player_name "Well, I'm free now. Do you still wanna go?"
    show player 1
    show old_debbie 3
    debbie "Really?! Great!"
    show old_debbie 2
    debbie "Just let me get ready and I'll meet you in the car, okay?"
    show old_debbie 1
    show player 2
    player_name "Alright."
    return

label debbie_dialogue_shower_basement:
    show player 2
    show old_debbie 1
    player_name "So uhh..."
    player_name "I was thinking we could maybe... Take a shower together?"
    show player 13
    show old_debbie 2
    debbie "Right now?"
    show old_debbie 1
    debbie "Hmm..."
    show old_debbie 3
    debbie "I suppose I could go for a shower."
    show old_debbie 2
    debbie "Let me just finish putting this load of laundry in and I'll meet you upstairs."
    scene shower_closeup
    show debbies 27
    with dissolve
    pause
    show debbies 28 at Position(xpos=487,ypos=768) with dissolve
    pause
    show debbies 34 with dissolve
    debbie "Hope you're not almost done..."
    debbie "I was hoping we could spend some time in here."
    return

label debbie_dialogue_shower_kitchen:
    show player 2
    show old_debbie 1
    player_name "Hey, {b}[deb_name]{/b}!"
    player_name "I was wondering..."
    show player 21
    player_name "Would you like to take a shower with me?"
    show player 14
    show old_debbie 2
    debbie "It is getting pretty hot in the house..."
    show old_debbie 3
    debbie "Sure! A shower sounds lovely right now."
    show old_debbie 2
    debbie "Give me a minute. I'll join you after I'm done here."
    scene shower_closeup
    show debbies 27
    with dissolve
    pause
    show debbies 28 at Position(xpos=487,ypos=768) with dissolve
    pause
    show debbies 34 with dissolve
    debbie "Sorry to keep you waiting, sweetie..."
    return

label debbie_dialogue_sex_in_debbies_room_basement:
    show player 14
    player_name "Would you like to join me in your room?"
    show player 13
    show old_debbie 3
    debbie "Right now?"
    show old_debbie 1
    show player 10
    player_name "Absolutely!"
    show player 5
    show old_debbie 2
    debbie "Heh, alright..."
    show player 13
    debbie "... Just make sure, {b}[jen_name]{/b} doesn't see us."
    show old_debbie 1
    show player 14
    player_name "I will."
    show player 13
    show old_debbie 2
    debbie "Hehehe..."
    debbie "You're going to wear me out!"
    show old_debbie 1
    show player 14
    player_name "I'm just making sure you get plenty of exercise!"
    show player 13
    show old_debbie 3
    debbie "Hahaha."
    show old_debbie 2
    debbie "Get your butt upstairs and get those clothes off!"
    scene debbie_bedroom_closeup2

    label sex_mom_bed_intro_1:
        show old_debbie 86 at left
        show player 434f at right
        with dissolve
        debbie "The bed sheets are so nice and soft... Why don't you come lay with me..."
        show old_debbie 84
        show player 8f with dissolve
        pause
        show player 261 with dissolve
        pause
        show old_debbie 85
        show player 263 with dissolve
        debbie "Naughty boy."
        show old_debbie 84
        show player 262
        player_name "What?"
        show player 263
        show old_debbie 85
        debbie "You truly are insatiable."
        show old_debbie 84
        show player 262
        player_name "You can just lay on your back and I can do the rest."
        show player 263
        show old_debbie 86
        debbie "Well, where's the fun in that?"
        show old_debbie 84
        show player 262
        player_name "Heh, don't worry. I'll make it fun!"
        show player 263
        show old_debbie 84
        debbie "Mmm, I have no doubt about that!"
        show old_debbie 89 with dissolve
        if not store._in_replay == None:
            call expression game.dialog_select("debbie_dialogue_sex_in_debbies_room_after")
            jump expression game.dialog_select("mom_sex")
    return

label debbie_dialogue_sex_in_debbies_room_kitchen:
    show player 14
    player_name "Would you like to join me in your room?"
    show player 13
    show old_debbie 2
    debbie "Right now?"
    debbie "Absolutely!"
    debbie "Let's just make sure, {b}[jen_name]{/b} doesn't see us."
    show old_debbie 1
    show player 14
    player_name "Yup."
    show player 13
    scene debbie_bedroom_closeup2

    label sex_mom_bed_intro_2:
        show player 434f at right
        show old_debbie 86 at left
        with dissolve
        debbie "I was hoping you'd bring me in here for this today!"
        show old_debbie 84
        show player 435f
        player_name "You were really thinking about it?"
        show player 434f
        show old_debbie 86
        debbie "Does that really surprise you?"
        debbie "I'm always thinking about that big cock of yours..."
        show old_debbie 84
        show player 435f
        player_name "Heh, I think about it a lot too... Especially when you're wearing that robe of yours."
        show player 434f
        show old_debbie 89 with dissolve
        debbie "You mean this old thing?"
        show old_debbie 90
        show player 435f
        player_name "... Oh, yeah."
        show player 434f
        show old_debbie 89
        debbie "Hehe, why don't you take off those clothes and come play with me?"
        show old_debbie 90
        show player 8f with dissolve
        pause
        show player 261 with dissolve
        pause
        show player 263
        show old_debbie 102
        with dissolve
        debbie "Mmmm..."
        show old_debbie 103
        if not store._in_replay == None:
            call expression game.dialog_select("debbie_dialogue_sex_in_debbies_room_after")
            jump expression game.dialog_select("mom_sex")
    return

label debbie_dialogue_sex_in_debbies_room_after:
    debbie "Come and get me, big boy!"
    hide player
    show old_debbie 104 at left
    with dissolve
    pause
    scene debbie_bedroom_closeup_sex
    return

label debbie_dialogue_sex_in_my_room:
    show player 2
    player_name "You wanna sleep in my room tonight?"
    show player 1
    show old_debbie 2
    debbie "Mmm, I would love that, sweetie."
    show player 2
    show old_debbie 1
    player_name "Great! I'll wait up for you then."
    show player 1
    show old_debbie 2
    debbie "Can't wait!"
    return

label debbie_dialogue_sex_in_car:
    show player 14
    player_name "{b}[deb_name]{/b}, would you come with me for a second?"
    show player 13
    show old_debbie 2
    debbie "Hmm?"
    show old_debbie 1
    show player 14
    player_name "Just follow me."
    show player 13
    show old_debbie 2
    debbie "Hehe, what are you up to?"
    show old_debbie 2
    debbie "..."
    show old_debbie 3
    debbie "You're planning something!"
    show old_debbie 2
    debbie "Hehe!"
    debbie "Is it a surprise?"
    debbie "... I love surprises!"
    show old_debbie 1
    show player 14
    player_name "Heh, I know you do."
    player_name "I wouldn't really call it a surprise though..."
    show player 13
    show old_debbie 3
    debbie "Hehe!"
    show old_debbie 2
    debbie "Well, what would you call it then?"
    show old_debbie 1
    debbie "..."
    show old_debbie 2
    debbie "Is this something naughty?"
    debbie "..."
    show old_debbie 1
    show player 14
    player_name "Maaaaybe."
    show old_debbie 2
    debbie "Hehe, alright. Let's go quickly while {b}[jen_name]{/b} is upstairs."
    hide player
    hide old_debbie
    scene black
    with fade
    return

label debbie_dialogue_watch_movie:
    show player 2
    player_name "I was thinking, maybe we should watch another movie tonight. Interested?"
    show player 1
    show old_debbie 2
    debbie "Mmm, a movie night, huh?"
    debbie "That sounds like a great idea, sweetheart!"
    show player 2
    show old_debbie 1
    player_name "Awesome!"
    player_name "I'll see you {b}tonight{/b} in the {b}living room{/b} then?"
    show player 1
    show old_debbie 2
    debbie "I can't wait..."
    return

label debbie_dialogue_laundry_sex_basement:
    scene home_basement
    show old_debbie 122 at right
    show player 14 at left
    player_name "Are you almost done with the laundry?"
    show player 13
    show old_debbie 123
    debbie "Almost. I just have to move this load into the dryer."
    debbie "Why, what's up, sweetie?"
    show player 14
    show old_debbie 122
    player_name "I just thought you might like to go for a ride?"
    show player 13
    show old_debbie 123
    debbie "Oh, feeling a bit naughty, are we?"
    show player 8 with dissolve
    pause
    show player 261f with dissolve
    pause
    show old_debbie 123
    debbie "Hehe, I'll take that as a yes!"
    show player 263f with dissolve
    debbie "..."
    show old_debbie 121
    show player 432
    player_name "Absolutely!"
    show player 431
    pause
    show old_debbie 123
    debbie "Get those clothes off and get on the washer!"
    scene home_basement_sex_01
    show player 271 at Position(xpos=655,ypos=768)
    show old_debbie 107 zorder 0 at Position(xpos=200)
    with dissolve
    pause
    show old_debbie 108
    debbie "My turn..."
    debbie "Mmm, I've been waiting all morning for this!"
    show old_debbie 109
    pause
    show old_debbie 110
    pause
    show old_debbie 111
    pause
    show old_debbie 112
    pause
    show old_debbie 113
    pause
    show old_debbie 114
    pause
    player_name "You look beautiful, {b}[deb_name]{/b}."
    show old_debbie 115
    debbie "Just sit back and relax, sweetie."
    debbie "I'll take care of everything..."
    debbie "... Just make sure you hold on to me."
    hide player
    hide old_debbie
    show debbies 124 at Position(xpos=650)
    with dissolve
    pause
    show debbies 125 at Position(xpos=655)
    pause
    show debbies 126f with dissolve
    debbie "Oh!"
    show debbies 126e
    pause
    show debbies 126d
    pause
    show debbies 126c
    pause
    show debbies 126b
    pause
    show debbies 126
    return

label debbie_dialogue_laundry_sex_basement_random_true:
    debbie "Mmmm..."
    debbie "I can barely fit you all in."
    return

label debbie_dialogue_laundry_sex_basement_random_false:
    debbie "Ahh..."
    player_name "( !!! )"
    player_name "You're so warm..."
    return

label debbie_dialogue_laundry_sex_kitchen:
    show player 14
    player_name "Hey, {b}[deb_name]{/b}... Do you want to hang out in the basement for some quick fun?"
    show player 13
    show old_debbie 2
    debbie "Oh?"
    show old_debbie 1
    show player 14
    player_name "I figured we could turn on the dryer and you could be as loud as you wanted..."
    show player 13
    show old_debbie 3
    debbie "Haha."
    show old_debbie 2
    debbie "That's quite naughty, sweetie."
    show old_debbie 1
    pause
    show old_debbie 2
    debbie "Hmm... Alright!"
    debbie "I have some free time and I could use some... Attention."
    show old_debbie 1
    show player 14
    player_name "Really?"
    show player 13
    show old_debbie 2
    debbie "Sure!"
    debbie "Just meet me down there in a minute..."
    hide old_debbie
    hide player
    with dissolve
    return

label debbie_dialogue_kiss:
    show player 10 at left
    show old_debbie 1 at right
    player_name "Hey... Umm, {b}[deb_name]{/b}?"
    show player 5
    show old_debbie 2
    debbie "Yes, sweetie?"
    show player 10
    show old_debbie 1
    player_name "Could I ask you something?"
    show player 5
    show old_debbie 3
    debbie "Of course! You can ask me anything."
    show player 10
    show old_debbie 1
    player_name "Well, it's kinda... Embarrassing."
    show player 5
    show old_debbie 13
    debbie "Oh? Well, that's okay, {b}[firstname]{/b}."
    debbie "There's no need to feel embarrassed."
    debbie "Not with me..."
    show old_debbie 14
    show player 10
    player_name "Okay."
    return

label debbie_dialogue_kiss_teach:
    show player 10 at left
    show old_debbie 14 at right
    player_name "I was wondering if you could..."
    player_name "Well..."
    show player 5
    show old_debbie 13
    debbie "If I could what, sweetheart?"
    show player 10
    show old_debbie 14
    player_name "Err... Remember the other day at the mall?"
    show player 5
    show old_debbie 14b
    player_name "..."
    show old_debbie 13
    debbie "... Yes?"
    show player 10
    show old_debbie 14b
    player_name "Well... I was hoping you could teach me more, you know, about kissing?"
    show player 5
    show old_debbie 13
    debbie "What?!"
    show old_debbie 14b
    player_name "..."
    show old_debbie 13
    debbie "That was a mistake, sweetie. I should never have..."
    debbie "What are you hoping I'd teach you anyways?"
    show player 10
    show old_debbie 14b
    player_name "You know, like, how to do it."
    player_name "I thought, maybe, you could show me what women like?"
    show player 5
    show old_debbie 13
    debbie "Hmm, well, I could certainly tell you what women like."
    debbie "... But I don't think showing you is a good idea. It would be kind of inappropriate..."
    show old_debbie 14b
    return

label debbie_dialogue_kiss_teach_stat_fail:
    show player 10 at left
    show old_debbie 14b at right
    player_name "Are you sure?"
    player_name "I'd really like to practice with you."
    show player 5
    debbie "..."
    show old_debbie 13
    debbie "It's just not a good idea, sweetie."
    show player 10
    show old_debbie 14b
    player_name "Oh... A-alright."
    show player 5
    show old_debbie 13
    debbie "Sorry, sweetheart."
    show player 10
    show old_debbie 14b
    player_name "It's okay, {b}[deb_name]{/b}."
    return

label debbie_dialogue_kiss_leave:
    show player 10 at left
    show old_debbie 14 at right
    player_name "... Actually."
    player_name "Never mind."
    show old_debbie 13
    show player 5
    debbie "Are you sure?"
    debbie "You can always talk to me, {b}[firstname]{/b}."
    show player 10
    show old_debbie 14
    player_name "Yeah, it's nothing."
    player_name "Sorry to bug you."
    show player 5
    show old_debbie 13
    debbie "You never bug me, sweetie."
    return

label debbie_dialogue_kiss_practice:
    show player 2 at left
    show old_debbie 1 at right
    player_name "Do you think we could practice again?"
    player_name "You know... Kissing?"
    show player 1
    show old_debbie 13
    debbie "Again?"
    show player 2
    show old_debbie 14b
    player_name "Y-yeah. I think I'm getting better!"
    show player 1
    show old_debbie 13
    debbie "... Alright."
    debbie "But just a little!"
    show player 2
    show old_debbie 14
    player_name "Okay, sure."
    hide player
    show old_debbie 79 at Position(xpos=0.70, ypos=1.0) with dissolve
    pause
    show old_debbie 80
    debbie "Mmm..."
    show old_debbie 79
    pause
    show old_debbie 78 at Position(xpos=0.80, ypos=1.0) with dissolve
    show player 233 at Position(xpos=0.30, ypos=1.0) with dissolve
    pause
    show old_debbie 77
    debbie "Wow... I'd say you're definitely getting better."
    debbie "... And you were already so good to begin with!"
    show player 232
    show old_debbie 76
    player_name "Thanks, {b}[deb_name]{/b}!"
    show player 231
    show old_debbie 74
    pause
    show player 230
    pause
    show player 232
    show old_debbie 76
    player_name "Sorry about the... You know."
    show player 231
    show old_debbie 75
    debbie "Hehe, it's alright, sweetheart."
    debbie "Perfectly natural."
    debbie "The girls in this town are in trouble."
    show player 232
    show old_debbie 72
    player_name "Hah, you bet!"
    show player 231
    show old_debbie 73
    debbie "Go get em, sweetie!"
    show player 232
    show old_debbie 72
    player_name "Yes, ma'am!"
    return

label debbie_dialogue_leave:
    show player 2
    player_name "Actually, never mind, see you later, {b}[deb_name]{/b}."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
