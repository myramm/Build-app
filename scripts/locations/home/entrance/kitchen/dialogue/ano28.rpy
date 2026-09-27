label ano28_food_home_kitchen:
    scene expression background() as stage
    show debbie a_mug_give f_normal_down:
        xoffset 600
        xzoom -1
    show anon with dissolve:
        xoffset 150
    anon "Is that bacon I smell?"

    debbie f_normal_back @ -m_talk "Mhmm."

    anon f_happy "Oh, I love you!"

    show debbie:
        xoffset 0
        xzoom 1

    if M_debbie.finished_state(S_debbie_night_visit_three):
        show anon f_flirt
        show debbie a_sides f_sexy
        with {'master': dissolve}
        debbie "hehe."

        pause
        hide anon
        show debbie b_robe_kiss_mc:
            xoffset -150
        with dissolve
        pause
        debbie f_sexy @ -m_talk "MM."

        pause
        show anon f_flirt_grin:
            xoffset 150
        show debbie a_front b_robe:
            xoffset 0
        with dissolve
        debbie f_sexy "Not as much as I love you... my little hero!"

    else:

        show debbie a_front f_laugh
        with {'master': dissolve}
        debbie "hehe."

        show anon f_normal
        debbie f_normal "The feeling is mutual, sweetie."

        debbie "It wouldn't do to have my little hero going hungry, now would it?"


    show anon f_grin
    pause
    show anon f_normal
    debbie f_normal "Is {b}[jen_name]{/b} up?"

    anon f_confused @ -m_talk "Hmm?"

    anon f_normal "Oh, umm... no idea."

    jenny "Yes, {b}[jen_name]{/b} {i}IS{/i} up, thank you very much."

    show anon f_normal_left
    show jenny a_sides b_dressed_magic:
        xoffset -150
        xzoom -1
    with dissolve
    jenny f_happy "Like anybody could sleep with all the noise you're making down here."

    show anon f_normal
    debbie f_curious "I chopped up some fresh fruit for you... if you want?"

    show debbie f_normal
    show anon f_normal_left
    jenny "Yeah, that sounds good."

    show debbie a_mug_give f_normal_down:
        xoffset 600
        xzoom -1
    with {'master': dissolve}

    if M_jenny.finished_state(S_jenny_cheerleader_sex):
        jenny "Terima kasih."

        show anon f_normal
        show debbie a_mug_drink f_kiss
        show jenny f_sexy
        with dissolve
        pause
        show jenny a_slap_butt behind anon
        show anon b_empty f_surprised:
            offset (198, -10)
        anon "!!!" with hpunch
        show jenny a_sides
        show anon a_sides b_dressed f_shy_left behind jenny:
            offset (150, 0)
        with {'master': dissolve}
        anon "Heh, good morning to you too."

        pause
        anon f_normal_left "Big plans today?"

        jenny f_happy "Just the usual."

        show debbie a_mug f_normal:
            xoffset 0
            xzoom 1
        with dissolve
        pause
        jenny "I've got some uhh... {i}*Ahem*{/i} work, scheduled for this afternoon."

        anon "Oh?"

        jenny f_sexy "Ya."

        show debbie f_curious
        pause
        jenny "So if you could..."

        anon f_flirt_left "Mengerti."

        jenny "Ya."

        anon "Tidak masalah."

        show anon f_normal
        show jenny f_normal
        debbie "If he could what, dear?"

        show anon f_confused
        jenny f_confused @ -m_talk "Hmm?"

        show anon f_surprised_teeth_left
        jenny f_surprised "Oh, umm... I just-"

        show anon f_thinking
        jenny f_concerned "He needs to... uhh-"

        anon f_confused_back "Keep the noise down?"

        jenny f_normal "Yeah, that!"

        show anon f_normal_left
        jenny "I need him to keep the noise down... while I'm working."

        show anon f_normal
    else:

        pause
        anon f_normal_left "Selamat pagi."

        show debbie a_mug_drink f_kiss with {'master': dissolve}
        jenny f_eyeroll "Ugh, terserah."

        show anon f_unimpressed_left
        pause
        show jenny f_upset
        anon "Grumpy as always, I see..."

        show jenny a_crossed with {'master': dissolve}
        jenny "Tch, do you really wanna start with-"

        show debbie a_mug f_sad:
            xoffset 0
            xzoom 1
        with {'master': dissolve}
        show jenny f_upset
        show anon f_worried
        debbie "Please not today, you two."

        pause
        debbie "Can't we just have a nice friendly breakfast for once?"

        show anon f_worried_left
        jenny f_upset "Maybe, if {i}SOMEONE{/i} wasn't always such a giant dillhole..."

        anon f_annoyed_left "Hey, I'm not the one who-"

        show anon f_frown_down
        show jenny f_upset_down
        debbie f_angry "Enough!" with hpunch
        pause
        debbie f_sad "Astaga."

        show anon f_shy
        show jenny a_sides f_concerned
        with {'master': dissolve}

    debbie f_sorry "You know, I really think you should cut {b}[firstname]{/b} some slack..."

    debbie "... He put his life on the line to save us after all."

    show anon f_normal_left
    jenny f_eyeroll "Ya, saya tahu..."

    show debbie f_sad
    show jenny a_crossed f_upset
    with {'master': dissolve}
    jenny "... But then again, the only reason they kidnapped us in the first place was because he stole some briefcase from them..."

    anon f_unimpressed_left "Hei, itu bukan-"

    show anon f_thinking_down
    pause
    anon f_sad_down "... The only reason."

    jenny @ f_confused -m_talk "Mhmm."

    debbie @ f_surprised "{b}[jen_name]{/b}, he knocked a Russian mobster out with his bare hands!"

    jenny "That doesn't make up for them snatching us!"

    pause

    if M_jenny.finished_state(S_jenny_cheerleader_sex):
        jenny f_normal_low "... Even if it was super hot."

        show anon f_shock_left
        debbie f_curious @ -m_talk "Hmm?"

        pause
        show anon f_shock
        debbie "I didn't catch that last thing you said, dear..."

        show anon f_surprised_left
        jenny f_eyeroll "Nothing... never mind."

        show anon f_shy_left

    show debbie f_normal
    jenny f_normal "Is the food done?"

    show anon f_normal
    show debbie a_mug_give f_normal_down:
        xoffset 600
        xzoom -1
    with dissolve
    debbie "Almost."

    show debbie a_mug f_normal_back
    with {'master': dissolve}
    debbie "If you kids wanna set the table, I'll-"

    show anon f_surprised_left
    show debbie f_surprised_back
    show jenny f_surprised_back
    "{i}*Ding Dong*{/i}"

    show anon f_normal
    show debbie f_curious:
        xoffset 0
        xzoom 1
    show jenny f_confused
    with {'master': dissolve}
    debbie "Was that the door?"

    anon "Y-ya, menurutku begitu."

    show anon f_normal_left
    jenny "Who could it be this early in the morning?"

    show anon a_sides f_confused:
        xoffset -400
        xzoom -1
    show jenny behind anon
    with {'master': dissolve}
    anon "Don't worry, I'll get it."

    hide anon
    show jenny:
        xoffset -625
        xzoom 1
    with {'master': dissolve}
    debbie a_nervous f_sad "Tidak uh!"

    debbie "Not by yourself you won't!"

    hide debbie
    show jenny f_eyeroll
    with dissolve
    pause

    scene location_home_entrance_frontdoor
    show location_home_entrance_frontdoor_day_door_overlay as door
    show anon a_sides f_surprised:
        xoffset -100
    show yumi a_sling behind door:
        xoffset -40
    with fade
    anon "{b}Yumi{/b}?"

    show debbie a_front f_curious behind anon with {'master': dissolve}:
        xoffset 100
        xzoom -1
    yumi "Hey, I'm just stopping by to-"

    show anon f_surprised_teeth
    show debbie b_empty f_normal_down:
        xoffset 320
    show yumi b_dressed_hug_debbie f_surprised_up
    yumi "Oof!" with hpunch
    show anon f_worried
    show yumi f_embarrassed_up
    debbie "It's so good to see you, dear!"

    yumi "Heh, umm... y-yeah, you too."

    show debbie a_front b_robe f_curious:
        xoffset 100
        xzoom -1
    show yumi a_sling b_dressed f_normal
    with dissolve
    show anon f_normal
    debbie f_sad "We've been worried."

    yumi "Oh, there's no reason to worry, ma'am... I'm fine."

    show debbie f_sad_back
    anon "Yeah, you look well."

    show debbie f_normal
    yumi f_happy "I'm pretty much back to one hundred percent."

    pause
    show anon f_normal_low
    show debbie f_normal_down
    yumi @ f_happy_down "In fact, this is my last day wearing this stupid sling, thank goodness."

    show anon f_normal
    debbie f_normal "Ya, itu kabar baik!"

    yumi "{b}Harold{/b} wanted me to swing by and inform you that they officially closed the investigation last night."

    show debbie f_normal_back
    anon f_shy "So it's finally over?"

    show debbie f_normal
    yumi "Ya."

    yumi "All of the suspects from the warehouse are either dead or incarcerated."

    yumi "And the warehouse itself will be going to auction in a week or so."

    debbie f_curious "Huh, I wonder who will buy it?"

    show debbie f_curious_back
    anon f_confused "What about those poor slave girls that vanished, still nothing?"

    show debbie f_sad
    yumi f_concerned "Sayangnya tidak."

    yumi "{b}Harold{/b}'s been working around the clock trying to track them down but so far he's come up empty handed."

    show debbie f_sad_back
    anon f_thinking "It's so weird how they just disappeared during the fighting..."

    anon f_confused "... I mean, where could they have gone?"

    show debbie f_sad
    yumi f_sad "We may never know."

    show anon f_worried
    pause
    yumi f_happy "Anyways, I'm just happy I got a chance to check in on you guys one last time."

    show anon f_normal
    show debbie f_normal
    yumi "I've been over here so much lately, it feels like my second home."

    debbie "Well, you're always welcome here, dear."

    debbie "In fact, why don't you come in and join us for breakfast?"

    yumi f_embarrassed "Oh, no... I really should be getting back to-"

    show debbie f_normal_down behind yumi:
        xoffset 240
    show anon behind debbie
    with {'master': dissolve}
    debbie @ f_excited "Nonsense, I insist!"

    yumi f_happy "Heh, it does smell good."

    anon "Yeah, {b}[deb_name]{/b}'s cooking is the best."

    show debbie f_normal_back:
        xoffset -350
        xzoom 1
    show yumi:
        xoffset -200
    with {'master': dissolve}
    debbie "You know, we're really gonna miss having you around here..."

    hide yumi
    hide debbie
    show anon:
        xoffset -600
        xzoom -1
    with dissolve
    debbie "... You're such a polite young woman."

    yumi "Aww, thanks {b}[deb_name]{/b}."


    if M_helen.finished_state(S_helen_route_split) and not M_helen.is_state(S_helen_mia_breakdown):
        debbie "I hope that {b}Harold{/b} knows how lucky he is to have you."

        yumi "I'm sure he does."

    else:

        debbie "I can't understand how you don't have a boyfriend..."

        yumi "Oh, I uhh... it's complicated."


    pause
    show anon f_worried with {'master': dissolve}:
        xoffset -50
        xzoom 1
    anon @ -m_talk "( Hmm, I wonder where {b}Svetlana{/b} and those other girls could have gone? )"

    show anon with dissolve:
        xoffset 125
    pause
    show anon with {'master': dissolve}:
        xoffset 300
    anon @ -m_talk "( Well, wherever they are, I hope they're doing okay... )"

    debbie "C'mon, sweetie, everyone is waiting for you!"

    anon f_normal_left "Coming!"

    hide door
    show anon a_reach
    with dissolve

    if L_bank_lobby.is_here(M_liu):
        scene expression background(440, 456, 4.2, l=L_bank_office) as underlay
    else:
        scene expression background(768, 384, 2, l=L_liu_lounge) as underlay
        show liu b_robe_hair

    show liu a_phone_talk f_worried:
        xoffset 500
        xzoom -1

    $ renpy.dynamic(stage=background(816, 400, 3, l=L_home_diningroom))
    show expression stage as stage
    show anon f_tired_happy
    with longfade
    anon "Phew, that was a lot of food."

    anon "I wonder if {b}[deb_name]{/b} wants help cleaning the dishes?"

    "{i}*Brrrzzzt* *Brrrzzzt*{/i}"

    anon f_surprised @ -m_talk "Hmm?"

    show anon f_surprised_down
    "{i}*Brrrzzzt* *Brrrzzzt*{/i}"

    show anon a_phone f_thinking_down with {'master': dissolve}
    anon "Jeez, now what?"

    anon f_confused_down "Hmm, I don't recognize this number..."

    show anon a_phone_talk f_confused with dissolve:
        xoffset -500
        xzoom -1
    show expression stage as stage at phoneright with phoneright.show
    anon "Halo?"

    liu "Halo, {b}[firstname]{/b}?"

    pause
    liu "It's umm... {b}Liu{/b}."

    anon f_normal "Oh, hei!"

    anon "It's great to hear from you!"

    liu f_nervous "Dia?"

    anon "Ya, tentu saja!"

    liu f_happy "Oh bagus."

    liu f_nervous_down "I was worried you'd forgotten about me."

    anon "Tidak, tidak sama sekali."

    show liu f_happy
    anon f_shy "I've been meaning to call, it's just, things have been crazy these past few weeks..."

    show liu f_worried
    anon "... You know, with the police investigation and reporters."

    liu f_worried_down "Yeah, no... I saw the news reports."

    liu f_confused "You really took them down, huh?"

    anon f_normal "Well, not just me."

    show liu f_normal
    anon "I had a plenty of help."

    liu f_happy "I'm just glad it's over and everyone is okay."

    anon "Ya, aku juga."

    pause
    show anon f_confused
    liu f_nervous_down "aku uhh..."

    show liu f_nervous_lipbite
    pause
    liu f_nervous "... I've been thinking about you... a lot."

    anon f_flirt "Oh ya?"

    pause
    liu "I wondered... maybe, if you aren't too busy we could-"

    liu "Err, umm... I mean, you might wanna come over... tonight, even... if you're free?"

    show anon f_flirt_grin
    show liu f_nervous_lipbite
    pause
    liu f_nervous "A-and you know, only if you want."

    anon f_normal "Yeah, I would love that."

    liu f_happy "Benar-benar?"

    anon f_flirt "I'm excited to see you."

    show anon f_grin
    liu f_happy_excited_closed "Saya juga!"

    show anon f_flirt_grin
    liu f_worried "Err, I mean... I'm also excited..."

    liu f_nervous_down "... to see you... heh."

    pause
    liu f_nervous "Umm... okay, great!"

    liu "So I'll, uhh... see you soon then, I guess?"

    anon f_normal "Ya, sepenuhnya."

    liu f_happy "Saya tidak sabar."

    pause
    liu "Sampai jumpa, {b}[firstname]{/b}."

    anon "Nanti, {b}Liu{/b}."

    show anon a_phone f_looking_down
    show liu a_phone f_happy_down
    with dissolve
    show expression stage as stage with {'master': phoneright.hide}
    "{i}*Bip*{/i}"

    show anon a_idle f_grin with {'master': dissolve}
    anon @ -m_talk "( Heh, she's so cute! )"

    show anon f_normal with {'master': dissolve}:
        xoffset 0
        xzoom 1
    anon @ -m_talk "( I should head to her apartment next time she's off work. )"

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
