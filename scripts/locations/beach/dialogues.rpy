label treasure_open_no_key:
    player_name "( Even if I had the combination I still need to find the {b}key{/b}! )"

    return

label beach_island_aqua_treasure_search:
    scene location_beach_island_blur
    show player 11 at left with dissolve
    pause
    show player 10
    player_name "That's one {b}strange looking statue{/b}."

    show player 2
    player_name "..."
    player_name "But according to the map, the {b}treasure{/b} should be right here."

    hide player with dissolve
    return

label beach_statue_no_shovel:
    scene location_beach_island_blur
    show player 2 at left
    player_name "( I can't dig for {b}buried treasure without a shovel{/b}. )"

    show player 4
    player_name "( ... I think we have one at {b}home{/b} somewhere. )"

    hide player with dissolve
    return

label beach_statue_aqua_treasure_search:
    scene location_beach_digging01
    show text _ ("I continued to dig for what must have been hours...") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("... Before long I started to tire, my arms aching.") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("Exhaustion was about to overtake me and I considered giving up.") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("Was I in the wrong spot?") as caption with dissolve
    pause

    scene location_beach_digging02
    show text _ ("... Then, bang! My shovel hit something hard!") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("My strength returned in an instant as I hurried to uncover what Ben Dover had buried.") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("... It was a large heavy chest; this was it! I had found the treasure!") as caption with dissolve
    pause
    return

label treasure_lock_intro:
    scene location_beach_lock with fade
    player_name "Ya ampun..."

    player_name "( It looks like I need a {b}key{/b}... And a {b}combination{/b} to open this. )"

    return

label treasure_unlocked:
    scene expression L_beach_island_chest.background
    if M_aqua.is_state(S_aqua_treasure_unlock):
        call expression game.dialog_select("treasure_aqua_treasure_unlock")
        $ player.get_item("golden_compass")
        $ M_aqua.trigger(T_aqua_treasure_unlocked)
    else:

        with fade
        pause
    $ game.main()

label treasure_aqua_treasure_unlock:
    show expression "objects/object_compass_01.png" at Position(xpos = 537, ypos = 473)
    with fade
    hide expression "objects/object_compass_01.png"
    call screen treasure_chest
    show closeup_compass_01 at Position(xalign = 0.5, yalign = 1.0) with dissolve
    player_name "Wah!!"

    player_name "( I can't believe it! I found the treasure! )"

    player_name "( This has to be the compass {b}Captain Terry{/b} was talking about. )"

    hide closeup_compass_01 with dissolve
    call popup ('give', 'golden_compass')
    return

