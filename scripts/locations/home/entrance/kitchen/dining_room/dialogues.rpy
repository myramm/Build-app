label dining_room_jenny_have_breakfast_4:
    scene expression game.timer.image("dining_room{}")
    show jenny b_breakfast_dressed a_phone f_upset_down zorder 1
    show anon b_dinner_sitting_look_left f_worried zorder 0
    show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 3
    with dissolve
    pause
    show jenny f_upset
    jenny "About time..."
    anon "What is your problem?"
    jenny "We've got a big show today."
    anon "Big show?"
    jenny "That's right so eat up."
    anon "What do you-"
    show anon f_surprised_left
    debbie "Good morning, sweetheart!"
    show debbie b_breakfast_potatoes
    anon b_dinner_sitting f_normal "Morning, {b}[deb_name]{/b}."
    debbie "I hope you're hungry."
    show jenny f_eyeroll
    anon "Starving."
    show jenny f_normal
    jenny "{b}[deb_name]{/b}, do you know where my uniform is?"
    debbie "What uniform, dear?"
    show anon f_looking_down_eating a_eating with dissolve
    jenny "You know, from college..."
    show anon f_looking_down_food a_resting with dissolve
    debbie "You mean, your cheerleading costume?"
    show jenny f_upset
    jenny "{b}[deb_name]{/b}, it's a uniform!"
    debbie "Okay, okay, uniform."
    debbie @ f_sorry "Umm..."
    debbie "It's probably stored away in the attic with the rest of our old clothes..."
    show jenny f_surprised
    jenny "In the attic?!"
    show jenny f_angry
    show anon f_surprised_food
    jenny "Damn it, {b}[deb_name]{/b}!"
    show debbie f_surprised
    jenny "It's going to be covered in dust and cobwebs!"
    show jenny f_angry_pouting
    debbie f_sad "Well, I'm sorry dear..."
    show anon f_surprised_high_food
    debbie "I dunno-"
    pause
    debbie f_sorry "What do you need that old thing for anyways?"
    debbie "It probably won't even fit you now."
    show anon f_surprised_food
    show jenny f_upset
    jenny "Yeah, I know but my fans-"
    show jenny f_surprised
    jenny "Err... I mean, I-"
    show jenny f_surprised_down_back m_talk
    pause
    show jenny f_upset -m_talk
    jenny "{i}*Sigh*{/i} It's not important, just never mind."
    show anon f_surprised_high_food
    debbie f_normal "Would you like me to get it down and wash it for you?"
    show anon f_surprised_food
    jenny "Ugh, I said forget it, {b}[deb_name]{/b}!!"
    show debbie f_sad
    menu:
        "Remain Silent {color=7ff7}[[Submissive]{/color}":
            show anon f_surprised_teeth_down
            anon @ -m_talk "..."
            debbie "O-okay, dear."
            hide debbie with dissolve
            pause
            jenny "Why does nothing ever go right in this house?!"
            anon b_dinner_sitting_look_left f_worried "I don't know."
            $ M_jenny.decrement("dominance")
        "Say Something {color=f77b}[[Dominant]{/color}":
            show anon f_grumpy_food_left
            anon "Hey, don't talk to {b}[deb_name]{/b} like that!"
            debbie f_surprised "!!!"
            $ M_jenny.increment("dominance")
            if M_jenny.get("dominance") <= 0:
                show jenny f_angry
                jenny "What did you say?!"
                show debbie f_sad
                anon "She's just trying to help!"
                pause
                jenny "Well, I didn't ask for her help, did I?!"
                anon "I wasn't-"
                show anon f_surprised_food
                anon "I didn't mean to-"
                show anon f_looking_down_food a_resting
                jenny "Mind your own business, loser!"
                show anon f_shy_down with dissolve
                anon @ -m_talk "..."
                debbie "Would you two please not fight at the breakfast table?!"
                hide debbie with dissolve
                debbie "I just don't understand where she gets that temper from..."
            else:
                show jenny f_angry
                show anon f_grumpy_food_left
                anon "She's just trying to help!"
                show debbie f_sad
                anon "You know, kinda like I WAS going to help you with your new job..."
                anon "... But now I'm thinking I won't bother."
                show jenny f_surprised
                jenny "That's not-"
                show jenny f_surprised_down
                jenny "I didn't mean to-"
                show anon f_worried_high with dissolve
                anon "{b}[jen_name]{/b} is sorry."
                anon f_worried_left "Aren't you?!"
                show jenny f_angry
                pause
                anon "Well?!"
                show jenny f_upset_down
                jenny "S-sorry, {b}[deb_name]{/b}..."
                show jenny f_upset
                jenny "... I'm just, having a bad day."
                show anon b_dinner_sitting f_normal
                debbie "It's alright, dear. I understand."
                show jenny f_upset_down
                pause
                show jenny zorder 2
                show anon zorder 1
                show debbie f_normal b_breakfast_kiss zorder 0 with dissolve
                debbie "Thank you, sweetie."
                show debbie f_kiss
                show anon f_surprised_left_low
                anon @ -m_talk "!!!"
                show anon f_normal of_blush
                show jenny f_eyeroll
                hide debbie with dissolve
                pause
                show jenny f_upset
                jenny "You know, I liked you better before you grew a backbone..."
                anon f_worried_left of_empty "No, you didn't."
                show jenny f_eyeroll
                jenny "W-whatever..."
    show jenny f_upset
    jenny "Before you {b}come to my room this afternoon{/b}, {b}pop up in the attic and grab my cheer uniform{/b}."
    anon "Why?!"
    jenny "Because I'm going to wear it for the show today."
    show anon f_surprised_left
    anon "!!!"
    anon f_normal_left "R-really?!"
    show anon f_laugh
    pause
    show anon f_normal_left
    show jenny f_eyeroll
    jenny "Yes, perv..."
    show jenny b_breakfast_gettingup f_upset with dissolve
    jenny "Don't forget."
    hide jenny with dissolve
    pause
    anon f_laugh "( Hmm, I wonder what we're going to do while she's wearing her old cheerleading outfit? )"
    return

