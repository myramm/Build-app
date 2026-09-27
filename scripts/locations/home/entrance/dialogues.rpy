label entrance_jenny_pregnancy_first_baby_coming_home:
    scene expression player.location.background_blur
    $ player.last_baby_gender = M_jenny.pregnancy.baby_gender
    show jenny b_casual a_baby f_happy with None:
        flip
        xoffset 150
    show debbie with None
    show anon f_normal:
        xoffset 450
    with dissolve
    anon "Hey, you're home!"

    show jenny f_eyeroll
    jenny "Yeah, finally..."

    show jenny f_upset
    jenny "I hate hospitals, so much!"

    debbie "I'm making you a big welcome home steak for dinner, dear."

    show jenny f_happy
    jenny "Oh, that sounds amazing!"

    pause
    if M_jenny.pregnancy.baby_gender == "twins":
        jenny "Would you mind watching them for a little bit?"

    elif M_jenny.pregnancy.baby_gender == "boy":
        jenny "Would you mind watching him for a little bit?"

    else:
        jenny "Would you mind watching her for a little bit?"

    jenny "I would literally kill for a bath right now."

    if M_jenny.pregnancy.baby_gender == "twins":
        debbie "Of course, I'll watch them!"

        debbie "Come see grandma, little ones!"

        show debbie f_normal_down a_baby
        show jenny a_sides
        with dissolve
        debbie "Aww, they're so cute!"

    elif M_jenny.pregnancy.baby_gender == "boy":
        debbie "Of course, I'll watch him!"

        debbie "Come see your grandma, little guy!"

        show debbie f_normal_down a_baby
        show jenny a_sides
        with dissolve
        debbie "Aww, such a cutie pie!"

    else:
        debbie "Of course, I'll watch her!"

        debbie "Come see your grandma, little girl!"

        show debbie f_normal_down a_baby
        show jenny a_sides
        with dissolve
        debbie "Aww, such a cutie pie!"

    show jenny f_happy
    jenny "Thanks, Mom."

    anon "Welcome home, {b}[jen_name]{/b}!"

    jenny "Yeah, thanks, {b}[firstname]{/b}."

    show jenny f_upset
    jenny "Out of my way, I have a date with the bath tub!"

    jenny "And don't bother me!"

    anon f_worried "I wasn't going to..."

    jenny "Eh ya."

    hide jenny with dissolve
    pause
    anon f_normal "The tyrant returns, huh?"

    show anon f_grin
    debbie f_normal @ -m_talk "Hmm?"

    anon f_tired "Sudahlah."

    hide anon with dissolve
    return

label entrance_jenny_first_baby_stage_2_end:
    pause
    show jenny f_upset
    jenny "So, now what?!"

    show debbie f_curious
    pause
    show anon f_worried
    anon "{b}[deb_name]{/b}?"

    anon "Apakah kamu baik-baik saja?!"

    debbie @ f_laugh "I'm just happy!"

    jenny "Happy?!"

    debbie @ f_normal "I can't believe I'm going to be a grandmother!"

    show jenny f_angry_pouting_top
    jenny "..."
    debbie f_normal "Isn't it wonderful, {b}[firstname]{/b}?!"

    anon "Eh, ya?"

    debbie @ f_laugh "hehe!"

    show jenny b_empty a_empty f_surprised:
        xoffset 120
    show debbie b_robe_hug_jenny_bump behind jenny:
        xoffset -166
    with dissolve
    debbie "{i}*Sniff*{/i} Your child is going to be the luckiest kid in the whole world!"

    show jenny f_sad
    jenny "Mom..."

    show jenny b_dressed_pregnant_bump a_sides:
        flip
        xoffset 100
    show debbie b_robe a_idle:
        xoffset 90
    with dissolve
    debbie "You've gotta help out too, {b}[firstname]{/b}!"

    debbie f_sad "Being a single mother is hard, believe me."

    debbie "{b}[jen_name]{/b}'s gonna need all the support she can get."

    show debbie f_normal
    anon f_normal "Y-ya, tentu saja!"

    debbie "Why don't you two go into the dining room and sit down?"

    debbie @ f_laugh "I'll make us a nice big breakfast to celebrate!"

    anon @ f_laugh "Ya baiklah."

    anon "C'mon, {b}[jen_name]{/b}!"

    hide anon with dissolve
    show jenny f_sad
    jenny "Thanks, Mom."

    debbie "You're welcome, dear."

    scene black with fade
    return

label entrance_jenny_first_baby_stage_2_no_diane:
    pause
    show debbie f_sad
    debbie "Just tell me, {b}[jen_name]{/b}."

    pause
    show jenny f_upset
    jenny "I think I got pregnant from a toilet seat at the mall..."

    debbie @ f_surprised_worried "{i}*Terkesiap*{/i}"

    show anon f_surprised
    anon @ -m_talk "!!!"
    show anon f_worried
    debbie "Itu bukan-"

    pause
    debbie @ f_surprised_worried "Can that even happen?"

    pause
    show jenny f_eyeroll
    jenny "I dunno, probably..."

    show jenny f_upset
    pause
    debbie "Look, you don't have to tell me if you don't want to..."

    debbie "... It's your decision."

    debbie "The important thing is that the baby is healthy and you get the care you need."

    jenny "B-benarkah?"

    debbie "Of course, dear."

    debbie "I just wish you had told me sooner, I could have been more help!"

    return

label entrance_jenny_first_baby_stage_2_diane:
    show diane f_laugh
    diane "Probably because she's sleeping with half the town..."

    show diane f_smirk
    show jenny f_angry
    jenny "Persetan denganmu!"

    show diane f_annoyed
    debbie f_angry "Hey, stop it! Both of you!"

    show jenny f_angry_pouting_top
    jenny "Hmm!"

    pause
    debbie f_sad "Just tell me, {b}[jen_name]{/b}."

    pause
    show jenny f_upset
    jenny "I think I got pregnant from a toilet seat at the mall..."

    show diane f_laugh
    debbie @ f_surprised_worried "{i}*Terkesiap*{/i}"

    show anon f_surprised
    anon @ -m_talk "!!!"
    show anon f_worried
    diane "Hahahaah, that's the most ridiculous thing I've ever heard!"

    show diane f_smirk
    show jenny f_angry
    jenny "Shut up, {b}Diane{/b}!!!"

    show jenny f_upset
    debbie "Itu bukan-"

    pause
    debbie @ f_surprised_worried "Can that even happen?"

    diane "Tidak."

    jenny "Yes, it can!!"

    show jenny f_angry_pouting_top
    show diane f_lookup
    diane "It really can't."

    show diane f_smirk
    debbie "{i}*Sigh*{/i} Stop."

    debbie "Look, she doesn't have to tell me if she doesn't want to-"

    show diane f_lookup
    diane "The hell she doesn't!"

    show diane f_shamed_smile_back
    diane "You deserve better than-"

    show diane f_shamed
    debbie "It's alright, {b}Diane{/b}..."

    debbie "... It's her decision."

    debbie "The important thing is that the baby is healthy and {b}[jen_name]{/b} gets the care she needs."

    show diane f_shamed_smile_back
    diane "Good lord, {b}[deb_name]{/b}..."

    diane "... You coddle her way too much!"

    show diane f_shamed
    debbie "Just let it go, please."

    diane @ -m_talk "..."
    show diane f_normal
    diane "Bagus."

    diane "I've gotta get going anyways..."

    show debbie b_empty f_normal
    show diane b_hug_deb_robe:
        flip
        xoffset 404
    with dissolve
    diane "... I'll see you tonight, love."

    debbie @ -m_talk "..."
    hide diane
    show debbie b_robe a_idle:
        xoffset 90
    with dissolve
    return

label entrance_jenny_first_baby_stage_2_intro:
    scene expression L_home_entrance.background_blur
    debbie "Why won't you tell me who the father is?!"

    show anon f_shock
    anon @ -m_talk "!!!" with hpunch
    jenny "Mom, would you please chill out?!"

    anon f_surprised_teeth "( Uh oh, it sounds like {b}[jen_name]{/b}'s secret is out... )"

    anon "( I'd better get down there! )"

    $ player.go_to(L_home_kitchen)
    scene expression player.location.background_blur
    show jenny b_dressed_pregnant_bump f_upset zorder 1:
        flip
        xoffset 100
    show debbie f_sad zorder 1:
        xoffset 90
    if M_diane.finished_state(S_diane_check_barn_out):
        show diane b_casual f_smirk zorder 0:
            xoffset -100
    show anon f_worried zorder 2 with dissolve:
        xoffset -100
    debbie "Why won't you tell me who the father is?"

    jenny "I don't know who the father is, okay Mom?!"

    jenny "Stop asking!"

    debbie "How can you not know?!"

    return

label entrance_jenny_want_some_breakfast:
    scene expression player.location.background_blur with None
    show anon
    show debbie
    with dissolve
    debbie "Sweetie, could you come in here for a second?"

    anon "Tentu."

    $ player.go_to(L_home_kitchen)
    scene expression player.location.background_blur with None
    show anon f_normal
    show debbie
    with dissolve
    anon "What's up, {b}[deb_name]{/b}?"

    debbie "Would you mind {b}poking your head outside{/b} and asking {b}[jen_name]{/b} if she wants some of this breakfast?"

    anon f_worried "Ehh, I don't mind."

    anon "She's just gonna say no..."

    debbie @ f_laugh "Hehe, probably."

    hide anon
    show debbie b_robe_hug1
    with dissolve
    debbie "Terima kasih sayang."

    show debbie b_robe_hug2
    anon "Tidak masalah."

    hide debbie
    show anon f_thinking a_thinking
    with dissolve
    anon @ -m_talk "( Hmm, menurutku {b}[jen_name] sedang bersantai di tepi kolam renang{/b}... )"

    hide anon with dissolve
    return

label entrance_jenny_catch_her_jilling:
    $ player.location = L_home_entrance
    if store._in_replay is not None:
        $ game.timer._tod = 3
    scene expression player.location.background_blur with None
    show anon f_thinking a_thinking at flip
    with dissolve
    anon @ -m_talk "(Hmm?)"

    anon @ -m_talk "( Why is the TV on? )"

    pause
    anon @ -m_talk "( Did someone forget to turn it off? )"

    anon @ -m_talk "( I should check it out. )"

    hide anon with dissolve
    scene expression "backgrounds/location_home_livingroom_couch_night_closeup.jpg"
    anon "( Is that {b}[jen_name]{/b}?! )"

    anon "( What's she- )"

    scene expression "backgrounds/location_home_livingroom_couch01.jpg"
    show player 300 at Position(xpos=566,ypos=331)
    show jenny b_couch_clit a_empty f_empty zorder 2
    anon "( !!! )"
    hide player
    show player 299d zorder 1 at Position (yoffset=-291,xoffset=16)
    with dissolve
    pause
    show player 301 at Position(xpos=602,ypos=386) with fastdissolve
    anon "( She's masturbating in the living room! )"

    anon "( This is awesome! )"

    pause
    anon "( What is she watching?! )"

    scene location_home_tv_night
    show home_tv_channel_10 at Position(xpos=522, ypos=521)
    with dissolve
    anon "( It's a woman jerking some guy off with her feet! )"

    pause
    scene expression "backgrounds/location_home_livingroom_couch01.jpg"
    show player 301 at Position(xpos=602,ypos=386)
    show jenny b_couch_clit a_empty f_empty
    anon "Feet?!"

    show jenny b_couch_cought
    jenny "!!!" with hpunch
    jenny "Apa-apaan ini, {b}[firstname]{/b}?!"

    hide player
    show anon b_couch_sit a_boner_covered f_couch_sit_right zorder 1
    show jenny b_couch_sit f_angry a_rest zorder 2
    with dissolve
    anon "Maafkan aku, aku-"

    jenny "Are you just stalking me all over the house now?!"

    anon "Shh, you're gonna wake {b}[deb_name]{/b}!"

    show jenny f_upset
    jenny "Seriously, what do I have to do to get some alone time?!"

    jenny "It's really beginning to-"

    show jenny f_surprised
    jenny "Are you hard right now?"

    anon @ f_couch_sit_down "Uhh, yeah..."

    anon "You were masturbating and it was really hot and..."

    jenny "Yesus."

    show jenny f_sexy_down
    pause
    jenny "Let me see it."

    anon "Hah?"

    jenny "Show me!"

    anon "O-oke..."

    show anon f_couch_sit_down a_boner_pull1 with dissolve
    pause
    show anon a_boner_pull2 with dissolve
    show anon a_boner with dissolve
    jenny "I've always wanted to try this..."

    show jenny a_up with dissolve
    anon @ f_couch_sit_down_surprised -m_talk "!!!"
    show anon a_sides
    $ M_jenny.set('sex speed', .3)
    show jenny a_empty
    show expression AnimatedImage("jenny_couch_dick_rub", [1,2,3], M_jenny) as jenny_couch_dick_rub zorder 3 at Position(xalign = 0.0, yoffset = 0)
    with dissolve
    anon "Apa yang kamu-"

    jenny "Ssst!"

    jenny "Now you're the one who's going to wake up my mom!"

    anon @ -m_talk "..."
    pause
    if store._in_replay is not None:
        jump jenny_couch_fj_loop
    return

