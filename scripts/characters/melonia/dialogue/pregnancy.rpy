label melonia_pregnancy_summon:
    scene expression player.location.background
    "{i}*Brrrzzzt* *Brrrzzzt*{/i}"

    scene expression background(288, 368, 3.5, l=L_rump_second) as underlay:
        xoffset -400
    show iwanka b_dressed_magic a_phone f_bored:
        xoffset -500

    $ renpy.dynamic(stage=player.location.background_phone)
    show expression stage as stage
    show anon f_confused with dissolve:
        flip
    anon @ -m_talk "Hmm?"

    if not M_iwanka.once('number_known'):
        anon a_phone f_thinking_down "It's {b}Iwanka{/b}."
        show anon a_phone_talk f_normal with dissolve:
            unflip
            xoffset 500
    else:

        anon a_phone f_thinking_down "I don't recognize this number..."
        show anon a_phone_talk f_skeptical with dissolve:
            unflip
            xoffset 500

    show expression stage as stage at phoneleft with phoneleft.show
    anon "Hello?"
    iwanka "Hey, {b}[firstname]{/b}."
    anon f_skeptical "{b}Iwanka{/b}?"
    iwanka "Yeah, listen..."
    iwanka "... You need to get over here ASAP."
    anon f_worried "Is everything okay?"
    iwanka "Something is wrong with {b}my mother{/b}... She's like totally flipping out."
    anon "{b}Melonia{/b}'s flipping out?"
    anon "Did something happen to the hot tub?"
    iwanka f_annoyed "I dunno, just... Get over here, will you?"
    anon "Y-yeah, okay."
    show anon f_sad_down a_phone with dissolve
    show expression stage as stage with {'master': phoneleft.hide}
    "{i}*Beep*{/i}"
    pause
    anon f_tired @ -m_talk "( I guess I'd better {b}hurry to the Rump estate{/b} and check on {b}Melonia{/b}. )"
    hide anon with dissolve
    return


label melonia_pregnancy_summon.repeat:
    scene expression player.location.background
    "{i}*Brrrzzzt* *Brrrzzzt*{/i}"

    scene expression background(288, 368, 3.5, l=L_rump_second) as underlay:
        xoffset -400
    show iwanka b_dressed_magic a_phone f_bored:
        xoffset -500

    $ renpy.dynamic(stage=player.location.background_phone)
    show expression stage as stage
    show anon f_confused with dissolve:
        flip
    anon @ -m_talk "Hmm?"
    anon a_phone f_thinking_down "It's {b}Iwanka{/b}."
    show anon a_phone_talk f_normal with dissolve:
        unflip
        xoffset 500
    show expression stage as stage at phoneleft with phoneleft.show
    anon "Hello?"
    iwanka "Dude, did you knock up my mother again?!"
    anon f_worried "Huh?"
    iwanka "She's totally flipping out over here!"
    anon "Aww, man..."
    anon "I'll be right there."
    iwanka f_normal @ f_laugh "Heh, you are so screwed..."
    show anon f_sad_down a_phone with dissolve
    show expression stage as stage with {'master': phoneleft.hide}
    "{i}*Beep*{/i}"
    pause
    anon f_tired @ -m_talk "( I guess I'd better {b}hurry to the Rump estate{/b} and check on {b}Melonia{/b}. )"
    hide anon with dissolve
    return


label melonia_pregnant_announcement_2:
    scene expression player.location.background_blur
    if player.location != L_map:
        show anon with dissolve
    anon @ -m_talk "( Hmm, I wonder what's going on? )"
    anon @ -m_talk "( I'd better {b}hurry to the Rump estate{/b} and check on {b}Melonia{/b}. )"
    if player.location != L_map:
        hide anon with dissolve
    return


label melonia_pregnant_labor_1:
    scene expression player.location.background_blur
    show anon f_normal with dissolve
    anon "Looks like I got a text."
    hide anon with dissolve
    return


label melonia_pregnant_labor_2:
    scene expression player.location.background_blur
    if player.location != L_map:
        show anon f_surprised a_phone with dissolve
    anon "{b}Melonia{/b} is having the baby?!"
    anon "Holy crap!"
    pause
    anon "I'd better {b}head to the hospital{/b} to check on them."
    if player.location != L_map:
        hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
