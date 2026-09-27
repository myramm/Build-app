label church_angelicas_room_mia_church_plan:
    scene expression player.location.background_blur
    show player 12 with dissolve
    player_name "( This looks like the right place. )"

    show player 30
    player_name "( There must be something I can wear in here... )"

    hide player with dissolve
    return

label church_angelicas_room_mia_return_priest_outfit:
    scene expression player.location.background_blur
    show player 14f at Position (xoffset=1)
    show players robe f
    with dissolve
    player_name "That went better than I exp-"

    show player 14f at Position (xpos=182)
    show players robe f at left
    show ang 2 at right
    with fastdissolve
    angelica "Itu dia!"

    show ang 1
    show player 23 at Position (xpos=180)
    show players robe
    with fastdissolve
    player_name "!!!" with hpunch
    show player 10
    player_name "Oh, sorry!"

    player_name "Aku tidak bermaksud-"

    show player 11
    show ang 2
    angelica "Stop."

    show ang 1
    show player 22
    player_name "..."
    show ang 2
    angelica "I've been watching you this whole time."

    angelica "Stealing the priest's robe... Impersonating our priest in the confessional..."

    angelica "... And lying to that poor woman."

    show ang 1
    show player 10
    player_name "It's not what you think!"

    player_name "I was just trying to help her..."

    show player 11
    show ang 2
    angelica "Help?"

    angelica "The only person you can help now is yourself..."

    angelica "... Because I'm thinking about reporting you to the authorities."

    show ang 1
    show player 22
    player_name "!!!"
    show ang 2
    angelica "Unless... You do something for me."

    show ang 1
    show player 11
    player_name "..."
    show player 12
    player_name "I don't see how I can be of any hel-"

    show player 11
    show ang 2
    angelica "Come visit me in a week."

    angelica "I'll explain what I need from you..."

    angelica "... And don't try hiding from me, or everyone will know what you did..."

    angelica "... Especially that lady. The one I saw you with!"

    show ang 1
    show player 10
    player_name "Please don't say anything to her... I'll be back. I promise."

    show player 11
    show ang 2
    angelica "Bagus."

    angelica "Now, return what you stole and leave my chambers..."

    show ang 1
    hide players robe
    show player 444 at left
    with dissolve
    player_name "..."
    hide player
    hide ang
    with dissolve
    return

label church_angelicas_room_mia_church_night_visit:
    scene church_nun_night_c
    show ang 1 at right
    show player 10 at left
    with dissolve
    player_name "Hai, {b}Suster Angelica{/b}..."

    show player 5
    show ang 2
    angelica "I knew I could count on you."

    angelica "You value our mutual agreement... And you value secrets."

    angelica "This is why I trust you will help me..."

    show ang 1
    show player 12
    player_name "So, what exactly are we talking about here?"

    show player 5
    show ang 2
    angelica "I perform a private sacrament at night... In my chambers..."

    show player 11
    angelica "Its purpose is to help members of our church struggling with their impurities..."

    angelica "... I help them purge away their sins!"

    show ang 1
    show player 10
    player_name "Sinners?"

    show player 11
    show ang 2
    angelica "Itu benar!"

    angelica "But, in order to keep performing this sacrament, I need to find appropriate candidates..."

    angelica "... Freshly picked from our local worshipers!"

    show ang 1
    show player 10
    player_name "Okay, but what am I supposed to do?"

    show player 11
    show ang 2
    angelica "I just need you to find some!"

    show ang 1
    show player 10
    player_name "You need me to find people?!"

    show player 11
    show ang 2
    angelica "Yes, sinners."

    show ang 1
    show player 37 with dissolve
    player_name "..."
    show player 38 with dissolve
    player_name "But, I don't really know anyone like that... I don't even-"

    show player 3 with dissolve
    show ang 2
    angelica "You DO know someone!"

    show ang 1
    show player 12 with dissolve
    player_name "... But, who?!"

    show player 11
    show ang 2
    angelica "The lady from the confessional."

    angelica "Her name is {b}Helen{/b}."

    angelica "She has always been a devout servant of our Lord."

    angelica "She believes herself to be very righteous and would never agree to my... Ritual."

    angelica "But she had such a look of shame after talking with you in the confessional."

    angelica "You know her secret sins."

    angelica "And you will bring her to me."

    angelica "I personally enjoy purging the sins of the truly faithful."

    angelica "It is one of the most... Satisfying... Experiences of our religion."

    show ang 1
    show player 22
    player_name "!!!"
    show player 10
    player_name "You want me to {b}bring Helen here{/b}?!"

    show player 11
    show ang 2
    angelica "In my chambers, at night."

    show ang 1
    show player 12
    player_name "How can I possibly convince her to come here?! I don't see how..."

    show player 11
    show ang 2
    angelica "I'm sure you will find a way."

    angelica "Both our interests are on the line here..."

    show ang 1
    show player 24
    player_name "{i}*Huh*{/i}"

    show player 12
    player_name "Okay, I'll give it a try... But what's this sacrament about anyway?"

    show player 5
    show ang 2
    angelica "You will find out, in due time."

    show ang 1
    show player 10
    player_name "I-I should really get going. It's getting late."

    show player 5
    show ang 2
    angelica "Of course! Just make sure you remember our agreement."

    hide ang with dissolve
    show player 24
    player_name "..."
    hide player with dissolve
    return

