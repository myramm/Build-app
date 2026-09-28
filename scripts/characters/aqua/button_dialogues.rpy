label aqua_dialogue_night:
    show player 10 with dissolve
    player_name "It's getting late..."
    player_name "I should find my way out of this underwater cavern before it gets too dark."
    hide player with dissolve
    return

label aqua_dialogue_aqua_found:
    show aqua 2 zorder 1 at Position(xpos=.5875, ypos=1.0) with dissolve
    pause
    show player 16 zorder 2 at Position(xpos=.125, ypos=1.0) with dissolve
    show aqua 1
    aqua "( !!! )" with hpunch
    aqua "You!!"
    show player 15
    show aqua 2
    player_name "That's right, me!"
    player_name "You said I had to come get it and here I am!"
    player_name "Now give me back the shiny!"
    show player 16
    show aqua 1
    aqua "Hahahaha, you funny human!"
    aqua "You come long way..."
    aqua "... You mussst be good ssswimmer, like {b}Aqua{/b}."
    show player 24
    show aqua 2
    player_name "{i}*Cough*{/i} Yeah, I guess..."
    show player 30
    player_name "What is this place anyways?"
    show player 16
    show aqua 1
    aqua "Thisss {b}Aqua{/b} nest!"
    show player 12
    show aqua 2
    player_name "You live here?"
    show player 11
    show aqua 1
    aqua "Yesss."
    show player 10
    show aqua 2
    player_name "By yourself?"
    show player 11
    show aqua 4
    aqua "Yesss."
    show player 10
    show aqua 3
    player_name "Are there more of you?"
    show player 11
    show aqua 4
    aqua "More... of me?"
    show player 10
    show aqua 3
    player_name "You know, other nests with other... umm, Aquas?"
    show player 11
    show aqua 4
    aqua "Oooh, no."
    show aqua 5
    aqua "Othersss go away long time ago..."
    aqua "... They leave {b}Aqua{/b} behind."
    show player 10
    show aqua 3
    player_name "Aww, that sounds lonely."
    show player 5
    show aqua 1
    aqua "Mmm, yes... Sssometimes..."
    aqua "... But fishiesss keep {b}Aqua{/b} company!"
    show aqua 2b
    aqua "Fishiesss you sssteals with your ssshiny!"
    show player 15
    show aqua 1b
    player_name "I told you that wasn't me!"
    player_name "It belonged to {b}CAPTAIN Terry{/b}."
    show player 16
    show aqua 4
    aqua "{b}Caplan Terry{/b}?"
    show aqua 5
    pause
    show aqua 4
    aqua "Hmm, maybe you tell truth..."
    show player 12
    show aqua 3
    player_name "I am telling the truth, {b}Aqua{/b}."
    show player 16
    show aqua 2b
    aqua "Well, what {b}Aqua{/b} do then?"
    aqua "{b}Caplan Terry{/b} ssstealsss fishiesss!"
    show aqua 4
    aqua "If fishiesss all gone, who {b}Aqua{/b} talksss to?"
    show player 11
    show aqua 5
    aqua "{b}Aqua{/b} go crazy and never find mate!"
    show player 10
    show aqua 3
    player_name "Mate?"
    show player 11
    show aqua 4
    aqua "Yesss, {b}Aqua{/b} waiting for mate to help make babiesss."
    show player 10
    show aqua 5
    player_name "Really?"
    player_name "How long have you been waiting?"
    show aqua 4
    show player 11
    aqua "Looooong time... but nobody comesss..."
    aqua "... Nobody findsss {b}Aqua{/b}."
    show player 10
    show aqua 5
    player_name "Well, I found you."
    show player 13
    show aqua 1
    aqua "Yesss, you findsss {b}Aqua{/b}!"
    show aqua 2
    aqua "And if you talk true, maybe we be friendsss."
    show aqua 9
    aqua "Promise not ssstealsss fishiesss and {b}Aqua{/b} give you back shiny."
    show player 14
    show aqua 8
    player_name "Yes!"
    player_name "I mean, thank you, {b}Aqua{/b}."
    show player 13
    show aqua 9
    aqua "You promise?"
    show player 14
    show aqua 8
    player_name "I promise, I won't steal \"fishies\"."
    show player 13
    show aqua 9
    aqua "Ookaay."
    show aqua 10
    pause
    show aqua 2
    show player 471
    player_name "Phew, thank you {b}Aqua{/b}!"
    show player 470
    show aqua 1
    aqua "Just remember, no ssstealsss {b}Aqua{/b} fishies..."
    hide player
    hide aqua
    with dissolve
    call popup ('give', 'special_lure')
    return

