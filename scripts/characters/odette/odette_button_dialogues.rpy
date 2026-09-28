label button_odette_sex_proposal:
    scene expression player.location.background_closeup with None
    show anon
    show odette
    with dissolve
    anon @ a_wave "Morning, {b}Odette{/b}."
    odette "Hey there, big fella!"
    odette "You're here early."
    anon "Yeah."
    anon "Is {b}Eve{/b} home?"
    odette "I'm not sure."
    anon "Can I go up and check?"
    odette "Sure..."
    show odette:
        xoffset -260
    with dissolve
    odette f_smirk "... But before you do that."
    odette "I never properly thanked you for your help with {b}Grace{/b}."
    anon "Oh, there's no need."
    anon "I'm just happy everything worked out."
    pause
    anon @ f_skeptical "Everything is working out, right?"
    odette "Oh, yes!"
    odette "{b}Grace{/b} and I have really turned a corner in our relationship."
    odette "Things are better now than they've ever been!"
    anon "Well, I'm glad to hear it."
    odette "We're almost like a couple."
    anon "That's wonderful, {b}Odette{/b}."
    odette "And the sex, phew... You should hear the noises that girl makes when I'm going down on her!"
    anon @ f_surprised "!!!"
    odette "She's all squeaks and whimpers, it's beyond adorable!"
    anon f_shy "..."
    odette "{b}Eve{/b} is nothing but smiles lately as well."
    odette "You must be giving her some of that good D, huh?"
    anon "Ehh."
    odette "C'mon, big fella... Give me some deets!"
    anon "Heh, I don't think that's a good idea..."
    odette f_confused "Oh?"
    pause
    odette f_smirk "Maybe you're right."
    odette "A demonstration would be much more enlightening."
    show odette b_drop1 with dissolve
    pause
    show odette b_drop2 with dissolve
    show odette b_topless with dissolve
    show anon f_surprised_down o_boner with dissolve
    anon "!!!"
    show odette a_grope with dissolve
    odette @ f_laugh "Hehehe!"
    anon f_worried "What are you-"
    odette @ -m_talk "Hmm?"
    anon @ a_behind_head "W-we can't-"
    odette "Why not?"
    odette "You know, there's three horny women in this house... It's not really fair of {b}Eve{/b} to keep this big dick all to herself!"
    anon "What about {b}Grace{/b}?"
    odette "Don't you worry about {b}Grace{/b}."
    odette "She won't be bothered over a little harmless fun."
    anon "I dunno, {b}Odette{/b}..."
    anon "{b}Eve{/b} and I are doing really well right now-"
    odette "She won't mind either, I promise."
    pause
    odette "She might even be persuaded to come join us."
    anon a_surprised "Ngh, this does feel really good."
    odette "Hehe, I'll make you feel even better..."
    odette "What do you say?"
    return

label button_odette_sex_proposal_okay:
    anon f_flirt "Okay."
    odette "Mm, that's what I like to hear!"
    hide odette
    show odette b_topless f_thinking
    with dissolve
    call odette_1st_sex_bike
    return

label button_odette_sex_proposal_no:
    anon f_sad_down "I can't do that to {b}Eve{/b}..."
    odette f_tired a_idle "Tch, well, that's disappointing."
    anon f_tired "Sorry."
    odette "No, it's alright."
    odette "I'm happy that {b}Evie{/b} found herself such a devoted man."
    pause
    odette f_pouting "{i}*Sigh*{/i} But we could all have so much more..."
    anon @ -m_talk "..."
    odette "Oh well."
    odette "You know where to find me, if you ever come to your senses."
    anon f_worried "Y-yeah, thanks for the offer."
    odette @ -m_talk "Mmhmm."
    hide anon with dissolve
    return

label button_odette_wanna_fool_around_first_time:
    show anon f_flirt
    odette f_smirk "Oh, changed your mind?"
    anon "Y-yeah."
    odette "Good!"
    odette "I knew you'd come around."
    if player.location != L_tattooparlor_garage:
        odette "Lemme throw an away sign on the door and lock up, I'll meet you in the garage."
        anon "Okay."
        $ player.go_to(L_tattooparlor_garage)
        scene expression player.location.background_blur with fade
        show anon
        show odette
        with dissolve
    return

label button_odette_refuse_sex:
    anon f_normal "No, thanks."
    odette f_smirk "Tsk, it's a real shame to let that big dick go to waste..."
    odette "{b}Evie{/b} and {b}Grace{/b} won't mind if we have a little fun, you know?"
    odette "I promise."
    anon f_thinking a_thinking @ -m_talk "..."
    pause
    odette @ f_pouting "{i}*Sigh*{/i} Suit yourself."
    show anon f_normal a_idle with dissolve
    return

label button_odette_accept_sex:
    anon f_happy @ a_point "Yes!"
    odette "Mmm, now we're talking!"
    odette "How do you want me?"
    return

label button_odette_you_and_grace:
    anon "How are you and {b}Grace{/b} doing?"
    odette "Oh my god, it's fantastic!"
    odette "You have no idea how good it felt to finally get with her after all these years!"
    odette f_smirk "The first time she went down on me, I came in like ten seconds..."
    anon f_surprised "!!!"
    odette "... And she's so adorable when she orgasms!"
    anon @ f_confused "{i}*Gulp*{/i} O-oh?"
    odette "Maybe I'll show you sometime..."
    anon f_shock "Huh?!"
    odette @ f_laugh "Hehehe!"
    show anon f_surprised
    return

label button_odette_i_should_go:
    anon f_normal "I should go."
    odette "Aww, so soon?"
    anon "Yeah, see ya {b}Odette{/b}."
    odette "Come back if you change your mind."
    hide anon with dissolve
    return

