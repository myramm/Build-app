label yacht_cabin_nuke_dialogue:
    scene expression background(880, 336, 3.4) as stage
    show anon f_worried_low with dissolve
    anon @ -m_talk "( Hmm, what a weird thing to have next to a bed... )"

    anon @ -m_talk "( I wonder what this button does? )"

    show anon a_thinking with dissolve

    menu:
        "Push it.":
            jump yacht_cabin_nuke_dialogue.push
        "Leave it be.":

            pass

    anon a_idle f_worried_low @ -m_talk "( Hmm, I probably shouldn't be pushing unmarked big red buttons... )"

    anon @ -m_talk "( Best to just leave it alone. )"

    anon f_laugh @ -m_talk "( Curiosity killed the cat after all. )"

    hide anon with dissolve
    return


label yacht_cabin_nuke_dialogue.push:
    anon a_point f_laugh @ -m_talk "( How could anyone resist pushing a big red button? )"


    scene expression game.timer.image('backgrounds/location_boat_cutscene01{}.jpg')
    show text _ ("{i}*Click*{/i}\n\n") as caption
    with fade
    pause
    pause
    show text _ ("{i}*Click*{/i}\n\n{i}Whoosh!{/i}") as caption with dissolve
    pause

    scene expression background(880, 336, 3.4) as stage
    show anon f_shock
    anon @ -m_talk "!!!" with hpunch
    anon f_worried @ -m_talk "( What the heck was that?! )"


    scene expression game.timer.image('backgrounds/location_boat_cutscene02{}.jpg')
    show text _ ("{i}...{/i}") as caption
    with fade
    pause

    scene expression background(880, 336, 3.4) as stage
    show anon f_surprised_forward
    with fastfade
    pause
    anon f_surprised "Oops..."

    anon @ f_worried -m_talk "( Ehh, I should probably get out of here... )"

    anon @ -m_talk "( Like, right now! )"

    hide anon with dissolve
    return True
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
