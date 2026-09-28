label nad01_find_svetlana:
    show anon with dissolve:
        xoffset -100
        xzoom -1
    anon "Hey, I know you!"
    show svetlana f_happy a_surprised with dissolve:
        xoffset 150
        xzoom -1
    svetlana "Ahh, it is little man who rescues us from bad men."
    svetlana a_sides "It is good to be seeing you again."
    anon "So this is where you disappeared to?"
    svetlana "Da."
    svetlana "I work security now for {b}Miss Chernyshevsky{/b}."
    anon f_brag "No kidding?"
    svetlana a_hips "She is good woman."
    svetlana "Pays big money and treats us well."
    anon "Well, I'm glad to hear that."
    svetlana "You have appointment?"
    anon f_shy a_behind_head "Ehh, yes?"
    svetlana "One second."
    show anon a_sides f_normal:
        xoffset 370
        xzoom 1
    show svetlana a_sides:
        xoffset 700
    with {'master': dissolve}
    svetlana f_normal "{b}Miss Chernyshevsky{/b}?"
    show anon f_confused
    nadya "What is it, {b}Svetlana{/b}?" (show_native="Chego ty khochesh', {b}Svetlana{/b}?")
    svetlana "The young man you've been waiting for is here to see you." (show_native="K vam prishel molodoy chelovek, kotorogo vy tak dolgo zhdali.")
    show anon a_phone f_normal_low with {'master': dissolve}:
        xoffset -200
        xzoom -1
    nadya "Shit." (show_native="Blyat.")
    show anon with {'master': dissolve}:
        xoffset -400
    nadya "Wait one second." (show_native="Podozhdite odnu sekundu.")
    show svetlana with {'master': dissolve}:
        xzoom 1
        xoffset 150
    svetlana m_talk "She is just finished business talkings with {b}Katya{/b}."
    show anon a_sides f_normal with {'master': dissolve}:
        xoffset 100
        xzoom 1
    svetlana -m_talk "One moment."
    anon "Okay."
    pause
    show katya b_naked_disheveled f_surprised a_clothes behind svetlana with dissolve:
        xoffset -80
    pause
    show svetlana f_happy
    anon f_surprised_low a_surprised_up @ -m_talk "!!!"
    katya f_happy "Hello."
    anon f_flirt a_behind_head "H-hi."
    pause
    show svetlana f_curious
    katya f_concerned "Ehh..."
    katya "... Please, excuse."
    hide katya
    show anon a_sides f_flirt_grin:
        xoffset -400
        xzoom -1
    with dissolve
    pause
    svetlana f_smirk a_hips "{b}Miss Chernyshevsky{/b} will see you now."
    show anon with {'master': dissolve}:
        xoffset 100
        xzoom 1
    anon f_confused @ -m_talk "Hmm?"
    anon f_shy "Oh, right... thanks!"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