label button_odette_wanna_fool_around:
    anon f_shy "Wanna fool around?"
    odette f_smirk "What, here in the shop?"
    anon f_worried_surprised "N-no, I thought in the garage... Maybe put a sign on the door or something?"
    odette f_pouting "Oh, but that's not as exciting..."
    anon f_confused @ -m_talk "Hmm?"
    show odette a_sides:
        xoffset -140
    with {'master': dissolve}
    odette "... C'mon, there's nobody in here right now and {b}Grace{/b} is busy upstairs."

    menu:
        "Are you sure?":
            jump button_odette_wanna_fool_around.blowjob
        "No way!":

            pass

    anon f_unimpressed "No way."
    pause
    show odette a_shrug f_eyeroll
    with {'master': dissolve}
    odette "Fine."
    show odette a_sides f_normal
    with {'master': dissolve}
    odette "Lemme throw an away sign on the door and lock up, I'll meet you in the garage."
    show anon f_shy:
        xoffset -500
        xzoom -1
    hide odette
    with {'master': dissolve}
    anon "Alright."
    hide anon with dissolve

    scene expression background(l=L_tattooparlor_garage) as stage
    show anon at flip
    with fade
    show odette f_smirk at flip
    with {'master': dissolve}
    odette "Mmm, you have the best dick {b}[firstname]{/b}..."
    anon @ a_behind_head "Heh, thanks."
    odette "How do you want me?"
    return True

label button_odette_wanna_fool_around.blowjob:
    anon "Are you-"
    show anon a_sides f_surprised behind odette
    show odette f_tired_happy:
        xoffset -250
    with {'master': dissolve}
    anon @ -m_talk "Uhh..."
    show anon a_surprised_up f_surprised
    show odette a_excited
    with {'master': dissolve}
    odette "Let's be naughty!"
    show anon a_surprised
    show odette f_tired_happy_lipbite
    with {'master': dissolve}
    anon "W-what did you have in mind?"
    show odette f_tired_happy
    with {'master': dissolve}
    odette "Heh, I'll show you..."
    show anon a_empty b_empty f_surprised_teeth:
        xoffset 150
    show odette b_dressed_pull_anon behind anon:
        xoffset 186
        xzoom -1
    with {'master': dissolve}
    odette "... Follow me big fella."
    hide anon
    hide odette
    with {'master': dissolve}
    pause

    call scene_odette_blowjob.repeat
    $ unlock_scene('Odette', '04_unlocked', variant='shop')

    scene expression player.location.background_closeup
    show odette a_wipe
    show anon a_sides f_flirt_grin
    with fade
    odette @ -m_talk "Mmm."
    show odette a_hips f_smirk
    with {'master': dissolve}
    odette "Well, that was fun."
    anon @ f_flirt "Phew, yeah it was!"
    odette "Thanks for stopping by big fella..."
    show odette a_kiss f_moo
    with {'master': dissolve}
    odette @ -m_talk "Muah!"
    show odette a_sides f_smirk
    with {'master': dissolve}
    odette "... I gotta start closing up."
    anon @ f_flirt "Y-yeah, okay."
    show anon a_wave
    hide odette
    with {'master': dissolve}
    anon @ f_flirt "See ya, {b}Odette{/b}."
    show anon a_sides
    with {'master': dissolve}
    pause
    anon f_grin @ -m_talk "( Wow! )"
    hide anon with dissolve
    return

label button_odette_intro_garage_e21:
    scene expression player.location.background_closeup with None
    show odette
    show anon
    with dissolve
    anon "Good morning, {b}Odette{/b}."
    odette "Hey there, big fella."
    odette f_smirk "Wanna go for a ride?"
    return

label button_odette_intro_interior_e21:
    scene expression player.location.background_closeup with None
    show odette
    show anon
    with dissolve
    anon @ a_wave "Hey, {b}Odette{/b}."
    odette "Hey there, big fella."
    return

