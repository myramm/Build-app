label pc_hook_camslut:
    if not M_jenny.once('pc_hook_camslut'):
        anon "( Here it is. )"
        pause
        anon "( Ugh, her profile is awful... )"
        anon "( Twenty-four-year-old goddess? Haha! )"
        pause
        anon "( Oh, there's a videos tab! )"
    return


label pc_hook_camslut_vids:
    if not M_jenny.once('pc_hook_camslut_vids'):
        anon "( She's got two videos saved here! )"
        pause
        anon "( I can't watch these in her room though... She might wake up! )"
        pause
        anon "( Maybe there's some way to {b}connect her computer to mine{/b}? )"
        pause
        anon "( Hmmm... I think I remember reading something about this. )"
        if not game.timer.is_day():
            anon "( If I just... Hold the command key... And tap break... )"
            hide screen pc
            jump hacking_minigame_pre
        else:
            anon "( Pretty sure I just had to hold the command key and tap break or something. )"
            anon "( I can't do that now though, {b}[jen_name]{/b} could come in any minute! )"
            anon "( Maybe I should try it later when there's more time. )"

    elif pc.system == 'jenny' and game.timer.is_dark():
        anon "( I can't watch those in her room... She might wake up! )"
        call pc_hack_attempt

    elif M_jenny.is_state(S_jenny_check_for_new_video):
        anon "( Dang it! )"
        pause
        anon "( Not a single new video... )"
        pause
        anon "( It says she was online yesterday... I wonder why she's not saving her new shows? )"
        $ M_jenny.trigger(T_jenny_checked_pc_for_new_vids)
        hide screen pc
        jump bedroom_dialogue

    elif M_jenny.is_state(S_jenny_video_3_uploaded):
        anon "( It worked, she saved a new video! )"

    return


label pc_hook_camshow(video):
    if pc.system == 'jenny':
        if game.timer.is_day():
            anon "( I can't do that when {b}[jen_name]{/b} can come in any minute! )"
        else:
            anon "( I can't watch that here! She might wake up! )"
            call pc_hack_attempt
        return

    if not (M_jenny.get("watched_video_ec") or M_jenny.get("watched_video_uv")):
        anon "( Nice! )"
        anon "( Now let's check out those videos! )"

    hide screen pc
    call expression game.dialog_select("jenny_computer_video_{}".format(video))
    $ M_jenny.set("watched_video_{}".format(video), True)

    if M_jenny.get("watched_video_ec") and M_jenny.get("watched_video_uv") and M_jenny.is_state(S_jenny_figure_out_password):
        scene expression player.location.background_blur with None
        show player 5
        anon "( A real penis? )"
        anon "( Is she talking about fucking someone on camera?! )"
        anon "( Surely she wouldn't go that far, would she? )"
        pause
        show player 403
        anon "( Man, I hope she makes more videos! )"
        hide player with dissolve
        $ M_jenny.trigger(T_jenny_a_real_penis)
        $ game.main()

    if M_jenny.is_state(S_jenny_video_3_uploaded):
        $ M_jenny.trigger(T_jenny_checked_new_vid)

    show screen pc_desktop
    return


label pc_hack_attempt:
    if not M_jenny.get('pc_hacked'):
        if M_jenny.get('pc_hack_attempted'):
            anon "( I know, I'll try to set up remote access again. )"
        else:
            anon "( I know, I'll try to set up remote access. )"
        hide screen pc
        jump hacking_minigame_pre
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
