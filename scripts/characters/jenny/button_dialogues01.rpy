label button_jenny_eve_party_speak_to_jenny:
    scene expression player.location.background_closeup with None
    show jane b_dance:
        flip
    with dissolve
    random_girl "Wooo!"
    random_guy "Damn, bro... These chicks are hot as hell!"
    jenny "Hahaha!"
    show anon f_confused with dissolve
    anon "{b}[jen_name]{/b}?"
    jenny "Hmm?"
    hide jane
    show jenny b_casual a_sides:
        xoffset 50
    show jane:
        xoffset -250
    with dissolve
    show anon f_worried
    if M_jenny.finished_inclusive(S_jenny_cheerleader_sex):
        show jenny f_surprised
        jane "Isn't that your roommate?"
        jenny f_upset "Y-yeah."
        jenny "What are you doing here, {b}[firstname]{/b}?"
        anon "My friend lives here and she invited me."
        jane "You're friends with {b}Grace{/b}?"
        anon "Yeah."
        anon "Err, well, kinda..."
        anon "I'm friends with her little sister."
        jane "Oh, yeah!"
        jane "You both came by the library the other day to hang those flyers, didn't you?"
        jenny @ f_eyeroll "What are you, banging her too?"
        anon f_sad_down "N-no."
        pause
        anon f_worried "I mean, we are kinda dating... I think..."
        anon "... But we haven't done anything like that!"
        show jane a_thinking f_sad:
            flip
            xoffset 300
        with dissolve
        jane "Are you jealous?"
        show jane f_normal
        jenny f_surprised "W-what?!"
        jenny f_upset @ f_eyeroll "Of course I'm not jealous!"
        jane f_sexy a_idle "Oh my god, you ARE jealous!"
        jenny f_angry a_crossed "Why should I care who my loser roommate dates?!"
        jane "I don't know but you clearly do."
        jenny "Shut up!"
        jane @ f_laugh "Hahaha!"
        jane "Spill it."
        jenny @ f_eyeroll "I'm leaving."
        jane f_sad "What?!"
        hide jenny with dissolve
        jane "Y-you're leaving?!"
        jenny "This party blows!"
        jane "{b}[jen_name]{/b}, hold up!"
        hide jane with dissolve
        anon @ -m_talk "( Huh. That was weird... )"
        anon @ -m_talk "( Oh well, best forget it. )"
        anon a_thinking f_thinking @ -m_talk "( {b}Grace{/b} said {b}Odette{/b} should be up here somewhere... )"
        hide anon with dissolve
    else:
        show jenny f_gross
        jane "Isn't that your roommate?"
        jenny "Tch, what are you doing here?"
        anon "My friend lives here and she invited me."
        jane "You're friends with {b}Grace{/b}?"
        anon "Yeah."
        anon @ a_behind_head "Err, well, kinda..."
        anon "I'm friends with her little sister."
        jane "Oh, yeah!"
        jane "You both came by the library the other day to hang those flyers, didn't you?"
        jenny @ f_eyeroll "Oh my god, YAWN!"
        show jenny f_angry
        pause
        jenny "Would you get lost, {b}[firstname]{/b}?!"
        jenny "We're trying to dance."
        anon @ f_surprised "Seriously?"
        jane "Haha, damn {b}[jen_name]{/b}..."
        jane "That's kinda harsh, don't you think?"
        jenny f_upset "Look, you said there would be hot, rich guys at this party and that's the only reason I came."
        jenny "Instead, it's just a bunch of fugly poor dudes and my loser roommate!"
        jane f_sexy a_thinking "I dunno, I think he's kinda cute..."
        jenny @ f_eyeroll "Eugh, you did not just say that?!"
        show jane f_normal a_idle:
            flip
            xoffset 300
        with dissolve
        jane "What?!"
        jenny "I'm outta here!"
        hide jenny with dissolve
        jane f_sad "Y-you're leaving?!"
        jenny "This party blows!"
        jane "{b}[jen_name]{/b}, hold up!"
        hide jane with dissolve
        anon @ -m_talk "( Sheesh, what crawled up her butt? )"
        anon @ -m_talk "( Oh well, best forget it. )"
        anon f_thinking a_thinking @ -m_talk "( {b}Grace{/b} said {b}Odette{/b} should be up here somewhere... )"
        hide anon with dissolve
    return

label jenny_button_gf_experience_stay_in:
    anon f_normal "Stay in."
    show jenny f_normal
    jenny "You seriously just wanna hang out around here?"
    anon f_worried "Bad idea?"
    jenny "Sounds a bit boring..."
    jenny f_grin "... But at least I won't have to worry about anyone seeing us together."
    anon "I'm pretty sure nobody would care, {b}[jen_name]{/b}..."
    jenny "Yeah, whatever."
    pause
    jenny @ -m_talk "Hmm."
    hide anon
    show jenny b_dressed_pulling1
    with dissolve
    jenny "Come with me."
    show jenny b_dressed_pulling2
    anon "W-where are we going?"
    hide jenny with dissolve
    jenny "Downstairs."
    scene black with fade
    pause
    scene expression "backgrounds/location_home_livingroom_couch08.jpg" with None
    show expression "backgrounds/location_home_livingroom_couch08b.png" with None
    show jenny b_front_undies a_lap f_front_left
    show anon b_front f_front_right zorder 1
    with dissolve
    if M_diane.finished_state(S_diane_barn_news):
        jenny "I guess {b}Diane{/b} is working late."
        jenny "Lucky us, we have the couch to ourselves."
    else:
        jenny "Looks like {b}[deb_name]{/b} is sleeping."
        jenny "Lucky us, we have the couch to ourselves."
    show jenny f_front_forward a_remote with dissolve
    if M_jenny.get("jenny_girlfriend_first_time"):
        anon "So what are we doing?"
        show jenny f_front_forward
        jenny "You said you wanted to hang out, didn't you?"
        anon "Yeah."
        anon "You wanna watch a kung fu movie?"
        show jenny f_front_left
        jenny "I hope you're joking..."
        anon f_front_shy_right "You don't like kung fu?"
        jenny "Heh, no girl likes kung fu, doofus..."
        anon "That's not true!"
        show jenny f_front_eyeroll a_down with dissolve
        jenny "Trust me."
        jenny "It's true."
        show jenny f_front_forward
        pause
        show jenny f_front_left
        jenny "What are you doing?!"
        anon f_front_right "I thought it would be nice to hold your hand..."
        jenny "... You wanna hold my hand?"
        anon f_front_shy_right "Yes?"
        jenny "What are you, twelve years old?!"
        anon @ f_front_surprised_right -m_talk "..."
        anon "Alright, whatever."
        anon "Just forget it."
        jenny @ f_front_eyeroll "{i}*Sigh*{/i} No, I'm sorry."
        jenny "I'm not very good at this whole girlfriend thing..."
        show anon a_hold_hands
        show jenny a_empty
        with dissolve
        jenny "There."
        show anon f_front_right
        pause
        jenny "Happy now?"
        anon "Yes."
        show anon a_down
        show jenny f_front_forward a_remote
        with dissolve
        pause
        show anon f_front_forward
        jenny "Oh, here we go!"
        show anon a_hold_hands
        show jenny a_empty
        with dissolve
        anon @ -m_talk "..."
        anon "What is this?"
        jenny "It's this old sitcom called {i}Pals{/i}."
        jenny "{b}[deb_name]{/b} and I used to watch it all the time when I was little."
        anon "What's it about?"
        jenny "A group of six friends living in Manhattan."
        anon "Sounds boring."
        jenny @ f_front_laugh "No, it's really funny!"
        anon f_front_right "You know, since I'm the one paying money for this... Don't you think I should control the remote?"
        show jenny f_front_laugh
        jenny "Okay, you've definitely never had a girlfriend before..."
        anon @ -m_talk "..."
        jenny "Haha!"
        show jenny f_front_left
        anon "You're supposed to be nice, remember?"
        jenny "Yeah, yeah... Okay!"
        show jenny b_front_cuddle a_empty f_front_cuddle_look zorder 2
        show anon f_front_surprised_right a_down
        with dissolve
        anon "!!!"
        show jenny f_front_cuddle_look_up
        jenny "Just shut up and watch, {b}[firstname]{/b}."
        jenny "It's really funny, you'll see."
        show jenny f_front_cuddle_look
        anon f_front_forward "O-okay..."
        pause
        jenny @ f_front_cuddle_look_up "Oh, this is the one where Matt puts the thanksgiving turkey on his head!"
        anon "What?"
        anon "Why would someone put a turkey on their head?"
        jenny @ f_front_cuddle_look_up "He's trying to scare his roommate!"
        show jenny f_front_cuddle_look
        pause
        anon "Whoa, who's that?!"
        jenny @ f_front_cuddle_look_up "Oh, her?"
        jenny @ f_front_cuddle_look_up "That's Courtney and you probably think she's super hot, big surprise..."
        anon "I mean, she is pretty..."
        anon f_front_right_low "Not as pretty as you though."
        show anon f_front_forward
        jenny @ f_front_cuddle_look_up "Oh, barf!"
        jenny @ f_front_cuddle_look_up "You say the dorkiest things sometimes..."
        anon f_front_gross_down "Sorry."
        jenny @ -m_talk "..."
        jenny @ f_front_cuddle_look_up "No, it's okay."
        show anon f_front_low
        pause
        jenny @ f_front_cuddle_look_up "Thanks, {b}[firstname]{/b}."
        anon f_front_right_low "You're welcome."
        show anon f_front_forward
        pause
        anon @ f_front_forward_laugh "Hahaha!"
        pause
        anon "Okay, you were right."
        anon "That is pretty funny!"
        show jenny f_front_cuddle_look_up
        jenny "Hehe, I told you!"
        show jenny f_front_cuddle_look
        anon "How come I don't remember you and {b}[deb_name]{/b} watching this?"
        show jenny f_front_cuddle_look_up
        jenny "Probably because you were always off doing things with your dad..."
        anon "Yeah, I guess that makes sense."
        jenny "It's one of those shows that is more fun to watch with other people."
        show jenny f_front_cuddle_look
        anon "I can see that."
        show jenny f_front_cuddle_look_up with None
        show anon a_empty
        show expression "characters/anon/anon_arms_front_a_cuddle.png" zorder 2
        with dissolve
        pause
        jenny "This is nice."
        anon "Yeah, it is."
        pause
        hide anon
        show jenny b_front_kiss
        hide expression "characters/anon/anon_arms_front_a_cuddle.png"
        with dissolve
        anon "!!!"
        pause
        show anon b_front_kiss_talk f_front_kiss
        show jenny b_front_kiss_talk f_front_kiss
        with dissolve
        anon "W-what was that for?"
        jenny "No reason."
        jenny "I just felt like it."
        anon "Heh, well, do you feel like doing a bit more?"
        jenny "Maaaybe..."
        hide anon
        show jenny b_front_kiss
        with dissolve
        jenny "Mmm."
        pause
        scene black with fade
        pause
        scene expression "backgrounds/location_home_livingroom_couch08.jpg"
        show expression "backgrounds/location_home_livingroom_couch08b.png"
        show anon b_front a_empty f_front_forward
        show jenny b_front_cuddle f_front_cuddle_look
        show expression "characters/anon/anon_arms_front_a_cuddle.png"
        with fade
        pause
        show jenny f_front_cuddle_look_up
        jenny "Alright, I'm getting sleepy..."
        show jenny b_front_undies a_lap f_front_left
        show anon a_down
        hide expression "characters/anon/anon_arms_front_a_cuddle.png"
        with dissolve
        anon f_front_right @ -m_talk "Hmm?"
        anon "That's okay, you can sleep if you want."
        anon "I'm interested to see what comes next."
        show jenny a_remote f_front_forward with dissolve
        jenny "Heh, we've already watched three episodes..."
        show jenny f_front_left
        jenny "... And besides, I'm your girlfriend, remember?"
        anon "Yeah?"
        jenny "So your girlfriend is telling you it's time for bed!"
        jenny "Let's go!"
        hide jenny with dissolve
        anon "Okay, okay..."
        jenny "Hehehe!"
        anon "( She took off in a hurry... )"
        anon "( I should {b}hurry upstairs after her{/b}. )"
        hide anon with dissolve
    else:
        anon "So are we watching {i}Pals{/i} again?"
        anon "I liked that show."
        show anon a_hold_hands
        show jenny f_front_left a_empty
        with dissolve
        jenny "Well, we definitely aren't watching kung fu movies..."
        show anon f_front_forward
        show jenny f_front_forward
        pause
        jenny "There we go."
        show jenny b_front_cuddle f_front_cuddle_look zorder 2
        show anon f_front_low a_down
        with dissolve
        anon @ -m_talk "!!!"
        show anon f_front_forward a_empty
        show expression "characters/anon/anon_arms_front_a_cuddle.png" zorder 3
        with dissolve
        pause
        show jenny f_front_cuddle_look_up
        jenny "Oh, this is another good episode!"
        show jenny f_front_cuddle_look
        scene black with fade
        pause
        scene expression "backgrounds/location_home_livingroom_couch08.jpg"
        show expression "backgrounds/location_home_livingroom_couch08b.png"
        show jenny b_front_kiss
        with fade
        pause
        jenny "Mmm..."
        show anon b_front_kiss_talk f_front_kiss
        show jenny b_front_kiss_talk f_front_kiss
        with dissolve
        jenny "Okay, let's go upstairs!"
        anon "Already?"
        show jenny b_front_undies a_remote f_front_forward with dissolve
        show anon f_front_right b_front a_down with dissolve
        jenny "C'mon {b}[firstname]{/b}, your girlfriend needs that big dick of yours!"
        show jenny f_front_left
        anon "Well, when you put it that way..."
        jenny "Let's go!"
        hide jenny with dissolve
        anon "Okay, okay..."
        jenny "Hehehe!"
        anon "( I should {b}hurry upstairs after her{/b}. )"
        hide anon with dissolve
    return