label beach_roxxy_spin_bottle_goldschwagger:
    scene expression game.timer.image("backgrounds/location_beach_water_day{}_blur.jpg")
    show player 13f at right with dissolve
    player_name "( Wow, this is the perfect day for the beach! )"

    player_name "( I wonder if the girls are here already? )"

    hide player
    show old_roxxy bikini 17f at right
    with dissolve
    roxxy "{b}[firstname]{/b}!!"

    player_name "!!!"
    pause
    hide old_roxxy
    show old_roxxy bikini 1f at Position (xpos=500)
    show player 14f at right
    with dissolve
    player_name "H-hey, {b}Roxxy{/b}..."

    show player 13f
    show old_roxxy bikini 2f
    roxxy "I'm glad you made it!"

    show old_becca bikini 11 at Position(xpos=315)
    show old_missy bikini 1 at left
    with dissolve
    show old_roxxy bikini 1f
    becca "Eugh, you two are hugging now?"

    show old_becca bikini 12
    show old_missy bikini 2
    missy "Hi, {b}[firstname]{/b}!!!"

    show old_missy bikini 1
    show player 14f
    player_name "Hey, {b}Missy{/b}! {b}Becca{/b}..."

    player_name "You all look beautiful in your swimsuits!"

    show player 13f
    show old_missy bikini 2b
    missy "Hehehe, I do?!"

    show old_missy bikini 1b
    becca "..."
    show old_becca bikini 11
    becca "Just try not to stare, perv."

    show old_becca bikini 12
    show old_missy bikini 2b
    missy "Does this top make my boobs look bigger?"

    show old_missy bikini 1b
    show old_becca bikini 14
    becca "Silicone is the only thing that's gonna make those tiny tits look bigger..."

    show old_becca bikini 12
    show old_missy bikini 11
    show player 5f
    player_name "..."
    show old_roxxy bikini 19 at Position (xpos=600) with dissolve
    roxxy "Are you gonna be a bitch all day, {b}Becca{/b}?"

    show old_roxxy bikini 20
    show old_becca bikini 11
    becca "... Mungkin."

    becca "Is {i}HE{/i} gonna be here all day?"

    show old_becca bikini 12
    show old_roxxy bikini 19
    roxxy "{i}*Huh*{/i}"

    show old_roxxy bikini 20
    show player 10f
    player_name "... {b}Becca{/b}, I umm..."

    show old_missy bikini 1
    show old_roxxy bikini 1f at Position (xpos=500) with dissolve
    player_name "... I brought you something!"

    show player 239_240f with dissolve
    show old_becca bikini 11
    becca "Why would I want anything from-"

    show player 654bf with dissolve
    show old_becca bikini 6
    becca "!!!"
    becca "Ya Tuhan!"

    becca "Is that {b}GoldSchwagger{/b}?!?!"

    show player 654f
    player_name "... Umm, yes?"

    show player 654bf
    show old_becca bikini 17
    becca "OhmygodohmygodOHMYGOD!!!"

    show old_becca bikini 8
    show player 13f
    with dissolve
    show old_roxxy bikini 1 at Position (xpos=600) with dissolve
    becca "This. Stuff. Is. THE BEST!"

    show old_becca bikini 7 with dissolve
    becca "Thanks for-"

    show old_becca bikini 7c
    becca "..."
    show old_becca bikini 7
    becca "Maksudku..."

    show old_becca bikini 7b
    show old_roxxy bikini 2
    roxxy "See {b}Becca{/b}."

    roxxy "{b}[firstname]{/b} is a good guy!"

    show old_roxxy bikini 1
    show old_missy bikini 2b
    missy "And cute!"

    show old_missy bikini 1b
    show old_becca bikini 7
    becca "... Yeah, well..."

    becca "I guess he's not SO bad."

    becca "For a nerd."

    show old_becca bikini 7b
    show old_missy bikini 2b
    missy "A cute nerd!"

    show old_missy bikini 1b
    show old_roxxy bikini 2
    roxxy "Okay, {b}Missy{/b}! We get it!"

    show old_roxxy bikini 2f at Position (xpos=500) with dissolve
    roxxy "C'mon, let's get this party started."

    roxxy "I've gotta get some sun!"

    hide old_roxxy
    show old_becca bikini 8
    with dissolve
    becca "I can't believe he brought me {b}GoldSchwagger{/b}!"

    hide old_becca with dissolve
    becca "{b}Dexter{/b} always forgets!"

    show player 17f
    player_name "..."
    show old_missy bikini 2b
    missy "C'mon {b}[firstname]{/b}, you can sit next to me!"

    show old_missy bikini 1b
    show player 14f
    player_name "Heh, sounds good."

    hide player
    hide old_missy
    with dissolve

    scene location_beach_cutscene02
    show text _ ("Beautiful weather. Beautiful beach. Beautiful girls...\n... What more could a guy ask for?!") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("{b}Becca{/b} and {b}Missy{/b} may not have been the greatest conversationalists in the world...\nBut they made up for those shortcomings in other ways!") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("... And {b}Roxxy{/b} turned out to be surprisingly good company!\nIt almost felt like we were close to becoming friends...") as caption with dissolve
    pause

    scene location_beach_fire_dialogue
    show old_roxxy sitting 3 zorder 1 at right
    show old_becca sitting 1 at Position (xpos=300)
    show player_sitting 3 zorder 0 at Position (xpos=650)
    show old_missy sitting 1 at left
    show xtra 47 zorder 2 at Position (xpos=400)
    with fade
    roxxy "... And then the entire pyramid collapsed!!"

    show old_roxxy sitting 2
    show old_missy sitting 5
    missy "Ha ha ha ha!"

    show old_missy sitting 2
    show player_sitting 4
    player_name "The whole thing?!"

    show player_sitting 3
    show old_becca sitting 3
    becca "Yeah... And this skinny bitch landed cunt first, right on my face!"

    show old_becca sitting 2
    show old_missy sitting 5
    missy "Aaahahahaha!"

    show player_sitting 4
    player_name "... Really?!"

    show player_sitting 3
    show old_roxxy sitting 3
    roxxy "It was pretty hilarious!"

    show old_roxxy sitting 2
    missy "{i}*Snort*{/i} Hahahaaaaah!"

    show old_becca sitting 7
    becca "... For you maybe!"

    becca "She's heavier than she looks!"

    show old_becca sitting 8
    show old_missy sitting 3
    missy "At least..."

    show old_missy sitting 5
    missy "{i}*Snort*{/i} ... At least I was wearing panties that day."

    show old_becca sitting 7
    becca "No, that little pink thong doesn't count!"

    show old_becca sitting 2
    show old_missy sitting 6
    show player_sitting 4
    player_name "You remember the color?"

    show player_sitting 3
    show old_becca sitting 3
    becca "Are you kidding? The image of that tiny pink thong coming at me, one hundred miles per hour, is like... Burned into my brain!"

    show old_becca sitting 5
    becca "It haunts my nightmares!"

    show player_sitting 5
    show old_missy sitting 5
    show old_roxxy sitting 5
    roxxy "Pfft, hahaha!"

    missy "Ha ha ha!"

    becca "Ha ha ha!"

    show old_roxxy sitting 1
    show old_becca sitting 1
    show player_sitting 3
    player_name "..."
    show player_sitting 3b
    show old_roxxy sitting 3
    roxxy "It's getting late... We should really get a fire going if we're gonna hang around."

    show old_roxxy sitting 2
    show player_sitting 3
    show old_becca sitting 3
    becca "That's a good idea-"

    becca "Whew, my head is spinning..."

    show old_becca sitting 2
    show old_missy sitting 5
    missy "Hahahaha! {i}*Snort*{/i}"

    show player_sitting 3b
    show old_roxxy sitting 3
    roxxy "Sheesh, you two really can't hold your liquor."

    show old_missy sitting 2
    show old_roxxy sitting 2
    show player_sitting 4
    player_name "aku akan melakukannya."

    player_name "You girls just chill."

    hide player_sitting with dissolve
    show old_becca sitting 3
    becca "Wow, such a gentleman..."

    show old_becca sitting 2
    roxxy "..."
    show old_roxxy sitting 3
    roxxy "... You finally warming up to him?"

    show old_roxxy sitting 2
    show old_becca sitting 3
    becca "... Mungkin."

    becca "Sedikit."

    show old_becca sitting 2
    show old_roxxy sitting 3
    roxxy "Sudah waktunya!"

    show old_roxxy sitting 2
    show old_missy sitting 3
    show old_becca sitting 8
    missy "For real."

    show old_becca sitting 1
    missy "Hai, {b}[firstname]{/b}?"

    show old_missy sitting 2
    player_name "Hmm?"

    show old_missy sitting 3
    missy "Is it true nerds have huge dicks?!"

    show old_becca sitting 8
    show old_roxxy sitting 8
    becca "!!!" with hpunch
    roxxy "!!!"
    show old_missy sitting 2
    show old_becca sitting 7b
    show old_roxxy sitting 7
    becca "Apa-apaan ini, {b}Nona{/b}?!"

    show old_becca sitting 6b
    show old_roxxy sitting 3
    roxxy "Oookay!"

    show old_becca sitting 6
    roxxy "No more beer for her..."

    show old_roxxy sitting 2
    show old_missy sitting 3
    missy "Oh c'mon, you can't tell me you guys aren't curious?!"

    show old_missy sitting 2
    show old_becca sitting 3
    becca "Hahaha, you're such a dumb slut, {b}Missy{/b}..."

    show old_becca sitting 2
    show old_roxxy sitting 5
    roxxy "Ha ha ha!"

    show old_roxxy sitting 2
    show old_missy sitting 3
    missy "... Jadi?"

    missy "I'm having fun!"

    show old_missy sitting 6
    missy "..."
    show old_missy sitting 3
    show old_becca sitting 8
    missy "Oh my gosh! I just had the best idea!"

    show old_becca sitting 2
    show old_missy sitting 2
    show old_roxxy sitting 3
    roxxy "Uh oh."

    show old_roxxy sitting 2
    show old_becca sitting 3
    becca "This should be good."

    show old_becca sitting 2
    show old_missy sitting 7
    missy "No seriously, shut up!"

    show old_missy sitting 3
    show old_becca sitting 8
    missy "We should play {b}Spin the Bottle{/b}!"

    show old_becca sitting 1
    show old_missy sitting 2
    show old_roxxy sitting 3
    roxxy "Apa?!"

    show old_roxxy sitting 2
    show old_missy sitting 3
    missy "Yeah, c'mon! It'll be so much fun!"

    show old_missy sitting 2
    show old_roxxy sitting 6
    roxxy "You just wanna kiss {b}[firstname]{/b}..."

    show old_roxxy sitting 2
    show old_missy sitting 3
    show old_becca sitting 8
    missy "Ya, ya!"

    missy "Don't you?!"

    show old_becca sitting 1
    show old_missy sitting 2
    show old_roxxy sitting 7
    roxxy "..."
    show old_roxxy sitting 6
    roxxy "Uhh, no... Not really."

    roxxy "... And I doubt {b}Becca{/b} wan-"

    show old_roxxy sitting 2
    show old_becca sitting 3
    becca "saya akan bermain!"

    show old_becca sitting 2
    show old_roxxy sitting 7
    roxxy "!!!" with hpunch
    show old_roxxy sitting 8
    roxxy "Benar-benar?!"

    show old_roxxy sitting 7
    show old_becca sitting 3
    becca "Meh, why not?"

    becca "I'm pretty wasted, so I probably won't remember anyways..."

    show old_roxxy sitting 1
    show old_becca sitting 2
    show old_missy sitting 5
    missy "Itulah semangatnya!"

    show old_missy sitting 2
    show old_roxxy sitting 2
    roxxy "..."
    show old_roxxy sitting 6
    roxxy "Well, I guess if you guys really want to... I'll play."

    show player_sitting 1 zorder 0 at Position (xpos=650) with dissolve
    show old_roxxy sitting 3
    roxxy "You okay with playing spin the bottle {b}[firstname]{/b}?"

    show old_roxxy sitting 2
    show player_sitting 4b
    player_name "Uhh... I dunno."

    player_name "Bagaimana cara kerjanya?"

    show player_sitting 3b
    show old_roxxy sitting 6
    roxxy "You seriously don't know?"

    show old_roxxy sitting 2
    show player_sitting 3
    show old_becca sitting 3
    becca "Of course he doesn't, he's a nerd..."

    becca "We'll show you."

    show old_becca sitting 2
    show old_missy sitting 3
    show old_becca sitting 8
    missy "Oh, I'm so going first!"

    show old_becca sitting 2
    show old_missy sitting 2
    show player_sitting 3b
    show old_roxxy sitting 6
    roxxy "{i}*Huh*{/i} Baik."

    show old_roxxy sitting 2
    show player_sitting 3
    show old_missy sitting 5
    missy "Hore!!"

    show old_missy sitting 3
    show old_becca sitting 8
    missy "Okay, so all you have to do is {b}spin this bottle{/b} and then {b}kiss whomever it's pointing at{/b} when it comes to a stop."

    show old_becca sitting 2
    show old_missy sitting 2
    show player_sitting 5
    player_name "!!!" with hpunch
    show player_sitting 4
    player_name "Kiss?!"

    player_name "Like on the lips?"

    show player_sitting 5
    show old_missy sitting 3
    missy "Itu benar!"

    show old_missy sitting 2
    show player_sitting 3b
    show old_roxxy sitting 6
    roxxy "We really don't have to play if you don't want to..."

    show old_roxxy sitting 2
    show player_sitting 4
    player_name "N-no! I'll play!"

    scene expression "backgrounds/location_beach_fire_dialogue.jpg"
    show old_roxxy sitting 6 zorder 1 at right
    show old_becca sitting 3 at Position (xpos=300)
    show player_sitting 3 zorder 0 at Position (xpos=650)
    show old_missy sitting 2 at left
    show xtra 47 zorder 2 at Position (xpos=400)
    with dissolve
    becca "Hehe, I bet you will..."

    show old_becca sitting 2
    roxxy "..."
    show player_sitting 3b
    show old_roxxy sitting 3
    roxxy "Baiklah."

    show old_roxxy sitting 2
    show player_sitting 3
    show old_missy sitting 4 with dissolve
    missy "Okay, so I spin first!"

    call screen spin_bottle("becca", True)
    show old_missy sitting 6
    missy "..."
    show old_missy sitting 3
    missy "... And then {b}[firstname]{/b} kisses me!"

    show old_missy sitting 2
    show player_sitting 3b
    show old_roxxy sitting 6
    roxxy "Tunggu sebentar!"

    roxxy "... It landed on {b}Becca{/b}. Not {b}[firstname]{/b}!"

    show old_roxxy sitting 2
    show player_sitting 3
    show old_missy sitting 7
    show old_becca sitting 8
    missy "Oh, did it?"

    missy "{i}*Huh*{/i} Baik."

    hide old_becca
    hide old_missy
    with dissolve
    scene expression "backgrounds/location_beach_fire_kiss.jpg" with fade
    show old_missy front sitting 1 at Position (xoffset=8)
    show old_becca front sitting 1f at Position (xoffset=-8)
    with dissolve
    pause
    show old_missy front sitting 3 at Position (xoffset=8)
    show old_becca front sitting 3f at Position (xoffset=-8)
    show old_missy_arm front sitting 1 at Position (xoffset=8)
    with dissolve
    pause
    hide old_becca
    hide old_missy
    hide old_missy_arm
    scene black
    with dissolve
    scene expression "backgrounds/location_beach_fire_dialogue.jpg" with fade
    show old_roxxy sitting 1 zorder 1 at right
    show old_becca sitting 6b at Position (xpos=300)
    show player_sitting 5 zorder 0 at Position (xpos=650)
    show old_missy sitting 8 at left
    show xtra 47 zorder 2 at Position (xpos=400)
    with dissolve
    player_name "!!!"
    show player_sitting 3
    show old_missy sitting 7
    missy "Di sana."

    show old_missy sitting 2
    show old_becca sitting 7b
    becca "What the hell was that?!"

    show old_becca sitting 6b
    show old_missy sitting 7
    missy "Hah?"

    show old_missy sitting 8
    show old_becca sitting 7b
    becca "You call that a kiss?"

    show old_becca sitting 6b
    show old_missy sitting 1
    missy "..."
    show old_roxxy sitting 2
    roxxy "..."
    show old_missy sitting 7
    missy "What, did you want me to slip you the tongue or something?!"

    show old_missy sitting 8
    show old_becca sitting 7b
    becca "Huh?! NO!"

    becca "I'm just..."

    becca "You're a pretty sucky kisser... Is all I'm saying."

    show old_becca sitting 6b
    show old_missy sitting 7
    missy "Diam!"

    missy "That's not fair, I wasn't trying!"

    missy "{b}[firstname]{/b}, I wasn't trying!"

    show old_missy sitting 8
    show old_becca sitting 1
    show player_sitting 5
    player_name "..."
    show player_sitting 4
    player_name "I'm not... I mean-"

    show player_sitting 5
    show old_missy sitting 7
    missy "Seriously, I wasn'-"

    show old_missy sitting 8
    show player_sitting 3b
    show old_roxxy sitting 6
    roxxy "MOVING ON!"

    show old_roxxy sitting 3
    show old_missy sitting 6
    roxxy "{b}[firstname]{/b}, it's your turn."

    show old_roxxy sitting 2
    show old_missy sitting 2
    show player_sitting 4b
    player_name "O-oke..."

    show player_sitting 15 with dissolve
    pause
    call screen spin_bottle("becca", True)
    show player_sitting 3
    show old_missy sitting 7
    missy "{b}Becca{/b} again!"

    missy "This is rigged!"

    show old_missy sitting 8
    hide player_sitting
    hide old_becca
    with dissolve
    scene expression "backgrounds/location_beach_fire_kiss.jpg" with fade
    show old_becca front sitting 2
    show player car 2b zorder 1
    show player_arms car 1 zorder 2
    with dissolve
    becca "It's a beer bottle... How would we rig-"

    show player front sitting 7b
    show player_arms front sitting 3
    show old_becca front sitting 3
    show player_shadow front sitting 1 zorder 0
    becca "!!!" with hpunch
    show old_becca front sitting 3b
    show player front sitting 7
    pause
    show old_becca front sitting 3
    show player front sitting 7b
    pause
    hide old_becca
    hide player_shadow
    hide player
    hide player_arms
    scene black
    with dissolve
    scene expression "backgrounds/location_beach_fire_dialogue.jpg" with fade
    show old_roxxy sitting 2 zorder 1 at right
    show old_becca sitting 2 at Position (xpos=300)
    show player_sitting 3 zorder 0 at Position (xpos=650)
    show old_missy sitting 8 at left
    show xtra 47 zorder 2 at Position (xpos=400)
    with dissolve
    becca "..."
    roxxy "..."
    show old_missy sitting 7
    missy "... How was it?!"

    show old_missy sitting 8
    show old_becca sitting 3
    becca "... Wow."

    show old_becca sitting 1
    show player_sitting 5
    show old_missy sitting 3
    missy "Was it good?!"

    show old_missy sitting 2
    show old_becca sitting 2
    becca "..."
    show player_sitting 3b
    show old_roxxy sitting 3
    roxxy "It looked pretty good!"

    show old_roxxy sitting 2
    show player_sitting 3
    show old_missy sitting 7
    missy "{b}Becca{/b}!!!"

    show old_missy sitting 8
    show old_becca sitting 6b
    becca "Hmm?"

    show old_missy sitting 7
    missy "How was it?!"

    show old_missy sitting 8
    pause
    show old_becca sitting 3
    becca "Pretty good..."

    show old_becca sitting 2
    show player_sitting 4
    player_name "Itu tadi?"

    show player_sitting 3
    show old_missy sitting 2
    show old_becca sitting 3
    becca "{i}*Ahem*{/i} I mean... Yeah, I guess."

    becca "... For a nerd. You know?"

    show old_becca sitting 2
    show player_sitting 3b
    show old_roxxy sitting 4 with dissolve
    roxxy "Alright, my turn!"

    call screen spin_bottle("missy", True)
    show player_sitting 3b
    show old_roxxy sitting 3
    roxxy "Hmm, {b}Missy{/b}..."

    show old_roxxy sitting 2
    show player_sitting 3
    show old_becca sitting 3
    becca "Be warned. She sucks."

    show old_becca sitting 2
    show old_missy sitting 7
    missy "Saya tidak!"

    missy "Watch this!"

    hide old_missy
    hide old_roxxy
    with dissolve
    scene expression "backgrounds/location_beach_fire_kiss.jpg" with fade
    show old_roxxy front sitting 1 at Position (xoffset=2)
    show old_missy front sitting 1f at Position (xoffset=-2)
    with dissolve
    pause
    show old_roxxy front sitting 3b at Position (xoffset=2)
    show old_missy front sitting 3f at Position (xoffset=-2)
    show old_missy_arm front sitting 1f at Position (xoffset=-2)
    show old_roxxy_arm front sitting 1 at Position (xoffset=2)
    with dissolve
    pause
    show old_roxxy front sitting 3 at Position (xoffset=2)
    show old_missy front sitting 3bf at Position (xoffset=-2)
    pause
    show old_roxxy front sitting 3b at Position (xoffset=2)
    show old_missy front sitting 3f at Position (xoffset=-2)
    pause
    show old_roxxy front sitting 3 at Position (xoffset=2)
    show old_missy front sitting 3bf at Position (xoffset=-2)
    pause
    hide old_missy
    hide old_missy_arm
    hide old_roxxy_arm
    hide old_roxxy
    scene black
    with dissolve
    scene expression "backgrounds/location_beach_fire_dialogue.jpg" with fade
    show old_roxxy sitting 2 zorder 1 at right
    show old_becca sitting 1 at Position (xpos=300)
    show player_sitting 5 zorder 0 at Position (xpos=650)
    show old_missy sitting 2 at left
    show xtra 47 zorder 2 at Position (xpos=400)
    with dissolve
    player_name "!!!"
    show old_roxxy sitting 6
    roxxy "... Sheesh, did you use enough tongue?!"

    show old_roxxy sitting 2
    show player_sitting 3
    show old_missy sitting 3
    missy "Wow... {b}Roxxy{/b}, you taste like cherries!"

    show old_missy sitting 2
    show old_roxxy sitting 6
    roxxy "Uhh... Right, okay."

    show old_roxxy sitting 3
    roxxy "{b}Becca{/b} it's your turn."

    show old_roxxy sitting 2
    show old_becca sitting 4 with dissolve
    call screen spin_bottle("mc", True)
    show old_becca sitting 2 with dissolve
    show old_missy sitting 7
    missy "{b}[firstname]{/b} again?!"

    missy "This is so unfair!"

    show old_missy sitting 8
    becca "..."
    roxxy "..."
    hide old_becca
    hide player_sitting
    with dissolve
    scene expression "backgrounds/location_beach_fire_kiss.jpg" with fade
    show old_becca front sitting 1
    show player car 2b zorder 1
    show player_arms car 1 zorder 2
    with dissolve
    pause
    show player front sitting 7b
    show player_shadow front sitting 1 zorder 0
    show player_arms front sitting 3
    show old_becca front sitting 3
    with dissolve
    becca "Hmm..."

    show player front sitting 7
    show old_becca front sitting 3b
    missy "Ya ampun..."

    show player front sitting 7b
    show old_becca front sitting 3
    roxxy "..."
    show player front sitting 7
    show old_becca front sitting 3b
    roxxy "... You should play with her tits a little, {b}[firstname]{/b}."

    hide player
    hide player_arms
    hide player_shadow
    hide old_becca
    scene black
    with dissolve
    scene expression "backgrounds/location_beach_fire_dialogue.jpg" with fade
    show old_roxxy sitting 2 zorder 1 at right
    show old_becca sitting 1 at Position (xpos=300)
    show player_sitting 5 zorder 0 at Position (xpos=650)
    show old_missy sitting 7 at left
    show xtra 47 zorder 2 at Position (xpos=400)
    with dissolve
    missy "Apa?!"

    missy "Tits aren't part of the game!"

    show old_missy sitting 8
    show old_roxxy sitting 6
    roxxy "Kenapa tidak?"

    show old_roxxy sitting 3
    roxxy "I'm just saying, they're right there."

    show old_roxxy sitting 2
    show old_becca sitting 3
    becca "... Okay. I lied."

    becca "He's really good at that!"

    show old_becca sitting 2
    show player_sitting 3b
    show old_roxxy sitting 3
    roxxy "Hah, now who's falling in love with him?"

    show old_roxxy sitting 2
    show player_sitting 3
    show old_becca sitting 3
    becca "Diam!"

    show old_becca sitting 2
    show old_missy sitting 4 with dissolve
    missy "Both of you shut up, it's my turn!"

    show old_missy sitting 2 with dissolve
    call screen spin_bottle("becca", True)
    show old_missy sitting 7
    missy "Oh c'mon, {b}Becca{/b} again?!"

    missy "What the hell!"

    show old_missy sitting 8
    show old_roxxy sitting 3
    roxxy "Just shut up and kiss her!"

    roxxy "Properly this time!"

    show old_roxxy sitting 2
    show old_missy sitting 7
    missy "{i}*Huh*{/i} Baik."

    hide old_missy
    hide old_becca
    with dissolve
    scene expression "backgrounds/location_beach_fire_kiss.jpg" with fade
    show old_becca front sitting 1f at Position (xoffset=-4)
    show old_missy front sitting 1 at Position (xoffset=4)
    with dissolve
    pause
    show old_becca front sitting 3bf at Position (xoffset=-4)
    show old_missy front sitting 3 at Position (xoffset=4)
    show old_missy_arm front sitting 1 at Position (xoffset=4)
    with dissolve
    pause
    show old_becca front sitting 3f at Position (xoffset=-4)
    show old_missy front sitting 3b at Position (xoffset=4)
    roxxy "Now that's much better."

    show old_becca front sitting 3bf at Position (xoffset=-4)
    show old_missy front sitting 3 at Position (xoffset=4)
    player_name "..."
    show old_becca front sitting 3f at Position (xoffset=-4)
    show old_missy front sitting 3b at Position (xoffset=4)
    roxxy "I bet you're glad you came to hang out with us tonight. Huh, {b}[firstname]{/b}?"

    show old_becca front sitting 3bf at Position (xoffset=-4)
    show old_missy front sitting 3 at Position (xoffset=4)
    player_name "... Definitely!"

    show old_becca front sitting 3f at Position (xoffset=-4)
    show old_missy front sitting 3b at Position (xoffset=4)
    roxxy "Hah!"

    hide old_missy
    hide old_becca
    hide old_missy_arm
    with dissolve
    pause
    scene expression "backgrounds/location_beach_fire_dialogue.jpg" with fade
    show old_roxxy sitting 2 zorder 1 at right
    show old_becca sitting 6b at Position (xpos=300)
    show player_sitting 5 zorder 0 at Position (xpos=650)
    show old_missy sitting 3 at left
    show xtra 47 zorder 2 at Position (xpos=400)
    with dissolve
    missy "See, I told you I'm a good kisser!"

    show old_missy sitting 2
    show old_becca sitting 7b
    becca "I dunno who told you that but they were lying!"

    becca "You're all tongue!"

    show old_missy sitting 8
    show old_becca sitting 2
    show old_roxxy sitting 5
    roxxy "Haha!"

    show old_roxxy sitting 2
    show old_missy sitting 7
    missy "Grr, screw you both!"

    show old_missy sitting 8
    show player_sitting 3b
    show old_roxxy sitting 3
    roxxy "Okay, {b}[firstname]{/b}'s turn!"

    show old_roxxy sitting 2
    show old_missy sitting 2
    show player_sitting 15 with dissolve
    pause
    call screen spin_bottle("roxxy", True)
    show player_sitting 3b
    show old_missy sitting 8
    show old_roxxy sitting 3
    roxxy "Oh, it looks like it's your lucky night."

    show old_roxxy sitting 2
    show old_missy sitting 7
    missy "This sucks..."

    show old_missy sitting 8
    hide player_sitting
    hide old_roxxy
    with dissolve
    scene expression "backgrounds/location_beach_fire_kiss.jpg" with fade
    show old_roxxy front sitting 1 at Position (xoffset=3)
    show player car 2b zorder 1 at Position (xoffset=-3)
    show player_arms car 1 zorder 2 at Position (xoffset=-3)
    with dissolve
    pause
    show player front sitting 7 at Position (xoffset=-3)
    show player_shadow front sitting 1 zorder 0
    show player_arms front sitting 3 at Position (xoffset=3-3)
    show old_roxxy front sitting 3b at Position (xoffset=3)
    show old_roxxy_arm front sitting 1 at Position (xoffset=3)
    with dissolve
    roxxy "Hmm..."

    show player front sitting 7b at Position (xoffset=-3)
    show old_roxxy front sitting 3 at Position (xoffset=3)
    becca "He's good, right!"

    show player front sitting 7 at Position (xoffset=-3)
    show old_roxxy front sitting 3b at Position (xoffset=3)
    missy "... So unfair."

    show player front sitting 7b at Position (xoffset=-3)
    show old_roxxy front sitting 3 at Position (xoffset=3)
    pause
    hide player
    hide old_roxxy
    hide old_roxxy_arm
    hide player_arms
    hide player_shadow
    scene black
    with dissolve
    scene expression "backgrounds/location_beach_fire_dialogue.jpg" with fade
    show old_roxxy sitting 8 zorder 1 at right
    show old_becca sitting 1 at Position (xpos=300)
    show player_sitting 3b zorder 0 at Position (xpos=650)
    show old_missy sitting 8 at left
    show xtra 47 zorder 2 at Position (xpos=400)
    with dissolve
    roxxy "Holy shit, {b}[firstname]{/b}..."

    show old_roxxy sitting 6
    roxxy "Why are you so good at that?!"

    show old_roxxy sitting 2
    show player_sitting 4b
    player_name "... Entahlah."

    show player_sitting 3b
    show old_roxxy sitting 3
    roxxy "Just... Wow!"

    show old_roxxy sitting 2
    show old_missy sitting 3
    show player_sitting 7
    missy "C'mon, let's keep it going!"

    show old_missy sitting 8
    roxxy "..."
    show old_missy sitting 7
    missy "{b}Roxxy{/b}!!!"

    show old_missy sitting 8
    show player_sitting 3b
    show old_roxxy sitting 3
    roxxy "Hmm?"

    show old_roxxy sitting 2
    show old_missy sitting 7
    missy "Sekarang giliranmu!"

    show old_missy sitting 8
    show old_roxxy sitting 3
    roxxy "Oh, sorry..."

    show old_roxxy sitting 4 with dissolve
    call screen spin_bottle("becca", True)
    show old_roxxy sitting 2
    show player_sitting 3
    show old_missy sitting 7
    missy "{b}Becca{/b} again."

    show old_missy sitting 8
    roxxy "..."
    show old_missy sitting 7
    missy "Why is it always {b}Becca{/b}?!"

    show old_missy sitting 8
    hide old_roxxy
    hide old_becca
    with dissolve
    scene expression "backgrounds/location_beach_fire_kiss.jpg" with fade
    show old_roxxy front sitting 1 at Position (xoffset=5)
    show old_becca front sitting 1f
    with dissolve
    pause
    show old_roxxy front sitting 3 at Position (xoffset=5)
    show old_roxxy_arm front sitting 2d
    show old_becca front sitting 3bf
    becca "!!!" with hpunch
    show old_roxxy front sitting 3b at Position (xoffset=5)
    show old_roxxy_arm front sitting 2c
    show old_becca front sitting 3f
    missy "Wah!"

    show old_roxxy front sitting 3 at Position (xoffset=5)
    show old_roxxy_arm front sitting 2d
    show old_becca front sitting 3bf
    missy "She actually went for her tits!"

    show old_roxxy front sitting 3b at Position (xoffset=5)
    show old_roxxy_arm front sitting 2c
    show old_becca front sitting 3f
    player_name "..."
    hide old_roxxy
    hide old_roxxy_arm
    hide old_becca
    scene black
    with dissolve
    scene expression "backgrounds/location_beach_fire_dialogue.jpg" with fade
    show old_roxxy sitting 2 zorder 1 at right
    show old_becca sitting 7 at Position (xpos=300)
    show player_sitting 5 zorder 0 at Position (xpos=650)
    show old_missy sitting 2 at left
    show xtra 47 zorder 2 at Position (xpos=400)
    with dissolve
    becca "What the hell, {b}Roxxy{/b}?!"

    show old_becca sitting 6
    show old_roxxy sitting 6
    roxxy "Oh, don't pretend like you didn't like it."

    show old_roxxy sitting 3
    roxxy "Your nipples are as hard as a rock."

    show old_roxxy sitting 2
    show old_becca 8b
    becca "!!!"
    show player_sitting 3b
    show old_roxxy sitting 6
    roxxy "Besides, this is boring if it's just kissing."

    show old_roxxy sitting 2
    show player_sitting 3
    show old_becca sitting 1
    becca "..."
    show old_missy sitting 3
    missy "Saya setuju!"

    show old_missy sitting 2
    show player_sitting 3b
    show old_roxxy sitting 3
    roxxy "I bet {b}[firstname]{/b} liked it!"

    show old_roxxy sitting 2
    show player_sitting 4
    player_name "Y-ya!"

    player_name "Itu luar biasa!"

    show player_sitting 3
    show old_roxxy sitting 5
    show old_missy sitting 5
    show old_becca sitting 5
    roxxy "Ha ha ha!"

    missy "Ha ha ha!"

    becca "Ha ha ha!"

    show old_roxxy sitting 3
    show old_missy sitting 2
    show old_becca sitting 2
    show player_sitting 3b
    roxxy "See {b}Becca{/b}, I know what I'm doing."

    roxxy "Spin it, bitch!"

    show old_roxxy sitting 2
    show player_sitting 3
    becca "..."
    show old_becca sitting 4 with dissolve
    call screen spin_bottle("mc", True)
    show old_becca sitting 2 with dissolve
    show old_roxxy sitting 3
    roxxy "{b}[firstname]{/b}."

    show old_roxxy sitting 2
    show old_missy sitting 6
    missy "!!!"
    show old_missy sitting 7
    missy "This is such bullshit!"

    show old_missy sitting 8
    show player_sitting 3b
    show old_roxxy sitting 6
    roxxy "Diam, {b}Nona{/b}!"

    show old_roxxy sitting 3
    roxxy "Some of us are trying to enjoy the show!"

    roxxy "Get in there {b}[firstname]{/b} and play with her tits this time!"

    show old_roxxy sitting 2
    show player_sitting 4b
    player_name "... Really?"

    show player_sitting 3b
    show old_roxxy sitting 3
    roxxy "Ya, ya!"

    roxxy "{b}Becca{/b}'s got a nice rack."

    show old_roxxy sitting 6
    roxxy "... Not as nice as mine but..."

    show old_roxxy sitting 2
    show old_becca sitting 7
    becca "Screw you, {b}Roxxy{/b}."

    show old_becca sitting 6
    show old_roxxy sitting 3
    roxxy "You know you want it, bitch..."

    show old_roxxy sitting 2
    show old_missy sitting 3
    missy "I want it!"

    show old_missy sitting 5
    missy "Ahahaah!"

    show old_becca sitting 6b
    becca "..."
    show old_roxxy sitting 3
    roxxy "See, she's totally turned on!"

    show old_becca sitting 9
    roxxy "Do it, {b}[firstname]{/b}!"

    show old_roxxy sitting 2
    hide old_becca
    hide player_sitting
    with dissolve
    scene expression "backgrounds/location_beach_fire_kiss.jpg" with fade
    show old_becca front sitting 1
    show player car 2b zorder 1
    show player_arms car 1 zorder 2
    with dissolve
    pause
    show player_shadow front sitting 1 zorder 0
    show player front sitting 7
    show player_arms front sitting 4
    show old_becca front sitting 3b
    with dissolve
    becca "Mmmm..."

    show player front sitting 7b
    show player_arms front sitting 4d
    show old_becca front sitting 3
    missy "I'm so jelly right now..."

    show player front sitting 7
    show player_arms front sitting 4
    show old_becca front sitting 3b
    roxxy "..."
    show player front sitting 7b
    show player_arms front sitting 4d
    show old_becca front sitting 3
    becca "Nnngh!"

    show player front sitting 7
    show player_arms front sitting 4
    show old_becca front sitting 3b
    missy "Damn!"

    hide player
    hide player_shadow
    hide player_arms
    hide old_becca
    scene black
    with dissolve
    scene expression "backgrounds/location_beach_fire_dialogue.jpg" with fade
    show old_roxxy sitting 2 zorder 1 at right
    show old_becca sitting 3 at Position (xpos=300)
    show player_sitting 3 zorder 0 at Position (xpos=650)
    show old_missy sitting 6 at left
    show xtra 47 zorder 2 at Position (xpos=400)
    with dissolve
    becca "ah..."

    show old_becca sitting 2
    show player_sitting 3b
    show old_roxxy sitting 3
    roxxy "You should have kept going!"

    show old_roxxy sitting 2
    show player_sitting 3
    show old_missy sitting 7
    missy "What?! No way, it's my turn!"

    show old_missy sitting 8
    show player_sitting 3b
    show old_roxxy sitting 3
    roxxy "... Oh, shut up, {b}Missy{/b}."

    show old_roxxy sitting 6
    roxxy "Look at her."

    roxxy "A couple of hours ago she didn't want anything to do with him."

    show old_roxxy sitting 3
    roxxy "Now she's totally ready to jump his bone."

    show old_roxxy sitting 2
    show player_sitting 5
    show old_becca sitting 7
    becca "Saya tidak!"

    show old_becca sitting 6
    show player_sitting 3b
    show old_roxxy sitting 5
    roxxy "Hah. Yeah right!"

    show old_roxxy sitting 2
    show player_sitting 3
    show old_missy sitting 7
    missy "Can I spin now, please?"

    show old_missy sitting 8
    show old_roxxy sitting 6
    roxxy "I bet your pussy is sopping wet right now!"

    show old_roxxy sitting 2
    show old_becca sitting 8b
    show player_sitting 5
    becca "..."
    show old_missy sitting 7
    missy "Screw it, I'm spinning!"

    show player_sitting 3
    show old_missy sitting 8
    show old_roxxy sitting 3
    roxxy "Admit it!"

    show old_roxxy sitting 2
    show old_becca sitting 10b
    becca "... Shut up!"

    show old_roxxy sitting 5
    show old_becca sitting 10
    roxxy "Ahaha, I knew it!"

    show old_missy sitting 4 with dissolve
    player_name "..."
    call screen spin_bottle("mc", True)
    show old_missy sitting 5
    show old_becca sitting 9
    missy "YA!"

    missy "Akhirnya!"

    show old_missy sitting 2
    becca "..."
    show old_missy sitting 3
    missy "Okay, feel free to grope whatever you want, {b}[firstname]{/b}!"

    show old_missy sitting 2
    show old_roxxy sitting 5
    roxxy "Hahahaah!"

    show old_roxxy sitting 3
    roxxy "You are such a dirty slut, {b}Missy{/b}!"

    show old_roxxy sitting 2
    show old_becca sitting 2
    show old_missy sitting 7
    missy "Shhh, don't ruin this for me!"

    show old_missy sitting 9
    show player_sitting 3b
    show old_roxxy sitting 3
    roxxy "Go ahead, {b}[firstname]{/b}."

    roxxy "Give it to her."

    show old_roxxy sitting 2
    hide old_becca
    hide player_sitting
    with dissolve
    scene expression "backgrounds/location_beach_fire_kiss.jpg" with fade
    show old_missy front sitting 1
    show player car 2b zorder 1 at Position (xoffset=-7)
    show player_arms car 1 zorder 2 at Position (xoffset=-7)
    pause
    show player_shadow front sitting 1 zorder 0
    show player front sitting 7 at Position (xoffset=-7)
    show player_arms front sitting 4 at Position (xoffset=-7)
    show old_missy front sitting 3b
    show old_missy_arm front sitting 1 zorder 3
    pause
    show player front sitting 7b at Position (xoffset=-7)
    show player_arms front sitting 4c
    show old_missy front sitting 3
    pause
    show player front sitting 7 at Position (xoffset=-7)
    show player_arms front sitting 4 at Position (xoffset=-7)
    show old_missy front sitting 3b
    pause
    show player front sitting 7b at Position (xoffset=-7)
    show player_arms front sitting 4c
    show old_missy front sitting 3
    pause
    hide old_missy
    hide old_missy_arm
    hide player
    hide player_arms
    scene black
    with dissolve

    scene location_beach_cutscene03
    show text _ ("This turned out to be a wonderful night!") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("I can't believe I'm actually making out with {b}Roxxy{/b} and {b}her friends{/b}!\nNobody is going to believe me!\n... And {b}Roxxy{/b} is even pushing her friends to take things further!") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("Why would she do that, I wonder?") as caption with dissolve
    pause

    scene location_beach_water_evening_blur
    show old_roxxy bikini 1f at Position (xpos=500)
    show old_becca bikini 9 at Position(xpos=315)
    show old_missy bikini 1b at left
    show player 14f at right
    with fade
    player_name "I should... Really get home."

    player_name "It's getting super late."

    show player 13f
    show old_missy bikini 2
    missy "Aww, but..."

    show old_missy bikini 1
    show old_roxxy bikini 2 at Position (xpos=600) with dissolve
    roxxy "{b}[firstname]{/b}'s right."

    roxxy "We gotta get the lush over here home before she passes out."

    show old_roxxy bikini 1
    show old_becca bikini 10
    becca "Hmm?"

    becca "No, I'm... {i}*Yawn*{/i}"

    becca "... I'm fine!"

    show old_becca bikini 9
    show old_roxxy bikini 2
    roxxy "Ya benar."

    roxxy "I'm not carrying her this time!"

    show old_roxxy bikini 1
    show old_missy bikini 8
    missy "Hey, I had to carry her last time!"

    show old_missy bikini 1
    show old_roxxy bikini 2
    roxxy "Well, you'd better hope she makes it home then."

    roxxy "'Cause I'm not doing it!"

    show old_roxxy bikini 1
    show old_missy bikini 8
    missy "Ahh, kawan..."

    show old_missy bikini 1
    show old_roxxy bikini 1f at Position (xpos=500) with dissolve
    show player 14f
    player_name "Thanks for the great night, ladies!"

    show player 13f
    show old_becca bikini 10
    becca "Thank you for the {b}GoldSchwagger{/b}, {b}[firstname]{/b}!"

    show old_becca bikini 9
    show player 14f
    player_name "Heh, my pleasure!"

    hide old_becca with dissolve
    pause
    hide player
    show old_roxxy bikini 17f at right
    with dissolve
    roxxy "I'll see you at school, {b}[firstname]{/b}."

    show old_roxxy bikini 18f
    player_name "Thanks for inviting me, {b}Roxxy{/b}!"

    hide old_roxxy
    show old_roxxy bikini 2f at Position (xpos=500)
    show player 13f at right
    with dissolve
    roxxy "Yeah, it was fun!"

    roxxy "... Maybe we'll do it again {b}next weekend{/b}!"

    hide old_roxxy with dissolve
    show old_missy bikini 1b
    missy "..."
    player_name "..."
    show old_missy bikini 2b
    missy "So... Uhh..."

    missy "Call me... Sometime?"

    show player 11f
    missy "K, bye!"

    hide old_missy with dissolve
    show player 10f
    player_name "Tunggu!"

    show player 5f
    player_name "..."
    show player 12f
    player_name "You never gave me your number..."

    show player 5f
    player_name "..."
    show player 10f
    player_name "Oh, well."

    show player 17f
    player_name "( Man, what a night! )"

    player_name "( I'd better get home before {b}[deb_name]{/b} starts worrying. )"

    hide player with dissolve
    return

