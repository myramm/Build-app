label nad01_thug_home_lobby:
    scene location_home_entrance_frontdoor
    show location_home_entrance_frontdoor_day_door_overlay as door
    show debbie f_surprised_worried a_nervous:
        xoffset 110
        xzoom -1
    show thug f_confused behind door
    with fade
    debbie "Y-you stay back!"
    show debbie f_sad
    jab a_defensive "Please, lady... I'm not here to hurt-"
    show debbie a_nervous f_surprised_worried:
        xoffset 0
    with {'master': dissolve}
    debbie "The cops are monitoring this place, you know?!"
    debbie "T-they'll come after you for-"
    show debbie f_sad
    anon "What is going on?!"
    show anon f_confused behind debbie:
        xoffset -200
    with {'master': dissolve}
    anon "Why are you scream-"
    show debbie b_robe_hug_mc behind anon:
        xzoom 1
        xoffset -200
    show anon b_empty f_worried
    with dissolve
    pause
    show thug a_sides with {'master': dissolve}
    anon f_surprised "{b}Jab{/b}?"
    jab f_happy a_wave "Hello, friend." (show_native="Privet, comrade {b}[firstname]{/b}.")
    show thug a_sides with {'master': dissolve}
    anon f_normal "It's okay, {b}[deb_name]{/b}."
    show debbie b_robe f_sad:
        xoffset -150
        xzoom -1
    show anon a_sides b_dressed behind debbie:
        xoffset 50
    with {'master': dissolve}
    anon f_normal "I know this one."
    show debbie b_robe_scared_anon f_sad behind anon
    show anon b_empty f_worried_left
    with {'master': dissolve}
    debbie @ f_curious "What is he doing here?"
    show anon f_normal
    jab "I come bearing gift, from {b}Miss Chernyshevsky{/b}."
    anon "You mean {b}Nadya{/b}?"
    jab "Da."
    show anon f_surprised_low
    show debbie f_gross
    show thug a_vodka_hold
    with {'master': dissolve}
    jab "She sends you fine wadka and invites you come visit at warehouse."
    show debbie f_sad
    anon f_confused "The warehouse?"
    anon "I thought it was being auctioned off?"
    jab f_confused "Ehh, da... she buys."
    anon "{b}Nadya{/b} bought the warehouse?"
    jab f_normal "Is distillery now."
    show anon f_normal
    jab "We are making best wadka!"
    pause
    show anon f_worried_low
    show debbie behind thug
    show thug a_vodka_give
    with dissolve
    jab "You try."
    anon "Ehh."
    show anon a_vodka_look b_dressed f_normal_low behind thug
    show debbie a_cover b_robe
    show thug a_sides
    with {'master': dissolve}
    anon "Thanks, I guess."
    anon f_shy a_vodka_hold "I'm not much of a vodka drinker."
    jab f_confused a_scratch_head "What?!"
    jab "How you no like wadka?"
    jab f_happy a_sides "I drink since I was little boy."
    jab a_chest "It makes man of you."
    jab @ f_laugh "Puts hair on chest."
    show debbie f_gross
    show thug a_sides
    with {'master': dissolve}
    anon "R-right... umm, okay."
    pause
    anon f_normal "Anything else?"
    jab f_normal "She is very grateful for help you provide with her papa."
    jab "She hopes you will come to visit."
    show anon f_surprised_left behind debbie
    debbie f_angry a_hips "No, thank you!"
    debbie "{b}[firstname]{/b} doesn't want anything to do with you people!"
    show anon f_confused
    jab f_confused "She speaks for you?"
    anon f_worried_left a_behind_head "I uhh..."
    pause
    show debbie f_surprised
    anon f_worried a_vodka_hold "... I'll think about it."
    jab f_happy "Okay."
    show debbie f_sad
    jab "I tell her, maybe you come."
    jab "If not, is no problem."
    pause
    jab a_wave "Farewell, friend." (show_native="Do svidaniya, comrade {b}[firstname]{/b}.")
    hide thug with dissolve
    pause
    anon "Well, that was unexpected."
    hide door
    show anon a_reach:
        xoffset 340
    with dissolve

    scene expression background(l=L_home_entrance) as stage
    show debbie a_hips f_angry:
        xzoom -1
    with fade
    show anon f_normal a_vodka_hold with dissolve:
        xzoom -1
    anon "You okay?"
    debbie "No, I'm not okay!"
    show anon f_worried
    debbie "You're not seriously thinking of going there, are you?"
    anon "I dunno."
    show anon f_surprised
    debbie "We already lost your dad to these people!"
    anon f_worried "No, that was different."
    anon "{b}Nadya{/b} isn't like her father..."
    anon "... And she's a big part of the reason I was able to rescue you."
    show debbie a_nervous f_sad with dissolve
    pause
    anon "I should at least go and hear her out."
    anon "I owe her that much."
    debbie "B-but, what if she-"
    show anon a_knock behind debbie with {'master': dissolve}:
        xoffset -150
    anon "I'm not going to let anything else happen to us."
    anon "I promise."
    show debbie b_robe_hug_mc behind anon:
        xoffset -150
    show anon b_empty f_surprised
    with {'master': dissolve}
    debbie "Oh, just be careful... okay?"
    anon "I'm always careful."
    show anon f_grin
    pause
    show debbie a_front b_robe:
        xoffset 100
    show anon a_vodka_hold b_dressed f_normal:
        xoffset -50
    with {'master': dissolve}
    debbie "I've gotta cook something and get my mind off all this..."
    debbie "... It's making me a nervous wreck."
    anon "Cookies?"
    debbie f_curious "You want cookies?"
    anon f_brag "I always want cookies."
    debbie f_normal "Well, what my boy wants, he gets!"
    anon "Thanks, {b}[deb_name]{/b}."
    hide debbie with dissolve
    pause
    show anon a_vodka_look f_confused_low with dissolve
    anon @ -m_talk "( Hmm, \"Gulag Juice\"? )"
    anon f_surprised_low @ -m_talk "( \"Taste the oppression\". )"
    pause
    anon a_vodka_hold f_thinking @ -m_talk "( {b}Maybe I should swing by the warehouse and see what they're up to{/b}. )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
