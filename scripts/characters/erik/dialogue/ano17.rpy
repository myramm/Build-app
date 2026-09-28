label ano17_erik_erik:
    scene expression background(768, 400, 2.) as stage
    show erik b_dressed_back_bending
    show anon f_normal_low with dissolve
    anon "What are you doing in here?"
    erik "Digging out my old board games."
    anon f_disgusted_low "Huh?"
    anon "Why are you doing that?"
    show erik b_dressed
    show anon f_normal
    with dissolve
    erik "Because the mayor's daughter is coming over, isn't she?"
    anon @ f_confused "Yeah?"
    erik "Well, we're gonna need something to entertain her, aren't we?"
    anon f_surprised "And you think board games are gonna do that?"
    erik "Umm, yes?"
    anon f_worried @ a_facepalm "{b}Iwanka{/b} is a college girl, man..."
    anon "She doesn't wanna play board games."
    erik f_woozy @ f_laugh "Aww, c'mon!"
    erik "I have all the classics!"
    erik "{i}Hungry, Hungry, Pachyderms.{/i}"
    show anon f_unimpressed
    erik "{i}Cockamamie Camels{/i}."
    erik "{i}Mitzvah Moon Menagerie{/i}."
    anon "No."
    erik f_worried "{i}Who Plotzed on the Kugel{/i}?"
    anon f_disgusted "Eww, definitely not!"
    erik f_nervous "Well, I don't know what we're going to do then!"
    erik f_surprised "She's gonna be here any second."
    anon a_thinking f_thinking @ f_brag_closed a_wave "Calm down!"
    anon "Let's start by setting the mood."
    anon "Do you have good dance music?"
    erik f_worried "Ehh, hold on."
    hide erik
    show anon f_normal a_idle
    with dissolve
    pause
    show anon f_surprised
    pause
    show anon b_dressed_bending1 with dissolve:
        xoffset 400
    pause
    erik "I've got the new Dr. Dreidel here somewhere..."
    show anon b_dressed f_thinking with {'master': dissolve}:
        flip
        xoffset 0
    anon "Mm, I think that might be too aggressive."
    show anon f_normal
    erik "Jewfro Tull?"
    anon f_unimpressed "No."
    erik "Black Shabbat?"
    show anon f_thinking a_thinking with dissolve
    pause
    anon f_worried a_idle "I really don't think {b}Iwanka{/b} is into rock music..."
    erik "Kosher Me Badd?"
    anon f_disgusted "Yuck!"
    anon "No way!"
    erik "Barmitzvah Streisand?"
    anon f_confused "What the-"
    anon "Umm, why do you have that?"
    erik "She's my landlady's favorite."
    anon @ f_worried -m_talk "..."
    anon "Don't you have anything other than Jewish bands?"
    erik "Not really."
    anon f_sad_down a_sides "{i}*Sigh*{/i} This is not a promising start, {b}Erik{/b}."
    pause
    erik "Boys II Mensch?"
    anon f_unimpressed "What is that, Jewish R&B?"
    erik "Yeah."
    anon @ f_shy_cringe a_facepalm "Ugh, it'll have to do."
    erik "Cool!"
    erik "Lemme set it up."
    pause
    show anon f_normal
    show erik:
        flip
    with dissolve
    erik "Done."
    erik "Now what?"
    anon "She specifically mentioned wanting alcohol."
    erik f_woozy "Well, that's no problem!"
    erik "{b}Mr. Johnson{/b} kept the bar down here fully stocked."
    anon "At least we have that going for us..."
    anon "Did you get snacks?"
    erik f_bored "Dude, who do you think you're talking to?"
    erik f_normal @ f_laugh "I got us three and a half bags of cheese puffs!"
    anon f_worried "Cheese puffs?"
    erik "Yup, and a big bowl of nacho cheese dip!"
    anon f_sad_down a_rub "Aww, man..."
    erik "I call dibs on the half bag!"
    anon f_worried a_sides "We can't serve the mayor's daughter cheese puffs..."
    erik f_worried "Why not?"
    anon "Because we just can't, okay?"
    anon f_normal a_idle "Go upstairs and find something else."
    erik f_bored "I don't think you understand how delicious cheese puffs are, dude!"
    erik "They literally melt in your mouth!"
    tammy "{b}Erik{/b}, sweetie, you got a visitor!!"
    show anon f_sad_down a_sides with dissolve
    erik f_nervous @ f_surprised "Oh, man... She's here!!!"
    erik "What do we do?!"
    anon "Ugh, this is going to be a disaster..."
    erik f_worried "Don't be like that, {b}[firstname]{/b}."
    erik "You're supposed to be the confident one!"
    anon f_worried "You're not going to lock up again, are you?"
    erik "N-no."
    erik f_woozy @ f_laugh a_whisper "I've got a plan, you'll see."
    tammy "Where the heck are you boys?"
    anon f_sad_down @ a_rub "We're coming!"
    hide anon with dissolve
    show erik f_nervous a_faint with dissolve
    pause
    erik a_proud f_worried "Hello, {b}Iwanka{/b}... My name is {b}Erik{/b}."
    pause
    erik f_normal "It's so nice to meet you!"
    erik a_thinking "Phew, okay."
    erik a_idle @ a_facepalm "I can do this!"

    scene expression background(560, 440, 3., l=L_erikhouse_basement) as stage
    show tammy a_sides:
        flip
        xoffset 100
    show iwanka b_club a_popsicle f_disgusted:
        flip
        xoffset -120
    with fade
    show anon f_shy with dissolve:
        flip
        xoffset 150
    tammy "There you are."
    anon @ a_wave "Hey!"
    tammy f_suspicious "I thought you said a girl was coming over?"
    tammy "This is a grown woman..."
    show iwanka f_smirk
    show erik f_nervous behind tammy:
        xoffset -40
    with dissolve
    anon f_shy @ f_worried "Ehh."
    erik "H-hi."
    show tammy f_normal
    erik a_proud "{i}*Ahem*{/i} Hi-loh!"
    show anon f_shy
    iwanka f_disgusted "Uhh?"
    erik a_idle "It's nice to meet you..."
    erik "I'm {b}Iwanka{/b}."
    show tammy f_suspicious
    anon f_worried @ -m_talk "..."
    erik @ a_thinking "Err, I mean, {b}Erik{/b}!"
    erik "I'm not {b}Iwanka{/b}... You're {b}Iwanka{/b}!"
    show tammy f_sad
    show anon f_tired a_facepalm
    with dissolve
    iwanka "Yeah, I'm aware..."
    show anon f_shy a_idle with dissolve
    erik "You look... Umm..."
    erik "T-this is my..."
    show erik a_facepalm with dissolve
    pause
    erik a_proud @ f_laugh "Welcome!"
    iwanka f_concerned "Is he okay?"
    show erik f_sad a_idle
    show anon f_sad_down
    with dissolve
    anon "{i}*Sigh*{/i} Probably not."
    show anon f_shy
    show erik f_nervous
    show tammy f_suspicious a_idle behind erik:
        unflip
        xoffset -300
    with dissolve
    tammy "How old are you anyways?"
    iwanka f_normal @ -m_talk "Hmm?"
    iwanka "Oh, uhh... Almost twenty-seven."
    tammy @ f_surprised "Oy vey!"
    tammy "Does your mother know you walk around dressed like this?"
    show iwanka f_smirk
    erik f_surprised "{b}Tam{/b}!!"
    show tammy f_annoyed with dissolve:
        flip
        xoffset 100
    tammy "What?!"
    tammy "I'm not allowed to show interest in the girls my little boy brings home?"
    erik f_nervous @ a_whisper "You're embarrassing me!"
    show iwanka f_normal
    tammy f_suspicious "Oh, don't be silly..."
    tammy "... There's no reason to be embarrassed."
    tammy f_normal "I'm just happy to see you're finally off that verkakte computer."
    show erik behind tammy
    tammy a_pinch @ f_laugh "My little oyster's finally growin' up."
    show tammy a_pinch_wave
    show erik a_shoo f_angry
    with dissolve
    erik "Stop that!"
    show erik a_idle
    show tammy a_idle f_laugh
    with dissolve
    tammy "Hehehe!"
    show tammy f_normal a_sides behind erik with dissolve:
        unflip
        xoffset -380
    tammy "Isn't he adorable?"
    show tammy with dissolve:
        flip
        xoffset 100
    tammy "I'm proud of you boys."
    tammy "You {i}should{/i} be out chasin' girls, instead of sittin' here on your tuchis all day."
    show tammy f_annoyed with dissolve:
        unflip
        xoffset -300
    tammy "Just try and find one a little less whorish next time, okay?"
    show iwanka f_surprised
    show erik f_surprised
    anon f_surprised_teeth "!!!" with hpunch
    show anon f_hurt
    iwanka f_annoyed a_popsicle_fists "Excuse me?!"
    show anon f_worried
    tammy @ f_laugh "No offense, dear."
    erik @ -m_talk "..."
    anon "Umm, {b}Mrs. Johnson{/b}... Can you give us a little privacy, please?"
    show tammy f_sad with dissolve:
        flip
        xoffset 100
    tammy @ -m_talk "Hmm?"
    tammy f_normal "Oh, sure."
    tammy "Should I warm up some pizza pockets for your little party?"
    erik f_normal @ f_laugh "Oh, pizza pockets!"
    anon @ f_unimpressed "No, we're good..."
    show erik f_sad with {'master': dissolve}:
        flip
        xoffset 380
    erik "Aww, but-"
    anon f_normal "Thanks anyway."
    tammy a_idle "Alright, have it your way."
    show erik:
        unflip
        xoffset -20
    show tammy f_laugh
    with {'master': dissolve}
    tammy f_normal @ f_laugh "You kids play nice, okay?"
    show anon f_hurt a_facepalm with dissolve
    pause
    anon a_idle f_tired "{i}*Sigh*{/i} We will, {b}Mrs. Johnson{/b}."
    iwanka @ -m_talk "..."
    show tammy f_annoyed with dissolve:
        unflip
        xoffset -260
    pause
    tammy a_watch @ -m_talk "...{w=.4}{nw}"
    show iwanka f_surprised
    show anon f_surprised
    with {'master': fastdissolve}
    tammy @ -m_talk "..."
    hide tammy with dissolve
    anon f_worried "I'm really sorry about that..."
    show iwanka f_annoyed
    iwanka a_popsicle_wtf @ f_suspicious_down "Tsk, what's wrong with my dress?!"
    anon f_shy "N-nothing!"
    anon "You look great!"
    show iwanka a_popsicle_fists with dissolve
    anon f_normal "Doesn't she look great, {b}Erik{/b}?"
    erik @ f_surprised "!!!"
    erik "Uhh..."
    show anon f_shy
    iwanka "I know I look great!"
    iwanka "This is a thirty-five-hundred-dollar Poolada dress!"
    anon f_shock "Thirty-five hundred dollars?!"
    iwanka a_popsicle_give "Would someone please take this?"
    iwanka "I told her I didn't want one but she insisted."
    show iwanka a_idle
    show erik a_popsicle f_woozy:
        xoffset -40
    with dissolve
    anon f_shy "Yeah, she does that."
    show iwanka f_surprised_up
    erik a_popsicle_eat f_eat @ -m_talk "Nom!"
    iwanka f_disgusted "So, is this the party?"
    iwanka "Where is everybody?"
    anon f_worried "Oh, umm... I'm sure more are coming."
    show erik a_whisper f_nervous with {'master': dissolve}:
        flip
        xoffset 400
    erik "Dude, who else did you invite?"
    anon @ f_worried_low "Nobody but she doesn't know that..."
    show erik a_idle with {'master': dissolve}:
        unflip
        xoffset -40
    erik @ f_normal_right "Oh, right!"
    anon f_shy @ a_behind_head "They're probably just trying to be fashionably late, you know?"
    iwanka f_normal @ f_laugh "Aww, see... I knew I should have done that!"
    iwanka "Nobody wants to be the first to arrive at a party."
    anon "Can we get you a drink or something?"
    iwanka @ f_laugh "Oh, a drink, please!"
    iwanka "Something strong but fruity."
    anon f_normal "Coming right up!"
    anon "{b}Erik{/b}, could you?"
    erik f_worried_right "Huh?"
    anon f_worried "Go make {b}Iwanka{/b} a drink."
    erik f_sad "Ehh..."
    show erik a_whisper with dissolve:
        flip
        xoffset 400
    erik "I don't know how to do that!"
    anon @ f_worried_low "Can't you just look it up on your phone or something?"
    erik f_laugh @ f_surprised "Oh, right!"
    erik "Good idea, {b}[firstname]{/b}."
    hide erik with dissolve
    show anon f_shy
    pause
    anon "So..."
    anon "Any trouble sneaking out?"
    iwanka f_bored "Nah, my mom was passed out drunk and my dad was preoccupied with one of the maids."
    anon f_shy "I see."
    pause
    anon "Don't you guys have a bunch of security guards though?"
    iwanka f_normal @ f_eyeroll "Pfft, they don't care what I do."
    show erik a_glass f_nervous behind iwanka with dissolve:
        xoffset -40
    pause
    iwanka "Is that for me?"
    erik "Uhh..."
    anon "Yep, it's definitely yours."
    show iwanka a_glass:
        xoffset -20
    show erik a_idle
    with dissolve
    pause
    iwanka f_concerned "He doesn't talk much, does he?"
    anon @ f_normal "Heh, not when pretty girls are around, no."
    iwanka f_normal @ f_laugh "Oh, right!"
    iwanka "I remember you mentioned that in the tree."
    iwanka @ f_laugh "He probably just needs some social lubrication to help him relax."
    anon f_confused "Social lubrication?"
    iwanka "Yeah, you know..."
    iwanka a_glass_drink f_drink @ f_smirk a_glass_cheer "... Booze."
    show anon f_shy
    show erik a_whisper with dissolve:
        flip
        xoffset 400
    erik "Does that really work?"
    anon @ f_worried_low "How should I know?"
    show erik a_idle with dissolve:
        unflip
        xoffset -40
    iwanka a_glass_empty f_smirk "Mmm, I love Screwdrivers!"
    iwanka "That is so freaking delish, like, oh em gee!"
    show erik a_glass_empty
    show iwanka a_idle
    with dissolve
    iwanka "Keep them coming, freckles!"
    pause
    show iwanka f_thinking
    show erik a_whisper with dissolve:
        flip
        xoffset 400
    erik "I'm gonna try it!"
    anon @ f_normal_low "Knock yourself out."
    hide erik with dissolve
    iwanka f_normal "I like it down here."
    anon "You do?"
    iwanka "Yeah, all these guitars and the cool lighting!"
    iwanka "It reminds me of this band I dated a while back."
    anon @ f_confused "Band?"
    anon "You mean you dated a guitar player or something?"
    iwanka "No."
    iwanka "I dated a band."
    anon f_worried "Like, more than one person?"
    show erik a_glass behind iwanka with dissolve:
        xoffset -40
    iwanka "Three to be exact."
    show anon f_surprised
    show erik a_idle
    show iwanka a_glass f_laugh
    with dissolve
    iwanka "Thanks!"
    show iwanka f_normal
    anon f_shy @ f_confused "How do you date three people at once?"
    show erik a_beer with dissolve
    iwanka "Well, to be fair... The drummer and bass player were kinda dating each other."
    show erik a_beer_drink f_drink with dissolve
    iwanka "And I was dating the lead guitarist."
    show erik a_beer f_normal with dissolve
    iwanka "But then one night we got really drunk and sorta had an orgy."
    show erik f_woozy
    anon f_surprised "Really?!"
    iwanka @ f_laugh "Heh, yeah."
    show iwanka a_glass_drink f_drink with dissolve
    pause
    iwanka a_glass_empty f_smirk "Yum!"
    anon f_shy "So you had a foursome with three guys?"
    iwanka "Heh, no."
    show iwanka
    iwanka a_glass_empty_give "The drummer was a girl."
    show iwanka a_idle
    show erik a_glass_empty f_surprised m_talk
    show anon f_shock
    with dissolve
    anon "!!!"
    erik "!!!"
    pause
    show anon f_normal
    show erik a_whisper f_woozy -m_talk:
        flip
        xoffset 400
    with {'master': dissolve}
    erik "Oh, I like her!"
    show erik a_idle with dissolve:
        unflip
        xoffset -40
    show anon f_shy
    iwanka "After that, we had a quad relationship for a while..."
    hide erik with dissolve
    iwanka @ f_eyeroll "... But then shit got super complicated and I had to break up with them."
    anon "Y-yeah, I bet."
    pause
    iwanka f_normal "So, what's on the menu tonight?"
    anon f_worried "Menu?"
    show iwanka f_smirk
    anon "Are you hungry?"
    anon "Because {b}Erik{/b} got us cheese puffs and {b}Mrs. Johnson{/b} could always-"
    iwanka @ f_laugh "Hehe, no silly!"
    iwanka "I meant, what kind of activities are you planning tonight?"
    anon f_shy @ a_behind_head "Oh!"
    anon f_thinking a_thinking "Umm..."
    iwanka @ f_laugh "What the heck are cheese puffs, anyways?"
    show anon a_idle f_shy
    show erik a_glass behind iwanka:
        xoffset -40
    with {'master': dissolve}
    erik "Only the most delicious snack on the planet."
    iwanka "Wow, it speaks!"
    erik "Yeah, it does."
    show erik a_idle
    show iwanka a_glass
    with dissolve
    iwanka "I told you the alcohol would work."
    erik "Yeah, I guess it did."
    iwanka "They don't call it liquid courage for nothing."
    iwanka a_glass_cheer f_laugh "Cheers!"
    erik a_beer_cheer f_laugh "Cheers!"
    show iwanka f_drink a_glass_drink
    show erik a_beer_drink f_drink
    with dissolve
    pause
    show erik a_beer f_woozy with dissolve
    iwanka f_snob a_glass_empty "Woo!!"
    erik @ f_laugh "Hehe!"
    anon f_worried "Maybe you should slow down a little?"
    iwanka f_smirk "Psh, that's not happening!"
    iwanka "This is my first time out in months."
    show iwanka a_idle
    show erik a_glass_empty
    with dissolve
    iwanka "Hit me again, freckles."
    iwanka @ f_laugh "I'm getting wasted tonight!"
    erik @ f_laugh "Coming right up!"
    hide erik with dissolve
    pause
    iwanka @ a_point "So what's in that room over there?"
    anon f_shy @ f_worried -m_talk "Hmm?"
    anon "Oh, it's just the den."
    anon "There's a couch and an entertainment system..."
    anon "... I was actually just about to turn on some music."
    iwanka f_normal @ f_surprised "That is a fantastic idea!"
    iwanka "Let's go."
    hide iwanka
    show anon f_worried a_sides:
        unflip
        xoffset 600
    with dissolve
    anon "W-wait for me!"
    pause
    anon f_thinking a_thinking @ -m_talk "( I better talk to {b}Erik{/b} about those drinks. )"
    hide anon with dissolve
    return

