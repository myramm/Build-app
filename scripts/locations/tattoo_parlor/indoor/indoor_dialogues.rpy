label tattoo_parlor_interior_odette_first_baby:
    scene expression player.location.background_blur with None
    show grace:
        flip
        xoffset 350
    show odette:
        xoffset 100
    with dissolve
    odette "Yeah, I'm thinking about getting one myself..."
    grace @ f_eyeroll "Oh, shut up."
    odette "I'm serious!"
    grace "Why would anyone ever want a piercing down there?"
    grace "Don't you think it would hurt like crazy?"
    show anon with dissolve
    odette "No, that's the thing... She said it felt really good!"
    grace f_tired "Pfft, she's so full of it."
    odette @ f_laugh "Hehehe!"
    anon @ a_wave "Hello, ladies."
    show grace f_tired_back
    odette f_smirk "Oh, hey there, big fella."
    anon "What's going on?"
    grace "{b}Odette{/b}'s trying to convince herself that a clit piercing is a good idea..."
    anon @ f_shock "!!!"
    show grace f_tired
    odette "Don't you think it would be hot, {b}[firstname]{/b}?"
    anon f_shy "Ehh, I dunno?"
    grace @ f_surprised "See?"
    grace "It's a stupid idea."
    odette f_smirk "Hmm, maybe I'll just get my nipples done instead."
    odette "You should get yours done too!"
    grace "Nope."
    odette @ f_normal "Aww, c'mon!"
    odette "It'll be so sexy, babe!"
    grace f_angry "Absolutely not, {b}Odette{/b}!"
    grace "I don't want a needle anywhere near my nipples and definitely not my pussy!"
    odette @ f_eyeroll "Ugh!"
    anon f_worried "Umm."
    anon "I'm really sorry to interrupt you guys but can I borrow {b}Odette{/b} for a second?"
    odette @ -m_talk "Hmm?"
    grace f_suspicious_back "You wanna borrow her?"
    anon "Just for a second, I need to ask her something in private."
    grace f_tired "Yeah, that's not suspicious..."
    odette @ f_laugh "Hehehe, would you chill out?"
    odette "We're just talking..."
    grace @ -m_talk "Mmhmm."
    odette f_normal "You got the store for a few minutes?"
    grace f_normal "Yeah."
    odette @ f_laugh "Thanks, babe!"
    if not M_grace.pregnancy:
        hide grace
        show odette b_dressed_kiss_peck f_smirk:
            flip
            xoffset 100
        with dissolve
        odette "!!!"
        pause
        show grace:
            flip
            xoffset 350
        hide odette
        show odette b_dressed:
            xoffset 100
        with dissolve
    grace "J-just hurry up."
    odette @ f_laugh "Hehehe!"
    odette "C'mon, we can talk in the garage."
    hide odette with dissolve
    anon "Alright."
    hide anon with dissolve
    $ player.go_to(L_tattooparlor_garage)
    scene expression player.location.background_blur with None
    show odette f_smirk
    show anon f_worried with dissolve
    odette "Mmm, I'm really glad you came by today..."
    odette "I'm craving dick like you wouldn't believe!"
    anon "Umm."
    odette "How do you want me, big fella?"
    anon "Actually, I wanted to talk to you about something..."
    odette @ f_confused "Oh, for real?"
    anon "Yeah."
    odette "Can't we just bang one out really quick and then talk afterwards?"
    anon "No, this is too important."
    odette f_normal @ f_eyeroll "Ugh, fine."
    odette "What is it?"
    anon @ f_skeptical "Are you pregnant?"
    odette f_surprised "!!!"
    odette "How did you-"
    odette f_happy_down "I'm not showing signs already, am I?!"
    anon "N-no."
    show odette f_normal
    anon "{b}Eve{/b} overheard you and {b}Grace{/b} talking about it."
    odette @ f_eyeroll "Oh, that makes sense."
    pause
    anon "S-so, is it mine?!"
    odette @ a_shrug "Yeah, probably."
    anon f_skeptical "Probably?"
    anon "What does that mean?!"
    odette f_smirk "It means that your dick is the only one I've been messing with since I got with {b}Grace{/b}..."
    anon f_surprised "So, it's definitely mine?"
    odette "Yeah, probably."
    anon "Stop saying probably!"
    odette @ -m_talk "..."
    anon "What are we going to do?"
    odette "What do you mean?"
    anon f_worried "What do I-"
    anon f_sad_down @ a_facepalm "{i}*Sigh*{/i} Are you going to have it?"
    odette @ f_eyeroll "Yeah, probably."
    anon f_unimpressed "{b}ODETTE{/b}!!!"
    odette @ f_laugh "Hahaha!"
    odette "Relax, {b}[firstname]{/b}..."
    odette "You're not on the hook for anything."
    odette "I talked it over with {b}Grace{/b}, and we decided that I should have it."
    anon f_worried "Yeah, but-"
    odette "The tattoo shop is making good money and I always have {b}Daddy{/b}'s money to fall back on if things go south."
    anon f_skeptical "What if I want to be involved?"
    odette "Do you?"
    show anon f_thinking a_thinking with dissolve
    pause .5
    anon f_angry a_fists "Of course I do!"
    anon "I am the father, after all..."
    odette "Aww, that's really sweet, {b}[firstname]{/b}."
    show odette f_thinking
    pause
    odette @ -m_talk "Hmm."
    odette f_normal "Well, I guess it wouldn't be a problem as long as you don't go blabbing that you're the father to {b}Evie{/b}."
    anon a_idle f_worried "Huh?"
    odette @ f_eyeroll "{b}Grace{/b} doesn't want to upset her."
    odette "As far as she's concerned, I used a sperm donor."
    anon f_surprised "Seriously?"
    odette f_tired "For the record, I think it's stupid..."
    odette "... But {b}Grace{/b} is adamant."
    anon f_worried @ a_behind_head "So I can be involved, so long as {b}Eve{/b} doesn't find out I'm the father?"
    odette f_smirk "Yup."
    anon f_sad_down @ -m_talk "..."
    pause
    odette "So are we gonna fuck, or-"
    show anon f_surprised
    return

