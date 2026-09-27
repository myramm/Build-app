label warn:
    return


label warn.migrate:
    scene expression background(l=L_beach_water, t=2)
    show screen popup_migrate() with dissolve
    pause
    hide screen popup_migrate with dissolve
    return


label warn.recovery:
    scene expression background(l=L_waterfall, t=3)
    show screen popup_recovery() with dissolve
    pause
    hide screen popup_recovery with dissolve
    show text _ ('LOADING') at Transform(align=(.5, .7), zoom=1.2) with dissolve
    return


label warn.rollback:
    scene expression background(l=L_tina_lounge, t=1) with dissolve
    show screen popup_rollback() with dissolve
    pause
    hide screen popup_rollback with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
