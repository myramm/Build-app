label button_grace_why_meditate_naked:
    anon f_worried "Why do you meditate naked?"
    grace a_cover "It's part of the relaxation technique in my book."
    grace "Being free with your body helps the anxiety evaporate."
    anon f_surprised "Anxiety evaporates?"
    grace @ f_laugh "Hehe, supposedly..."
    pause
    anon f_worried "Is it working?"
    grace "Yeah, I think so."
    pause
    grace f_uneasy_back "Sorry, I know it's probably weird seeing your girlfriend's sister naked all the time..."
    anon f_flirt a_point "Heh, I'm not complaining."
    show grace f_uneasy
    anon "You've got an amazing body!"
    show anon f_flirt_grin a_idle with dissolve
    grace f_uneasy a_idle "O-oh, umm... thanks, {b}[firstname]{/b}."
    anon f_flirt "You're welcome."
    return

label button_grace_is_she_here:
    anon f_worried "Is she here?"
    grace "Y-yeah."
    grace "{i}*Ahem*{/i} If she isn't in her room, then she's probably up on the roof."
    anon @ f_laugh "Alright, thanks!"
    grace "N-no problem."
    show anon f_flirt_grin
    pause
    show grace f_uneasy_back
    show anon f_normal
    pause
    show grace f_uneasy
    return

label button_grace_just_saying_hi:
    anon "Sorry, I can't stay."
    anon "I just saw you in here working and thought I'd say hello."
    grace f_happy @ f_laugh "O-oh, well, that's nice of you!"
    pause
    grace "You should come by later."
    anon "Oh?"
    grace "Yeah!"
    pause
    grace "Y-you know, to see my sister."
    anon @ f_laugh "Hehe, will do!"
    grace "Later, {b}[firstname]{/b}."
    hide anon with dissolve
    return

label button_grace_you_and_odette:
    anon "Are you and {b}Odette{/b} doing alright?"
    grace f_happy @ f_laugh "Yeah, she's been a huge help lately!"
    grace "It's kinda hard to believe, if I'm being honest."
    anon "I'm glad to hear it."
    anon @ f_flirt "You two make a cute couple."
    if player.location == L_tattooparlor_interior:
        grace a_neck f_uneasy "Oh, uhh... thanks, {b}[firstname]{/b}."
    else:
        grace f_uneasy "Oh, uhh... thanks, {b}[firstname]{/b}."
    show anon a_point with dissolve
    if player.location == L_tattooparlor_interior:
        show grace f_uneasy a_crossed with dissolve
    else:
        show grace f_uneasy
    anon "You're welcome."
    show anon a_idle f_normal with dissolve
    return

label button_grace_really:
    anon f_surprised "Really?"
    grace f_happy "Yes."
    grace "All I hear nowadays is, \"{b}[firstname]{/b} this...\" or \"{b}[firstname]{/b} that...\""
    anon f_normal @ f_laugh "Haha!"
    grace "Don't get me wrong, it's really good you two are becoming so close."
    grace "I'm not sure I've ever seen her this happy before."
    anon "Yeah, I'm happy about it too."
    grace f_laugh @ f_angry a_idea "Just make sure you take good care of her, otherwise, I'll sic {b}Odette{/b} on you."
    anon @ f_worried a_behind_head "Hehe, I will."
    show grace f_normal
    return

label button_grace_bike:
    anon "Is your bike still running well?"
    grace @ f_proud "Oh, like a dream!"
    grace "Thanks again for fixing it."
    anon "No problem."
    anon "Where'd you get it anyways?"
    grace "I pulled it out of a scrap heap at the dump when I was nineteen."
    anon @ f_surprised "Really?!"
    grace @ f_proud "Yup."
    grace "It took me two years to earn the money to fix her up."
    anon "It's such a pretty bike."
    grace "Aww, thank you."
    grace @ f_sexy "Perhaps I'll take you for a ride sometime?"
    anon @ f_laugh a_cheering "I'd love that!"
    return

label button_grace_eve_around:
    anon "{b}Eve{/b} around?"
    grace "Hmm, I'm not sure."
    grace "If you can't find her at school, then she's probably hanging out up on the roof."
    grace @ a_idea "She's been spending her free time there since the park incident."
    anon "Oh, okay."
    anon @ f_laugh "Thanks!"
    return

label button_grace_apologize:
    anon f_worried "I wanted to apologize about the whole thing in the park..."
    grace a_hips_mad "No, it's not your fault, {b}[firstname]{/b}."
    anon "It really was just bad luck."
    grace f_tired @ f_eyeroll "Oh, sure... bad luck."
    grace "It was bad luck that my sister stole half a pound of weed and then lit up in public."
    show anon f_surprised_teeth
    pause
    anon f_worried @ f_thinking a_thinking "Well, when you put it like that..."
    grace f_normal "Look, I get it."
    grace "{b}Odette{/b} and I did stupid stuff in college too."
    grace f_sad "I just really hoped that {b}Eve{/b} would act smarter than we did."
    anon f_worried @ -m_talk "..."
    grace f_suspicious "Can you do me a favor?"
    anon "S-sure."
    grace f_normal "Keep an eye on my sister and make sure she doesn't do anything stupid like that again."
    anon f_normal a_behind_head "Yeah, I'll try."
    grace "Thanks, {b}[firstname]{/b}."
    show anon a_idle with dissolve
    return