label tattoo_parlor_interior_odette_first_baby_okay:
    anon f_flirt "Yeah, okay."
    odette "Mmm, now we're talking!"
    odette "How do you want me?"
    return

label tattoo_parlor_interior_odette_first_baby_not_now:
    anon f_angry @ a_fists "Not right now!"
    anon "I really don't think this is the time, {b}Odette{/b}!"
    odette f_eyeroll "Ugh, what are you talking about?!"
    odette "It's the perfect time!"
    show anon f_grumpy
    odette "It's not like you can get me MORE pregnant..."
    anon @ -m_talk "..."
    odette @ -m_talk "Hehehe!"
    anon "I'm going to be a father..."
    odette "Yup."
    odette "Congrats!"
    show anon f_depressed a_idle with dissolve
    pause
    odette "Tsk, I should be getting back to the shop."
    hide odette with dissolve
    odette "Later, {b}[firstname]{/b}."
    return

label tattoo_parlor_interior_odette_repeat_baby:
    scene expression player.location.background_blur with None
    show grace f_tired:
        flip
        xoffset 350
    show odette f_smirk:
        xoffset 100
    show eve:
        flip
        xoffset 200
    with dissolve
    odette "I had a kid, remember?"
    odette "I probably wouldn't even feel it."
    grace "We can't seriously be having this conversation again..."
    odette "Why shouldn't I do it?"
    grace "Because I will absolutely dump you if you pierce your clit, {b}Odette{/b}!"
    odette @ f_eyeroll "Ugh, you are such a downer!"
    pause
    odette f_smirk "I guess I'll just do my nipples then..."
    grace @ f_eyeroll "Oh god, please... Take me now."
    odette @ f_laugh "Hehehe!"
    show anon:
        xoffset -100
    with dissolve
    eve "{b}[firstname]{/b}!!"
    show eve f_happy:
        unflip
        xoffset -450
    with dissolve
    anon "!!!"
    hide anon
    show eve b_dressed_kiss
    with dissolve
    pause
    show anon:
        xoffset -100
    show eve b_dressed
    with dissolve
    odette "Oh, hey there, big fella."
    anon "What's going on?"
    show eve:
        flip
        xoffset 200
    with dissolve
    grace "Oh, you know us, S.S.D.D."
    show eve f_happy_right
    anon @ f_skeptical "Heh, I see."
    anon "I'm really sorry to interrupt you guys but can I borrow {b}Odette{/b} for a second?"
    show eve f_happy
    odette @ -m_talk "Hmm?"
    grace f_suspicious "Is this about her being pregnant again?"
    show eve f_happy_right
    anon f_worried "Oh, uhh... Yeah."
    show eve f_happy
    grace f_tired "{i}*Sigh*{/i} It's true."
    odette @ f_laugh "Hehehe!"
    grace "And before you ask, she used the same donor as last time."
    show eve f_happy_right
    anon @ f_confused "Donor?"
    pause
    show eve f_happy
    grace f_surprised "You know, sperm donor..."
    anon "O-oh."
    show anon f_thinking a_thinking with dissolve
    pause
    show eve f_happy_right
    anon f_surprised a_idle "OH!"
    anon @ f_skeptical "The same one, huh?"
    odette "That's right, big fella."
    eve "Pretty lucky for them, huh?"
    anon @ -m_talk "Hmm?"
    eve "That the same guy donated multiple samples..."
    eve "Her kids are going to be full-blooded siblings."
    anon f_shy "Y-yeah, lucky."
    odette @ f_laugh "Hehehe!"
    hide anon with dissolve
    return

