label home_front_mom_mrsj_visit:
    scene expression L_home.background_blur
    show old_debbie 164f zorder 2 at left
    show mrsj 17 at right
    with dissolve
    mrsj "Hai, {b}[deb_name]{/b}!"

    show old_debbie 165f
    show mrsj 14
    debbie "Oh, hello there, {b}Tammy{/b}."

    show old_debbie 164f
    show mrsj 17
    mrsj "I wanted to stop by and give my condolences for your loss. I know he was your close friend..."

    show old_debbie 165f
    show mrsj 14
    debbie "Oh, thanks... that's so very thoughtful of you."

    show old_debbie 169f
    show mrsj 19
    mrsj "I want you to know that {b}Erik{/b} and I are right next door if you ever need anything."

    mrsj "Even if it's just a friendly ear to listen."

    show old_debbie 168f
    show mrsj 14
    debbie "That's very generous."

    show old_debbie 169f
    show mrsj 17
    mrsj "I know it's not the same, but I can relate a little bit you know?"

    show old_debbie 168f
    show mrsj 14
    debbie "Because of your divorce?"

    show old_debbie 169f
    show mrsj 17
    mrsj "Tentu saja!"

    show mrsj 20
    mrsj "I mean, my husband's not technically dead..."

    show mrsj 18
    mrsj "... But he might as well be, so far as I'm concerned."

    show old_debbie 168f
    show mrsj 14
    debbie "Do you get lonely?"

    debbie "I mean, it can't be easy being by yourself all the time."

    show old_debbie 169f
    show mrsj 20
    mrsj "Yeah, I had a rough time of it for a while there..."

    show mrsj 17
    mrsj "... But then I decided to sublet my house and ended up living with {b}Erik{/b}."

    mrsj "He's been such a blessing!"

    show old_debbie 168f
    show mrsj 14
    debbie "Oh, how so?"

    show old_debbie 169f
    show mrsj 17
    mrsj "He's such a sweet young man, and he needs me to take care of him!"

    show old_debbie 169bf
    mrsj "It feels good to be needed like that again. It really gives me a sense of purpose, you know?"

    show old_debbie 169f
    mrsj "I cook for him and do his laundry. I ask him about his day and show him affection when he needs it."

    show old_debbie 168f
    show mrsj 14
    debbie "Jadi begitu."

    show old_debbie 169f
    show mrsj 18
    mrsj "I think it's helping him come out of his shell too! So it's mutually beneficial!"

    show old_debbie 168f
    show mrsj 14
    debbie "I just don't know how to talk to {b}[firstname]{/b}. I mean, I know he needs guidance but I'm not his mother..."

    show old_debbie 169f
    show mrsj 17
    mrsj "Well, keep at it, honey. It's not going to sort itself out overnight."

    mrsj "Just focus on him and how he's feeling. It's what I did!"

    mrsj "The rest will fall into place soon enough."

    show old_debbie 168f
    show mrsj 14
    debbie "Saya harap Anda benar."

    show old_debbie 169f
    pause
    show player 1 zorder 1 at Position(xpos=300) with dissolve
    show old_debbie 165f
    debbie "Oh! Hi, sweetie!"

    show old_debbie 164f
    show player 14
    player_name "Hey, {b}[deb_name]{/b}... Hi, {b}Mrs. Johnson{/b}!"

    show player 1
    show mrsj 17
    mrsj "Hello there, {b}[firstname]{/b}."

    mrsj "{b}[deb_name]{/b} was just telling me how happy she is that you came to live with her..."

    show mrsj 14
    show player 14
    player_name "Oh, yeah? I'm just thankful she was willing to take me in."

    show mrsj 17
    show player 13
    mrsj "She's a good woman, so you had better take good care of her!"

    show mrsj 14
    show player 14
    player_name "Saya akan!"

    show player 1
    show mrsj 17
    mrsj "Hehe, see {b}[deb_name]{/b}? You guys are gonna be just fine!"

    mrsj "Well, I'd best be getting home."

    show mrsj 14
    show old_debbie 165f
    debbie "You sure you don't want to come in?"

    show old_debbie 164f
    show mrsj 17
    mrsj "No, thanks! I should really get home and check on {b}Erik{/b}. See if there's anything he needs..."

    show mrsj 14
    show old_debbie 165f
    debbie "Well, thanks for the chat {b}Tammy{/b}. Come see us again real soon!"

    show old_debbie 164f
    show mrsj 17
    mrsj "I'll do that! You two take care of each other now, you hear?"

    hide mrsj
    hide old_debbie
    hide player
    with dissolve
    return

label home_front_mom_mow_lawn:
    scene location_home_grass_cutscene_01
    show text _ ("This is a lot harder than I expected. I should've paid more attention to how {b}Dad{/b} used to do it.") as caption
    with fade
    pause

    scene location_home_grass_cutscene_02
    show text _ ("It doesn't look half bad. I Hope {b}[deb_name]{/b} thinks the same.") as caption
    with fade
    pause

    scene location_home_grass_cutscene_03
    show text _ ("Hmm, I wonder how long she's been standing there? I was so focused I didn't notice her come out.") as caption
    with fade
    pause

    scene expression L_home.background_blur
    show player 2 at left
    show xtra 15 zorder 2 at Position(xpos=170,ypos=754)
    show old_debbie 1 at right
    with fade
    player_name "{b}[deb_name]{/b}, I finished the lawn."

    show player 203
    show old_debbie 2
    debbie "I saw that. It looks great, sweetie!"

    show old_debbie 3
    debbie "You did a wonderful job!"

    show old_debbie 2
    debbie "I'm proud of you."

    show player 2
    show old_debbie 1
    player_name "I was just doing it the way I thought {b}Dad{/b} would."

    show player 11
    show old_debbie 2
    debbie "Well, I'm sure he'd be proud too."

    debbie "He always went out of his way to help me out around here."

    show player 21
    show old_debbie 1
    player_name "I will too, {b}[deb_name]{/b}. I feel like it's what he'd want."

    show player 2
    player_name "Should we go inside now?"

    show old_debbie 1
    debbie "Tentu!"

    scene expression L_home.background_blur with None
    show xtra 15 zorder 2 at Position(xpos=520,ypos=754)
    show player 10 zorder 1
    with dissolve
    player_name "{i}*Panting*{/i}"

    show player 14
    player_name "Wow, that was a lot of work!"

    show player 24
    player_name "I need to get out of these stinky clothes and shower now..."

    show player 4 at Position(xoffset=5)
    player_name "I should head {b}downstairs to put these clothes in the wash{/b}."

    hide player with dissolve
    return

