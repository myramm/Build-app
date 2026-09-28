label trailer_park_first_visit:
    scene expression game.timer.image("trailer_interior_c{}")
    show player 10 with dissolve
    player_name "( Is this where {b}Roxxy{/b} lives? )"
    player_name "( There's trash all over the place... )"
    hide player with dissolve
    return

label trailer_interior_roxxy_get_cheerleader_outfit:
    scene expression game.timer.image("trailer_interior_c{}")
    show old_roxxy 1f f at Position (xpos=400)
    show player 5 zorder 1 at left
    show old_crystal 3 at right
    with dissolve
    crystal "What the hell are ya doin' home?!"
    crystal "Ya know ya ain't 'spose to be missin' no more school!"
    show old_crystal 1
    show old_roxxy 3f
    roxxy "Ugh, relax!"
    roxxy "I just came back to get something is all..."
    show old_roxxy 1f f
    show old_crystal 2
    crystal "... And I see ya brought that cute boyfriend of yers!"
    show player 13
    show old_crystal 4 with dissolve
    show old_roxxy 2f
    roxxy "... He's not my boyfriend!"
    show player 5
    show old_crystal 1 with dissolve
    roxxy "I just didn't wanna walk across town on my own!"
    show old_roxxy 1f f
    show old_crystal 2
    crystal "Well, if he ain't yer boyfriend, can he be mine?!"
    show player 22
    crystal "Hahahaha!"
    show old_crystal 1
    show old_roxxy 3f
    roxxy "... Ugh, shuddup {b}Mom{/b}!"
    hide old_roxxy with dissolve
    show player 5
    show old_crystal 3
    crystal "... So, what are yer intentions with my daughter?"
    show old_crystal 1
    show player 10
    player_name "... Huh?"
    show player 5
    show old_crystal 2
    crystal "Ya know, yer intentions?!"
    crystal "Ya plannin' on fornicatin' with her?"
    show old_crystal 1
    show player 21
    player_name "What?! ... No, ma'am!"
    player_name "I'm just helping her out with school."
    show player 5
    show xtra 21 zorder 2 at left
    show old_crystal 2
    crystal "Haha, no need to go gettin' all embarrassed!"
    show old_crystal 3
    crystal "I'm just curious is all..."
    show old_crystal 2
    crystal "If yer gonna be havin' the intercourse with my daughter..."
    show player 22
    crystal "... Ya better find yerself a good job!"
    crystal "We don't need another deadbeat 'round here."
    show old_crystal 1
    hide xtra
    show player 21
    player_name "... Really, ma'am. We're just friends."
    show xtra 21 zorder 2 at left
    show player 5
    show old_crystal 3
    crystal "Hehe, look at ya turnin' red..."
    crystal "I swear, yer cuter than socks on a rooster!"
    show old_crystal 4
    show old_roxxy 3cf zorder 0 at Position (xpos=400)
    with dissolve
    roxxy "Did you move my cheerleading uniform somewhere?"
    show old_roxxy 3df
    show old_crystal 2 with dissolve
    crystal "... Not that I recall."
    show old_crystal 1
    show old_roxxy 3f
    roxxy "I can't find it!"
    show old_roxxy 3df
    show old_crystal 2
    crystal "Well, what do ya expect me to do about it?"
    show old_crystal 1
    show old_roxxy 3f
    roxxy "Ugh, nothing {b}Mom{/b}... Just sit on your ass and drink all day."
    roxxy "... As usual."
    show old_roxxy 3df
    show old_crystal 3
    crystal "{b}Roxanne{/b}!"
    crystal "Now, I dun told ya not to be talking to me like that!"
    crystal "I do plenty 'round here."
    show old_roxxy 2bf
    crystal "Why just this mornin' yer cousin came by fer a bit of business and we was-"
    show old_crystal 1
    show old_roxxy 2cf
    show player 11
    roxxy "Hold on a second!"
    roxxy "{b}Clyde{/b} was here this morning?!"
    show old_roxxy 2bf
    show old_crystal 2
    crystal "... Yeah."
    show old_crystal 1
    show old_roxxy 3f
    roxxy "Damnit!"
    roxxy "Is he sitting out on that stupid tractor drinking again?"
    show old_roxxy 3df
    show old_crystal 2
    crystal "How should I know?!"
    show old_crystal 1
    show old_roxxy 3cf
    roxxy "Ugh, come with me {b}[firstname]{/b}..."
    hide old_roxxy
    hide player
    hide xtra
    with dissolve
    show old_crystal 2
    crystal "... That girl needs whoopin'."
    show old_crystal 4 with dissolve
    pause
    scene black with fade
    return