label beach_roxxy_spin_bottle_no_goldschwagger:
    scene expression game.timer.image("backgrounds/location_beach_water_day{}_blur.jpg")
    show player 5 with dissolve
    player_name "( {b}Roxxy{/b} and her friends are over there but I can't go in empty-handed! )"

    player_name "( I should {b}speak with Captain Terry about getting a bottle of GoldSchwagger for Becca{/b} first... )"

    hide player with dissolve
    return

label beach_roxxy_spin_bottle_wrong_time:
    scene expression "backgrounds/location_beach_water_night_blur.jpg"
    show old_roxxy bikini 19f at Position (xpos=500)
    show old_becca bikini 1b at Position(xpos=315)
    show old_missy bikini 12 at left
    show player 13f at right
    with dissolve
    roxxy "Psh, well look who finally decided to showed up!"

    show old_roxxy bikini 20f
    show player 5f
    show old_becca bikini 17
    becca "Nerd!"

    show old_missy bikini 8
    missy "You missed the entire party, {b}[firstname]{/b}!"

    show old_missy bikini 12
    becca "Hahaha, nerdy neeeeerd!"

    show old_becca bikini 1b
    show player 12f
    player_name "Is {b}Becca{/b} hammered?"

    show old_becca bikini 17
    show old_missy bikini 1
    show player 5f
    show old_roxxy bikini 19bf
    roxxy "Yeah, we were just about to take her home..."

    show old_roxxy bikini 20f
    show player 10f
    player_name "Oh baiklah."

    show old_becca bikini 1b
    player_name "Do you need help or something?"

    show player 5f
    show old_roxxy bikini 19f
    roxxy "No, we've got it."

    roxxy "I'd think that when the most popular girl in school invites you to a party, you'd show up for it on time..."

    show old_roxxy bikini 20f
    show player 10f
    player_name "I'm sorry, {b}Roxxy{/b}. I must have gotten confused..."

    show player 5f
    show old_roxxy bikini 19f
    roxxy "Yeah, or you weren't listening!"

    roxxy "Whatever, I've gotta tend to {b}Becca{/b}'s drunk ass..."

    hide old_roxxy
    hide old_becca
    with dissolve
    becca "NEEEEEEERD!!!"

    becca "Ha ha ha!"

    show player 37f with dissolve
    player_name "I really screwed up..."

    show player 5f with dissolve
    show old_missy bikini 2
    missy "It's okay, {b}[firstname]{/b}."

    missy "{b}Just show up in the afternoon next weekend{/b}."

    missy "{b}Roxxy{/b} will be over it by then."

    show old_missy bikini 1
    show player 10f
    player_name "Ya baiklah."

    player_name "Thanks, {b}Missy{/b}."

    show player 5f
    show old_missy bikini 2b
    missy "Sampai jumpa!"

    hide player
    hide old_missy
    with dissolve
    return