label dining_room_jenny_pissed_at_blowjob:
    scene expression game.timer.image("dining_room{}")
    show jenny b_breakfast_dressed a_phone f_upset_down zorder 1
    show anon b_dinner_sitting_look_left f_worried zorder 0
    show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
    with dissolve
    pause
    jenny @ -m_talk "..."
    anon "Good morning."
    show jenny f_upset_down
    jenny "Yeah, morning."
    pause
    anon "Are you going to pay me for yesterday?"
    show jenny f_angry
    jenny "Oh, you wanna get paid to cum down my throat, huh?"
    if M_jenny.get("dominance")<= 0:
        anon "I said, I was sorry..."
        show jenny f_upset_down
        pause
        anon "You know, you came in my mouth too!"
        jenny "Haha, oh yeah!"
        jenny "I forgot about that..."
        anon "You practically waterboarded me!"
        show jenny f_laugh
        jenny "HAHAHAAH!"
    else:
        anon "{b}[jen_name]{/b}, I warned you!"
        show jenny f_angry
        jenny "Yeah, well, it's hard to concentrate on what you're saying!"
        jenny "You're really good at-"
        show jenny f_upset_down
        jenny "Never mind."
        anon "Really good at what?"
        anon "... Eating your pussy?"
        jenny "I didn't say that..."
        anon f_normal "Mmm, you kinda did..."
        jenny "Shut up."
        pause
        anon f_worried "So are you going to pay me or what?"
    show jenny f_upset_down
    jenny "{i}*Sigh*{/i} Fine."
    show jenny a_money f_upset with dissolve
    jenny "I guess you earned it."
    show jenny a_phone f_upset_down with dissolve
    anon f_normal "Thanks."
    show anon f_shy_down
    pause
    jenny "You know, my fans really did like that show."
    anon f_normal "Yeah?"
    jenny "It's got more than double the views that our handjob video has."
    anon "That's great!"
    show jenny f_grin
    jenny "Yeah, it means you're going to be eating a lot more pussy."
    if M_jenny.get("dominance") <= 0:
        anon f_surprised_left "!!!"
        anon f_normal "O-okay."
        jenny "Lucky little loser..."
    else:
        anon "... And you'll be sucking a lot more dick."
        show jenny f_grin_down
        jenny "Tch, yeah... Maybe."
        anon "Haha!"
        show jenny f_upset
    jenny "Just don't go thinking I enjoy-"
    show jenny f_surprised
    show anon f_worried_high
    debbie "What are you kids talking about?"
    anon @ -m_talk "!!!" with hpunch
    show debbie b_breakfast_potatoes
    show jenny f_surprised_down
    debbie "Has {b}[firstname]{/b} been eating something?"
    anon "I..."
    show jenny f_surprised_down_back
    anon f_worried "W-we aren't..."
    jenny "Peaches!"
    anon "Huh?!"
    show jenny f_surprised
    jenny "I bought some peaches the other day..."
    show jenny f_normal
    jenny "... {b}[firstname]{/b} was eating my peaches."
    show anon f_worried_high
    debbie "Oh, I love peaches!"
    debbie "They're so juicy!"
    anon f_laugh "{i}*Snort*{/i}"
    show anon f_normal
    show jenny f_grin
    jenny "Heh, you should have seen him when he finished."
    jenny "{b}[firstname]{/b} is a real sloppy eater."
    show anon f_normal_high
    debbie "Hehe, was his face all messy?"
    show jenny f_laugh
    jenny "He even had some in his hair!"
    show jenny f_grin
    debbie @ f_laugh "Haha!"
    pause
    debbie "It's nice you're sharing with {b}[firstname]{/b}."
    debbie "One day, you kids are going to realize how fortunate you are to have one another."
    anon "Heh, you think?"
    jenny "Yeah, right."
    debbie @ f_laugh "Now, who wants bacon?!"
    anon "Oh, me!"
    show debbie b_breakfast_potatoes3 with dissolve
    show jenny f_eyeroll
    pause
    call popup ('earn', 100)
    $ player.get_money(100)
    scene black with dissolve
    return

