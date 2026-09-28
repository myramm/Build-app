label mar01_tour_maria_bedroom:
    scene expression background(728, 400, 3.5) as stage
    show anon f_normal_high with dissolve:
        flip
    anon "Whoa."
    anon "Look at all the stars..."
    pause
    show anon with {'master': dissolve}:
        unflip
        xoffset 350
    anon "Where did you get this night light?"
    maria "You like it?"
    anon f_normal "Yeah, it's beautiful."
    show anon f_normal_high with {'master': dissolve}:
        flip
        xoffset -350
    maria "{b}Tony{/b} set all that up for the baby."
    pause
    anon f_laugh @ -m_talk "( Wow, {b}Tony{/b} sure is gonna be a great dad... )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
