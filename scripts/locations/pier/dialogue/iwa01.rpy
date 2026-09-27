label iwa01_pier_pier:
    scene expression game.timer.image('pier_closeup{}')
    show terry with None
    show anon:
        xoffset 100
    show iwanka b_maid o_glasses:
        flip
        xoffset -80
    with dissolve

    if M_terry.finished_state(S_terry_start):
        anon @ a_wave "Hey, {b}Captain Terry{/b}."

        terry "Well, bless my beard!"

        terry "What brings you out here this evening, skipper?"

        show terry f_surprised
        pause .25
        terry f_smirk "Ho Ho, and in such fine company, I might add!"

        iwanka @ a_wave "Halo."

        terry "It's nice to meet you, young lass!"

        terry "Any friend of the skipper here is a friend of mine to be sure."

    else:

        terry "Well, bless my beard."

        terry "What have we here?"

        anon "Halo."

        terry "Taking a stroll along the beach are we?"

        anon @ f_shy "Ehh, not exactly."

        terry "It's a beautiful evening for it, if I do say so myself."

        anon "Yeah, you're not wrong about that..."


    anon "... Actually, we're looking to rent a boat."

    terry f_normal "You don't say?"

    anon "Would you happen to know a place nearby we could get one?"

    terry "Heh, I'd say that depends on how big a boat you need and how fast you'll be needin' it?"

    anon f_worried_left "Ya..."

    iwanka "We just need something that fits two and can get us up the coast a bit."

    iwanka "Right away if possible?"

    show anon f_normal
    terry @ f_laugh "Oh, you're in luck then!"

    terry "I've got a wee row boat tied up just 'round the bend."

    anon f_worried "Did you say row boat?"

    terry "Indeed I did, lad."

    anon "I don't suppose you have something with a motor?"

    terry "Well, of course I do!"

    anon f_normal @ f_brag_closed "Phew, thank goodness."

    terry "I can have it fueled up and ready for open waters first thing in the morning."

    anon f_unimpressed @ -m_talk "..."
    iwanka @ f_laugh "The row boat will be fine, thank you."

    show anon f_worried
    terry "Aye, she's all yours, lass."

    iwanka f_smirk "You can handle the rowing, can't you {b}[firstname]{/b}?"

    anon f_worried_left "{i}*Sigh*{/i} Do I have a choice?"

    iwanka @ f_laugh "Hehe, tidak."

    hide iwanka with dissolve
    terry "Don't you worry, skipper."

    show anon f_worried
    terry "Rowin' is about the best exercise a person can get!"

    terry @ f_laugh "It'll put hair on your chest, it will!"

    anon @ a_behind_head "Ya terima kasih."

    terry "Just be sure and return it when you're done, eh?"

    terry "I don't wanna have to be trackin' ya down come morning."

    anon "Jangan khawatir."

    anon "I'll leave it exactly as we find it."

    terry @ f_laugh "Good enough for me."

    show anon with dissolve:
        flip
        xoffset -500
    anon "Man, I hope wherever we're going is close..."

    hide anon with dissolve

    scene location_boat_cutscene_03
    show text _ ("The ocean air was chilly as I rowed us away from shore but {b}Iwanka{/b} didn't seem to notice, busy fiddling with her nails.") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("She hummed a pleasant melody as we went and I quickly found myself matching her beat with my oar strokes.") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("The sound of her voice coupled with the lapping waves against the hull soothed my senses and, before I knew it, we had arrived at our destination.") as caption with dissolve
    pause

    scene location_boat_cutscene_03b
    show text _ ("I was surprised to find that {b}Iwanka{/b} hadn't oversold it.") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("The luxury yacht was the biggest boat I'd ever seen!") as caption with dissolve
    pause

    scene expression background(200, 400, 2.6, l=L_boat_bridge) as stage
    show anon f_surprised a_salute
    show iwanka b_maid o_glasses
    with fade
    anon "Sialan!"

    anon "Your dad owns this thing?"

    show anon a_idle with dissolve
    iwanka f_smirk @ -m_talk "Mhmm."

    pause
    iwanka @ f_laugh a_dust "He like, almost never uses it."

    anon f_worried "So what, it just sits anchored out here?"

    iwanka "Cukup banyak."

    hide iwanka with dissolve
    anon f_normal "Sayang sekali."

    show anon with dissolve:
        flip
        xoffset -500
    pause
    iwanka "Well, he throws parties out here like twice a year..."

    iwanka "... But it's always just a bunch of old politicians and their trophy wives."

    anon "Jadi begitu."

    iwanka "It's not nearly as nice with old, wrinkly balls, and saggy tits scattered all over the place."

    anon f_disgusted "Y-yeah, that's really not something I wanna picture right now."

    show iwanka b_swimsuit a_glass with dissolve
    iwanka @ f_laugh "Phew, it feels so freaking good to get out of those smelly rags!"

    show anon f_surprised with dissolve:
        unflip
        xoffset 0
    pause
    anon f_normal "Wow, you look great!"

    iwanka @ f_laugh "Ya, saya tahu."

    iwanka "You want me to fix you a drink?"

    anon "T-tidak, tidak apa-apa."

    anon @ f_brag_closed "I'm the designated driver, remember?"

    iwanka f_smirk "Designated rower, you mean?"

    anon f_shy @ a_behind_head "Hehe, ya."

    show iwanka a_glass_drink f_drink with dissolve
    pause
    show iwanka a_glass f_normal with dissolve
    anon "So do your parents make you attend these parties?"

    iwanka @ f_eyeroll "Sayangnya ya."

    iwanka a_mime "\"We spent a lot of time and effort making you look that good, {b}Iwanka{/b}!\""

    iwanka "\"The least you can do is use it to further your father's career.\""

    show iwanka a_hip with dissolve
    anon f_worried "They don't make you like, you know?"

    iwanka f_suspicious @ -m_talk "Hmm?"

    anon "Sleep around or whatever?"

    iwanka f_annoyed "Are you asking me if my parents whore me out to potential investors?"

    anon @ a_frustrated "Ehh."

    anon f_worried "Well, I wasn't going to put it like that..."

    iwanka @ f_eyeroll "Heh, no, {b}[firstname]{/b}..."

    iwanka f_smirk "Nothing so objectionable."

    iwanka f_concerned "That being said, there is a certain expectation to flirt and coerce when the opportunity presents itself."

    anon "That sounds awful."

    iwanka a_glass f_normal @ f_eyeroll "Meh."

    iwanka "To be honest, it's a small price to pay for the lifestyle they provide me with."

    show iwanka a_glass_drink f_drink with dissolve
    pause
    show iwanka a_glass f_normal with dissolve
    anon "I can't imagine having expectations like that for one of my children."

    iwanka "It's just politics."

    pause
    anon "What other shady stuff are your parents into?"

    anon "You mentioned something about Russians the other day, I remember."

    iwanka f_suspicious "Wow, {b}[firstname]{/b}..."

    iwanka @ f_eyeroll "... Real subtle."

    anon f_shy "Saya minta maaf."

    iwanka "What's really going on here, dude?"

    anon f_worried @ -m_talk "Hmm?"

    iwanka "You keep trying to steer things back to my dad."

    anon @ a_point_self "Do I?"

    iwanka f_smirk "Don't be coy."

    iwanka "Just spit it out and lets be done with it."

    iwanka "I wanna enjoy at least some of this evening..."

    show anon f_sad_down
    pause
    anon "O-okay, umm..."

    anon f_worried "... You see, a few months ago, something really bad happened... To my family."

    iwanka f_suspicious "Oke?"

    anon f_sad_down "And well, there's quite a bit of evidence suggesting that the people responsible for this bad thing are working with your father."

    iwanka @ f_eyeroll "That's not surprising..."

    anon f_worried @ -m_talk "..."
    iwanka "So you're saying that my father and his Russian associates did something bad to your family and you want evidence to prove it?"

    anon "Y-yeah, that's the gist of it."

    iwanka @ f_thinking "Is it bad enough to put my father in prison for a long time?"

    anon "Well, assuming he played a part in it..."

    pause
    anon "... Yes, I should think so."

    iwanka f_thinking @ -m_talk "Hmm."

    iwanka f_smirk "Well, whatever I can do to help, consider it done."

    anon f_surprised "!!!"
    anon "Wait, just like that?"

    iwanka f_eyeroll "Hmm, ya."

    iwanka f_annoyed "I hate my father."

    iwanka f_smirk "Haven't you figured that out yet?"

    anon f_worried "saya-"

    pause
    anon "I don't know what to say..."

    iwanka "Well, you could start by saying, \"Thank you...\""

    anon f_normal "Of course, you have no idea how much this means to me!"

    show iwanka a_glass_drink f_drink with dissolve
    anon "Terima kasih banyak!"

    show iwanka a_glass f_normal with dissolve
    anon f_normal_low "Phew, this is just such a relief."

    show anon f_worried a_frustrated with dissolve:
        xoffset -500
        flip
    anon "I've just been chasing down leads on these assholes for what feels like forever..."

    show iwanka f_lipbite
    show anon a_idle with dissolve
    anon "... And every time I think I'm getting somewhere, something goes wrong!"

    show iwanka a_undress f_smirk_down with dissolve
    pause
    show iwanka b_swimsuit_undress2 with {'master': dissolve}
    anon "Your father is literally the last avenue I have left of solving this..."

    show iwanka b_naked a_undress_swimsuit3 f_smirk with dissolve:
        xoffset 750
        flip
    pause 0.5
    hide iwanka with {'master': dissolve}
    anon "I'm just so thankful that you're willing to help, {b}Iwanka{/b}."

    show anon with dissolve:
        xoffset 0
        unflip
    anon "Anything I can do to make it up to you, just let me know and I'll-"

    show anon f_shock a_sides with dissolve
    pause
    show iwanka b_undress
    anon "!!!" with hpunch
    iwanka "Oh, I can think of a few things..."

    anon "A-apa yang kamu-"

    iwanka "You can start by joining me for a swim."

    anon "You wanna swim... Now?"

    iwanka @ -m_talk "Mhmm."


    scene expression background(200, 400, 2.6, l=L_boat_bridge) as stage
    show anon f_worried a_behind_head
    show iwanka b_naked f_smirk a_hip
    with fade
    anon "Telanjang?"

    iwanka "You've never been skinny dipping before?"

    anon "N-no, not really..."

    iwanka @ f_laugh "Well, there's no time like the present!"

    hide iwanka
    show anon a_frustrated
    with dissolve
    anon "Kamu tidak bisa serius..."


    scene location_boat_cutscene_04 with fade
    anon "{b}Iwanka{/b}!!"


    scene black
    show text _ ("{i}*Splash*{/i}") at truecenter
    with fade
    pause 1.

    scene expression background(96, 344, 5.75, l=L_boat_bridge) as stage
    show anon f_surprised_low a_sides:
        flip
        xoffset -500
    with fade
    anon "Sialan!"

    anon "You're crazy!!"


    scene location_boat_cutscene_05 with fade
    iwanka "Heh, it's your turn!"

    anon "I'm not sure I can..."

    iwanka "Ayolah!"

    iwanka "You can't back out now!!"


    scene expression background(96, 344, 5.75, l=L_boat_bridge) as stage
    show anon f_worried_low a_sides:
        flip
        xoffset -500
    with fade
    anon "Isn't there something else-"

    iwanka "Jump you coward!"

    anon f_unimpressed "I am not a coward!"

    iwanka "Really, because you look like one from down here!"

    anon f_eyeroll "Uh, baiklah!"

    show anon b_dressed_changing3 with dissolve:
        unflip
        xoffset 0
    pause
    show anon b_dressed_changing2 with dissolve
    iwanka "Woo!!"

    show anon b_naked_undress_bottom with dissolve
    iwanka "Take it off, baby!!"

    show anon b_naked a_rub f_skeptical od_naked_dick1 with dissolve
    anon "How do I always get talked into stuff like this?"


    scene location_boat_cutscene_06 with fade
    anon "Here I come!!"


    scene black
    show text _ ("{i}*Splash*{/i}") at truecenter
    with fade
    pause 1.

    scene location_boat_water
    show anon b_swim f_worried
    show iwanka b_swim f_smirk
    with fade
    anon "Holy crap, this water is freezing!"

    iwanka @ f_laugh "hehe!"

    iwanka "It's not so bad..."

    anon "Ya benar."

    iwanka f_excited "Check out that sunset, though."

    show anon f_normal with dissolve:
        flip
        xoffset -500
    pause
    anon "Whoa."

    iwanka "Beautiful, isn't it?"

    anon m_talk "Y-yeah, very beautiful."

    show anon f_unimpressed with {'master': dissolve}:
        unflip
        xoffset 0
    anon -m_talk "I bet it would look even more beautiful from the nice, warm, deck of the yacht..."

    show anon f_worried
    iwanka @ f_eyeroll "Oh em gee, you are such a baby!"

    show iwanka f_smirk with dissolve:
        xoffset -250
    iwanka "Let me warm you up."

    anon @ -m_talk "Hmm?"

    hide anon
    show iwanka b_swim_kiss1:
        xoffset 0
    with dissolve
    anon "!!!"
    show iwanka b_swim_kiss
    pause
    show anon b_swim f_shy behind iwanka
    show iwanka b_swim:
        xoffset -250
    with dissolve
    iwanka "Apakah itu lebih baik?"

    anon "Yeah, a little bit..."

    anon "... We should probably keep doing that."

    iwanka @ f_laugh "hehe!"

    hide anon
    show iwanka b_swim_kiss:
        xoffset 0
    with dissolve
    pause
    iwanka "MM."

    pause
    show anon b_swim f_shy behind iwanka
    show iwanka b_swim:
        xoffset -250
    with dissolve
    iwanka "Warmer?"

    anon "I'm getting there."

    hide anon
    show iwanka b_swim_kiss:
        xoffset 0
    with dissolve
    pause
    show anon b_swim f_flirt behind iwanka
    show iwanka b_swim:
        xoffset -250
    with dissolve
    anon "Much better, thank you."

    iwanka "Terima kasih kembali."

    pause
    anon "C'mon, let's head back to the boat."

    iwanka @ f_suspicious "Tsk, already?"

    anon f_worried "I'm just saying, there could be sharks out here."

    iwanka @ f_eyeroll "Oh, there's no sharks out here!"

    anon f_surprised "There are absolutely sharks out here!"

    pause
    anon "And sting rays..."

    iwanka @ f_laugh "Tidak uh!"

    anon f_worried "Jellyfish."

    pause
    anon "Electric eels."

    iwanka @ f_laugh "Haha, you're so full of it!"

    anon f_normal "Heh, I'm serious!"

    iwanka f_smirk "What about octopuses?"

    anon f_laugh "Oh, you'd like that wouldn't you?"

    iwanka @ f_laugh "Diam!"

    anon "hehe!"

    show anon f_normal
    iwanka @ f_lipbite -m_talk "MM."

    pause
    iwanka "Okay, fine!"

    iwanka "We'll head back."

    anon @ f_laugh "Ya!!"

    hide iwanka with dissolve
    iwanka "But if you want my help with my father, you're gonna have to earn it!"

    anon f_skeptical "What the heck does that mean?"


    scene expression background(208, 400, 2.5, l=L_boat_bridge) as stage
    show anon b_naked od_naked_dick1 a_cold f_worried:
        xoffset -50
    show iwanka b_naked
    with slowfade
    anon "Brr, my nipples could cut diamonds right now!"

    iwanka f_laugh a_nipple "Heh, mine too."

    show anon f_flirt
    show iwanka f_smirk -a_nipple
    with dissolve
    pause
    show iwanka a_towel_throw f_normal with dissolve:
        flip
        xoffset 680
    pause
    show iwanka a_towel_throw f_smirk with {'master': dissolve}:
        unflip
        xoffset 80
    iwanka "Here, dry off."

    show anon a_towel
    show anon_arms_naked_a_towel:
        xoffset -50
    show iwanka a_towel_throw:
        flip
        xoffset 680
    with dissolve
    anon "Terima kasih."

    show iwanka a_towel f_smirk_down with dissolve:
        unflip
        xoffset 0
    with dissolve
    pause
    show iwanka b_naked_bend a_idle
    show anon f_flirt_low
    with dissolve
    iwanka "I don't wanna get the sheets all wet."

    anon f_worried_low @ f_skeptical "Sheets?"

    anon "What exactly are you planning?"

    show iwanka a_towel b_naked f_smirk
    show anon f_worried
    with dissolve
    iwanka "We're naked and alone on my father's yacht, {b}[firstname]{/b}..."

    iwanka "... Take a wild guess."

    show iwanka b_naked_bend a_idle with dissolve
    show anon f_shock
    pause
    anon f_shy_low "Y-maksudmu-"

    show iwanka a_nipple b_naked
    show anon f_shy
    with dissolve
    iwanka "It's been over a month since I came home from college and I haven't been properly fucked since!"

    anon "This is really happening?!"

    iwanka @ -m_talk "Mhmm!"

    iwanka "Just remember to pull out because my dad will absolutely kill us both if I get pregnant."

    anon "{i}*Gulp*{/i} Y-ya, oke."

    hide anon_arms_naked_a_towel
    show anon b_empty f_surprised od_empty:
        xoffset 0
    show iwanka b_naked_pulling_anon behind anon
    with dissolve
    iwanka "Ayo."

    anon @ -m_talk "!!!"

    call scene_iwanka_sex
    $ unlock_scene('iwanka', '02_unlocked', variant='first')

    scene location_boat_interior_bed_closeup
    show iwanka b_onbed_cuddle_naked f_content_closed
    show anon b_empty f_flirt_low:
        xzoom -1
        offset (84, -17)
    show anon_overlay_dick_onbed_naked_od_dick1
    with fade
    iwanka "Mmm, I needed that so bad..."

    pause
    iwanka "You have an amazing dick, {b}[firstname]{/b}!"

    anon "Hehe, terima kasih."

    pause
    iwanka @ -m_talk "MM."

    iwanka "This feels nice."

    pause
    anon "You're not falling asleep on me, are you?"

    pause
    anon "{b}Iwanka{/b}?"

    iwanka @ -m_talk "Hmm?"

    anon "We have to get you back home soon or someone will notice you're missing."

    iwanka f_snob "Aww, but I don't wanna go back!"

    anon "I know you don't..."

    anon "... But I need your help with your father, remember?"

    iwanka "{i}*Huh*{/i} Ya, saya tahu."

    pause
    iwanka f_excited_up "What are you hoping to get, anyways?"

    anon f_normal "Aku tidak tahu."

    show iwanka f_content_closed
    pause
    anon f_confused "Something that proves he's working with the Russians?"

    pause
    anon f_flirt_low "I was kinda hoping you'd have an idea..."

    pause
    iwanka f_excited_up "Well, he keeps all his business stuff in his office."

    anon "Yeah, I kinda figured that would be the best place to look."

    iwanka "I can give you the code to get in but the guards will stop you."

    anon f_worried_low "You can't send them away or something?"

    iwanka f_snob "No, they don't take orders from me."

    iwanka "Especially now that my father has me on house arrest."

    pause
    iwanka "My parents are the only ones they'll listen to."

    show iwanka f_content_closed
    anon f_thinking "Your parents, huh?"


    if M_melonia.finished_state(S_mel05_init):
        iwanka "Why don't you just ask my mother to send them away?"

        show anon f_flirt_low
        iwanka "I mean, you two are fucking, aren't you?"

        pause
        anon "You think she would do it?"

        iwanka "Probably."

        iwanka @ f_excited_up "She hates him almost as much as I do."

        pause
        anon "Alright, I'll ask her."

    else:

        anon @ -m_talk "( Maybe I can get {b}Mrs. Rump{/b} to help me? )"

        anon f_normal @ -m_talk "( I should {b}speak with Ricky{/b} about that job she offered me. )"

        pause
        anon f_flirt_low "I guess it's something I'll have to figure out on my own."


    anon "In the meantime, we should probably get you back to the mansion."

    iwanka "Ya baiklah."

    iwanka f_excited_up "But we should definitely do this again sometime, don't you think?!"

    anon "Yeah, I'm down for that."

    iwanka @ f_laugh "Hehe, yay!"


    scene expression background(l=L_rump_front)
    show anon
    show iwanka b_maid f_excited o_glasses
    with slowfade
    iwanka "Thanks for tonight, {b}[firstname]{/b}."

    iwanka "I'm pretty sure I can sneak out anytime I want now with this disguise you got me."

    anon "Yeah, it's no problem."

    anon "I'm happy to help."

    iwanka f_smirk "And happy to wax this ass too, I'll bet?"

    anon f_flirt @ a_point "Heh, that too."

    iwanka "If you ever feel like doing it again, I'll meet you {b}on the yacht in the evenings{/b}... Okay?"

    anon f_normal "Alright, that sounds like a plan."

    iwanka "Oke."

    show iwanka f_excited
    pause
    iwanka "Well, goodnight."

    show iwanka b_maid_kiss o_empty:
        xoffset -200
    hide anon
    with dissolve
    pause
    show anon f_shy a_behind_head behind iwanka
    show iwanka b_maid f_smirk o_glasses:
        xoffset 0
    with dissolve
    anon "Y-ya."

    anon a_idle @ a_wave "{i}*Ahem*{/i} Goodnight, {b}Iwanka{/b}."

    iwanka @ f_laugh a_dust "hehe."

    hide iwanka with dissolve
    anon f_grin @ f_brag_closed "Wah!"

    pause
    anon @ -m_talk "( Alright, that takes care of the code. )"

    anon @ a_cheering -m_talk "( Now I just need to get rid of the guards and into that office! )"

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