label jenny_button_gf_experience_start:
    show anon f_flirt a_money with dissolve
    anon "Here."
    show anon a_idle
    show jenny f_sexy_down a_money b_dressed
    with dissolve
    if M_jenny.get("jenny_girlfriend_first_time"):
        jenny "Heh, I can't believe I'm doing this..."
    else:
        jenny "Heh, that's what I like to see!"
    show jenny f_sexy a_hips with dissolve
    jenny @ -m_talk "..."
    show jenny f_eyeroll
    jenny "{i}*Sigh*{/i} So what do you wanna do?"
    show jenny f_normal
    return

label jenny_button_gf_experience_no_money_repeat:
    anon f_flirt "Well... Not all of it."
    show jenny f_upset
    jenny "Since when are you broke?!"
    anon f_normal "I dunno..."
    jenny @ f_eyeroll "{i}*Sigh*{/i} Fine, just give me whatever you have and let's do this..."
    anon f_confused "R-really?"
    show anon f_surprised
    jenny "Yes!"
    return

label jenny_button_gf_experience_no_money_first:
    anon f_flirt "Well... Not all of it."
    show jenny f_upset
    jenny @ -m_talk "..."
    jenny "I told you five hundred dollars!"
    anon f_worried "B-but I don't have that much..."
    show jenny f_eyeroll
    jenny "Aww, that's very sad for you."
    show jenny f_grin
    jenny "{b}Come back when you have the money{/b}, doofus."
    anon f_sad_down "{i}*Sigh*{/i} Fine."
    show anon f_tired
    return

label jenny_button_gf_experience_nevermind:
    anon f_worried "On second thought, I'm not interested right now."
    show jenny f_upset
    jenny "Tch, don't waste my time, {b}[firstname]{/b}!"
    return

label jenny_button_gf_experience_evening:
    anon f_flirt "Want to do that thing?"
    show jenny f_grin
    jenny "Oh, you want the girlfriend experience tonight, huh?"
    jenny "I hope you've brought money..."
    return

label jenny_button_gf_experience_day:
    anon f_flirt "Want to do that thing?"
    show jenny f_upset
    jenny "Not now, you doofus!"
    anon f_worried @ -m_talk "Hmm?"
    show jenny f_grin
    jenny "Bug me about that {b}later this evening{/b}!"
    anon f_normal "Oh, right."
    jenny "Don't forget to {b}bring the five hundred dollars{/b} either!"
    return

label button_jenny_have_a_surprise_no:
    anon f_worried "No, I want the real thing."
    show jenny f_eyeroll
    jenny "Yeah, not happening, loser."
    show jenny f_upset
    jenny "Let me know when you come to your senses..."
    show jenny b_magic_sit_stand_dressed a_idle with dissolve
    return

label button_jenny_have_a_surprise_yes:
    anon f_normal "Yes."
    show jenny f_grin
    jenny "Then we have a deal!"
    jenny "{b}Come back this evening with five hundred dollars{/b} and I'm all yours."
    anon f_worried "Why can't we start now?"
    show jenny f_upset
    jenny "Uhh, because it's camshow time and that pays way more then five hundred measly dollars, idiot!"
    anon f_sad_down "... Fine."
    show anon f_tired
    show jenny b_magic_sit_stand_dressed a_idle with dissolve
    return

label button_jenny_have_a_surprise_necklace:
    anon f_normal "I have a surprise for you!"
    show jenny f_eyeroll
    jenny "Well, it had better be something nice!"
    show jenny f_upset
    show anon f_shy_down a_backpack with dissolve
    pause
    if player.has_item("crystal_necklace"):
        show anon f_laugh a_necklace1 with dissolve
    elif player.has_item("pearl_necklace"):
        show anon f_laugh a_necklace3 with dissolve
    else:
        show anon f_laugh a_necklace2 with dissolve
    anon "Ta-da!"
    show anon f_normal
    show jenny f_surprised
    jenny "..."
    show jenny f_gross
    jenny "Eww!"
    anon f_worried "Y-you don't like it?"
    show anon f_tired
    show jenny b_dressed a_crossed with dissolve
    jenny "Eugh, no!"
    anon "..."
    jenny "Why in the hell would you buy me that?!"
    anon "I just thought, maybe it would convince you to-"
    show anon f_worried
    jenny @ f_upset "Oh my god, are you trying to butter me up for a date again?!"
    show anon f_tired a_idle with dissolve
    anon @ -m_talk "..."
    show jenny f_eyeroll
    jenny "What the fuck, {b}[firstname]{/b}?!"
    show jenny f_upset
    jenny "{i}*Sigh*{/i} Okay, first of all, you have terrible taste..."
    jenny "That necklace looks cheap as hell!"
    anon @ -m_talk "..."
    jenny "I mean, honestly, if by some miracle you actually do land a girlfriend one day... You should just give her cash and let her-"
    show jenny f_surprised
    jenny "..."
    anon f_worried "Let her what?"
    show jenny f_grin a_hips with dissolve
    jenny "Oh my god, I just had a brilliant idea!"
    anon @ -m_talk "..."
    jenny "I'm thinking, since you're obviously pathetic and desperate for a girlfriend..."
    anon f_skeptical "Hey, that's not-"
    show anon f_worried
    jenny "I {i}might{/i} be willing to {b}act like one{/b}... For a modest fee of course."
    anon f_skeptical "Wait a second."
    anon "Are you seriously suggesting that I pay you to be my girlfriend?"
    jenny "No, I'm suggesting that you pay me to {i}pretend{/i} to be your girlfriend..."
    anon @ -m_talk "..."
    anon "Why would I ever do that?"
    show jenny f_laugh
    jenny "Because like I said, you're pathetic and desperate."
    show jenny f_grin
    anon "I am not!"
    show jenny f_laugh
    jenny "Hahahaah, you so are!"
    show jenny f_grin
    anon @ -m_talk "..."
    jenny "Plus, this will give me a chance to work on my acting!"
    anon "Yeah, you are a terrible actress..."
    show jenny f_angry
    jenny "{i}*Gasp*{/i} Fuck you!"
    jenny "I'm an awesome actress!"
    anon f_sad_down "Yeah, right."
    show anon f_sad
    show jenny f_grin a_hips_touch1:
        xoffset -100
    with dissolve
    jenny "C'mon, this would be a perfect excuse for us to spend more time together."
    anon f_worried "W-what are you doing?"
    show jenny a_hips_touch2 with dissolve
    jenny "I really wanna do this, {b}[firstname]{/b}..."
    jenny "Let me show you how I really feel about you."
    anon @ -m_talk "..."
    jenny "I don't wanna hide it anymore..."
    show anon f_surprised
    jenny "I wanna tell the whole world just how much I care about you!"
    jenny "How I think about you all the time..."
    jenny "Your handsome face, your strong arms... Your adorable little haircut!"
    anon f_worried "R-really?"
    jenny "Mhmm."
    jenny "I want to hold your hand, {b}[firstname]{/b}!"
    anon f_normal @ -m_talk "..."
    jenny "I want to taste your lips..."
    jenny "... Fall asleep in your arms."
    anon @ -m_talk "..."
    jenny "I want to tell you that I love you!"
    anon "I want that too!"
    pause
    hide jenny
    show jenny f_laugh
    with dissolve
    jenny "Pfft, HAHAHAHAHAAAH!!"
    anon f_surprised @ -m_talk "..."
    anon f_angry "That's not funny, {b}[jen_name]{/b}!"
    jenny "You should have seen your face!!"
    jenny "HAHAHAAH! {i}*Snort*{/i}"
    anon "You are such a bitch!"
    show jenny f_grin
    jenny "You're the one who said I couldn't act!"
    jenny "Admit it, I'm damn good!"
    anon f_tired @ -m_talk "..."
    jenny "I could girlfriend the shit out of you... For the right price."
    anon "{i}*Sigh*{/i} How much do you want?"
    jenny "Mmm, let's say five hundred dollars for the night."
    anon f_surprised "Five hundred!!"
    anon "That's a lot, {b}[jen_name]{/b}!"
    jenny @ f_eyeroll "Oh, please... It's chump change."
    jenny "Tell ya what, I'll throw in tomorrow morning too."
    anon f_normal "Y-you mean you'll stay with me all night?"
    jenny "That's what you want, isn't it?"
    return