label button_grace_how_work_going_e6:
    anon "How's work going?"
    grace f_sad a_neck "Slow."
    anon "Not many customers, huh?"
    grace "Nope."
    pause
    grace f_normal a_idle "You know, considering we're the only tattoo parlor in town, you'd think we'd have a lot more business."
    anon "Yeah, but then again, it is a really small town."
    grace "True."
    grace "I probably should have bought a place in the city..."
    pause
    grace @ f_sad_down "{i}*Sigh*{/i} Too late now."
    return

label button_grace_how_work_going_e18:
    grace @ f_laugh "Things have really picked up, thanks to {b}Eve{/b} and you!"
    anon "That's good to hear."
    grace @ f_eyeroll "Yeah, tell me about it."
    grace "I was really worried I might lose the shop."
    grace "Now, the only thing I worry about is finding time for all these customers!"
    anon @ f_laugh "Haha!"
    anon @ f_snarky a_point "Just don't overwork yourself, okay?"
    grace "Oh, I'm fine."
    grace "No need to worry about me."
    return

label button_grace_odette_and_tuuku:
    anon f_skeptical "So, do {b}Odette{/b} and {b}Tuuku{/b} live here with {b}Eve{/b} and you?"
    grace @ f_eyeroll "Uhh, yes and no."
    grace "They have their own places, but most of their time is spent here."
    grace "{b}Odette{/b} sleeps on our couch most nights and {b}Tuuku{/b} has a tent up on our roof."
    anon f_surprised "He sleeps on your roof?"
    grace "Yeah, sometimes."
    pause
    anon f_confused "Do they pay you rent or something?"
    grace @ f_laugh "Oh, no!"
    grace "I couldn't ask them to do that."
    anon f_surprised "Why not?"
    grace "We've been friends since we were children, they're practically family!"
    anon f_normal "That's really nice of you."
    grace @ f_happy "Yeah, I know."
    grace "Don't tell them I said this but it's nice having them around."
    grace @ f_eyeroll "I'd probably go stir crazy, stuck in here all day by myself."
    return

label button_grace_yup:
    anon "She around?"
    show grace f_thinking
    pause
    grace f_normal "Hmm, I'm not sure..."
    grace "If you can't find her at school, then she's probably hanging out in the park."
    grace "She likes to draw there."
    anon "Oh, okay."
    anon @ f_laugh "Thanks!"
    return

label button_grace_nevermind:
    anon "I'm just looking around, thanks."
    grace "Okay."
    grace @ a_idea "All my previous work is in a book over by the door, if you wanna check it out."
    anon "Alright, will do."
    hide anon with dissolve
    return

label button_grace_i_should_go:
    anon "Actually, I just wanted to pop in and say hi."
    anon "Could you tell {b}Eve{/b} I stopped by?"
    grace "Sure."
    anon @ a_wave "Thanks, {b}Grace{/b}."
    grace "See ya, {b}[firstname]{/b}."
    hide anon with dissolve
    return

label button_grace_tattoo:
    grace "You interested in getting some ink?"
    anon @ f_surprised -m_talk "Hmm?"
    anon "Oh, heh... no thanks."
    anon f_unimpressed "That would be way too much work for the developers to implement... I mean the art assets alone woul-"
    grace f_suspicious "Huh?"
    pause
    anon a_behind_head f_grin @ f_surprised "I mean, my landlady would kill me!"
    grace "O-oh."
    grace f_normal "Yeah, I can understand that."
    grace "My mother was the same way when I was your age."
    pause
    grace "Just let me know if you change your mind."
    show anon a_idle with dissolve
    return

label grace_button_intro_e1e5:
    scene expression player.location.background_closeup with None
    show anon
    show grace
    with dissolve
    grace "Welcome to {b}Sugar Tats{/b}."
    grace "How can I help you?"
    return

label grace_button_intro_e5e14:
    scene expression player.location.background_closeup with None
    show anon
    show grace
    with dissolve
    grace "Welcome to {b}Sugar Tats{/b}."
    grace "How can I he-"
    grace "Oh, hey {b}[firstname]{/b}."
    anon @ a_wave "Hey, {b}Grace{/b}."
    grace @ f_suspicious "You here to see my sister?"
    return

label grace_button_intro_e14e20:
    scene expression player.location.background_closeup with None
    show anon
    show grace
    with dissolve
    anon @ a_wave "Hey, {b}Grace{/b}."
    grace "Hey, {b}[firstname]{/b}!"
    grace f_happy "It's good to see you!"
    anon "Y-yeah, you too."
    return

label grace_button_intro_final_apartment:
    scene expression player.location.background_closeup with None
    if M_grace.get("nude_meditation_first"):
        show anon f_shock with dissolve
    else:
        show anon f_worried a_behind_head with dissolve
    anon "{b}G-Grace{/b}?"
    grace "!!!"
    show grace f_uneasy b_naked a_cover with dissolve
    grace "H-hey, {b}[firstname]{/b}..."
    if M_grace.get("nude_meditation_first"):
        $ M_grace.set("nude_meditation_first", False)
        show anon f_worried a_behind_head with dissolve
    anon "I'm sorry to interrupt you."
    grace "It's okay, just give me a second to get some clothes on..."
    anon f_flirt a_idle "No worries, I don't mind."
    grace f_uneasy a_idle @ f_uneasy_back "Heh, umm... {b}Eve{/b} didn't tell me you were stopping by?"
    return

