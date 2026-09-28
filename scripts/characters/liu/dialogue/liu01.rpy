label liu01_init_liu:
    show anon f_shy with dissolve
    liu "Hello there and welcome to {b}Saga Financial{/b}."
    liu "My name is {b}Liu Kim{/b}."
    liu "How can I help you today?"
    anon "Hi."
    if M_anon.finished_state(S_ano13_tina):
        anon "I'm looking for {b}Tina{/b}."
        liu @ f_worried "Oh, I'm sorry, she's not here right now."
        anon f_sad_down "Oh..."
        liu "Can I take a message for her?"
        anon f_worried "No, that's OK, I'll come back later."
        liu "Is there anything else I can help you with?"
        anon "Ooh, actually, would I be able to speak with you about a loan my friend recently took out?"
    else:
        anon f_worried "Umm, I was hoping I could speak with you about a loan my friend recently took out."
    liu "Okay, sure."
    liu "What's your friend's name?"
    anon "{b}[deb_name] Cummings{/b}."
    liu f_surprised @ a_mouth_cover "{i}*Gasp*{/i}"
    liu "A-are you {b}Frank{/b}'s son?"
    anon f_sad_down @ -m_talk "Mmhmm."
    liu f_worried_down "Oh, I umm-"
    liu f_nervous "{i}*Ahem*{/i} I'm real sorry about your dad..."
    liu "It's just awful, what happened."
    anon "Thanks for saying that."
    anon f_worried "Were you two friends?"
    liu @ f_curious "Friends?!"
    liu "N-no, I just-"
    show anon f_skeptical
    liu "Err, I mean, yes..."
    liu "We were friends."
    anon f_normal "Oh, good."
    anon "Maybe you can help me then?"
    liu @ f_nervous_laugh "Heh, umm... Sure."
    liu "I'd love to."
    liu f_normal_down a_typing "Let me just pull it up here and see what we're dealing with..."
    anon "Thanks."
    pause
    show liu f_surprised
    pause
    liu f_worried_down "Oh, okay..."
    liu f_curious "It looks like she took out a loan of two hundred and fifty thousand at an interest rate of three percent?"
    anon @ -m_talk "..."
    liu "Which is strange because we don't usually lend that much..."
    anon "Yeah, she put our house up as collateral."
    liu f_nervous "Oh, umm..."
    pause
    liu f_normal_down "Well, that explains it."
    pause
    liu f_curious "So, what's the problem then?"
    anon f_worried "Well, you see, we're kinda having a family crisis at the moment."
    show liu f_nervous
    anon @ f_sad_down "Umm."
    anon "{i}*Sigh*{/i} I'm not really sure how to put this..."
    pause
    anon "I think my dad might have stolen a bunch of money from some very scary Russian criminals."
    show liu f_nervous_lipbite
    pause
    anon "And my friend took this loan out to buy us some time, you see?"
    pause
    anon "Which, didn't really work... Like, at all."
    anon f_sad_down "In fact, their threats are becoming even more aggressive."
    pause
    anon "And to top it all off, I'm afraid we're not going to be able to make a payment anytime soon."
    pause
    anon f_worried "So, I was hoping there might be something you can do?"
    liu f_ashamed_down "..."
    anon "I know that all sounds crazy but it's-"
    liu "I knew {b}Frank{/b} was going to do something stupid..."
    pause
    anon f_surprised_teeth "!!!" with hpunch
    anon f_skeptical "W-wait a minute."
    anon "Do you know something about all of this?"
    liu f_nervous @ -m_talk "Hmm?"
    liu "N-no, I-"
    liu "I don't know anything."
    anon "But you just said-"
    liu @ f_surprised a_holdup "Look!"
    liu f_curious a_idle "Umm, I'm sorry... I didn't catch your name?"
    anon "{b}[firstname]{/b}."
    liu f_nervous "Right."
    liu "I'm sorry, {b}[firstname]{/b}."
    liu "It sounds like you and your friend are going through a really rough time right now, and I sympathize, I do."
    liu "However, I'm not really sure how much help I can be with all this..."
    pause
    liu "I mean, I can take away the interest rate and push back your initial payment for a few months, but that's really the extent of what I can do."
    anon @ -m_talk "..."
    liu "Is that helpful?"
    anon f_worried "Yeah, I guess it's better than nothing."
    liu "Okay, great!"
    show liu f_normal_down a_typing with dissolve
    pause
    anon f_thinking @ -m_talk "( She definitely knows more about {b}Dad{/b} than she's letting on. )"
    pause
    anon @ -m_talk "( I wonder why she won't tell me? )"
    liu f_nervous "Is there anything else I can do for you, {b}[firstname]{/b}?"
    anon f_worried "Uhh, no... I don't think so."
    liu "Alright, well thank you for banking with-"
    anon @ f_surprised "Wait!"
    anon "I almost forgot; I wanted to open up an account of my own while I'm here."
    liu f_curious "Oh, you don't have an account?"
    anon "Nope."
    liu f_normal "Well then, you're right!"
    liu "You should definitely start one."
    liu "It's the safest thing you can do with your money and you'll be earning interest on whatever you deposit."
    pause
    liu f_normal_down "Just give me one minute here to set it all up for you."
    anon "Thanks, {b}Liu{/b}."
    liu "Not a problem."
    pause
    anon a_thinking f_thinking @ -m_talk "( There has to be something I can do to get her to open up to me... )"
    pause
    anon f_grin @ -m_talk "( Maybe I just need to find the right moment? )"
    liu f_normal "Alright, {b}[firstname]{/b}."
    show anon f_normal a_idle with dissolve
    liu a_card "Here's the account information along with an ATM card."
    show anon a_card_atm
    show liu a_idle
    with dissolve
    liu "Which should work at any of our branches."
    anon a_idle "Alright."
    liu "Is there anything else I can do for you today?"
    anon "No, I think that will be it."
    liu "Alright, well thank you for banking with us here at {b}Saga Financial{/b}."
    liu @ f_laugh "Have a wonderful day!"
    anon "Yeah, you too."
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