label jenny_button_what_are_you_writing:
    anon f_worried "What are you writing?"
    show jenny f_upset
    jenny "None of your business, idiot!"
    anon "I'm just curio-"
    show anon f_surprised_teeth a_up
    show jenny f_angry a_crossed
    with dissolve
    jenny "GET OUT!!!"
    hide anon with dissolve
    return

label jenny_button_what_are_you_writing_2:
    anon f_worried "What are you writing?"
    show jenny f_upset
    jenny "None of your business."
    anon f_normal "Aww, c'mon... I'm curious."
    jenny "No way, {b}[firstname]{/b}!"
    show anon f_worried
    jenny "These are my private thoughts!"
    show anon a_up with dissolve
    anon f_skeptical "Alright, alright... Sheesh!"
    show anon a_idle with dissolve
    return

label jenny_button_nevermind_evening:
    anon f_worried "I guess I'll just be going then..."
    show jenny f_eyeroll
    jenny "God, you are such a loser."
    show jenny f_upset
    show anon f_skeptical a_thinking with dissolve
    anon @ -m_talk "..."
    show jenny f_angry a_crossed with dissolve
    jenny "Get lost!!"
    hide anon with dissolve
    return

label jenny_button_nevermind_evening_2:
    anon f_skeptical "Mmm, forget it."
    anon f_laugh "I've got other things to do today."
    show anon f_normal
    show jenny f_eyeroll
    jenny "Yeah, right!"
    show jenny f_grin
    jenny "What the hell do you ever do?"
    show jenny f_laugh
    show anon f_tired
    jenny "Besides sit in your room and play with your tiny little dingus?"
    if M_jenny.get("dominance") <= 0:
        anon @ -m_talk "..."
        jenny "Hahaha!"
        show jenny f_grin
        show anon a_wave with dissolve
        anon "Whatever, I'm leaving."
        show anon a_idle with dissolve
        jenny "Bye, loser!"
        hide anon with dissolve
    else:
        anon f_skeptical @ -m_talk "..."
        show jenny f_grin
        show anon f_flirt a_point with dissolve
        anon "It's not that tiny and you should know."
        anon "You play with it more than I do these days..."
        show anon a_idle with dissolve
        show jenny f_surprised
        jenny "!!!"
        show jenny f_surprised_down_back
        jenny "That's not-"
        show jenny f_angry a_crossed with dissolve
        jenny "Fuck you!"
        anon f_laugh "Haha!"
        jenny "Go away!"
        anon f_flirt "Gladly."
        hide anon with dissolve
    return

label jenny_button_fool_around_evening:
    show anon f_flirt a_point with dissolve
    anon "Wanna fool around?"
    show anon a_idle with dissolve
    show jenny f_normal
    jenny "Nah, {b}Jane{/b} is supposed to be calling any minute."
    anon "So?"
    show jenny f_upset
    jenny "So not right now, {b}[firstname]{/b}..."
    show jenny f_normal
    jenny "... Ask me again {b}later{/b}."
    anon f_tired "Okay."
    return

label button_jenny_fool_around_pool_repeat:
    anon f_normal "Wanna fool around?"
    show jenny f_grin
    jenny "You wanna fuck me in the pool again?"
    anon f_skeptical "Ehh, I dunno... You almost drowned me last time!"
    anon "Let's just go upstairs and do it in your room."
    show anon f_normal
    jenny "No, I wanna do it out here!"
    show anon f_worried
    pause
    anon "The chair then?"
    show jenny f_upset
    jenny "Are you joking?! {b}[deb_name]{/b} would totally see us!!"
    anon "Y-yeah, but..."
    show jenny f_grin
    jenny "You'll be fine, you big baby!"
    jenny "C'mon!"
    hide jenny with dissolve
    pause
    anon f_tired "{i}*Sigh*{/i} Damn it..."
    hide anon with dissolve
    jump jenny_pool_sex_intro

label button_jenny_fool_around_pool_first:
    if store._in_replay is not None:
        $ player.location = L_home_backyard
        scene expression player.location.background_closeup
        show jenny f_upset b_swimsuit a_hips
    show anon f_normal
    anon "Wanna fool around?"
    show jenny f_normal b_swimsuit a_hips
    jenny "No, I'm busy."
    anon f_confused "Busy with what?"
    show jenny f_upset
    jenny "This is my alone time, twerp."
    anon "Your alone time?"
    show jenny f_normal
    jenny "Yes, I'm reconnecting with nature!"
    anon f_worried @ -m_talk "..."
    anon f_skeptical "{b}[jen_name]{/b}, you're just sitting in our backyard taking pictures of your boobs..."
    show jenny f_grin
    jenny "They look great in this bikini, don't they?"
    anon f_tired "{i}*Sigh*{/i} So, you're weird!"
    show anon f_skeptical
    show jenny f_upset
    jenny "Fuck you, {b}[firstname]{/b}!"
    anon "Why don't you like, go for a swim or something?"
    jenny "Why the fuck would I want to go-"
    show jenny f_surprised
    pause
    show jenny f_grin
    jenny "Wait a second, what's {b}[deb_name]{/b} doing right now?"
    anon f_worried "Uhh, I dunno?"
    anon "Probably cleaning the house or doing laundry."
    show jenny f_sexy
    jenny @ -m_talk "Hmm."
    anon "Why are you looking at me like that?"
    show jenny f_grin
    jenny "Let's go for a swim."
    anon f_confused "Really?!"
    jenny "Yeah, c'mon..."
    anon f_normal "Awesome, just lemme run upstairs and get my swimsuit!"
    show jenny f_laugh
    jenny "You don't need a swimsuit, dummy!"
    show jenny f_grin
    jenny "Just take your clothes off and get in!"
    anon f_worried "Y-you mean, skinny dipping?"
    show jenny f_eyeroll
    jenny "Duh."
    show jenny f_grin
    anon "What if {b}[deb_name]{/b} comes out here?!"
    show jenny f_laugh
    jenny "Heh, then she'll discover what a perverted loser you are..."
    show jenny f_grin
    anon f_angry @ -m_talk "..."
    jenny "Don't be a pussy, she's busy cleaning the house!"
    anon f_worried "Alright, but only if you take your clothes off too!"
    jenny "Fine."
    jenny "You first."
    anon "Fine."
    show anon b_dressed_changing with dissolve
    pause
    show anon b_dressed_changing2 with dissolve
    pause
    show anon b_underwear a_sides f_skeptical with dissolve
    anon "Aren't you going to start undressing?"
    jenny "Mmm, naaah."
    anon "What?!"
    show jenny f_laugh
    jenny "Hahaha!"
    scene expression "backgrounds/location_home_backyard_pool_day_closeup.jpg"
    show jenny b_pool_enter with dissolve
    pause
    show jenny b_pool_edge f_normal
    with dissolve
    anon "Hey, you said you'd get naked too!"
    show jenny f_grin
    jenny "Ya well, I lied."
    anon @ -m_talk "..."
    jenny "Just stop whining and get in here..."
    show anon b_pool_undress with dissolve
    anon "Alright, fine!"
    show jenny b_pool f_surprised with dissolve
    jenny "Whoa, don't you dare-"
    show anon b_pool_jumping1
    show jenny b_pool_cover f_nipple2
    with dissolve
    anon "CANNONBALL!!!"
    jenny "{b}[firstname]{/b}!!!"
    show anon b_pool_jumping2 with dissolve
    pause
    show jenny b_pool f_angry
    show anon b_pool_under
    with dissolve
    jenny "You fucking dickhead!"
    show anon b_pool f_laugh
    with dissolve
    anon "Hahahahaaah!"
    show anon f_normal
    jenny "Grrr, you're such a pain in the ass!"
    anon "You deserve it, you liar."
    show jenny b_pool_hair with dissolve
    jenny "..."
    show jenny b_pool with dissolve
    anon "So, now what?"
    show jenny f_upset
    jenny "Well, I was going to fuck you but after that cannonball, I'm having second thoughts..."
    if M_jenny.get("dominance") <= 0:
        anon f_surprised @ -m_talk "!!!"
        anon f_worried "R-really?"
        jenny "{i}*Sigh*{/i} Yes, but now you're going to have to beg..."
        show jenny f_angry
        anon "Please?"
        show jenny f_grin
        jenny "Go on, you know what I wanna hear..."
        anon "{i}*Sigh*{/i} Please, {b}Princess [jen_name]{/b}?"
        jenny "Please what?"
        anon "Please have sex with me?"
        jenny "Hmm, alright... That was good enough."
    else:
        anon f_skeptical "Yeah right."
        show jenny f_angry
        jenny "I'm serious, I want an apology!"
        anon "Okay, tell you what."
        anon "You apologize for lying to me and then I'll apologize for splashing you."
        show jenny f_angry_pouting
        jenny "..."
        anon f_laugh "Then we'll have sex, deal?"
        show anon f_normal
        show jenny f_angry
        jenny "Screw you!"
        anon "Yeah, that's the idea."
        show jenny f_upset
        jenny "NO, I mean-"
        anon f_laugh "Hehe!"
        show anon f_normal
        jenny @ f_eyeroll "Ugh, you are so, not funny..."
        anon "Well, we could just skip the apologies and go right to the sex?"
        jenny "Fine."
    show jenny b_pool_plunge1 f_grin with dissolve
    pause
    hide anon
    show jenny b_pool_plunge2 f_sexy_down
    with dissolve
    pause
    jump jenny_pool_sex_intro

