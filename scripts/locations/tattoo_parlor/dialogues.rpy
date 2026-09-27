label tattoo_parlor_eve_party_start:
    scene expression player.location.background_blur with None
    show anon f_surprised with dissolve
    "{i}*Music blaring*{/i}"

    anon @ -m_talk "( Wow, you can hear the music from two blocks away! )"

    anon f_normal @ -m_talk "( I guess the party is already going in full force. )"

    hide anon with dissolve
    return


label tattoo_parlor_eve_clients_tattooshop_crowd:
    scene expression player.location.background_blur with None
    show anon f_surprised
    show eve f_surprised:
        flip
        xoffset 300
    with dissolve
    anon "Wah..."

    eve "Holy crap, look at all these people!"

    pause
    eve f_happy @ f_laugh "Kami berhasil!"

    show anon f_normal
    eve "Oh my god, this actually worked!"

    anon "Y-yeah, looks like it."

    hide eve
    show anon b_hug_eve f_shy_down
    with dissolve
    eve "Hehehe!"

    eve "This is so wonderful!"

    show anon b_dressed f_normal
    show eve f_happy
    with dissolve
    eve "C'mon, let's check inside!"

    hide anon
    hide eve
    with dissolve
    return

label tattoo_parlor_eve_voyeurism_meetup:
    scene expression player.location.background_blur with None
    show anon
    with dissolve
    "{i}*Engine revving*{/i}"

    grace "Oh, c'mon girl... Don't do this to me now!"

    "{i}*Engine revving*{/i}"

    grace "No, no, no..."

    anon f_worried @ -m_talk "(Hmm?)"

    odette "Maukah kamu berhenti?!"

    odette "You're going to flood it!"

    eve "It was working earlier..."

    anon f_grin "( Sounds like they're in the garage. )"

    $ player.go_to(L_tattooparlor_garage)
    scene expression player.location.background_blur with None
    show anon:
        xoffset -100
    show eve f_sad:
        flip
        xoffset 300
    show odette a_sides:
        xoffset 100
    with dissolve
    eve "What's wrong with it?"

    odette "Bagaimana saya bisa tahu?"

    eve "Is it the battery or something?"

    grace "It's not the battery."

    grace "You can hear the engine turning over, can't you?"

    eve "Y-ya?"

    grace "Well, it wouldn't be doing that if the battery was dead!"

    odette f_smirk "Yeah, {b}Evie{/b}... Duh!"

    eve @ f_eyeroll "Diam, {b}Odette{/b}!"

    odette @ f_laugh "Ha ha ha!"

    eve "Can you fix it?"

    grace "Just hold on, I'm still trying to figure out what the problem is..."

    eve "{i}*Huh*{/i}"

    pause
    odette f_confused "You know, it sure does seem like you're awfully eager to see us leave..."

    eve "Hah?"

    odette f_smirk "You got a hot date or something?"

    eve f_angry a_rossed "Tidak!"

    odette @ -m_talk "Mmhmm."

    eve @ a_wtf "Who would want to date me?"

    pause
    odette @ a_point "Him."

    show anon f_surprised
    show eve f_surprised a_sides:
        unflip
        xoffset -350
    pause
    eve "{b}[firstname]{/b}?!"

    show eve a_idle with dissolve
    anon f_shy @ a_wave "H-hei."

    odette @ f_laugh "hehe."

    anon "Am I early?"

    eve f_sad_right "Uhh..."

    odette "No stud, you're not early."

    show anon f_normal
    show eve f_nervous_down
    odette "We're just having a little car trouble..."

    odette f_normal @ f_eyeroll "... Or bike trouble, rather."

    pause
    odette @ f_confused "What's the diagnosis, doc?"

    show eve f_nervous zorder 1:
        flip
        xoffset 250
    show grace o_oil f_sad zorder 0:
        flip
        xoffset 400
    with dissolve
    grace "The ignition is dead..."

    show eve f_sad
    grace "I'll have to replace it."

    odette f_confused "Is that going to be expensive?"

    grace @ f_suspicious "I dunno, I'll have to price it."

    grace "We definitely aren't going to make it to the city tonight though."

    odette f_sad "Itu menyebalkan."

    grace "{i}*Huh*{/i} Ya."

    grace @ f_weary "I'll have to call the guy and tell him to find another buyer for the gun."

    show anon f_shock
    odette "No, don't do that!"

    show anon f_thinking a_thinking
    grace "I can't afford it now, {b}Odette{/b}..."

    grace "Who knows how much it's going to cost me to get this bike up and running again?"

    grace "... And I've got {b}Eve{/b}'s legal fees to pay for..."

    show anon f_worried a_idle
    eve f_sad_down "I'm sorry, {b}Sis{/b}."

    grace @ f_sad_back "Tidak, tidak apa-apa."

    grace "I can just keep using the one we have."

    odette f_normal @ f_eyeroll "You're not going to keep using that old piece of crap!"

    odette "I'll pay for the new one."

    show eve f_surprised
    grace f_surprised "Apa?!"

    odette "Yeah, I'll pay for it."

    show eve f_nervous
    grace "You can't do that!"

    odette @ f_confused "Kenapa tidak?"

    odette "It's my money and you really need it."

    grace f_sad "Y-ya, tapi..."

    grace "What if I can't pay you back?"

    odette "Jangan khawatir tentang hal itu."

    pause
    odette f_smirk "I'm sure we'll figure something out..."

    show eve f_eyeroll a_hip with dissolve
    pause
    show eve f_normal
    grace f_suspicious "Apakah kamu serius?"

    odette f_normal "Yes, I'm serious."

    odette "Go call the guy and tell him to hold it for you until tomorrow."

    grace f_uneasy "{b}Odette{/b}..."

    odette @ f_eyeroll "Hurry up, before I change my mind."

    hide grace
    show odette f_surprised b_hug_grace
    odette "!!!" with hpunch
    grace "Terima kasih, terima kasih, terima kasih!!!"

    odette f_smirk "Whoa, c'mon!"

    odette "You're getting oil on me!"

    show odette b_dressed
    show grace o_oil f_happy zorder 0:
        flip
        xoffset 400
    with dissolve
    grace "I owe you big time for this!"

    odette @ f_laugh "Hehe, go call him."

    grace "Alright, I will."

    hide grace
    pause
    anon "Wow, that was really nice of you, {b}Odette{/b}..."

    eve f_confused "How are you going to afford this?"

    eve @ a_wtf "You don't even have a job!"

    odette "Tch, I'll just tell {b}Daddy{/b} I need new boots or something..."

    eve @ f_eyeroll "Ugh, I hate it when you call him that..."

    anon f_skeptical "D-daddy?"

    eve f_nervous_right "Yeah, her father is like, super rich."

    anon f_normal @ f_surprised "Benar-benar?"

    show eve f_nervous
    odette "He invented a line of male brassieres."

    anon f_confused "Brassieres?"

    pause
    eve f_nervous_right "You know, like bras..."

    pause
    anon "Yeah, but for men?"

    odette @ f_laugh "Hehe, they're called \"Bros\"."

    anon f_unimpressed @ -m_talk "..."
    anon "Okay, that's just weird."

    eve "Ya, ceritakan padaku tentang hal itu."

    show eve f_nervous
    odette f_normal @ f_tired "It's not THAT weird!"

    odette "... And even if it is, he made a buttload of money, so who cares?!"

    anon f_normal "Meh, fair enough."

    eve "Yeah, don't worry."

    eve "I'm not going to rag on you about it tonight."

    eve "Not after you made {b}Grace{/b} so happy."

    pause
    odette f_smirk "So, what were you two planning?"

    pause
    show eve f_surprised
    pause .1
    eve f_nervous "We weren't planning anything..."

    odette "Oh, don't lie!"

    odette "You invited him over when you knew your sister and I would be out."

    eve f_nervous_down "... N-no, I didn't."

    odette "C'mon, {b}Evie{/b}... Spill it!"

    pause
    eve f_normal "Baiklah baiklah."

    eve "I rented us a movie and I thought, maybe... I dunno..."

    pause
    eve f_nervous_down "We could drink a couple beers."

    odette f_confused "Beers?"

    odette f_tired a_idle "I know you're not talking about my beer!"

    eve f_nervous "No, just whatever we could find in the fridge."

    odette f_angry "Yeah, those are MINE!"

    eve f_sad_down a_idle "... Maaf."

    pause
    odette f_smirk @ f_eyeroll "Tsk, what movie did you get?"

    eve a_dvd f_nervous "Witchwood Witches 2: The Witchening."

    odette "Oh, cuddling up on the couch to a scary movie, huh?"

    eve @ -m_talk "..."
    odette "I know that move."

    odette "It works almost every time."

    pause
    odette f_angry "Especially when you're drinking stolen beer!"

    eve @ f_eyeroll "I'm sorry, okay!"

    odette @ -m_talk "Mmhmm."

    eve f_angry "I dunno what I'm apologizing for, you guys didn't even go!"

    odette f_smirk "Oh, I'm not mad."

    odette "In fact, it makes what I'm about to do, much, much easier."

    eve f_confused @ -m_talk "Hmm?"

    show eve f_surprised a_hip
    show odette a_dvd_take
    with dissolve
    show anon f_worried
    eve "!!!"
    show odette a_dvd with dissolve
    eve f_angry "Hei!"

    odette "I want you two to beat it and give {b}Grace{/b} and me some alone time."

    eve "You can't-"

    odette f_angry a_idle "Take your date somewhere else!"

    eve a_rossed "It's not a date!"

    odette f_normal @ f_eyeroll "Bisa aja."

    eve a_hip @ a_wtf "Where the hell are we supposed to go?!"

    odette "I dunno, figure something out."

    eve @ -m_talk "..."
    odette "Why don't you go up on the roof and sit around the campfire?"

    anon f_surprised "You have a campfire on your roof?"

    odette "Yup, {b}Tuuku{/b}'s got a whole thing going on up there."

    odette "It's nice."

    show anon f_normal
    eve "{i}*Sigh*{/i} Not as nice as our couch..."

    odette @ f_laugh "You can make s'mores or something."

    eve @ a_wtf "What are we, twelve?"

    odette f_tired "Just do me a favor and make yourself scarce, okay?"

    eve f_disgusted "She's not going to sleep with you {b}Odette{/b}..."

    odette f_angry "You don't know-"

    eve f_happy @ f_laugh "Pretty sure she's not into women."

    odette f_smirk @ f_eyeroll "She just doesn't know she's into women!"

    show anon f_flirt_grin
    eve @ f_eyeroll "..."
    odette f_normal "Look, there's a few beers in the cooler up there..."

    odette "They're a little old but you can have them."

    eve f_disgusted "Uh, baiklah."

    odette "Just promise me you won't do something stupid like fall off the roof or set the place on fire!"

    show anon f_normal
    eve f_happy @ f_eyeroll "Ya, ya."

    pause
    eve "You're totally gonna strike out..."

    odette f_angry "Diam!"

    hide odette with dissolve
    eve @ f_laugh "Ha ha ha!"

    pause
    anon f_skeptical a_behind_head "So, I'm confused..."

    anon "{b}Odette{/b} and your sister are... An item?"

    eve f_nervous_right @ f_eyeroll "Only in her head."

    pause
    eve "C'mon, let's head up to the roof and I'll explain it to you."

    hide eve with dissolve
    pause
    anon a_idle "O-oke."

    hide anon with dissolve
    return

