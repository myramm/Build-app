label tattoo_parlor_apartment_odette_pregnancy_first_baby:
    scene expression player.location.background_blur with None
    show odette f_happy_down a_baby:
        xoffset 100
    show grace:
        flip
        xoffset 350
    show eve f_happy:
        flip
        xoffset 200
    with dissolve
    if M_odette.pregnancy.baby_gender == "boy":
        eve "Oh my god, he's so tiny!"
        pause
        eve "{i}*Gasp*{/i} Look at his little fingers!"
        grace "Isn't he just adorable?"
    elif M_odette.pregnancy.baby_gender == "twins":
        eve "Oh my god, they're so tiny!"
        pause
        eve "{i}*Gasp*{/i} Look at their little fingers!"
        grace "Aren't they just adorable?"
    else:
        eve "Oh my god, she's so tiny!"
        pause
        eve "{i}*Gasp*{/i} Look at her little fingers!"
        grace "Isn't she just adorable?"
    eve "Hello there."
    eve "I'm your {b}Aunt Eve{/b}."
    show anon:
        xoffset -100
    with dissolve
    grace "{b}Aunt{/b}, huh?"
    eve "Well, close enough."
    odette @ f_laugh "Hehehe!"
    anon "Hey, {b}Odette{/b} is home!"
    eve f_happy_right "{b}[firstname]{/b}!"
    show eve f_happy:
        unflip
        xoffset -350
    with dissolve
    eve "{b}[firstname]{/b}!"
    hide anon
    show eve b_dressed_kiss
    with dissolve
    odette f_smirk "Ugh, get a room you two..."
    show anon:
        xoffset -100
    show eve b_dressed
    with dissolve
    eve "S-sorry."
    pause
    grace "She's joking."
    odette @ f_laugh "Hehehe!"
    if M_odette.pregnancy.baby_gender == "twins":
        grace "Would you like to meet {b}Odette's babies{/b}, {b}[firstname]{/b}?"
    else:
        grace "Would you like to meet {b}Odette's baby{/b}, {b}[firstname]{/b}?"
    show anon f_skeptical
    if M_odette.pregnancy.baby_gender == "boy":
        anon "Meet him?"
    elif M_odette.pregnancy.baby_gender == "twins":
        anon "Meet them?"
    else:
        anon "Meet her?"
    anon f_surprised a_idle "Oh, right!"
    anon f_shy "Uhh, yeah... I'd love to."
    eve f_confused @ -m_talk "..."
    show eve f_happy:
        flip
        xoffset 220
    show anon a_wave
    with dissolve
    if M_odette.pregnancy.baby_gender == "twins":
        anon "Hey there, little ones!"
    else:
        anon "Hey there, little one!"
    anon "I'm {b}[firstname]{/b}."
    pause
    if M_odette.pregnancy.baby_gender == "boy":
        anon "He looks just like you, {b}Odette{/b}."
    elif M_odette.pregnancy.baby_gender == "twins":
        anon "They look just like you, {b}Odette{/b}."
    else:
        anon "She looks just like you, {b}Odette{/b}."
    eve "Right?"
    eve "Look at all that thick, black hair!"
    odette @ f_laugh "Hehehe!"
    hide anon with dissolve
    return