label tattoo_parlor_interior_grace_repeat_baby:
    scene expression player.location.background_blur with None
    show grace:
        flip
        xoffset 350
    show odette:
        xoffset 100
    with dissolve
    odette "Well, I just assumed we wouldn't have discussed all the options this time..."
    grace "It's not about that, {b}Odette{/b}."
    grace "Of course I'm going to have it..."
    show anon zorder 2 with dissolve
    grace "I just want to make sure he's on board, is all."
    anon "On board with what?"
    hide grace
    show grace zorder 1:
        xoffset -200
    with dissolve
    odette "{b}Grace{/b} is pregnant again."
    anon @ f_surprised "Again?!"
    anon @ f_skeptical "I thought you went back on birth control?"
    grace "Yeah, I am on birth control."
    grace @ f_laugh "Apparently it doesn't matter when it comes to you!"
    odette f_smirk "Man, you slipped one past the goalie again, {b}[firstname]{/b}..."
    odette "You must be packing some crazy powerful spunk~"
    odette f_normal @ f_laugh "Hehehe!"
    grace "Anyways, I'm going to have it."
    anon "Y-yeah, okay."
    grace f_sad "... And I hope you support me?"
    anon "Of course."
    grace f_happy @ f_eyeroll "Phew, thank goodness!"
    odette "You all are turning into a big, happy, almost family..."
    grace @ f_eyeroll "{i}*Sigh*{/i}"
    odette "I'm just joking with you."
    anon @ -m_talk "..."
    hide anon with dissolve
    return

label tattoo_parlor_interior_grace_first_baby_agree:
    show grace f_sad
    anon "I agree!"
    show grace f_sad_down
    odette f_surprised "{b}[firstname]{/b}, you're on board with this?"
    anon @ a_point "I mean, it's her decision."
    anon f_normal "If she wants to have it, of course, I'll support her..."
    grace "N-no, I can't do that to {b}Eve{/b}."
    call tattoo_parlor_interior_grace_first_baby_agree_end
    return

label tattoo_parlor_interior_grace_first_baby_keep_it:
    anon f_normal "No, you should keep it!"
    grace f_sad "You must be joking..."
    anon @ f_laugh "No, I'm serious."
    anon @ a_point "You were on birth control, weren't you?"
    grace @ f_eyeroll "Of course."
    grace "I've been on birth control since I was thirteen years old."
    anon "... And yet somehow, you still got pregnant?"
    anon "What are the chances?!"
    odette "Ridiculously low."
    anon "Right?"
    anon "I think this was meant to happen."
    show anon f_brag_closed
    grace f_sad_down @ -m_talk "..."
    return

