label button_lucy_how_are_the_little_ones:
    show anon f_normal
    anon "How are the little ones?"
    show lucy f_normal
    lucy "Aww, it's so sweet of you to come and check on them!"
    lucy "Everyone is doing wonderful!!"
    lucy "In fact, we were just about to sit down for story time."
    lucy "Would you like to join us?"
    anon "Oh, ehh... N-no, thanks."
    anon "I'd probably just get in your way..."
    lucy "Oh, nonsense!"
    return

label button_lucy_baby_dialogue:
    show anon f_normal
    show lucy
    anon "How's my little one doing?"
    lucy @ f_laugh "Oh, just fine!"
    lucy "Everyone is having a wonderful time!"
    lucy "Little {b}Jack{/b} has been chasing after all the girls today."
    lucy "That's one child we'll have to keep an eye on as he gets older."
    anon "Silly kids."
    anon "Well, they all look like they are having fun!"
    lucy @ f_laugh "Oh, yeah! That's all we do every day is have fun, fun, fun!"
    anon "Good. Well, I just thought I'd stop by and see how everyone was doing."
    lucy "Awwww."
    lucy "I must say, it's so refreshing to see a dad stop in and check up on his little one."
    return

label button_lucy_baby_dialogue_multiple:
    show anon f_normal
    show lucy
    anon "How are my little ones doing?"
    lucy @ f_laugh "Oh, just fine!"
    lucy "Everyone is having a wonderful time!"
    if randomizer() > 50:
        lucy "Just keep an eye out for {b}Jacob{/b}."
        lucy "He found some stickers and has been placing them everywhere."
    elif randomizer() > 50:
        lucy "Little {b}Jack{/b} has been chasing after all the girls today."
        lucy "That's one child we'll have to keep an eye on as he gets older."
    else:
        lucy "Otherwise, the children have been pretty well-behaved."
        lucy "I wish every day were like this."
    anon "Silly kids."
    anon "Well, they all look like they are having fun!"
    lucy @ f_laugh "Oh, yeah! That's all we do every day is have fun, fun, fun!"
    anon "Good. Well, I just thought I'd stop by and see how everyone was doing."
    lucy "Awwww."
    lucy "I must say, it's so refreshing to see a dad stop in and check up on his little ones."
    return

label lucy_button_intro_day:
    show anon f_normal
    show lucy
    with dissolve
    lucy "Hey there, {b}[firstname]{/b}."
    lucy "What brings you by today?"
    anon "Oh, I was just in the neighborhood and thought I'd say hello."
    lucy "Well, that's nice."
    return

label lucy_button_intro_night:
    show anon f_normal
    show lucy f_sad b_messy a_cover
    with dissolve
    lucy "Oh, goodness."
    show lucy f_normal a_idle with dissolve
    lucy "I didn't know you were stopping by, {b}[firstname]{/b}."
    lucy @ f_normal_down "I imagine I look like quite a mess..."
    anon "No, not at all."
    anon "You always look nice, {b}Lucy{/b}."
    lucy "Well, that's nice of you to say."
    return

label button_lucy_how_are_you:
    show anon f_normal
    show lucy f_normal
    anon "You doing alright?"
    lucy "Hmm?"
    lucy "Oh, I'm just fine."
    lucy @ f_laugh "These kids just brighten up my day."
    anon f_worried "{b}Richard{/b} treating you okay?"
    lucy "Oh, you know {b}Richard{/b}."
    lucy "He's set in his ways."
    anon @ f_skeptical "Well, let me know if you ever need any help, okay?"
    lucy "You're so sweet."
    show anon f_normal
    lucy "Thanks, {b}[firstname]{/b}."
    return

label button_lucy_hows_the_milk:
    show anon f_normal
    show lucy f_normal
    anon "Satisfied with your last shipment of milk?"
    lucy @ f_laugh "Oh, yes."
    lucy "The little ones just can't get enough."
    anon f_worried "You really like looking after all these kids?"
    lucy @ f_laugh "I love it!"
    lucy "It keeps me young, you know?"
    anon f_normal "Well, you certainly do look young."
    show lucy f_smirk
    lucy "Aww, you're such a charmer, {b}[firstname]{/b}!"
    return

label button_lucy_annie_around_day:
    show anon f_worried
    show lucy f_normal
    anon "{b}Annie{/b} around?"
    lucy "No, I think she's at school, dear."
    lucy "You want me to tell her you stopped by?"
    anon "N-no, that's okay."
    anon "I was just curious."
    return

label button_lucy_annie_around_night:
    show anon f_worried
    show lucy f_normal
    anon "{b}Annie{/b} around?"
    lucy "I think she mentioned she had some homework to do."
    lucy "You know her, she's very particular about her school work."
    anon "Oh, I know."
    anon f_normal "Thanks, {b}Lucy{/b}."
    lucy @ -m_talk "Mmhmmm."
    return

label button_lucy_leave:
    show anon f_normal
    show lucy f_normal
    anon @ a_wave "I should get going."
    lucy "Alright, sweetie."
    anon "It was nice seeing you again."
    lucy "You too, dear."
    hide anon
    hide lucy
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