label trailer_interior_crystal_sex_offer_pre_first:
    scene expression "backgrounds/location_trailer_day_closeup.jpg"
    show player 13 at left
    show old_crystal 2 zorder 1 at right
    with dissolve
    crystal "Well, well, well... If it isn't {b}Roxanne{/b}'s new beau..."
    show old_crystal 4 with dissolve
    show player 10
    player_name "Eh, beau?"
    show player 5
    show old_crystal 2 with dissolve
    crystal "Ya here lookin' to knock boots with my little gal again?"
    show old_crystal 1
    show player 10
    player_name "... Knock boots?"
    show player 12
    player_name "I'm not sure what you're talking about, ma'am."
    show player 5
    show old_crystal 2
    crystal "Ma'am?"
    show old_crystal 2b
    crystal "Hahahaha!!"
    crystal "Ain't nobody ever called me \"ma'am\" before..."
    show old_crystal 2
    crystal "Just call me, {b}Crystal{/b}."
    show old_crystal 3 with dissolve
    crystal "... And as fer the boot knockin'..."
    show old_crystal 3b_3c with dissolve
    pause
    show player 22
    player_name "!!!" with hpunch
    show old_crystal 4 with dissolve
    show player 29 with dissolve
    player_name "Oh! I wasn't..."
    show old_crystal 1 with dissolve
    player_name "I mean, we don't..."
    show player 3
    show old_crystal 2b
    crystal "Hahaha!"
    show old_crystal 3 with dissolve
    crystal "Of course ya do!"
    show old_crystal 2 with dissolve
    crystal "Ya think I can't hear y'all going at it in there?!"
    show player 22 with dissolve
    crystal "This trailer don't exactly offer a lot in the way of privacy!"
    show old_crystal 1
    show player 21
    player_name "Heh, yea... I guess you're right."
    player_name "Sorry."
    show player 5
    show old_crystal 2
    crystal "Oh, it's nothin' to apologize fer."
    crystal "{b}Roxanne{/b}'s had to listen to me ruttin' around with a fella, more than once."
    show old_crystal 1
    show player 10
    player_name "Yeah, umm... is she here?"
    show player 5
    show old_crystal 2
    crystal "I'm afraid not."
    show old_crystal 1
    show player 10
    player_name "Oh."
    show player 36
    player_name "Well, I'll get out of your hair then-"
    hide player
    show old_crystal 17 at left
    with dissolve
    crystal "Now, hold yer horses there, handsome!"
    crystal "Ya know, I can tell from {b}Roxanne{/b}'s wailin' that yer takin' real good care of my daughter, Romeo..."
    show old_crystal 17b
    player_name "Umm?"
    show player 106 zorder 0 at left
    show old_crystal 16c at Position (xpos=134)
    with dissolve
    crystal "Is she doin' the same?"
    crystal "Gettin' all that poison out of yer system?"
    show old_crystal 16d
    show player 108f
    player_name "P-poison?"
    show player 109f
    show old_crystal 16c
    crystal "Hehe, yeah."
    show old_crystal 18_18b
    show old_crystal_talking_head zorder 2
    with dissolve
    crystal "It's important for young boys to get that stuff out."
    hide old_crystal_talking_head
    show player 106
    player_name "!!!"
    show player 108f
    player_name "W-what are you-"
    show player 109f
    show old_crystal_talking_head zorder 2
    crystal "Shh, it's alright..."
    crystal "... I don't mind helpin' out a bit."
    hide old_crystal_talking_head
    show player 10
    player_name "What about {b}Roxxy{/b}?!"
    show player 5
    show old_crystal_talking_head zorder 2
    crystal "Oh, don't ya worry about {b}Roxanne{/b}..."
    crystal "... Ya see, my baby girl and I are a package deal!"
    crystal "She's known that since she was a whipper."
    hide old_crystal_talking_head
    show player 5
    player_name "..."
    show old_crystal undress 1 at center with dissolve
    pause
    show old_crystal undress 2 with dissolve
    show player 428
    crystal "Just let me take care of you..."
    show old_crystal undress 3 with dissolve
    show player 427
    player_name "{i}*Gulp*{/i}"
    show player 428
    show old_crystal undress 4 with dissolve
    crystal "... I'll make sure yer nice and satisfied."
    show player 426
    show old_crystal undress 5 with dissolve
    pause
    show old_crystal undress 6 with dissolve
    pause
    show old_crystal undress 7 at right with dissolve
    crystal "Bring that fine piece of man meat over here to Momma!"
    show old_crystal undress 7b
    show player 427
    player_name "Oh, I dunno..."
    show player 426
    show old_crystal undress 7
    crystal "Hehe, no need to be shy, Romeo."
    show old_crystal undress 10 with dissolve
    crystal "I know what yer packin' in them shorts..."
    crystal "... And it's got my pussy wet as October!"
    show old_crystal undress 10b
    player_name "..."
    show old_crystal undress 10
    crystal "Unless..."
    crystal "... Ya prefer to kick in mah back door?"
    show old_crystal undress 9 with dissolve
    show player 427
    player_name "Huh?"
    player_name "Y-you don't mean-"
    show player 428
    show old_crystal undress 11_11b
    player_name "!!!" with hpunch
    crystal "Ya can use me any way ya want, {b}[firstname]{/b}!"
    show player 429
    player_name "R-really?"
    show player 426
    crystal "Mhmm!"
    return

