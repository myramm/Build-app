label jen0m_food_home_kitchen:
    scene expression background() as stage
    show jenny a_sides b_dressed_pregnant_belly f_sexy_down:
        xoffset 600
        xzoom -1
    show debbie f_surprised_worried:
        xoffset 450
        xzoom -1
    debbie "Are you sure about this, dear?"

    show jenny f_happy:
        xoffset 175
        xzoom 1
    with {'master': dissolve}
    jenny "Yes, I'm sure."

    show anon f_happy:
        xoffset -100
    show debbie f_sorry
    with {'master': dissolve}
    debbie "Peanut butter pancakes is one thing but then topping it with cottage cheese and applesauce..."

    show anon f_confused
    jenny "And green olives."

    show debbie f_gross_back
    anon f_disgusted "Please, tell me I didn't just hear that..."

    debbie f_gross "It does sound awful, dear."

    jenny f_upset "Well, I don't care... I want it!"

    pause
    jenny "It's not my fault I'm pregnant and hormonal."

    show debbie f_gross_back
    anon f_brag "Tidak?"

    show anon a_point f_flirt
    with {'master': dissolve}
    anon "I mean, it's at least half your fault... right?"

    show debbie f_sorry
    show jenny a_upset f_angry
    with {'master': dissolve}
    pause
    show anon a_pocket
    show debbie b_robe_hug_jenny_sad behind jenny:
        xoffset 400
    show jenny a_empty b_empty:
        align (.5, .5)
        offset (400 - 213, 53)
        rotate -7.5
    with {'master': dissolve}
    debbie "Tidak apa-apa."

    show jenny f_upset
    debbie f_normal "If that's what my girl wants for breakfast, I'll do it."

    show jenny f_happy
    pause
    anon f_unimpressed "Bruto."

    show anon a_surprised_up_both f_surprised_teeth
    show debbie a_facepalm b_robe f_eyeroll:
        xoffset 500
    show jenny a_upset b_dressed_pregnant_belly f_angry behind debbie:
        reset
        offset (-375, 0)
    with {'master': fastdissolve}
    jenny "Ugh, shut up, {b}[firstname]{/b}!"

    show anon a_surprised_up f_surprised:
        xoffset -225
    show debbie f_sad_closed
    with {'master': dissolve}
    jenny "You're the one who put this stupid baby in-"

    show anon f_shock
    show jenny f_surprised
    pause
    show anon a_sides f_worried_surprised
    show debbie a_sides f_surprised:
        xoffset 50
        xzoom 1
    with dissolve
    show jenny f_surprised_back
    with fastdissolve
    pause .3
    show jenny f_surprised_down
    with fastdissolve
    pause .3
    show jenny f_surprised_down_back
    with fastdissolve
    pause .3
    show jenny f_concerned_low
    with fastdissolve
    pause .3
    show jenny f_concerned
    with {'master': fastdissolve}
    jenny "Umm, I mean-"

    show jenny a_pregnant_touch f_concerned_back
    with {'master': dissolve}
    jenny "Put this baby in a bad mood..."

    show anon f_confused
    show debbie f_curious
    jenny f_upset "... with your loud music!"

    debbie "Music, dear?"

    jenny f_upset_back "Yes, {b}[firstname]{/b} was blaring loud music late last night and I couldn't sleep..."

    jenny f_upset "... Right?!"

    anon "Hah?"

    pause
    show anon a_behind_head f_shy behind jenny
    with {'master': dissolve}
    anon "Oh, y-yeah!"

    anon f_normal "I guess, I sorta was doing that..."

    show debbie f_sad
    pause
    show anon a_sides f_worried_down
    with {'master': dissolve}
    anon "... Sorry, {b}[jen_name]{/b}."

    debbie f_curious "I never heard any music."

    show anon f_worried
    show jenny f_concerned behind anon:
        xoffset 0
        xzoom -1
    with {'master': dissolve}
    jenny "Ya, baiklah..."

    jenny "... That's probably because you're such a heavy sleeper."

    debbie f_normal "Oh."

    debbie "Yeah, I suppose that makes sense."

    pause
    show jenny a_crossed f_confused
    with {'master': dissolve}
    jenny "{i}*Ehem*{/i}"

    show anon f_confused
    show debbie f_curious
    pause
    jenny f_upset "Would you focus on my food, please?"

    show anon f_eyeroll
    jenny "I don't want it burned."

    show anon f_tired
    show debbie a_idle:
        xoffset 600
        xzoom -1
    with {'master': dissolve}
    debbie f_normal "Oh, the food isn't going to burn, dear..."

    show anon_arms_naked_a_wipe as arm:
        crop (0, 0, 1024, 350)
        xoffset -225
    show anon f_drink
    show jenny a_sides f_drink
    with {'master': fastdissolve}
    pause
    hide arm
    show anon f_normal
    show jenny f_normal
    with {'master': dissolve}
    debbie "... It's fine."

    show anon a_pocket f_unimpressed
    hide debbie
    with {'master': dissolve}
    anon "Nothing about that food is fine."

    show jenny f_upset_back
    anon "It's an abomination."

    show jenny a_upset f_angry:
        xoffset -375
        xzoom 1
    with {'master': dissolve}
    jenny "Permisi?!"


    if M_jenny.get('dominance') <= 0:
        show anon a_sides f_sad_down
        with {'master': dissolve}
        anon "T-tidak ada."

        show jenny a_sides f_sexy
        with {'master': dissolve}
        jenny @ -m_talk "Mhmm."

        anon @ -m_talk "..."
        show debbie a_pancakes:
            xoffset 225
            xzoom 1
        show jenny f_normal_back:
            xoffset 0
            xzoom -1
        with {'master': dissolve}
        jenny "That's what I thought."

    else:

        show jenny f_upset
        anon f_annoyed "{b}[jen_name]{/b}, I'm not eating peanut butter pancakes with applesauce and cottage cheese..."


        show jenny a_crossed f_grin
        with {'master': dissolve}
        jenny "And green olives!"

        anon f_disgusted "Yeah, eww."

        show debbie a_pancakes:
            xoffset 225
            xzoom 1
        with {'master': dissolve}
        anon f_unimpressed "Please, tell me you're making normal food too?"

        show jenny f_normal_back:
            xoffset 0
            xzoom -1
        with {'master': dissolve}

    debbie "Here you go, {b}[jen_name]{/b}."

    show jenny f_happy a_pregnant_belly_gimme
    with {'master': dissolve}
    jenny "Oh, gimme, gimmie!!"

    anon f_disgusted @ -m_talk "..."
    show debbie a_sides f_excited:
        xoffset 0
    show jenny a_pregnant_belly_pancakes f_happy_closed
    with {'master': dissolve}
    jenny "Mmm, it smells perfect!"

    show debbie f_normal
    hide jenny
    with {'master': dissolve}
    pause
    show anon f_worried:
        xoffset -50
    with {'master': dissolve}
    anon "{b}[deb_name]{/b}?"

    debbie f_curious @ -m_talk "Hmm?"

    anon f_worried "You made normal food too, right?"

    debbie f_normal "Of course, dear."

    show anon f_shy
    debbie "It's waiting for you on the table."

    anon f_happy "Manis!"

    show anon a_empty b_empty f_happy:
        xoffset 0
    show debbie b_robe_hug_mc behind anon:
        xoffset 0
    with {'master': dissolve}
    debbie "Anything for you, sweetie."


    if M_debbie.finished_state(S_debbie_night_visit_three):
        show anon f_flirt
        pause
        hide anon
        show debbie b_robe_kiss_mc:
            xoffset -250
        with {'master': dissolve}
        debbie @ -m_talk "MM."

        pause
        show anon a_sides f_flirt behind debbie:
            xoffset 50
        show debbie a_mouth_shock b_robe f_surprised_worried:
            xoffset -125
        with {'master': dissolve}
        debbie "{b}[firstname]{/b}!!"

        debbie "{b}[jen_name]{/b} is right in the other room!"

        anon a_rub f_shy "Anda benar, saya minta maaf."

        show debbie a_nervous o_blush
        with {'master': dissolve}
        anon "You just smell so good, I couldn't help myself."

        show anon a_sides
        with {'master': dissolve}
        debbie f_normal "Well, save it for later, okay?"

        anon f_flirt @ -m_talk "Mhmm."

        debbie "Now go eat your breakfast!"

        debbie "I want my boy big and strong."

        show anon a_salute f_happy
        show debbie -o_blush
        with {'master': dissolve}
        anon "Ya, Bu."

        hide anon
        with {'master': dissolve}
        debbie f_laugh "hehe."


    scene location_home_dining_day as stage
    show jenny a_eat b_breakfast_dressed_eat_pregnant_belly
    show overlay_o_dinner_table as table
    show overlay_o_dinner_plate_breakfast as plate:
        xoffset 150
    show overlay_o_dinner_bowl1 as bowl:
        xoffset 125
    with fade
    jenny "Om, nom, nom!"

    show anon b_dinner_sitting f_disgusted_left_low behind jenny
    with {'master': dissolve}
    pause
    show jenny a_pregnant_spoon b_breakfast_dressed_pregnant_belly f_upset
    with {'master': dissolve}
    pause
    jenny "Apa?!"


    if M_jenny.get('dominance') <= 0:
        show anon a_bowl f_worried_low
        with {'master': dissolve}
        anon "Tidak ada apa-apa."

    else:

        anon f_disgusted_left "I can't believe you're eating that."

        jenny "Would you drop it already?!"

        jenny "Why does it matter?"

        anon f_disgusted_low "It doesn't, I suppose."


    show anon a_eat f_eat
    show jenny a_eat b_breakfast_dressed_eat_pregnant_belly
    with {'master': dissolve}
    jenny "Om, nom, nom."

    pause
    show anon a_bowl1 f_confused_back_low
    with {'master': dissolve}
    anon "So you really doing a show today?"

    show anon f_confused_back
    show jenny a_pregnant_spoon b_breakfast_dressed_pregnant_belly f_upset
    with {'master': dissolve}
    jenny "Umm, yeah..."

    show anon f_worried_left
    jenny "... I told you, people pay out the nose for this kinda thing!"

    jenny "We have to strike while the iron is hot."

    anon f_unimpressed_left "The iron in this case being our unborn child..."

    jenny "Relax, it'll be fine."

    anon "Jika kamu berkata begitu..."

    show anon a_eat f_eat
    show jenny a_eat b_breakfast_dressed_eat_pregnant_belly
    with {'master': dissolve}
    pause
    jenny "Om, nom."

    pause
    show anon a_bowl1 f_worried_back_low
    with {'master': dissolve}
    anon "There's not going to be kissing involved, is there?"

    show anon f_worried_left
    show jenny a_pregnant_spoon b_breakfast_dressed_pregnant_belly f_confused
    with {'master': dissolve}
    jenny @ -m_talk "Hmm?"

    show anon f_disgusted_left_low
    jenny "Why would there be-"

    show jenny f_confused_low
    pause
    jenny f_upset "Oh, I get it... Hah, hah."

    show anon a_bowl f_flirt
    show jenny f_eyeroll
    with {'master': dissolve}
    pause
    show anon a_eat f_eat
    with {'master': dissolve}
    jenny f_upset "Sangat lucu."

    show jenny a_eat b_breakfast_dressed_eat_pregnant_belly
    with {'master': dissolve}
    jenny "Om."

    pause
    show jenny a_pregnant_spoon b_breakfast_dressed_pregnant_belly
    with {'master': dissolve}
    jenny "Doofus."


    if M_jenny.get('dominance') <= 0:
        anon @ -m_talk "..."
    else:

        show anon a_resting f_flirt_left
        with {'master': dissolve}
        anon "Says the girl begging me to have sex with her."

        show jenny f_angry_pouting_top
        with {'master': dissolve}
        pause
        jenny f_upset_back_low "Apa pun."

        pause

    show anon f_confused_back
    show jenny f_grin_down
    pause
    hide plate
    show anon a_resting f_shock_left
    show jenny a_pregnant_plate b_breakfast_dressed_pregnant_belly f_happy_closed
    with {'master': dissolve}
    jenny @ -m_talk "Hmm!"

    anon f_disgusted_left "Ya."

    pause
    show overlay_o_dinner_plate_empty as plate:
        xoffset 300
    show jenny a_pregnant_spoon f_happy o_pancake_dirt
    with {'master': dissolve}
    jenny "Fuck, that was good!"

    anon "Eh ya."

    show anon f_surprised_left
    show jenny b_breakfast_gettingup_pregnant_belly f_sexy_down
    with {'master': dissolve}
    jenny "Alright, now I'm ready for that deep dicking."

    show jenny a_sides b_breakfast_standing_pregnant_belly
    with {'master': dissolve}
    anon f_confused_back "Hah?"

    jenny "It's showtime, let's get upstairs and do this!"

    anon "W-wait, I-"

    hide anon
    show jenny b_breakfast_pulling_pregnant_belly f_grin
    with {'master': dissolve}
    pause
    hide jenny
    with {'master': dissolve}
    anon "{b}[jen_name]{/b}, I'm still hungry!!"

    jenny "Good, because we might start with you eating my pussy."

    anon "Argh!!"


    scene expression background(240, 352, 2.2, l=L_home_sisbedroom, o=1) as stage
    show anon a_sides f_worried
    show jenny a_pregnant_belly_remove_panties b_dressed_pregnant_belly f_grin_down o_pancake_dirt
    with fade
    anon "Hmm..."

    show anon f_worried_low
    show jenny b_dressed_pregnant_belly_panties_remove_down
    with {'master': dissolve}
    pause
    show anon f_flirt_low
    show jenny b_naked_pregnant_belly_pull1
    with {'master': dissolve}
    pause
    show jenny b_naked_pregnant_belly_pull2
    with dissolve
    show jenny b_naked_pregnant_belly_pull3
    with dissolve
    show jenny b_naked_pregnant_belly_pull4 -o_pancake_dirt
    with dissolve
    show jenny a_hips b_naked_pregnant_belly
    with {'master': dissolve}
    jenny f_upset "Apa yang kamu lakukan?"

    show anon a_behind_head f_worried
    with {'master': dissolve}
    anon "aku uhh..."

    jenny "Get naked!"

    show anon a_sides
    with {'master': dissolve}
    anon "Don't you wanna, like... shower first?"

    jenny "Tidak."

    pause
    jenny f_confused "Why, do I smell?"

    anon "Well, no... I just-"

    jenny "Then why are you being such a baby today?!"

    show anon f_grumpy
    jenny "We've had sex like a dozen times!"

    show jenny a_touch f_upset
    with {'master': dissolve}
    jenny "I'm pregnant with your child for fucks sake!"

    show anon a_crossed
    with {'master': dissolve}
    anon "I'm not being a baby!"

    jenny "Ya, benar!"

    anon f_skeptical "Could you, just please, go brush your teeth before we start?!"

    jenny f_sexy "Mengapa?"

    show anon a_frustrated f_annoyed
    with {'master': dissolve}
    anon f_annoyed "You know I hate olives!"

    jenny f_eyeroll "It's not like we're gonna be kissing or anything..."

    show anon a_cover_boner f_disgusted
    with {'master': dissolve}
    anon "Yeah, well... I don't want my dick to smell like cottage cheese and peanut butter!"

    jenny f_laugh "Hah!"

    show anon f_confused
    pause
    jenny f_sexy "If you think I'm sucking your dick today, you're out of your mind, {b}[firstname]{/b}."

    show anon a_sides f_grumpy
    with {'master': dissolve}
    jenny f_upset "Now seriously... clothes off and mask on!"

    anon f_squint @ -m_talk "Grr."

    show anon b_dressed_changing3:
        xoffset -500
        xzoom -1
    show jenny f_sexy_down
    with {'master': dissolve}
    pause
    show anon a_towel b_shorts f_looking_down
    show jenny f_sexy
    with {'master': dissolve}
    pause
    show anon b_dressed_changing2
    show jenny f_normal_low:
        xoffset 500
        xzoom -1
    with {'master': dissolve}
    pause
    show anon b_underwear f_confused_back_low
    show jenny b_naked_pregnant_belly_pickup
    with {'master': dissolve}
    pause
    show anon a_rub f_surprised:
        xoffset 0
        xzoom 1
    show jenny a_jersey b_naked_pregnant_belly
    with {'master': dissolve}
    anon "What the hell is that thing?"

    show jenny a_show b_jersey_pregnant_belly f_sexy:
        xoffset 0
        xzoom 1
    with {'master': dissolve}
    jenny "It's a football jersey from college."

    jenny "I ordered it a few days ago."

    show anon a_sides f_confused
    with {'master': dissolve}
    anon "Okay, but why?"

    show jenny a_touch f_normal
    with {'master': dissolve}
    jenny "Because my fans don't know I'm pregnant and I wanna make a show of the unveiling."

    anon "Unveiling?"

    jenny "Yeah, you know... tease them a little?"

    pause
    jenny "It's the best way to get tips."

    anon "But what does the jersey have to do with-"

    jenny f_upset "Ugh, just shut up and get on the bed!"

    hide jenny
    with {'master': dissolve}
    jenny "Jesus, it's like pulling teeth with you sometimes..."

    anon f_sad_down "{i}*Huh*{/i}"

    hide anon with dissolve

    scene location_home_jennybedroom_closeup_peek
    show anon b_bed_jenny_sit_back f_confused of_mask
    show jenny b_jersey_bed_side f_normal
    show jenny_overlay_o_laptop as laptop
    with fade
    anon "You're not getting on the bed?"

    jenny "No, I'm going to start down here so they can't see my belly."

    anon f_normal "Oh."

    pause
    jenny "Just relax and keep your mouth shut."

    anon f_worried "Ya, ya..."

    show jenny b_jersey_bed_side_laptop f_normal_low
    with {'master': dissolve}
    pause
    jenny "Oke..."

    show anon f_normal_low
    show jenny a_laptop
    with {'master': dissolve}
    jenny "... Here we go."

    pause
    show jenny f_happy_down
    pause
    jenny "Hey there, boys!"

    jenny "Did you miss me?!"

    pause
    jenny "I know I've been gone a while."

    pause
    jenny "No, I'm not dead."

    jenny "I've just been busy, that's all."

    pause
    jenny "Well, you know... being a sex goddess is time consuming work."

    pause
    jenny f_sexy_down "You'll find out why in a second."

    pause
    jenny "That's right, sam9, special show today."

    pause
    jenny "No, it's going to be even more special than that!"

    pause
    jenny "That's right, better than anal."

    pause
    jenny "Yes, I'm serious."

    pause
    show anon f_surprised_low
    jenny f_eyeroll "No, it's not double anal."

    pause
    show anon f_normal
    jenny f_upset_down "I said, I'll tell you in a second... sheesh."

    jenny f_normal_low "I'm just waiting for the room to fill a bit."

    show anon f_normal_low
    pause
    jenny "Aww, I know..."

    pause
    jenny "... I'll be back to my regular schedule soon guys."

    pause
    show anon f_confused_low
    show jenny b_jersey_bed_side f_normal
    with {'master': dissolve}
    jenny @ -m_talk "Mhmm."

    show anon f_confused
    show jenny a_side
    with {'master': dissolve}
    jenny "It's the same guy."

    show anon f_flirt
    show jenny b_jersey_bed_side_laptop f_normal_low
    with {'master': dissolve}
    pause
    show anon f_flirt_low
    jenny "Tentu saja."

    show jenny a_laptop
    with {'master': dissolve}
    jenny "I wouldn't settle for anything but the best."

    show anon f_flirt_grin
    show jenny f_sexy_down
    pause
    jenny "Yeah, he wishes."

    show anon f_confused_low
    pause
    show anon f_confused
    jenny "Heh, it would take a lot more than a big ass ring."

    anon "Apa yang kamu bicarakan?"

    show jenny a_side b_jersey_bed_side f_angry
    with {'master': dissolve}
    jenny @ -m_talk "Shh!!!"

    show anon f_worried_down
    show jenny f_upset
    pause
    show jenny a_laptop b_jersey_bed_side_laptop f_normal_low
    with {'master': dissolve}
    pause
    jenny "Alright, it looks like we're filling up pretty nicely."

    show anon f_worried_low
    jenny "You boys ready to find out where I've been and what we're doing today?"

    "{i}*PING*{/i} {i}*PING*{/i}"

    jenny "Aww, c'mon... you can do better than that."

    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"

    show anon f_normal_low
    jenny f_happy_down "That's better!"

    pause
    jenny "So, the reason I haven't been around..."

    show anon f_normal
    show jenny b_jersey_bed_climb
    with {'master': dissolve}
    jenny "... Is because..."

    show jenny a_idle b_bed_jersey
    with {'master': dissolve}
    jenny "... My little boy toy here put a baby in me!"

    show anon f_normal_low
    pause
    jenny "Yes, it's real."

    pause
    jenny f_upset_down "No, it wasn't planned."

    show anon f_surprised
    pause
    jenny "Hmm, ya."

    show anon f_normal_low
    pause
    jenny "It's a bit late for that, don't you think?"

    pause
    jenny f_normal_low "You wanna see?"

    pause
    jenny f_sexy_down "Do you {i}REALLY{/i} wanna see?"

    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"

    show anon f_flirt
    show jenny a_lift
    with {'master': dissolve}
    pause
    show jenny a_surprise b_bed_jersey_belly
    with {'master': dissolve}
    pause
    jenny "Heh, I told you!"

    show anon f_flirt_low
    pause
    jenny a_touch "Aku tahu."

    pause
    jenny "Umm, it could be twins... I don't know."

    pause
    show anon f_shock_low
    show jenny a_touch2 f_upset_down
    with {'master': dissolve}
    jenny "Yes, sam9... I know you can't get pregnant that way."

    show anon f_surprised
    jenny @ f_eyeroll "I'll keep it in mind going forward."

    show anon f_surprised_low
    pause
    show anon f_normal_low
    jenny f_happy_down "Oh, you do like it, huh?"

    show anon f_shy_low
    jenny "I had a feeling you might."

    pause
    jenny f_sexy_down "The real question is, how much do you like it?"

    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"

    show jenny a_lift2
    with {'master': dissolve}
    pause
    show anon f_flirt
    show jenny b_bed_jersey_boobs a_lift3
    with {'master': dissolve}
    jenny "Aaaaand how about now?"

    show anon f_flirt_low
    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"

    show anon f_happy
    jenny f_laugh "Hehehe!"

    show anon f_shy_low
    pause
    show anon f_confused_low
    jenny f_happy_down "Aku tahu!"

    pause
    show anon f_worried_low
    jenny a_down "Ya, tentu saja."

    pause
    show anon f_surprised_low
    jenny "Ya."

    pause
    jenny f_sexy_down "If you tip me well enough."

    show anon f_surprised
    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"

    jenny "Hehe, baiklah."

    jenny "Di Sini."

    show anon f_happy
    show jenny a_squeeze
    with {'master': dissolve}
    pause
    show anon f_flirt_grin
    show jenny a_squeeze1
    with {'master': dissolve}
    jenny "Did you see it?"

    pause
    show anon f_flirt
    show jenny a_squeeze
    with {'master': dissolve}
    jenny "See?!"

    pause
    show jenny a_squeeze1 f_laugh
    with {'master': dissolve}
    jenny "Hehehe!"

    jenny f_normal_low "No, I haven't tasted it."

    show anon f_confused_low
    pause
    show anon f_worried_low
    jenny "No, he hasn't either."

    pause
    show anon f_surprised_low
    jenny f_upset_down "No, I'm not sending you any!"

    pause
    show anon f_shock_low
    show jenny a_down f_surprised_down
    with {'master': dissolve}
    jenny "Wait, how much?!"

    show anon f_surprised_low
    pause
    show anon f_squint
    pause
    anon f_angry @ f_annoyed "{b}[jen_name]{/b}!"

    jenny f_eyeroll "{i}*Huh*{/i}"

    jenny f_upset_down "No, really... I can't."

    show anon f_shy
    jenny "Sorry, boys."

    show anon f_shy_low
    pause
    jenny "Because my boyfriend would get all pissy if I sent you some..."

    pause
    show jenny f_surprised_down
    anon f_surprised @ -m_talk "!!!"
    jenny f_concerned_back "Err, I mean-"

    jenny f_concerned_low "M-my boy toy!"

    pause
    jenny f_upset_down "He is {i}NOT{/i} my boyfriend!"

    anon f_flirt "But you just said I was."

    show jenny b_bed_jersey_boobs_back
    with {'master': dissolve}
    jenny f_upset "No I didn't."

    show anon f_laugh
    pause
    anon f_happy "Heh, yes, you did!"

    jenny f_upset "Diam!"

    anon f_laugh "Hehehe!"

    show jenny b_bed_jersey_boobs
    with {'master': dissolve}
    jenny f_gross_down @ -m_talk "Grr!!"

    show jenny f_upset_down
    pause
    jenny "Oh my god, he is {i}SO{/i} not!"

    pause
    jenny "Eugh, whatever."

    jenny "I'm flipping this over to subscribers only..."

    jenny "... So if you wanna see your pregnant sex goddess get fucked, then pay up!"

    pause
    show jenny b_bed_jersey_boobs_back
    with {'master': dissolve}
    jenny f_angry "Stop laughing!"

    anon f_happy "Heh, I'm sorry..."

    anon "... It's just funny."

    jenny f_eyeroll "{i}*Sigh*{/i} It was a slip of the tongue..."

    show jenny b_bed_jersey_boobs f_upset_down
    with {'master': dissolve}
    jenny "... It doesn't mean anything."

    anon "Ya baiklah."

    show jenny f_concerned_low
    anon "Keep telling yourself that."

    jenny f_helpless_down @ -m_talk "..."
    show jenny f_concerned_low
    pause
    jenny f_upset_down "Yes, we're gonna sex."

    show anon f_normal_low
    pause
    jenny f_normal_low "Soon."

    pause
    jenny f_sexy_down "I don't know, sam9... you'll just have to wait and see."

    pause
    jenny "Oh, god yes!"

    jenny "With all these hormones, I get like, crazy horny!"

    show anon f_flirt
    pause
    jenny "No, I've just been using my toys."

    pause
    jenny "Umm, because I haven't felt like shaving..."

    show anon f_confused_low
    pause
    show anon f_disgusted_low m_talk
    jenny f_gross_down "... Eww, seriously?"

    show anon -m_talk
    pause
    show anon f_surprised_low
    jenny f_sexy_down "Heh, wow."

    jenny "I guess that shouldn't surprise me..."

    show anon f_worried
    show jenny f_laugh
    pause
    show anon f_normal_low
    jenny f_normal_low "... You boys are thirsty as fuck!"

    pause
    jenny "Umm, okay... can we talk about it another time?"

    jenny f_sexy_down "I really wanna get this big dick in me."

    show anon f_flirt_grin
    pause
    jenny f_grin_down "Ya."

    show anon f_surprised
    show jenny b_jersey_bed_mount f_nipple3:
        offset (-50, -20)
    with {'master': dissolve}
    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"


    call scene_jenny_sex_pregnant.repeat
    $ unlock_scene('Jenny', '19_unlocked')

    scene location_home_jennybedroom_closeup_peek
    show jenny b_jersey_bed_after
    show anon b_bed_jenny_laptop f_confused_back_low of_mask
    show jenny_overlay_o_laptop as laptop
    with fade
    anon @ -m_talk "Hmm..."

    anon "... I think I might have broken her."

    show anon f_worried_down
    "*PING*{w=.5} *PING*{w=.4} *PING*{w=.4} *PING*{w=1} *PING*{w=.1} *PING*{w=.1}"

    show anon f_surprised_down
    "*PING*{w=.2} *PING*{w=.2} *PING*{w=1} *PING*{w=.3} *PING*{w=.4} *PING*{w=.1} *PING*{w=.2}"

    "*PING*{w=.2} *PING*{w=.2} *PING*{w=.2} *PING*{w=.2} *PING*{w=1} *PING*{w=.1}"

    show anon f_shock_down
    "*PING*{w=.1} *PING*{w=.1} *PING*{w=.1} *PING*{w=.1} *PING*{w=.1} *PING*{w=.1} *PING*{w=.1} *PING* *PING*{w=.1} *PING*{w=.1} *PING*{w=.1} *PING*{w=.1} *PING*{w=.1} *PING*{w=.1} *PING*{w=.1} *PING* *PING*{w=.1} *PING*{w=.1} *PING*{w=.1} *PING*{w=.1} *PING*{w=.1} *PING*{w=.1} *PING*{w=.1} *PING*"

    pause
    anon f_surprised_down "Should I shut the stream off or something?"

    show anon f_confused_back_low
    jenny "{i}*Bergumam tak jelas*{/i}"

    anon f_shy_down "Uhh, sorry guys... I think that's all for today."

    pause
    anon "Yeah, it was pretty good."

    pause
    anon f_worried_down "Umm, I dunno... it's complicated."

    pause
    anon f_confused_down "My name?"

    anon "Oh, I don't think-"

    show anon f_worried_back_low
    jenny "Dun ev thunkit, asshuuuul."

    pause
    anon f_shy_down "Let's just say I'm her boyfriend and leave it at that..."

    jenny "Noma boyfren..."

    anon f_happy_back_low "Apa itu {b}[jen_name]{/b}?"

    jenny "{i}*Bergumam tak jelas*{/i}"

    anon "You love me?"

    anon "Aww, that's nice."

    jenny "{i}*Mengerang*{/i}"

    anon f_laugh "hehe!"

    anon f_shy_down "Jadi uhh... Saya rasa, terima kasih sudah mendengarkannya kawan!"

    anon "And we'll just... ehh, see you all next time!"

    pause

    scene expression background(240, 352, 2.2, l=L_home_sisbedroom, o=2) as stage
    show anon b_underwear f_looking_down
    with fade
    pause
    show anon b_dressed_changing2
    with {'master': dissolve}
    pause
    show anon a_towel b_shorts
    with {'master': dissolve}
    pause
    show anon b_dressed_changing
    with {'master': dissolve}
    pause
    show anon a_sides b_dressed f_normal
    with {'master': dissolve}
    anon "Jadi, um..."

    anon f_happy "... Bagaimana kabarmu?"

    jenny "{i}*Bergumam tak jelas*{/i}"

    anon "Oh oke."

    pause
    anon f_confused "Apakah kamu memerlukan aku untuk membelikanmu sesuatu?"

    jenny "{i}*Bergumam tak jelas*{/i}"

    anon f_worried "Benar."

    pause
    anon f_shy "Jadi, menurutku, kamu akan memberiku bagianku saja nanti?"

    jenny "{i}*Bergumam tak jelas*{/i}"

    anon f_normal "Keren keren."

    pause
    show anon a_wave f_happy
    with {'master': dissolve}
    anon "'Baiklah, sampai jumpa!"

    hide anon
    with {'master': dissolve}
    pause
    jenny "Kontol."


    scene expression background(360, 360, 4., l=L_home_hallway, o=2) as stage
    with fade
    show anon f_happy:
        xzoom -1
    with {'master': dissolve}
    anon @ -m_talk "( Well, that wasn't so bad... )"

    anon f_grin @ -m_talk "( ... And {b}[jen_name]{/b} called me her boyfriend... AGAIN! )"

    anon f_thinking @ -m_talk "( So that has to mean something, right?! )"

    pause
    anon f_happy @ -m_talk "( She can deny it all she wants but there's definitely some feelings there! )"

    anon @ -m_talk "( I'll just have to wait until the day she's ready to admit it to herself. )"

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
