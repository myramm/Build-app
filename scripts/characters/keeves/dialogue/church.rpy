label keeves_button_church:
    show anon with dissolve:
        xoffset -50
    anon "Hey there, {b}Father Keeves{/b}."
    keeves "Heeey, how's it going, little dude?!"
    keeves "Can I help you with something?"

    menu keeves_button_church.choice:
        "{b}Consuela{/b}." if M_consuela.is_state(S_con02_init):
            jump con02_init_keeves
        "You look really familiar.":

            jump keeves_button_church.glitch
        "How are you?":

            jump keeves_button_church.excellent
        "Never mind.":

            pass

    anon f_normal @ a_wave "See ya around, {b}Father Keeves{/b}."
    keeves @ a_point "Heh, excellent."
    keeves @ f_laugh a_rock "Later, little dude!"
    hide anon with dissolve
    return


label keeves_button_church.glitch:
    show anon f_thinking a_thinking with dissolve
    pause
    anon a_idle f_skeptical "You look really familiar."
    keeves f_happy @ f_brag "Ah, yeah?"
    keeves "I get that a lot."
    keeves @ a_point "You know, because my brother is famous and all."
    anon f_surprised "Really?"
    anon f_laugh @ a_point "Is your brother an actor or something?"
    keeves "Nah, he's a city councilman."
    anon f_unimpressed @ -m_talk "..."
    keeves "In North Dakota."
    anon f_skeptical "You know, I don't think that's it..."
    keeves @ -m_talk "Hmm?"
    keeves @ a_raise "I guess it's a mystery then, little dude."
    jump keeves_button_church.choice


label keeves_button_church.excellent:
    anon f_normal "How are you?"
    keeves f_confused "Ugh, {b}Sister Angelica{/b} has been really harshing my chill lately..."
    keeves "I dunno why she's always so edged but it's totally bogus!"
    anon "Oh?"
    keeves @ a_raise "Yeah, I keep telling her not to tax my gig, but she's being a complete cruster."
    anon "Cruster?"
    show keeves f_normal a_raise with dissolve
    pause
    show keeves a_idle with dissolve
    anon "You're a really weird guy {b}Father Keeves{/b}, you know that?"
    keeves @ f_confused "I am?"
    anon "Yeah, but it's cool."
    anon @ f_laugh "You're also pretty awesome!"
    keeves @ f_laugh a_rock "Heh, excellent!"
    jump keeves_button_church.choice


label kee01_keeves_meet:
    show anon with dissolve
    anon "Umm, hi."
    keeves f_happy "Heeey, how's it going, little dude?!"
    keeves @ a_point "First time here?"
    anon "Y-yeah."
    keeves @ f_laugh a_rock "Excellent!"
    pause
    keeves @ a_raise "Be welcomed in the House of the Lord and whatnot."
    keeves "I'm {b}Father Keeves{/b}."
    keeves "And this bodacious babe next to me with the massive chesticles is {b}Sister Angelica{/b}."
    show angelica f_surprised with easeinright:
        xoffset 100
    show anon f_surprised
    with {'master': hpunch}
    angelica "FATHER!!!"
    show keeves f_confused with {'master': dissolve}:
        flip
        xoffset 300
    angelica "You can't say things like that!"
    show anon f_worried
    show angelica f_normal
    keeves "Huh?"
    angelica "It's improper."
    keeves "Oh, sorry {b}Sister{/b}... That's my bad."
    show keeves f_normal with dissolve:
        unflip
        xoffset -100
    keeves "She's not a bodacious babe..."
    keeves "... She's a very pious young woman."
    pause
    keeves f_happy @ a_raise "With tremendous bazongas!"
    show angelica f_normal_close a_facepalm with dissolve
    angelica "{i}*Sigh*{/i} Lord, give me strength."
    anon @ -m_talk "..."
    show angelica f_normal a_idle with dissolve
    keeves "So, did you enjoy the sermon?"
    anon @ -m_talk "Hmm?"
    anon f_normal "Oh, umm... Yeah."
    anon @ f_skeptical "It was very unique."
    keeves "Excellent, yeah... That's what I was going for."
    keeves "You see, I like to promote a chill environment for the congregation."
    keeves "It really brings people closer together."
    anon "Oh, really?"
    keeves "Yeah, or at least, that's what Jesus told me once."
    anon f_skeptical "You've spoken with Jesus?"
    anon "Like, THE Jesus?"
    keeves "Oh, totally!"
    keeves "I met him backstage at a Wyld Stallyns concert back in '91."
    anon f_surprised "You met Jesus Christ backstage at a rock concert?"
    keeves "No, dude, Jesus Jimenez..."
    show anon f_unimpressed
    keeves "He was all like, \"You guys took my breath away tonight!\""
    keeves "And I said, \"No, YOU'RE breathtaking, Jesus!\""
    keeves "\"YOU'RE breathtaking!\""
    keeves "And he said, \"Party on, Ted!\""
    keeves "Heh."
    keeves "Then we lit up some doobage and had meatball subs."
    keeves "It was a most triumphant time!"
    anon f_skeptical "So wait, you were in a band?"
    keeves @ f_laugh a_rock "Ahh yeah, totally!"
    keeves "My best friend Bill and I, plus a couple babes from the 1400s."
    anon f_unimpressed "The 1400s?"
    keeves "That was before the big bus incident..."
    anon f_surprised "Bus incident?"
    keeves "Yeah, some wack job put a bomb on a city bus..."
    keeves @ a_point "... It was NOT excellent."
    pause
    keeves "After that I moved to New York for a while and the Devil stole my wife..."
    anon f_unimpressed @ -m_talk "..."
    keeves "... Then I saved the world from robots..."
    keeves "... Spent a year playing quarterback with the Washington Sentinels..."
    anon "What the f-"
    keeves "... Lived at a lake house with a magical mailbox..."
    keeves "... Became a world-famous assassin..."
    anon f_worried "Is he being serious right now?"
    angelica "I have no idea."
    angelica f_stern "{b}Father{/b}, are you feeling alright?"
    show keeves f_confused with dissolve:
        flip
        xoffset 300
    keeves @ -m_talk "Hmm?"
    keeves "Oh, man... now that you mention it, I am kinda hungry."
    keeves f_happy "Do we have any of those righteous pudding cups left?"
    angelica "N-no, I'm afraid you ate them all last night."
    keeves "Ahh, bogus!"
    hide keeves with {'master': dissolve}
    keeves "What's the number for that pizza place again?"
    show angelica f_surprised with dissolve:
        flip
        xoffset 700
    angelica "Wait a second!"
    angelica -f_surprised "You have to tend to the confessions!"
    keeves "Take a chill pill, {b}Sister{/b}."
    keeves "I need Canadian bacon and sausage inside me, ASAP!"
    hide angelica with {'master': dissolve}
    angelica "{b}Father{/b}!"
    pause
    anon f_worried @ -m_talk "( Okay, that guy is either mental or the coolest priest on the planet! )"
    anon f_laugh @ -m_talk "( Either way, I'm intrigued. )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
