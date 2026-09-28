label con01_init_ricky:
    anon f_worried "Do they always treat {b}Consuela{/b} so poorly?"
    pause
    ricky f_confused "You seem surprised?"
    anon "I am."
    anon "I mean, the mayor always seems like a pretty generous guy on TV..."
    ricky f_sad "You have a lot to learn about the world, my friend."
    ricky "That's just his public persona."
    ricky "Most politicians act very differently behind closed doors."
    anon "Yeah, I guess..."
    pause
    anon "Can you think of any way I could help her?"
    ricky f_smirk "Heh, can you get her a green card?"
    anon "No."
    ricky "Then I think not."
    pause
    anon f_thinking a_thinking "I could try talking to the mayor."
    ricky f_surprised "Bad idea!"
    ricky f_sad "You'll likely make things worse for her..."
    show anon f_worried
    pause
    ricky f_thinking "Hmm, you could try {b}speaking with the mayor's wife{/b}, I suppose..."
    anon f_surprised "{b}Melonia{/b}?"
    anon f_skeptical "You really think she might help?"
    ricky f_normal "Not out of kindness, she won't..."
    ricky "... But if you can convince her that it's in her best interest to help {b}Consuela{/b}, there's a chance she might do it."
    ricky "Especially if it screws her husband over."
    ricky "She has very little love for him."
    anon f_thinking "Hmm."
    pause
    anon f_normal "Well, it's not like I have a better idea."
    anon "{b}I'll go and talk to the mayor's wife{/b}."

    if game.timer.is_day():
        ricky "{b}Wait for evening{/b}, after her soak in the tub has relaxed her."

    anon a_idle @ a_wave "Thanks, {b}Ricky{/b}."
    ricky f_smirk "Good luck, amigo."
    hide anon with dissolve
    return


label con01_init_ricky.repeat:
    ricky f_confused "Did you {b}speak with the mayor's wife{/b}?"
    anon "Not yet."
    ricky f_sad "Just be careful, yeah?"
    ricky "She's smarter than she lets on."
    anon "I'll be careful."

    if game.timer.is_day():
        hide anon with {'master': dissolve}
        ricky "And remember to {b}wait for evening{/b}, amigo!"
    else:
        hide anon with dissolve
    return


label con01_plan_ricky:
    show ricky f_smirk
    anon f_normal "Good news!"
    anon "I think I found a way to see {b}Consuela{/b} free of this place."
    ricky "Really?"
    ricky "How did you manage that?"
    anon @ f_brag_closed "The mayor's wife says I just need to find a replacement maid."
    ricky @ -m_talk "..."
    ricky @ f_laugh "Hahahahahahaah!"
    anon f_worried @ f_skeptical "Why are you laughing?"
    ricky "Who's going to willingly work for the wages {b}the Rumps{/b} pay and put up with {b}Mister Rump{/b} when he gets handsy?"
    anon "Well, I was hoping you might know somebody?"
    ricky @ f_laugh "Pfft, hahahahaah!"
    anon f_sad_down @ -m_talk "..."
    ricky "Even illegal immigrants have standards."
    ricky "I'm not sure I'd be comfortable suggesting it to them, either."
    anon "{i}*Sigh*{/i} Crap."
    ricky "Trust me, nobody is going to put up with this place if they don't have to."
    anon "There's gotta be someone!"
    ricky "Yeah, right."
    ricky "What you need is a {b}prostitute{/b} or something..."
    anon f_surprised "Prostitute?!"
    ricky "A really desperate prostitute."
    anon f_worried "We don't have anything like that in Summerville!"
    ricky "Hah!"
    ricky "Your naiveté is quite adorable, amigo."
    anon @ -m_talk "..."
    ricky "Anything else I can help you with?"
    anon "No."
    ricky "No prostitutes in Summerville..."
    hide ricky with {'master': dissolve}
    ricky "Hahahahahahaah!"
    anon f_thinking a_thinking @ -m_talk "( Do we really have sex workers in our small town? )"
    pause
    anon f_grin a_idle @ -m_talk "( {b}I guess it wouldn't hurt to look into it{/b}. )"
    hide anon with dissolve

    $ M_consuela.trigger(T_con01_plan)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