label entrance_jenny_catch_her_leaving_has_money_dom:
    show anon f_worried
    anon "Di Sini."

    show anon a_money2 with dissolve
    pause
    show anon a_idle
    show jenny f_upset a_money
    with dissolve
    jenny "It's about freaking time..."

    show jenny f_grin_down a_money_counting
    pause
    anon "Can I go with you?"

    show jenny f_upset a_hips with dissolve
    jenny "What?! NO!"

    anon f_grumpy "Ayolah!"

    jenny "Sama sekali tidak!"

    jenny "I'm not going out in public with a loser like you..."

    show jenny f_gross
    anon f_worried "... But I've given you so much money and-"

    pause
    show jenny f_upset
    jenny "You are such a pain in my ass..."

    show anon b_dressed_bow with dissolve
    anon "P-please?!"

    pause
    show jenny f_eyeroll
    jenny "{i}*Sigh*{/i} Fine, just quit whining."

    show jenny f_upset
    show anon f_normal b_dressed with dissolve
    anon "Manis!"

    jenny "... And don't walk too close! I don't want people thinking we're together."

    anon f_worried "O-oke."

    hide anon
    hide jenny
    with dissolve
    return

label entrance_jenny_catch_her_leaving_no_money_dom:
label entrance_jenny_catch_her_leaving_no_money_sub:
label entrance_jenny_catch_her_leaving_no_money_dom_first:
    show anon f_shy a_behind_head with dissolve
    anon "Actually, I don't have two hundred right now..."

    show anon a_idle with dissolve
    show jenny f_upset
    jenny "Ugh, are you kidding me?"

    show anon f_worried
    pause
    jenny "Well, go and get it!"

    anon f_grumpy "Ya, ya..."

    show jenny f_angry
    jenny "aku serius!"

    anon "I'll get it, just chill out."

    jenny "Cepatlah!"

    hide anon
    hide jenny
    with dissolve
    return

label entrance_jenny_catch_her_leaving_repeat:
    scene expression player.location.background_blur with None
    show anon f_worried
    show jenny b_casual f_upset
    with dissolve
    jenny "You get the money yet?"

    return

label entrance_jenny_catch_her_leaving_has_money_sub:
    show anon f_worried
    anon "Di Sini."

    show anon a_money2 with dissolve
    pause
    show anon a_idle
    show jenny f_upset a_money
    with dissolve
    jenny "It's about freaking time..."

    show jenny f_grin_down a_money_counting
    pause
    anon "Can I go with you?"

    show jenny f_upset a_hips with dissolve
    jenny "What?! NO!"

    anon f_grumpy "Ayolah!"

    jenny "Sama sekali tidak!"

    jenny "I'm not going out in public with a loser like you..."

    show jenny f_gross
    anon "... But I've given you so much money and-"

    pause
    show jenny f_upset
    jenny "You are such a pain in my ass..."

    show anon b_dressed_bow with dissolve
    anon "P-please?!"

    pause
    show jenny f_eyeroll
    jenny "{i}*Sigh*{/i} Fine, just quit whining."

    show jenny f_upset
    show anon f_normal b_dressed with dissolve
    anon "Manis!"

    jenny "... And don't walk too close! I don't want people thinking we're together."

    anon f_worried "O-oke."

    hide anon
    hide jenny
    with dissolve
    return

label entrance_jenny_catch_her_leaving:
    show expression player.location.background_blur with None
    show anon f_worried
    show jenny b_casual a_phone f_grin_down:
        flip
        xoffset 500
    with dissolve
    pause
    anon "Kemana kamu pergi?"

    show jenny f_gross_down
    jenny "Out."

    show jenny f_grin_down
    anon "Uhh, okay?"

    pause
    anon f_skeptical "Care to elaborate?"

    show jenny f_gross_down
    jenny "Tch, I need to pick up some things from the mall..."

    show jenny f_grin_down
    pause
    anon f_worried "What kind of things?"

    show jenny f_eyeroll
    jenny "None of your business, loser!"

    jenny "I don't know why you've always gotta have your nose in MY BUSINESS?!"

    show jenny f_gross_down
    pause
    show anon f_grumpy
    show jenny f_angry_pouting_top
    pause
    hide jenny
    show jenny b_casual f_upset
    with dissolve
    jenny "How much money do you have?"

    anon f_worried "Hah?"

    jenny "Give me two hundred dollars."

    anon @ f_skeptical "No way, I've given you tons of money already!"

    show jenny f_eyeroll
    jenny "Psh! Yeah, and you got stuff in return!"

    show jenny f_upset
    jenny "Don't act like I haven't been more than fair with you..."

    return

label entrance_jenny_catch_her_leaving_dom_first:
    show anon f_worried
    anon "Alright, so what do I get this time?"

    show jenny f_upset
    jenny "Tsk, you ain't getting shit."

    anon f_grumpy "Bagus."

    show anon with dissolve:
        flip
        xoffset -500
    anon "Have fun shopping."

    jenny "W-wait!"

    show anon f_snarky with dissolve:
        unflip
        xoffset 0
    pause
    show jenny f_angry
    jenny "Grr, damn it!"

    show jenny f_angry_pouting
    pause
    show jenny f_angry
    jenny "Why won't you just do what I fucking ask?!"

    anon f_worried @ f_skeptical "Why don't you ever ask me nicely?"

    show jenny f_upset
    jenny "Ayo, {b}[firstname]{/b}!"

    jenny "You owe me for that screw up with the toy the other day."

    anon f_thinking a_thinking @ -m_talk "( Man, screw her. She's lucky I bought her that toy at all... )"

    anon @ -m_talk "( ... Then again, this might be a good opportunity to learn more about what she's doing for that money. )"

    jenny "So are you gonna give me the money or not?"

    anon a_idle f_worried @ f_skeptical a_idle "Yeah, I guess... If you say please."

    show jenny f_eyeroll
    jenny "Ugh..."

    jenny "... Please?"

    show jenny f_angry_pouting_top
    return

label entrance_jenny_catch_her_leaving_sub_first:
    show anon f_snarky
    anon "Y-ya, oke, tapi-"

    show anon f_surprised
    show jenny f_upset
    jenny "Quit being such a little bitch, {b}[firstname]{/b}!"

    jenny "You make plenty of money."

    jenny "Besides, you owe me for that little screw up with the toy the other day."

    anon f_thinking a_thinking @ -m_talk "( Ugh, I guess she's right about that... )"

    anon @ -m_talk "( ... And this might be a good opportunity to learn more about what she's doing for that money. )"

    jenny "Umm, hello?!"

    jenny "Earth to loser!"

    anon a_idle f_tired "{i}*Huh*{/i} Baik."

    anon f_worried "You said two hundred?"

    show jenny f_grin
    jenny "Ya."

    return

label entrance_jenny_debbie_altercation:
    scene expression player.location.background_blur with None
    show jenny f_upset a_crossed
    show old_debbie 10bf zorder 1 at left
    jenny "Kenapa tidak?!"

    show old_debbie 11bf
    debbie "Because I can't afford it!"

    debbie "You're not a kid anymore {b}[jen_name]{/b}..."

    debbie "If you want new clothes then you need to get yourself a job and buy them with your own money."

    show old_debbie 10bf
    show anon f_worried zorder 0:
        xoffset 75
    jenny "Ugh, how am I supposed to get a job when I have nothing nice to wear to the interview?!"

    show old_debbie 9bf with dissolve
    pause
    show old_debbie 11bf with dissolve
    debbie "{b}[jen_name]{/b}, you have plenty of nice clothes..."

    show old_debbie 10bf
    jenny "Not nice enough, not for the job I want..."

    anon @ f_skeptical "What the heck kind of job are you trying to get?"

    show jenny f_eyeroll
    jenny "I don't know, something with an office maybe?"

    show jenny f_upset
    anon f_laugh "Hah, yeah right."

    anon f_snarky "I don't think many companies are looking for a college dropout with no qualifications and zero experience..."

    jenny "Shut up, turd!"

    jenny "Who asked for your opinion?!"

    show anon f_surprised
    show old_debbie 11bf
    debbie "Would you two cut it out?!"

    show jenny f_angry_pouting
    debbie "I'm so sick of you fighting all the time."

    show old_debbie 10bf
    anon f_sad "Maaf, {b}[deb_name]{/b}."

    show anon f_worried
    show old_debbie 11bf
    debbie "{i}*Sigh*{/i} Just borrow something out of my closet, {b}[jen_name]{/b}."

    show old_debbie 10bf
    show jenny f_upset
    jenny "Bagus."

    pause
    show old_debbie 11bf
    debbie "You should have never quit your job at {b}Consum-R{/b}..."

    show old_debbie 10bf
    jenny "Psh, that job was lame!"

    show anon a_phone f_looking_down with dissolve
    show old_debbie 11bf
    debbie "Oh, grow up, {b}[jen_name]{/b}."

    debbie "Do you think everyone enjoys what they do for a living?!"

    show old_debbie 10bf
    jenny "... Tidak."

    show old_debbie 11bf
    debbie "People do what they have to in order to put food on the table!"

    debbie "I can't support you forever, you know?!"

    show old_debbie 10bf
    show anon a_idle f_worried with dissolve
    jenny "Oh, that's real nice, Mom..."

    show jenny f_eyeroll
    jenny "... Sorry I'm such a HUGE burden on you guys!"

    show jenny f_upset
    show old_debbie 11bf
    debbie "I never said that."

    show old_debbie 10bf
    jenny "You might as well have!"

    jenny "Don't worry, you won't have to suffer me much longer."

    jenny "The second I get a little money, I'm gone."

    show jenny f_angry_pouting_top
    show old_debbie 11bf
    debbie "... Good grief."

    debbie "Why do you always have to turn everything into a big drama?!"

    show old_debbie 10bf
    show jenny f_angry_pouting
    jenny "..."
    show old_debbie 11bf
    debbie "{i}*Sigh*{/i} You know I love you {b}[jen_name]{/b} and you're not a burden..."

    debbie "I'm just saying you need to do something with your life."

    debbie "You can't sit around on your ass forever, waiting for the perfect opportunity to present itself."

    debbie "You have to go out and make it happen."

    show old_debbie 10bf
    show jenny f_upset
    jenny "Ya, ya..."

    hide jenny with dissolve
    jenny "God, I can't wait to leave this stupid town!"

    pause
    show old_debbie at center
    show anon
    with dissolve
    debbie "..."
    show old_debbie 11bf
    debbie "Maybe I'm being too hard on her?"

    show old_debbie 10bf
    anon f_worried "Eh, tidak juga."

    anon "I mean, I'm helping out around here, and she's older than I am..."

    show old_debbie 11bf
    debbie "Aku tahu."

    hide anon
    show old_debbie 4b at left
    with dissolve
    debbie "I really appreciate it, sweetie."

    debbie "You're such a good boy."

    show old_debbie 4
    pause
    show anon
    show old_debbie 2 at right
    with dissolve
    debbie "Want me to fix you something to eat?"

    show old_debbie 1
    anon "N-no, that's okay {b}[deb_name]{/b}..."

    anon "I'm not really hungry."

    show old_debbie 2
    debbie "Oh baiklah."

    debbie "Maybe I'll bake a pie..."

    debbie "... Something to get my mind off all this drama."

    show old_debbie 1
    anon @ f_laugh "Hehe, oke."

    hide old_debbie with dissolve
    pause
    anon f_worried @ -m_talk "( Poor {b}[deb_name]{/b}. )"

    anon @ -m_talk "( {b}[jen_name]{/b} doesn't realize how lucky she is... )"

    hide anon with dissolve
    return