label tattoo_parlor_eve_upset_pot:
    scene expression player.location.background_blur with None
    show grace f_tired a_sides:
        flip
    show odette f_smirk:
        xoffset -250
    with dissolve
    odette "Oh, c'mon {b}Grace{/b}, it was just a little pot..."

    odette "We've all done it."

    grace a_hip "It was not, \"Just a little...\""

    grace "She had half a pound of weed stuffed in her pocket!"

    odette "Yeah, that she swiped off a bunch of assholes who were hassling her..."

    odette "You should be proud that she stood up for herself!"

    grace f_angry "She got arrested, {b}Odette{/b}!"

    pause
    grace f_suspicious "... And how do you know where she got it from?!"

    odette f_sad "Oh, ehh... {b}Tuuku{/b}, might have, filled me in on the story..."

    grace f_angry "Tch, I knew he was involved!"

    odette "Well, of course he was involved!"

    odette f_smirk @ f_laugh "Do you know any other pot dealers in this shitty little town?!"

    grace f_tired @ a_facepalm f_weary "{i}*Sigh*{/i} I'm telling him to take those plants down off my roof the second he walks in here!"

    odette f_normal @ f_eyeroll "Bisa aja."

    odette "Like you can afford to lose the money he pays you to store those plants..."

    odette "You're just overreacting..."

    grace f_angry "Overreacting?!"

    odette f_smirk "{b}Eve{/b} wasn't doing anything that you and I haven't done a thousand times!"

    odette "She just had some bad luck and stumbled into some cops, that's all."

    grace "I'm sorry, do you have three thousand dollars lying around to pay her fine?"

    show odette f_tired_down
    pause
    odette "Tidak."

    grace f_weary "Yeah, me neither..."

    show odette f_normal
    grace f_angry @ a_upset "Which is why I'm flipping out!"

    odette @ f_eyeroll "{i}*Sigh*{/i} You know, you used to be a lot more fun..."

    grace f_tired "{b}Odette{/b}, please don't start in on that again, I'm really not in the mood."

    show anon:
        flip
        xoffset 100
    with dissolve
    odette f_smirk "I'm just saying, you need to take a vacation or something..."

    grace f_sad "I can't take a vacation, I've got too many responsibilities here!"

    odette "Well then, you need to get laid!"

    show anon f_surprised
    grace @ f_eyeroll "Yeah, that's easier said than done."

    show anon f_tired_happy
    grace f_uneasy "I'd have to find a decent man first..."

    odette @ f_wink "Who said anything about a man?"

    show anon f_surprised_teeth
    grace @ f_suspicious "Hah?"

    odette "Why don't we go upstairs and you can show me more of that shiatsu massage stuff?"

    grace "You know I can't leave the shop right now..."

    odette "Well, maybe later tonight then, we coul-"

    anon f_normal @ a_wave "B-permisi?"

    show grace f_surprised
    show odette f_surprised
    pause
    grace f_normal "Oh, hey there {b}[firstname]{/b}!"

    show odette f_exasperated
    grace "Apa yang kamu lakukan di sini?"

    anon "I was hoping I could speak with {b}Eve{/b}..."

    show odette f_normal_back
    anon "Apakah dia di sini?"

    odette f_smirk_back "Aww, Clyde's come to check up on Bonnie."

    odette f_smirk "Isn't that sweet, {b}Grace{/b}?"

    anon f_confused "Hmm?"

    odette f_smirk_back "You know, Bonnie and Clyde?"

    odette "The famous outlaw couple?"

    show grace f_eyeroll
    anon "Y-ya?"

    grace f_suspicious "Would you cut that out!"

    grace "It's not funny."

    odette f_smirk @ f_laugh "C'mon, it's a little funny..."

    odette "Their first date and they both end up in the clink!"

    grace "I'm pretty sure it wasn't a date..."

    anon f_worried "Y-yeah, I was just helping-"

    odette @ f_laugh "Oh, you're both just arguing semantics!"

    odette "He clearly wants to date her..."

    pause
    odette f_smirk_back "Bukan begitu?"

    show grace f_surprised
    pause
    menu:
        "Ya!":
            anon f_normal @ f_laugh "Ya!"

            show grace f_suspicious
            odette @ f_laugh "That's good to hear!"

            odette f_smirk "I was beginning to worry {b}Evie{/b} would never get herself a boyfriend!"

            grace @ -m_talk "..."
            odette f_confused "Ada apa denganmu?"

            grace @ f_surprised "T-tidak ada, aku hanya-"

            odette f_smirk "Uh oh, here comes {b}Mom{/b} again..."

            grace f_angry "Diam!"

            odette @ f_laugh "Ha ha ha!"

            grace f_sad @ f_normal_down "I just don't want to see {b}Eve{/b} get hurt."

            odette @ f_eyeroll "Oh, please..."

            odette f_shy "{b}[firstname]{/b} seems like a nice guy, I'm sure he won't do anything to hurt her..."

            show grace f_normal
            odette f_smirk_back "... And if he does, I'll murder him."

            anon f_surprised_teeth "!!!"
            odette f_smirk @ f_laugh "Hahaha, look at his face!"

        "Saya tidak tahu...":

            anon f_worried a_behind_head "Saya tidak tahu..."

            show grace f_sad
            odette f_normal_back "Bagaimana mungkin kamu tidak tahu?"

            grace "{b}Odette{/b}..."

            show anon a_idle
            odette f_shy "Apa?!"

            odette "Either he wants to date {b}Evie{/b} or he doesn't..."

            odette "It's not like there's a right or wrong answer!"

            grace "You can't push people into relationships, {b}Odette{/b}."

            odette @ f_eyeroll "Yeah, okay {b}Mom{/b}!"

            grace f_angry "Berhenti memanggilku seperti itu!"

            odette f_smirk @ f_laugh "Ha ha ha!"

    grace f_weary "I'm just not sure he knows what he's getting into..."

    grace "{b}Eve{/b} isn't like other girls, she's been through a lot."

    odette f_confused "Sheesh, you are so overprotective with her..."

    grace f_suspicious "Well, it's sorta my job to be overprotective with her!"

    odette f_shy @ f_eyeroll "Ya benar..."

    odette "Just let the kid go up and see her!"

    odette "If she wants to open up to him, that's her decision, not yours..."

    pause
    grace f_normal "Y-yeah, you're right..."

    grace "{b}She's been moping around upstairs all day{/b}."

    grace "{b}Maybe you can cheer her up{/b}?"

    show odette f_smirk_back
    anon "Ya, saya akan mencoba."

    grace "Just be careful, {b}[firstname]{/b}."

    grace "The last thing {b}Eve{/b} needs right now is to get her heart broken..."

    anon "Saya akan berhati-hati."

    hide anon with dissolve
    odette "Oh, and if you guys are planning on robbing banks or something later, let me know!"

    show grace f_angry a_crossed with dissolve
    odette "I'll be your getaway driver!"

    odette f_smirk @ f_laugh "Ha ha ha!"

    odette "Apa?"

    pause
    odette f_laugh "A good getaway driver is the most valuable member of the team!"

    return