label grace_button_intro_final_tattoo:
    scene expression player.location.background_closeup with None
    show anon
    show grace
    with dissolve
    anon "Hey, {b}Grace{/b}."
    grace "Hey, {b}[firstname]{/b}!"
    grace "Looking for my sister?"
    grace @ f_eyeroll "You know, she can't shut up about you..."
    return

label grace_button_massage_sex_proposal:
    scene location_tattoo_apartment_oil
    show odette b_massage_leaning f_smirk_down
    show grace b_massage_laying
    show odette_arms_massage_leaning_a_rub1_2
    with dissolve
    grace "I just can't believe the piercings are bringing in so much money..."
    odette "Hehe, I told you it would make up the difference."
    grace "Yeah, but it's bound to decline eventually."
    odette "Could you please relax?"
    odette "We're trying to release your tension, not create more!"
    grace "You're right, I'm sorry."
    pause
    grace "This does feel really good..."
    odette "Just enjoy it, babe."
    odette "You've been working yourself too hard."
    grace "Mmm, I know."
    hide odette_arms_massage_leaning_a_rub1_2
    show odette b_massage a_bottle1
    with dissolve
    odette "Close your eyes and let me work my magic."
    show odette a_bottle2 with dissolve
    pause
    show odette b_massage_leaning
    show odette_arms_massage_leaning_a_rub1_2
    with dissolve
    pause
    odette "Let all your worries melt away..."
    odette "... {b}Odette{/b}'s gonna handle everything."
    grace "It's so weird hearing you say stuff like that."
    odette "Shhh!"
    grace "Hehehe!"
    pause
    grace "{b}Eve{/b} seems really happy lately, doesn't she?"
    odette "Definitely."
    grace "I think this relationship she's started up with {b}[firstname]{/b} is doing her a lot of good."
    odette "His big dick is what's doing her good..."
    grace "{b}Odette{/b}!!"
    odette "... Don't pretend like you aren't curious!"
    grace "..."
    grace "You really think it's as big as {b}Tuuku{/b} says?"
    odette "Well, he has been known to exaggerate..."
    odette "... But if it is true... can you imagine?"
    grace "Hmm?"
    odette "{b}[firstname]{/b}'s dick."
    grace "..."
    odette "It's been a long time since you had a real one, huh?"
    grace "Heh, that's an understatement."
    odette "Just imagine how good it would feel after all this time..."
    hide odette_arms_massage_leaning_a_rub1_2
    show odette_arms_massage_leaning_a_rub3_4
    with dissolve
    grace "{i}*Gasp*{/i}"
    odette "His strong hands, caressing your thighs."
    grace "{b}Odette{/b}..."
    odette "His warm mouth, teasing your nipples."
    grace "We shouldn't be talking about-"
    odette "His big."
    odette "Thick."
    grace "Ahh!"
    odette "Throbbing cock... sliding inside you."
    grace "Ngh!"
    odette "Ramming into you."
    show expression "characters/grace/grace_sex_mc_foreground.png" with dissolve
    odette "Harder and harder."
    grace "Oh, god."
    anon "Ehh, h-hey you two..."
    grace "!!!"
    grace "OH SHIT!!"
    show odette b_massage a_idle f_smirk
    hide odette_arms_massage_leaning_a_rub3_4
    show grace b_massage f_sad a_cover
    with dissolve
    grace "{b}[firstname]{/b}?!"
    odette @ f_laugh "Hehehe!"
    grace "H-how long were you-"
    odette "Relax, he just got here."
    anon "Sorry, I didn't mean to interrupt."
    anon "I'm just here to see {b}Eve{/b}."
    grace "O-oh."
    grace "She's in her room, playing games."
    show grace f_sad_down
    anon "Alright, I'll let you two get back to-"
    odette "Well, hold on a second."
    odette "You know, it occurs to me that we never properly thanked you for everything you've done for us..."
    anon "Hmm?"
    odette "... I feel like you deserve a massage or something, at least."
    anon "!!!"
    grace f_sad_back "{b}Odette{/b}, we can't just-"
    odette "Think about it, babe!"
    odette "I mean, he did help grow your business with that flyer idea..."
    odette "... And he inspired me to help out around here..."
    odette "... AND he's changed our little {b}Evie{/b}'s life in a positive and meaningful way!"
    grace "Y-yeah, but-"
    odette "You said it yourself, you've never seen her so happy."
    grace f_sad_down "..."
    odette "Why don't you undress and come lay down over here?"
    odette "{b}Grace{/b} has the most incredible hands."
    grace f_angry_back "{b}ODETTE{/b}!!!"
    odette "What?"
    grace "He's {b}Eve{/b}'s boyfriend!"
    odette "I know that."
    odette "It's just an innocent little massage, you big prude..."
    grace a_idle f_tired_back "Damn it, quit calling me a prude!"
    odette @ f_eyeroll "I'll quit when you stop acting like one."
    grace f_sad_down @ f_eyeroll "Ugh."
    pause
    odette "See, she's willing."
    grace f_tired_back "Hey, I did not say that!"
    odette "Hehehe!"
    odette "What do you think, big fella?"
    odette "{b}Evie{/b} can wait a little longer, can't she?"
    show grace f_sad
    return