label aqua_sex:
    $ game.timer.tick()
    if M_aqua.is_state(S_aqua_mate):
        call expression game.dialog_select("aqua_sex_pre_first")

    call expression game.dialog_select("aqua_sex_pre")
    if M_aqua.is_state(S_aqua_mate):
        label aqua_sex_replay:
            call expression game.dialog_select("aqua_sex_after_first")

    call expression game.dialog_select("aqua_sex_after")
    jump expression game.dialog_select("aqua_sex_loop")

label aqua_sex_pre_first:
    scene location_lair_mount
    show aqua 2 zorder 1 at Position(xpos=.5875, ypos=1.0)
    show player 2 zorder 2 at Position(xpos=.125, ypos=1.0)
    player_name "{b}Aqua{/b}, I have some good news!"
    show player 1
    show aqua 1
    aqua "{i}*Gasp*{/i} You learn to breathe underwater, like {b}Aqua{/b}?!"
    show player 12
    show aqua 2
    player_name "Wha-"
    player_name "No."
    show player 1
    show aqua 7
    aqua "Oh, Ookaay."
    aqua "What isss newsss?"
    show player 2
    show aqua 6
    player_name "I convinced {b}Captain Terry{/b} to stop fishing!"
    show player 1
    show aqua 7
    aqua "You mean fishiesss sssafe?!"
    aqua "{b}Captain Terry{/b} gone?!"
    show player 17
    show aqua 6
    player_name "Hey, you said it right that time!"
    show player 1
    show aqua 7
    aqua "Huh?"
    show player 2
    show aqua 6
    player_name "You said \"{b}Captain Terry{/b}\" correctly that time."
    show player 1
    show aqua 7
    aqua "Yesss, {b}Caplan Terry{/b}!"
    show player 90
    show aqua 6
    player_name "..."
    show aqua 6b
    aqua "..."

    show player 37
    player_name "Just, never mind."
    show player 2
    player_name "Your fish will be safe from now on."
    show player 1
    show aqua 7
    aqua "Oh, thisss isss good newsss!"
    show aqua 14
    aqua "You nice human!"
    aqua "Ssstrong human!"
    show player 29
    show aqua 13
    player_name "You're welcome, {b}Aqua{/b}..."
    show player 1
    show aqua 11
    aqua "..."
    show aqua 12
    aqua "So, human ready to mate with {b}Aqua{/b}?"
    show player 21
    show aqua 13
    player_name "R-right now?"
    show player 297
    show aqua 14
    aqua "Yesss, {b}Aqua{/b} tired of waiting."
    aqua "Mate take her ssstrongly in water!"
    show player 10
    show aqua 13
    player_name "In the water?"
    show player 11
    show aqua 14
    aqua "Yesss, come."
    return

label aqua_sex_pre:
    scene location_lair_cutscene
    show text _ ("{b}Aqua{/b}'s touch was soft and gentle as she took my hand and started towards the luminescent pool.") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("I struggled to keep pace, fumbling with my clothes.") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("But she didn't seem to notice, her excitement palpable as she lead her new mate into the water.") as caption with dissolve
    pause
    return