label button_odette_eve_make_up_grace_upset:
    scene expression player.location.background_closeup with None
    show odette f_sad a_cover_face:
        xoffset 100
    show anon f_worried
    with dissolve
    anon "{b}Odette{/b}?"
    odette a_cheeks @ -m_talk "Hmm?"
    odette a_sides "Oh, hey {b}[firstname]{/b}."
    anon "Are you alright?"
    odette "Y-yeah, I'm okay."
    anon "{b}Grace{/b} is still upset with you, huh?"
    odette "Yes."
    odette "She's barely said three words to me since the party."
    odette "It's not my fault {b}Tuuku{/b}'s stupid friend brought drugs."
    odette "If I'd known, I would have kicked his ass out myself!"
    anon "{b}Odette{/b}, she was against having the party in the first place..."
    odette "{i}*Sigh*{/i} Yeah, I know."
    pause
    odette "I'm just not sure what she wants from me."
    odette "Everyone knows I'm only good at two things, partying and fucking."
    odette "Nowadays, it seems like she's not interested in either one."
    anon f_normal "Oh, c'mon... Surely you've got other talents besides that."
    odette "I don't think so, {b}[firstname]{/b}."
    show anon f_worried
    pause
    odette a_cover_face "Ugh, this has become such a mess."
    anon @ -m_talk "..."
    eve "{b}[firstname]{/b}?"
    show odette a_head with dissolve
    show eve:
        xoffset -300
    with dissolve
    show anon f_normal
    eve "Hey."
    show odette a_sides with dissolve
    eve f_happy "What are you doing here?"
    anon "Hey, you."
    hide anon
    show eve b_dressed_kiss1
    with dissolve
    pause
    show anon
    show eve b_dressed
    with dissolve
    anon "I was coming by to see you and I ran into {b}Odette{/b}."
    anon f_worried "We were talking about her situation with your sister."
    eve f_normal "Oh, I see."
    eve "Yeah, things have definitely been a little tense around here since the party..."
    show eve f_normal_right
    pause
    eve f_confused_right "Jesus, are you crying?"
    odette "N-no."
    eve f_normal_right "Yes, you are!"
    odette f_angry a_idle "Shut up!"
    eve "Holy shit."
    eve "I don't think I've ever seen you get emotional about anything before..."
    odette "I'm fine!"
    anon "I think we should help her."
    show odette f_sad
    eve f_normal "Yeah?"
    anon "C'mon, look at her."
    show eve:
        flip
        xoffset 300
    with dissolve
    eve "..."
    eve @ f_eyeroll "{i}*Sigh*{/i} I don't know..."
    eve "Do you really love my sister?"
    odette "What?"
    odette @ f_eyeroll "Of course I do, she's my best friend!"
    eve "No, you know what I'm asking, {b}Odette{/b}."
    eve "If this is just about getting in her pants, I'm out."
    eve "But if you really do love her, we'll help you."
    odette f_surprised a_sides "I-"
    odette f_sad @ f_sad_back "Uhh, I mean-"
    eve "It's a yes or no question, {b}Odette{/b}."
    odette f_disgusted "Yes."
    eve @ -m_talk "Hmm?"
    odette f_shy "I do."
    odette f_normal "I love your sister."
    anon "Aww!"
    odette f_sad "But believe me, she's not interested."
    eve "That's because she thinks you're flighty and immature."
    odette @ f_eyeroll "Wow, don't sugar coat it or anything..."
    eve f_happy @ f_laugh "Haha, I'm serious!"
    eve "Think about it."
    eve "You've never had a job, you basically live here without paying rent, you eat our food, use our shower-"
    odette f_normal @ f_angry "Okay, okay, I get it!"
    odette "What do you propose I do?"
    eve "Well, you could start by helping out around here."
    odette @ f_eyeroll "Tch, every time I ask her if I can help, she says no!"
    anon "That's the problem, right there."
    odette f_confused @ -m_talk "Hmm?"
    show eve f_normal_right
    anon "Don't ask her, just do it."
    anon "If she complains, say, \"I'm helping, whether you like it or not.\""
    eve f_normal "He's right."
    eve "{b}Grace{/b} spends all her time looking after us."
    eve "What she needs is someone to look after her."
    odette @ -m_talk "..."
    eve "So if you really love her, step up and do it."
    odette f_thinking @ -m_talk "Hmm."
    odette f_normal "I suppose I can do that."
    anon "Probably start with an apology."
    eve "Yeah, and maybe dinner."
    odette f_thinking @ f_surprised "Alright, alright, just slow down!"
    pause
    odette f_normal "I think I have an idea but I need to go see {b}Daddy{/b}..."
    eve f_disgusted "Eugh, stop calling him that!"
    odette "If I give you guys some money, could you get dinner all set up?"
    show eve f_normal
    menu:
        "Sure.":
            anon f_normal "We can handle that."
            odette "Good."
            show odette a_money zorder 1 with dissolve
            odette "Here."
            show odette a_idle
            show anon a_money
            with dissolve
            pause
            odette "Get {b}Grace{/b}'s favorite, okay?"
            show anon a_idle with dissolve
            odette "I'll be back for dinner."
            eve "Okay."
            $ player.get_money(200)
        "You don't need to give us money.":

            anon f_normal @ a_wave "I can handle it."
            odette f_smirk @ f_confused "Really?"
            odette "I didn't realize you were so flush, {b}[firstname]{/b}."
            eve f_happy_right "That's my man!"
            show eve b_dressed_kiss1:
                unflip
                xoffset -300
            hide anon
            with dissolve
            anon "!!!"
            show eve b_dressed
            show anon
            with dissolve
            odette @ f_laugh "Hehe."
            odette "Just make sure you get {b}Grace{/b}'s favorite, okay?"
            eve "Okay."
            odette "Thanks!"
            odette "I'll be back for dinner."
            $ M_eve.dating.increment(5)

    hide odette with dissolve
    anon f_snarky "I guess we have a lot of work to do."
    show eve f_happy:
        unflip
        xoffset -300
    eve "Seems like it."
    anon f_thinking "What's {b}Grace{/b}'s favorite, anyways?"
    eve "Lasagna."
    anon f_worried "Oh, can you make that?"
    eve @ f_laugh "Heh, hell no!"
    eve "I can barely boil water."
    anon f_sad_down a_behind_head @ -m_talk "..."
    eve "Hehe, don't worry!"
    eve "We can get it carry out from {b}Tony's Pizza{/b}."
    anon f_normal a_idle @ f_skeptical "Okay."
    eve "We should probably get some candles and wine as well."
    eve "Make it romantic, you know?"
    anon "Done."
    anon "We should get {b}Grace{/b} something nice too."
    anon @ a_thinking f_thinking "Flowers, maybe?"
    eve "Yeah, she'd love that!"
    eve @ f_surprised "Oh, we could get her chocolates!"
    eve "She was just saying the other day that she was craving chocolates."
    anon f_flirt "Chocolates it is then."
    hide anon
    show eve b_dressed_kiss:
        xoffset -400
    with dissolve
    anon "!!!"
    pause
    show anon
    show eve b_dressed:
        xoffset 0
    with dissolve
    eve "This is going to be so much fun!"
    eve "C'mon, let's {b}go to the mall{/b} and get started."
    anon "Right behind you."
    hide anon
    hide eve
    with dissolve
    return

label button_odette_progress_with_eve_no_way:
    anon f_skeptical "I'm not going to try and coax her into doing something she doesn't want."
    odette @ f_eyeroll "Who says she doesn't want it?"
    anon @ -m_talk "..."
    odette @ f_angry "Fine, be that way."
    show anon f_normal
    return

label button_odette_progress_with_eve_think_about_it:
    anon f_flirt "I'll think about it."
    odette f_smirk "Mmm, you do that."
    odette "Think about our hot, sweaty bodies rubbing against each other while you have your way with us..."
    anon f_flirt_grin @ -m_talk "!!!"
    odette "I know I will."
    odette @ f_laugh "Hehehe!"
    show anon f_normal
    return

label button_odette_progress_with_eve:
    odette f_smirk "So, how are you and {b}Evie{/b} doing?"
    anon @ -m_talk "Hmm?"
    if M_eve.biggus_dickus:
        odette "Have you taken that girldick for a spin yet?"
    else:
        odette "Have you taken that pussy for a spin yet?"
    anon f_surprised "!!!"
    anon f_worried "Umm, that's not really something I'm comfortable discussing, {b}Odette{/b}..."
    odette f_confused "Why not?"
    odette "It's nothing to be embarrassed about."
    anon f_sad_down "..."
    odette f_smirk "I know you want to."
    anon f_skeptical "What makes you say that?"
    odette "Well, you'd have to be stupid not to..."
    odette "{b}Eve{/b} is like, the perfect girl!"
    anon f_surprised "You think she's hot?"
    odette @ f_eyeroll "Duh!"
    if M_eve.biggus_dickus:
        odette "Cute, perky breasts and a nice throbbing cock?"
        odette @ f_laugh "It's the best of both worlds!"
        anon f_snarky @ -m_talk "..."
        odette "I bet she makes the most adorable noises when you stick it in her ass..."
        anon f_shock @ -m_talk "..."
        odette "Have you tasted it yet?"
    else:
        odette "Those cute, shy, inexperienced types always get me hot."
        pause
        odette "I bet she makes the most adorable noises when she orgasms..."
        anon f_surprised_teeth @ -m_talk "..."
        odette "Have you tasted her south of the border yet?"
    anon f_unimpressed @ -m_talk "..."
    odette "Oh c'mon, give me something?!"
    anon "A gentleman doesn't discuss such things."
    odette @ f_eyeroll "Ugh, gentlemen are boring."
    anon "If you're so interested, why don't you try and get with her?"
    odette "Oh believe me, I've tried."
    show anon f_surprised
    odette "She's only got eyes for you, big fella."
    pause
    odette f_confused "You know, you could mention to her that it would be hot to watch her with another girl..."
    odette "If we worked together, who knows what we could accomplish?"
    return

