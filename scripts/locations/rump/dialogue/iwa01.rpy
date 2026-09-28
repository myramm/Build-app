label iwa01_exit_rump_front:
    scene expression background(960, 448, 6.) as stage at flip with None
    show iwanka b_maid o_glasses
    show anon f_worried:
        xoffset 300
    with dissolve
    anon "Alright, just play it cool and let me do the talking..."
    show anon f_worried
    iwanka @ -m_talk "Mhmm."
    pause
    show bodyguard with dissolve:
        flip
    bodyguard "Heading home for the night?"
    show anon f_surprised a_sides with dissolve:
        flip
        xoffset -200
    anon f_surprised @ -m_talk "Hmm?"
    anon @ a_point_self "Pool boy!"
    bodyguard "Excuse me?"
    anon f_worried "I umm... I work for {b}Mrs. Rump{/b}..."
    anon "... As the pool boy."
    bodyguard f_suspicious "Uh huh."
    anon @ a_point_self "I'm allowed to be here."
    anon a_badge "See."
    bodyguard @ -m_talk "..."
    anon f_shy "Heh, Yup... Nothing unusual going on here!"
    show iwanka f_eyeroll
    pause
    iwanka f_concerned "Smooth."
    anon @ f_worried_left "Shut up!"
    bodyguard f_normal "I don't think I've seen this one before. What is your name?"
    anon a_sides "Oh, really?"
    anon f_thinking "Umm, that's... Because..."
    anon f_shy a_idle "... She's new!"
    bodyguard "Oh?"
    bodyguard f_smirk "What's your name, gorgeous?"
    iwanka f_smirk @ -m_talk "..."
    anon @ f_worried_left "Ehh, I'm afraid she doesn't speak any English."
    bodyguard f_normal "Oh?"
    bodyguard "Well, that's not that uncommon around here..."
    bodyguard f_smirk @ a_point_self "My name is Joe." (show_native="Mi nombre es Joe.")
    bodyguard "What is your name?" (show_native="¿Cuál es tu nombre?")
    show anon f_surprised_teeth behind iwanka with dissolve:
        unflip
        xoffset 300
    anon "!!!"
    pause
    iwanka f_suspicious @ f_thinking "Ehh?"
    iwanka "Quesadilla?"
    show iwanka f_smirk
    bodyguard f_surprised "Quesadilla?!"
    anon f_hurt a_facepalm @ -m_talk "!!!"
    bodyguard f_smirk "Now that's a pretty name!"
    show iwanka behind anon
    show anon a_sides f_shy:
        flip
        xoffset -200
    with dissolve
    anon "Isn't it?"
    bodyguard a_defensive "Heh, I gotta admit that's about the extent of my Spanish."
    anon "Oh?"
    bodyguard a_idle "I keep meaning to learn more but who has the time, you know?"
    anon "I hear ya, man."
    bodyguard "Tsk, the maids around here just keep getting prettier and prettier!"
    anon @ -m_talk "Mhmm."
    bodyguard "Where does {b}Rump{/b} find these girls anyway?"
    anon @ a_frustrated "Y-yeah, it's a real mystery..."
    pause
    anon f_worried "Sorry, I don't mean to rush you but ehh, we really should be going now."
    bodyguard "You got somewhere important to be, do you?"
    anon "Yeah, umm..."
    anon "... Well, Quesadilla and I are supposed to meet some friends, for some... Uhh..."
    show anon f_thinking
    pause
    anon f_shy "... Salsa dancing!"
    bodyguard "Oh, I've always wanted to try that!"
    anon "Yeah, you totally should."
    anon "It's a real hoot!"
    bodyguard "Alright, well everything checks out."
    bodyguard "You two have a nice night, eh?"
    anon "Thanks!"
    anon f_worried "You too."
    bodyguard @ a_wave "I hope I get to see you again real soon, beautiful."
    show anon f_worried_left
    iwanka @ f_eyeroll "Ehh."
    iwanka @ a_wave "Taco."
    anon f_hurt "!!!"
    bodyguard f_suspicious "Huh?"
    anon f_shy "Heh, she's joking!"
    bodyguard "I don't get it..."
    anon a_wave "Good night, sir!"
    hide iwanka
    hide anon
    show bodyguard:
        xoffset -600
        unflip
    with dissolve
    pause
    bodyguard "Hmm, what an odd girl..."

    scene expression player.location.background_blur
    show anon f_unimpressed
    show iwanka b_maid o_glasses
    with fade
    anon "Taco?!"
    iwanka f_laugh "Hahaha!"
    anon "Are you kidding me?!"
    iwanka "{i}*Snort*{/i} Hahaaah!"
    anon f_normal "That guy seriously believed your name was Quesadilla..."
    iwanka f_smirk "Just be thankful he didn't ask me anything else!"
    iwanka "The only other Spanish words I know are burrito and cinnamon twist!"
    anon f_worried "What?!"
    anon "That's not even-"
    iwanka f_laugh "Hahahaah!!"
    anon f_tired "{i}*Sigh*{/i} At least we're out of the estate..."
    pause
    show iwanka f_smirk
    anon f_normal "... Where to now?"
    iwanka "Now we need to find a boat."
    anon f_skeptical "A boat?"
    iwanka "Yeah, you know a place where we can rent one?"
    anon f_thinking "Hmm, maybe..."
    anon f_skeptical "Where exactly are we going, {b}Iwanka{/b}?"
    iwanka "It's a secret!"
    anon f_unimpressed @ -m_talk "..."
    iwanka "Trust me, this is going to be awesome!"
    anon @ -m_talk "Hmm."
    anon f_worried "Well, I suppose we should {b}head to the pier and see about renting a boat{/b}."
    iwanka "Works for me."
    iwanka "Lead the way!"
    pause
    hide anon with dissolve
    iwanka @ f_laugh a_dust "This is so exciting!"
    hide iwanka with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
