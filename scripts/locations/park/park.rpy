label park_dialogue:
    $ player.go_to(L_park)
    if game.timer.is_dark():
        if getPlayingMusic("<loop 108.292 to 180.658>audio/music_rap_distant.ogg"):
            $ playMusic("<loop 108.292 to 180.658>audio/music_rap_distant.ogg")

    if not game.timer.is_dark():
        if getPlayingSound("<loop 7 to 114>audio/ambience_suburb.ogg"):
            $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg", 1.0)
    else:

        if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
            $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)

    if game.timer.is_dark() and L_park.first_visit:
        call expression game.dialog_select("park_count_night_0")
        $ L_park.visited()

    if M_eve.is_state(S_eve_clients_park_fliers) and game.timer.is_day():
        call expression game.dialog_select("park_eve_clients_park_fliers")
        $ M_eve.trigger(T_eve_park_fliers_hung)

    $ game.main()

label park_night_closed:
    scene expression player.location.background_blur
    show player 10 with dissolve
    player_name "( It's getting late. I should go home. )"
    hide player
    $ game.main()

label park_pilly_button:
    call expression game.dialog_select("park_pilly_button_dialogue")
    $ player.go_to(L_map)
    $ M_roxxy.trigger(T_roxxy_drug_deal_over)
    $ game.timer.tick()
    $ game.sleep_lock = False
    $ game.main()