label button_odette_big_fella:
    anon f_worried "Why do you keep calling me that?"
    odette "Oh c'mon, you know why..."
    anon f_confused "Not really."
    odette "{b}Tuuku{/b} told me you were, {i}*Ahem*{/i}, \"gifted...\""
    anon f_worried @ -m_talk "..."
    odette @ a_point "... Below the equator."
    show anon f_looking_down
    pause
    anon f_surprised "!!!"
    anon f_shy "O-oh."
    odette @ f_laugh "Hahaha!"
    odette "{b}Evie{/b} won't spill the beans on whether it's true or not."
    anon @ -m_talk "..."
    odette "If it is, I might have to ask her if she'll let me play with it once in a while."
    anon f_worried @ a_behind_head "Ehehe..."
    return

label button_odette_are_you_alright_2:
    anon f_worried "Are you alright?"
    odette "Yeah, I'm fine."
    odette "Just really, really, REALLY hungover..."
    pause
    odette f_tired_happy "You wanna come nap with me?"
    anon f_surprised_teeth "!!!"
    anon f_worried "Uhh, I don't think that's a good idea..."
    odette f_smirk a_idle "Aww, c'mon... I'll let you be the little spoon?"
    anon f_normal "Heh, nah."
    odette @ f_pouting "Aww, you're no fun."
    return

label button_odette_grace_and_tuuku:
    anon "So how long have you known {b}Grace{/b}?"
    odette "She and I have been best friends since kindergarten."
    anon "Really?"
    odette "Yup, she traded her banana for my pudding cup and that was it."
    odette @ f_laugh "Besties for life!"
    anon "Heh, that's funny!"
    pause
    anon f_worried "What about {b}Tuuku{/b}?"
    odette @ -m_talk "Hmm?"
    odette @ f_eyeroll a_mock "Oh, {b}Grace{/b} had a crush on {b}Tuuku{/b} in middle school, and they started dating."
    anon f_surprised "They dated?"
    odette "Yeah, for like a week."
    odette "Then she realized what a loser he was."
    anon f_confused "Loser?"
    odette "Heh, I'm joking."
    show anon a_thinking with dissolve
    pause
    odette "Well, mostly..."
    odette "Anyways, he's been following {b}Grace{/b} and I around ever since."
    odette "He's like our little puppy dog."
    anon f_worried a_idle "Puppy dog?"
    odette @ f_laugh "Plus he grows AMAZING weed!"
    odette "It's like, the bomb, seriously!"
    anon "I see."
    return

label button_odette_what_are_you_reading:
    anon "What are you reading?"
    odette @ a_shrug "Oh, just a catalogue for trashy lingerie."
    anon "L-lingerie?"
    odette f_smirk "Yeah, a girl can never have enough lingerie... Wouldn't you agree?"
    anon f_worried @ a_behind_head "{i}*Gulp*{/i} Yeah, sure."
    odette @ f_laugh "Hahaha!"
    return

label button_odette_nevermind_generic:
    anon "See you around."
    odette "I'll be here."
    hide anon with dissolve
    return

label button_odette_nevermind_morning:
    odette f_confused "Is {b}Grace{/b} in the shop?"
    anon "Yeah, I think so."
    odette f_tired @ f_yawn a_stretch "{i}*Yawn*{/i} Okay, good."
    anon "I should probably let you get back to sleep, huh?"
    odette f_tired_happy "Either that or cook me breakfast?"
    anon "Ehh, sweet dreams {b}Odette{/b}."
    odette @ f_laugh "Haha!"
    hide anon with dissolve
    return

label button_odette_have_you_seen_eve:
    anon "Have you seen {b}Eve{/b}?"
    odette "Umm, no?"
    odette @ a_point "I was sleeping."
    anon @ a_behind_head "Right."
    odette "If she isn't {b}at school{/b} then she's probably still {b}in bed{/b}."
    anon "Ah, okay."
    odette "You can {b}go on upstairs{/b} and wake her if you really want."
    anon "Thanks."
    odette @ -m_talk "Mmhmm."
    return

label button_odette_are_you_alright_1:
    anon f_worried "Are you alright?"
    odette "Yeah, I'm fine."
    odette "Just really, really, REALLY hungover..."
    pause
    odette f_confused "... And I think I'm missing my underwear."
    anon f_surprised @ f_shock "!!!"
    anon "Y-your underwear?"
    odette f_smirk @ a_shrug "No worries, they'll turn up somewhere."
    anon f_worried "Does this happen often?"
    odette f_thinking "Mmm, only every time I drink..."
    odette f_tired @ f_laugh "Hahaha!"
    return

label button_odette_intro_garage_e15e20:
    scene expression player.location.background_closeup with None
    show odette f_tired a_cheeks
    show anon
    with dissolve
    anon "Good morning, {b}Odette{/b}."
    odette @ -m_talk "Hmm?"
    odette "Oh, hey there big fella."
    odette a_sides @ a_stretch f_yawn "{i}*Yawn*{/i}"
    odette "What are you doing here so early?"
    return