label beach_roxxy_invite_to_bikini_contest:
    scene expression "backgrounds/location_beach_water_contest_day_blur02.jpg"
    show player 14f at right with dissolve
    player_name "Whoa, look at this place!"

    player_name "There are so many bikinis!"

    show player 31f with dissolve
    player_name "..."
    show player 32f
    player_name "Hey, is that {b}Captain Terry{/b} up there?!"

    player_name "I should go and see what he's doing here."

    hide player with dissolve
    return

label beach_cabin_roxxy_in_cabin:
    scene expression "backgrounds/location_beach_cabin_closeup.jpg"
    show old_roxxy bikini 13f at right
    show player 10 at left
    with dissolve
    player_name "... {b}Roxxy{/b}?"

    player_name "Kamu baik-baik saja?"

    show player 5
    show old_roxxy bikini 15f
    roxxy "... Tidak."

    roxxy "Ugh, that was so embarrassing!"

    show old_roxxy bikini 14f
    show player 10
    player_name "It's not so bad."

    player_name "I don't think anybody saw but {b}Becca{/b} and I..."

    show player 5
    show old_roxxy bikini 15f
    roxxy "... Really?"

    show old_roxxy bikini 14f
    show player 14
    player_name "Ya."

    player_name "Besides, even if somebody did... Who cares?"

    show player 18
    player_name "You have amazing breasts!"

    player_name "Definitely nothing to be ashamed of..."

    show player 13
    roxxy "..."
    show old_roxxy bikini 15 with dissolve
    roxxy "Yeah, I guess you're right about that."

    show old_roxxy bikini 14
    roxxy "..."
    show old_roxxy bikini 13
    roxxy "... But what am I going to do?!"

    roxxy "I can't compete in the contest with a broken bikini top!"

    show old_roxxy bikini 14
    show player 10
    player_name "You don't have a back up?"

    show player 5
    show old_roxxy bikini 13
    roxxy "... Tidak."

    show old_roxxy bikini 14
    show player 34
    player_name "..."
    show player 14
    player_name "Don't worry, {b}Roxxy{/b}."

    player_name "I'll just go and buy you a new one!"

    show player 13
    show old_roxxy bikini 15
    roxxy "We don't have time for that!"

    show player 5
    roxxy "The competition is starting soon, {b}[firstname]{/b}!"

    show old_roxxy bikini 13
    roxxy "... I'm completely screwed."

    show old_roxxy bikini 14
    show player 10
    player_name "Calm down."

    player_name "I'll find you something!"

    show player 5
    show old_roxxy bikini 15
    roxxy "Ya benar!"

    roxxy "Where are you going to find one?"

    show old_roxxy bikini 14
    show player 10
    player_name "Well, this is a beach..."

    show player 14
    player_name "There's gotta be {b}an extra bathing suit here somewhere{/b}."

    show player 13
    show old_roxxy bikini 15b
    roxxy "Go and tell {b}Becca{/b} to bring me hers!"

    show old_roxxy bikini 15c
    show player 12
    player_name "Hah?"

    player_name "You want to take {b}Becca{/b}'s swimsuit?"

    show player 5
    show old_roxxy bikini 15b
    roxxy "Yeah, that bitch will give it to me if I tell her to."

    show old_roxxy bikini 15c
    show player 12
    player_name "... But then, what is she going to wear?"

    show player 5
    show old_roxxy bikini 15b
    roxxy "Umm, who cares?"

    roxxy "It's not like she's gonna win anyways!"

    show old_roxxy bikini 15c
    show player 10
    player_name "Don't do that, I'll {b}find you one{/b}!"

    show player 5
    show old_roxxy bikini 15b
    roxxy "Hmm, fine!"

    roxxy "I'll give you ten minutes but after that, I'm taking {b}Becca{/b}'s..."

    show old_roxxy bikini 15c
    show player 10
    player_name "Saya akan kembali."

    hide player with dissolve
    show old_roxxy bikini 15b
    roxxy "... Don't get me an ugly one either!"

    hide old_roxxy with dissolve
    return