label dining_room_jenny_pissed_at_handjob:
    scene expression game.timer.image("dining_room{}")
    show jenny b_breakfast_dressed a_phone f_upset_down zorder 1
    show anon b_dinner_sitting_look_left f_worried zorder 0
    show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
    with dissolve
    pause 
    jenny @ -m_talk "..."
    anon "You still pissed at me?"
    jenny "Hmm?"
    show jenny f_upset_down
    jenny "Oh."
    jenny "Morning, asshole!"
    anon "Heh, you're still mad."
    show jenny f_angry
    jenny "Of course, I'm mad!"
    jenny "You're disgusting!"
    anon "Look, I didn't mean to cum on you! It was just-"
    show jenny f_upset
    jenny "Shhh!!!"
    jenny "Not so loud dummy, {b}[deb_name]{/b} will hear you!"
    anon @ f_worried_high "Right, sorry."
    show jenny f_angry
    jenny "I had to do laundry because of you!"
    jenny "You know I hate doing laundry!"
    anon "I thought {b}[deb_name]{/b} still did your laundry?"
    jenny "Well, I can't exactly just hand her a bunch of cum stained bed sheets to wash, now can I?!"
    anon "No, I guess not..."
    show jenny f_eyeroll
    jenny "Moron."
    show jenny f_upset
    if M_jenny.get("dominance") <= 0:
        anon @ -m_talk "..."
        anon "Seriously, I'm sorry!"
    else:
        anon "You don't have to be such a bitch about it."
        jenny "Ugh."
    jenny "Whatever."
    jenny "Next time it happens, {i}YOU'RE{/i} washing my sheets!"
    anon "Next time?"
    jenny "Well, yeah..."
    show jenny f_normal
    jenny "... We made mad bank yesterday!"
    anon "Really?"
    jenny "Here."
    show jenny a_money with dissolve
    jenny "Your cut."
    anon f_normal "Whoa, thanks!"
    show jenny a_idle with dissolve
    pause
    anon "So when is our next show?"
    jenny "Anytime {b}in the afternoon{/b} works for me."
    jenny "Just {b}come to my room{/b}."
    anon "Awesome!"
    show debbie b_breakfast_potatoes with dissolve
    show anon f_normal_high
    show jenny f_normal_low
    debbie "Who's hungry?"
    anon "Me!"
    debbie "Hehe!"
    debbie "Here you go, sweetie."
    show debbie b_breakfast_potatoes3 with dissolve
    show anon b_dinner_sitting f_normal
    pause
    show debbie b_breakfast_potatoes with dissolve
    debbie "Are you kids getting along okay?"
    show anon b_dinner_sitting_look_left f_worried
    show jenny f_sad
    pause
    anon b_dinner_sitting f_normal "Y-yes?"
    show jenny f_normal_low
    show anon f_normal_high
    debbie "Good."
    debbie "It warms my heart, you two spending time together."
    show jenny f_eyeroll
    anon "T-thanks, {b}[deb_name]{/b}."
    show jenny f_normal_low
    debbie @ -m_talk "Mhmm."
    show anon f_shy_down
    hide debbie with dissolve
    pause
    call popup ('earn', 50)
    $ player.get_money(50)
    scene black with dissolve
    return

