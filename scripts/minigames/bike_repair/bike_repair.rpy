label bike_repair_minigame_prepare:
    call screen bike_repair_minigame()

label bike_repair_success:
    scene expression player.location.background_blur with None
    show anon o_oil
    show eve f_happy
    with dissolve
    anon "Okay, you wanna try and start her?"

    eve "A-aku?"

    eve @ f_laugh "Ya, ya!"

    anon "Well, go ahead."

    hide eve with dissolve
    "{i}*Engine revving*{/i}"

    pause
    "{i}*Engine starts*{/i}"

    eve "!!!"

    scene location_tattoo_garage_cutscene01
    show text _ ("{b}Eve{/b} started as the engine hummed to life. The surprise on her face was priceless!\nThough, to be honest, I was just as surprised.\nI really hadn't expected my tiny repairs would fix the problem.") as caption
    with fade
    pause
    scene expression player.location.background_blur
    show anon o_oil
    show eve f_happy
    with fade
    eve "You're amazing!"

    hide eve
    show anon b_hug_eve f_shy_down
    with dissolve
    pause
    show odette:
        xoffset 100
    show grace f_surprised:
        xoffset -100
    with dissolve
    grace "What the hell-"

    grace f_happy "You got it started?"

    show anon b_dressed f_normal:
        xoffset -66
    show eve f_happy zorder 1:
        flip
        xoffset 250
    with dissolve
    eve "{b}[firstname]{/b} did it!"

    anon "Heh, I just taped a couple wires and tightened a few bolts..."

    anon "You did all the hard stuff."

    show grace b_dressed_hug_mc:
        xoffset -400
    show anon b_empty zorder 2
    show eve:
        unflip
        xoffset -200
    with dissolve
    grace "Oh my god, thank you!"

    odette "Your boyfriend is full of surprises, {b}Evie{/b}..."

    eve "Aku tahu, kan?!"

    pause
    eve "You think we could take it for a spin?"

    show grace b_dressed:
        xoffset -100
    show anon b_dressed zorder 0
    show eve:
        flip
        xoffset 250
    with dissolve
    grace "Apa?!"

    eve @ f_eyeroll "Oh c'mon, we're old enough!"

    grace f_uneasy "You don't even have a license!"

    eve "{b}[firstname]{/b} has one!"

    grace @ -m_talk "..."
    eve "We'll be careful!"

    grace f_sad_down "Entahlah..."

    odette @ f_eyeroll "Oh, let them take it around the block a few times, {b}Grace{/b}..."

    odette "He did fix it for you, after all!"

    show odette f_wink
    grace f_normal @ f_sad_back "{i}*Sigh*{/i} You're right."

    show odette f_normal
    eve "YA!!!"

    grace @ f_uneasy "... But just around the block, okay?!"

    show anon a_empty b_empty f_surprised_left zorder 1:
        flip
        xoffset -694
    show eve a_grab_mc:
        unflip
        xoffset -350
    with dissolve
    eve "Ayo, {b}[firstname]{/b}!"

    anon "!!!"
    hide anon
    hide eve
    with dissolve
    grace "Put helmets on!"

    hide grace with dissolve
    odette @ f_laugh "hehe!"


    scene location_tattoo_garage_cutscene02
    show text _ ("It felt good to be the hero and earn some major brownie points with {b}Eve{/b} and her sister.\nPlus we got to take {b}Grace{/b}'s bike out for a ride! Which was awesome!") as caption
    with fade
    pause

    scene location_tattoo_garage_cutscene03
    show text _ ("We had an absolute blast and {b}Eve{/b} looked adorable in that helmet!\nI don't think I had ever seen her so happy...") as caption
    with fade
    pause

    $ game.timer.tick(2)

    scene expression player.location.background_blur
    show odette:
        xoffset 100
    show grace f_happy:
        xoffset -100
    with fade
    show anon o_helmet:
        xoffset -75
    show eve f_happy b_dressed_hoodless o_helmet:
        flip
        xoffset 250
    with dissolve
    grace "You're pretty good on that thing!"

    anon "Terima kasih."

    eve "Itu."

    eve "Dulu."

    eve @ f_laugh "LUAR BIASA!"

    odette @ f_laugh "hehe!"

    eve "Wow, we were really flying!"

    show eve a_remove_helmet o_empty with dissolve
    pause
    eve a_idle "Did you see us, {b}Grace{/b}?"

    grace "Hehe, yes I saw you."

    odette "You're so cute..."

    eve f_angry "Diam!"

    grace "We should probably get back to the shop."

    odette @ f_eyeroll "Psh, screw that!"

    odette "Your bike is finally fixed and it's getting late anyways..."

    odette f_smirk "Let's go upstairs and celebrate!"

    eve f_happy "Ya!"

    grace f_uneasy "What if a customer comes and-"

    odette "{b}Grace{/b}, seriously!"

    odette "You can take one night off..."

    grace f_sad_back "..."
    eve "C'mon, {b}sis{/b}!"

    show grace f_sad
    eve "You really need a break."

    grace f_happy @ f_eyeroll "{i}*Huh*{/i} Baiklah, baiklah."

    odette "Thank god!"

    odette "Grab us some drinks and get the fire started, I'll close up."

    grace f_sad_back "Anda yakin?"

    odette "Yes, go!"

    hide odette with dissolve
    show grace f_happy
    odette "Saya akan segera ke sana."

    grace "You wanna help me?"

    eve "Benar sekali!"

    hide grace with dissolve
    show eve:
        unflip
        xoffset -400
    eve "Ayo, {b}[firstname]{/b}!"

    hide eve with dissolve
    anon "O-oke."

    hide anon with dissolve
    $ player.go_to(L_tattooparlor_roof)
    scene expression player.location.background_blur with None
    show anon a_cooler
    show eve f_happy:
        xoffset -200
    show grace f_happy:
        xoffset 100
    with dissolve
    eve "... So the fucking idiot decides he's going to climb up on our roof and cannonball into our pool!"

    anon "Sialan, benarkah?"

    eve "Hehe, ya!"

    eve "Only he's so drunk, he gets about halfway up the lattice and falls off into {b}our mom{/b}'s thorn bushes!"

    anon "Mustahil!"

    eve @ f_laugh "Haha, seriously!"

    grace @ f_eyeroll "Yeah, {b}Tuuku{/b} always does stupid shit when he's drinking..."

    eve f_happy_right "He's not the only one!"

    eve "Remember {b}Odette{/b} and the table?"

    grace @ f_proud a_facepalm "Oh god, I forgot about that..."

    eve @ f_laugh "hehe!"

    anon "Oh, tell me!"

    eve f_happy "She was trying to impress some guy she really liked and this funny hip-hop song came on the radio..."

    eve f_happy_right "What was it called?"

    grace @ f_eyeroll "\"Baby Got Stacked\"."

    eve @ f_laugh "Haha, that's it!"

    eve f_happy "It's basically a song about a girl with giant tits."

    anon "Hehe, oke..."

    eve "So this song comes on and {b}Odette{/b}, who had been drinking rum and cokes all night, decides she's going to get up on the table and dance!"

    anon "Sungguh?"

    eve "Haha, ya!"

    eve "... And we're talking real slutty dancing too, you know, because she's trying to seduce this guy..."

    anon f_flirt_grin @ -m_talk "Mmhmm."

    eve "She's got her bikini top on and her tits are bouncing all over the place, so of course, every guy at the party is mesmerized!"

    grace "Heh, she has such an unfair advantage..."

    eve "Saya tahu, kan?"

    show anon f_surprised
    grace @ f_proud a_boobs "I would kill for tits like that..."

    eve f_happy_right "Oh, please!"

    eve "It could be a lot worse, you know?"

    eve f_disgusted_wince_down a_boobs "I mean, look at these pathetic things!"

    show anon f_flirt_grin
    grace "No, yours are cute."

    grace "They're like, super perky, guys love that!"

    eve f_happy a_idle @ f_eyeroll "Ya benar."

    eve "Pretty sure, {b}[firstname]{/b} is the only guy who likes them..."

    show eve f_happy_right
    grace f_sexy "Ah, benarkah?"

    grace "So you like my sister's tits, {b}[firstname]{/b}?"

    show eve f_nervous_down
    anon f_worried "Uhh, yeah... Of course I do."

    anon f_flirt "I think they're perfect."

    eve f_nervous "P-perfect?"

    grace f_happy @ f_uneasy "Aduh."

    anon f_grin @ f_worried "B-but yours are nice too!"

    grace "Okay, you definitely found a keeper with this one..."

    show anon f_hurt
    eve f_happy @ f_happy_right "Hehe, I think so too."

    anon f_worried "So what happened next?"

    eve @ -m_talk "Hmm?"

    anon "With {b}Odette{/b} and the table?"

    eve "Oh benar!"

    eve "Well, she's up on the table dancing and everyone starts chanting, \"Take it off!\" Over and over."

    anon "{i}*Gulp*{/i} D-did she do it?"

    grace @ f_eyeroll "Of course she did, it's {b}Odette{/b}..."

    eve "Hehe, except right as she started to untie her top, the table broke!"

    anon f_surprised "You're joking?!"

    eve "Haha, nope!"

    eve "It snapped right down the middle and she went flying!"

    eve "Broke her arm, in two places."

    anon f_worried "Sial."

    grace "Itu benar."

    grace "I had to drive her to the hospital..."

    eve f_happy_right "That's nothing compared to the night you had to get your stomach pumped..."

    grace f_weary @ f_disgusted "Eugh, don't make me relive that one, please."

    eve f_happy @ f_laugh "Haha!"

    show anon f_hurt
    show grace f_happy
    eve "I'm telling you, my sister used to be the queen of throwing parties!"

    show anon f_worried
    grace @ f_eyeroll "That was a long time ago..."

    eve f_sad_right "Now she just works all the time."

    grace f_normal a_hips_mad "Tsk, well, somebody has to act like an adult around here..."

    grace "God knows {b}Odette{/b} and {b}Tuuku{/b} never will."

    eve "Ya, ya..."

    eve "Just, not tonight, okay?"

    grace f_sad "I'm really not that person anymore, {b}Eve{/b}..."

    eve "C'mon, {b}Grace{/b}!"

    eve "I want to hang out with my fun, crazy, older sister again!"

    grace "{i}*Sigh*{/i} I'll try, okay?"

    eve f_normal_right "I don't know why it's so hard for you to-"

    grace "{b}Eve{/b}, please don't start."

    pause
    grace "Why don't you go and get the fire started?"

    eve "I've never done that before, but okay..."

    hide eve with dissolve
    show grace f_happy:
        flip
        xoffset 600
    with dissolve
    if M_eve.biggus_dickus:
        grace "Didn't {b}Dad{/b} enroll you in boy scouts when you were younger?"

    else:
        grace "Didn't {b}Dad{/b} enroll you in girl scouts when you were younger?"

    eve "He tried but I refused to go, remember?"

    show anon f_hurt
    show grace f_thinking
    pause
    show anon f_tired
    grace f_happy "Oh ya."

    grace "I can't believe you got away with that!"

    pause
    grace "Man, you really were his favorite..."

    if M_eve.biggus_dickus:
        grace "He had me in girl scouts for six years!"

    else:
        grace "He had me going to those meetings for six years!"

    eve "Well, I wasn't his favorite for very long..."

    pause
    show anon f_hurt
    grace "That's true, I guess..."

    show grace:
        unflip
        xoffset 0
    with dissolve
    pause
    show grace f_suspicious
    pause
    grace "You want some help carrying that?"

    anon f_tired "T-tidak, tidak apa-apa."

    grace "Apa kamu yakin?"

    show anon f_disgusted_wince
    grace "It has to be heavy..."

    anon f_cough "Really, it's fine {b}Grace{/b}."

    show grace f_eyeroll
    anon "I've got it."

    show anon f_hurt
    show grace f_normal
    eve "You do realize, I have no idea what I'm doing over here..."

    anon f_disgusted_wince "You should probably go and help her."

    "{i}*Snap*{/i}"

    show anon f_cough
    show grace:
        flip
        xoffset 600
    with dissolve
    eve "Ouch, motherfu-"

    show anon f_hurt
    eve "Damn it, I broke a nail!"

    grace f_happy "Hehe, I think you're right about that."

    show grace:
        unflip
        xoffset 0
    with dissolve
    grace @ a_idea "Just put the beer over there by the tent."

    anon f_disgusted_wince "Tentu saja."

    hide grace with dissolve
    grace "Let me do it."

    anon f_surprised_teeth_down @ -m_talk "( Man, this thing is heavier than it looks! )"

    anon f_hurt @ -m_talk "( How many beers did they cram into it, I wonder? )"

    grace "Go and get the music started."

    show anon f_disgusted_wince
    eve "Now you're talking my language!"

    show anon b_dressed_pickup:
        flip
        xoffset 0
    with dissolve
    pause
    show anon b_dressed_catch_breath with dissolve
    pause
    hide anon with dissolve
    $ M_eve.trigger(T_eve_bike_breakdown_repaired_bike)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