label button_jenny_wanna_watch_porn:
    anon f_normal "You wanna watch porn together?"
    show jenny f_grin
    jenny "Oh, you liked that, huh?"
    anon "Definitely."
    anon "I thought maybe tonight we could-"
    jenny "Pfft!"
    show jenny f_eyeroll
    jenny "Yeah, I know exactly what we could do..."
    show jenny f_grin
    anon f_worried "Is that a yes?"
    show jenny f_upset
    jenny "No, it's a maybe... If I feel like it."
    anon "... And if you don't?"
    show jenny f_laugh
    jenny "Then I guess you'll just have to finish yourself off, won't you, little loser?"
    jenny "Hahahaah!"
    show jenny f_grin
    anon @ -m_talk "..."
    return

label button_jenny_fool_around_diningroom_first:
    if store._in_replay is not None:
        $ player.location = L_home_diningroom
    scene expression game.timer.image("dining_room{}")
    show jenny b_breakfast_dressed a_phone f_upset_down zorder 1
    show anon b_dinner_sitting_look_left f_worried zorder 0
    show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
    with dissolve
    pause
    anon f_normal "Wanna fool around?"
    show jenny f_upset
    jenny "What, here?"
    anon f_worried "N-no!"
    anon "I mean, let's go upstairs, and we can-"
    show jenny f_grin a_rub with dissolve
    anon f_surprised @ -m_talk "!!!" with hpunch
    jenny "What if I wanna do it right here?"
    anon f_worried "Y-you can't be serious!!"
    jenny "Why not?"
    anon "{b}[deb_name]{/b} is cooking in the next room!"
    jenny "So?"
    anon "So, she'll kill us!"
    jenny "She doesn't have to know..."
    anon "Yeah, right!"
    show jenny f_eyeroll a_crossed with dissolve
    jenny "You are such a wuss..."
    show jenny f_upset
    anon "No, I'm not!"
    show jenny f_grin
    jenny "Then prove it!"
    anon "Huh?"
    show jenny a_yell with dissolve
    jenny "Hey, {b}[deb_name]{/b}?!"
    show jenny a_crossed with dissolve
    debbie "Huh?"
    anon "What are you-"
    if store._in_replay is not None:
        jump jenny_dining_room_sex_intro
    return

label button_jenny_fool_around_diningroom_repeat:
    anon f_normal "Wanna fool around?"
    show jenny f_grin
    jenny "You wanna have some fun?"
    anon "Yeah, let's go upstai-"
    show anon f_surprised
    jenny "Hey, {b}[deb_name]{/b}?!"
    debbie "Huh?"
    anon f_worried "No, I don't wann-"
    return

label jenny_button_leave_final_morning:
    anon f_worried "I'll just, see you later... Okay?"
    show jenny f_upset
    jenny "Yeah, whatever."
    jenny "See ya."
    hide anon with dissolve
    return

label jenny_button_leave_final_bedroom:
    anon f_normal "Sorry."
    show jenny f_upset
    jenny "Ugh, what the fuck, {b}[firstname]{/b}?!"
    jenny "You're costing me money!"
    show jenny f_gross
    anon f_confused "Can't you do one without me?"
    show jenny f_eyeroll
    jenny "Yes..."
    show jenny f_upset
    jenny "... But they pay more when that big dick of yours is involved!"
    anon f_normal "I'll be back tomorrow, okay?"
    jenny "You'd better, asshole."
    hide anon with dissolve
    return

label jenny_button_ask_movie_date:
    scene expression player.location.background_closeup with None
    show anon f_normal
    show jenny f_normal
    with dissolve
    anon "Hey, you should get dressed."
    show jenny f_gross
    jenny "Get dressed?!"
    show jenny f_grin
    jenny "You usually want me to take clothes off, not put them on..."
    anon f_laugh "Hah, yeah I know but I have a surprise for you."
    show anon f_normal
    show jenny f_sad
    jenny "Huh?"
    anon "I found that guy who's been spying on you."
    jenny "Really?"
    anon "Yeah, he apologized and offered us free movie tickets!"
    show jenny f_surprised
    jenny @ -m_talk "..."
    jenny "You want me to see a movie... With you?"
    show jenny f_sad
    anon "Yeah?"
    jenny "In public..."
    anon f_worried "Yes?!"
    jenny @ -m_talk "..."
    show jenny f_upset a_crossed
    jenny "{i}*Sigh*{/i} Do we have to?"
    anon f_normal "C'mon, it'll be nice!"
    show jenny f_eyeroll
    jenny "Ugh, fine."
    show jenny f_upset
    jenny "But I'm picking the movie!"
    anon "Okay."
    jenny "And I want popcorn!"
    anon f_surprised @ -m_talk "..."
    jenny "And gummy worms!"
    anon f_skeptical "Okay, sheesh!"
    show jenny f_eyeroll
    pause
    hide anon with dissolve
    return

label jenny_button_movie_date:
    scene expression player.location.background_closeup with None
    show anon f_skeptical
    show jenny f_normal
    with dissolve
    anon "Hurry up and get dressed, {b}we've got a movie to catch{/b}."
    show anon f_normal
    show jenny f_upset
    jenny "Ugh, I heard you the first time!"
    hide anon with dissolve
    return

label jenny_button_come_to_my_room:
    anon f_flirt "Why don't you come to my room tonight?"
    show jenny f_sexy
    jenny "Heh, oh you'd like that, wouldn't you?"
    if M_jenny.get("dominance") <= 0:
        anon f_worried "Y-yes."
        show jenny f_grin b_dressed a_crossed with dissolve
        jenny "You gonna beg me for it?"
        anon "I guess..."
        anon "I-if you want."
        show jenny f_laugh
        jenny "Hahahaah!"
    else:
        anon f_flirt "Yeah... I asked, didn't I?"
        show jenny f_laugh
        jenny "Hehehe!"
        show jenny f_sexy
        anon "You like it too and you know it."
        show anon f_grin
        show jenny f_eyeroll
        jenny "Yeah, whatever."
        show jenny f_sexy
        pause
        anon f_flirt "You're the one who's always swooning over my dick..."
        show jenny f_upset b_dressed a_crossed with dissolve
        jenny "I do not!"
        anon f_laugh "Hah, you totally do!"
        show jenny f_angry_pouting
        pause
        anon f_flirt "Just... Quit being stubborn and come to my room tonight!"
    show jenny f_sexy
    jenny "Yeah, I might come by..."
    show jenny f_grin
    pause
    jenny "... {b}{i}IF{/i}{/b} I feel like it."
    show jenny b_magic_sit_stand_dressed a_idle with dissolve
    return