label aqua_sex_after_first:
    scene location_lair_water
    show aswim 1 at left
    show pswim 1 at right
    with fade
    pause
    show aswim 2
    aqua "Ooh, mate has good body."
    show aswim 1
    show pswim 2
    player_name "Thanks, {b}Aqua{/b}..."
    show aswim 3
    show pswim 1
    pause
    show aswim 2
    aqua "Your eel isss sssleeping."
    show aswim 1
    show pswim 2
    player_name "Huh?"
    show aswim 3
    pause
    show pswim 3
    pause
    show pswim 2
    player_name "Oh, yeah."
    show aswim 2
    show pswim 1
    aqua "Does mate like {b}Aqua{/b} body?"
    show aswim 1
    show pswim 2
    player_name "Yes... {i}*Gulp*{/i} Umm, \"mate\" likes {b}Aqua{/b}'s body very much."
    show aswim 2
    show pswim 1
    aqua "Good, {b}Aqua{/b} body belong to you now."
    aqua "Your eel can play inside {b}Aqua{/b} whenever it wantsss."
    show aswim 3
    pause
    show aswim 2
    aqua "It's warm inside {b}Aqua{/b}..."
    show aswim 3
    pause
    show aswim 2
    aqua "... And sssoft..."
    show aswim 3
    pause
    show aswim 2
    aqua "... And wet."
    show pswim 3
    pause
    show aswim 3
    show pswim 4
    pause
    show aswim 4
    show pswim 5
    pause
    show pswim 9
    pause
    show aswim 2
    show pswim 6
    aqua "Ooh, eel likesss thisss, yesss?"
    show aswim 3
    show pswim 7
    player_name "Y-yes."
    show aswim 4
    aqua "Mmm, {b}Aqua{/b} wantsss it."
    show aswim 3
    show pswim 8
    player_name "..."
    show aswim 4
    aqua "{b}Aqua{/b} wantsss it now!"
    hide pswim
    show aswim 5
    with dissolve
    pause
    show aswim 6 at right with dissolve
    player_name "{i}*Gulp*{/i}"
    aqua "Aaah, yessss... Come eel, you play inside {b}Aqua{/b} now."
    aqua "Give {b}Aqua{/b} ssstrong babiesss..."
    player_name "Oh, wow!"
    aqua "Mmm!"
    return

label aqua_sex_after:
    scene location_lair_watersex
    show aquas 1 at Position(xalign = 1.0, yalign = 1.0)
    with fade
    aqua "{b}Aqua{/b} needsss it inside her!"
    aqua "Hurry my mate!"
    player_name "..."
    show aquas 2 with dissolve
    aqua "Hissss."
    aqua "Your eel sssooo big!"
    aqua "Take me ssstrong!"
    $ M_aqua.set("sex speed", .175)
    show expression AnimatedImage("aquas", [3,4,5,6,7], M_aqua) as aquas with dissolve
    aqua "Ooohh!"
    pause
    aqua "So ssstrong!"
    pause
    aqua "And deep!"
    $ M_aqua.set("sex speed", .125)
    aqua "Aaahh!"
    pause
    aqua "Mmm, my mate."
    aqua "Faster!"
    $ M_aqua.set("sex speed", .075)
    pause
    return

