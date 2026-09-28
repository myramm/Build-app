label ano12_oops_warehouse_bushes:
    scene location_warehouse_frontyard_cutscene_01
    show text _ ("The warehouse seemed eerily quiet as I crept through the bushes to my chosen vantage point.") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("It certainly didn't appear to be a base of operation for a giant criminal enterprise.") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("I'd have thought the place to be completely abandoned, if it wasn't for the two guards...") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("... Was it possible {b}Tony{/b} had been given bad information?") as caption with dissolve
    pause

    scene location_warehouse_frontyard_cutscene_02
    show text _ ("But then a pair of familiar faces emerged from a side door,\nescorting a couple of terrified, half-naked women with face masks.") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("What were they up to in there?!") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("Were these women part of the business or were they the product?") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("My mind was racing, there were so many unanswered questions...") as caption with dissolve
    pause

    scene location_warehouse_frontyard_cutscene_03
    show text _ ("... But as it turns out, unanswered questions were the least of my problems.") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("I should have been more careful.") as caption with dissolve
    pause

    scene black with slowdissolve
    pause

    scene location_warehouse_frontyard_cutscene_04
    anon "Mmggh!!" with hpunch
    fmv "Shhh!"

    scene expression im.Blur('backgrounds/location_warehouse_frontyard_cutscene_04.jpg', 3.)
    anon "Hrrgnn!!" with hpunch
    fmv "Be silent!"

    scene expression im.Blur('backgrounds/location_warehouse_frontyard_cutscene_04.jpg', 7.)
    "{i}*Crack*{/i}{p=1.}{nw}" with vpunch

    scene black with {'master': dissolve}
    "{i}*Crack*{/i}"
    pause
    anon "..."
    pause

    scene ano12_oops_knockout_slit_open
    fmv "He's here."

    scene ano12_oops_knockout_slit_shut
    pause
    ffv "What did you do to him?!"
    fmv "Hmm?"
    ffv "He's barely conscious!"
    fmv "He was making too much noise."
    ffv "So you knocked him out?!"

    scene ano12_oops_knockout_blur
    anon "Ugh."
    fmv "You know as well as I do what will happen if we get caught out here."
    fmv "It was just a little bonk on the head, he'll be fine."
    pause
    fmv "Can you hear me, son?"
    anon "Ngh, what happened?"
    fmv "Take it slow."
    anon "Everything is all blurry."
    ffv "He could have a concussion."
    fmv "No, I doubt that..."

    scene ano12_oops_knockout_wide with slowdissolve
    pause .4
    anon "..."
    anon "{b}D-dad{/b}?"
    frank @ -m_talk "Hmm?"
    anon "You're alive?"
    show frank f_wakeup_confused
    frank "{b}Dad{/b}?"
    frank @ f_wakeup_concerned "Okay, that's not a good sign..."
    ffv "I told you!"
    ffv "I'm calling for an ambulance."
    frank "No!"
    ffv "But he's-"
    frank "If we call an ambulance here, it's gonna blow the entire operation!"
    frank "Just give him a minute!"
    anon "How could you do this to us, {b}Dad{/b}?"
    frank "Do what, son?"
    anon "Why did you leave me?"
    pause
    frank "C'mon, kid... Snap out of it!"
    anon "Hmm?"

    scene location_warehouse_wakeup_03 with dissolve
    pause .2
    anon "{b}Officer Yumi{/b}?"
    yumi "Mhmm."

    scene black with eyeshut
    pause .2

    scene location_warehouse_wakeup_06 with eyeopen
    anon "!!!"
    anon "{b}Harold{/b}?"
    show harold b_empty f_wakeup_concerned
    harold "That's right."
    pause
    harold "I think he's coming around."
    anon "What are you two doing here?"
    harold "I was gonna ask you the same question, son."
    anon "Ngh."
    harold "Can you stand up?"
    anon "Y-yeah, I think so."

    scene expression background(0, 400, 2.) as stage
    show harold f_worried:
        xoffset -100
    show yumi f_concerned:
        xoffset 100
    with fade
    show anon a_rub f_hurt behind yumi with dissolve:
        xoffset -100
    harold "There, that's better, isn't it?"
    anon @ -m_talk "Ugh."
    yumi "Are you sure you're okay, {b}[firstname]{/b}?"
    yumi "You were really out of it there for a second..."
    anon f_tired "Y-yeah, I think so."
    anon "What's going on?!"

    if False:
        yumi "We're on a stake out, monitoring the mob activities and-"
        show harold:
            flip
            xoffset 350
        harold f_normal "{b}Yumi{/b}!" with hpunch
        show yumi f_embarrassed
        pause
        harold "Don't you think {i}we{/i} should be the ones questioning {i}him{/i}?"
        yumi f_concerned "Sorry, sir."
        show harold f_worried with {'master': dissolve}:
            unflip
            xoffset -100
    else:
        harold f_normal "{i}*Ahem*{/i} I'll be the one asking questions..."

    harold f_suspicious "What are YOU doing out here, {b}[firstname]{/b}?"
    anon f_worried @ -m_talk "..."
    harold "Do you have any idea what this place is, or what those animals will do to you if they find you snooping around?"
    anon f_worried_low "..."
    harold "What in the hell were you thinking, coming here?"
    anon f_skeptical "Well, somebody has to do something!"
    anon f_angry "These assholes are terrorizing my friends and I!"
    harold f_concerned @ -m_talk "Hmm?"
    harold "What friends?"
    anon @ f_squint -m_talk "..."
    anon "Never mind."
    harold "If you have information that could help us, then-"
    anon @ f_skeptical "I don't."
    anon "Just forget I said anything."
    harold @ -m_talk "..."
    anon "Have you seen the bound women down there?!"
    harold "Yes, we're aware of them."
    anon "So, why aren't you guys going down there to help them?!"
    harold "Well, besides the fact that they have an army of goons in that warehouse..."
    harold "... And we'd probably be shot on sight."
    yumi f_embarrassed @ -m_talk "..."
    harold "We're under strict orders not to engage them at this time."
    anon f_angry "Why?"

    if M_mia.finished_state(S_mia_harold_to_the_rescue):
        harold f_normal "That's something I'm trying to figure out my own self."
        harold "It doesn't make any sense."
    else:
        harold f_worried "It's not my job to question orders, kid."
        harold "I just follow them."

    harold f_normal "Regardless, you shouldn't be out here!"

    if M_mia.finished_state(S_mia_find_harold):
        harold f_worried "Do you realize how devastated my daughter would be if you got yourself killed?"
        harold "You want her weeping over your casket?"
    else:
        harold "Haven't your friends been through enough?"
        harold "You want them weeping over your casket too?"

    anon f_sad_down @ -m_talk "..."
    harold "I need you to trust me when I tell you I'll handle this, okay?"
    anon "Y-yeah, okay."
    show harold with {'master': dissolve}:
        flip
        xoffset 350
    harold "{b}Officer Yumi{/b} drive him home, please."
    yumi f_concerned "What about you, sir?"
    harold "I'm going to finish up here."
    harold "Just return once it's done and we'll head down to the station to make our report."
    yumi "Yes, sir."
    show yumi:
        xoffset -400
    show harold:
        unflip
        xoffset -150
    with {'master': slowdissolve}
    yumi "C'mon, {b}[firstname]{/b}, let's go."
    anon @ -m_talk "..."
    hide anon
    hide yumi
    with dissolve

    scene location_police_car_interior_night
    show anon b_dressed_car_front f_frown_left
    show yumi b_dressed_car_front f_annoyed a_wheel
    show xtra 30
    show yumi_overlay_o_wheel_fingers
    with fade
    pause
    yumi "I can't believe you came out here all by yourself..."
    yumi @ f_yelling_left "Just what in the hell were you thinking?!"
    anon "I was thinking that they killed my dad."
    yumi "You don't know that!"
    anon "Yes, I do."
    pause
    show anon b_dressed_car f_skeptical with dissolve
    anon "And you know it too."
    yumi f_concerned @ -m_talk "..."
    yumi "Well, it doesn't matter."
    yumi "You shouldn't be going anywhere near that place."
    anon "I said I was sorry, didn't I?"

    if False:
        "{i}*Scrreeeeecch*{/i}" with hpunch
        show yumi a_idle f_annoyed_left
        hide yumi_overlay_o_wheel_fingers
        with dissolve
        anon f_surprised @ -m_talk "!!!"
        anon "Jesus, what are you-"
        yumi f_yelling_left "I don't care if you're sorry!"
        yumi "It was reckless and stupid and there's no excuse for it!"
        show yumi f_annoyed_left
        show anon b_dressed_car_front f_frown_left with dissolve
        anon @ -m_talk "..."
        yumi "There's a lot of people that care about you, you know?!"
        show anon b_dressed_car f_skeptical with dissolve
        anon "Yeah, I know that, {b}Yumi{/b}."
        yumi "I care about you!"
        show anon f_worried
        yumi "I'd be devastated if something were to happen to you."
        yumi "Does that even cross your mind when you consider doing stupid stuff like this?!"
        anon "Of course it does."
        show yumi f_annoyed a_wheel
        show yumi_overlay_o_wheel_fingers
        with dissolve
        yumi "Well, apparently it's not enough to stop you."
        anon "C'mon, don't be like that..."
    else:
        yumi "What were you even expecting to accomplish on your own, anyway?"
        anon @ -m_talk "..."
        yumi f_annoyed_left "{b}[firstname]{/b}?"
        anon "I don't know, okay?"
        show yumi f_annoyed
        anon "I just wanted to have a look around."
        anon "Maybe get a better idea of what we're dealing with."
        yumi "YOU shouldn't be dealing with anything."
        yumi "This is a police matter, remember?"
        show anon b_dressed_car_front f_frown_left with dissolve
        anon "Yeah, right."
        yumi "Look, I know you aren't exactly thrilled with our lack of progress so far..."
        yumi f_concerned @ f_concerned_left "... But you have to understand, these things take time, yeah?"
        anon @ -m_talk "..."
        yumi "{b}Harold{/b} is a good cop, he'll get to the bottom of all this."
        yumi @ f_concerned_left "I know he will."
        pause

    yumi "{i}*Sigh*{/i} I don't know what I'm supposed to tell {b}[deb_name]{/b} about this..."

    if not False:
        show anon b_dressed_car f_worried with dissolve

    anon "What do you mean?"
    yumi "You don't think she'll be curious as to why I'm driving you home?"
    anon "Then just don't tell her anything!"
    yumi "I'm not going to lie to her, {b}[firstname]{/b}."
    show anon b_dressed_car_front f_frown_left with dissolve
    anon "Then let me out here and I'll walk."

    if False:
        yumi @ f_annoyed_left "Uhh, not a chance, {b}[firstname]{/b}!"
        yumi "After the stunt you just pulled, you'll be lucky if I ever let you out of my sight again."
    else:
        yumi @ f_concerned_left "Yeah, that's not happening."
        yumi "I have my orders."

    anon @ -m_talk "..."
    yumi "I just hope she's not still upset about that box of personal effects I dropped off this morning..."
    show anon b_dressed_car f_skeptical with dissolve
    anon "Personal effects?"
    anon "What are you talking about?"
    yumi f_concerned @ f_concerned_left "Yeah, evidence released a box of your father's belongings today."
    yumi "I guess you hadn't heard?"
    show anon b_dressed_car_front f_frown_left with dissolve
    anon "I had not."
    pause
    yumi @ f_concerned_left "It was just some clothes from the crime scene and a few knick-knacks we found in his old desk at the bank."
    anon @ -m_talk "..."
    pause
    yumi @ f_concerned_left "What's the matter?"
    anon "Nothing."
    pause
    anon @ -m_talk "..."
    yumi "You're just, being awfully quiet..."
    anon "Yeah well, I'm tired."
    anon "And my head hurts because somebody's partner knocked me out!"
    yumi @ f_concerned_left -m_talk "..."
    yumi "{b}Harold{/b} only did that to keep everyone safe."
    anon @ -m_talk "Mhmm."
    anon "I feel REAL safe, let me tell you..."
    yumi @ f_concerned_left "We're trying our best, you know?"
    anon "Yeah, that's the part that's worrying me."
    yumi @ -m_talk "..."
    pause
    yumi "We're here."
    pause
    yumi f_concerned_left "I'll do the talking."
    yumi "You just follow my lead, okay?"
    anon "Sure."
    anon "It's not like I have much choice."

    $ player.go_to(L_home_entrance)
    scene location_home_entrance_frontdoor_night
    show location_home_entrance_frontdoor_night_door_overlay as door
    show debbie f_sad a_front behind door:
        flip
        xoffset -100
    with fade
    show anon f_worried behind door:
        flip
        xoffset -275
    show yumi behind door:
        xoffset -100
    with dissolve
    debbie "{i}*Gasp*{/i} Where have you been?!"
    debbie "Did something happen?!"
    yumi @ a_calm_down "Everything is fine, ma'am."
    yumi "I was just helping your tenant get home, that's all."
    show anon b_empty f_worried_low
    show debbie b_robe_hug_mc:
        xoffset -275
    with dissolve
    debbie "You had me worried sick!"
    pause
    show anon b_dressed f_worried:
        xoffset -275
    show debbie b_robe a_sides:
        xoffset -100
    with dissolve
    debbie "You know you shouldn't be out by yourself this late at night."
    anon @ f_worried_low "Y-yeah, I know."
    anon "I was working late and I lost track of time."
    pause
    anon "I'm really sorry."
    show anon behind debbie with {'master': slowdissolve}:
        unflip
        xoffset 60
    debbie f_normal "{i}*Phew*{/i} Thank you so much, {b}Yumi{/b}..."
    debbie "... For seeing him home."
    yumi "My pleasure, ma'am."
    debbie "Would you like to come in?"
    debbie "I can get you something to eat or-"
    yumi @ a_calm_down "N-no, thank you."
    yumi "I appreciate the offer but {b}Harold{/b} is waiting for me."
    yumi "I'll be by tomorrow to check in on you guys, okay?"
    debbie "Alright, thanks again."
    yumi "Farewell."
    hide yumi with dissolve
    show debbie:
        xoffset 400
    with slowdissolve
    pause
    debbie "She's such a sweet young woman..."
    show debbie with dissolve:
        unflip
        xoffset -125
    debbie @ f_laugh "... And so petite."
    debbie "I wonder what lead to her becoming a cop?"
    anon @ a_behind_head "Yeah, uhh... Who could say?"
    show debbie f_sad
    pause
    anon "I think I'm just gonna head to bed, if that's alright?"
    hide anon with dissolve

    scene expression background(640, 360, 3.) as stage with fade
    show anon f_worried with dissolve:
        flip
        xoffset -500
    pause
    show debbie a_sides f_sad behind anon with {'master': dissolve}

    if M_debbie.finished_state(S_debbie_night_visit_three):
        debbie f_sexy "By yourself?"
        show anon with {'master': dissolve}:
            unflip
            xoffset 0
        anon "Yeah."
        anon @ f_worried_low "Sorry, I'm just really tired tonight."
        debbie f_sad "That's alright, sweetie."
        debbie "Can I get you anything?"
        anon "No, really... I just need sleep."
        debbie "Oh."
        debbie "Okay then."
        show debbie b_robe_kiss_mc1
        hide anon
        with dissolve
        pause
        show debbie b_robe
        show anon b_dressed f_worried
        with dissolve
    else:
        debbie "Are you sure everything is alright, sweetie?"
        show anon with {'master': dissolve}:
            unflip
            xoffset 0
        anon "Yeah, I'm sure."
        anon "I'm just really tired, that's all."
        anon "Long day."
        debbie "Oh."
        debbie "Okay then."
        show anon b_empty f_worried_low
        show debbie b_robe_hug_mc
        with dissolve
        pause
        show debbie b_robe
        show anon b_dressed f_worried
        with dissolve

    anon "I'll see you tomorrow."
    debbie "Good night."
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