label button_odette_intro_garage_e6e14:
    scene expression player.location.background_closeup with None
    show odette a_head f_tired
    show anon
    with dissolve
    anon @ a_wave "Good morning, {b}Odette{/b}."
    odette "Eugh, {b}[firstname]{/b}?"
    odette "What time is it?"
    anon "I'm not sure."
    odette "My head is killing me..."
    anon @ f_snarky "Sorry to wake you."
    odette "No, it's alright."
    odette "What do you want?"
    show odette a_idle with dissolve
    return

label button_odette_intro_interior_e15e20:
    scene expression player.location.background_closeup with None
    show odette
    show anon
    with dissolve
    anon "Hey, {b}Odette{/b}."
    odette "Hey there, big fella."
    return

label button_odette_intro_interior_e6e14:
    scene expression player.location.background_closeup with None
    show odette
    show anon
    with dissolve
    anon "Hey, {b}Odette{/b}."
    odette "Hey there, handsome."
    return

label button_odette_intro_interior_e1e5:
    scene expression player.location.background_closeup with None
    show odette
    show anon
    with dissolve
    odette "The proprietor is over there, handsome."
    anon "O-oh, okay."
    anon @ a_wave "Thanks."
    odette @ -m_talk "Mhmm."
    hide anon with dissolve
    return

label button_odette_eve_party_speak_to_tuuku:
    scene expression player.location.background_closeup with None
    show anon:
        xoffset -100
    show eve b_dress:
        flip
        xoffset 200
    show odette
    with dissolve
    odette "{b}Tuuku{/b} must have gone outside, I can't find him anywhere..."
    eve "We'll find him."
    show odette f_smirk
    if M_eve.biggus_dickus:
        odette "Y-you know, I'm sure {b}[firstname]{/b} can find him on his own... If you wanna hang up here with me {b}Evie{/b}?"
    else:
        odette "Y-you know, I'm sure {b}Evie{/b} can find him on her own... If you wanna hang up here with me {b}[firstname]{/b}?"
    eve @ -m_talk "Hmm?"
    odette "Help me scratch a little itch, I'm feeling at the moment?"
    show odette a_suck_fingers with dissolve
    show anon f_confused
    eve f_surprised "!!!"
    if M_eve.biggus_dickus:
        eve "N-no, that's okay..."
        show eve f_normal
        odette a_idle "You sure?"
        odette "{b}[firstname]{/b} wouldn't mind, would you big fella?"
    else:
        eve "N-no, he's coming with me!"
        show eve f_normal
        odette a_idle "Aww, don't be so greedy {b}Evie{/b}..."
        odette "You can come back and join us when you're done."
    anon "Ehh?"
    show anon b_empty f_surprised_left zorder 1:
        flip
        xoffset -744
    show eve a_grab_mc f_normal_right:
        unflip
        xoffset -400
    eve "We're going to stick together, thanks!"
    hide anon
    hide eve
    with dissolve
    odette @ f_laugh "Hahaha, I just love making her blush!"
    return