label dining_room_jenny_cedric_upset:
    scene expression game.timer.image("dining_room{}")
    show jenny b_breakfast_dressed a_phone f_normal_low zorder 1
    show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
    with dissolve
    pause
    show player 323e zorder 0 at Position(xpos=610,ypos=770) with dissolve
    anon "Good morning."
    hide player
    show anon f_looking_down_eating a_eating b_dinner_sitting_look_left zorder 0
    with dissolve
    jenny @ -m_talk "..."
    pause
    show jenny f_upset_down
    show anon f_surprised_food a_resting
    jenny "Asshole!!!" with hpunch
    jenny "Grr!"
    anon f_grumpy_food_left "What's your problem?"
    show jenny f_angry
    jenny "Fucking {b}Cedric{/b}!"
    anon f_surprised_food "{b}Cedric{/b}, your ex-boyfriend?"
    jenny "Tch, do you know any other people named {b}Cedric{/b}?!"
    anon f_grumpy_food_left "No."
    pause
    show jenny f_eyeroll
    jenny "... Moron."
    show jenny f_upset
    anon "Why are you always such a bitch towards me?"
    jenny "Umm, I dunno..."
    jenny "... Why are you always such a perv towards me?"
    show anon f_surprised_food
    debbie "What's going on in here?" with hpunch
    show debbie b_breakfast_potatoes f_sad with dissolve
    anon f_surprised_high_food @ -m_talk "..."
    jenny "Nothing, {b}Mom{/b}."
    debbie "I heard yelling."
    anon "She's just yelling at her phone like a crazy person."
    show jenny f_angry
    jenny "Screw you, {b}[firstname]{/b}!"
    debbie "Hey, cut it out, both of you!"
    show jenny f_upset_down
    anon "Sorry, {b}[deb_name]{/b}."
    jenny @ -m_talk "..."
    debbie "Why are you yelling at your phone, {b}[jen_name]{/b}?"
    show jenny f_upset_down
    jenny "{i}*Sigh*{/i} It's nothing..."
    jenny "... Just, stupid {b}Cedric{/b} is refusing to answer my texts."
    anon f_grumpy_food_left "I don't blame him."
    show jenny f_angry
    debbie "{b}[firstname]{/b}!"
    anon f_surprised_high_food @ -m_talk "..."
    show anon a_bowl f_shy_down
    debbie "I thought you broke up with {b}Cedric{/b}?"
    show jenny f_upset
    jenny "I did."
    show anon f_looking_down_eating a_eating with dissolve
    debbie "Then why are you texting him?"
    show anon f_looking_down_food a_resting with dissolve
    jenny "I need him for-"
    show anon f_surprised_food
    show jenny f_sad
    pause
    show jenny f_upset
    jenny "{i}*Ahem*{/i} I uhh, need his help... with work."
    show anon a_bowl f_shy_down with dissolve
    debbie f_normal "Oh."
    show anon f_normal with dissolve
    anon "{b}Cedric{/b} is going to help you with transcribing?"
    show jenny f_angry
    pause
    anon "That's what you said you're doing, right?"
    jenny @ -m_talk "..."
    show anon a_bowl f_shy_down with dissolve
    debbie "Why don't you just call him, dear?"
    show jenny f_upset
    jenny "I've been trying, he won't answer."
    debbie "Well, why don't yo-"
    "{i}*Sizzle*{/i}"
    show debbie f_sad
    pause
    show anon f_worried_high
    debbie "Oh, shoot!"
    hide debbie with dissolve
    debbie "I forgot about breakfast!"
    show anon f_shy_down
    show jenny f_grin
    pause
    jenny "Sounds like you're getting burnt bacon today, loser."
    anon f_worried "It's still better than that cereal you're eating."
    jenny "Whatever."
    show jenny f_upset_down
    show anon a_bowl f_shy_down with dissolve
    pause
    pause
    show anon f_looking_down_eating a_eating with dissolve
    show jenny f_angry
    jenny "Motherfucker!"
    show anon f_looking_down_food a_resting with dissolve
    jenny "Will you go down to {b}the gym{/b} and tell that asshole to call me?"
    anon f_surprised_food "Huh?"
    anon "No way!"
    show jenny f_upset
    jenny "Oh, c'mon {b}[firstname]{/b}."
    anon "I hate that guy!"
    anon "He always treats me like a little kid."
    show jenny f_grin
    jenny "Well, compared to him, you are a little kid."
    anon f_grumpy_food_left "Absolutely not."
    show jenny f_angry
    jenny "COME ON!"
    pause
    show jenny f_upset
    jenny "What if, I get naked for you again?"
    anon f_surprised_food "Completely naked?"
    show jenny f_eyeroll
    jenny "That's what I said, dummy."
    show jenny f_upset
    anon "Can I touch?"
    jenny "{i}*Sigh*{/i} I suppose..."
    jenny "... But just my tits."
    if M_jenny.get("dominance") <= 0:
        anon f_laugh od_dinner_sitting_boner "Sweet!"
    else:
        show anon f_looking_down_eating a_eating with dissolve
        pause
        anon f_grumpy_food_left "Just tits?"
        anon "Forget it, I've got better things to do."
        show anon f_looking_down_food a_resting
        show jenny f_angry
        pause
        jenny @ -m_talk "Grr!!"
        jenny "Fine, okay?!"
        show jenny f_upset
        jenny "You can touch whatever you want, just..."
    show anon f_normal
    show jenny b_breakfast_gettingup with dissolve
    jenny "... C'mon, let's go!"
    anon "Hold on, I wanna finish breakfast."
    show jenny b_breakfast_pulling
    hide anon
    with dissolve
    anon "!!!"
    hide jenny with dissolve
    jenny "No, right now!"
    $ player.go_to(L_home_kitchen)
    scene expression player.location.background_blur with None
    show jenny b_dressed_pulling2 f_upset:
        flip
        xoffset -150
    show debbie
    with dissolve
    anon "{b}[jen_name]{/b}, stop pulling me!"
    show jenny b_dressed_pulling1
    debbie "Breakfast is almost ready if you two wanna-"
    show debbie f_surprised
    pause
    debbie f_normal "Are you kids going somewhere?"
    show jenny f_normal
    jenny "{b}[firstname]{/b} is going to talk to {b}Cedric{/b} for me."
    debbie "Well, that's nice of him."
    pause
    show jenny b_dressed_pulling2
    anon "I was still eating, you know?!"
    show jenny b_dressed_pulling1 f_upset
    jenny "Shut up!"
    pause
    debbie f_laugh "It's nice to see you two finally getting along!"
    hide jenny
    with dissolve
    anon "Hey, that hurts!"
    show debbie f_normal
    pause
    debbie "I knew they'd bond eventually."
    hide debbie with dissolve
    pause
    $ player.go_to(L_home_sisbedroom)
    scene expression player.location.background_blur with None
    show jenny b_dressed_pulling2
    anon "Ack!"
    show anon f_skeptical
    show jenny b_dressed a_hips
    with dissolve
    anon "What is the rush?!"
    anon "I promise I'll go and talk to-"
    show anon f_surprised
    show jenny b_pull1 f_grin_down with dissolve
    pause
    show jenny b_pull2 with dissolve
    show anon f_worried_low
    anon "... To..."
    show jenny b_pull3 with dissolve
    show jenny b_pull4 with dissolve
    pause
    show jenny b_naked a_panties_remove f_grin_down with dissolve
    anon "..."
    show jenny b_naked_panties_remove_down with dissolve
    pause
    show jenny b_naked f_upset a_hips with dissolve
    jenny "I want {b}Cedric{/b} to call me ASAP!"
    show jenny f_eyeroll
    jenny "So let's hurry up and get this over with..."
    show jenny f_gross
    if M_jenny.get("dominance") <= 0:
        anon f_worried @ -m_talk "..."
        show jenny f_upset
        jenny "Are you going to touch them or what?!"
        show jenny f_gross
        anon f_surprised @ -m_talk "Hmm?"
        show jenny f_eyeroll a_breasts with dissolve
        pause
        show jenny f_gross a_hips with dissolve
        show anon f_shock a_up
        anon "OH!"
        show anon f_flirt a_idle
        anon "Right."
        hide anon
        show jenny b_groping_naked_touch_talk a_hips f_upset
        with dissolve
        anon "Wow!"
        show jenny b_groping_naked_touch with dissolve
        pause
        anon "They're really nice!"
        jenny "Tell me something I don't know..."
        pause
        show jenny b_groping_naked_suck_pre with dissolve
        jenny "Guys always love them."
        show jenny f_nipple1 b_groping_naked_suck a_up_clench
        jenny "!!!" with hpunch
        jenny "What are you-"
        pause
        show jenny f_nipple2
        jenny "Ahh..."
        pause
        jenny "I didn't say you could-"
        pause
        jenny "Ffffuuu-"
        pause
        jenny "Ngghhh!!"
        show jenny f_upset b_groping_naked_cover
        show anon f_depressed
        with dissolve
        jenny "Alright, stop!!"
        show anon f_worried
        anon "What's the problem?"
        jenny "That's plenty for today!"
        jenny "Go talk to {b}Cedric{/b}."
        anon @ f_skeptical "Ugh, alright."
        anon "Where did you say I could find him?"
        jenny "He'll probably be at the Gym, {b}that meathead is always at the Gym{/b}."
        anon f_laugh "On it."
        hide anon with dissolve
        pause
        show jenny b_groping_naked_orgasm f_nipple3
        with dissolve
        jenny "( Hmm, not bad for a little virgin loser... )"
        pause
        scene black with fade
    else:

        show anon f_flirt
        anon "O-okay."
        hide anon
        show jenny f_nipple1 b_groping_naked_suck a_up_clench
        jenny "!!!" with hpunch
        pause
        show jenny f_nipple2
        jenny "Jesus, you're just jumping right into-"
        jenny "Ahh!"
        pause
        show jenny f_nipple3
        jenny "Mmm."
        pause
        show jenny f_nipple1 b_groping_naked_finger
        jenny "Oh, shit!"
        show jenny f_nipple2
        pause
        jenny "Ffffuuu-"
        pause
        jenny "I'm gonna!"
        show anon f_surprised:
            xoffset 0
        show jenny b_groping_naked_orgasm f_nipple2
        jenny "Ngghhh!!!" with flash
        pause
        pause
        show jenny b_groping_naked_cover a_up_clench f_upset
        jenny "Haah... Fuck!"
        show anon f_worried
        anon "Did you just cum?"
        show jenny f_angry
        jenny "What? NO!"
        anon f_laugh "Yes, you did! Look at my fingers!"
        show anon a_up with dissolve
        jenny "Shut up!"
        show anon a_idle f_normal
        pause
        jenny "That's plenty for today!"
        anon "Heh, you just squirted in my hand!"
        jenny "I said shut up!!!"
        jenny "Go talk to {b}Cedric{/b}."
        anon f_worried "Ugh, alright."
        anon @ f_skeptical "Where did you say I could find him?"
        show jenny f_upset
        jenny "He'll probably be at the Gym, {b}that meathead is always at the Gym{/b}."
        anon f_normal "On it."
        hide anon with dissolve
        pause
        show jenny b_groping_naked_orgasm f_nipple3 with dissolve
        jenny "( Where the hell did that come from?! )"
        scene black with fade
    return