label beach_cabin_roxxy_get_new_bikini:
    scene expression "backgrounds/location_beach_cabin_closeup.jpg"
    show player 5 at left
    show old_roxxy bikini 15 at right
    with dissolve
    roxxy "Did you find one?!"

    show old_roxxy bikini 14
    show player 10
    player_name "Stop worrying, I'll {b}find you a swimsuit{/b}!"

    show player 5
    show old_roxxy bikini 15b
    roxxy "Hmph!"

    roxxy "Well, it had better be a good one, otherwise, I'm taking {b}Becca{/b}'s..."

    hide old_roxxy with dissolve
    show player 10
    player_name "Hmm, {b}I should look around here for a bikini that nobody's using{/b}."

    hide player with dissolve
    return

label beach_cabin_roxxy_has_bikini:
    scene expression "backgrounds/location_beach_cabin_closeup.jpg"
    show old_roxxy bikini 14 at right
    show player 14 at left
    with dissolve
    player_name "{b}Roxxy{/b}, I think I've found one!"

    show old_roxxy bikini 15
    roxxy "Benar-benar?!"

    roxxy "Lemme see, lemme see!"

    show old_roxxy bikini 14
    show player 239_240 with dissolve
    pause
    show player 656b with dissolve
    show old_roxxy bikini 15
    roxxy "{i}*Terkesiap*{/i}"

    show old_roxxy bikini 15d
    show player 13
    with dissolve
    roxxy "It's pretty!"

    show old_roxxy bikini 15e
    show player 14
    player_name "Yeah, it's umm... Patriotic."

    show player 13
    show old_roxxy bikini 15d
    roxxy "Hehehe!"

    show old_roxxy bikini 9 with dissolve
    show player 433
    pause
    show old_roxxy bikini usa 5
    show player 296
    with dissolve
    pause
    show old_roxxy 22 with dissolve
    pause
    show old_roxxy 23b with dissolve
    roxxy "Apa yang sedang kamu lakukan?"

    show old_roxxy 23
    pause
    player_name "Hmm?"

    show old_roxxy 24
    roxxy "You've already seen me naked, remember?"

    show old_roxxy 23
    player_name "Yeah, I know... I'm just..."

    show old_roxxy 23b
    roxxy "Psh, stop acting so nerdy!"

    show player 433 with dissolve
    show old_roxxy 22 with dissolve
    pause
    show player 434
    show old_roxxy bikini usa 6 with dissolve
    pause
    show old_roxxy bikini usa 14 with dissolve
    show player 435
    player_name "... Wah!"

    show old_roxxy bikini usa 11 with dissolve
    show player 434
    roxxy "Saya tahu, benar!"

    show old_roxxy bikini usa 6b with dissolve
    roxxy "Hmm, it's a bit tight..."

    show old_roxxy bikini usa 6c with dissolve
    pause
    show old_roxxy bikini usa 6b with dissolve
    roxxy "It's not too small, is it?"

    pause
    show old_roxxy bikini usa 6c with dissolve
    player_name "..."
    show old_roxxy bikini usa 6b
    roxxy "... What do you think?"

    show old_roxxy bikini usa 9 with dissolve
    player_name "..."
    show old_roxxy bikini usa 12 with dissolve
    roxxy "{b}[firstname]{/b}!!!"

    show old_roxxy bikini usa 13
    show player 435
    player_name "Hmm?"

    show player 434
    show old_roxxy bikini usa 8 with dissolve
    roxxy "Bagaimana tampilannya?"

    show player 435
    player_name "... Really, REALLY good!"

    player_name "... That's like, my favorite bikini ever!"

    show player 434
    show old_roxxy bikini usa 10 with dissolve
    roxxy "Hehehe!"

    roxxy "You still think I'll win?"

    show old_roxxy bikini usa 9
    show player 17
    player_name "Without a doubt!"

    show player 13
    show old_roxxy bikini usa 10
    roxxy "Bagus!"

    roxxy "Now, I just need you to oil me up and it's a sure thing!"

    show old_roxxy bikini usa 9
    show player 22
    player_name "!!!" with hpunch
    show player 23
    player_name "Did you say, you want {i}me{/i} to..."

    show player 22
    player_name "{i}*Meneguk*{/i}"

    show old_roxxy bikini usa 12 with dissolve
    roxxy "Hah, you getting shy on me, {b}[firstname]{/b}?"

    roxxy "I can have {b}Becca{/b} do it if you don't want to..."

    roxxy "I just thought, since you found me the replacement bikini and all..."

    show old_roxxy bikini usa 13
    show player 36 with dissolve
    player_name "N-no! I'll do it!"

    show player 14 with dissolve
    player_name "I'll definitely do it!"

    show player 13
    show old_roxxy bikini usa 12
    roxxy "Haha, I thought so!"

    roxxy "They usually keep some {b}in the life guard's tower{/b}."

    roxxy "Why don't you go grab the bottle and I'll wait for you here."

    show old_roxxy bikini usa 13
    show player 14
    player_name "Totally! I'll be right back!"

    show player 12
    player_name "Don't move!"

    hide player with fastdissolve
    pause
    show old_roxxy bikini usa 6b with dissolve
    roxxy "Haha, hurry back, {b}[firstname]{/b}!"

    hide old_roxxy with dissolve
    return

