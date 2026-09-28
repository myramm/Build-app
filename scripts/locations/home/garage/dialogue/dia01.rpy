label dia01_find_home_garage_shovel:
    scene expression background(780, 420, 2.5) as stage
    show anon f_shy_low a_shovel with dissolve
    anon "Yeah, this should work!"
    anon "It'll be nice to have some money for a change..."
    jenny "{i}*Ahem*{/i}"
    anon f_surprised_teeth "!!!" with hpunch
    show jenny f_upset a_crossed with dissolve
    jenny "What are you doing with that shovel?"
    anon f_worried "... Huh?"
    anon f_normal "Oh! I'm taking it to {b}Diane{/b}'s house."
    anon "I'm going to be working for her this summer."
    jenny "{b}Diane{/b} gave you a job?"
    jenny "... She's never offered me any work!"
    anon a_idle "Well, it's physical labor in her garden."
    anon "She probably just assumed you wouldn't be interested..."
    jenny f_eyeroll "Ugh, in this heat?"
    jenny f_upset "Yeah, no way. Screw that!"
    anon f_worried "What are you doing in the garage?"
    anon "You never come out here..."
    jenny f_normal a_hips "I need some batteries. Don't we still have some out here?"
    show anon f_thinking a_thinking with dissolve
    pause
    anon a_idle f_normal "Yeah, I think so."
    anon @ a_point "Try that box on bottom shelf there."
    pause
    show jenny b_bend with dissolve:
        flip
        offset (200, 10)
    anon f_surprised_low "!!!"
    pause
    show jenny b_bend_down with dissolve
    pause
    show jenny a_hips_battery f_upset b_dressed with dissolve:
        unflip
        offset (0, 0)
    anon f_skeptical "Holy crap, what do you need so many for?"
    jenny "None of your business, loser!"
    jenny "Just take your shovel and beat it."
    anon "Tch, whatever."
    jenny f_grin "Have fun busting your ass for {b}Diane{/b}..."
    jenny f_laugh "Hahaha!"
    hide jenny with dissolve
    anon "... She's such a bitch."
    anon @ -m_talk "( {i}*Sigh*{/i} Alright, well... I've got a shovel for {b}Diane{/b} now. )"
    anon f_laugh "( Time to {b}head back to her place and start gardening{/b}. )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
