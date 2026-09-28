label ano14_init_liu:
    scene expression background(520, 492, 4.) as stage
    show kim f_angry:
        flip
        xoffset 50
    show liu f_worried
    liu "I don't want to go."
    kim "What you mean you no go?!"
    liu "Please... Don't make me."
    liu "The mayor is a lecherous old man and he makes me super uncomfortable."
    liu f_ashamed_down "The way he stares at me..."
    liu "... Like he's undressing me with his eyes."
    kim a_crossed "Pfft, {b}Kim{/b} not care 'bout this!"
    liu f_worried @ f_surprised "!!!"
    kim "Mayor make promise to {b}Kim{/b}."
    kim "Give {b}Kim{/b} contror over dearership."
    kim "He make {b}Kim{/b} a very wearthy man!"
    liu "So you're just gonna serve me up to further your ambitions?!"
    kim a_point "You {b}Kim{/b}'s wife, stupid!"
    kim "It your job to herp {b}Kim{/b} further ambition!"
    liu f_ashamed_down @ -m_talk "..."
    kim a_crossed "Don't forget, I pay good money for you in Korea!"
    kim "I bring you here and give you nice rife!"
    kim "I even ret you have job at bank."
    kim "This the thanks {b}Kim{/b} get?!"
    liu f_worried "N-no, I just-"
    kim @ a_point "You ungratefur!"
    pause .3
    kim @ a_point "You bad wife!"
    liu "Isn't there something else I can do?"
    kim @ a_cry "Brah, brah, brah... {b}Kim{/b} want no more tarking..."
    kim "Mayor ask you come, so you come."
    show liu f_worried_down
    show kim f_smirk a_swimsuit
    with dissolve
    pause
    kim "{b}Kim{/b} buy for you."
    liu f_gross @ -m_talk "..."
    kim "You wear."
    liu f_worried "Please, {b}Kim{/b}... Don't make-"
    kim f_angry "Quiet!"
    kim "You obey or {b}Kim{/b} send you back to Korea!"
    liu @ -m_talk "..."
    kim "Say you understand!"
    liu "... I understand."
    kim f_smirk "Good."
    kim "You take!"
    show kim a_idle
    show liu a_swimsuit f_worried_down
    with dissolve
    pause
    show liu f_worried
    kim "{b}Kim{/b} pick you up, after shift at dearership."
    kim "We go."
    kim f_angry a_counter_raised "You make mayor happy, yes?"
    liu "{i}*Sniff*{/i} Y-yes."
    kim f_smirk a_idle "Good."
    kim "Finarry, you obey."
    kim @ a_point "Be ready."
    kim a_rub "{b}Kim{/b} not want be rate."
    hide kim with dissolve
    pause
    show liu f_worried_down
    pause
    show liu a_swimsuit_drop with dissolve
    pause .2
    liu a_cry f_crying @ -m_talk "{i}*Sobs*{/i}"

    scene expression player.location.background_blur
    show anon f_worried
    with fade
    anon @ -m_talk "( What the hell?! )"
    anon @ -m_talk "( I knew {b}Kim{/b} was an asshole but that was just gross! )"
    pause
    anon @ -m_talk "( How could anyone treat their wife like that? )"
    anon @ -m_talk "( I should make sure she's okay... )"
    hide anon with dissolve
    return


