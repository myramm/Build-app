label hallway_jenny_hallway_talk:
    scene expression player.location.background_blur with None
    show anon
    show jenny f_normal b_towelhead
    with dissolve
    jenny "Hai, {b}[firstname]{/b}!"

    show anon f_worried
    with dissolve
    anon "Oh, h-hey {b}[jen_name]{/b}..."

    anon "Did you just get out of the shower?"

    show jenny f_gross
    jenny "Duh, what gave it away?"

    show jenny f_normal
    anon f_skeptical @ -m_talk "..."
    show jenny f_laugh
    jenny "Hahahaah!"

    anon "Sangat lucu."

    show jenny f_grin
    pause
    anon f_normal "So, what are you doing today?"

    show jenny f_eyeroll
    jenny "Uhh, {i}WE'RE{/i} doing a camshow, remember?"

    show jenny f_normal
    anon "Yeah, I know that..."

    anon "I was just thinking that maybe afterwards we could hang out?"

    show jenny f_gross
    jenny "Hang out?"

    anon "Yeah, or maybe go out and do something together?"

    jenny "Why would we do that?"

    anon @ f_laugh "'Cause it would be fun!"

    jenny "..."
    anon "We had fun at the movie theater the other day, didn't we?"

    jenny "Uhh, I guess..."

    pause
    show jenny f_upset
    jenny "{i}*Sigh*{/i} Do we need to have the dating talk again?"

    anon f_tired @ -m_talk "..."
    anon "I just thought-"

    show anon f_surprised
    jenny "You thought what, that I didn't really mean it the first two times I told you I'm not interested?"

    anon f_worried "T-tapi-"

    show jenny f_angry
    jenny "I DON'T WANNA DATE YOU, {b}[firstname!u]{/b}!"

    show jenny f_upset
    anon "Kenapa tidak?!"

    show jenny f_eyeroll
    jenny "Because we've known each other for like, our entire lives, and dating you would be super weird!!!"

    show jenny f_upset
    show anon f_thinking a_rub with dissolve
    anon @ -m_talk "..."
    show jenny f_gross
    jenny "It would be like dating my brother or something..."

    show jenny f_grin
    show anon f_laugh a_idle with dissolve
    pause 1
    anon f_worried "Itu bukan-"

    anon f_unimpressed "Apa?!"

    show jenny f_upset
    jenny "Saya serius, {b}[firstname]{/b}!"

    jenny "We have a good thing going here..."

    jenny "Why are you trying to ruin it?"

    anon "Baiklah, terserah."

    anon "Forget about it."

    jenny "Gladly!"

    show jenny f_grin
    jenny "Now, don't forget about our show this afternoon!"

    anon "Ya, ya..."

    hide anon with dissolve
    jenny "... And make sure you eat something!"

    jenny "My fans are expecting a good performance!"

    pause
    show jenny f_eyeroll
    jenny "Pain in my ass..."

    scene black with fade
    $ player.go_to(L_home_entrance)
    scene expression player.location.background_blur with None
    show anon f_tired with dissolve
    anon @ -m_talk "( Well, that could have gone better... )"

    anon @ -m_talk "( She's really being stubborn about this! )"

    show anon f_thinking a_thinking with dissolve
    anon @ -m_talk "( {b}There's gotta be some way to convince her{/b}! )"

    anon @ -m_talk "( Hmm, maybe I should {b}check her diary again{/b}? )"

    anon @ -m_talk "( It's been pretty helpful so far... )"

    hide anon with dissolve
    return

