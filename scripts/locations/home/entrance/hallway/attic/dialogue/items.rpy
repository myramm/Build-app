label home_attic_evidence_dialogue:
    scene expression player.location.background_blur
    show anon f_sad_down with dissolve
    anon @ -m_talk "( It's the box of {b}Dad{/b}'s personal effects. )"
    anon @ -m_talk "( I don't think I can handle going through it again. )"
    hide anon with dissolve
    return


label home_attic_globe_dialogue:
    scene location_home_attic_globe
    pause
    return


label home_attic_painting_dialogue:
    scene expression game.timer.image('attic{}')
    show closeup_painting01 with dissolve
    player_name "{b}[deb_name]{/b} used to love painting farm animals..."
    hide closeup_painting01 with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