label dining_room_jenny_have_breakfast_3:
    scene expression game.timer.image("dining_room{}") with None
    show debbie b_breakfast_sitting zorder 1 with None
    show anon b_dinner_sitting f_normal zorder 0
    with dissolve
    show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
    with dissolve
    anon "Mmm, that was so good {b}[deb_name]{/b}!"
    anon "You're the best cook in the whole world!"
    debbie @ f_laugh "Aww, hehe!"
    debbie "Thanks, sweetie."
    anon "You want help with the dishes?"
    debbie "Oh, no..."
    debbie "I can handle it just fine. Don't you worry!"
    debbie "I'm in such a good mood, now that {b}[jen_name]{/b} found herself a job."
    debbie "I was so worried about her!"
    anon @ f_laugh "Heh, yeah."
    debbie "Transcribing..."
    debbie "I didn't know she had it in her!"
    anon f_worried "Uh huh..."
    show anon f_shy_down
    debbie "Oh, listen to me blathering on."
    debbie "I'm sure you have a million things you'd rather do than listen to me."
    anon f_worried "No, not at all!"
    anon f_normal "I enjo-"
    debbie "You just run along now and have a good day, alright?"
    pause
    anon "Okay."
    pause
    anon "Thanks again for breakfast."
    debbie "My pleasure, sweetie."
    hide anon with dissolve
    $ player.go_to(L_home_entrance)
    scene expression player.location.background_blur
    show anon f_worried
    with fade
    anon @ -m_talk "( I can't believe {b}[deb_name]{/b} bought that transcribing story... )"
    pause
    show anon a_thinking f_thinking with dissolve
    anon @ -m_talk "( Hmm, I wonder what {b}[jen_name]{/b} is really up to? )"
    hide anon with dissolve
    return