label church_angelicas_room_mia_church_sacrement:
    scene church_nun_night_c
    show player 5f at right
    show helen 23 at Position (xpos=575)
    show ang 2f at left
    with dissolve
    angelica "Thank you, {b}[firstname]{/b}, for bringing this wonderful disciple to us!"

    angelica "{b}Helen{/b} has been attending our church for a very long time..."

    angelica "... And she told me everything about her failing marriage."

    show ang 1f
    show helen 24
    helen "I... I'm just hoping this will help me deal with our ungodly ways..."

    show helen 23
    show ang 2f
    angelica "Indeed, {b}Helen{/b}."

    angelica "I'm proud of you for willing to face your demons."

    angelica "Are you willing to follow my commands, in order to find the light?"

    show ang 1f
    show helen 24
    helen "Yes. I am..."

    show helen 23
    show ang 2f
    angelica "Good! There will be three levels towards your redemption."

    angelica "The first step requires that you rid yourself of all earthly materials..."

    show player 11f
    angelica "... Such as your {i}clothes{/i}."

    angelica "Only then, will we be able to start the process of purging your sins!"

    show ang 1f
    show helen 4 at Position (xoffset=2) with dissolve
    helen "You don't actually expect me to... Get undressed here?!"

    show helen 1 at Position (xoffset=2)
    show ang 2f
    angelica "We are God's creatures, {b}Helen{/b}... We are all equal!"

    angelica "You shouldn't be ashamed of who you are..."

    show ang 1f
    show helen 25 with dissolve
    helen "..."
    show helen 23
    show ang 2f
    angelica "Go on, {b}Helen{/b}. Rid yourself of it all..."

    show ang 1f
    show helen 27
    pause
    show helen 28
    helen "If this is what I must do, then I shall do it..."

    show player 106f
    show helen 21 with dissolve
    pause
    show player 11f
    show helen 22 at Position (xoffset=-13) with dissolve
    pause
    show helen 33 with dissolve
    show player 23f
    player_name "!!!"
    show ang 2f
    show helen 29
    angelica "Well done, {b}Helen{/b}."

    show ang 1f
    show helen 33
    helen "..."
    show ang 2f
    show helen 29
    angelica "{b}[firstname]{/b}?"

    show ang 1f
    show helen 31
    show player 21f
    player_name "Ehh... Yes?"

    show player 5f
    show ang 2f
    show helen 29
    angelica "You can leave us now, I won't be needing your help for tonight."

    angelica "Come back another time, so we can continue our sessions..."

    show ang 1f
    show player 10f
    player_name "Oh baiklah."

    player_name "Good night, then!"

    hide player
    hide helen
    hide ang
    with dissolve
    return

