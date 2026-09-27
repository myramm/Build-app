label eriks_basement_backroom_dialogue:
    $ game.main()


label mrsj_afterpoker_fun:
    scene erik_basement_back_c
    show mrsjsex 1 at left
    with dissolve
    mrsj "I was wondering what was taking you two so long!"

    show mrsjsex 3
    erik "Sorry, {b}Mrs. Johnson{/b}."

    show mrsjsex 1
    mrsj "I thought you two didn't want to spend time with me..."

    show mrsjsex 2
    player_name "Of course we do."

    show mrsjsex 1
    mrsj "I see you both can't help staring at me."

    mrsj "Would you boys like to... Touch me?"

    show mrsjsex 2
    player_name "We can?"

    show mrsjsex 3
    erik "Are you sure, {b}Mrs. Johnson{/b}?"

    show mrsjsex 1
    mrsj "Why don't you give it try?"

    show mrsjsex 4 with fastdissolve
    pause
    show mrsjsex 5
    mrsj "Haha!"

    show mrsjsex 6
    mrsj "That's all?"

    mrsj "You two must be shy!"

    show mrsjsex 7 with fastdissolve
    mrsj "Maybe you just need a little encouragement..."

    show mrsjsex 8_9 with fastdissolve
    pause 8
    show mrsjsex 10 with fastdissolve
    mrsj "Oh my!"

    mrsj "Someone is excited..."

    show mrsjsex 11
    mrsj "... And wants more."

    show mrsjsex 12 with fastdissolve
    pause
    show mrsjsex 13_14_13_12
    pause 7.5
    show mrsjsex 12b_13b_14b
    mrsj "I could use some help, boys!"

    mrsj "Why don't you suck on my nipples, {b}[firstname]{/b}..."

    mrsj "... {b}Erik{/b} already knows what to do."

    show mrsjsex 15_16_17
    $ anim_toggle = True
    $ animated = False
    $ xray = False

    label mrsj_afterpoker_fun_repeat:
    show mrsjsex 17
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    if anim_toggle:
        show mrsjsex 15_16_17 at left
        pause 8
    else:
        $ animcounter = 0
        while animcounter < 3:
            show mrsjsex 15
            pause
            show mrsjsex 16
            pause
            show mrsjsex 17
            pause
            $ animcounter += 1
    show mrsjsex 17
    menu:
        "Terus berlanjut.":
            jump mrsj_afterpoker_fun_repeat
        "Make her cum.":

            show mrsjsex 15_16_17 at left
            pause 8
            show mrsjsex 18
            mrsj "Ahhh!!!" with hpunch
            show mrsjsex 19 with fastdissolve
            mrsj "Goodness me!"

            mrsj "That was well done, boys..."

            mrsj "I feel like you two wanted more..."

            mrsj "I... I think we should stop... For tonight, at least."


            $ player.go_to(L_erikhouse_basement)
            scene expression player.location.background_blur
            show player 1f at Position(xpos=756)
            show old_erik 1 at Position(xpos=876)
            show mrsj 28f at left
            with fade
            mrsj "Alright boys! I think this is enough for tonight..."

            mrsj "I have to get up early tomorrow."

            show mrsj 27f at Position(xoffset=-1)
            show old_erik 5
            erik "Sorry for keeping you up, {b}Mrs. Johnson{/b}..."

            show mrsj 28f
            show old_erik 1
            mrsj "It's fineee! I enjoyed our little night."

            show mrsj 27f at Position(xoffset=-1)
            show player 14f
            player_name "Thanks for playing with us, {b}Mrs. Johnson{/b}."

            show mrsj 28f
            show player 1f
            mrsj "It was my pleasure, playing with... With each other."

            show mrsj 34 at center
            hide old_erik
            hide player
            with dissolve
            mrsj "You boys let me know if you need someone to play with again..."

            show mrsj 35
            player_name "Sure thing, {b}Mrs. Johnson{/b}..."

            player_name "I better get home, goodnight!"

            $ renpy.end_replay()
            $ persistent.cookie_jar["Mrs Johnson"]["unlocked"] = True
            $ persistent.cookie_jar["Mrs Johnson"]["gallery"]["01_unlocked"] = True
            $ M_mrsj.set('poker_after_party', False)
            $ M_erik.trigger(T_erik_poker_fun)

    jump resume_sleeping_bedroom
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