label entrance_diane_gave_birth_dialogue_seen:
    scene expression L_home_entrance.background_blur
    show player 10 at left
    show old_debbie 1f at Position (xpos=600)
    show diane a_baby b_casual:
        xoffset 125
    show jenny f_grin:
        flip
        xoffset 150
    with dissolve
    player_name "{b}Diane{/b}?"

    show player 14
    player_name "You guys are finally home?"

    show player 13
    diane "Yup, we're home."

    show old_debbie 2f
    show diane f_down_front
    if M_diane.pregnancy.baby_gender == "boy":
        debbie "Isn't he just the most precious thing ever?!"

        show old_debbie 1f
        show jenny f_normal
        jenny "I dunno, he kinda looks like a potato..."

        show old_debbie 2f
        debbie "No he doesn't!"

        debbie "He's so handsome!"

        show old_debbie 1f
        pause
        show old_debbie 2f
        debbie "Who's a handsome boy, huh?"

    elif M_diane.pregnancy.baby_gender == "twins":
        debbie "Aren't they just the most precious things ever?!"

        show old_debbie 1f
        show jenny f_normal
        jenny "I dunno, they kinda look like potatoes..."

        show old_debbie 2f
        debbie "No they don't!"

        show old_debbie 1f
        pause
        show old_debbie 2f
        debbie "Who's beautiful, huh?"

    else:
        debbie "Isn't she just the most precious thing ever?!"

        show old_debbie 1f
        show jenny f_normal
        jenny "I dunno, she kinda looks like a potato..."

        show old_debbie 2f
        debbie "No she doesn't!"

        debbie "She's beautiful!"

        show old_debbie 1f
        pause
        show old_debbie 2f
        debbie "Who's a pretty girl, huh?"

    show old_debbie 1f
    show diane f_laugh
    diane "hehe!"

    show diane f_normal
    show old_debbie 2f
    if M_diane.pregnancy.baby_gender == "twins":
        debbie "I can't believe you finally have kids, {b}Diane{/b}."

    else:
        debbie "I can't believe you finally have a child, {b}Diane{/b}."

    debbie "I'm so happy for you!"

    show old_debbie 1f
    diane "I know, I didn't think I'd ever get to be a mommy."

    show old_debbie 2f
    show diane f_down_front
    if M_diane.pregnancy.baby_gender == "boy":
        debbie "He's so adorable..."

        show jenny f_eyeroll
        show old_debbie 3f
        debbie "I could just gobble him up!"

        show old_debbie 1f
        show jenny f_normal
        pause
        show diane f_normal
        diane "I should really get him down for the night."

        diane "He's had a busy day."

    elif M_diane.pregnancy.baby_gender == "twins":
        debbie "They're so adorable..."

        show jenny f_eyeroll
        show old_debbie 3f
        debbie "I could just gobble them up!"

        show old_debbie 1f
        show jenny f_normal
        pause
        show diane f_normal
        diane "I should really get them down for the night."

        diane "They've had a busy day."

    else:
        debbie "She's so adorable..."

        show jenny f_eyeroll
        show old_debbie 3f
        debbie "I could just gobble her up!"

        show old_debbie 1f
        show jenny f_normal
        pause
        show diane f_normal
        diane "I should really get her down for the night."

        diane "She's had a busy day."

    show diane f_down_front
    show old_debbie 2f
    debbie "Ah, oke..."

    if M_diane.pregnancy.baby_gender == "twins":
        debbie "Bye-bye, little ones."

    else:
        debbie "Bye-bye, little one."

    show old_debbie 1f
    pause
    show old_debbie 1 at right
    show jenny:
        xoffset 200
    hide diane
    with dissolve
    pause
    show old_debbie 3
    debbie "Oh, I just love babies!"

    show old_debbie 1
    show jenny f_eyeroll
    jenny "Ugh, terserah."

    show jenny f_upset
    if M_diane.pregnancy.baby_gender == "twins":
        jenny "If those things are up all night screaming, I will absolutely lose my shit!"

    else:
        jenny "If that thing is up all night screaming, I will absolutely lose my shit!"

    show old_debbie 13
    debbie "{i}*Sigh*{/i} ... {b}[jen_name]{/b}..."

    debbie "Don't be like that, dear."

    show old_debbie 14b
    show jenny f_normal
    jenny "I'm just saying, I need my eight hours or I get cranky."

    show player 12
    player_name "You're always cranky..."

    show player 13 with None
    show jenny f_upset:
        unflip
        xoffset -200
    with dissolve
    jenny "What did you say?!"

    show jenny f_gross
    show player 10
    player_name "T-tidak ada."

    show player 5
    pause
    show jenny f_upset
    jenny "Eh ya."

    pause
    jenny "You better watch your mouth."

    jenny "I know where you sleep."

    hide jenny with dissolve
    pause
    show player 12
    player_name "She's such a ray of sunshine..."

    show player 13
    show old_debbie 3
    debbie "Hehehe!"

    show old_debbie 2
    debbie "Oh, jangan pedulikan dia."

    debbie "She likes babies too, she just doesn't want to admit it."

    show old_debbie 1
    show player 12
    player_name "Jika Anda berkata demikian."

    hide player
    hide old_debbie
    hide diane
    with dissolve
    return

label entrance_diane_peeking:
    scene expression L_home_entrance.background_blur
    show player 34 with dissolve
    pause
    show player 35
    player_name "Hmm, it sure is quiet in here tonight..."

    show player 10
    player_name "I wonder what {b}[deb_name]{/b} and {b}Diane{/b} are doing."

    show player 14
    player_name "{b}They're usually in the living room{/b} watching TV and having girl talk."

    player_name "I should {b}check on them{/b}."

    hide player with dissolve
    return

label entrance_diane_couch_crashing:
    scene expression background(l=L_home_entrance, t=3)
    show player 13 at left
    show diane b_casual a_bag f_laugh zorder 1:
        xoffset 50
    with dissolve
    diane "Honey, we're home!"

    diane "Haha!"

    show player 17
    player_name "Haha!"

    show diane f_normal
    show old_debbie 2f zorder 0 with dissolve
    debbie "What in the heck is going-"

    show old_debbie 3f
    show player 13
    debbie "{i}*Terkesiap*{/i} Anda di sini!"

    show old_debbie 2f
    diane "I'm here!"

    show diane a_bag_point with dissolve
    diane "Are we starting with a pajama party?"

    show diane a_bag
    show old_debbie 222f
    with dissolve
    debbie "Hah?"

    pause
    show old_debbie 3f with dissolve
    debbie "Oh, shuddup."

    show old_debbie 1f
    diane "I'm serious, I brought my nightgown and everything!"

    show old_debbie 2f
    debbie "Apakah kamu lapar?"

    show old_debbie 1f
    diane "Oh, room service and everything."

    show diane f_smirk
    diane "You didn't tell me it was gonna be so fancy..."

    show old_debbie 2f
    debbie "Just get in here and I'll help you unpack."

    show old_debbie 1f
    show diane f_laugh
    diane "Ya, Bu."

    show diane f_normal
    diane "You wanna join us, {b}[firstname]{/b}?"

    show old_debbie 1 with dissolve
    show player 55 with dissolve
    player_name "{i}*Menguap*{/i}"

    show player 26 with dissolve
    player_name "... Sure!"

    show player 25
    show old_debbie 2
    debbie "Oh sweetie, you look exhausted!"

    debbie "Why don't you just head on to bed and let {b}Diane{/b} and I spend some time together."

    show diane f_wink
    show old_debbie 1f with dissolve
    pause
    show diane f_smirk
    diane "Mmm, time together, huh?"

    debbie "Oh, hush!"

    show old_debbie 3f
    show diane f_laugh
    diane "Haha."

    show diane f_normal
    show old_debbie 1 with dissolve
    show player 26
    player_name "Ya baiklah."

    player_name "I am pretty tired."

    show player 25
    show diane f_smirk
    diane "I guess it's just you and me then, beautiful."

    show old_debbie 3f with dissolve
    debbie "Hehe, stop it!"

    show old_debbie 1f
    diane "Selamat malam, {b}[firstname]{/b}."

    show player 55
    hide old_debbie
    hide diane
    with dissolve
    pause
    hide player with dissolve
    return

label entrance_diane_debbie_drop_off_request:
    scene expression L_home_entrance.background_blur
    show player 13 at left
    show old_debbie 221 at right
    with dissolve
    debbie "Hold on, {b}[firstname]{/b}."

    show old_debbie 220
    show player 14
    player_name "Hey, {b}[deb_name]{/b}."

    player_name "Ada apa?"

    show player 13
    show old_debbie 221
    debbie "Did you do any work for {b}Diane{/b} today?"

    show old_debbie 220
    show player 14
    player_name "Yeah, I was over there earlier."

    show player 13
    show old_debbie 221
    debbie "Is she doing alright?"

    show old_debbie 220
    show player 5
    player_name "Hmm?"

    show player 10
    player_name "Ya, menurutku..."

    show player 5
    show old_debbie 221
    debbie "... 'Cause I just got off the phone with her, and she sounds exhausted."

    show old_debbie 220
    show player 10
    player_name "Well, she is working herself really hard with that new business of hers."

    player_name "I told her to slow down but you know how passionate she is about it."

    show player 5
    show old_debbie 221
    debbie "Yeah, she has a tendency to throw herself into her work and disregard her needs."

    debbie "It worries me."

    debbie "Would you mind heading back over there?"

    show old_debbie 220
    show player 10
    player_name "Malam ini?"

    show player 5
    show old_debbie 221
    debbie "Yeah, I want you to take her this pie I made today and make sure she eats it!"

    debbie "She probably hasn't eaten a thing all day."

    show old_debbie 220
    show player 14
    player_name "Ya, saya bisa melakukan itu."

    show player 13
    show old_debbie 221
    debbie "I would really appreciate it."

    show old_debbie 2
    show player 673
    with dissolve
    debbie "Tell her she had better get a solid eight hours sleep too or it'll be me visiting her next!"

    show old_debbie 1
    show player 674
    player_name "Hehe, baiklah."

    hide player with dissolve

    scene expression L_home.background_blur with fade
    show anon a_backpack2 f_surprised_down with dissolve
    anon @ -m_talk "( This pie isn't getting any warmer... Better move it! )"

    hide anon with dissolve

    scene expression L_diane_yard.background_blur with fade
    show anon a_backpack2 f_surprised_down with dissolve
    anon @ -m_talk "( Still warm, but I better find {b}Diane{/b} quickly! )"

    hide anon with dissolve
    return

label entrance_erik_bully_intro:
    scene expression L_home_entrance.background_blur
    show mrsj 19c at right with dissolve
    show player 10 at left with dissolve
    player_name "Is everything okay, {b}Mrs. Johnson{/b}?"

    show player 5
    show mrsj 19
    mrsj "Sorry to disturb you this morning."

    show mrsj 52
    mrsj "It's just... It's about {b}Erik{/b}."

    mrsj "Has {b}Erik{/b} been having trouble lately at school?"

    show mrsj 19c
    show player 12
    player_name "Hah?"

    show player 35
    player_name "Not that I know of?"

    show player 10
    player_name "He usually does well at school..."

    show player 5
    show mrsj 20
    mrsj "No. I'm not talking about grades."

    show mrsj 52
    mrsj "Have the other kids in school been giving {b}Erik{/b} a hard time?"

    mrsj "He's been asking to stay home instead of going to class."

    show mrsj 20
    mrsj "I... I even saw him come home last week with bruises."

    show mrsj 19c
    show player 23
    player_name "!!!" with hpunch
    show player 12
    player_name "{b}Erik{/b} is pretty quiet at school."

    player_name "I've never seen him get involved in any kind of bad stuff."

    show player 5
    show mrsj 19
    mrsj "Maybe if a close friend stopped over to him see him, he'd be more willing to talk..."

    show mrsj 19c
    show player 10
    player_name "You want me to ask him?"

    show player 5
    show mrsj 19
    mrsj "I just want what's best for him, and you're his only friend."

    show mrsj 19c
    show player 12
    player_name "Okay. I'll go see him."

    hide mrsj
    hide player
    with dissolve
    return