label button_jenny_pool_talk:
    scene expression player.location.background_closeup with None
    show jenny b_swimsuit a_hips
    show anon f_normal
    with dissolve
    anon "Good morning."
    jenny "Hey."
    show jenny f_normal_low
    pause
    anon "You want me to move that umbrella so you can get some sun?"
    show jenny f_normal
    jenny "What?"
    jenny "Oh, nah..."
    anon f_worried "B-but-"
    show jenny f_laugh
    jenny "I'm not out here to tan, you dork..."
    show jenny f_normal
    jenny "Just trying to relax."
    anon f_normal "Oh."
    show jenny f_eyeroll
    jenny "Besides, I don't tan."
    show jenny f_normal
    anon f_worried "N-no?"
    jenny "I just burn."
    anon f_laugh "Heh, me too."
    show anon f_normal
    show jenny f_normal_low
    pause
    anon f_worried "So, uhh... {b}[deb_name]{/b} wanted me to ask you-"
    show anon f_surprised
    show jenny f_normal
    anon "..."
    show anon f_skeptical a_point with dissolve
    show jenny f_upset_down
    jenny "What are you-"
    show jenny f_upset
    anon "Who's that?"
    show anon a_idle
    show jenny f_upset:
        flip
        xoffset 500
    with dissolve
    jenny @ -m_talk "Hmm?"

    scene location_home_backyard_cutscene01
    show text _ ("The interloper in the hedge seemed visibly alarmed as Jenny turned to focus on him.") as caption
    with fade
    pause

    scene expression player.location.background_closeup
    show anon f_surprised
    show jenny b_swimsuit a_hips f_angry:
        flip
        xoffset 475
    with fade
    jenny "Again, you creepy motherfucker?!"
    jenny "This is the third time, this month!"
    jenny "My boyfriend is gonna kick your stalker ass!"

    scene location_home_backyard_cutscene02
    show text _ ("His alarm rapidly turned to panic, and he started to flee!") as caption
    with fade
    pause

    scene expression player.location.background_closeup
    show jenny f_angry b_swimsuit a_crossed
    show anon f_worried
    with fade
    jenny "Don't just stand there, go punch that guy!"
    anon "D-did you just call me your boyfriend?"
    show jenny f_gross
    jenny "Seriously?!"
    show jenny f_angry
    jenny "There's some pervert spying on me and you're worried about that?!"
    anon "R-right... Sorry."
    jenny "Hurry up before he gets away!"
    hide anon with dissolve

    scene location_home_backyard_cutscene03
    show text _ ("I rushed to the spot where the stalker had been, but he was already well on his way.") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("He was faster than he looked... and there was no way I was going to catch him.") as caption with dissolve
    pause

    scene expression player.location.background_closeup with fade
    show anon b_dressed_catch_breath with dissolve
    anon "Haah... Haah..."
    show jenny f_angry b_swimsuit a_crossed with dissolve
    jenny "Where is that bastard?!"
    anon f_tired b_dressed "He took off..."
    show jenny f_eyeroll
    jenny "Ugh, damn it!"
    show jenny f_upset
    anon f_confused "Who was that guy?!"
    jenny "I dunno, just some weirdo who keeps spying on me when I'm out here by the pool..."
    show anon f_normal
    pause
    jenny "Man, I'd like to teach that creep a lesson!"
    show jenny f_angry_pouting
    show anon f_grin
    pause
    show jenny f_gross
    pause
    show jenny f_upset
    jenny "Why are you looking at me like that?!"
    anon f_laugh "You called me your boyfriend."
    show anon f_grin
    jenny "Oh my god..."
    jenny "I was just trying to scare that guy off!"
    show jenny f_gross
    anon @ f_laugh "Hehe, sure you were..."
    show jenny f_eyeroll
    jenny "Ugh, in your dreams, loser."
    hide jenny with dissolve
    anon f_laugh "Well, that's not a very nice thing to say to your boyfriend..."
    jenny "Screw you, {b}[firstname]{/b}!"
    anon "Hahahaah!"
    anon f_surprised_down "( Hmm? )"
    show anon b_dressed_pickup with dissolve
    pause
    show anon a_ticket b_dressed f_surprised_down with dissolve
    anon "( It's a {b}movie ticket from the local theater{/b}... )"
    anon @ f_skeptical -m_talk "( I wonder if that guy dropped it? )"
    pause
    anon "( It's for later today. )"
    anon "( Perhaps, {b}I'll find him there{/b}? )"
    hide anon with dissolve
    return

label jenny_button_fool_around:
    anon f_worried "Wanna fool around?"
    show jenny f_normal
    jenny "Hell yeah, I do!"
    show anon f_normal
    show jenny f_grin_down b_pull1 with dissolve
    pause
    show jenny b_pull2 with dissolve
    pause
    show jenny b_pull3 with dissolve
    show jenny b_pull4 with dissolve
    show anon f_surprised
    pause
    show jenny f_grin_down b_naked a_panties_remove with dissolve
    pause
    show jenny b_naked_panties_remove_down with dissolve
    pause
    show jenny b_naked a_hips f_grin with dissolve
    pause
    jenny "What are you waiting for?"
    hide anon
    show jenny b_groping_naked_suck_pre a_up with dissolve
    show jenny b_groping_naked_suck a_up_clench f_surprised with dissolve
    jenny "!!!"
    pause
    show jenny f_nipple3
    jenny "Mmm..."
    pause
    show jenny b_groping_naked_touch_talk with dissolve
    anon "You have like the best tits, ever!"
    show jenny b_groping_naked_touch_look a_hips f_laugh
    jenny "Hehe, I know."
    show jenny b_groping_naked_suck_pre a_up f_nipple3 with dissolve
    pause
    show jenny b_groping_naked_suck a_up_clench f_nipple1 with dissolve
    jenny "Haah!"
    jenny "That feels awesome..."
    show jenny f_nipple3
    pause
    show jenny b_groping_naked_finger with dissolve
    jenny "Ngghhh..."
    pause
    show jenny f_nipple2
    jenny "Fuuuuck..."
    show jenny f_nipple3
    pause
    show jenny f_nipple2
    jenny "Are you just gonna tease me?"
    jenny "Let's do a camshow!"
    show jenny f_nipple3
    return

label jenny_button_fool_around_not_today:
    show jenny b_groping_naked_touch_talk f_surprised with dissolve
    anon "Sorry, I don't have time today."
    show jenny b_groping_naked_touch_look a_hips f_upset
    jenny "Mmm, seriously?!"
    jenny "Then why the fuck are we-"
    show jenny b_groping_naked_finger a_up_clench f_nipple1 with dissolve
    jenny "Haaah!"
    show jenny f_nipple2
    jenny "Oh, fuck!"
    show jenny f_nipple3
    pause
    show jenny f_nipple2
    jenny "I'm gonna-"
    show jenny f_nipple3
    pause
    show jenny b_groping_naked_squirt f_nipple2
    jenny "NGGHHH!!!" with flash
    pause
    show jenny b_groping_naked_orgasm f_nipple3
    show anon
    with dissolve
    jenny "Haah... Haah..."
    show jenny f_grin
    jenny "Asshole."
    anon @ f_grin -m_talk "Hehe."
    show jenny b_naked a_sides f_normal with dissolve
    jenny "Phew, I need to lie down..."
    anon "I'll see ya later, {b}[jen_name]{/b}."
    jenny "See ya."
    hide anon with dissolve
    return

label jenny_button_really_staying:
    if player.location == L_home_diningroom:
        show anon f_worried b_dinner_sitting_look_left
    else:
        show anon f_worried
    with dissolve
    anon "You really staying?"
    show jenny b_magic_sit_stand_dressed a_idle f_upset with dissolve
    jenny "That's what I said, didn't I?"
    anon "Yeah, but I thought you hated it here?"
    jenny "Mmm, it's not so bad... Now that I've got some money rolling in."
    jenny "{b}[deb_name]{/b} isn't on my ass about finding a job anymore and I get three free meals a day..."
    show jenny f_grin
    pause
    jenny "... And all my sexual needs are being met."
    anon f_normal "Oh, yeah?"
    show jenny f_upset
    jenny "Just don't go thinking I'm your girlfriend or something!"
    anon f_worried @ -m_talk "..."
    jenny "You have a nice dick but that's all I'm interested in..."
    jenny "Got it?!"
    anon "I guess."
    show jenny f_grin
    jenny "Good."
    return

label jenny_button_nevermind_2:
    anon f_skeptical "Mmm, forget it."
    anon "I've got other things to do today."
    show jenny f_eyeroll
    jenny "Yeah, right!"
    show jenny f_grin
    jenny "What the hell do you ever do?"
    show jenny f_laugh
    jenny "Besides sit in your room and play with your tiny little dingus?"
    show jenny f_grin
    if M_jenny.get("dominance") <= 0:
        anon f_worried @ -m_talk "..."
        show jenny f_laugh
        jenny "Hahaha!"
        anon @ f_skeptical "Whatever, I'm leaving."
        show jenny f_grin
        jenny "Bye, loser!"
        hide anon with dissolve
    else:
        anon f_angry @ -m_talk "..."
        anon "It's not that tiny and you should know."
        anon f_laugh "You play with it more than I do these days..."
        show anon f_grin
        show jenny f_surprised
        jenny "!!!"
        jenny "That's not-"
        show jenny f_angry a_crossed with dissolve
        jenny "Fuck you!"
        show jenny f_angry_pouting
        anon f_laugh "Haha!"
        show anon f_normal
        show jenny f_angry
        jenny "Go away!"
        anon "Gladly."
        hide anon with dissolve
    return

label jenny_button_nothing_2:
    anon f_worried "Just making conversation."
    show jenny f_upset_down
    jenny "Riiiight."
    hide anon with dissolve
    return

label jenny_button_warming_up:
    if player.location == L_home_diningroom:
        show anon f_normal b_dinner_sitting_look_left
    else:
        show anon f_normal
    with dissolve
    anon "Finally warming up to me?"
    show jenny b_magic_sit_stand_dressed a_idle f_eyeroll with dissolve
    jenny "Pfft, fuck no!"
    show jenny f_upset
    anon f_worried @ -m_talk "..."
    jenny "... But you're making me good money, so I'm willing to put up with you."
    anon "Yeah, right."
    jenny "That doesn't mean you're going to get a bigger cut of the profits though!"
    anon "Oh, I would never dare think that..."
    jenny "Don't be a smart ass!"
    anon "Why can't you just admit that you're warming up to me."
    show jenny f_laugh
    jenny "Hah!"
    show jenny f_upset
    jenny "Keep dreaming, asshole!"
    pause
    anon "Whatever."
    return

label button_jenny_not_swimming:
    anon f_worried "Not swimming?"
    show jenny f_upset
    jenny "Uhh, no."
    jenny "The water is fucking freezing!"
    anon "Aww, c'mon."
    anon "What's the point in having a pool if you never use it?!"
    show jenny f_eyeroll
    jenny "You just wanna see me all wet."
    show jenny f_upset
    anon f_laugh "Yeah, you caught me."
    show anon f_normal
    show jenny f_gross
    jenny "Perv."
    return