label church_angelicas_room_mia_angelicas_order:
    scene church_nun_night_c with fade
    show player 23f at right
    show helen 29 at Position (xpos=575)
    show ang 5f at left
    with dissolve
    player_name "!!!"
    show ang 6f
    angelica "What is the matter, {b}[firstname]{/b}?"

    show ang 7f with dissolve
    pause
    show ang 8f
    angelica "You're not having any sinful thoughts, are you?"

    show player 22f
    angelica "Maybe you should take {b}Helen{/b}'s place..."

    show ang 7f
    show player 10f
    player_name "No! I'm... I'm just surprised to see you aren't wearing your robe!"

    show player 11f
    angelica "..."
    show ang 9 with dissolve
    angelica "I was just illustrating to {b}Helen{/b} how God blesses his chosen few who are truly holy and devout inwardly and outwardly."

    angelica "As you can see... He has showered me with a truly sacred body..."

    show ang 10
    pause
    show ang 9
    angelica "Right, {b}Helen{/b}?"

    show ang 10
    show helen 34
    helen "... Yes, your body... Is a temple to our Lord."

    show helen 33
    show ang 8f with dissolve
    angelica "In addition, from this point forward the purification sacrament requires me to lay my hands on the repentant filthy sinner."

    angelica "I prefer not to get my clothes dirty..."

    show ang 6f with dissolve
    angelica "Now then, if there is nothing else, I must get back to my instruction with {b}Helen{/b}."

    show ang 9 with dissolve
    angelica "And if I see any sinful desires appearing in your nether regions, I won't be slow to bring about God's judgement on you..."

    show ang 11
    show player 22f
    player_name "!!!"
    show ang 9
    angelica "Understood?"

    show ang 10
    show player 138f at Position (xoffset=-16) with dissolve
    player_name "Y... Ye... Yes... {b}Sister Angelica{/b}."

    hide player
    hide ang
    hide helen
    with dissolve
    return

label priest_outfit:
    call expression game.dialog_select("priest_outfit_dialogue")

    $ M_mia.trigger(T_mia_priest_outfit)
    $ game.main()

label priest_outfit_dialogue:
    scene expression player.location.background_blur
    show player 444f with dissolve
    player_name "..."
    player_name "( This thing is heavy! )"

    show player 106f at Position (xoffset=1)
    show players robe f
    with dissolve
    player_name "Hmm..."

    show player 33f at Position (xoffset=1)
    player_name "( Looks like this could actually work. )"

    show player 14f at Position (xoffset=1)
    player_name "( Let's see if I can get close to {b}Helen{/b}... )"

    hide player
    hide players robe
    with dissolve
    return

label helen_final_sacrament:
    if store._in_replay == None:
        $ player.remove_item("strapon_drawing")
        $ player.remove_item("strapon")
        $ M_mia.trigger(T_angelicas_final_ritual)
    label helen_final_mc:
        call expression game.dialog_select("helen_final_sacrament_pre")

    if store._in_replay == "helen_final_mc":
        jump expression game.dialog_select("helen_mc_replay")

    elif store._in_replay == "helen_final_sacrament":
        jump expression game.dialog_select("helen_ang_replay")
    menu mia_helen_route_spilt:
        "Fuck {b}Helen{/b}.":
            label helen_mc_replay:
                call expression game.dialog_select("helen_final_sacrament_fuck_helen_pre")

            label helen_mc_churchsex:
                call expression game.dialog_select("helen_final_sacrament_fuck_helen_after")

            $ anim_toggle = True
            $ animated = False
            $ xray = False
            jump expression game.dialog_select("helen_final_sacrament_fuck_helen_loop")
        "Watch {b}Sister Angelica{/b}.":

            label helen_ang_replay:
                call expression game.dialog_select("helen_final_sacrament_watch_angelica")

            $ anim_toggle = True
            $ animated = False
            $ xray = False
            jump expression game.dialog_select("helen_final_sacrament_watch_angelica_loop")
    $ game.main()