label grace_button_massage_sex_proposal_yeah:
    anon "Yeah, I guess..."
    anon "... As long as we're quick."
    odette @ f_laugh "Hehehe!"
    odette "Well, hopefully not TOO quick."
    grace f_tired_back "{b}Odette{/b}!!"
    odette "Relax, I'm kidding around..."
    grace @ -m_talk "..."
    odette "Take off those clothes and lie down here, {b}[firstname]{/b}."
    show grace f_sad
    return

label grace_button_massage_sex_proposal_dunno:
    anon "She's kinda expecting me."
    grace f_sad_back "See, he's not even interested."
    odette "Tsk, of course he is!"
    odette "{b}Eve{/b} won't even realize you're late; she's in her own little world when she's gaming."
    grace f_tired_back "{b}Odette{/b}..."
    odette "This will just take like fifteen minutes and then you can head on in to see her."
    anon "..."
    show grace f_sad
    odette "C'mon big fella, what do you say?"
    anon "Just fifteen minutes?"
    odette "Yeah, more or less..."
    grace "{b}[firstname]{/b}, you really don't have to do this if you don't want-"
    odette "You hush!"
    odette "It'll be fine, get over here."
    return

label grace_button_party_speak_to_tuuku:
    scene expression player.location.background_closeup with None
    show anon:
        xoffset -100
    show eve b_dress:
        flip
        xoffset 200
    show grace a_beer
    with dissolve
    grace "You two having fun?"
    anon "Yeah."
    grace f_sad "You're not drinking too much, are you?"
    eve f_angry @ f_eyeroll "No, {b}Sis{/b}... I've only had one beer so far."
    grace f_normal "Good."
    pause
    eve "You know, most of the party is upstairs, right?"
    grace @ f_eyeroll "Yeah, I know."
    eve "So why are you sulking down here in the garage?"
    grace f_angry "I'm not sulking!"
    grace @ f_tired "I just don't feel comfortable with all these strangers in our home."
    grace "They could rob us blind."
    eve @ f_eyeroll "Psh, unlikely."
    hide anon with dissolve
    return

label grace_button_party_generic:
    scene expression player.location.background_closeup with None
    show anon
    show grace a_beer
    with dissolve
    grace "Go on and head up, {b}[firstname]{/b}."
    grace "I'll let {b}Eve{/b} know you're here."
    anon "Thanks."
    random_guy "Damn, this bike is boss!"
    grace f_angry "Hey, be careful with that!"
    show anon f_surprised_teeth
    grace "I just got it up and running again!"
    hide anon with dissolve
    return

label grace_button_party_speak_to_grace:
    scene expression player.location.background_closeup with None
    show anon
    show grace a_beer f_tired:
        flip
        xoffset 500
    with dissolve
    grace "Hey c'mon, man... stop ashing on my couch!"
    show anon f_worried
    random_girl "Oh, uhh... my bad."
    grace "I know it's a piece of shit but I prefer it to a pile of kindling..."
    anon "{b}Grace{/b}?"
    show grace f_tired a_beer:
        unflip
        xoffset 0
    with dissolve
    grace "Huh?"
    grace "Oh, hey {b}[firstname]{/b}."
    anon f_normal "Having fun?"
    grace @ f_eyeroll "Oh yeah, tons..."
    anon "What are you doing down here?"
    grace "Making sure nobody runs off with any of our shit."
    anon f_worried "Oh, umm... okay."
    grace "I can't believe {b}Odette{/b} thought this was a good idea..."
    anon "Yeah, where is she anyways?"
    grace "Up on the roof I think."
    anon "Oh, okay."
    pause
    anon "Is {b}Eve{/b} up there too?"
    grace f_sexy "I think she's still inside getting ready."
    grace f_normal "Why don't you head on up and I'll send her your way?"
    anon f_normal "Yeah, okay."
    anon "Thanks!"
    grace "No problem."
    show anon:
        xoffset 500
    show grace:
        xoffset -500
    with MoveTransition(2)
    pause
    show grace with dissolve:
        flip
        xoffset 0
    grace f_normal "Oh, hey {b}[firstname]{/b}?"
    show anon:
        flip
        xoffset 0
    with dissolve
    anon @ -m_talk "Hmm?"
    grace f_happy "I'm really glad you're here."
    anon @ f_laugh "Y-yeah, me too."
    grace f_tired "Tell {b}Odette{/b} she's a rotten cunt for me."
    anon @ a_behind_head "Haha, okay."
    hide anon with dissolve
    return

label grace_button_party_start:
    scene expression player.location.background_closeup with None
    show anon
    show grace f_tired
    with dissolve
    grace "Oh right, the stupid party."
    show anon f_worried
    grace "{i}*Sigh*{/i} I don't even wanna think about it!"
    grace "It's {b}Odette{/b}'s thing and I'm leaving her to it."
    anon "You seem really annoyed about it?"
    grace f_angry "Of course I'm annoyed!"
    show anon f_surprised_teeth
    grace "The last thing I wanna do after a twelve-hour shift is babysit a bunch of drunken idiots!"
    show grace f_tired
    anon f_worried @ a_behind_head "I'm sure it'll be fine."
    grace @ f_eyeroll "Yeah, right."
    pause
    grace f_sad "Just do me a favor {b}Saturday{/b} and keep an eye on my sister, will you?"
    grace "I'm worried she'll drink too much and get sick again."
    anon "I can do that."
    grace f_normal "Thanks, {b}[firstname]{/b}."
    return