label button_odette_eve_party_speak_to_odette:
    scene expression player.location.background_closeup with None
    show anon
    show odette f_smirk
    with dissolve
    odette "Hey there, big fella!"
    anon @ a_wave "H-hey, {b}Odette{/b}."
    odette "Did I just see you arguing with Thundercunt?"
    anon f_confused "Thundercunt?"
    odette "Yeah, the girl who just left in a huff."
    show anon f_normal
    odette "I went to school with her, you know?"
    anon "You mean {b}[jen_name]{/b}?"
    odette @ f_laugh "Hehe, yeah."
    anon "She's my roommate."
    odette f_surprised "Thundercunt is your roommate?!"
    anon f_sad_down "..."
    odette f_smirk "Holy shit, you poor kid."
    anon f_skeptical "Why do you keep calling her that?"
    odette "Thundercunt?"
    odette "That's what everyone called her in high school."
    anon f_normal @ f_laugh "For real?"
    anon "I thought she was popular in high school?"
    odette @ f_eyeroll "Well, she was, sorta..."
    odette "She ran with the cheer squad and all the meathead jocks but pretty much everyone else hated her."
    anon "I had no idea."
    odette "She was such a bitch back then..."
    anon f_normal @ f_flirt "Oh, she still is."
    odette @ f_laugh "Hahaha!"
    pause
    anon "So I seem to recall you mentioning a surprise for me?"
    odette "Oh, you mean you haven't seen it yet?"
    anon "N-no?"
    odette "That's a shame."
    odette "Took me hours to get it all wrapped up and looking pretty for you."
    odette @ f_laugh "Hehehe!"
    anon f_worried "I don't get it."
    odette @ f_surprised "{i}*Gasp*{/i} Speak of the devil..."
    anon @ -m_talk "Hmm?"
    show odette a_point with dissolve
    pause
    show anon:
        flip
        xoffset -500
    with dissolve
    show odette a_idle with dissolve
    pause
    anon f_shock "!!!"

    scene location_tattoo_rooftop_cutscene02
    show text _ ("My breath caught in my throat as {b}Eve{/b} ascended the stairs onto the rooftop.\nI don't know how {b}Odette{/b} had managed this but it was more than\nI could have hoped for!") as caption
    with fade
    pause

    scene location_tattoo_rooftop_cutscene03
    show text _ ("She looked so, incredibly, beautiful!") as caption
    with fade
    pause

    scene expression player.location.background_closeup
    show anon f_shock:
        flip
        xoffset -500
    show odette f_smirk
    with fade
    odette "Hehe, you should probably pick your jaw up off the floor, {b}[firstname]{/b}..."
    anon "..."
    odette "You owe me big time for this, you know?"
    anon f_flirt "Y-yeah..."
    hide anon
    show anon:
        xoffset -100
    show eve f_nervous b_dress:
        xoffset -400
    with dissolve
    eve "Hey."
    anon "H-hey."
    odette "Why don't I go get you guys a couple beers, eh?"
    hide odette with dissolve
    odette "Damn, I'm good!"
    eve "..."
    anon f_normal "You look..."
    eve f_sad_down "Is it bad?"
    anon f_shock "N-no!"
    anon f_worried "It's-"
    eve "{b}Odette{/b} did it."
    anon f_normal "You're the most beautiful girl I've ever seen!"
    eve f_happy "R-really?"
    anon "Definitely."
    eve @ f_nervous_down "Heh, I was a little worried..."
    eve "I've never worn anything like this before."
    anon "I just-"
    show anon f_flirt
    pause
    anon "Wow!"
    eve @ f_laugh "Hehe!"
    anon f_normal "You should dress like this every day."
    eve @ f_nervous_down "Oh, I don't think so..."
    eve @ f_surprised "Do you have any idea how long this took?"
    anon @ f_laugh "No, tell me."
    eve "The makeup alone took over an hour!"
    anon f_worried "Wow, really?"
    eve @ f_eyeroll "Yeah, and that was after {b}Odette{/b} had me try on like a hundred different outfits!"
    anon f_normal "Well, you two definitely chose a good one..."
    eve "Hehe, I'm glad you like it."
    pause
    eve "I suppose it was fun, trying on all those clothes..."
    eve "... But I definitely couldn't wear something like this to school!"
    eve f_sad_down "The other girls would-"
    anon "Be insanely jealous?"
    eve f_normal @ f_surprised "What?!"
    show odette a_beers with dissolve
    show eve f_normal_right
    odette "Alright, I got you each one."
    show anon a_beer
    show eve a_beer
    show odette a_idle f_smirk
    with dissolve
    odette "So, what are you lovebirds talking about?"
    show eve f_normal
    anon "How jealous all the girls at school would be if she dressed like this all the time."
    eve f_normal_right @ f_laugh "Oh, shut up!"
    odette "He's right, you know."
    odette "Half the guys at this party are checking you out right now."
    eve f_angry_right "N-no, they aren't!"
    odette "Oh, yes they are..."
    eve f_nervous_down @ -m_talk "..."
    odette "Oh, look at her getting all anxious now."
    odette "Don't think about it, {b}Evie{/b}!"
    odette "Chug that beer and take {b}[firstname]{/b} out on the dance floor."
    show eve a_beer_drink f_drink with dissolve
    anon f_worried "Ehh, I'm not much of a dancer..."
    show eve a_beer f_nervous_down with dissolve
    odette "Trust me, nobody is going to care."
    odette "Not when you have the hottest girl at the party out there with you."
    eve f_nervous "Y-you want to, {b}[firstname]{/b}?"
    anon f_confused "Ehh."
    odette "Go on, big fella."
    odette "Make all the other guys jealous."
    anon f_worried "Y-yeah, okay."

    scene location_tattoo_rooftop_cutscene04
    show text _ ("I was nervous as hell about dancing in front of everyone but as I looked at {b}Eve{/b}'s\nbeautiful face and saw how much fun she was having; the butterflies in my stomach went away.") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("What did I care what other people thought?\nThe only person that mattered was her and she was having the time of her life.") as caption with dissolve
    pause

    scene expression player.location.background_closeup
    show anon b_dressed_catch_breath
    show eve f_laugh b_dress
    with fade
    eve "Hehehehe!"
    show anon
    anon "Phew, I'm getting tired."
    eve f_happy "Y-yeah, me too."
    eve "You wanna take a break for a while?"
    anon "Sure."

    scene location_tattoo_rooftop_ledge with slowfade
    show eve b_dress_sidebed:
        yoffset 10
    show anon b_sit zorder 1:
        yoffset 10
    with dissolve
    eve "You know, you're really not that bad at dancing..."
    anon @ f_surprised "I'm not?"
    eve @ f_laugh "Hehe, no."
    eve @ f_eyeroll "I mean, you're not going to be winning any dancing contests but you do alright."
    anon f_grumpy "Tsk, aww man... Way to crush a man's dreams, {b}Eve{/b}!"
    eve @ f_laugh "Hahaha!"
    show anon f_flirt
    pause
    anon "I just can't get over how amazing you look tonight..."
    eve f_nervous_down "You really like it that much?"
    anon "I do."
    anon "You're so beautiful!"
    eve f_nervous "Heh, thank you."
    pause
    anon @ f_surprised "I mean, it doesn't really matter what you're wearing... You're always beautiful!"
    anon "But this was just-"
    pause
    anon "This was a really great surprise."
    eve f_sexy "Well, you know, I could probably be convinced to dress like this again..."
    anon "Oh?"
    eve "Maybe, on a date or something?"
    anon f_normal "That's a great idea!"
    eve f_normal "Yeah?"
    anon "Absolutely!"
    anon "We could go see a movie or out to dinner or-"
    hide eve
    show anon b_sit_kiss_eve1
    with dissolve
    anon "!!!"
    pause
    show anon b_sit_kiss_eve
    pause
    show eve b_dress_sidebed f_sexy zorder 0:
        yoffset 10
    show anon b_sit f_surprised
    with dissolve
    eve "God, you're a good kisser!"
    anon f_flirt "Heh, t-thanks."
    hide eve
    show anon b_sit_kiss_eve
    with dissolve
    pause
    pause
    eve "Mmm."
    pause
    show eve b_dress_sidebed f_sexy zorder 0:
        yoffset 10
    show anon b_sit f_flirt a_touch_eve
    with dissolve
    eve "Y-you know, if you want..."
    eve "We can go downstairs to my room and-"
    show anon f_surprised
    show eve f_surprised
    odette "HEY, {b}EVIE{/b}!"
    show eve f_sad_down
    odette "WHERE YOU AT?!"
    eve f_normal @ f_eyeroll "{i}*Sigh*{/i} We're over here..."
    odette "Oh, there you are!"
    scene expression player.location.background_blur with None
    show anon o_boner:
        xoffset -100
    if M_eve.biggus_dickus:
        show eve b_dress_boner a_cover:
            flip
            xoffset 200
    else:
        show eve b_dress a_cover:
            flip
            xoffset 200
    show odette
    with dissolve
    if M_eve.biggus_dickus:
        odette "Sorry to interrupt you two but-"
        odette f_surprised_down "!!!"
        pause
        eve "W-what?"
        show eve f_normal_down
        pause .5
        eve f_surprised "!!!" with hpunch
        show eve
        eve a_idle "EEEEEEP!"
        show eve f_nervous_down zorder 0:
            xoffset -100
        show anon f_surprised_left zorder 1:
            xoffset 50
        with dissolve
        pause
        show anon f_normal
        odette f_normal "{i}*Ahem*{/i} I uhh, w-would you guys do me a favor?"
        anon "Sure, what's up?"
        odette "Could you run outside and tell {b}Tuuku{/b} to get his ass up here?"
        odette "People are starting to sample his merchandise and I'm sure he doesn't want them smoking it all up."
        anon "Yeah, we can do that."
        odette "I'd really appreciate it."
        show odette f_smirk
        pause
        odette "Sorry again for the interruption."
        eve "I-it's fine."
        odette @ f_laugh "Heh, you guys are too fucking adorable, I swear..."
        hide odette with dissolve
        pause
        show anon f_worried:
            flip
            xoffset -350
        with dissolve
        anon "You alright?"
        eve @ f_nervous "Umm, y-yeah..."
        eve "I just need a minute."
        anon "Sure."
    else:
        odette "Sorry to interrupt you two but-"
        odette f_surprised "!!!"
        pause
        eve "W-what?"
        eve f_surprised_right "!!!" with hpunch
        show eve f_surprised a_idle:
            xoffset 100
        with dissolve
        eve "EEEEEEP!"
        anon f_worried @ -m_talk "Hmm?"
        pause
        odette "{i}*Ahem*{/i} I uhh, w-would you guys do me a favor?"
        anon "Sure, what's up?"
        odette "Could you run outside and tell {b}Tuuku{/b} to get his ass up here?"
        odette "People are starting to sample his merchandise and I'm sure he doesn't want them smoking it all up."
        anon "Yeah, we can do that."
        odette "I'd really appreciate it."
        show odette f_smirk
        pause
        odette "Sorry again for the interruption."
        eve "I-it's fine."
        odette @ f_laugh "Heh, you fucking lucky girl you..."
        hide odette with dissolve
        pause
        show eve f_nervous:
            unflip
            xoffset -400
        with dissolve
        anon f_confused "What's the matter?"
        eve "Y-you're umm... Hard."
        anon f_surprised_down "!!!"
        show anon a_cover_boner
        show expression "characters/anon/anon_arms_dressed_a_cover_boner.png":
            xpos -100
        with dissolve
        anon f_worried "Whoopsie!"
        anon "S-sorry about that..."
        eve @ f_laugh "Heh, it's okay."
        hide anon
        hide expression "characters/anon/anon_arms_dressed_a_cover_boner.png"
        with dissolve
    return

