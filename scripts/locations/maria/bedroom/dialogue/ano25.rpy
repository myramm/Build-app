label ano25_find_duffel:
    scene expression background(512, 400, 4) as stage
    show anon b_dressed_pickup with dissolve:
        xoffset -300
        xzoom -1
    anon @ -m_talk "( Hmm, is this it? )"

    anon a_duffel b_dressed f_looking_down @ -m_talk "( I thought {b}Tony{/b} said it would be in the closet?! )"

    show anon f_thinking
    pause
    anon @ -m_talk "( Heh, I guess they couldn't make it fit. )"

    anon @ -m_talk "( Maybe after the tech update when the game is in 1080p widescreen? )"

    show anon f_looking_down
    pause
    show anon f_normal with {'master': dissolve}:
        xoffset 200
        xzoom 1
    anon @ -m_talk "( This is definitely the bag. Time to go! )"

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
