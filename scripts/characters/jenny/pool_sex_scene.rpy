label jenny_pool_sex_intro:
    scene expression "backgrounds/location_home_backyard_pool_sex.jpg"
    show jenny_pool_sex pre
    show jenny_pool_sex_face normal_talk_down
    show overlay_o_water zorder 100
    with fade
    jenny "Just make sure you keep your head down, I don't want {b}[deb_name]{/b} to see us!"
    show jenny_pool_sex_face normal_down
    anon "I will!"
    show jenny_pool_sex insert with dissolve
    anon "Wow, this feels weird in the water..."
    show jenny_pool_sex_face normal_talk_down
    jenny "Shut up and get down lower, dummy!"
    show jenny_pool_sex_face normal_down
    anon "I can't go lower, the water is-"
    hide jenny_pool_sex_face normal_down
    show jenny_pool_sex 1
    anon "!!!" with hpunch
    $ M_jenny.set('pool_clothes', True)
    $ animated = True
    $ anim_toggle = True
    $ M_jenny.set('sex speed', .12)
    show expression AnimatedImage("jenny_pool_sex", [1,2,3,4,5,6,7,8,9,10], M_jenny) as jenny_pool_sex at Position(xalign = 0.0, yoffset = 0) with dissolve
    pause
    jenny "Mmm, fuck!"
    anon "Stop, you're pushing me under!"
    jenny "Shh!!"
    anon "{i}*Bllgggh*{/i}"
    pause
    anon "{b}[jen_name]{/b} you're goin-"
    anon "{i}*Bllgghhrrghhh*{/i}"
    jenny "Stop making so much noise!"
    anon "You're drowning me!"
    jenny "Oh, I am not you big baby!"
    pause
    anon "{i}*Bllggh*{/i}"
    anon "{i}*Cough* *Cough*{/i}"
    jenny "Mm, I love this big dick... So much!!"
    pause
    jenny "C'mon, fuck me faster, {b}[firstname]{/b}!"
    anon "I'm trying!"
    pause
    jenny "Holy fuck!!"
    jenny "I'm going to cum!"
    anon "Me to-"

label jenny_pool_sex_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                if M_jenny.get('pool_clothes'):
                    show expression AnimatedImage("jenny_pool_sex", [1,2,3,4,5,6,7,8,9,10], M_jenny) as jenny_pool_sex at Position(xalign = 0.0, yoffset = 0)
                else:
                    show expression AnimatedImage("jenny_pool_sex_naked", [1,2,3,4,5,6,7,8,9,10], M_jenny) as jenny_pool_sex at Position(xalign = 0.0, yoffset = 0)
                $ animated = True
            pause 5
            call expression game.dialog_select("jenny_pool_sex_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8,9,10]
            $ poses_done = []
            while poses_done != pose_list:
                if M_jenny.get('pool_clothes'):
                    show expression "jenny_pool_sex {}".format(pose_list[pose_counter]) as jenny_pool_sex at Position(xalign = 0.0, yoffset = 0)
                else:
                    show expression "jenny_pool_sex_naked {}".format(pose_list[pose_counter]) as jenny_pool_sex at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("jenny_pool_sex_hscene_dialog")
        $ animcounter += 1
    call screen jenny_pool_sex_options

label jenny_pool_sex_hscene_dialog:
    if animcounter == 0 and randomizer() < 10:
        jenny "Ahh!!{p=1}{nw}"
        anon "{i}*Blghrghhh*{/i}!!!{p=1}{nw}"
    if animcounter == 1 and randomizer() < 10:
        anon "{i}*Bllgggh*{/i}{p=1}{nw}"
        jenny "It's so deep!{p=1}{nw}"
        jenny "Oh, fuck me!{p=1}{nw}"
    if animcounter == 2 and randomizer() < 10:
        jenny "FUUUUUCK!!!{p=1}{nw}"
    if animcounter == 3 and randomizer() < 10:
        anon "{i}*Bllgghhrrghhh*{/i}{p=1}{nw}"
    return

label jenny_pool_sex_cum_inside:
    jenny "Ohmygod, ohmygod, OHMYGOD!!"
    jenny "Don't stop!!"
    jenny "NGGHHH!!!"
    show jenny_pool_sex cum
    anon "HNNGGG!!!" with flash
    show jenny_pool_sex cum2
    show xray_jenny_pool:
        align (0,0)
    pause
    hide xray_jenny_pool
    show jenny_pool_sex pullout1
    show jenny_pool_sex_face normal_down
    with dissolve
    pause
    show jenny_pool_sex after
    show jenny_pool_sex_face normal_talk_down
    show player_jenny_pool pullout2
    with dissolve
    jenny "Haah... Haah..."
    jenny "That was awesome!"
    call call_pregnancy_minigame ("jenny_pool_sex_cum_inside_post_pregnancy", M_jenny)

label jenny_pool_sex_cum_inside_post_pregnancy:
    scene expression "backgrounds/location_home_backyard_pool_day_closeup.jpg"
    show anon f_tired b_pool
    show jenny b_pool f_upset_down
    with fade
    anon "I think I'm going to pass out..."
    show jenny f_angry
    jenny "Did you cum in me?!"
    anon "I don't even know, {b}[jen_name]{/b}... My life was flashing before my eyes!"
    show jenny f_eyeroll
    jenny "Oh, quit being so dramatic..."
    show jenny f_angry
    jenny "I swear, if I get pregnant, I'm gonna kill you!"
    anon "{b}[jen_name]{/b}, I can't even-"
    anon "I need to go lay down or something..."
    hide anon with dissolve
    pause
    show jenny f_angry
    jenny "Put your pants on before you go inside, moron!"
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["16_unlocked"] = True
    $ player.go_to(L_home_bedroom)
    $ game.timer.tick()
    $ game.main()

label jenny_pool_sex_cum_outside:
    jenny "Ohmygod, ohmygod, OHMYGOD!!"
    jenny "Don't stop!!"
    jenny "NGGHHH!!!"
    show jenny_pool_sex pullout1
    show jenny_pool_sex_face normal_down
    with dissolve
    pause
    show jenny_pool_sex after
    show jenny_pool_sex_face normal_down
    show player_jenny_pool flying_cum
    anon "HNNGGG!!!" with flash
    show player_jenny_pool pullout3 with dissolve
    pause
    show jenny_pool_sex_face normal_talk_down
    jenny "Haah... Haah..."
    jenny "That was awesome!"
    scene expression "backgrounds/location_home_backyard_pool_day_closeup.jpg"
    show anon f_tired b_pool
    show jenny b_pool f_upset_down
    with fade
    anon "I think I'm going to pass out..."
    show jenny f_gross
    jenny "Eww, your cum is floating all around me!"
    anon "Y-yeah, sorry... My life was flashing before my eyes!"
    jenny "Oh, quit being so dramatic..."
    jenny "I'm the one marinating in your ball juice over here!"
    anon "{b}[jen_name]{/b}, I can't even-"
    anon "I need to go lay down or something..."
    hide anon with dissolve
    pause
    show jenny f_gross
    jenny "Put your pants on before you go inside, moron!"
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["16_unlocked"] = True
    $ player.go_to(L_home_bedroom)
    $ game.timer.tick()
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