label tattoo_parlor_apartment_grace_pregnancy_first_baby:
    scene expression player.location.background_blur with None
    show odette:
        xoffset 100
    show grace f_happy_down a_baby:
        xoffset -100
    show eve f_nervous_down:
        flip
        xoffset 200
    with dissolve
    if M_grace.pregnancy.baby_gender == "boy":
        eve "{i}*Gasp*{/i} He's so beautiful!"
        pause
        eve "Hey, buddy."
        grace "Be careful with him."
    elif M_grace.pregnancy.baby_gender == "twins":
        eve "{i}*Gasp*{/i} They're so beautiful!"
        pause
        eve "Hey, little ones!"
        grace "Be careful with them."
    else:
        eve "{i}*Gasp*{/i} She's so beautiful!"
        pause
        eve "Hey, girlie."
        grace "Be careful with her."
    eve "Hi there, I'm your {b}Aunt Eve{/b}."
    show anon with dissolve
    eve "I'm the one who's going to stuff you full of sweets and let you stay up past your bedtime."
    grace "I will murder you."
    show anon f_surprised
    pause
    anon f_normal "Hey, {b}Grace{/b} is home!"
    show eve f_happy:
        unflip
        xoffset -350
    with dissolve
    eve "{b}[firstname]{/b}!"
    hide anon
    show eve b_dressed_kiss
    with dissolve
    anon "!!!"
    pause
    odette f_smirk "Ugh, get a room you two..."
    show anon
    show eve b_dressed
    with dissolve
    eve f_happy_right "S-sorry."
    pause
    grace "She's joking."
    grace f_happy_down @ f_laugh "Hehehe!"
    if M_grace.pregnancy.baby_gender == "twins":
        odette "Would you like to meet {b}Grace's babies{/b}, {b}[firstname]{/b}?"
    else:
        odette "Would you like to meet {b}Grace's baby{/b}, {b}[firstname]{/b}?"
    show eve f_happy
    show anon f_skeptical a_thinking with dissolve
    if M_grace.pregnancy.baby_gender == "boy":
        anon "Meet him?"
    elif M_grace.pregnancy.baby_gender == "twins":
        anon "Meet them?"
    else:
        anon "Meet her?"
    anon f_surprised a_idle "Oh, right!"
    anon f_shy "Uhh, yeah... I'd love to."
    eve f_confused @ -m_talk "..."
    anon f_shy_low "Hey there, little one!"
    show eve f_happy
    anon "I'm {b}[firstname]{/b}."
    pause
    if M_grace.pregnancy.baby_gender == "boy":
        anon "He's so precious, {b}Grace{/b}."
    elif M_grace.pregnancy.baby_gender == "twins":
        anon "They're so precious, {b}Grace{/b}."
    else:
        anon "She's so precious, {b}Grace{/b}."
    eve "Right?"
    show eve f_angry
    if M_grace.pregnancy.baby_gender == "boy":
        eve "I must corrupt him quickly!"
    elif M_grace.pregnancy.baby_gender == "twins":
        eve "I must corrupt them quickly!"
    else:
        eve "I must corrupt her quickly!"
    show eve f_happy_right
    grace @ f_tired "Again, I will murder you."
    eve @ f_laugh "Hehehe!"
    hide anon with dissolve
    return