label hallway_jenny_acknowleges_debbie_sex:
    scene expression player.location.background_blur with None
    show anon
    show debbie
    debbie "Oh, good morning {b}[firstname]{/b}."

    anon "Morning, {b}[deb_name]{/b}."

    debbie f_sexy "I was just getting ready to take a shower..."

    anon "Oh?"

    debbie "Is {b}[jen_name]{/b} still sleeping?"

    anon "Ya, menurutku begitu."

    debbie "You wanna join me?"

    anon f_shy "B-benarkah?"

    debbie f_normal @ f_laugh "Mmhmm!"

    debbie "Just wait a few minutes before coming in, okay?"

    show debbie f_sexy
    anon "Y-ya, oke."

    debbie @ f_laugh "Hehe, and don't keep me waiting too long!"

    anon f_laugh "Heh, I won't."

    show anon f_normal
    hide debbie with dissolve
    pause
    anon f_grin @ -m_talk "(Luar biasa!)"

    jenny "So you two {i}are{/i} fucking, huh?!"

    anon f_surprised @ -m_talk "!!!" with hpunch
    show jenny f_grin with dissolve
    anon f_worried "W-wha-"

    anon "I don't know what you're talking about..."

    show jenny f_eyeroll
    jenny "Oh, please!"

    show jenny f_upset
    jenny "It's so obvious!"

    anon "..."
    jenny "Look, I don't really give a fuck."

    anon "Y-you don't?"

    show jenny f_laugh
    jenny "Psh, hell no!"

    show jenny f_upset a_crossed with dissolve
    jenny "Fuck whoever you want, just don't let it interfere with our camshows!"

    anon f_skeptical @ -m_talk "..."
    jenny "aku serius!"

    show jenny f_angry
    jenny "If you screw up my gravy train, I'll fucking cut you!"

    anon f_shock "!!!"
    show jenny f_upset
    pause
    anon f_worried "Y-you don't think it's weird that me and {b}[deb_name]{/b} are... You know?"

    show jenny f_laugh
    jenny "Haha, of course it's weird!"

    show jenny f_grin a_hips with dissolve
    jenny "Not really my concern though, is it?!"

    anon "Saya kira tidak..."

    show jenny f_upset
    jenny "Just make sure you're ready for the show this afternoon, got it?"

    anon "Ya, saya mengerti."

    jenny "Bagus."

    show jenny f_grin
    jenny "Nanti, pecundang!"

    hide jenny with dissolve
    anon "..."
    show anon f_thinking a_thinking with dissolve
    anon @ -m_talk "( Hmm, {b}[deb_name]{/b} is waiting on me... )"

    show anon a_idle with dissolve
    anon f_worried @ -m_talk "( ... Maybe this isn't such a good idea after all. )"

    hide anon with dissolve
    return

