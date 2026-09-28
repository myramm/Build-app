label scene_roz_sex:
    scene location_hospital_sex
    show old_roz 16 at right
    show player 24 at Position(xpos=.25,ypos=1.0)
    with fade
    if M_roz.is_state(S_roz_obits_collect):
        call roz02_roz_sex_intro
    else:
        call scene_roz_sex.intro
    $ anim_toggle = True
    $ animated = True
    $ M_roz.set("sex speed", .175)
    scene location_hospital_sex
    show expression AnimatedImage("rozs", [1,2,3,4,5,6,7], M_roz) as rozs at right
    with dissolve
    roz "That's it kid, nice and deep."
    pause
    roz "Oh Yeeaah..."
    pause
    roz "Don't you worry about pullin' out neither."
    roz "None of the plumbing works anymore and I like the feel of it inside."
    $ M_roz.set("sex speed", .125)
    roz "That's it, just like that."
    pause
    roz "C'mon kid, harder!"
    $ M_roz.set("sex speed", .075)
    jump scene_roz_sex.loop

label scene_roz_sex.intro:
    pause
    show old_roz 17 with dissolve
    pause
    show old_roz 18 with dissolve
    pause
    show player 80 with dissolve
    pause
    show old_roz 19
    roz "Why don't you get that monster out and so we can get started."
    show player 83
    show old_roz 18
    player_name "Yes, ma'am!"
    show player 480 at Position(xpos=.35,ypos=1.0) with dissolve
    pause
    show old_roz 19
    roz "Kid, you really got a great one."
    show old_roz 18
    show player 482
    pause
    show old_roz 19
    roz "Don't you be forgettin' to finish inside now..."
    show old_roz 18
    show player 481
    player_name "Y-yes ma'am!"
    show player 483 at Position (xpos=.36,ypos=1.0)
    show old_roz 19
    with dissolve
    roz "That's a good boy..."
    return

label scene_roz_sex.loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("rozs", [1,2,3,4,5,6,7], M_roz) as rozs at right
                $ animated = True
            pause 5
            call scene_roz_sex.dialogue
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "rozs {}".format(pose_list[pose_counter]) as rozs at right
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call scene_roz_sex.dialogue
        $ animcounter += 1
    call screen scene_roz_sex_options

label scene_roz_sex.dialogue:
    if animcounter == 1 and randomizer() > 50:
        roz "Ahhhh!!!{p=1}{nw}"
    elif animcounter == 3 and randomizer() > 50:
        roz "Oh!!!{p=1}{nw}"
        player_name "Uhhh...{p=1}{nw}"
    return

label scene_roz_sex.finish:
    player_name "{b}Roz{/b}, I can't hold out... M-much longer."
    roz "Finish inside me!"
    pause
    roz "Oh goodness!!!"
    show rozs 8_9 with flash
    player_name "UHHH!!"
    roz "AAAAHHH!!!!"
    pause
    hide rozs
    show player 482 zorder 2 at Position(xpos = .36, ypos = 1.0)
    show old_roz 18 zorder 1 at right
    show rozs 144 zorder 3 at Position(xpos = .5155, ypos = .895)
    show players 143 zorder 4 at Position(xpos = .435, ypos = .8625)
    with dissolve
    pause
    show old_roz 19
    roz "{i}*Wheeze*{/i} ... Whew."
    roz "Dear me... {i}*Cough*{/i} That was really good, {b}[firstname]{/b}!"
    show old_roz 18
    show player 481
    player_name "Y-yeah..."
    show player 482
    show old_roz 19
    roz "Just give me a moment... To catch my breath."
    show old_roz 18
    pause
    return


label roz02_roz_sex_intro:
    pause
    show old_roz 17 with dissolve
    pause
    show old_roz 18 with dissolve
    pause
    show player 78 with dissolve
    pause
    show old_roz 19
    roz "Heh, I still got it."
    show player 80
    show old_roz 18
    with dissolve
    pause
    show old_roz 19
    roz "What's the hold up?"
    show old_roz 18
    show player 83
    player_name "Oh man..."
    show player 480 at Position(xpos=.35,ypos=1.0) with dissolve
    pause
    show old_roz 19
    roz "Phew wee! What a monster!"
    show old_roz 18
    show player 482
    pause
    show old_roz 19
    roz "I knew this was a good idea!"
    show old_roz 18
    pause
    show old_roz 19
    roz "Now get over here and give ole {b}Roz{/b} what she's been missin'."
    show old_roz 18
    show player 481
    player_name "O-okay!"
    show player 483 at Position (xpos=.36,ypos=1.0)
    show old_roz 19
    with dissolve
    roz "That's a good boy..."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
