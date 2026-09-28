label jenny_dining_room_sex_intro:
    show anon f_worried
    show jenny f_grin
    jenny "Shh!!"
    show anon f_surprised_teeth_down with None
    show debbie b_breakfast_mug f_normal
    with dissolve
    debbie "Did you say something, dear?"
    jenny "Would you make me some breakfast?"
    show anon f_shy_down
    debbie "You want me to cook for you?"
    jenny "Yes."
    debbie "Well, of course I will, dear!"
    debbie "I always worry about you not getting enough to eat-"
    show debbie f_sad
    show jenny f_eyeroll
    jenny "Yeah, I know {b}[deb_name]{/b}... You tell me all the time!"
    show jenny f_upset
    debbie "R-right... Umm..."
    show anon f_looking_down_eating a_eating with dissolve
    debbie f_normal "I'll whip you up some eggs and bacon right now!"
    show anon f_looking_down_food a_resting with dissolve
    show jenny f_grin
    jenny "Thanks."
    debbie "It'll just be a few minutes, dear."
    show anon f_surprised_high_food with None
    show expression "characters/xtra/overlay_o_dinner_mug.png"
    hide debbie
    with dissolve
    show jenny f_laugh a_laugh with dissolve
    jenny "Hehe..."
    show jenny b_breakfast_gettingup f_grin_down with dissolve
    pause
    show jenny b_breakfast_remove with dissolve
    if M_jenny.get("first_sex_dining"):
        $ M_jenny.set("first_sex_dining", False)
        show anon f_worried_high
        anon "Okay, so now wha-"
        show jenny b_breakfast_leaning f_grin with dissolve
        show anon f_surprised_teeth_left
        anon "!!!"
        if M_jenny.get("dominance") <= 0:
            anon f_worried "W-we can't-"
            show jenny f_upset
            jenny "{i}*Sigh*{/i} Well, not if you're going to be a little bitch about it..."
            show jenny b_breakfast_remove with dissolve
            pause
            show jenny b_breakfast_gettingup with dissolve
            jenny "... And here I thought you were finally starting to grow a backbone."
            anon "Fine!"
            show jenny b_breakfast_remove with dissolve
            anon "Let's just hurry, okay?"
            show jenny b_breakfast_leaning f_grin with dissolve
            jenny "Yeah, yeah... Get your cock out already!"
        else:
            anon f_worried "Are you out of your mind?!"
            show jenny b_breakfast_standing_panties_down a_hips f_sexy_down with dissolve
            jenny "C'mon, {b}[firstname]{/b}... You know you want to."
            anon "{i}*Sigh*{/i} Fine."
            jenny "You'd better hurry up, we only have a few minutes..."
            anon "Just shut up and get back down there!"
            show jenny b_breakfast_leaning f_laugh with dissolve
            jenny "Hehehe!"
            show jenny f_grin
    else:
        anon f_worried "Why can't we just go upstairs?!"
        show jenny f_grin b_breakfast_leaning with dissolve
        jenny "Just shut up and fuck me, {b}[firstname]{/b}!"
        anon f_tired "{i}*Sigh*{/i}"
        scene black with fade
        pause

label jenny_dining_room_sex_pre_insert:
    scene expression "backgrounds/location_home_diningroom_sex.jpg"
    show jenny_sex_table b_default f_back
    show player_jenny_diningroom_sex pre
    with fade
    anon "Just don't get too loud..."
    show jenny_sex_table f_back_talk
    jenny "Oh, please... I'm pretty sure I can control my-"
    hide jenny_sex_table
    hide player_jenny_diningroom_sex
    show jenny_diningroom_sex insert
    with dissolve
    pause 1
    show jenny_diningroom_sex 1
    jenny "SELF!!!" with hpunch
    $ animated = True
    $ anim_toggle = True
    $ M_jenny.set('sex speed', .12)
    show expression AnimatedImage("jenny_diningroom_sex", [1,2,3,4,5,6,7,8,9], M_jenny) as jenny_diningroom_sex at Position(xalign = 0.0, yoffset = 0) with dissolve
    jenny "Oh, fuuuck!"
    anon "Shhh!!!"
    jenny "Ngghhh!"
    pause
    jenny "Holy-"
    jenny "!!!"
    anon "You have to be quiet or I'm going to stop!"
    jenny "Don't you dare fucking stop!"
    pause
    anon "You're squeezing me too tight!"
    jenny "I can't help it, this is really turning me on!"
    pause
    debbie "{b}[jen_name]{/b}?!"
    hide jenny_diningroom_sex
    show jenny_sex_table b_default f_surprised
    show player_jenny_diningroom_sex pre
    with dissolve
    anon "!!!" with hpunch
    jenny "!!!"
    show jenny_sex_table f_angry_talk
    jenny "Y-yes?"
    show jenny_sex_table f_angry
    debbie "Do you want your eggs scrambled or over easy?"
    show jenny_sex_table f_angry_talk
    jenny "Oh, umm... Scrambled is fine!"
    hide jenny_sex_table
    hide player_jenny_diningroom_sex
    show expression AnimatedImage("jenny_diningroom_sex", [1,2,3,4,5,6,7,8,9], M_jenny) as jenny_diningroom_sex at Position(xalign = 0.0, yoffset = 0) with hpunch
    debbie "Okay, dear."
    jenny "Hurry up, {b}[firstname]{/b}!"
    pause
    anon "I'm getting close."
    jenny "Me too!"