label tattoo_parlor_apartment_eve_make_up_dress_table:
    scene expression player.location.background_blur with None
    show anon a_lasagna:
        xoffset -100
    show odette:
        xoffset 100
    show eve f_happy:
        xoffset -200
    with dissolve
    eve "See, there's {b}[firstname]{/b} with the food now."
    odette "Oh my god, that smells amazing!"
    anon "Yeah, tell me about it."
    anon @ f_snarky "I'm half tempted to take this home and eat it myself."
    eve @ f_laugh "Haha, not a bad idea!"
    eve "I'll go with you!"
    odette f_surprised "No, no, no, put that down!"
    show eve:
        flip
        xoffset 400
    with dissolve
    eve "It's a joke, {b}Odette{/b}."
    odette f_sad "{i}*Sigh*{/i} I know, sorry."
    odette "I'm just nervous."
    show odette a_head with dissolve
    pause
    odette a_idle "Ugh, why am I so nervous?!"
    odette "This is stupid."
    eve "Would you relax?"
    eve "You did good."
    eve "She's going to love all this and your news will seal the deal for sure."
    anon "What news?"
    eve f_happy_right "{b}Odette{/b}'s been busy today."
    anon "Oh?"
    odette f_normal "Yeah, stick around and you'll find out."
    anon "Alright."
    odette "Where did you get that expensive wine by the way?"
    eve f_happy "{b}Tuuku{/b}."
    odette @ f_surprised "Wow, how did you convince him to do that?"
    eve "I might have threatened to tell {b}Grace{/b} that he invited that drug guy to the party."
    odette f_smirk "You didn't?!"
    anon "She did."
    show anon f_grin
    eve "Yeah."
    odette @ f_laugh "Hahaha!"
    show anon f_normal
    odette "Clever girl."
    pause
    odette f_sad "Do I look okay?"
    anon "Y-yeah, you look great!"
    eve "Just remember to be assertive."
    eve "Don't ask; tell her to shut down the shop and get her ass upstairs for dinner."
    odette "Okay, okay."
    odette @ f_kiss "Phew, here I go."
    hide odette with dissolve
    pause
    show eve:
        unflip
        xoffset -300
    with dissolve
    eve "I've never seen her so flustered before."
    eve "It's kind of funny, isn't it?"
    anon "Y-yeah, it is."
    eve "Come and help me finish setting the table."
    anon "Alright."

    scene location_tattoo_apartment_cutscene03
    show text _ ("{b}Eve{/b} had really outdone herself with the table.\nIt was like a scene out of those romantic movies!") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("If this didn't win {b}Grace{/b}'s heart, nothing would.") as caption with dissolve
    pause

    $ game.timer.tick(2)
    scene expression player.location.background_blur
    show anon f_worried
    show eve
    with fade
    anon f_normal @ f_worried "This is going to work, right?"
    eve "It's perfect!"
    eve "If someone did this for me, I'd have sex with them for sure."
    anon f_surprised "You don't say?"
    anon f_flirt "I'll have to keep that in mind!"
    eve @ f_laugh "Haha!"
    grace "What if customers come?"
    hide eve
    hide anon
    show anon:
        xoffset -100
    show eve f_happy:
        flip
        xoffset 150
    with dissolve
    odette "Then they'll see that we're closed and come back tomorrow."
    odette "You deserve a night off and you're taking one."
    odette "End of story."
    grace "{i}*Sigh*{/i}"
    odette "{b}Grace{/b}, go!"
    show grace f_tired:
        flip
        xoffset 350
    with dissolve
    grace "Alright, fine."
    show odette f_smirk zorder 1:
        xoffset 100
    hide grace
    show grace zorder 0:
        xoffset -200
    with dissolve
    grace "Just don't go thinking-{p=2}{nw}"
    grace f_surprised "!!!"
    pause
    grace "W-what's all this?"
    eve @ f_laugh "Surprise!"
    grace f_proud "Is that lasagna I'm smelling?"
    pause
    grace f_surprised "{i}*Gasp*{/i} And chocolates?!"
    eve "Yup."
    eve "It was all {b}Odette{/b}."
    show grace:
        flip
        xoffset 350
    grace f_suspicious "T-these are for me?"
    odette f_sad "Yes, and let me start things off by saying, I'm sorry."
    grace f_surprised @ -m_talk "Hmm?"
    odette "You told me you didn't want to throw a party and I should have listened."
    grace "You're serious?"
    grace "That's like, the last thing I expected you to say..."
    odette "I know, and there's more."
    odette "I wanna start paying you rent."
    grace f_surprised "What?"
    grace f_tired "I don't want your money, {b}Odette{/b}."
    odette f_angry "Well, I don't care what you want."
    odette "You need help around here and I'm in a position to give it."
    odette "I'm tired of watching you kill yourself and scrape by with the bare minimum."
    grace f_sad @ -m_talk "..."
    odette "You're also done working nights."
    grace "{b}Odette{/b}, we can't-"
    odette "I mean it {b}Grace{/b}!"
    grace f_surprised "!!!"
    odette f_normal "This is the way it's going to be."
    odette "From now on, your shift ends at five!"
    odette "I'll close up and you can finally get some time to yourself and make sure {b}Eve{/b} gets proper attention."
    eve "Sounds good to me, {b}Sis{/b}."
    show grace f_sad_back
    pause
    grace f_sad "B-but we'll lose too much money..."
    odette "The money we gain from piercings will more than make up the difference."
    grace f_surprised "P-piercings?!"
    odette a_piercing "I went and talked to {b}daddy{/b} today and got him to buy us everything we need."
    grace f_suspicious "You're not qualified to give people piercings, {b}Odette{/b}!"
    odette f_smirk "I will be in a few weeks..."
    odette "... Signed up for classes on my way home."
    eve f_surprised "You're going to take classes?"
    show odette f_angry
    eve f_happy @ f_laugh "Hahaha!"
    odette "Yes, I'm going to take classes."
    odette "So stop laughing, unless you wanna be my guinea pig to practice on?"
    eve "Yeah, that's not happening!"
    anon @ f_laugh "Haha!"
    grace "Y-you're serious about all of this?"
    odette f_normal a_idle "I'm dead serious."
    odette "You've been taking care of all of us for years now."
    odette "It's time someone took care of you."
    eve @ f_happy_right "{i}*Whispers*{/i} Hmm, I wonder where she got that line?"
    anon @ f_laugh "Haha!"
    grace "You're really going to work?"
    odette @ f_laugh "Yes!"
    odette "How hard could it be to poke holes in people for a living?"
    grace f_sad_down "I-"
    grace f_happy "I don't know what to say."
    odette "You don't have to say anything."
    odette "This is happening."
    show odette b_hug_grace f_surprised
    hide grace
    with dissolve
    odette "!!!"
    show odette f_smile b_hug_grace_both with dissolve
    pause
    eve "So uhh, {b}[firstname]{/b} and I are going to go..."
    show grace f_happy:
        xoffset -200
    show odette b_dressed f_normal
    with dissolve
    grace "You're not going to stay and eat with us?"
    eve f_happy_right "We have plans of our own, right {b}[firstname]{/b}?"
    anon "Y-yeah."
    show eve f_happy
    grace "Alright, just don't be out too late."
    eve "I won't."
    show grace:
        flip
        xoffset 350
    with dissolve
    grace "I guess it's just the two of us then?"
    odette f_smirk "Yup."
    hide grace with dissolve
    grace "Oh, this wine looks expensive!"
    odette "Thanks, you two."
    anon "No problem."
    eve "Good luck."
    hide odette with dissolve
    odette "Sit down and I'll get us some glasses."
    pause
    show eve f_sexy:
        unflip
        xoffset -200
    with dissolve
    eve "You wanna go upstairs and make out?"
    anon "Of course!"
    eve @ f_laugh "Hehe, c'mon!"
    scene black with fade
    pause
    return

