label jenny_computer:
    if L_home_sisbedroom.is_here(M_jenny) and not game.timer.is_night():
        call expression game.dialog_select("jenny_bedroom_cannot_snoop")

    elif M_jenny.is_state(S_jenny_figure_out_password) and game.timer.is_day():
        call siscomp_day
        $ player.go_to(L_home_hallway)
        $ game._in_shower = None
    else:

        call pc ('jenny')

    $ game.main()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