label jenny_diningroom_sex_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("jenny_diningroom_sex", [1,2,3,4,5,6,7,8,9], M_jenny) as jenny_diningroom_sex at Position(xalign = 0.0, yoffset = 0)
                $ animated = True
            pause 5
            call expression game.dialog_select("jenny_diningroom_sex_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8,9]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "jenny_diningroom_sex {}".format(pose_list[pose_counter]) as jenny_diningroom_sex at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("jenny_diningroom_sex_hscene_dialog")
        $ animcounter += 1
    call screen jenny_diningroom_sex_options

label jenny_diningroom_sex_hscene_dialog:
    if animcounter == 0 and randomizer() < 10:
        jenny "Ahh!!{p=1}{nw}"
    if animcounter == 1 and randomizer() < 10:
        jenny "It's so good!{p=1}{nw}"
    if animcounter == 2 and randomizer() < 10:
        jenny "FUUUUUCK!!!{p=1}{nw}"
    if animcounter == 3 and randomizer() < 10:
        anon "Uhh!{p=1}{nw}"
    return

label jenny_diningroom_sex_cum_inside:
    anon "Here it comes!"
    jenny "Don't stop!!"
    show jenny_diningroom_sex cum
    anon "HNNGGG!!!" with flash
    show jenny_diningroom_sex cum2
    show xray_jenny_diningroom_table:
        align (0,0)
    jenny "NGGHHH!!!"
    hide xray_jenny_diningroom_table
    pause
    show jenny_diningroom_sex 1 with dissolve
    anon "Haah... Haah..."
    jenny "Holy shit..."
    anon "Yeah..."
    jenny "Get off me."
    hide jenny_diningroom_sex
    show jenny_sex_table b_default f_angry
    show player_jenny_diningroom_sex after
    with dissolve
    pause
    call call_pregnancy_minigame ("jenny_diningroom_sex_cum_inside_post_pregnancy", M_jenny)

label jenny_diningroom_sex_cum_inside_post_pregnancy:
    scene expression game.timer.image("dining_room{}")
    show jenny b_breakfast_standing_panties_down a_cum2 f_upset_down zorder 1
    show anon b_dinner_sitting_look_left f_shy_down zorder 0
    show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
    show expression "characters/xtra/overlay_o_dinner_mug.png" zorder 2
    with fade
    jenny "Goddamnit, {b}[firstname]{/b}!"
    jenny "If I get pregnant I'm going to kill you!"
    show jenny a_cum1 with dissolve
    show anon f_flirt_left
    anon "You told me not to stop..."
    show jenny f_gross_down
    jenny "Yeah, but I didn't tell you to cum inside me, did I?"
    anon @ -m_talk "..."
    jenny "Fucking moron..."
    anon f_worried "Shut up!"
    debbie "Okay, who's hungry?!"
    show anon f_surprised
    show jenny f_surprised
    jenny "!!!" with hpunch
    show jenny b_breakfast_remove with dissolve
    pause
    show jenny b_breakfast_dressed a_spoon f_upset_down with dissolve
    show anon f_normal_high with None
    show debbie b_breakfast_potatoes f_normal zorder 1
    with dissolve
    debbie "Two eggs scrambled and three strips of bacon, just like you wanted."
    show jenny f_normal
    jenny "T-thanks, {b}[deb_name]{/b}."
    show anon f_shy_down
    debbie "You're welcome dear!"
    hide expression "characters/xtra/overlay_o_dinner_mug.png"
    show debbie b_breakfast_sitting a_mug
    with dissolve
    pause
    debbie "{b}[firstname]{/b}, you look tired..."
    debbie "Are you feeling okay, sweetie?"
    show anon f_surprised
    anon @ -m_talk "Hmm?"
    jenny "He's fine."
    anon b_dinner_sitting f_normal "Yeah, I feel fine."
    debbie "Alright, just make sure you're getting enough rest, okay?"
    anon "O-okay."
    show anon f_shy_down
    show debbie a_mug_drink f_kiss with dissolve
    pause
    show debbie f_sad a_mug with dissolve
    debbie "Mmm, does it smell weird in here?"
    anon f_worried "N-no?"
    show debbie f_normal
    jenny "I don't smell anything."
    debbie "Hmm, something smells funny..."
    show jenny f_laugh a_phone with dissolve
    anon "Y-yeah, I dunno {b}[deb_name]{/b}..."
    jenny "Hehehe!"
    hide anon with dissolve
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["15_unlocked"] = True
    $ game.timer.tick()
    $ player.go_to(L_home_diningroom)
    $ game.main()

label jenny_diningroom_sex_cum_outside:
    anon "Here it comes!"
    jenny "Don't stop!!"
    hide jenny_diningroom_sex
    show jenny_sex_table b_default f_angry
    show player_jenny_diningroom_sex after
    with dissolve
    pause
    scene expression game.timer.image("dining_room{}")
    show jenny b_breakfast_standing_panties_down a_hips f_gross_down zorder 1
    show anon b_dinner_standing_cumming f_surprised_teeth_down zorder 0
    show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
    with fade
    jenny "What the fuck, {b}[firstname]{/b}?!"
    show anon f_brag
    anon @ -m_talk "HNNGGG!!!" with flash
    jenny "I told you not to stop!"
    show anon f_surprised_teeth_down
    pause
    show anon b_dinner_sitting_look_left f_tired zorder 0
    show expression "characters/xtra/overlay_o_dinner_mug.png" zorder 2
    with dissolve
    anon "Haah... Haah..."
    anon f_worried "What do you want me to do, {b}[jen_name]{/b}?!"
    anon "Am I supposed to cum inside you?!"
    show jenny b_breakfast_remove with dissolve
    pause
    show jenny b_breakfast_dressed a_spoon f_upset with dissolve
    jenny "N-no..."
    jenny "{i}*Sigh*{/i} It just would have been nice to finish, asshole!"
    anon "Shut up!"
    debbie "Okay, who's hungry?!"
    show anon f_surprised
    show jenny f_surprised
    jenny "!!!" with hpunch
    show anon f_normal_high with None
    show debbie b_breakfast_potatoes f_normal zorder 1
    with dissolve
    debbie "Two eggs scrambled and three strips of bacon, just like you wanted."
    show jenny f_normal
    jenny "T-thanks, {b}[deb_name]{/b}."
    show anon f_shy_down
    debbie "You're welcome dear!"
    hide expression "characters/xtra/overlay_o_dinner_mug.png"
    show debbie b_breakfast_sitting a_mug
    with dissolve
    pause
    debbie "{b}[firstname]{/b}, you look tired..."
    debbie "Are you feeling okay, sweetie?"
    show anon f_surprised
    anon @ -m_talk "Hmm?"
    jenny "He's fine."
    anon b_dinner_sitting f_normal "Yeah, I feel fine."
    debbie "Alright, just make sure you're getting enough rest, okay?"
    anon "O-okay."
    show anon f_surprised
    show jenny f_surprised
    show debbie a_mug_drink f_kiss with dissolve
    anon "W-wait-"
    pause
    show jenny f_laugh
    show debbie f_gross a_mug with dissolve
    debbie "Eugh, this coffee tastes awful!"
    anon f_worried "R-really?"
    debbie "Yeah!"
    jenny "{i}*Snort*{/i}"
    show jenny f_grin
    debbie "I don't understand, it tasted fine a few minutes ago..."
    anon "W-weird..."
    anon "You should probably dump it out and get a new cup."
    debbie "Yeah, I think so too."
    debbie "Yuck!"
    show jenny f_laugh
    jenny "Hehehe!"
    hide anon with dissolve
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["15_unlocked"] = True
    $ game.timer.tick()
    $ player.go_to(L_home_diningroom)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