label tattoo_parlor_eve_distract_grace:
    scene expression player.location.background_blur with None
    show eve b_dressed_wet
    show anon
    eve "Alright, just try and distract her so I can sneak into my room, okay?"

    anon "Y-ya, oke."

    eve "I'll try to be quick, so you won't have to distract her long."

    anon "Benar."

    show anon f_surprised
    pause
    anon f_skeptical "Ehh, can I ask you something?"

    eve "Apa itu?"

    scene expression "backgrounds/location_tattoo_apartment_cutscene01.jpg" with fade
    anon "Why is your sister sitting on the floor in her underwear?"

    eve "!!!"
    pause
    $ player.go_to(L_tattooparlor_fire_escape)
    scene expression player.location.background_blur with None
    show eve f_nervous_down b_dressed_wet
    show anon f_surprised
    eve "Y-yeah, she uhh... Does that... From time to time..."

    anon f_flirt "Benar-benar?"

    eve "It's some kind of meditation thing..."

    eve "She says it relieves stress."

    anon "Huh, interesting."

    eve "Sorry, it's weird, I know..."

    anon f_thinking a_thinking "Won't she freak out about me seeing her dressed like that?"

    eve "Saya meragukannya."

    show anon f_surprised a_idle
    eve "She's always been pretty open about her body... She's not the shy type at all."

    eve "You should ask her about it, you know?"

    anon "About her underwear?"

    eve f_happy @ f_eyeroll "No, dummy."

    eve "About her meditation!"

    anon f_normal @ f_laugh "Oh."

    eve "It'll be a good distraction."

    anon f_flirt "O-oke, tentu saja."

    eve "Lanjutkan."

    anon f_worried "{i}*Gulp*{/i} Now?"

    show eve f_eyeroll
    pause
    eve a_point "Pergi!"

    hide anon with dissolve
    return

