label ano09_hint_tony:
    call tony_button_stage
    show tony a_frustrated
    show anon with dissolve:
        flip
    tony "You get some new wheels yet, champ?"
    anon "No, I'm still working on it."
    tony f_suspicious "Well, don't dilly-dally around here..."
    tony @ a_point "{b}Get down to the car dealership and see what's in your price range{/b}!"
    anon @ f_laugh "Yes, sir!"
    hide anon with dissolve
    return


label ano09_wage_tony:
    show anon with dissolve:
        flip
    anon "{b}Tony{/b}!"
    anon "I got new wheels like you wanted."
    tony @ a_frustrated "Oh, yeah?"
    show tony with dissolve:
        unflip
        xoffset -400
    tony f_suspicious @ a_whisper "'Ey, {b}Maria{/b}!!"
    tony "Come check out {b}[firstname]{/b}'s new ride with me!"
    maria "He got another one?"
    maria "I'm comin'!"
    show tony with dissolve:
        flip
        xoffset 0
    pause .5
    hide tony
    show anon:
        unflip
        xoffset 500
    with dissolve
    pause .5
    hide anon with dissolve

    scene expression background(712, 480, 2.0, l=L_pizzeria_exterior) as stage
    show tony f_normal_down:
        flip
    show tony_overlay_o_racer as coupe:
        flip
    with fade
    show anon behind coupe with dissolve:
        flip
        xoffset -32
    show maria f_surprised behind coupe with {'master': dissolve}:
        flip
        xoffset -200
    tony "Now that's a car!"
    maria "Holy Mary, Mother, and Joseph..."
    maria "This thing must have cost an arm and a leg!"
    show tony f_normal
    anon "Nah, it wasn't too bad."
    anon "The girl at the dealership sold it to me for half price."
    maria f_normal @ f_confused "No kiddin'?"
    show tony a_mc_hip_single
    show tony_arms_dressed_a_mc_shoulder_single behind coupe:
        flip
    with dissolve
    tony "Heh, attaboy!"
    show tony a_idle:
        unflip
        xoffset -400
    hide tony_arms_dressed_a_mc_shoulder_single
    with dissolve
    tony "That's my tutelage payin' off, right there..."
    show maria f_eyeroll
    tony "The kid's a chip off the ole' block, I tell ya."
    show maria f_normal
    show tony with dissolve:
        flip
        xoffset 0
    tony "What do they call this beauty?"
    anon @ f_laugh "The Overcompensator."
    tony f_suspicious @ -m_talk "..."
    maria f_normal @ f_laugh "Pfft, hahahaah!"
    show anon f_worried
    maria "Yeah, he's a chip off the ole' block alright..."
    show tony with dissolve:
        unflip
        xoffset -400
    tony "Oh, stop actin' like you aren't impressed!"
    show tony f_normal a_frustrated with dissolve:
        flip
        xoffset 0
    tony "Ahh, don't mind her, she's just bustin' my balls."
    show tony a_idle with dissolve
    anon "I don't get the joke..."
    tony @ f_smirk_wink a_point "You might want to come up with a better name for this monster."
    anon "Oh?"
    tony "You know, something like blue falcon or sapphire stallion."
    anon f_normal "Blue falcon sounds cool."
    tony "Yeah, it does."
    show tony with dissolve:
        unflip
        xoffset -400
    tony "You hear that?"
    tony "It's the blue falcon now."
    maria @ f_laugh "Well, that's certainly an improvement."
    maria @ f_sexy "You'll have to take me for a spin sometime, eh?"
    tony "Now that's a great idea!"
    show tony with dissolve:
        flip
        xoffset 0
    tony "See champ, I told ya the ladies would love it."
    anon "Yeah, anytime, {b}Maria{/b}."
    tony "C'mon, let's go celebrate over some pizza and cannolis!"
    maria @ f_surprised "Oh, you're sharin' the cannolis now?"
    show tony a_mc_hip_single
    show tony_arms_dressed_a_mc_shoulder_single behind coupe:
        flip
    with dissolve
    tony "With this guy, you betcha!"
    maria "Well, I guess you're officially part of the family now, kid."
    maria "Let's go."
    anon "Thanks you guys!"
    hide tony
    hide maria
    hide anon
    hide tony_arms_dressed_a_mc_shoulder_single
    with dissolve

    $ game.timer.tick(3)
    $ player.go_to(L_pizzeria_exterior)
    scene expression background(712, 480, 2.0) as stage
    show tony_overlay_o_racer as coupe:
        flip
    with slowfade
    show anon f_disgusted_wince behind coupe with dissolve
    anon @ -m_talk "( So many cannolis... )"
    anon f_grin @ -m_talk "( So good though... )"
    hide anon
    hide coupe
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