label tattoo_parlor_apartment_clients_wake_up_grace:
    scene expression player.location.background_blur with None
    show anon f_worried with dissolve
    anon "H-hello?"
    pause
    anon f_normal @ -m_talk "( Hmm, nobody's here... )"
    anon f_grin @ -m_talk "( They must be in the bedroom. )"
    hide anon with dissolve
    return

label tattoo_parlor_apartment_eve_pot_look_for_eve:
    scene expression player.location.background_blur with None
    show anon f_worried with dissolve
    anon "{b}Eve{/b}?"
    pause
    anon a_thinking f_thinking @ -m_talk "( Hmm, {b}she must be in her room{/b}. )"
    hide anon with dissolve
    return

label tattoo_parlor_apartment_eve_bathroom_embarassed:
    scene expression player.location.background_blur with None
    show grace b_shirt f_suspicious:
        flip
    show anon f_worried o_boner a_cover_boner:
        flip
    show expression "characters/anon/anon_arms_dressed_a_cover_boner.png" at flip
    with dissolve
    grace "Are you leaving?"
    anon "Y-yeah."
    grace "I thought you were supposed to be meeting my sister here?"
    anon "I was... But I uhh... Got a call while I was in the bathroom and I need to head home immediately."
    grace "Oh?"
    grace @ a_point "Is something the matter?"
    anon "N-no, it's just a silly family thing..."
    anon "Can you tell {b}Eve{/b} that I'll talk to her tomorrow?"
    grace f_normal "Sure, I can do that."
    show anon f_laugh a_wave
    hide expression "characters/anon/anon_arms_dressed_a_cover_boner.png"
    with dissolve
    anon "Thanks, see ya!"
    show anon f_surprised_down a_cover_boner
    show expression "characters/anon/anon_arms_dressed_a_cover_boner.png" at flip
    with fastdissolve
    show anon f_surprised
    grace f_happy "See ya!"
    scene black with fade
    pause
    $ player.go_to(L_tattooparlor_fire_escape)
    scene expression player.location.background_blur
    show anon o_boner f_depressed
    anon "( Ugh, just kill me... )"
    pause
    anon "( Tomorrow is going to be super awkward now! )"
    anon @ -m_talk "( {i}*Sigh*{/i} I should just head home. )"
    hide anon with dissolve
    return