label tattoo_parlor_interior_grace_first_baby_keep_it_pass:
    grace f_sad "Y-you really think so?"
    anon f_normal "I do."
    anon "And I think it's a gift."
    anon "A little bundle of joy that's part you and part me..."
    grace @ -m_talk "..."
    odette @ f_laugh "{i}*Snort*{/i}"
    odette f_normal "Wow, that is so sappy!"
    grace f_sad_back "{b}Odette{/b}..."
    odette "Sorry, sorry."
    odette "He is right, though."
    odette "I mean, don't you want to be a mother?"
    grace f_sad_down "{i}*Sigh*{/i} Of course I do."
    grace "But I didn't expect it to happen this soon..."
    grace "... Or with my sister's boyfriend for fuck's sake!"
    odette @ f_laugh "Hehehe!"
    anon @ -m_talk "..."
    odette f_normal "Life is funny that way, huh?"
    odette "You never know what kind of curveball it's going to throw you..."
    grace "Yeah, I suppose."
    anon "I'll support you no matter what you decide, but I really hope you keep it."
    grace "{i}*Sniff*{/i} That's so sweet, {b}[firstname]{/b}."
    odette "Just imagine how sweet your kid is going to be..."
    grace f_normal_back @ f_eyeroll "Ugh, you just know how to ruin everything, don't you?"
    odette @ f_laugh "Hehehe!"
    pause
    odette "So are we doing this?"
    anon @ -m_talk "..."
    grace f_normal "{i}*Sigh*{/i} Alright, but on one condition!"
    anon "Anything."
    grace "We're not telling {b}Eve{/b} it's yours."
    odette f_confused "What?!"
    odette "You can't do that..."
    grace f_normal_back "I'm serious, {b}Odette{/b}!"
    grace "As far as she's concerned, I went to a sperm donor."
    anon @ -m_talk "..."
    odette "You're serious?!"
    pause
    odette f_normal "{b}Grace{/b}, she's a big girl, she can handle this..."
    grace f_sad_back "I can't do it to her, okay?"
    grace @ f_sad "Both of you need to promise me."
    grace "Otherwise, let's just go and get it taken care of."
    odette f_sad @ -m_talk "..."
    anon "I promise."
    odette f_normal @ f_eyeroll "Fine."
    grace f_sad_back "Promise me, {b}Odette{/b}!"
    odette "I promise."
    grace "Thank you."
    if not M_odette.pregnancy:
        hide grace
        show odette b_dressed_kiss_peck f_smirk:
            flip
            xoffset 100
        with dissolve
    anon @ -m_talk "..."
    $ player.go_to(L_tattooparlor)
    scene expression player.location.background_blur
    show anon with dissolve
    anon @ -m_talk "( {b}Grace{/b} is having my kid... )"
    anon @ -m_talk "( ... And I can't tell anyone that I'm the father. )"
    show anon f_thinking a_thinking with dissolve
    pause
    anon f_sad_down a_idle @ -m_talk "( Oh man, why does everything have to be so complicated? )"
    hide anon with dissolve
    return

label tattoo_parlor_interior_grace_first_baby_keep_it_fail:
    grace @ f_sad "No, you guys are freaking nuts!"
    grace "I'm not going to do this to my sister..."
    call tattoo_parlor_interior_grace_first_baby_agree_end
    return

label tattoo_parlor_interior_grace_first_baby_agree_end:
    anon f_worried @ -m_talk "..."
    odette f_sad "{i}*Sigh*{/i} Well, I guess that settles it then."
    grace f_sad_back "Are you mad at me?"
    odette "No, of course not, babe."
    odette "I just hope you don't end up regretting this..."
    grace f_sad_down "Y-yeah, me too."
    odette "C'mon, I'll take you to the clinic."
    grace "Thanks."
    anon f_surprised_teeth a_behind_head @ -m_talk "..."
    hide anon with dissolve
    return