label home_front_mom_car_fixed:
    scene expression game.timer.image("home_front_mechanic{}_b")
    show jiang at flip
    show old_debbie 1 at right
    with dissolve
    jiang "Everything should be good as new, ma'am."

    show old_debbie 3
    debbie "Really? That was fast!"

    show old_debbie 1
    jiang "You betcha!"

    jiang "I always work hard when a beautiful woman is involved!"

    jiang "You just give me a call if you have any more trouble."

    jiang "I love making pretty little ladies engines purr. Know what I mean?"

    show old_debbie 3
    debbie "Oh, stop. You're hilarious!"

    debbie "Ha ha ha."

    jiang "Hyuk hyuk hyuk."

    show old_debbie 1
    show player 14 zorder 1
    player_name "Hey, {b}[deb_name]{/b}."

    show player 13
    show old_debbie 2
    debbie "Itu dia!"

    show old_debbie 1
    show player 10f with dissolve
    player_name "Engine repairs all finished?"

    show player 5f
    jiang "Well, I had to replace the whole damn thing, but yeah. It's all finished."

    jiang "Just another day in the life of {b}Jiang{/b} the Car Whisperer. No need to thank me."

    show player 11f
    jiang "Hyuk hyuk."

    jiang "We'll I'd best be off!"

    show player 5f
    jiang "Just gonna take a quick peek under your hood to make sure I didn't leave my tool in her. Know what I mean?"

    show old_debbie 2
    debbie "{i}*Ahem*{/i} Yes, well. Thanks again!"

    show old_debbie 1
    jiang "Not a problem, ma'am."

    hide jiang with dissolve
    show player 13 with dissolve
    show old_debbie 2
    debbie "Want to give it a test drive?"

    show old_debbie 1
    show player 14
    player_name "Tentu!"

    show player 12
    player_name "I hope he's not trying to screw us over."

    show player 5
    show old_debbie 14
    debbie "( He was trying to screw someone alright... )"

    hide player
    hide old_debbie
    with dissolve
    return

label home_front_mom_car_fixed_check_car:
    scene car_interior
    show old_debbie car 2b at right
    show player car 1b
    show player_arms car 1
    show debbie_arms_car 1
    show xtra 30 at right
    with dissolve
    debbie "Let's see..."

    show player car 2b
    show old_debbie car 1
    hide debbie_arms_car
    with dissolve
    debbie "Hmm..."

    show old_debbie car 2b
    show debbie_arms_car 1
    with dissolve
    debbie "It works!"

    show old_debbie car 3
    show player car 2
    player_name "Besar!"

    show player car 1
    show old_debbie car 2
    player_name "Sounds good, too."

    show player car 2b
    show old_debbie car 3b
    debbie "How did you get them to come out so quickly?"

    show old_debbie car 3
    show player car 2
    player_name "It was nothing {b}[deb_name]{/b}."

    show player car 5
    player_name "I guess I can be quite persuasive..."

    player_name "I'm just relieved to see you smiling again..."

    show player car 6
    pause
    show player car 5b
    show old_debbie car 3b
    show debbie_arms_car 2 with dissolve
    debbie "Aduh..."

    debbie "Terima kasih sayang."

    scene car_interior kiss
    hide player car
    hide debbie_arms_car
    hide player_arms car
    show old_debbie car 6 at right
    show xtra 30 at right
    with dissolve
    pause
    show player_boner car 1 with dissolve
    pause
    scene car_interior
    show player car 3b
    show player_arms car 2
    show old_debbie car 3 at right
    show debbie_arms_car 2
    show xtra 30 at right
    show player_boner car 1
    with dissolve
    pause
    show old_debbie car 4c
    show debbie_arms_car 4 with dissolve
    debbie "( !!! )"
    show old_debbie car 5b
    debbie "Oh!"

    show old_debbie car 4c
    show player car 4c
    player_name "Sorry, {b}[deb_name]{/b}..."

    show player car 3
    show old_debbie car 5b
    debbie "It's alright, sweetie."

    debbie "You seem to be getting these quite often when I'm around."

    show old_debbie car 4b
    show debbie_arms_car 2 with dissolve
    debbie "I'm not sure if I should be worried or flattered?"

    show old_debbie car 3
    show player car 4c
    show player_arms car 1 with dissolve
    player_name "I know... I'm really trying hard not to but you're just so pretty."

    show player car 3
    show old_debbie car 4
    debbie "..."
    show old_debbie car 5b
    debbie "Oh sayang..."

    hide player_boner car
    show debbie_arms_car 5b at Position(xalign = 0.357, yalign = 0.558)
    with dissolve
    debbie "I suppose it's not such a bad thing."

    show old_debbie car 5
    show player car 4c
    player_name "{b}[deb_name]{/b}?"

    show player car 3
    show old_debbie car 3b
    debbie "Ssst."

    show old_debbie car 5b
    show debbie_arms_car 5 with dissolve
    debbie "It's normal for young men your age to get excited at the drop of a hat."

    show old_debbie car 5
    show player car 3b
    player_name "{i}*Meneguk*{/i}"

    show player car 3
    show expression AnimatedImage("debbie_arms_car", [5,"5b","5c","5b"], M_debbie) as debbie_arms_car at Position(xalign = 0.357, yalign = 0.558) with dissolve
    pause 1.2
    show debbie_arms_car 5 with dissolve
    show old_debbie car 5b
    debbie "I really wish I could help you out with this, sweetie."

    debbie "... But it just wouldn't be right."

    show expression AnimatedImage("debbie_arms_car", [5,"5b","5c","5b"], M_debbie) as debbie_arms_car at Position(xalign = 0.357, yalign = 0.558) with dissolve
    show old_debbie car 3b
    debbie "You need to find someone your own age..."

    debbie "Someone cute to be your girlfriend. Wouldn't that be nice?"

    show old_debbie car 3
    show debbie_arms_car 5c with dissolve
    show player car 5
    player_name "Y-ya, oke..."

    show player car 5b
    show old_debbie car 3b
    debbie "That's good."

    show debbie_arms_car 5 with dissolve
    debbie "Do you want me to keep going?"

    show old_debbie car 3
    return

