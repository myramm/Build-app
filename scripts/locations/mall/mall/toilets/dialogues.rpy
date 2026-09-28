label mall_toilets_rump_n_cunt:
    scene mall_toilets_event_b
    player_name "( A body guard? )"
    player_name "( What is he doing in here... )"
    return

label mall_toilets_stall:
    scene expression player.location.background_blur
    show player 1 at left with dissolve
    player_name "( Nothing in here... Just some crusty stains on the walls. )"
    hide player with dissolve
    return

label rump_toilets_stall:
    call expression game.dialog_select("rump_toilets_stall_dialogue")
    $ renpy.end_replay()
    $ persistent.cookie_jar["Rump"]["unlocked"] = True
    $ persistent.cookie_jar["Rump"]["gallery"]["01_unlocked"] = True
    $ A_rump_n_pump.unlock()
    call screen button(Image = "boxes/auto_option_generic_02", Label = "rump_toilets_stall_block")

label rump_toilets_stall_dialogue:
    scene expression player.location.background_blur
    show rump_overlay zorder 3
    show rump_n_cunt 01_02_03_04 zorder 2 at left
    with fade
    $ renpy.pause(1, hard=True)
    rump "YES!"
    $ renpy.pause(1, hard=True)
    rump "YOU NASTY WOMAN!!!"
    $ renpy.pause(1, hard=True)
    return

label rump_toilets_stall_block:
    $ player.go_to(L_mall_toilets)
    call expression game.dialog_select("rump_toilets_stall_block_dialogue")
    $ game.timer.tick()
    $ M_rump.set('rump_n_cunt', False)
    $ player.go_to(L_mall_parking_lot if game.timer.is_night() else L_mall)
    $ game.main()

label rump_toilets_stall_block_dialogue:
    scene location_mall_washroom_event_blur with fade
    show player 37 at left with dissolve
    player_name "( ... )"
    show player 38
    player_name "( Was that {b}Mayor Rump{/b}?! )"
    scene expression player.location.background_blur
    show player 22 at left
    show bodyguard
    with hpunch
    player_name "!!!"
    bodyguard a_stop f_suspicious "Hey!"
    bodyguard "No one is allowed in here!"
    bodyguard "I need you to leave right NOW!!!"
    show bodyguard a_ear with dissolve
    scene black with fade
    return

label rump_hscene_replay:
    $ player.go_to(L_mall_toilets_stall)
    jump rump_toilets_stall
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