label beach_tower_roxxy_get_oil:

    scene location_beach_cutscene01
    show text _ ("I practically flew up the ladder to the life guard's tower!") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("{b}Roxxy{/b} was actually going to let me oil her body up for the competition...") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("... What good fortune that {b}Miss Sara{/b} had left her bikini behind for me to find!") as caption with dissolve
    pause

    scene location_beach_tower_cutscene01
    show text _ ("And as I crested the top of the ladder I found my mind wondering what might have become of her and the captain...") as caption
    with fade
    pause
    hide caption with dissolve
    scene location_beach_tower_cutscene02
    show text _ ("... But I didn't need to wonder very long.") as caption
    with dissolve
    pause

    call scene_sara_terry
    $ unlock_scene('sara', '01_unlocked')

    call wait

    scene expression background(672, 456, 8.5, l=L_beach_water) as stage
    show anon a_backpack2 f_shy_high
    with fade
    anon @ -m_talk "( Wow. )"

    pause
    show anon a_backpack1 f_shy_down
    with {'master': dissolve}
    anon @ -m_talk "( Welp, that's the lotion sorted. )"

    show anon a_sides f_grin
    with {'master': dissolve}
    anon @ -m_talk "( {b}I'd best get this back to Roxxy{/b} ASAP. )"

    hide anon with dissolve
    return

label beach_tower_roxxy_get_oil.repeat:
    scene expression background(672, 456, 8.5, l=L_beach_water) as stage
    show anon f_shy_high with dissolve
    anon @ -m_talk "( I can't peep all day, {b}Roxxy is waiting on me{/b}! )"

    hide anon with dissolve
    return

label beach_cabin_roxxy_get_oil:
    scene location_beach_water_contest_day_blur
    show player 29 with fastdissolve
    player_name "Holy crap! What am I doing?!"

    show player 29f with fastdissolve
    player_name "I've gotta {b}get that bottle of oil{/b} from the {b}life guard's tower{/b} before {b}Roxxy{/b} changes her mind!"

    hide player with fastdissolve
    return