label tattoo_parlor_interior_grace_first_baby:
    scene expression player.location.background_blur with None
    show grace f_sad_down:
        flip
        xoffset 350
    show odette:
        xoffset 100
    with dissolve
    odette "You need to stop freaking out."
    grace "How could I have let this happen?!"
    odette "It's not that big a deal."
    grace f_sad "What are you talking about?!"
    grace "This is a fucking disaster, {b}Odette{/b}!"
    odette "Everything is going to be alright, babe..."
    show anon zorder 2 with dissolve
    odette "Look, {b}[firstname]{/b} is here."
    hide grace
    show grace f_sad zorder 1:
        xoffset -200
    with dissolve
    anon "What's going on?"
    anon @ f_skeptical "Is {b}Eve{/b} okay?"
    odette "{b}Evie{/b} is fine."
    grace "Yeah, she's fine for the moment."
    anon f_worried "What does that mean?"
    odette @ f_laugh "{b}Grace{/b} is pregnant."
    anon f_surprised "Huh?"
    grace f_sad_down "It's yours."
    anon f_shock "!!!" with hpunch
    anon f_surprised "Are you sure?"
    grace f_tired a_crossed @ f_eyeroll "Of course I'm sure!"
    grace "What do you think? I sleep around with half the guys I meet?"
    grace "Do I look like {b}Odette{/b}?"
    odette "Okay, first of all... Ouch."
    odette "Not nice."
    odette "And secondly, {b}[firstname]{/b} is the only other person I've been with since you and I got together."
    grace @ a_facepalm f_proud "Oh my god, I'm going to end up in a wrestling match with my sister on one of those cheesy daytime talk shows."
    odette @ f_laugh "Hehehe!"
    grace "Ugh, this is so fucked up!"
    anon @ -m_talk "..."
    grace "I just-"
    grace f_sad_down "I have to get it taken care of... There's no question about it."
    odette @ f_surprised "Whoa, whoa, hold up..."
    odette "You're going to get rid of it?"
    grace f_tired_back "Well, it's the only sane option, isn't it?!"
    return

