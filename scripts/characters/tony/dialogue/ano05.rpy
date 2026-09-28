label ano05_hint_tony:
    show anon with dissolve:
        flip
    tony @ a_frustrated "You get some new wheels yet, champ?"
    anon f_worried "No, I'm still working on it."
    tony f_suspicious "Well, don't dilly-dally around here..."
    tony @ a_point "{b}Get down to the car dealership and see what's in your price range{/b}!"
    anon f_normal @ a_salute "Yes, sir!"
    hide anon with dissolve
    return


label ano05_wage_tony:
    show anon with dissolve:
        flip
    anon "Hey, {b}Tony{/b}!"
    anon "I did it!"
    tony "You did what?"
    anon "I got myself a vehicle!"
    tony "Oh, you did huh?"
    anon "Yeah, I've got it parked outside now."
    tony "Well, let's go take a look then, shall we?"
    hide tony
    show anon:
        unflip
        xoffset 500
    with {'master': dissolve}
    anon "Yes, sir!"
    hide anon with dissolve

    scene expression background(712, 480, 2.0, l=L_pizzeria_exterior) as stage
    show tony f_normal_down:
        flip
    show tony_overlay_o_scooter as scooter
    with fade
    show anon f_shy_low behind scooter with dissolve:
        flip
        xoffset 100
    tony "Hey, look at this!"
    tony f_normal "You got yourself a nice little scooter, didn't ya?"
    anon f_normal "You bet!"
    anon @ f_laugh a_point "I got it for half-price too."
    tony @ a_frustrated "Nice work, champ!"
    tony "I'm real proud of ya!"
    anon @ f_laugh "Thanks, {b}Tony{/b}!"
    show tony f_suspicious a_whisper with dissolve:
        unflip
        xoffset -400
    tony "Ey, {b}Maria{/b}!"
    tony "Get out here, quick!"
    pause
    tony f_normal a_idle "She's gotta see this..."
    show maria f_annoyed behind scooter with dissolve:
        flip
        xoffset -200
    maria "What the hell are you yellin' about?"
    tony @ a_point_back "Check out our delivery boy's new wheels."
    maria f_surprised "Ahh, don't tell me you bought this for him?"
    tony f_suspicious "I most certainly did not!"
    tony "He bought this with his own money that he earned right here, workin' for you."
    maria f_normal "Is that so?"
    show tony f_normal with dissolve:
        flip
        xoffset 0
    anon "Yes, ma'am."
    maria "Well, color me surprised."
    tony @ a_point "I told ya, this one was a keeper."
    tony "Eh?"
    tony "Didn't I tell ya?"
    maria f_annoyed "Yeah, yeah..."
    maria "Don't be too humble now, you big ape."
    tony @ f_laugh a_belly "Hahahaah!"
    tony a_heart "He came here as a boy, but he's gonna be leavin' as a man."
    tony "I tell you what."
    maria "I'm going back to the kitchen before my calzones burn."
    maria f_normal "Congratulations, kid."
    maria "I love the color."
    anon "Thanks, {b}Maria{/b}."
    hide maria with dissolve
    pause
    show tony a_mc_hip_single:
        xoffset 132
    show tony_arms_dressed_a_mc_shoulder_single behind scooter:
        flip
        xoffset 132
    with dissolve
    tony "Well, I guess I'm gonna have to start payin' you more now, huh?"
    anon "Oh, that's right!"
    anon "You promised me a raise, didn't you?"
    tony "Well, only if you want it?"
    anon "I definitely want it!"
    tony "Heh, attaboy!"
    tony "C'mon, let's get crackin' on those deliveries, eh?"
    tony "I wanna see what this baby can do."
    hide tony_arms_dressed_a_mc_shoulder_single
    hide tony
    with dissolve
    anon f_grin @ f_laugh "Yes, sir!"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
