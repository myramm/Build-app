label yumi_button_dialogue:
    call yumi_button_stage

    if L_home.is_here(M_yumi):
        call yumi_button_driveway
    else:

        call yumi_police_basement_button_dialogue

    $ game.main()
    return


label yumi_button_stage:
    if L_home.is_here(M_yumi):
        scene expression background(400, 520, 5.5) as stage
        show expression im.Blur(game.timer.image('objects/object_car_police{}.png'), .5) as car:
            offset (-1688, 109)
            zoom 5.5
    else:
        scene expression player.location.background_blur
        show yumi
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
