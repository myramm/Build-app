label ano10_init_pizzeria_interior:
    call tony_button_stage
    hide tony
    show tony b_casual:
        flip
    show maria b_dressed_behind_fix_tony:
        flip
    show anon with dissolve:
        flip
        xoffset 100
    maria "Tsk, we should have gotten you a nice dress shirt and tie..."
    show anon f_flirt_low
    tony "You want me to wear a tie?!"
    tony "Darlin', it's a meetin' with the adoption agency, not the Pope."
    show maria b_casual f_annoyed with dissolve:
        unflip
        xoffset -100
    show anon f_normal
    maria "Yeah, but we gotta make a good impression, {b}Tony{/b}!"
    maria "If these people don't like us, we'll never get a kid."
    tony "Psh, how could they not like us?"
    pause
    anon "What's going on?"
    show maria f_normal with dissolve:
        flip
        xoffset 300
    tony "Oh, hey there, champ!"
    maria "We're headin' into the city to see about gettin' approved for adoption."
    anon "Really?"
    anon "I didn't realize you guys had decided already?"
    tony @ a_calm_down "Whoa, nothin' is decided..."
    tony "We're just checkin' things out, you know?"
    tony "Lettin' the guy give us the sales pitch."
    show maria f_sad with dissolve:
        unflip
        xoffset -100
    maria "We don't even know if we'll qualify..."
    tony @ f_eyeroll "Of course, we'll qualify, {b}Maria{/b}!"
    maria "What if they think I'm unfit to be a mother?"
    tony "Tsk, you're bein' ridiculous..."
    tony "There ain't nobody out there more fit to be a mother than you!"
    tony "Ain't that right, {b}[firstname]{/b}?"
    anon @ f_surprised -m_talk "Hmm?"
    anon "Y-yeah, totally!"
    show maria with dissolve:
        flip
        xoffset 300
    anon @ f_laugh "You're going to make a great mom, {b}Maria{/b}!"
    maria "You really think so?"
    tony "Tsk, of course he does."
    show maria f_normal with dissolve:
        unflip
        xoffset -100
    maria "I wonder if we'll get to see pictures?"
    tony "You got all that paperwork they requested?"
    maria "Yeah, I think so."
    tony "Where is it?"
    maria "In my purse, out in the van."
    tony "Well, why don't you head on out and double-check while I get {b}[firstname]{/b} the last delivery and close up, eh?"
    maria "Y-yeah, okay."
    hide maria
    show tony b_dressed_kiss_casual
    with dissolve
    pause
    show tony b_casual
    show maria b_casual f_normal behind anon:
        unflip
        xoffset -100
    with dissolve
    maria "Just don't take forever, alright?"
    maria "We can't be late!"
    tony "We're not gonna be late, darlin'."
    hide maria with dissolve
    pause
    anon f_shy "Wow, I've never seen her so... Ehh-"
    tony @ f_suspicious "Anxious?"
    anon "Yeah."
    tony "Heh, you have no idea..."
    anon "Has she been like this all day?"
    tony "Yeah, pretty much."
    tony "I been tellin' her to chill out, 'cause this ain't a sure thing, you know?"
    tony "But she's way past listenin' to that noise."
    anon @ -m_talk "..."
    tony "Ahh, don't worry yourself, champ!"
    tony "She's just frettin' about the agency approval, which is ridiculous!"
    tony "We're a shoo-in for that."
    anon f_normal "Yeah, I'm sure everything will work out."
    anon "You guys are great and you deserve a family!"
    show tony a_mc_hip_single:
        xoffset 132
    show tony_arms_dressed_a_mc_shoulder_single:
        flip
        xoffset 132
    with dissolve
    tony "Thanks, champ."
    tony "That's nice of you to say."
    anon "I really mean it, {b}Tony{/b}."
    anon "Any kid would be lucky to have you as a dad."
    tony "Ahh, c'mere you knucklehead!"
    hide tony_arms_dressed_a_mc_shoulder_single
    show tony f_normal_down_belly a_empty:
        xoffset 100
    show tony_arms_dressed_a_scrub:
        flip
        xoffset 100
    hide anon
    with dissolve
    tony "What's the big idea, huh?"
    anon "Haha!"
    tony "Tryin' to get all mushy on me?"
    hide tony_arms_dressed_a_scrub
    show tony a_mc_hip_single f_normal:
        xoffset 132
    show anon behind tony:
        flip
        xoffset 100
    show tony_arms_dressed_a_mc_shoulder_single:
        flip
        xoffset 132
    with dissolve
    anon "I'm just being honest, that's all."
    tony "Well, cut it out!"
    tony "You're gettin' me all emotional here..."
    pause
    hide tony_arms_dressed_a_mc_shoulder_single
    show tony a_idle
    with dissolve
    tony "Oh, hey!"
    tony "While we're off doin' this adoption nonsense tonight..."
    tony "... You think you could handle a little job for me?"
    anon "Of course, {b}Tony{/b}."
    anon "Anything you need, I'm your guy."
    tony "Attaboy!"
    tony "I knew I could count on you, champ!"
    tony a_pizza "You see, we got this special order in today..."
    anon "Oh?"
    tony "... For a pear-prosciutto-gorgonzola pizza."
    anon f_skeptical "Pear and prosciutto?"
    show tony a_idle behind anon
    show anon a_pizza f_disgusted_low
    with dissolve
    anon "Eugh, that sounds disgusting!"
    show anon f_disgusted
    tony @ a_finger_up "Now usually, I would refuse to make an abomination such as this, on principle."
    tony "But it just so happens that this particular customer knows where my old pal, Eddie Four-Fingers, is hidin' out."
    anon f_surprised "!!!"
    anon "You mean, your old contact?!"
    anon "The guy with the intel on the Russians?!"
    tony @ f_laugh "The very same."
    anon f_normal "That's great news, {b}Tony{/b}!"
    tony "Heh, I thought you might like that..."
    tony "It's why I'm makin' an exception."
    anon @ f_laugh "Absolutely!"
    anon "Thank you so much!"
    tony "You're welcome, champ."
    pause
    anon "So what's the play?!"
    anon "Do I need to interrogate them or something?!"
    tony f_suspicious "Interrogate?!"
    anon "Yeah, you know?"
    anon "Put the screws to them!"
    tony @ f_surprised -m_talk "..."
    tony f_normal @ f_laugh a_belly "Hahahaah!"
    tony "What do you think this is champ, a mob movie?"
    show anon f_tired
    tony "Hahahaah!"
    anon @ -m_talk "..."
    tony "All you gotta do is deliver the pie and then follow their directions..."
    tony "... Piece of cake."
    anon "Y-yeah, okay."
    tony "Hah, put the screws to 'em..."
    tony "You killed me with that one, kid!"
    anon f_unimpressed "You going to tell me where I'm taking this?"
    tony "It's going over to that {b}apartment complex{/b} on the {b}south side of town{/b}."
    tony "{b}Room 301{/b}."
    anon f_normal "{b}Apartment complex, south side of town, room 301{/b}."
    anon "Got it!"
    show tony a_mc_hip_single:
        xoffset 132
    show tony_arms_dressed_a_mc_shoulder_single:
        flip
        xoffset 132
    with dissolve
    tony "And remember, champ..."
    tony "Whatever they ask, capisce?"
    anon "No worries."
    hide tony_arms_dressed_a_mc_shoulder_single
    show tony a_finger_up
    with dissolve
    tony "Customer satisfaction is priority one on this job."
    show tony a_idle with dissolve
    pause
    tony "Oh, and you might wanna grab a sports drink or somethin' on the way."
    anon "Huh?"
    tony "Trust me, hydration is key!"
    anon f_skeptical "..."
    tony @ f_smirk_wink "You'll thank me later."
    anon "Oh kay..."
    tony "Go get em, champ."
    hide anon with dissolve

    $ player.go_to(L_pizzeria_exterior)
    scene expression player.location.background_blur with fade
    show anon a_pizza with dissolve
    anon @ -m_talk "( Oh man, this is so awesome! )"
    anon @ -m_talk "( I wonder who this contact could be? )"
    pause
    anon f_thinking @ -m_talk "( Maybe it's like, a retired assassin or famous wheelman? )"
    anon @ f_laugh -m_talk "( That would be so cool! )"
    pause
    anon f_shy_down @ -m_talk "( Whoever it is, he has weird taste in pizza... )"
    anon f_disgusted @ -m_talk "( Pear and prosciutto, gorgonzola pizza? )"
    anon @ -m_talk "( Bleh! )"
    pause
    anon @ -m_talk "( {b}I should head straight there.{/b} )"
    anon @ -m_talk "( This is my chance to finally learn more about what happened to {b}Dad{/b}... )"
    hide anon with dissolve

    $ game.timer.tick(2)
    $ player.go_to(L_apt)
    scene expression player.location.background_blur with slowfade
    show anon a_pizza with dissolve
    anon @ -m_talk "( This is the place, time to find {b}room 301{/b}, )"
    hide anon with dissolve
    return