label trailer_interior_crystal_sex_offer_pre_repeat:
    scene expression "backgrounds/location_trailer_day_closeup.jpg"
    show player 10 at left
    show old_crystal 1 at right
    with dissolve
    player_name "So about what you said earlier..."
    show player 5
    show old_crystal 2
    crystal "Oh, changed yer mind have ya?"
    show old_crystal 1
    show player 24
    player_name "..."
    show old_crystal undress 1 with dissolve
    crystal "Ya won't regret it, Romeo."
    show old_crystal undress 3 with dissolve
    show player 428
    crystal "If there's one thing I know, it's how to please a man!"
    show old_crystal undress 4 with dissolve
    pause
    show old_crystal undress 5 with dissolve
    pause
    show old_crystal undress 6 with dissolve
    pause
    show old_crystal undress 7b
    player_name "!!!" with hpunch
    show old_crystal undress 7
    crystal "Hehe!"
    crystal "Oh, the things I'd do to ya..."
    show old_crystal undress 9 with dissolve
    show player 426
    player_name "..."
    show old_crystal undress 11_11b with dissolve
    crystal "... Get that cock out and I'll show ya?"
    return

label trailer_interior_crystal_sex_offer_menu:
    menu:
        "Okay.":
            call expression game.dialog_select("trailer_interior_crystal_sex_offer_accept")
            call expression game.dialog_select("trailer_interior_crystal_sex_or_anal_menu")
            $ anim_toggle = True
            $ animated = False
            jump expression game.dialog_select("trailer_interior_crystal_sex_loop")

        "I can't do this." if not M_crystal.is_set("crystal sex offer denied"):
            call expression game.dialog_select("trailer_interior_crystal_sex_offer_denied_first")
            $ M_crystal.set("crystal sex offer denied", True)

        "I still can't do this." if M_crystal.is_set("crystal sex offer denied"):
            call expression game.dialog_select("trailer_interior_crystal_sex_offer_denied_repeat")
    $ game.main()

label trailer_interior_crystal_sex_offer_accept:
    show player 429
    player_name "O-okay."
    show player 426 zorder 2
    show old_crystal undress 10 with dissolve
    crystal "That's what I wanted to hear!"
    crystal "Ya can take me any way ya want, Romeo!"
    show old_crystal undress 10b
    return

label trailer_interior_crystal_sex_offer_denied_first:
    show player 24
    player_name "I-"
    show old_crystal undress 9 with dissolve
    crystal "Hehe, c'mon Romeo, don't make me beg fer it!"
    show player 37 with dissolve
    player_name "I can't."
    show old_crystal undress 8 with dissolve
    crystal "Hmm?"
    crystal "What do ya mean, ya can't?!"
    crystal "It ain't difficult!"
    crystal "Just whip that big boy out and choose a hole!"
    show old_crystal undress 8b
    show player 12 with dissolve
    player_name "No, I mean... I can't do it to {b}Roxxy{/b}."
    show player 5
    show old_crystal undress 8
    crystal "Psh, I dun told ya, we're a package deal!"
    crystal "Besides, {b}Roxanne{/b} ain't got to find out, ya silly boy!"
    show old_crystal undress 8b
    show player 10
    player_name "Yeah, but I would know..."
    show player 12
    player_name "... And I don't want to be that guy."
    show player 5
    show old_crystal undress 6 with dissolve
    crystal "..."
    show old_crystal undress 5 with dissolve
    pause
    show old_crystal undress 4 with dissolve
    crystal "Sheesh, ya know... ya really are a good kid."
    show old_crystal undress 2 with dissolve
    crystal "I don't understand how in the world my {b}Roxanne{/b} managed to get hold of ya..."
    show old_crystal undress 1 with dissolve
    crystal "{i}*Sigh*{/i}"
    show old_crystal 6 with dissolve
    crystal "... But I hope she's smart enough to keep ya 'round."
    crystal "Still, offer's on the table, Romeo."
    crystal "Iffin' ya ever change yer mind."
    show old_crystal 16
    crystal "Mmm, and I hope ya do."
    show old_crystal 14
    show player 11
    player_name "..."
    hide old_crystal with dissolve
    show player 10
    player_name "Well, that was awkward."
    hide player with dissolve
    return

label trailer_interior_crystal_sex_offer_denied_repeat:
    show player 24
    player_name "I-"
    show player 25
    player_name "I'm sorry, {b}Crystal{/b}, I can't do it..."
    show old_crystal undress 9 with dissolve
    crystal "..."
    show old_crystal undress 6 with dissolve
    crystal "Tch, ya know... it ain't nice to tease a girl, Romeo!"
    show old_crystal undress 5 with dissolve
    show player 10
    player_name "I'm really sorry."
    show player 5
    show old_crystal undress 5 with dissolve
    pause
    show old_crystal undress 1 with dissolve
    crystal "Yeah, whatever."
    show old_crystal 6 with dissolve
    crystal "Ya know where to find me, iffin' ya should change yer mind."
    hide old_crystal with dissolve
    player_name "..."
    hide player with dissolve
    return

label trailer_interior_crystal_sex_or_anal_menu:
    menu:
        "Sex.":
            $ M_crystal.set("crystal anal", False)
            if M_roxxy.get("roxxy crystal sex"):
                call expression game.dialog_select("trailer_interior_crystal_sex_or_anal_choose_sex_first")
            else:

                call expression game.dialog_select("trailer_interior_crystal_sex_or_anal_choose_sex_repeat")
        "Anal.":

            $ M_crystal.set("crystal anal", True)
            if M_roxxy.get("roxxy crystal sex"):
                call expression game.dialog_select("trailer_interior_crystal_sex_or_anal_choose_anal_first")
            else:

                call expression game.dialog_select("trailer_interior_crystal_sex_or_anal_choose_anal_repeat")
    return

