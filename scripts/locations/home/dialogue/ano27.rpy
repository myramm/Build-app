label ano27_home_home:
    scene expression player.location.background_blur
    show anon f_surprised a_sides with dissolve
    pause
    anon @ -m_talk "( What the- )"
    anon @ -m_talk "( Why is the door open? )"
    pause
    anon @ -m_talk "( That's strange... )"
    hide anon with dissolve
    return


label ano27_yumi_police_cruiser:
    scene expression background(400, 520, 5.5) as stage
    show expression im.Blur(game.timer.image('objects/object_car_police_empty{}.png'), .5) as car:
        offset (-1688, 109)
        zoom 5.5
    show anon a_sides f_worried with dissolve:
        flip
        xoffset -200
    anon @ -m_talk "( Where's {b}Yumi{/b} gone? )"
    anon @ -m_talk "( Something's wrong, I can feel it. )"
    hide anon with dissolve
    return


label ano27_tony_police_cruiser:
    scene expression background(400, 520, 5.5) as stage
    show expression im.Blur(game.timer.image('objects/object_car_police_empty{}.png'), .5) as car:
        offset (-1688, 109)
        zoom 5.5
    show anon a_sides f_worried with dissolve:
        flip
        xoffset -200
    anon @ -m_talk "( {b}Yumi{/b}'s lucky to be alive ... )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
