label ano28_debt_debbie_debt:
    anon "I have a surprise for you."
    debbie f_curious "Oh?"
    debbie "What kind of surpise?"
    anon "You know your debt with the bank?"
    debbie f_sad "Yeah, what about it?"
    anon f_happy "It's gone."
    anon "I paid it off."
    debbie a_sides f_surprised "Wha-"
    debbie "How could you?"
    anon f_normal "The money the mob was after..."
    anon "... I found it."
    debbie f_surprised_worried "Y-you..."
    pause
    anon "I'm serious, {b}[deb_name]{/b}."
    anon "The debt is gone."
    debbie f_surprised "I-"
    pause
    show anon a_surprised_up_both f_worried_surprised
    show debbie a_mouth_shock f_crying_closed
    with {'master': fastdissolve}
    debbie "Oh my god..."
    anon f_worried "Whoa, hey... C'mon, don't cry."
    show debbie b_robe_hug_mc behind anon
    show anon b_empty f_surprised
    with {'master': dissolve}
    debbie "I can't help it... they're happy tears!"
    anon f_shy_low "Heh."
    anon "There, there..."
    pause

    if M_debbie.finished_state(S_debbie_night_visit_three):
        hide anon
        show debbie b_robe_kiss_mc:
            xoffset -350
        with dissolve
        debbie "Mmm."
        pause
        show debbie b_robe_hug_mc:
            xoffset -0
        show anon b_empty f_flirt_low
        with dissolve

    debbie "You are such a wonderful boy!"
    anon "Yeah, I've been hearing that a lot recently."
    debbie "How did I get so lucky?!"
    anon f_normal "I'm the lucky one."
    show anon a_idle b_dressed f_normal
    show debbie a_front b_robe f_laugh:
        xoffset -150
    with dissolve
    debbie "Hehe!"
    show anon f_normal_left
    show debbie f_normal
    jenny "What the hell is going on?"
    show anon b_empty f_shy:
        xoffset 140
        xzoom -1
    show debbie a_idle b_robe_mc_touch f_normal_back:
        xoffset 44
    with dissolve
    pause
    show debbie a_touch f_normal with {'master': dissolve}
    debbie "{b}[jen_name]{/b}, come in here!"
    show anon a_sides b_dressed f_normal:
        xoffset 50
        xzoom -1
    show debbie a_sides b_robe:
        xoffset -150
    show jenny a_magic b_dressed_magic f_upset:
        xzoom -1
    with {'master': dissolve}
    debbie "You're not gonna believe this!"
    jenny @ f_eyeroll "Oh god, now what's happened?"
    show debbie a_front f_excited
    with {'master': dissolve}
    debbie "Something wonderful!"
    show anon f_happy
    debbie f_normal "{b}[firstname]{/b} paid off our debt at the bank!"
    show jenny a_up_surprised f_surprised with {'master': dissolve}
    jenny "Wait, what?!"
    debbie "It's true!"
    show jenny a_sides with {'master': dissolve}
    jenny "How?"
    show debbie f_normal_back
    anon "The money the mob was looking for..."
    pause
    anon f_normal "... I found it."
    show debbie f_normal
    jenny "So we're not gonna lose the house?!"
    show debbie f_normal_back
    anon f_happy "Nope."
    show debbie f_normal
    jenny f_happy "Holy shit, {b}[firstname]{/b}!!"
    debbie @ f_excited "Isn't that great?!"
    jenny "Yeah!"
    hide jenny
    show debbie b_robe_hug_jenny_front_arm f_normal_back:
        crop (0, 0, 940, 768)
    with dissolve
    hide anon
    show debbie b_robe_hug_jenny_front_anon f_content:
        crop None
    with dissolve
    pause
    debbie "I love you both, so much."
    anon "I love you too."
    pause
    show jenny a_magic b_dressed_magic f_happy:
        xzoom -1
    show debbie a_front b_robe f_normal
    show anon a_sides b_dressed f_normal:
        xoffset 50
        xzoom -1
    with dissolve
    debbie "We should celebrate!"
    show debbie f_normal_back
    anon "Oh?"
    debbie f_excited_back "I'm thinking ice cream and a movie!"
    show anon f_confused
    show debbie f_normal
    jenny f_concerned "Ice cream and a movie?"
    show jenny a_crossed
    with {'master': dissolve}
    jenny "What are we, twelve years old?"
    debbie "Oh, c'mon!"
    anon f_normal "I'm down."
    jenny f_eyeroll "Eugh, Of course you are."
    show anon f_worried
    debbie f_sad "Please, it'll be like a family night!"
    jenny f_upset @ f_upset_back_low "{i}*Sigh*{/i} Fine."
    show anon f_normal
    debbie f_normal "That's my girl!"
    pause
    show jenny a_sides f_grin with {'master': dissolve}
    jenny "But I'm picking the movie!"
    show debbie f_normal_back
    anon f_worried "Oh, no!"
    anon "Bad idea."
    show jenny f_upset
    anon f_disgusted "If you think I'm watching anymore of that sparkly vampire shit, you've got another thing coming!"
    show anon f_surprised
    show jenny behind debbie
    show debbie a_hips f_surprised:
        xoffset 350
        xzoom -1
    with {'master': fastdissolve}
    debbie "{b}[firstname]{/b}, language!"
    anon f_shy "Sorry, {b}[deb_name]{/b}."
    show anon f_unimpressed
    show debbie a_facepalm f_sad_closed:
        xoffset -150
        xzoom 1
    show jenny a_upset f_angry
    with {'master': dissolve}
    jenny "Hey, it's not shit!"
    jenny f_upset "It's the greatest film franchise of our generation."
    anon f_annoyed "You're a monster."
    show debbie a_sides f_laugh
    show jenny a_sides f_laugh
    with {'master': dissolve}
    jenny "Hahaha!"
    show anon f_normal
    show jenny f_happy
    debbie f_normal @ f_excited "I'll get the ice cream!"
    hide debbie
    show jenny a_magic:
        xoffset -500
        xzoom 1
    with dissolve
    anon f_worried "Please, don't make me watch that crap, {b}[jen_name]{/b}."
    show jenny with {'master': dissolve}:
        xoffset 0
        xzoom -1

    if M_jenny.finished_state(S_jenny_cheerleader_sex) and M_jenny.get("dominance") > 0:
        jenny f_eyeroll "{i}*Sigh*{/i} Fiiiine."
        jenny f_normal "Just this once, because you got us the house back... You can choose!"
        anon f_laugh "Yes!!"
        show anon f_normal
        jenny f_upset "Don't fuck it up by choosing some cheesy action movie!"
        anon f_brag "Oh, never fear!"
        anon "I know just the one."
        anon f_normal "Marty Pythin and the Holy Cheese!"
        jenny f_happy "Alright, I can live with that."
        pause
        hide jenny with dissolve
        show anon a_cheering f_laugh with {'master': dissolve}
        anon "Ah, yeah!"
        hide anon with {'master': dissolve}
        jenny "Come sit by me."
    else:

        jenny f_grin "Too late."
        jenny "We're watching it."
        anon f_frown_down "Aww, man..."
        show anon f_annoyed
        jenny f_normal "Just be thankful I'm spending time with you at all... dillhole."
        hide jenny with dissolve
        anon "Yeah, whatever."
        pause
        anon f_sad_smile_down "{i}*Sigh*{/i} At least there's gonna be ice cream."
        show anon f_surprised
        jenny "If you're a good boy, I might even let you paint my nails."
        show anon f_unimpressed with {'master': dissolve}:
            xoffset -250
        anon "Yeah, right... why would I wanna-"
        show anon f_thinking
        pause
        hide anon with {'master': dissolve}
        anon "Wait, fingernails or toenails?"
        jenny "You're such a perv."
        jenny "Hahaha!"

    scene expression background(l=L_home_bedroom, t=3) with longfade
    show anon f_tired_happy with dissolve:
        xoffset 250
    anon @ -m_talk "( What a great day! )"
    anon @ -m_talk "( {b}[deb_name]{/b} can finally stop stressing out about money... )"
    anon f_grin @ -m_talk "( ... And my bank account is overflowing! )"
    anon a_yawn f_yawn @ -m_talk "{i}*Yawn*{/i}"
    anon a_sides f_tired_happy @ -m_talk "( Man, I wonder what adventures tomorrow will bring? )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