label grace_button_talked_to_grace:
    scene expression player.location.background_closeup with None
    show anon a_beer
    show grace f_happy a_beer
    with dissolve
    grace "I really hope {b}Odette{/b} doesn't get too crazy tonight..."
    anon @ f_skeptical "Just exactly how crazy does {b}Odette{/b} get when she's drinking?"
    grace "Oh, don't worry."
    grace "I'm sure you'll find out..."
    hide anon with dissolve
    return

label grace_button_eve_talk_to_girls:
    scene expression player.location.background_closeup with None
    show anon a_beer
    show grace f_happy
    with dissolve
    anon "Here you go."
    show anon a_idle
    show grace a_beer
    with dissolve
    grace "Thanks."
    anon "No problem."
    show grace a_beer_drink f_proud m_talk with dissolve
    pause
    show anon b_dressed_pickup with dissolve
    show grace f_happy a_beer -m_talk with dissolve
    grace @ -m_talk "Mmm!"
    show anon b_dressed a_beer with dissolve
    anon "You sure got that fire started quickly."
    grace "Yeah, I guess those six years in girls scouts really paid off, huh?"
    anon "Hehe, seems like it."
    pause
    grace "Hey, by the way..."
    grace "... You did a great job the other night."
    anon @ -m_talk "Hmm?"
    grace "You know, when my sister opened up to you..."
    grace "About her... you know."
    show grace a_beer_drink f_proud m_talk with dissolve
    if M_eve.biggus_dickus:
        anon f_worried @ f_surprised "The penis?"
        show grace a_beer f_happy -m_talk with dissolve
        grace "Y-yeah."
        grace "It's really awesome that you're okay with it."
        anon f_snarky "Why wouldn't I be?"
        anon f_normal "Your sister is a wonderful person and I enjoy hanging out with her so much..."
        anon "... That other stuff isn't important, you know?"
        grace f_uneasy "Well, yeah... I know..."
        grace "... But not everybody thinks that way and {b}Eve{/b} has faced a lot of adversity, just from trying to be herself."
        grace "So, she's pretty self-conscious about it."
        anon "I think she's beautiful."
    else:
        anon f_worried @ f_surprised "The scar?"
        show grace a_beer f_sad -m_talk with dissolve
        grace "Well, that... and all the emotional baggage."
        grace "She was a wreck for a long time after our parents died."
        grace "Actually, we both were."
        anon f_worried "I understand, believe me."
        grace @ f_surprised "Oh, that's right!"
        grace "{b}Eve{/b} told me, you just lost your dad..."
        anon "Y-yeah."
        grace "... I'm really sorry, {b}[firstname]{/b}."
        grace @ f_eyeroll "Here I am complaining about our problems from years ago, and your wounds are fresh-"
        anon "No, really... it's fine."
        anon "I'm getting through it."
        pause
        anon f_normal "Honestly, I think talking about it and trading painful experiences with others really helps heal, you know?"
    show grace f_happy
    pause
    grace "You're a really great guy, {b}[firstname]{/b}!"
    grace "I'm glad {b}Eve{/b} found you."
    anon @ f_laugh "So am I."
    pause
    show anon a_beer_drink f_smoke
    show grace a_beer_drink f_proud m_talk
    with dissolve
    pause
    show anon a_beer f_normal
    show grace a_beer f_happy -m_talk
    with dissolve
    grace "Man, I wish someone felt that way about me!"
    anon "Are you sure somebody doesn't?"
    grace f_uneasy @ -m_talk "Hmm?"
    anon "Nothing... never mind."
    pause
    anon a_beer_cheer "Cheers?"
    pause
    grace f_happy a_beer_cheer "Cheers!"
    "{i}*Clink*{/i}"
    show anon a_beer_drink f_smoke
    show grace a_beer_drink f_proud m_talk
    with dissolve
    pause
    show anon a_beer f_normal
    show grace a_beer f_happy -m_talk
    with dissolve
    return

label button_grace_odette_eve_pot_cheerup:
    scene expression player.location.background_closeup with None
    show anon f_worried
    show odette f_smirk:
        xoffset -200
    show grace
    with dissolve
    grace "Any luck cheering her up?"
    anon "N-no, not yet."
    odette "Well, what are you waiting for Clyde?!"
    odette "Bonnie needs you!"
    grace f_angry "Stop that!"
    odette f_laugh "Hahaha!"
    anon "{b}I'll go upstairs and talk to her now{/b}."
    hide anon with dissolve
    return

label button_grace_bathroom_break:
    scene expression player.location.background_closeup with None
    show anon f_confused o_boner a_cover_boner:
        flip
    show expression "characters/anon/anon_arms_dressed_a_cover_boner.png" at flip
    show grace b_shirt f_happy:
        flip
    with dissolve
    anon "W-where did you say the bathroom was again?"
    grace "It's just through {b}Eve{/b}'s bedroom there and it'll be on your right."
    anon f_shy "T-thanks."
    hide anon
    hide expression "characters/anon/anon_arms_dressed_a_cover_boner.png"
    with dissolve
    return

