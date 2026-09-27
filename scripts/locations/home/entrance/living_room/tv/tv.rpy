label television:
    if M_debbie.is_set("movie night") or M_debbie.is_state(S_debbie_romance_movie,
                                                             S_debbie_romance_movie_two):
        jump mom_movie_night
    elif game.timer.is_night():
        call tv_tired
    elif not game.timer.is_dark():
        call tv_daytime
    else:
        call tv (0, True)
    $ game.main()


label tv(chan=0, power=True):
    scene location_home_tv_night
    show screen tv(chan)
    if not power:
        with None
    call tv_on (chan, power)
    while True:
        call screen empty()
        label tv.pre:
        python hide:
            try:
                _return is True and renpy.jump('tv.quit')
                renpy.run(_return)
            except renpy.game.JumpException as e:
                renpy.scene(layer='screens')
                raise
    label tv.quit:
    call tv_off (power)
    return


label tv_on(chan, power=False):
    $ renpy.dynamic(mono=chan)
    if chan == 7:
        if tv_authed:
            show tv_channel_09 as prg at tv
        else:
            show tv_channel_08 as prg at tv
            show screen tv_auth()
    elif chan == 1 and M_kim.state == 'jailed' and game.timer.random('tv', tick=True) > .5:
        $ mono = 'rump_cellmate'
        show tv_channel_12 as prg at tv
    elif chan == 1 and M_rump.state == 'jailed' and L_police_basement.is_here(M_rump):
        $ mono = 'rump_arrest'
        show tv_channel_11 as prg at tv
    elif chan == 3 and M_anon.finished_state(S_ano20_cops):
        $ mono = 'rump_jumpsuit'
        show tv_channel_04b as prg at tv
    else:
        show expression 'buttons/tv_channel_0' + str(chan + 1) + '.png' as prg at tv
    if not power:
        show tv_channum str (chan).zfill(2) as channum at tv_channum
        with tv_switch
    call tv_commentary (mono, 'tv_chan_' + str(mono))
    return


label tv_off(power=False):
    hide prg
    hide screen tv_auth
    hide channum
    if not power:
        with tv_switch
    return


label tv_switch(chan):
    call tv_off
    call tv_on (chan)
    return

label tv_auth():
    $ tv_authed = True
    hide prg
    hide screen tv_auth
    with tv_switch
    show expression 'buttons/tv_channel_09.png' as prg at tv
    with tv_switch
    call tv_auth_pass
    call tv_commentary (7, 'tv_chan_7')
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