label helen_final_sacrament_pre:
    scene church_nun_night_c with fade
    show helen whip 1 at left
    show ang 5f at Position (xpos=418)
    show player 12f at right
    with dissolve
    player_name "Oh, good. You guys are already here..."

    show player 5f
    show ang 6f
    angelica "Where else would we be, {b}[firstname]{/b}?"

    show ang 5f
    show player 34f
    player_name "..."
    show player 35f
    player_name "In the church, sitting around a table reading the Bible... With your clothes on?"

    show player 5f
    show ang 8f at Position (xoffset=3) with dissolve
    angelica "{b}Helen{/b}'s soul requires more than common church education."

    angelica "She needs only complete my last ritual."

    angelica "We've already completed the pre-ritual preparations..."

    show ang 9 at Position (xoffset=22) with dissolve
    angelica "Right {b}Helen{/b}?"

    show ang 10 at Position (xoffset=22)
    helen "Yes... {b}Sister Angelica{/b}..."

    helen "My body... Is waiting for your final ritual."

    helen "I want to be purified..."

    helen "I understand now, that I need to be cleansed... From the inside..."

    show ang 9 at Position (xoffset=22)
    angelica "Do you have the object required to penetrate {b}Helen{/b}'s sinful flesh?"

    show ang 10 at Position (xoffset=22)
    show player 239_240f with dissolve
    pause
    show player 457f with dissolve
    player_name "... This is what you wanted, right?"

    show player 458f
    show ang 8f at Position (xoffset=3) with dissolve
    angelica "It's... It's perfect."

    angelica "Put it on me."

    show ang 28 at Position (xpos=393) with dissolve
    show player 457f
    player_name "Wha?"

    show player 458f
    show ang 29
    angelica "Did I stutter?"

    show ang 28
    show player 457f
    player_name "Baiklah..."

    hide player
    show ang 30 at right
    with dissolve
    player_name "Hmm..."

    player_name "I guess there's no easy way to do this..."

    hide ang
    show ang 32 at Position (xpos=483)
    with dissolve
    angelica "Careful now!"

    show ang 31
    pause
    player_name "( ... Her breasts... )"

    player_name "( ... They're so big! )"

    show ang 32
    angelica "Hey! Mind your fingers down there..."

    angelica "I've gotten better at using that whip..."

    show ang 31
    player_name "( ... )"
    show ang 33 at Position (xpos=412)
    show player 10f at right
    with dissolve
    player_name "There. It's on."

    show player 5f
    pause
    show ang 34
    angelica "Did you know this strap-on has a special feature?"

    show ang 35 at Position (xoffset=79)
    show player 6f
    pause
    show ang 33
    show player 22f
    player_name "!!!" with hpunch
    show player 23f
    player_name "Apa-"

    show player 22f
    show ang 34
    angelica "Hurry up and undress."

    show ang 33
    show player 23f
    player_name "Undress?!"

    show player 10f
    player_name "You're not going to use that... On m-"

    show player 11f
    show ang 34
    angelica "We all have to be exposed for the last purification ritual."

    show ang 33
    show player 12f
    player_name "Alright! I'm getting undressed!"

    show player 8f with dissolve
    pause
    show player 261 with dissolve
    pause
    show player 8bf with dissolve
    pause
    show player 64f
    show ang 37
    pause
    show ang 34
    angelica "Well... Well..."

    angelica "This could get interesting..."

    show ang 33
    show player 63f
    pause
    show player 61f at Position (xoffset=-19) with dissolve
    player_name "..."
    show player 68f at Position (xoffset=-19)
    show ang 34f at Position (xpos=475) with dissolve
    angelica "{b}Helen{/b}?"

    show ang 33f
    helen "Yes, {b}Sister Angelica{/b}?"

    show ang 34f
    angelica "Apakah kamu siap?"

    show ang 33f
    helen "Ya."

    helen "Purge me, {b}Sister Angelica{/b}."

    show ang 34f
    angelica "Anak yang baik."

    angelica "Turn around and show {b}[firstname]{/b} the root of your lust..."

    show ang 33f
    show helen whip 3 with dissolve
    pause
    hide helen
    show ang 22f at left
    with dissolve
    pause
    show ang 23f with dissolve
    pause
    show ang 24f with dissolve
    pause
    show ang 25f with dissolve
    pause
    show player 68bf at Position (xoffset=-19)
    player_name "!!!"
    show ang 26f
    angelica "Do you like what you see, {b}[firstname]{/b}?"

    angelica "Her... Wet... Obedient... Pussy?"

    show player 65f with dissolve
    pause
    show player 66f with dissolve
    pause
    show player 430bf
    show ang 25bf
    angelica "!!!"
    show ang 22_23_24f
    pause
    show ang 26f
    angelica "What's wrong..."

    show player 430f
    show ang 22_23_24f
    pause
    show ang 26bf
    angelica "... Getting excited?"

    show ang 26f
    angelica "I must say, I'm impressed by how helpful you've been towards {b}Helen{/b}..."

    show player 67bf
    angelica "You must care about her..."

    show ang 26bf
    angelica "Or at least your body is eager to help her..."

    show ang 22_23_24f
    pause
    show player 430f
    show ang 25f
    helen "Ohh..."

    show player 430bf
    player_name "I... I don't think she's as bad as you say she is."

    show player 430f
    show ang 26f
    angelica "Good to know..."

    show ang 25f
    pause
    show ang 26f
    angelica "Now then, I'm sure you're wondering why I asked for the item in the photo."

    angelica "The last step of my purification sacrament requires a long... Rod of judgement."

    angelica "You see... In order to cure {b}Helen{/b}, and become one with her body, she needs holy seeds."

    angelica "It needs to be planted deep... Inside her!"

    angelica "Only then can {b}Helen{/b}'s inner soul be salvaged from all her sins."

    show ang 22_23_24f
    show player 430bf
    player_name "Apa maksudmu?"

    show player 430f
    show ang 26f
    angelica "I'm graciously offering you a choice, {b}[firstname]{/b}."

    angelica "Either you let me purge {b}Helen{/b} and leave her undefiled, so she may return to her husband purified..."

    angelica "Or..."

    angelica "Better yet, you purge her yourself..."

    show ang 25f
    show player 67bf
    player_name "..."
    show ang 26f
    angelica "She'll then become your holy servant, {b}[firstname]{/b}."

    show ang 22_23_24f
    show player 430bf
    player_name "!!!"
    helen "Please, fuck me!!"

    show ang 26f
    angelica "{b}Helen{/b} needs one of us to penetrate her sinful flesh..."

    angelica "... I leave this decision in your hands."

    show ang 25f
    show player 67cf
    player_name "( If I... Do... {b}Helen{/b}, {b}Mia{/b}'s parents won't get back together. )"

    player_name "( And {b}Mia{/b}... {b}Mia{/b} will be so upset. )"

    show player 67bf
    show ang 26f
    angelica "So? Will you help {b}Helen{/b}, or not?"

    show ang 22_23_24f
    return

