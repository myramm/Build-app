label ano20_cops_harold:
    show expression background(760, 386, 4.) as stage
    show harold f_surprised
    show anon with dissolve:
        xoffset -100
    harold "{b}[firstname]{/b}?"
    harold f_concerned "What are you doing here so late?"
    anon "I have something for you."
    harold f_suspicious "For me?"
    show anon f_looking_down a_backpack with dissolve
    pause
    show anon a_recorder_give_cashless f_normal with dissolve
    harold f_surprised @ -m_talk "!!!"
    anon "This is evidence that proves {b}Mayor Rump{/b} is working with the Russians."
    show harold a_recorder_cashless
    show anon a_idle
    with dissolve
    harold "What the-"
    harold "Where did you get this?"
    anon "I found it in {b}Mayor Rump{/b}'s office."
    harold f_suspicious "Huh?!"
    harold "How in the heck did you get into the mayor's personal office?"
    anon "Does that really matter?"
    harold f_angry "Of course it matters!"
    show anon f_worried
    harold "If {b}Rump{/b} is in bed with the Russians like we suspect, then you should be staying well clear of him."
    harold "You're going to get yourself killed, {b}[firstname]{/b}!"
    anon f_angry "Would you just look at the evidence, please?!"
    harold @ -m_talk "..."
    harold f_surprised_down "What is this stuff anyways?"
    anon f_worried @ a_point "That folder there is full of bank statements for about a dozen offshore accounts."
    anon "Based on the amounts, I'd say it's a good bet that's where he's keeping his cut of the profits."
    harold f_suspicious "What profits?"
    anon "You know, his cut of whatever the Russians are peddling."
    harold @ -m_talk "Hmm."
    anon "There's also bunch of deeds for property here in Summerville."
    anon "Including that warehouse you were scoping out the other night."
    harold f_surprised "Wait a second, {b}Rump{/b} owns that place?!"
    anon @ -m_talk "Mhmm."
    harold f_concerned "I told {b}Earl{/b} that company name sounded fake..."
    harold a_recorder_listen_cashless f_suspicious "... What about this?"
    anon "It's a recording of {b}Rump{/b} and the Russians talking shop."
    anon "On it, you'll hear the mob boss confess to killing two women and {b}Rump{/b} laughing about it."
    harold f_concerned "You're serious?"
    anon f_angry "Then they discuss killing my father."
    harold @ f_surprised "!!!"
    harold "That's-"
    pause
    harold "Jesus, kid..."
    harold "Did you find anything else?"
    show anon f_worried

    $ renpy.dynamic(rv=None)
    menu:
        "Tell him about the money. {color=7ff7}[[Honest]{/color}":
            anon "I found this too."
            show anon a_recorder_give_cash with dissolve
            pause
            show harold a_recorder f_surprised_down
            show anon a_idle
            with dissolve
            harold "Whoa, that's a lot of cash."
            show harold f_concerned
            anon "Yeah."
            anon "Some of his ill-gotten gains no doubt."
        "Nope, that's everything. {color=f77b}[[Dishonest]{/color}":

            $ rv = True
            anon f_thinking a_thinking @ -m_talk "( Hmm. )"
            anon @ -m_talk "( There's no reason I shouldn't keep this money, right? )"
            anon @ -m_talk "( I mean, it's not going to do anybody any good sitting in some evidence room... )"
            anon f_shy a_behind_head "Ehh, nope."
            anon "That's everything I found."

    anon a_idle "There's enough there to make an arrest, don't you think?"
    harold "If it all checks out, then yes."
    harold "Wait here a minute while I take this to my boss, okay?"
    anon "Yeah, okay."
    hide harold
    show anon:
        flip
        xoffset -600
    with dissolve
    harold "Hey {b}Yumi{/b}, can you watch the kid for a minute?"
    yumi "Sure thing, boss."
    show yumi f_concerned with dissolve:
        xoffset -50
    pause
    show anon with dissolve:
        unflip
        xoffset -100
    yumi "Jeez, you look like you're having a rough night..."
    pause
    yumi "What are you doing here anyways?"
    anon @ f_sad_down "{i}*Sigh*{/i} It's a long story."
    pause
    yumi "Something to do with your father's case?"
    anon "Yeah."
    yumi f_suspicious "You weren't snooping on those Russians again, were you?"
    anon "No."
    yumi f_concerned "You'd better not be!"

    if False:
        yumi f_normal @ f_wink "I'll handcuff you to my bed and keep you hostage until this whole thing blows over..."
        show anon f_surprised
        yumi "Don't you think I won't!"
        anon "That-"
        pause
        anon f_normal @ f_laugh "Doesn't sound so bad actually."
        yumi @ f_laugh "Heh, shut up!"
    else:

        yumi "Those guys will kill you, {b}[firstname]{/b}!"
        yumi "I don't think I could face your landlady if that happened..."
        anon "Well, you can relax."
        anon "I haven't gone anywhere near them since you guys caught me at the warehouse."

    yumi f_normal "We are making progress, you know?"
    anon f_normal @ f_surprised "Oh?"
    yumi "{b}Harold{/b} was able to ID the mob boss."
    anon @ -m_talk "..."
    yumi "{b}Raznikov Putin Chernyshevsky{/b}."
    yumi @ f_eyeroll "But he goes by {b}Raz{/b} for short."
    anon f_surprised "Wait a second..."
    anon "Let me guess."
    anon f_worried "Short guy?"
    anon "Kinda looks like a pale goblin?"
    yumi f_suspicious "How did you know that?"
    anon "Lucky guess."
    yumi f_concerned "There's something you're not telling me!"
    anon f_surprised a_sides "No."
    pause
    yumi "Yes, there is!"
    yumi "C'mon, spill it."
    anon f_worried @ -m_talk "..."

    if False:
        yumi f_concerned "That's it, I'm getting the handcuffs!"
        anon @ f_laugh "Heh, alright... Just-"
    else:

        yumi "Do I need to take you down to interrogation?!"
        anon @ f_confused "Huh?"
        yumi "I don't like being kept-"

    harold "{b}Yumi{/b}, I need you to go grab our gear and get it in the car."
    show anon with dissolve:
        flip
        xoffset -600
    yumi @ -m_talk "Hmm?"
    show anon:
        unflip
        xoffset -100
    show harold behind anon:
        flip
        xoffset 175
    with dissolve
    yumi f_suspicious "What's going on, boss?"
    harold "The chief just authorized me to bring {b}Rump{/b} in on charges."
    yumi f_surprised "Are you serious?"
    harold "Yes, hurry up."
    yumi "Y-yes, sir!"
    hide yumi with dissolve
    pause
    show harold with dissolve:
        unflip
        xoffset -200
    harold f_concerned "Can you get yourself home alright?"
    anon f_worried a_idle "Well, hold on a second... can't I come with you?"
    harold f_concerned "No, you can't come with us!"
    anon "Why not?!"
    harold "This is police business, {b}[firstname]{/b}..."
    harold "We can't just let civilians tag along for their own personal enjoyment."
    anon f_angry "Hey, if it wasn't for my evidence you wouldn't-"
    harold "I'm not going to argue with you about this."
    anon "What about the Russians?!"
    anon "You're gonna arrest them too, right?!"
    harold "I don't know, okay?"
    harold "We can discuss it tomorrow."
    harold "For now, can you just get your butt home and let us do our job?!"
    anon "Yeah, fine... Whatever."
    harold "Thank you!"
    hide harold with dissolve
    pause
    anon f_disgusted @ -m_talk "( Well, at least they're finally doing something... )"
    anon @ -m_talk "( I guess there's nothing for me to do but go home and wait. )"
    hide anon with dissolve
    return rv
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