label tattoo_parlor_apartment_eve_big_sis_check_apartment:
    scene expression player.location.background_blur with None
    show grace f_angry b_shirt zorder 1:
        flip
        xoffset 200
    show eve f_angry a_hip_angry
    with dissolve
    grace "... You're supposed to be in school!"
    eve "Well, it's a good thing I'm not... You're up here sleeping and {b}Odette{/b}'s passed out in the garage!"
    eve "Who knows how much business you've lost this morning!"
    grace @ f_weary a_facepalm "{i}*Sigh*{/i} I'll deal with {b}Odette{/b}..."
    grace "You just need to get your ass back to class!"
    show anon f_worried zorder 0:
        xoffset -100
    with dissolve
    eve "Are you serious?!"
    eve @ a_wtf "I don't give a shit about school, {b}Grace{/b}!"
    grace f_tired "{b}Eve{/b}..."
    show anon f_shy_low m_talk
    eve "{b}Odette{/b} might be unreliable, but she's not wrong about you needing a break!"
    eve f_sad "If you'd just let me help..."
    grace f_weary a_facepalm "We've been over this..."
    eve "I can watch the shop in the mornings, you know I can work the tattoo gun just as good as-"
    show anon f_surprised_teeth -m_talk
    grace f_angry a_hip @ a_angry "Absolutely not!"
    eve f_angry "Ugh, this isn't all on you, you know... I can pull my own weight around-"
    show anon f_worried
    grace "Your job, your ONLY job, is to go to school and finish your education!"
    grace "I dropped out early and now, this is the only thing I'm qualified to do..."
    grace "I'll be damned if I'm going to let you end up in the same situation!"
    eve "So what, I don't even get a say concerning my own fucking life?!"
    eve "That's not fair, {b}Grace{/b}!"
    grace @ f_surprised "Hah, fair?!"
    grace "Don't even get me started on what's fair!!"
    show eve a_rossed f_sad_down with dissolve
    grace a_point "I'm here busting my ass, EVERY SINGLE DAY, so we can keep a roof over our heads and food in our bellies..."
    grace a_hip @ a_point "Do you know how long it's been since I went out and did anything even remotely fun?"
    eve @ -m_talk "..."
    grace f_weary "... Or had a date?"
    eve "I know... I-"
    grace @ a_angry "I mean, Jesus... I can't even remember the last time I had a day off!"
    show grace a_facepalm with dissolve
    eve f_cry_down @ -m_talk "..."
    grace f_sad a_sides "{i}*Sigh*{/i} Look, I'm sorry... I don't mean to take it out on you..."
    grace "I appreciate that you wanna help but I really just need you to focus on-"
    show grace f_sad_back m_talk
    pause
    grace f_surprised_back "!!!"
    grace "{b}[firstname]{/b}?"
    show anon f_surprised_teeth a_behind_head with dissolve
    grace f_angry "You dragged him into this too?!"
    show grace -m_talk
    eve @ -m_talk "..."
    anon f_worried "T-that's not... I-"
    grace f_tired @ f_weary a_facepalm "Ugh, whatever you're about to say, I don't wanna hear it."
    show anon a_idle with dissolve
    grace @ a_point "Just go back to school, please... Both of you."
    eve @ -m_talk a_wipe_tears "{i}*Sniff*{/i}"
    pause
    hide eve with dissolve
    pause
    grace f_weary a_facepalm "Make sure she gets there, please."
    anon "Y-yes, ma'am."
    scene black with fade
    $ player.go_to(L_tattooparlor)
    scene expression player.location.background_blur
    show eve f_cry_down a_rossed:
        flip
        xoffset 600
    show anon f_worried
    with dissolve
    eve @ -m_talk "..."
    anon "You alrigh-"
    eve @ a_wtf f_mad_yelling "I'm fine!"
    show anon f_surprised_teeth
    pause
    anon f_worried "S-sorry, I didn't mean to-"
    eve f_sad_down @ a_wipe_tears "{i}*Sniff*{/i} No, I'm sorry..."
    eve "I wish you hadn't seen all that."
    eve "You probably think I'm a terrible person now or something..."
    anon "No, not at all!"
    eve @ -m_talk "..."
    anon "I think you're a person who sees their older sister in a tough situation and wants to help."
    hide eve
    show eve f_sad_down a_rossed
    with dissolve
    eve "Yeah."
    pause
    eve @ -m_talk "{i}*Sniff*{/i}"
    anon "You wanna talk about it?"
    eve "N-not really..."
    eve "Let's just head back to school, okay?"
    anon "Sure."
    eve @ -m_talk "{i}*Sniff*{/i}"
    show eve a_wipe_tears with dissolve
    pause
    hide eve with dissolve
    player_name @ -m_talk "..."
    hide anon with dissolve
    return

