label ano10_tina_tina_lounge:
    scene location_apt_hall3_301_closeup as stage
    show location_apt_hall3_301_closeup_door1 as door behind stage
    show anon a_pizza with dissolve:
        xoffset 100
    anon @ -m_talk "( Alright, I gotta admit... This pizza is starting to smell really good. )"

    show anon a_pizza_knock with dissolve
    "{i}*Ketuk* *Ketuk*{/i}"

    anon a_pizza @ -m_talk "( Hopefully this doesn't take long because I'm starving! )"

    pause
    anon f_skeptical @ -m_talk "(Hmm?)"

    anon @ a_pizza_knock "Hello?!"

    "{i}*Ketuk* *Ketuk*{/i}"

    anon a_pizza_knock "Is anybody hom-"

    show location_apt_hall3_301_closeup_door2 as door
    show anon f_shock
    with {'master': fastdissolve}
    anon "YA TUHAN!"


    scene tina b_doorway
    anon "!!!" with hpunch
    anon "{b}Tina{/b}?!"

    tina "Hey there, babyface..."

    anon "{i}*Gulp*{/i} D-did you order a pizza?"

    tina "I certainly did."

    tina "Pear and prosciutto, gorgonzola?"

    anon "Ya, Bu."

    tina "Extra sausage on the side?"

    anon "Sausage?"

    anon "{b}Tony{/b} didn't say anything about sausage..."

    tina @ f_laugh "Hehe, bukan?"

    tina @ f_happy "Well, that's a pity!"

    pause
    tina "Why don't you come inside and set it on the table while I get your tip?"

    anon "O-oke."


    scene expression background(600, 552, 1.75) as stage
    show tina b_lingerie a_wine
    with fade
    show anon a_pizza f_shy with dissolve:
        xoffset -50
    anon "Wow, this is a nice place!"

    tina "Menurutmu begitu?"

    anon "Tentu saja."

    tina "Back in Brooklyn, I became accustomed to a... Certain standard of living."

    tina @ f_sad "To be honest, it's quite a bit smaller than my last place."

    pause
    tina "But then again, everything is smaller out here in the sticks..."

    tina "... So, I suppose I shouldn't complain."

    show tina a_wine_drink f_kiss with dissolve
    anon "Oh, ehh... Okay."

    show tina a_wine f_normal with dissolve
    pause
    anon "Where did you want the pizza?"

    show tina with dissolve:
        flip
        xoffset 200
    tina "Right there on the coffee table will be fine."

    show anon f_shy_low with dissolve:
        xoffset 575
    tina @ f_laugh "It certainly smells delicious!"

    show anon a_idle f_shy behind tina with dissolve:
        flip
        xoffset 75
    anon "Yeah, I was thinking the exact same thing."

    anon f_disgusted "I've never heard of pear-prosciutto-gorgonzola pizza before..."

    tina @ f_laugh "Hehe, it was Luigi's favorite and now it's my daughter's as well."

    show anon f_shy
    pause
    tina "{b}Maria{/b} makes it better than anyone else..."

    tina @ f_normal_wink "... If you can twist her arm and convince her."

    anon @ f_skeptical "Is your daughter home?"

    tina "No, I'm afraid not."

    tina "She went over to her friend's house for the evening."

    tina "I'm not expecting her home for a few more hours..."

    anon "Jadi begitu."

    pause
    tina f_sexy "Whatever shall I do in the meantime, I wonder?"

    anon f_surprised @ -m_talk "..."
    tina "Would you like a glass of wine?"

    anon f_shy @ a_behind_head "Oh, heh... No thanks."

    anon "I'm not much of a wine drinker."

    tina @ f_sad "Tidak?"

    tina "Tsk, you don't know what you're missing out on."

    pause
    tina "I guess, I'll just have to drink it all myself..."

    show tina a_wine_drink f_kiss with dissolve
    pause
    anon f_surprised @ -m_talk "( !!! )"
    tina a_wine_empty f_sexy "Mmm, so good!"

    tina a_idle "So, what did {b}Tony{/b} tell you before sending you over?"

    anon f_shy "Umm, that the pizza was for a very important customer that had information about his contact."

    tina @ -m_talk "Mhmm."

    anon "And that I should follow their instructions and make sure their needs are satisfied."

    tina f_suspicious "He never mentioned that the customer was me?"

    anon "Tidak, Bu."

    tina f_sexy @ f_laugh "Hah, that old scoundrel!"

    pause
    tina "So you just agreed to follow some stranger's instructions?"

    anon @ f_laugh a_salute "Ya, Bu."

    tina "Eddie must really have something you need badly..."

    anon "He does."

    tina "Well, I think we can work something out, babyface."

    hide tina
    with {'master': dissolve}
    tina "Follow me."

    anon f_surprised @ -m_talk "..."
    hide anon with dissolve

    scene expression background(744, 420, 3.5) as stage
    show tina b_lingerie:
        xoffset -50
    with fade
    show anon with dissolve
    tina "My first instruction is for you to tell me what you think of my lingerie?"

    anon f_surprised_low "Y-your lingerie?"

    show tina b_lingerie_showoff with dissolve
    show anon f_surprised
    tina @ -m_talk "Mmhmm."

    pause
    show tina b_lingerie_back1_cloth with dissolve
    show anon f_surprised_low
    tina "Does blue suit me?"

    anon "Eh ya."

    show tina b_lingerie with dissolve
    show anon f_surprised
    tina "You know, I saw you staring at my tits the other day in the pizzeria..."

    anon f_worried "Oh, umm... I'm sorry about that."

    anon "I didn't mean to offend-"

    tina @ f_laugh "Hehe, it's okay."

    tina "I liked it!"

    anon f_surprised "Anda melakukannya?"

    tina @ -m_talk "Mmhmm."

    tina f_normal_down a_squeeze "I've had these things since I was fourteen."

    tina "And they have always attracted a lot of stares..."

    show anon f_flirt_low
    pause
    tina f_sexy "Would you like to see them?"

    show tina a_remove_cloth1 with dissolve
    anon f_surprised "Benar-benar?"

    show tina a_remove_cloth2 with dissolve
    pause
    show tina b_lingerie_back1 behind anon with dissolve
    tina "My next instruction is for you to come over here and pull this string..."

    anon f_surprised_low "{i}*Gulp*{/i} O-oke."

    show anon b_tina_lingerie1 f_flirt_low with dissolve:
        xoffset -50
    anon "This one?"

    tina "Mmhmm."

    show anon b_tina_lingerie2
    show tina b_lingerie_back2
    with dissolve
    pause
    show tina b_lingerie_back3
    show anon b_dressed behind tina:
        xoffset 90
    with dissolve
    tina "Sangat bagus."

    show tina b_lingerie_back_bend with dissolve
    pause
    show tina b_panties a_cover_panties behind anon with dissolve
    tina "Apakah kamu siap?"

    anon @ f_flirt "Y-ya."

    show tina b_panties_reveal1 with dissolve
    show tina b_panties_reveal2 with dissolve
    anon "!!!"
    anon "saya-"

    anon "Just, wow!"

    show anon o_boner with fastdissolve
    anon "Those are perfect!"

    tina "Perfect huh?"

    pause
    tina "Do you wanna touch them?"

    anon @ f_flirt "Can I?"

    tina "Ya."

    tina "In fact, that's my next instruction."

    anon "Ya, Bu!"

    show anon a_empty behind tina
    show tina b_panties_grope
    with dissolve
    pause
    anon "Wow."

    anon "They're massive!"

    tina "kamu suka?"

    anon "Oh, I definitely like."

    pause
    show tina f_sexy_down_lipbite
    pause
    tina f_sexy_down "Speaking of massive..."

    show anon a_up o_empty f_shy_down
    show tina b_panties_knees a_remove1:
        align (0, 0)
        xoffset 90
    with dissolve
    tina "I think I see that extra sausage I ordered."

    show anon b_shirt a_idle od_dick4
    show tina a_remove2
    with dissolve
    pause
    show tina a_up f_sexy_down_lipbite with dissolve
    pause
    show anon od_empty
    show tina a_jerk1 f_sexy_down
    with dissolve
    anon "!!!"
    tina "Mmm, I was wrong!"

    anon "Hah?"

    tina "Not everything is smaller in the sticks after all."

    show tina a_jerk with dissolve
    pause
    hide anon
    show tina b_panties_kiss:
        xoffset 0
    with dissolve
    tina @ -m_talk "MM."

    pause
    show anon b_shirt f_shy_down od_empty behind tina:
        xoffset 90
    show tina b_panties_knees a_jerk:
        xoffset 90
    with dissolve
    tina "I want you to fuck me."

    anon "K-kamu yakin?"

    tina "Ya!"

    pause
    show tina b_naked a_undress1:
        xoffset 50
    show anon f_flirt od_dick4
    with dissolve
    pause
    show anon b_naked_changing3 od_naked_dick3
    show tina b_naked_undress2 f_normal_down
    with dissolve
    pause
    show anon b_naked f_flirt
    show tina b_naked f_sexy a_idle
    with dissolve
    anon "Which way is your bedroom?"

    tina @ f_laugh "No time for that!"

    hide anon
    show tina b_naked_mc_throw_naked:
        flip
    with dissolve
    anon "Hah?!"

    hide tina with dissolve
    tina "hehe!"


    call scene_tina_sex_lounge
    $ unlock_scene('tina', '01_unlocked', variant='first')

    scene expression background(744, 420, 3.5) as stage
    show anon b_naked f_flirt od_naked_dick1
    show tina b_naked f_sexy
    with fade
    anon "Phew, that was incredible!"

    tina "Hehe, terima kasih."

    pause
    tina "You think you can go another round or two?"

    anon f_worried @ -m_talk "Hmm?"

    tina "You're supposed to make sure I'm completely satisfied, aren't you?"

    anon @ a_rub "Y-ya?"

    tina @ f_laugh "Well, then buckle up, babyface."

    tina "I've got three years of sexual frustration to work through!"

    hide anon
    show tina b_naked_mc_throw_naked:
        flip
    with dissolve
    anon "Wah!"

    hide tina with dissolve
    tina "hehe!"


    $ player.go_to(L_apt_hall3)
    scene location_apt_hall3_301_closeup as stage
    show location_apt_hall3_301_closeup_door2 as door behind stage
    show tina b_naked_disheveled f_sexy
    show location_apt_hall3_301_closeup as doorframe:
        crop (768, 0, 256, 768)
        right
    show anon f_flirt:
        xoffset 282
    with slowfade
    tina "Phew, now that was some A+ customer service!"

    tina "I'd say you more than earned that meeting with Eddie..."

    anon @ f_laugh "Senang mendengarnya."

    tina "I'll send {b}Tony{/b} all the info first thing tomorrow."

    anon "Thank you, {b}Tina{/b}."

    tina "Dengan senang hati."

    show anon b_empty
    show tina b_naked_disheveled_kiss
    with dissolve
    pause
    show anon b_dressed
    show tina b_naked_disheveled
    with dissolve
    tina "You know, we should do this again sometime..."

    anon "Ya?"

    tina "Why don't you just-"

    missy "{i}*Terkesiap*{/i}"

    becca "YA TUHAN!"

    show missy f_surprised behind anon:
        flip
        xoffset 75
    show becca f_surprised:
        flip
        xoffset -125
    show anon f_worried a_sides
    with dissolve
    show tina f_surprised
    becca "{b}MOM{/b}!!"

    show missy f_surprised_smile with None
    show anon f_surprised a_up o_kiss_tina behind missy:
        flip
        xoffset -275
    show tina a_cover f_sad
    with dissolve
    anon "{b}Mom{/b}?!"

    show anon f_worried a_idle with dissolve
    tina "{b}Rebecca{/b}?!"

    becca "WHAT THE-?!"

    show missy f_happy_back
    becca f_upset @ f_upset_yelling "WHERE ARE YOUR CLOTHES?!"

    show missy f_happy
    tina "Y-you're home early?"

    becca "YA!!"

    missy f_happy_back "Dude, I think {b}[firstname]{/b} is boning your mom..."

    becca "Shut the fuck up, {b}Missy{/b}!"

    show missy f_laugh a_shock with dissolve
    tina f_annoyed "{b}Becca{/b}, language!"

    becca a_crossed "Language?!"

    show missy f_happy a_idle with dissolve
    becca "Are you fucking serious right now?!"

    tina "Just calm down, please."

    becca "No, I'm not gonna calm down!"


    if M_roxxy.finished_state(S_roxxy_get_oil):
        anon @ f_shy "Uhh, this is just a misunderstanding..."

        missy @ f_laugh "{i}*Mendengus*{/i}"

        becca "{b}Mom{/b}, that's my-"

        becca f_surprised a_hip "I mean, that's {b}Roxxy{/b}'s boyfriend!"

        tina f_surprised "Hah?!"

        show missy f_angry with dissolve:
            unflip
            xoffset -525
        missy "Hey, he's my boyfriend too!"

        becca f_upset a_crossed @ f_eyeroll "Ugh, shut up {b}Missy{/b}!"

        tina f_suspicious "You mean, this is the one you girls won't stop talking about?"

        show missy f_happy with dissolve:
            flip
            xoffset 75
        becca @ f_upset_yelling "Ya!!!"

        pause
        tina f_annoyed "Well, I didn't know that!"

        becca "So what, you just fuck random guys when I'm not around?!"

        becca @ f_eyeroll "Thank god, {b}Dad{/b} isn't around to see this..."

    else:
        anon "Uhh, I should probably go..."

        missy @ f_laugh "{i}*Mendengus*{/i}"

        becca "{b}Mom{/b}, he's like, one of the nerdiest guys at my school!"

        tina "Jadi?"

        becca "So, you're disgusting!"


    missy f_surprised "Oh, shit... This just got real!"

    hide doorframe
    show anon -o_kiss_tina behind tina:
        unflip
        xoffset 175
    show tina a_hips:
        xoffset -160
    with dissolve
    tina a_hips "Hey, don't you talk to me like that!"

    tina "I'm your mother!"

    tina "And who I choose to sleep with is none of your business!"

    becca "Ya, tapi-"

    tina "I'm not arguing about this any further in the hallway."

    tina "Get inside and we'll discuss it like adults."

    becca @ -m_talk "..."
    tina @ a_point_back "NOW, {b}REBECCA{/b}!!"

    becca "Grr!!"

    hide becca
    show tina:
        flip
        xoffset 340
    with dissolve
    pause
    show tina behind stage:
        xoffset 515
    with dissolve
    tina "Your favorite pizza is on the table."

    missy @ f_laugh "Oh, pizza?"

    missy f_normal "Can I get in on that?"

    show tina with dissolve:
        unflip
        xoffset 0
    tina "Tidak."

    tina "Go home, {b}Missy{/b}."

    missy f_confused "Aww, man... Okay."

    show missy f_happy a_wave with dissolve:
        xoffset -50
    missy "Sampai jumpa, {b}[firstname]{/b}."

    show missy a_idle
    show anon f_skeptical o_kiss_tina:
        flip
        xoffset -325
    with dissolve
    anon @ -m_talk "..."
    hide missy with dissolve
    pause
    show tina f_sad
    show anon f_worried -o_kiss_tina with dissolve:
        unflip
        xoffset 175
    anon "I'm sorry, I had no idea {b}Becca{/b} was your daughter..."

    tina "No, it's not your fault."

    pause
    tina "Look, I gotta go and deal with this..."

    tina f_sexy "I'll see you around, yeah?"

    anon f_shy a_behind_head "Y-ya, tentu saja."

    tina "Later, babyface."

    anon "Sampai jumpa."

    hide tina
    show location_apt_hall3_301_closeup_door1 as door
    with dissolve
    pause
    anon f_worried a_idle @ -m_talk "( So {b}Becca{/b} is {b}Tina{/b}'s daughter? )"

    anon @ -m_talk "( This is a lot to process... )"

    pause
    anon @ -m_talk "( It kinda feels like I just wandered into a minefield! )"

    anon f_hurt @ -m_talk "( Man, she wasn't kidding about being sexually frustrated either! )"

    anon @ -m_talk "( I'm pretty sure I pulled a muscle in there. )"

    show anon f_tired
    pause
    anon @ -m_talk "( I should have listened to {b}Tony{/b} and picked up a sports drink... )"

    anon @ -m_talk "( Hydration is key. )"

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
