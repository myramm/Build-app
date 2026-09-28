label tuuku_button_eve_make_up_extort_tuuku:
    scene expression player.location.background_closeup with None
    show anon:
        xoffset -100
    show eve:
        flip
        xoffset 200
    show tuuku
    with dissolve
    anon "Hey there, {b}Tuuku{/b}."
    tuuku "Sup, {b}[firstname]{/b}?"
    tuuku @ a_point "What are you two lovebirds doing?"
    anon "We're planning a surprise dinner for {b}Grace{/b} and {b}Odette{/b}."
    tuuku f_surprised "Really?"
    eve f_happy "Yup, and you're going to buy us some wine."
    tuuku f_confused @ a_thumb "I am?"
    eve @ -m_talk "Mmhmm."
    tuuku "Why would I want to do something like that?"
    eve f_angry "Because you owe us for that shit that went down at the party the other night!"
    tuuku f_surprised "What?!"
    tuuku "I didn't have anything to do with that!"
    eve f_sexy "Hmm, I'm not sure {b}Grace{/b} will see it that way..."
    eve "Especially after I tell her you invited that guy!"
    tuuku f_annoyed "Tsk, seriously {b}Evie{/b}... Blackmail?"
    tuuku "{i}*Sigh*{/i} You're spending too much time around {b}Odette{/b}, you know that?"
    eve "Aww, don't be sad {b}Tuuku{/b}... It's for a good cause."
    tuuku @ f_eyeroll "Yeah, right."
    tuuku "I'll do it."
    tuuku "Just please, don't tell your sister that I know that guy."
    eve "We need it by tonight."
    tuuku "Yeah, yeah... I said I'll get it."
    hide tuuku with dissolve
    tuuku "Jesus, even the little one is manipulating me now..."
    eve f_angry a_point "It better be a nice expensive red too!"
    eve "None of that cheap boxed stuff!"
    show eve f_happy a_idle:
        unflip
        xoffset -300
    with dissolve
    eve @ f_laugh "See, piece of cake."
    anon "Hehe, quite the performance."
    eve "Thank you, thank you!"
    eve "Now you just need to go {b}pick up the lasagna at Tony's Pizza{/b}."
    eve "I'll get everything set up here."
    anon "Alright."
    hide anon with dissolve
    return