label beach_cabin_roxxy_has_oil:
    scene expression "backgrounds/location_beach_cabin_closeup.jpg"
    show old_roxxy bikini usa 9 at right with None
    show player 184b at left
    with fastdissolve
    player_name "{i}*Huff*{/i} I made..."

    player_name "I made it..."

    player_name "{i}*Puff*{/i}"

    show player 658 with dissolve
    player_name "Phew! Here's your oil..."

    show old_roxxy bikini usa 10
    roxxy "Sheesh, did you run the entire way or something?!"

    show old_roxxy bikini usa 9
    show player 184b with dissolve
    player_name "..."
    show old_roxxy bikini usa 10
    roxxy "Hahahahaah!"

    show old_roxxy bikini usa 10
    roxxy "Well, thanks, I guess..."

    show old_roxxy bikini usa 9
    player_name "..."
    show old_roxxy bikini usa 10
    roxxy "Okay, well..."

    roxxy "Let's start oiling then, shall we?!"

    show old_roxxy bikini usa 9
    show player 658 with dissolve
    player_name "Y-yeah, okay!"

    scene expression "backgrounds/location_beach_cabin_closeup_massage.jpg"
    show old_roxxy massage 2 with dissolve
    roxxy "Just make sure you get everything, okay!"

    show old_roxxy massage 3 with dissolve
    roxxy "Start with my shoulders..."

    show old_roxxy massage 1 with dissolve
    player_name "Baiklah!"

    show old_roxxy massage 4_5 with dissolve
    roxxy "Hmm..."

    player_name "..."
    pause
    show old_roxxy massage 1 with dissolve
    player_name "Am I doing it right?"

    show old_roxxy massage 2
    roxxy "... What, have you never rubbed a girl's shoulders before?"

    show old_roxxy massage 1
    player_name "A- Tidak!"

    player_name "I mean... Of course, I've rubbed plenty of girl's shoulders!"

    show old_roxxy massage 2
    roxxy "Eh ya..."

    roxxy "Well, don't ask stupid questions then!"

    show old_roxxy massage 1
    player_name "..."
    pause
    label roxxy_massage_45:
        show old_roxxy massage 4_5 with dissolve
        pause
        pause
    call screen roxxy_massage("roxxy_massage_45")
    show old_roxxy massage 3 with dissolve
    pause
    show old_roxxy massage 8_9 with dissolve
    roxxy "Mmm... That's good."

    roxxy "Make sure you don't miss any spots!"

    player_name "Ya, saya tahu."

    player_name "I'll make sure to coat everything!"

    pause
    roxxy "Ooh, that's really good."

    player_name "..."
    label roxxy_massage_89:
        show old_roxxy massage 8_9 with dissolve
        pause
        pause
    call screen roxxy_massage("roxxy_massage_89")
    show old_roxxy massage 3 with dissolve
    pause
    show old_roxxy massage 5 with dissolve
    pause
    show old_roxxy massage 6_7 with dissolve
    roxxy "Ahhh... That feels REALLY good, {b}[firstname]{/b}..."

    player_name "... Y-yeah?"

    roxxy "Mmmhmm, don't stop..."

    player_name "O-oke."

    pause
    label roxxy_massage_67:
        show old_roxxy massage 6_7 with dissolve
        pause
        pause
    call screen roxxy_massage("roxxy_massage_67")
    show old_roxxy massage 3 with dissolve
    pause
    show old_roxxy massage 8 with dissolve
    pause
    show old_roxxy massage 9_10 with dissolve
    roxxy "Ngghh!!"

    roxxy "..."
    roxxy "Wah!"

    player_name "..."
    roxxy "Rasanya luar biasa!"

    pause
    show old_roxxy massage 3 with dissolve
    roxxy "Ahh, keep going!"

    show old_roxxy massage 9_10 with dissolve
    roxxy "Jangan berhenti!"

    roxxy "Jangan-"

    becca "{b}Roxxy{/b}, it's time to start heading-"


    scene location_beach_cutscene04
    show text _ ("Just my luck...\n{b}Missy{/b} and {b}Becca{/b} were at the entrance of the tent...") as caption
    with fade
    pause

    scene location_beach_cabin_closeup
    show old_roxxy bikini usa 1 at right
    roxxy "!!!" with hpunch
    show old_becca bikini 18 at Position(xpos=315)
    show old_missy bikini 12 at left
    with dissolve
    becca "... Holy shit!"

    show old_becca bikini 1b
    hide old_roxxy
    show old_roxxy bikini usa 15 zorder 1 at Position (xpos=650)
    show player 81f zorder 0 at right
    with dissolve
    show old_missy bikini 14
    pause
    show old_missy bikini 15 with dissolve
    missy "I fucking knew it!"

    missy "See, {b}Becca{/b}?"

    missy "I told you nerds have huge dicks!"

    show old_becca bikini 15
    show old_missy bikini 14
    becca "..."
    show player 78f
    show old_becca bikini 18
    becca "Sorry, we didn't realize-"

    show old_becca bikini 15
    becca "..."
    show old_becca bikini 18
    becca "Seriously though... Holy shit {b}[firstname]{/b}!"

    show old_becca bikini 15
    show player 82f
    show old_roxxy bikini usa 18 with dissolve
    roxxy "We weren't doing anything..."

    show old_becca bikini 1b
    roxxy "He was just putting oil on me for the competition!!!"

    show old_roxxy bikini usa 17
    becca "..."
    show old_becca bikini 2b
    becca "Well, it certainly didn't look like nothing {b}Roxxy{/b}..."

    show old_becca bikini 1b
    show old_missy bikini 13
    missy "Sungguh!"

    missy "Can I go next?"

    show old_missy bikini 14
    show old_becca bikini 14
    becca "Diam, {b}Nona{/b}!"

    show old_becca bikini 16
    show old_missy bikini 2
    missy "... What?!"

    show old_missy bikini 13
    missy "I want some oil too!"

    missy "You'll rub oil on me, won't you {b}[firstname]{/b}?"

    show old_becca bikini 1b
    show old_missy bikini 14
    show player 83f
    player_name "... I uhh."

    show player 82f
    show old_roxxy bikini usa 18
    roxxy "You guys, seriously!"

    roxxy "You can't tell anybody about this!"

    show old_roxxy bikini usa 17
    show old_becca bikini 2b
    becca "Yeah, {b}Dexter{/b} would kill you both if he heard about this."

    show old_becca bikini 1b
    player_name "..."
    roxxy "..."
    show old_becca bikini 2
    becca "We won't tell anybody."

    show old_becca bikini 14
    becca "Right, {b}Missy{/b}?!"

    show old_becca bikini 16
    show old_missy bikini 2b
    missy "Hmm?!"

    missy "Tell anybody what?"

    show old_missy bikini 14
    show old_becca bikini 14
    becca "... Tepat."

    show old_becca bikini 2
    becca "C'mon, they are calling everyone to the stage."

    show old_becca bikini 16
    missy "..."
    show old_becca bikini 14
    becca "Quit staring at his dick and let's go!"

    show old_becca bikini 16
    show old_missy bikini 13
    missy "... Aww."

    hide old_missy with dissolve
    show old_becca bikini 15
    pause
    show old_becca bikini 18
    becca "... Holy shit."

    hide old_becca with dissolve
    pause
    show old_roxxy bikini usa 19
    roxxy "..."
    show player 83f
    player_name "... You okay?"

    show player 82f
    show old_roxxy bikini usa 18f at Position (xpos=550) with dissolve
    roxxy "Y-ya."

    roxxy "Just nervous about the competition is all."

    show old_roxxy bikini usa 17f
    show player 83f
    player_name "Benar."

    player_name "Don't worry, you're gonna do great!"

    show player 82f
    roxxy "..."
    show player 83f
    player_name "C'mon, we better hurry!"

    hide player with dissolve
    roxxy "..."
    show old_roxxy bikini usa 13f
    pause
    hide old_roxxy with dissolve
    scene expression "backgrounds/location_beach_water_contest_closeup.jpg"
    show tstand 19b zorder 0 at Position (xpos=729)
    terry "Oh ho ho! You're gonna be the death of me one day, love..."

    show tstand 20b
    sara "Hehe, well, at least you'll die happy!"

    show tstand 19b
    terry "Amin untuk itu!"

    show player 11 zorder 2 at left with dissolve
    show tstand 19
    terry "Well then, if it isn't the Skipper, once more."

    terry "How's it going, lad?"

    show tstand 19d
    show player 14
    player_name "It's going awesome, {b}Captain{/b}!"

    player_name "I was just escorting my friend here to the stage."

    show player 13
    show old_roxxy bikini usa 9f zorder 1 at Position (xpos=400) with dissolve
    pause
    show tstand 19
    terry "Phew, what a beauty!"

    show tstand 19d
    show old_roxxy bikini usa 10f
    roxxy "... T-thanks!"

    show old_roxxy bikini usa 9f
    show tstand 20c with dissolve
    sara "{i}*Terkesiap*{/i}"

    sara "Is that my bikini?"

    show tstand 19d
    show old_roxxy bikini usa 16f
    with dissolve
    roxxy "!!!"
    show player 21
    player_name "Y-ya."

    show old_roxxy bikini usa 17f
    player_name "{b}Roxxy{/b}'s top broke at the last second and it was the only replacement I could find."

    player_name "I hope that's okay, {b}Miss Sara{/b}?"

    player_name "... I would have asked but..."

    show player 11
    show tstand 20
    sara "Hehehe, say no more."

    sara "It's no problem at all, dear."

    show old_roxxy bikini usa 13f
    show player 13
    sara "I just wish it was a little bigger is all..."

    show tstand 19d
    show old_roxxy bikini usa 11f with dissolve
    roxxy "Does it look bad?"

    show old_roxxy bikini usa 9f
    show tstand 19
    terry "Not at all!"

    terry "It's a bit tight but there's nothing wrong with that..."

    terry "In fact, it's making me want to salute all the more!"

    terry "Oh ho ho!"

    show tstand 20
    sara "Haha, {b}Terry{/b} you're terrible!"

    sara "You look gorgeous, sweetie!"

    sara "Go ahead and keep it!"

    show tstand 20d at right with dissolve
    sara "But first you gotta get up there and win this thing!"

    hide tstand
    show tstand 19d at Position (xpos=729)
    with dissolve
    show old_roxxy bikini usa 10f
    roxxy "Benar!"

    show old_roxxy bikini usa 10 zorder 1 at Position (xpos=450) with dissolve
    roxxy "Wish me luck, {b}[firstname]{/b}!"

    show old_roxxy bikini usa 9
    show player 14
    player_name "Heh, you don't need it but good luck!"

    show old_roxxy bikini usa 10
    roxxy "Aww, thanks, {b}[firstname]{/b}!"

    hide player
    show old_roxxy bikini usa 7 at left
    with dissolve
    pause
    hide old_roxxy
    show player 13 at left
    with dissolve
    show tstand 19
    terry "I take it things are progressing well with that one?"

    show tstand 19d
    show player 10
    player_name "Hah?"

    show player 5
    show tstand 19c
    terry "Oh ho ho!"

    terry "Never mind Skipper."

    show tstand 19
    terry "Why don't you take my {b}Sara{/b} here and go find a couple of seats?"

    terry "I've got a show to host!"

    show player 13
    show tstand 20b
    sara "Go get 'em, love."

    show tstand 20e with dissolve
    pause
    show tstand 20 with dissolve
    sara "C'mon, {b}[firstname]{/b}! Let's go find some seats!"

    hide tstand with dissolve
    show player 14
    player_name "Ya, Bu."

    hide player with dissolve

    scene location_beach_cutscene05
    show text _ ("The competition was so much fun to watch!\nAll those beautiful women in skimpy bikinis...\n... And {b}Miss Sara{/b} sitting beside me the entire event.\nIt was such a good day!") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("{b}Roxxy{/b} and her friends all made it to the finals too!\n... But there was never a doubt as to who was going to win.") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("None of those other girls could compare to {b}Roxxy{/b}!!!") as caption with dissolve
    pause

    scene location_beach_water_contest_closeup
    show player 13 at Position (xpos=500)
    show old_missy bikini 13 at left
    show old_becca bikini 17 at Position (xpos=315)
    show old_roxxy bikini usa 4 at right
    with fade
    roxxy "Wooooo!!!"

    missy "Hehehe!"

    show old_roxxy bikini usa 2
    becca "Way to go, girl!"

    show old_missy bikini 1
    show old_becca bikini 1
    show player 14
    player_name "Congratulations, {b}Roxxy{/b}!"

    show player 14f at Position (xpos=550) with dissolve
    player_name "To all of you, really!"

    show player 13f
    show old_missy bikini 2
    missy "I made it to the finals!"

    show old_missy bikini 13
    missy "Did you see me, {b}[firstname]{/b}?!"

    show old_missy bikini 1
    show old_becca bikini 14
    becca "... Of course he saw you, dummy..."

    becca "He was in the crowd watching the entire time."

    show old_becca bikini 16
    show old_missy bikini 2b
    missy "Oh, were you checking to see if he was watching?!"

    show old_missy bikini 1b
    show old_becca bikini 14
    becca "Apa?!"

    becca "T-tidak!"

    becca "Diam!"

    show old_becca bikini 1
    show old_roxxy bikini usa 4
    roxxy "Ha ha ha!"

    show old_roxxy bikini usa 3
    roxxy "You guys never stop!"

    show player 13 at Position (xpos=500) with dissolve
    show old_roxxy bikini usa 4
    roxxy "I can't believe I won!"

    show player 18
    roxxy "{b}[firstname]{/b}, I won!!!"

    show old_roxxy bikini usa 2
    show player 14
    player_name "I know! You were really awesome!"

    show player 13
    show old_roxxy bikini usa 4
    roxxy "Hehehe!"

    show old_roxxy bikini usa 3
    roxxy "Thank you so much for all your help today!"

    show old_roxxy bikini usa 2
    show old_becca bikini 2b
    becca "Heh, yeah... He was a \"big help\" wasn't he, {b}Roxxy{/b}?!"

    show old_becca bikini 1b
    roxxy "..."
    show old_missy bikini 8
    missy "... Hah?"

    show old_missy bikini 2
    missy "Oh, wait! I get it!"

    show old_missy bikini 13
    show old_becca bikini 16
    missy "You're talking about his huge dick, right?!"

    show old_becca bikini 17
    show old_roxxy bikini usa 4
    show player 37 at Position (xoffset=41) with dissolve
    becca "Ha ha ha!"

    missy "Ha ha ha!"

    roxxy "... Hahaha!"

    show old_becca bikini 1
    show old_missy bikini 1
    show old_roxxy bikini usa 3
    roxxy "Just ignore them, {b}[firstname]{/b}."

    roxxy "Seriously, thank you for today!"

    show old_roxxy bikini usa 2
    show player 14 with dissolve
    player_name "Dengan senang hati."

    player_name "You need help carrying it home?"

    show player 13
    show old_roxxy bikini usa 3
    roxxy "Nah, I'll make these two bitches carry it."

    show old_roxxy bikini usa 2
    becca "..."
    show old_missy bikini 2
    missy "Oh, I'll carry it!"

    show old_missy bikini 1
    show old_roxxy bikini usa 3
    roxxy "I'll see you at school?"

    show old_roxxy bikini usa 2
    show player 14
    player_name "Sure. I'll see you all tomorrow."

    show player 13
    show old_becca bikini 2b
    becca "Sampai jumpa, {b}[firstname]{/b}."

    show old_becca bikini 1b
    show old_missy bikini 13
    missy "Byeee, {b}[firstname]{/b}!!!"

    hide old_becca
    hide old_missy
    hide old_roxxy
    hide player
    with dissolve
    return

