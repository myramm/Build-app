label eve_preg_stage_1_intro:
    scene expression player.location.background_closeup
    show eve b_undies
    show anon with dissolve
    anon "Hey, you."
    eve "Hehe, hey {b}[firstname]{/b}!"
    anon "What are you up to?"
    eve "Oh, just relaxing..."
    return

label eve_preg_stage_1_leave:
label eve_preg_stage_2_leave:
label eve_preg_stage_3_leave:
label eve_preg_stage_4_leave:
    anon @ a_wave "I'll leave you to it then."
    eve "Alright."
    anon "Let me know if there's anything I can do, okay?"
    eve "Thanks, {b}[firstname]{/b}."
    hide anon with dissolve
    return

label eve_preg_stage_1_feeling:
    eve "Other than a little morning sickness, I feel great!"
    anon f_worried "Morning sickness?"
    eve f_happy "Yeah, but it's nothing to worry about."
    eve "The books {b}Grace{/b} got me say it's perfectly normal."
    anon f_normal "So you guys got a bunch of pregnancy books, huh?"
    eve "Yup and we've been reading them together in the evenings."
    anon "That sounds fun."
    eve "Yeah, it has been."
    show eve f_normal
    return

label eve_preg_stage_1_doctor:
    anon "How did your doctor's visit go?"
    eve @ f_eyeroll "Oh, it was fine."
    eve "He did the ultrasound and said everything looked normal."
    anon "That's good to hear."
    eve "It's still too early to tell if it's a boy or a girl but {b}Odette{/b} is certain that it's going to be a boy."
    anon @ -m_talk "Hmm?"
    anon @ f_confused "Why does she think that?"
    eve "Because you were doing me from behind when we conceived."
    anon f_worried @ f_surprised "!!!"
    anon "A-and that matters?"
    eve "According to her it does..."
    anon @ a_behind_head "Weird."
    eve @ f_laugh "Hehehe!"
    show anon f_normal
    return

label eve_preg_stage_1_grace:
    anon "How's {b}Grace{/b} been doing with this whole thing?"
    eve @ f_laugh "She's been amazing!"
    eve "I don't know what I'd do without her, to be honest."
    anon "Yeah?"
    eve "She's got me on a strict pregnancy diet and I'm learning yoga."
    anon @ f_confused "You're learning yoga?"
    eve "Hehe, yeah!"
    eve "Apparently it's important to keep your anxiety levels down when you're pregnant."
    eve "She's even offered to start giving me daily massages."
    anon @ f_sad_down "Dang, I'm jealous."
    return

label eve_preg_stage_2_intro:
    scene expression player.location.background_closeup
    show eve f_happy b_pajamas_pregnant_bump
    show anon with dissolve
    anon "Hey, you."
    eve "Hehe, hey {b}[firstname]{/b}!"
    anon "What are you up to?"
    eve @ f_nervous_down "Ugh, just trying to relax..."
    return

label eve_preg_stage_2_feeling:
    anon "How are you feeling?"
    eve "Uhh, not bad all things considered."
    eve "I think the diet, yoga, and constant massages are working wonders!"
    anon "Yeah, I'd say so."
    show eve f_normal_down a_squeeze1 with dissolve
    show anon f_surprised
    eve "And have you seen these tits?!"
    show eve a_squeeze2 with dissolve
    show anon f_flirt
    eve f_happy "I've gone up a full cup size!"
    anon "{i}*Gulp*{/i} Y-yeah?"
    show eve f_sexy a_squeeze with dissolve
    eve "You better drink it in, {b}[firstname]{/b}."
    eve "{b}Odette{/b} says they're gonna go all wonky after the baby comes..."
    show eve f_happy a_idle with dissolve
    show anon f_normal
    return

label eve_preg_stage_2_anything:
    anon "Can I get you anything?"
    eve "A kiss would be nice."
    anon "I can do that."
    hide anon
    show eve b_pajamas_kiss:
        xoffset 50
    with dissolve
    eve "Mmm."
    pause
    hide eve
    show anon
    show eve f_happy b_pajamas_pregnant_bump
    with dissolve
    eve "You promise you'll still love me when I'm all fat and irritable?"
    anon f_thinking "Hmm, I dunno..."
    anon "How fat are we talking exactly?"
    eve f_surprised "{i}*Gasp*{/i}"
    anon f_normal @ f_laugh a_point "Hehe, I'm joking!"
    anon "Of course I'll still love you."
    eve f_happy @ f_angry "You'd better!"
    return

label eve_preg_stage_3_intro:
label eve_preg_stage_4_intro:
    scene expression player.location.background_closeup
    show eve f_sad b_pajamas_pregnant_belly
    show anon with dissolve
    anon "Hey, you."
    eve "Hehe, hey {b}[firstname]{/b}!"
    anon f_worried "What are you up to?"
    eve "Ugh, just trying to relax..."
    return