label odette_button_party_start:
    scene expression player.location.background_closeup with None
    show anon
    show odette
    with dissolve
    odette "You're coming right?"
    anon "Yeah, I'm coming."
    odette f_smirk "Good, because I've got something special planned and you're definitely going to like it!"
    anon f_worried "R-really?"
    odette @ f_laugh "Yup!"
    pause
    anon "What is-"
    odette @ a_mock "Ah, ah, ah!"
    odette "It's a surprise!"
    anon @ -m_talk "..."
    odette "You'll just have to wait and see on {b}Saturday{/b}."
    odette f_normal @ f_laugh "It's going to be epic!"
    return

label button_odette_eve_clients_wake_up_grace:
    scene expression player.location.background_closeup with None
    show anon f_worried
    show odette a_head f_tired b_wakeup
    with dissolve
    odette "Eugh, my head feels like it's going to explode!"
    anon @ a_behind_head -m_talk "( I should probably leave her be... )"
    hide anon with dissolve
    return

label button_odette_eve_bike_breakdown_check_bike:
    scene expression player.location.background_closeup with None
    show anon
    show odette
    with dissolve
    odette "Well, well... Look who's here!"
    anon "H-hi."
    odette f_smirk "{b}Tuuku{/b} told me all about you and our little {b}Evie{/b} in the tent."
    anon f_worried "He did?"
    odette @ -m_talk "Mmhmm."
    odette "I'm so happy for you guys!"
    anon f_normal "Heh, thanks."
    pause
    odette "And I hear she's quite the lucky girl..."
    anon f_confused "Ehh, lucky?"
    anon "What do you mean?"
    odette @ f_wink "Oh c'mon, you know what I mean!"
    odette @ a_point "No need to be shy, big fella!"
    anon f_normal @ f_grin a_behind_head -m_talk "..."
    odette @ f_laugh "Hahaha!"
    odette f_normal "You looking for her?"
    anon "Y-yeah."
    odette "I think she's helping {b}Grace{/b} with her bike."
    odette "In the garage."
    anon "Alright, thanks!"
    hide anon with dissolve
    odette f_smirk "You're welcome, stud."
    pause
    odette "Mmm, lucky girl indeed!"
    odette @ f_laugh "Hehe!"
    hide odette with dissolve
    return

label button_odette_eve_big_sis_check_apartment:
    scene expression player.location.background_blur with None
    show anon f_surprised
    show odette b_wakeup f_yawn a_stretch
    with dissolve
    odette "{i}*Yawn*{/i} You're back..."
    show anon f_flirt
    odette f_tired_happy a_sides "You change your mind there, handsome?"
    anon @ -m_talk "Hmm?"
    odette "You can be the little spoon if you want?"
    anon f_shy_down a_behind_head "I don't think that's such a good idea..."
    odette f_laugh "Hehe, suit yourself..."
    hide odette with dissolve
    anon a_idle f_worried @ -m_talk "( Hmm, I should probably follow {b}Eve{/b} upstairs and make sure she's okay... )"
    hide anon with dissolve
    return