label entrance_erik_bully_return:
    scene expression L_home_entrance.background_blur
    show mrsj 19c at Position (xpos=700)
    show old_debbie 13 at right
    with dissolve
    show player 5 at left with dissolve
    debbie "Sweetie!! Are you okay?!"

    show old_debbie 14b
    show player 10
    player_name "I'm fine, {b}[deb_name]{/b}. The nurse said I just had a small concussion."

    show player 11
    show old_debbie 13
    debbie "You had a concussion!"

    show old_debbie 14b
    show player 10
    player_name "Everything is fine. I'll be okay, {b}[deb_name]{/b}."

    show player 5
    show old_debbie 13
    debbie "Your stupid school didn't even call to let me know you were in the hospital!"

    debbie "I had to hear about it from {b}Tammy{/b}!"

    show old_debbie 14b
    show player 10
    player_name "{b}[deb_name]{/b}, it's alright. I'm really fine! Calm down."

    show player 11
    show old_debbie 13
    debbie "I'm sorry... I was just so worried about you!"

    debbie "Your father is counting on me to watch over you!"

    show old_debbie 14b
    show mrsj 19
    mrsj "I'm so happy to see you're okay, {b}[firstname]{/b}."

    mrsj "I came over here to fill {b}[deb_name]{/b} in the second {b}Erik{/b} called me."

    mrsj "You did a good thing standing up for {b}Erik{/b}."

    show mrsj 38
    show old_debbie 13
    debbie "Yes, it was really brave of you to stand up for your friend at school."

    debbie "But, be please be careful!"

    show old_debbie 14b
    show player 24
    player_name "I know {b}[deb_name]{/b}..."

    show player 25
    player_name "I promise I'll try and stay out of trouble."

    show player 24
    show old_debbie 13
    debbie "Kemarilah."

    hide player
    show mrsj 14
    show old_debbie 4 at Transform(xalign=.3)
    with dissolve
    debbie "I'm so glad you're safe."

    debbie "Your father would just throw a fit if he knew I let this happen."

    player_name "It's alright, {b}[deb_name]{/b}."

    show old_debbie 1 at right
    show player 13 at left
    show mrsj 17
    with dissolve
    mrsj "Thanks again, {b}[firstname]{/b}."

    mrsj "You're always welcome to stop over and visit."

    show mrsj 14
    show player 14
    player_name "It's fine. Just helping a friend."

    show player 13
    show mrsj 17
    mrsj "Terima kasih."

    show mrsj 14
    show player 36 with dissolve
    player_name "Good night {b}Mrs. Johnson{/b}."

    show player 13 with dissolve
    show mrsj 17
    mrsj "Selamat malam."

    hide mrsj with dissolve
    show old_debbie 2
    debbie "Now hurry up to bed and get some rest."

    hide player
    hide old_debbie
    with dissolve
    return

label entrance_mia_angelicas_impatience:
    scene expression L_home_entrance.background_blur
    show old_debbie 1f at Position (xpos=500)
    show ang 1 at right
    with dissolve
    pause.5
    show player 5 at left
    show old_debbie 3
    with dissolve
    debbie "Itu dia!"

    show old_debbie 1
    show player 22
    player_name "!!!" with hpunch
    show old_debbie 2
    debbie "I'm so happy to hear {b}[firstname]{/b} visited our local church lately..."

    debbie "... And offered volunteer work with the clergy!"

    show old_debbie 1
    show player 24
    player_name "Uhh..."

    show old_debbie 2
    debbie "Well! I will leave you two to it, I have things cooking in the kitchen!"

    show old_debbie 2f with dissolve
    debbie "It was great meeting you {b}Sister Angelica{/b}!"

    hide old_debbie with dissolve
    show player 12
    player_name "Volunteer work?"

    player_name "And why are you here?!"

    show player 11
    show ang 2
    angelica "I thought we had an agreement?"

    show ang 1
    show player 24
    player_name "..."
    show ang 2
    angelica "Did you think I would just let you slip away from me?!"

    show ang 1
    show player 10
    player_name "No, I just... What do you want from me?"

    show player 11
    show ang 2
    angelica "The door of the church will be left unlocked at night."

    angelica "Come visit me in my chamber and I will explain what I need from you..."

    angelica "... And don't try to hide from me again, or else."

    show ang 1
    show player 12
    player_name "Oke oke!"

    player_name "Just don't say anything to my landlady..."

    show player 11
    show ang 2
    angelica "That will be up to you..."

    hide ang with dissolve
    show player 12
    player_name "Now I have to go see her at church? In the middle of the night?!"

    show player 10
    player_name "This is strange..."

    hide player with dissolve
    return

label entrance_mia_angelicas_home_visit:
    scene expression L_home_entrance.background_blur with fade
    show old_debbie 2f at Position (xpos=500)
    show ang 1 at right
    with dissolve
    pause.5
    show player 5 at left
    show old_debbie 3f
    with dissolve
    debbie "It's always a pleasure to hear that {b}[firstname]{/b} is actively involved with the church."

    debbie "You two must be getting to know each other quite well."

    show old_debbie 1f
    show ang 2
    angelica "Yes, {b}[firstname]{/b} has been very helpful bringing in remorsefully wretched sinners."

    angelica "God will surely remember his fruits of love to his neighbors."

    show ang 1
    show old_debbie 3f
    debbie "That's great!"

    debbie "I know we all can be naughty at times..."

    show old_debbie 2f
    debbie "Well then, I'd better get going. The laundry isn't going to fold itself."

    hide old_debbie with dissolve
    show ang 3
    player_name "..."
    show player 30
    player_name "Bagaimana sekarang?"

    player_name "I brought you {b}Helen{/b}. Isn't that enough?"

    show player 5
    show ang 4
    angelica "Oh no my dear child. God has many things in store for you."

    angelica "{b}Helen{/b} is far from being purified. Her stubbornness is most annoying."

    show ang 3
    show player 26
    player_name "Ceritakan padaku tentang hal itu."

    show player 5
    show ang 2
    angelica "The most penitent Christians require extra care."

    angelica "They need to be broken down from their pedestal so that we may build them back up."

    angelica "I believe it will take two more rituals for her..."

    angelica "That is why I have come to see you."

    angelica "I am in need of an essential tool used throughout biblical times."

    show ang 1
    show player 11
    player_name "..."
    show player 12
    player_name "What do you need?"

    show player 5
    show ang 2
    angelica "I intend to subvert {b}Helen{/b} through the means of flagellation."

    show ang 1
    show player 12
    player_name "Apa?"

    show player 5
    show ang 4
    angelica "{b}Get me a whip{/b}."

    show ang 3
    show player 23
    player_name "A whip?!"

    show player 11
    show ang 4
    angelica "I'd prefer a cat-o'-nine-tails of which our Savior was subjected to."

    angelica "But I fear that might be more difficult to come by."

    angelica "{b}A standard leather whip{/b} will do."

    show ang 2
    angelica "Bring it to me in my chambers."

    show ang 1
    show player 10
    player_name "This doesn't seem right at-"

    show player 11
    show ang 2
    angelica "Do you forget your place? Don't make me remind you and everyone else of your depraved sins!"

    show ang 1
    show player 15
    player_name "But you want to whip {b}Helen{/b}!"

    show player 16
    show ang 2
    angelica "You made a deal with me. Don't question my... The church's methods."

    show ang 1
    show player 12
    player_name "It's just not right."

    show player 5
    show ang 4
    angelica "And who are you to judge right from wrong?"

    show ang 3
    show player 24
    player_name "..."
    show player 12
    player_name "Fine. Where am I even supposed to get a whip though?"

    show player 17
    player_name "Is there a listing of distributors in the back of the Bible?"

    show player 5
    show ang 1
    angelica "..."
    show ang 2
    angelica "Saya yakin seseorang seusia Anda mengetahui tempat-tempat kotor dan penuh nafsu yang menjual barang-barang seperti itu."

    angelica "Don't keep me waiting."

    hide ang with dissolve
    show player 37 with dissolve
    player_name "I should never have gone to church."

    pause
    show player 38 with dissolve
    player_name "Where am I going to {b}get a whip{/b}?"

    player_name "Maybe the {b}Pink store at the mall{/b} carries something like that."

    show player 37 with dissolve
    player_name "..."
    hide player with dissolve
    return

label entrance_mia_angelicas_final_home_visit:
    scene expression L_home_entrance.background_blur with fade
    show player 11 at left
    show ang 2 at right
    with dissolve
    angelica "It's about time you came downstairs."

    angelica "I have need of you again."

    show ang 1
    show player 5
    player_name "..."
    show player 12
    player_name "I'm not sure I want to continue helping after what you did to {b}Helen{/b}, I-"

    show player 5
    show ang 4
    angelica "Oh, don't be so naive!"

    angelica "Despite her reluctance, we both know she enjoyed it."

    show ang 3
    show player 11
    player_name "..."
    show ang 2
    angelica "I didn't come here to argue with a sinner."

    show ang 39 with dissolve
    angelica "If you truly intend to help {b}Helen{/b} you will help me obtain this..."

    show ang 38
    pause
    show ang 3
    show player 459 at Position (xoffset=1)
    with dissolve
    player_name "..."
    hide player
    hide ang
    show note_01_c
    with dissolve
    pause
    hide note_01_c
    show player 1 at left
    show ang 3 at right
    show player 460 at Position (xoffset=1)
    with dissolve
    player_name "What... Is it?"

    show player 461 at Position (xoffset=1)
    show ang 4
    angelica "It is a crucial element to the final ritual of {b}Helen{/b}'s purification..."

    angelica "... And your last task."

    show ang 3
    show player 460 at Position (xoffset=1)
    player_name "But how is this going to be used to purify {b}Helen{/b}?"

    show player 11 with dissolve
    show ang 2
    angelica "Don't question me!"

    angelica "Sinners should just accept the words spoken by God's chosen."

    angelica "Now, {b}get me the item in the photograph and meet me in my chambers{/b}."

    show ang 1
    show player 5
    player_name "..."
    show player 12
    player_name "Baiklah..."

    show player 5
    show ang 2
    angelica "Good. And be quick about it."

    hide ang with dissolve
    show player 5
    player_name "..."
    show player 10
    player_name "{b}Helen{/b} doesn't even seem to realize {b}Sister Angelica{/b} is transforming her into..."

    player_name "... A sex freak!"

    show player 12
    player_name "I should talk with {b}Harold{/b} before I help out {b}Sister Angelica{/b}."

    player_name "Maybe he can help me figure out what to do."

    hide player with dissolve
    $ player.get_item("strapon_drawing")
    call popup ('give', 'strapon_drawing')
    return

label entrance_mom_overheard:
    scene expression player.location.background_blur
    show anon f_tired with dissolve
    debbie "No, I'm not going to pay you..."

    anon @ -m_talk "( Is that {b}[deb_name]{/b}? )"

    debbie "I don't even know who you are!"

    pause
    debbie "Ugh, that's ridiculous."

    debbie "He worked for the bank."

    anon f_surprised @ -m_talk "( ... She's talking about {b}Dad{/b}! )"

    debbie "None of this makes any sense!"

    anon @ -m_talk "( I should see what's going on. )"

    hide anon with dissolve
    return