label trailer_interior_crystal_sex_or_anal_choose_sex_first:
    show old_crystal undress 10 with dissolve
    crystal "That works for me, Romeo."
    show old_crystal undress 10b
    show player 8 with dissolve
    pause
    show player 261f with dissolve
    pause
    show player crystal 13 with dissolve
    pause
    hide player
    show old_crystal undress 12
    with dissolve
    crystal "Mmm, gimme that monster!"
    hide old_crystal
    scene expression "backgrounds/location_trailer_sex.jpg"
    show old_crystals insert 1 at left
    show trailer_counter at right
    with dissolve
    pause
    show old_crystals cum 2 with dissolve
    crystal "!!!"
    $ M_crystal.set("sex speed", .175)
    show expression AnimatedImage("old_crystals", [1,2,3,4,5,6,7,8], M_crystal) as old_crystals
    with dissolve
    pause
    return

label trailer_interior_crystal_sex_or_anal_choose_sex_repeat:
    show old_crystal undress 10
    crystal "Ya got it, handsome!"
    show old_crystal undress 10b
    show player 8 with dissolve
    pause
    show player 261f with dissolve
    pause
    show player crystal 13 with dissolve
    pause
    hide player
    show old_crystal undress 12
    with dissolve
    crystal "Mmm, I don't need no foreplay, Romeo..."
    crystal "... Stuff it in there!"
    player_name "Y-yes, ma'am..."
    hide old_crystal

    scene expression "backgrounds/location_trailer_sex.jpg"
    show old_crystals insert 1 at left
    show trailer_counter at right
    with dissolve
    pause
    show old_crystals cum 2
    crystal "Goddamn, Romeo!" with hpunch
    crystal "That dick is somethin' special!"
    crystal "Phew!"
    $ M_crystal.set("sex speed", .175)
    show expression AnimatedImage("old_crystals", [1,2,3,4,5,6,7,8], M_crystal) as old_crystals
    with dissolve
    pause
    return

label trailer_interior_crystal_sex_or_anal_choose_anal_first:
    show old_crystal undress 10 with dissolve
    crystal "Mmm, my favorite!"
    show old_crystal undress 10b
    show player 8 with dissolve
    pause
    show player 261f with dissolve
    pause
    show player crystal 13 with dissolve
    crystal "Get that monster in my ass!"
    hide player
    show old_crystal undress 12b
    with dissolve
    pause
    hide old_crystal

    scene expression "backgrounds/location_trailer_sex.jpg"
    show old_crystals insert 1 at left
    show trailer_counter at right
    with dissolve
    player_name "You ready?"
    crystal "Do it!"
    show old_crystals cum 2
    crystal "!!!" with hpunch
    crystal "NGGHHH!!!"
    pause
    player_name "You're shaking..."
    crystal "..."
    player_name "Ma'am?"
    crystal "Shut up and give it to me!"
    player_name "O-okay!"
    $ M_crystal.set("sex speed", .175)
    show expression AnimatedImage("old_crystals", [1,2,3,4,5,6,7,8], M_crystal) as old_crystals
    with dissolve
    pause
    return

label trailer_interior_crystal_sex_or_anal_choose_anal_repeat:
    crystal "Oh, now that's what momma likes to hear!"
    show player 429
    player_name "Yeah?"
    show player 426
    crystal "Hell yeah!"
    crystal "Don't get me wrong now."
    crystal "Regular sex is good too..."
    crystal "... But I get crazy intense orgasms when I'm gettin' my ass fucked!"
    crystal "Always have."
    show player 427
    player_name "Really?"
    show player 426
    crystal "Ya better believe it!"
    show old_crystal undress 10 with dissolve
    crystal "Go on, stuff it in there and I'll show ya."
    show old_crystal undress 10b
    show player 429
    player_name "O-okay."
    show player 8 with dissolve
    pause
    show player 261f with dissolve
    pause
    show player crystal 13 with dissolve
    pause
    hide player
    show old_crystal undress 12b
    with dissolve
    crystal "That's it, handsome."

    scene expression "backgrounds/location_trailer_sex.jpg"
    show old_crystals insert 1
    show trailer_counter at right
    with dissolve
    crystal "Don't be scared to push it in there real deep!"
    crystal "I can take it!"
    show old_crystals cum 2
    crystal "!!!" with hpunch
    crystal "Oooh, fuck yeah!"
    $ M_crystal.set("sex speed", .175)
    show expression AnimatedImage("old_crystals", [1,2,3,4,5,6,7,8], M_crystal) as old_crystals
    with dissolve
    crystal "RRRRRAAAAGGGGHHH!!!"
    crystal "Goddamn, that's deep!"
    pause
    crystal "Feels like ya scramblin' mah insides!"
    player_name "Should I stop?!"
    crystal "GGRRRAAAHHH!!!"
    player_name "{b}Crystal{/b}?!"
    crystal "NO, IT'S FUCKIN' FANTASTIC!!!"
    crystal "C'MON, ROMEO..."
    crystal "... OBLITERATE THAT ASS!!!"
    pause
    $ M_crystal.set("sex speed", .125)
    crystal "{i}*Gasp*{/i}"
    pause
    crystal "AAAAAHHHHH!!!"
    crystal "FUCK! FUCK!! FUUUUUCK!!!"
    pause
    crystal "DON'T STOP!!!"
    pause
    crystal "NGGHHH!!!" with hpunch
    return