label tattoo_parlor_apartment_eve_visit_apartment:
    scene expression player.location.background_blur with None
    show eve f_nervous
    show anon
    with dissolve
    eve "You'll have to forgive the mess."
    anon f_skeptical "What mess?"
    show anon f_grin
    eve "{b}Grace{/b} doesn't have much time to clean things and {b}Odette{/b} is a total slob when she's over!"
    anon f_normal "Seriously, it all looks fine..."
    eve "Okay, if you say so..."
    pause
    anon f_normal_high "I love the vibe in here!"
    anon "It's like, brick and mortar meets postmodern."
    eve f_happy "Yeah, my sister is way into that..."
    show anon f_normal:
        flip
        xoffset -300
    with dissolve
    show anon f_confused
    pause
    anon "What's with the bed?"
    eve f_nervous @ -m_talk "Hmm?"
    anon f_normal "There's a bed over there, behind the folding screen."
    show anon with dissolve:
        unflip
        xoffset 0
    anon "Is that where you sleep?"
    eve f_nervous_down "Oh, nah... {b}Grace{/b} sleeps there."
    eve "We only have the one bedroom, and she insisted that I take it."
    anon f_worried "Really?"
    eve "Yeah."
    anon "My roommate would never do that for me..."
    show anon f_normal
    eve f_sad "I told her it was stupid."
    eve "She pays the bills, she should have the bedroom..."
    eve "... But she wanted me to have a place of my own, where I can be alone and get some privacy if I need it."
    anon "She sounds like an amazing sister, you're lucky."
    eve f_sad_down "Y-yeah, I know."
    eve "I really don't deserve her..."
    pause
    show anon f_worried
    pause
    anon "So, eh..."
    anon f_normal "Can I see your room?"
    eve f_nervous_down "Oh, umm... I dunno..."
    anon "Hey c'mon, you promised me the full tour!"
    eve @ f_laugh "Hehe, did I?"
    show eve f_nervous
    anon @ f_laugh "You certainly did!"
    eve f_normal_up @ -m_talk "Hmm."
    eve f_happy "Alright, fine."
    eve "Just don't be disappointed when you see how nerdy it is..."
    hide eve with dissolve
    anon "Yeah, right."
    hide anon with dissolve
    return