label entrance_mom_lawn_help:
    scene expression L_home_entrance.background_blur
    show player 1 at left
    show old_debbie 2 at right
    with dissolve
    if game.timer.is_morning():
        debbie "Good morning, sweetie."

    else:
        debbie "Hello, sweetie."

    show old_debbie 1
    show player 2
    if game.timer.is_morning():
        player_name "Morning, {b}[deb_name]{/b}."

    else:
        player_name "Halo, {b}[deb_name]{/b}."

    show player 1
    show old_debbie 2
    if game.timer.is_morning():
        debbie "Ready for school?"

    else:
        debbie "Happy to be back at school?"

    show old_debbie 1
    show player 10
    player_name "Yeah, I guess. I have so much homework to catch up on."

    show player 1
    show old_debbie 3
    debbie "Oh, I'm sure you'll do fine."

    show old_debbie 2
    debbie "It's good to get back into a normal routine."

    show old_debbie 1
    show player 14
    player_name "Kukira."

    player_name "Apa yang kamu lakukan hari ini?"

    show player 13
    show old_debbie 13
    debbie "Oh, me?"

    debbie "Housework mostly. It keeps me pretty busy."

    debbie "It's not easy taking care of this big place by myself you know?"

    show old_debbie 14b
    show player 5
    pause
    show player 2
    player_name "I could help, you know?"

    show player 1
    show old_debbie 13
    debbie "You want to help with the housework?"

    show old_debbie 1
    show player 29 with dissolve
    player_name "Sure! I mean, I feel like I should pull my own weight around here..."

    show player 1 with dissolve
    show old_debbie 2
    debbie "That's a great attitude to have, {b}[firstname]{/b}!"

    show old_debbie 1
    debbie "Hmm..."

    show old_debbie 2
    debbie "Well, the lawn hasn't been mowed in weeks."

    debbie "You can start there if you want!"

    debbie "{b}The lawn mower should be in the garage{/b}."

    show old_debbie 1
    show player 14
    player_name "All right. I'll go take a look."

    show player 13
    show old_debbie 2
    debbie "Terima kasih, {b}[firstname]{/b}."

    debbie "Be careful!"

    hide old_debbie
    hide player
    with dissolve
    return

label entrance_mom_clothes_dirty:
    scene expression L_home_entrance.background_blur
    show player 11 zorder 1 at left
    show xtra 15 zorder 2 at Position(xpos=170,ypos=754)
    show jenny f_gross
    with dissolve
    jenny "Eugh, what's that smell?!"

    show player 14
    player_name "... Me I think. I was outside mowing the law-"

    show player 11
    jenny "That's disgusting! You're getting grass everywhere, you slob!"

    show player 12
    player_name "I'm sorry. I was just trying to help {b}[deb_name]{/b}."

    show player 11
    show jenny f_upset
    jenny "So what, you're going to start doing chores around here now?"

    show jenny f_grin a_crossed with dissolve
    jenny "You got a thing for my mom or something?"

    show player 10
    player_name "No! I'm just-"

    show player 11
    show jenny f_eyeroll
    jenny "Pfft, don't play dumb! I see what you're up to!"

    hide jenny with dissolve
    pause
    show player 12
    player_name "What's her problem?"

    show player 10
    player_name "Oh well, I should get these clothes {b}downstairs to the wash{/b}."

    hide player with dissolve
    return

label entrance_mom_pipe_help:
    scene expression L_home_entrance.background_blur
    show player 11 at left
    show old_debbie 13 at right
    with dissolve
    debbie "Sweetie! Thank god you're here!"

    show old_debbie 14b
    show player 10
    player_name "{b}[deb_name]{/b}?"

    show player 5
    show old_debbie 13
    debbie "{b}[jen_name]{/b} and I need your help."

    show old_debbie 14b
    show player 12
    player_name "Hah?"

    show player 5
    show old_debbie 13
    debbie "There's a broken pipe upstairs and water everywhere!"

    debbie "She's up there messing with it now."

    debbie "Could you go and help her?"

    show old_debbie 14b
    show player 10
    player_name "Me? I err..."

    show player 5
    show old_debbie 13
    debbie "I can't afford to call a repairman right now. Not with everything that's happened recently..."

    show old_debbie 14b
    show player 10
    player_name "Oh benar..."

    show player 14
    player_name "I'll go take a look."

    show player 13
    show old_debbie 2
    debbie "Thanks, sweetie! Let me know if there's anything I can do to help."

    show old_debbie 1
    show player 14
    player_name "Baiklah."

    hide old_debbie
    hide player
    with dissolve
    return

label entrance_mom_movie_night:
    scene expression L_home_entrance.background_blur
    show player 1 at left
    show old_debbie 62 at right
    debbie "Oh, hey, sweetie!"

    debbie "Heading to bed?"

    show player 2
    show old_debbie 61
    player_name "Nah, just looking around for something to do..."

    show player 14
    player_name "Why, what are you up to?"

    show player 1
    show old_debbie 62
    debbie "I was just thinking about starting a movie."

    show player 2
    show old_debbie 61
    player_name "Dingin."

    show player 1
    debbie "..."
    show old_debbie 63
    debbie "Why don't you come join me?"

    show player 10
    show old_debbie 61
    player_name "Benar-benar?"

    show player 11
    show old_debbie 62
    debbie "Sure, why not? It's still early and I would love the company!"

    show player 2
    show old_debbie 61
    player_name "Y-yeah, okay. That sounds nice, {b}[deb_name]{/b}."

    show player 1
    show old_debbie 62
    debbie "Besar!"

    debbie "I'll go get situated and you just come join me when you're ready, alright?"

    show player 2
    show old_debbie 61
    player_name "Sounds good!"

    hide old_debbie
    hide player
    with dissolve
    return

label entrance_mom_hang_out:
    scene expression L_home_entrance.background_blur
    show player 1 at left with dissolve
    show old_debbie 165 at right with dissolve
    debbie "Hey there, sweetheart!"

    show player 2
    show old_debbie 164
    player_name "Hey {b}[deb_name]{/b}!"

    player_name "You look nice! Going somewhere?"

    show player 1
    show old_debbie 165
    debbie "Oh, I just need to run to the mall and pick up a few things."

    show old_debbie 164
    debbie "..."
    show old_debbie 165
    debbie "Would you like to join me?"

    show player 11
    show old_debbie 164
    player_name "Hmm?"

    show player 10
    player_name "Oh I dunno, I was gonna-"

    show player 11
    show old_debbie 165
    debbie "Aww, c'mon! It'll do you good to get some fresh air."

    show old_debbie 164
    player_name "..."
    show old_debbie 165
    debbie "... And besides, I don't want to go all by myself..."

    debbie "Won't you come and keep me company?"

    show old_debbie 164
    return

label entrance_mom_hang_out_yes:
    show player 2
    player_name "Heh, sheesh {b}[deb_name]{/b}! Alright, I'll go."

    show player 1
    show old_debbie 166
    debbie "Besar!"

    show old_debbie 165
    debbie "I'll meet you in the car then, sweetie!"

    return

label entrance_mom_hang_out_no:
    show player 10
    player_name "Sorry {b}[deb_name]{/b}, I have something else planned for today..."

    show player 11
    show old_debbie 168
    debbie "Oh."

    show old_debbie 169
    debbie "..."
    show old_debbie 168
    debbie "Okay, sweetie, well... Just stay safe and be home for dinner."

    show player 2
    show old_debbie 169
    player_name "Tentu saja."

    return

label entrance_mom_spy:
    scene expression L_home_entrance.background_blur
    show player 10 with dissolve
    player_name "Hah?"

    player_name "What was that noise?"

    show player 11
    pause
    show player 10
    player_name "Maybe the TV is on in the living room."

    hide player with dissolve
    return

label entrance_mom_kissing_practice:
    scene expression L_home_entrance.background_blur
    show player 4 with dissolve
    player_name "I wonder if {b}[deb_name]{/b} would let me kiss her again if I asked?"

    player_name "I should {b}talk to her{/b} about it..."

    hide player with dissolve
    return

label entrance_mom_car_broken:
    scene expression player.location.background_blur
    show debbie
    show anon f_tired with dissolve
    debbie "Good morning, sweetie."

    anon @ f_yawn a_yawn -m_talk "{i}*Menguap*{/i}"

    anon "Morning, {b}[deb_name]{/b}."

    debbie f_sad "Oh my, you look exhausted!"

    anon "Ya maaf."

    anon "I haven't been getting much sleep recently."

    debbie "Oh?"

    debbie "Apa yang terjadi?"

    anon "I dunno, I keep having these weird dreams..."

    debbie "What kind of weird dreams?"

    anon f_worried "Ehh, I'd rather not get into it..."

    anon "It's kinda embarrassing."

    debbie f_curious "... Naughty dreams?"

    anon f_shy @ a_behind_head "Y-ya."

    debbie f_normal "Well, that's nothing to be embarrassed about, sweetheart!"

    debbie "It's perfectly normal for boys your age."

    pause
    debbie "So, who's the lucky girl?"

    anon f_worried "Ehh..."

    debbie "Is it someone I know?"

    anon "Y-yeah, you know her..."

    debbie "Oh, I bet it's that cute little neighbor girl... What's her name?"

    anon "{b}Mia{/b}."

    debbie @ f_laugh "Itu dia!"

    debbie "Oh, I think she's just the most adorable thing..."

    anon "Can we change the subject?"

    debbie @ f_eyeroll "Oh, fine. Keep your secrets!"

    debbie "I need your help with something anyways..."

    anon f_normal "Ya tentu saja."

    anon "Anything."

    debbie "I can't seem to get the car started..."

    anon f_confused "Didn't we just take it out the other day?"

    debbie "Yeah, but for some reason it's not working now."

    anon f_worried "You didn't leave the lights on and kill the battery again, did you?"

    debbie f_curious "Hah, no... I mean, well... I don't think I did."

    debbie f_normal "Would you mind taking a look at it?"

    anon f_normal "Not at all!"

    hide anon
    show debbie b_robe_hug1
    with dissolve
    debbie "Terima kasih sayang."

    show debbie b_robe_hug2
    anon "T-tidak masalah."

    hide debbie with dissolve
    return

label entrance_mom_panties_masturbation_again:
    scene expression L_home_entrance.background_blur
    show player 1
    player_name "( I can't believe {b}[deb_name]{/b} actually rubbed my cock! )"

    player_name "( ... A couple more seconds and I would have popped. )"

    player_name "( Arrgh, I want her so bad! This is torture! )"

    show player 11
    player_name "( ... )"
    player_name "( Hmm, I know I promised not to jerk off in her room but... )"

    show player 13
    player_name "( It just felt so good last time! )"

    player_name "( ... )"
    player_name "( Maybe if I do it quickly and quietly, {b}I can snag a pair of her panties{/b} and bust a nut without her noticing. )"

    player_name "( She seems to be busy in the [temp] which should allow me to sneak into her room and rub one out in her bed. )"

    player_name "( I think it's worth a shot... I need the release... To clear my head! )"

    hide player with dissolve
    return

label entrance_mom_diane_visit:
    scene expression L_home_entrance.background_blur
    show player 34 with dissolve
    player_name "{i}*Distant voice*{/i}"

    show player 35
    player_name "( Hmm, sounds like {b}[deb_name]{/b} is talking to someone in the kitchen... )"

    show player 12
    player_name "( I wonder who's here? )"

    show player 10
    player_name "( I should go take a look... )"

    hide player with dissolve
    return

label entrance_mom_vacuum:
    scene location_home_entrance_fight
    show old_debbie 94 at right with dissolve
    pause
    show old_debbie 95
    pause
    show old_debbie 94
    pause
    show old_debbie 95
    pause
    show old_debbie 94
    show player 1 at left with dissolve
    pause
    show old_debbie 95
    pause
    show old_debbie 97 with dissolve
    debbie "Oh!!"

    debbie "You startled me..."

    show old_debbie 98
    show player 17
    player_name "Maaf, {b}[deb_name]{/b}."

    show player 14
    player_name "I didn't mean to!"

    show old_debbie 97
    show player 1
    debbie "Sorry about the noise."

    debbie "I should be done with the vacuum soon."

    debbie "... Ugh, this is killing my back!"

    show old_debbie 98
    return

