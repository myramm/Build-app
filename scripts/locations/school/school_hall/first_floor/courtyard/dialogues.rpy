label courtyard_roxxy_intense_gymercise:
    scene expression game.timer.image("backgrounds/location_school_gym{}_blur.jpg") with dissolve
    show bridget a_crossed f_angry
    show anon b_jersey f_surprised
    with dissolve
    bridget "Well, look what the cat dragged in."
    bridget "How's your training?"
    show bridget f_normal
    anon @ f_worried "Uhm... I've been trying to go to the gym!"
    bridget f_angry "Trying, huh?"
    bridget "Let's see how many push-ups you can do, now."
    bridget f_normal "Maybe you beat your personal best of... What was it again, two?!"
    show anon f_surprised_teeth
    bridget f_angry_yell "Now drop and give me twenty!" with hpunch
    show bridget b_bend f_angry_down
    show anon b_jersey_pushup01 with fastdissolve
    pause 0.5
    show anon b_jersey_pushup02 with fastdissolve
    pause 0.5
    show anon b_jersey_pushup01 with fastdissolve
    bridget "One!"
    show anon b_jersey_pushup02 with fastdissolve
    pause 0.5
    show anon b_jersey_pushup01 with fastdissolve
    bridget "Two!"
    show anon b_jersey_pushup02 with fastdissolve
    pause 0.7
    show anon b_jersey_pushup01 with fastdissolve
    bridget "Three!"
    show anon b_jersey_pushup02 with fastdissolve
    pause 0.9
    show anon b_jersey_pushup01 with fastdissolve
    bridget "Four!"
    show anon b_jersey f_tired of_blush
    show bridget a_idle f_normal b_dressed
    with fastdissolve
    bridget "Congratulations, {b}[firstname]{/b}! You've improved from worthless to pathetic!"
    bridget f_angry "Keep training, maggot!"
    anon "Yes... {b}Coach Bridget{/b}..."
    bridget "Now, get out of my sight!"
    bridget "And you better show more progress next time!"
    anon "Sorry, {b}Coach Bridget{/b}!"
    hide bridget
    hide anon
    with dissolve
    return

label courtyard_bridget_intro:
    scene expression game.timer.image("backgrounds/location_school_gym{}_blur.jpg")
    show bridget a_crossed f_normal:
        xoffset 50
    show anon b_jersey with {'master': dissolve}
    bridget "Look who decided to show up!"
    anon f_laugh "Hi, {b}Coach Bridget{/b}!"
    anon "I know I've missed a few training sessions, but I assure you that I will be ready for the Regional Athletics Tri-"
    show anon f_surprised_teeth
    bridget f_angry "Shut up, you maggot!" with hpunch
    bridget "You are one month behind everyone else, {b}[firstname]{/b}, and I'm not going to let you drag down the team with your lack of commitment!"
    bridget "If you can't make the qualifying scores, you can {b}forget about your credits and graduating this year{/b}."
    anon f_worried "Don't worry, ma'am! I'm sure the qualifiers will be no problem!"
    bridget "... Oh yeah?"
    bridget "Why don't you show us your \"elite athletic skills\" by doing twenty push-ups right now, you pathetic little twerp?!"
    show bridget a_whistle f_angry_yell with {'master': dissolve}
    anon "But-"
    show anon f_shock
    bridget "{i}*WHISTLE*{/i}"
    show anon b_jersey_pushup02 with fastdissolve
    show bridget b_bend f_angry_down with dissolve
    anon "Ghh..."
    show anon b_jersey_pushup01 with fastdissolve
    bridget "One..."
    show anon b_jersey_pushup02 with fastdissolve
    anon "Ghhhh..."
    show anon b_jersey_pushup01 with fastdissolve
    bridget "Two..."
    show anon b_jersey_pushup02 with fastdissolve
    anon "... I... I can't..."
    show anon b_jersey_pushup01 with {'master': dissolve}
    show anon b_jersey_pushup02 with {'master': dissolve}
    bridget "Thr-"
    hide anon with {'master': dissolve}
    bridget "... ... ..."
    show bridget a_crossed f_angry b_dressed with {'master': dissolve}
    bridget "What?! Is that all you got?"
    show anon b_jersey of_blush f_depressed with {'master': dissolve}
    bridget "You can't even do three miserable push-ups?!"
    anon f_worried_down "I..."
    anon @ f_worried "I'm... Sorry... Ma'am..."
    bridget "You better {b}get your ass to the local gym{/b} now, and start lifting, if you want to pass this class..."
    bridget "... Just {b}stick to Miss Bissette's class{/b}, where hard work and good grades don't matter!"
    bridget f_angry_yell "Now, GET OUT OF MY SIGHT!!!"
    hide bridget with {'master': dissolve}
    show ronda b_jersey with {'master': dissolve}
    show anon f_tired -of_blush
    ronda "You're never going to make it past the qualifiers..."
    ronda "Why do you even bother coming to this class?"
    anon "I can still make it..."
    anon "And you know what... I was thinking, maybe you could help me tr-"
    ronda f_upset_angry "Hold it right there!"
    ronda f_upset "If, by some miracle, you manage to {b}make the trials{/b}... Then come talk to me. Otherwise, you can stop wasting your breath."
    show ronda f_normal
    anon f_normal "Okay!"
    anon "But when I do, you'll have to show me some of your tricks!"
    ronda "I'll be at the swimming pool for the next two weeks, training for the 200-meter trials..."
    ronda "If you make the team, then come see me."
    anon f_grin a_handshake "Deal!!"
    show anon f_surprised
    ronda @ f_eyeroll "Ugh... Pathetic..."
    hide ronda
    hide anon
    with {'master': dissolve}
    return

label courtyard_bridget_training:
    scene gym
    show anon f_worried with dissolve
    show bridget a_crossed f_angry with dissolve
    bridget "{b}[firstname]{/b}!"
    bridget "You better {b}be training your ass off at the gym{/b}, or I'm going to shove my foot up your ass!!"
    anon f_surprised a_salute "Yes, ma'am!!!"
    hide bridget
    hide anon
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