label home_front_mom_car_fixed_check_car_little_longer:
    show player car 5
    player_name "Can... Can you keep going a little longer?"

    show player car 2
    player_name "It feels so good!"

    show player car 2b
    show old_debbie car 3b
    debbie "Alright, {b}[firstname]{/b}, but I'm not going to finish you if that's what you're hoping for..."

    show old_debbie car 3
    return

label mom_car_jerk_loop:
    show screen sex_anim_buttons 
    pause
    hide screen sex_anim_buttons 
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("debbie_arms_car", [5,"5b","5c","5b"], M_debbie) as debbie_arms_car at Position(xalign = 0.357, yalign = 0.558)
                $ animated = True
        else:

            $ pose_counter = 0
            $ pose_list = [5,"5b","5c","5b"]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "debbie_arms_car {}".format(pose_list[pose_counter]) as debbie_arms_car at Position(xalign = 0.357, yalign = 0.558)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1

        if animcounter == 1 or M_debbie.get("jerk count") == 1:
            show old_debbie car 3
        else:
            show old_debbie car 4
            show player car 4b
        pause 2

        if animcounter == 3 and M_debbie.get("jerk count") >= 1:
            show player car 4c
            pause 1
        $ animcounter += 1

    $ M_debbie.set("jerk count", M_debbie.get("jerk count") + 1)

    if M_debbie.get("jerk count") == 2:
        jump expression game.dialog_select("home_front_mom_car_fixed_check_car_finished")
    call screen car_mom_jerk_options

label home_front_mom_car_fixed_check_car_finished:
    if M_debbie.get("jerk count") == 2:
        call expression game.dialog_select("home_front_mom_car_fixed_check_car_finished_too_much")
    else:
        call expression game.dialog_select("home_front_mom_car_fixed_check_car_finished_not_enough")
    call expression game.dialog_select("home_front_mom_car_fixed_check_car_finished_after")
    $ M_debbie.trigger(T_debbie_car_fun)
    $ game.timer.tick()
    $ game.main()

label home_front_mom_car_fixed_check_car_finished_too_much:
    show player car 3
    show player_boner car 1
    hide debbie_arms_car
    show debbie_arms_car 4
    with dissolve
    show old_debbie car 5b
    debbie "I... I don't think I should keep doing this..."

    show old_debbie car 5
    show debbie_arms_car 1 with dissolve
    show player car 5
    player_name "But, {b}[deb_name]{/b}-"

    show player car 3
    return

label home_front_mom_car_fixed_check_car_finished_not_enough:
    show player car 4c
    player_name "I guess we should probably stop, huh?"

    show player car 4b
    show old_debbie car 5
    debbie "..."
    show player_boner car 1
    hide debbie_arms_car
    show debbie_arms_car 4
    with dissolve
    show old_debbie car 5b
    debbie "That's a good idea, sweetheart."

    show old_debbie car 5
    show debbie_arms_car 1 with dissolve
    show player car 5
    player_name "... Ya."

    show player car 5b
    return

label home_front_mom_car_fixed_check_car_finished_after:
    show old_debbie car 5b
    debbie "If you feel yourself getting hard, you should go up to your room and take care of it."

    show old_debbie car 3b
    debbie "... Okay, sweetie?"

    show old_debbie car 3
    show player car 4c
    player_name "... Ya, Bu."

    scene black with fade
    hide old_debbie
    hide debbie_arms_car
    hide xtra
    hide player
    hide player_arms car
    hide player_boner car
    return