label hallway_jenny_caught_talking_to_camslut:
    if store._in_replay is not None:
        $ player.location = L_home_hallway
        $ game.timer.tick(3)
    scene expression player.location.background_blur with None
    show anon f_worried
    jenny "Apakah kamu gila?!"

    pause
    show anon f_thinking a_thinking with dissolve
    anon @ -m_talk "(Hmm?)"

    show anon f_worried a_idle with dissolve
    jenny "No fucking way, haha!"

    anon f_grumpy @ -m_talk "( She's being awfully loud... )"

    pause
    anon f_worried @ -m_talk "( I wonder who she's talking to? )"

    jenny "The butt plug is enough you losers, trust me!"

    show anon f_surprised
    pause
    jenny "Hahaha, fucking sam9!"

    anon @ -m_talk "( Is she... Streaming? Right now?! )"

    anon f_flirt @ -m_talk "( I should take a quick peek... )"

    scene expression "backgrounds/location_home_jennybedroom_cutscene03.jpg" with dissolve
    jenny "So which toy do you guys want to see tonight?"

    jenny "{b}Bad Monster{/b}?"

    pause
    jenny "Yeah, I know you guys want to see me ride a real dick... I'm working on it, okay?!"

    pause
    jenny "Hmm?"

    pause
    jenny "Apa maksudmu?"

    pause
    jenny "There's someone in the background?"

    scene expression "backgrounds/location_home_jennybedroom_cutscene04.jpg"
    jenny "!!!" with hpunch
    jenny "{b}[firstname]{/b}?!"

    pause
    $ player.go_to(L_home_sisbedroom)
    scene expression game.timer.image("backgrounds/location_home_jennybedroom{}.jpg")
    show anon f_surprised_teeth:
        flip
    show jenny f_angry b_naked a_hips at flip
    with dissolve
    jenny "YOU FUCKING PERVERT!!"

    anon f_worried "Do you have something in your ass right now?!"

    show anon f_snarky
    jenny "GET OUT OF HERE!!!"

    anon @ f_laugh "Heh, are you a camgirl?!"

    jenny "RRRAAAAAHHH!!!"

    show jenny a_monster_hit:
        xoffset 100
    show anon b_dressed_blocking
    with dissolve
    anon "Ouch!"

    jenny "GET!!!"

    anon "Oke oke!"

    jenny "OUT!!!"

    anon "I'm sorry!"

    anon "Just stop hitting me!"

    hide anon with dissolve
    show jenny a_hips with dissolve
    jenny "Sulit dipercaya!"

    scene black with dissolve
    pause
    scene expression "backgrounds/location_home_jennybedroom_desk_evening.jpg"
    show jenny b_naked_back_plug a_sides with dissolve
    jenny "{i}*Sigh*{/i} Sorry guys..."

    pause
    jenny "No, that's my-"

    jenny "... He's just some guy I live with."

    pause
    show jenny a_hips with dissolve
    jenny "No, I'm not going to fuck him."

    pause
    jenny "Ugh, absolutely not!"

    pause
    jenny "... For real?"

    pause
    jenny "I don't believe you!"

    "PING"

    show jenny a_sides with dissolve
    pause
    show jenny b_naked_back_bending_plug with dissolve
    jenny "Astaga..."

    pause
    jenny "Three times that?!"

    pause
    jenny "Look, guys... I really can't."

    jenny "Just forget it, okay?"

    jenny "I'll find someone... I promise."

    jenny "Not him."

    pause
    jenny "Aku tahu."

    jenny "Let's just do the toys for tonight."

    pause
    jenny "No, don't leave!"

    pause
    jenny "..."
    show jenny b_naked_back_plug a_hips with dissolve
    jenny "Sial!"

    scene black with dissolve
    pause
    $ player.go_to(L_home_bedroom)
    scene expression player.location.background_blur with None
    show anon f_tired a_facepalm with dissolve
    anon @ -m_talk "( Sheesh, did she really just beat me with a giant dildo? )"

    anon @ -m_talk "( At least it wasn't the hair dryer... That thing really hurts! )"

    pause
    show anon a_idle with dissolve
    anon @ -m_talk "( Man, I'm exhausted. )"

    anon @ -m_talk "( I hope she's not still mad about this tomorrow. )"

    hide anon with dissolve
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["06_unlocked"] = True
    return

label hallway_jenny_confront_her_hallway:
    scene expression player.location.background_blur with None
    show jenny a_sides at flip
    show anon f_snarky:
        flip
    anon "Kamu pembohong!"

    show jenny f_upset a_hips with dissolve
    jenny "Permisi?!"

    anon "I know you're not transcribing online."

    jenny "Yeah, right. You don't know anything..."

    anon "Well, I know you're lying to {b}[deb_name]{/b}!"

    jenny "Why don't you just mind your own business, loser?!"

    anon @ -m_talk "..."
    anon f_worried "I just hope you're not doing something you're gonna regret for that money."

    show jenny f_eyeroll
    jenny "Ugh, terserah."

    show anon f_surprised_teeth a_up:
        unflip
    show jenny f_upset a_wave_off:
        xoffset 500
    with dissolve
    jenny "Get out of my way, I'm taking a shower!"

    show anon f_worried a_idle
    hide jenny
    with dissolve
    pause
    anon @ -m_talk "( Hmm, she's hiding something for sure and I'm going to find out what! )"

    hide anon with dissolve
    return