label ano14_sobs_liu:
    scene expression background(644, 492, 4.) as stage
    show liu a_cry f_crying:
        xoffset -500
    show anon f_worried with dissolve:
        flip
    liu @ -m_talk "{i}*Sobs*{/i}"
    show liu a_wipe_tears b_dressed f_crying with {'master': dissolve}
    anon "{i}*Ahem*{/i} Ma'am?"
    liu f_surprised a_cover "!!!"
    show liu f_worried with {'master': dissolve}:
        flip
        xoffset 0
    liu @ -m_talk "{i}*Sniff*{/i}"
    liu a_idle "Oh, sorry about that..."
    liu "... I'll be right with you."
    show liu b_dressed_bend with {'master': dissolve}:
        unflip
        xoffset -550
    anon "N-no, don't apologize."
    show liu b_dressed a_nervous with {'master': dissolve}:
        flip
        xoffset 0
    anon a_behind_head "I kinda... Well, I overheard what was going on..."
    pause
    anon a_idle "... Are you alright?"
    liu "{i}*Sniff*{/i} Y-yeah, I'll be fine."
    show liu f_surprised
    pause
    liu a_behind "Oh, shoot!"
    liu f_worried "You're {b}Frank{/b}'s kid, umm..."
    liu "... {b}[firstname]{/b}, right?"
    anon "That's right."
    anon "Are you really married to that guy?"
    liu "{i}*Sniff*{/i} Yeah, unfortunately."
    anon "How did that happen?"
    liu f_curious @ -m_talk "Hmm?"
    liu f_worried_down "Oh, umm..."
    anon @ a_hands_up "Sorry, I know it's not my business."
    anon "It's just, he shouldn't talk to you like that."
    liu f_worried "Heh, that's just what your father said."
    anon "What do you mean?"
    liu f_worried_down "{i}*Sniff*{/i} N-no, it's nothing."
    pause
    liu "I didn't marry him by choice, if that's what you're asking."
    anon "Oh?"
    liu "My family is from a small village on the Chinese border near North Korea."
    liu "We were very poor."
    pause
    liu "So when {b}Kim{/b} offered my weight in silver to my father, it wasn't a hard decision."
    anon "Your father sold you to him?"
    anon "That's awful!"
    liu "... And the money helped my family immensely."
    pause
    liu f_worried_down "He's not wrong when he says he brought me here and gave me a better life either."
    liu "I have a nice house and a job making fair money... He even lets me keep a bit of my paycheck to spend as I like."
    anon @ f_skeptical "A bit, huh?"
    anon @ f_skeptical "How generous of him."
    liu "{i}*Sniff*{/i} It's really not so bad."
    liu "He's too busy at the dealership to bother with me most of the time..."
    liu "... So long as I keep his house and make him dinner, things are peaceful."
    anon "You deserve much better."
    liu f_worried "T-that's kind of you to say."
    pause
    liu "You're so much like your father, you know?"
    liu "I really am sorry for all that happened..."
    pause
    liu f_worried_down "... He was a good man."
    anon @ f_sad_down "Y-yeah, I know."
    anon "I'm trying my best to figure out what happened..."
    anon "... In fact, that's why I'm here today."
    liu f_curious "Hmm?"
    anon f_normal "Well, you see, I found this key to a lockbox."
    liu "One of ours, down in the vault?"
    anon "Yeah, that's what I've been told."
    anon "I think {b}Dad{/b} might have left something there."
    pause
    anon "{b}Tina{/b} said she'd take me down to check it out."
    liu f_worried "I see."
    liu "Unfortunately, she's not here at the moment."
    anon f_worried "Oh?"
    liu "She got a phone call from her daughter's school and rushed off."
    liu "Something about a wardrobe malfunction during cheerleading practice."
    anon "No kidding?"
    pause
    anon f_unimpressed "Well, crap."
    pause
    anon f_worried "I guess, I'll have to come back later then."
    liu "I could, maybe... Take you down there."
    show anon f_surprised
    pause
    anon @ f_skeptical "Maybe?"
    liu "N-no, I can."
    liu f_worried_down @ f_surprised "I will!"
    anon f_worried "You're sure?"
    liu f_worried "Definitely!"
    liu a_nervous "Just, umm..."
    show liu a_swimsuit_show with dissolve
    show anon f_worried_low
    liu "... Give me a moment to put this stupid bikini away."
    show liu f_nervous
    anon f_normal "Of course."
    liu a_behind "You'll find the stairs to the vault at the end of that hallway there."
    liu "I'll meet you in a moment."
    anon "Thank you, {b}Liu{/b}."
    liu "My pleasure, {b}[firstname]{/b}."
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