label tattoo_parlor_interior_eve_clients_take_care_clients:
    scene expression player.location.background_blur with None
    show anon f_surprised:
        flip
        xoffset -100
    show eve f_surprised:
        flip
    with dissolve
    eve "I've never seen this place so packed!"
    anon "Y-yeah, this is nuts!"
    show odette zorder 1:
        xoffset 100
    with dissolve
    odette "I'll be right with-"
    odette f_surprised "!!!"
    odette @ f_moo "{b}Grace{/b}, they're back!"
    odette @ a_point "This is insane!"
    show eve f_nervous
    show grace f_tired a_flyer zorder 0:
        xoffset -300
    with dissolve
    grace "Did you guys do this?!"
    eve "Y-yes?"
    pause
    show eve b_dressed_hug_grace1 f_surprised
    hide grace
    with dissolve
    show odette f_normal
    show anon f_normal
    eve "!!!"
    show eve f_happy_closed
    grace "I love you SO much!"
    grace "You are fucking brilliant!"
    eve f_happy @ f_laugh "Hehehe!"
    eve "It was {b}[firstname]{/b}'s idea..."
    show eve b_dressed_hug_grace2 with dissolve
    pause 1
    hide anon
    show eve b_dressed_hug_grace3 f_happy_closed
    with dissolve
    anon "!!!"
    grace "You have no idea how much this is going to help us!"
    odette "Aww..."
    hide odette
    show eve b_dressed_hug_grace4
    with dissolve
    pause
    odette "You know, I had a naughty dream the other day that started just like this..."
    hide eve
    show anon o_boner:
        xoffset -100
    show eve f_hood_remove a_facepalm:
        flip
        xoffset 200
    show grace f_tired_back:
        xoffset -100
    show odette:
        xoffset 100
    with dissolve
    grace "{b}Odette{/b}!"
    show grace f_happy
    eve f_laugh "Oh my god..."
    show eve f_happy a_idle with dissolve
    anon f_surprised_down "!!!"
    show anon f_surprised_teeth a_cover_boner
    show expression "characters/anon/anon_arms_dressed_a_cover_boner.png":
        xpos -100
    with dissolve
    odette @ f_laugh "Hahaha!"
    grace "C'mon, we've got to get everyone's name and schedule them a time."
    grace "I need everyone helping."
    eve f_surprised "I thought you didn't want me helping?"
    grace "Today's the exception."
    show eve f_happy
    grace "We've gotta hurry before people start leaving."
    odette "You heard her, let's move it!"
    anon f_surprised "O-okay."

    scene location_tattoo_cutscene03
    show text _ ("{b}Odette{/b}, {b}Eve{/b} and I spent the rest of the day taking down the names and phone numbers\nof the people waiting in line.\nIt was boring, tedious work but at least I got to sneak occasional glances at {b}Grace{/b} doing her thing.") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("She really was quite talented.") as caption with dissolve
    pause

    $ game.timer.tick(2)
    scene expression player.location.background_blur
    show anon f_tired:
        xoffset -100
    show eve a_sides f_tired:
        flip
        xoffset 200
    show grace f_tired a_sides:
        xoffset -100
    show odette f_tired a_sides:
        xoffset 100
    with fade
    odette "Phew, that's the last of them!"
    eve "I'm exhausted..."
    grace "Y-yeah, I feel like my arm is going to fall off."
    odette f_normal @ f_laugh "Haha!"
    eve f_happy @ f_laugh "Haha!"
    grace "I can't believe how many people were asking for piercings..."
    odette "Right?"
    odette "You should get a gun and start offering it."
    grace f_tired_back "We can't afford a piercing gun, {b}Odette{/b}."
    odette @ f_eyeroll "Pfft, I'm sure after today, you can splurge a little..."
    grace "No!"
    odette "Fine, just focus on inking all these crazy people, okay?"
    odette "You're going to be busy for months!"
    grace f_normal "Y-yeah, thanks to {b}Eve{/b} and {b}[firstname]{/b}."
    grace "I can't believe you guys did this!"
    grace @ f_laugh "It's unbelievable!"
    eve "We did good?"
    grace f_happy "You did very good!"
    grace "Thank you, both."
    eve @ f_laugh "Hehe!"
    anon "You're welcome."
    grace f_tired "Phew, I'm ready for a nap."
    odette "How about a massage?"
    grace f_tired_back "Oh, god... That sounds amazing."
    odette "Let's go upstairs and get you out of those clothes..."
    odette "We can discuss what you wanna do for the party."
    grace "Y-yeah, oka-"
    grace f_surprised_back "!!!"
    grace f_suspicious_back "Did you say party?"
    odette f_smirk "Yeah, I told all the customers to come back next weekend for a party we were throwing."
    show grace f_tired
    odette "Didn't you hear?"
    show grace f_angry_back a_crossed with dissolve
    eve f_surprised "{i}*Gasp*{/i} Really?!"
    eve f_happy @ f_laugh "That's an awesome idea!"
    odette "Right?"
    grace "What the fuck, {b}Odette{/b}?!"
    show anon f_surprised
    show eve f_surprised
    show odette f_surprised
    grace "We're not throwing a party!"
    show anon f_worried
    show eve f_sad
    odette f_sad "Well, we kinda have to now..."
    grace "No way!"
    grace "Not happening."
    show grace f_angry
    eve f_confused "Why not?"
    show grace f_angry_back
    odette "Yeah, you just lucked out and got a ton of people interested in your brand..."
    odette f_normal "We have to capitalize on that and strike while the iron is hot!"
    grace @ f_suspicious_back "What does a party have to do with any of that?"
    odette "Don't you see, the people who come will bring a few friends."
    odette "And those friends will spread the word to their friends."
    odette "And on and on it goes!"
    grace f_tired @ -m_talk "..."
    odette "Before you know it, you'll have the hottest hangout spot in town!"
    grace f_sad_down "Goddamnit, I don't want the hottest hangout spot in town... I just want a profitable business!"
    show grace f_sad
    eve "C'mon, {b}sis{/b}... It's a good idea."
    grace f_angry "You're just looking for an excuse to get drunk again."
    eve "N-no, I want the same thing you want!"
    eve "I mean, Jesus {b}Grace{/b}, you were talking about getting a second job last night."
    eve "I don't want that!"
    show grace f_sad
    eve "I barely see you as it is..."
    grace "{i}*Sigh*{/i} I know, I'm sorry."
    grace "I just don't want a big party in our house... I'm tired of that shit."
    show grace f_sad_back
    odette "We'll keep everyone outside and I'll handle everything, okay?"
    odette "You won't have to worry about a thing!"
    grace f_tired_back "Yeah, right."
    grace "You'll be smashed and jumping some guy's bone within the first hour..."
    odette f_angry "I will not!"
    pause
    odette f_sad "Look, I know how important this all is... Let me do this, please."
    odette "It's something I'm actually good at for once!"
    grace f_sad_down "{i}*Sigh*{/i} Goddamnit..."
    grace "Fine."
    grace f_tired_back "But I swear to god, if you let a bunch of strangers wreck our home, I'll murder you!"
    odette f_normal "Not going to happen, I promise."
    grace f_tired "And you are sticking to beer, understand?"
    eve f_normal "Y-yeah, sure."
    grace "I'm going to bed."
    hide grace with dissolve
    odette f_sad "What about your massage?"
    grace "I'm not in the mood!"
    odette f_disgusted "Seriously?!"
    hide odette with dissolve
    odette "Hold up!"
    pause
    hide eve
    show eve f_sad
    with dissolve
    eve "Sorry about that."
    anon "N-no, it's fine."
    eve "I guess she really is genuinely tired of the party life..."
    anon "Seems like it."
    eve f_happy "You're going to come though, right?"
    anon f_normal "To the party?"
    eve "Yeah!"
    eve "I'll be bored the entire time if you don't..."
    anon @ f_laugh "Well, I guess I'll have to come then, huh?"
    hide eve
    show anon b_hug_eve f_shy_down
    with dissolve
    eve "Yes."
    eve "Hehe!"
    show anon b_dressed f_normal
    show eve f_happy
    with dissolve
    eve "Thanks again for today."
    anon "You're welcome."
    hide anon
    show eve b_dressed_kiss:
        xoffset 100
    with dissolve
    anon "!!!"
    pause
    show eve b_dressed f_happy:
        xoffset 0
    show anon f_flirt
    with dissolve
    eve "I'll see you tomorrow?"
    anon "For sure."
    hide anon with dissolve
    return