label hallway_jenny_hallway_eavesdropping:
    if store._in_replay is not None:
        $ player.location = L_home_hallway
        $ game.timer.tick(3)
    scene expression player.location.background_blur with None
    show anon f_worried
    anon @ -m_talk "..."
    anon "What's that light coming out of {b}[jen_name]{/b}'s room?"

    pause
    anon @ f_skeptical "She must be on her computer or something..."

    mans_voice "You like that don't ya, you little whore?!"

    show anon f_surprised
    jenny "Mmm, yeah I do!"

    mans_voice "Didn't I tell you to call me {b}Daddy{/b}?!"

    jenny "I'm sorry, {b}Daddy{/b}!"

    anon @ f_worried "Apa yang-"

    mans_voice "Do you think this big cock is gonna fit up your tight little asshole?!"

    jenny "Ahh, I dunno {b}Daddy{/b}..."

    anon "Does she have somebody in there?!"

    mans_voice "Well, you're about to find out... Get on your knees, bitch."

    jenny "Ngghhh, yes {b}Daddy{/b}!"

    anon "Okay, I have to peek now!"

    scene expression "backgrounds/location_home_jennybedroom_cutscene01.jpg" with dissolve
    pause
    anon "Phew, there's no guy in here..."

    anon "She's just watching porn."

    pause
    anon "!!!" with hpunch
    anon "Whoa, I didn't know {b}[jen_name]{/b} watched porn!"

    jenny "Ngghh!! Give it to me {b}Daddy{/b}!"

    jenny "Please!!!"

    anon "{i}*Snort*{/i} Dang, she's into some freaky-"

    scene expression "backgrounds/location_home_jennybedroom_cutscene02.jpg" with dissolve
    anon "!!!" with hpunch
    jenny "YA TUHAN!"

    jenny "ARE YOU SPYING ON ME AGAIN?!"

    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["01_unlocked"] = True
    $ player.go_to(L_home_hallway)
    scene expression player.location.background_blur with None
    show anon f_surprised_teeth
    show jenny f_angry a_upset:
        xoffset -80
    with dissolve
    jenny "What did I tell you!"

    anon f_surprised "I'm sorry!"

    jenny "About spying on me!"

    show jenny a_hit with dissolve
    show jenny a_hit2
    show anon b_dressed_blocking
    with dissolve
    anon "Ouch!!"

    show jenny a_hit with dissolve
    jenny "You freaking loser!"

    show jenny a_hit2 with dissolve
    pause
    show jenny a_hit with dissolve
    show anon f_unimpressed a_rub with dissolve
    anon "Would you cut it out!"

    hide jenny
    show jenny a_upset f_angry
    with dissolve
    jenny @ -m_talk "..."
    show anon b_dressed f_skeptical a_idle
    anon "Sheesh, where do you keep pulling these hair dryers from anyways?!"

    show anon f_worried
    jenny "I'm telling {b}Mom{/b}!"

    show jenny:
        flip
        xoffset 550
    with dissolve
    anon f_surprised "Apa?!"

    anon f_worried "No, no, no, please!!"

    show jenny a_crossed:
        unflip
        xoffset -80
    with dissolve
    anon "Don't tell {b}[deb_name]{/b}!"

    show anon f_surprised_teeth
    show jenny f_grin a_hips with dissolve
    pause
    jenny "One hundred bucks."

    anon f_surprised "Apa?!"

    jenny "Give me one hundred dollars or I'm telling my mom, right now!"

    anon f_worried "Dengan serius?!"

    pause
    anon f_skeptical "You're out of your mind if you think I'm gonn-"

    show jenny:
        flip
        xoffset 550
    with dissolve
    jenny "{b}Mom{/b}!"

    show anon f_tired a_facepalm with dissolve
    anon "Okay, okay, stop!"

    show anon f_sad_down with dissolve
    show jenny:
        unflip
        xoffset -80
    with dissolve
    if player.has_money(100):
        show anon f_worried a_money with dissolve
        anon "Yesus..."

        anon "{i}*Sigh*{/i} Here."

        show anon a_idle
        show jenny f_grin_down a_money_counting
        with dissolve
    else:
        if not player.has_money(1):
            show anon f_worried
        else:
            show anon f_worried a_money2 with dissolve
        anon "I don't even have one hundred."

        show jenny f_grin
        jenny "Then give me what you do have!"

        if not player.has_money(1):
            hide anon
            show player 529 at left
            with dissolve
            player_name "{i}*Sigh*{/i} Does this work?"

            show player 528
            show jenny f_upset
            jenny "sial!"

            jenny "You're pathetic..."

        else:
            show anon f_tired
            anon "{i}*Sigh*{/i} Here."

            show anon a_idle
            show jenny f_grin_down a_money_counting
            with dissolve
    pause
    hide player
    show anon f_worried
    with dissolve
    anon "So you're not gonna tell {b}[deb_name]{/b}, right?"

    if not player.has_money(1):
        show jenny f_eyeroll
    else:
        show jenny f_grin
    jenny "Not this time."

    if not player.has_money(1):
        show jenny f_angry
        jenny "Get some money, perv."

    else:
        jenny "Pleasure doing business with you, perv."

    hide jenny with dissolve
    pause
    show anon f_tired a_facepalm with dissolve
    anon @ -m_talk "( Phew, that was close! )"

    pause
    show anon a_behind_head with dissolve
    if player.has_money(1):
        anon @ -m_talk "( ... And expensive, damn it! )"

    anon @ -m_talk "( I have got to be more careful. )"

    hide anon with dissolve
    return

