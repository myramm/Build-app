label mrs_johnsons_room_dialogue:
    if not L_erikhouse_mrsjroom.is_here(M_mrsj):
        pass

    elif M_erik.is_state(S_erik_feed_curious, S_erik_feed_search):
        call expression game.dialog_select("mrsjsroom_erik_feed_found")
        $ M_erik.trigger(T_erik_feed_found)
        $ game.timer.tick()
        $ player.go_to(L_erikhouse)

    elif M_erik.is_state(S_erik_learn_acquired):
        call mrsjsroom_erik_learn_prep
        $ M_erik.trigger(T_erik_learn_report)
        $ player.remove_item('kamasutra')
        $ player.remove_item('birth_control_pills')
        $ player.go_to(L_erikhouse_entrance)

    $ game.main()

label mrsj_ball:
    scene expression game.timer.image("mrsj_ball{}")
    call popup ('alpha')
    $ game.main()

label mrsj_private_yoga:
    if _in_replay:
        scene erik_upstairs_night_c2
        call expression game.dialog_select("mrsjroom_mrsj_private_yoga_intro")
    $ game.timer.tick()
    $ player.go_to(L_erikhouse_entrance)
    $ M_mrsj.set('sex speed', .4)
    $ anim_toggle = True
    $ animated = False
    $ xray = False

    label mrsj_private_yoga_pos1_repeat:
        hide screen erimom_private_pos1_sex_options
        show screen sex_anim_buttons
        pause
        hide screen sex_anim_buttons
        if anim_toggle:
            show mrsjsex 36_37
            pause 8
        else:

            $ animcounter = 0
            while animcounter < 4:
                show mrsjsex 36 at Position(yoffset=70)
                pause
                show mrsjsex 37 at Position(yoffset=60)
                pause
                $ animcounter += 1

        show screen erimom_private_pos1_sex_options
        pause
        jump mrsj_private_yoga_pos1_repeat

        label erimom_private_pos1_switch:
            hide screen erimom_private_pos1_sex_options
            $ M_mrsj.set('sex speed', .3)
            call expression game.dialog_select("mrsjroom_mrsj_private_yoga_pos1")
            $ anim_toggle = True
            $ animated = False

            label mrsj_private_yoga_pos2_repeat:
                hide screen erimom_private_pos2_sex_options
                show screen sex_anim_buttons
                pause
                hide screen sex_anim_buttons
                if anim_toggle:
                    show mrsjsex 42_43_44_45_46 at Position(xpos=580,ypos=710)
                    pause 8
                else:

                    $ animcounter = 0
                    while animcounter < 4:
                        show mrsjsex 42 at Position(xoffset=-14)
                        pause
                        show mrsjsex 43 at Position(xoffset=-20)
                        pause
                        show mrsjsex 44 at Position(xoffset=-30)
                        pause
                        show mrsjsex 45 at Position(xoffset=-23)
                        pause
                        show mrsjsex 46 at Position(xoffset=-19)
                        pause
                        $ animcounter += 1

                show screen erimom_private_pos2_sex_options
                pause
                jump mrsj_private_yoga_pos2_repeat

                label erimom_private_pos2_cum:
                    call expression game.dialog_select("mrsjroom_mrsj_private_yoga_pos2")
                    $ renpy.end_replay()
                    $ persistent.cookie_jar["Mrs Johnson"]["unlocked"] = True
                    $ persistent.cookie_jar["Mrs Johnson"]["gallery"]["05_unlocked"] = True
    $ game.main()

label mrsj_3some:
    scene erik_upstairs_night_c
    $ game.timer.tick()
    $ player.go_to(L_erikhouse_entrance)
    $ M_erik.trigger(T_erik_learn_threesome)
    call expression game.dialog_select("mrsjroom_mrsj_3some_intro")
    $ anim_toggle = True
    $ animated = False
    $ xray = False
    $ M_mrsj.set('sex speed', .4)

    label mrsj_3some_pos1_repeat:
        hide screen mrsj_3some_pos1_sex_options
        show screen sex_anim_buttons
        pause
        hide screen sex_anim_buttons
        if anim_toggle:
            show mrsjsex 21_22_23_24_25 at topright
            pause 8
        else:

            $ animcounter = 0
            while animcounter < 4:
                show mrsjsex 21
                pause
                show mrsjsex 22
                pause
                show mrsjsex 23
                pause
                show mrsjsex 24
                pause
                show mrsjsex 25
                pause
                $ animcounter += 1

        show screen mrsj_3some_pos1_sex_options
        pause
        jump mrsj_3some_pos1_repeat

        label mrsj_3some_pos1_switch:
            hide screen mrsj_3some_pos1_sex_options
            $ M_mrsj.set('sex speed', .3)
            call expression game.dialog_select("mrsjroom_mrsj_3some_pos1")
            $ anim_toggle = True
            $ animated = False

            label mrsj_3some_pos2_repeat:
                hide screen mrsj_3some_pos2_sex_options
                show screen sex_anim_buttons
                pause
                hide screen sex_anim_buttons
                if anim_toggle:
                    show mrsjsex 28_29_30 at Position(xanchor=0,xpos=200,ypos=100)
                    pause 8
                else:

                    $ animcounter = 0
                    while animcounter < 4:
                        show mrsjsex 28 at Position(yoffset=42)
                        pause
                        show mrsjsex 29 at Position(yoffset=36)
                        pause
                        show mrsjsex 30 at Position(xoffset=-4,yoffset=41)
                        pause
                        $ animcounter += 1

                show screen mrsj_3some_pos2_sex_options
                pause
                jump mrsj_3some_pos2_repeat

                label mrsj_3some_pos2_cum:
                    call expression game.dialog_select("mrsjroom_mrsj_3some_pos2")
                    $ renpy.end_replay()
                    $ persistent.cookie_jar["Mrs Johnson"]["unlocked"] = True
                    $ persistent.cookie_jar["Mrs Johnson"]["gallery"]["04_unlocked"] = True
    $ game.main()

label erimom_private_pos1_faster_sex:
    $ M_mrsj.set('sex speed', M_mrsj.get('sex speed') - 0.1)
    jump mrsj_private_yoga_pos1_repeat

label erimom_private_pos1_slower_sex:
    $ M_mrsj.set('sex speed', M_mrsj.get('sex speed') + 0.1)
    jump mrsj_private_yoga_pos1_repeat

label erimom_private_pos2_faster_sex:
    $ M_mrsj.set('sex speed', M_mrsj.get('sex speed') - 0.1)
    jump mrsj_private_yoga_pos2_repeat

label erimom_private_pos2_slower_sex:
    $ M_mrsj.set('sex speed', M_mrsj.get('sex speed') + 0.1)
    jump mrsj_private_yoga_pos2_repeat

label mrsj_3some_pos1_faster_sex:
    $ M_mrsj.set('sex speed', M_mrsj.get('sex speed') - 0.1)
    jump mrsj_3some_pos1_repeat

label mrsj_3some_pos1_slower_sex:
    $ M_mrsj.set('sex speed', M_mrsj.get('sex speed') + 0.1)
    jump mrsj_3some_pos1_repeat

label mrsj_3some_pos2_faster_sex:
    $ M_mrsj.set('sex speed', M_mrsj.get('sex speed') - 0.1)
    jump mrsj_3some_pos2_repeat

label mrsj_3some_pos2_slower_sex:
    $ M_mrsj.set('sex speed', M_mrsj.get('sex speed') + 0.1)
    jump mrsj_3some_pos2_repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