label entrance_mom_vacuum_yes:
    show old_debbie 98 at right
    show player 14 at left
    player_name "Here, {b}[deb_name]{/b}, pass me the vacuum."

    show player 1
    show old_debbie 96
    debbie "..."
    show old_debbie 97
    debbie "You want the vacuum?"

    show old_debbie 96
    show player 14
    player_name "Yeah, I'll take over from here."

    player_name "You should rest your back for a bit..."

    show player 10
    player_name "No sense in working yourself so hard when I'm here to help."

    show old_debbie 97
    show player 11
    debbie "No, it's okay, sweetie. You don't have-"

    show old_debbie 98
    show player 10
    player_name "I know I don't have to help, {b}[deb_name]{/b}."

    player_name "I want to do it."

    show old_debbie 97
    show player 1
    debbie "Well, if you insist..."

    show player 257
    show old_debbie 100
    with dissolve
    debbie "This is very sweet of you."

    show player 259
    show old_debbie 99
    player_name "Tidak masalah!"


    scene location_home_cutscene02
    show text _ ("I felt bad {b}[deb_name]{/b} was having a hard time with her back pain.\nThe least I could do was help her out, even if it took me forever to finish.\nThe stairs were the worst part! No wonder her back is hurting her...\nAt least {b}[deb_name]{/b} kept me company while I worked.") as caption
    with fade
    pause

    scene black with dissolve
    return

label entrance_mom_vacuum_no:
    show old_debbie 96 at right
    show player 10 at left
    player_name "Can you please finish cleaning another time?"

    player_name "I'm trying to study upstairs and all this noise is distracting."

    show old_debbie 97
    show player 11
    debbie "I'm sorry, sweetie!"

    debbie "I had no idea you were upstairs studying."

    show old_debbie 96
    show player 14
    player_name "Tidak apa-apa, {b}[deb_name]{/b}."

    show old_debbie 97
    show player 1
    debbie "It'll be good to rest my back for a bit anyways..."

    show old_debbie 96
    show player 17
    player_name "Terima kasih!"

    hide player
    hide old_debbie
    with dissolve
    return

label entrance_sis_couch_1:
    scene expression L_home_entrance.background_blur
    show anon f_surprised with dissolve
    anon @ -m_talk "( What's that sound? )"

    anon @ -m_talk "( It sounds like the TV is on. )"

    anon f_thinking a_thinking @ -m_talk "( Who could be watching TV this late? )"

    hide anon with dissolve
    return

label entrance_sis_couch_2:
    scene expression L_home_entrance.background_blur
    show anon f_flirt with dissolve
    anon @ -m_talk "( That porno {b}[jen_name]{/b} was watching was hot! I kind of feel like watching it, too... )"

    anon a_thinking f_thinking "Hmm... Maybe {b}another night{/b}."

    hide anon with dissolve
    return

label entrance_sis_couch_3:
    scene expression L_home_entrance.background_blur
    show anon f_surprised with dissolve
    anon @ -m_talk "( What was that sound? )"

    hide anon with dissolve
    return

label entrance_bissette_roxxy_jenny_mentoring:
    scene expression L_home_entrance.background_blur
    show player 13 at Position (xpos=300)
    show old_debbie 2 at right
    with dissolve
    debbie "Sweetie, somebody is at the door! Can you get it?"

    show old_debbie 1
    show player 14
    player_name "Sure thing, {b}[deb_name]{/b}!"

    show player 10
    show old_roxxy 1 at Position (xpos=600) with dissolve
    player_name "Hey {b}Roxxy{/b}! You here for your session with {b}[jen_name]{/b}?"

    show player 5
    show old_roxxy 2
    roxxy "Duh. What, do you think I'm here to see you or something?!"

    show old_roxxy 1
    show player 21
    player_name "... Tidak."

    show player 5
    show old_roxxy 2
    roxxy "Good, 'cause there is no fucking way-"

    show old_roxxy 1 with None
    show jenny f_grin a_crossed:
        flip
        xoffset -120
    with dissolve
    jenny "{i}*Ehem*{/i}"

    jenny "Is this that girl you wanted me to help?"

    jenny "You know, the one you're trying to bang?"

    hide xtra
    show player 11
    with dissolve
    show old_debbie 14
    player_name "!!!" with hpunch
    show old_roxxy 3
    roxxy "PERmisi?!"

    show old_roxxy 14
    show player 113
    player_name "N-no!!"

    show player 10
    player_name "{b}Roxxy{/b}, I swear I never said-"

    show player 11
    show old_roxxy 2
    roxxy "As if you even have a shot... Not even in your dreams, twerp!"

    show old_roxxy 1
    show player 37 at Position (xoffset=41) with dissolve
    show jenny f_grin
    jenny "Aww, too bad little pervert."

    jenny "I guess you're stuck with your hand and a bottle of lotion."

    show old_roxxy 4
    roxxy "Hah! Yeah, and I feel sorry for the lotion..."

    show old_roxxy 1
    show jenny f_laugh a_hips with dissolve
    jenny "Hahaha! Oh, I like you! {b}Roxxy{/b}, was it?"

    show jenny f_grin
    show old_roxxy 1b
    roxxy "Yeah, and you're {b}[jen_name]{/b}?"

    show old_roxxy 1
    jenny "Itu benar."

    jenny "C'mon, {b}Roxxy{/b}. We can ditch the dweeb and get started in my room."

    show old_roxxy 1b
    roxxy "Dengan senang hati."

    show old_roxxy 2
    roxxy "See ya, dweeb!"

    hide old_roxxy
    hide jenny
    show player 25
    with dissolve
    player_name "..."
    show player 24
    player_name "I have a bad feeling about this."

    hide player
    hide old_debbie
    with dissolve

    scene location_home_entrance_cutscene04
    show text _ ("Those two had formed a connection almost instantly...\nI guess {b}[jen_name]{/b} and {b}Roxxy{/b} did have a lot in common.") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("They were both captains of the cheer squad, popular, beautiful,\nand both of them had mastered the art of being a bitch...") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("I really hope I don't end up regretting this...") as caption with dissolve
    pause

    scene expression L_home_entrance.background_blur
    show player 24 at Position (xpos=300)
    show old_debbie 13 at right
    with fade
    debbie "Who was that?"

    show old_debbie 14
    show player 10
    player_name "Just a girl from my school. {b}[jen_name]{/b} agreed to help her with some cheerleading stuff."

    show player 5
    show old_debbie 13
    debbie "{b}[jen_name]{/b} is helping somebody?"

    show old_debbie 3
    debbie "That's a new one."

    show old_debbie 1
    show player 12
    player_name "Yeah, because I paid her..."

    show player 90
    show old_debbie 13
    debbie "Ah."

    debbie "Sweetie, you really shouldn't let {b}[jen_name]{/b} take advantage of you like that..."

    show old_debbie 14
    show player 12
    player_name "Ya, saya tahu."

    show player 90
    player_name "..."
    show old_debbie 13
    debbie "Something else on your mind?"

    show old_debbie 14
    show player 12
    player_name "I've just never seen {b}[jen_name]{/b} hit it off with someone like that..."

    show player 10
    player_name "Kinda freaks me out, to be honest."

    show player 5
    show old_debbie 2
    debbie "Well, I think it's a good thing she's made a new friend."

    debbie "I worry about her sitting upstairs by herself all day..."

    show old_debbie 13
    debbie "I'm sure she gets lonely."

    show old_debbie 14
    show player 10
    player_name "Saya meragukannya."

    show player 5
    player_name "..."
    show player 11
    jenny "Ha ha ha ha!!"

    show player 10
    player_name "... Maybe I should go {b}check on them{/b}?"

    show player 5
    show old_debbie 2
    debbie "Mungkin."

    show old_debbie 13
    debbie "... Just be careful, sweetie."

    hide player
    hide old_debbie
    with dissolve

    $ player.go_to(L_home_hallway)
    scene expression player.location.background_blur with fade
    show anon f_worried with dissolve
    anon @ -m_talk "( They really didn't waste any time, I can hear them in {b}[jen_name]{/b}'s room. )"

    hide anon with dissolve
    return

label entrance_bissette_roxxy_jenny_mentoring_sex:
    scene expression L_home_entrance.background_blur
    show player 13 at Position (xpos=300)
    show old_debbie 2 at right
    with dissolve
    debbie "Sweetie, somebody is at the door! Can you get it?"

    show old_debbie 1
    show player 14
    player_name "Sure thing, {b}[deb_name]{/b}!"

    show player 10
    show old_roxxy 1 at Position (xpos=600) with dissolve
    player_name "Hey {b}Roxxy{/b}! You here for your session with {b}[jen_name]{/b}?"

    show player 5
    show old_roxxy 2
    roxxy "Yup. It's still on, right?"

    show old_roxxy 1
    show player 21
    player_name "Sangat."

    show player 5
    show old_roxxy 2
    roxxy "Awesome! I'm so excited to-"

    show old_roxxy 1 with None
    show jenny f_grin a_crossed:
        flip
        xoffset -120
    with dissolve
    jenny "{i}*Ehem*{/i}"

    jenny "Is this that girl you wanted me to help?"

    jenny "You know, the one you're trying to bang?"

    hide xtra
    show player 11
    with dissolve
    show old_debbie 14
    player_name "!!!" with hpunch
    show old_roxxy 4
    roxxy "... Hahaha!"

    show old_roxxy 14
    show player 113
    player_name "aku tidak-"

    show player 10
    player_name "{b}Roxxy{/b}, I swear I never said-"

    show player 11
    show old_roxxy 1h
    roxxy "What exactly have you been telling them, {b}[firstname]{/b}?"

    show old_roxxy 1
    show player 37 at Position (xoffset=41) with dissolve
    show jenny f_surprised
    jenny "Tunggu sebentar..."

    jenny "You mean, you... A-and him?!"

    show jenny f_sad
    show old_roxxy 4
    roxxy "Uhh, yeah?!"

    roxxy "So long as he keeps taking good care of me..."

    show jenny f_grin
    roxxy "... And doesn't get fat or lose his hair, yuck!"

    show old_roxxy 1
    show jenny f_laugh
    jenny "Hahaha! Oh, I like you! {b}Roxxy{/b}, was it?"

    show jenny f_grin
    show old_roxxy 1b
    roxxy "Yeah, and you're {b}[jen_name]{/b}?"

    show old_roxxy 1
    jenny "Itu benar."

    jenny "C'mon, {b}Roxxy{/b}. We'll do this in my room."

    show old_roxxy 1b
    roxxy "Baiklah."

    show old_roxxy 2
    roxxy "Thanks again, {b}[firstname]{/b}."

    hide old_roxxy
    hide jenny
    show player 25
    with dissolve
    player_name "..."
    show player 24
    player_name "I have a bad feeling about this."

    hide player
    hide old_debbie
    with dissolve

    scene location_home_entrance_cutscene04
    show text _ ("Those two had formed a connection almost instantly...\nI guess {b}[jen_name]{/b} and {b}Roxxy{/b} did have a lot in common.") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("They were both captains of the cheer squad, popular, beautiful,\nand both of them had mastered the art of being a bitch...") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("I really hope I don't end up regretting this...") as caption with dissolve
    pause

    scene expression L_home_entrance.background_blur
    show player 24 at Position (xpos=300)
    show old_debbie 13 at right
    with dissolve
    debbie "So you two are dating now?"

    show old_debbie 14
    show player 10
    player_name "Heh, yeah. {b}[jen_name]{/b} agreed to help her with some cheerleading stuff."

    show player 5
    show old_debbie 13
    debbie "{b}[jen_name]{/b} is helping somebody?"

    show old_debbie 3
    debbie "That's a new one."

    show old_debbie 1
    show player 12
    player_name "Yeah, because I paid her..."

    show player 90
    show old_debbie 13
    debbie "Ah."

    debbie "Sweetie, you really shouldn't let {b}[jen_name]{/b} take advantage of you like that..."

    show old_debbie 14
    show player 12
    player_name "Ya, saya tahu."

    show player 90
    player_name "..."
    show old_debbie 13
    debbie "Something else on your mind?"

    show old_debbie 14
    show player 12
    player_name "I've just never seen {b}[jen_name]{/b} hit it off with someone like that..."

    show player 10
    player_name "Kinda freaks me out, to be honest."

    show player 5
    show old_debbie 2
    debbie "Well, I think it's a good thing she's made a new friend."

    debbie "I worry about her sitting upstairs by herself all day..."

    show old_debbie 13
    debbie "I'm sure she gets lonely."

    show old_debbie 14
    show player 10
    player_name "Saya meragukannya."

    show player 5
    player_name "..."
    show player 11
    jenny "Ha ha ha ha!!"

    show player 10
    player_name "... Maybe I should go {b}check on them{/b}?"

    show player 5
    show old_debbie 2
    debbie "Mungkin."

    show old_debbie 13
    debbie "... Just be careful, sweetie."

    hide player
    hide old_debbie
    with dissolve

    $ player.go_to(L_home_hallway)
    scene expression player.location.background_blur with fade
    show anon f_worried with dissolve
    anon @ -m_talk "( They really didn't waste any time, I can hear them in {b}[jen_name]{/b}'s room. )"

    hide anon with dissolve
    return