label tattoo_parlor_apartment_eve_pregnancy_first:
    scene expression player.location.background_blur
    show eve f_sad
    show anon with dissolve
    anon "There you are."
    eve "Hey."
    anon f_worried "Is everything okay?"
    eve f_sad_down "Umm, I dunno."
    anon "What's wrong?"
    eve "I uhh-"
    pause
    eve "I think I'm pregnant."
    anon f_shock a_behind_head "!!!" with hpunch
    anon "Y-you're pregnant?!"
    eve f_sad "I'm sorry, I didn't mean for this to happen..."
    eve "To be honest, I wasn't even sure it was possible after the accident and all the damage-"
    anon f_normal a_idle @ f_laugh "This is wonderful news!"
    eve f_surprised "!!!"
    eve f_confused "Wonderful?"
    anon "I'm going to be a father!"
    eve "You're happy about this?"
    anon "Of course."
    anon "Why wouldn't I be?"
    eve f_nervous_down "I dunno, I just wasn't expecting this..."
    anon "You're going to be a mom, {b}Eve{/b}!"
    anon "Why aren't you more excited?"
    eve f_nervous "Heh, I am."
    eve "I mean, I wasn't... I was terrified, but after seeing you react like this..."
    hide eve
    show anon b_hug_eve f_shy_down
    with dissolve
    eve "I love you, {b}[firstname]{/b}."
    anon "Heh, I love you too."
    hide anon
    show eve b_dressed_kiss:
        xoffset -400
    with dissolve
    pause
    hide eve
    show eve f_happy
    show anon
    with dissolve
    anon "Oh my gosh, we're gonna be parents!"
    eve "Hehe, yeah..."
    pause
    eve f_sad "There is one little issue though."
    anon @ f_confused -m_talk "Hmm?"
    eve "Well, I still have to tell {b}Grace{/b}."
    anon "Yeah?"
    eve "She's probably going to flip out..."
    anon f_worried "Oh."
    pause
    anon f_normal "Well, let's just go and tell her!"
    eve f_surprised "What, right now?"
    anon @ f_laugh "Yeah, we'll just rip it off quick like a bandaid!"
    hide anon with dissolve
    eve "You can't be serio-"
    eve "H-hey, wait for me!"
    scene black with dissolve
    pause

    $ player.go_to(L_tattooparlor_interior)
    scene expression player.location.background_blur
    show odette f_surprised:
        xoffset 100
    if M_grace.pregnancy:
        show grace f_angry:
            xoffset -150
    else:
        show grace f_angry a_upset:
            xoffset -150
    show anon f_surprised_teeth:
        xoffset -100
    show eve f_sad:
        flip
        xoffset 150
    with hpunch
    grace "YOU'RE WHAT?!"
    eve "I'm pregnant."
    pause
    eve "With {b}[firstname]{/b}'s child."
    if M_grace.pregnancy:
        grace @ -m_talk "..."
    else:
        grace a_crossed @ -m_talk "..."
    odette f_confused "Congratulations?"
    grace f_tired_back "No, not congratulations!"
    show anon f_depressed
    grace f_angry_back "What's the matter with you?"
    odette "Heh, I dunno... It's what people are supposed to say, isn't it?"
    grace f_angry "You can't be pregnant, you're only eighteen!"
    odette f_normal @ f_eyeroll "Pretty sure people get pregnant a lot younger than eighteen, babe..."
    grace f_tired_back "That's not what I-"
    grace "Ugh, can you just shut up for two seconds while I talk to my sister?!"
    show grace f_tired
    eve "Look, {b}[firstname]{/b} and I talked, we've decided to keep it."
    grace f_angry "Are you out of your mind?!"
    grace "What about school?"
    eve "I can still finish school with a baby..."
    eve "Lots of girls do it."
    grace "Y-yeah, but-"
    grace "What about money?"
    grace "Babies are expensive, you know?"
    odette "We can help them."
    grace f_angry_back "Huh?"
    grace "How are we going to help them?"
    grace "A month ago, I could barely make the rent payments!"
    odette "Hehe, well, a lot has changed in that month, hasn't it?"
    grace f_tired @ -m_talk "..."
    if M_grace.pregnancy:
        grace f_proud "I dunno you guys, this just seems like terrible timing..."
    else:
        grace a_facepalm f_proud "I dunno you guys, this just seems like terrible timing..."
    pause
    grace f_tired a_idle "Wouldn't you rather wait a few years?"
    grace "Finish college, find a good job, become financially stable?"
    eve "Yeah, in an ideal world, sure..."
    eve "But what if this is my only chance?"
    odette f_confused @ -m_talk "Hmm?"
    odette "Why would this-"
    grace f_sad_down "{i}*Sigh*{/i} Because the doctor told us after the accident that she probably wouldn't be able to conceive."
    odette f_surprised "Oh, shit."
    eve f_sad_down @ -m_talk "..."
    odette f_sad "I'm sorry, {b}Evie{/b}, I didn't know that."
    eve "Yeah well, it's not exactly something that's easy to talk about."
    grace f_sad "... But this proves that you can, {b}Eve{/b}!"
    grace "If it happened once, it can happen again."
    eve f_angry "You don't know that!"
    show grace f_sad_down
    odette "Sorry babe, but I gotta side with your sister on this one..."
    odette "She should have this kid."
    grace f_suspicious "And you're on board with this?"
    anon f_worried "Of course."
    show grace f_sad
    eve "C'mon {b}Sis{/b}, I really need you with me on this!"
    grace "Tsk, well, of course I'm with you... I'm always with you, no matter what!"
    grace "I just worry, you know that."
    anon f_normal "Just think, pretty soon, you're going to be an aunt!"
    odette f_smirk "{b}Aunt Grace{/b} does have a nice ring to it, don't you think?"
    grace f_happy "Yes, it does."
    eve f_happy "Boring old {b}Aunt Grace{/b}..."
    grace f_tired "{i}*Gasp*{/i} I am not boring!"
    eve @ f_laugh "But you are old!"
    show grace f_tired_back
    odette @ f_laugh "Hehehe!"
    odette "At least you'll be the {b}Aunt{/b} with the hot girlfriend, huh?"
    grace a_idle "Oh, you think I'm going to meet someone hot soon?"
    show grace f_happy_back
    odette f_sad "Hey!"
    eve @ f_laugh "Hehehe!"
    show odette f_normal
    if M_grace.pregnancy:
        grace f_happy "I'll make a doctor's appointment for you tomorrow, okay?"
    else:
        grace f_happy @ a_idea "I'll make a doctor's appointment for you tomorrow, okay?"
    eve "Alright."
    grace "Then on the way home, we'll stop and get a bunch of those what to expect when you're expecting books."
    hide grace
    show eve b_dressed_hug_grace1 f_nervous_down
    with dissolve
    show odette f_smirk
    eve "Thank you, {b}Sis{/b}."
    show eve f_happy_closed
    grace "You're welcome."
    pause
    show eve b_dressed
    show grace f_happy:
        xoffset -150
    with dissolve
    grace "I just hope the kid takes after {b}[firstname]{/b}..."
    grace "I'm not sure I could survive another you..."
    odette "True that!"
    eve @ f_laugh "Hehehe!"
    scene black with dissolve
    pause

    $ player.go_to(L_tattooparlor)
    scene expression player.location.background_blur with dissolve
    show anon f_worried with dissolve
    anon @ -m_talk "( Wow, I can't believe {b}Eve{/b} is pregnant... )"
    anon f_brag_closed @ -m_talk "( ... And she said she loves me! )"
    anon @ -m_talk "( What a great day. )"
    hide anon with dissolve
    return