label dining_room_jenny_have_breakfast_2:
    scene expression game.timer.image("dining_room{}")
    show jenny b_breakfast_dressed a_phone f_normal_low zorder 1
    show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
    with dissolve
    pause
    show player 323e zorder 0 at Position(xpos=610,ypos=770) with dissolve
    anon "Morning."
    hide player
    show anon b_dinner_sitting_look_left a_bowl f_shy_down zorder 0
    with dissolve
    pause
    show anon f_looking_down_eating a_eating with dissolve
    pause
    show anon f_grumpy_food_left a_resting with dissolve
    anon "Hello?!"
    show jenny f_upset_down
    jenny "Hmm, what?!"
    anon "What's your problem?"
    jenny "Nothing, leave me alone."
    show anon a_bowl f_shy_down with dissolve
    anon @ -m_talk "..."
    pause
    jenny @ f_eyeroll "Ugh, this stupid Sluttygram thing is a waste of time!"
    anon f_worried "Those pictures didn't help?"
    jenny "They did but it's just not making me enough money..."
    anon "Yeah, well, Sluttygram is pretty small potatoes compared to what's out there..."
    show jenny f_upset
    jenny "What do you mean?"
    anon "You do realize that porn exists, right?"
    jenny "Yeah, so?"
    anon "Why would anyone pay good money to look at sexy photos with no nudity when they can watch hardcore porn, for free?!"
    show jenny f_eyeroll
    jenny "Umm, I dunno... How about because I'm hot and those porno skanks aren't?!"
    show jenny f_upset
    anon @ f_laugh "You're joking, right?"
    show jenny f_angry
    jenny "No, shut up!"
    show jenny b_breakfast_gettingup f_upset with dissolve
    jenny "Don't pretend like you don't think I'm hot!"
    anon f_surprised_forward "..."
    show jenny f_angry
    jenny "Say it!"
    return