label hallway_jenny_in_shower:
    scene expression player.location.background_blur with None
    show anon f_surprised with dissolve
    anon @ -m_talk "(Hmm?)"

    show anon f_worried
    anon @ -m_talk "( Looks like somebody left the bathroom door cracked open... )"

    anon @ -m_talk "( I wonder who's in there? )"

    show anon f_flirt
    pause
    anon @ -m_talk "( One little peek wouldn't hurt, right? )"

    hide anon with dissolve
    return

label hallway_jenny_start:
    scene expression player.location.background_blur
    show jenny
    show anon f_worried with dissolve
    anon "Oh, uhh..."

    show jenny f_gross
    show anon f_normal a_wave with dissolve
    anon "H-hey-"

    show anon f_surprised a_idle
    show jenny f_upset
    jenny "Save it, loser!"

    anon "..."
    anon f_skeptical "Jeez, what's your problem?!"

    jenny "Tch, what do you think my problem is?!"

    jenny "... Stuck here, living with you."

    anon f_tired "{i}*Sigh*{/i} Yeah, whatever..."

    show jenny f_normal
    jenny "Shouldn't you be at school or something?"

    anon f_skeptical "Shouldn't you be out looking for a new job?!"

    show jenny f_surprised a_upset with dissolve
    jenny "!!!"
    show jenny f_upset a_crossed with dissolve
    jenny "Oh, you do not want to play this game with me, smart ass."

    anon "Hey, you're the one who started it!"

    anon @ -m_talk "..."
    show anon f_thinking a_thinking with dissolve
    anon @ -m_talk "{i}*Mengendus*{/i}"

    jenny "What are you making that face for?"

    anon @ -m_talk "{i}*Mengendus*{/i}"

    show anon a_idle f_flirt with dissolve
    anon "Something smells really good..."

    jenny "Uhh, yeah... It's the breakfast that's waiting for you {b}downstairs{/b}, dummy."

    show jenny f_eyeroll
    jenny "I can't believe {b}Mom{/b}'s still making you breakfast every day."

    show jenny f_upset
    jenny "It's been over a month since your dad died."

    anon f_worried "Yeah, well... maybe she likes doing it?"

    anon "She's a nice lady."

    jenny "Ugh, yeah. She's too nice if you ask me."

    show anon f_angry
    hide jenny with dissolve
    pause
    anon @ -m_talk "( I wonder what crawled up her butt? )"

    anon f_normal @ -m_talk "( I should get downstairs and see what smells so delicious! )"

    hide anon with dissolve
    return

label hallway_mom_sis_boobs_afterthoughts:
    scene hallway
    show anon f_tired_happy with dissolve
    anon "Wah..."

    anon "I can't believe {b}[jen_name]{/b} actually took her top off in front of me..."

    anon "Her breasts are so nice..."

    hide anon with dissolve
    return

label hallway_sis_final_started:
    scene hallway
    show anon f_surprised with dissolve
    anon @ -m_talk "..."
    anon @ -m_talk "( There are voices coming from {b}[jen_name]{/b}'s room... )"

    anon f_thinking a_thinking @ -m_talk "( It sounds like... She's talking to someone? But who... )"

    anon a_idle f_snarky @ -m_talk "( Maybe I can sneak up to her door and find out... )"

    hide anon with dissolve
    return

