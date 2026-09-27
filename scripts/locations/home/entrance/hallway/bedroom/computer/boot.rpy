label anon_computer:
    if game.timer.is_night():
        call bedroom_anon_too_tired
    elif game.rails():
        call bedroom_anon_no_time
    else:
        call pc ('anon')
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