label ano10_tony_pizzeria_interior:
    call tony_button_stage
    show tony a_phone_talk:
        unflip
        xoffset -400
    show anon with dissolve:
        flip
    tony "You don't say..."
    pause
    tony f_surprised "Completely naked?"
    show anon f_surprised
    pause
    tony f_normal @ f_laugh "Hah, that's exactly what Luigi woulda said!"
    show anon f_normal
    tony "She's got his temper, that's for sure."
    show tony:
        flip
        xoffset 0
    with dissolve
    show tony f_surprised
    pause
    tony f_normal @ f_surprised "Ahh crap, I gotta go!"
    pause
    tony "No, he just walked in."
    pause
    tony "Yeah, thanks again, {b}Tina{/b}."
    show anon f_surprised
    tony "I owe you one."
    show anon f_worried a_rub with dissolve
    pause
    tony @ f_laugh "Hah, yeah?"
    pause
    tony "Well, maybe it's you who owes me one then..."
    pause
    tony @ f_laugh "Hahahaah!"
    tony "Later, dollface."
    show tony f_smirk_wink a_point with dissolve
    show anon a_sides with dissolve
    pause
    tony f_normal "There's the man of the hour!"
    show tony a_idle with dissolve
    anon "What's going on?"
    tony "I was just chattin' with {b}Tina{/b} on the phone there..."
    tony "... And she was singing your praises."
    anon f_shy a_behind_head "Oh?"
    tony "You must have really rung her bell good, eh?"
    anon f_shy_low a_idle "Jeez, {b}Tony{/b}... I'm not sure I should talk about it."
    tony @ f_laugh a_belly "Heh, and a gentleman to boot!"
    tony a_fists "I like your style, champ!"
    anon f_normal "Did she set up a meeting with that Eddie guy?"
    tony a_idle "Yeah, sort of..."
    anon @ -m_talk "Hmm?"
    tony @ f_eyeroll "Turns out, Eddie got caught with his four-fingered hand in the wrong cookie jar."
    tony "They got him serving a ten stretch upstate."
    anon f_confused "Ten stretch?"
    tony f_suspicious "He's in prison, champ."
    anon f_surprised "Prison?!"
    anon f_worried "That's not good!"
    show tony f_normal
    pause
    anon "How are we supposed to get the info from him?"
    tony "Well, I'll have to drive up there and pay him a visit."
    tony @ f_smirk_wink "I might even take him a calzone with a file baked in it, eh?"
    anon "You're just gonna drive up there?"
    anon "As simple as that?"
    tony "As simple as that."
    show tony a_mc_hip_single:
        xoffset 32
    show tony_arms_dressed_a_mc_shoulder_single:
        flip
        xoffset 32
    with dissolve
    tony "I'll find out what he knows concernin' {b}Raz{/b} and the rest of those dirty Ruskies, I promise."
    anon "Thank you so much, {b}Tony{/b}."
    pause
    anon "{i}*Sigh*{/i} I don't know how I'm ever gonna repay you for all of this..."
    tony "Ahh, don't worry about it!"
    tony "You're as good as family, champ."
    show tony a_point:
        xoffset 0
    hide tony_arms_dressed_a_mc_shoulder_single
    with dissolve
    tony "And we take care of family, remember?"
    show tony a_idle with dissolve
    anon "I remember, {b}Tony{/b}."
    pause
    anon "Hey, speaking of family; how did the meeting with the adoption agency go?"
    tony f_sad @ f_wincing "Ugh, not so good actually..."
    anon f_worried "Huh?"
    tony "They wouldn't give us approval to adopt."
    anon f_skeptical "You're kidding!"
    tony "Nah, it's true."
    anon f_worried "What happened?!"
    tony "{i}*Sigh*{/i} The head of the agency knew who I was..."
    tony "... Or who I used to be anyways."
    tony "He said there was no way in hell he'd sign a child over to a criminal like me."
    anon "So it's just over, like that?"
    tony "I'm afraid so."
    pause
    anon "Ah, man... That sucks, {b}Tony{/b}!"
    tony f_sad_down "Yeah, it's a real crap shoot."
    pause
    tony f_sad @ a_frustrated "Just do me a favor and don't bring it up in front of {b}Maria{/b} today, yeah?"
    tony "She's hurtin'."
    anon "Yeah, I won't."
    tony "I appreciate it."
    pause
    anon "So what are you guys gonna do now?"
    tony "Well, the only option left is sperm donation, but {b}Maria{/b} ain't too happy at the idea..."
    tony "... Neither am I, really."
    anon @ -m_talk "..."
    tony "To be honest, I'm not even sure we can afford it."
    anon f_normal "Maybe I could help?"
    tony @ -m_talk "Hmm?"
    anon "I mean, I've got money..."
    tony f_normal @ a_calm_down "Heh, nah."
    tony "I appreciate it, champ, but we don't want you doin' that."
    anon "Really, I don't mind."
    tony @ f_smirk_wink "There might be somethin' else you could do to help us..."
    anon "Yeah, of course!"
    anon "Anything you need, just tell me."
    tony "I'm not sure I'm ready to get into it yet."
    tony "Maybe once I'm back from visitin' Eddie, eh?"
    anon "Sure."
    tony a_pizza "In the meantime, let's just focus on business as usual..."
    anon @ f_laugh a_salute "You got it, boss."
    tony a_idle "Thanks, champ."
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
