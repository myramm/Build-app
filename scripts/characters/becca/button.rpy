label becca_button_dialogue:
    call becca_button_stage

    if M_becca.is_state(S_bec01_talk) and L_tina_bed2.is_here(M_becca):
        call bec01_talk_becca
        $ M_becca.trigger(T_bec01_talk)

    elif L_tina_bed2.is_here(M_becca):
        call becca_button_bedroom

    if _return == 'afterglow':
        $ player.go_to(L_apt_hall3)
        $ game.timer.tick()

    $ game.main()
    return


label becca_button_stage:
    if L_tina_bed2.is_here(M_becca):
        scene location_tina_becca_bedroom_bed
        show becca b_home_bed_read f_normal_down
        show becca_overlay_o_books as books
    else:
        scene expression player.location.background_blur
        show becca
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