label jenny_button_nevermind:
    anon f_worried "I guess I'll just be going then..."
    show jenny f_upset
    jenny "God, you are such a loser."
    anon f_angry @ -m_talk "..."
    show jenny f_angry
    show anon f_surprised
    jenny "Get lost!!"
    hide anon with dissolve
    return

label jenny_button_just_saying_hi:
    anon f_worried "Just wanted to say hi."
    show jenny f_upset
    jenny "... Seriously?!"
    jenny "Don't waste my time, {b}[firstname]{/b}."
    anon "Can't we just-"
    show anon f_surprised
    show jenny f_angry
    jenny "NO!!!" with hpunch
    jenny "We can't \"just!\""
    jenny "Either show me some money or get the fuck out, loser!"
    anon f_skeptical "Ugh, fine..."
    return

label jenny_button_nothing:
    anon f_worried "Just trying to be friendly..."
    show jenny f_upset_down
    jenny "{i}*Snort*{/i} Yeah, whatever."
    jenny "I don't need a friend, dipshit..."
    jenny "I need money!"
    anon f_laugh "Good luck with that."
    hide anon with dissolve
    return

label jenny_button_you_and_phone:
    anon f_worried "Didn't anyone ever tell you that it's rude to stare at your phone during a conversation?"
    show jenny f_upset_down
    jenny "What are you, my mother?!"
    jenny @ f_eyeroll "{i}It's rude to stare at your phone{/i}."
    jenny "You sound like a senile old woman..."
    anon f_tired "..."
    show anon m_talk
    jenny "Loser."
    return

label jenny_button_just_curious:
    anon f_worried "Just curious how things are going."
    show jenny f_upset
    jenny "Yeah, great."
    jenny "Why do you care anyways?!"
    anon "Well, we're kinda like... Family, now."
    jenny @ f_eyeroll "Pfft, hardly..."
    jenny "Just eat your breakfast and leave me be."
    show jenny f_upset_down
    anon f_tired "Tch, fine."
    show anon f_shy_down
    return

label jenny_dialogue_make_a_deal_breakfast:
    if player.location == L_home_diningroom:
        show anon f_normal b_dinner_sitting_look_left
    else:
        show anon f_normal
    with dissolve
    anon "Let's make a deal."
    show jenny b_magic_sit_stand_dressed a_idle f_upset with dissolve
    jenny "Not here, you dipshit..."
    jenny "{b}[deb_name]{/b} might catch us."
    anon f_worried "Oh, right."
    jenny "Come see me {b}this afternoon{/b}."
    show anon f_normal
    pause
    jenny "... And bring the money!"
    hide anon with dissolve
    return

label button_jenny_camshow:
    show jenny f_upset
    jenny "C'mon, we have a show to do and times wasting."
    anon f_worried "O-okay."
    return

label button_jenny_start_camshow_handjob:
    if store._in_replay is not None:
        $ player.location = L_home_sisbedroom
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["08_unlocked"] = True
    scene expression player.location.background_closeup with None
    show jenny f_upset
    show anon f_worried
    with dissolve
    jenny "You ready to do this?"
    anon "Y-yeah, I guess."
    anon "I'm a little nervous..."
    jenny "Well, man up!"
    jenny "My subscribers are expecting a rock hard performance from you and I do mean that literally!"
    anon "I know."
    jenny "Well, if you know, then why are your clothes still on?!"
    anon "Huh?"
    show jenny f_grin_down b_pull1 with dissolve
    pause
    show jenny b_pull2 with dissolve
    pause
    show jenny b_pull3 with dissolve
    show jenny b_pull4 with dissolve
    show anon f_surprised
    anon "!!!"
    show jenny b_panties a_hips f_upset with dissolve
    jenny "C'mon, let's go!"
    show jenny f_grin_down b_naked a_panties_remove with dissolve
    anon f_worried "O-okay."
    show jenny b_naked_panties_remove_down with dissolve
    pause
    scene black with fade
    pause
    scene expression "backgrounds/location_home_jennybedroom_cutscene05.jpg" with dissolve
    jenny "Just sit there on the bed and put your mask on."
    anon "Yeah, I've got it."
    jenny "And don't take it off!"
    anon "Yeah, yeah..."
    jenny "I'm serious, {b}[firstname]{/b}!"
    anon "I'm not going to take the mask off!"
    scene black with fade
    pause

    scene expression "backgrounds/location_home_jennybedroom_closeup_peek.jpg" with None
    $ M_jenny.set('cam show mask', True)
    show anon b_bed_jenny_sit f_shy_down of_mask
    show jenny o_under_body_laptop b_naked_bed_belly f_sexy_down
    with dissolve
    jenny "Just remember to keep your mouth shut and let me handle everything."
    anon @ f_worried "Yeah {b}[jen_name]{/b}, I've got it."
    jenny @ f_eyeroll "Good, don't forget it!"
    pause
    jenny "Alright, here we go."
    show jenny b_naked_bed_bellytype with dissolve
    pause
    show anon f_worried
    show jenny b_naked_bed_belly with dissolve
    jenny "Hi there, boys!"
    pause
    jenny @ f_laugh "Hehe, I missed you too."
    show anon f_shy_down
    pause
    jenny "No, of course I wasn't kidding!"
    jenny "He's sitting right behind me."
    pause
    jenny "Hmm, I dunno..."
    jenny "That depends on how much you guys tip me."
    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"
    jenny @ f_laugh "Hehe, very nice!"
    "{i}*PING*{/i} {i}*PING*{/i}"
    jenny "I guess we should take a closer look at what I've brought for you guys, huh?"
    show jenny o_laptop b_bed_side_laptop a_laptop with dissolve
    show anon f_worried
    pause
    jenny "No, he doesn't have a name..."
    pause
    jenny @ f_laugh "Haha, because it's not important!"
    pause
    jenny "Yeah, he's a little nervous."
    show jenny b_bed_side f_upset with dissolve
    jenny "Would you relax already?!"
    jenny "Open up and let them see you!"
    anon "..."
    show anon b_bed_jenny_sit_back f_worried of_mask with dissolve
    pause
    show jenny f_normal
    jenny "There we go!"
    show jenny b_bed_side_laptop f_sexy_down with dissolve
    jenny "See, he's a quick learner."
    pause
    jenny "Oh, I think you'll be pleasantly surprised!"
    pause
    jenny "Well, let's take a look then, shall we?"
    show jenny b_bed_side f_normal with dissolve
    jenny "Lay back."
    show anon b_bed_jenny_laying od_bed_jenny_laying_dick1 of_bed_jenny_laying_mask_X with dissolve
    pause
    show jenny a_pull1 with dissolve
    pause
    show anon od_empty
    show jenny a_pull2
    with dissolve
    pause
    show jenny f_upset a_point
    show anon od_bed_jenny_laying_dick2
    with dissolve
    jenny "Are you kidding me?"
    jenny "Why aren't you hard?!"
    anon "I can't help it!"
    show jenny b_bed_side_laptop a_laptop f_sexy_down with dissolve
    jenny "{i}*Sigh*{/i} Just give me one second guys..."
    show jenny b_bed_side a_balls
    show expression "characters/anon/anon_overlay_dick_od_bed_jenny_laying_dick2.png"
    with dissolve
    anon "!!!"
    pause
    jenny "C'mon, big guy... It's time to come out and play!"
    hide expression "characters/anon/anon_overlay_dick_od_bed_jenny_laying_dick2.png"
    show anon od_bed_jenny_laying_dick4
    with dissolve
    show anon od_bed_jenny_laying_dick5 with dissolve
    show anon od_bed_jenny_laying_dick6 with dissolve
    pause
    show jenny b_bed_side_laptop a_laptop with dissolve
    jenny "See, I told you guys you wouldn't be disappointed."
    pause
    jenny "I know right!"
    pause
    jenny "Hehe, you guys should know by now, I wouldn't settle for anything less..."
    pause
    jenny "So, what should I do next?"
    pause
    jenny "No... I don't think so."
    pause
    jenny "Mmm, nah..."
    pause
    jenny "Oh my god, no way Sam9..."
    jenny "It's his first time on camera for fuck's sake!"
    pause
    jenny "Yeah, okay..."
    jenny "I can do that."
    jenny "Just as soon as I see some tips, of course."
    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"
    pause
    show jenny b_bed_side f_normal with dissolve
    jenny "Looks like it's your lucky day..."
    $ M_jenny.set("sex speed",0.4)
    show jenny a_jerk f_sexy_down
    anon "!!!" with hpunch
    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"
    anon "Holy crap!"
    jenny @ f_laugh "Hehe!"
    pause
    anon "That feels amazing!"
    jenny "Duh."
    jenny "What, you think I don't know what I'm doing?"
    pause
    scene expression "backgrounds/location_home_jennybedroom_sex_hj.jpg" with None
    $ animated = True
    $ anim_toggle = True
    $ M_jenny.set('sex speed', .1)
    show jenny_hj_mc
    show expression AnimatedImage("jenny_hj", [1,2,3,4,5,4,3,2], M_jenny) as jenny_hj at Position(xalign = 0.0, yoffset = 0)
    jenny "I hope you guys appreciate watching me stroke this BIG..."
    jenny "MEATY..."
    "{i}*PING*{/i} {i}*PING*{/i}"
    jenny "COCK."
    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"
    jump jenny_hj_loop

label button_jenny_come_back_camshow:
    show anon f_worried
    anon "So about that camshow with me..."
    show jenny f_upset
    jenny "I told you I have to promote first."
    jenny "{b}Come back tomorrow afternoon{/b}, dummy!"
    hide anon
    hide jenny
    with dissolve
    return