label entrance_bissette_roxxy_jenny_spying:
    scene expression L_home_entrance.background_blur
    show anon f_worried with dissolve
    anon "I should go check on {b}Roxxy{/b} and {b}[jen_name]{/b}..."

    hide anon with dissolve
    return

label entrance_diane_debbie_evening_visit_overhear:
    scene expression L_home_entrance.background_blur
    show player 34 with dissolve
    player_name "(Hmm?)"

    player_name "( Is that {b}Diane{/b}? )"

    player_name "( {b}[deb_name]{/b} must have invited her over. )"

    player_name "( {b}I wonder what they're talking about{/b}? )"

    hide player with dissolve
    return

label entrance_diane_checkup_results:
    scene expression background(l=L_home_entrance, t=3)
    show player 13 at left
    show diane b_casual
    with dissolve
    diane "Thanks for going with me, {b}[firstname]{/b}."

    diane "You were so great today!"

    show player 14
    player_name "Tidak masalah."

    player_name "I'm just glad we got good news."

    show player 13
    diane "Saya juga."

    hide player
    show diane b_kiss_casual
    with dissolve
    pause
    show player 13 at left
    show diane b_casual
    with dissolve
    diane "We'll get started tomorrow, okay?"

    show player 14
    player_name "Baiklah."

    show player 13
    diane "You'd better head up to bed and get a good nights sleep."

    show diane f_wink
    pause
    show diane f_smirk
    diane "Lots of hard work waiting for you tomorrow, stud."

    show player 29 with dissolve
    player_name "{i}*Gulp*{/i} Y-ya, oke."

    hide player
    hide diane
    with dissolve
    return

label ano01_cops_home_entrance:
    scene expression player.location.background_blur
    show anon with dissolve
    debbie "Can I get you a cup of coffee, officer?"

    show anon f_surprised
    harold "Oh, you can call me {b}Harold{/b}, ma'am."

    harold "Coffee would be lovely."

    debbie "Tentu."

    anon @ -m_talk "( It's a police officer. )"

    show anon f_worried
    harold "I thought you might like an update on your friend's case."

    anon f_shock "!!!"
    debbie "{i}*Gasp*{/i} You have news?"

    anon "( He's here about {b}Dad{/b}! )"


    $ player.go_to(L_home_kitchen)
    scene expression player.location.background_blur
    show harold f_worried:
        flip
    show debbie f_sad
    with fade
    harold "Ehh, not as much as I'd hoped."

    show debbie a_mug_give with dissolve
    pause
    show debbie a_front
    show harold a_mug
    with dissolve
    harold f_normal "Thank you for this."

    show harold f_normal_closed a_mug_drink m_talk with dissolve
    pause
    harold f_normal a_mug -m_talk "Mm, that's nice!"

    debbie "What have you found out?"

    harold f_worried "Benar."

    harold "Well, the autopsy report confirms that he died from asphyxiation..."

    harold "... And that coupled with the excessive bruising around his throat means suicide is the most likely scenario."

    debbie "{i}*Sigh*{/i} It just doesn't make any sense."

    debbie "{b}Frank{/b} would never have killed himself."

    harold "Hmm, I can't really speak to that, ma'am."

    harold "But it seems like your friend was keeping quite a lot from you."

    debbie "Apa maksudmu?"

    harold "You said he was working as an accountant, correct?"

    debbie "Ya."

    harold "And he was employed at {b}Saga Financial Bank{/b}?"

    debbie "That's right, for fifteen years."

    harold "Well, I spoke with the bank manager there, and she told me that your friend was fired eighteen months ago."

    debbie @ f_surprised_worried "APA?!"

    debbie "No, no, that can't be right..."

    harold "The paperwork cited a declining work performance and multiple incidents involving shady characters."

    debbie "But that doesn't-"

    debbie a_facepalm f_crying_closed "{i}*Sniff*{/i} How could he keep this from me?!"

    pause
    debbie "W-what was he doing for work all this time?"

    harold "{i}*Sigh*{/i} Well, I'm afraid we haven't figured that part out yet."

    debbie @ -m_talk "..."
    harold "We do have evidence linking him to several high-value accounts, and eyewitness statements claim he was moving a lot of money around."

    debbie f_sad a_front "Witness statements?"

    harold "Yes, apparently he was quite friendly with a teller by the name of... {b}Liu Kim{/b}."

    debbie "I'm not familiar with her..."

    harold "She said he had recently started working for a new client and that their accounts were all valued at well over seven figures."

    debbie @ f_surprised_worried -m_talk "!!!"
    harold "Unfortunately, that money vanished not long after your friend's death."

    harold "From what we can tell, it was moved electronically into offshore accounts. But so far, we've been unable to trace it."

    harold "At this time, we don't have a clue where it came from or who else might have been involved."

    debbie a_facepalm f_crying_closed @ -m_talk "..."
    harold "It's my opinion that your friend got mixed up with some sort of criminal element and was most likely helping them to launder money."

    debbie "This can't be happening..."

    pause
    harold "It would also explain the threats you've been receiving."

    debbie @ -m_talk "..."
    harold "You said they're demanding money?"

    debbie a_front f_sad "{i}*Mengendus*{/i} Y-ya."

    harold "I pulled your phone records from the past couple days and it seems the calls are coming from an overseas number."

    debbie "How is that possible?"

    harold "I don't know, ma'am."

    harold "{i}*Sigh*{/i} There's really not much I can do to help you at this point..."

    debbie "B-but, what am I supposed to do?!"

    harold "I'm terribly sorry, ma'am."


    $ player.go_to(L_home_entrance)
    scene expression L_home_entrance.background_blur
    show anon f_shock:
        xoffset 500
    with fade
    anon "( ... Eighteen months?! )"

    anon "( That doesn't make any sense! )"

    anon "( My dad would never work for a bunch of criminals... Would he? )"

    anon a_thinking f_thinking @ -m_talk "( Was he just lying to us the whole time? )"

    pause
    show yumi with dissolve:
        flip
    anon @ -m_talk "( It's just so hard to believe, he- )"

    yumi "Permisi?"

    show anon f_surprised_teeth a_surprised_up_both:
        flip
        xoffset 0
    anon "!!!" with hpunch
    anon f_skeptical a_idle "Holy crap lady, you scared the bejesus out of me!"

    yumi @ f_laugh "Hehe, sorry about that."

    yumi "I'm looking for my partner, {b}Harold{/b}."

    anon f_worried "Y-yeah, he's in there."

    yumi "Terima kasih."

    hide yumi with dissolve
    anon f_sad_down @ -m_talk "..."

    $ player.go_to(L_home_kitchen)
    scene expression player.location.background_blur
    show debbie f_crying_closed a_facepalm zorder 2:
        xoffset -115
    show harold f_worried zorder 2:
        flip
        xoffset 100
    with fade
    harold "I'm sure there's something we're overlooking."

    harold "I just need a little more time-"

    show yumi f_concerned zorder 1 with dissolve:
        flip
        xoffset -100
    yumi "Permisi, Pak?"

    show debbie a_front f_sad
    show anon f_worried zorder 1:
        flip
        xoffset 175
    show harold:
        unflip
        xoffset -400
    with dissolve
    harold "What is it, {b}Yumi{/b}?"

    show yumi a_point_back
    show anon b_empty zorder 3
    show debbie b_robe_mc_touch a_idle:
        xoffset 79
    with dissolve
    yumi "We just got a call on a possible 10-62."

    show yumi a_idle with dissolve
    harold "The bedtime bandit again?"

    yumi "Most likely."

    harold @ f_normal_closed a_facepalm "{i}*Sigh*{/i} I'll be right there."

    hide yumi with dissolve
    harold "The fun never stops..."

    show harold with dissolve:
        flip
        xoffset 100
    harold "I'm afraid we're going to have to cut this short."

    harold "Hey there, kiddo."

    anon "Halo."

    show debbie a_touch with dissolve
    pause
    harold a_card "If you think of anything else that might help in our investigation, or the threats escalate into something worse, don't hesitate to call me..."

    show harold a_card_give with dissolve
    debbie "{i}*Sniff*{/i} Yeah, okay."

    harold a_idle "I'll have my partner {b}Yumi{/b} drop in on you from time to time..."

    harold "... Just to check that your family is safe."

    debbie "Terima kasih."

    harold "We're gonna sort this whole thing out, ma'am."

    harold "You have my word."

    debbie "..."
    harold "Son, you take good care of your landlady now, alright?"

    anon "Y-ya, tuan."

    harold "I'll be in touch."

    hide harold with dissolve
    pause
    anon "{b}[deb_name]{/b}?"

    show anon b_dressed:
        xoffset 0
    show debbie b_robe f_sad a_front:
        flip
        xoffset 200
    with dissolve
    debbie "{i}*Sniff*{/i} How much of that did you overhear?"

    anon "saya..."

    show anon f_sad_down
    pause
    anon "Entahlah."

    anon "Enough to be worried."

    pause
    anon f_worried "What are we going to do?"

    debbie "Sweetie, this isn't something you need concern yourself with..."

    debbie "That's my job."

    anon "Y-ya, tapi-"

    debbie "I'll handle it."

    anon "{b}[deb_name]{/b}, you don't have to do this alone..."

    debbie "I want you to focus on school."

    debbie "That's the most important thing for you right now."

    anon @ -m_talk "..."
    debbie "It's what your father would want."

    anon "{i}*Sigh*{/i} Dad doesn't want anything anymore..."

    debbie "{b}[firstname]{/b}, don't say things like that!"

    anon "Maaf, {b}[deb_name]{/b}."

    show anon b_empty f_sad_down
    show debbie b_robe_hug_mc:
        xoffset 0
    with dissolve
    debbie "{i}*Sniff*{/i} Everything is going to be alright."

    debbie "Saya berjanji."

    anon @ -m_talk "..."
    show anon b_dressed f_worried
    show debbie b_robe:
        xoffset 200
    with dissolve
    debbie "Now go get ready for school."

    anon "Ya baiklah."

    hide anon with dissolve
    return