label eve_preg_stage_3_feeling:
label eve_preg_stage_4_feeling:
    anon "How are you feeling?"
    eve f_sad_down "Fat and irritable."
    anon "Uh oh."
    eve "I'm so freaking uncomfortable, all the time..."
    eve f_sad "And my tits are killing me!"
    anon "Can't you pump or something?"
    eve "No, I can't."
    eve "The books say that might cause premature labor."
    anon f_surprised "Really?"
    eve "{i}*Sigh*{/i} Yeah."
    show anon f_worried
    return

label eve_preg_stage_3_anything:
label eve_preg_stage_4_anything:
    anon "Can I get you anything?"
    eve "Yeah, you think you could carry this kid inside you for a while, so I can get a good night's sleep?"
    anon "You're having problems sleeping?"
    eve f_angry "Well, I've got a freaking bowling ball attached to me, what do you think?"
    anon "Sorry."
    anon "Is there anything I can do to help?"
    eve f_sad "No, I'm sorry..."
    eve "I don't mean to snap at you, {b}[firstname]{/b}."
    eve "I just want this thing out of me, you know?"
    anon "It'll happen soon, you just have to hang in there a little longer, okay?"
    eve f_sad_down "{i}*Sigh*{/i} I know."
    show eve f_sad
    return

label eve_preg_stage_4_bathroom:
    scene expression background(544, 288, 2.) as stage at flip
    show layer master at flip
    show eve b_naked_pregnant_belly f_happy a_towel_back
    show anon f_flirt with dissolve
    eve "Tsk, haven't you seen enough?"
    anon "Of course not!"
    anon "I'll never see enough of you, my love."
    eve "Nice one, Casanova... Laying it on a little thick, don't you think?"
    anon "Not if it works."
    eve @ f_laugh "Hehehe!"
    anon "C'mon, just one more look?"
    eve "{i}*Sigh*{/i} Alright, you win."
    show eve a_remove1 with dissolve
    pause
    show eve a_remove2 with dissolve
    anon @ f_laugh "I love you so much!"
    eve "I love you too."
    show anon f_flirt_low
    pause
    show eve a_remove1 with dissolve
    show anon f_flirt
    eve "Now get out of here so I can finish my hair."
    anon "Alright, alright."
    hide anon with dissolve
    $ game.main()
    return

label eve_preg_stage_5_bedridden:
    scene expression game.timer.image('location_hospital_baby_bed{}')
    show grace f_happy:
        crop (0, 0, 1024, 650)
        flip
        xoffset 200
        zoom .9
    show eve b_gown_bed
    with None
    show grace:
        unflip
        xoffset -100
    show anon
    with dissolve
    eve "Hey, {b}[firstname]{/b}."
    eve "You come by to check on us again?"
    anon "Yeah, how are you guys doing?"
    eve "We're all anxious to get out of here and back home."
    grace "It shouldn't be much longer now."
    eve "I hope you're right, I'm dying for some real food!"
    show grace f_laugh:
        flip
        xoffset 400
    with dissolve
    grace "Hehe, yeah... Hospital food is never any good."
    grace f_happy "Maybe we'll order some Chinese or something to celebrate?"
    eve f_happy "Oh my god, that sounds amazing!"
    show grace:
        unflip
        xoffset -100
    with dissolve
    eve "Doesn't that sound good, {b}[firstname]{/b}?"
    anon "Yeah, definitely."
    show grace:
        flip
        xoffset 200
    hide anon
    with dissolve
    $ game.main()
    return

label eve_preg_stage_5_intro:
label eve_preg_stage_6_intro:
    scene expression player.location.background_closeup
    show eve b_pajamas a_baby f_happy_down
    show anon with dissolve
    eve "♪ {i}Sleep my baby on my bosom?{/i} ♪"
    eve "♪ {i}Warm and cozy will it prove?{/i} ♪"
    eve "♪ {i}Round thee mother's arms are folding?{/i} ♪"
    eve "♪ {i}In her heart a mother's love?{/i} ♪"
    eve "♪ {i}There shall no one come to harm thee?{/i} ♪"
    eve "♪ {i}Naught shall ever break thy rest?{/i} ♪"
    eve "♪ {i}Sleep my darling babe in quiet?{/i} ♪"
    eve "♪ {i}Sleep on mother's gentle breast?{/i} ♪"
    return

label eve_preg_stage_5_singing:
label eve_preg_stage_6_singing:
    anon "What's that you're singing?"
    eve f_happy @ -m_talk "Hmm?"
    eve "Oh, it's just something my mother used to sing to {b}Grace{/b} and I when we were little."
    eve "Always put me right to sleep."
    anon "It's really beautiful!"
    eve @ f_laugh "Hehe, thanks."
    show eve f_happy_down
    return

label eve_preg_stage_5_anything:
label eve_preg_stage_6_anything:
    anon "You guys need anything?"
    eve f_happy "No, we're good."
    eve f_happy_down "Out like a light, aren't you little one?"
    eve "Yes, you are!"
    pause
    anon "Mmm, I love you both so much."
    eve @ f_happy "Hehe, we love you too!"
    return

label eve_preg_stage_5_leave:
label eve_preg_stage_6_leave:
    anon "I'll leave you be."
    eve f_happy "Leaving already?"
    anon "Yeah, I'll be back soon though."
    eve "Alright."
    eve f_happy_down "Hurry back to us."
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
