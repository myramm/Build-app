label mel01_init_rump_master:
    scene expression background(200, 384, 5.) as stage
    show anon with dissolve
    pause
    show anon f_worried
    show melonia f_annoyed
    with dissolve
    melonia "Where the hell have you been?"
    anon f_surprised a_sides "Excuse me?"
    melonia "I waited around all morning for my hot tub to get cleaned and you never showed!"
    anon f_worried "Oh, was I-"
    melonia @ f_yell "{b}Ricky{/b} had to do it!"
    anon f_surprised_teeth @ f_surprised a_up "I'm sorry, I-"
    melonia "No, no... I don't wanna hear your excuses!"
    melonia @ a_point "Get it done tomorrow or you can find yourself another job!"
    anon "Y-yes, ma'am."
    melonia @ f_yell a_fired "Now get out!"
    hide anon with fastdissolve

    scene expression background(l=L_rump_lobby) with fade
    show anon f_surprised with dissolve
    anon @ -m_talk "( Holy crap! )"
    anon @ -m_talk "( That lady has anger issues... )"
    pause
    anon f_sad_down @ -m_talk "( I'd better show up to {b}clean that hot tub{/b} tomorrow morning or I could lose my access to this place. )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