label button_grace_distract_grace:
    scene expression player.location.background_closeup
    show anon f_worried a_rub:
        flip
    anon "{i}*Ahem*{/i} E-excuse me, {b}Grace{/b}?"
    grace "Hmm?"
    pause
    show grace b_shirt f_suspicious:
        flip
    grace "{b}[firstname]{/b}?"
    grace "What are you doing here?"
    anon f_shy a_idle @ a_wave "H-hey... there."
    anon "I tried knocking but I guess you couldn't hear me..."
    grace f_happy "Heh, no I didn't hear you... sorry, I was really in the zone."
    anon "What were you doing anyways?"
    grace @ -m_talk "Hmm?"
    grace "I'm fine."
    anon "It looked like you were sleeping or something?"
    grace @ f_laugh "Haha, no..."
    grace "I was meditating."
    anon @ f_confused a_thinking "Meditating?"
    grace f_suspicious "You've never heard of meditation?"
    anon "N-no, I guess not..."
    grace f_happy @ f_laugh "Oh, it's wonderful!"
    grace "It really works wonders if you have a lot of stress or anxiety..."
    anon "That sounds really neat."
    grace f_suspicious "Y-yeah, it is..."
    grace "What are you doing here again?"
    anon f_worried "Oh, uhh... {b}Eve{/b} told me to meet her here after school."
    grace "She did?"
    anon "Y-yeah."
    grace "Well, where is she?"
    anon "W-where is she?"
    grace "Yeah, have you seen her?"
    anon @ f_thinking a_thinking "She umm... had to speak with {b}Miss Ross{/b} about some project..."
    grace "Oh, she's still struggling with that?"
    anon "Y-yeah, I guess so."
    grace f_sad "Poor thing."
    grace f_happy "I've been meaning to ask if I can help her with it but work keeps getting in the way, you know?"
    anon a_behind_head "Heh, yeah."
    pause
    grace f_suspicious "Sorry I'm not dressed."
    grace "I wasn't expecting company..."
    anon a_idle f_shy "Oh, don't worry about it!"
    anon @ f_laugh "You look great!"
    grace f_sexy "Heh, thanks."
    pause
    grace f_happy "Can I get you a drink or something?"
    anon f_worried a_behind_head @ f_shock a_surprised_up_both "NO!"
    anon "I mean, n-no, I'm okay... we should stay right here in the living room."
    grace f_suspicious @ a_point "Is everything alright, {b}[firstname]{/b}?"
    anon f_surprised_teeth @ -m_talk "( Shoot, this isn't going very well... I just need to keep her talking! )"
    anon a_rub f_shy "Y-yeah, everything is great!"
    pause
    anon @ f_worried "S-so uhh... what else do you do?"
    anon "You know, to relieve stress?"
    grace f_happy "Heh, oh my..."
    pause
    grace a_hip f_normal @ f_normal_down "... Well, I suppose... I uhh..."
    pause
    grace f_happy @ f_laugh "Oh, I've been learning all about shiatsu massage!"
    anon f_confused "What's that?"
    grace "It's a traditional form of Japanese massage that uses acupressure to release tension in your muscles and bring balance to your body."
    anon f_normal "That sounds awesome!"
    grace "Yeah, it's really cool!"
    grace @ f_eyeroll "Err, well... at least I think it is..."
    grace "{b}Odette{/b} and I have been trying it, but we aren't very good yet."
    anon "Oh, you're doing it together?"
    grace @ f_laugh "Hehe, yeah."
    grace "Though, to be honest, I think {b}Odette{/b} is just using it as an excuse to get naked in our apartment... heh."
    anon f_shock "{i}*Gulp*{/i} N-naked {b}Odette{/b}?"
    show anon f_flirt o_boner with dissolve
    anon @ -m_talk "..."
    anon f_surprised_down @ -m_talk "!!!" with hpunch
    show anon f_surprised a_cover_boner
    show expression "characters/anon/anon_arms_dressed_a_cover_boner.png" at flip
    grace "I've got lots of books about it, if you're interested-"
    anon @ -m_talk "( Oh, crap! )"
    anon @ -m_talk "( Not now!! )"
    anon f_worried "Eh, I... uhh, I should probably-"
    grace f_suspicious @ -m_talk "Hmm?"
    grace "Are you sure you're alright, {b}[firstname]{/b}?"
    grace "You look a little pale."
    anon "Oh, ehh... I'm fine, I just... c-could I use your restroom?"
    grace "Sure, but you'll have to go through {b}Eve{/b}'s bedroom."
    anon "Through her bedroom?"
    pause
    anon "I uhh... on second thought, I should probably just head home..."
    grace f_happy @ f_laugh "Oh, don't be silly!"
    grace "It's not like she's in there changing or anything!"
    anon @ f_shy "Heh, y-yeah..."
    grace "Just go in and turn right, you can't miss it."
    anon "T-thanks."
    hide grace with dissolve
    anon @ -m_talk "( Oh my god, why did she have to mention {b}Odette{/b} naked? )"
    anon @ -m_talk "( I hope she didn't notice! )"
    hide anon
    hide expression "characters/anon/anon_arms_dressed_a_cover_boner.png"
    with dissolve
    return