label aqua_sex_loop:
    show screen sex_anim_buttons 
    pause
    hide screen sex_anim_buttons 
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("aquas", [3,4,5,6,7], M_aqua) as aquas
                $ animated = True
            pause 5
            call expression game.dialog_select("aqua_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [3,4,5,6,7]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "aquas {}".format(pose_list[pose_counter]) as aquas
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("aqua_hscene_dialog")
        $ animcounter += 1
    call screen aqua_sex_options

label aqua_hscene_dialog:
    if animcounter == 1:
        aqua "Ahhhh!!!{p=1}{nw}"

    elif animcounter == 3:
        aqua "Take me!!!{p=1}{nw}"
        player_name "Uhhh...{p=1}{nw}"
    return

label aqua_sex_cum:
    call expression game.dialog_select("aqua_sex_cum_pre")
    if not store._in_replay == None or M_aqua.is_state(S_aqua_mate):
        call expression game.dialog_select("aqua_sex_cum_first")
    scene black with dissolve

    $ renpy.end_replay()
    $ persistent.cookie_jar["Aqua"]["unlocked"] = True
    $ persistent.cookie_jar["Aqua"]["gallery"]["01_unlocked"] = True
    $ M_aqua.trigger(T_aqua_mated)
    $ player.go_to(L_map)
    $ game.main()

label aqua_sex_cum_pre:
    player_name "This is unbelievable!"
    player_name "{b}Aqua{/b}, I'm gonna..."
    aqua "Yesss... YESSS MY MATE!"
    aqua "Give {b}Aqua{/b} your ssseeeeeeds!"
    aqua "HISSSSS!!!"
    show aquas 8 with flash
    player_name "UHHH!!"
    aqua "AAAAHHH!!!!"
    pause
    show aquas 9
    player_name "Wow!"
    player_name "That was incredible!"
    aqua "Yesss..."
    aqua "... {b}Aqua{/b} can feel ssstrong ssseed ssswimming inside her!"
    pause
    return

label aqua_sex_cum_first:
    scene location_lair_mount
    show aqua 11 zorder 1 at Position(xpos=.5875, ypos=1.0)
    show player 2 zorder 2 at Position(xpos=.125, ypos=1.0)
    with fade
    player_name "So you enjoyed that?"
    show player 1
    show aqua 12
    aqua "Yesss, {b}Aqua{/b} enjoys much..."
    aqua "... Feelsss like ssseafoam all over."
    show player 2
    show aqua 11
    player_name "You were incredible, I've never felt anything like that before."
    show player 1
    show aqua 14
    aqua "Yesss, thisss {b}Aqua{/b} first time too..."
    show aqua 12
    aqua "... But Mate must take {b}Aqua{/b} many more times!"
    show aqua 14
    aqua "More ssseeed is needed, yesss?"
    show player 2
    show aqua 13
    player_name "Absolutely, I'll come back really soon!"
    show player 1
    show aqua 14
    aqua "Mate promise?"
    show player 2
    show aqua 13
    player_name "Oh, I promise!"
    show player 1
    show aqua 12
    aqua "Good."
    aqua "{b}Aqua{/b} want much more!"
    show aqua 14
    aqua "Come back sssoon, human."
    show aqua 11
    aqua "{b}Aqua{/b} wait here until ssseafoam ssstop dancing..."
    return

label aqua_dialogue_pre:
    show aqua 2 zorder 1 at Position(xpos=.5875, ypos=1.0) with dissolve
    show player 36 zorder 2 at Position(xpos=.125, ypos=1.0) with dissolve
    player_name "Hi, {b}Aqua{/b}!"
    show player 1
    show aqua 1
    aqua "Yess?"
    show player 2
    show aqua 2
    player_name "I wanted to speak with you."
    show player 1
    show aqua 4
    aqua "What doesss human boy want?"
    return

label aqua_dialogue_the_others:
    show aqua 3 zorder 1 at Position(xpos=.5875, ypos=1.0)
    show player 10 zorder 2 at Position(xpos=.125, ypos=1.0)
    player_name "{b}Aqua{/b}, what happened to the rest of your kind?"
    show player 11
    show aqua 4
    aqua "Hmm, {b}Aqua{/b} not sssure..."
    aqua "... Maybe they don't like {b}Aqua{/b}..."
    aqua "... or maybe they forget?"
    show aqua 5
    show player 10
    player_name "Aww, I'm sorry {b}Aqua{/b}."
    show player 11
    show aqua 1
    aqua "You ask more questionsss?"
    show aqua 2
    return

label aqua_dialogue_how_are_you:
    show aqua 3 zorder 1 at Position(xpos=.5875, ypos=1.0)
    show player 2 zorder 2 at Position(xpos=.125, ypos=1.0)
    player_name "{b}Aqua{/b}, how are you?"
    show player 1
    show aqua 4
    aqua "Hmm?"
    show player 2
    show aqua 3
    player_name "How are you feeling?"
    show player 1
    show aqua 5
    aqua "Hmm, {b}Aqua{/b} lonely, with so few fishies..."
    show aqua 4
    aqua "... But likesss when human boy come visit."
    show player 2
    show aqua 3
    player_name "I like talking with you too, {b}Aqua{/b}."
    show player 1
    show aqua 1
    aqua "Yesss, like talking."
    aqua "You ask more questionsss?"
    show aqua 2
    return

label aqua_dialogue_mating_pre:
    show aqua 3 zorder 1 at Position(xpos=.5875, ypos=1.0)
    show player 10 zorder 2 at Position(xpos=.125, ypos=1.0)
    player_name "{b}Aqua{/b}, what kind of mate are you looking for?"
    show player 11
    show aqua 4
    aqua "Man."
    aqua "Ssstrong man, that give {b}Aqua{/b} ssstrong babiesss."
    show aqua 1
    aqua "You know man like this?"
    show player 34
    show aqua 3
    player_name "Hmm."
    return

label aqua_dialogue_mating_stat_fail:
    show aqua 3 zorder 1 at Position(xpos=.5875, ypos=1.0)
    show player 29 zorder 2 at Position(xpos=.125, ypos=1.0)
    player_name "How about me?"
    show player 3
    show aqua 4
    aqua "You ssstrong man?"
    show player 29
    show aqua 3
    player_name "Yes?"
    show player 3
    show aqua 5
    aqua "..."
    aqua "Hmm..."
    pause
    show aqua 4
    aqua "... {b}Aqua{/b} thinks... No."
    aqua "This is bad idea."
    show player 24
    show aqua 3
    player_name "Aww, man."
    return

label aqua_dialogue_mating_stat_pass:
    show aqua 3 zorder 1 at Position(xpos=.5875, ypos=1.0)
    show player 2 zorder 2 at Position(xpos=.125, ypos=1.0)
    player_name "Maybe I could help?"
    show player 1
    show aqua 7
    aqua "You?"
    show player 2
    show aqua 6
    player_name "Well, I mean, I did swim all the way down here to find you."
    show player 1
    show aqua 7
    aqua "You did."
    show player 2
    show aqua 6
    player_name "... And I fought a very mean squid along the way."
    show player 1
    show aqua 7 with hpunch
    aqua "You fight Inky?!"
    show player 2
    show aqua 6
    player_name "Inky?"
    player_name "Yes, I fight Inky."
    show aqua 7
    aqua "Oooh, Inky ssstrong!"
    show aqua 12
    pause
    show aqua 11
    aqua "Maybe you do give {b}Aqua{/b} ssstrong babiesss."
    show player 14
    show aqua 13
    player_name "Really?!"
    show player 1
    show aqua 14
    aqua "Yesss, but no mate yet!"
    aqua "First you prove strength."
    show player 10
    show aqua 13
    player_name "Prove my strength?"
    player_name "How am I supposed to do that?"
    show player 1
    show aqua 7
    aqua "You sssay {b}Caplan Terry{/b} ssstealsss fishiesss, yesss?"
    show player 12
    show aqua 6
    player_name "{b}CAPTAIN Terry{/b}."
    player_name "Yes, he's the guy who's been fishing off the dock."
    show player 11
    show aqua 7
    aqua "Hmm, you make {b}Caplan Terry{/b} go away!"
    show aqua 11
    aqua "You do this and then you mate with {b}Aqua{/b}."
    show player 10
    show aqua 13
    player_name "Well, I suppose I can give it a shot."
    show player 11
    show aqua 14
    aqua "Good, you go."
    aqua "Sssave fishiesss!"
    return

label aqua_dialogue_mating_hint:
    show aqua 3 zorder 1 at Position(xpos=.5875, ypos=1.0)
    show player 12 zorder 2 at Position(xpos=.125, ypos=1.0)
    player_name "What do I need to do again, {b}Aqua{/b}?"
    player_name "To prove my strength?"
    show player 11
    show aqua 7
    aqua "Make {b}Caplan Terry{/b} go away!"
    aqua "Sssave fishiesss!"
    show player 10
    show aqua 6
    player_name "Oh, right... {b}CAPTAIN Terry{/b}."
    show player 11
    show aqua 7
    aqua "That's what {b}Aqua{/b} say... {b}Caplan Terry{/b}!"
    show player 12
    show aqua 6
    player_name "CAPT-"
    player_name "{i}*Sigh*{/i} Never mind."
    player_name "I guess, I'll go try and talk to him."
    show player 5
    show aqua 7
    aqua "Yesss, tell him leave fishiesss alone!"
    return

label aqua_dialogue_mate:
    show aqua 2 zorder 1 at Position(xpos=.5875, ypos=1.0)
    show player 21 zorder 2 at Position(xpos=.125, ypos=1.0)
    player_name "I thought maybe you would like to... get in the water again?"
    show player 26
    show aqua 3
    aqua "..."
    show aqua 1
    aqua "Oh, you want make babiesss?"
    show player 21
    show aqua 12
    player_name "I, err... yes?"
    show player 26
    show aqua 11
    aqua "Hahaha, you funny human."
    aqua "You {b}Aqua{/b} mate now..."
    show aqua 14
    aqua "... {b}Aqua{/b} always ready for more ssseeds!"
    aqua "If mate wantsss {b}Aqua{/b}, he must take her..."
    aqua "... Ssstrongly in water isss best but mate should choose!"
    return

label aqua_dialogue_nothing:
    show aqua 3 zorder 1 at Position(xpos=.5875, ypos=1.0)
    show player 36 zorder 2 at Position(xpos=.125, ypos=1.0)
    player_name "Nothing, I was just saying hi!"
    show player 1
    show aqua 4
    aqua "Human boy isss... funny..."
    show aqua 1
    aqua "... I like human boy..."
    show player 21
    show aqua 2
    player_name "I err... like you too, {b}Aqua{/b}."
    show player 13
    aqua "..."
    show player 29
    player_name "Anyway, I should get going."
    show player 3
    show aqua 1
    aqua "Ssso sssoon?"
    aqua "You come back tomorrow?"
    show player 17
    show aqua 2
    player_name "You bet!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