label jenny_button_bought_mask:
    scene expression player.location.background_closeup with None
    show anon f_normal
    show jenny f_upset
    with dissolve
    jenny "Did you get it?"
    anon "Yup."
    show anon f_shy_down a_backpack
    pause
    show anon f_normal a_mask with dissolve
    anon "What do you think?"
    show anon a_idle
    show jenny f_gross_down a_mask
    with dissolve
    jenny "It's pink."
    show jenny f_gross_down
    anon "So?"
    show jenny f_upset
    jenny "It's kinda girly, don't you think?"
    anon f_worried "Does that really matter?"
    show jenny f_eyeroll
    jenny "I guess not."
    show jenny f_upset a_mask_throw
    show anon f_normal a_idle
    with dissolve
    anon "So when do we start?"
    show jenny a_hips with dissolve
    jenny "I need to promote a little first."
    jenny "Come back {b}tomorrow afternoon{/b}, alright?"
    anon "Got it."
    show jenny f_angry
    jenny "And you had better put on a good show!"
    jenny "I've got a lot riding on this!"
    anon f_worried "O-okay."
    hide jenny with dissolve
    pause
    anon f_grin @ -m_talk "I guess {b}I'll come back tomorrow afternoon{/b} then..."
    hide anon with dissolve
    return

label jenny_button_get_mask:
    scene expression player.location.background_closeup with None
    show anon f_worried
    show jenny f_upset
    with dissolve
    jenny "Did you get it?"
    anon "Did I get what?"
    jenny "{b}The mask{/b}, dummy?!"
    anon "Oh, right."
    anon f_shy "Nah, I'm still working on that."
    jenny "Ugh, well, get out of my room then!"
    show anon f_worried
    hide jenny with dissolve
    pause
    show anon f_thinking a_thinking with dissolve
    anon @ -m_talk "( Hmm, I wonder what she's planning to do for the stream? )"
    pause
    anon "( I'll have to {b}get a mask{/b} if I wanna find out... )"
    anon "( I should {b}head to the mall and look around for one{/b}. )"
    hide anon with dissolve
    return

label jenny_button_talked_to_cedric:
    if player.location == L_home_diningroom:
        scene expression game.timer.image("dining_room{}")
        show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 3
        show anon b_dinner_sitting_look_left f_worried a_resting zorder 2
    else:
        scene expression player.location.background_closeup with None
        show anon f_worried zorder 2
    show jenny f_upset b_magic_sit_stand_dressed a_idle zorder 1
    with dissolve
    jenny "Did you speak with {b}Cedric{/b} yet?"
    anon "Yeah."
    pause
    anon @ -m_talk "..."
    jenny "Well?"
    jenny "Why the fuck hasn't he called me back yet?!"
    anon "He's not going to call you back."
    jenny "What?!"
    anon @ f_skeptical "He said, and I quote, \"I don't want anything to do with that crazy bitch.\""
    show jenny a_magic_sit_stand_crossed with dissolve
    jenny "You're serious?"
    anon "Mmmhmm."
    pause
    anon "Sorry."
    show jenny f_angry
    jenny "Well, fuck him then!"
    show jenny a_magic_sit_stand_phone f_phone_upset with dissolve
    jenny "Stupid asshole."
    pause
    anon @ -m_talk "..."
    show jenny f_angry a_idle with dissolve
    jenny "Grr!!!"
    hide jenny with dissolve
    pause
    anon "... Okay."
    anon @ -m_talk "( I should probably give her space until she calms down. )"
    hide anon with dissolve

    return

label button_jenny_talk_to_cedric:
    show anon f_worried
    anon "Where did you say I could find {b}Cedric{/b}?"
    show jenny f_upset
    jenny "He'll probably be at {b}the Gym{/b}."
    jenny "That meathead is always at {b}the Gym{/b}."
    anon "Alright, I'm on it."
    hide anon
    hide jenny
    with dissolve
    return

label button_jenny_has_toy_electroclit:
    scene expression player.location.background_closeup with None
    show anon f_normal
    show jenny
    with dissolve
    anon "I've got your toy."
    show jenny f_upset
    jenny "It's about time!"
    show anon a_backpack f_shy_down
    pause
    show anon f_normal a_toy1 with dissolve
    anon "This is it, right?"
    jenny "Lemme see that!"
    return

label button_jenny_has_toy_electroclit_submissive:
    show anon f_surprised a_idle
    show jenny f_gross_down a_hips_toy2
    with dissolve
    jenny "..."
    show jenny f_angry
    jenny "This is an Electro Clit Light!"
    anon f_worried "Is that a bad thing?"
    jenny "Yes, it's a bad thing!"
    jenny "How stupid are you?"
    anon "I'm not-"
    jenny "There's no way this thing is going to get me off!"
    jenny "Why didn't you get me the original model, you idiot?!"
    anon f_tired "They were sold out..."
    show jenny f_upset
    jenny "Yeah, right. Sure they were."
    show jenny f_angry
    anon f_worried "I'm serious!"
    show jenny f_upset a_crossed with dissolve
    jenny "I'm thinking, the deal is off..."
    anon "What?! C'mon {b}[jen_name]{/b}, I spent good money on that!"
    jenny "That's not my problem."
    anon b_dressed_bow "Please?"
    show jenny f_surprised
    jenny "!!!"
    show jenny f_grin
    jenny "Oh, I like that... Beg me some more!"
    anon b_dressed "Seriously?"
    jenny "Beg or the deal is off."
    anon b_dressed_bow "{i}*Sigh*{/i} Please, can I see you naked?"
    jenny "You have to say, \"I'm a pathetic little loser and I'll be a virgin forever.\""
    anon b_dressed f_skeptical "What?! I'm not gonna-"
    show anon f_surprised
    show jenny f_angry
    jenny "Do it or get out!"
    anon f_depressed "..."
    anon "I'm a pathetic little loser and I'll be a virgin forever."
    show jenny f_laugh
    jenny "Hahahahaha!"
    show anon f_sad
    show jenny f_grin
    jenny "Alright, so long as you admit it."
    jenny "I guess you've earned a treat."
    show jenny f_upset b_pull1 with dissolve
    show anon f_normal
    jenny "You're only looking for one minute though!"
    show jenny b_pull2 with dissolve
    jenny "Bringing me this stupid piece of crap toy..."
    show jenny b_pull3 with dissolve
    show jenny b_pull4 with dissolve
    pause
    show jenny b_naked a_panties_remove f_normal_low with dissolve
    pause
    show jenny b_naked_panties_remove_down with dissolve
    pause
    show jenny f_grin a_hips b_naked with dissolve
    jenny "There ya go, perv."
    anon f_surprised "!!!"
    show anon f_flirt_low
    show jenny f_upset
    jenny "Try not to drool on my rug."
    show jenny f_gross
    anon f_flirt "W-wow, you shave down there..."
    show anon f_flirt_low
    show jenny f_upset
    jenny "No shit?"
    jenny "Only old ladies and losers let their shit grow wild."
    pause
    show jenny f_grin
    jenny "Is this the first vagina you've ever seen?"
    show anon f_skeptical a_behind_head with dissolve
    anon "Well, actually I'-"
    show anon f_flirt_low
    show jenny f_eyeroll
    jenny "Yeah, of course it is. What a stupid question to ask."
    show jenny f_grin
    show anon a_idle with dissolve
    jenny "It'll probably be the last one you ever see too."
    jenny "Loser."
    pause
    show jenny f_upset
    jenny "Alright, times up!"
    anon f_worried "Aww, c'mon {b}[jen_name]{/b}... Just a little more!"
    show jenny f_angry
    jenny "No!"
    show jenny f_upset
    jenny "Screw ups like you don't get to ask for more!"
    jenny "Next time, do exactly what I tell you!"
    anon "{i}*Sigh*{/i} Fine."
    show anon f_flirt_low
    pause
    show jenny f_angry
    jenny "Now get out!"
    hide anon
    hide jenny
    with dissolve
    $ player.go_to(L_home_hallway)
    scene expression player.location.background_closeup with None
    show anon f_confused with dissolve
    anon @ -m_talk "( Sheesh, that was demeaning... )"
    show anon
    anon @ f_grin -m_talk "( I got to see her naked though. )"
    anon f_flirt_grin @ -m_talk "( So, I guess it was worth it? )"
    pause
    show anon f_thinking a_thinking with dissolve
    anon @ -m_talk "( I wonder what she's planning to do for money now? )"
    hide anon with dissolve
    return

label button_jenny_has_toy_electroclit_dominant:
    show jenny a_hips_asking f_upset
    show anon a_toy1_protect f_snarky
    with dissolve
    anon "Ah, ah!"
    anon "We had a deal, remember?"
    show jenny a_hips f_angry with dissolve
    jenny "..."
    anon @ f_skeptical "You're a little overdressed, don't you think?"
    show jenny f_eyeroll
    jenny "{i}*Sigh*{/i} Fine."
    show jenny b_pull1 f_grin_down with dissolve
    pause
    show jenny b_pull2 with dissolve
    pause
    show anon f_flirt_low
    show jenny b_pull3 with dissolve
    show jenny b_pull4 with dissolve
    pause
    show jenny b_naked a_panties_remove f_grin_down with dissolve
    pause
    show jenny b_naked_panties_remove_down with dissolve
    pause
    show jenny b_naked f_upset a_hips with dissolve
    jenny "There."
    jenny "Now let me see it!"
    anon f_flirt "Alright, here's your toy."
    show jenny f_gross_down a_hips_toy2
    show anon a_idle
    with dissolve
    pause
    show jenny f_gross_down
    jenny "Hey, this is the light version..."
    show jenny f_angry
    jenny "I wanted the original!"
    anon "Sorry, that's the only one they had."
    jenny "Well, what the fuck {b}[firstname]{/b}!"
    jenny "This thing is never gonna get me off!"
    anon "Like I said, it's the only thing they had."
    anon "Trust me, you're lucky to be getting that."
    anon "I had to jump through some hoops to get my hands on it."
    anon "Now stop bitching, you're ruining this for me!"
    show anon f_flirt_low
    show jenny f_eyeroll
    jenny "Ugh, whatever..."
    show jenny f_upset a_hips with dissolve
    anon @ f_flirt "I really like that you shave down there..."
    show jenny f_happy_down
    jenny "Y-you do?"
    show jenny f_angry
    jenny "I mean, shut up!"
    jenny "I don't care what you like, loser!"
    show jenny f_angry_pouting
    anon @ f_flirt "If you say so..."
    pause
    show anon o_boner with dissolve
    show jenny f_surprised_down
    jenny "!!!"
    jenny "Is that-"
    anon @ -m_talk "Hmm?"
    anon f_flirt "Oh, sorry."
    anon "I'm not used to-"
    anon "Well, you're really hot, you know?"
    jenny "That can't be your dick..."
    anon "Uhh, yes?"
    show anon f_grin
    show jenny f_upset
    jenny "No fucking way!"
    jenny "It's hu-"
    show jenny f_surprised_down_back a_shocked m_talk with dissolve
    pause
    anon f_flirt "It's what?"
    show anon f_grin
    show jenny f_angry a_hips -m_talk with dissolve
    jenny "Nothing."
    jenny "Are we done here?"
    anon f_flirt "Yeah, I guess that's good enough."
    show anon f_flirt_low
    show jenny f_eyeroll
    jenny "Thank god."
    show jenny f_upset
    anon @ f_flirt "Are you blushing?"
    show jenny f_angry
    jenny "N-no!"
    jenny "Get out!"
    anon f_flirt "Yeah, yeah... I'm going."
    $ player.go_to(L_home_hallway)
    scene expression player.location.background_closeup with None
    show anon f_flirt o_boner with dissolve
    anon @ -m_talk "( Well, that was hot! )"
    anon @ -m_talk "( She really seems to respond to me when I'm stern with her and don't take her crap. )"
    pause
    anon @ -m_talk "( I wonder what she's planning for money? )"
    hide anon with dissolve
    return

