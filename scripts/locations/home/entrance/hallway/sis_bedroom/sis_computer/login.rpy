label pc_hook_login_jenny:
    if not M_jenny.finished_state(S_jenny_snoop_around_for_laptop):
        call expression game.dialog_select("jenny_computer_password_unknown")
        $ game.main()

    if M_jenny.is_state(S_jenny_check_laptop) and game.timer.is_dark():
        call expression game.dialog_select("jenny_computer_password_unknown")
        $ game.main()

    if M_jenny.is_state(S_jenny_check_laptop) and game.timer.is_day():
        call expression game.dialog_select("jenny_computer_password_caught")
        $ game.main()

    return

label jenny_computer_password_unknown:
    anon "( It's password locked... )"
    anon "( I should try to figure out the password first. )"
    anon "( Maybe she left some kind of clue around )"
    return

label jenny_computer_password_caught:
    anon "( I need her password! )"
    $ renpy.scene(layer='screens')
    scene expression player.location.background_blur with None
    show player 4 with dissolve
    pause
    player_name "( \"My favorite toy...\" )"
    player_name "( Didn't she mention something about a toy in {b}her diary{/b}? )"
    jenny "{b}[deb_name]{/b}, have you seen my hair straightener?!"
    show player 22 with dissolve
    player_name "( Oh crap, it sounds like {b}[jen_name]{/b} is done with her shower! )"
    debbie "No, sweetie."
    jenny "Well, I can't find it!"
    player_name "( I'd better get out of here! )"
    hide player with dissolve
    $ player.go_to(L_home_hallway)
    scene expression player.location.background_blur with None
    show player 11 at left
    show jenny b_towel a_hips f_upset
    with dissolve
    jenny "Did you just come out of my room?!"
    show jenny f_upset
    show player 10
    player_name "Huh?"
    player_name "No..."
    show player 5
    show jenny f_angry
    pause
    show player 6 with dissolve
    player_name "Please don't hit me with the hair dryer again!"
    show jenny f_eyeroll
    jenny "Ugh, just get out of my way, loser!"
    hide jenny with dissolve
    pause
    show player 37 with dissolve
    player_name "( Phew, that was close! )"
    pause
    show player 5 with dissolve
    player_name "( Who knows how long it will take me to find naughty stuff on {b}her laptop{/b}... )"
    player_name "( I should only attempt this when I know I'll have plenty of time to snoop around. )"
    pause
    show player 4 with dissolve
    player_name "( Maybe {b}at night{/b}, when {b}she's sleeping{/b}? )"
    pause
    show player 17 with dissolve
    player_name "( I'll have to be careful but I think it's worth a shot. )"
    hide player with dissolve
    $ game.timer.tick()
    $ player.go_to(L_home_hallway)
    $ M_jenny.trigger(T_jenny_return_from_shower)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