label home_front_mom_bad_guys_revisit:
    $ playMusic("<loop 73.5>audio/music_villain.ogg", 1.0)
    scene location_home_front_car_day_blur
    show anon f_surprised
    anon "!!!"
    anon f_shock @ -m_talk "( Oh, no! )"

    anon @ -m_talk "( That's the vehicle those Russian goons drive around in! )"

    show anon f_surprised_teeth
    pause
    anon @ -m_talk "( Where the heck is {b}Yumi{/b}?! )"

    hide anon with dissolve
    $ playSound()

    scene location_home_entrance_cutscene01
    show text _ ("It quickly became apparent that both {b}Dimitri{/b} and {b}Igor{/b} were already inside our home, threatening {b}[deb_name]{/b}.") as caption
    with fade
    pause

    scene location_home_entrance_cutscene02
    show text _ ("I couldn't make out what they were saying, but she looked terrified.\nI was completely frozen, unsure what to do or how to save her...") as caption
    with fade
    pause

    play audio smack
    scene location_home_entrance_cutscene03
    show text _ ("Suddenly, one of them hit her, knocking her to the floor and my vision went red.\nI couldn't just stand there and watch any longer...") as caption
    with hpunch
    pause
    hide text with dissolve
    show text _ ("I {b}had{/b} to do something!") as caption with dissolve
    pause

    scene location_home_entrance_fight
    show debbie f_crying_closed a_facepalm:
        flip
        xoffset -100
    show igor:
        xoffset 100
    show dimitri a_sides:
        xoffset -100
    with fade
    anon "{b}[deb_name]{/b}!!"

    show anon f_worried_left a_protect with dissolve:
        xoffset 100
    anon "Are you okay??"

    debbie a_nervous f_sad "{b}[firstname]{/b}?"

    debbie "N-no, you shouldn't be here!"

    dimitri "Ah, wonderful!"

    show anon f_angry
    dimitri "You've come at perfect time."

    anon "Get out of our house!"

    dimitri @ a_out "Oh, such fire!"

    igor @ a_point "You want we should take them to {b}Raz{/b} now?"

    debbie "P-please, you can't-"

    anon a_fists "Back off!"

    anon "I swear, if you touch her again I'm going to-"

    dimitri @ f_laugh "Hah, what are you going to do, little bunny?"

    dimitri "Attack us with carrot?"

    igor "I don't see carrot, {b}Dimitri{/b}..."

    dimitri f_angry_right "Don't be stupid, I only make joke."

    igor "Oh."

    show dimitri f_angry
    anon "I'm calling the cops!"

    dimitri @ a_stop "I think not!"

    dimitri @ f_angry_right "Hold him."

    igor "Yes, {b}Dimitri{/b}."

    show dimitri:
        unflip
        xoffset 100
    show igor f_angry_down b_dressed_holding_mc:
        xoffset 100
    show anon b_empty f_shock:
        xoffset 194
    with dissolve
    debbie @ f_surprised_worried "T-tidak!"

    anon "Get off me!"

    debbie "I'll get you the money, please!"

    debbie "Don't hurt him."

    dimitri "Be silent!"

    dimitri "You had your chance."

    dimitri "Now you must pay in blood."

    hide dimitri
    hide anon
    show igor b_dressed_holding_mc_punched_face
    with dissolve
    anon "Gan!"

    show igor b_dressed_holding_mc_facedown
    show dimitri:
        xoffset 100
    with dissolve
    debbie f_crying_closed "{b}[firstname]{/b}!!!"

    dimitri "This is what happens, when {b}Raz{/b} does not get his money..."

    hide dimitri
    show igor b_dressed_holding_mc_punched_gut
    show anon b_empty f_hurt o_bloody_nose:
        xoffset 239
        yoffset 64
    with dissolve
    anon "Ugh!"

    show igor b_dressed_holding_mc_facedown
    hide anon
    show dimitri:
        xoffset 100
    with dissolve
    dimitri "Perhaps we kill him, and you watch, eh?"

    debbie "Stop, please!!"

    hide dimitri
    show igor b_dressed_holding_mc_punched_gut
    show anon b_empty f_hurt o_bloody_nose:
        xoffset 239
        yoffset 64
    with dissolve
    anon "Urk!"

    show igor b_dressed_holding_mc_facedown
    hide anon
    show dimitri:
        xoffset 100
    with dissolve
    debbie f_sad "Saya akan melakukan apa saja!"

    dimitri "Heh, indeed you will."

    show dimitri b_empty f_grin
    show igor b_dressed_holding_mc_facegrab
    with dissolve
    dimitri "You see, little bunny."

    dimitri "{b}Raz{/b} always gets what is owed."

    dimitri "Perhaps he make whore of your friend, huh?"

    dimitri "She will repay debt on her knees, with cock in her mouth."

    pause
    igor "Heh, I like this plan, {b}Dimitri{/b}."

    dimitri "Come then, take off robe and let us see-"

    "{i}*Sirens blaring*{/i}"

    dimitri f_surprised @ -m_talk "!!!"
    igor f_sad "The police come, {b}Dimitri{/b}."

    dimitri f_angry "Yes, I have ears, idiot!"

    igor f_angry_down "What of them?"

    dimitri "Leave them for now."

    hide dimitri
    show igor b_dressed_holding_mc_punched_gut
    show anon b_empty f_hurt o_bloody_nose:
        xoffset 239
        yoffset 64
    with dissolve
    anon @ -m_talk "..."
    show igor b_dressed_holding_mc_facedown
    hide anon
    show dimitri:
        xoffset 100
    with dissolve
    dimitri "This is far from over."

    show igor b_dressed f_angry:
        xoffset -100
    show anon b_punch f_hurt:
        xoffset 60
    show anon_overlay_o_bloody_nose:
        xoffset 133
        yoffset 143
    with dissolve
    dimitri @ a_point "You tell the cops of this, we fucking kill you all!"

    debbie @ f_surprised_worried -m_talk "!!!"
    dimitri "You hear me?"

    igor f_sad "We must go, {b}Dimitri{/b}!"

    hide igor with dissolve
    dimitri f_grin "See you soon, little bunny."

    hide dimitri with dissolve
    $ playMusic()
    debbie f_sad "Oh, {b}[firstname]{/b}!"

    show debbie b_robe_hug_mc_behind
    hide anon_overlay_o_bloody_nose
    show anon b_empty f_sad_down o_bloody_nose:
        xoffset 39
    show anon_arms_dressed_a_sides_debbie_hug as anon_arms:
        flip
        xoffset -100
    with dissolve
    anon "Ugh."

    debbie "Speak to me!"

    anon "I think they broke my nose..."

    show anon f_hurt
    debbie "{i}*Sniff*{/i} I'm so sorry, sweetie!"

    show jenny f_sad with dissolve
    jenny "Are they gone?"

    pause
    show anon f_depressed
    jenny a_shock "Oh god, he's bleeding!"

    jenny "I called the cops like you told me."

    show jenny a_sides with dissolve
    debbie "Aku tahu."

    debbie "You did good, {b}[jen_name]{/b}."

    jenny "Is he gonna be okay?"

    debbie "Help me get him upstairs to the shower."

    jenny "The shower?"

    debbie "We can't let the police see him like this..."

    jenny "Kenapa tidak?!"

    debbie "Just do what I ask, please!"

    debbie "Easy, sweetie."

    debbie "I've got you."


    $ player.go_to(L_home_shower)
    scene expression player.location.background_blur
    show anon f_worried a_sides o_bloody_nose
    show debbie f_sad a_sides:
        xoffset -100
    show jenny f_sad a_crossed:
        xoffset 100
    with fade
    anon "I tried to stop them..."

    debbie "I know, sweetie."

    debbie "You were so brave."

    jenny "I can't believe they did this..."

    debbie "{b}[jen_name]{/b}, I need you to go open the door for the police."

    jenny "Oke."

    debbie "Don't mention {b}[firstname]{/b}!"

    jenny @ -m_talk "..."
    debbie "I'll be down in a second."

    hide jenny with dissolve
    debbie "C'mon, let's get these bloody clothes off you..."

    show anon b_dressed_changing3 o_empty with dissolve
    pause
    show anon b_shorts f_hurt a_rub o_bloody_nose with dissolve
    anon "Agh!"

    debbie "Apakah kamu baik-baik saja?"

    anon f_sad_down "Y-yeah, just really sore..."

    debbie "A warm shower will help."

    debbie "I'll come back to check on you as soon as the cops leave, okay?"

    anon "Terima kasih, {b}[deb_name]{/b}."

    hide debbie with dissolve

    $ player.go_to(L_home_hallway)
    scene expression player.location.background_blur with fade
    show debbie f_sad with dissolve
    pause
    debbie @ -m_talk "( I feel like I should be in there taking care of him. )"

    pause
    debbie @ -m_talk "( I can't believe he stood up to those men, for me. )"

    debbie @ -m_talk "( He's grown up so quickly because of all this... )"

    debbie @ -m_talk "( ... In more ways than one. )"

    debbie @ -m_talk "( Hmm, maybe I should- )"

    jenny "{b}[deb_name]{/b}!"

    show debbie f_surprised with dissolve:
        flip
        xoffset 500
    jenny "{b}Yumi and Harold{/b} are waiting down here!"

    debbie f_sad @ -m_talk "aku datang!"

    hide debbie with dissolve
    pause

    call scene_shower_with_vfx
    show debbies 26 zorder 2
    with slowfade
    anon "Well, it looks like the bleeding finally stopped..."

    pause
    anon "Maybe it's not broken afterall."

    show debbies 31 at Position(xpos=484,ypos=768) with vpunch
    anon "{b}[deb_name]{/b}??"

    anon "Kenapa kamu-"

    show debbies 30
    debbie "Shhh, It's okay, Sweetie."

    debbie "Let me help you..."

    show debbies 34
    debbie "You deserve it, after what you did back there."

    show debbies 37_36
    pause 4
    show debbies 34
    debbie "How's your abdomen?"

    show debbies 35
    anon "Sore, but I think I'll live."

    show debbies 34
    debbie "When did you get so tough?"

    debbie "You really are a man now..."

    show debbies 36
    show debbies 76 with dissolve
    show debbies 41_76
    pause
    show debbies 42 with hpunch
    with dissolve
    debbie "Here sweetie, let me-"

    show debbies 72
    anon "Wah!!"

    anon "{b}[deb_name]{/b}, are you sure?"

    show debbies 43
    debbie "Yes, it's okay."

    debbie "Just let me take care of you..."

    show debbies 44
    debbie "You were so brave today, sweetheart!"

    show debbies 45 with dissolve
    debbie "I was so proud of you..."

    show debbies 74
    anon "... Ohh, that feels really good!"

    show debbies 73_74
    pause 4
    show debbies 73
    anon "{b}[deb_name]{/b}, I'm gonna..."

    show debbies 46
    debbie "It's okay, sweetie, just let it out!"

    show debbies 47 at Position(xpos=498,ypos=768)
    anon "HNNGGG!!!"

    show white zorder 4 with dissolve
    show debbies 47 at Position(xpos=498,ypos=768)
    show playersex 33 zorder 3 at Position(xpos=610,ypos=880)
    hide white with dissolve
    pause
    show debbies 48
    hide playersex
    with dissolve
    debbie "Wow, you had a lot in you..."

    show debbies 44 at Position(xpos=484,ypos=768) with dissolve
    debbie "Di sana."

    show debbies 34 at Position(xpos=447,ypos=768) with dissolve
    debbie "Doesn't that feel better?"

    show debbies 35 at Position(xpos=447,ypos=768)
    anon "So much better!"

    anon "... Thanks, {b}[deb_name]{/b}!"

    show debbies 34
    debbie "Now let's get you cleaned up."


    scene expression L_home_shower.background_blur
    show anon b_dressed_changing
    show old_debbie 35b at right
    with slowfade
    pause
    show anon b_dressed f_shy with dissolve
    show old_debbie 35c with dissolve
    pause
    show old_debbie 34 with dissolve
    anon "{b}[deb_name]{/b}, was this just a one-time thing?"

    show old_debbie 34
    debbie "..."
    show old_debbie 35
    debbie "Oh, sweetie... I don't know."

    show old_debbie 34
    debbie "..."
    show old_debbie 35
    debbie "I suppose, we can do it again."

    show anon f_grin
    show old_debbie 36
    debbie "But you can't tell {b}ANYBODY{/b} and we can't take things any further!"

    show anon f_normal
    show old_debbie 34
    debbie "..."
    show old_debbie 36
    debbie "And we {b}ABSOLUTELY CANNOT{/b} let {b}[jen_name]{/b} find out!"

    debbie "Do you {b}understand{/b}?"

    show old_debbie 34
    anon "I understand, {b}[deb_name]{/b}."

    show old_debbie 35
    debbie "Alright, I have to go and get dinner started."

    show old_debbie 36
    debbie "You wait a minute or two before coming out of the bathroom."

    debbie "We don't want {b}[jen_name]{/b} to suspect anything, yeah?"

    show old_debbie 32
    anon "O-okay, {b}[deb_name]{/b}."

    show old_debbie 33
    debbie "That's my boy."

    hide old_debbie with dissolve
    pause
    anon @ f_laugh "... Wah!"

    anon "That was totally worth a beating!"

    hide anon with dissolve
    call popup ('scene', 'deb_shower')
    return