label dining_room_jenny_have_breakfast_2_youre_hot:
    show anon f_worried
    anon "You're hot."
    show jenny f_angry
    jenny "Damn right!"
    show jenny b_breakfast_dressed a_phone f_upset_down with dissolve
    show anon a_bowl f_shy_down with dissolve
    pause
    show anon f_looking_down_eating a_eating with dissolve
    pause
    show anon f_grumpy_food_left with dissolve
    anon "But it's still small potatoes."
    show anon f_looking_down_food a_resting
    jenny "Yeah, yeah..."
    pause
    jenny @ f_eyeroll "Grr, I need more money!!!"
    pause
    show anon a_bowl f_shy_down with dissolve
    show jenny f_upset
    pause
    jenny "Come with me."
    show anon f_worried with dissolve
    anon "Huh, where?"
    jenny "To my room, dummy."
    jenny "I've got a proposition for you."
    hide jenny with dissolve
    anon "Uhh, okay."
    anon @ -m_talk "( I hope I didn't piss her off... )"
    hide anon with dissolve
    return

label dining_room_jenny_have_breakfast_2_no:
    show anon f_looking_down_eating a_eating with dissolve
    pause
    show anon f_grumpy_food_left a_resting with dissolve
    anon "Wow, are you that desperate for attention?"
    show jenny f_upset
    jenny "What?!"
    jenny "That's not-"
    show jenny f_angry
    pause
    jenny "SHUT UP!"
    anon "Heh and you call me pathetic..."
    jenny "Grrr!!"
    hide jenny with dissolve
    show anon f_looking_down_food
    pause
    show debbie b_breakfast_potatoes f_sad with dissolve
    debbie "What's gotten into her this morning?"
    anon f_surprised_high_food "Who knows?"
    debbie "This whole job business must really be stressing her out."
    anon "Yeah, maybe."
    debbie "Poor thing."
    debbie "Here's some more breakfast, sweetie."
    show debbie b_breakfast_potatoes3 with dissolve
    pause
    show debbie b_breakfast_potatoes f_normal with dissolve
    anon f_surprised_high_food "Thanks, {b}[deb_name]{/b}!"
    show anon b_dinner_sitting a_bowl f_shy_down with dissolve
    hide debbie with dissolve
    pause
    anon "( I should probably go and check on {b}[jen_name]{/b}... )"
    anon "( I wasn't trying to be mean, she just really knows how to push my buttons. )"
    anon "( Not until after I eat this delicious breakfast though! )"
    show anon f_looking_down_eating a_eating with dissolve
    return

label dining_room_sis_breakfast_started:
    scene expression game.timer.image("dining_room{}")
    show jenny b_breakfast_dressed a_phone f_normal_low zorder 1
    show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
    show player 323d zorder 0 at Position(xpos=610,ypos=770)
    with fade
    player_name "( Huh. {b}[jen_name]{/b} is awake already? )"
    player_name "( She usually sleeps in. )"
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