label button_grace_mia_get_tattoo:
    scene expression player.location.background_closeup
    show old_mia 7f at Position (xpos=400)
    show anon
    show grace f_normal
    show tattoo_desk at right
    with dissolve
    grace "Hey there!"
    grace "Are you here for an appointment?"
    return

label button_grace_generic:
    show anon
    show grace f_normal
    show tattoo_desk at right
    with dissolve
    grace "Hey there!"
    grace "Are you here for an appointment?"
    return

label button_grace_tattoo_mia:
    show old_mia 10f
    mia "I'd like to get a tattoo... now."
    show old_mia 7f
    show grace f_normal
    grace "Now? I see..."
    grace f_suspicious "Do you have a design in mind?"
    show grace f_normal
    show old_mia 30f at Position (xoffset=64) with dissolve
    mia "My friend here drew this for me, and I'd like it done today!"
    show old_mia 7f
    show grace f_normal_down a_hip_paper
    with dissolve
    grace "Hmm..."
    grace f_normal "Are you sure you want this done?"
    grace "Tattoos are permanent, so I have to make sure my clients know what they're getting into!"
    show old_mia 10f
    mia "I've been thinking about it for a long time and... yes, I do want it."
    show old_mia 7f
    grace "Alright, sweetie. But, it ain't cheap!"
    anon f_normal "How much is it?"
    grace f_normal_down "For that size... With colors... Around {b}four hundred dollars{/b}."
    show grace f_normal
    show anon f_surprised
    show old_mia 12f
    mia "!!!"
    mia "Damn... I think I only have two hundred..."
    show old_mia 8f
    anon f_worried @ -m_talk "..."
    anon "You don't have enough?"
    show old_mia 12 with dissolve
    mia "No, that's all I was able to save up."
    mia "What do you think I should do?"
    show old_mia 8
    return

label button_grace_tattoo_help:
    anon f_normal "I'll cover the rest."
    show old_mia 12
    mia "Really?!"
    show old_mia 7
    anon "Why not."
    anon "I've been working lately, so I have some money to spend..."
    anon @ f_laugh "... And it's for a good cause!"
    show old_mia 10
    mia "That's really sweet of you..."
    mia "... And I'll make sure to pay you back!"
    show old_mia 7
    anon @ f_laugh "It's alright, haha."
    show grace f_normal
    grace "So?"
    show old_mia 7f with dissolve
    grace "Ready to start?"
    show old_mia 10f
    mia "I'm ready!"

    scene tattoo_cs01
    show text _ ("It took a while for {b}Grace{/b} to finish the work.\nI was really nervous for {b}Mia{/b}...\n... But, she seemed to be fine the whole time!") as caption
    with fade
    pause


    scene tattoo_indoor_b
    show old_mia 7f at Position (xpos=400)
    show anon
    show grace f_normal
    with fade
    grace "All done!"
    grace "I hope you guys like it."
    show old_mia 10f
    mia "It's great! And it didn't hurt as much as I thought..."
    show old_mia 7f
    grace "Make sure you leave the bandage on it for at least a few days."
    show old_mia 10f
    mia "Okay, thank you!"
    show old_mia 7f
    grace "Bye, guys."
    hide grace with dissolve
    pause(.25)
    hide old_mia
    show old_mia 7 at right
    with dissolve
    anon "How does it feel?"
    show old_mia 12
    mia "The tattoo?"
    show old_mia 7
    anon "Yeah."
    show old_mia 12
    mia "It's fine... It just has this tingling sensation."
    show old_mia 10
    mia "And I'm glad I did it... I can finally say I did something that I wanted."
    show old_mia 7
    anon f_worried "Are you scared your mom might find out?"
    mia "Hopefully not, but it's in a well-hidden spot, haha."
    show old_mia 9
    show old_mia 7
    anon f_grin @ f_laugh "I think it's cool you did it."
    show old_mia 10
    mia "Thanks, {b}[firstname]{/b}. I'm happy you came with me."
    show anon f_normal
    mia "I should get going, though. Before my mom starts getting suspicious..."
    show old_mia 7
    anon "Okay, see you at school!"
    show old_mia 10
    mia "Bye."
    hide anon
    hide old_mia
    with dissolve
    return

label button_grace_tattoo_come_back:
    anon f_worried "Maybe we should come back later?"
    mia "..."
    show old_mia 12
    mia "I suppose we should."
    show old_mia 8
    anon "It's okay. We can always come back another time."
    show old_mia 12
    mia "You're right."
    show old_mia 8
    anon "Sorry you couldn't get your tattoo today..."
    show old_mia 12
    mia "It's fine. I should get home now."
    show old_mia 8
    anon "Alright, see you later."
    hide anon
    hide old_mia
    hide grace
    hide tattoo_desk
    with dissolve
    return