label ano02_thug_home:
    $ playMusic("<loop 73.5>audio/music_villain.ogg", 1.0)
    scene location_home_entrance_frontdoor_cutscene
    show text _ ("When I opened the door, I was greeted not by a police lady\nbut instead a stern and ugly-looking thug all dressed in black.") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("His tattoos and demeanor just screamed bad news.") as caption with dissolve
    pause

    scene location_home_entrance_frontdoor_cutscene_closeup
    show text _ ("And his greasy smile sent chills up my spine.") as caption
    with fade
    pause

    $ player.go_to(L_home_entrance)
    scene location_home_entrance_frontdoor
    show anon f_surprised:
        xoffset -140
    show dimitri f_grin:
        xoffset -120
    with fade
    anon "!!!"
    pause
    anon f_worried "C-can I help you?"

    dimitri "Nice place."

    anon "Hmm..."

    anon "Thanks?"

    dimitri "Hmm, I am thinking you're {b}Frank{/b}'s son, yes?"

    anon "You knew my dad?"

    dimitri "Hehe."

    dimitri "Yes, you could say this..."

    anon @ -m_talk "..."
    dimitri "Where is nice lady who takes care of you?"

    anon "Uhh, she's..."

    pause
    anon f_confused "W-who are you?"

    dimitri @ f_normal "Who am I?"

    dimitri "I am man at door."

    show anon f_worried
    dimitri "I am man asking to see nice lady responsible for you..."

    dimitri "... Lady who owes us big money."

    anon @ f_surprised "Big money?"

    anon "L-look man, we don't know anything about any of this..."

    anon "I really think you've made a mistake or something."

    dimitri "Ahh, talking, talking..."

    dimitri "Your father like talking too, you know?"

    dimitri "He talk all the way to the end."

    dimitri f_normal a_talk "\"You make mistake.\""

    dimitri "\"I no take money!\""

    dimitri f_grin "Yip, yip, yip."

    dimitri a_idle "Like frightened little bunny."

    anon f_surprised "!!!"
    dimitri f_normal "{b}Boss{/b} wants no more talking."

    dimitri a_point "He wants money back!"

    dimitri "You tell nice lady to be smart and pay up."

    show dimitri a_idle with dissolve
    anon "saya..."

    anon "I think you should leave now."

    dimitri f_grin "Heh, so {i}this{/i} little bunny does have spine..."

    dimitri "I guess apple can fall far from tree."


    $ playMusic()
    scene location_home_entrance_frontdoor_cutscene_yumi
    show text _ ("It was at that moment {b}Harold{/b}'s partner, {b}Yumi{/b}, pulled up in her squad car.") as caption
    with fade
    pause

    scene location_home_entrance_frontdoor
    show dimitri:
        xoffset -120
    show anon f_worried:
        xoffset -140
    with fade
    dimitri "Tsk, Tsk, police involvement not so good for you..."

    pause
    dimitri f_grin "Not so good idea for nice lady either."

    anon @ -m_talk "..."
    dimitri f_normal a_point "You give her message."

    dimitri @ a_throat "You tell her I come back here and things will get ugly."

    dimitri "Ya?"

    anon @ -m_talk "..."
    show dimitri a_idle with dissolve
    yumi "B-permisi?"

    show dimitri f_grin
    show yumi f_suspicious a_cautious behind anon with dissolve:
        flip
        xoffset 100
    yumi "Who are you?"

    dimitri @ a_out "Aku?"

    dimitri "I am just old friend of family, come to pay respects."

    yumi "I'd like to ask you a few questions..."

    dimitri "Bah, I've no time for questions."

    dimitri "Much to do."

    dimitri @ a_stop "aku pergi sekarang."

    show dimitri a_sides with dissolve:
        flip
        xoffset 400
    yumi f_angry "Now you hold on just one second!"

    pause
    show dimitri a_out with dissolve:
        unflip
        xoffset -120
    dimitri "Oh, are you planning to arrest me, Officer?"

    yumi f_suspicious "N-no, but-"

    dimitri a_sides "Hmm, I did not think so..."

    show yumi f_angry
    pause
    show yumi behind dimitri
    dimitri a_point "See you soon, little bunny."

    hide dimitri with dissolve
    yumi @ -m_talk "..."
    pause
    yumi "Lock the door, kid."

    show anon a_reach with dissolve:
        xoffset 340

    scene expression player.location.background_blur
    show anon a_idle:
        flip
        xoffset 100
    show yumi a_idle f_exhale:
        flip
        xoffset 250
    with fade
    pause
    show yumi f_normal
    debbie "What's going on?!"

    show debbie f_sad with dissolve:
        flip
        xoffset -100
    show yumi with dissolve:
        unflip
        xoffset -300
    debbie "W-who was that?"

    yumi "Bad news, is who that was..."

    anon "Pretty sure it's the guy who's been threatening you on the phone."

    debbie f_surprised a_mouth_shock "!!!"
    yumi "I need to call this in."

    hide yumi with dissolve
    show debbie b_robe_hug_mc:
        xoffset 100
    show anon b_empty f_sad_down zorder 1
    with dissolve
    debbie "Oh my goodness, are you alright?!"

    debbie "He didn't try and hurt you, did he?"

    anon "N-no, I'm fine."

    show debbie b_robe a_front f_sad:
        xoffset 0
    show anon b_dressed f_worried
    with dissolve
    debbie "Apa yang dia katakan?"

    anon "He wanted money and... He..."

    anon f_sad_down "... Mentioned {b}Dad{/b}."

    debbie @ a_mouth_shock "Oh, sweetie!"

    anon "{b}[deb_name]{/b}, I think he had something to do with {b}Dad{/b}'s death."

    show debbie b_robe_hug_mc:
        xoffset 100
    show anon b_empty
    with dissolve
    debbie "Shh, it's okay... He's gone now."

    debbie "Everything is going to be alright."

    pause
    show debbie b_robe:
        xoffset 0
    show anon b_dressed f_worried
    with dissolve
    debbie "C'mon, let's go sit down in the living room and see what the police officer can tell us."

    anon "Y-ya, oke."

    hide debbie
    hide anon
    with dissolve

    $ player.go_to(L_home_livingroom)
    scene expression background(760, 400, 2.5) as stage
    show yumi a_phone f_concerned:
        xoffset -500
    with fade
    show debbie f_sad:
        xoffset 100
    show anon f_worried:
        flip
        xoffset -39
    with dissolve
    yumi "That's correct, sir."

    pause
    yumi f_angry "He can't have gone far."

    pause
    yumi f_suspicious "Apa?!"

    pause
    yumi "No, I don't understand, sir!"

    pause
    yumi "We can't just-"

    pause
    yumi f_concerned "Y-ya."

    pause
    yumi "{i}*Sigh*{/i} Yes, sir."

    pause
    yumi "Baiklah."

    show yumi a_phone_close
    pause
    debbie "What's happening?"

    show yumi a_idle f_normal with dissolve:
        flip
        xoffset 0
    anon "Yeah, shouldn't you be calling for backup or something?"

    yumi "We put out an APB to our patrolmen, they're looking for the car now."

    yumi "I need to get a statement from you..."

    debbie "A statement?"

    anon "You mean you're not going after that guy?!"

    yumi f_concerned "No, I've been expressly ordered not to pursue him."

    debbie @ -m_talk "..."
    anon "But he was making threats!"

    yumi "saya tahu..."

    yumi "... And I'm sorry."

    pause
    yumi "{i}*Sigh*{/i} Look, it's very important that you tell me exactly what he said to you."

    anon "Uhh, I'm not sure..."

    anon "Everything happened so fast."

    yumi "That's understandable."

    yumi "This is a very stressful situation."

    show debbie b_robe_hug_mc_behind
    show anon b_empty
    show anon_arms_dressed_a_sides_debbie_hug as anon_arms:
        xoffset 100
    with dissolve
    yumi "Let's just take a moment to breathe and calm down, alright?"

    anon @ f_smoke "Y-ya, oke."

    pause
    yumi f_down a_notes "Sangat bagus."

    yumi f_normal "Now I need you to focus, {b}[firstname]{/b}."

    anon @ -m_talk "Mmhmm."

    yumi "What did the man say to you when you opened the door?"

    anon "He said, \"Nice place.\""

    yumi @ f_down "Oke, bagus."

    yumi "Then what did he say?"

    anon "He said I looked like my father, and then he asked after {b}[deb_name]{/b}."

    yumi @ f_down "Bagus."

    yumi "What next?"

    anon "He said his boss was done talking."

    anon "A-and that they wanted their money back."

    debbie "Pfft, how can we give back something we never took?!"

    yumi "You said he mentioned his boss?"

    anon "Ya."

    yumi "Did he say a name?"

    anon f_sad_down "T-tidak."

    yumi "{i}*Huh*{/i} Baiklah."

    yumi "Ada lagi?"

    anon "Yeah, he said if we didn't pay up, he'd be back..."

    anon "... And that next time, things would get ugly."

    show debbie b_robe f_surprised a_mouth_shock
    show anon b_dressed
    hide anon_arms
    with dissolve
    debbie "!!!"
    yumi "Is that all he said?"

    anon f_worried "Saya kira demikian."

    show yumi a_idle with dissolve
    pause
    yumi "Thank you for your cooperation."

    debbie a_front f_sad "Are you going to tell us who that man was?!"

    yumi f_concerned "{i}*Sigh*{/i} Truthfully ma'am, we don't know who he is."

    yumi "All I can tell you is that he's part of a criminal organization that's recently set up shop here, in Summerville."

    debbie f_surprised "Criminal organization?!"

    yumi "We're still trying to get a grip on the situation; but for now, my best advice for you both is to remain calm and stay vigilant."

    yumi "If they call, just hang up."

    yumi "If anyone suspicious comes knocking on your door, do not answer and phone the police immediately."

    anon f_skeptical "That's your advice?!"

    yumi "Lay low and don't give them any incentive."

    yumi "I'm going to personally be monitoring your neighborhood while my partner {b}Harold{/b} gets to the bottom of all this, okay?"

    debbie @ -m_talk "..."
    anon f_worried "I don't like this."

    yumi "Everything is going to be fine."

    yumi "We'll keep you safe, I assure you."

    debbie f_sad @ -m_talk "..."
    yumi "Ma'am, can you help me set up a schedule?"

    debbie @ -m_talk "Hmm?"

    yumi "Just the overview of everyone's weekly routine?"

    debbie "Y-ya, tentu saja."

    yumi "Terima kasih."

    hide yumi
    hide debbie
    with dissolve
    pause
    show anon f_sad_down
    anon @ -m_talk "( I don't like this one bit. )"

    anon @ -m_talk "( {i}*Sigh*{/i} I need some air. )"

    hide anon with dissolve
    return