label home_roxxy_studying_at_mcs:
    scene expression L_home_entrance.background_blur
    show anon
    show old_roxxy 1f f at Position (xpos=400)
    show old_debbie 2 at right
    with dissolve
    debbie "Hey, sweetie!"

    debbie "How was sch-"

    show old_debbie 13
    debbie "... Oh."

    debbie "Who's this?"

    show old_debbie 14
    anon "{b}[deb_name]{/b}, this is {b}Roxxy{/b}."

    anon "I'm helping her study for French class."

    show old_debbie 3
    debbie "Well, that's nice!"

    show old_debbie 2
    debbie "I'm happy to meet you, {b}Roxxy{/b}."

    show old_debbie 1
    show old_roxxy 1bf
    roxxy "... Terima kasih."

    roxxy "Nice to meet you too."

    show old_roxxy 1f f
    show old_debbie 2
    debbie "I was just finishing up dinner."

    debbie "You want me to bring you kids up a couple plates?"

    show old_debbie 1
    anon "Yeah, that would be great!"

    show old_roxxy 1bf
    roxxy "Oh, I don't wanna impose..."

    show old_roxxy 1f f
    show old_debbie 3
    debbie "Psh, not at all, dear!"

    show old_debbie 2
    debbie "You kids get on up there and have fun!"

    debbie "I'll bring you dinner as soon as it's ready."

    show old_debbie 1
    anon "Terima kasih, {b}[deb_name]{/b}!"

    hide anon
    hide old_roxxy
    hide old_debbie
    with dissolve

    scene expression L_home_bedroom.background_blur
    show player 13 at left
    show old_roxxy 2 at right
    with dissolve
    roxxy "Your landlady is really nice."

    show old_roxxy 1
    show player 33
    player_name "Yeah, I'm pretty lucky."

    show player 13
    show old_roxxy 30
    roxxy "So, this is your room?"

    show old_roxxy 1
    show player 10
    player_name "Eh ya."

    show player 5
    show old_roxxy 2
    roxxy "Well, it's pretty dorky..."

    roxxy "... But I guess it's nice too."

    show old_roxxy 1
    show player 14
    player_name "Heh, was that a compliment?"

    show player 13
    show old_roxxy 2
    roxxy "No, don't be stupid."

    show old_roxxy 1
    show player 10
    player_name "Alright, sorry."

    player_name "You okay with studying here?"

    show player 5
    show old_roxxy 1b
    roxxy "The bed looks comfy."

    show old_roxxy 1
    show player 10
    player_name "You ehh... wanna study on my bed?"

    show player 11
    show old_roxxy 2
    roxxy "Tentu, kenapa tidak?"

    show old_roxxy 1
    show player 29 with dissolve
    player_name "Baik menurutku."

    hide player
    hide old_roxxy
    with dissolve
    scene expression "backgrounds/location_home_bedroom_bed_dialogue.jpg"
    show player bed 1 at right
    show old_roxxy 36b at left
    show old_roxxy_outfit at left
    with dissolve
    roxxy "Jadi..."

    show old_roxxy 35b
    roxxy "..."
    show old_roxxy 35e
    roxxy "You have girls up here often?"

    show old_roxxy 35d
    show player bed 3
    player_name "Hah?"

    player_name "N-no, not really."

    show player bed 2
    show old_roxxy 35e
    roxxy "Is this the first time you've ever had a girl on your bed?"

    show old_roxxy 35d
    player_name "..."
    show player bed 3
    player_name "Tidak?"

    show player bed 2
    show old_roxxy 35e
    roxxy "You're not a virgin, are you?"

    show old_roxxy 35d
    show player bed 6
    player_name "!!!" with hpunch
    show player bed 3
    player_name "Apa?!"

    player_name "That's not... I mean, I'm not really comfortable..."

    show player bed 2
    player_name "..."
    show player bed 5
    player_name "... Are you a virgin?"

    show player bed 4
    show old_roxxy 35c
    roxxy "Pfft!"

    show old_roxxy 37 at Position (xoffset=120, yoffset=-100)
    roxxy "Haha, as if I'd tell you!"

    roxxy "Relax, I'm just having a laugh."

    show old_roxxy 35e at left
    roxxy "Like I said, studying isn't really my strong suit."

    show old_roxxy 35d
    show player bed 5
    player_name "Oh, c'mon... You aren't even trying."

    player_name "I think you're smarter than you make yourself out to be, {b}Roxxy{/b}."

    show player bed 4
    show old_roxxy 38b
    roxxy "..."
    show old_roxxy 36 at Position (xoffset=120, yoffset=-100)
    roxxy "Cih, terserah."

    show old_roxxy 35b
    show player bed 5
    player_name "aku serius!"

    show player bed 4
    roxxy "..."
    show old_roxxy 35c
    roxxy "Have you ever had a girlfriend?"

    show old_roxxy 35b
    show player bed 6
    player_name "!!!" with hpunch
    player_name "..."
    show player bed 3
    player_name "Why would you ask me that?"

    show player bed 2
    show old_roxxy 37 at Position (xoffset=120, yoffset=-100)
    roxxy "Haha, boredom mostly..."

    show old_roxxy 35b
    show player bed 5
    player_name "Here look, I'll show you a trick to make this more interesting..."

    show player bed 4
    show old_roxxy 40 at Position (xoffset=120, yoffset=-100)
    roxxy "Pfft, ya benar."

    show old_roxxy 35b
    show player bed 5
    player_name "Just look!"


    scene location_home_bedroom_cutscene10
    show text _ ("I spent hours trying to coax {b}Roxxy{/b} into studying.\nShe mostly just watched me work and asked awkward questions about my experience with girls.\n... But eventually I managed to teach her what she needed to know.") as caption
    with fade
    pause

    scene expression L_home_entrance.background_blur
    show old_roxxy 1 at right
    show player 10 at left
    with fade
    player_name "So, I guess we might have to do this again sometime, huh?"

    show player 5
    show old_roxxy 2
    roxxy "Let's hope not!"

    show old_roxxy 1
    show player 12
    player_name "Oh, c'mon... It wasn't that bad!"

    show player 5
    roxxy "..."
    show old_roxxy 1b
    roxxy "No, it wasn't that bad."

    roxxy "Just..."

    show old_roxxy 1
    roxxy "..."
    show old_roxxy 1b
    roxxy "... Thanks... For being cool about... you know, everything."

    show old_roxxy 1
    show player 13
    player_name "..."
    roxxy "..."
    show old_roxxy 2
    roxxy "Kenapa kamu menatapku seperti itu?"

    show old_roxxy 1
    show player 29 with dissolve
    player_name "S-sorry... It's just... I'm not used to you, being nice, like this..."

    show player 3
    show old_roxxy 2
    roxxy "Well, don't get used to it!"

    roxxy "You're still a dork and I'm gonna treat you like one at school!"

    show old_roxxy 28 with dissolve
    roxxy "... But..."

    show old_roxxy 27
    roxxy "..."
    hide player
    show old_roxxy 59 at left with dissolve
    player_name "!!!" with hpunch
    show player 11 at left
    show old_roxxy 1e at right
    with dissolve
    player_name "..."
    show player 10
    player_name "Untuk apa itu?"

    show player 11
    show old_roxxy 1b
    roxxy "Just a little show of gratitude."

    show player 13
    roxxy "Nothing more!"

    show old_roxxy 2
    roxxy "Don't go thinking it means anything!"

    show old_roxxy 1
    player_name "..."
    show player 29 with dissolve
    player_name "... Benar."

    player_name "I'll walk you home, then."

    show player 3
    show old_roxxy 1b
    roxxy "Nah, I'll be fine."

    roxxy "Later, nerd!"

    hide old_roxxy with dissolve
    pause
    show player 34 with dissolve
    player_name "..."
    show player 35
    player_name "Pigs must be flying somewhere."

    hide player with dissolve
    return

label home_front_roxxy_cookies_and_milk:
    scene expression L_home_entrance.background_blur
    show player 5 at Position (xpos=400)
    show old_roxxy 32f at left
    show old_debbie 13 at right
    with dissolve
    debbie "{b}[firstname]{/b}?"

    debbie "What on earth are you doing home so early?"

    show old_debbie 14
    show player 10
    player_name "Hey, {b}[deb_name]{/b}."

    player_name "My friend here is having a really rough day."

    show player 5
    show old_debbie 13
    debbie "Oh!"

    show old_debbie 2
    debbie "Hello again, dear..."

    show old_debbie 1
    show player 10
    player_name "I brought her here to talk things over."

    player_name "... And I offered her lunch."

    player_name "I hope that's okay?"

    show player 5
    show old_debbie 3
    debbie "Of course, it's okay!"

    show old_debbie 2
    debbie "... It's {b}Roxxy{/b}, isn't it?"

    show old_debbie 1
    show old_roxxy 33f
    roxxy "Ya, Bu."

    roxxy "Sorry to inconvenience you again..."

    show old_roxxy 32f
    show old_debbie 3
    debbie "It's no trouble at all, dear!"

    show old_debbie 2
    debbie "Why don't you two go on upstairs and I'll whip something up for you."

    show old_debbie 1
    show player 14
    player_name "Terima kasih, {b}[deb_name]{/b}."

    scene black with fade
    pause

    scene expression L_home_bedroom.background_blur
    show player 5 at left
    show old_roxxy 1l
    with dissolve
    roxxy "Does your landlady ever wear clothes?"

    show old_roxxy 1k
    show player 10
    player_name "Hah?"

    player_name "Apa maksudmu?"

    show player 5
    show old_roxxy 1i
    roxxy "..."
    show old_roxxy 1l
    roxxy "... Sudahlah."

    show old_roxxy 30 at Position (xoffset=-33) with dissolve
    roxxy "Ugh, this is such a disaster..."

    roxxy "What the hell am I gonna do!"

    show old_roxxy 29 at Position (xoffset=-33)
    show player 10
    player_name "Calm down, {b}Roxxy{/b}."

    player_name "There's no sense getting yourself all worked up before we have all the details."

    show player 5
    show old_roxxy 3c at Position (xoffset=-33)
    roxxy "Apa maksudmu?"

    show old_roxxy 3d at Position (xoffset=-33)
    show player 10
    player_name "All we know is that your mom was arrested for possession and that the police are investigating."

    player_name "There might still be a way to salvage the situation."

    show player 5
    show old_roxxy 1k with dissolve
    roxxy "..."
    show old_roxxy 1l
    roxxy "Menurutmu begitu?"

    show old_roxxy 1k
    show player 10
    player_name "... Mungkin."

    player_name "We should go down to the Police Station and find out exactly what's going on."

    show player 5
    show old_roxxy 27
    roxxy "..."
    show old_roxxy 1l
    roxxy "Anda benar..."

    show old_roxxy 1k
    roxxy "..."
    show player 10
    player_name "For now, just breathe and relax."

    player_name "I'm sure we can find a way to fix this."

    show player 5
    show old_roxxy 1l
    roxxy "... Why are you being so nice to me?"

    show old_roxxy 1k
    show player 10
    player_name "Hah?"

    player_name "saya..."

    show player 5
    show old_debbie 218 at right with dissolve
    debbie "I brought snacks!"

    show old_roxxy 1kf at Position (xpos=400) with dissolve
    show player 13
    show old_debbie 217
    debbie "Some fresh milk and oven baked cookies..."

    debbie "It's the perfect thing to get you feeling better after a rough day, {b}Roxxy{/b}!"

    show old_debbie 219 with dissolve
    show old_roxxy 27f at Position (xoffset=33)
    show player 428
    pause
    show old_roxxy 1bf with dissolve
    roxxy "{i}*Sniff*{/i} Oh, wow!"

    show old_debbie 1 with dissolve
    show player 11
    roxxy "Those looks wonderful, ma'am!"

    show old_roxxy 1f f
    show old_debbie 3
    debbie "Aww, well, thank you, dear."

    show old_roxxy 32f at Position (xoffset=-34)
    show player 13
    with dissolve
    debbie "The recipe has been in my family for generations!"

    show old_debbie 14b
    show old_roxxy 27f at Position (xoffset=33)
    debbie "..."
    show old_debbie 13
    debbie "Your mascara is running, dear..."

    show player 5
    show old_debbie 14b
    show old_roxxy 33f at Position (xoffset=-34)
    roxxy "{i}*Sniff*{/i} Oh, sorry..."

    show old_roxxy 33bf with dissolve
    pause
    show old_debbie 13
    debbie "There's nothing to be sorry for!"

    show old_roxxy 32f at Position (xoffset=-34)
    debbie "You guys just eat up and let me know if there's anything else I can do for you."

    debbie "I just hate seeing a pretty thing like you all upset..."

    show old_debbie 14
    show player 13
    show old_roxxy 33f at Position (xoffset=-34)
    roxxy "... Thanks, ma'am."

    show old_roxxy 32f at Position (xoffset=-34)
    show old_debbie 2
    debbie "Please, call me {b}[deb_name]{/b}, dear."

    hide old_debbie with dissolve
    roxxy "..."
    show old_roxxy 33 at center with dissolve
    roxxy "Thanks, for all this {b}[firstname]{/b}..."

    show old_roxxy 32
    show player 14
    player_name "Anytime!"

    show player 13
    show old_roxxy 33b
    roxxy "{i}*Mengendus*{/i}"

    show old_roxxy 32
    show player 10
    player_name "Let's eat, and then we'll {b}head down to the police station{/b} and sort things out."

    show player 13
    show old_roxxy 33
    roxxy "... Yeah, okay."

    hide old_roxxy
    hide player
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