label tuuku_button_eve_party_speak_to_tuuku:
    scene expression player.location.background_closeup with None
    show tuuku f_confused:
        flip
        xoffset 300
    show pilly:
        xoffset 100
    with dissolve
    pilly "... Oh yeah, my income has tripled since I made the commitment."
    pilly "Don't have to worry about crackheads pulling any shit either."
    pilly "Nobody wants to mess with heavies like this, {b}Tuuku{/b}."
    tuuku @ a_rub "Ehh, I dunno man... I think it's all a little too big for me."
    tuuku "I just sell pot."
    pilly "You don't wanna be a little fish forever, do you?"
    show anon:
        xoffset -100
    show eve b_dress:
        flip
        xoffset 150
    with dissolve
    eve "Hey, {b}Tuuku{/b}."
    show tuuku f_nervous_back
    pilly "Wow, take a look at you!"
    pilly "You know this tight little package, {b}Tuuku{/b}?"
    eve f_nervous "Uhh..."
    show tuuku f_nervous
    tuuku "This is {b}Eve{/b}, she's a friend of mine."
    pilly "No shit?"
    tuuku "{b}Eve{/b} this is {b}Pilly{/b}."
    tuuku "He used to be a competitor of mine before he moved on to greener pastures."
    pilly "Pleasure to meet you, beautiful."
    eve "H-hello."
    show tuuku f_nervous_back
    anon "Competitor?"
    anon "What does that mean?"
    if M_roxxy.finished_state(S_roxxy_meeting_buyer):
        show tuuku f_nervous
        pilly "You look familiar..."
        pilly "Have we met before?"
        anon f_surprised_teeth "!!!"
        anon f_worried @ f_shock "N-nope, definitely not!"
    tuuku "This is {b}[firstname]{/b}, {b}Eve{/b}'s boyfriend."
    pilly "Ah, lucky fellow."
    show tuuku f_nervous_back
    tuuku "{b}Pilly{/b} here used to supply the best pot in all of Summerville."
    show tuuku f_normal
    tuuku "That was before I moved in and put him to shame, of course."
    pilly "Hah, you wish!"
    pilly "You're just lucky I'm too ambitious for the weed game, otherwise, you'd have no clients."
    show tuuku f_nervous_back
    eve f_confused "I'm confused."
    eve "What do you do exactly?"
    tuuku "You really don't wanna know, {b}Evie{/b}!"
    show eve f_normal
    show tuuku f_nervous
    pilly "I deal in the higher end stuff."
    pilly "You know, meth, coke, heroin, angel dust... That sort of stuff."
    show eve f_surprised
    anon f_surprised "!!!"
    eve f_nervous "O-oh."
    show tuuku f_nervous_back
    tuuku "Ehh, did you two need something?"
    eve @ -m_talk "Hmm?"
    eve "Oh, yeah."
    eve "{b}Odette{/b} wanted me to tell you that people were getting into your plants upstairs."
    tuuku f_surprised_back "Oh, fuck... Really?!"
    eve "Yup."
    tuuku f_normal "I gotta go handle that."
    tuuku "Catch you around, {b}Pilly{/b}!"
    pilly "Oh, you know it."
    hide tuuku with dissolve
    eve "We should probably get going too."
    pilly "Oh, so soon?"
    pilly "I was thinking maybe I could interest you in a sample?"
    show pilly a_weed_get with dissolve
    eve f_sad "N-no, that's alri-"
    show pilly a_weed_hold with dissolve
    pilly "Don't be scared."
    pilly "It's on the house, for beautiful ladies."
    anon "We're okay, thanks."
    pilly "I don't believe I was talking to you, was I?"
    anon f_surprised @ -m_talk "..."
    pilly "What do you say, darlin'?"
    pilly "Just try one hit."
    grace "What the fuck is going on here?"
    show grace f_angry:
        flip
        xoffset 400
    with dissolve
    pilly "Well, well, my day just keeps getting better and better..."
    pilly "What's your name, beautiful?"
    grace "My name is none of your fucking business."
    grace "What exactly are you trying to sell my sister?"
    pilly "Oh, this?"
    pilly "This is the good stuff, baby."
    pilly "You wanna try a little?"
    grace "Let me see it."
    show pilly a_idle
    show grace a_weed_hold
    with dissolve
    pause
    grace f_surprised @ a_weed_smell "!!!"
    grace "Is this fucking angel dust?!"
    pilly "Mmm, sounds like you've indulged before..."
    grace f_angry "Uh huh..."
    show grace a_weed_throw with dissolve
    pause
    show grace a_idle
    pilly "!!!" with hpunch
    pilly "What the fuck, bitch?!"
    grace "I want you off my property, right now!"
    pilly "Do you have any idea how much that shit is worth?"
    grace f_angry_yelling "It's not worth jack shit now, is it?"
    grace "Get out of here!"
    pilly "Y-you're going to regret th-"
    hide pilly
    show grace a_pull_pilly:
        unflip
        xoffset 100
    with dissolve
    pilly "What the-"
    show anon f_surprised
    eve f_surprised "!!!"
    anon "!!!"
    grace "Yeah, yeah... I don't want to hear it."
    pilly "Ouch!"
    hide grace
    hide pilly
    with dissolve
    grace "Get the fuck out!"
    pause
    show grace f_tired with dissolve
    grace "Fucking animals..."
    anon f_normal "Wow, you handled that guy like it was nothing!"
    grace "You two alright?"
    hide eve
    show grace a_hug_eve f_surprised
    with dissolve
    show anon f_flirt_grin
    grace "!!!"
    grace f_proud "Hehe, not my first rodeo."
    eve "I'm sorry I was a bitch to you earlier."
    grace "Shh, it's okay."
    show grace f_happy a_idle
    show eve b_dress:
        flip
        xoffset 150
    with dissolve
    grace "C'mon, I'm done with this bullshit party."
    hide grace
    hide eve
    with dissolve
    anon a_thinking f_thinking @ -m_talk "( What did she mean by that? )"
    scene black with fade
    pause
    $ player.go_to(L_tattooparlor_garage)
    scene expression player.location.background_blur with None
    show anon f_worried:
        xoffset -100
    show eve f_sad b_dress:
        flip
        xoffset 200
    show grace f_angry:
        flip
        xoffset 400
    grace "Alright, everyone!"
    grace @ f_angry_yelling "Party's over!"
    random_girl "You for real?"
    grace f_tired "Yes, I'm for real."
    grace "Get the fuck out, all of you."
    random_guy "Aww, man."
    grace "Go on, beat it!"
    eve "A-are you sure about this, {b}Grace{/b}?"
    grace @ f_tired_back "Yes."
    odette "What's going on?!"
    show odette f_sad:
        xoffset 100
    with dissolve
    odette "Why is everybody leaving?"
    grace f_angry "Some asshole was dealing angel dust and hassling {b}Eve{/b}!"
    odette "Oh, shit... Are you serious?"
    grace "Yeah."
    odette f_angry "I'll handle it, where is he?"
    grace "It's already been handled."
    odette f_normal "Okay, good."
    odette f_sad "That's no reason to break up the party though..."
    grace f_tired "{b}Odette{/b}, I'm through with this shit."
    grace "I don't enjoy it anymore and I don't want my sister around it."
    odette "O-okay, but you're overreacting-"
    grace f_angry "I'm not overreacting!!"
    grace "Don't you realize I have to get up in like five hours to get ready for tomorrow's appointments?!"
    odette @ -m_talk "..."
    grace f_tired "Either help me get these people out of our home or you can fucking go with them!"
    odette a_sides @ f_surprised "!!!" with hpunch
    grace "Do you understand me?"
    odette "Y-yes."
    grace "I'm taking {b}Eve{/b} upstairs."
    eve f_sad_right "I'll see you tomorrow, okay?"
    anon "Y-yeah."
    show eve b_dress_kiss1:
        unflip
        xoffset -450
    hide anon
    with dissolve
    pause
    hide eve
    show anon f_flirt_grin:
        xoffset -100
    show eve f_happy_right b_dress:
        flip
        xoffset 200
    with dissolve
    pause
    hide eve
    hide grace
    with dissolve
    pause
    show tuuku f_sad:
        xoffset -200
    with dissolve
    tuuku "{b}Grace{/b} looks pissed..."
    tuuku "What happened?"
    show tuuku f_nervous_back
    show anon f_worried
    odette "Some guy was trying to get {b}Eve{/b} to try angel dust."
    tuuku f_sad "Oh, fuck me."
    tuuku "{b}Pilly{/b}?"
    anon @ -m_talk "Mhmm."
    odette f_angry "Tch, don't tell me it was one of your fucking friends?!"
    tuuku f_annoyed_back @ a_arrest "N-no, not friend..."
    tuuku "Just a guy I know."
    tuuku "I didn't invite him or anything!"
    odette "You better not have!"
    odette "Go upstairs and get these fucking people out of here."
    tuuku "Y-yeah, okay."
    hide tuuku with dissolve
    pause
    odette f_sad a_head "{i}*Sigh*{/i} What the hell am I supposed to do now?"
    anon "You alright?"
    odette a_sides "{b}Grace{/b} has never talked to me like that before..."
    anon "I'm sure it's fine."
    anon "She's just having a rough night."
    odette "I dunno, I'm worried."
    pause
    anon f_normal "C'mon, I'll help you clean up."
    odette "Y-yeah, thanks."
    scene black with fade
    pause
    $ game.timer.tick(3)
    $ player.go_to(L_tattooparlor)
    scene expression player.location.background_blur with None
    show anon f_tired with dissolve
    anon @ -m_talk "( Wow, that got pretty heated... )"
    anon @ -m_talk "( At least everyone is more or less okay. )"
    pause
    anon @ a_thinking f_thinking -m_talk "( I wonder if there's a way I could help {b}Odette{/b} and {b}Grace{/b} sort this whole thing out? )"
    anon @ -m_talk "( Hmm, I'll have to think about it. )"
    pause
    anon @ -m_talk "( For now, it's getting late and I should head home. )"
    hide anon with dissolve
    return