label ano02_warn_home:
    scene location_home_driveby_cutscene01
    show text _ ("Hmm, why is that car driving so slow?") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("Wait a second...") as caption with dissolve
    pause

    scene location_home_driveby_cutscene02
    show text _ ("It's that creepy guy with the strange accent who was making the threats!") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("This is bad!") as caption with dissolve
    pause

    scene expression background(584, 504, 3.0) as stage
    show anon f_surprised a_sides:
        xoffset 300
    with fade
    anon "I need to tell {b}[deb_name]{/b} about this!"

    anon "Sekarang!"

    hide anon with fastdissolve

    $ player.go_to(L_home_entrance)
    scene expression player.location.background_blur with fade
    show anon f_surprised a_sides with fastdissolve:
        flip
    anon "{b}[deb_name]{/b}!"

    pause
    anon a_behind_head "Where are you?!"

    show debbie f_sad with {'master': fastdissolve}:
        flip
    debbie "Sweetie?!"

    debbie "Ada apa?"

    anon a_sides "I just saw that guy again!"

    debbie f_surprised a_mouth_shock "Y-you did?"

    debbie "Where?!"

    anon f_worried @ a_point_back "He and another guy just drove by in a black car."

    debbie f_sad a_idle "Did they say anything to you?"

    anon "No, they just kept on driving."

    anon "He was staring right at me though!"

    debbie "I think we'd better stay inside the house for a while..."

    debbie "... I'll go phone the police."

    anon "Y-ya, oke."

    hide debbie with dissolve
    pause
    anon f_angry @ -m_talk "( I'm getting really sick of these assholes. )"

    hide anon with dissolve

    $ player.go_to(L_home_kitchen)
    scene expression player.location.background_blur
    show debbie a_phone f_sad
    with fade
    debbie "Yes, just now."

    pause
    show anon f_worried with dissolve:
        xoffset 200
    debbie "No, they didn't stop."

    pause
    debbie "B-baiklah."

    pause
    debbie "Terima kasih."

    show debbie a_phone_down
    pause
    anon "What did they say?"

    debbie "{b}Yumi{/b} is on her way over."

    anon "Have they made any progress?"

    debbie "She didn't say."

    anon f_unimpressed @ a_facepalm "Of course she didn't."

    anon "You know, I'm starting the think the cops in this town are pretty useless..."

    debbie "Don't say that, sweetie."

    show anon f_worried
    debbie "They're doing their best."

    show jenny f_upset with dissolve:
        flip
        xoffset -100
    anon "Yeah, a lot of good that's doing us."

    show anon f_worried_left
    jenny "Sekarang apa yang terjadi?"

    jenny "Those creepy guys come by again?"

    anon "Ya."

    show anon f_worried
    debbie "I'm sure it's nothing, dear..."

    debbie "The police are on their way, everything is going to be fine."

    debbie "We just need to stay inside for a while."

    show anon f_worried_left
    jenny "Are they going to actually do something this time?"

    show anon f_worried
    debbie "Don't you start too."

    pause
    debbie "Why don't you take {b}[firstname]{/b} upstairs and play a board game or something?"

    show anon f_worried_left
    jenny f_gross "Eugh, you must be joking..."

    show anon f_worried
    debbie "No, I think it would be good if you two spent some time together bonding."

    show anon f_worried_left
    jenny f_upset @ f_eyeroll "First of all, we're not little kids... we don't play board games."

    anon f_confused_back "You don't want to play a board game?"

    anon f_normal_left "I'd play a board game."

    jenny @ a_facepalm "{i}*Sigh*{/i} Secondly, I'd rather coat my labia in honey and sit on an anthill."

    show anon f_thinking
    debbie f_angry "{b}[jen_name]{/b}!"

    anon f_flirt_left "That was oddly specific."

    show anon f_normal
    show jenny f_sexy
    debbie "... And disgusting."

    show anon f_normal_left
    jenny "Maybe, but it's true."

    jenny f_upset "I'm going upstairs to watch a movie."

    hide jenny with dissolve
    jenny "Don't bother me!"

    pause
    show anon f_normal
    debbie f_normal "Well, you can wait here with me if you'd like?"

    debbie "I'll cook you something."

    anon "Nah, that's okay {b}[deb_name]{/b}."

    anon "I'll just head to my room and catch up on some homework or something."

    debbie "Oh, that's a good idea!"

    show debbie b_robe_hug_mc:
        xoffset 200
    show anon b_empty
    with dissolve
    debbie "You're such a good boy!"

    anon "Y-yeah, thanks {b}[deb_name]{/b}."

    show debbie b_robe a_front:
        xoffset 0
    show anon b_dressed
    with dissolve
    debbie "I'll whip you up something to snack on!"

    anon "Sounds great."


    scene location_home_bedroom_cutscene_study_01
    show text _ ("I had a literal mountain of homework piled up from the time I missed at school...") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("... But try as I might, I just couldn't get anything accomplished.") as caption with dissolve
    pause

    scene intro_04
    show text _ ("I was too worried to focus.") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("How had my dad managed to get us into this mess?!") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("What in the world could I do to get us out of it?") as caption with dissolve
    pause

    $ player.go_to(L_home_bedroom)
    scene expression player.location.background_blur
    show debbie f_sad:
        flip
    with fade
    debbie "Sayang?"

    debbie "It's awfully quiet in here..."

    show anon f_worried with dissolve:
        flip
    anon "Are the police still downstairs?"

    debbie "No, {b}Yumi{/b} just left."

    debbie "They've got patrols out looking for that car again."

    anon @ f_sad_down "Ya, bagus."

    pause
    show debbie with dissolve:
        xoffset 100
    debbie "Are you doing okay?"

    anon "Ehh, I'm fine."

    debbie "Anda yakin?"

    debbie "I hope you know you can talk to me... if you need to?"

    anon "Y-ya, aku tahu."

    pause
    anon "aku hanya-"

    anon "I'm worried something bad might happen and..."

    anon "... I want to be able to protect you and {b}[jen_name]{/b}, you know."

    show debbie b_robe_hug1
    hide anon
    with dissolve
    debbie "Ahh, sweetie."

    debbie "It's not your responsibility to protect us."

    debbie "You've got enough worries, just being the age you are..."

    debbie "... Getting through school..."

    debbie "... Finding a nice girlfriend..."

    show anon f_worried:
        flip
    show debbie b_robe f_sad
    with dissolve
    debbie "You should focus on things like that, you know?"

    anon "I'm not sure I can do that, {b}[deb_name]{/b}."

    debbie f_normal "Tsk, of course you can!"

    debbie "All this other stuff... it's for me to solve, not you."

    debbie "It's my responsibility."

    debbie "You hear me?"

    anon "Ya."

    anon "B-but I don't think-"

    show debbie b_robe_hug1
    hide anon
    with dissolve
    debbie "No buts!"

    debbie "I'm gonna take care of it, okay?"

    debbie "Everything is going to be fine."

    show anon f_worried:
        flip
    show debbie b_robe
    with dissolve
    pause
    debbie "Why don't you get out of the house for a while and do something fun?"

    debbie "Go see what new games {b}Erik{/b} is playing?"

    anon @ -m_talk "..."
    debbie "Maybe spend some time with that cute girl next door?"

    anon f_shy a_behind_head "{b}[deb_name]{/b}..."

    debbie @ f_laugh "Hehe, or you could always go {b}help Diane with her garden{/b}."

    anon a_idle "{i}*Sigh*{/i} Yeah, alright."

    debbie "That's my boy!"

    hide anon with dissolve
    show debbie with dissolve:
        unflip
        xoffset -300
    debbie "Get your mind off all this nonsense!"

    pause
    debbie f_sad a_nervous "I'll handle everything."

    show debbie f_sad_closed a_facepalm with dissolve
    pause

    $ player.go_to(L_map)
    scene expression player.location.background_blur with fade
    anon "( {b}[deb_name]{/b} is right, it doesn't do any good to sit around worrying about this stuff. )"

    anon "( Best I get my mind off it. )"

    anon "( I've got the whole town full of adventures in front of me. )"

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