label hallway_mom_sleepover_offer:
    scene hallway_night
    show old_debbie 3 at right
    show player 1 at left
    with dissolve
    debbie "Hai, sayang."

    show player 17
    show old_debbie 1
    player_name "Hey, {b}[deb_name]{/b}."

    show old_debbie 2
    show player 1
    debbie "How have you been sleeping?"

    show player 10
    show old_debbie 14
    player_name "I don't sleep as easy as I used to, you know, before {b}Dad{/b} died. I'm okay though."

    show player 5
    show old_debbie 13
    debbie "You thinking about all the things that have been happening lately?"

    show old_debbie 14b
    show player 10
    player_name "Yeah, I guess... A little bit."

    show player 5
    show old_debbie 13
    debbie "I don't want you to worry about it, sweetie."

    debbie "Semuanya akan baik-baik saja, aku janji."

    show old_debbie 14
    show player 10
    player_name "How about you? You sleeping okay?"

    show player 5
    show old_debbie 13
    debbie "Tidak juga."

    show old_debbie 14
    pause
    show old_debbie 13
    debbie "... But I'm used to it. I've had trouble sleeping since my husband left many years ago."

    show player 11
    debbie "I understand what you're going through."

    show old_debbie 14b
    show player 12
    player_name "Benar-benar?"

    show player 5
    show old_debbie 13
    debbie "Yeah. I miss your dad too."

    show old_debbie 14
    pause
    show old_debbie 2
    debbie "We were friends for a long time, you know?"

    show old_debbie 1
    show player 13
    pause
    hide player
    show old_debbie 4 at center
    with dissolve
    pause
    show player 13 at left
    show old_debbie 2 at right
    with dissolve
    debbie "At least I have you now..."

    show old_debbie 1
    pause
    show old_debbie 2
    debbie "If you have any trouble sleeping again, just come visit me, okay?"

    show old_debbie 1
    show player 10
    player_name "In your bedroom?"

    show player 5
    show old_debbie 3
    debbie "Tentu!"

    show old_debbie 2
    debbie "Perhaps the company will help us both fall asleep?"

    show old_debbie 1
    show player 10
    player_name "You don't mind me sleeping in your bed?"

    show player 11
    pause
    show old_debbie 13
    debbie "I think it could do us some good..."

    show player 13
    debbie "... After everything that's happened."

    show old_debbie 14
    show player 14
    player_name "... Okay. Sure, {b}[deb_name]{/b}."

    hide player
    hide old_debbie
    with dissolve
    call popup ('scene', 'deb_sleep')
    return

label hallway_mom_movie_night_two:
    scene hallway_night
    show player 1 at left
    show old_debbie 62 at right
    debbie "Hey there, sweetie!"

    show player 2
    show old_debbie 61
    player_name "Hey {b}[deb_name]{/b}, what's up?"

    show player 1
    show old_debbie 62
    debbie "I was thinking about watching another movie."

    debbie "Mau bergabung dengan saya?"

    show player 2
    show old_debbie 61
    player_name "Of course, I'd love to!"

    show player 1
    show old_debbie 62
    debbie "Wonderful, I'll go get situated then! Come and {b}join me in the livingroom{/b} when you're ready."

    show player 2
    show old_debbie 61
    player_name "Sounds good! I'll be right down."

    hide old_debbie
    hide player
    with dissolve
    return

label anon02_next_home_hallway:
    scene expression player.location.background_blur
    show jenny f_upset a_hips:
        flip
    show anon f_worried with dissolve:
        flip
    jenny "What's going on down there?"

    anon @ -m_talk "Hmm?"

    anon "Oh, some guy was at our door demanding money."

    jenny f_surprised "Hah?!"

    jenny "What guy?"

    anon "Aku tidak tahu."

    anon "Some creepy guy with a bunch of tattoos and a crazy accent."

    jenny f_sad "Is he still down there?"

    anon "No, the cops showed up and he left."

    anon "{b}[deb_name]{/b} is down there talking to the police officer now."

    jenny "Do you think it was the same guy who's been calling her on the phone?"

    anon "Yeah, probably."

    pause
    jenny f_upset a_idle "Ugh, great."

    jenny "First your dad dies, sticking us with you..."

    jenny "... And now we're all going to be murdered."

    anon f_skeptical "Nobody is going to be murdered."

    anon "Quit being a bitch."

    jenny @ f_eyeroll "Apa pun."

    jenny "I'm going to my room."

    hide jenny
    show anon f_worried
    with dissolve
    pause
    anon f_depressed "( I don't like this one bit. )"

    anon "( {i}*Sigh*{/i} I need some air. )"

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