label button_tuuku_intro_roof:
    scene expression player.location.background_closeup with None
    show anon
    show tuuku
    with dissolve
    tuuku "Sup, {b}[firstname]{/b}?"
    anon @ a_wave "Hey, {b}Tuuku{/b}."
    tuuku "What brings you up here?"
    return

label button_tuuku_intro_alley:
    scene expression player.location.background_closeup with None
    show anon
    show tuuku
    with dissolve
    tuuku "Sup, {b}[firstname]{/b}?"
    anon @ a_wave "Hey, {b}Tuuku{/b}."
    tuuku @ a_point "Looking to score some bud?"
    return

label button_tuuku_your_plants:
    anon @ a_point "Your plants."
    tuuku f_confused "You got a thing for plants or something?"
    anon @ f_thinking "Mm, you could say that."
    anon "I just recently developed an interest in gardening."
    tuuku "Oh?"
    anon "Yeah, my friend {b}Diane{/b} has been paying me to assist with hers."
    tuuku f_normal @ a_point "She growing any bud?"
    anon f_worried "Bud?"
    tuuku f_confused "You know, weed?"
    tuuku "Reefer, herb, grass, sticky icky?"
    anon @ -m_talk "..."
    tuuku f_annoyed @ a_rub "Marijuana."
    anon f_normal @ f_laugh "Oh, uhh... Definitely not!"
    tuuku f_normal @ f_laugh "Haha!"
    return

