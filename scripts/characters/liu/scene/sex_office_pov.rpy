label scene_liu_sex_office_pov:

    return


label scene_liu_sex_office_pov.loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 3:
        if anim_toggle:
            if not animated:
                show liu_sex_printer_front_anim as animation with dissolve
                $ animated = True
            pause 5
            call scene_liu_sex_office.dialogue
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8,9,10,11]
            $ poses_done = []
            while poses_done != pose_list:
                show expression 'liu_sex_printer_front_anim {}'.format(pose_list[pose_counter]) as animation
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call scene_liu_sex_office.dialogue
        $ animcounter += 1
    call screen scene_liu_sex_office_controls(angle='pov')
    if not _return:
        jump scene_liu_sex_office_pov.loop
    return _return


label scene_liu_sex_office_pov.switch:
    scene location_bank_office_printer_sex_front
    show liu_sex_printer_front_anim as animation
    with fade
    jump scene_liu_sex_office_pov.repeat


label scene_liu_sex_office_pov.repeat:
    call scene_liu_sex_office_pov.loop
    if _return == 'switch':
        jump scene_liu_sex_office.switch
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