label tattoo_parlor_eve_visit_tattoo_shop:
    scene expression player.location.background_blur with None
    show grace f_suspicious:
        xoffset -180
    show odette f_angry a_sides:
        xoffset 80
    show tuuku f_angry:
        flip
    with dissolve
    odette "You're such a child..."

    tuuku "Why can't you just admit that I'm right?!"

    odette "Umm, because you're not right!"

    grace "Are you guys arguing about horror movies again?"

    show tuuku a_shrug with dissolve
    tuuku "He literally turns into your worst fear, and then he eats you!"

    show tuuku a_hips
    show odette a_hips
    with dissolve
    odette "Umm, he's also bound to a small town in Maine..."

    tuuku "So?!"

    odette "So all you have to do is leave the town and you're safe!"

    show odette f_smirk a_mock with dissolve
    odette "\"Like, oh my god, I have to take a vacation until the monster goes back to sleep...\""

    show grace f_proud a_laugh with dissolve
    grace @ -m_talk "{i}*Mendengus*{/i}"

    odette "\"How will I ever manage...\""

    show odette a_hips with dissolve
    grace f_laugh "Hahaah!"

    tuuku @ f_eyeroll "Ugh, you are such a bitch..."

    show grace a_hip f_happy with dissolve
    tuuku "He only attacks children and the adults are completely oblivious to him."

    show odette f_eyeroll
    tuuku "They can't just move away in that scenario!"

    odette f_angry "So lemme get this straight..."

    odette "According to you, the scariest monster in horror movies... Is a clown that wouldn't even bother with us because we're adults?"

    tuuku "Itu bukan-"

    odette @ f_eyeroll "Laaaaaame."

    show odette f_smirk
    tuuku "It's not who he kills that matters, it's how he kills them!"

    grace @ f_eyeroll "Oh great, now you've really got him started..."

    tuuku "He can shapeshift into the exact thing that scares you the most!"

    odette "So for you, I guess that would probably be a vagina?"

    show tuuku a_hips with dissolve
    tuuku "Oh, fuck you!"

    grace "For {b}Odette{/b}, it would probably be the sun..."

    odette f_smirk "Hey, you're supposed to be on my side!"

    grace @ f_laugh "Hahaah!"

    tuuku f_confused "Okay, so tell me who's scarier then?!"

    show odette a_shrug with dissolve
    odette "I dunno, evil spirits?"

    show odette a_hips with dissolve
    tuuku f_annoyed "... Evil spirits?"

    odette f_normal "You know, like when people get possessed and start crawling on the ceiling?!"

    show grace f_uneasy a_hug_self with dissolve
    grace "Yeah, exorcism flicks really freak me out!"

    show grace f_proud zorder 1
    show odette a_hug zorder 0
    with dissolve
    odette "Aww, don't worry beautiful... I'll protect you."

    show tuuku a_shrug f_eyeroll with dissolve
    tuuku "Oh my god, you're cheating!"

    show tuuku a_hips f_annoyed
    show grace f_happy a_sides
    show odette a_hips zorder 2
    with dissolve
    odette f_confused "How is that cheating?!"

    show tuuku a_point zorder 2 with dissolve
    tuuku f_angry "You have to name a specific monster, you can't just say, \"Evil spirits.\""

    show tuuku a_hips with dissolve
    show odette f_eyeroll
    tuuku "That's too vague!"

    show odette f_angry
    show grace f_proud a_idea with dissolve
    grace "Oh, I've got one!"

    show grace f_happy a_sides with dissolve
    show tuuku f_annoyed
    grace "What's that movie with the curse that passes through sex?"

    odette f_confused @ -m_talk "Hmm?"

    grace f_uneasy "C'mon, we just watched it a few weeks ago, remember?!"

    odette f_thinking @ -m_talk "..."
    grace "That entity that comes after you relentlessly and the only way to stop it, is to pass it on to someone else via sex..."

    odette f_normal "Oh, yeah... That is a good one!"

    grace f_happy "Then, after it kills the person you infected, it comes back after you."

    odette f_thinking "What the heck was the movie called?"

    tuuku f_confused "So it's like, a sexually transmitted curse?"

    grace "Pretty much..."

    grace @ f_proud "... And once you have it, you're completely fucked!"

    grace "You can't trust anyone because it shapeshifts and you can basically never sleep again!"

    tuuku "Sounds like a metaphor for HIV or something..."

    show tuuku f_annoyed
    odette f_shy "No, it was deeper than that!"

    grace f_suspicious "Hmm?"

    odette f_normal "I'm pretty sure it's about facing our own mortality."

    odette "Death, or in this case the entity, is coming for you and there is no escape."

    odette "You don't know when it will get you or what form it will take..."

    odette "... All you know is that it's coming and it's relentless!"

    show grace f_normal
    tuuku @ f_eyeroll "Unless you abstain from sex, then you're safe!"

    show odette f_angry
    show tuuku f_confused a_shrug with dissolve
    tuuku "Also, what about condoms?"

    tuuku "Does it still transfer to you if you use protection?"

    show tuuku f_happy a_hips with dissolve
    odette "Oh, diamlah!"

    show tuuku f_angry
    odette f_wink "It's a good choice, {b}Grace{/b}!"

    odette f_smirk "{b}Tuuku{/b} just can't understand how scary it is because he's a perpetual virgin!"

    show odette f_laugh
    show anon f_worried:
        xoffset -200
    show tuuku a_flip
    show grace f_proud a_laugh
    with dissolve
    tuuku "Fuck you, {b}Odette{/b}!"

    odette "Hahaah!"

    grace f_laugh "Why don't you two screw already and get it over with?"

    odette f_eyeroll "Eugh, in his dreams..."

    show grace f_normal a_hip with dissolve
    odette f_smirk "Besides, you know I only have eyes for y-"

    show odette f_surprised
    anon "B-permisi?"

    show anon:
        xoffset -100
    show tuuku f_surprised a_sides:
        unflip
        xoffset -320
    with dissolve
    show odette f_sad
    show grace f_happy a_sides with dissolve
    grace "Oh, hello there!"

    tuuku f_annoyed "Who the fuck is that guy?"

    show tuuku b_slap
    show odette a_slap f_angry zorder 0
    odette "Shh!!" with hpunch
    show odette a_hips
    show grace f_weary a_facepalm
    show tuuku b_dressed a_rub f_annoyed_back
    with dissolve
    tuuku @ -m_talk "!!!"
    odette "He's a customer, obviously..."

    show odette f_normal
    tuuku "Hey, no hitting!"

    show grace a_sides f_uneasy with dissolve
    grace "Heh, please don't mind them..."

    show tuuku f_annoyed a_sides with dissolve
    grace f_happy "Apa yang bisa saya bantu?"

    anon "Eh, is {b}Eve{/b} here?"

    anon "She asked me to stop by..."

    show grace f_surprised
    odette f_surprised "{i}*Terkesiap*{/i}"

    grace "You're here to see {b}Eve{/b}?"

    odette f_eyeroll "That's a first..."

    show grace f_weary a_hips_mad with dissolve
    odette f_smirk "Since when is {b}Evie{/b} inviting boys over?!"

    grace "Would you just please go and tell her she has a visitor?!"

    odette @ f_laugh "Hehe, sure thing!"

    show grace f_angry:
        flip
        xoffset 400
    with dissolve
    grace "... And don't embarrass her!"

    odette "Oh please, it's my job to embarrass her!"

    show anon a_behind_head with dissolve
    grace "{b}Odette{/b}, I'm serious..."

    odette "Somebody has to do it, it's part of growing up!"

    hide odette
    show grace a_facepalm f_weary
    show anon a_idle
    with dissolve
    grace @ -m_talk "..."
    show tuuku a_thumb f_annoyed_back with dissolve
    tuuku "I should probably get going too..."

    show grace a_idle f_weary:
        unflip
        xoffset -100
    show tuuku a_sides
    with dissolve
    tuuku "... Gotta check up on {b}Mary Jane{/b} before work, you know?"

    grace "{i}*Sigh*{/i} Just make sure nobody can see it from the street, okay?"

    show tuuku f_happy a_shrug:
        flip
        xoffset 100
    with dissolve
    show grace f_uneasy
    tuuku "C'mon, what do I look like, an amateur?!"

    show tuuku a_sides with dissolve
    pause
    tuuku f_confused "We're still on for that concert this weekend, aren't we?"

    show grace f_oops
    pause
    grace f_uneasy "About that..."

    show tuuku f_nervous a_hips with dissolve
    tuuku "Dengan serius?!"

    grace "I got a last minute appointment."

    tuuku "... You're cancelling again?"

    grace "You know I have a business to run, and we really need the money!"

    tuuku a_idle @ f_eyeroll "Ugh, yeah but... That means it's just gonna be me and {b}Odette{/b} again..."

    grace f_suspicious "Jadi?"

    tuuku "So, you know how she is!"

    tuuku "She'll ditch me for the first random dude who looks her way!"

    grace f_normal "Oh, c'mon... No she won't."

    tuuku "She will..."

    pause
    tuuku "... And you really need to get out of this shop, {b}Grace{/b}!"

    tuuku "You're wasting away in here!"

    grace f_eyeroll "I'm fine, {b}Tuuku{/b}."

    tuuku f_annoyed "No, you're not!"

    grace f_angry "Go and tend to your plants."

    tuuku @ f_eyeroll "Tsk, whatever."

    tuuku "I'm going to bug you about this again later!"

    grace @ f_eyeroll "BYE, {b}TUUKU{/b}..."

    tuuku f_sad "{i}*Sigh*{/i} Bye."

    hide tuuku with dissolve
    grace f_uneasy "Sorry about all that..."

    anon "Tidak masalah."

    show anon f_worried_low
    pause
    show grace f_happy
    pause
    grace "So, you go to school with {b}Eve{/b}?"

    anon f_worried @ -m_talk "Mhmm."

    grace "Apakah kamu menyukainya?"

    anon "Tidak apa-apa, menurutku."

    pause
    grace "How's my sister doing?"

    anon @ -m_talk "Hmm?"

    grace "She's not getting bullied or anything, is she?"

    anon f_skeptical "Err, not that I know of..."

    grace @ f_laugh "Oh, good!"

    show anon f_worried
    grace f_uneasy "She's been so tight-lipped about school."

    grace "I was a bit worried for her..."

    grace f_laugh "... But now I see she's making friends!"

    show grace f_happy
    anon f_shy "Heh, yup."

    pause
    show grace a_idea with dissolve
    grace "I'm {b}Grace{/b} by the way."

    show grace a_idle with dissolve
    show anon a_wave with dissolve
    anon "{b}[firstname]{/b}."

    show anon a_idle with dissolve
    grace "Senang bertemu dengan Anda, {b}[firstname]{/b}!"

    anon "Y-ya, juga."

    odette "Would you stop messing with your hair and get in there already!"

    show grace:
        flip
        xoffset 200
    with dissolve
    odette "You look fine."

    eve "Shh, shut up!!"

    eve "He'll hear you!"

    grace f_uneasy "{b}Odette{/b}, stop teasing her!"

    show eve f_nervous:
        xoffset -150
    show odette f_smirk zorder 2:
        xoffset 150
    with dissolve
    odette "Since when is it teasing to tell someone they look good?!"

    grace "You're embarrassing her!"

    odette f_eyeroll "Oh, for fuck's sake... There's nothing to be embarrassed about!"

    odette f_smirk "Everyone can see she's hot except her, apparently..."

    pause
    show odette a_point with dissolve
    odette "You think she's pretty, don't you?"

    show anon f_worried_low a_behind_head
    show odette a_hips with dissolve
    show grace f_angry
    show eve f_hood_remove a_facepalm
    with dissolve
    anon "Uhh..."

    grace "{b}ODETTE{/b}!!!" with hpunch
    show anon a_idle f_surprised
    show odette a_shrug
    with dissolve
    odette "Apa?!"

    show odette a_hips with dissolve
    menu:
        "Tentu saja.":
            anon f_shy "Y-yeah, I do."

            show eve f_surprised a_idle with dissolve
            eve @ -m_talk "!!!"
            show eve f_nervous_down
            odette f_laugh "See, what did I tell you?"

            odette "You're fishing with dynamite, girl!"

            show odette f_smirk
            grace @ f_eyeroll "Ya Tuhan..."

        "...":
            show anon f_worried_low
            grace "Don't put him on the spot like that!"

            odette "C'mon, he's obviously into her, or he wouldn't be-"

    show eve f_angry_right a_wtf with dissolve
    eve "OH MY GOD, STOP TALKING!!!"

    show eve f_nervous_down a_cover zorder 1 with dissolve
    show anon f_surprised
    show grace f_surprised
    show odette f_surprised
    pause
    show anon f_worried
    odette f_eyeroll "Well, excuse me for trying to help..."

    show odette f_smirk
    eve "I don't need your help, {b}Odette{/b}!"

    grace f_uneasy "Alright, let's not start an argument... Both of you."

    odette @ f_eyeroll "Sorry, mom..."

    show grace f_uneasy a_sides with dissolve
    grace "{i}*Huh*{/i}"

    show grace f_happy:
        unflip
        xoffset -350
    with dissolve
    grace "{b}Eve{/b}, why don't you introduce us to your friend?"

    pause
    eve f_disgusted "If {b}Odette{/b} ever shuts up, I will."

    odette @ -m_talk "..."
    eve f_nervous "Guys, this is {b}[firstname]{/b}... A new friend I made at school."

    show eve f_nervous_down
    show anon f_shy
    odette "Just friends, huh?"

    show grace f_angry:
        flip
        xoffset 150
    show eve f_angry a_wtf:
        flip
        xoffset 450
    with dissolve
    pause
    show eve a_cover
    show odette a_shrug
    with dissolve
    odette "Sorry, I'm just saying he's cute, is all!"

    show odette a_hips
    show eve f_nervous_down zorder 1:
        unflip
        xoffset -150
    with dissolve
    eve "{i}*Huh*{/i}"

    show grace f_happy zorder 0:
        unflip
        xoffset -350
    with dissolve
    eve f_nervous "{b}[firstname]{/b}, I'm sure you've met my sister {b}Grace{/b} by now..."

    grace "Yup, he was just filling me in on your school while we waited."

    eve @ f_eyeroll "The one who can't shut her mouth is {b}Odette{/b}, my sister's best friend."

    odette "Nice to meet you, handsome."

    show grace f_weary a_facepalm with dissolve
    show eve f_angry:
        flip
        xoffset 450
    with dissolve
    eve @ -m_talk "..."
    show grace f_happy a_idea zorder 2:
        flip
        xoffset 200
    with dissolve
    grace "Why don't you take {b}[firstname]{/b} upstairs and show him around?"

    show grace a_sides
    show eve f_nervous:
        unflip
        xoffset -150
    with dissolve
    eve "Oke."

    grace f_angry "I need to have a word with big mouth..."

    odette @ f_laugh "Uh oh, am I in trouble?"

    eve f_happy "C'mon, {b}[firstname]{/b}. I'll give you the full tour!"

    eve "We have to start in {b}the garage{/b}."

    hide eve
    hide anon
    with dissolve
    show grace a_hips_mad with dissolve
    odette "You know, I love it when you get stern with me..."

    scene black with dissolve
    pause
    return

