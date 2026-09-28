label con02_init_keeves:
    anon "Well, umm... I don't need help {b}Father Keeves{/b} but I know someone who does."
    keeves f_happy @ f_laugh a_rock "Excellent!"
    keeves "Go on."
    anon "Okay."
    anon f_worried "You see, I've been doing a bit of work at {b}the mayor's house{/b} recently and it came to my attention that one of the maids there was being mistreated..."
    keeves f_confused "How so?"
    anon "Well, {b}the mayor{/b} and {b}his wife{/b} basically had her working as an indentured servant."
    keeves f_sad "Really?"
    anon "Yeah."
    anon "They were paying her next to nothing and verbally assaulting her every chance they got."
    keeves "That sounds bad."
    anon "I'm pretty sure {b}the mayor{/b} was harassing her too."
    keeves f_surprised @ -m_talk "!!!"
    keeves "{b}The mayor{/b} was?"
    anon "Y-yes, sir."
    keeves f_sad @ f_woa "Whoa!"
    pause
    keeves "That is so bogus!"
    anon "Right?"
    keeves f_normal "Sounds like strange things are afoot at {b}the mayor's mansion{/b}."
    keeves "We should intervene immediately."
    show anon f_normal
    pause
    keeves "It's like your classic damsel in distress situation."
    keeves "Which, in my experience, almost always leads to a most excellent adventure."
    anon @ f_skeptical -m_talk "..."
    anon "Right."
    anon f_normal "Well, I already managed to get her free of that job and away from {b}the mayor{/b} and {b}his wife{/b}."
    keeves "Oh?"
    keeves f_happy "Nicely done, little dude!"
    keeves f_confused "So what's the problem?"
    anon "Well, now she's really in need of a new job."
    keeves f_normal "Ahh, I see."
    anon "Which is hard to find because, she's kinda... An illegal immigrant."
    pause
    anon "Who can't speak English."
    keeves f_sad "Bummer!"
    anon "Yeah."
    pause
    anon "So, I thought maybe she could help out around here, you know?"
    keeves f_happy @ a_point "That's a truly triumphant idea, little dude!"
    keeves "But first, I have two very important questions."
    anon "Okay."
    keeves "How does this woman feel about our Lord and Savior, Jesus Christ?"
    anon "Oh, she's a devout Catholic."
    anon "That's why I immediately thought to ask you for help."
    keeves @ f_laugh a_rock "Tubular!"
    keeves "Now, question two..."
    keeves @ f_confused a_raise "Is she a babe?"
    anon f_surprised @ -m_talk "..."
    anon f_confused "Huh?"
    keeves f_normal @ a_point "What's the cones situation?"
    anon f_worried "Are you being serious right now?"
    keeves "Are they built for speed or for comfort?"
    anon "I mean, I think she's pretty..."
    keeves a_raise @ f_laugh "Alright, two for two!"
    keeves -a_raise @ f_laugh a_rock "Most excellent!"
    anon f_normal "So you'll hire her?"
    keeves f_happy "Most definitely."
    anon "Oh, that's awesome!"
    anon "Thank you so much, {b}Father Keeves{/b}!"
    keeves "No worries, little dude."
    anon "I'll bring her by ASAP."
    hide anon with dissolve

    scene expression player.location.background_blur with fade
    show anon with dissolve
    anon f_brag_closed @ -m_talk "( Yes, I knew I could find {b}Consuela{/b} a new job! )"
    anon @ -m_talk "( I can't wait to {b}tell her the good news{/b}! )"
    hide anon with dissolve

    $ M_consuela.trigger(T_con02_init)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
