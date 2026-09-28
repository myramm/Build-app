label rump_button_hottub:
    $ renpy.dynamic(stage=background(840, 408, 2.85, b=.6))

    scene expression stage as stage:
        align (.5, .5)
        offset (-60, 100)
        zoom 1.75
    show rump b_jacuzzi f_smirk:
        yoffset 0
    show location_rump_backyard_jacuzzi_overlay_evening as hottub:
        offset (-205, -220)
        zoom 1.4
    show anon b_telescope_peeking_caught with dissolve:
        offset (-580, 140)
        zoom 1.4
    rump "Nuh uh, I'm not taking no for an answer!"
    pause
    rump "Well, of course Bill's gonna be there..."
    rump "You think he'd miss a chance to party with the {b}Rump{/b}-meister?!"
    pause
    rump "Yeah, I can get us some blow."
    pause
    rump @ -m_talk "Mhmm."
    rump "Not a problem!"
    pause
    rump @ f_normal "Yeah, the girls are Russian."
    pause
    rump "Nah, they're real docile."
    rump "And eager to please, you better believe it!"
    pause
    rump "You just make sure you bring Michelle with you."
    rump "{b}Melonia{/b} loves her."
    rump "Plus, I'm dying to see her in a bikini!"
    pause
    rump @ f_laugh "Heh, you dog you!"
    show rump f_suspicious_down
    pause
    rump f_normal "Excuse me one second."
    rump a_phone_down f_angry "Hey, you!"
    anon f_surprised @ -m_talk "Hmm?"
    rump "This is a private conversation!"
    show layer master:
        linear .9 yoffset 155
    show expression stage as stage:
        linear .9 offset (0, 0) zoom 1.55
    show location_rump_backyard_jacuzzi_overlay_evening as hottubback behind rump:
        offset (-205, -220)
        zoom 1.4
        linear .9 offset (0, -15) zoom 1.
    show rump:
        linear .9 xoffset 100
    show location_rump_backyard_jacuzzi_overlay_evening as hottub:
        linear .9 offset (0, 0) zoom 1.
    show anon b_dressed_pickup with dissolve:
        offset (-200, -80)
        zoom 1.1
    pause .2
    show anon a_point_self b_dressed f_surprised_low with dissolve:
        offset (-100, -155)
        zoom 1.
    anon "Oh, I didn't mean to-"
    rump "Get the hell out of here before I call security!"
    anon a_wave "Y-yes, sir!"
    hide anon with fastdissolve

    scene expression background(400, 392, 5.) as stage with fade
    show anon f_surprised a_sides with dissolve
    anon @ -m_talk "( That was close! )"
    anon @ -m_talk "( I should probably keep my distance from him for now. )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
