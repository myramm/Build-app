label ano07_hint_tony:
    show anon with dissolve:
        flip
    tony @ a_frustrated "You get some new wheels yet, champ?"
    anon f_worried "No, I'm still working on it."
    tony f_suspicious "Well, don't dilly-dally around here..."
    tony @ a_point "{b}Get down to the car dealership and see what's in your price range{/b}!"
    anon f_normal @ a_salute "Yes, sir!"
    hide anon with dissolve
    return


label ano07_wage_tony:
    show anon with dissolve:
        flip
    anon "Hey, {b}Tony{/b}!"
    anon @ f_laugh "I did it!"
    tony "You did what?"
    anon "I got myself a car!"
    tony @ a_point "Oh, you did huh?"
    anon "Yeah, I've got it parked outside now."
    tony @ a_frustrated "Well, let's go take a look then, shall we?"
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
    show tony_overlay_o_car as compact:
        flip
    with fade
    show anon behind compact with dissolve:
        flip
        xoffset -100
    tony f_suspicious "Jesus, what the hell is this thing?"
    tony "Did it come with a purse and high heels?"
    anon f_worried_low "Hey, c'mon {b}Tony{/b}... It was the only thing they had in my price range."
    tony f_normal "Heh, fair enough."
    anon f_normal "I got it for less than half-price too."
    tony @ a_frustrated "Nice work, champ!"
    tony "You know, I bet this thing will actually attract a lot of female attention!"
    anon @ f_laugh "You think so?"
    tony "Ah, yeah!"
    tony @ a_fists "Just make sure you wear your confidence on your sleeve while you're drivin' it, eh?"
    tony "They'll be on you like bees on honey."
    anon "I hope you're right."
    show tony f_suspicious a_whisper with dissolve:
        unflip
        xoffset -400
    tony "Ey, {b}Maria{/b}!"
    tony "Get out here, quick!"
    show tony f_normal a_idle with dissolve
    pause
    tony "She's gotta see this..."
    show maria f_annoyed behind compact with dissolve:
        flip
        xoffset -200
    maria "What, the kid got himself a new car?"
    tony "You betcha."
    tony "{b}[firstname]{/b} is movin' up in the world."
    maria f_surprised "!!!"
    maria "What's with the color?"
    tony @ f_smirk_wink "He says it's the only thing they had in his price range..."
    maria f_normal "Is that so?"
    show tony with dissolve:
        flip
        xoffset 0
    anon "Yes, ma'am."
    maria "Well, I'll say this..."
    maria "A guy drives around in this thing, he's either queer or very comfortable in his masculinity."
    tony @ f_laugh a_belly "Hahahaah!"
    tony "I'm pretty sure it's the latter."
    maria "Yeah, I'm sure."
    pause
    maria "Just be careful out there drivin' it, eh?"
    maria "We finally got ourselves a good delivery boy."
    maria "God knows if we'll ever find another one."
    maria "Congratulations, kid."
    maria "I love the color."
    anon @ f_laugh "Thanks, {b}Maria{/b}."
    hide maria with dissolve
    pause
    show tony a_mc_hip_single:
        xoffset -68
    show tony_arms_dressed_a_mc_shoulder_single behind compact:
        flip
        xoffset -68
    with dissolve
    tony "Well, you've certainly won her over."
    anon "Yeah?"
    tony "You must have made a good impression with those pizzas, eh?"
    anon "I guess so."
    tony "Heh, attaboy!"
    tony "C'mon, let's get crackin' on those deliveries, eh?"
    tony "I'll have to see about givin' you another raise."
    hide tony_arms_dressed_a_mc_shoulder_single
    hide tony
    with dissolve
    anon @ a_salute "Yes, sir!"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
