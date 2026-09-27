label ano22_ally_town_map:
    $ renpy.dynamic(unknown=Character('???', kind=character.nadya))

    scene location_mugging_cutscene01 with fade
    anon "( I can't believe he asked if I had a cheeseburger on me... )"

    anon "( ... He was definitely high on something. )"

    pause
    anon "( How does a guy like that end up working for a church anyways? )"

    pause
    anon "( I should have gone back and said goodbye to {b}Dad{/b}...)"


    scene location_mugging_cutscene06
    show text _ ("I was so caught up in my own thoughts...") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("... I didn't notice the limousine until it was right on top of me.") as caption with dissolve
    pause

    scene location_mugging_cutscene03 with fade
    anon "C'mon, guys... not this again!"

    anon "I don't have any cash on me today."

    goon "Come here, you!"

    anon "You guys already took everything!"


    scene location_mugging_cutscene07
    show text _ ("This was really getting old.") as caption
    with fade
    pause

    scene location_mugging_cutscene08
    show text _ ("But then suddenly, the script changed...") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("... I found myself being hurled into the back seat of the car.") as caption with dissolve
    pause

    scene location_mugging_limo
    show anon b_dressed_car_fall
    anon "( !!! )" with hpunch
    pause
    anon b_dressed_car_getup f_angry_back "What the hell, man?!"

    anon "Are you deaf or something?!"

    anon b_dressed_car_front f_frown_left "I told you, I don't have any-"

    anon f_surprised "Money."

    pause

    scene location_mugging_limo_back
    show nadya b_dress_limo1
    with fade
    unknown "Yes, we hear you."

    unknown "You have no monies."

    unknown b_dress_limo3 "This is quite pathetic thing to say, is it not?"

    show nadya b_dress_limo4 with dissolve
    anon "W-what's going on?"

    show nadya f_normal_smoke_blow b_dress_limo3 with dissolve
    pause
    show nadya f_normal with {'master': dissolve}
    anon "Who are you?"

    unknown f_confused "I've been told that you are man who puts disgusting mayor behind bars..."

    unknown "... Is this true?"

    anon "{i}*Gulp*{/i} Y-yes."

    pause
    unknown @ -m_talk "Hmm."

    unknown f_serious "I was expecting you to be taller."

    anon "Oh, um..."

    pause
    anon "... I'm sorry?"

    unknown @ f_laugh "Hehe."

    show nadya b_dress_limo4 with dissolve
    anon "Are you going to kill me?"

    show nadya f_normal_smoke_blow b_dress_limo3 with dissolve
    pause
    unknown f_normal "Hmm, I have not decided this yet."

    pause
    unknown f_serious "It is certainly what my papa would be wanting."

    anon "Your papa?"

    unknown "{b}Raznikov Chernyshevsky{/b}."

    unknown "You have heard of him, I think?"

    anon "Ya."

    anon "He killed my dad."

    unknown f_normal "Mhmm, this is my understanding too."

    show nadya b_dress_limo4 with dissolve
    pause
    show nadya f_normal_smoke_blow b_dress_limo3 with dissolve
    pause
    unknown f_normal "And now, you are wishing for retribution, yes?"

    anon "Ehh-"

    unknown "Tsk, I do not think you will be getting this."

    unknown "... My papa is powerful man."

    unknown "Very difficult to get to him..."

    anon "Ya, aku sadar."

    unknown "... But not impossible."

    pause
    unknown "Perhaps we could help one another, hmm?"

    show nadya b_dress_limo4 with dissolve
    anon "Tunggu sebentar."

    anon "A-are you saying you wanna help me..."

    show nadya f_normal_smoke_blow b_dress_limo3 with dissolve
    anon "... Kill your father?"

    unknown f_normal "Ya."

    pause
    anon "And why would you do that... ehh, Miss?"

    unknown f_serious "{b}Nadya{/b}."

    nadya "{b}Nadya Chernyshevsky{/b}."

    anon "Okay, {b}Nadya{/b}."

    anon "Why do you want your father dead?"

    nadya "Because he is evil man."

    nadya f_normal "Is this not reason enough?"

    show nadya b_dress_limo4 with dissolve
    anon "D'ahh..."

    anon "... I mean, lots of people have evil fathers..."

    show nadya f_normal_smoke_blow b_dress_limo3 with dissolve
    anon "... Not many try and have them killed."

    nadya b_dress_limo8 f_serious "This is because most people are cowards."

    anon "( !!! )"
    nadya f_angry "You must understand..."

    nadya "... My papa has big asshole."

    anon "{i}*Snort*{/i} What did you just say?!"

    nadya b_dress_limo9 f_confused "He has big asshole?"

    show nadya b_dress_limo3 with dissolve
    anon "Heh, I think you mean he {i}IS{/i} a big asshole."

    nadya f_angry @ f_eyeroll "Ugh, terserah."

    nadya "He is wanting control of everything I do!"

    nadya "What I wear."

    nadya "Where I go."

    nadya "Who I am friends with."

    nadya b_dress_limo9 "No more!!!"

    nadya "I am grown woman and I want him gone!"

    nadya "Dead and buried!"

    anon "( Okay, this girl is crazy! )"

    nadya "He is not fit to lead Bratva!"

    anon "Bratva?"

    nadya f_surprised b_dress_limo10 "aku tidak-"

    show nadya b_dress_limo8 with dissolve
    anon "What's that mean?"

    nadya f_serious_right "Is not important."

    anon "No, I wanna know."

    show nadya b_dress_limo4 with dissolve
    pause
    show nadya f_normal_smoke_blow b_dress_limo3 with dissolve
    pause
    show nadya f_normal with {'master': dissolve}
    anon "You want my help or not?"

    nadya f_eyeroll "{i}*Sigh*{/i} Shit!" (show_native="{i}*Sigh{/i} Der'mo!")
    nadya "I don't know, what is American word..."

    nadya f_confused "... Ehh, it is when the criminal makes monies from illegal business..."

    pause
    anon "Mafia?"

    nadya f_serious "Da, mafia."

    nadya f_serious_right "Silly word."

    show nadya b_dress_limo4 with dissolve
    anon "So you want to take your father's place?"

    show nadya f_normal_smoke_blow b_dress_limo3 with dissolve
    pause
    show nadya f_normal with {'master': dissolve}
    anon "Mengapa?"

    nadya f_angry "Kenapa tidak?"

    nadya b_dress_limo9 "You think woman cannot run Bratva?!"

    anon "( !!! )"
    anon "N-no, I'm not saying that!"

    anon "I just mean, what will you do..."

    anon "... Once you're in control?"

    show nadya b_dress_limo3 with dissolve
    pause
    nadya "My papa take many risk, trafficking drugs and whores into your country."

    nadya "These are old ways of thinking."

    nadya "He is too stupid to see that there are real, legitimate business opportunity here!"

    show nadya f_serious
    anon "Business opportunities?"

    nadya "Ya."

    pause
    nadya b_dress_limo8 "I will say no more."

    pause
    nadya "But when I am in charge..."

    nadya "... men will stop harassing your family."

    nadya b_dress_limo3 "This I promise."

    show nadya b_dress_limo4 with dissolve
    pause
    show nadya f_normal_smoke_blow b_dress_limo3 with dissolve
    anon "Well, that's a nice start, I suppose."

    show nadya f_normal with {'master': dissolve}
    pause
    anon "So, how exactly do you expect to pull this off?"

    nadya f_normal "I get you into room with my papa and you kill him."

    nadya b_dress_limo11 "Bang."

    anon "( !!! )"
    anon "You can do that?"

    nadya b_dress_limo3 "Ya."

    nadya "There is secret entrance to {b}warehouse{/b}."

    nadya "Not many know of it."

    anon "( Holy crap, this is exactly what I've been looking for! )"

    anon "A-and you'll show my friend and I this secret way?"

    nadya "Da..."

    nadya b_dress_limo10 "... If you do something for me first!"

    anon "( Ugh, I knew there was going to be a catch! )"

    show nadya b_dress_limo4 with dissolve
    anon "That depends on what you want."

    show nadya f_normal_smoke_blow b_dress_limo3 with dissolve
    pause
    nadya @ f_eyeroll "Is small thing."

    anon "I'm listening."

    nadya f_serious "There is bank in town... ehh, I believe is called {b}Saga Financial{/b}?"

    anon "Yeah, I know it."

    nadya "And in the basement of bank, is large vault."

    anon "Mhmm?"

    nadya "Inside large vault, is black briefcase."

    anon "A black briefcase?"

    nadya "Ya."

    nadya f_normal "You will retrieve briefcase and bring to me."

    anon "Apa?!"

    anon "Bagaimana saya bisa melakukan itu?"

    nadya f_confused @ -m_talk "Hmm?"

    nadya "You sneak into disgusting {b}Mayor{/b}'s house, yes?"

    anon "Y-ya, tapi-"

    nadya f_confused @ f_normal "So now, you sneak into bank."

    nadya "Why is problem?"

    show nadya b_dress_limo4 with dissolve
    anon "Banks have cameras..."

    anon "... And alarms..."

    show nadya f_normal_smoke_blow b_dress_limo3 with dissolve
    anon "... Which bring police."

    nadya f_normal "Psh, I'm sure you can figure it out."

    nadya "You're cleaver boy, aren't you?"

    anon "Entahlah..."

    pause
    anon "... Why do you need this briefcase anyways?"

    nadya f_serious "That is no concern to you."

    anon "Well, with all due respect, I disagree."

    anon "This is a federal crime you're asking me to commit..."

    anon "... On top of killing your father for you."

    nadya f_angry @ -m_talk "..."
    anon "It's a pretty big ask, don't you think?"

    nadya "Are you wanting revenge or not?"

    anon "Yes but how will I get revenge if I'm arrested for bank robbery?"

    anon "This could land me in prison for a long time."

    pause
    anon "Why should I risk it?"

    nadya f_serious_right "{i}*Sigh*{/i} The item in briefcase is of consequence only to Papa and I..."

    pause
    nadya f_serious "... If you bring me, I might be able convince some of Papa's men to turn on him when you attack warehouse."

    nadya "That is worth risk, yes?"

    anon "Hmm."

    anon "I suppose so..."

    pause
    anon "... But how do I know you'll hold up your end of the bargain?"

    nadya "Neither of us can kill my papa alone."

    nadya f_normal "Only by working together can we accomplish this..."

    pause
    nadya "... Surely you can see benefit of arrangement?"

    anon "Yeah, I see it."

    anon "But the question remains, why should I trust you?"

    nadya f_serious "You do not trust me?"

    anon "Tentu saja tidak."

    nadya f_normal "Tsk, this is shame..."

    nadya "I was wanting we could be friends."

    anon "Friends?"

    anon "Why would we-"

    show nadya b_dress_limo1 with dissolve
    anon "( !!! )"
    nadya b_dress_limo2 f_pouting "You do not wish to be my friend?"

    anon "I-itu bukan-"

    nadya "My papa has never allow me friends, {b}[firstname]{/b}..."

    nadya f_normal_down "... But I am thinking you could be my first."

    anon "{i}*Gulp*{/i} Y-your first?"

    nadya f_normal @ -m_talk "Mhmm."

    nadya "I am not the type to be hurting my friends..."

    nadya "... Or their families."

    pause
    nadya "So let us be friends... yes?"

    anon "I'll uhh-"

    pause
    anon "I'll need time to think this over."

    nadya "Tentu saja."

    show nadya b_dress_limo1 with dissolve
    pause
    nadya b_dress_limo3 "You wish to talk with fat man with pretty wife at restaurant."

    anon "( Does she mean {b}Tony{/b} and {b}Maria{/b}?! )"

    nadya "I'm sure they agree is good deal."

    anon "( I wonder what else she knows? )"

    pause
    nadya "Driver will give you contact number."

    nadya b_dress_limo10 f_angry "But I warn you... Only dial if we are to be friends."

    nadya "Otherwise, the next time we meet..."

    show nadya b_dress_limo11 with dissolve
    pause
    nadya "Bang."

    nadya b_dress_limo3 f_normal "Memahami?"

    anon "Y-yeah, I get it."

    nadya "Bagus."

    show nadya b_dress_limo4 with dissolve
    pause
    show nadya f_normal_smoke_blow b_dress_limo3 with dissolve
    pause
    nadya b_dress_limo9 f_angry "Now get the fuck out of my car."

    anon "!!!"

    scene location_mugging_closeup
    show anon f_worried a_sides
    with fade
    anon @ -m_talk "(Yah, itu tidak terduga...)"

    anon @ -m_talk "( ... And a little terrifying. )"

    pause
    anon @ -m_talk "( Can I really trust her? )"

    anon f_thinking @ -m_talk "( If so, this is worth considering. )"

    pause
    anon @ -m_talk "( {b}I should swing by the pizzeria tomorrow{/b} and see what {b}Tony{/b} makes of all this. )"

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