label ano17_talk_erik:
    scene expression background(200, 480, 4.) as stage
    show erik a_glass_empty:
        flip
    show anon f_worried_low with dissolve:
        flip
    anon "Exactly how much alcohol are you putting in those drinks?"
    show anon f_worried
    erik "The website said fifty-fifty vodka and orange juice."
    anon "Alright, well... Maybe we should tone it down a bit."
    erik @ f_sad "Tone it down?"
    anon "I can't ask about her dad and the Russians if she's unconscious, now can I?"
    erik f_woozy "Relax, dude."
    erik "This isn't some teenage girl from school."
    erik "I'm pretty sure {b}Iwanka{/b} can handle her alcohol..."
    anon f_sad "{b}Erik{/b}, I'm serious!"
    anon "This is important."
    erik "Trust me, dude!"
    anon @ f_unimpressed -m_talk "..."
    iwanka "{b}[firstname]{/b}!!"
    show anon f_worried with dissolve:
        unflip
        xoffset 500
    anon @ -m_talk "Hmm?"
    iwanka "Are you coming?"
    anon "Yes, be right there!"
    show anon with dissolve:
        flip
        xoffset 0
    erik "I'll handle the drinks."
    erik "You just focus on getting some answers out of her."
    anon f_sad_down a_sides "Ugh, fine."
    hide anon with dissolve
    return

label ano17_porn_erik:
    scene expression player.location.background_blur
    show anon f_shy with dissolve
    anon @ -m_talk "( I should hurry to {b}Iwanka{/b}. )"
    anon @ -m_talk "( She's in the den. )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
