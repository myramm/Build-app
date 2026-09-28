label kim_button_dialogue:
    call kim_button_stage

    if M_anon.is_state(S_ano05_prat):
        call ano05_prat_kim
        $ M_anon.trigger(T_ano05_prat)

    elif M_josie.is_state(S_jos01_find) and not M_josie.once('jos01_kim'):
        call jos01_find_kim

    elif L_dealership_showroom.is_here(M_kim):
        call kim_button_showroom

    elif L_dealership_lounge.is_here(M_kim):
        call kim_button_lounge
    else:

        kim "I swear that's the last straw!"
        kim "I'm telling my agent I don't care how well it pays, I'm done playing these stereotypes!"
        kim "I grew up in Minnesota and have BA from Juilliard for God's sake!"

    $ game.main()
    return


label kim_button_stage:
    if L_dealership_showroom.is_here(M_kim):
        if L_dealership_showroom.is_here(M_josie):
            scene expression background(856, 464, 4.5) as stage
            show kim f_disgusted
        else:
            scene expression background(608, 512, 3.8) as stage
            show kim f_disgusted
            show xtra3 as counter at right

    elif L_dealership_lounge.is_here(M_kim):
        scene expression background(272, 376, 3.) as stage
        show kim:
            yoffset 150
    elif L_dealership_garage.is_here(M_kim):
        scene expression background(896, 488, 4.) as stage
        show kim
    else:
        scene expression player.location.background_blur as stage
        show kim
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
