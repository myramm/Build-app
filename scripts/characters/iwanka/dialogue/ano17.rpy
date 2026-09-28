label ano17_porn_iwanka:
    scene expression background(768, 400, b=.75) as stage:
        anchor (1., 400 / 768.)
        pos (1., .5)
        zoom 2
    show iwanka b_club_back
    show anon f_shy with dissolve:
        xoffset -100
    anon "Is this music okay?"
    show iwanka b_club with dissolve
    iwanka @ -m_talk "Hmm?"
    iwanka "Yeah, it's fine."
    show iwanka b_club_back with dissolve
    show anon f_flirt_low
    iwanka "Are these real fish?"
    anon "Yeah."
    iwanka "Very cool!"
    show iwanka b_club
    show anon f_shy
    with dissolve
    iwanka "I always wanted an aquarium but my mom won't let me have one."
    anon "How come?"
    iwanka @ f_eyeroll "Because she almost drowned in a koi pond when I was little."
    anon f_surprised "What?!"
    iwanka @ f_laugh "Hehe, yup!"
    anon "How did that happen?"
    iwanka f_smirk "We used to have one in the backyard of our old mansion."
    iwanka "And one night, well... She had a little too much to drink and fell in."
    anon "You're kidding!"
    iwanka @ f_laugh "Nope."
    iwanka "Apparently, the bottom was really slick with moss or something and she couldn't stand up in her high heels."
    anon f_worried "How did she get out?"
    iwanka @ f_laugh "Heh, one of the butlers had to jump in and rescue her..."
    iwanka "... It was hilarious!"
    anon "And that's the reason she won't let you have an aquarium?"
    iwanka "Yeah, that's the big reason."
    iwanka "She never really saw the appeal in having pets."
    iwanka @ f_drunk a_point "\"Just take one of the maids for a walk if you're so desperate for a pet, {b}Iwanka{/b}!\""
    show anon f_surprised_teeth
    iwanka "Which, doesn't work FYI."
    iwanka f_snob "Lupe sure did complain when I put that leash on her..."
    show erik a_glass behind iwanka:
        flip
        xoffset 50
    show anon f_shock
    with dissolve
    pause
    iwanka f_smirk @ f_laugh "... And she wasn't very good at doing tricks."
    anon f_surprised @ -m_talk "..."
    erik f_woozy "{i}*Ahem*{/i} Your drink, milady."
    show erik a_idle
    show iwanka a_glass f_laugh
    show anon f_normal
    with dissolve
    iwanka "Hehe!"
    iwanka a_glass_drink f_drink @ f_smirk a_glass_cheer "Thank you, kind sir!"
    pause
    iwanka f_drunk a_glass_empty "Mmm, these are so good!"
    iwanka "Do you like, moonlight as a bartender or something, freckles?"
    erik f_shy "Me?"
    erik "N-no, I've never tended a bar in my life..."
    iwanka "You should look into it!"
    show iwanka a_glass_empty_give with dissolve
    erik f_normal "I mean, I did spend a little bit of time leveling up my alchemy skill but that was just for an achievement."
    show iwanka f_laugh a_idle
    show erik a_glass_empty
    with dissolve
    iwanka "Heh, what?!"
    show iwanka f_drunk
    erik "I'm a bit of a completionist when it comes to {i}World of Orcette{/i}."
    iwanka @ f_disgusted "I have no idea what you're talking about."
    iwanka @ a_point "Phew, I think these drinks are starting to get to me!"
    show erik f_woozy
    anon f_worried "Maybe we should go sit down..."
    iwanka "Heh, okay."
    anon "... You can tell me more about your family."
    iwanka f_disgusted "Eww, wait... No."
    anon @ -m_talk "Hmm?"
    iwanka "I don't wanna talk about my family, they suck!"
    anon "That's-"
    iwanka f_drunk @ f_laugh "Let's dance!"
    anon f_shy "Ehh, I'm not much of a dancer..."
    show layer master:
        ease 1.6 xpos 685
    with None
    show iwanka b_club_pulling_mc:
        xoffset -690
    show anon b_empty f_surprised:
        flip
        xoffset -650
    show erik a_idle:
        unflip
        xoffset -450
    with {'master': MultipleTransition((False, Pause(.2), False, slowdissolve, True))}
    iwanka "C'mon, it'll be fun!"
    show iwanka b_club:
        flip
        xoffset -685
    show anon b_dressed f_shy:
        flip
        xoffset -885
    with {'master': dissolve}
    iwanka "If you play your cards right, I might even let you cop a feel."
    show erik f_nervous
    show anon f_surprised
    pause
    show anon f_normal behind iwanka with {'master': dissolve}:
        unflip
        xoffset -550
    iwanka "What do you say, freckles?"
    iwanka @ a_point "You wanna dance with us?"
    erik "Ehh."
    show erik a_whisper f_thinking with dissolve:
        flip
        xoffset -80
    erik "What's that, {b}Tam{/b}?"
    show erik f_worried_right
    pause
    show anon f_worried
    show iwanka f_disgusted
    erik f_thinking "Sure, I'll be right there!"
    show erik a_idle f_nervous with dissolve:
        unflip
        xoffset -450
    erik "You two go ahead, she's calling me."
    iwanka "I didn't hear anything..."
    hide erik with {'master': dissolve}
    erik "I'll get you a refill on the way back!"
    iwanka f_smirk @ f_excited "Make it a double!!"
    erik "I don't know what that means but okay!"
    iwanka "I guess it's just you and me then, huh?"
    show anon f_shy with dissolve:
        flip
        xoffset -785
    anon "Y-yeah, I guess..."
    $ M_iwanka.set('sex speed', .3)
    show iwanka b_club_dance with dissolve
    show anon f_surprised a_surprised_up_both with dissolve
    pause
    anon f_flirt_low a_sides "Whoa, you're umm..."
    anon "... Really good at this."
    iwanka @ -m_talk "Hehe!"
    pause
    show iwanka b_club with dissolve
    show anon f_shy
    iwanka "Well, what are you waiting for?"
    anon "Umm."
    anon "O-okay."
    show anon b_dressed_dance_shy with dissolve
    show iwanka f_disgusted
    pause
    iwanka f_smirk @ a_point "Wow, you do suck at this..."
    show anon b_dressed f_unimpressed with fastdissolve
    anon "I told you!"
    iwanka @ f_laugh "Hahahaah!"
    pause
    iwanka "Your problem is you're too self-conscious."
    anon f_worried @ -m_talk "Hmm?"
    iwanka "You need to relax a little."
    iwanka "Dancing is all about having fun and not worrying what other people think."
    show iwanka b_club_dance_back behind anon
    show anon f_flirt_low
    with dissolve
    pause
    iwanka @ -m_talk "See?"
    anon "Uh huh."
    pause
    iwanka @ -m_talk "It's easy."
    iwanka @ -m_talk "Just move to the music and do what feels natural."
    show anon behind iwanka
    show iwanka b_club_dance with dissolve
    anon "Uh huh."
    pause
    show iwanka b_club
    show anon f_shy a_behind_head
    with dissolve
    iwanka "C'mon, shake those hips {b}[firstname]{/b}!"
    anon "Ehh, I really think I'm better off watching..."
    iwanka "Tsk, don't be a party pooper!"
    show iwanka b_club_dance_back behind anon with dissolve
    iwanka @ -m_talk "Just shut up and dance!"
    pause
    anon "Ehh, right..."
    show anon b_dressed_dance_flirt_low with dissolve
    pause
    anon @ -m_talk "( Oh man, look at those hips go... )"
    anon b_dressed_dance_unimpressed @ -m_talk "( ... And here I am looking like an idiot. )"
    pause
    iwanka @ -m_talk "How's it going back there?"
    anon b_dressed_dance_flirt_low @ b_dressed_dance_shy_talk "Just enjoying the view."
    iwanka @ -m_talk "Hehe!"
    anon @ -m_talk "( Please don't turn around! )"
    pause
    erik "Okay, who's ready for another drink?!"
    show erik a_glass:
        unflip
        xoffset -450
    show iwanka b_club f_laugh
    show anon a_sides b_dressed behind iwanka:
        unflip
        xoffset -400
    with {'master': dissolve}
    iwanka "{i}*Gasp*{/i} Me!!"
    hide iwanka
    hide erik
    show anon b_dressed_catch_breath:
        flip
        xoffset -785
    with slowdissolve
    anon @ -m_talk "( Oh, thank goodness. )"
    anon @ -m_talk "( I'll have to thank {b}Erik{/b} for the rescue after she leaves... )"
    erik "Come sit on the couch and help me pick a board game!"
    iwanka "Board game?"
    show anon f_surprised b_dressed a_surprised_up_both with dissolve
    pause
    anon a_fists f_unimpressed "( ... And once I'm finished murdering him! )"

    scene location_erik_basement_back_couch
    show iwanka b_sidebed_right a_glass f_disgusted
    show erik b_sidebed a_orcette_figure
    with fade
    iwanka "And this game is called {i}Orcette Party{/i}?"
    erik @ -m_talk "Mhmm!"
    erik "This is Orcette right here, she's the leader of the orc faction."
    iwanka f_smirk "She's hot!"
    erik "Oh, totally!"
    erik "She's like crazy powerful too!"
    erik "You have to be at least level seventy-five before you can even issue a challenge to her."
    iwanka f_disgusted "Umm, okay..."
    show anon b_sit f_worried with dissolve:
        xoffset -250
    iwanka "... But what's an orc?"
    erik f_surprised "Huh?"
    erik f_worried "You're not serious, are you?"
    anon "{b}Erik{/b}, not everyone is into fantasy roleplaying games..."
    erik "Y-yeah, okay."
    erik f_normal "Orcs are a tribal, cave-dwelling society of green humanoids."
    iwanka f_suspicious "Humanoids?"
    erik "It means they have human characteristics."
    erik "You know, bipedal, two arms, relatively tall compared to wide..."
    iwanka f_disgusted @ -m_talk "..."
    anon f_unimpressed "He's saying they look just like us but green."
    iwanka b_sidebed_left f_normal "Oh, okay!"
    iwanka "That makes sense."
    show iwanka b_sidebed_right with {'master': dissolve}
    erik "Well, technically they have more in common with elves than humans but I suppose we don't have to get into that..."
    show iwanka a_glass_orcette f_smirk_down
    show erik a_idle
    with dissolve
    pause
    iwanka @ f_suspicious "Are her tits supposed to be real?"
    iwanka @ f_laugh "Because I can tell you from experience that it costs good money to get them to stand up like that!"
    show iwanka f_drink a_glass_drink b_sidebed_left
    show erik a_orcette_figure
    with dissolve
    erik "Ehh, they might be magically enhanced or something?"
    show iwanka a_glass f_suspicious b_sidebed_right with dissolve
    iwanka @ f_suspicious "Magically enhanced?"
    anon "You know, we really don't have to talk about this, {b}Iwanka{/b}."
    show iwanka b_sidebed_left f_normal with dissolve
    iwanka "No, it's okay."
    iwanka @ f_suspicious "It's umm... Interesting... I think."
    show iwanka b_sidebed_right a_glass_orcette
    show erik a_idle
    with dissolve
    iwanka "So can I be Orcette?"
    erik @ f_laugh "Sure!"
    iwanka @ f_suspicious_down "Does she get a sword or something?"
    erik "Actually, she uses a spear made from the bones of a giant serpent."
    iwanka @ f_laugh "Dope!"
    iwanka f_smirk "Okay, give me my spear, I wanna fuck some shit up!"
    erik "See, I knew she'd be into this!"
    anon @ -m_talk "..."
    erik "I'll go get the rest of the stuff."
    erik "{b}[firstname]{/b}, do you wanna be Ivar the Insatiable or Joxer the Well-endowed?"
    anon @ f_skeptical "Does it matter?"
    show iwanka b_sidebed_left with dissolve
    iwanka "Go with the well-endowed one, then we'll see who has the bigger spear."
    show erik f_worried
    show anon f_shy of_blush
    with {'master': dissolve}
    anon f_shy "Ehh."
    show anon -of_blush with {'master': slowdissolve}
    iwanka @ f_laugh "Hehehe!"
    show iwanka b_sidebed_right with {'master': dissolve}
    erik "No, no, no!"
    erik f_normal "Joxer doesn't use spears."
    erik "He's a bard, so he uses his lute to combat evil!"
    iwanka f_smirk @ f_laugh "Oh, a musician, even better!"
    iwanka "They are like, so hot."
    erik @ f_laugh "I'll be right back!"
    iwanka a_glass_finger "Hold up, freckles."
    show iwanka a_glass_drink f_drink b_sidebed_left with dissolve
    pause
    show iwanka a_idle f_drunk b_sidebed_right with dissolve
    iwanka @ -m_talk "Mmm!!!"
    iwanka "Hit me again!"
    erik a_thumbs "O-okay."
    hide erik
    show iwanka b_sidebed_left f_smirk
    with dissolve
    show anon f_shy
    pause
    anon "So..."
    iwanka f_drunk "Can I tell you a secret, {b}[firstname]{/b}?"
    anon "S-sure?"
    iwanka "I am like, super wasted right now."
    anon f_worried "Yeah, I can see that."
    iwanka @ f_laugh "Hehehe!"
    anon f_shy "Do you drink like this at your parents' parties?"
    iwanka @ f_eyeroll "Ugh, if only..."
    iwanka "... They don't allow me to drink during their parties."
    iwanka @ f_bored "In fact, I don't think I've been this drunk since I left college."
    anon "Oh?"
    iwanka "Yeah."
    iwanka "It was so much fun there!"
    iwanka f_sad "I wish I could go back."
    pause
    iwanka f_drunk "Oh em gee, this one time, freshman year..."
    iwanka "... We were driving around in my friend Damian's party limousine and I got like, totally hammered on jello shots, right?"
    anon f_worried "Uh huh."
    iwanka "And my other friend Macy was like, \"We should totally grind on that stripper pole together!\""
    iwanka "Which sounded super fun... But we were so wasted, we just ended up in a tangled mess on the floor!"
    iwanka @ f_laugh "Hahahaah!"
    anon f_tired "Uh huh."
    iwanka "She was all, \"Oh em gee, why are you such a stupid drunk bitch?\""
    iwanka "And I was like, \"Tsk, you're the one who can't stand up!\""
    anon @ -m_talk "..."
    iwanka @ f_laugh "Then we made out while everyone in the limo watched."
    anon "Uh huh."
    pause
    anon f_surprised "Wait-"
    anon "What was that last part?"
    iwanka "Then she went down on me."
    anon f_shock "..."
    iwanka @ a_shrug "Yeah, I get kinda slutty when I drink."
    anon f_shy "Then what happened?"
    iwanka "I puked in her purse."
    anon f_disgusted @ -m_talk "!!!"
    iwanka "And that's not a metaphor, I really puked in her eleven-hundred-dollar Vispucci purse."
    iwanka @ f_laugh "She was maaaad!"
    anon "Y-yeah, I can imagine."
    iwanka "It was fun though!"
    iwanka f_annoyed "Until my dad's staff found the video online."
    anon f_shy "Oh?"
    iwanka "He made me come home and spend the rest of spring break at this island resort with my mother..."
    anon "That doesn't sound so bad to me."
    iwanka f_disgusted "Ugh, that's because you don't know my mother..."
    anon "That's true."
    iwanka "... All she did the entire trip was complain about my dad!"
    pause
    iwanka "Oh, and screw the cabana boy!"
    anon @ f_surprised "!!!"
    iwanka @ f_eyeroll "I swear, there's not enough therapy in the world to help me get over the things I heard coming out of her hotel room!"
    anon "Do your father and her fight a lot?"
    iwanka f_suspicious @ -m_talk "Hmm?"
    iwanka "Umm, I guess..."
    anon "What do they fight about?"
    iwanka "Tsk, why are you so interested in my parents?"
    anon f_worried "Am I?"
    iwanka "You keep asking about them, like, every five minutes!"
    anon "I'm sorry, I don't mean to-"
    iwanka f_annoyed "Do you think I'm ugly or something?"
    anon "N-no, of course not!"
    anon "I'm just... Umm..."
    anon f_shy "... Trying to learn more about you..."
    show iwanka f_suspicious
    pause
    anon "... Because I like you so much!"
    iwanka f_drunk "Aww, really?!"
    anon "Yes?"
    iwanka @ f_laugh "You are so sweet, {b}[firstname]{/b}!"
    anon @ f_grin -m_talk "Mhmm."
    iwanka "I think we should like, totally hang out again sometime!"
    anon "Yeah, definitely."
    pause
    anon "Maybe you could invite me over to your place?"
    iwanka f_annoyed "Ehh, no..."
    anon f_worried "No?"
    iwanka "Well, it's kinda embarrassing but..."
    iwanka "... My dad doesn't really let me invite boys over."
    anon "Really?"
    iwanka "Yeah, it's been a rule since I was thirteen."
    anon f_confused "But you're a grown woman..."
    iwanka @ f_drunk "I know, right?!"
    iwanka "It's so ridiculous!"
    anon f_worried "Is there a way I could sneak in or something?"
    iwanka f_smirk "You wanna try and sneak into my father's estate?"
    anon f_shy "If it means I get to see you, sure!"
    iwanka f_drunk @ f_laugh "Aww!!"
    anon "Bad idea?"
    iwanka @ a_shrug "Well, not if you enjoy getting tasered in the nuts..."
    anon @ f_surprised_teeth "!!!"
    anon "{i}*Ahem*{/i} I do not."
    iwanka @ f_laugh "Hehe!"
    anon "Any other ideas?"
    iwanka f_thinking "Well, there is one thing that might work..."
    anon f_normal "Oh?"
    iwanka f_smirk "... You wanna know?"
    anon f_shy "I do."
    iwanka "You {i}really{/i} wanna know?"
    anon "Yes, please!"
    iwanka f_drunk "It's simple."
    iwanka "All you have to do is-"
    erik "I'm baaaack!"
    show iwanka b_sidebed_right
    anon f_hurt @ f_surprised "!!!" with hpunch
    show erik b_sidebed a_glass f_woozy with dissolve
    erik "Did you miss me?"
    anon "( Nooooo!!! )"
    iwanka @ f_laugh "Oh, is that my drink?"
    erik "It sure is, milady."
    show anon f_unimpressed
    iwanka "Gimme, gimme!"
    show iwanka a_glass
    show erik a_box
    with dissolve
    erik "Okay, so it might take a while to get through all the rules..."
    show iwanka a_glass_drink f_drink b_sidebed_left with dissolve
    pause
    show iwanka a_glass f_drunk b_sidebed_right with dissolve
    erik f_worried "... And a couple of the game pieces are a bit... Umm, sticky."
    anon f_worried "{i}*Sigh*{/i} Of course they are..."
    erik f_normal "It's nothing to worry about though."
    erik "Just something that happens to action figures over time."
    anon f_angry "{b}Erik{/b}, we are in the middle of a conversation!"
    erik f_worried "O-oh?"
    anon f_shy "What were you saying, {b}Iwanka{/b}?"
    iwanka b_sidebed_left @ f_laugh "I wanna dance some more!"
    anon f_worried "Huh?"
    hide iwanka with dissolve
    anon "But what about-"
    pause
    anon f_angry "Damnit, {b}Erik{/b}!!"
    erik "I thought we were gonna play?"
    anon "Nobody wants to play board games!"
    erik f_sad "I'm sorry, {b}[firstname]{/b}... I-"
    iwanka "Are you guys coming?!"
    anon f_tired @ f_worried_forward "Yeah, just a second."
    anon "Dude, she was just about to tell me how to get inside the estate!"
    erik f_angry "Well, I didn't know that..."
    erik "I'm just trying to help!"
    anon "{i}*Sigh*{/i} You just screwed me so hard!"
    erik "I said I'm sorry!"
    iwanka "Ahhh!!!"
    "{i}*Crash*{/i}" with hpunch
    show anon f_surprised_low
    show erik f_surprised_down a_idle with dissolve:
        flip
        xoffset 550
    erik "Oh, crap!"
    hide anon with dissolve
    anon "{b}Iwanka{/b}!!!"

    scene location_erik_basement_back_floor with fade
    iwanka "Pffft, hahahaah!!"
    anon "Are you alright?!"
    iwanka "I think I had an oopsie."
    anon "Yeah, you did."
    iwanka "I am so wasted right now!!"
    iwanka "Hahahaah!"
    pause
    anon "Let me help you up..."
    show iwanka_face_f_floor_surprised
    iwanka "Hmm?"
    hide iwanka_face_f_floor_surprised
    iwanka "What are these?"
    show iwanka_face_f_floor_surprised
    erik "Ehh, those are nothing!"
    erik "Don't look at-"
    hide iwanka_face_f_floor_surprised
    iwanka "{i}Warcocks{/i}?"
    erik "!!!"

    scene expression background(424, 400, 2.) as stage
    show erik f_worried:
        flip
        xoffset 100
    show anon f_worried:
        xoffset -100
    with fade
    iwanka "{i}Elves Gone Wild{/i}?"
    erik "One of my guildmates left those here..."
    anon "You're not hurt, are you?"
    show iwanka b_club f_disgusted a_dvd_show with dissolve:
        xoffset 50
    iwanka "{i}The Fisherman's Daughter{/i}?"
    iwanka a_dvd "Are these porn DVDs?"
    erik "N-no..."
    iwanka "This one is animated!"
    erik "Yeah, it's called hentai."
    show iwanka f_suspicious
    show anon f_confused
    pause
    erik f_nervous @ f_worried_right "I mean, that's what I've been told..."
    erik "... By people who watch that stuff..."
    pause
    erik f_sad_down "... People, not me."
    iwanka @ -m_talk "Mhmm."
    iwanka f_smirk_down "\"Kano the fisherman and his family have always held a deep love for the sea... But for his voluptuous daughter Hamako, that love goes both ways!\""
    iwanka "\"Can her great lust for the denizens of the deep ever be satiated?\""
    iwanka "\"Does her depravity know no bounds?!\""
    anon f_surprised "Dude, is that tentacle porn?"
    erik @ f_worried_right "It's not mine, I swear!"
    iwanka f_suspicious "So she like, has sex with fish or something?"
    erik @ -m_talk "..."
    iwanka f_drunk @ f_laugh "Oh em gee, can we watch it?!"
    show erik f_surprised m_talk
    anon f_surprised "WHAT?!"
    erik -m_talk "!!!"
    iwanka "I wanna see her fuck the fish!"
    erik f_normal @ f_eyeroll "Tsk, she doesn't fuck a fish..."
    anon f_worried "I thought you said you've never seen it!"
    show erik f_nervous with {'master': dissolve}:
        unflip
        xoffset -350
    erik "Well, obviously I lied!"
    erik "{i}*Sigh*{/i} She fucks an octopus..."
    pause
    show erik f_sad_down with dissolve:
        flip
        xoffset 100
    erik "... Then a squid."
    show anon f_hurt a_facepalm with dissolve
    pause
    erik f_woozy "Then both."
    iwanka @ f_laugh "Oh, we are so watching this!!"
    show anon f_surprised a_sides with dissolve
    erik f_worried "You're serious?"
    iwanka "Yes, hurry up!"
    show erik a_dvd
    show iwanka a_idle
    with dissolve
    erik f_normal "A-alright."
    hide erik with dissolve
    anon f_worried "You really wanna watch a woman have sex with a squid?"
    iwanka "And an octopus!"
    anon f_tired -m_talk "..."
    iwanka f_suspicious "Don't make it weird, {b}[firstname]{/b}."
    hide iwanka
    show anon f_surprised:
        flip
        xoffset -550
    with {'master': dissolve}
    iwanka "Come sit with me!"
    anon f_eyeroll "Yeah, I'm the one making it weird."
    hide anon with dissolve

    scene location_erik_basement_back_couch
    show iwanka b_sidebed_right_shy f_drunk
    with fade
    show anon b_sit f_worried behind iwanka with {'master': dissolve}:
        xoffset -250
    anon "This had better not awaken something in me..."
    show iwanka b_sidebed_left_shy f_laugh with dissolve
    iwanka "Hah, relax!"
    iwanka f_drunk "With a premise like this, it's sure to be cheesy and humorous."
    show erik b_sidebed with dissolve
    show iwanka b_sidebed_right_shy
    erik "You're wrong."
    erik "It's actually very well written and quite erotic."
    iwanka @ f_laugh "You are so full of it!"
    erik "I'm serious!"
    show anon f_tired
    iwanka "Shh!!"
    iwanka "It's starting."
    show erik behind iwanka with dissolve:
        flip
        xoffset 550
    pause
    iwanka f_suspicious @ f_disgusted "What the-"
    iwanka "Is this all in Japanese?"
    erik "Yeah, you have to read the subtitles."
    iwanka f_disgusted "Seriously?"
    iwanka "If I wanted to read, I'd get a book!"
    iwanka f_drunk "Just tell me what happens and skip to the juicy part."
    erik f_worried_right "Really?"
    iwanka "I wanna see her get fucked by tentacles!"
    show anon f_surprised_teeth
    erik "Okay, okay..."
    show anon f_tired
    hide erik
    with dissolve
    pause
    erik "Basically, her father is a fisherman and one day a baby octopus gets caught in his net."
    show anon f_tired with {'master': dissolve}
    erik "He brings it home, intent on turning it into tako; but Hamako stops him because it's so cute."
    iwanka @ f_laugh "Aww, I wanna see the baby!"
    erik "Hold on."
    pause
    erik "There."
    show anon f_tired_happy
    iwanka "Oh em gee, it's adorable!!!"
    show iwanka b_sidebed_left_shy with dissolve
    iwanka "Look at its sad little eyes!!!"
    show iwanka b_sidebed_right_shy with dissolve
    anon "Uh huh."
    show anon f_tired
    iwanka "Okay, then what happens!"
    erik "Well, Hamako begs her father to let her keep the baby octopus as a pet..."
    erik "... And over the years, it grows really large."
    erik "So large in fact, that she has to release him back into the ocean."
    iwanka f_pouting "Aww, that's sad!"
    label ano17_porn_iwanka.replay:
    erik "But he comes back every night and waits at the dock for her to visit him."
    erik "Then, well..."
    erik "... You'll see."
    iwanka f_smirk @ f_laugh "Go, go, go!"
    show erik b_sidebed behind iwanka with dissolve:
        flip
        xoffset 550
    pause
    iwanka "Okay, so it's hugging her..."
    pause

    scene location_erik_basement_back_hentai_pre with fade
    iwanka "Whoa, look at all those tentacles!"
    pause
    iwanka "That seems like it would tickle..."
    pause

    scene location_erik_basement_back_couch
    show anon b_sit f_skeptical:
        xoffset -250
    show erik b_sidebed f_woozy o_boner:
        flip
        xoffset 550
    show iwanka b_sidebed_right_shy f_smirk
    with fade
    anon f_tired @ f_skeptical "Pretty sure clothes don't just explode like that..."
    iwanka "Shh!!"
    pause
    iwanka @ f_suspicious "How do you have sex with an octopus anyways?"
    erik "They have sex glands on their tentacles."
    iwanka "They do?"
    erik "Well, in the movie at least."
    pause
    show iwanka f_concerned
    pause
    iwanka "There is no way that's going to fit inside-"
    show anon f_surprised_down o_sit_boner with {'master': dissolve}
    iwanka f_surprised "Oh, never mind... There it goes."

    $ M_iwanka.set('sex speed', 1 / 12.)

    scene location_erik_basement_back_hentai_sex
    show iwanka_sex_hentai
    with fade
    iwanka "Wow, in her ass too, huh?"
    erik "Well, just the one for now."
    iwanka "One is plenty, trust me..."
    iwanka "... And look how thick they are!"
    pause

    scene location_erik_basement_back_couch
    show anon b_sit f_worried o_sit_boner:
        xoffset -250
    show erik b_sidebed f_woozy o_boner:
        flip
        xoffset 550
    show iwanka b_sidebed_right_shy f_suspicious
    with fade
    iwanka "What's that blue stuff?"
    erik "Sperm."
    iwanka f_surprised "Holy crap, that's a lot of sperm!"
    pause
    iwanka f_annoyed "She can't swallow all that!"
    show anon f_shy
    erik "No, but she sure does try..."
    pause

    scene location_erik_basement_back_hentai_sex
    show iwanka_sex_hentai_cum
    with fade
    iwanka "This is umm... a little intense."
    iwanka "She's just like, a helpless fuck doll for this creature..."
    erik "Yeah, pretty much."
    pause
    iwanka "... It's kinda hot."
    pause

    scene location_erik_basement_back_couch
    show anon b_sit f_shy o_sit_boner:
        xoffset -250
    show erik b_sidebed f_woozy o_boner:
        flip
        xoffset 550
    show iwanka b_sidebed_right_shy f_smirk
    with fade
    pause
    show iwanka b_sidebed_left_shy with dissolve
    pause .4
    show iwanka f_smirk_down
    show anon of_blush
    with dissolve
    pause
    show iwanka b_sidebed_right_shy f_lipbite with dissolve
    pause
    show iwanka f_drunk a_rub with dissolve
    pause

    scene location_erik_basement_back_hentai_sex
    show iwanka_sex_hentai_cum
    with fade
    iwanka "Oh em gee!"
    iwanka "Look at all that cum it's pumping into her pussy..."
    iwanka "... It's spurting out of her!"
    pause

    scene location_erik_basement_back_couch
    show anon b_sit f_shy o_sit_boner:
        xoffset -250
    show erik b_sidebed f_woozy o_boner:
        flip
        xoffset 550
    show iwanka a_rub b_sidebed_right_shy f_drunk
    with fade
    iwanka @ f_content_closed -m_talk "Mmm."
    anon f_surprised_low "!!!"
    anon @ -m_talk "( Is she... Masturbating? )"
    show anon f_flirt_low
    pause
    iwanka "How many tentacles are going to fit in there?!"
    erik "Oh, this is nothing."
    erik "Just wait until you see the threesome scene with the squid..."
    iwanka "Nghh, I don't think I'm gonna last that long!"
    pause

    python:
        renpy.end_replay()
        unlock_scene('iwanka', '03_unlocked')

    show iwanka a_touch b_sidebed_left_shy
    show anon f_surprised_down o_empty
    with dissolve
    anon "!!!"
    anon @ f_surprised "W-whoa, what are you doing?!"
    show erik b_sidebed f_worried with dissolve:
        unflip
        xoffset 0
    iwanka "Isn't it obvious?"
    show anon o_sit_boner
    show erik f_surprised
    show iwanka b_kneeling a_idle:
        xoffset -146
    with dissolve
    iwanka "This is making me horny as hell, {b}[firstname]{/b}!"
    erik @ f_surprised_down "Holy crap, dude!"
    iwanka "Can I see it?"
    anon "Oh, I dunno..."
    iwanka "Mmm, please?"
    anon "{b}Erik{/b} is sitting right there!"
    iwanka "He won't mind..."
    iwanka "You won't mind, will you, freckles?"
    show anon f_surprised
    show erik a_thumbs f_laugh with dissolve
    pause
    show erik f_woozy a_idle with dissolve
    iwanka "See."
    show anon b_sit_back f_flirt_low
    show iwanka a_undress1
    with dissolve
    anon "This escalated very quickly..."
    show anon b_sit_back_shirt o_empty od_empty
    show iwanka a_undress2
    with dissolve
    iwanka "Hehe!"
    show iwanka a_undress3 with dissolve
    show iwanka a_undress4 with dissolve
    anon "Oh, man..."
    erik @ f_laugh "Greatest... Party... EVER!"
    erik a_phone "This is so going on my guild's message board!"

    call scene_iwanka_blowjob
    $ unlock_scene('iwanka', '01_unlocked', variant='basement')

    scene location_erik_basement_back_couch
    show anon b_sit f_shy:
        xoffset -250
    show iwanka b_sidebed_left f_drunk o_cum
    show erik b_sidebed f_woozy
    with fade
    iwanka "That was fun!"
    anon "Y-yeah, it was."
    show iwanka b_sidebed_right with dissolve
    iwanka "Can I get a towel or something?"
    erik @ -m_talk "Hmm?"
    erik "Oh, sure!"
    hide erik with dissolve
    pause
    show iwanka b_sidebed_left with dissolve
    iwanka "Now that I've taken care of you, maybe you can return the favor?"
    anon f_flirt "Uhh, yeah... I suppose I could."
    iwanka "Excellent."
    show iwanka b_sidebed_left_shy with dissolve
    iwanka "Just be careful because with all this excitement, it's like a tropical storm down there!"
    "{i}*Brrriiiing*{/i}"
    anon @ f_confused "What is that?"
    "{i}*Brrriiiing*{/i}"
    iwanka f_annoyed "Ugh, it's my stupid phone..."
    show iwanka b_sidebed_left with dissolve
    iwanka "... Hold on."
    iwanka a_phone f_suspicious_down "Aww, man... It's my dad."
    show anon f_worried
    iwanka a_phone_talk f_annoyed "Hello?"
    pause
    iwanka "I'm at a friend's house."
    pause
    iwanka "Umm, because you were busy disciplining the maid?"
    pause
    iwanka "{b}Dad{/b}, I'm twenty-seven..."
    pause
    iwanka "So I can take care of myself!"
    pause
    iwanka "Yes, for your information, my friend is a boy."
    pause
    iwanka "No, we're not having sex!"
    iwanka @ f_eyeroll "Jesus!"
    show iwanka f_drunk
    pause
    iwanka f_annoyed "I'll be home in a little while."
    pause
    iwanka "Can't it wait?"
    pause
    iwanka "Grr, I'm really getting sick of this!"
    pause
    iwanka "Hello?"
    iwanka a_phone @ f_suspicious_down "Asshole!"
    anon "What's going on?"
    iwanka f_sad "{i}*Sigh*{/i} I have to go..."
    anon "What, right now?"
    iwanka "Yes."
    iwanka "My dad sent a car to collect me."
    anon "Huh?"
    anon "How do they know where you are?"
    iwanka "They track my phone."
    pause
    anon "Well, can I see you again?"
    iwanka f_surprised "You were serious about that?"
    anon "Umm, yeah?"
    iwanka f_drunk "Huh."
    anon "You were gonna tell me how to sneak in to your dad's estate so we could hang out, remember?"
    iwanka "Heh, you don't have to sneak in..."
    anon @ f_confused "I don't?"
    iwanka "No."
    iwanka "Just tell the guard at the front gate that you have an appointment with me..."
    iwanka "... And when he asks for what purpose, tell him it's to interview as my new assistant."
    anon "Your assistant, seriously?"
    iwanka "Do you wanna come see me or not?"
    anon f_shy "Of course."
    iwanka "Well, that's the only way you're getting inside."
    iwanka "Just act confident and you'll be fine."
    anon "O-okay."
    iwanka a_idle f_eyeroll "Ugh, things were just getting fun too."
    hide iwanka with dissolve
    pause
    erik "Here's your towe-"
    erik "W-wait, where are you going?"
    iwanka "My dad sent a car to pick me up."
    erik "Oh."
    iwanka "Thanks for the party."
    erik "Y-yeah, no problem."
    erik "Hold up!"
    iwanka "Hmm?"
    erik "You might wanna wipe your face off."
    show anon f_laugh
    iwanka "Oh, right."
    show anon f_shy
    pause
    iwanka "Thanks."
    pause
    show erik b_sidebed f_woozy with dissolve
    pause
    erik "So..."
    erik "... Was that awesome or what?!"
    anon f_normal @ f_flirt "Yeah, it kinda was."
    erik "It's too bad you didn't get the info you wanted but a blowjob from {b}Iwanka Rump{/b} is a pretty good consolation prize!"
    anon @ f_laugh "Actually, she did give me a way inside the mayor's estate before she left."
    erik f_normal "Oh, really?"
    anon "Yup."
    erik "Cool beans, dude!"
    erik "I guess tonight was a huge success then, huh?"
    anon "Surprisingly, yes."
    erik "Good."
    pause
    erik a_phone @ f_laugh "So, can I go upload this video now?"
    anon "Heh, yes, go ahead."
    erik "Awesome!"
    hide erik with dissolve
    erik "This is totally gonna max my popularity stat with my guild!"
    show anon f_laugh
    pause
    anon f_normal @ -m_talk "( I really thought this night was going to be a disaster... )"
    anon @ f_flirt -m_talk "( ... But things worked out in the end. )"
    anon @ f_laugh -m_talk "( Now, the next step is {b}infiltrating Mayor Rump's mansion{/b}! )"
    anon @ -m_talk "( I should {b}speak with his security{/b} tomorrow and see if {b}Iwanka{/b}'s info is good. )"
    hide anon with dissolve

    scene black with slowdissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