label tattooparlor_first_visit:
    scene expression player.location.background_blur
    show player 13 with dissolve
    player_name "( I've never been in a tattoo shop before. )"

    show player 34
    player_name "( Maybe I should get a tattoo one day... )"

    hide player with dissolve
    return

label tattooparlor_mia_get_tattoo:
    scene tattoo_indoor_b
    show old_mia 7f at Position (xpos=400)
    show player 13 at left
    show grace f_normal
    with dissolve
    grace "Hey guys!"

    show player 14
    player_name "Hai."

    show player 13
    show old_mia 10f
    mia "Hai!"

    show old_mia 7f
    grace @ f_laugh "Selamat datang di {b}Gula Tats{/b}."

    grace "Have a look around the shop for cool tats..."

    grace "... And come see me if you have any questions!"

    hide grace with dissolve
    pause(.25)
    hide old_mia
    show old_mia 12 at right
    with dissolve
    mia "She seems busy, maybe we should come back another time?"

    show old_mia 8
    show player 12
    player_name "Oh, come on."

    show player 10
    player_name "You're going to stop now?!"

    show player 5
    show old_mia 12
    mia "{i}*Huh*{/i}"

    mia "Anda benar."

    mia "I said I would, so let's do it!"

    hide old_mia with dissolve
    show player 17
    player_name "Itulah semangatnya!"

    hide player with dissolve
    return

