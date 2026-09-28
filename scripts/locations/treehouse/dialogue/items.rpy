label treehouse_dink_dialogue:
    scene expression background(160, 616, 6) as stage
    show erik_overlay_o_boat as boat:
        xzoom -1
    show erik_overlay_o_boat_tarp as tarp:
        xzoom -1
    show anon f_shy_low behind boat with dissolve:
        xoffset -200
        xzoom -1
    anon @ -m_talk "( This is the old boat my dad and I used to take fishing when I was little. )"
    anon @ -m_talk "( \"The Dink.\" )"
    pause
    anon @ -m_talk "( Brings back a lot of good memories... )"
    pause
    anon f_thinking_down @ -m_talk "( ... Maybe I should see about fixing it up sometime? )"
    anon f_shy_down @ -m_talk "( Get it seaworthy again! )"
    pause
    anon f_grin @ -m_talk "( Who knows, I might even take my own son fishing in it one day? )"
    hide anon with dissolve
    return


label treehouse_window_dialogue:
    scene black

    if game.timer.is_day() and L_rump_back.is_here(M_rump):
        scene location_rump_backyard_spy_default_rump_day with fastdissolve
        anon "!!!"
        scene black with {'master': eyeshut}
        anon "Nope! Nope-nope-nope-nope-nope!"
    else:

        scene expression game.timer.image('location_rump_backyard_spy_default') with dissolve
        anon "Guess there's no one around at the moment..."
        scene black with dissolve

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