label tattoo_parlor_apartment_eve_baby_first:
    scene expression player.location.background_blur
    show odette f_smirk:
        xoffset 100
    show eve b_pajamas a_baby f_happy_down:
        xoffset -150
    show grace f_happy:
        flip
        xoffset 200
    with None
    show anon:
        xoffset -100
    with dissolve
    if M_eve.pregnancy.baby_gender == "boy":
        odette "Wow, look at this little guy!"
        odette "He's like a tiny, fat clone of {b}[firstname]{/b}!"
    else:
        odette "Wow, look at this little girl!"
        odette "She's like a tiny, fat clone of {b}Eve{/b}!"
    show eve f_angry_right
    grace @ f_laugh "Haha!"
    anon f_worried @ -m_talk "..."
    eve "Hey, don't call my kid fat!"
    odette "Oh, relax... It's just baby weight."
    pause
    odette "I can't believe you pushed this out of your vagina!"
    odette "It must be a war zone down there."
    eve f_sad_down @ -m_talk "..."
    grace "Yeah, let's not talk about that..."
    grace "How about I order us some Chinese food?"
    eve f_happy "Yes, please!"
    show anon f_normal
    odette "Oh, Chinese?"
    odette "That sounds delicious."
    grace f_happy_back "You want some {b}[firstname]{/b}?"
    anon "Sure, thanks!"
    hide grace with dissolve
    odette "I am so buying this kid a white t-shirt, red shorts, and a pair of flip-flops!"
    eve f_angry_right "Shut up, {b}Odette{/b}!"
    odette @ f_laugh "Hehehe!"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