label helen_final_sacrament_fuck_helen_pre:
    show player 430bf
    player_name "I'll... I'll do it."

    show player 430f
    show ang 26f
    angelica "Sempurna. Perbuatanmu tidak akan luput dari perhatian di mata Tuhan, {b}[firstname]{/b}..."

    angelica "... Atau milikku."

    angelica "Kalau begitu mari kita mulai ritual terakhir."

    hide ang
    hide player
    with dissolve
    return

label helen_final_sacrament_fuck_helen_after:
    scene church_nun_night_hs_1
    show helens 4_4b
    with fade
    angelica "Just the tip, {b}[firstname]{/b}."

    angelica "I want you to go slow."

    if not M_helen.is_state(S_helen_start):
        angelica "The first time is always so... Special."

    show helens 5 with dissolve
    helen "Ohhhh, {b}[firstname]{/b}!"

    $ M_helen.set("sex speed", .175)
    show expression AnimatedImage("helens", [6,7,8,9,10], M_helen) as helens with dissolve
    helen "Ahhhh... Be gentle..."

    player_name "It's so... Wet!"

    player_name "Holy s-"

    angelica "Ah ah ah. We are in a place of worship."

    angelica "Good. Now go deeper and don't release your seed until I say."

    angelica "Don't forget I have my whip..."

    pause
    $ M_helen.set("sex speed", .125)
    angelica "Deeper! Faster {b}[firstname]{/b}! Make her understand what a sinful woman she is!"

    angelica "{b}Helen{/b} needs to realize she can never truly be free of her sin now!"

    $ M_helen.set("sex speed", .075)
    pause
    return