label button_tuuku_known_the_girls_long:
    anon "You all seem really close."
    tuuku "Yeah, we've been friends forever."
    tuuku "{b}Odette{/b} likes to bust my balls and {b}Grace{/b} has become a little boring these past few years, but they're practically family at this point."
    anon "That's really cool man."
    tuuku @ -m_talk "Mmhmm."
    return

label button_tuuku_youre_selling_here:
    anon f_surprised "You're selling here?"
    tuuku @ a_shrug f_confused "That surprises you?"
    anon f_worried a_behind_head "Y-yeah, I guess."
    tuuku "So long as I keep it outside the store, {b}Grace{/b} doesn't mind."
    anon a_idle "Isn't that kinda risky though?"
    anon "Given its proximity to your... Umm... Garden?"
    tuuku f_annoyed @ a_point "Whoa man, you gotta keep that shit on the down low!"
    anon "Oh, umm... Sorry."
    tuuku "Nobody knows about that 'cept the girls."
    anon "I didn't know."
    tuuku "We try to keep it hush-hush, you feel me?"
    anon f_normal @ f_snarky a_point "Y-yeah, I got it."
    tuuku f_normal "Good man."
    return

label button_tuuku_why_take_off:
    anon f_worried "Why'd you take off the other night?"
    tuuku f_confused @ -m_talk "Hmm?"
    anon f_unimpressed "You totally flaked on us when the cops showed up!"
    tuuku f_normal "You're damn right I did!"
    anon "Yeah well, we got into some serious trouble because of that whole incident."
    tuuku a_point "Word of advice."
    tuuku "The next time you're engaging in illegal activity and someone yells out, \"Oh shit, it's the fuzz!\""
    tuuku "Don't stand there like a deer in the headlights."
    anon @ a_point_self "I don't bail on my friends."
    tuuku a_idle @ a_shrug "Tch, c'mon... Don't be like that."
    tuuku "I can't be messing with no cops, {b}[firstname]{/b}... I got priors!"
    anon @ a_up "Whatever, man."
    return

label button_tuuku_just_looking_around:
    anon "You've got a pretty sweet set-up here."
    tuuku "Yeah, it's not bad."
    tuuku "It's a pain in the ass to keep the plants alive during the winter months but I've been managing so far."
    anon "I'll let you get back to it."
    tuuku "See ya, {b}[firstname]{/b}."
    hide anon with dissolve
    return

label button_tuuku_no_thanks:
    anon "Just thought I'd say hi."
    tuuku "Right on."
    tuuku @ a_thumb "If you change your mind, you know where to find me."
    anon @ a_wave "See ya, {b}Tuuku{/b}."
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