label park_eve_pranking_douches_backpack:
    if M_eve.is_state(S_eve_pranking_douches):
        scene expression player.location.background_blur with None
        show anon f_worried with dissolve
        anon @ -m_talk "( Those look like they belong to {b}Tyrone{/b} and his friends. )"
        anon @ -m_talk "( I should leave them alone, I don't wanna start anything with those guys. )"
        $ game.main()
    scene expression player.location.background_blur with None
    show anon f_worried_low a_backpack_chico
    show eve f_nervous_down a_backpack_tyrone
    with dissolve
    eve "Remember to be careful, you do not want any of this liquid on you..."
    eve "You'll be scrubbing for a week to get the stink off!"
    anon "Y-yeah, okay..."
    show eve a_backpack_tyrone_in with dissolve
    anon f_worried_low @ -m_talk "( Just drop, seal, and smash... )"
    anon @ -m_talk "( You can do this! )"
    show anon a_backpack_chico_vials with dissolve
    eve f_surprised "Holy shit!"
    anon a_backpack_chico f_surprised @ -m_talk "!!!"
    anon f_worried "What?"
    eve f_happy a_backpack_tyrone_weed @ f_laugh a_backpack_tyrone_weed "Jackpot baby!"
    anon f_surprised "I-is that?"
    eve "{b}Tyrone{/b}'s stash!"
    pause
    eve a_hip @ f_laugh a_idle "Oh, this just keeps getting better and better!"
    anon f_worried "You're taking it?!"
    eve "Of course."
    anon @ -m_talk "..."
    eve @ a_wtf "What?!"
    eve @ f_eyeroll "{i}*Sigh*{/i} It's just going to get ruined in there anyways..."
    anon f_unimpressed "Fine."
    anon "Just hurry up, before they catch us."
    eve "You finished with yours?"
    anon f_worried a_idle @ f_worried_low "Yup."
    eve @ f_laugh "Hehehe!"
    eve "Time for our getaway!"
    hide eve with dissolve
    anon @ a_surprised_up_both "Whoa, wait for me!"
    hide anon with dissolve
    scene black with fade
    pause
    $ player.go_to(L_park_bushes)
    scene expression player.location.background_blur with None
    show anon b_dressed_catch_breath:
        xoffset 50
    show eve b_dressed_tired f_disgusted_wince_down
    with dissolve
    anon "Haah... Haah..."
    anon "Man, you're faster than you look..."
    show anon b_dressed f_tired with dissolve
    eve f_laugh "Hehe, what a rush!"
    show eve b_dressed f_happy a_hip with dissolve
    eve "That was so awesome!"
    anon "I'm just glad it's over."
    eve "You worry too much, {b}[firstname]{/b}..."
    eve "Everything worked out."
    anon f_worried "Yeah, I guess..."
    eve "I just wish I could see their faces when they open those bags!"
    show anon f_normal
    eve @ f_laugh "Hahahaah!"
    ronda "Hey, move it!"
    show eve f_surprised:
        flip
        xoffset 400
    show ronda:
        xoffset 100
    with dissolve
    show anon f_surprised
    eve "!!!"
    anon "{b}Ronda{/b}?"
    show anon f_surprised_teeth
    eve f_nervous "Jesus, you scared me!"
    show anon f_worried
    ronda f_suspicious "What are you two doing out here anyways?!"
    eve "We could ask you the same question!"
    ronda f_normal @ f_eyeroll "Umm, the same thing I do every night?"
    ronda "Going for a jog before bed."
    eve "Oh."
    ronda "Never seen you two out here before though..."
    anon f_shy a_behind_head "Y-yeah, we were just-"
    eve f_surprised "Looking for our friend!"
    anon f_skeptical a_idle "Huh?"
    eve f_nervous_right "You know, OUR FRIEND?!"
    anon f_surprised_teeth @ f_surprised "O-oh, right!"
    eve f_normal "He's a tall guy, dark clothes, goofy haircut... You seen him?"
    show anon f_worried
    ronda f_suspicious a_crossed "No."
    eve "Oh, well, shoot..."
    eve "I guess we'd best keep looking then, huh?"
    anon @ -m_talk "..."
    eve f_normal_right "C'mon, {b}[firstname]{/b}... Let's-"
    $ playMusic()
    chico "YO, WHAT THE FUCK!" with hpunch
    show eve f_surprised:
        unflip
        xoffset -200
    show anon:
        flip
        xoffset -350
    show ronda f_normal
    anon f_surprised_teeth "!!!"
    chico "Did you fart or something?"
    show eve f_happy
    chad "N-no?"
    tyrone "Damn, something fucking stinks..."
    chad "Maybe it's a skunk or something?"
    tyrone "That ain't no skunk, man..."
    chico "Eugh, it smells like whale diarrhea!"
    chico "What the fuck is that?!"
    tyrone "I dunno man, my eyes are watering..."
    tyrone "Let's get up on out of here!"
    chico "For real, yo!"
    show anon f_shy a_behind_head:
        unflip
        xoffset 100
    show eve f_nervous:
        flip
        xoffset 400
    with dissolve
    show ronda f_glaring
    chad "{i}*Cough* *Cough*{/i}"
    chico "Ahh, fuck... I think it's the bags, dawg!"
    tyrone "Sweet Jesus, it smells like Bigfoot's dick cheese!"
    pause
    eve f_nervous_right "Eheh, that's weird..."
    eve "I wonder what happened?"
    anon f_worried_high "Y-yeah, weird."
    show eve f_nervous
    ronda f_normal @ f_eyeroll "Alright, what did you guys do?"
    show anon f_surprised
    eve "Us?!"
    eve "We didn't-"
    tuuku "Hahahaaah!!"
    show tuuku f_laugh a_hips:
        flip
        xoffset -100
    with dissolve
    show anon f_surprised_left
    show eve f_nervous_right
    tuuku "Did you guys hear that?!"
    tuuku "We got those fuckers so goo-"
    show tuuku f_surprised
    pause
    show anon f_surprised_teeth a_idle with dissolve
    tuuku f_normal "Oh."
    tuuku f_happy @ a_point "Umm, who's the babe?"
    show ronda f_eyeroll
    eve "That's {b}Ronda{/b}... She goes to our school."
    show ronda f_normal
    show anon f_worried
    tuuku "Reeeeally?"
    tuuku "How you doing, beautiful?"
    show eve f_nervous
    ronda f_upset "Eugh, in your dreams, goth boy..."
    tuuku @ f_sad "Ouch, alright... Just trying to be friendly."
    ronda f_suspicious "So, are you guys gonna tell me what you're {i}really{/i} doing out here?"
    show eve f_nervous_down
    anon f_worried_low "{i}*Sigh*{/i} We were pulling a prank on {b}Tyrone{/b} and his friends..."
    show eve f_nervous
    ronda f_smirk "Yeah, I figured that much."
    show anon f_surprised
    ronda "What did you do to them?"
    show anon f_worried
    eve "We put stink bombs in their bags..."
    ronda f_normal @ f_laugh "Heh, really?!"
    eve "Yeah."
    eve f_normal "They totally deserved it though, those douchebags sprayed me with a watergun filled with beer the other day!"
    ronda "Hey, you'll get no arguments from me... I hate those tools!"
    anon @ f_surprised "You do?"
    ronda "Yeah, every night I jog past them and every night they find some way to annoy me."
    eve "Yup, that sounds like their M.O."
    tuuku f_confused "Why don't you just jog somewhere else?"
    ronda f_suspicious a_idle "Hmph, why should I change my routine?"
    ronda "They're the jackasses!"
    show ronda f_normal
    tuuku f_normal @ a_arrest "Whoa, calm down killer... I was just asking."
    chico "Just get the bags, {b}Chad{/b}!"
    show tuuku f_surprised:
        unflip
        xoffset -600
    show anon f_surprised:
        flip
        xoffset -400
    show eve f_happy:
        unflip
        xoffset -200
    with dissolve
    chad "{i}*Cough*{/i} Eugh, I can taste it you guys..."
    chad "Fuck this, let's just leave em!"
    show tuuku f_laugh
    tyrone "Nah, man... My stash is in there!"
    ronda "I guess I'd better jog somewhere else tonight though, huh?"
    show tuuku f_happy:
        flip
        xoffset -100
    show anon f_worried:
        unflip
        xoffset 100
    show eve:
        flip
        xoffset 400
    eve "Yeah, I would if I were you."
    tuuku "Unless you wanna jog into a stink cloud, the likes of which you can't even imagine!"
    eve @ f_laugh "Haha!"
    ronda @ f_laugh "Haha!"
    anon "What do we do now?"
    eve f_happy_right "We celebrate our victory!"
    tuuku "Oh, yeah?"
    tuuku "What did you have in mind?"
    show eve a_idle with dissolve
    eve a_weed_hold "Mm, I'm thinking we blaze up one of these!"
    show tuuku f_surprised
    show anon f_surprised
    show ronda f_surprised
    tuuku f_happy @ a_point "Hey, where did you get that?!"
    show ronda f_normal
    eve "I might have lifted {b}Tyrone{/b}'s stash..."
    show anon f_worried
    tuuku "You sneaky monkey!"
    eve f_nervous_down a_weed_light @ f_laugh "Hehehe!"
    pause
    show eve f_drink a_weed_smoke with dissolve
    pause
    eve f_happy_right a_weed_hold "You guys want a hit?"
    show tuuku f_laugh a_thumb with dissolve
    tuuku "Of course!"
    show eve a_idle
    show tuuku a_weed_smoke f_smoke
    with dissolve
    pause
    eve f_happy "{b}Ronda{/b}?"
    show tuuku a_weed_hold f_happy with dissolve
    ronda @ f_suspicious "Ehh, no thanks."
    ronda "They test me all the time before swim meets."
    ronda "If I pop positive for marijuana, it's goodbye scholarship..."
    eve "Hmm, fair enough..."
    eve f_happy_right "{b}[firstname]{/b}?"
    show anon f_surprised_teeth
    menu:
        "Sure.":
            show tuuku a_idle
            show anon f_worried_low a_weed_hold
            with dissolve
            pause
            show anon f_smoke a_weed_smoke with dissolve
            pause
            anon f_tired a_weed_hold @ f_cough a_weed_cough "{i}*Cough Cough* *Sputter* *Cough Cough*{/i}"
            show ronda f_happy
            eve f_happy_right @ f_laugh "Hehe!"
            tuuku @ f_laugh "Uh oh, somebody has virgin lungs!"
            anon "Heh, yeah..."
            show anon a_idle
            show eve a_weed_hold
            with dissolve
            tuuku "You're in for a real treat kid, this is some of my best stuff!"
        "No thanks.":

            anon f_worried "Nah, drugs aren't really my thing..."
            show ronda f_happy
            tuuku @ f_confused "Dude, for real?"
            tuuku "You don't know what you're missing out on... This is some of my best shit."
            eve f_sad_right "Hey, don't pressure him!"
            eve f_normal_right "It's cool, {b}[firstname]{/b}."
            eve "You don't have to do anything you don't want to."
            anon "Y-yeah, thanks."

    ronda f_normal "I should really start heading home."
    show eve f_happy
    tuuku "Well, hold on now... Why don't you walk with us?"
    ronda @ f_suspicious "I'm supposed to be jogging, remember?"
    tuuku f_normal "Tsk, c'mon... You can take one night off, can't you?"
    eve "Yeah, what's with you and sports, {b}Ronda{/b}?"
    ronda @ f_suspicious "Huh?"
    show tuuku a_weed_smoke f_smoke with dissolve
    eve "Well, I mean... You're always doing something!"
    eve "Volleyball, basketball, swimming... And when you're not doing that, you're exercising!"
    show tuuku f_normal a_idle with dissolve
    ronda @ -m_talk "..."
    eve f_happy_right "I mean, she's really nonstop with it!"
    eve "I'm pretty sure I saw her doing leg lifts under her desk in {b}Miss Okita{/b}'s class the other day."
    show eve f_happy
    ronda @ f_eyeroll "I don't really wanna get into it..."
    eve "Oh?"
    ronda "Let's just say, it's complicated and leave it at that."
    anon "I think it's impressive."
    eve f_normal_right "Impressive?"
    anon "Y-yeah, she's like, totally committed to being the best she can be."
    anon f_normal "It's cool!"
    tuuku f_happy "Plus, it's given you that rocking body!"
    ronda @ f_suspicious "Yeeeeah, because that's not a creepy thing to say..."
    eve f_happy @ f_laugh "Haha!"
    tuuku @ a_shrug "What, it was a compliment!"
    eve "Nice one, Romeo!"
    tuuku @ a_flip "Shut up!"
    anon f_laugh "Haha!"
    tuuku a_hips "It's not my fault this girl is impervious to my legendary charm!"
    show anon f_normal
    ronda @ f_laugh "Pfft, hahaha!"
    pause
    eve f_surprised "Whoa, whoa, whoa..."
    eve "Hold on a second, guys."
    ronda "What?"
    eve "Do you hear that?"
    show tuuku f_confused
    pause
    ronda f_suspicious "No?"
    pause
    anon f_surprised @ f_confused "Yeah, I don't hear anything eith-"
    eve @ f_pouting a_wtf "Shhh!!"
    pause
    tuuku f_happy @ f_laugh "I think it's just the weed kicking in..."
    eve "No, seriously... I heard something up ahead!"
    pause
    tuuku "Hehe, maybe it's aliens?!"
    show anon f_laugh
    show ronda f_eyeroll
    eve f_sad_right "Shut up!"
    show ronda f_normal
    show anon f_normal
    tuuku f_normal "No seriously, you better watch out, {b}Evie{/b}!"
    tuuku f_laugh "They're gonna take you up in their spaceship and probe you!"
    show anon f_flirt
    eve "Stop, you know that shit freaks me out!"
    tuuku f_happy @ f_laugh "Hahaha!"
    anon "Aliens freak you out?"
    eve f_nervous_down "Yeah..."
    anon f_skeptical "Seriously?"
    eve f_sad_right "Look, I know it's stupid but {b}Grace{/b} brought home a creepy movie about an alien abduction when I was little, and it scared the bejeezus out of me!"
    tuuku @ f_laugh "Haha!"
    show anon f_grin
    eve "It's not funny!"
    ronda "They aren't even real, you know that right?"
    show anon f_normal
    eve f_sad "No, and neither do you!"
    eve @ f_eyeroll "They could totally be real."
    ronda f_smirk "It's like being afraid of the boogeyman..."
    tuuku f_sad "Well, c'mon now, the boogeyman is real for sure."
    ronda f_normal @ f_eyeroll "Tsk."
    show eve f_normal_right
    tuuku "I'm serious, I've seen that dude... He's disgusting!"
    tuuku f_confused_back a_rub "... And he keeps stealing my socks when I'm asleep!"
    eve @ f_laugh "Pfft, hahaha!"
    eve "Damn it, {b}Tuuku{/b}... Stop maki-"
    show eve f_surprised
    show tuuku f_surprised a_idle
    if M_helen.finished_inclusive(S_helen_master_servant_fun):
        yumi "{i}*Gurk* *Gurk* *Gurk*{/i}"
        yumi "{i}*Sluuuurp*{/i}"
        harold "Ah, jeez..."
        anon f_surprised_teeth "!!!"
        eve "O-okay, you guys heard that right?"
        yumi "{i}*Gllllaaarrgghhh*{/i}"
        show anon f_surprised_low a_surprised_up
        show eve b_dressed_scared:
            unflip
            xoffset -223
        with dissolve
        eve "Eeep!!"
        eve "What is it?"
        show anon f_surprised
        ronda @ f_suspicious "Sounds like people."
        tuuku f_sad "Boogey people?"
        eve f_sad_right "Shut up!"
        anon "I think it's coming from over there..."
        harold "Ahh, I'm getting close..."
        yumi "{i}*Gurk* *Gurk* *Gurk*{/i}"
        scene expression "backgrounds/location_park_cutscene_04.jpg"
        anon "!!!" with hpunch
        eve "{i}*Gasp*{/i}"
        ronda "Holy shit..."
        tuuku "Oh shit!"
        tuuku "It's the fuzz!"
        scene expression "backgrounds/location_park_cutscene_05.jpg" with fade
        harold "What the-"
        harold "{b}Yumi{/b} stop!!"
        yumi "What's the matter?"
        harold "There're kids watching us!"
        yumi "Oh, crap!"
    else:
        yumi "Why do we always get park patrol?"
        yumi "It's so boring..."
        anon f_surprised "!!!"
        eve f_sad "O-okay, you guys heard that right?"
        harold "It's not that bad... Just try and enjoy the fresh air, will ya?"
        show anon f_surprised_low a_surprised_up
        show eve f_surprised b_dressed_scared:
            unflip
            xoffset -223
        with dissolve
        eve "Eeep!!"
        eve "What is it?"
        show anon f_surprised
        ronda @ f_suspicious "Sounds like people."
        tuuku f_sad "Boogey people?"
        eve f_sad_right "Shut up!"
        harold "Hey, who's out there?!"
        scene expression "backgrounds/location_park_cutscene_03.jpg" with fade
        yumi "Is that marijuana?!"
        harold "Stop right there and identify yourselves!"
        tuuku "Oh shit!"
        tuuku "It's the fuzz!"
        scene expression "backgrounds/location_park_cutscene_05.jpg" with fade
        ronda "Uhh..."
        anon "Uh oh."
        eve "..."
    scene expression player.location.background_blur
    show ronda f_surprised a_crossed:
        flip
        xoffset -125
    show eve f_sad:
        flip
        xoffset 250
    show anon f_worried
    if M_helen.finished_inclusive(S_helen_master_servant_fun):
        show harold f_suspicious a_light:
            xoffset -100
        show yumi f_suspicious:
            xoffset 50
    else:
        show harold b_disheveled f_suspicious a_light:
            xoffset -100
        show yumi b_disheveled f_embarrassed:
            xoffset 50
    with fade
    harold @ a_light_point "What's that in your hand, young lady?"
    eve "Uhh... N-nothing!"
    yumi f_suspicious "It doesn't look like nothing..."
    harold f_surprised "{b}Ronda{/b}?"
    ronda f_surprised_down "..."
    harold "Are you smoking pot?!"
    ronda f_surprised "What?!"
    ronda "Of course not!"
    yumi "You know her?"
    harold f_normal_closed a_facepalm "Y-yeah, it's the chief's daughter."
    yumi f_concerned "Oh, crap... Are you serious?"
    harold f_normal a_light "Dead serious."
    harold "What are you doing out here?"
    ronda "Jogging."
    harold "It doesn't look like jogging..."
    yumi "It certainly doesn't..."
    ronda "Well, I ran into them, see... And we were just talking, I-"
    yumi f_normal "We should search them."
    eve "What?!"
    eve "Y-you can't do that!"
    yumi "I'm afraid we can, young lady."
    yumi "If we suspect you are in possession of drugs, it's our job to search you."
    show anon a_up f_depressed:
        flip
        xoffset -513
    show yumi b_searching_mc:
        xoffset 0
    with dissolve
    ronda f_normal "C'mon, {b}Harold{/b}... You know I wouldn't get involved with drugs, not with my scholarship on the line."
    harold f_concerned "It's not my call, {b}Ronda{/b}."
    harold "If we find something, I have to take you to your father... Otherwise, he'll have my head."
    ronda f_surprised "Tsk, seriously?!"
    yumi "This one is clean."
    harold f_surprised "Hey, I know you too."
    harold "You're {b}Mia{/b}'s little friend, aren't you?"
    anon f_worried_left "Y-yes, sir."
    harold f_concerned @ f_normal_closed a_facepalm "{i}*Sigh*{/i}"
    hide anon
    show anon f_worried
    show eve f_sad_down a_wtf zorder 1:
        unflip
        xoffset -400
    show yumi b_searching_eve
    with dissolve
    eve "No, get away from me!"
    yumi "Young lady, please stop resisting..."
    eve "You can't do this!"
    if M_helen.finished_inclusive(S_helen_master_servant_fun):
        show yumi b_disheveled a_weed:
            xoffset 100
    else:
        show yumi b_dressed a_weed:
            xoffset 100
    hide eve
    show eve a_idle:
        flip
        xoffset 250
    with dissolve
    show anon f_hurt
    show ronda f_surprised_down
    show harold f_normal
    yumi "Shit."
    eve f_sad "That's not mine!"
    show anon f_sad
    yumi "Uh huh."
    harold "{i}*Sigh*{/i} Alright, everyone with us... We're taking you all down to the station."
    eve "Wait, no... Y-you can't-"
    show eve f_surprised
    ronda f_surprised "C'mon, {b}Harold{/b}... Please, don't do this!"
    harold "Not now {b}Ronda{/b}!"
    eve "It is mine, okay?!"
    eve f_sad_down "{b}Ronda{/b} didn't have anything to do with it!"
    eve f_surprised "Neither did, {b}[firstname]{/b}!"
    eve "It's all me!"
    harold "Enough!"
    harold @ a_light_point "You're all coming with us!"
    eve f_sad "Please..."
    yumi "MOVE!"
    scene black with fade
    $ player.go_to(L_police_lobby)
    $ L_police_lobby.first_visit = False
    scene expression player.location.background_blur with None
    show eve f_sad:
        flip
        xoffset -125
    show anon f_sad:
        xoffset -25
    show ronda f_surprised a_crossed:
        flip
        xoffset 200
    show harold f_concerned:
        xoffset -150
    show earl f_annoyed:
        xoffset 150
    with dissolve
    earl "You caught my daughter doing what?!"
    ronda "{b}Daddy{/b}, I swear I wasn't-"
    earl f_angry "You go and wait for me in my office!"
    ronda f_sad @ -m_talk "..."
    earl @ a_point_back "Now, damn it!"
    ronda "Yes, {b}Daddy{/b}."
    hide ronda with dissolve
    pause
    harold "To be fair, the only one we caught using was the girl with the blue hair."
    show yumi a_weed f_concerned_right:
        xoffset -350
    with dissolve
    show eve f_disgusted
    yumi "We found this on her too, sir."
    earl f_tired "Jesus..."
    eve "I told you, that isn't mine!"
    yumi f_concerned @ f_eyeroll "Yeah, right."
    harold @ f_normal "Even if that is the case, possession is nine-tenths of the law, young lady."
    eve f_confused "What's that supposed to mean?!"
    yumi "It means, that we found the drugs in YOUR possession!"
    yumi "So, unless you can definitively prove that it belongs to someone else... You're taking the wrap."
    show anon f_depressed
    eve f_sad @ -m_talk "..."
    show yumi f_concerned_right a_idle
    earl f_annoyed "I'll deal with my daughter."
    eve "{b}Ronda{/b} didn't even do anything!"
    earl f_angry "{b}Harold{/b}, see that our little drug queen here is booked and given her phone call."
    eve f_surprised "WHAT?!"
    harold f_surprised "You really want me to put her in a cell, sir?"
    eve f_sad "Y-you can't-"
    earl "If she wants to go down the path of drug abuse, I think it's best she finds out where it leads..."
    harold f_suspicious "{i}*Sigh*{/i} Alright."
    harold "C'mon, kiddo."
    hide harold
    hide eve
    with dissolve
    show yumi f_concerned
    eve "W-wait, I-"
    pause
    earl f_annoyed "{b}Yumi{/b}, take the boy to the lobby and alert his parents to come pick him up."
    yumi f_normal_right "Yes, sir."
    hide anon
    hide yumi
    with dissolve
    pause
    earl f_tired a_facepalm "Ugh, what a mess..."
    scene black with fade
    pause
    scene expression player.location.background_blur with None
    show anon f_worried:
        xoffset -50
    show yumi f_concerned:
        xoffset -250
    with dissolve
    anon "So, what's going to happen to us?"
    yumi "Well, you're just getting a ticket and a slap on the wrist."
    pause
    anon "What about {b}Eve{/b}?"
    yumi "She'll stay in lock-up until the morning, unless her family comes and bails her out."
    anon f_tired @ f_sad_down "That sucks..."
    yumi "After that, I suspect she'll just be fined, seeing as she's so young and it's her first offense."
    anon f_worried "Phew, okay... That's not so bad."
    pause
    yumi "You kids really picked a bad time to get caught smoking pot."
    anon "What do you mean?"
    yumi "Well, I shouldn't really be telling you this..."
    yumi @ f_embarrassed "... But a lot of drugs have been going through Summerville as of late."
    yumi "The chief has the entire force on high alert!"
    anon @ f_surprised "R-really?"
    yumi "Yup and to make matter worse, we've had to downsize our department recently because the mayor keeps cutting our budget!"
    anon "Why would he do that?"
    yumi "I don't know."
    pause
    yumi "It just doesn't make any sense..."
    yumi "We are way too understaffed to deal with something of this magnitude."
    anon "That's crazy!"
    yumi "Yeah, tell me about i-"
    grace "Hey, you!"
    show grace f_tired with dissolve
    show yumi f_normal_right
    grace "Can you tell me where my sister is?"
    anon f_surprised "{b}Grace{/b}?"
    grace @ f_surprised "{b}[firstname]{/b}?"
    grace @ f_eyeroll "Ugh, this is unbelievable..."
    show anon f_sad
    yumi "Can I help you?"
    grace "Yeah, I'm here to pay her bail."
    yumi f_concerned_right "Did they explain the situation to you?"
    grace "Apparently you guys have nothing better to do than hassle a couple kids over a little bit of marijuana!"
    yumi "Ma'am, please calm down..."
    grace "No seriously, it's so comforting to know that you guys are protecting us from these violent criminals..."
    grace "You should probably scope out the kindergarten up the road next..."
    yumi f_embarrassed @ -m_talk "..."
    grace "Just tell me where my sister is..."
    yumi "{i}*Sigh*{/i} Head down those stairs and turn right, my partner {b}Harold{/b} will sort you out."
    grace @ f_eyeroll "Hmph!"
    hide grace with dissolve
    show yumi f_concerned
    pause
    anon "Wow, she's seriously pissed."
    yumi "Y-yeah, I don't envy {b}Harold{/b} right now."
    debbie "Where is he?!"
    anon f_surprised_teeth @ f_shock "{b}[deb_name]{/b}?"
    yumi f_concerned_right "Your mother?"
    anon f_worried @ f_flirt "Ehh, she's more like a guardian..."
    show debbie b_casual f_sad with dissolve
    debbie "Oh my goodness, are you alright?!"
    show yumi f_normal:
        xoffset 0
    hide anon
    show debbie b_casual_hug2:
        xoffset 100
    with dissolve
    anon "Y-yeah, I'm okay..."
    show debbie b_casual_hug1:
        xoffset -400
    debbie "I was so worried!"
    show debbie b_casual f_sad:
        flip
        xoffset 250
    show anon f_worried:
        xoffset -50
    with dissolve
    debbie "What happened?"
    yumi f_embarrassed "We just found him and his friends smoking a little pot, ma'am..."
    debbie a_hips "{i}*Gasp*{/i} Drugs, {b}[firstname]{/b}?!"
    debbie "That isn't like you!"
    anon "I'm sorry, {b}[deb_name]{/b}..."
    yumi "It's only a minor offense, ma'am..."
    yumi "You just need to pay his ticket and you two can be on your way."
    debbie f_normal_down a_purse "Alright, how much is the ticket?"
    yumi f_concerned "Two hundred, ma'am."
    debbie f_surprised_worried "TWO HUNDRED?!"
    yumi "I'm afraid so..."
    anon f_sad_down "..."
    debbie f_sad @ f_gross "Ehh, will you take a check?"
    yumi f_normal "Of course, just speak with the front desk."
    debbie "T-thanks."
    yumi @ f_wink "Try and stay outta trouble, okay?"
    anon f_worried "Y-yeah, I will..."
    hide yumi
    hide debbie
    with dissolve
    pause
    anon "( Man, this is the last thing {b}[deb_name]{/b} needed right now... )"
    scene black with fade
    pause

    $ player.go_to(L_police_front)
    scene expression player.location.background_blur with None
    show anon f_worried
    show debbie b_casual
    with dissolve
    debbie "Heh, I never expected I'd be picking YOU up from the police station, {b}[firstname]{/b}!"
    debbie "{b}[jen_name]{/b} maybe, but not you..."
    anon "I'm so sorry, {b}[deb_name]{/b}."
    debbie f_sorry "Oh sweetie, it's alright..."
    debbie "The important thing is that you're safe."
    anon @ a_point_self "I'll pay you back for the ticket, I swear."
    debbie "Don't worry about it."
    debbie "Just promise me you won't do anything like this again..."
    anon f_shy @ f_brag_closed a_wave "Y-yeah, I promise."
    debbie "C'mon, let's get you home."
    hide debbie with dissolve
    pause
    eve "I'm sorry, okay?!"
    anon f_surprised @ -m_talk "( Hmm? )"
    anon f_worried @ -m_talk "( Looks like {b}Eve and her sister{/b} are arguing over there... )"
    hide anon with dissolve
    $ M_eve.trigger(T_eve_pranked_douches)
    $ L_police_lobby.visited()
    $ game.timer.tick(3)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