label trailer_interior_crystal_sex_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("old_crystals", [1,2,3,4,5,6,7,8], M_crystal) as old_crystals
                $ animated = True
            pause 5
            call expression game.dialog_select("crystal_trailer_interior_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "old_crystals {}".format(pose_list[pose_counter]) as old_crystals
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("crystal_trailer_interior_hscene_dialog")
        $ animcounter += 1
    if not M_roxxy.get("roxxy crystal sex") and store._in_replay == None:
        $ M_roxxy.trigger(T_roxxy_crystal_sex)
    call screen crystal_sex_options

label crystal_trailer_interior_hscene_dialog:
    $ random_count = randomizer()
    if animcounter == 0:
        if not M_roxxy.get("roxxy crystal sex"):
            crystal "Good lord!{p=1}{nw}"
            crystal "This is definitely the biggest I ever had!{p=2}{nw}"
            pause
            crystal "It feels like I'm fuckin' a t-rex!{p=2}{nw}"
            player_name "Should I stop?{p=2}{nw}"
            crystal "Hell no!{p=1}{nw}"
            crystal "Fuck me harder, Romeo!{p=1}{nw}"

        elif M_roxxy.get("roxxy crystal sex"):
            if random_count <= 33:
                if M_crystal.is_set("crystal anal"):
                    crystal "Rrraaahh!!{p=1}{nw}"
                    crystal "That's so damn good!{p=1}{nw}"
                else:

                    crystal "Mmm, that's it handsome!{p=1}{nw}"
                    crystal "Ya go on and get all that poison out!{p=2}{nw}"

            elif random_count > 33 and random_count <= 66:
                if M_crystal.is_set("crystal anal"):
                    crystal "Oh yeah, Romeo...{p=1}{nw}"
                    pause
                    crystal "... This is just what {b}Momma{/b} needed today!{p=2}{nw}"
                    player_name "Feels good?{p=1}{nw}"
                    crystal "Ya better believe it!{p=1}{nw}"
            else:

                if M_crystal.is_set("crystal anal"):
                    player_name "I can't believe you like anal so much...{p=2}{nw}"
                    crystal "Oh handsome, I don't just like anal...{p=2}{nw}"
                    crystal "... I fuckin' LOVE it!{p=2}{nw}"
                    crystal "It just sends sparks all throughout my body...{p=2}{nw}"
                    player_name "...{p=1}{nw}"
                    crystal "... And if ya angle it just right, and it hits my-{p=2}{nw}"
                    crystal "AAAHHH!!{p=1}{nw}"
                    pause
                    crystal "There, there, there!!!{p=2}{nw}"
                    crystal "GGRRRAAAHHH!!!{p=1}{nw}"
                else:

                    crystal "Mmm, yer hittin' it good, Romeo!{p=2}{nw}"
                    player_name "Heh, thanks!{p=1}{nw}"

    elif animcounter == 1:
        if M_roxxy.get("roxxy crystal sex"):
            if random_count <= 33:
                if M_crystal.is_set("crystal anal"):
                    crystal "C'mon, Romeo! Deeper!{p=1}{nw}"
                    player_name "Yes, ma'am.{p=1}{nw}"
                    if M_crystal.get("sex speed") > .076:
                        $ M_crystal.set("sex speed", M_crystal.get("sex speed") - 0.05)
                else:

                    crystal "Give it to {b}Momma{/b}!{p=1}{nw}"

            elif random_count > 33 and random_count <= 66:
                if M_crystal.is_set("crystal anal"):
                    crystal "Mmm, that's it, handsome!{p=1}{nw}"
                    crystal "Keep giving me those nice deep strokes!{p=2}{nw}"
                else:

                    crystal "Say, Romeo?{p=1}{nw}"
                    player_name "Hmm?{p=1}{nw}"
                    crystal "Is my daughter tighter than me?{p=2}{nw}"
                    player_name "Yeah, she's a lot tighter than you.{p=2}{nw}"
                    pause
                    crystal "Hmm, she doesn't take it this deep though, does she?{p=2}{nw}"
                    player_name "No, she does not!{p=1}{nw}"
                    crystal "Hehehe, well, I guess experience counts for somethin-{p=2}{nw}"
                    $ M_crystal.set("sex speed", .075)
                    crystal "Oh, goddamn!!!{p=1}{nw}" with hpunch
                    pause
                    crystal "AAAAAAHHHHH!!!{p=1}{nw}"
            else:

                if M_crystal.is_set("crystal anal"):
                    crystal "GRAAAHHH!!!{p=1}{nw}"
                else:

                    crystal "Aah!{p=1}{nw}"
        else:

            crystal "Fuck me harder, handsome!{p=2}{nw}"

    elif animcounter == 2:
        if not M_roxxy.get("roxxy crystal sex"):
            crystal "Aaah!!{p=1}{nw}"
            crystal "Ya been stickin' to my daughter with this monster?!{p=2}{nw}"
            player_name "Y-yes, ma'am.{p=1}{nw}"
            pause
            player_name "Though she never takes it this deep!{p=2}{nw}"
            crystal "I should hope not!{p=1}{nw}"
            crystal "Poor girl ain't ready for this kinda deep dickin'!{p=2}{nw}"

        elif M_roxxy.get("roxxy crystal sex"):
            if random_count <= 33:
                if M_crystal.is_set("crystal anal"):
                    crystal "Goddamn, handsome!{p=1}{nw}"
                    crystal "AAahhhh!!{p=1}{nw}"
                else:

                    crystal "Aaahh!!{p=1}{nw}"
                    crystal "Fuck yeah!!{p=1}{nw}"

            elif random_count > 33 and random_count <= 66:
                if M_crystal.is_set("crystal anal"):
                    player_name "It's so tight!{p=1}{nw}"
                    crystal "Mmm, don't stop!{p=1}{nw}"
            else:

                crystal "Yer dick sure is somethin' special, {b}[firstname]{/b}!{p=2}{nw}"
                player_name "Hehe, thanks!{p=1}{nw}"

    elif animcounter == 3:
        if M_roxxy.get("roxxy crystal sex"):
            if random_count <= 33:
                if not M_crystal.is_set("crystal anal"):
                    crystal "Nngghhh!{p=1}{nw}"

            elif random_count > 66:
                if not M_crystal.is_set("crystal anal"):
                    crystal "I'm gonna-{p=1}{nw}"
                    crystal "NGGHHH!!!{p=1}{nw}"
        else:

            if random_count > 50:
                crystal "Aaah!!{p=1}{nw}"
                crystal "I'm gettin' close!{p=1}{nw}"
    return

label trailer_interior_crystal_sex_cum:
    if M_roxxy.get("roxxy crystal sex"):
        if M_crystal.is_set("crystal anal"):
            call expression game.dialog_select("trailer_interior_crystal_sex_cum_repeat_anal")
        else:

            call expression game.dialog_select("trailer_interior_crystal_sex_cum_repeat")

    elif M_crystal.is_set("crystal anal"):
        call expression game.dialog_select("trailer_interior_crystal_sex_cum_first_anal")
        $ M_roxxy.set("roxxy crystal sex", 0)
    else:

        call expression game.dialog_select("trailer_interior_crystal_sex_cum_first")
        $ M_roxxy.set("roxxy crystal sex", 0)
    $ renpy.end_replay()
    $ persistent.cookie_jar["Crystal"]["unlocked"] = True
    $ persistent.cookie_jar["Crystal"]["gallery"]["01_unlocked"] = True
    $ M_roxxy.trigger(T_roxxy_crystal_sex)
    $ game.timer.tick()
    $ game.main()

label trailer_interior_crystal_sex_cum_repeat_anal:
    player_name "Your ass it so tight!"
    player_name "I can't hold it!"
    crystal "Just a little more!"
    pause
    crystal "Oh, fuck... I'm gonna cum!"
    player_name "Me too!!"
    show old_crystals cum 2_2b
    crystal "AAAHHHH!!!"
    player_name "HNNGGG!!!" with flash
    pause
    show old_crystals retract 3
    show old_crystals_anal_cum
    with dissolve
    player_name "Wow, that was intense!"
    hide old_crystals
    hide old_crystals_anal_cum
    with dissolve

    scene expression "backgrounds/location_trailer_day_closeup.jpg"
    show old_crystal undress 10b at right
    show old_crystal_anal_cum undress
    show player crystal 13 at left
    show player_slick_boner crystal
    with dissolve
    crystal "Phew, goddamn..."
    hide old_crystal_anal_cum
    show old_crystal undress 11
    with dissolve
    player_name "..."
    player_name "You alright, ma'am?"
    crystal "... Heh, yeah... Just-"
    show old_crystal undress 11b with dissolve
    crystal "Tch!"
    crystal "..."
    show old_crystal undress 9 with dissolve
    crystal "I got them sparks coursin' through me, heh..."
    show old_crystal undress 7 with dissolve
    crystal "... Go fetch a couple cold ones from the fridge, would ya?"
    show old_crystal undress 7b
    player_name "Sure thing!"
    hide player
    hide player_slick_boner
    with dissolve
    pause
    show old_crystal undress 7
    crystal "Goddamn, that boy is gifted!"
    hide old_crystal with dissolve
    return

label trailer_interior_crystal_sex_cum_repeat:
    player_name "I'm getting close!"
    crystal "Let it out, handsome!"
    crystal "Ya just get it all outta ya system!"
    show old_crystals cum 2_2b
    player_name "HNNGGHHH!!!" with flash
    show old_crystals cum 2b
    show xray_crystal_trailer at Position (align=(0,0))
    crystal "Ahhh!!"
    hide xray_crystal_trailer
    pause
    show old_crystals retract 3 with dissolve
    pause
    crystal "Phew! That was exactly what I needed!"
    hide old_crystals with dissolve

    scene expression "backgrounds/location_trailer_day_closeup.jpg"
    show old_crystal undress 10 at right
    show old_crystal_pussy_cum undress
    show player crystal 13 at left
    show player_slick_boner crystal
    with dissolve
    crystal "Ya feel better now, Romeo?"
    hide old_crystal_pussy_cum
    show old_crystal undress 6
    hide player_slick_boner
    show player 261f at left
    with dissolve
    pause
    show old_crystal undress 5
    show player 8
    with dissolve
    player_name "Yeah, much better."
    show player 111f
    show old_crystal undress 4
    with dissolve
    crystal "Good boy!"
    show old_crystal undress 2 with dissolve
    show player 13
    crystal "Ya just come on back and see me when ya need another release..."
    show old_crystal undress 1 with dissolve
    crystal "... Alright?"
    show old_crystal 4 with dissolve
    show player 14
    player_name "Sure thing, {b}Crystal{/b}."
    show player 13
    show old_crystal 2b with dissolve
    crystal "Hehehe!"
    hide player
    hide old_crystal
    with dissolve
    return

label trailer_interior_crystal_sex_cum_first_anal:
    player_name "I can't hold it any longer!"
    crystal "Fuckin' goddamn!!"
    pause
    player_name "{b}Crystal{/b}?!"
    crystal "GODDAMN!!!"
    pause
    player_name "{b}CRYSTAL{/b}?!?!"
    player_name "I'm gonna-"
    pause
    show old_crystals cum 2_2b
    player_name "HNNGGG!!!" with flash
    crystal "NGGHHHAAAAAAAAAHHHH!!!" with hpunch
    pause
    show old_crystals retract 3
    show old_crystals_anal_cum
    with dissolve
    pause
    hide old_crystals
    hide old_crystals_anal_cum
    with dissolve
    scene expression "backgrounds/location_trailer_day_closeup.jpg"
    show old_crystal undress 10b at right
    show old_crystal_anal_cum undress
    show player crystal 13 at left
    show player_slick_boner crystal
    with dissolve
    player_name "You alright, ma'am?"
    crystal "Uggghhhh..."
    player_name "Ma'am?!"
    show old_crystal undress 10
    crystal "... Mhmm?"
    show old_crystal undress 10b
    player_name "Sheesh, you had me worried there for a second."
    show old_crystal undress 10
    crystal "Just gimme a minute, handsome."
    crystal "I'm fuckin-"
    crystal "Phew, goddamn."
    show old_crystal undress 10b
    hide player_slick_boner
    show player 261f at left
    with dissolve
    player_name "..."
    show player 8 with dissolve
    show old_crystal undress 10
    crystal "I ain't gonna be walkin' right fer a week!"
    show old_crystal undress 10b
    show player 427
    player_name "I'm sorry."
    show player 426
    show old_crystal undress 10
    crystal "Ain't no need to be sorry..."
    crystal "... I aim cum like that since before I had {b}Roxanne{/b}!"
    hide old_crystal_anal_cum
    show old_crystal undress 11b
    with dissolve
    crystal "Ya feel me shakin'!"
    show player 429
    player_name "Heh, I guess I did good then?"
    show player 426
    show old_crystal undress 11 with dissolve
    crystal "Better than good, I'd say!"
    show old_crystal undress 9 with dissolve
    pause
    show old_crystal undress 7 with dissolve
    crystal "Wow, I don't think I can even stand..."
    crystal "... Ya ain't stuck that thing up my daughter's ass have ya?"
    show old_crystal undress 7b
    show player 429
    player_name "No, ma'am."
    show player 426
    show old_crystal undress 7
    crystal "Good!"
    crystal "The poor girl ain't ready for that monster..."
    crystal "... Not yet anyways."
    show old_crystal undress 7b
    player_name "..."
    show old_crystal undress 7
    crystal "Grab me a couple cold ones outta the fridge, will ya?"
    show old_crystal undress 7b
    show player 427
    player_name "You want two?"
    show player 426
    show old_crystal undress 7
    crystal "Hehe, yes."
    crystal "One fer me and one fer mah asshole!"
    crystal "Ya really did a number on it!"
    show old_crystal undress 7b
    show player 429
    player_name "Haha, alright."
    hide player with dissolve
    pause
    show old_crystal undress 7
    crystal "Goddamn, my daughter better be treatin' this one right..."
    crystal "... She lets him get away and I'll disown her ass for sure!"
    hide old_crystal with dissolve
    return

label trailer_interior_crystal_sex_cum_first:
    player_name "Yeah, I'm getting close too."
    crystal "Give it to me now, handsome!"
    crystal "Ya just fire when ready!"
    player_name "Nngghh!"
    pause
    crystal "That's it!"
    crystal "Oh, shit, here it comes!"
    show old_crystals cum 2_2b
    player_name "HNNGGG!!" with flash
    show old_crystals cum 2b
    show xray_crystal_trailer at Position (align=(0,0))
    crystal "AAAhhhh!!"
    hide xray_crystal_trailer
    pause
    show old_crystals retract 3 with dissolve
    crystal "Haaah... Haaah..."
    crystal "Goddamn, Romeo!"
    crystal "Haaah..."
    hide old_crystals with dissolve
    scene expression "backgrounds/location_trailer_day_closeup.jpg"
    show old_crystal undress 10 at right
    show old_crystal_pussy_cum undress
    show player crystal 13 at left
    show player_slick_boner crystal
    with dissolve
    crystal "Mah daughter best be takin' good care of ya, that's all I know."
    show old_crystal undress 10b
    hide player_slick_boner
    show player 261f at left
    with dissolve
    player_name "..."
    show player 8 with dissolve
    show old_crystal undress 10
    crystal "She ever leaves ya feelin' unsatisfied..."
    show player 110f with dissolve
    crystal "... Ya just come see momma {b}Crystal{/b}!"
    crystal "Ya hear me, Romeo?!"
    show old_crystal undress 10b
    show player 111f
    player_name "Yes, ma'am."
    show player 110f
    hide old_crystal_pussy_cum
    show old_crystal undress 5
    with dissolve
    crystal "We gotta keep that dick in the family, for sure!"
    show old_crystal undress 2 with dissolve
    show player 13
    pause
    show old_crystal undress 1 with dissolve
    crystal "Alright, I need a beer after gettin' stuffed like that!"
    show old_crystal 6 with dissolve
    crystal "Ya want one?"
    show old_crystal 5
    show player 14
    player_name "No, thanks."
    player_name "In fact, I should probably get going."
    show player 13
    show old_crystal 6
    crystal "Hmm, iffin' ya say so..."
    crystal "... Come back and see me real soon, handsome."
    hide player
    hide old_crystal
    with dissolve
    return

label trailer_interior_crystal_sex_repeat_inside:

    hide old_crystal
    hide player
    show anon:
        xoffset -90
    show crystal b_dressed_leaning f_smirk:
        xoffset 35
    with {'master': dissolve}

    anon @ -m_talk "..."
    crystal "Hey, how 'bouts a quickie while yer here?"
    anon f_confused @ -m_talk "Hmm?"
    show anon a_surprised_up_both f_surprised_down
    show crystal a_beer_rub b_dressed:
        xoffset -300
    with {'master': dissolve}

    if game.timer.is_morning():
        crystal "I gots 'bout twenty minutes 'fore Gerald Springer starts..."
        crystal "... And fer most men, that's enough time to do it twice!"
    else:
        crystal "Judge Jody just ended and I ain't got nothin' else to do..."
        crystal "... A little hanky panky would really hit the spot, don't ya think?"

    anon f_confused "Y-yeah, but-"
    show anon a_sides f_worried
    with {'master': dissolve}
    anon "What if {b}Roxxy{/b} comes home?"
    show crystal a_beer f_annoyed
    with {'master': dissolve}
    crystal "Oh, quit yer frettin'..."
    show crystal:
        xoffset 0
    with {'master': dissolve}

    if game.timer.is_weekend():
        crystal "... She's off playin' with her friends!"
    else:
        crystal "... She's at school!"

    show crystal a_beer_point b_dressed_leaning f_tired:
        xoffset 35
    with {'master': dissolve}
    crystal "Besides, I know fer a fact my daughter'd appreciate ya helpin' her momma out in her time a need!"
    show crystal a_beer
    with {'master': dissolve}
    anon "Oh, I dunno..."
    crystal f_smirk "What's not to know?!"
    crystal "Ya like sex, don'tcha?!"
    show anon a_behind_head f_shy
    with {'master': dissolve}
    anon "Well, yeah but-"
    crystal f_tired "There ain't nobody better at the sex than me..."
    show crystal a_beer_point
    with {'master': dissolve}
    crystal "... Ya oughta know that by now!"
    show anon a_sides
    show crystal b_dressed_beer:
        xoffset 0
    with {'master': dissolve}
    crystal "Mmm!"
    show crystal a_beer b_dressed
    with {'master': dissolve}
    pause
    show anon f_surprised
    show crystal a_beer_throw
    with {'master': dissolve}
    pause
    show crystal a_remove01 f_smirk
    with {'master': dissolve}
    crystal @ f_burp -m_talk "{i}*Buuuurp*{/i}"
    show crystal a_remove02 b_topless_boobless
    with {'master': dissolve}
    crystal "I know whats ya need..."
    show anon f_surprised_low
    show crystal a_remove03
    with dissolve
    show crystal a_remove04 b_topless
    with {'master': dissolve}
    crystal "... A little incentive, ta get ya engine goin'!"
    show anon f_flirt_low
    show crystal b_dressed_back_shake01:
        xoffset 210
        xzoom -1
    with {'master': dissolve}
    crystal "I got the ticket right here!"
    show crystal b_dressed_back_shake
    with {'master': dissolve}
    anon f_surprised_low @ -m_talk "!!!"
    show anon f_flirt_low
    with {'master': dissolve}
    crystal "Hehehe!"
    show crystal b_dressed_back_remove_pants01
    with {'master': dissolve}
    crystal "C'mon, now..."
    show crystal b_dressed_back_remove_pants02
    with {'master': dissolve}
    crystal "... Get over here and throw it in me quick!"


    hide crystal
    show old_crystal undress 7b at right:
        xoffset 32
    with {'master': dissolve}
    pause
    show old_crystal undress 10:
        xoffset 8
    with {'master': dissolve}
    crystal "You can have mah pussy, iffin' dat's what ya after..."
    show old_crystal undress 9
    with {'master': dissolve}
    pause
    show old_crystal undress 11_11b
    with {'master': dissolve}
    crystal "... but I'm more partial ta takin' it up the old dirt trail."


    hide anon
    show player 426 zorder 2 at left
    with {'master': dissolve}
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