label helen_final_sacrament_fuck_helen_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("helens", [6,7,8,9,10], M_helen) as helens
                $ animated = True
            pause 2
            call expression game.dialog_select("helen_final_sacrament_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [6,7,8,9,10]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "helens {}".format(pose_list[pose_counter]) as helens
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("helen_final_sacrament_hscene_dialog")
        $ animcounter += 1
    angelica "Now! {b}[firstname]{/b}, cum for me!"

    angelica "Cum deep in {b}Helen{/b}!"

    call screen final_sacrament_fuck_helen_options

label helen_final_sacrament_hscene_dialog:
    if animcounter == 1:
        player_name "Ohhh!!!{p=1}{nw}"


    elif animcounter == 2:
        helen "Ahhhh!!!{p=1}{nw}"


    elif animcounter == 4:
        helen "{b}[firstname]{/b}!!!{p=1}{nw}"

    return

label helen_final_sacrament_fuck_helen_cum:
    call expression game.dialog_select("helen_final_sacrament_fuck_helen_cum_pre")
    if not M_helen.is_state(S_helen_start):
        jump expression game.dialog_select("sacrament_complete")

    call expression game.dialog_select("helen_final_sacrament_fuck_helen_cum_after")
    $ renpy.end_replay()
    $ persistent.cookie_jar["Angelica"]["unlocked"] = True
    $ persistent.cookie_jar["Angelica"]["gallery"]["03_unlocked"] = True
    $ M_helen.trigger(T_helen_route)
    $ M_helen.set("helen route", True)
    $ game.timer.tick()
    $ player.go_to(L_map)
    $ game.main()

label helen_final_sacrament_fuck_helen_cum_pre:
    show helens 11_11b with flash
    player_name "UHHH!!"

    helen "AHHHH!!!!"

    show helens 11b with fastdissolve
    helen "I... I feel... Cleansed..."

    show helens 12 with dissolve
    helen "Ohhh... So... Much..."

    scene black with fade
    pause 1
    return

label helen_final_sacrament_fuck_helen_cum_after:


    scene church_nun_night_c with fade
    show helen whip 2 at left
    show ang 34 at Position (xpos=412)
    show player 5f at right
    with dissolve
    angelica "Bless you, {b}[firstname]{/b}!"

    angelica "{b}Helen{/b}'s body is once again purged from her sins..."

    angelica "... And you have just made her your holy servant!"

    show ang 33
    show player 10f
    player_name "What... Does that mean?"

    show player 5f
    show ang 34
    angelica "You have just bound {b}Helen{/b}'s desires to you."

    angelica "She will now obey your commands..."

    show player 11f
    angelica "You have taken her husband's place in their marriage bed."

    angelica "{b}Helen{/b} will now require a daily serving of your holy seed."

    angelica "In order for you to keep each other pure and faithful."

    show ang 33
    show player 12f
    player_name "Apa?!"

    show player 22f
    show ang 34
    angelica "Isn't that right, {b}Helen{/b}?"

    show ang 33
    helen "Y-yes... I must now serve, {b}[firstname]{/b}."

    helen "I... Will accept his holy seed... As a submissive and obedient wife should."

    show ang 34
    angelica "Good, {b}Helen{/b}."

    angelica "This concludes our holy sacrament. You two may now leave in peace."

    angelica "I will continue to offer the various rituals of the sacrament at night."

    angelica "Feel free to visit if you wish to... Participate."

    show ang 33
    show player 12f
    player_name "That's nice and all..."

    show player 10f
    player_name "... But I'd better get back home."

    hide player
    hide helen
    hide ang
    with dissolve
    return

label helen_final_sacrament_watch_angelica:
    show player 67cf
    player_name "saya..."

    player_name "Saya tidak bisa melakukannya."

    player_name "{b}Helen{/b} needs her husband, and {b}Mia{/b} needs her parents."

    show player 67bf
    show ang 26f
    angelica "Fine, I guess I'll have to be the one to save {b}Helen{/b}."

    angelica "Stand back, {b}[firstname]{/b}."

    show ang 23f
    pause
    show ang 22f
    show player 430f
    player_name "..."
    helen "Thank you, {b}Sister Angelica{/b}..."

    hide ang
    hide player
    with dissolve

    scene church_nun_night_hs_2 with fade
    show helens 13 with dissolve
    angelica "{b}Helen{/b}, I've been looking forward to this moment."

    angelica "You've always presented yourself as the most devout and pious member of God's flock."

    angelica "I've always wanted to penetrate a dirty sinner's soul... And not using God's word."

    helen "Oh?"

    angelica "You are not greater than anyone else..."

    angelica "You are worse..."

    angelica "You are a slut, {b}Helen{/b}."

    angelica "Receive my rod of judgement!"

    show helens 14 with dissolve
    helen "Ohhh!!!"

    angelica "Deeper, slut!"

    angelica "Take it all!"

    $ M_helen.set("sex speed", .175)
    show expression AnimatedImage("helens", [15,16,17,18,19], M_helen) as helens with dissolve
    helen "Ohhh!!!"

    helen "Faster! {b}Sister Angelica{/b}! Faster!"

    $ M_helen.set("sex speed", .125)
    return

label helen_final_sacrament_watch_angelica_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("helens", [15,16,17,18,19], M_helen) as helens
                $ animated = True
            pause 2
            call expression game.dialog_select("angelica_final_sacrament_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [15,16,17,18,19]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "helens {}".format(pose_list[pose_counter]) as helens
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("angelica_final_sacrament_hscene_dialog")
        $ animcounter += 1
    helen "I'm sooo close!"

    call screen final_sacrament_watch_angelica_options

label angelica_final_sacrament_hscene_dialog:
    if animcounter == 1:
        player_name "Ohhh!!!{p=1}{nw}"


    elif animcounter == 2:
        helen "Ahhhh!!!{p=1}{nw}"


    elif animcounter == 4:
        helen "{b}Sister{/b}!!!{p=1}{nw}"

    return

label helen_final_sacrament_watch_angelica_cum:
    call expression game.dialog_select("helen_final_sacrament_watch_angelica_cum_pre")
    $ renpy.end_replay()
    $ persistent.cookie_jar["Angelica"]["unlocked"] = True
    $ persistent.cookie_jar["Angelica"]["gallery"]["02_unlocked"] = True
    $ M_mia.trigger(T_mia_route)
    $ game.timer.tick()
    $ player.go_to(L_map)
    $ game.main()

label helen_final_sacrament_watch_angelica_cum_pre:
    show helens 14 with fastdissolve
    angelica "Now, release your sins!"

    angelica "Cum for me, {b}Helen{/b}!"

    show helens 20 with flash
    helen "OHHHH!!!!!"

    helen "OHHHHHHHH!!!!"

    show helens 21 with dissolve
    angelica "Good slut..."

    scene black with fade
    pause 1



    scene church_nun_night_c with fade
    show helen whip 2 at left
    show ang 34 at Position (xpos=412)
    show player 5f at right
    with dissolve
    angelica "{b}Helen{/b} has now been purified."

    angelica "Through my training, she has become more submissive."

    angelica "God's demand of all holy wives to their husbands."

    show ang 33

    helen "Thank you, {b}Sister Angelica{/b}."

    show player 11f
    show ang 34
    angelica "As for you {b}[firstname]{/b}, I have to say, I am a bit disappointed."

    show player 24f
    angelica "God called upon your aid, and you turned your back..."

    angelica "... When you should have been the one to share your seeds with {b}Helen{/b}!"

    show player 5f
    angelica "But perhaps this is faith."

    angelica "Thank you for you assistance."

    angelica "I release you of your duties and will not require your services anymore."

    show ang 33
    show player 12f
    player_name "I'm just glad our deal is over."

    show player 10f
    player_name "I truly hope that {b}Helen{/b} feels better after all this."

    hide player
    hide helen
    hide ang
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