label tattoo_parlor_interior_eve_bike_breakdown_check_bike:
    scene expression player.location.background_blur
    show anon with dissolve
    anon @ -m_talk "( Hmm? )"
    anon @ -m_talk "( It's just {b}Odette{/b} here by herself... )"
    anon @ -m_talk "( Where's {b}Grace{/b} at? )"
    hide anon with dissolve
    return

label tattoo_parlor_interior_eve_pregnancy_repeat:
    scene expression player.location.background_blur
    show odette:
        xoffset 100
    show eve f_nervous:
        xoffset -150
    show grace:
        flip
        xoffset 200
    with None
    show anon:
        xoffset -100
    with dissolve
    odette "There he is!"
    grace f_normal_back "Hey, {b}[firstname]{/b}."
    anon "What's going on?"
    show grace f_happy
    eve f_happy "I'm pregnant again."
    anon f_shock "Whoa, for real?!"
    eve "Yeah."
    eve "Are you ready to have another kid?"
    show grace f_normal_back
    anon f_normal @ a_behind_head "Uhh, I guess?"
    grace f_happy_back "You know, given that we've established {b}Eve{/b}'s fertility at this point... You two might wanna look into contraceptives."
    odette f_smirk "Hehe, yeah... I hear they have these new fangled things called condoms."
    odette "Supposedly they're pretty effective."
    anon "I don't think they're available anywhere in the game at the moment..."
    eve f_confused @ f_laugh "Hah, hah, very funn-"
    pause
    eve "Wait, what did you just say?"
    anon f_surprised @ -m_talk "Hmm?"
    anon f_unimpressed "I didn't say anything..."
    show grace f_sad_back
    eve "I could have sworn-"
    anon f_flirt_grin @ -m_talk "..."
    grace f_happy "I'll make a doctor's appointment for you tomorrow, okay?"
    eve f_happy "Thanks, {b}Sis{/b}."
    show anon f_normal
    grace "You still have the baby books from last time?"
    eve "Yeah."
    grace "You'd better dust them off."
    odette "You're not trying to create your own soccer team, are you?"
    eve @ f_eyeroll "Shut up, {b}Odette{/b}!"
    odette @ f_laugh "Hehehe!"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