label tattoo_pick_up_boxes:
    scene expression player.location.background_closeup
    show xtra 26 at Position(xpos=0.65, ypos=1.0)
    if M_ross.get("failed pick up boxes"):
        call expression game.dialog_select("tattoo_boxes_try_again")
    else:

        call expression game.dialog_select("tattoo_boxes_intro")

    if player.has_required_str(6):
        $ display.toast(str_pass)
        call expression game.dialog_select("tattoo_boxes_str_pass")
        $ player.get_item("ink")
        call popup ('give', 'ink')
    else:

        $ display.toast(str_fail)
        call expression game.dialog_select("tattoo_boxes_str_fail")
        $ M_ross.set("failed pick up boxes", True)
    $ game.main()

label tattoo_boxes_try_again:
    show grace f_normal:
        flip
    show player 1f at Position(xpos=0.5, ypos=1.0)
    with dissolve
    grace "Ready to move these boxes for me?"

    show player 2f
    player_name "Yup, I'm doing it now."

    return

label tattoo_boxes_intro:
    show grace f_normal:
        flip
    show player 1f at Position(xpos=0.5, ypos=1.0)
    with dissolve
    grace "Yup, that's the ones."

    grace "Just move them to the back for me and the ink is yours."

    show player 2f
    player_name "Tidak masalah!"

    return

