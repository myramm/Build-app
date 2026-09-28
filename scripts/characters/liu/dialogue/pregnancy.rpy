label liu_pregnancy_summon:
    scene expression player.location.background
    "{i}*Brrrzzzt* *Brrrzzzt*{/i}"

    scene expression background(768, 384, 2, l=L_liu_lounge) as underlay:
        xoffset -400
    show liu a_phone_talk b_robe_hair f_nervous:
        xoffset -500

    $ renpy.dynamic(stage=player.location.background_phone)
    show expression stage as stage
    show anon f_confused with dissolve:
        xzoom -1
    anon @ -m_talk "Hmm?"
    anon a_phone f_normal_low "{b}Liu{/b} is calling me."
    show anon a_phone_talk f_normal with dissolve:
        xoffset 500
        xzoom 1
    show expression stage as stage at phoneleft with phoneleft.show
    anon "{b}Liu{/b}?"
    liu "H-hey, {b}[firstname]{/b}."
    liu "I umm..."
    liu f_frightened "... S-something's happened, and... I uhh... need to see you."
    anon f_worried "Something's happened?"
    show liu f_ashamed_down
    pause
    anon "Are you okay?"
    liu f_nervous_down "Y-yeah, I'm-"
    liu f_worried_down "Err, no... I'm not... really..."
    anon f_confused "What's going on, {b}Liu{/b}?"
    liu f_worried "Can you come to my apartment... please?"
    liu "I really need to see you."
    anon f_worried "Yeah, of course!"
    anon "I'll be right over."
    liu "Thank you."
    show anon a_phone f_worried_low
    show liu a_phone f_worried_down
    with dissolve
    show expression stage as stage with {'master': phoneleft.hide}
    "{i}*Beep*{/i}"
    anon @ -m_talk "( Yikes, it sounded like she was on the verge of tears... )"
    anon f_worried @ -m_talk "( ... What could have happened?! )"
    show anon a_idle with {'master': dissolve}:
        xoffset 0
        xzoom -1
    anon @ -m_talk "( {b}I'd better get over to Liu's apartment{/b} quick and find out what's going on. )"
    hide anon with dissolve
    return


label liu_pregnancy_summon.repeat:
    scene expression player.location.background
    "{i}*Brrrzzzt* *Brrrzzzt*{/i}"

    scene expression background(768, 384, 2, l=L_liu_lounge) as underlay:
        xoffset -400
    show liu a_phone_talk b_robe_hair f_nervous:
        xoffset -500

    $ renpy.dynamic(stage=player.location.background_phone)
    show expression stage as stage
    show anon f_confused with dissolve:
        xzoom -1
    anon @ -m_talk "Hmm?"
    anon a_phone f_normal_low "{b}Liu{/b} is calling me."
    show anon a_phone_talk f_normal with dissolve:
        xoffset 500
        xzoom 1
    show expression stage as stage at phoneleft with phoneleft.show
    anon "{b}Liu{/b}?"
    liu "H-hey, {b}[firstname]{/b}."
    liu f_nervous_down "We umm..."
    liu f_nervous "... N-need to talk about something?"
    anon f_worried "Is everything alright?"
    liu "Y-yeah, everything's fine... It's just..."
    liu f_worried "... Well, it's really something better said in person."
    liu "{b}Can you come over to my apartment?{/b}"
    anon "Yeah, of course!"
    anon "I'll be right over."
    liu f_nervous "Thank you."
    show anon a_phone f_worried_low
    show liu a_phone f_worried_down
    with dissolve
    show expression stage as stage with {'master': phoneleft.hide}
    "{i}*Beep*{/i}"
    anon f_confused @ -m_talk "( Hmm, I wonder what that was about? )"
    show anon a_idle f_worried with {'master': dissolve}:
        xoffset 0
        xzoom -1
    anon @ -m_talk "( {b}I'd better get over to Liu's apartment{/b} quick and find out what's going on. )"
    hide anon with dissolve
    return


label liu_pregnant_announcement_2:
    scene expression player.location.background_blur
    if player.location != L_map:
        show anon with dissolve
    anon @ -m_talk "( I'd better {b}hurry to Liu's apartment{/b} and find out what's going on. )"
    if player.location != L_map:
        hide anon with dissolve
    return


label liu_pregnant_labor_1:
    scene expression player.location.background_blur
    show anon f_normal with dissolve
    anon "Looks like I got a text."
    hide anon with dissolve
    return


label liu_pregnant_labor_2:
    scene expression player.location.background_blur
    if player.location != L_map:
        show anon f_surprised a_phone with dissolve
    anon "{b}Liu{/b} is having the baby?!"
    anon "Holy crap!"
    pause
    anon "I'd better {b}head to the hospital{/b} to check on them."
    if player.location != L_map:
        hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