label button_grace_paint:
    scene expression player.location.background_closeup
    show anon f_worried zorder 3
    show xtra 26 zorder 1 at Position(xpos=0.65, ypos=1.0)
    show grace f_normal zorder 0
    anon "May I ask you something?"
    grace "Sure!"
    anon "Well, you see..."
    pause
    anon "The thing is..."
    grace "..."
    anon "... Here's the thing..."
    show eve f_normal_right zorder 2:
        flip
        xoffset 200
    with dissolve
    eve "Jeez, spit it out already, {b}[firstname]{/b}!"
    eve f_happy "What up, Raggedy Ann?"
    grace @ f_laugh "Heh, not much."
    grace "You staying outta trouble, punk?"
    eve "Of course not."
    show anon f_normal
    grace @ f_laugh "Hehe."
    eve "Look, {b}[firstname]{/b} here needs some ink."
    grace "Oh, you thinking of getting a tattoo?"
    anon @ -m_talk "..."
    eve f_happy_right @ f_laugh "No, no, no. He needs actual ink! Like in bottles, ya dummy!"
    eve "Sorry, she can be a little slow."
    show eve f_happy
    grace @ f_suspicious "Hey! I heard that!"
    eve "Yeah, I said it loud..."
    grace @ f_laugh "Haha, smart ass."
    eve @ f_laugh "Looove ya, Sis!"
    grace "Yeah, yeah. You're lucky you're cute."
    eve "Shut up!"
    grace @ f_laugh "Haha!"
    grace "So, how much ink do you need, {b}[firstname]{/b}?"
    show eve f_happy_right
    anon "Umm, I'm not sure."
    anon "Just enough to do one painting."
    show eve f_happy
    grace "Ahhh, an artist, huh?"
    grace @ f_laugh "Figures, the first guy {b}Eve{/b} brings home is an artist."
    show anon f_worried
    eve @ f_eyeroll "Tch, better than that biker freak you were dating in high school."
    grace @ f_laugh "Heh, you'll get no arguments there..."
    grace "Would one bottle of each primary color be enough?"
    grace @ f_suspicious "I assume you know how to mix?"
    anon "Mix?"
    eve f_happy_right "Yeah, you know? Blue and red make purple."
    eve "Yellow and blue make green."
    anon "Oh yeah, like color wheel stuff, right?"
    show eve f_happy
    grace "Yeah, exactly."
    grace @ f_suspicious "I guess the only question now, is what are you gonna do for me?"
    show eve f_happy_right
    anon "Oh, uhh. I dunno? What do you want me to do?"
    show eve f_happy
    grace @ f_suspicious "Hmm, did you happen to notice the graffiti on the side of the building when you came in?"
    show eve f_happy_right
    anon "... Yeah, it's pretty hard to miss."
    show eve f_happy
    grace "I'll give you the inks if you can wash it off for me."
    eve f_confused @ f_surprised "For real?"
    anon f_normal "I can do that!"
    eve "Pfft, what a waste of time!"
    anon f_worried @ -m_talk "..."
    eve "It's just gonna get tagged again..."
    show grace f_angry a_hips_mad
    with dissolve
    grace "Well, it's that stupid fucking rap gang in the park that keep doing it!"
    grace "You need to tell those little bitches that I'll whoop their fucking asses if it happens again!"
    anon "Daaang, I didn't know your sister was such a badass!"
    eve f_normal @ f_happy_right "Heh, you have no idea."
    grace "I dunno why those douchebags can't just leave our shop alone..."
    eve "... If you're going to blackmail {b}[firstname]{/b} into doing chores, you could at least have him do something useful."
    eve "Like maybe moving all that heavy shit you ordered into the back room?"
    show grace f_normal a_hip with dissolve
    eve f_happy @ f_laugh "I don't wanna bust my ovaries carrying that shit!"
    grace @ f_suspicious "Hmm, I suppose that's not a bad idea..."
    grace @ f_laugh "... Especially if it gets you to shut up about your ovaries! Ugh!"
    eve @ a_flip "... Bitch."
    grace @ f_laugh "Hahaha, don't pretend like you don't love the abuse."
    eve @ f_eyeroll "Yeah, yeah..."
    eve f_happy_right "If you'll excuse me, {b}[firstname]{/b}."
    show anon f_normal
    eve "I'm going upstairs to \"accidentally\" drop all of my sister's makeup in the toilet."
    show eve f_happy
    grace @ f_laugh "{i}*Gasp*{/i} Don't even think about it!"
    eve @ a_wave "See ya, Sis!"
    grace f_suspicious "{b}Eve{/b}, I'm serious!"
    hide eve with dissolve
    eve "Hahaha!"
    grace f_uneasy "She's joking..."
    anon @ -m_talk "..."
    grace f_normal "The {b}boxes are right in front of the counter{/b}. Just {b}move them{/b} into the back for me and the ink is yours."
    anon "Sounds good!"
    return

label button_grace_you_look_familiar:
    anon f_worried @ f_skeptical "You know... I think..."
    anon "Uhh."
    show anon f_thinking a_thinking with dissolve
    grace @ f_suspicious "Is everything okay?"
    anon a_idle "Sorry, but you look... Familiar."
    show anon f_worried
    grace @ f_suspicious "Huh?"
    grace "Hmm... Maybe you're thinking of my sister?"
    anon "Sister?"
    grace @ f_suspicious "My little sister? {b}Eve{/b}?"
    anon f_normal @ f_laugh "Oh! Of course!"
    anon "I can see the connection, now."
    grace @ f_laugh "Haha."
    grace "Anyway, is there anything I can do for you?"
    return

label button_grace_nothing:
    anon f_normal "I'm just looking around."
    grace "Cool! Have a look."
    grace "I do all styles and designs showcased in my shop!"
    grace "Just let me know if you ever think about getting something, and we can make an appointment!"
    anon "Okay, thanks!"
    grace "See ya."
    hide grace
    hide old_mia
    hide anon
    hide tattoo_desk
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