label button_odette_eve_big_sis_talk_odette:
    scene expression player.location.background_blur with None
    show anon f_worried:
        xoffset -100
    show eve a_hip_angry f_sad:
        flip
        xoffset 200
    with dissolve
    eve "{b}Odette{/b}?!"
    odette "Hmm?"
    eve "What's going on!"
    show odette b_wakeup f_yawn a_stretch:
        xoffset 100
    with dissolve
    show anon f_surprised
    odette "{i}*Yawn*{/i} Oh, maaaan..."
    show anon f_flirt
    odette f_tired a_sides "Ugh, what the fuck are you doing home so early?"
    anon @ -m_talk "..."
    eve f_surprised "Oh my god, {b}Odette{/b}, your boob is out!"
    odette f_tired_down "Is it?"
    odette a_pull_top @ a_grab_top "Ugh, shit..."
    show anon f_unimpressed
    pause
    odette b_dressed f_tired a_sides "What time is it?"
    eve f_sad "Like twelve-thirty?"
    odette "Are you skipping class again?"
    show anon f_surprised_teeth
    eve f_angry a_rossed "It's not a big deal!"
    odette "Your sister is gonna be pissed..."
    show anon f_worried
    eve "Where is she anyways?"
    eve "Why isn't anyone minding the shop?!"
    odette @ a_shrug "Okay, first of all... Please lower your voice, I have a splitting migraine!"
    eve f_angry "What are you, hung over?!"
    odette @ a_point "Your sister was up half the night yesterday working on some chick who wanted a full sleeve... So, I told her to go get some shut-eye while I watched the shop..."
    eve @ a_wtf "... But you're not watching the shop, you're passed out in here!"
    odette a_head f_yawn "Oww, seriously... Not so loud..."
    show odette f_tired
    eve "You know {b}Grace{/b} can't afford to lose any business, right?"
    odette a_sides @ f_yawn "{i}*Yawn*{/i} Gimme a break, {b}Evie{/b}... It's not like you guys ever have customers in the morning anyways."
    eve @ f_eyeroll "Jesus Christ..."
    hide eve with dissolve
    anon @ -m_talk "..."
    odette f_tired_happy "What are you doing here, handsome?"
    anon "Ehh..."
    odette "You wanna come lay down with me?"
    anon f_shy "I don't think that's such a good idea..."
    odette "Aww, c'mon... I don't bite!"
    odette "... Unless you're into that?"
    show odette f_laugh
    anon f_shy_down a_behind_head "..."
    show odette f_tired_happy
    pause
    odette f_yawn a_stretch "{i}*Yawn*{/i} Suit yourself..."
    hide odette with dissolve
    anon a_idle f_worried @ -m_talk "( Hmm, I should probably follow {b}Eve{/b} upstairs and make sure she's okay... )"
    hide anon with dissolve
    return

label button_odette_crypt:
    anon f_worried "Why do I keep waking up in the graveyard?"
    odette f_confused "Huh?"
    anon "When I visit you in the crypt..."
    anon "... After we umm, you know?"
    odette "After we what?"
    anon @ a_whisper_back "Have sex."
    odette f_smirk "We didn't have sex, {b}[firstname]{/b}."
    anon f_surprised "!!!"
    anon f_worried_left a_sides @ a_whisper_back "Shh!"
    pause
    anon f_worried "What do you mean, we didn't have sex?"
    anon "I remember-"
    odette "We drank some wine and you left again..."
    anon "I did?"
    odette "You really can't handle your alcohol, you know?"
    anon f_skeptical "But I-"
    pause
    anon "I'm positive we-"
    pause
    odette "I feel like smoke is about to come out of your ears or something..."
    anon f_sad_down "This is all very confusing."
    odette "Uh huh."
    pause
    odette "Don't worry, I'm sure you'll do better next time."
    anon f_worried @ f_skeptical "Next time?"
    odette "Just {b}come see me in the crypt during a full moon{/b}."

    $ renpy.dynamic(ttl=game.timer.days_until_lunar(.5))
    $ renpy.dynamic(day=game.timer.dayOfWeek(delta=ttl, full=True))

    if game.timer.is_fullmoon():
        show anon f_surprised
        odette @ f_wink "By which I mean tonight!"
    elif ttl > 21:
        odette @ f_sad "The last one only just ended, so it'll be a few weeks."
    elif ttl > 14:
        odette @ f_pouting "The last one was only a week or so ago, so the next won't be for a few weeks yet."
    elif ttl > 7:
        odette @ f_shy "The next one is just over a week away, I'm so excited!"
    elif ttl > 1:
        odette "The next one is on [day], I hope you're ready!"
    else:
        show anon f_surprised
        odette @ f_wink "Oh, and {i}spoiler alert{/i}: That's tomorrow!"

    odette "And bring {b}Eve{/b}, if you want..."
    anon f_normal @ f_surprised -m_talk "{i}*Gulp*{/i}"
    return


label odette_repeat_boobjob:
    anon "On the couch... with your breasts?"
    odette f_smirk "Oh ho ho!"
    show odette a_pull_top f_happy_down
    with {'master': dissolve}
    odette "You wanna fuck my tits?"
    show anon a_sides f_shy
    show odette f_tired_happy
    with {'master': dissolve}
    anon "{i}*Gulp*{/i} Y-yes, please."
    odette "Alright, big fella..."
    show anon f_shy_low
    show odette b_drop1
    with dissolve
    show anon f_flirt_low
    show odette b_drop2
    with dissolve
    show anon f_flirt_grin
    show odette a_reveal b_topless
    with {'master': dissolve}
    pause
    odette "... Follow me."
    hide odette
    with {'master': dissolve}
    anon f_shy "Sweet!"
    hide anon with dissolve

    call scene_odette_paizuri.repeat
    $ unlock_scene('Odette', '05_unlocked')

    scene expression background(l=L_tattooparlor_garage) as stage
    show odette a_hair_cum b_topless f_annoyed_back o_cum_chest:
        xoffset 100
        xzoom -1
    show anon a_sides f_confused at flip
    with fade
    odette "Aww man, I got it in my hair again..."
    show anon a_shy_neck f_worried
    with {'master': dissolve}
    anon "Oh, uhh... Oops?"
    show anon f_surprised_teeth
    with {'master': dissolve}
    odette "... Son of a bitch."
    show anon a_sides f_sad
    with {'master': dissolve}
    anon "I'm really sorry."
    show odette a_reveal f_shy
    with {'master': dissolve}
    odette "Heh, it's alright, big fella."
    show anon f_shy
    with {'master': dissolve}
    odette "I'll go wash it out."
    show anon f_worried
    show odette a_hips f_thinking:
        xoffset -400
        xzoom 1
    with {'master': dissolve}
    odette "I just hope {b}Grace{/b} isn't up there."
    show anon f_worried_high
    hide odette
    with {'master': dissolve}
    anon "Right, well..."
    show anon a_wave f_shy_high
    with {'master': dissolve}
    anon "... Thanks again!"
    odette "You're welcome."
    show anon a_sides f_normal
    with {'master': dissolve}
    pause
    show anon f_grin
    with {'master': dissolve}
    anon @ -m_talk "( Awesome. )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