label button_jenny_get_toy_electroclit:
    show anon f_worried
    anon "What toy did you want me to get for you again?"
    show jenny f_upset
    jenny "Did you forget or something?!"
    anon "N-no, I didn't for-"
    pause
    anon f_skeptical "Ugh, just tell me!"
    jenny "You are worthless, you know that?"
    show jenny f_gross
    show anon f_worried
    pause
    show jenny f_upset
    jenny "{b}Go to Pink on the second floor of the mall{/b}, and {b}look for the Electro Clit{/b}."
    anon "Alright."
    jenny "Do I need to write it backwards on your forehead so you won't forget again?"
    anon f_brag_closed "No, I've got it this time."
    show anon f_normal
    show jenny f_eyeroll
    jenny "Psh, yeah right."
    show jenny f_upset
    return

label jenny_dialogue_make_a_deal:
    menu:
        "Tits.":

            if M_jenny.get("dominance") <= 0:
                show anon f_worried
                anon "Can I see your tits?"
                show jenny f_upset
                jenny "I dunno, do you have two hundred dollars?"
                if player.has_money(200):
                    anon f_normal "Yes."
                    jenny @ f_eyeroll "{i}*Sigh*{/i} Fine, hand it over."
                    show anon a_money with dissolve
                    pause
                    show anon a_idle
                    show jenny f_grin_down a_money_counting b_dressed
                    with dissolve
                    pause
                    show jenny f_upset
                    $ player.spend_money(200)
                    jump repeat_boobies
                else:
                    jump player_no_money
            else:
                show anon f_worried
                anon "Can I see your tits?"
                show jenny f_upset
                jenny "I dunno, do you have two hundred dollars?"
                if player.has_money(200):
                    $ player.spend_money(200)
                    anon "Yes."
                    jenny "{i}*Sigh*{/i} Fine, hand it over."
                    jump jenny_bedroom_jenny_go_to_her_room_dominant_has_money
                else:
                    anon "I don't even have two hundred!"
                    jenny "Well, I'm not showing you my tits for anything less than two hundred."
                    jenny "So you'd better go and get it if you want a look at these things..."
                    anon f_tired "{i}*Sigh*{/i} Fine."
                    anon "{b}I'll be back with the money{/b}."
                    jenny "Hurry up, loser."
                    jenny "I need that money!"
                    anon "Yeah, yeah."
                    hide anon
                    hide jenny
                    with dissolve
        "Never mind.":
            label player_no_money:
            show anon f_worried
            anon "Never mind."
            show jenny f_upset
            jenny "Quit messing around, {b}[firstname]{/b}!"
            jenny "If you don't have money, then get out."
            anon f_skeptical "Fine."
            hide anon
            hide jenny
            with dissolve
    return

label jenny_dialogue_roxxy_pre:
    anon f_worried "So, about {b}Roxxy{/b}'s routine..."
    show jenny f_upset
    jenny "Did you {b}bring the money{/b}?"
    return

label jenny_dialogue_roxxy_pay:
    anon f_skeptical "Here."
    show anon a_money with dissolve
    pause
    if M_jenny.pregnancy.stage > 1:
        show jenny f_grin
    else:
        show jenny f_grin a_money
    show anon a_idle
    with dissolve
    jenny "Perfect."
    jenny "Tell {i}Whatshername{/i} she can come see me after school tomorrow."
    anon f_skeptical "Her name is {b}Roxxy{/b}."
    show jenny f_gross
    jenny "Whatever."
    return

label jenny_dialogue_roxxy_do_not_pay:
    anon f_worried "I don't have it yet."
    show jenny f_upset
    jenny "Well then, beat it, I'm busy."
    return

label jenny_button_old_photo:
    anon f_worried a_backpack "I have something for you."
    show anon a_box_attic_pic2_look with dissolve
    jenny f_normal @ -m_talk "Hmm?"
    anon a_box_attic_pic2_give "Here."
    pause
    show anon a_idle
    show jenny a_attic_box_pic1 f_gross
    with dissolve
    pause
    jenny f_sad a_attic_box_pic1_sad "Where did you find this?"
    anon "It was in a box of {b}Dad{/b}'s belongings that the police released back to us."
    anon "He must have had it on his desk at work."
    jenny @ -m_talk "..."
    pause

    if M_jenny.finished_state(S_jenny_cheerleader_sex):
        anon f_shy "Do you remember that day?"
        jenny f_normal_low "Yes."
        pause
        jenny "{b}Frank{/b} got us both cotton candy, a blue and a pink..."
        anon f_worried "Wait, what?"
        jenny f_happy "... But you wanted to keep riding the ferris wheel with {b}[deb_name]{/b} so he let me eat both of them."
        anon f_shy "I didn't know that."
        jenny @ f_laugh "You don't remember me puking it all up in the car on the way home?"
        jenny "The colors mixed and it came out purple."
        anon f_normal "Oh, yeah!!"
        anon @ f_laugh "Heh, that's what you get for eating my candy!"
        jenny @ f_laugh "Whatever, you guys rode that stupid ferris wheel like twelve times... We were waiting forever!"
        anon @ a_point_back "What can I say, I like ferris wheels..."
        jenny f_normal_low @ f_eyeroll "You're ridiculous."
        pause
        jenny "That was a good day."
        pause
        show jenny f_sad
        pause
        anon f_confused "Why are you looking at me like-"
        show anon b_empty f_surprised
        show jenny b_dressed_hug_mc1 behind anon
        with dissolve
        anon "!!!"
        pause
        jenny "Thanks... For umm..."
        jenny "... Giving me this."
        pause
        show jenny b_dressed_hug_mc2
        anon f_shy_low "Y-yeah, no problem."
        pause
        show anon b_dressed f_shy
        show jenny b_dressed f_normal_low:
            flip
            xoffset 500
        with dissolve
        jenny "I need to find some place to put it."
        anon @ a_behind_head "Y-yeah, okay."
        hide jenny with dissolve
        anon "I'll just, umm... Leave you to it... I guess."
        pause
        anon "... Right."
        anon "See ya later."
        hide anon with dissolve

        $ player.go_to(L_home_hallway)
        scene expression background(360, 360, 4.) as stage with fade
        show anon with dissolve:
            flip
            xoffset -200
        anon @ -m_talk "( Well, that was unexpected... )"
        pause
        anon f_grin @ -m_talk "( Maybe things are starting to improve between {b}[jen_name]{/b} and I? )"
    else:
        anon "I thought you might want it?"
        jenny f_upset "Why would I want this?"
        anon "Umm, because it captures a pleasant memory of you and my father?"
        jenny @ f_eyeroll "Tch, that's dumb..."
        anon f_unimpressed @ -m_talk "..."
        anon a_reach "Fine, give it back then."
        show jenny with dissolve:
            xoffset 50
        jenny "What, no!"
        jenny "It's mine!"
        anon f_surprised a_idle "But you just said-"
        jenny a_idle "Shut up!"
        anon f_unimpressed "You are so weird sometimes..."
        jenny f_angry @ a_point_out "Get out of my room!"
        anon f_worried "Seriously?!"
        jenny "{b}[deb_name]{/b}!!!"
        anon f_angry "Alright, I'm going... Sheesh!"
        anon "I was just trying to do something nice for you..."
        hide anon with dissolve
        pause .6
        show jenny a_sides f_sad with dissolve
        pause
        show jenny a_attic_box_pic1_sad f_sad_down with dissolve:
            flip
            xoffset 500
        pause

        $ player.go_to(L_home_hallway)
        scene expression background(360, 360, 4.) as stage with fade
        show anon f_unimpressed with dissolve:
            flip
            xoffset -200
        anon @ -m_talk "( Well, that's not how I expected that to go at all... )"
        show anon f_surprised
        jenny "{i}*Sniff*{/i}"
        anon f_worried @ -m_talk "( Wait a minute. )"
        show anon:
            unflip
            xoffset 300
        pause
        anon @ -m_talk "( Is she... Crying? )"
        jenny "{i}*Sobbing sounds*{/i}"
        anon f_surprised "Huh."
        pause
        anon f_thinking a_thinking @ -m_talk "( I guess she didn't want me to see her upset. )"
        anon @ -m_talk "( Typical {b}[jen_name]{/b}. )"

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
