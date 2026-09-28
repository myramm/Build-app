label kha01_talk_warehouse_depot:
    scene expression background(560, 480, 5) as stage
    show nadya:
        xoffset 200 xzoom -1
    show svetlana a_sides b_dressed:
        xoffset -50 xzoom -1
    show anon a_sides f_shy behind nadya with dissolve:
        xzoom -1
    nadya "Well?!"
    nadya "How did it go?"
    anon "She's feeling much better."
    show anon a_jaw_out
    with {'master': dissolve}
    nadya f_happy "Heh, dick magic!" (show_native="Heh, Dik magiya!")
    svetlana f_concerned "Wait, I don't think so..." (show_native="Podozhdi, ya tak ne dumayu...")
    show anon a_sides f_confused
    show nadya a_sides f_confused:
        xoffset -375 xzoom 1
    with {'master': dissolve}
    nadya @ -m_talk "Hmm?"
    show svetlana a_point_front
    with {'master': dissolve}
    svetlana "He doesn't look like a man who just had sex." (show_native="On ne pokhozh na cheloveka, kotoryy tol'ko chto zanimalsya seksom.")
    show nadya a_hips f_worried:
        xoffset 200 xzoom -1
    with {'master': dissolve}
    pause
    show nadya a_point
    show svetlana a_hips
    with {'master': dissolve}
    nadya "She's right, you don't look like a man who just had sex!"
    anon f_brag "That's because I didn't."
    show anon a_jaw_in f_disgusted
    show nadya a_crossed f_worried
    show svetlana f_annoyed
    with {'master': dissolve}
    nadya "Then how did you-"
    show anon f_disgusted_wince
    show nadya f_confused
    with {'master': dissolve}
    pause
    show anon a_sides f_shy
    with {'master': dissolve}
    nadya f_sexy "Oh, I see."
    svetlana f_curious "What?"
    show nadya a_sides:
        xoffset -375 xzoom 1
    with {'master': dissolve}
    nadya "He ate her pussy." (show_native="On s'yel yeye kisku.")
    svetlana f_surprised "Seriously?!" (show_native="Ty ser'yeznyy?")
    show anon f_surprised
    show svetlana a_crossed f_bored
    with {'master': dissolve}
    svetlana @ f_eyeroll "I could have done that..." (show_native="Ya mogla by eto sdelat'...")
    nadya "But you didn't." (show_native="No ty etogo ne sdelal.")
    show anon f_confused
    show nadya a_hips f_confused:
        xoffset 200 xzoom -1
    with {'master': dissolve}
    nadya "She will keep making vodka?"
    anon f_happy @ -m_talk "Mhmm."
    nadya f_happy "Excellent!" (show_native="Prevoskhodno!")
    nadya "It seems I am in your debt once again, {b}[firstname]{/b}."
    anon f_shy "Yeah, don't mention it."
    show anon a_jaw_out
    with {'master': dissolve}
    pause
    anon f_worried "Man, I need a beverage or something!"
    show nadya a_sides:
        xoffset -375 xzoom 1
    with {'master': dissolve}
    nadya "Heh, {b}Svetlana{/b}, take {b}[firstname]{/b} upstairs and get him whatever he wants."
    show anon a_sides f_shy
    with {'master': dissolve}
    svetlana "Da, {b}Miss Chernyshevsky{/b}."
    hide svetlana
    show nadya:
        xoffset 200 xzoom -1
    with {'master': dissolve}
    anon "Thanks."
    nadya "No, thank you."
    hide anon
    show nadya a_sides:
        xoffset -375 xzoom 1
    with {'master': dissolve}
    pause
    nadya @ f_laugh "Heh!"
    nadya "I knew it would work." (show_native="Ya znal, chto eto srabotayet.")

    scene black
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
