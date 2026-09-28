label hospital_laboratory_dialogue:
    if M_priya.is_state(S_priya_look_in_lab):
        call expression game.dialog_select("hospital_lab_priya_look_in_lab")

    $ game.main()


label hospital_laboratory_take_pills_dialogue:
    scene expression player.location.background_blur
    show player 706 at left with dissolve
    player_name "( Hmm, so it comes in pill form? )"
    player_name "( Weird. )"
    player_name "( I was expecting some kind of cream... )"
    player_name "( ... Or maybe something in a syringe. )"
    player_name "( This is much simpler! )"
    priya "Who the hell are you?!"
    show player 23
    player_name "!!!" with hpunch
    show priya f_angry a_crossed with dissolve
    player_name "I uhh..."
    show player 22
    priya "How did you get in-"
    show priya a_point with dissolve
    priya "{i}*Gasp*{/i} Are you stealing my drugs!"
    show priya a_crossed with dissolve
    show player 23
    player_name "N-no, I wasn't-"
    show player 22
    show priya a_point with dissolve
    priya "I'm calling security!"
    show priya a_idle:
        flip
        xoffset 650
    show player 40 with dissolve
    player_name "W-wait, please!"
    pause
    show priya f_angry a_crossed:
        unflip
        xoffset 0
    with dissolve
    show player 10 with dissolve
    player_name "I wasn't going to steal them, I was just looking!"
    show player 5
    priya "Yeah, right!"
    show player 10
    player_name "I'm serious!"
    player_name "Look, here."
    show player 239_240 with dissolve
    pause
    show player 705f with dissolve
    player_name "See, no harm done."
    show player 704f
    show priya a_point with dissolve
    priya "This is a restricted area!"
    priya "How did you even get down here?!"
    show priya a_crossed with dissolve
    show player 24 with dissolve
    player_name "{i}*Sigh*{/i} It's a long story. Please don't make me think about it again."
    show player 10
    player_name "Maybe you can help me?"
    player_name "I'm looking for a guy named {b}Doctor Singh{/b}?"
    show player 5
    pause
    priya @ f_eyeroll "Well, you found \"him\"."
    show player 12
    player_name "Huh?"
    show player 10
    player_name "... You mean-"
    show player 37 with dissolve
    priya "I'm {b}Doctor Singh{/b}."
    show player 30
    player_name "B-but you're a woman... Right?"
    show player 5
    priya "No shit, Sherlock."
    show player 10
    player_name "Sorry, I didn't-"
    show player 401
    player_name "I was under the impression you were a man."
    show player 403
    priya @ -m_talk "..."
    priya "Would you hurry up and tell me what this is all about?!"
    show player 10
    player_name "R-right, sorry!"
    show player 4 with dissolve
    player_name "Umm."
    show player 10 with dissolve
    player_name "I heard something about this {b}Pregnax{/b} drug you're developing..."
    show player 5
    priya "Oh, and who exactly did you hear it from?!"
    show player 10
    player_name "I... I promised I wouldn't say..."
    show player 18
    priya "It was that airheaded nurse on the second floor, wasn't it?!"
    priya "That woman can't keep her mouth closed for two seconds."
    show player 11
    player_name "..."
    priya @ f_eyeroll "Go on."
    show player 10
    player_name "You see, my fri-"
    player_name "{i}*Ahem*{/i} M-my girlfriend is trying to get pregnant and her odds aren't very good."
    player_name "I want to do everything I can to help increase her odds."
    show player 5
    priya "So, that's why you broke into my lab?"
    show player 29 with dissolve
    player_name "Y-yeah."
    show player 26 with dissolve
    player_name "Which again, was not to steal anything!"
    show player 38 with dissolve
    player_name "I just wanted to speak with you about the {b}Pregnax{/b} drug trial."
    show player 5 with dissolve
    priya "The trial is at capacity."
    show player 24
    player_name "Y-yeah, I heard about that too."
    pause
    player_name "Is there nothing you can do?"
    show priya f_facepalm a_facepalm with dissolve
    priya @ -m_talk "..."
    priya "Well, I'll admit. I'm impressed with your determination."
    priya "It couldn't have been easy getting down here."
    show priya a_idle f_normal with dissolve
    priya "... And I'm not unsympathetic to your girlfriend's plight."
    show player 11
    pause
    priya "What's your name?"
    show player 10
    player_name "{b}[firstname]{/b}."
    show player 5
    priya "How old are you, {b}[firstname]{/b}?"
    show player 10
    player_name "I'm eighteen."
    show player 5
    priya "That's very young."
    priya "Our other test subjects are all ten to thirty years older than you."
    show player 30
    player_name "Is that a good or bad thing?"
    show player 5
    show priya f_thinking a_thinking with dissolve
    pause
    show priya f_suspicious
    priya "It's... Intriguing."
    show priya f_normal
    priya "... And your girlfriend, how old is she?"
    show player 35
    player_name "Uhh, I'm not sure exactly..."
    show player 34
    priya @ f_suspicious "You're trying for a baby with this woman and you don't even know her age?"
    show player 35
    player_name "N-no, I uhh..."
    player_name "I mean, she's in her late thirties, I think."
    show player 34
    priya "Oh, now that is interesting..."
    priya "Is she your only sexual partner?"
    show player 17
    player_name "... No."
    show player 18
    show priya f_eyeroll a_crossed with dissolve
    priya "Tsk."
    show priya f_thinking a_thinking with dissolve
    pause
    show priya f_normal a_crossed with dissolve
    priya "Would you be willing to subject yourself to a few tests?"
    show player 10
    player_name "Uhh, sure."
    show player 5
    priya "This would all be strictly off the books, mind you."
    show player 10
    player_name "I'm fine with that."
    show player 5
    priya "I am not a charitable person by nature, {b}[firstname]{/b}."
    show priya a_point with dissolve
    priya "However, your unique circumstances would certainly prove useful to my research."
    show priya f_thinking a_thinking with dissolve
    priya @ -m_talk "..."
    show priya f_normal a_point with dissolve
    priya "I'll give you one bottle, for now."
    priya "Perhaps more, in the future."
    show priya a_crossed with dissolve
    show player 14
    player_name "That would be wonderful!"
    show player 13
    priya "... But only if you agree to return here for testing."
    show player 14
    player_name "Not a problem!"
    show player 13
    show priya a_point with dissolve
    priya "... And I want a full accounting of each and every time you use the pill."
    priya "Every detail."
    show priya a_crossed with dissolve
    show player 10
    player_name "Every detail?"
    show player 5
    priya "If at any point I'm unsatisfied with your quality of information or test results, the deal ends."
    show player 14
    player_name "O-okay."
    show player 13
    priya "There is something else you must understand, {b}[firstname]{/b}."
    priya "We're still very early in testing with {b}Pregnax{/b}."
    priya "{b}You must be cautious about using it{/b}."
    priya "{b}There may very well be side effects{/b} we aren't aware of yet."
    priya "Although, in theory, it should be relatively safe."
    show player 37 with dissolve
    player_name "{i}*Gulp*{/i} I-I understand."
    pause
    show player 13 with dissolve
    priya @ -m_talk "Hmmph."
    priya "Return to me if you run out of pills."
    priya "I'll be in touch with you about those... Tests."
    show player 14
    player_name "I will and look forward to hearing from you."
    player_name "Thank you, {b}Doctor Singh{/b}!"
    show player 13
    priya "It's {b}Priya{/b}."
    show player 30
    player_name "Hmm?"
    show player 5
    priya "My name is {b}Priya{/b}."
    priya "{b}Priya Singh{/b}."
    show player 30
    player_name "{b}Priya{/b}."
    show player 33
    player_name "That's a very pretty name!"
    show player 18
    priya @ f_eyeroll "Yes, yes..."
    priya "Go on, Casanova."
    show priya a_point with dissolve
    priya "Get out of my lab."
    hide player with dissolve
    pause
    show priya f_facepalm a_facepalm
    priya "Grr, what are you thinking {b}Priya{/b}?!"
    priya "You've completely lost your mind!"
    pause
    show priya f_normal a_idle with dissolve
    priya "..."
    show priya f_facepalm
    priya "Oh, please, let him bring me good news..."
    hide priya with dissolve

    $ player.go_to(L_hospital_basement)
    scene expression player.location.background_blur
    show player 705 with dissolve
    player_name "( Hmm, the directions say I need to {b}take one pill, orally, prior to engaging in sexual activity{/b}. )"
    player_name "( {b}Effects will last for 24 hours{/b}. )"
    player_name "( There's also a warning label: \"Do not use this medication if your partner is currently menstruating or has undergone menopause.\" )"
    hide player with dissolve
    call popup ('give', 'pregnax_pills')
    $ player.get_item('pregnax_pills')
    call popup ('give', 'cumdoom_pills')
    $ player.get_item('cumdoom_pills')
    $ M_priya.trigger(T_priya_start_testing)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