label tattoo_boxes_str_pass:
    show player 580 at Position(xpos=0.65, ypos=1.0) with dissolve
    pause
    player_name "..."
    show player 581f at Position(xpos=0.5, ypos=1.0) with dissolve
    player_name "Where do you want them again?"

    show player 580f
    show grace f_normal with dissolve:
        flip
    grace "The back room, if you don't mind."

    show player 581 at Position(xpos=0.65, ypos=1.0) with dissolve
    player_name "Tidak masalah."

    show player 580 at Position(xpos=0.75, ypos=1.0) with dissolve
    grace "Terima kasih, {b}[firstname]{/b}!"


    scene location_tattoo_cutscene02
    show text _ ("... Who knew that tattoo equipment could be so heavy?") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("I understand now why {b}Eve{/b} didn't want to move these.") as caption with dissolve
    pause

    scene expression player.location.background_closeup
    show xtra 26 at Position(xpos=0.65, ypos=1.0)
    show player 10 at Position(xpos=0.55, ypos=1.0)
    with fade
    player_name "Fiuh!"

    player_name "That was a lot of boxes!"

    show player 1
    pause
    show grace f_normal a_paint with dissolve:
        flip
    grace "All done?"

    show player 2f with dissolve
    player_name "Yup. They're all stacked up in the back where you showed me."

    show player 1f
    grace "Awesome job, {b}[firstname]{/b}!"

    grace "Sheesh... Sweet, handsome, and strong!"

    grace "{b}Eve{/b} really hit the jackpot with you!"


    if M_eve.finished_inclusive(S_eve_end):
        show player 17f
        player_name "Heh yeah, I guess..."

    else:
        show player 21f
        player_name "Whaaat?"

        player_name "I'm not... I mean, we aren't..."

    show player 1f
    grace "Here's that ink you wanted."

    grace "You should be able to mix everything you need with these."

    show grace a_hip
    show player 590f
    with dissolve
    player_name "Sweet! Thanks, {b}Grace{/b}!"

    show player 589f
    grace @ f_laugh "My pleasure, stud!"

    pause
    grace "Just promise me you'll take good care of {b}Eve{/b}."

    grace @ f_laugh "It would be a real shame if I had to whoop that cute butt of yours..."

    if M_eve.finished_inclusive(S_eve_end):
        show player 590f
        player_name "Ya, tentu saja."

        show player 589f
    else:
        show player 589bf
        player_name "Heh, seriously... We aren't..."

        show player 590bf
    grace f_laugh "Welp, I hope I see you again real soon, {b}[firstname]{/b}!"

    hide grace
    with dissolve
    pause
    if not M_eve.finished_inclusive(S_eve_end):
        show player 589bf
        player_name "... Together."

        show player 590bf
        pause
        show player 589bf
        player_name "... Oke."

    show player 590f
    player_name "I should {b}get this ink back to Miss Ross in the art class{/b}."

    hide player with dissolve
    return

label tattoo_boxes_str_fail:
    show player 581b at Position(xpos=0.55, ypos=1.0) with dissolve
    player_name "HNNGGG!"

    player_name "..."
    show player 10f with dissolve
    player_name "What heck is in these boxes? Anvils?!"

    show player 11f
    show grace f_normal with dissolve:
        flip
    grace "... Too heavy?"

    show player 10f
    player_name "Err, n-no..."

    show player 11f
    pause
    show player 10f
    player_name "... I'm just wearing the wrong shoes for this..."

    player_name "... Yeah, that's it!"

    show player 2f
    player_name "I'll be back later with the right shoes."

    show player 1f
    grace @ f_laugh "Hehe, oke."

    grace "... Just don't take too long."

    hide grace
    show player 35 with dissolve
    player_name "Hmm, I'd better {b}hit the gym and get my strength up{/b} before coming back."

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