label beach_cabin_roxxy_massage:
    scene expression "backgrounds/location_beach_cabin_closeup.jpg"
    show old_roxxy bikini 2 at right
    show player 13 at left
    with dissolve
    roxxy "Sorry, it took me forever to slip away from them!"

    show old_roxxy bikini 1
    show player 14
    player_name "Tidak masalah."

    player_name "You ready for a massage?"

    show player 13
    show old_roxxy bikini 2
    roxxy "Ya, ya!"

    roxxy "You give the best massages!"

    show old_roxxy bikini 1
    show player 12
    player_name "Hey, isn't that {b}Miss Sara{/b}'s bikini?"

    show player 13
    show old_roxxy bikini 2
    roxxy "Yeah, she told me to keep it remember?"

    roxxy "I thought you might want me to wear it for our massage sessions?"

    show old_roxxy bikini 1
    show player 14
    player_name "Y-yeah, definitely!"

    show player 13
    show old_roxxy bikini 2
    roxxy "Hehehe!"

    show old_roxxy bikini 5 with dissolve
    pause
    show old_roxxy bikini 6 with dissolve
    show player 434
    pause
    show old_roxxy bikini 7 with dissolve
    pause
    show old_roxxy bikini 8 with dissolve
    pause
    show old_roxxy bikini 9 with dissolve
    pause
    show old_roxxy bikini usa 5 with dissolve
    pause
    show old_roxxy 22 with dissolve
    pause
    show old_roxxy bikini usa 6 with dissolve
    pause
    show old_roxxy bikini usa 14 with dissolve
    pause
    show old_roxxy bikini usa 12 with dissolve
    roxxy "Well, don't just stand there gawking at my tits, start rubbing!"

    hide old_roxxy
    hide player
    with dissolve
    scene expression "backgrounds/location_beach_cabin_closeup_massage.jpg"
    show old_roxxy massage 3 with dissolve
    pause
    show old_roxxy massage 4_5 with dissolve
    roxxy "Hmm..."

    player_name "..."
    pause
    show old_roxxy massage 1 with dissolve
    player_name "Apakah itu terasa enak?"

    show old_roxxy massage 2
    roxxy "... Oh ya."

    roxxy "Rub a little harder."

    show old_roxxy massage 1
    player_name "You got it!"

    show old_roxxy massage 3 with dissolve
    pause
    show old_roxxy massage 4_5 with dissolve
    pause
    roxxy "Phew, that's good!"

    player_name "..."
    pause
    label roxxy_massage_45_repeat:
        show old_roxxy massage 4_5 with dissolve
        pause
    call screen roxxy_massage("roxxy_massage_45_repeat")
    pause
    show old_roxxy massage 3 with dissolve
    pause
    show old_roxxy massage 8_9 with dissolve
    roxxy "Mmm... That's so good."

    roxxy "Make sure you don't miss any spots!"

    player_name "Ya, saya tahu."

    player_name "I'll make sure to get everything!"

    pause
    roxxy "Ooh, that's it!"

    player_name "..."
    label roxxy_massage_89_repeat:
        show old_roxxy massage 8_9 with dissolve
        pause
    call screen roxxy_massage("roxxy_massage_89_repeat")
    pause
    show old_roxxy massage 3 with dissolve
    pause
    show old_roxxy massage 5 with dissolve
    pause
    show old_roxxy massage 6_7 with dissolve
    pause
    roxxy "Ahhh... That feels REALLY good, {b}[firstname]{/b}..."

    player_name "... Y-yeah?"

    roxxy "Mmmhmm, don't stop..."

    player_name "O-oke."

    pause
    label roxxy_massage_67_repeat:
        show old_roxxy massage 6_7 with dissolve
        pause
    call screen roxxy_massage("roxxy_massage_67_repeat")
    pause
    show old_roxxy massage 3 with dissolve
    pause
    show old_roxxy massage 8 with dissolve
    pause
    show old_roxxy massage 9_10 with dissolve
    roxxy "Ngghh!!"

    roxxy "..."
    roxxy "Wah!"

    player_name "..."
    roxxy "Rasanya luar biasa!"

    pause
    show old_roxxy massage 3 with dissolve
    roxxy "Ahh, keep going!"

    show old_roxxy massage 9_10 with dissolve
    roxxy "Jangan berhenti!"

    roxxy "Jangan-"

    missy "{b}Roxxy{/b}, are you guys in here?"


    scene location_beach_cutscene06
    show text _ ("Once again, {b}Missy{/b} and {b}Becca{/b} were at the entrance of the tent...") as caption
    with fade
    pause

    scene location_beach_cabin_closeup
    show old_roxxy bikini usa 1 at right
    show old_becca bikini 1b at Position(xpos=315)
    show old_missy bikini 1b at left
    with fade
    roxxy "!!!" with hpunch
    hide old_roxxy
    show old_roxxy bikini usa 15b zorder 1 at Position (xpos=650)
    show player 82f zorder 0 at right
    with dissolve
    roxxy "Goddamnit, you two!"

    roxxy "Are you spying on us again?!"

    show old_roxxy bikini usa 15
    show old_missy bikini 13
    missy "Ya."

    show old_missy bikini 1b
    show old_becca bikini 14
    becca "Huh?! No!"

    show old_roxxy bikini usa 17 with dissolve
    becca "Diam, {b}Nona{/b}!"

    show old_becca bikini 16
    show old_missy bikini 8
    missy "Apa?"

    show old_missy bikini 15 with dissolve
    missy "We want a massage too..."

    show old_missy bikini 14 with dissolve
    show old_becca bikini 18
    becca "Oh. My. God."

    show old_becca bikini 1
    show old_roxxy bikini usa 15b with dissolve
    roxxy "{i}*Huh*{/i}"

    show old_roxxy bikini usa 18 with dissolve
    roxxy "We were just finishing anyways..."

    show old_roxxy bikini usa 17
    show old_missy bikini 13
    missy "Cool, I'll go next!"

    show old_missy bikini 14
    show old_roxxy bikini usa 18
    roxxy "Yeah, I don't think so!"

    roxxy "Get your dumb asses back out to the water!"

    show old_roxxy bikini usa 17
    show old_missy bikini 10
    missy "Aduh..."

    hide old_becca
    hide old_missy
    with dissolve
    show old_roxxy bikini usa 18f at Position (xpos=550) with dissolve
    roxxy "Sorry about them, {b}[firstname]{/b}..."

    show old_roxxy bikini usa 17f
    show player 83bf
    player_name "Hehe, tidak apa-apa."

    player_name "It's actually really cute."

    show player 83cf
    show old_roxxy bikini usa 12f
    roxxy "Heh, yeah I know..."

    roxxy "... But I can't give them everything they want."

    roxxy "Buncha greedy bitches, those two!"

    show old_roxxy bikini usa 13f
    show player 83bf
    player_name "Ha ha ha!"

    show player 83cf
    show old_roxxy bikini usa 10f with dissolve
    roxxy "Well, thanks for the massage."

    show old_roxxy bikini usa 9f
    show player 83bf
    player_name "Dengan senang hati."

    show player 83cf
    show old_roxxy bikini usa 11f
    roxxy "Who knows? Maybe next time we'll get to finish..."

    show old_roxxy bikini usa 9f
    show player 82f
    player_name "{i}*Meneguk*{/i}"

    show old_roxxy bikini usa 10f
    roxxy "Hehehe."

    hide old_roxxy with dissolve
    hide player with dissolve
    return

label beach_roxxy_spin_bottle_sex_intro:
    scene expression game.timer.image("backgrounds/location_beach_water_day{}_blur.jpg")
    show player 14f at right
    show old_missy bikini 1 zorder 2 at left
    with dissolve
    player_name "Hey, {b}Missy{/b}."

    show player 13f
    show old_missy bikini 16 with dissolve
    missy "{i}*Terkesiap*{/i}!"

    show old_missy bikini 13 with dissolve
    missy "He's here!"

    missy "{b}Roxxy{/b}, {b}Becca{/b}!! He's here, he's here, HE'S HERE!!!"

    show old_missy bikini 1 with None
    show old_becca bikini 2 zorder 1 at Position (xpos=315)
    show old_roxxy bikini 1f zorder 0 at Position (xpos=500)
    with dissolve
    becca "Hai, {b}[firstname]{/b}."

    show old_becca bikini 1
    show player 14f
    player_name "Hai, {b}Becca{/b}."

    show player 13f
    show old_missy bikini 2
    missy "He's finally here!!"

    show old_missy bikini 1
    show old_roxxy bikini 19bf
    roxxy "Oh my god, shut up."

    roxxy "We heard you the first time."

    show old_roxxy bikini 1f
    show old_missy bikini 10
    missy "Tsk, you shut up!"

    show old_missy bikini 13
    show old_roxxy bikini 20 at Position (xpos=600) with dissolve
    missy "I'm excited..."

    show old_missy bikini 1
    show old_becca bikini 19
    becca "..."
    show old_roxxy bikini 19
    roxxy "Do you want me to call the whole thing off?!"

    show old_roxxy bikini 20
    show old_becca bikini 6
    show old_missy bikini 8
    becca "Apa?!"

    missy "No, please!"

    show old_becca bikini 6b
    missy "I'm sorry! Look, I'm shutting up right now!"

    show old_missy bikini 16 with dissolve
    show old_roxxy bikini 2
    roxxy "Yeah, we'll see how long that lasts..."

    show old_roxxy bikini 1
    show player 17f
    player_name "Hahaha, you girls are too funny!"

    show player 14f
    show old_roxxy bikini 1f at Position (xpos=500) with dissolve
    player_name "Jadi, ada apa?"

    player_name "{b}Roxxy{/b} said something about a surprise?"

    show player 13f
    show old_roxxy bikini 2f
    roxxy "Yeah, I've got-"

    show old_missy bikini 13 with dissolve
    missy "A great surprise!"

    show old_roxxy bikini 24f
    show old_becca bikini 13
    with dissolve
    pause
    show old_roxxy bikini 20 at Position (xpos=600) with dissolve
    missy "You're going to love-"

    hide old_becca
    show old_missy bikini 18
    with dissolve
    becca "{b}Missy{/b} shut up!"

    show old_missy bikini 18b
    show old_roxxy bikini 19
    roxxy "Dengan serius?!"

    roxxy "You can't even be quiet for five seconds?!"

    show old_roxxy bikini 20
    show old_missy bikini 19
    becca "Don't worry, she's done."

    show old_missy bikini 19b
    show old_roxxy bikini 19b
    roxxy "{i}*Huh*{/i}"

    show old_roxxy bikini 2f at Position (xpos=500) with dissolve
    roxxy "We're gonna play spin the bottle."

    show old_roxxy bikini 1f
    show player 14f
    player_name "Heh, spin the bottle again?"

    show player 13f
    show old_roxxy bikini 22f with dissolve
    roxxy "Yes, but with a slight rule change."

    show old_roxxy bikini 21f
    show player 12f
    player_name "Rule change?"

    show player 13f
    roxxy "Mmmhmm..."

    show old_roxxy bikini 22f
    roxxy "You see, at a certain point... I'm gonna call {b}final spin{/b}."

    roxxy "Then you will spin one final time."

    roxxy "... And whomever the bottle lands on, will join us in the changing room for a special reward."

    show old_roxxy bikini 21f
    show player 14f
    player_name "Oh?"

    player_name "What kind of special reward?"

    show player 13f
    show old_missy bikini 17 with dissolve
    missy "Mrffllmmmrf!"

    show old_roxxy bikini 19bf with dissolve
    roxxy "..."
    show old_missy bikini 18b with dissolve
    roxxy "She really can't keep her mouth shut!"

    show old_missy bikini 19b
    show old_roxxy bikini 2f
    roxxy "Anyways, it's a surprise."

    roxxy "You'll have to play to find out."

    show old_roxxy bikini 1f
    show player 14f
    player_name "Hehe, baiklah."

    player_name "Ayo lakukan!"

    show player 13f
    show old_missy bikini 17 with dissolve
    missy "Mrrfff!!"

    show player 14f
    player_name "Heh, she's so excited..."

    show player 13f
    show old_missy bikini 18b with dissolve
    show old_roxxy bikini 19f
    roxxy "{i}*Sigh*{/i}..."

    show old_roxxy bikini 1f
    show old_missy bikini 19
    becca "You have no idea..."

    hide old_roxxy
    hide old_missy
    hide player
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
