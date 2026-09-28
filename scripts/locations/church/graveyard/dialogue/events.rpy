label church_graveyard_wake:
    scene black
    pause
    anon "Ngh."
    pause

    scene location_graveyard_wakeup_cutscene01 with sliteyeopen
    pause
    anon "Ugh, man..."
    anon "... Not again."

    scene black with sliteyeshut
    pause 0.25

    scene location_graveyard_wakeup_cutscene03 with wideeyeopen
    pause

    scene location_graveyard_wakeup_cutscene04 with dissolve
    pause

    scene location_graveyard_ground_day
    show anon b_laying_ground f_worried
    with dissolve
    pause
    anon f_worried_left "Why do I keep waking up here?"
    pause
    anon f_skeptical "Did last night really happen or did I imagine it again?"
    anon f_worried "This is all very confusing..."

    scene black with fade
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
